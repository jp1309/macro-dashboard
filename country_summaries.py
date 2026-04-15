"""
Country summaries extracted from IMF World Economic Outlook, April 2026.
Source: "Global Economy in the Shadow of War"
All data and analysis based exclusively on the WEO April 2026 PDFs and API data.

Context: The April 2026 WEO is published against the backdrop of a new military conflict
in the Middle East that erupted in late February 2026, adding to ongoing uncertainty from
US trade policies (tariffs, USMCA review due July 2026) and geopolitical tensions.
LATAM growth: 2.4% (2025), 2.3% (2026), 2.7% (2027).
"""

COUNTRY_SUMMARIES = {
    "es": {
        # ===================== LATAM =====================
        "ARG": (
            "Según el WEO de abril 2026, Argentina registró una contracción del PIB de –1,3% en 2024, "
            "pero muestra un fuerte repunte con un crecimiento de 4,4% en 2025 y proyecciones de 3,5% "
            "en 2026 y 4,0% en 2027. La inflación continúa su marcada desaceleración: de 219,9% en 2024 "
            "a 41,9% en 2025, 30,4% en 2026 y 15,7% en 2027. La cuenta corriente pasa de un superávit "
            "de 0,9% del PIB en 2024 a un déficit de –1,1% en 2025 y –0,8% en 2026. El desempleo sube "
            "ligeramente a 7,4% en 2025. Argentina es mencionada en el informe como uno de los "
            "principales productores de cereales, con exportaciones agrícolas que contribuyen al "
            "comercio global de alimentos. El conflicto en Medio Oriente tiene implicaciones "
            "heterogéneas para la región, aunque Argentina podría beneficiarse de precios de materias "
            "primas agrícolas más elevados."
        ),
        "BOL": (
            "El WEO de abril 2026 proyecta una contracción del PIB de Bolivia de –1,1% en 2024, "
            "que se profundiza a –1,2% en 2025 y –3,3% en 2026, sin datos publicados para 2027. "
            "La inflación se dispara de 5,1% en 2024 a 19,5% en 2025 y 20,7% en 2026, señalando "
            "presiones de precios severas. La cuenta corriente mejora de –2,4% del PIB en 2024 a "
            "–1,9% en 2025, recuperando superávit de 1,2% en 2026. El desempleo sube de 3,7% a "
            "4,5% en 2026. La ausencia de proyecciones para 2027 y la persistente recesión "
            "reflejan un alto grado de incertidumbre e inestabilidad macroeconómica en Bolivia."
        ),
        "BRA": (
            "Brasil es una de las economías emergentes más analizadas en el WEO de abril 2026. "
            "El crecimiento se desacelera de 3,4% en 2024 a 2,3% en 2025 y 1,9% en 2026, antes de "
            "repuntar a 2,0% en 2027. El informe destaca que el conflicto en Medio Oriente tiene un "
            "pequeño efecto neto positivo en Brasil en 2026 (aproximadamente +0,2 puntos porcentuales) "
            "dado que el país es exportador neto de energía. La inflación sube de 4,4% en 2024 a 5,0% "
            "en 2025, antes de moderarse a 4,0% en 2026 y 3,4% en 2027. El déficit de cuenta corriente "
            "se estabiliza en torno a –3,0% del PIB en 2025, mejorando a –2,7% en 2026. El desempleo "
            "baja a 6,0% en 2025. El texto señala que las reservas internacionales adecuadas, la baja "
            "dependencia de deuda en moneda extranjera, grandes reservas fiscales y un tipo de cambio "
            "flexible ayudan al país a absorber el choque externo. Para 2027, la demanda global más débil, "
            "mayores costos de insumos (incluidos fertilizantes) y condiciones financieras más restrictivas "
            "reducirían el crecimiento aproximadamente 0,3 puntos respecto a enero 2026."
        ),
        "CHL": (
            "Chile registra un crecimiento del PIB de 2,6% en 2024, que se modera a 2,3% en 2025 "
            "y se mantiene en 2,4% en 2026, subiendo a 2,6% en 2027, según el WEO de abril 2026. "
            "La inflación sube de 3,9% en 2024 a 4,2% en 2025, antes de descender a 2,9% en 2026 "
            "y 3,3% en 2027. La cuenta corriente mejora significativamente: el déficit se reduce de "
            "–1,5% del PIB en 2024 a –2,3% en 2025, pero se estrecha drásticamente a –0,8% en 2026. "
            "El desempleo se mantiene en torno al 8,5%. Chile, como economía abierta con fuerte "
            "dependencia del cobre, enfrenta los efectos del conflicto en Medio Oriente a través de "
            "las presiones en precios de energía y la incertidumbre comercial del entorno global."
        ),
        "COL": (
            "Según el WEO de abril 2026, Colombia registra un crecimiento del PIB de 1,5% en 2024, "
            "que se acelera a 2,6% en 2025 y 2,3% en 2026, antes de subir a 2,5% en 2027. La "
            "inflación se desacelera de 6,6% en 2024 a 5,1% en 2025, aunque repunta a 5,9% en 2026 "
            "antes de moderarse a 5,2% en 2027, reflejando las presiones del conflicto global sobre "
            "precios de energía y alimentos. El déficit de cuenta corriente se amplía de –1,7% del "
            "PIB en 2024 a –2,4% en 2025 y –2,5% en 2026. El desempleo baja de 9,1% a 8,0% en 2025, "
            "aunque vuelve a subir a 9,0% en 2026. Colombia enfrenta los efectos heterogéneos del "
            "conflicto en Medio Oriente sobre los precios de energía y la incertidumbre comercial global."
        ),
        "CRI": (
            "Según el WEO de abril 2026, Costa Rica registra un crecimiento del PIB de 4,1% en 2024, "
            "que se acelera a 4,6% en 2025 y se modera a 3,6% en 2026 y 2027. La inflación es "
            "negativa: –0,4% en 2024, –0,1% en 2025 y –0,4% en 2026, antes de subir a 2,0% en 2027. "
            "El déficit de cuenta corriente mejora de –0,9% del PIB en 2024 a –0,7% en 2025, antes "
            "de ampliarse a –1,5% en 2026 y –1,6% en 2027. El desempleo baja de 6,9% en 2024 a "
            "6,3% en 2025. Como parte del grupo CAPDR, Costa Rica mantiene fundamentos "
            "macroeconómicos sólidos aunque enfrenta los efectos indirectos del conflicto en Medio "
            "Oriente, la incertidumbre comercial global y las restricciones migratorias de EE.UU. "
            "sobre los flujos de remesas."
        ),
        "CUB": (
            "Cuba no cuenta con proyecciones individuales en el WEO de abril 2026. El informe "
            "titulado 'Global Economy in the Shadow of War' describe un entorno de incertidumbre "
            "elevada para la región de América Latina y el Caribe, con crecimiento proyectado de "
            "2,4% en 2025 y 2,3% en 2026. La economía cubana enfrenta los desafíos regionales "
            "comunes: restricciones al flujo de ayuda internacional, limitaciones en el espacio "
            "fiscal y los efectos del conflicto en Medio Oriente sobre precios de energía y "
            "alimentos a nivel global."
        ),
        "DOM": (
            "Según el WEO de abril 2026, la República Dominicana registra un sólido crecimiento de "
            "5,0% en 2024, que se modera a 2,1% en 2025 antes de repuntar a 3,7% en 2026 y 4,4% "
            "en 2027. La inflación sube de 3,3% en 2024 a 3,9% en 2025 y 5,1% en 2026, reflejando "
            "presiones externas globales. La cuenta corriente mejora de –3,3% del PIB en 2024 a "
            "–1,2% en 2025 y –1,5% en 2026. El desempleo se mantiene en torno al 5,1-5,3%. Como "
            "parte del grupo CAPDR, la República Dominicana enfrenta los efectos del conflicto en "
            "Medio Oriente sobre los precios de combustibles importados y los cambios en las "
            "políticas migratorias de EE.UU. que pueden impactar los flujos de remesas."
        ),
        "ECU": (
            "Ecuador registra una contracción de –1,9% del PIB en 2024, pero el WEO de abril 2026 "
            "proyecta un fuerte repunte con un crecimiento de 3,7% en 2025 y 2,5% en 2026 y 2027. "
            "La inflación se mantiene muy baja: 1,5% en 2024, 0,7% en 2025, 2,9% en 2026 y 1,6% "
            "en 2027. El superávit de cuenta corriente es notable: 5,7% del PIB en 2024, 5,8% en "
            "2025 y 5,2% en 2026. El desempleo mejora levemente de 3,4% a 3,1% en 2025. Como "
            "economía dolarizada y exportadora de petróleo, Ecuador podría beneficiarse del alza "
            "de precios del crudo asociada al conflicto en Medio Oriente, aunque el informe señala "
            "que los efectos del conflicto son heterogéneos según la posición neta energética de "
            "cada economía y el riesgo de contagio financiero."
        ),
        "SLV": (
            "Según el WEO de abril 2026, El Salvador registra un crecimiento del PIB de 2,6% en 2024, "
            "que se acelera a 3,7% en 2025 y 3,3% en 2026, antes de moderarse a 3,0% en 2027. La "
            "inflación es muy baja: 0,9% en 2024, 0,3% en 2025, 2,5% en 2026 y 2,0% en 2027. El "
            "déficit de cuenta corriente se deteriora de –1,8% del PIB en 2024 a –3,9% en 2025 y "
            "–3,3% en 2026. El desempleo baja de 4,7% a 4,2-4,3% en 2025-2026. Como economía "
            "dolarizada, El Salvador se ve afectada por los precios de combustibles importados y "
            "enfrenta los efectos de las políticas migratorias restrictivas de EE.UU. sobre los "
            "flujos de remesas, un recurso significativo para la economía salvadoreña."
        ),
        "GTM": (
            "Según el WEO de abril 2026, Guatemala registra un crecimiento del PIB de 3,7% en 2024, "
            "que se acelera a 4,1% en 2025 y se modera a 3,9% en 2026 y 4,0% en 2027. La inflación "
            "es baja: 2,9% en 2024, 1,6% en 2025, 2,6% en 2026 y 4,0% en 2027. El superávit de "
            "cuenta corriente sube de 2,9% del PIB en 2024 a 4,8% en 2025, antes de moderarse a "
            "3,2% en 2026. Guatemala, como parte del grupo CAPDR y receptor significativo de "
            "remesas, enfrenta los efectos de las políticas migratorias más restrictivas de EE.UU. "
            "y los impactos heterogéneos del conflicto en Medio Oriente sobre el entorno regional."
        ),
        "GUY": (
            "Según el WEO de abril 2026, Guyana registra un crecimiento extraordinario del PIB de "
            "43,8% en 2024 y 19,3% en 2025, impulsado por el auge de la producción petrolera. El "
            "crecimiento se modera a 16,2% en 2026 pero repunta a 19,7% en 2027 con nuevos proyectos. "
            "La inflación se mantiene contenida: 2,9% en 2024, 3,3% en 2025 y 4,1% en 2026. El "
            "superávit de cuenta corriente es notable: 16,5% del PIB en 2024, 12,9% en 2025 y 21,5% "
            "en 2026. El alza de precios del crudo asociada al conflicto en Medio Oriente podría "
            "beneficiar adicionalmente los ingresos fiscales y externos de Guyana, que es el "
            "principal impulsor del crecimiento del grupo del Caribe."
        ),
        "HTI": (
            "Según el WEO de abril 2026, Haití continúa en recesión con una contracción del PIB de "
            "–4,2% en 2024, que se atenúa a –2,7% en 2025 y –1,7% en 2026, antes de alcanzar un "
            "crecimiento positivo de 0,5% en 2027. La inflación es muy elevada: 25,8% en 2024, 28,3% "
            "en 2025, 23,5% en 2026 y 19,7% en 2027. La cuenta corriente mejora de –0,6% del PIB en "
            "2024 a 1,9% en 2025. Como economía frágil altamente vulnerable, Haití se ve "
            "especialmente afectada por el alza de precios de energía y alimentos vinculada al "
            "conflicto en Medio Oriente, los recortes de ayuda al desarrollo internacional y las "
            "políticas migratorias más restrictivas que amenazan los flujos de remesas."
        ),
        "HND": (
            "Según el WEO de abril 2026, Honduras registra un crecimiento del PIB de 3,6% en 2024 "
            "y 2025, que se modera a 3,3% en 2026 y 3,7% en 2027. La inflación se mantiene estable: "
            "4,6% en 2024 y 2025, bajando a 4,4% en 2026. La cuenta corriente muestra un déficit de "
            "–4,4% del PIB en 2024, mejorando notablemente a un superávit de 2,4% en 2025, antes de "
            "retornar a déficit de –2,6% en 2026. El desempleo sube de 5,2% a 5,9% en 2025 y 6,8% "
            "en 2026. Como parte del grupo CAPDR, Honduras enfrenta riesgos relacionados con las "
            "restricciones migratorias de EE.UU. sobre las remesas y el alza de precios de energía "
            "y alimentos derivada del conflicto en Medio Oriente."
        ),
        "JAM": (
            "Según el WEO de abril 2026, Jamaica registra una leve contracción del PIB de –0,5% "
            "en 2024 y –0,1% en 2025, y entra en recesión de –1,2% en 2026 antes de recuperarse "
            "con 3,1% en 2027. La inflación sube de 5,5% en 2024 a 3,9% en 2025 y 6,1% en 2026. "
            "La cuenta corriente pasa de superávit de 2,9% del PIB en 2024 y 1,2% en 2025, a "
            "déficit de –6,0% en 2026. El desempleo baja de 4,2% a 3,4% en 2025. El impacto del "
            "conflicto en Medio Oriente sobre los precios de energía es especialmente relevante "
            "para Jamaica, que depende de combustibles importados para su generación eléctrica."
        ),
        "MEX": (
            "México es una de las economías más destacadas en el WEO de abril 2026. El crecimiento "
            "desacelera de 1,4% en 2024 a apenas 0,6% en 2025, pero se proyecta una recuperación "
            "a 1,6% en 2026 y 2,2% en 2027. El informe indica que la debilidad de 2025 refleja "
            "la consolidación fiscal, la política monetaria restrictiva y los vientos en contra "
            "comerciales. La inflación baja de 4,7% en 2024 a 3,8% en 2025 y se mantiene en 3,9% "
            "en 2026. El déficit de cuenta corriente es reducido: –0,9% del PIB en 2024 y –0,4% "
            "en 2025 y 2026. El desempleo sube levemente de 2,7% a 2,6% en 2025. México es "
            "especialmente relevante por la revisión obligatoria del USMCA prevista para julio 2026 "
            "y la extensión de los aranceles de la Sección 122 de EE.UU., que requieren aprobación "
            "del Congreso. El informe señala que los acuerdos comerciales de EE.UU. con socios clave "
            "como México proporcionan solo alivio temporal y vencen a finales de 2026."
        ),
        "NIC": (
            "Según el WEO de abril 2026, Nicaragua registra un crecimiento del PIB de 3,6% en 2024, "
            "que se acelera a 4,9% en 2025 y se modera a 3,8% en 2026 y 2027. La inflación baja de "
            "4,6% en 2024 a 2,1% en 2025, subiendo a 3,5% en 2026. El superávit de cuenta corriente "
            "es notable: 4,2% del PIB en 2024, aumentando a 8,6% en 2025 y 6,4% en 2026. El "
            "desempleo baja de 3,1% a 2,7% en 2025. Como parte del grupo CAPDR, Nicaragua comparte "
            "los desafíos regionales derivados de la incertidumbre comercial global, los cambios en "
            "políticas migratorias y el impacto del conflicto en Medio Oriente sobre los precios "
            "internacionales de energía y alimentos."
        ),
        "PAN": (
            "Según el WEO de abril 2026, Panamá registra un crecimiento del PIB de 2,7% en 2024, "
            "que se acelera a 4,4% en 2025 y se modera a 3,8% en 2026 y 4,5% en 2027. La inflación "
            "es muy baja: 0,7% en 2024, prácticamente nula (0,0%) en 2025, y 1,4% en 2026. La "
            "cuenta corriente pasa de un superávit de 0,7% del PIB en 2024 a 0,3% en 2025, y "
            "retorna a déficit de –1,5% en 2026. El desempleo sube de 9,5% a 10,4% en 2025. Panamá, "
            "como hub logístico vinculado al comercio internacional a través del Canal, enfrenta los "
            "efectos del conflicto en Medio Oriente sobre las rutas de transporte marítimo y las "
            "tensiones comerciales globales que podrían afectar los flujos de tránsito del Canal."
        ),
        "PRY": (
            "Paraguay registra un crecimiento de 4,7% en 2024 y un sólido 6,0% en 2025, que se "
            "modera a 4,2% en 2026 y 3,5% en 2027, según el WEO de abril 2026, por encima del "
            "promedio regional de América Latina. La inflación se mantiene moderada: 3,8% en 2024, "
            "4,1% en 2025 y 3,3% en 2026. El déficit de cuenta corriente se sitúa en –3,5% del PIB "
            "en 2025, mejorando a –3,0% en 2026. El desempleo mejora de 5,8% a 5,2% en 2025. "
            "Paraguay enfrenta los desafíos derivados de la incertidumbre comercial global y los "
            "efectos del conflicto en Medio Oriente sobre los precios de materias primas agrícolas."
        ),
        "PER": (
            "Perú muestra un crecimiento del PIB de 3,5% en 2024 y 3,4% en 2025, que se modera a "
            "2,8% en 2026 y 2027, según el WEO de abril 2026. La inflación es notablemente baja "
            "para la región: 2,4% en 2024, 1,5% en 2025 y 2,5% en 2026. El superávit de cuenta "
            "corriente mejora de 2,2% del PIB en 2024 a 3,1% en 2025 y 3,4% en 2026. El desempleo "
            "baja de 6,4% a 5,9% en 2025. Como exportador de materiales críticos como el cobre, "
            "Perú podría verse afectado por los cambios en la demanda global derivados del conflicto "
            "en Medio Oriente y la desaceleración del crecimiento en sus principales socios comerciales."
        ),
        "URY": (
            "Uruguay registra un crecimiento de 3,3% en 2024 que se desacelera a 1,8% en 2025 y "
            "2026, antes de repuntar a 2,6% en 2027, según el WEO de abril 2026. La inflación se "
            "modera ligeramente: 4,8% en 2024, 4,7% en 2025 y 4,0% en 2026. El déficit de cuenta "
            "corriente se mantiene reducido en torno a –0,5% a –0,8% del PIB. El desempleo sube de "
            "8,2% a 7,5% en 2025 y 8,0% en 2026. Como economía abierta con sólidos fundamentos, "
            "Uruguay enfrenta los desafíos comunes de la región derivados de la incertidumbre "
            "comercial y los efectos del conflicto en Medio Oriente sobre el entorno global."
        ),
        "VEN": (
            "Venezuela presenta uno de los cuadros macroeconómicos más difíciles en el WEO de "
            "abril 2026. El crecimiento baja de 5,3% en 2024 a 1,5% en 2025, con proyecciones de "
            "4,0% en 2026 y 6,0% en 2027. La inflación se dispara de 49,4% en 2024 a 252,0% en "
            "2025 y 387,4% en 2026, antes de bajar a 94,4% en 2027. La cuenta corriente muestra "
            "un superávit de 4,1% del PIB en 2024, cayendo a 2,6% en 2025 y recuperándose a 7,1% "
            "en 2026. El FMI excluye a Venezuela de los agregados de inflación de mercados emergentes "
            "por la magnitud de sus distorsiones. El alza de precios del petróleo vinculada al "
            "conflicto en Medio Oriente podría beneficiar los ingresos externos venezolanos."
        ),
        "BLZ": (
            "Según el WEO de abril 2026, Belice registra un crecimiento del PIB de 3,5% en 2024, "
            "que se desacelera a 2,7% en 2025 y 2,2% en 2026. La inflación baja de 3,3% en 2024 a "
            "1,1% en 2025 y 1,5% en 2026. El déficit de cuenta corriente se amplía de –1,9% del "
            "PIB en 2024 a –3,5% en 2025 y –4,5% en 2026. Como pequeña economía abierta del Caribe, "
            "Belice comparte los desafíos regionales de espacio fiscal limitado, vulnerabilidad a "
            "choques climáticos y los efectos del conflicto en Medio Oriente sobre los precios "
            "internacionales de combustibles importados y la incertidumbre del entorno global."
        ),
        "SUR": (
            "Según el WEO de abril 2026, Surinam registra un crecimiento del PIB de 1,7% en 2024 "
            "y 1,5% en 2025, que se acelera a 3,9% en 2026 y 4,4% en 2027. La inflación baja de "
            "16,2% en 2024 a 9,2% en 2025, antes de subir a 11,8% en 2026. Lo más notable es el "
            "dramático deterioro de la cuenta corriente: de –12,9% del PIB en 2024, se profundiza "
            "a –53,3% en 2025 y –44,8% en 2026, reflejando las masivas inversiones en nuevos "
            "proyectos petroleros. El alza de precios del crudo derivada del conflicto en Medio "
            "Oriente podría mejorar las perspectivas de ingresos de los proyectos petroleros en "
            "desarrollo, aunque el déficit de cuenta corriente refleja la intensidad inversora del "
            "período de construcción."
        ),
        "TTO": (
            "Según el WEO de abril 2026, Trinidad y Tobago registra un crecimiento del PIB de 2,5% "
            "en 2024, que se desacelera a 0,8% en 2025 y 2026, antes de recuperarse a 3,0% en 2027. "
            "La inflación es baja: 0,5% en 2024, 1,0% en 2025 y 1,8% en 2026. La cuenta corriente "
            "muestra un superávit sólido de 2,5% del PIB en 2024, mejorando a 3,1% en 2025 y 3,8% "
            "en 2026. El desempleo baja de 5,5% a 4,0% en 2025. Como exportador de energía, Trinidad "
            "y Tobago podría beneficiarse del alza de precios del petróleo y gas natural asociada al "
            "conflicto en Medio Oriente, que el informe proyecta en 21,4% en 2026 respecto a 2025."
        ),

        # ===================== G7 =====================
        "USA": (
            "Estados Unidos es la economía más analizada en el WEO de abril 2026. El crecimiento se "
            "desacelera de 2,8% en 2024 a 2,1% en 2025, pero se proyecta una recuperación a 2,3% "
            "en 2026 y 2,1% en 2027. El conflicto en Medio Oriente tiene un efecto neto positivo "
            "pequeño en EE.UU. dado su estatus de exportador neto de energía. La inflación sube de "
            "3,0% en 2024 a 2,7% en 2025 y 3,2% en 2026, reflejando las presiones de los aranceles "
            "y los precios de energía. El desempleo sube a 4,3% en 2025 y 4,4% en 2026. El déficit "
            "de cuenta corriente se reduce a –3,6% del PIB en 2025. El texto menciona el fallo sobre "
            "la IEEPA y sus implicaciones para los ingresos arancelarios, la revisión obligatoria del "
            "USMCA en julio 2026, y los acuerdos comerciales temporales que vencen a finales de 2026. "
            "La Ley OBBBA genera estímulo fiscal a corto plazo. La probabilidad de recesión se redujo "
            "pero la incertidumbre histórica sigue elevada. El crecimiento de la productividad "
            "tecnológica y la IA sostienen el crecimiento potencial."
        ),
        "JPN": (
            "Japón muestra un rebote del crecimiento a 1,2% en 2025, antes de moderarse a 0,7% en "
            "2026 y 0,6% en 2027, según el WEO de abril 2026. El consumo más fuerte e inversión "
            "impulsaron el repunte. La inflación sube de 2,7% en 2024 a 3,2% en 2025, moderándose "
            "a 2,2% en 2026. El superávit de cuenta corriente se sitúa en 4,8% del PIB en 2025. "
            "El informe señala que el conflicto en Medio Oriente tiene un efecto positivo en el "
            "crecimiento de Japón en 2026 gracias al mayor gasto gubernamental de compensación y "
            "al impulso más fuerte del crecimiento, que más que compensa el efecto negativo de "
            "los altos precios de energía para esta economía importadora neta de energía."
        ),
        "DEU": (
            "Alemania registró una contracción de –0,5% en 2024, recuperándose a 0,2% en 2025 y "
            "0,8% en 2026, antes de subir a 1,2% en 2027, según el WEO de abril 2026. La inflación "
            "sube de 2,5% en 2024 a 2,3% en 2025 y 2,7% en 2026. El superávit de cuenta corriente "
            "baja de 5,8% del PIB en 2024 a 4,4% en 2025 y 3,9% en 2026. El desempleo sube de "
            "3,4% a 3,8% en 2025. El impacto del conflicto en Medio Oriente en Alemania y la zona "
            "euro es negativo dado que son importadores netos de energía, con una revisión a la baja "
            "de –0,2 puntos porcentuales en 2026 respecto a la proyección base sin conflicto."
        ),
        "GBR": (
            "El Reino Unido crece 1,3% en 2025 pero se modera a 0,8% en 2026, antes de recuperarse "
            "a 1,3% en 2027, según el WEO de abril 2026. La inflación sube de 2,5% en 2024 a 3,4% "
            "en 2025 y 3,2% en 2026, persistiendo por encima del objetivo. El déficit de cuenta "
            "corriente se amplía a –3,1% y –3,4% del PIB en 2025 y 2026. El desempleo sube "
            "significativamente de 4,3% en 2024 a 4,8% en 2025 y 5,6% en 2026. El conflicto en "
            "Medio Oriente tiene un efecto negativo en el crecimiento del Reino Unido como "
            "importador neto de energía, con una revisión a la baja de –0,5 puntos para 2026."
        ),
        "FRA": (
            "Francia crece 0,9% en 2025 y mantiene ese ritmo en 2026 y 2027, según el WEO de "
            "abril 2026. La inflación baja a 0,9% en 2025, la más baja entre las grandes economías "
            "del área euro, subiendo a 1,8% en 2026. La cuenta corriente pasa de un leve superávit "
            "de 0,1% del PIB en 2024 a déficit de –0,4% en 2025 y –0,3% en 2026. El desempleo sube "
            "de 7,4% en 2024 a 7,6% en 2025 y 7,9% en 2026. Como importador neto de energía, "
            "Francia enfrenta el efecto negativo del conflicto en Medio Oriente sobre los costos "
            "energéticos, con una revisión a la baja de –0,3 puntos porcentuales para 2026."
        ),
        "ITA": (
            "Italia crece 0,8% en 2024 y 0,5% en 2025, manteniéndose en 0,5% en 2026 y 2027, "
            "según el WEO de abril 2026. La inflación sube de 1,1% en 2024 a 1,6% en 2025 y "
            "2,6% en 2026, presionada por los precios de energía vinculados al conflicto en Medio "
            "Oriente. El superávit de cuenta corriente se reduce de 1,1% del PIB en 2024 a 1,2% "
            "en 2025 y 0,6% en 2026. El desempleo baja de 6,6% en 2024 a 6,0% en 2025. El "
            "impacto del conflicto en Medio Oriente en Italia es negativo, con una revisión a la "
            "baja de –0,2 puntos porcentuales en 2026 respecto al escenario sin conflicto. Las "
            "necesidades de refinanciamiento de deuda pública de Italia son entre las más altas "
            "de las economías avanzadas."
        ),
        "CAN": (
            "Canadá crece 2,0% en 2024 y 1,7% en 2025, moderándose a 1,5% en 2026 y repuntando "
            "a 1,9% en 2027, según el WEO de abril 2026. La inflación se mantiene contenida: 2,4% "
            "en 2024, 2,1% en 2025 y 2,5% en 2026. El déficit de cuenta corriente es reducido: "
            "–0,5% del PIB en 2024, ampliándose a –0,9% en 2025 y estrechándose a –0,2% en 2026. "
            "El desempleo sube de 6,4% a 6,9% en 2025, mejorando a 6,5% en 2026. Canadá es "
            "especialmente relevante por la revisión obligatoria del USMCA prevista para julio "
            "2026. El informe señala que los acuerdos comerciales de EE.UU. con socios como Canadá "
            "y México proporcionan solo alivio temporal y vencen a finales de 2026."
        ),

        # ===================== EMERGENTES =====================
        "AUS": (
            "Australia crece 1,0% en 2024 y 2,0% en 2025 y 2026, según el WEO de abril 2026. La "
            "inflación sube de 3,2% en 2024 a 2,9% en 2025 y 4,0% en 2026, presionada por el "
            "contexto de precios de materias primas. El déficit de cuenta corriente se mantiene en "
            "torno a –2,2-2,6% del PIB. El desempleo se sitúa en 4,0-4,2%. Australia, como "
            "economía con fuerte sector de materias primas, se ve afectada por los cambios en los "
            "precios globales derivados del conflicto en Medio Oriente y la evolución de la demanda "
            "de sus principales socios comerciales en Asia."
        ),
        "CHN": (
            "China es la segunda economía más analizada en el WEO de abril 2026. El crecimiento se "
            "mantiene en 5,0% en 2024 y 2025, desacelerándose a 4,4% en 2026 y 4,0% en 2027. La "
            "inflación es prácticamente nula: 0,2% en 2024, 0,0% en 2025, antes de subir a 1,2% "
            "en 2026. El superávit de cuenta corriente es de 2,2% del PIB en 2024 y sube a 3,7% "
            "en 2025. El informe señala que la actividad doméstica china —especialmente en el "
            "sector inmobiliario— rezaga respecto a las exportaciones. El comercio de mercancías de "
            "China marcó un superávit récord de 1,2 billones de dólares (6% del PIB) en 2025. Los "
            "controles de exportación de tierras raras y la reorientación de exportaciones hacia "
            "Asia y Europa son elementos clave. El conflicto en Medio Oriente agrega incertidumbre "
            "a las perspectivas de la demanda energética global."
        ),
        "IND": (
            "India mantiene un crecimiento robusto de 7,1% en 2024, acelerando a 7,6% en 2025 y "
            "moderándose a 6,5% en 2026 y 2027, según el WEO de abril 2026. La inflación baja "
            "significativamente de 4,6% en 2024 a 2,1% en 2025, antes de subir a 4,7% en 2026 "
            "en parte por las presiones del conflicto global sobre precios de energía y alimentos. "
            "El déficit de cuenta corriente es reducido: –0,6% del PIB en 2024, ampliándose a "
            "–2,0% en 2026. Como gran importadora neta de energía, India se ve afectada "
            "negativamente por el alza de precios del petróleo derivada del conflicto en Medio "
            "Oriente, que el informe señala como uno de los efectos de segundo orden sobre la "
            "inflación y las perspectivas de crecimiento."
        ),
        "IDN": (
            "Indonesia crece 5,0% en 2024, acelerando a 5,1% en 2025, y manteniéndose en 5,0% en "
            "2026 y 5,1% en 2027, según el WEO de abril 2026. La inflación baja de 2,3% en 2024 "
            "a 1,9% en 2025, antes de subir a 3,0% en 2026. El déficit de cuenta corriente mejora "
            "de –0,6% del PIB en 2024 a –0,1% en 2025, antes de ampliarse a –1,1% en 2026. El "
            "desempleo se mantiene en 4,8-4,9%. Indonesia forma parte del grupo ASEAN-5, que "
            "enfrenta los efectos combinados de los aranceles de EE.UU. y el impacto heterogéneo "
            "del conflicto en Medio Oriente sobre los precios de energía."
        ),
        "RUS": (
            "Rusia registra un crecimiento de 4,9% en 2024, que se desacelera drásticamente a 1,0% "
            "en 2025, estabilizándose en 1,1% en 2026 y 2027, según el WEO de abril 2026. La "
            "inflación se sitúa en 8,4% en 2024 y 8,7% en 2025, bajando a 5,6% en 2026. El "
            "superávit de cuenta corriente se reduce a 1,6% del PIB en 2025, recuperando 2,9% en "
            "2026. El desempleo es muy bajo, en 2,2-2,5%. El informe señala que los mayores precios "
            "de materias primas derivados del conflicto en Medio Oriente impulsan una revisión al "
            "alza de 0,3 puntos porcentuales en el crecimiento de 2026, siendo Rusia un beneficiario "
            "neto del alza de precios de energía."
        ),
        "SAU": (
            "Arabia Saudita crece 2,6% en 2024, acelerando a 4,5% en 2025 y moderándose a 3,1% en "
            "2026 y 4,5% en 2027, según el WEO de abril 2026. La inflación es baja: 1,5% en 2024, "
            "2,0% en 2025 y 2,3% en 2026. La cuenta corriente pasa de déficit de –1,3% del PIB en "
            "2024 a –3,0% en 2025 y –1,6% en 2026. El informe señala que Arabia Saudita es uno de "
            "los principales países afectados por el conflicto en Medio Oriente, con una revisión "
            "a la baja de –1,4 puntos en 2026 respecto al escenario sin conflicto. Sin embargo, "
            "el alza de precios del petróleo podría mejorar parcialmente los ingresos fiscales."
        ),
        "ZAF": (
            "Sudáfrica crece 0,5% en 2024 y 1,1% en 2025, antes de desacelerarse a 1,0% en 2026 "
            "y recuperarse a 1,3% en 2027, según el WEO de abril 2026. La inflación baja de 4,4% "
            "en 2024 a 3,2% en 2025, subiendo a 3,9% en 2026. El desempleo se mantiene "
            "extremadamente alto en torno a 32,4-32,6%. El déficit de cuenta corriente es reducido: "
            "–0,7% del PIB en 2024. El informe señala que el conflicto en Medio Oriente proyecta "
            "un enlentecimiento del crecimiento de Sudáfrica en 2026 y que se espera una "
            "recuperación en 2027 apoyada por la reanudación gradual de la inversión privada "
            "impulsada por reformas estructurales."
        ),
        "KOR": (
            "Corea del Sur crece 2,0% en 2024, desacelerándose a 1,0% en 2025 y recuperándose a "
            "1,9% en 2026 y 2,1% en 2027, según el WEO de abril 2026. La inflación se modera a "
            "2,1% en 2025 y 2,5% en 2026. El superávit de cuenta corriente aumenta a 6,6% del PIB "
            "en 2025. El desempleo se mantiene en 2,8%. Como economía exportadora de semiconductores "
            "y tecnología, Corea se beneficia del dinamismo del comercio tecnológico global, pero "
            "enfrenta el impacto del conflicto en Medio Oriente sobre los precios de energía "
            "importada y la incertidumbre en el entorno comercial."
        ),
        "TUR": (
            "Turquía crece 3,3% en 2024, acelerando a 3,6% en 2025 y manteniéndose en 3,4% en "
            "2026 y 3,5% en 2027, según el WEO de abril 2026. La inflación se desacelera "
            "marcadamente: de 58,5% en 2024 a 34,9% en 2025 y 28,6% en 2026. El déficit de cuenta "
            "corriente se amplía de –1,0% del PIB en 2024 a –1,9% en 2025 y –2,8% en 2026. El "
            "desempleo baja de 8,7% a 8,3% en 2025-2026. El informe indica que el crecimiento de "
            "Turquía es revisado a la baja 0,8 puntos para 2026 respecto a enero 2026, dado que "
            "el crecimiento de 2025 fue más débil de lo esperado y los altos precios de energía "
            "pesan sobre la actividad como importador neto de energía."
        ),
        "TWN": (
            "Taiwán registra un crecimiento de 5,3% en 2024 y un extraordinario 8,7% en 2025, "
            "que se modera a 5,2% en 2026 y 3,0% en 2027, según el WEO de abril 2026. La inflación "
            "se mantiene baja: 2,2% en 2024, 1,7% en 2025 y 1,5% en 2026. El superávit de cuenta "
            "corriente es muy elevado: 17,4% del PIB en 2025 y 18,1% en 2026. El desempleo es "
            "bajo en 3,4%. Taiwán es beneficiaria clave del auge del comercio de semiconductores "
            "y tecnología de IA global, siendo mencionada en el informe como uno de los países "
            "cuyas exportaciones a EE.UU. aumentaron significativamente como resultado de la "
            "reconfiguración de las cadenas de suministro globales."
        ),
        "SGP": (
            "Singapur crece 5,3% en 2024 y 5,0% en 2025, desacelerándose a 3,5% en 2026 y 2,7% "
            "en 2027, según el WEO de abril 2026. La inflación baja de 2,4% en 2024 a 0,9% en "
            "2025, subiendo a 2,3% en 2026. El superávit de cuenta corriente se mantiene muy "
            "elevado: 17,2% del PIB en 2024 y 16,7% en 2025. El desempleo es muy bajo en 1,9-2,0%. "
            "Singapur forma parte del grupo ASEAN-5 y se beneficia como hub financiero y logístico "
            "del dinamismo del comercio tecnológico en Asia, aunque el conflicto en Medio Oriente "
            "y la incertidumbre comercial global generan riesgos de desaceleración."
        ),
        "ARE": (
            "Los Emiratos Árabes Unidos crecen 4,0% en 2024, acelerando a 5,8% en 2025 y "
            "moderándose a 3,1% en 2026 y 5,3% en 2027, según el WEO de abril 2026. La inflación "
            "es baja: 1,7% en 2024, 1,3% en 2025 y 2,5% en 2026. El superávit de cuenta corriente "
            "es elevado: 15,4% del PIB en 2024 y 15,3% en 2025. Los EAU son uno de los países "
            "directamente más afectados por el conflicto en Medio Oriente iniciado a finales de "
            "febrero 2026, con impactos sobre la infraestructura crítica, el tráfico marítimo y "
            "aéreo, y el sentimiento de riesgo en los mercados financieros regionales."
        ),
        "PHL": (
            "Filipinas crece 5,7% en 2024, desacelerándose a 4,4% en 2025 y 4,1% en 2026, antes "
            "de repuntar a 5,8% en 2027, según el WEO de abril 2026. La inflación baja de 3,2% en "
            "2024 a 1,7% en 2025, subiendo a 4,3% en 2026. El déficit de cuenta corriente mejora "
            "de –4,0% del PIB en 2024 a –3,3% en 2025, antes de ampliarse a –4,4% en 2026. El "
            "desempleo sube de 3,8% a 4,2% en 2025 y 4,7% en 2026. Filipinas forma parte del "
            "grupo ASEAN-5 y enfrenta los efectos combinados de los aranceles de EE.UU. y el "
            "impacto del conflicto en Medio Oriente sobre los precios de energía importada."
        ),
        "VNM": (
            "Vietnam crece 7,0% en 2024 y un destacado 8,0% en 2025, que se modera a 7,1% en "
            "2026 y 6,7% en 2027, según el WEO de abril 2026. La inflación se mantiene moderada: "
            "3,6% en 2024, 3,3% en 2025 y 4,9% en 2026. El superávit de cuenta corriente se "
            "mantiene en 6,6-6,7% del PIB en 2024-2025. El desempleo es muy bajo en 2,1-2,2%. "
            "El informe señala que Vietnam es uno de los beneficiarios de la reconfiguración de "
            "las cadenas de suministro globales, con un aumento significativo de las exportaciones "
            "hacia EE.UU. a medida que las importaciones estadounidenses desde China caen "
            "y se redirigen."
        ),
        "MYS": (
            "Malasia crece 5,1% en 2024 y 5,2% en 2025, moderándose a 4,7% en 2026 y 4,3% en "
            "2027, según el WEO de abril 2026. La inflación se mantiene baja: 1,8% en 2024, 1,4% "
            "en 2025 y 1,9% en 2026. El superávit de cuenta corriente se sitúa en 1,4-1,6% del "
            "PIB. El desempleo mejora a 3,0% en 2025. Malasia forma parte del grupo ASEAN-5 y "
            "se beneficia del dinamismo del comercio tecnológico en Asia, aunque enfrenta los "
            "efectos de los aranceles de EE.UU. y la incertidumbre derivada del conflicto en "
            "Medio Oriente sobre el entorno energético y comercial global."
        ),
        "EGY": (
            "Egipto crece 2,4% en 2024, acelerando a 4,4% en 2025 y 4,2% en 2026, según el WEO "
            "de abril 2026. La inflación se desacelera de 33,3% en 2024 a 20,4% en 2025 y 13,2% "
            "en 2026. El déficit de cuenta corriente se mantiene en –5,4% del PIB en 2024 y –4,2% "
            "en 2025 y 2026. El desempleo baja de 7,4% a 7,3% en 2025. Egipto es uno de los "
            "países de Medio Oriente más afectados por el conflicto iniciado en febrero 2026, "
            "con impactos directos sobre el Canal de Suez, el turismo y los flujos de inversión "
            "extranjera directa en la región."
        ),
        "NGA": (
            "Nigeria crece 4,1% en 2024 y 4,0% en 2025, manteniéndose en 4,1% en 2026 y "
            "acelerando a 4,3% en 2027, según el WEO de abril 2026. La inflación se desacelera "
            "de 33,2% en 2024 a 23,0% en 2025 y 16,0% en 2026. El superávit de cuenta corriente "
            "se reduce de 6,8% del PIB en 2024 a 5,1% en 2025 y 5,8% en 2026. Como exportador "
            "de petróleo, Nigeria podría beneficiarse del alza de precios del crudo vinculada al "
            "conflicto en Medio Oriente. El informe no incluye mención narrativa individual de "
            "Nigeria, pero la sitúa entre los exportadores de petróleo del grupo África "
            "Subsahariana con revisión a la baja de –0,3 puntos en 2026."
        ),
    },
    "en": {
        # ===================== LATAM =====================
        "ARG": (
            "According to the April 2026 WEO, Argentina recorded a GDP contraction of -1.3% in 2024, "
            "but shows a strong rebound with growth of 4.4% in 2025 and projections of 3.5% in 2026 "
            "and 4.0% in 2027. Inflation continues its marked deceleration: from 219.9% in 2024 to "
            "41.9% in 2025, 30.4% in 2026, and 15.7% in 2027. The current account shifts from a "
            "surplus of 0.9% of GDP in 2024 to a deficit of -1.1% in 2025 and -0.8% in 2026. "
            "Unemployment rises slightly to 7.4% in 2025. Argentina is mentioned as a major cereal "
            "producer contributing to global food trade. The Middle East conflict has heterogeneous "
            "implications for the region, though Argentina could benefit from higher agricultural "
            "commodity prices."
        ),
        "BOL": (
            "The April 2026 WEO projects Bolivia's GDP to contract by -1.1% in 2024, deepening to "
            "-1.2% in 2025 and -3.3% in 2026, with no data published for 2027. Inflation surges from "
            "5.1% in 2024 to 19.5% in 2025 and 20.7% in 2026, signaling severe price pressures. The "
            "current account improves from -2.4% of GDP in 2024 to -1.9% in 2025, recovering a surplus "
            "of 1.2% in 2026. Unemployment rises from 3.7% to 4.5% in 2026. The absence of 2027 "
            "projections and persistent recession reflect a high degree of uncertainty and "
            "macroeconomic instability in Bolivia."
        ),
        "BRA": (
            "Brazil is one of the most analyzed emerging economies in the April 2026 WEO. Growth "
            "decelerates from 3.4% in 2024 to 2.3% in 2025 and 1.9% in 2026, before rebounding to "
            "2.0% in 2027. The report highlights that the Middle East conflict has a small net positive "
            "effect on Brazil in 2026 (approximately +0.2 percentage points) given that the country is "
            "a net energy exporter. Inflation rises from 4.4% in 2024 to 5.0% in 2025, before "
            "moderating to 4.0% in 2026 and 3.4% in 2027. The current account deficit stabilizes "
            "around -3.0% of GDP in 2025, improving to -2.7% in 2026. Unemployment falls to 6.0% in "
            "2025. The text notes that adequate international reserves, low reliance on foreign-currency "
            "debt, large government cash buffers, and a flexible exchange rate help the country absorb "
            "the external shock. For 2027, weaker global demand, higher input costs (including "
            "fertilizers), and tighter financial conditions are expected to reduce growth by about "
            "0.3 percentage points compared to the January 2026 projection."
        ),
        "CHL": (
            "Chile records GDP growth of 2.6% in 2024, moderating to 2.3% in 2025 and holding at "
            "2.4% in 2026, rising to 2.6% in 2027, according to the April 2026 WEO. Inflation rises "
            "from 3.9% in 2024 to 4.2% in 2025, before declining to 2.9% in 2026 and 3.3% in 2027. "
            "The current account deficit narrows dramatically to -0.8% of GDP in 2026 from -2.3% in "
            "2025. Unemployment remains around 8.5%. Chile, as an open economy highly dependent on "
            "copper, faces the effects of the Middle East conflict through energy price pressures and "
            "global trade uncertainty."
        ),
        "COL": (
            "According to the April 2026 WEO, Colombia records GDP growth of 1.5% in 2024, "
            "accelerating to 2.6% in 2025 and 2.3% in 2026, before rising to 2.5% in 2027. Inflation "
            "decelerates from 6.6% in 2024 to 5.1% in 2025, but rebounds to 5.9% in 2026 before "
            "moderating to 5.2% in 2027, reflecting global conflict pressures on energy and food prices. "
            "The current account deficit widens from -1.7% of GDP in 2024 to -2.4% in 2025 and -2.5% "
            "in 2026. Unemployment falls from 9.1% to 8.0% in 2025, but rises again to 9.0% in 2026. "
            "Colombia faces the heterogeneous effects of the Middle East conflict on energy prices and "
            "global trade uncertainty."
        ),
        "CRI": (
            "According to the April 2026 WEO, Costa Rica records GDP growth of 4.1% in 2024, "
            "accelerating to 4.6% in 2025 and moderating to 3.6% in 2026 and 2027. Inflation is "
            "negative: -0.4% in 2024, -0.1% in 2025, and -0.4% in 2026, before rising to 2.0% in "
            "2027. The current account deficit improves from -0.9% of GDP in 2024 to -0.7% in 2025, "
            "before widening to -1.5% in 2026 and -1.6% in 2027. Unemployment falls from 6.9% in "
            "2024 to 6.3% in 2025. As part of the CAPDR group, Costa Rica maintains solid "
            "macroeconomic fundamentals but faces indirect effects from the Middle East conflict, "
            "global trade uncertainty, and US immigration restrictions affecting remittance flows."
        ),
        "CUB": (
            "Cuba has no individual projections in the April 2026 WEO. The report titled 'Global "
            "Economy in the Shadow of War' describes a high-uncertainty environment for the Latin "
            "America and Caribbean region, with projected growth of 2.4% in 2025 and 2.3% in 2026. "
            "The Cuban economy faces common regional challenges: restrictions on international aid "
            "flows, fiscal space limitations, and the effects of the Middle East conflict on global "
            "energy and food prices."
        ),
        "DOM": (
            "According to the April 2026 WEO, the Dominican Republic records solid GDP growth of "
            "5.0% in 2024, moderating to 2.1% in 2025 before rebounding to 3.7% in 2026 and 4.4% "
            "in 2027. Inflation rises from 3.3% in 2024 to 3.9% in 2025 and 5.1% in 2026, reflecting "
            "global external pressures. The current account improves from -3.3% of GDP in 2024 to "
            "-1.2% in 2025 and -1.5% in 2026. Unemployment remains around 5.1-5.3%. As part of the "
            "CAPDR group, the Dominican Republic faces the effects of the Middle East conflict on "
            "imported fuel prices and US immigration policy changes that may impact remittance flows."
        ),
        "ECU": (
            "Ecuador records a GDP contraction of -1.9% in 2024, but the April 2026 WEO projects a "
            "strong rebound with growth of 3.7% in 2025 and 2.5% in 2026 and 2027. Inflation remains "
            "very low: 1.5% in 2024, 0.7% in 2025, 2.9% in 2026, and 1.6% in 2027. The current "
            "account surplus is notable: 5.7% of GDP in 2024, 5.8% in 2025, and 5.2% in 2026. "
            "Unemployment improves slightly from 3.4% to 3.1% in 2025. As a dollarized economy and "
            "oil exporter, Ecuador could benefit from higher crude prices associated with the Middle "
            "East conflict, though the report notes that conflict effects are heterogeneous depending "
            "on each economy's net energy position and the risk of financial contagion."
        ),
        "SLV": (
            "According to the April 2026 WEO, El Salvador records GDP growth of 2.6% in 2024, "
            "accelerating to 3.7% in 2025 and 3.3% in 2026, before moderating to 3.0% in 2027. "
            "Inflation is very low: 0.9% in 2024, 0.3% in 2025, 2.5% in 2026, and 2.0% in 2027. "
            "The current account deficit deteriorates from -1.8% of GDP in 2024 to -3.9% in 2025 "
            "and -3.3% in 2026. Unemployment falls from 4.7% to 4.2-4.3% in 2025-2026. As a "
            "dollarized economy, El Salvador is affected by imported fuel prices and faces the "
            "effects of US immigration restrictions on remittance flows."
        ),
        "GTM": (
            "According to the April 2026 WEO, Guatemala records GDP growth of 3.7% in 2024, "
            "accelerating to 4.1% in 2025 and moderating to 3.9% in 2026 and 4.0% in 2027. "
            "Inflation is low: 2.9% in 2024, 1.6% in 2025, 2.6% in 2026, and 4.0% in 2027. The "
            "current account surplus rises from 2.9% of GDP in 2024 to 4.8% in 2025, before "
            "moderating to 3.2% in 2026. Guatemala, as part of the CAPDR group and a significant "
            "remittance recipient, faces challenges from more restrictive US immigration policies "
            "and the heterogeneous regional effects of the Middle East conflict."
        ),
        "GUY": (
            "According to the April 2026 WEO, Guyana records extraordinary GDP growth of 43.8% in "
            "2024 and 19.3% in 2025, driven by the oil production boom. Growth moderates to 16.2% "
            "in 2026 but rebounds to 19.7% in 2027 with new projects. Inflation remains contained: "
            "2.9% in 2024, 3.3% in 2025, and 4.1% in 2026. The current account surplus is notable: "
            "16.5% of GDP in 2024, 12.9% in 2025, and 21.5% in 2026. Higher crude prices associated "
            "with the Middle East conflict could additionally benefit Guyana's fiscal and external "
            "revenues, as it is the main driver of Caribbean group growth."
        ),
        "HTI": (
            "According to the April 2026 WEO, Haiti remains in recession with a GDP contraction of "
            "-4.2% in 2024, easing to -2.7% in 2025 and -1.7% in 2026, before reaching positive "
            "growth of 0.5% in 2027. Inflation is very high: 25.8% in 2024, 28.3% in 2025, 23.5% "
            "in 2026, and 19.7% in 2027. The current account improves from -0.6% of GDP in 2024 to "
            "1.9% in 2025. As a highly vulnerable fragile economy, Haiti is especially affected by "
            "rising energy and food prices linked to the Middle East conflict, cuts in international "
            "development aid, and more restrictive migration policies threatening remittance flows."
        ),
        "HND": (
            "According to the April 2026 WEO, Honduras records GDP growth of 3.6% in 2024 and 2025, "
            "moderating to 3.3% in 2026 and 3.7% in 2027. Inflation remains stable: 4.6% in 2024 "
            "and 2025, falling to 4.4% in 2026. The current account shows a deficit of -4.4% of GDP "
            "in 2024, improving notably to a surplus of 2.4% in 2025, before returning to a deficit "
            "of -2.6% in 2026. Unemployment rises from 5.2% to 5.9% in 2025 and 6.8% in 2026. As "
            "part of the CAPDR group, Honduras faces risks from US immigration restrictions on "
            "remittances and rising energy and food prices from the Middle East conflict."
        ),
        "JAM": (
            "According to the April 2026 WEO, Jamaica records a mild GDP contraction of -0.5% in "
            "2024 and -0.1% in 2025, entering recession at -1.2% in 2026 before recovering to 3.1% "
            "in 2027. Inflation rises from 5.5% in 2024 to 3.9% in 2025 and 6.1% in 2026. The "
            "current account shifts from a surplus of 2.9% of GDP in 2024 and 1.2% in 2025 to a "
            "deficit of -6.0% in 2026. Unemployment falls from 4.2% to 3.4% in 2025. The impact of "
            "the Middle East conflict on energy prices is particularly relevant for Jamaica, which "
            "depends on imported fuels for electricity generation."
        ),
        "MEX": (
            "Mexico is one of the most prominent economies in the April 2026 WEO. Growth decelerates "
            "from 1.4% in 2024 to just 0.6% in 2025, but a recovery to 1.6% in 2026 and 2.2% in "
            "2027 is projected. The report indicates that the 2025 weakness reflects fiscal "
            "consolidation, restrictive monetary policy, and trade headwinds. Inflation falls from "
            "4.7% in 2024 to 3.8% in 2025 and remains at 3.9% in 2026. The current account deficit "
            "is modest: -0.9% of GDP in 2024 and -0.4% in 2025 and 2026. Unemployment rises slightly "
            "from 2.7% to 2.6% in 2025. Mexico is especially relevant given the mandatory USMCA "
            "review scheduled for July 2026 and the extension of US Section 122 tariffs, which "
            "require Congressional approval. The report notes that US trade agreements with key "
            "partners like Mexico and Canada provide only temporary relief and expire by end-2026."
        ),
        "NIC": (
            "According to the April 2026 WEO, Nicaragua records GDP growth of 3.6% in 2024, "
            "accelerating to 4.9% in 2025 and moderating to 3.8% in 2026 and 2027. Inflation falls "
            "from 4.6% in 2024 to 2.1% in 2025, rising to 3.5% in 2026. The current account surplus "
            "is notable: 4.2% of GDP in 2024, increasing to 8.6% in 2025 and 6.4% in 2026. "
            "Unemployment falls from 3.1% to 2.7% in 2025. As part of the CAPDR group, Nicaragua "
            "shares the regional challenges from global trade uncertainty, migration policy changes, "
            "and the impact of the Middle East conflict on international energy and food prices."
        ),
        "PAN": (
            "According to the April 2026 WEO, Panama records GDP growth of 2.7% in 2024, accelerating "
            "to 4.4% in 2025 and moderating to 3.8% in 2026 and 4.5% in 2027. Inflation is very low: "
            "0.7% in 2024, virtually zero (0.0%) in 2025, and 1.4% in 2026. The current account shifts "
            "from a surplus of 0.7% of GDP in 2024 to 0.3% in 2025, returning to a deficit of -1.5% "
            "in 2026. Unemployment rises from 9.5% to 10.4% in 2025. Panama, as a logistics hub "
            "connected to international trade through the Canal, faces the effects of the Middle East "
            "conflict on maritime shipping routes and global trade tensions that could affect Canal "
            "transit flows."
        ),
        "PRY": (
            "Paraguay records growth of 4.7% in 2024 and a solid 6.0% in 2025, moderating to 4.2% "
            "in 2026 and 3.5% in 2027, according to the April 2026 WEO, above the Latin American "
            "regional average. Inflation remains moderate: 3.8% in 2024, 4.1% in 2025, and 3.3% in "
            "2026. The current account deficit stands at -3.5% of GDP in 2025, improving to -3.0% in "
            "2026. Unemployment improves from 5.8% to 5.2% in 2025. Paraguay faces the challenges "
            "of global trade uncertainty and the effects of the Middle East conflict on agricultural "
            "commodity prices."
        ),
        "PER": (
            "Peru shows GDP growth of 3.5% in 2024 and 3.4% in 2025, moderating to 2.8% in 2026 "
            "and 2027, according to the April 2026 WEO. Inflation is notably low for the region: "
            "2.4% in 2024, 1.5% in 2025, and 2.5% in 2026. The current account surplus improves "
            "from 2.2% of GDP in 2024 to 3.1% in 2025 and 3.4% in 2026. Unemployment falls from "
            "6.4% to 5.9% in 2025. As an exporter of critical materials such as copper, Peru could "
            "be affected by changes in global demand stemming from the Middle East conflict and the "
            "slowdown in growth among its main trading partners."
        ),
        "URY": (
            "Uruguay records growth of 3.3% in 2024, decelerating to 1.8% in 2025 and 2026, before "
            "rebounding to 2.6% in 2027, according to the April 2026 WEO. Inflation moderates "
            "slightly: 4.8% in 2024, 4.7% in 2025, and 4.0% in 2026. The current account deficit "
            "remains modest at around -0.5% to -0.8% of GDP. Unemployment rises from 8.2% to 7.5% "
            "in 2025 and 8.0% in 2026. As an open economy with solid fundamentals, Uruguay faces "
            "the common regional challenges from trade uncertainty and the effects of the Middle "
            "East conflict on the global environment."
        ),
        "VEN": (
            "Venezuela presents one of the most difficult macroeconomic pictures in the April 2026 "
            "WEO. Growth falls from 5.3% in 2024 to 1.5% in 2025, with projections of 4.0% in 2026 "
            "and 6.0% in 2027. Inflation surges from 49.4% in 2024 to 252.0% in 2025 and 387.4% in "
            "2026, before falling to 94.4% in 2027. The current account shows a surplus of 4.1% of "
            "GDP in 2024, falling to 2.6% in 2025 and recovering to 7.1% in 2026. The IMF excludes "
            "Venezuela from emerging market inflation aggregates due to the magnitude of its "
            "distortions. Higher oil prices linked to the Middle East conflict could benefit "
            "Venezuela's external revenues."
        ),
        "BLZ": (
            "According to the April 2026 WEO, Belize records GDP growth of 3.5% in 2024, "
            "decelerating to 2.7% in 2025 and 2.2% in 2026. Inflation falls from 3.3% in 2024 to "
            "1.1% in 2025 and 1.5% in 2026. The current account deficit widens from -1.9% of GDP "
            "in 2024 to -3.5% in 2025 and -4.5% in 2026. As a small open Caribbean economy, Belize "
            "shares the regional challenges of limited fiscal space, vulnerability to climate shocks, "
            "and the effects of the Middle East conflict on imported fuel prices and global "
            "uncertainty."
        ),
        "SUR": (
            "According to the April 2026 WEO, Suriname records GDP growth of 1.7% in 2024 and 1.5% "
            "in 2025, accelerating to 3.9% in 2026 and 4.4% in 2027. Inflation falls from 16.2% in "
            "2024 to 9.2% in 2025, before rising to 11.8% in 2026. Most notably, the current account "
            "deteriorates dramatically: from -12.9% of GDP in 2024, deepening to -53.3% in 2025 and "
            "-44.8% in 2026, reflecting massive investments in new oil projects. Higher crude prices "
            "from the Middle East conflict could improve revenue prospects for Suriname's oil projects "
            "under development, even as the current account deficit reflects the capital-intensive "
            "construction phase."
        ),
        "TTO": (
            "According to the April 2026 WEO, Trinidad and Tobago records GDP growth of 2.5% in 2024, "
            "decelerating to 0.8% in 2025 and 2026, before recovering to 3.0% in 2027. Inflation is "
            "low: 0.5% in 2024, 1.0% in 2025, and 1.8% in 2026. The current account shows a solid "
            "surplus of 2.5% of GDP in 2024, improving to 3.1% in 2025 and 3.8% in 2026. "
            "Unemployment falls from 5.5% to 4.0% in 2025. As an energy exporter, Trinidad and "
            "Tobago could benefit from higher oil and natural gas prices associated with the Middle "
            "East conflict, which the report projects at a 21.4% increase in 2026 versus 2025."
        ),

        # ===================== G7 =====================
        "USA": (
            "The United States is the most analyzed economy in the April 2026 WEO. Growth decelerates "
            "from 2.8% in 2024 to 2.1% in 2025, but a recovery to 2.3% in 2026 and 2.1% in 2027 is "
            "projected. The Middle East conflict has a small net positive effect on the US given its "
            "net energy exporter status. Inflation rises from 3.0% in 2024 to 2.7% in 2025 and 3.2% "
            "in 2026, reflecting tariff and energy price pressures. Unemployment rises to 4.3% in 2025 "
            "and 4.4% in 2026. The current account deficit narrows to -3.6% of GDP in 2025. The text "
            "mentions the IEEPA ruling and its implications for tariff revenues, the mandatory USMCA "
            "review in July 2026, and temporary trade agreements expiring by end-2026. The OBBBA "
            "provides near-term fiscal stimulus. Technology-driven productivity growth and AI "
            "investment support the potential growth outlook."
        ),
        "JPN": (
            "Japan shows a growth rebound to 1.2% in 2025, before moderating to 0.7% in 2026 and "
            "0.6% in 2027, according to the April 2026 WEO. Stronger consumption and investment drove "
            "the rebound. Inflation rises from 2.7% in 2024 to 3.2% in 2025, moderating to 2.2% in "
            "2026. The current account surplus stands at 4.8% of GDP in 2025. The report notes that "
            "the Middle East conflict has a positive effect on Japan's 2026 growth due to stronger "
            "government offsetting measures and growth momentum, more than compensating for the "
            "negative effect of high energy prices on this net energy-importing economy."
        ),
        "DEU": (
            "Germany recorded a contraction of -0.5% in 2024, recovering to 0.2% in 2025 and 0.8% "
            "in 2026, before rising to 1.2% in 2027, according to the April 2026 WEO. Inflation rises "
            "from 2.5% in 2024 to 2.3% in 2025 and 2.7% in 2026. The current account surplus falls "
            "from 5.8% of GDP in 2024 to 4.4% in 2025 and 3.9% in 2026. Unemployment rises from 3.4% "
            "to 3.8% in 2025. The impact of the Middle East conflict on Germany and the euro area is "
            "negative given their net energy importer status, with a downward revision of -0.2 "
            "percentage points in 2026 relative to the baseline pre-conflict projection."
        ),
        "GBR": (
            "The United Kingdom grows 1.3% in 2025 but moderates to 0.8% in 2026, before recovering "
            "to 1.3% in 2027, according to the April 2026 WEO. Inflation rises from 2.5% in 2024 to "
            "3.4% in 2025 and 3.2% in 2026, persisting above target. The current account deficit "
            "widens to -3.1% and -3.4% of GDP in 2025 and 2026. Unemployment rises significantly "
            "from 4.3% in 2024 to 4.8% in 2025 and 5.6% in 2026. The Middle East conflict has a "
            "negative effect on UK growth as a net energy importer, with a downward revision of "
            "-0.5 percentage points for 2026."
        ),
        "FRA": (
            "France grows 0.9% in 2025 and maintains that pace in 2026 and 2027, according to the "
            "April 2026 WEO. Inflation falls to 0.9% in 2025, the lowest among major euro area "
            "economies, rising to 1.8% in 2026. The current account shifts from a slight surplus of "
            "0.1% of GDP in 2024 to a deficit of -0.4% in 2025 and -0.3% in 2026. Unemployment "
            "rises from 7.4% in 2024 to 7.6% in 2025 and 7.9% in 2026. As a net energy importer, "
            "France faces the negative effect of the Middle East conflict on energy costs, with a "
            "downward revision of -0.3 percentage points for 2026."
        ),
        "ITA": (
            "Italy grows 0.8% in 2024 and 0.5% in 2025, maintaining 0.5% in 2026 and 2027, "
            "according to the April 2026 WEO. Inflation rises from 1.1% in 2024 to 1.6% in 2025 "
            "and 2.6% in 2026, pressured by energy prices linked to the Middle East conflict. The "
            "current account surplus narrows from 1.1% of GDP in 2024 to 1.2% in 2025 and 0.6% in "
            "2026. Unemployment falls from 6.6% in 2024 to 6.0% in 2025. The Middle East conflict "
            "impact on Italy is negative, with a downward revision of -0.2 percentage points in 2026 "
            "relative to the no-conflict scenario. Italy's public debt refinancing needs remain "
            "among the highest of major advanced economies."
        ),
        "CAN": (
            "Canada grows 2.0% in 2024 and 1.7% in 2025, moderating to 1.5% in 2026 and rebounding "
            "to 1.9% in 2027, according to the April 2026 WEO. Inflation remains contained: 2.4% in "
            "2024, 2.1% in 2025, and 2.5% in 2026. The current account deficit is modest: -0.5% of "
            "GDP in 2024, widening to -0.9% in 2025 and narrowing to -0.2% in 2026. Unemployment "
            "rises from 6.4% to 6.9% in 2025, improving to 6.5% in 2026. Canada is especially "
            "relevant given the mandatory USMCA review scheduled for July 2026. The report notes "
            "that US trade agreements with partners like Canada and Mexico provide only temporary "
            "relief and expire by end-2026."
        ),

        # ===================== EMERGENTES =====================
        "AUS": (
            "Australia grows 1.0% in 2024 and 2.0% in 2025 and 2026, according to the April 2026 "
            "WEO. Inflation rises from 3.2% in 2024 to 2.9% in 2025 and 4.0% in 2026, pressured by "
            "commodity price dynamics. The current account deficit remains around -2.2-2.6% of GDP. "
            "Unemployment stands at 4.0-4.2%. Australia, as an economy with a large commodity sector, "
            "is affected by changes in global prices stemming from the Middle East conflict and the "
            "evolution of demand from its main Asian trading partners."
        ),
        "CHN": (
            "China is the second most analyzed economy in the April 2026 WEO. Growth holds at 5.0% "
            "in 2024 and 2025, decelerating to 4.4% in 2026 and 4.0% in 2027. Inflation is virtually "
            "zero: 0.2% in 2024 and 0.0% in 2025, before rising to 1.2% in 2026. The current account "
            "surplus stands at 2.2% of GDP in 2024, rising to 3.7% in 2025. The report notes that "
            "China's domestic activity — especially in the housing sector — lags behind exports. China's "
            "merchandise trade surplus hit a record $1.2 trillion (6% of GDP) in 2025. Rare earth "
            "export controls and the reorientation of exports toward Asia and Europe are key elements. "
            "The Middle East conflict adds uncertainty to global energy demand prospects and China's "
            "export markets."
        ),
        "IND": (
            "India maintains robust growth of 7.1% in 2024, accelerating to 7.6% in 2025 and "
            "moderating to 6.5% in 2026 and 2027, according to the April 2026 WEO. Inflation falls "
            "significantly from 4.6% in 2024 to 2.1% in 2025, before rising to 4.7% in 2026 partly "
            "due to global conflict pressures on energy and food prices. The current account deficit "
            "is modest: -0.6% of GDP in 2024, widening to -2.0% in 2026. As a major net energy "
            "importer, India is negatively affected by oil price increases from the Middle East "
            "conflict, which the report identifies as one of the second-order effects on inflation "
            "and growth prospects."
        ),
        "IDN": (
            "Indonesia grows 5.0% in 2024, accelerating to 5.1% in 2025, and maintaining around "
            "5.0-5.1% in 2026 and 2027, according to the April 2026 WEO. Inflation falls from 2.3% "
            "in 2024 to 1.9% in 2025, before rising to 3.0% in 2026. The current account deficit "
            "improves from -0.6% of GDP in 2024 to near balance at -0.1% in 2025, before widening "
            "to -1.1% in 2026. Unemployment remains at 4.8-4.9%. Indonesia is part of the ASEAN-5 "
            "group, facing the combined effects of US tariffs and the heterogeneous impact of the "
            "Middle East conflict on energy prices."
        ),
        "RUS": (
            "Russia records growth of 4.9% in 2024, decelerating sharply to 1.0% in 2025, "
            "stabilizing at 1.1% in 2026 and 2027, according to the April 2026 WEO. Inflation "
            "stands at 8.4% in 2024 and 8.7% in 2025, falling to 5.6% in 2026. The current account "
            "surplus narrows to 1.6% of GDP in 2025, recovering to 2.9% in 2026. Unemployment is "
            "very low at 2.2-2.5%. The report notes that higher commodity prices from the Middle East "
            "conflict drive a 0.3 percentage point upward revision to Russia's 2026 growth, making "
            "Russia a net beneficiary of higher energy prices."
        ),
        "SAU": (
            "Saudi Arabia grows 2.6% in 2024, accelerating to 4.5% in 2025 and moderating to 3.1% "
            "in 2026 and 4.5% in 2027, according to the April 2026 WEO. Inflation is low: 1.5% in "
            "2024, 2.0% in 2025, and 2.3% in 2026. The current account shifts from a deficit of "
            "-1.3% of GDP in 2024 to -3.0% in 2025 and -1.6% in 2026. The report identifies Saudi "
            "Arabia as one of the countries most affected by the Middle East conflict, with a "
            "downward revision of -1.4 percentage points in 2026 relative to the no-conflict "
            "scenario. However, higher oil prices could partially improve fiscal revenues."
        ),
        "ZAF": (
            "South Africa grows 0.5% in 2024 and 1.1% in 2025, before decelerating to 1.0% in 2026 "
            "and recovering to 1.3% in 2027, according to the April 2026 WEO. Inflation falls from "
            "4.4% in 2024 to 3.2% in 2025, rising to 3.9% in 2026. Unemployment remains extremely "
            "high at around 32.4-32.6%. The current account deficit is modest at -0.7% of GDP in "
            "2024. The report notes that the Middle East conflict is projected to slow South Africa's "
            "growth in 2026, with a recovery expected in 2027 supported by a gradual resumption of "
            "structural-reform-driven private investment as conflict disruptions subside."
        ),
        "KOR": (
            "South Korea grows 2.0% in 2024, decelerating to 1.0% in 2025 and recovering to 1.9% "
            "in 2026 and 2.1% in 2027, according to the April 2026 WEO. Inflation moderates to 2.1% "
            "in 2025 and 2.5% in 2026. The current account surplus increases to 6.6% of GDP in 2025. "
            "Unemployment remains at 2.8%. As a major semiconductor and technology exporter, Korea "
            "benefits from global technology trade dynamism but faces the impact of the Middle East "
            "conflict on imported energy prices and global trade uncertainty."
        ),
        "TUR": (
            "Turkey grows 3.3% in 2024, accelerating to 3.6% in 2025 and maintaining 3.4% in 2026 "
            "and 3.5% in 2027, according to the April 2026 WEO. Inflation decelerates markedly: from "
            "58.5% in 2024 to 34.9% in 2025 and 28.6% in 2026. The current account deficit widens "
            "from -1.0% of GDP in 2024 to -1.9% in 2025 and -2.8% in 2026. Unemployment falls from "
            "8.7% to 8.3% in 2025-2026. The report indicates that Turkey's growth is revised down "
            "0.8 percentage points for 2026 relative to January 2026, as 2025 growth was weaker than "
            "expected and high energy prices weigh on activity as a net energy importer."
        ),
        "TWN": (
            "Taiwan records growth of 5.3% in 2024 and an extraordinary 8.7% in 2025, moderating to "
            "5.2% in 2026 and 3.0% in 2027, according to the April 2026 WEO. Inflation remains low: "
            "2.2% in 2024, 1.7% in 2025, and 1.5% in 2026. The current account surplus is very high: "
            "17.4% of GDP in 2025 and 18.1% in 2026. Unemployment is low at 3.4%. Taiwan is a key "
            "beneficiary of the global semiconductor and AI technology trade boom, mentioned in the "
            "report as one of the countries whose US imports increased significantly as a result of "
            "global supply chain rewiring, with exports of semiconductors and equipment sought after "
            "by firms racing to invest in digital and AI technologies."
        ),
        "SGP": (
            "Singapore grows 5.3% in 2024 and 5.0% in 2025, decelerating to 3.5% in 2026 and 2.7% "
            "in 2027, according to the April 2026 WEO. Inflation falls from 2.4% in 2024 to 0.9% in "
            "2025, rising to 2.3% in 2026. The current account surplus remains very high: 17.2% of "
            "GDP in 2024 and 16.7% in 2025. Unemployment is very low at 1.9-2.0%. Singapore, as part "
            "of the ASEAN-5 group, benefits as a financial and logistics hub from the dynamism of "
            "technology trade in Asia, though the Middle East conflict and global trade uncertainty "
            "generate deceleration risks."
        ),
        "ARE": (
            "The United Arab Emirates grows 4.0% in 2024, accelerating to 5.8% in 2025 and "
            "moderating to 3.1% in 2026 and 5.3% in 2027, according to the April 2026 WEO. Inflation "
            "is low: 1.7% in 2024, 1.3% in 2025, and 2.5% in 2026. The current account surplus is "
            "high: 15.4% of GDP in 2024 and 15.3% in 2025. The UAE is one of the countries most "
            "directly affected by the Middle East conflict that erupted in late February 2026, with "
            "impacts on critical infrastructure, maritime and air traffic, and risk sentiment in "
            "regional financial markets."
        ),
        "PHL": (
            "The Philippines grows 5.7% in 2024, decelerating to 4.4% in 2025 and 4.1% in 2026, "
            "before rebounding to 5.8% in 2027, according to the April 2026 WEO. Inflation falls "
            "from 3.2% in 2024 to 1.7% in 2025, rising to 4.3% in 2026. The current account deficit "
            "improves from -4.0% of GDP in 2024 to -3.3% in 2025, before widening to -4.4% in 2026. "
            "Unemployment rises from 3.8% to 4.2% in 2025 and 4.7% in 2026. The Philippines is part "
            "of the ASEAN-5 group and faces the combined effects of US tariffs and the impact of the "
            "Middle East conflict on imported energy prices."
        ),
        "VNM": (
            "Vietnam grows 7.0% in 2024 and a remarkable 8.0% in 2025, moderating to 7.1% in 2026 "
            "and 6.7% in 2027, according to the April 2026 WEO. Inflation remains moderate: 3.6% in "
            "2024, 3.3% in 2025, and 4.9% in 2026. The current account surplus holds at 6.6-6.7% of "
            "GDP in 2024-2025. Unemployment is very low at 2.1-2.2%. The report identifies Vietnam "
            "as one of the beneficiaries of global supply chain rewiring, with a significant increase "
            "in exports to the US as American imports from China fall and are redirected."
        ),
        "MYS": (
            "Malaysia grows 5.1% in 2024 and 5.2% in 2025, moderating to 4.7% in 2026 and 4.3% in "
            "2027, according to the April 2026 WEO. Inflation remains low: 1.8% in 2024, 1.4% in "
            "2025, and 1.9% in 2026. The current account surplus stands at 1.4-1.6% of GDP. "
            "Unemployment improves to 3.0% in 2025. Malaysia is part of the ASEAN-5 group and "
            "benefits from the dynamism of technology trade in Asia, though it faces the effects of "
            "US tariffs and uncertainty from the Middle East conflict on the global energy and "
            "commercial environment."
        ),
        "EGY": (
            "Egypt grows 2.4% in 2024, accelerating to 4.4% in 2025 and 4.2% in 2026, according to "
            "the April 2026 WEO. Inflation decelerates from 33.3% in 2024 to 20.4% in 2025 and 13.2% "
            "in 2026. The current account deficit stands at -5.4% of GDP in 2024 and -4.2% in 2025 "
            "and 2026. Unemployment falls from 7.4% to 7.3% in 2025. Egypt is one of the Middle "
            "Eastern countries most affected by the conflict that erupted in February 2026, with "
            "direct impacts on the Suez Canal, tourism, and foreign direct investment flows in the "
            "region."
        ),
        "NGA": (
            "Nigeria grows 4.1% in 2024 and 4.0% in 2025, maintaining 4.1% in 2026 and accelerating "
            "to 4.3% in 2027, according to the April 2026 WEO. Inflation decelerates from 33.2% in "
            "2024 to 23.0% in 2025 and 16.0% in 2026. The current account surplus narrows from 6.8% "
            "of GDP in 2024 to 5.1% in 2025 and 5.8% in 2026. As an oil exporter, Nigeria could "
            "benefit from higher crude prices associated with the Middle East conflict. The report "
            "does not include individual narrative mention of Nigeria, but places it among sub-Saharan "
            "African oil exporters with a downward growth revision of -0.3 percentage points for 2026."
        ),
    },
}
