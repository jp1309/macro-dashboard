"""
Country summaries extracted from IMF World Economic Outlook, October 2025.
Source: "Global Economy in Flux, Prospects Remain Dim"
All data and analysis based exclusively on the WEO October 2025 PDF text.
"""

COUNTRY_SUMMARIES = {
    "es": {
        # ===================== LATAM =====================
        "ARG": (
            "Según el WEO de octubre 2025, Argentina registró una contracción del PIB de –1,3% en 2024, "
            "pero se proyecta un fuerte repunte con un crecimiento de 4,5% en 2025 y 4,0% en 2026. "
            "La inflación, aunque sigue siendo extremadamente elevada, muestra una marcada desaceleración: "
            "de 219,9% en 2024 a 41,3% en 2025 y 16,4% en 2026. La cuenta corriente pasaría de un superávit "
            "de 0,9% del PIB en 2024 a un déficit de –1,2% en 2025 y –0,4% en 2026. "
            "El desempleo se ubicaría en 7,5% en 2025 antes de bajar a 6,6% en 2026. "
            "El texto también menciona a Argentina como uno de los principales productores de cereales "
            "que contribuyen a las perspectivas de cosechas robustas a nivel mundial."
        ),
        "BOL": (
            "El WEO de octubre 2025 proyecta un crecimiento del PIB de apenas 0,7% para Bolivia en 2024 "
            "y 0,6% en 2025, sin datos publicados para 2026, lo que refleja una situación económica "
            "particularmente compleja. La inflación se dispara de 5,1% en 2024 a 20,8% en 2025, "
            "señalando presiones de precios significativas. El déficit de cuenta corriente se amplía "
            "de –3,0% a –3,4% del PIB entre 2024 y 2025, mientras el desempleo se mantiene estable en "
            "torno al 5%. La ausencia de proyecciones para 2026 sugiere un alto grado de incertidumbre "
            "sobre las perspectivas económicas del país."
        ),
        "BRA": (
            "Brasil es una de las economías emergentes más mencionadas en el WEO de octubre 2025. "
            "El crecimiento se desacelera de 3,4% en 2024 a 2,4% en 2025 y 1,9% en 2026, en parte por "
            "políticas monetarias y fiscales restrictivas y por los aranceles más altos de Estados Unidos "
            "sobre sus exportaciones. La inflación sube de 4,4% a 5,2% en 2025 antes de moderarse a 4,0% "
            "en 2026, reflejando desafíos de credibilidad asociados a incertidumbres fiscales, aunque se "
            "espera alivio por la reciente apreciación cambiaria. El informe destaca que Brasil mostró "
            "fortaleza en la primera mitad de 2025 gracias a una producción agrícola récord, pero "
            "aparecen señales de moderación. El déficit primario es menor que antes de la pandemia, "
            "pero la deuda pública continúa aumentando significativamente. Brasil también es mencionado "
            "como importante productor agrícola, con cosechas récord de maíz y café que influyeron en "
            "los precios mundiales de materias primas."
        ),
        "CHL": (
            "Chile registra un crecimiento del PIB de 2,6% en 2024, que se mantiene estable en 2,5% "
            "en 2025 y se modera a 2,0% en 2026, según las proyecciones del WEO de octubre 2025. "
            "La inflación aumenta ligeramente de 3,9% en 2024 a 4,3% en 2025, antes de descender a "
            "3,1% en 2026. El déficit de cuenta corriente se amplía de –1,5% a –2,5% del PIB en 2025, "
            "mientras el desempleo se mantiene elevado en torno al 8,5%. Como parte de la región de "
            "América Latina y el Caribe, Chile enfrenta los efectos indirectos de los cambios en la "
            "política comercial de EE.UU. y la incertidumbre global, aunque la revisión de su pronóstico "
            "fue relativamente moderada respecto a proyecciones anteriores."
        ),
        "COL": (
            "Según el WEO de octubre 2025, Colombia proyecta un crecimiento del PIB de 2,5% en 2025 y "
            "2,3% en 2026, una mejora respecto al 1,6% de 2024. La inflación se desacelera "
            "significativamente de 6,6% en 2024 a 4,9% en 2025 y 3,5% en 2026. El déficit de cuenta "
            "corriente se amplía de –1,7% a –2,3% del PIB en 2025. El desempleo se mantiene alto "
            "en torno al 10%. Colombia, al igual que la región, se ve afectada por la mayor "
            "incertidumbre comercial y las tensiones proteccionistas, con un pronóstico acumulado "
            "0,5 puntos porcentuales inferior al del WEO de octubre 2024."
        ),
        "CRI": (
            "Costa Rica forma parte del grupo de Centroamérica (CAPDR), que en su conjunto registra "
            "un crecimiento de 3,9% en 2024, proyectado en 3,4% en 2025 y 3,8% en 2026, con una "
            "inflación regional promedio de 1,9% en 2025. El WEO de octubre 2025 no incluye datos "
            "individuales detallados para Costa Rica en las tablas presentadas, pero como parte de "
            "América Latina y el Caribe, el país enfrenta los efectos indirectos de las tensiones "
            "comerciales globales y la incertidumbre en la política comercial de Estados Unidos, "
            "aunque la región centroamericana muestra perspectivas relativamente favorables."
        ),
        "CUB": (
            "Cuba no es mencionada de forma individual en el WEO de octubre 2025. La isla no cuenta "
            "con proyecciones específicas en las tablas del informe. Como parte de la región de América "
            "Latina y el Caribe, donde el crecimiento se proyecta en 2,4% para 2025 y 2,3% para 2026, "
            "la economía cubana enfrenta los mismos desafíos regionales relacionados con la incertidumbre "
            "comercial global, las restricciones al flujo de ayuda internacional y las limitaciones "
            "en el espacio fiscal."
        ),
        "DOM": (
            "La República Dominicana forma parte del grupo CAPDR (Centroamérica, Panamá y República "
            "Dominicana), que en su conjunto crece 3,9% en 2024 y se proyecta en 3,4% en 2025 y 3,8% "
            "en 2026, según el WEO de octubre 2025. Aunque no se proporcionan cifras individuales en "
            "las tablas del capítulo, la subregión muestra una inflación moderada de 1,9% en 2025 y un "
            "saldo de cuenta corriente cercano al equilibrio. La República Dominicana, al igual que la "
            "región, enfrenta los efectos de la incertidumbre comercial global y cambios en las políticas "
            "migratorias de las economías avanzadas, que pueden impactar los flujos de remesas."
        ),
        "ECU": (
            "Ecuador registra una contracción de –2,0% del PIB en 2024, pero el WEO de octubre 2025 "
            "proyecta un fuerte repunte con un crecimiento de 3,2% en 2025 y 2,0% en 2026. La inflación "
            "se mantiene baja: 1,1% en 2025, antes de subir a 2,8% en 2026. El superávit de cuenta "
            "corriente se reduce de 5,7% del PIB en 2024 a 4,9% en 2025 y 3,4% en 2026. El desempleo "
            "sube ligeramente de 3,4% a 4,0% en 2025. Como economía dolarizada y miembro de la región "
            "LAC, Ecuador se beneficia de la depreciación del dólar pero enfrenta los desafíos comunes "
            "de incertidumbre comercial y espacio fiscal limitado."
        ),
        "SLV": (
            "El Salvador forma parte del grupo CAPDR (Centroamérica, Panamá y República Dominicana), "
            "que en conjunto crece 3,9% en 2024 y se proyecta en 3,4% en 2025 y 3,8% en 2026, según "
            "el WEO de octubre 2025. El informe no presenta datos individuales para El Salvador en las "
            "tablas del capítulo. La subregión centroamericana muestra una inflación moderada y saldos "
            "de cuenta corriente cercanos al equilibrio. Como parte de América Latina y el Caribe, "
            "El Salvador enfrenta los efectos de las restricciones migratorias en EE.UU. y sus "
            "implicaciones para las remesas."
        ),
        "GTM": (
            "Guatemala forma parte del grupo CAPDR, que registra un crecimiento de 3,9% en 2024, con "
            "proyecciones de 3,4% en 2025 y 3,8% en 2026 según el WEO de octubre 2025. Aunque el "
            "informe no incluye datos individuales para Guatemala, la subregión muestra estabilidad "
            "macroeconómica con inflación moderada de 1,9% en 2025. Como parte de LAC, Guatemala "
            "enfrenta los desafíos de las políticas migratorias más restrictivas en EE.UU., que podrían "
            "afectar los flujos de remesas, un recurso significativo para muchos países de América "
            "Latina y el Caribe."
        ),
        "GUY": (
            "Guyana forma parte del grupo del Caribe en el WEO de octubre 2025, que en su conjunto "
            "registra un crecimiento excepcional de 12,1% en 2024, impulsado principalmente por la "
            "producción petrolera de Guyana. El crecimiento del Caribe se modera a 3,6% en 2025 y "
            "repunta a 8,2% en 2026. El informe no desglosa datos individuales para Guyana, pero "
            "su condición de importante productor de petróleo la sitúa en un contexto donde los precios "
            "del crudo caen un 12,9% en 2025, lo que podría moderar los ingresos fiscales y externos "
            "del país."
        ),
        "HTI": (
            "Haití forma parte del grupo del Caribe en el WEO de octubre 2025, aunque no cuenta con "
            "proyecciones individuales en las tablas del capítulo. El Caribe en su conjunto registra "
            "una inflación de 6,1% en 2025 y un deterioro del saldo de cuenta corriente. Como economía "
            "frágil, Haití se ve especialmente afectada por los recortes de ayuda al desarrollo "
            "internacional destacados en el informe, y por las políticas migratorias más restrictivas "
            "en economías avanzadas, que amenazan los flujos de remesas que son un recurso vital para "
            "los países más vulnerables de la región."
        ),
        "HND": (
            "Honduras forma parte del grupo CAPDR (Centroamérica, Panamá y República Dominicana), que "
            "en su conjunto muestra un crecimiento de 3,9% en 2024, con proyecciones de 3,4% en 2025 y "
            "3,8% en 2026 según el WEO de octubre 2025. La subregión mantiene una inflación moderada "
            "de 1,9% en 2025. Honduras, como parte de América Latina y el Caribe, enfrenta riesgos "
            "relacionados con las restricciones migratorias en economías avanzadas y sus efectos sobre "
            "las remesas, que constituyen un recurso significativo para varios países centroamericanos."
        ),
        "JAM": (
            "Jamaica forma parte del grupo del Caribe en el WEO de octubre 2025, que en su conjunto "
            "muestra un crecimiento de 3,6% en 2025 y 8,2% en 2026. La inflación del Caribe se sitúa "
            "en 6,1% en 2025. Aunque el informe no incluye datos individuales para Jamaica, el país "
            "enfrenta los desafíos comunes de la región LAC: mayor incertidumbre comercial, espacio "
            "fiscal limitado y los efectos de las políticas migratorias más restrictivas en las "
            "economías avanzadas sobre los flujos de remesas."
        ),
        "MEX": (
            "México es una de las economías más destacadas en el WEO de octubre 2025. El crecimiento "
            "se desacelera de 1,4% en 2024 a 1,0% en 2025, pero se espera un repunte a 1,5% en 2026. "
            "La proyección para 2025 fue revisada al alza en 1,3 puntos porcentuales respecto al WEO de "
            "abril, siendo el principal impulsor de la revisión regional al alza. La inflación baja de "
            "4,7% en 2024 a 3,9% en 2025 y 3,3% en 2026, aunque las categorías volátiles como alimentos "
            "y la inflación persistente en servicios contribuyen a revisiones al alza. El desempleo "
            "sube ligeramente de 2,7% a 2,9%. México aparece en la Figura 1.1 del informe como uno de "
            "los países con aranceles efectivos de EE.UU. entre 10% y 20%, y la inflación mexicana "
            "sorprendió al alza respecto a las proyecciones del FMI. El informe también señala que "
            "Canadá y México han tenido una contribución negativa al crecimiento de las exportaciones "
            "de EE.UU. en 2025, en contraste con 2018-19."
        ),
        "NIC": (
            "Nicaragua forma parte del grupo CAPDR del WEO de octubre 2025, que en conjunto crece "
            "3,4% en 2025 y 3,8% en 2026. El informe no presenta datos individuales para Nicaragua "
            "en las tablas del capítulo. La subregión centroamericana muestra estabilidad con inflación "
            "moderada. Como parte de América Latina y el Caribe, Nicaragua comparte los desafíos "
            "regionales derivados de la incertidumbre comercial global y los cambios en las políticas "
            "migratorias y de ayuda internacional."
        ),
        "PAN": (
            "Panamá forma parte del grupo CAPDR (Centroamérica, Panamá y República Dominicana), que "
            "registra un crecimiento de 3,9% en 2024, proyectado en 3,4% en 2025 y 3,8% en 2026 según "
            "el WEO de octubre 2025. El informe no incluye datos individuales para Panamá. La subregión "
            "mantiene una inflación moderada y un saldo de cuenta corriente cercano al equilibrio. "
            "Panamá, como economía dolarizada vinculada al comercio internacional, enfrenta los efectos "
            "de las tensiones comerciales globales y la fragmentación del comercio mundial que el "
            "informe describe ampliamente."
        ),
        "PRY": (
            "Paraguay registra un crecimiento de 4,2% en 2024, con proyecciones de 4,4% en 2025 y 3,7% "
            "en 2026 según el WEO de octubre 2025, ubicándose por encima del promedio regional de "
            "América Latina y el Caribe. La inflación se mantiene moderada en torno al 3,8-3,9% en "
            "2024-2025. El déficit de cuenta corriente se sitúa en –3,5% del PIB en 2025, mientras el "
            "desempleo mejora de 5,8% a 5,2%. Paraguay comparte con la región los desafíos derivados "
            "de los cambios en la política comercial de EE.UU. y la incertidumbre global."
        ),
        "PER": (
            "Perú muestra un crecimiento del PIB de 3,3% en 2024, que se modera a 2,9% en 2025 y 2,7% "
            "en 2026 según el WEO de octubre 2025. La inflación es notablemente baja para la región: "
            "2,4% en 2024, bajando a 1,7% en 2025 antes de subir ligeramente a 1,9% en 2026. El "
            "superávit de cuenta corriente se reduce de 2,2% a 1,8% del PIB en 2025. El desempleo "
            "se mantiene estable en 6,5%. Perú, como parte de LAC, enfrenta los efectos indirectos "
            "de las tensiones comerciales globales, aunque su pronóstico es relativamente estable."
        ),
        "URY": (
            "Uruguay registra un crecimiento de 3,1% en 2024, moderándose a 2,5% en 2025 y 2,4% en "
            "2026 según el WEO de octubre 2025. La inflación se mantiene estable entre 4,5% y 4,8% "
            "durante el período. El déficit de cuenta corriente se amplía ligeramente de –1,0% a –1,4% "
            "del PIB en 2025. El desempleo mejora de 8,2% a 7,9%. Como parte de América Latina y el "
            "Caribe, Uruguay enfrenta los desafíos comunes de la región derivados de la incertidumbre "
            "comercial y las políticas proteccionistas."
        ),
        "VEN": (
            "Venezuela presenta uno de los cuadros más difíciles en el WEO de octubre 2025. Tras un "
            "crecimiento de 5,3% en 2024, el PIB se desacelera abruptamente a 0,5% en 2025 y se contrae "
            "–3,0% en 2026. La inflación se dispara de 49,0% en 2024 a 269,9% en 2025 y 682,1% en 2026. "
            "La cuenta corriente pasa de un superávit de 4,9% a 4,2% del PIB. El FMI excluye a Venezuela "
            "de los agregados de inflación del grupo de mercados emergentes y economías en desarrollo "
            "debido a la magnitud de sus distorsiones. El informe incluye a Venezuela entre los "
            "exportadores de petróleo en la categoría de cuenta corriente global."
        ),
        "BLZ": (
            "Belice forma parte del grupo del Caribe en el WEO de octubre 2025, que en su conjunto "
            "crece 12,1% en 2024, 3,6% en 2025 y 8,2% en 2026. El informe no incluye datos "
            "individuales para Belice en las tablas del capítulo. Como pequeña economía abierta del "
            "Caribe, Belice comparte los desafíos regionales de espacio fiscal limitado, vulnerabilidad "
            "a choques climáticos y los efectos de las tensiones comerciales globales descritos en "
            "el WEO."
        ),
        "SUR": (
            "Surinam forma parte del grupo del Caribe en el WEO de octubre 2025. El grupo del Caribe "
            "registra un crecimiento de 3,6% en 2025 con una inflación de 6,1%. Aunque el informe no "
            "presenta datos individuales para Surinam, como economía dependiente de materias primas en "
            "la región LAC, enfrenta los efectos de la caída de los precios del petróleo (–12,9% en "
            "2025) y los desafíos comunes de incertidumbre comercial global."
        ),
        "TTO": (
            "Trinidad y Tobago forma parte del grupo del Caribe en el WEO de octubre 2025, que registra "
            "un crecimiento de 3,6% en 2025. El informe no incluye datos individuales para el país. "
            "Como exportador de energía, Trinidad y Tobago se ve afectada por el contexto descrito en "
            "el informe de caída de precios del petróleo (–12,9% en 2025) y precios del gas natural "
            "a la baja por incertidumbre comercial y producción abundante. Los precios del gas en el "
            "Henry Hub cayeron un 30% a $2,9/MMBtu debido a la incertidumbre de demanda por aranceles "
            "y producción doméstica récord en EE.UU."
        ),

        # ===================== G7 =====================
        "USA": (
            "Estados Unidos es la economía más analizada en el WEO de octubre 2025. El crecimiento se "
            "desacelera de 2,8% en 2024 a 2,0% en 2025 y 2,1% en 2026, una revisión a la baja "
            "acumulada de 0,1 puntos respecto al WEO de octubre 2024. La inflación se proyecta en "
            "2,7% para 2025, significativamente por encima del 1,9% previsto un año antes, reflejando "
            "el traspaso de aranceles a los consumidores. El desempleo sube a 4,2% en 2025. La tasa "
            "arancelaria efectiva se mantiene elevada en torno al 19%, generando choques de oferta. "
            "Las políticas migratorias más restrictivas podrían reducir el PIB entre 0,3% y 0,7% anual. "
            "La Ley OBBBA amplía el déficit fiscal, con la deuda pública subiendo de 122% del PIB en "
            "2024 a 143% en 2030. La inversión en inteligencia artificial impulsa el gasto en equipo "
            "e infraestructura tecnológica. La tasa de fondos federales se proyecta en 3,50-3,75% a "
            "finales de 2025, con un rango terminal de 2,75-3,0% hacia finales de 2028. La probabilidad "
            "de recesión en 2026 se estima en 30%, y hay un riesgo similar de que la inflación supere "
            "el 3%."
        ),
        "JPN": (
            "Japón muestra una aceleración del crecimiento de 0,1% en 2024 a 1,1% en 2025, antes de "
            "moderarse a 0,6% en 2026, según el WEO de octubre 2025. La inflación sube a 3,3% en 2025 "
            "y baja a 2,1% en 2026. El superávit de cuenta corriente se sitúa en 3,9% del PIB. "
            "El crecimiento de los salarios reales impulsa el consumo privado, aunque la incertidumbre "
            "comercial y la demanda externa más débil son vientos en contra. Las tasas de interés se "
            "elevan gradualmente hacia un nivel neutral de 1,5%. Japón es mencionado en el análisis "
            "como caso donde los precios de exportación de automóviles a América del Norte cayeron más "
            "del 20%, mientras que a otros destinos se mantuvieron estables. El refinanciamiento de "
            "deuda pública de Japón es de 26,2% del PIB, el más alto entre las grandes economías "
            "avanzadas."
        ),
        "DEU": (
            "Alemania registró una contracción de –0,5% en 2024, pero se recupera con un crecimiento "
            "de 0,2% en 2025 y 0,9% en 2026 según el WEO de octubre 2025. La inflación baja de 2,5% "
            "en 2024 a 2,1% en 2025 y 1,8% en 2026. La expansión fiscal alemana, con un aumento del "
            "déficit de 0,8 puntos porcentuales por mayor gasto en infraestructura y capacidad militar, "
            "impulsa el crecimiento en 2026. El superávit de cuenta corriente se mantiene en torno al "
            "5,4% del PIB. El informe menciona a Alemania junto a China y EE.UU. como uno de los tres "
            "mayores contribuyentes a los desequilibrios globales de cuenta corriente. Los precios de "
            "exportación de automóviles alemanes a países fuera de la UE se mantuvieron relativamente "
            "estables hasta ahora."
        ),
        "GBR": (
            "El Reino Unido crece 1,3% tanto en 2025 como en 2026, según el WEO de octubre 2025, una "
            "leve revisión al alza respecto a abril. La inflación sube de 2,5% en 2024 a 3,4% en 2025, "
            "en parte por cambios en precios regulados, antes de regresar a la meta a finales de 2026. "
            "El déficit de cuenta corriente se amplía a –3,1% del PIB en 2025. El desempleo sube a "
            "4,7%. El informe señala que la inflación del Reino Unido sorprendió al alza, mientras que "
            "su actividad fue fuerte en la primera mitad de 2025. El acuerdo comercial UK-EE.UU. "
            "anunciado en mayo mejoró el entorno externo. El crecimiento acumulado en 2025-26 es 0,4 "
            "puntos inferior al previsto en octubre 2024."
        ),
        "FRA": (
            "Francia crece 0,7% en 2025 y 0,9% en 2026, desacelerándose desde el 1,1% de 2024, según "
            "el WEO de octubre 2025. La inflación cae a 1,1% en 2025, la más baja entre las grandes "
            "economías del área euro. La cuenta corriente registra un ligero déficit de –0,1% del PIB. "
            "El desempleo sube marginalmente a 7,6%. Francia es mencionada como uno de los países donde "
            "la deuda pública está en trayectoria ascendente significativa. El refinanciamiento de "
            "deuda es de 12,2% del PIB. El balance fiscal se deteriora junto con el del área euro "
            "en general."
        ),
        "ITA": (
            "Italia crece 0,5% en 2025 y 0,8% en 2026, moderándose desde el 0,7% de 2024, según "
            "el WEO de octubre 2025. La inflación sube de 1,1% en 2024 a 1,7% en 2025 y 2,0% en 2026. "
            "El superávit de cuenta corriente se mantiene estable en 1,0% del PIB. El desempleo se "
            "sitúa en 6,7%. Italia es mencionada junto a Alemania como país donde el crecimiento "
            "declinó en el segundo trimestre de 2025 dentro del área euro. Las necesidades de "
            "refinanciamiento de deuda de Italia son 18,1% del PIB, entre las más altas de las "
            "grandes economías avanzadas."
        ),
        "CAN": (
            "Canadá crece 1,2% en 2025 y 1,5% en 2026, según el WEO de octubre 2025, una revisión "
            "significativamente a la baja de 1,7 puntos acumulados respecto al WEO de octubre 2024, "
            "la más pronunciada entre las economías avanzadas. La inflación se mantiene contenida en "
            "2,0% en 2025-2026. El déficit de cuenta corriente se amplía a –1,4% del PIB. El desempleo "
            "sube a 6,9%. La fuerte revisión a la baja refleja el impacto del cambio en el panorama "
            "comercial internacional, con aranceles elevados y aranceles sobre productos no conformes "
            "con el TMEC. Canadá y México tuvieron una contribución negativa al crecimiento de las "
            "exportaciones de EE.UU. en 2025, en contraste con el episodio de 2018-19."
        ),

        # ===================== EMERGENTES =====================
        "AUS": (
            "Australia crece 1,8% en 2025 y 2,1% en 2026, mejorando desde el 1,0% de 2024, según "
            "el WEO de octubre 2025. La inflación se sitúa en 2,6% en 2025 y 3,0% en 2026. El déficit "
            "de cuenta corriente se mantiene en –1,8% del PIB. Australia es mencionada en el análisis "
            "del Commodity Special Feature como ejemplo de economía avanzada con un sector de materias "
            "primas altamente interconectado (alto NAVAS), lo que implica una co-movimiento más fuerte "
            "entre el consumo agregado y los choques de términos de intercambio de materias primas, "
            "similar a las economías emergentes."
        ),
        "CHN": (
            "China es la segunda economía más analizada en el WEO de octubre 2025. El crecimiento se "
            "desacelera de 5,0% en 2024 a 4,8% en 2025 y 4,2% en 2026. La inflación es prácticamente "
            "nula: 0,0% en 2025, con deflación persistente en precios al productor. El superávit de "
            "cuenta corriente aumenta a 3,3% del PIB en 2025. China es el país más afectado por los "
            "aranceles de EE.UU. y el más expuesto a aranceles adicionales en el escenario A del "
            "informe (30 puntos adicionales). La depreciación del tipo de cambio real efectivo, el "
            "redireccionamiento de exportaciones hacia Asia y Europa, y la expansión fiscal compensan "
            "parcialmente. Sin embargo, el sector inmobiliario sigue sin estabilizarse más de cuatro "
            "años después del estallido de la burbuja, y la economía bordea un ciclo de deuda-deflación. "
            "Los subsidios al sector manufacturero están generando una significativa mala asignación de "
            "recursos. Los controles de exportación de tierras raras causaron picos de precios temporales. "
            "La política fiscal es apropiadamente expansiva pero insostenible a mediano plazo."
        ),
        "IND": (
            "India mantiene un crecimiento robusto de 6,6% en 2025 y 6,2% en 2026 según el WEO de "
            "octubre 2025, respaldado por una fuerte expansión del sector servicios. La inflación baja "
            "significativamente a 2,8% en 2025, con sorpresas a la baja. El déficit de cuenta corriente "
            "se amplía ligeramente a –1,0% del PIB. India fue revisada al alza para 2025 por el efecto "
            "arrastre de un sólido primer trimestre, pero a la baja para 2026 por el aumento de la "
            "tasa arancelaria efectiva de EE.UU. sobre importaciones indias. El déficit primario es "
            "menor que antes de la pandemia. India aparece en la Figura 1.1 como uno de los países con "
            "aranceles efectivos de EE.UU. más elevados."
        ),
        "IDN": (
            "Indonesia crece 4,9% en 2025 y 2026, prácticamente estable respecto al 5,0% de 2024, "
            "según el WEO de octubre 2025. La inflación baja a 1,8% en 2025 antes de subir a 2,9% en "
            "2026. El déficit de cuenta corriente se sitúa en –1,1% del PIB. Indonesia forma parte del "
            "grupo ASEAN-5, que crece 4,2% en 2025 y es una de las regiones más afectadas por la "
            "evolución de las tasas arancelarias efectivas. Las economías del ASEAN vieron sus "
            "pronósticos de crecimiento seguir de cerca la trayectoria de los aranceles."
        ),
        "RUS": (
            "Rusia experimenta una desaceleración drástica según el WEO de octubre 2025: el crecimiento "
            "cae de 4,3% en 2024 a apenas 0,6% en 2025 y 1,0% en 2026. La inflación se sitúa en "
            "9,0% en 2025 y baja a 5,2% en 2026. La revisión a la baja de 0,9 puntos para 2025 "
            "respecto a abril se debe a la concentración del gasto fiscal en el cuarto trimestre de "
            "2024, cuyo efecto de payback se incorpora en las proyecciones de 2025. El superávit de "
            "cuenta corriente se reduce a 1,7% del PIB. Rusia es mencionada como miembro de OPEC+ y "
            "participante en el esquema acelerado de producción petrolera. Las negociaciones de paz "
            "con Ucrania se han estancado."
        ),
        "SAU": (
            "Arabia Saudita crece 4,0% tanto en 2025 como en 2026, acelerando significativamente desde "
            "el 2,0% de 2024, según el WEO de octubre 2025. La inflación se mantiene baja en 2,1% en "
            "2025. La cuenta corriente pasa a déficit de –2,1% del PIB en 2025. La revisión al alza "
            "de 1,0 punto porcentual para 2025 respecto a abril se debe a que el desmantelamiento de "
            "los recortes de producción petrolera de OPEC+ fue más rápido de lo esperado. Arabia "
            "Saudita es identificada como el principal impulsor de la revisión al alza de la región "
            "de Medio Oriente y Asia Central, junto con Egipto."
        ),
        "ZAF": (
            "Sudáfrica crece 1,1% en 2025 y 1,2% en 2026, mejorando ligeramente desde el 0,5% de "
            "2024, según el WEO de octubre 2025. La inflación se sitúa en 3,4% en 2025 y 3,7% en "
            "2026. El desempleo se mantiene extremadamente alto en 32,7%. El Commodity Special Feature "
            "analiza extensamente a Sudáfrica como caso de estudio: pese a ser un exportador neto de "
            "materias primas con un sector de tamaño similar al de Kazajistán (39% del PIB), su menor "
            "interconexión (NAVAS de 0,73 vs 0,90) implica que los choques de precios de materias "
            "primas pueden tener un efecto negativo sobre el consumo agregado, algo contraintuitivo "
            "para un exportador neto."
        ),
        "KOR": (
            "Corea del Sur crece 0,9% en 2025 y 1,8% en 2026, desacelerándose significativamente "
            "desde el 2,0% de 2024, según el WEO de octubre 2025. La inflación se modera a 2,0% en "
            "2025. El superávit de cuenta corriente se sitúa en 4,8% del PIB. El informe menciona que "
            "los precios de exportación de automóviles coreanos mostraron un patrón similar al de "
            "Japón, con caídas significativas en los precios destinados a América del Norte como "
            "consecuencia de los aranceles."
        ),
        "TUR": (
            "Turquía crece 3,5% en 2025 y 3,7% en 2026, acelerando desde el 3,3% de 2024, según "
            "el WEO de octubre 2025. La inflación se desacelera marcadamente pero sigue muy elevada: "
            "de 58,5% en 2024 a 34,9% en 2025 y 24,7% en 2026. Las proyecciones fueron revisadas al "
            "alza para ambos años por resultados mejores de lo esperado y demanda interna resiliente. "
            "Turquía aparece en la Figura 1.1 como uno de los países con aranceles efectivos de EE.UU. "
            "más elevados. El informe menciona la demanda interna resiliente como factor de fortaleza."
        ),
        "TWN": (
            "Taiwán (Provincia China de) crece 3,7% en 2025 y 2,1% en 2026, desacelerándose desde "
            "el 4,8% de 2024, según el WEO de octubre 2025. La inflación se mantiene baja en 1,7% en "
            "2025. El superávit de cuenta corriente es de 13,8% del PIB, uno de los más altos del "
            "mundo. Como economía avanzada de Asia, Taiwán enfrenta la incertidumbre comercial global "
            "y los aranceles de EE.UU. que afectan a la región, pero no recibe mención narrativa "
            "individual en el texto del capítulo."
        ),
        "SGP": (
            "Singapur crece 2,2% en 2025 y 1,8% en 2026, desacelerándose desde el 4,4% de 2024, según "
            "el WEO de octubre 2025. La inflación es muy baja: 0,9% en 2025. El superávit de cuenta "
            "corriente se mantiene en 17,4% del PIB. Singapur forma parte del grupo ASEAN-5, que "
            "enfrenta los efectos de los aranceles de EE.UU. y la reconfiguración del comercio global. "
            "El informe no incluye mención narrativa individual de Singapur."
        ),
        "ARE": (
            "Los Emiratos Árabes Unidos crecen 4,8% en 2025 y 5,0% en 2026, acelerando desde el 4,0% "
            "de 2024, según el WEO de octubre 2025. La inflación se mantiene baja en 1,6% en 2025. El "
            "superávit de cuenta corriente se sitúa en 13,2% del PIB. Los EAU se benefician del "
            "desmantelamiento de los recortes de producción de OPEC+, con una cuota de producción mayor "
            "(0,3 mb/d adicionales) mencionada específicamente en el Commodity Special Feature. El país "
            "es también incluido en la lista de exportadores de petróleo que contribuyen a los "
            "desequilibrios globales de cuenta corriente."
        ),
        "PHL": (
            "Filipinas crece 5,4% en 2025 y 5,7% en 2026, una leve desaceleración respecto al 5,7% "
            "de 2024, según el WEO de octubre 2025. La inflación baja significativamente a 1,6% en "
            "2025, habiendo sorprendido a la baja respecto a las proyecciones del FMI. El déficit "
            "de cuenta corriente mejora ligeramente a –3,8% del PIB. Filipinas forma parte del grupo "
            "ASEAN-5, donde la evolución de los pronósticos de crecimiento siguió de cerca la "
            "trayectoria de los aranceles efectivos de EE.UU."
        ),
        "VNM": (
            "Vietnam crece 6,5% en 2025 y 5,6% en 2026, desacelerándose desde el 7,1% de 2024, según "
            "el WEO de octubre 2025. La inflación se mantiene moderada en 3,4% en 2025. El superávit "
            "de cuenta corriente se reduce de 6,6% a 4,0% del PIB. Vietnam es mencionada en el "
            "Commodity Special Feature: pese a tener un sector energético de tamaño similar al de "
            "Noruega, su menor interconexión con el resto de la economía (NAVAS de 0,48 vs 0,94) "
            "implica una menor correlación entre choques de precios de energía y el consumo agregado."
        ),
        "MYS": (
            "Malasia crece 4,5% en 2025 y 4,0% en 2026, desacelerándose desde el 5,1% de 2024, según "
            "el WEO de octubre 2025. La inflación se mantiene baja en 1,6% en 2025, habiendo "
            "sorprendido a la baja. El superávit de cuenta corriente se sitúa en 1,5% del PIB. "
            "Malasia forma parte del grupo ASEAN-5 y de la categoría de Asia emergente, cuya "
            "inflación fue inferior a lo esperado. La región asiática enfrenta los efectos de los "
            "aranceles y la reconfiguración del comercio global."
        ),
        "EGY": (
            "Egipto crece 4,3% en 2025 y 4,5% en 2026, acelerando desde el 2,4% de 2024, según el "
            "WEO de octubre 2025. La inflación se desacelera de 33,3% en 2024 a 20,4% en 2025 y 11,8% "
            "en 2026. El déficit de cuenta corriente mejora de –5,4% a –5,1% del PIB. El informe "
            "menciona específicamente que el resultado del primer semestre de 2025 en Egipto fue mejor "
            "de lo esperado, contribuyendo a la revisión al alza de la región de Medio Oriente y "
            "Asia Central, junto con Arabia Saudita."
        ),
        "NGA": (
            "Nigeria crece 3,9% en 2025 y 4,2% en 2026, según el WEO de octubre 2025. La inflación se "
            "mantiene muy elevada en 23,0% en 2025 y 22,0% en 2026, aunque en descenso desde el 31,4% "
            "de 2024. El superávit de cuenta corriente se reduce a 5,7% del PIB. Las cuentas nacionales "
            "de Nigeria fueron revisadas con base 2019, aumentando el nivel del PIB un 40,8%. El "
            "crecimiento fue revisado al alza por factores domésticos favorables, incluyendo mayor "
            "producción de petróleo, mejor confianza de los inversores, una posición fiscal favorable "
            "en 2026 y la limitada exposición del país a los aranceles elevados de EE.UU. Nigeria "
            "también es incluida entre los exportadores de petróleo en los desequilibrios globales."
        ),
    },
    "en": {
        # ===================== LATAM =====================
        "ARG": (
            "According to the October 2025 WEO, Argentina recorded a GDP contraction of -1.3% in 2024, "
            "but is projected to rebound strongly with growth of 4.5% in 2025 and 4.0% in 2026. "
            "Inflation, while still extremely high, shows a marked deceleration: from 219.9% in 2024 "
            "to 41.3% in 2025 and 16.4% in 2026. The current account shifts from a surplus of 0.9% "
            "of GDP in 2024 to a deficit of -1.2% in 2025. Unemployment is projected at 7.5% in 2025 "
            "before declining to 6.6% in 2026. The text also mentions Argentina as a major cereal "
            "producer contributing to robust global harvest prospects."
        ),
        "BOL": (
            "The October 2025 WEO projects Bolivia's GDP growth at just 0.7% in 2024 and 0.6% in 2025, "
            "with no data published for 2026, reflecting a particularly complex economic situation. "
            "Inflation surges from 5.1% in 2024 to 20.8% in 2025, signaling significant price "
            "pressures. The current account deficit widens from -3.0% to -3.4% of GDP between 2024 "
            "and 2025, while unemployment remains stable at around 5%. The absence of 2026 projections "
            "suggests a high degree of uncertainty about the country's economic outlook."
        ),
        "BRA": (
            "Brazil is one of the most frequently mentioned emerging economies in the October 2025 WEO. "
            "Growth decelerates from 3.4% in 2024 to 2.4% in 2025 and 1.9% in 2026, partly due to "
            "tight monetary and fiscal policies and higher US tariffs on its exports. Inflation rises "
            "from 4.4% to 5.2% in 2025 before moderating to 4.0% in 2026, reflecting credibility "
            "challenges associated with fiscal uncertainties, although relief from recent currency "
            "appreciation is expected. The report highlights that Brazil showed strength in the first "
            "half of 2025 thanks to record agricultural output, but signs of moderation are appearing. "
            "The primary deficit is smaller than pre-pandemic, but public debt continues to rise "
            "significantly. Brazil is also noted as a major agricultural producer whose record corn "
            "and coffee harvests influenced global commodity prices."
        ),
        "CHL": (
            "Chile records GDP growth of 2.6% in 2024, remaining stable at 2.5% in 2025 and moderating "
            "to 2.0% in 2026, according to the October 2025 WEO. Inflation rises slightly from 3.9% "
            "in 2024 to 4.3% in 2025 before declining to 3.1% in 2026. The current account deficit "
            "widens from -1.5% to -2.5% of GDP in 2025, while unemployment remains elevated at around "
            "8.5%. As part of the Latin America and Caribbean region, Chile faces the indirect effects "
            "of US trade policy changes and global uncertainty, though forecast revisions have been "
            "relatively moderate."
        ),
        "COL": (
            "According to the October 2025 WEO, Colombia projects GDP growth of 2.5% in 2025 and 2.3% "
            "in 2026, an improvement from 1.6% in 2024. Inflation decelerates significantly from 6.6% "
            "in 2024 to 4.9% in 2025 and 3.5% in 2026. The current account deficit widens from -1.7% "
            "to -2.3% of GDP in 2025. Unemployment remains high at around 10%. Colombia, like the "
            "region, is affected by higher trade uncertainty and protectionist tensions, with a "
            "cumulative forecast 0.5 percentage points lower than the October 2024 WEO."
        ),
        "CRI": (
            "Costa Rica belongs to the Central America (CAPDR) group, which as a whole records growth "
            "of 3.9% in 2024, projected at 3.4% in 2025 and 3.8% in 2026, with regional average "
            "inflation of 1.9% in 2025. The October 2025 WEO does not include individual detailed "
            "data for Costa Rica in the chapter tables, but as part of Latin America and the Caribbean, "
            "the country faces indirect effects from global trade tensions and US trade policy "
            "uncertainty, though the Central American subregion shows relatively favorable prospects."
        ),
        "CUB": (
            "Cuba is not mentioned individually in the October 2025 WEO. The island has no specific "
            "projections in the report's tables. As part of the Latin America and Caribbean region, "
            "where growth is projected at 2.4% for 2025 and 2.3% for 2026, the Cuban economy faces "
            "the same regional challenges related to global trade uncertainty, restrictions on "
            "international aid flows, and fiscal space limitations."
        ),
        "DOM": (
            "The Dominican Republic belongs to the CAPDR group (Central America, Panama, and the "
            "Dominican Republic), which as a whole grows 3.9% in 2024 and is projected at 3.4% in "
            "2025 and 3.8% in 2026, according to the October 2025 WEO. While individual figures are "
            "not provided in the chapter tables, the subregion shows moderate inflation of 1.9% in "
            "2025. The Dominican Republic, like the region, faces the effects of global trade "
            "uncertainty and changes in advanced economy immigration policies that may impact "
            "remittance flows."
        ),
        "ECU": (
            "Ecuador records a GDP contraction of -2.0% in 2024, but the October 2025 WEO projects a "
            "strong rebound with growth of 3.2% in 2025 and 2.0% in 2026. Inflation remains low at "
            "1.1% in 2025 before rising to 2.8% in 2026. The current account surplus declines from "
            "5.7% of GDP in 2024 to 4.9% in 2025 and 3.4% in 2026. Unemployment rises slightly "
            "from 3.4% to 4.0% in 2025. As a dollarized economy and LAC member, Ecuador benefits "
            "from dollar depreciation but faces common challenges of trade uncertainty and limited "
            "fiscal space."
        ),
        "SLV": (
            "El Salvador belongs to the CAPDR group (Central America, Panama, and the Dominican "
            "Republic), which as a whole grows 3.9% in 2024 and is projected at 3.4% in 2025 and "
            "3.8% in 2026, according to the October 2025 WEO. The report does not present individual "
            "data for El Salvador. The Central American subregion shows moderate inflation and "
            "near-balanced current accounts. As part of LAC, El Salvador faces effects from US "
            "immigration restrictions and their implications for remittances."
        ),
        "GTM": (
            "Guatemala belongs to the CAPDR group, which records growth of 3.9% in 2024, with "
            "projections of 3.4% in 2025 and 3.8% in 2026 according to the October 2025 WEO. "
            "The report does not include individual data for Guatemala, though the subregion shows "
            "macroeconomic stability with moderate inflation of 1.9% in 2025. As part of LAC, "
            "Guatemala faces challenges from more restrictive US immigration policies that could "
            "affect remittance flows, a significant resource for many LAC countries."
        ),
        "GUY": (
            "Guyana belongs to the Caribbean group in the October 2025 WEO, which as a whole records "
            "exceptional growth of 12.1% in 2024, largely driven by Guyana's oil production. Caribbean "
            "growth moderates to 3.6% in 2025 and rebounds to 8.2% in 2026. The report does not "
            "disaggregate individual data for Guyana, but its status as a major oil producer places "
            "it in a context where crude prices fall 12.9% in 2025, which could moderate fiscal and "
            "external revenues."
        ),
        "HTI": (
            "Haiti belongs to the Caribbean group in the October 2025 WEO, though it has no individual "
            "projections in the chapter tables. The Caribbean as a whole records inflation of 6.1% "
            "in 2025 and a deteriorating current account balance. As a fragile economy, Haiti is "
            "particularly affected by the cuts to international development aid highlighted in the "
            "report, and by more restrictive immigration policies in advanced economies that threaten "
            "remittance flows, a vital resource for the region's most vulnerable countries."
        ),
        "HND": (
            "Honduras belongs to the CAPDR group, which as a whole shows growth of 3.9% in 2024, "
            "with projections of 3.4% in 2025 and 3.8% in 2026 according to the October 2025 WEO. "
            "The subregion maintains moderate inflation of 1.9% in 2025. Honduras, as part of Latin "
            "America and the Caribbean, faces risks related to immigration restrictions in advanced "
            "economies and their effects on remittances, a significant resource for several Central "
            "American countries."
        ),
        "JAM": (
            "Jamaica belongs to the Caribbean group in the October 2025 WEO, which as a whole shows "
            "growth of 3.6% in 2025 and 8.2% in 2026. Caribbean inflation stands at 6.1% in 2025. "
            "While the report does not include individual data for Jamaica, the country faces common "
            "LAC challenges: higher trade uncertainty, limited fiscal space, and the effects of more "
            "restrictive immigration policies in advanced economies on remittance flows."
        ),
        "MEX": (
            "Mexico is one of the most prominent economies in the October 2025 WEO. Growth decelerates "
            "from 1.4% in 2024 to 1.0% in 2025, but a rebound to 1.5% in 2026 is expected. The 2025 "
            "projection was revised upward by 1.3 percentage points from the April WEO, being the main "
            "driver of the regional upward revision. Inflation falls from 4.7% in 2024 to 3.9% in "
            "2025 and 3.3% in 2026, though volatile categories like food and more-persistent-than-"
            "expected services inflation contribute to upward revisions. Mexico appears in Figure 1.1 "
            "as one of the countries with US effective tariff rates between 10% and 20%, and Mexican "
            "inflation surprised to the upside relative to IMF projections. The report also notes that "
            "Canada and Mexico made a negative contribution to US export growth in 2025, in contrast "
            "to the 2018-19 episode."
        ),
        "NIC": (
            "Nicaragua belongs to the CAPDR group in the October 2025 WEO, which as a whole grows "
            "3.4% in 2025 and 3.8% in 2026. The report does not present individual data for Nicaragua. "
            "The Central American subregion shows stability with moderate inflation. As part of Latin "
            "America and the Caribbean, Nicaragua shares the regional challenges stemming from global "
            "trade uncertainty and changes in immigration and international aid policies."
        ),
        "PAN": (
            "Panama belongs to the CAPDR group, which records growth of 3.9% in 2024, projected at "
            "3.4% in 2025 and 3.8% in 2026 according to the October 2025 WEO. The report does not "
            "include individual data for Panama. The subregion maintains moderate inflation and a "
            "near-balanced current account. Panama, as a dollarized economy linked to international "
            "trade, faces the effects of global trade tensions and the trade fragmentation extensively "
            "described in the report."
        ),
        "PRY": (
            "Paraguay records growth of 4.2% in 2024, with projections of 4.4% in 2025 and 3.7% in "
            "2026 according to the October 2025 WEO, above the LAC regional average. Inflation "
            "remains moderate at around 3.8-3.9% in 2024-2025. The current account deficit stands "
            "at -3.5% of GDP in 2025, while unemployment improves from 5.8% to 5.2%. Paraguay "
            "shares with the region the challenges from US trade policy changes and global uncertainty."
        ),
        "PER": (
            "Peru shows GDP growth of 3.3% in 2024, moderating to 2.9% in 2025 and 2.7% in 2026 "
            "according to the October 2025 WEO. Inflation is notably low for the region: 2.4% in "
            "2024, falling to 1.7% in 2025 before rising slightly to 1.9% in 2026. The current "
            "account surplus declines from 2.2% to 1.8% of GDP in 2025. Unemployment remains stable "
            "at 6.5%. Peru, as part of LAC, faces indirect effects from global trade tensions, "
            "though its forecast remains relatively stable."
        ),
        "URY": (
            "Uruguay records growth of 3.1% in 2024, moderating to 2.5% in 2025 and 2.4% in 2026 "
            "according to the October 2025 WEO. Inflation remains stable between 4.5% and 4.8% "
            "during the period. The current account deficit widens slightly from -1.0% to -1.4% "
            "of GDP in 2025. Unemployment improves from 8.2% to 7.9%. As part of Latin America and "
            "the Caribbean, Uruguay faces common regional challenges from trade uncertainty and "
            "protectionist policies."
        ),
        "VEN": (
            "Venezuela presents one of the most difficult cases in the October 2025 WEO. After "
            "growth of 5.3% in 2024, GDP decelerates sharply to 0.5% in 2025 and contracts -3.0% "
            "in 2026. Inflation surges from 49.0% in 2024 to 269.9% in 2025 and 682.1% in 2026. "
            "The current account moves from a surplus of 4.9% to 4.2% of GDP. The IMF excludes "
            "Venezuela from inflation aggregates for emerging market and developing economies due "
            "to the magnitude of its distortions. The report includes Venezuela among oil exporters "
            "in the global current account category."
        ),
        "BLZ": (
            "Belize belongs to the Caribbean group in the October 2025 WEO, which as a whole grows "
            "12.1% in 2024, 3.6% in 2025, and 8.2% in 2026. The report does not include individual "
            "data for Belize. As a small open Caribbean economy, Belize shares the regional "
            "challenges of limited fiscal space, vulnerability to climate shocks, and the effects "
            "of global trade tensions described in the WEO."
        ),
        "SUR": (
            "Suriname belongs to the Caribbean group in the October 2025 WEO. The Caribbean group "
            "records growth of 3.6% in 2025 with inflation of 6.1%. While the report does not "
            "present individual data for Suriname, as a commodity-dependent economy in the LAC "
            "region, it faces the effects of declining oil prices (-12.9% in 2025) and the common "
            "challenges of global trade uncertainty."
        ),
        "TTO": (
            "Trinidad and Tobago belongs to the Caribbean group in the October 2025 WEO, which "
            "records growth of 3.6% in 2025. The report does not include individual data for the "
            "country. As an energy exporter, Trinidad and Tobago is affected by the context described "
            "in the report of declining oil prices (-12.9% in 2025) and falling natural gas prices "
            "driven by trade uncertainty and ample supply. Henry Hub prices fell 30% to $2.9/MMBtu "
            "due to tariff-induced demand uncertainty and record US domestic production."
        ),

        # ===================== G7 =====================
        "USA": (
            "The United States is the most extensively analyzed economy in the October 2025 WEO. "
            "Growth decelerates from 2.8% in 2024 to 2.0% in 2025 and 2.1% in 2026, a cumulative "
            "downward revision of 0.1 percentage points from the October 2024 WEO. Inflation is "
            "projected at 2.7% for 2025, well above the 1.9% forecast a year earlier, reflecting "
            "tariff pass-through to consumers. Unemployment rises to 4.2% in 2025. The effective "
            "tariff rate remains elevated at about 19%, generating supply shocks. Stricter immigration "
            "policies could reduce GDP by 0.3%-0.7% annually. The OBBBA legislation widens the fiscal "
            "deficit, with public debt rising from 122% of GDP in 2024 to 143% by 2030. AI investment "
            "is driving equipment and technology spending. The federal funds rate is projected at "
            "3.50-3.75% by end-2025, with a terminal range of 2.75-3.0% around end-2028. Recession "
            "probability for 2026 is estimated at about 30%, with a similar risk of inflation "
            "exceeding 3%."
        ),
        "JPN": (
            "Japan shows growth accelerating from 0.1% in 2024 to 1.1% in 2025, before moderating "
            "to 0.6% in 2026, according to the October 2025 WEO. Inflation rises to 3.3% in 2025 "
            "and falls to 2.1% in 2026. The current account surplus stands at 3.9% of GDP. Real wage "
            "growth supports private consumption, though trade uncertainty and weaker external demand "
            "are headwinds. Policy rates are gradually rising toward a neutral 1.5%. Japan is noted "
            "in the analysis as a case where export prices of standard passenger cars to North America "
            "plummeted more than 20%, while those to the rest of the world remained stable. Japan's "
            "public debt refinancing stands at 26.2% of GDP, the highest among major advanced "
            "economies."
        ),
        "DEU": (
            "Germany recorded a contraction of -0.5% in 2024 but recovers with growth of 0.2% in "
            "2025 and 0.9% in 2026 according to the October 2025 WEO. Inflation falls from 2.5% in "
            "2024 to 2.1% in 2025 and 1.8% in 2026. Germany's fiscal expansion, with the deficit "
            "widening by 0.8 percentage points from increased infrastructure and military spending, "
            "drives growth in 2026. The current account surplus remains at about 5.4% of GDP. The "
            "report mentions Germany alongside China and the US as one of the three largest "
            "contributors to global current account imbalances. Export prices of German cars to "
            "non-EU countries have remained relatively stable so far."
        ),
        "GBR": (
            "The United Kingdom grows 1.3% in both 2025 and 2026, according to the October 2025 WEO, "
            "a slight upward revision from April. Inflation rises from 2.5% in 2024 to 3.4% in "
            "2025, partly from changes in regulated prices, before returning to target by end-2026. "
            "The current account deficit widens to -3.1% of GDP in 2025. Unemployment rises to 4.7%. "
            "The report notes that UK inflation surprised to the upside, while activity was strong in "
            "the first half of 2025. The UK-US trade deal announced in May improved the external "
            "environment. Cumulative growth in 2025-26 is 0.4 percentage points below the October "
            "2024 forecast."
        ),
        "FRA": (
            "France grows 0.7% in 2025 and 0.9% in 2026, decelerating from 1.1% in 2024, according "
            "to the October 2025 WEO. Inflation drops to 1.1% in 2025, the lowest among major euro "
            "area economies. The current account records a slight deficit of -0.1% of GDP. "
            "Unemployment rises marginally to 7.6%. France is mentioned as one of the countries where "
            "public debt is on a significantly rising trajectory. Debt refinancing stands at 12.2% "
            "of GDP. The fiscal balance deteriorates along with the broader euro area."
        ),
        "ITA": (
            "Italy grows 0.5% in 2025 and 0.8% in 2026, moderating from 0.7% in 2024, according to "
            "the October 2025 WEO. Inflation rises from 1.1% in 2024 to 1.7% in 2025 and 2.0% in "
            "2026. The current account surplus remains stable at 1.0% of GDP. Unemployment stands at "
            "6.7%. Italy is mentioned alongside Germany as a country where growth declined in the "
            "second quarter of 2025 within the euro area. Italy's debt refinancing needs are 18.1% "
            "of GDP, among the highest of major advanced economies."
        ),
        "CAN": (
            "Canada grows 1.2% in 2025 and 1.5% in 2026, according to the October 2025 WEO, a "
            "cumulative downward revision of 1.7 percentage points from the October 2024 WEO--the "
            "most pronounced among advanced economies. Inflation remains contained at 2.0% in "
            "2025-2026. The current account deficit widens to -1.4% of GDP. Unemployment rises "
            "to 6.9%. The sharp downward revision reflects the impact of the changing international "
            "trade landscape, with elevated tariffs and tariffs on non-USMCA-compliant products. "
            "Canada and Mexico made a negative contribution to US export growth in 2025, in contrast "
            "to the 2018-19 episode."
        ),

        # ===================== EMERGENTES =====================
        "AUS": (
            "Australia grows 1.8% in 2025 and 2.1% in 2026, improving from 1.0% in 2024, according "
            "to the October 2025 WEO. Inflation stands at 2.6% in 2025 and 3.0% in 2026. The current "
            "account deficit remains at -1.8% of GDP. Australia is mentioned in the Commodity Special "
            "Feature as an example of an advanced economy with a highly interconnected commodity sector "
            "(high NAVAS), implying stronger co-movement between aggregate consumption and commodity "
            "terms-of-trade shocks, similar to emerging market economies."
        ),
        "CHN": (
            "China is the second most analyzed economy in the October 2025 WEO. Growth decelerates "
            "from 5.0% in 2024 to 4.8% in 2025 and 4.2% in 2026. Inflation is virtually zero at "
            "0.0% in 2025, with persistent producer price deflation. The current account surplus rises "
            "to 3.3% of GDP in 2025. China is the country most affected by US tariffs and most "
            "exposed to additional tariffs under the report's scenario A (30 additional percentage "
            "points). Real effective exchange rate depreciation, export redirection toward Asia and "
            "Europe, and fiscal expansion partially offset the impact. However, the property sector "
            "remains unsettled more than four years after the bubble burst, and the economy teeters "
            "on the verge of a debt-deflation cycle. Manufacturing subsidies are generating significant "
            "resource misallocation. Rare earth export controls caused temporary price spikes. Fiscal "
            "policy is appropriately expansionary but unsustainable over the medium term."
        ),
        "IND": (
            "India maintains robust growth of 6.6% in 2025 and 6.2% in 2026 according to the October "
            "2025 WEO, supported by strong service sector expansion. Inflation drops significantly to "
            "2.8% in 2025 with downside surprises. The current account deficit widens slightly to "
            "-1.0% of GDP. India was revised upward for 2025 on carryover from a strong first "
            "quarter, but downward for 2026 due to the increase in the US effective tariff rate on "
            "Indian imports. The primary deficit is smaller than pre-pandemic. India appears in "
            "Figure 1.1 as one of the countries with the highest US effective tariff rates."
        ),
        "IDN": (
            "Indonesia grows 4.9% in both 2025 and 2026, virtually stable from 5.0% in 2024, "
            "according to the October 2025 WEO. Inflation falls to 1.8% in 2025 before rising to "
            "2.9% in 2026. The current account deficit stands at -1.1% of GDP. Indonesia is part "
            "of the ASEAN-5 group, which grows 4.2% in 2025 and is among the regions most affected "
            "by the evolution of effective tariff rates. ASEAN economies saw their growth forecasts "
            "closely track tariff trajectory."
        ),
        "RUS": (
            "Russia experiences a dramatic slowdown according to the October 2025 WEO: growth falls "
            "from 4.3% in 2024 to just 0.6% in 2025 and 1.0% in 2026. Inflation stands at 9.0% in "
            "2025 and falls to 5.2% in 2026. The 0.9 percentage point downward revision for 2025 "
            "from April is due to the concentration of fiscal expenditures in Q4 2024, whose payback "
            "is incorporated into 2025 projections. The current account surplus declines to 1.7% of "
            "GDP. Russia is mentioned as an OPEC+ member participating in the accelerated oil "
            "production schedule. Peace negotiations with Ukraine have stalled."
        ),
        "SAU": (
            "Saudi Arabia grows 4.0% in both 2025 and 2026, accelerating significantly from 2.0% in "
            "2024, according to the October 2025 WEO. Inflation remains low at 2.1% in 2025. The "
            "current account shifts to a deficit of -2.1% of GDP in 2025. The 1.0 percentage point "
            "upward revision for 2025 from April is due to faster-than-expected unwinding of OPEC+ "
            "oil production cuts. Saudi Arabia is identified as the main driver of the upward "
            "revision for the Middle East and Central Asia region, alongside Egypt."
        ),
        "ZAF": (
            "South Africa grows 1.1% in 2025 and 1.2% in 2026, improving slightly from 0.5% in "
            "2024, according to the October 2025 WEO. Inflation stands at 3.4% in 2025 and 3.7% in "
            "2026. Unemployment remains extremely high at 32.7%. The Commodity Special Feature "
            "extensively analyzes South Africa as a case study: despite being a net commodity exporter "
            "with a sector of similar size to Kazakhstan's (39% of GDP), its lower interconnectedness "
            "(NAVAS of 0.73 vs 0.90) means commodity price shocks can have a counterintuitively "
            "negative effect on aggregate consumption."
        ),
        "KOR": (
            "South Korea grows 0.9% in 2025 and 1.8% in 2026, decelerating significantly from 2.0% "
            "in 2024, according to the October 2025 WEO. Inflation moderates to 2.0% in 2025. The "
            "current account surplus stands at 4.8% of GDP. The report notes that Korean automobile "
            "export prices showed a similar pattern to Japan's, with significant declines in prices "
            "destined for North America as a consequence of tariffs."
        ),
        "TUR": (
            "Turkey grows 3.5% in 2025 and 3.7% in 2026, accelerating from 3.3% in 2024, according "
            "to the October 2025 WEO. Inflation decelerates markedly but remains very high: from "
            "58.5% in 2024 to 34.9% in 2025 and 24.7% in 2026. Projections were revised upward for "
            "both years on better-than-expected outturns and resilient domestic demand. Turkey appears "
            "in Figure 1.1 as one of the countries with the highest US effective tariff rates."
        ),
        "TWN": (
            "Taiwan Province of China grows 3.7% in 2025 and 2.1% in 2026, decelerating from 4.8% "
            "in 2024, according to the October 2025 WEO. Inflation remains low at 1.7% in 2025. The "
            "current account surplus is 13.8% of GDP, one of the highest in the world. As an advanced "
            "Asian economy, Taiwan faces global trade uncertainty and US tariffs affecting the region, "
            "but does not receive individual narrative mention in the chapter text."
        ),
        "SGP": (
            "Singapore grows 2.2% in 2025 and 1.8% in 2026, decelerating from 4.4% in 2024, "
            "according to the October 2025 WEO. Inflation is very low at 0.9% in 2025. The current "
            "account surplus remains at 17.4% of GDP. Singapore is part of the ASEAN-5 group, which "
            "faces the effects of US tariffs and the reconfiguration of global trade. The report does "
            "not include individual narrative mention of Singapore."
        ),
        "ARE": (
            "The United Arab Emirates grows 4.8% in 2025 and 5.0% in 2026, accelerating from 4.0% "
            "in 2024, according to the October 2025 WEO. Inflation remains low at 1.6% in 2025. The "
            "current account surplus stands at 13.2% of GDP. The UAE benefits from the unwinding of "
            "OPEC+ production cuts, with a higher production quota (0.3 mb/d additional) specifically "
            "mentioned in the Commodity Special Feature. The country is also included among oil "
            "exporters contributing to global current account imbalances."
        ),
        "PHL": (
            "The Philippines grows 5.4% in 2025 and 5.7% in 2026, a slight deceleration from 5.7% "
            "in 2024, according to the October 2025 WEO. Inflation drops significantly to 1.6% in "
            "2025, having surprised to the downside relative to IMF projections. The current account "
            "deficit improves slightly to -3.8% of GDP. The Philippines is part of the ASEAN-5 group, "
            "where the evolution of growth forecasts closely tracked the trajectory of US effective "
            "tariff rates."
        ),
        "VNM": (
            "Vietnam grows 6.5% in 2025 and 5.6% in 2026, decelerating from 7.1% in 2024, according "
            "to the October 2025 WEO. Inflation remains moderate at 3.4% in 2025. The current account "
            "surplus declines from 6.6% to 4.0% of GDP. Vietnam is mentioned in the Commodity Special "
            "Feature: despite having an energy sector of similar size to Norway's, its lower "
            "interconnectedness with the rest of the economy (NAVAS of 0.48 vs 0.94) implies a lower "
            "correlation between energy price shocks and aggregate consumption."
        ),
        "MYS": (
            "Malaysia grows 4.5% in 2025 and 4.0% in 2026, decelerating from 5.1% in 2024, according "
            "to the October 2025 WEO. Inflation remains low at 1.6% in 2025, having surprised to the "
            "downside. The current account surplus stands at 1.5% of GDP. Malaysia is part of the "
            "ASEAN-5 group and the emerging Asia category, where inflation was lower than expected. "
            "The Asian region faces the effects of tariffs and the reconfiguration of global trade."
        ),
        "EGY": (
            "Egypt grows 4.3% in 2025 and 4.5% in 2026, accelerating from 2.4% in 2024, according to "
            "the October 2025 WEO. Inflation decelerates from 33.3% in 2024 to 20.4% in 2025 and "
            "11.8% in 2026. The current account deficit improves from -5.4% to -5.1% of GDP. The "
            "report specifically mentions that Egypt's first-half 2025 outturn was better than "
            "expected, contributing to the upward revision for the Middle East and Central Asia "
            "region, alongside Saudi Arabia."
        ),
        "NGA": (
            "Nigeria grows 3.9% in 2025 and 4.2% in 2026, according to the October 2025 WEO. "
            "Inflation remains very high at 23.0% in 2025 and 22.0% in 2026, though declining from "
            "31.4% in 2024. The current account surplus declines to 5.7% of GDP. Nigeria's national "
            "accounts were revised and rebased with 2019 as the new base year, increasing GDP level "
            "by 40.8%. Growth was revised upward on supportive domestic factors including higher oil "
            "production, improved investor confidence, a supportive fiscal stance in 2026, and the "
            "country's limited exposure to higher US tariffs. Nigeria is also included among oil "
            "exporters in global imbalances."
        ),
    },
}
