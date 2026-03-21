# Macro Dashboard — FMI World Economic Outlook

Dashboard interactivo de indicadores macroeconómicos para **América Latina, G7 y Emergentes**, construido con datos del [World Economic Outlook (WEO)](https://www.imf.org/en/Publications/WEO) del FMI.

**Autor:** Juan-Pablo Erráez

## Demo

**[https://jp1309-macro-dashboard.streamlit.app/](https://jp1309-macro-dashboard.streamlit.app/)**

## Vista rápida

- 27 indicadores económicos (PIB, inflación, empleo, finanzas públicas, sector externo, ahorro e inversión)
- 41 países: 25 América Latina + 7 G7 + 9 Emergentes
- Serie histórica 1980–2024 + proyecciones FMI 2025–2030
- Gráficos interactivos con Plotly + Streamlit
- Modo Base 100 para comparar evolución relativa entre países
- Eje Y duplicado (izquierda y derecha) para lectura desde ambos lados
- Última actualización de datos: octubre 2025

## Requisitos

```
pip install -r requirements.txt
```

Python 3.10+

## Uso

### 1. Descargar / actualizar datos

```bash
python download.py
```

Descarga los 27 indicadores desde la API SDMX del FMI para los 41 países. Genera:
- Un CSV por indicador (`NGDP_RPCH.csv`, `PCPIPCH.csv`, etc.)
- Un CSV maestro consolidado: `latam_weo_all.csv`

**Cuándo actualizar:** el FMI publica el WEO dos veces al año:

| Publicación FMI | Ejecutar script |
|---|---|
| Abril | Mayo |
| Octubre | Noviembre |

### 2. Lanzar el dashboard localmente

```bash
streamlit run streamlit_app.py
```

Se abre automáticamente en **http://localhost:8501**.

### 3. Deploy en Streamlit Community Cloud

1. Push de este repo a GitHub
2. Ir a [share.streamlit.io](https://share.streamlit.io/)
3. New app → seleccionar repo, branch `main`, archivo `streamlit_app.py`
4. Deploy

## Estructura del proyecto

```
macro-dashboard/
├── streamlit_app.py       # Dashboard Streamlit
├── download.py            # Script de descarga desde API del FMI
├── requirements.txt       # Dependencias Python
├── .gitignore
├── latam_weo_all.csv      # CSV maestro (generado por download.py)
└── README.md
```

## Funcionalidades del dashboard

### Controles

Todos los controles están en el cuerpo principal de la página (no en sidebar):

| Control | Descripción |
|---|---|
| **Categoría** | Selector para filtrar por grupo de indicadores |
| **Indicador** | Selector encadenado con los indicadores de la categoría |
| **Período** | Slider 1980–2030 |
| **Base 100** | Toggle para normalizar series al primer año del rango |
| **Presets** | Botones para seleccionar grupos de países predefinidos |
| **Países** | Multi-select manual para agregar/quitar países individuales |

### Presets de países

| Preset | Países |
|---|---|
| **LA7** | Argentina, Brasil, Chile, Colombia, México, Perú, Uruguay |
| **Centroamérica** | Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panamá |
| **Caribe** | Cuba, Rep. Dominicana, Haití, Jamaica, Trinidad y Tobago, Surinam, Guyana |
| **Andinos** | Ecuador, Perú, Bolivia, Colombia |
| **G7** | EE.UU., Japón, Alemania, Reino Unido, Francia, Italia, Canadá |
| **Emergentes** | Australia, China, India, Indonesia, Rusia, Arabia Saudita, Sudáfrica, Corea del Sur, Turquía |
| **Todos** | Los 41 países |
| **Ninguno** | Limpia la selección |

### Visualización

- **Línea sólida** → datos observados (hasta 2024)
- **Línea punteada** con marcador diamante → proyecciones FMI (2025–2030)
- **Zona sombreada** + línea vertical punteada en 2025 → inicio de proyecciones
- **Línea negra** en el eje Y=0 para referencia
- **Eje Y duplicado** a izquierda y derecha para facilitar lectura
- **Colores fijos** por país (Ecuador = rojo intenso), maximizando contraste visual
- **Hover** muestra solo la información de la línea bajo el cursor

### Modo Base 100

Activa el toggle **"Base 100"** para normalizar todas las series al valor del primer año del rango seleccionado. Útil para comparar evolución relativa entre países con magnitudes muy distintas (ej: PIB nominal de Brasil vs. Bolivia).

- El año base cambia automáticamente al mover el slider de período
- El título y eje Y muestran `Base 100 = {año}`
- **No aplica** a tasas de variación ni indicadores con valores negativos (crecimiento del PIB, inflación, balance fiscal, cuenta corriente, crecimiento de comercio). Se muestra un aviso y los datos se presentan en su unidad original.

## Datos

### Países (41)

**América Latina (25):** Argentina, Belice, Bolivia, Brasil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Guyana, Haití, Honduras, Jamaica, México, Nicaragua, Panamá, Paraguay, Perú, República Dominicana, Surinam, Trinidad y Tobago, Uruguay, Venezuela

**G7 (7):** Alemania, Canadá, Estados Unidos, Francia, Italia, Japón, Reino Unido

**Emergentes (9):** Arabia Saudita, Australia, China, Corea del Sur, India, Indonesia, Rusia, Sudáfrica, Turquía

### Indicadores (27)

| Categoría | Indicadores |
|---|---|
| **PIB y Crecimiento** | Crecimiento real del PIB, PIB nominal (USD y moneda local), PIB per cápita, PIB PPA, PIB PPA per cápita |
| **Precios y Empleo** | Inflación IPC, Inflación esperada, Desempleo, Empleo total, Población |
| **Finanzas Públicas** | Ingresos y gasto gobierno (% PIB y moneda local), Balance fiscal, Deuda pública bruta |
| **Sector Externo** | Cuenta corriente (% PIB y USD), Crecimiento de exportaciones e importaciones (total y bienes) |
| **Ahorro e Inversión** | Inversión total (% PIB), Ahorro nacional bruto (% PIB) |

### Formato del CSV maestro (`latam_weo_all.csv`)

| Columna | Descripción |
|---|---|
| `country_code` | Código ISO3 del país |
| `country_name` | Nombre en español |
| `year` | Año (1980–2030) |
| `value` | Valor numérico del indicador |
| `is_projection` | `True` si el año ≥ 2025 (proyección FMI) |
| `indicator_code` | Código WEO del FMI |
| `indicator_description` | Descripción en español |

## API del FMI

El script `download.py` usa la API SDMX del FMI:

```
https://api.imf.org/external/sdmx/2.1/data/IMF.RES,WEO,+/{países}.{indicador}.A
```

Consideraciones de rate-limit:
- Requests separados por grupo (LATAM, G7, Emergentes)
- 3 segundos de pausa entre requests
- Reintentos con backoff exponencial (10s, 20s, 40s) hasta 4 intentos
