# -*- coding: utf-8 -*-
"""
Macro Dashboard — FMI World Economic Outlook
Autor: Juan-Pablo Erráez
"""
import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from country_summaries import COUNTRY_SUMMARIES

# ── Config ───────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Macro Dashboard — FMI WEO",
    page_icon="📊",
    layout="wide",
)

# ── Datos ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "latam_weo_all.csv")


@st.cache_data(ttl=3600)
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["is_projection"] = data["is_projection"].astype(str).str.strip().str.lower() == "true"
    data["value"] = pd.to_numeric(data["value"], errors="coerce")
    return data


df = load_data()

indicators = (
    df[["indicator_code", "indicator_description"]]
    .drop_duplicates()
    .sort_values("indicator_description")
)
countries = (
    df[["country_code", "country_name"]]
    .drop_duplicates()
    .sort_values("country_name")
)

YEAR_MIN = int(df["year"].min())
YEAR_MAX = int(df["year"].max())
PROJECTION_YEAR = int(df.loc[df["is_projection"], "year"].min()) if df["is_projection"].any() else YEAR_MAX + 1

# ── Colores fijos por país ───────────────────────────────────────────────────
COUNTRY_COLORS = {
    "ECU": "#FF0000",  "ARG": "#6CACE4",  "BOL": "#2E8B57",  "BRA": "#FFD700",
    "CHL": "#B22222",  "COL": "#FF8C00",  "CRI": "#4169E1",  "CUB": "#1B1B6E",
    "DOM": "#8B008B",  "SLV": "#00BFFF",  "GTM": "#40E0D0",  "HTI": "#6A0DAD",
    "HND": "#0077B6",  "JAM": "#228B22",  "MEX": "#006847",  "NIC": "#87CEEB",
    "PAN": "#E91E63",  "PRY": "#DC143C",  "PER": "#D2691E",  "URY": "#191970",
    "VEN": "#DAA520",  "BLZ": "#708090",  "GUY": "#00CED1",  "SUR": "#556B2F",
    "TTO": "#C71585",
    "USA": "#3C3B6E",  "JPN": "#FF6347",  "DEU": "#333333",  "GBR": "#00247D",
    "FRA": "#0055A4",  "ITA": "#008C45",  "CAN": "#FF4500",
    "AUS": "#FFCD00",  "CHN": "#DE2910",  "IND": "#FF9933",  "IDN": "#CC0000",
    "RUS": "#0039A6",  "SAU": "#006C35",  "ZAF": "#007749",  "KOR": "#003478",
    "TUR": "#E30A17",
    "TWN": "#4B0082",  "SGP": "#E8A317",  "ARE": "#BF00FF",  "PHL": "#1E90FF",
    "VNM": "#8B4513",  "MYS": "#00C78C",  "EGY": "#CD853F",  "NGA": "#2F4F4F",
}

