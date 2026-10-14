"""
Country summaries based on the IMF World Economic Outlook, October 2026:
"Resilience Under Strain, Urgent Choices" (published October 13, 2026).
Narrative from the report (Chapter 1, Tables 1.1 and Annex Tables 1.1.1-1.1.5);
figures and revisions vs. April 2026 from the WEO API data.

Context: the war in the Middle East drags on (Strait of Hormuz assumed to reopen in
March 2027, with prewar conditions by October 2027; oil at $95.7/bbl in 2026, +41%),
while AI-related investment acts as a positive demand shock concentrated in a few
economies. Global growth: 3.5% (2025), 3.1% (2026), 3.4% (2027).
Latin America and the Caribbean: 2.5% (2025), 2.3% (2026), 2.5% (2027).

HOW TO UPDATE (each new WEO edition)
  1. Rewrite the texts below with the new report.
  2. Set SUMMARIES_EDITION to the new edition ("YYYY-04" or "YYYY-10").
While SUMMARIES_EDITION differs from the edition in weo_meta.json, the dashboard
shows a notice and the GitHub Action opens an issue as a reminder. The key-figure
tables shown above each text always come from the data, so they never go stale.
"""

# Edición del WEO en la que se basan los textos (formato de weo_meta.json)
SUMMARIES_EDITION = "2026-10"

