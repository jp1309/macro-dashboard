# -*- coding: utf-8 -*-
"""
Descarga datos WEO del FMI para países de América Latina + G7.
Genera un CSV por variable y un CSV maestro.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CUÁNDO ACTUALIZAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El FMI publica nuevas ediciones del WEO dos veces al año:
  • Abril      → datos actualizados + proyecciones nuevas
  • Octubre    → revisión completa del año en curso

El GitHub Action (.github/workflows/update-data.yml) lo corre a diario
en abril, septiembre y octubre y sube los datos apenas detecta una
edición nueva.

CÓMO ACTUALIZAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Correr:
       python download.py
2. Los CSVs individuales, el maestro y weo_meta.json se sobreescriben.
3. No hay END_YEAR fijo — la API devuelve todos los años disponibles,
   incluyendo nuevas proyecciones que el FMI extienda.
4. Si falla algún indicador, el script termina con error y NO toca el
   maestro ni weo_meta.json (evita publicar datos incompletos).

EDICIÓN Y PROYECCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La API informa la fecha de publicación del dataset (PUBLICATION_DATE).
De ahí se derivan:
  • la edición (abril u octubre de ese año) → weo_meta.json, que usa el
    dashboard para sus etiquetas;
  • PROJECTION_START_YEAR = año de publicación: ese año y los siguientes
    se marcan como proyección.
"""
import sys
import json
import datetime
import requests
import pandas as pd
from lxml import etree
import os
import time

# ── Configuración de años ───────────────────────────────────────────────────
START_YEAR = 1980
# Sin END_YEAR fijo: la API devuelve todos los años disponibles (incluye
# proyecciones que el FMI extienda a futuro, ej. 2031+).
# El año de inicio de proyecciones se toma de la fecha de publicación del WEO
# (ver weo_edition()); no depende del día en que se corra el script.

# ── Países de América Latina (código ISO3 WEO) ─────────────────────────────
LATAM = {
    "ARG": "Argentina",
    "BOL": "Bolivia",
    "BRA": "Brasil",
    "CHL": "Chile",
    "COL": "Colombia",
    "CRI": "Costa Rica",
    "CUB": "Cuba",
    "DOM": "República Dominicana",
    "ECU": "Ecuador",
    "SLV": "El Salvador",
    "GTM": "Guatemala",
    "HTI": "Haití",
    "HND": "Honduras",
    "MEX": "México",
    "NIC": "Nicaragua",
    "PAN": "Panamá",
    "PRY": "Paraguay",
    "PER": "Perú",
    "URY": "Uruguay",
    "VEN": "Venezuela",
    "BLZ": "Belice",
    "GUY": "Guyana",
    "SUR": "Surinam",
    "JAM": "Jamaica",
    "TTO": "Trinidad y Tobago",
}

# ── Países del G7 (referencia de comparación) ───────────────────────────────
G7 = {
    "USA": "Estados Unidos",
    "JPN": "Japón",
    "DEU": "Alemania",
    "GBR": "Reino Unido",
    "FRA": "Francia",
    "ITA": "Italia",
    "CAN": "Canadá",
}

# ── Emergentes (G20 resto) ───────────────────────────────────────────────────
EMERGENTES = {
    "AUS": "Australia",
    "CHN": "China",
    "IND": "India",
    "IDN": "Indonesia",
    "RUS": "Rusia",
    "SAU": "Arabia Saudita",
    "ZAF": "Sudáfrica",
    "KOR": "Corea del Sur",
    "TUR": "Turquía",
    "TWN": "Taiwán",
    "SGP": "Singapur",
    "ARE": "Emiratos Árabes Unidos",
    "PHL": "Filipinas",
    "VNM": "Vietnam",
    "MYS": "Malasia",
    "EGY": "Egipto",
    "NGA": "Nigeria",
}

# Todos los países a descargar
ALL_COUNTRIES = {**LATAM, **G7, **EMERGENTES}

