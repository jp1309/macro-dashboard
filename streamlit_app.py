# -*- coding: utf-8 -*-
"""
Macro Dashboard — FMI World Economic Outlook
Autor: Juan-Pablo Erráez
"""
import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

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

# ── Indicadores ──────────────────────────────────────────────────────────────
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

country_options = dict(zip(countries["country_code"], countries["country_name"]))

# Inicializar selección
if "selected_countries" not in st.session_state:
    st.session_state.selected_countries = list(PRESETS["Andinos"])

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0.5rem;'>"
    "<span style='font-weight:700;'>Macro Dashboard</span>"
    "<span style='font-weight:300;'> — FMI World Economic Outlook</span>"
    "</h2>",
    unsafe_allow_html=True,
)

# ── Fila 1: Categoría, Indicador, Período, Base 100 ─────────────────────────
col_cat, col_ind, col_period, col_base = st.columns([2, 3, 4, 1])

with col_cat:
    group = st.selectbox("Categoría", list(INDICATOR_GROUPS.keys()))

with col_ind:
    available_codes = [c for c in INDICATOR_GROUPS[group] if c in indicator_lookup]
    available_labels = [indicator_lookup[c] for c in available_codes]
    ind_label = st.selectbox("Indicador", available_labels)
    indicator = available_codes[available_labels.index(ind_label)]

with col_period:
    year_range = st.slider("Período", YEAR_MIN, YEAR_MAX, (2000, YEAR_MAX))

with col_base:
    st.markdown("<br>", unsafe_allow_html=True)
    base100 = st.toggle("Base 100")

# ── Fila 2: Presets + Países ─────────────────────────────────────────────────
preset_names = list(PRESETS.keys())
preset_cols = st.columns(len(preset_names) + 2)

for i, name in enumerate(preset_names):
    if preset_cols[i].button(name, use_container_width=True, key=f"preset_{name}"):
        st.session_state.selected_countries = list(PRESETS[name])

if preset_cols[-2].button("Todos", use_container_width=True):
    st.session_state.selected_countries = list(countries["country_code"])
if preset_cols[-1].button("Ninguno", use_container_width=True):
    st.session_state.selected_countries = []

_valid_options = set(country_options.keys())
selected_countries = st.multiselect(
    "Países seleccionados",
    options=list(country_options.keys()),
    default=[c for c in st.session_state.selected_countries if c in _valid_options],
    format_func=lambda x: country_options.get(x, x),
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
desc = indicator_lookup.get(indicator, indicator)

base100_valid = base100 and indicator in BASE100_ALLOWED

if base100 and not base100_valid:
    st.warning("Base 100 no aplicable a tasas de variación o indicadores con valores negativos")

fig = go.Figure()

for code in selected_countries:
    sub = dff[dff["country_code"] == code].copy()
    if sub.empty:
        continue
    name = sub["country_name"].iloc[0]
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
                mode="lines+markers", name=f"{name} (proy.)",
                line=dict(color=color, width=line_width, dash="dot"),
                marker=dict(size=marker_size, color=color, symbol="diamond-open"),
                legendgroup=code, showlegend=False,
                hovertemplate=f"<b>{name} (proy.)</b><br>%{{x}}: %{{y:,.2f}}<extra></extra>",
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
        text="← Proyecciones FMI", showarrow=False,
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

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    "<p style='text-align:center; color:gray; font-size:0.8rem;'>"
    "Fuente: FMI — World Economic Outlook (última actualización: octubre 2025)"
    "  •  Zona sombreada = proyecciones FMI  •  Línea punteada = datos proyectados"
    "</p>"
    "<p style='text-align:center; color:gray; font-size:0.75rem;'>"
    "Autor: Juan-Pablo Erráez"
    "</p>",
    unsafe_allow_html=True,
)
