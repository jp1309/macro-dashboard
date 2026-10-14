# Macro Dashboard — FMI World Economic Outlook

Dashboard interactivo de indicadores macroeconómicos para **América Latina, G7 y Emergentes**, construido con datos del [World Economic Outlook (WEO)](https://www.imf.org/en/Publications/WEO) del FMI.

**Autor:** Juan-Pablo Erráez

## Demo

**[https://jp1309-macro-dashboard.streamlit.app/](https://jp1309-macro-dashboard.streamlit.app/)**

## Vista rápida

- 21 indicadores económicos (PIB, inflación, empleo, finanzas públicas, sector externo, ahorro e inversión)
- 49 países: 25 América Latina + 7 G7 + 17 Emergentes
- Serie histórica desde 1980 + proyecciones FMI (horizonte dinámico)
- Actualización automática de datos vía GitHub Actions (abril, septiembre y octubre), con detección automática de la edición del WEO
- Gráficos interactivos con Plotly + Streamlit
- Modo Base 100 para comparar evolución relativa entre países
- Eje Y duplicado (izquierda y derecha) para lectura desde ambos lados
- Toggle idioma Español/English para toda la interfaz
- Resúmenes WEO por país con banderas, extraídos del PDF oficial del FMI

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

Descarga los 30 indicadores desde la API SDMX del FMI para los 49 países. Genera:
- Un CSV por indicador (`NGDP_RPCH.csv`, `PCPIPCH.csv`, etc.; ignorados por git)
- Un CSV maestro consolidado: `latam_weo_all.csv`
- `weo_meta.json` con la edición del WEO (p. ej. `"2026-10"`), derivada de la fecha de publicación que informa la API. El dashboard la usa para sus etiquetas y para marcar las proyecciones (año de publicación en adelante).

Si falla cualquier indicador, el script termina con error y **no** modifica el CSV maestro ni `weo_meta.json`.

No hay año final fijo — la API devuelve todos los años disponibles, incluyendo proyecciones que el FMI extienda a futuro. Los datos históricos se re-descargan completos en cada ejecución (el FMI los reprocesa periódicamente).

### 2. Actualización automática

Un **GitHub Action** (`.github/workflows/update-data.yml`) corre **todos los días de abril, septiembre y octubre** a las 10:00 UTC, porque la fecha de publicación del WEO cambia cada año.

Cada día descarga los datos y revisa si cambiaron `latam_weo_all.csv` o `weo_meta.json`:
- **Hay cambios** (WEO nuevo publicado): hace commit y push — Streamlit Cloud se actualiza solo.
- **No hay cambios**: no hace nada y vuelve a revisar al día siguiente.
- **Los resúmenes por país quedaron atrás** (la edición de `SUMMARIES_EDITION` en `country_summaries.py` no coincide con la de los datos): abre un issue en GitHub como recordatorio (uno solo, sin duplicados).

El workflow necesita permiso de escritura (`permissions: contents: write`, ya declarado en el YAML). Si en *Settings → Actions → General → Workflow permissions* la organización fuerza "Read repository contents", el push fallará.

También se puede ejecutar manualmente desde la pestaña **Actions** del repo en GitHub.

### 3. Actualizar los resúmenes por país (manual, dos veces al año)

Los textos de `country_summaries.py` se escriben a partir del informe del FMI y no se pueden generar solos. Cuando sale un WEO nuevo:

1. El Action actualiza los datos y abre el issue *"Actualizar resúmenes por país al WEO AAAA-MM"*.
2. Mientras tanto, el dashboard muestra un aviso sobre los textos; las **cifras clave** de cada país (PIB, inflación, desempleo, cuenta corriente, balance fiscal y deuda) se calculan desde el CSV y ya están actualizadas.
3. Reescribir los textos con el nuevo informe y cambiar `SUMMARIES_EDITION = "AAAA-MM"`. Al hacer push, el aviso desaparece; cerrar el issue.

### 4. Lanzar el dashboard localmente

```bash
streamlit run streamlit_app.py
```

Se abre automáticamente en **http://localhost:8501**.

### 5. Deploy en Streamlit Community Cloud

1. Push de este repo a GitHub
2. Ir a [share.streamlit.io](https://share.streamlit.io/)
3. New app → seleccionar repo, branch `main`, archivo `streamlit_app.py`
4. Deploy

## Estructura del proyecto

```
macro-dashboard/
├── streamlit_app.py              # Dashboard Streamlit (ES/EN)
├── download.py                   # Script de descarga desde API del FMI
├── country_summaries.py          # Resúmenes WEO por país (ES/EN, 49 países)
├── requirements.txt              # Dependencias Python
├── .github/workflows/
│   └── update-data.yml           # GitHub Action para actualización automática
├── .gitignore
├── latam_weo_all.csv             # CSV maestro (generado por download.py)
├── weo_meta.json                 # Edición del WEO de los datos (generado por download.py)
├── analysis/
│   └── clustering_jerarquico/    # Análisis de clustering jerárquico
└── README.md
```

## Funcionalidades del dashboard

### Controles

Todos los controles están en el cuerpo principal de la página (no en sidebar):

| Control | Descripción |
|---|---|
| **Categoría** | Selector para filtrar por grupo de indicadores |
| **Indicador** | Selector encadenado con los indicadores de la categoría |
| **Período** | Slider dinámico según rango disponible en los datos |
| **Base 100** | Toggle para normalizar series al primer año del rango |
| **Presets** | Botones para seleccionar grupos de países predefinidos |
| **Países** | Multi-select manual para agregar/quitar países individuales |
| **Idioma** | Botón English/Español para cambiar idioma de toda la interfaz |

### Presets de países

| Preset | Países |
|---|---|
| **LA7** | Argentina, Brasil, Chile, Colombia, México, Perú, Uruguay |
| **Centroamérica** | Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panamá |
| **Caribe** | Cuba, Rep. Dominicana, Haití, Jamaica, Trinidad y Tobago, Surinam, Guyana |
| **Andinos** | Ecuador, Perú, Bolivia, Colombia |
| **G7** | EE.UU., Japón, Alemania, Reino Unido, Francia, Italia, Canadá |
| **Emergentes** | Australia, China, India, Indonesia, Rusia, Arabia Saudita, Sudáfrica, Corea del Sur, Turquía, Taiwán, Singapur, EAU, Filipinas, Vietnam, Malasia, Egipto, Nigeria |
| **Todos** | Los 49 países |
| **Ninguno** | Limpia la selección |

### Visualización

- **Línea sólida** → datos observados
- **Línea punteada** con marcador diamante → proyecciones FMI
- **Zona sombreada** + línea vertical punteada → inicio de proyecciones
- **Línea negra** en el eje Y=0 para referencia
- **Eje Y duplicado** a izquierda y derecha para facilitar lectura
- **Colores fijos** por país (Ecuador = rojo intenso, línea más gruesa), maximizando contraste visual
- **Hover** muestra solo la información de la línea bajo el cursor

### Idioma

Botón **"English"** / **"Español"** en la parte superior para cambiar el idioma de toda la interfaz: título, categorías, indicadores, nombres de países, presets, etiquetas y resúmenes.

### Resúmenes WEO por país

Debajo del gráfico se muestran, para cada país seleccionado y con su bandera:

- una tabla de **cifras clave** (año anterior al inicio de las proyecciones y los dos siguientes) calculada desde el CSV, siempre alineada con la edición de los datos;
- un **texto** con las revisiones frente a la edición anterior y los factores que destaca el informe del FMI (edición indicada en el título del recuadro).

### Modo Base 100

Activa el toggle **"Base 100"** para normalizar todas las series al valor del primer año del rango seleccionado. Útil para comparar evolución relativa entre países con magnitudes muy distintas (ej: PIB nominal de Brasil vs. Bolivia).

- El año base cambia automáticamente al mover el slider de período
- El título y eje Y muestran `Base 100 = {año}`
- **No aplica** a tasas de variación ni indicadores con valores negativos (crecimiento del PIB, inflación, balance fiscal, cuenta corriente, crecimiento de comercio). Se muestra un aviso y los datos se presentan en su unidad original.

## Datos

### Países (49)

**América Latina (25):** Argentina, Belice, Bolivia, Brasil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Guyana, Haití, Honduras, Jamaica, México, Nicaragua, Panamá, Paraguay, Perú, República Dominicana, Surinam, Trinidad y Tobago, Uruguay, Venezuela

**G7 (7):** Alemania, Canadá, Estados Unidos, Francia, Italia, Japón, Reino Unido

**Emergentes (17):** Arabia Saudita, Australia, China, Corea del Sur, Egipto, Emiratos Árabes Unidos, Filipinas, India, Indonesia, Malasia, Nigeria, Rusia, Singapur, Sudáfrica, Taiwán, Turquía, Vietnam

### Indicadores

| Categoría | Indicadores |
|---|---|
| **PIB y Crecimiento** | Crecimiento real del PIB, PIB nominal (USD), PIB per cápita, PIB PPA, PIB PPA per cápita |
| **Precios y Empleo** | Inflación IPC, Desempleo, Empleo total, Población |
| **Finanzas Públicas** | Ingresos gobierno (% PIB), Gasto gobierno (% PIB), Balance fiscal (% PIB), Deuda pública bruta (% PIB) |
| **Sector Externo** | Cuenta corriente (% PIB y USD), Crecimiento de exportaciones e importaciones (total y bienes) |
| **Ahorro e Inversión** | Inversión total (% PIB), Ahorro nacional bruto (% PIB) |

### Formato del CSV maestro (`latam_weo_all.csv`)

| Columna | Descripción |
|---|---|
| `country_code` | Código ISO3 del país |
| `country_name` | Nombre en español |
| `year` | Año (desde 1980 hasta el horizonte máximo del FMI) |
| `value` | Valor numérico del indicador |
| `is_projection` | `True` si el año ≥ año de publicación del WEO (proyección FMI) |
| `indicator_code` | Código WEO del FMI |
| `indicator_description` | Descripción en español |

## API del FMI

El script `download.py` usa la API SDMX del FMI:

```
https://api.imf.org/external/sdmx/2.1/data/IMF.RES,WEO,+/{países}.{indicador}.A
```

Consideraciones:
- Sin `endPeriod` fijo — descarga todos los años disponibles
- Requests separados por grupo (LATAM, G7, Emergentes) para evitar rate-limit
- 3 segundos de pausa entre requests
- Reintentos con backoff exponencial (10s, 20s, 40s) hasta 4 intentos
- Datos históricos se re-descargan completos (el FMI los reprocesa)