# ── Traducciones ─────────────────────────────────────────────────────────────
I18N = {
    "es": {
        "title_bold": "Macro Dashboard",
        "title_light": " — FMI World Economic Outlook",
        "category": "Categoría",
        "indicator": "Indicador",
        "period": "Período",
        "all": "Todos",
        "none": "Ninguno",
        "base100_warn": "Base 100 no aplicable a tasas de variación o indicadores con valores negativos",
        "proj_label": "Proyecciones FMI",
        "proj_suffix": "(proy.)",
        "footer_source": "Fuente: FMI — World Economic Outlook (última actualización: octubre 2025)",
        "footer_legend": "Zona sombreada = proyecciones FMI  •  Línea punteada = datos proyectados",
        "footer_author": "Autor: Juan-Pablo Erráez",
        "groups": {
            "PIB y Crecimiento": "PIB y Crecimiento",
            "Precios y Empleo": "Precios y Empleo",
            "Finanzas Públicas": "Finanzas Públicas",
            "Sector Externo": "Sector Externo",
            "Ahorro e Inversión": "Ahorro e Inversión",
        },
        "indicators": {
            "NGDP_RPCH":   "Crecimiento real del PIB (%)",
            "NGDPD":       "PIB nominal (USD, miles de millones)",
            "NGDPDPC":     "PIB per cápita (USD)",
            "PPPGDP":      "PIB PPA (miles de millones USD)",
            "PPPPC":       "PIB PPA per cápita (USD)",
            "PCPIPCH":     "Inflación IPC (%)",
            "LUR":         "Tasa de desempleo (%)",
            "LE":          "Empleo total (millones)",
            "LP":          "Población (millones)",
            "GGR_NGDP":    "Ingresos gobierno (% PIB)",
            "GGX_NGDP":    "Gasto gobierno (% PIB)",
            "GGXCNL_NGDP": "Balance fiscal neto (% PIB)",
            "GGXWDG_NGDP": "Deuda pública bruta (% PIB)",
            "BCA_NGDPD":   "Cuenta corriente (% PIB)",
            "BCA":         "Cuenta corriente (USD)",
            "TX_RPCH":     "Crecimiento exportaciones (%)",
            "TM_RPCH":     "Crecimiento importaciones (%)",
            "TXG_RPCH":    "Crecimiento exportaciones bienes (%)",
            "TMG_RPCH":    "Crecimiento importaciones bienes (%)",
            "NID_NGDP":    "Inversión total (% PIB)",
            "NGSD_NGDP":   "Ahorro nacional bruto (% PIB)",
        },
        "countries": {
            "ARG": "Argentina", "BOL": "Bolivia", "BRA": "Brasil", "CHL": "Chile",
            "COL": "Colombia", "CRI": "Costa Rica", "CUB": "Cuba",
            "DOM": "República Dominicana", "ECU": "Ecuador", "SLV": "El Salvador",
            "GTM": "Guatemala", "HTI": "Haití", "HND": "Honduras", "MEX": "México",
            "NIC": "Nicaragua", "PAN": "Panamá", "PRY": "Paraguay", "PER": "Perú",
            "URY": "Uruguay", "VEN": "Venezuela", "BLZ": "Belice", "GUY": "Guyana",
            "SUR": "Surinam", "JAM": "Jamaica", "TTO": "Trinidad y Tobago",
            "USA": "Estados Unidos", "JPN": "Japón", "DEU": "Alemania",
            "GBR": "Reino Unido", "FRA": "Francia", "ITA": "Italia", "CAN": "Canadá",
            "AUS": "Australia", "CHN": "China", "IND": "India", "IDN": "Indonesia",
            "RUS": "Rusia", "SAU": "Arabia Saudita", "ZAF": "Sudáfrica",
            "KOR": "Corea del Sur", "TUR": "Turquía", "TWN": "Taiwán",
            "SGP": "Singapur", "ARE": "Emiratos Árabes Unidos", "PHL": "Filipinas",
            "VNM": "Vietnam", "MYS": "Malasia", "EGY": "Egipto", "NGA": "Nigeria",
        },
    },
    "en": {
        "title_bold": "Macro Dashboard",
        "title_light": " — IMF World Economic Outlook",
        "category": "Category",
        "indicator": "Indicator",
        "period": "Period",
        "all": "All",
        "none": "None",
        "base100_warn": "Base 100 not applicable to growth rates or indicators with negative values",
        "proj_label": "IMF Projections",
        "proj_suffix": "(proj.)",
        "footer_source": "Source: IMF — World Economic Outlook (last update: October 2025)",
        "footer_legend": "Shaded area = IMF projections  •  Dotted line = projected data",
        "footer_author": "Author: Juan-Pablo Erráez",
        "groups": {
            "PIB y Crecimiento": "GDP & Growth",
            "Precios y Empleo": "Prices & Employment",
            "Finanzas Públicas": "Public Finance",
            "Sector Externo": "External Sector",
            "Ahorro e Inversión": "Savings & Investment",
        },
        "indicators": {
            "NGDP_RPCH":   "Real GDP Growth (%)",
            "NGDPD":       "Nominal GDP (USD, billions)",
            "NGDPDPC":     "GDP per capita (USD)",
            "PPPGDP":      "GDP PPP (USD, billions)",
            "PPPPC":       "GDP PPP per capita (USD)",
            "PCPIPCH":     "CPI Inflation (%)",
            "LUR":         "Unemployment Rate (%)",
            "LE":          "Total Employment (millions)",
            "LP":          "Population (millions)",
            "GGR_NGDP":    "Government Revenue (% GDP)",
            "GGX_NGDP":    "Government Expenditure (% GDP)",
            "GGXCNL_NGDP": "Net Fiscal Balance (% GDP)",
            "GGXWDG_NGDP": "Gross Public Debt (% GDP)",
            "BCA_NGDPD":   "Current Account (% GDP)",
            "BCA":         "Current Account (USD)",
            "TX_RPCH":     "Export Growth (%)",
            "TM_RPCH":     "Import Growth (%)",
            "TXG_RPCH":    "Goods Export Growth (%)",
            "TMG_RPCH":    "Goods Import Growth (%)",
            "NID_NGDP":    "Total Investment (% GDP)",
            "NGSD_NGDP":   "Gross National Savings (% GDP)",
        },
        "countries": {
            "ARG": "Argentina", "BOL": "Bolivia", "BRA": "Brazil", "CHL": "Chile",
            "COL": "Colombia", "CRI": "Costa Rica", "CUB": "Cuba",
            "DOM": "Dominican Republic", "ECU": "Ecuador", "SLV": "El Salvador",
            "GTM": "Guatemala", "HTI": "Haiti", "HND": "Honduras", "MEX": "Mexico",
            "NIC": "Nicaragua", "PAN": "Panama", "PRY": "Paraguay", "PER": "Peru",
            "URY": "Uruguay", "VEN": "Venezuela", "BLZ": "Belize", "GUY": "Guyana",
            "SUR": "Suriname", "JAM": "Jamaica", "TTO": "Trinidad and Tobago",
            "USA": "United States", "JPN": "Japan", "DEU": "Germany",
            "GBR": "United Kingdom", "FRA": "France", "ITA": "Italy", "CAN": "Canada",
            "AUS": "Australia", "CHN": "China", "IND": "India", "IDN": "Indonesia",
            "RUS": "Russia", "SAU": "Saudi Arabia", "ZAF": "South Africa",
            "KOR": "South Korea", "TUR": "Turkey", "TWN": "Taiwan",
            "SGP": "Singapore", "ARE": "United Arab Emirates", "PHL": "Philippines",
            "VNM": "Vietnam", "MYS": "Malaysia", "EGY": "Egypt", "NGA": "Nigeria",
        },
    },
}

