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

Recomendación: correr este script en mayo y noviembre de cada año.

CÓMO ACTUALIZAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Correr:
       python download.py
2. Los CSVs individuales y el maestro se sobreescriben automáticamente.
3. No hay END_YEAR fijo — la API devuelve todos los años disponibles,
   incluyendo nuevas proyecciones que el FMI extienda.

NOTA SOBRE PROYECCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECTION_START_YEAR se calcula automáticamente como el año actual.
Datos del año en curso y posteriores se marcan como proyección.
"""
import sys
import requests
import pandas as pd
from lxml import etree
import os
import time

# ── Configuración de años ───────────────────────────────────────────────────
import datetime
START_YEAR            = 1980
# Sin END_YEAR fijo: la API devuelve todos los años disponibles (incluye
# proyecciones que el FMI extienda a futuro, ej. 2031+).
PROJECTION_START_YEAR = datetime.date.today().year  # primer año sin datos observados

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
    "NGDPD":       "PIB nominal (USD, miles de millones)",
    "NGDPDPC":     "PIB per cápita (USD)",
    "PPPGDP":      "PIB PPA (miles de millones USD)",
    "PPPPC":       "PIB PPA per cápita (USD)",
    "PPPSH":       "Participación en PIB mundial (%)",
    # Precios y Empleo
    "PCPIPCH":     "Inflación IPC (%)",
    "LUR":         "Tasa de desempleo (%)",
    "LE":          "Empleo total (millones)",
    "LP":          "Población (millones)",
    # Finanzas Públicas
    "GGR_NGDP":    "Ingresos gobierno (% PIB)",
    "GGX_NGDP":    "Gasto gobierno (% PIB)",
    "GGXCNL_NGDP": "Balance fiscal neto (% PIB)",
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
                    "is_projection": year >= PROJECTION_START_YEAR,
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


def main():
    total      = len(INDICATORS)
    all_frames = []

    print(f"Descargando {total} indicadores para {len(ALL_COUNTRIES)} paises "
          f"(desde {START_YEAR})...\n", flush=True)

    for i, (code, description) in enumerate(INDICATORS.items(), 1):
        sys.stdout.write(f"[{i:02d}/{total}] {code} ... ")
        sys.stdout.flush()
        try:
            df = fetch_indicator(code)
            if df.empty:
                print("SIN DATOS")
                continue

            df["indicator_code"]        = code
            df["indicator_description"] = description
            all_frames.append(df)

            out_path = os.path.join(OUTPUT_DIR, f"{code}.csv")
            df.to_csv(out_path, index=False, encoding="utf-8")
            print(f"{len(df)} filas")
        except Exception as e:
            print(f"ERROR: {e}")

        time.sleep(BASE_DELAY)

    if all_frames:
        master      = pd.concat(all_frames, ignore_index=True)
        master_path = os.path.join(OUTPUT_DIR, "latam_weo_all.csv")
        master.to_csv(master_path, index=False, encoding="utf-8")
        obs  = master[~master["is_projection"]].shape[0]
        proj = master[ master["is_projection"]].shape[0]
        print(f"\nCSV maestro: latam_weo_all.csv")
        print(f"  Total filas : {len(master):,}")
        print(f"  Observados  : {obs:,}  (hasta {PROJECTION_START_YEAR - 1})")
        max_year = int(master["year"].max())
        print(f"  Proyecciones: {proj:,}  ({PROJECTION_START_YEAR}-{max_year})")
        print(f"\nProxima actualizacion recomendada:")
        print(f"  Mayo    (tras publicacion WEO de abril)")
        print(f"  Noviembre (tras publicacion WEO de octubre)")
    else:
        print("\nNo se descargo ningun dato.")


if __name__ == "__main__":
    main()