# Grupos para hacer requests separados (evita rate-limit del API)
COUNTRY_GROUPS = [
    list(LATAM.keys()),
    list(G7.keys()),
    list(EMERGENTES.keys()),
]

# ── Variables WEO a descargar ───────────────────────────────────────────────
INDICATORS = {
    # PIB y Crecimiento
    "NGDP_RPCH":   "Crecimiento real del PIB (%)",
    "NGDP":        "PIB nominal (moneda local, miles de millones)",
    "NGDPD":       "PIB nominal (USD, miles de millones)",
    "NGDPPC":      "PIB per cápita (moneda local)",
    "NGDPDPC":     "PIB per cápita (USD)",
    "PPPGDP":      "PIB PPA (miles de millones USD)",
    "PPPPC":       "PIB PPA per cápita (USD)",
    "PPPSH":       "Participación en PIB mundial PPA (%)",
    # Precios y Empleo
    "PCPIPCH":     "Inflación IPC promedio (%)",
    "PCPIEPCH":    "Inflación IPC fin de período (%)",
    "LUR":         "Tasa de desempleo (%)",
    "LE":          "Empleo total (millones)",
    "LP":          "Población (millones)",
    # Finanzas Públicas
    "GGR":         "Ingresos gobierno (moneda local)",
    "GGR_NGDP":    "Ingresos gobierno (% PIB)",
    "GGX":         "Gasto gobierno (moneda local)",
    "GGX_NGDP":    "Gasto gobierno (% PIB)",
    "GGXCNL":      "Balance fiscal neto (moneda local)",
    "GGXCNL_NGDP": "Balance fiscal neto (% PIB)",
    "GGXWDG":      "Deuda pública bruta (moneda local)",
    "GGXWDG_NGDP": "Deuda pública bruta (% PIB)",
    "GGXONLB_NGDP":"Balance fiscal primario (% PIB)",
    # Sector Externo
    "BCA_NGDPD":   "Cuenta corriente (% PIB)",
    "BCA":         "Cuenta corriente (USD)",
    "TX_RPCH":     "Crecimiento exportaciones (%)",
    "TM_RPCH":     "Crecimiento importaciones (%)",
    "TXG_RPCH":    "Crecimiento exportaciones bienes (%)",
    "TMG_RPCH":    "Crecimiento importaciones bienes (%)",
    # Ahorro e Inversión
    "NID_NGDP":    "Inversión total (% PIB)",
    "NGSD_NGDP":   "Ahorro nacional bruto (% PIB)",
}

BASE_URL     = "https://api.imf.org/external/sdmx/2.1/data/IMF.RES,WEO,+/"
OUTPUT_DIR   = os.path.dirname(os.path.abspath(__file__))
META_PATH    = os.path.join(OUTPUT_DIR, "weo_meta.json")

# Fechas de publicación vistas en las respuestas de la API
PUBLICATION_DATES = set()

MAX_RETRIES  = 4
BASE_DELAY   = 3     # delay base entre requests (segundos)
RETRY_DELAY  = 10    # delay base para reintentos (segundos)


def _fetch_group(indicator: str, country_codes: list) -> list:
    """Descarga un indicador para un grupo de países, con reintentos exponenciales."""
    countries_key = "+".join(country_codes)
    url = (
        f"{BASE_URL}{countries_key}.{indicator}.A"
        f"?startPeriod={START_YEAR}"
    )
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, timeout=90)
            r.raise_for_status()
            break
        except requests.exceptions.RequestException as e:
            if attempt == MAX_RETRIES:
                raise
            wait = RETRY_DELAY * (2 ** (attempt - 1))  # 10, 20, 40s
            sys.stdout.write(f"\n    reintento {attempt}/{MAX_RETRIES} en {wait}s... ")
            sys.stdout.flush()
            time.sleep(wait)

    root = etree.fromstring(r.content)
    rows = []

    for dataset in root.iter("{*}DataSet"):
        pub = dataset.get("PUBLICATION_DATE")
        if pub:
            PUBLICATION_DATES.add(pub[:10])

    for series in root.iter("Series"):
        country = series.get("COUNTRY")
        if country not in ALL_COUNTRIES:
            continue
        for obs in series.findall("Obs"):
            try:
                year = int(obs.get("TIME_PERIOD"))
                rows.append({
                    "country_code":  country,
                    "country_name":  ALL_COUNTRIES[country],
                    "year":          year,
                    "value":         float(obs.get("OBS_VALUE")),
                })
            except (ValueError, TypeError):
                pass

    return rows