PRESET_NAMES_EN = {
    "Centroamérica": "Central America",
    "Caribe": "Caribbean",
    "Andinos": "Andean",
    "Emergentes": "Emerging",
    "Todos": "All",
    "Ninguno": "None",
}

# ── Indicadores (estructura interna) ────────────────────────────────────────
INDICATOR_GROUPS = {
    "PIB y Crecimiento": ["NGDP_RPCH", "NGDPD", "NGDPDPC", "PPPGDP", "PPPPC"],
    "Precios y Empleo": ["PCPIPCH", "LUR", "LP"],
    "Finanzas Públicas": ["GGR_NGDP", "GGX_NGDP", "GGXCNL_NGDP", "GGXWDG_NGDP"],
    "Sector Externo": ["BCA_NGDPD", "BCA", "TX_RPCH", "TM_RPCH", "TXG_RPCH", "TMG_RPCH"],
    "Ahorro e Inversión": ["NID_NGDP", "NGSD_NGDP"],
}

indicator_lookup = dict(zip(indicators["indicator_code"], indicators["indicator_description"]))

BASE100_ALLOWED = {
    "NGDPD", "NGDPDPC", "PPPGDP", "PPPPC",
    "LP", "LE", "LUR",
    "GGR_NGDP", "GGX_NGDP", "GGXWDG_NGDP",
    "NID_NGDP", "NGSD_NGDP",
}

# ── Presets de países ────────────────────────────────────────────────────────
PRESETS = {
    "LA7": ["ARG", "BRA", "CHL", "COL", "MEX", "PER", "URY"],
    "Centroamérica": ["CRI", "SLV", "GTM", "HND", "NIC", "PAN"],
    "Caribe": ["CUB", "DOM", "HTI", "JAM", "TTO", "SUR", "GUY"],
    "Andinos": ["ECU", "PER", "BOL", "COL"],
    "G7": ["USA", "JPN", "DEU", "GBR", "FRA", "ITA", "CAN"],
    "Emergentes": ["AUS", "CHN", "IND", "IDN", "RUS", "SAU", "ZAF", "KOR", "TUR", "TWN", "SGP", "ARE", "PHL", "VNM", "MYS", "EGY", "NGA"],
}

# Inicializar selección
if "selected_countries" not in st.session_state:
    st.session_state.selected_countries = list(PRESETS["Andinos"])

# ── Idioma ───────────────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "es"

col_header, col_lang = st.columns([9, 1])

with col_lang:
    if st.button("English" if st.session_state.lang == "es" else "Español",
                 use_container_width=True, key="lang_toggle"):
        st.session_state.lang = "en" if st.session_state.lang == "es" else "es"
        st.rerun()

t = I18N[st.session_state.lang]

# Funciones helper de traducción
def t_country(code):
    return t["countries"].get(code, code)

def t_indicator(code):
    return t["indicators"].get(code, indicator_lookup.get(code, code))

def t_group(group_key):
    return t["groups"].get(group_key, group_key)

