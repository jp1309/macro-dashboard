# LATAM Macro Dashboard

Dashboard interactivo de indicadores macroeconómicos para **América Latina, G7 y Emergentes**, construido con datos del [World Economic Outlook (WEO)](https://www.imf.org/en/Publications/WEO) del FMI.

## Vista rápida

- 27 indicadores económicos (PIB, inflación, empleo, finanzas públicas, sector externo, ahorro e inversión)
- 41 países: 25 América Latina + 7 G7 + 9 Emergentes
- Serie histórica 1980–2024 + proyecciones FMI 2025–2030
- Gráficos interactivos con Plotly, interfaz con Dash + Bootstrap
- Modo Base 100 para comparar evolución relativa entre países

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

### 2. Lanzar el dashboard

```bash
python app.py
```

Abrir **http://127.0.0.1:8060/** en el navegador.

## Estructura del proyecto

```
latam_weo_data/
├── app.py                 # Dashboard Dash/Plotly
├── download.py            # Script de descarga desde API del FMI
├── requirements.txt       # Dependencias Python
├── .gitignore
├── latam_weo_all.csv      # CSV maestro (generado)
├── NGDP_RPCH.csv          # CSVs individuales por indicador (generados)
├── ...                    # (27 CSVs de indicadores)
└── README.md
```

## Funcionalidades del dashboard

### Controles

| Control | Descripción |
|---|---|
| **Categoría** | Dropdown para filtrar por grupo de indicadores |
| **Indicador** | Dropdown encadenado con los indicadores de la categoría seleccionada |
| **Países** | Multi-select + botones de presets regionales |
| **Período** | Range slider 1980–2030 |
| **Base 100** | Switch para normalizar todas las series al primer año del rango seleccionado |

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

**Combinar grupos:** mantener presionada la tecla **CTRL** al hacer click en un preset para agregar esos países a la selección actual (ej: CTRL+Andinos + CTRL+G7).

### Visualización

- **Línea sólida** → datos observados (hasta 2024)
- **Línea punteada** con marcador diamante → proyecciones FMI (2025–2030)
- **Zona sombreada** + línea vertical punteada en 2025 → inicio de proyecciones
- **Línea negra** en el eje Y=0 para referencia
- **Colores fijos** por país, diferenciados para máximo contraste visual
- **Hover** muestra solo la información de la línea sobre la que se pasa el mouse

### Modo Base 100

Activa el switch **"Base 100"** para normalizar todas las series al valor del primer año del rango seleccionado. Útil para comparar evolución relativa entre países con magnitudes muy distintas (ej: PIB nominal de Brasil vs. Bolivia).

- El año base cambia automáticamente al mover el slider de período
- El título y eje Y muestran `Base 100 = {año}`
- **No aplica** a indicadores que pueden tener valores negativos o cero en el año base (balance fiscal, cuenta corriente, crecimiento del PIB). En ese caso se muestra un aviso y los datos se presentan en su unidad original.

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
- Requests separados por grupo (LATAM, G7, Emergentes) — máx ~25 países por request
- 3 segundos de pausa entre requests
- Reintentos con backoff exponencial (10s, 20s, 40s) hasta 4 intentos