def fetch_indicator(indicator: str) -> pd.DataFrame:
    """Descarga un indicador para todos los países, por grupos separados."""
    all_rows = []

    for group in COUNTRY_GROUPS:
        all_rows.extend(_fetch_group(indicator, group))
        time.sleep(BASE_DELAY)

    return pd.DataFrame(all_rows)


def weo_edition(publication_date: str) -> dict:
    """Deriva la edición del WEO a partir de la fecha de publicación (YYYY-MM-DD).

    El WEO sale en abril y en septiembre/octubre: lo publicado en el primer
    semestre es la edición de abril; lo del segundo, la de octubre.
    """
    pub = datetime.date.fromisoformat(publication_date)
    month = 4 if pub.month <= 6 else 10
    return {
        "edition": f"{pub.year}-{month:02d}",
        "publication_date": pub.isoformat(),
        "projection_start_year": pub.year,
    }


def main():
    total      = len(INDICATORS)
    all_frames = []
    failed     = []

    print(f"Descargando {total} indicadores para {len(ALL_COUNTRIES)} paises "
          f"(desde {START_YEAR})...\n", flush=True)

    for i, (code, description) in enumerate(INDICATORS.items(), 1):
        sys.stdout.write(f"[{i:02d}/{total}] {code} ... ")
        sys.stdout.flush()
        try:
            df = fetch_indicator(code)
            if df.empty:
                print("SIN DATOS")
                failed.append(code)
                continue

            df["indicator_code"]        = code
            df["indicator_description"] = description
            all_frames.append(df)
            print(f"{len(df)} filas")
        except Exception as e:
            print(f"ERROR: {e}")
            failed.append(code)

        time.sleep(BASE_DELAY)

    if failed:
        # No sobrescribir el maestro con datos incompletos
        print(f"\nFallaron {len(failed)} indicadores: {', '.join(failed)}")
        print("latam_weo_all.csv y weo_meta.json NO fueron modificados.")
        sys.exit(1)

    if not PUBLICATION_DATES:
        print("\nLa API no informó PUBLICATION_DATE; no se puede determinar la edición.")
        print("latam_weo_all.csv y weo_meta.json NO fueron modificados.")
        sys.exit(1)

    meta = weo_edition(max(PUBLICATION_DATES))
    proj_start = meta["projection_start_year"]

    master = pd.concat(all_frames, ignore_index=True)
    master.insert(4, "is_projection", master["year"] >= proj_start)

    # CSVs individuales por indicador (ignorados por git)
    for code, sub in master.groupby("indicator_code", sort=False):
        sub.to_csv(os.path.join(OUTPUT_DIR, f"{code}.csv"), index=False, encoding="utf-8",
                   lineterminator="\n")

    master_path = os.path.join(OUTPUT_DIR, "latam_weo_all.csv")
    # Fin de línea fijo: el mismo archivo byte a byte en Windows y en el runner Linux
    master.to_csv(master_path, index=False, encoding="utf-8", lineterminator="\n")
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
        f.write("\n")

    obs  = master[~master["is_projection"]].shape[0]
    proj = master[ master["is_projection"]].shape[0]
    max_year = int(master["year"].max())
    print(f"\nEdición WEO  : {meta['edition']} (publicada {meta['publication_date']})")
    print(f"CSV maestro  : latam_weo_all.csv")
    print(f"  Total filas : {len(master):,}")
    print(f"  Observados  : {obs:,}  (hasta {proj_start - 1})")
    print(f"  Proyecciones: {proj:,}  ({proj_start}-{max_year})")


if __name__ == "__main__":
    main()