def t_preset(name):
    if st.session_state.lang == "en":
        return PRESET_NAMES_EN.get(name, name)
    return name

# ── Header ───────────────────────────────────────────────────────────────────
with col_header:
    st.markdown(
        f"<h2 style='text-align:center; margin-bottom:0.5rem;'>"
        f"<span style='font-weight:700;'>{t['title_bold']}</span>"
        f"<span style='font-weight:300;'>{t['title_light']}</span>"
        f"</h2>",
        unsafe_allow_html=True,
    )

# ── Fila 1: Categoría, Indicador, Período, Base 100 ─────────────────────────
col_cat, col_ind, col_period, col_base = st.columns([2, 3, 4, 1])

group_keys = list(INDICATOR_GROUPS.keys())
group_labels = [t_group(g) for g in group_keys]

with col_cat:
    group_label = st.selectbox(t["category"], group_labels)
    group = group_keys[group_labels.index(group_label)]

with col_ind:
    available_codes = [c for c in INDICATOR_GROUPS[group] if c in indicator_lookup]
    available_labels = [t_indicator(c) for c in available_codes]
    ind_label = st.selectbox(t["indicator"], available_labels)
    indicator = available_codes[available_labels.index(ind_label)]

with col_period:
    year_range = st.slider(t["period"], YEAR_MIN, YEAR_MAX, (2000, YEAR_MAX))

with col_base:
    st.markdown("<br>", unsafe_allow_html=True)
    base100 = st.toggle("Base 100")

# ── Fila 2: Presets + Países ─────────────────────────────────────────────────
preset_names = list(PRESETS.keys())
preset_cols = st.columns(len(preset_names) + 2)

for i, name in enumerate(preset_names):
    if preset_cols[i].button(t_preset(name), use_container_width=True, key=f"preset_{name}"):
        st.session_state.selected_countries = list(PRESETS[name])

if preset_cols[-2].button(t["all"], use_container_width=True):
    st.session_state.selected_countries = list(countries["country_code"])
if preset_cols[-1].button(t["none"], use_container_width=True):
    st.session_state.selected_countries = []

_valid_options = set(countries["country_code"])
selected_countries = st.multiselect(
    "countries",
    options=list(countries["country_code"]),
    default=[c for c in st.session_state.selected_countries if c in _valid_options],
    format_func=t_country,
    label_visibility="collapsed",
)
st.session_state.selected_countries = selected_countries

# ── Gráfico ──────────────────────────────────────────────────────────────────
y_min, y_max = year_range
mask = (
    (df["indicator_code"] == indicator)
    & (df["country_code"].isin(selected_countries))
    & (df["year"].between(y_min, y_max))
)
dff = df.loc[mask].sort_values("year")
desc = t_indicator(indicator)

base100_valid = base100 and indicator in BASE100_ALLOWED

if base100 and not base100_valid:
    st.warning(t["base100_warn"])

fig = go.Figure()

for code in selected_countries:
    sub = dff[dff["country_code"] == code].copy()
    if sub.empty:
        continue
    name = t_country(code)
    color = COUNTRY_COLORS.get(code, "#636EFA")

    if base100_valid:
        base_val = sub["value"].iloc[0]
        sub["value"] = sub["value"] / base_val * 100

    obs = sub[~sub["is_projection"]]
    proj = sub[sub["is_projection"]]

    line_width = 3.5 if code == "ECU" else 2
    marker_size = 6 if code == "ECU" else 4

    fig.add_trace(
        go.Scatter(
            x=obs["year"], y=obs["value"],
            mode="lines+markers", name=name,
            line=dict(color=color, width=line_width),
            marker=dict(size=marker_size, color=color),
            legendgroup=code,
            hovertemplate=f"<b>{name}</b><br>%{{x}}: %{{y:,.2f}}<extra></extra>",
        )
    )

    if not proj.empty:
        bridge = pd.concat([obs.iloc[[-1]], proj]) if not obs.empty else proj
        fig.add_trace(
            go.Scatter(
                x=bridge["year"], y=bridge["value"],
                mode="lines+markers", name=f"{name} {t['proj_suffix']}",
                line=dict(color=color, width=line_width, dash="dot"),
                marker=dict(size=marker_size, color=color, symbol="diamond-open"),
                legendgroup=code, showlegend=False,
                hovertemplate=f"<b>{name} {t['proj_suffix']}</b><br>%{{x}}: %{{y:,.2f}}<extra></extra>",
            )
        )