COUNTRY_SUMMARIES = {
    "es": {
        # ===================== LATAM =====================
        "ARG": (
            "El WEO de octubre 2026 recorta con fuerza el crecimiento de Argentina para 2026, a 2,1% "
            "(3,5% en abril), tras un repunte de 4,5% en 2025, y espera una reaceleración a 3,5% en "
            "2027 (4,0% en abril). La desinflación continúa —de 41,9% en 2025 a 32,5% en 2026 y "
            "21,2% en 2027—, aunque a un ritmo más lento que el previsto en abril (30,4% y 15,7%). "
            "La cuenta corriente pasa a un leve superávit de 0,6% del PIB en 2026, frente al déficit "
            "proyectado en abril, y la deuda pública baja a cerca de 69% del PIB. El informe cita el "
            "acuerdo comercial entre la Unión Europea y el MERCOSUR como un factor que podría mejorar "
            "las perspectivas."
        ),
        "BOL": (
            "Bolivia sigue en recesión: el PIB cae –1,6% en 2025 y –3,0% en 2026 (–3,3% en abril), y "
            "el FMI publica ahora una proyección para 2027 de –1,5%, que sería el cuarto año "
            "consecutivo de contracción. La inflación se modera a 12,7% en 2026 (20,7% en abril), "
            "pero vuelve a subir a 15,8% en 2027. Los desequilibrios fiscales son severos: el déficit "
            "supera el 9% del PIB en 2026 y la deuda pública supera el 100% del PIB. La cuenta "
            "corriente pasa a un superávit de 1,6% del PIB en 2026. Es una de las pocas economías de "
            "la región con contracción proyectada en todo el horizonte cercano."
        ),
        "BRA": (
            "El WEO de octubre 2026 eleva el crecimiento de Brasil para 2026 a 2,2% (+0,3 puntos "
            "frente a abril) y prevé una desaceleración a 1,9% en 2027, que el informe atribuye a "
            "condiciones monetarias todavía restrictivas para devolver la inflación a la meta, el "
            "retiro del apoyo fiscal y la incertidumbre global. Brasil figura entre los productores "
            "fuera del Golfo Pérsico que aumentaron su producción de petróleo y ayudaron a "
            "compensar el cierre del estrecho de Ormuz. La inflación se ubica en 4,4% en 2026 (4,0% "
            "en abril). El déficit fiscal ronda el 8% del PIB y la deuda pública sube hacia 99% del "
            "PIB en 2027. El informe también menciona lluvias en Minas Gerais que retrasaron la "
            "cosecha de café."
        ),
        "CHL": (
            "Chile registra la mayor revisión a la baja de la región: el crecimiento de 2026 cae a "
            "0,6%, frente a 2,4% proyectado en abril, antes de recuperarse a 2,6% en 2027. El informe "
            "no detalla las causas específicas para Chile; como importador neto de energía, el país "
            "enfrenta el encarecimiento del petróleo, mientras que, como exportador de cobre, figura "
            "entre las economías de materias primas que se benefician indirectamente del auge de "
            "exportaciones tecnológicas de Corea y Taiwán (Figura 1.6). La inflación de 2026 se "
            "revisa al alza a 3,7% (2,9% en abril) y el desempleo sube a 9,5%, frente a 8,1% previsto "
            "en abril. La deuda pública se mantiene moderada, en torno a 43% del PIB."
        ),
        "COL": (
            "El crecimiento de Colombia se proyecta en 2,2% en 2026 y 2,3% en 2027, ligeramente por "
            "debajo de lo previsto en abril. La inflación se revisa al alza: 6,0% en 2026 y 5,7% en "
            "2027 (5,9% y 5,2% en abril), por encima de la meta del banco central. El principal cambio "
            "es fiscal: el déficit se amplía a 6,9% del PIB en 2026 y 6,6% en 2027, frente a 5,2% y "
            "4,3% en abril, y la deuda sube a cerca de 63% del PIB en 2027. El desempleo aumenta a "
            "9,0% en 2026 y 10,0% en 2027. El informe insiste en que los países con alta deuda "
            "necesitan planes creíbles de consolidación fiscal."
        ),
        "CRI": (
            "Costa Rica crece 4,6% en 2025 y se modera a 3,3% en 2026 (3,6% en abril) y 3,5% en 2027. "
            "La inflación sigue siendo negativa en 2026 (–0,8%) antes de volver a terreno positivo, "
            "2,2%, en 2027. Según el informe, Costa Rica está entre los principales exportadores "
            "netos de hardware vinculado a la inteligencia artificial (Figura 1.5), lo que la conecta "
            "con el ciclo tecnológico que compensa parte del choque energético en otras economías. "
            "El déficit de cuenta corriente se amplía a –1,5% del PIB en 2026 y la deuda pública "
            "sube gradualmente hacia 63% del PIB."
        ),
        "CUB": (
            "Cuba no cuenta con proyecciones individuales en el WEO de octubre 2026. El informe "
            "proyecta para América Latina y el Caribe un crecimiento de 2,3% en 2026 y 2,5% en 2027, "
            "y señala que el efecto del choque energético en la región depende del balance entre "
            "exportadores de materias primas e importadores de energía. Para economías importadoras "
            "de combustibles, el escenario base supone un petróleo en torno a 96 dólares por barril "
            "en 2026 y contempla escasez de combustibles en algunas economías en desarrollo sin "
            "inventarios propios que compiten con países más ricos por los cargamentos disponibles."
        ),
        "DOM": (
            "La República Dominicana recibe una de las mayores revisiones al alza de la región: el "
            "crecimiento de 2026 sube a 4,6% (3,7% en abril), tras 2,1% en 2025, y se mantiene en "
            "4,4% en 2027. La inflación se ubica en 5,1% en 2026 y 5,3% en 2027, por encima de lo "
            "previsto en abril para 2027. El déficit de cuenta corriente se mantiene acotado, en "
            "torno a –1,5% del PIB, y la deuda pública baja a 55% del PIB en 2027. Como importador "
            "de energía, el país está expuesto al encarecimiento del petróleo; el informe señala las "
            "remesas y el turismo como factores que diferencian el desempeño entre economías emergentes."
        ),
        "ECU": (
            "Tras la contracción de –1,9% en 2024, Ecuador crece 3,7% en 2025 y el WEO de octubre 2026 "
            "eleva la proyección para 2026 a 2,7% (2,5% en abril), con 2,5% en 2027. La inflación se "
            "revisa a la baja, a 2,0% en 2026 (2,9% en abril). El superávit de cuenta corriente sigue "
            "siendo amplio, alrededor de 4,6% del PIB en 2026 y 2027. Como economía dolarizada y "
            "exportadora de petróleo fuera de la zona del conflicto, Ecuador está en el grupo que, "
            "según el informe, se beneficia de términos de intercambio favorables, con el crudo "
            "proyectado 41% más caro en 2026. El FMI no publica proyecciones fiscales ni de deuda "
            "para Ecuador desde 2026."
        ),
        "SLV": (
            "El Salvador recibe una fuerte revisión al alza: el crecimiento se proyecta en 4,5% en "
            "2026 y 4,0% en 2027, frente a 3,3% y 3,0% en abril. La inflación sigue baja, en 2,7% en "
            "2026. El déficit de cuenta corriente se amplía a –4,8% del PIB en 2026. En lo fiscal, el "
            "WEO proyecta que el déficit sube a 7,7% del PIB en 2027 y que la deuda pública vuelve a "
            "subir a 89% del PIB, frente a 82% previsto en abril. Como economía dolarizada, importadora "
            "de energía y muy dependiente de las remesas, es sensible tanto al precio de los "
            "combustibles como a la evolución de la economía estadounidense."
        ),
        "GTM": (
            "Guatemala crece 4,3% en 2025 y mantiene un ritmo sólido de 4,0% en 2026 y 3,8% en 2027, "
            "prácticamente sin cambios frente a abril. La inflación sube de 1,6% en 2025 a 3,0% en "
            "2026 y 4,1% en 2027, reflejando el encarecimiento de la energía y los alimentos. La "
            "cuenta corriente mantiene un superávit de 3,6% del PIB en 2026, mayor que el previsto en "
            "abril, y la deuda pública sigue entre las más bajas de la región, cerca de 28% del PIB. "
            "Las remesas siguen siendo un soporte clave del consumo."
        ),
        "GUY": (
            "Guyana sigue entre las economías de mayor crecimiento del mundo: el WEO de octubre 2026 "
            "eleva la proyección de 2026 a 22,3% (16,2% en abril), tras 19,3% en 2025, con 16,8% en "
            "2027. Como exportador de petróleo fuera de la zona del conflicto, Guyana está entre los "
            "países que, según el informe, se benefician de términos de intercambio favorables. El "
            "superávit de cuenta corriente llega a 31,6% del PIB en 2026. El informe recomienda que "
            "las ganancias extraordinarias por materias primas se ahorren o se destinen a inversión "
            "de alto retorno, en lugar de alimentar gasto procíclico."
        ),
        "HTI": (
            "Haití sigue en recesión: el PIB cae –2,7% en 2025 y –1,7% en 2026, y el WEO de octubre "
            "2026 proyecta ahora –0,5% para 2027, frente al leve crecimiento (+0,5%) previsto en "
            "abril. La inflación baja de 28,3% en 2025 a 21,5% en 2026 y 15,7% en 2027, aunque sigue "
            "muy elevada. El informe advierte que el alza de los precios de la energía y los alimentos "
            "tiene efectos severos sobre la pobreza y la seguridad alimentaria en las economías más "
            "vulnerables, y que la asistencia internacional puede ser necesaria para financiar "
            "transferencias focalizadas."
        ),
        "HND": (
            "Honduras crece 3,8% en 2025, 3,3% en 2026 y 3,4% en 2027 (3,7% en abril para 2027). La "
            "inflación se revisa al alza, a 5,6% en 2026 y 5,3% en 2027. La cuenta corriente pasa de "
            "un superávit de 2,4% del PIB en 2025 a un déficit de –2,0% en 2026, en línea con la "
            "mayor factura energética de los importadores de combustibles. El desempleo sube a 7,1% "
            "en 2026. Las remesas siguen siendo determinantes para el consumo y el balance externo."
        ),
        "JAM": (
            "El WEO de octubre 2026 mejora la proyección de Jamaica para 2026 a un estancamiento "
            "(0,0%), frente a la contracción de –1,2% prevista en abril, y espera una recuperación de "
            "2,4% en 2027 (3,1% en abril). La inflación sube a 5,9% en 2026. La cuenta corriente pasa "
            "de un superávit de 1,5% del PIB en 2025 a un déficit de –5,1% en 2026, y el déficit "
            "fiscal se amplía a 4,9% del PIB, mientras la deuda pública se mantiene en torno a 64% "
            "del PIB. El turismo y las remesas, que el informe destaca como fuentes de "
            "diferenciación entre economías, siguen siendo claves."
        ),
        "MEX": (
            "México crece 0,5% en 2025 y el WEO de octubre 2026 proyecta una aceleración moderada a "
            "1,5% en 2026 y 1,8% en 2027 (1,6% y 2,2% en abril). El informe atribuye la mejora al "
            "apoyo de las exportaciones —incluidas las de las cadenas de valor de la inteligencia "
            "artificial, donde México es uno de los principales exportadores netos de hardware— y a "
            "la estabilización de la inversión, aunque la incertidumbre comercial seguirá limitando "
            "la actividad. La inflación se mantiene en 3,8% en 2026. El déficit fiscal baja a 4,2% del "
            "PIB y la deuda pública ronda el 62% del PIB."
        ),
        "NIC": (
            "Nicaragua crece 4,9% en 2025 y se proyecta en 3,8% en 2026 y 2027, sin cambios frente a "
            "abril. La inflación se ubica en 3,5% en 2026. Nicaragua mantiene un amplio superávit de "
            "cuenta corriente (6,4% del PIB en 2026) y un superávit fiscal, ahora mayor que el "
            "previsto en abril (2,3% del PIB en 2026), lo que permite que la deuda pública siga "
            "bajando, hasta 29% del PIB en 2027. Las remesas siguen siendo un soporte importante de "
            "la demanda interna."
        ),
        "PAN": (
            "Panamá recibe una revisión al alza importante: el crecimiento de 2026 sube a 5,0% (3,8% "
            "en abril), tras 4,4% en 2025, y se modera a 4,2% en 2027. La inflación sigue baja, en "
            "1,8% en 2026, tras una ligera deflación en 2025. El desempleo baja de 10,4% en 2025 a "
            "9,1% en 2026. El déficit fiscal se reduce gradualmente, a 3,4% del PIB en 2026, y la "
            "deuda se mantiene cerca de 56% del PIB. Como economía dolarizada y centro logístico, "
            "Panamá está expuesta a la reconfiguración de las rutas del comercio mundial."
        ),
        "PRY": (
            "Paraguay crece 6,6% en 2025, uno de los ritmos más altos de la región, y el WEO de "
            "octubre 2026 eleva sus proyecciones a 4,5% en 2026 y 4,0% en 2027 (4,2% y 3,5% en "
            "abril). La inflación se mantiene cerca de 3%. El déficit fiscal se amplía a 3,1% del PIB "
            "en 2026 y 2027, frente a 1,3% previsto en abril, aunque la deuda pública sigue moderada, "
            "en torno a 37% del PIB. El informe menciona el acuerdo entre la Unión Europea y el "
            "MERCOSUR como un factor que podría mejorar las perspectivas comerciales."
        ),
        "PER": (
            "Perú crece 3,4% en 2025 y el WEO de octubre 2026 eleva sus proyecciones a 3,0% en 2026 y "
            "2,9% en 2027 (2,8% en abril para ambos años). Como exportador de cobre, Perú figura "
            "entre las economías de materias primas que se benefician de forma indirecta del "
            "auge de exportaciones tecnológicas de Corea y Taiwán (Figura 1.6). La inflación sube "
            "temporalmente a 3,8% en 2026 (2,5% en abril) antes de volver a 2,6% en 2027. El "
            "superávit de cuenta corriente llega a 4,0% del PIB y la deuda pública baja a cerca de "
            "29% del PIB."
        ),
        "URY": (
            "El WEO de octubre 2026 recorta el crecimiento de Uruguay a 1,3% en 2026 (1,8% en abril) "
            "y a 2,4% en 2027 (2,6% en abril), tras 1,8% en 2025. La inflación se mantiene entre 4,0% "
            "y 4,5%. El déficit fiscal se amplía a 4,1% del PIB en 2026 y la deuda pública sube a "
            "cerca de 69% del PIB en 2027. El desempleo baja a 7,5%. El informe menciona el acuerdo "
            "entre la Unión Europea y el MERCOSUR como un posible impulso al comercio de la región."
        ),
        "VEN": (
            "Venezuela crece 9,0% en 2025 y el WEO de octubre 2026 eleva sus proyecciones a 5,0% en "
            "2026 y 7,0% en 2027 (4,0% y 6,0% en abril). El informe destaca que Venezuela está entre "
            "los productores que aumentaron su extracción de petróleo fuera del Golfo Pérsico, "
            "ayudando a compensar el cierre del estrecho de Ormuz. Sin embargo, la inflación se "
            "dispara a 467,9% en 2026 (387,4% en abril) y se proyecta en 174,7% en 2027; por eso el "
            "FMI la excluye de los agregados regionales de inflación. La cuenta corriente pasa a "
            "déficit (–1,0% del PIB en 2026), frente al superávit previsto en abril."
        ),
        "BLZ": (
            "Belice crece 2,6% en 2025 y se modera a 1,9% en 2026 (2,2% en abril) y 2,0% en 2027. La "
            "inflación sube a 3,5% en 2026. El déficit de cuenta corriente se amplía a –5,2% del PIB y "
            "el déficit fiscal se duplica frente a lo previsto en abril, a 3,0% del PIB en 2026, con "
            "una deuda pública cercana a 65% del PIB. Como pequeña economía importadora de energía y "
            "dependiente del turismo, Belice es sensible al encarecimiento de los combustibles y a "
            "la demanda externa."
        ),
        "SUR": (
            "Surinam crece 4,0% en 2025 y 2026 y 4,1% en 2027, en línea con lo previsto en abril. La "
            "inflación vuelve a subir, a 10,5% en 2026 y 12,4% en 2027. El déficit de cuenta "
            "corriente es excepcionalmente alto, alrededor de –51% del PIB en 2026-2027, mayor que en "
            "abril. La deuda pública mantiene su trayectoria descendente, de 97% del PIB en 2025 a "
            "72% en 2027, y el desempleo baja gradualmente hasta 8,0%."
        ),
        "TTO": (
            "El WEO de octubre 2026 recorta el crecimiento de Trinidad y Tobago a 0,2% en 2026 (0,8% "
            "en abril) y a 2,2% en 2027 (3,0% en abril), tras una contracción de –0,5% en 2025. Como "
            "exportador de energía, el país se beneficia de mejores términos de intercambio: el "
            "superávit de cuenta corriente sube a 5,6% del PIB en 2026 y 8,1% en 2027. La inflación "
            "sigue baja, cerca de 1%. El déficit fiscal se reduce gradualmente, aunque la deuda "
            "pública se mantiene cerca de 84% del PIB."
        ),
        # ===================== G7 =====================
        "USA": (
            "Estados Unidos crece 2,3% en 2026 y 2027, sin cambios para 2026 y +0,2 puntos para 2027 "
            "frente a abril. El informe atribuye la fortaleza al consumo privado, la política fiscal, "
            "las condiciones financieras holgadas y la inversión empresarial vinculada a la tecnología "
            "y la inteligencia artificial; como exportador neto de energía, el impacto directo de la "
            "guerra es limitado. La inflación sube a 3,6% en 2026 y la inflación subyacente volvería "
            "a 2% recién a mediados de 2028. El déficit fiscal ronda el 8,5% del PIB y la deuda supera "
            "el 126% del PIB; el FMI pide una consolidación fiscal creíble. Los aranceles de la "
            "Sección 122 fueron reemplazados en gran parte por nuevos aranceles bajo la Sección 301."
        ),
        "JPN": (
            "El crecimiento de Japón se desacelera de 1,2% en 2025 a 0,7% en 2026 y se estabiliza en "
            "ese nivel en 2027. Según el informe, las medidas de apoyo fiscal amortiguan en parte el "
            "impacto del encarecimiento de la energía, y la política monetaria se normaliza "
            "gradualmente hacia una tasa neutral. El PIB del segundo trimestre fue mejor de lo "
            "esperado. La inflación baja a 2,0% en 2026 y sube a 2,6% en 2027; la subyacente "
            "volvería a 2% a fines de 2027. El informe menciona una intervención cambiaria conjunta "
            "entre Japón y Estados Unidos en medio de la volatilidad de las monedas asiáticas."
        ),
        "DEU": (
            "Alemania recibe una de las mayores revisiones al alza entre las economías avanzadas: "
            "crece 1,3% en 2026 (+0,5 puntos frente a abril), tras 0,2% en 2025, y 1,1% en 2027. La "
            "inflación sube a 2,7% en 2026 y 3,1% en 2027. El déficit fiscal se amplía a 4,3% del PIB "
            "en 2026 y 4,6% en 2027, y la deuda pública sube hacia 67% del PIB. Para la zona euro en "
            "su conjunto, el informe mantiene el crecimiento en 1,1% en 2026, frenado por los altos "
            "precios de la energía y la débil confianza del consumidor; los inventarios de gas siguen "
            "bajo lo normal en partes de Europa."
        ),
        "GBR": (
            "El Reino Unido crece 1,3% en 2026, una revisión al alza de 0,5 puntos frente a abril, y "
            "se modera a 1,2% en 2027, ya que los altos precios de la energía y las tasas de interés "
            "de largo plazo pesan sobre el consumo y la inversión. La inflación se mantiene en 3,3% en "
            "2026 y baja a 2,8% en 2027; la subyacente volvería a 2% a fines de 2027. El déficit fiscal "
            "se reduce de 5,3% a 3,8% del PIB en 2026, con una deuda pública estable cerca de 102% del "
            "PIB."
        ),
        "FRA": (
            "Francia recibe la mayor revisión a la baja del G7: crece apenas 0,4% en 2026 (–0,5 "
            "puntos frente a abril) y 0,7% en 2027. La inflación sube a 2,4% en 2026. El desempleo "
            "aumenta a 8,4% y el déficit fiscal se mantiene por encima de 5% del PIB, con una deuda "
            "pública que supera el 120% del PIB en 2027. El informe advierte que, con deuda alta y "
            "tasas de largo plazo en aumento, las economías avanzadas están más expuestas a cambios "
            "bruscos en las condiciones financieras."
        ),
        "ITA": (
            "Italia crece 0,8% en 2026 (+0,3 puntos frente a abril) y 0,6% en 2027. La inflación sube "
            "a 3,3% en 2026, por el encarecimiento de la energía, y baja a 2,8% en 2027. El déficit "
            "fiscal se mantiene por debajo de 3% del PIB, pero la deuda pública sigue cerca de 138% "
            "del PIB, de las más altas entre las economías avanzadas. El desempleo baja a 5,6%. El "
            "informe destaca los riesgos de refinanciamiento en países con deuda elevada en un "
            "contexto de tasas de largo plazo en máximos de varias décadas."
        ),
        "CAN": (
            "El crecimiento de Canadá se modera a 1,1% en 2026 (–0,4 puntos frente a abril) y sube a "
            "1,7% en 2027. Según el informe, las políticas de apoyo y los efectos positivos de los "
            "términos de intercambio, como exportador de energía, compensan en parte un menor impulso "
            "de la actividad y la elevada incertidumbre comercial. La inflación sube a 2,8% en 2026. "
            "El desempleo baja de 6,9% en 2025 a 6,5% en 2026, y la deuda pública bruta ronda el 115% "
            "del PIB."
        ),
        # ===================== EMERGENTES =====================
        "AUS": (
            "Australia crece 1,9% en 2026 y 1,6% en 2027, prácticamente sin cambios frente a abril. "
            "La inflación sube a 3,9% en 2026 y baja a 3,1% en 2027. Como exportador de energía y "
            "materias primas, Australia aparece en el informe entre las economías que se benefician "
            "indirectamente del auge de exportaciones tecnológicas de Corea y Taiwán (Figura 1.6). "
            "El déficit fiscal se amplía a 3,2% del PIB en 2026, más que lo previsto en abril, y la "
            "deuda pública sube levemente, a 53% del PIB."
        ),
        "CHN": (
            "El crecimiento de China se desacelera de 5,0% en 2025 a 4,5% en 2026 y 4,0% en 2027. El "
            "informe atribuye la desaceleración a los mayores precios del petróleo, la incertidumbre "
            "prolongada y obstáculos estructurales —consumo débil y tensiones en el sector "
            "inmobiliario—; el apoyo de la política económica evitaría una caída mayor. China redujo "
            "23% sus importaciones de crudo entre marzo y junio de 2026, ayudando a absorber el "
            "choque petrolero. Junto con Estados Unidos concentra más del 75% de las importaciones "
            "netas de hardware para IA. Su superávit de cuenta corriente sube a 4,0% del PIB en 2026 y "
            "la deuda pública supera el 100% del PIB; el FMI recomienda reequilibrar hacia el consumo."
        ),
        "IND": (
            "India sigue entre las grandes economías de mayor crecimiento: el WEO de octubre 2026 eleva "
            "su proyección a 7,0% para el año fiscal 2026/27 (+0,5 puntos frente a abril) y 7,0% para "
            "2027/28 (7,4% en 2026 en año calendario). El informe lo atribuye a la demanda interna "
            "resiliente y al dinamismo de los servicios, pese al encarecimiento del petróleo. India "
            "también destaca por las revisiones al alza de su crecimiento de mediano plazo y es la "
            "excepción entre las mayores economías, que en su mayoría necesitarían un ajuste fiscal "
            "mayor al previsto para estabilizar su deuda. "
            "La inflación sube a 5,0% en 2026."
        ),
        "IDN": (
            "Indonesia mantiene un crecimiento estable de 5,1% en 2025, 2026 y 2027, levemente por "
            "encima de lo previsto en abril. La inflación sube a 3,3% en 2026 y baja a 2,8% en 2027. "
            "El déficit de cuenta corriente se amplía a –1,6% del PIB en 2026. El déficit fiscal se "
            "mantiene cerca de 3% del PIB y la deuda pública en torno a 42% del PIB. "
            "Para el grupo ASEAN-5, el informe proyecta un crecimiento de 4,4% en 2026, apoyado por "
            "la actividad de centros de datos y el ciclo tecnológico."
        ),
        "RUS": (
            "Rusia crece apenas 1,0% en 2025 y 0,9% en 2026 y 2027 (–0,2 puntos frente a abril). "
            "Según el informe, los mayores precios de las materias primas dan cierto apoyo a la "
            "actividad, pese a la caída de las exportaciones petroleras por los ataques a la "
            "infraestructura energética rusa, en tierra y en el mar Negro, que redujeron en especial "
            "la exportación de diésel y otros refinados. La inflación baja de 8,7% en 2025 a 6,1% en "
            "2026. El déficit fiscal se amplía a 3,2% del PIB y la deuda pública, aunque baja, sube "
            "hacia 22% del PIB en 2027."
        ),
        "SAU": (
            "Arabia Saudita sufre una de las mayores revisiones a la baja: el PIB se contrae –3,3% en "
            "2026 (+3,1% en abril) y rebota 7,9% en 2027. El informe explica que el país está algo "
            "menos afectado que otros productores del Golfo, como Bahréin, Irak, Kuwait o Qatar —que "
            "sufren contracciones de dos dígitos—, gracias a sus rutas de exportación más "
            "diversificadas. El supuesto base es que el estrecho de Ormuz reabre en marzo de 2027. El "
            "déficit fiscal se amplía a 6,5% del PIB en 2026 y la deuda pública sube a 35% del PIB."
        ),
        "ZAF": (
            "Sudáfrica crece 1,1% en 2025, 1,0% en 2026 y 1,3% en 2027, sin cambios frente a abril. "
            "Según el informe, las perspectivas se mantienen estables en el corto plazo y mejorarían "
            "gradualmente en el mediano plazo, apoyadas en marcos de política más sólidos y reformas "
            "estructurales en curso. La inflación sube a 4,4% en 2026. El desempleo sigue siendo muy "
            "alto, en torno a 33%. El déficit fiscal baja a 4,4% del PIB en 2026 y la deuda pública "
            "se estabiliza cerca de 78% del PIB."
        ),
        "KOR": (
            "Corea del Sur recibe una fuerte revisión al alza: crece 3,3% en 2026 (1,9% en abril) y "
            "2,8% en 2027, impulsada por la fuerte demanda externa de semiconductores, que, según el "
            "informe, supera el impacto negativo de la guerra. Junto con Taiwán, Corea concentra el "
            "62% del comercio neto de hardware para inteligencia artificial. El superávit de cuenta "
            "corriente se dispara a 18,8% del PIB en 2026. El informe advierte sobre episodios de "
            "volatilidad en las acciones tecnológicas coreanas, expuestas a una posible corrección "
            "si se revisan las expectativas sobre la IA."
        ),
        "TUR": (
            "Turquía crece 2,7% en 2026 (–0,7 puntos frente a abril) y 3,6% en 2027. Como importador "
            "de energía con alta dependencia de los combustibles fósiles, enfrenta el choque "
            "energético que, según el informe, debilita las perspectivas de Europa emergente. La "
            "inflación sigue alta y se revisa al alza: 31,2% en 2026 y 26,5% en 2027 (28,6% y 21,4% "
            "en abril). El déficit de cuenta corriente se amplía a –2,9% del PIB en 2026, mientras la "
            "deuda pública se mantiene baja, cerca de 23% del PIB."
        ),
        "TWN": (
            "Taiwán es uno de los grandes beneficiarios del ciclo de inversión en inteligencia "
            "artificial: crece 8,8% en 2025 y 10,7% en 2026 (5,2% en abril), antes de moderarse a "
            "4,3% en 2027. Junto con Corea, concentra el 62% del comercio neto de hardware para IA, y "
            "sus exportaciones generan efectos de arrastre para exportadores de materias primas y "
            "centros manufactureros de Asia. El superávit de cuenta corriente sube a 22% del PIB en "
            "2026. La inflación se mantiene cerca de 2% y la deuda pública baja a 21% del PIB."
        ),
        "SGP": (
            "Singapur crece 5,0% en 2025 y 2026, una revisión de +1,5 puntos para 2026 frente a abril, "
            "y se modera a 3,0% en 2027. El informe destaca que varias economías del sudeste asiático "
            "se benefician de la actividad de centros de datos y del auge del ciclo tecnológico "
            "global. La inflación sube a 2,3% en 2026. Singapur mantiene un superávit de cuenta "
            "corriente cercano a 17% del PIB y un superávit fiscal de 3,7% del PIB."
        ),
        "ARE": (
            "Los Emiratos Árabes Unidos pasan de crecer 6,2% en 2025 a contraerse –3,9% en 2026 "
            "(+3,1% en abril), antes de rebotar 7,7% en 2027 cuando se normalicen la producción, las "
            "exportaciones y la logística. El informe vincula la caída de los productores del Golfo "
            "a un cierre del estrecho de Ormuz más prolongado que el supuesto en abril. La inflación "
            "sube a 4,5% en 2026. El superávit de cuenta corriente baja de 13,3% a 4,8% del PIB y el "
            "superávit fiscal se reduce a 1,5% del PIB."
        ),
        "PHL": (
            "Filipinas recibe una revisión a la baja: el crecimiento cae a 3,4% en 2026 (4,1% en "
            "abril) y se recupera a 5,1% en 2027. Como importador de energía, enfrenta el "
            "encarecimiento del petróleo: la inflación sube a 5,6% en 2026 (4,3% en abril). El "
            "desempleo aumenta a 5,4% y el déficit de cuenta corriente se amplía a –4,8% del PIB. "
            "Según el informe, Filipinas está entre los principales exportadores netos de hardware "
            "para IA, lo que compensa en parte el choque energético."
        ),
        "VNM": (
            "Vietnam recibe una fuerte revisión al alza: crece 8,4% en 2026 (7,1% en abril) y 7,5% en "
            "2027, tras 8,0% en 2025. Según el informe, está entre los principales exportadores netos "
            "de hardware para inteligencia artificial y entre las economías del sudeste asiático que "
            "se benefician de la actividad de centros de datos y del ciclo tecnológico. La inflación "
            "se ubica en 4,7% en 2026. El superávit de cuenta corriente baja de 6,7% a 0,3% del PIB en "
            "2026, y la deuda pública sigue baja, cerca de 28% del PIB."
        ),
        "MYS": (
            "Malasia crece 5,2% en 2025 y 2026 (4,7% en abril para 2026) y 4,6% en 2027. Junto con "
            "Corea, Tailandia y Taiwán, es uno de los cuatro mayores exportadores de hardware para "
            "inteligencia artificial en relación con su PIB, según el informe, lo que le permite "
            "beneficiarse del auge tecnológico. La inflación se mantiene baja, en 2,2% en 2026. El "
            "superávit de cuenta corriente sube a 2,1% del PIB y la deuda pública ronda el 69% del PIB."
        ),
        "EGY": (
            "Egipto crece 4,4% en 2025 y el WEO de octubre 2026 eleva su proyección a 5,1% en 2026 "
            "(4,2% en abril) y 4,7% en 2027. Según el informe, los importadores de materias primas de "
            "Oriente Medio y Norte de África se mantendrían relativamente resilientes frente al choque "
            "de términos de intercambio por el encarecimiento de la energía y los alimentos. La "
            "inflación sigue desacelerándose, a 13,3% en 2026, aunque repunta a 14,8% en 2027. El "
            "déficit fiscal sube a 11,4% del PIB en 2026 y la deuda pública baja a 84% del PIB."
        ),
        "NGA": (
            "Nigeria crece 4,0% en 2025, 4,2% en 2026 y 4,3% en 2027, levemente por encima de lo "
            "previsto en abril. Según el informe, el país se apoya en una mejor estabilidad "
            "macroeconómica y en términos de intercambio favorables como exportador de petróleo, "
            "aunque el alza de los precios de bienes esenciales agravaría la pobreza y la inseguridad "
            "alimentaria. La inflación sigue bajando, de 23,0% en 2025 a 15,6% en 2026. El superávit "
            "de cuenta corriente sube a 7,0% del PIB en 2026 y la deuda pública baja a 35% del PIB."
        ),
    },
    "en": {
        # ===================== LATAM =====================
        "ARG": (
            "The October 2026 WEO sharply cuts Argentina's 2026 growth to 2.1% (3.5% in April), "
            "following a 4.5% rebound in 2025, and expects growth to pick up to 3.5% in 2027 (4.0% in "
            "April). Disinflation continues—from 41.9% in 2025 to 32.5% in 2026 and 21.2% in 2027—"
            "though more slowly than projected in April (30.4% and 15.7%). The current account turns "
            "to a small surplus of 0.6% of GDP in 2026, versus the deficit projected in April, and "
            "public debt falls to about 69% of GDP. The report cites the EU–MERCOSUR trade agreement "
            "as a factor that could improve the outlook."
        ),
        "BOL": (
            "Bolivia remains in recession: GDP falls -1.6% in 2025 and -3.0% in 2026 (-3.3% in April), "
            "and the IMF now publishes a 2027 projection of -1.5%, which would be the fourth "
            "consecutive year of contraction. Inflation eases to 12.7% in 2026 (20.7% in April) but "
            "rises again to 15.8% in 2027. Fiscal imbalances are severe: the deficit exceeds 9% of "
            "GDP in 2026 and public debt rises above 100% of GDP. The current account turns to a "
            "surplus of 1.6% of GDP in 2026. Bolivia is one of the few economies in the region with "
            "a contraction projected throughout the near-term horizon."
        ),
        "BRA": (
            "The October 2026 WEO raises Brazil's 2026 growth to 2.2% (+0.3 points vs. April) and "
            "projects a slowdown to 1.9% in 2027, which the report attributes to still-restrictive "
            "monetary conditions aimed at returning inflation to target, the withdrawal of fiscal "
            "support, and global uncertainty. Brazil is among the producers outside the Persian Gulf "
            "that increased oil output and helped offset the closure of the Strait of Hormuz. "
            "Inflation stands at 4.4% in 2026 (4.0% in April). The fiscal deficit is around 8% of GDP "
            "and public debt rises toward 99% of GDP in 2027. The report also notes heavy rainfall "
            "in Minas Gerais that delayed the coffee harvest."
        ),
        "CHL": (
            "Chile has the largest downward revision in the region: 2026 growth falls to 0.6%, versus "
            "2.4% projected in April, before recovering to 2.6% in 2027. The report does not detail "
            "Chile-specific causes; as a net energy importer, the country faces higher oil prices, "
            "while as a copper exporter it is among the commodity economies that benefit indirectly "
            "from the boom in technology exports from Korea and Taiwan (Figure 1.6). Inflation for "
            "2026 is revised up to 3.7% (2.9% in April) and unemployment rises to 9.5%, versus 8.1% "
            "projected in April. Public debt remains moderate, around 43% of GDP."
        ),
        "COL": (
            "Colombia's growth is projected at 2.2% in 2026 and 2.3% in 2027, slightly below April. "
            "Inflation is revised up: 6.0% in 2026 and 5.7% in 2027 (5.9% and 5.2% in April), above "
            "the central bank's target. The main change is fiscal: the deficit widens to 6.9% of GDP "
            "in 2026 and 6.6% in 2027, versus 5.2% and 4.3% in April, and debt rises to about 63% of "
            "GDP in 2027. Unemployment increases to 9.0% in 2026 and 10.0% in 2027. The report "
            "stresses that high-debt countries need credible fiscal consolidation plans."
        ),
        "CRI": (
            "Costa Rica grows 4.6% in 2025, moderating to 3.3% in 2026 (3.6% in April) and 3.5% in "
            "2027. Inflation remains negative in 2026 (-0.8%) before turning positive at 2.2% in "
            "2027. According to the report, Costa Rica is among the leading net exporters of "
            "AI-related hardware (Figure 1.5), linking it to the technology cycle that offsets part "
            "of the energy shock elsewhere. The current account deficit widens to -1.5% of GDP in "
            "2026, and public debt rises gradually toward 63% of GDP."
        ),
        "CUB": (
            "Cuba has no individual projections in the October 2026 WEO. The report projects growth "
            "for Latin America and the Caribbean of 2.3% in 2026 and 2.5% in 2027, noting that the "
            "impact of the energy shock on the region depends on the balance between commodity "
            "exporters and energy importers. For fuel-importing economies, the baseline assumes oil "
            "at around $96 a barrel in 2026 and envisages fuel shortages in some developing "
            "economies without their own stocks that compete with wealthier countries for available "
            "cargoes."
        ),
        "DOM": (
            "The Dominican Republic receives one of the largest upward revisions in the region: 2026 "
            "growth rises to 4.6% (3.7% in April), after 2.1% in 2025, and stays at 4.4% in 2027. "
            "Inflation stands at 5.1% in 2026 and 5.3% in 2027, above April's projection for 2027. "
            "The current account deficit remains contained at around -1.5% of GDP, and public debt "
            "falls to 55% of GDP in 2027. As an energy importer, the country is exposed to higher "
            "oil prices; the report highlights remittances and tourism as factors that differentiate "
            "performance across emerging economies."
        ),
        "ECU": (
            "After a -1.9% contraction in 2024, Ecuador grows 3.7% in 2025, and the October 2026 WEO "
            "raises its 2026 projection to 2.7% (2.5% in April), with 2.5% in 2027. Inflation is "
            "revised down to 2.0% in 2026 (2.9% in April). The current account surplus remains "
            "large, around 4.6% of GDP in 2026 and 2027. As a dollarized oil exporter outside the "
            "conflict zone, Ecuador is in the group that, according to the report, benefits from "
            "favorable terms of trade, with crude oil projected 41% more expensive in 2026. The IMF "
            "does not publish fiscal or debt projections for Ecuador from 2026 onward."
        ),
        "SLV": (
            "El Salvador receives a strong upward revision: growth is projected at 4.5% in 2026 and "
            "4.0% in 2027, versus 3.3% and 3.0% in April. Inflation remains low at 2.7% in 2026. The "
            "current account deficit widens to -4.8% of GDP in 2026. On the fiscal side, the WEO "
            "projects the deficit rising to 7.7% of GDP in 2027 and public debt climbing back to 89% "
            "of GDP, versus 82% projected in April. As a dollarized, energy-importing economy heavily "
            "reliant on remittances, it is sensitive both to fuel prices and to the US economy."
        ),
        "GTM": (
            "Guatemala grows 4.3% in 2025 and maintains a solid pace of 4.0% in 2026 and 3.8% in "
            "2027, virtually unchanged from April. Inflation rises from 1.6% in 2025 to 3.0% in 2026 "
            "and 4.1% in 2027, reflecting higher energy and food prices. The current account surplus "
            "stands at 3.6% of GDP in 2026, larger than projected in April, and public debt remains "
            "among the lowest in the region, near 28% of GDP. Remittances continue to be a key "
            "support for consumption."
        ),
        "GUY": (
            "Guyana remains among the world's fastest-growing economies: the October 2026 WEO raises its 2026 "
            "projection to 22.3% (16.2% in April), after 19.3% in 2025, with 16.8% in 2027. As an oil "
            "exporter outside the conflict zone, Guyana is among the countries that, according to "
            "the report, benefit from favorable terms of trade. The current account surplus reaches "
            "31.6% of GDP in 2026. The report recommends that commodity windfalls be saved or "
            "channeled into high-return investment rather than fuel procyclical spending."
        ),
        "HTI": (
            "Haiti remains in recession: GDP falls -2.7% in 2025 and -1.7% in 2026, and the October "
            "2026 WEO now projects -0.5% for 2027, versus the slight growth (+0.5%) expected in "
            "April. Inflation declines from 28.3% in 2025 to 21.5% in 2026 and 15.7% in 2027, though "
            "it remains very high. The report warns that higher energy and food prices have severe "
            "effects on poverty and food security in the most vulnerable economies, and that "
            "international assistance may be needed to finance targeted transfers."
        ),
        "HND": (
            "Honduras grows 3.8% in 2025, 3.3% in 2026, and 3.4% in 2027 (3.7% in April for 2027). "
            "Inflation is revised up to 5.6% in 2026 and 5.3% in 2027. The current account swings "
            "from a surplus of 2.4% of GDP in 2025 to a deficit of -2.0% in 2026, in line with the "
            "higher energy bill of fuel importers. Unemployment rises to 7.1% in 2026. Remittances "
            "remain decisive for consumption and the external balance."
        ),
        "JAM": (
            "The October 2026 WEO improves Jamaica's 2026 outlook to stagnation (0.0%), versus the "
            "-1.2% contraction projected in April, and expects a 2.4% recovery in 2027 (3.1% in "
            "April). Inflation rises to 5.9% in 2026. The current account swings from a surplus of "
            "1.5% of GDP in 2025 to a deficit of -5.1% in 2026, and the fiscal deficit widens to 4.9% "
            "of GDP, while public debt stays around 64% of GDP. Tourism and remittances, which the "
            "report highlights as sources of differentiation across economies, remain key."
        ),
        "MEX": (
            "Mexico grows 0.5% in 2025, and the October 2026 WEO projects a moderate acceleration to "
            "1.5% in 2026 and 1.8% in 2027 (1.6% and 2.2% in April). The report attributes the "
            "improvement to support from exports—including through AI value chains, where Mexico is "
            "one of the leading net exporters of hardware—and stabilizing investment, although trade "
            "and other uncertainties will continue to constrain activity. Inflation stays at 3.8% in "
            "2026. The fiscal deficit falls to 4.2% of GDP and public debt is around 62% of GDP."
        ),
        "NIC": (
            "Nicaragua grows 4.9% in 2025 and is projected at 3.8% in 2026 and 2027, unchanged from "
            "April. Inflation stands at 3.5% in 2026. Nicaragua maintains a large current account "
            "surplus (6.4% of GDP in 2026) and a fiscal surplus, now larger than projected in April "
            "(2.3% of GDP in 2026), allowing public debt to keep falling to 29% of GDP in 2027. "
            "Remittances remain an important support for domestic demand."
        ),
        "PAN": (
            "Panama receives a significant upward revision: 2026 growth rises to 5.0% (3.8% in "
            "April), after 4.4% in 2025, moderating to 4.2% in 2027. Inflation remains low at 1.8% "
            "in 2026, after slight deflation in 2025. Unemployment falls from 10.4% in 2025 to 9.1% "
            "in 2026. The fiscal deficit narrows gradually to 3.4% of GDP in 2026, and debt stays "
            "near 56% of GDP. As a dollarized economy and logistics hub, Panama is exposed to the "
            "reconfiguration of global trade routes."
        ),
        "PRY": (
            "Paraguay grows 6.6% in 2025, one of the fastest rates in the region, and the October "
            "2026 WEO raises its projections to 4.5% in 2026 and 4.0% in 2027 (4.2% and 3.5% in "
            "April). Inflation stays near 3%. The fiscal deficit widens to 3.1% of GDP in 2026 and "
            "2027, versus 1.3% projected in April, though public debt remains moderate at around 37% "
            "of GDP. The report mentions the EU–MERCOSUR agreement as a factor that could improve "
            "trade prospects."
        ),
        "PER": (
            "Peru grows 3.4% in 2025, and the October 2026 WEO raises its projections to 3.0% in 2026 "
            "and 2.9% in 2027 (2.8% in April for both years). As a copper exporter, Peru is among "
            "the commodity economies that benefit indirectly from the boom in technology "
            "exports from Korea and Taiwan (Figure 1.6). Inflation rises temporarily to 3.8% in 2026 "
            "(2.5% in April) before returning to 2.6% in 2027. The current account surplus reaches "
            "4.0% of GDP and public debt falls to about 29% of GDP."
        ),
        "URY": (
            "The October 2026 WEO cuts Uruguay's growth to 1.3% in 2026 (1.8% in April) and 2.4% in "
            "2027 (2.6% in April), after 1.8% in 2025. Inflation stays between 4.0% and 4.5%. The "
            "fiscal deficit widens to 4.1% of GDP in 2026 and public debt rises to about 69% of GDP "
            "in 2027. Unemployment falls to 7.5%. The report mentions the EU–MERCOSUR agreement as "
            "a potential boost to trade in the region."
        ),
        "VEN": (
            "Venezuela grows 9.0% in 2025, and the October 2026 WEO raises its projections to 5.0% "
            "in 2026 and 7.0% in 2027 (4.0% and 6.0% in April). The report highlights Venezuela as "
            "one of the producers that increased oil output outside the Persian Gulf, helping offset "
            "the closure of the Strait of Hormuz. However, inflation soars to 467.9% in 2026 (387.4% "
            "in April) and is projected at 174.7% in 2027, which is why the IMF excludes it from "
            "regional inflation aggregates. The current account turns to a deficit (-1.0% of GDP in "
            "2026), versus the surplus projected in April."
        ),
        "BLZ": (
            "Belize grows 2.6% in 2025, moderating to 1.9% in 2026 (2.2% in April) and 2.0% in 2027. "
            "Inflation rises to 3.5% in 2026. The current account deficit widens to -5.2% of GDP and "
            "the fiscal deficit doubles relative to April's projection, to 3.0% of GDP in 2026, with "
            "public debt near 65% of GDP. As a small energy-importing, tourism-dependent economy, "
            "Belize is sensitive to higher fuel prices and to external demand."
        ),
        "SUR": (
            "Suriname grows 4.0% in 2025 and 2026 and 4.1% in 2027, in line with April. Inflation "
            "rises again to 10.5% in 2026 and 12.4% in 2027. The current account deficit is "
            "exceptionally large, around -51% of GDP in 2026-27, wider than in April. Public debt "
            "continues its downward path, from 97% of GDP in 2025 to 72% in 2027, and unemployment "
            "declines gradually to 8.0%."
        ),
        "TTO": (
            "The October 2026 WEO cuts Trinidad and Tobago's growth to 0.2% in 2026 (0.8% in April) "
            "and 2.2% in 2027 (3.0% in April), after a -0.5% contraction in 2025. As an energy "
            "exporter, the country benefits from improved terms of trade: the current account "
            "surplus rises to 5.6% of GDP in 2026 and 8.1% in 2027. Inflation remains low, near 1%. "
            "The fiscal deficit narrows gradually, though public debt stays near 84% of GDP."
        ),
        # ===================== G7 =====================
        "USA": (
            "The United States grows 2.3% in 2026 and 2027, unchanged for 2026 and +0.2 points for "
            "2027 versus April. The report attributes this strength to private consumption, fiscal "
            "policy, accommodative financial conditions, and technology- and AI-related business "
            "investment; as a net energy exporter, the direct impact of the war is limited. "
            "Inflation rises to 3.6% in 2026, and core inflation would return to 2% only by mid-2028. "
            "The fiscal deficit is around 8.5% of GDP and debt exceeds 126% of GDP; the IMF calls for "
            "credible fiscal consolidation. Section 122 tariffs have been largely replaced by new "
            "tariffs under Section 301."
        ),
        "JPN": (
            "Japan's growth slows from 1.2% in 2025 to 0.7% in 2026 and stabilizes at that level in "
            "2027. According to the report, fiscal support measures partly cushion the impact of "
            "higher energy prices, and monetary policy gradually normalizes toward a neutral rate. "
            "Second-quarter GDP was better than expected. Inflation falls to 2.0% in 2026 and rises "
            "to 2.6% in 2027; core inflation would return to 2% by end-2027. The report mentions a "
            "joint Japan–US foreign exchange intervention amid volatility in Asian currencies."
        ),
        "DEU": (
            "Germany receives one of the largest upward revisions among advanced economies: it grows "
            "1.3% in 2026 (+0.5 points vs. April), after 0.2% in 2025, and 1.1% in 2027. Inflation "
            "rises to 2.7% in 2026 and 3.1% in 2027. The fiscal deficit widens to 4.3% of GDP in 2026 "
            "and 4.6% in 2027, and public debt rises toward 67% of GDP. For the euro area as a whole, "
            "the report keeps growth at 1.1% in 2026, held back by high energy prices and weak "
            "consumer confidence; gas inventories remain below seasonal norms in parts of Europe."
        ),
        "GBR": (
            "The United Kingdom grows 1.3% in 2026, a 0.5-point upward revision from April, edging "
            "down to 1.2% in 2027 as higher energy prices and long-term interest rates weigh on "
            "consumption and investment. Inflation stays at 3.3% in 2026 and eases to 2.8% in 2027; "
            "core inflation would return to 2% by end-2027. The fiscal deficit narrows from 5.3% to "
            "3.8% of GDP in 2026, with public debt stable near 102% of GDP."
        ),
        "FRA": (
            "France receives the largest downward revision in the G7: it grows just 0.4% in 2026 "
            "(-0.5 points vs. April) and 0.7% in 2027. Inflation rises to 2.4% in 2026. Unemployment "
            "increases to 8.4% and the fiscal deficit remains above 5% of GDP, with public debt "
            "exceeding 120% of GDP in 2027. The report warns that, with high debt and rising "
            "long-term rates, advanced economies are more exposed to abrupt changes in financial "
            "conditions."
        ),
        "ITA": (
            "Italy grows 0.8% in 2026 (+0.3 points vs. April) and 0.6% in 2027. Inflation rises to "
            "3.3% in 2026 on higher energy costs and eases to 2.8% in 2027. The fiscal deficit stays "
            "below 3% of GDP, but public debt remains near 138% of GDP, among the highest in advanced "
            "economies. Unemployment falls to 5.6%. The report highlights refinancing risks in "
            "high-debt countries as long-term rates reach multidecade highs."
        ),
        "CAN": (
            "Canada's growth eases to 1.1% in 2026 (-0.4 points vs. April) and rises to 1.7% in 2027. "
            "According to the report, supportive policies and positive terms-of-trade effects, as an "
            "energy exporter, partly offset weaker momentum and elevated trade uncertainty. "
            "Inflation rises to 2.8% in 2026. Unemployment falls from 6.9% in 2025 to 6.5% in 2026, "
            "and gross public debt is around 115% of GDP."
        ),
        # ===================== EMERGING =====================
        "AUS": (
            "Australia grows 1.9% in 2026 and 1.6% in 2027, virtually unchanged from April. "
            "Inflation rises to 3.9% in 2026 and eases to 3.1% in 2027. As an energy and commodity "
            "exporter, Australia appears in the report among the economies that benefit indirectly "
            "from the boom in technology exports from Korea and Taiwan (Figure 1.6). The fiscal "
            "deficit widens to 3.2% of GDP in 2026, more than projected in April, and public debt "
            "rises slightly to 53% of GDP."
        ),
        "CHN": (
            "China's growth slows from 5.0% in 2025 to 4.5% in 2026 and 4.0% in 2027. The report "
            "attributes the slowdown to higher oil prices, protracted uncertainty, and structural "
            "headwinds—weak consumption and property sector strains—while policy support would "
            "prevent a sharper slowdown. China cut crude imports by 23% between March and June 2026, "
            "helping absorb the oil shock. Together with the United States, it accounts for more "
            "than 75% of net imports of AI hardware. Its current account surplus rises to 4.0% of GDP "
            "in 2026 and public debt exceeds 100% of GDP; the IMF recommends rebalancing toward "
            "consumption."
        ),
        "IND": (
            "India remains among the fastest-growing major economies: the October 2026 WEO raises its "
            "projection to 7.0% for fiscal year 2026/27 (+0.5 points vs. April) and 7.0% for 2027/28 "
            "(7.4% in calendar 2026). The report attributes this to resilient domestic demand and "
            "robust services activity, despite higher oil prices. India also stands out for upward "
            "revisions to its medium-term growth and is the exception among the largest economies, "
            "most of which would need more fiscal adjustment than planned to stabilize debt. Inflation rises to 5.0% in 2026."
        ),
        "IDN": (
            "Indonesia maintains stable growth of 5.1% in 2025, 2026, and 2027, slightly above "
            "April. Inflation rises to 3.3% in 2026 and eases to 2.8% in 2027. The current account "
            "deficit widens to -1.6% of GDP in 2026. The fiscal deficit stays near 3% of GDP "
            "and public debt around 42% of GDP. For the ASEAN-5 group, the report "
            "projects 4.4% growth in 2026, supported by data center activity and the technology cycle."
        ),
        "RUS": (
            "Russia grows just 1.0% in 2025 and 0.9% in 2026 and 2027 (-0.2 points vs. April). "
            "According to the report, higher commodity prices provide some support to activity, "
            "despite lower oil exports due to attacks on Russian energy infrastructure, onshore and "
            "in the Black Sea, which particularly reduced exports of diesel and other refined "
            "products. Inflation falls from 8.7% in 2025 to 6.1% in 2026. The fiscal deficit widens "
            "to 3.2% of GDP and public debt, though low, rises toward 22% of GDP in 2027."
        ),
        "SAU": (
            "Saudi Arabia suffers one of the largest downward revisions: GDP contracts -3.3% in 2026 "
            "(+3.1% in April) and rebounds 7.9% in 2027. The report explains that the country is "
            "somewhat less affected than other Gulf producers such as Bahrain, Iraq, Kuwait, or "
            "Qatar—which face double-digit contractions—thanks to its more diversified export "
            "routes. The baseline assumes the Strait of Hormuz reopens in March 2027. The fiscal "
            "deficit widens to 6.5% of GDP in 2026 and public debt rises to 35% of GDP."
        ),
        "ZAF": (
            "South Africa grows 1.1% in 2025, 1.0% in 2026, and 1.3% in 2027, unchanged from April. "
            "According to the report, the outlook remains stable in the near term and would improve "
            "gradually over the medium term, underpinned by strengthened policy frameworks and "
            "ongoing structural reforms. Inflation rises to 4.4% in 2026. Unemployment remains very "
            "high, around 33%. The fiscal deficit falls to 4.4% of GDP in 2026 and public debt "
            "stabilizes near 78% of GDP."
        ),
        "KOR": (
            "South Korea receives a strong upward revision: it grows 3.3% in 2026 (1.9% in April) "
            "and 2.8% in 2027, buoyed by strong external demand for semiconductors, which, according "
            "to the report, supersedes the negative impact of the war. Together with Taiwan, Korea "
            "accounts for 62% of net trade in AI hardware. The current account surplus jumps to "
            "18.8% of GDP in 2026. The report warns of bouts of volatility in Korean technology "
            "stocks, exposed to a possible correction if AI expectations are reassessed."
        ),
        "TUR": (
            "Türkiye grows 2.7% in 2026 (-0.7 points vs. April) and 3.6% in 2027. As an energy "
            "importer heavily reliant on fossil fuels, it faces the energy shock that, according to "
            "the report, weakens the outlook for emerging Europe. Inflation remains high and is "
            "revised up: 31.2% in 2026 and 26.5% in 2027 (28.6% and 21.4% in April). The current "
            "account deficit widens to -2.9% of GDP in 2026, while public debt remains low, near 23% "
            "of GDP."
        ),
        "TWN": (
            "Taiwan is one of the main beneficiaries of the AI investment cycle: it grows 8.8% in "
            "2025 and 10.7% in 2026 (5.2% in April), before moderating to 4.3% in 2027. Together with "
            "Korea, it accounts for 62% of net trade in AI hardware, and its exports generate "
            "spillovers for commodity exporters and manufacturing hubs in Asia. The current account "
            "surplus rises to 22% of GDP in 2026. Inflation stays near 2% and public debt falls to "
            "21% of GDP."
        ),
        "SGP": (
            "Singapore grows 5.0% in 2025 and 2026, a +1.5-point revision for 2026 versus April, "
            "moderating to 3.0% in 2027. The report highlights that several southeast Asian "
            "economies benefit from data center activity and the global technology upturn. "
            "Inflation rises to 2.3% in 2026. Singapore maintains a current account surplus near 17% "
            "of GDP and a fiscal surplus of 3.7% of GDP."
        ),
        "ARE": (
            "The United Arab Emirates goes from 6.2% growth in 2025 to a -3.9% contraction in 2026 "
            "(+3.1% in April), before rebounding 7.7% in 2027 as production, exports, and logistics "
            "normalize. The report links the decline of Gulf producers to a longer closure of the "
            "Strait of Hormuz than assumed in April. Inflation rises to 4.5% in 2026. The current "
            "account surplus falls from 13.3% to 4.8% of GDP and the fiscal surplus narrows to 1.5% "
            "of GDP."
        ),
        "PHL": (
            "The Philippines receives a downward revision: growth falls to 3.4% in 2026 (4.1% in "
            "April) and recovers to 5.1% in 2027. As an energy importer, it faces higher oil prices: "
            "inflation rises to 5.6% in 2026 (4.3% in April). Unemployment increases to 5.4% and the "
            "current account deficit widens to -4.8% of GDP. According to the report, the "
            "Philippines is among the leading net exporters of AI hardware, which partly offsets "
            "the energy shock."
        ),
        "VNM": (
            "Vietnam receives a strong upward revision: it grows 8.4% in 2026 (7.1% in April) and "
            "7.5% in 2027, after 8.0% in 2025. According to the report, it is among the leading net "
            "exporters of AI hardware and among the southeast Asian economies benefiting from data "
            "center activity and the technology cycle. Inflation stands at 4.7% in 2026. The current "
            "account surplus falls from 6.7% to 0.3% of GDP in 2026, and public debt remains low, "
            "near 28% of GDP."
        ),
        "MYS": (
            "Malaysia grows 5.2% in 2025 and 2026 (4.7% in April for 2026) and 4.6% in 2027. Along "
            "with Korea, Thailand, and Taiwan, it is one of the top four AI hardware exporters "
            "relative to GDP, according to the report, allowing it to benefit from the technology "
            "boom. Inflation remains low at 2.2% in 2026. The current account surplus rises to 2.1% "
            "of GDP and public debt is around 69% of GDP."
        ),
        "EGY": (
            "Egypt grows 4.4% in 2025, and the October 2026 WEO raises its projection to 5.1% in 2026 "
            "(4.2% in April) and 4.7% in 2027. According to the report, commodity importers in the "
            "Middle East and North Africa would remain relatively resilient to the terms-of-trade "
            "shock from higher energy and food prices. Inflation keeps falling to 13.3% in 2026, "
            "though it picks up to 14.8% in 2027. The fiscal deficit rises to 11.4% of GDP in 2026 "
            "and public debt falls to 84% of GDP."
        ),
        "NGA": (
            "Nigeria grows 4.0% in 2025, 4.2% in 2026, and 4.3% in 2027, slightly above April. "
            "According to the report, the country is supported by improved macroeconomic stability "
            "and favorable terms of trade as an oil exporter, although higher prices for essentials "
            "would further aggravate poverty and food insecurity. Inflation continues to fall, from "
            "23.0% in 2025 to 15.6% in 2026. The current account surplus rises to 7.0% of GDP in "
            "2026 and public debt falls to 35% of GDP."
        ),
    },
}