# Trace invisible para activar eje derecho (mirror)
fig.add_trace(
    go.Scatter(x=[None], y=[None], yaxis="y2", showlegend=False, hoverinfo="skip")
)

if y_min < PROJECTION_YEAR <= y_max:
    fig.add_vrect(
        x0=PROJECTION_YEAR - 0.5, x1=y_max + 0.5,
        fillcolor="rgba(128,128,128,0.08)", line_width=0,
    )
    fig.add_vline(
        x=PROJECTION_YEAR, line_dash="dash",
        line_color="rgba(128,128,128,0.4)", line_width=1,
    )
    fig.add_annotation(
        x=PROJECTION_YEAR + 0.3, y=1.02, yref="paper",
        text=t["proj_label"], showarrow=False,
        font=dict(size=10, color="gray"),
    )

y_title = f"Base 100 = {y_min}" if base100_valid else desc

fig.update_layout(
    title=dict(
        text=f"{desc}  (Base 100 = {y_min})" if base100_valid else desc,
        font=dict(size=18),
    ),
    xaxis=dict(title="", dtick=5, gridcolor="rgba(0,0,0,0.05)"),
    yaxis=dict(
        title=y_title, gridcolor="rgba(0,0,0,0.1)",
        zeroline=True, zerolinecolor="black", zerolinewidth=1.5,
    ),
    yaxis2=dict(
        overlaying="y", side="right",
        showgrid=False, zeroline=False,
        matches="y", showticklabels=True,
    ),
    template="plotly_white",
    hovermode="closest",
    legend=dict(
        orientation="h", yanchor="top", y=-0.12,
        xanchor="center", x=0.5, font=dict(size=11),
    ),
    margin=dict(l=60, r=60, t=50, b=100),
    plot_bgcolor="white",
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

# ── Resúmenes WEO por país ──────────────────────────────────────────────────
summaries_lang = COUNTRY_SUMMARIES.get(st.session_state.lang, COUNTRY_SUMMARIES["es"])
country_summaries_to_show = [
    (code, t_country(code), summaries_lang.get(code))
    for code in selected_countries
    if summaries_lang.get(code)
]

COUNTRY_FLAGS = {
    "ARG": "ar", "BOL": "bo", "BRA": "br", "CHL": "cl", "COL": "co",
    "CRI": "cr", "CUB": "cu", "DOM": "do", "ECU": "ec", "SLV": "sv",
    "GTM": "gt", "GUY": "gy", "HTI": "ht", "HND": "hn", "JAM": "jm",
    "MEX": "mx", "NIC": "ni", "PAN": "pa", "PRY": "py", "PER": "pe",
    "URY": "uy", "VEN": "ve", "BLZ": "bz", "SUR": "sr", "TTO": "tt",
    "USA": "us", "JPN": "jp", "DEU": "de", "GBR": "gb", "FRA": "fr",
    "ITA": "it", "CAN": "ca", "AUS": "au", "CHN": "cn", "IND": "in",
    "IDN": "id", "RUS": "ru", "SAU": "sa", "ZAF": "za", "KOR": "kr",
    "TUR": "tr", "TWN": "tw", "SGP": "sg", "ARE": "ae", "PHL": "ph",
    "VNM": "vn", "MYS": "my", "EGY": "eg", "NGA": "ng",
}
_FLAG_URL = "https://flagcdn.com/24x18/{}.png"

if country_summaries_to_show:
    weo_title = "WEO Octubre 2025 — Resumen por país" if st.session_state.lang == "es" else "WEO October 2025 — Country Summary"
    with st.expander(weo_title, expanded=True):
        for code, name, summary in country_summaries_to_show:
            color = COUNTRY_COLORS.get(code, "#636EFA")
            flag_code = COUNTRY_FLAGS.get(code, "")
            flag_img = f'<img src="{_FLAG_URL.format(flag_code)}" style="vertical-align:middle; margin-right:6px;">' if flag_code else ""
            st.markdown(
                f"<h4 style='color:{color}; margin-bottom:0.3rem;'>{flag_img}{name}</h4>"
                f"<p style='font-size:0.9rem; text-align:justify;'>{summary}</p>"
                f"<hr style='margin:0.5rem 0;'>",
                unsafe_allow_html=True,
            )

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    f"<p style='text-align:center; color:gray; font-size:0.8rem;'>"
    f"{t['footer_source']}"
    f"  •  {t['footer_legend']}"
    f"</p>"
    f"<p style='text-align:center; color:gray; font-size:0.75rem;'>"
    f"{t['footer_author']}"
    f"</p>",
    unsafe_allow_html=True,
)
