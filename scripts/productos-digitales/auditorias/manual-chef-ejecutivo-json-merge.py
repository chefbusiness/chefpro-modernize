# -*- coding: utf-8 -*-
"""
Fusiona los ids CE-01..CE-40 (normativa de cocina, L3) y CS-01..CS-23
(datos del sector, renumerados desde el CE-01..CE-23 local de L4) en
guias-v2-research-sector.json, para el «Manual del Chef Ejecutivo».

Decisión D24 de manual-chef-ejecutivo-SPEC.md. Aplica las correcciones
D15a (CE-10), D15b (CE-21) y D15c (CE-33) de la SPEC §1.

Ejecutar una sola vez. Idempotente: si los ids ya existen, aborta sin tocar
el fichero (usar --force para sobrescribir).
"""
import json
import sys
from pathlib import Path

JSON_PATH = Path(__file__).parent / "guias-v2-research-sector.json"
FECHA = "2026-09-06"
NOTA_L3 = (
    "Research L3 del Manual del Chef Ejecutivo "
    "(manual-chef-ejecutivo-research-L3-normativa.md), consultado el 2026-09-06."
)
NOTA_L4 = (
    "Research L4 del Manual del Chef Ejecutivo "
    "(manual-chef-ejecutivo-research-L4-laboral-datos.md), consultado el 2026-09-06."
)
BLACKLIST_NOTA = "LISTA NEGRA: no se cita; el lector lo mide con su herramienta."


def row(id_, tema, dato, cifra="", unidad="", anio="2026", fuente_titulo="",
        url="", fecha_pub=None, cita=None, fiabilidad="alta", nota=""):
    return {
        "id": id_,
        "tema": tema,
        "dato": dato,
        "cifra": cifra,
        "unidad": unidad,
        "anio_del_dato": anio,
        "fuente_titulo": fuente_titulo,
        "url": url,
        "fecha_publicacion": fecha_pub,
        "cita_literal": cita,
        "fiabilidad": fiabilidad,
        "nota": nota,
    }


EURLEX_852 = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324"

CE = [
    row("CE-01", "Alérgenos (contaminación cruzada)",
        "El equipo, medios de transporte o recipientes usados para transformar, manipular o almacenar "
        "un alérgeno del Anexo II del Reglamento 1169/2011 no pueden reutilizarse para alimentos sin ese "
        "alérgeno salvo limpieza y comprobación de ausencia de restos visibles. No es un capítulo propio "
        "de gestión de alérgenos: es el punto 9 del Capítulo IX del Anexo II, insertado por el Reglamento "
        "(UE) 2021/382",
        anio="2021", fuente_titulo="Reglamento (CE) 852/2004, Anexo II, Cap. IX, punto 9 (redacción del Reglamento 2021/382)",
        url=EURLEX_852, fiabilidad="alta", nota=NOTA_L3),
    row("CE-02", "Cultura de seguridad alimentaria",
        "Desde la modificación de 2021, el titular debe establecer y demostrar una cultura de seguridad "
        "alimentaria: compromiso de la dirección, liderazgo, conocimiento de peligros por todo el personal, "
        "comunicación abierta entre turnos y actividades, y recursos suficientes, aplicada teniendo en "
        "cuenta la naturaleza y el tamaño de la empresa",
        anio="2021", fuente_titulo="Reglamento (CE) 852/2004, Anexo II, Capítulo XI bis, puntos 1-3",
        url=EURLEX_852, fiabilidad="alta", nota=NOTA_L3),
    row("CE-03", "Donación de alimentos",
        "El capítulo del Anexo II que el research de partida suponía dedicado a alérgenos («Cap. V bis») "
        "es en realidad de donación: permite redistribuir alimentos comprobando que no son nocivos, "
        "respetando fecha de caducidad o duración mínima, integridad del envase, temperatura, fecha de "
        "congelación y trazabilidad",
        fuente_titulo="Reglamento (CE) 852/2004, Anexo II, Capítulo V bis", url=EURLEX_852,
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-04", "Formación de manipuladores",
        "La formación en higiene debe darse de acuerdo con la actividad laboral de cada puesto, no de "
        "forma genérica",
        fuente_titulo="Reglamento (CE) 852/2004, Anexo II, Cap. XII, punto 1", url=EURLEX_852,
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-05", "Uniformidad",
        "Toda persona en zona de manipulación debe llevar vestimenta adecuada, limpia y, en su caso, "
        "protectora; y no puede manipular alimentos si padece una enfermedad transmisible, heridas "
        "infectadas o diarrea sin avisar al operador",
        fuente_titulo="Reglamento (CE) 852/2004, Anexo II, Capítulo VIII, puntos 1-2", url=EURLEX_852,
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-06", "Alérgenos (declaración obligatoria)",
        "14 alérgenos de declaración obligatoria también en platos sin envasar; el cartel «consulte al "
        "personal» no basta sin respaldo escrito o electrónico accesible",
        cifra="14 alérgenos",
        fuente_titulo="Reglamento (UE) 1169/2011, Anexo II y art. 44.1; RD 126/2015 art. 6.5",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293", fiabilidad="alta", nota=NOTA_L3),
    row("CE-07", "Sin gluten",
        "Límites para anunciar un plato «sin gluten» (≤20 mg/kg) o «muy bajo en gluten» (≤100 mg/kg), "
        "vigentes desde el 20-07-2016. El reglamento no menciona expresamente a la restauración, aunque "
        "tampoco la excluye",
        cifra="20 mg/kg / 100 mg/kg", fuente_titulo="Reglamento (UE) 828/2014, arts. 1-3 y 5",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32014R0828",
        fiabilidad="media",
        nota=NOTA_L3 + " Alta en los límites y la fecha; media en la aplicabilidad expresa a restauración, que el texto no dice literalmente."),
    row("CE-08", "Vida útil y Listeria monocytogenes",
        "El Reglamento 2073/2005 aplica a toda la cadena, incluida la venta al por menor; para alimentos "
        "listos para el consumo que favorezcan el crecimiento de Listeria monocytogenes exige un estudio "
        "de vida útil documentado (características fisicoquímicas, literatura científica, modelos "
        "predictivos o estudios de inoculación), no un número de días fijado por ley",
        fuente_titulo="Reglamento (CE) 2073/2005, art. 1 y Anexo II",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02005R2073-20200308",
        fiabilidad="media",
        nota=NOTA_L3 + " Verificado por intermediario sobre el HTML, no letra a letra."),
    row("CE-09", "Trazabilidad",
        "El paso adelante de trazabilidad (identificar a quién se suministra) no alcanza al consumidor "
        "final: solo importa si el restaurante suministra a otro establecimiento",
        fuente_titulo="Reglamento (CE) 178/2002, art. 18.2 y 18.3",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02002R0178-20220701",
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-10", "Temperaturas",
        "Elaborar con la menor antelación posible; mantener en caliente a ≥63 °C (art. 30.2); "
        "refrigeradas a ≤4 °C si la vida útil es mayor de 24 horas o a ≤8 °C si es menor; congeladas a "
        "≤-18 °C; enfriar de 60 a 10 °C en menos de 2 horas; recalentar a ≥74 °C durante 15 segundos en "
        "el centro, en la hora siguiente a sacarlo del frigorífico. El art. 30.5 admite temperaturas "
        "distintas si el operador demuestra ante la autoridad competente que son seguras, y el art. 30.7 "
        "admite un recalentamiento a temperatura distinta si se documenta su equivalencia",
        cifra="63/4/8/-18/74 °C",
        fuente_titulo="RD 1086/2020, art. 30.1, 30.2, 30.5 y 30.7 (redacción del RD 1021/2022)",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872", fiabilidad="alta",
        nota=NOTA_L3 + " Corrección D15a de la SPEC (2026-09-06): amplía el art. 30.2 (mantenimiento en "
        "caliente ≥63 °C), el 30.5 y el 30.7, que la primera versión del research no citaba de forma explícita."),
    row("CE-11", "Comidas testigo",
        "Obligación de conservar comidas testigo (ración mínima 100 gramos, identificada y fechada, en "
        "refrigeración ≤4 °C o congelación ≤-18 °C durante mínimo 7 días) para quien elabore o sirva "
        "comidas a residencias, hospitales, comedores escolares, comedores colectivos con menú común, "
        "medios de transporte, eventos como actividad principal, o encargos para grupos de más de 40 "
        "personas. Muy relevante para el chef ejecutivo de catering, banquetes u hotel",
        cifra="100 g / 7 días / 40 personas",
        fuente_titulo="RD 1086/2020, art. 30, apartados 8, 9 y 10",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872", fiabilidad="alta", nota=NOTA_L3),
    row("CE-12", "Etiquetado «elaboración propia»",
        "La mención «ELABORADO POR» o «ELABORACIÓN PROPIA» es voluntaria, no obligatoria. No se considera "
        "elaboración el fraccionamiento o envasado de un producto ya elaborado por otro fabricante, ni el "
        "corte o deshuesado de carne fresca, ni la limpieza o corte de pescado",
        fuente_titulo="RD 1021/2022, art. 11",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681", fiabilidad="alta", nota=NOTA_L3),
    row("CE-13", "Congelación y etiquetado",
        "Un producto elaborado en el propio establecimiento y después congelado debe etiquetarse con "
        "fecha de elaboración o transformación, fecha de congelación y fecha de caducidad o consumo "
        "preferente del producto congelado, con registro de descripción y cantidad",
        cifra="3 fechas", fuente_titulo="RD 1021/2022, art. 5",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681", fiabilidad="alta", nota=NOTA_L3),
    row("CE-14", "Anisakis",
        "Congelar a -20 °C durante 24 horas como mínimo o a -35 °C durante 15 horas como mínimo, en la "
        "totalidad del producto; informar al consumidor por cartel o carta-menú; excepción si se aplica "
        "un tratamiento térmico de 60 °C durante al menos 1 minuto antes de servir",
        cifra="-20°C/24h · -35°C/15h · 60°C/1min",
        fuente_titulo="RD 1021/2022, art. 8.1-8.3",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681", fiabilidad="alta", nota=NOTA_L3),
    row("CE-15", "Doggy bag / desperdicio",
        "Obligación universal de permitir llevarse la comida sobrante, sin coste adicional, salvo en "
        "bufé libre; hay que informar de ello de forma clara y visible. Vigente desde el 22 de diciembre "
        "de 2022",
        fuente_titulo="RD 1021/2022, art. 18.5",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681", fiabilidad="alta",
        nota=NOTA_L3 + " La fecha se alinea con la ya corregida en MM-36 (22-12-2022, no 15-12-2022)."),
    row("CE-16", "Trazabilidad práctica en cocina",
        "La guía de Madrid detalla qué comprueba el inspector: relaciona los productos que ENTRAN "
        "(albaranes con lote y fecha de caducidad) con los PROCESOS (envases originales conservados, "
        "fecha de elaboración, registros) y con lo que SALE (empresas destinatarias, comidas servidas, "
        "cantidad y fecha). La trazabilidad de proceso interna no la exige la norma, pero sin ella una "
        "retirada de producto es mucho más lenta y cara",
        fuente_titulo="Guía de requisitos de seguridad alimentaria para establecimientos de restauración, "
        "Comunidad de Madrid, 2024, sección Trazabilidad (basada en Reglamento 178/2002)",
        url="https://gestiona3.madrid.org/bvirtual/BVCM051144.pdf", fiabilidad="alta", nota=NOTA_L3),
    row("CE-17", "Aceites de fritura",
        "Límite de componentes polares inferior al 25 %, vigente pese a que el RD 176/2013 derogó otros "
        "artículos de la misma Orden",
        cifra="<25 %", fuente_titulo="Orden de 26-01-1989, art. 6.3",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265", fiabilidad="alta", nota=NOTA_L3),
    row("CE-18", "Contaminantes en materia prima",
        "El Reglamento (UE) 2023/915 deroga al Reglamento (CE) 1881/2006 desde su entrada en vigor "
        "(~25-05-2023) y fija límites máximos de dioxinas, PCB, mercurio, cadmio, plomo y estaño en "
        "pescado y marisco, y de dioxinas, PCB y metales en carne, más micotoxinas (aflatoxinas, "
        "ocratoxina A). Vinculan al comprar materia prima, no al elaborar en cocina",
        fuente_titulo="Reglamento (UE) 2023/915, arts. 9 y 11",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0915",
        fiabilidad="media",
        nota=NOTA_L3 + " Alta en la derogación y la fecha; media en el detalle de límites, verificado por intermediario."),
    row("CE-19", "Acrilamida — ámbito",
        "El Reglamento 2017/2158 obliga a fabricantes de patatas fritas, pan, cereales y café, con "
        "régimen simplificado para pequeños operadores y requisitos adicionales para franquicias con "
        "suministro centralizado. No menciona a los restaurantes como sujeto obligado explícito",
        fuente_titulo="Reglamento (UE) 2017/2158, art. 1.2 y Anexo II",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32017R2158",
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-20", "Acrilamida — niveles",
        "Fritura de patatas por debajo de 175 °C; niveles de referencia de acrilamida en café tostado "
        "400 μg/kg e instantáneo 850 μg/kg, que son un disparador de revisión de medidas, no un límite "
        "legal sancionable directamente",
        cifra="175°C / 400 / 850 μg/kg",
        fuente_titulo="Reglamento (UE) 2017/2158, Anexo I y II",
        url="https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32017R2158",
        fiabilidad="media",
        nota=NOTA_L3 + " Parafraseado por intermediario sobre el HTML, sin cotejo letra a letra de los anexos."),
    row("CE-21", "PRL — temperatura del local",
        "La temperatura del local de trabajo debe estar entre 17 y 27 °C para trabajo sedentario y entre "
        "14 y 25 °C para trabajo ligero; la norma no fija un rango para trabajo pesado. La categoría de "
        "trabajo (sedentario/ligero/pesado) la determina la evaluación de riesgos de cada cocina, y el "
        "Anexo III del RD 486/1997 admite condicionantes propios del local. Humedad relativa 30-70 %; "
        "ventilación mínima 50 m³/hora/trabajador en ambientes calurosos",
        cifra="17-27 °C sedentario / 14-25 °C ligero",
        fuente_titulo="RD 486/1997, Anexo III, punto 3",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1997-8669", fiabilidad="alta",
        nota="Corrección D15b de la SPEC del Manual del Chef Ejecutivo (2026-09-06), verificada por el "
        "verificador legal independiente (D23) sobre el Anexo III del RD 486/1997 consolidado: la primera "
        "versión del research citaba solo el rango de trabajo ligero (14-25 °C) como si fuera el único; "
        "el Anexo III fija además 17-27 °C para trabajo sedentario y no fija rango para trabajo pesado. "
        "Lista negra: nunca «la temperatura legal de la cocina es 14-25 °C» sin esta matización. " + NOTA_L3),
    row("CE-22", "PRL — suelos",
        "Los suelos de los locales de trabajo deben ser fijos, estables y no resbaladizos, sin "
        "irregularidades ni pendientes peligrosas",
        fuente_titulo="RD 486/1997, Anexo I, punto 3.1",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1997-8669", fiabilidad="alta", nota=NOTA_L3),
    row("CE-23", "PRL — EPI de cocina",
        "La utilización regular de cuchillos de mano en producción exige guantes de protección mecánica "
        "y delantal o pantalón resistente a cortes; los ambientes húmedos exigen calzado antideslizante. "
        "El empresario debe proporcionar el EPI gratuitamente y reponerlo",
        fuente_titulo="RD 773/1997, art. 3.c) y Anexo III",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1997-12735", fiabilidad="alta", nota=NOTA_L3),
    row("CE-24", "PRL — manipulación de cargas",
        "El RD 487/1997 no fija ninguna cifra en kilos; solo exige evaluar factores cualitativos "
        "(postura, frecuencia, suelo, agarre). El límite de 25 kg que circula viene de la Guía Técnica no "
        "vinculante del INSST",
        cifra="sin cifra en la norma", fuente_titulo="RD 487/1997, Anexo, puntos 1-5",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1997-8670", fiabilidad="alta", nota=NOTA_L3),
    row("CE-25", "PRL — máquinas de cocina",
        "Los elementos móviles de un equipo de trabajo con riesgo de contacto mecánico deben llevar "
        "resguardos o dispositivos que impidan el acceso a zonas peligrosas, aplicable a picadoras, "
        "cortadoras de fiambre y batidoras industriales",
        fuente_titulo="RD 1215/1997, Anexo I, punto 1.8",
        url="https://www.boe.es/buscar/doc.php?id=BOE-A-1997-17824", fiabilidad="alta", nota=NOTA_L3),
    row("CE-26", "PRL — revisión de equipos",
        "Los equipos sometidos a desgaste con riesgo de generar situaciones peligrosas deben someterse a "
        "comprobaciones periódicas documentadas por personal competente, conservadas durante toda la vida "
        "útil del equipo",
        fuente_titulo="RD 1215/1997, art. 4",
        url="https://www.boe.es/buscar/doc.php?id=BOE-A-1997-17824", fiabilidad="alta", nota=NOTA_L3),
    row("CE-27", "PRL — formación e información",
        "Formación teórica y práctica suficiente y adecuada al puesto, dentro de la jornada de trabajo, "
        "con coste nunca a cargo del trabajador",
        fuente_titulo="Ley 31/1995 de Prevención de Riesgos Laborales, art. 19",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292", fiabilidad="alta", nota=NOTA_L3),
    row("CE-28", "PRL — EPI, obligación general",
        "El empresario debe proporcionar equipos de protección individual adecuados «cuando, por la "
        "naturaleza de los trabajos realizados, sean necesarios», velar por su uso efectivo, y usarlos "
        "solo cuando el riesgo no se pueda evitar o limitar por medios de protección colectiva",
        fuente_titulo="Ley 31/1995, art. 17.2",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292", fiabilidad="alta", nota=NOTA_L3),
    row("CE-29", "Guía oficial de riesgos en cocina",
        "Guía «Restaurantes, Bares y Cafeterías» (Serie Microempresas), editada por el entonces Instituto "
        "Nacional de Seguridad e Higiene en el Trabajo (renombrado INSST en 2018, lo que sitúa la edición "
        "como anterior a esa fecha; el PDF no lleva año visible). Documenta riesgos de cocina con medidas "
        "concretas: caídas (suelo antideslizante, limpiar grasa en frío), cortes (cuchillos con mango "
        "antideslizante, EPI con marcado CE, resguardos en picadoras y cortadoras), quemaduras (cambiar el "
        "aceite en frío, mangos de sartenes hacia dentro, comprobar el termostato de la freidora antes de "
        "usar) y riesgos químicos (no trasvasar productos, EPI con marcado CE)",
        fuente_titulo="INSHT, «Restaurantes, Bares y Cafeterías», Serie Microempresas",
        url="https://www.prevencionparahosteleria.es/documents/recursos%20prl/10-Guia-para-la-Accion-Preventiva..pdf",
        fiabilidad="media",
        nota=NOTA_L3 + " Documento oficial sin fecha de edición verificable en el propio PDF, descargado de "
        "un mirror sectorial: insst.es devolvió 404 el día del research."),
    row("CE-30", "Siniestralidad de hostelería",
        "En el avance enero-diciembre 2025, hostelería registró 50.837 accidentes de trabajo en jornada "
        "con baja (5º sector, no el 4º, como dicen algunas notas de prensa que omiten «actividades "
        "administrativas»), 19 accidentes mortales, índice de incidencia con baja de 2.731,1 por cada "
        "100.000 trabajadores (por encima de la media de 2.547,5) e índice mortal de 1,02 (muy por debajo "
        "de la media de 2,81)",
        cifra="50.837 / 19 / 2.731,1 por 100.000",
        fuente_titulo="Estadística de Accidentes de Trabajo, MITES, avance enero-diciembre 2025",
        url="https://www.mites.gob.es/estadisticas/eat/eat25_12/ATR_12_2025_Resumen.pdf",
        fiabilidad="alta", nota=NOTA_L3),
    row("CE-31", "Desperdicio — jerarquía de prioridades",
        "Orden legal de prioridades ante un excedente de cocina: 1º prevención, 2º donación o "
        "redistribución para consumo humano, 3º alimentación animal, 4º subproductos industriales, 5º "
        "reciclado o compost, 6º valorización energética como último recurso",
        cifra="6 niveles", fuente_titulo="Ley 1/2025, art. 5.1-5.2",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597", fiabilidad="alta", nota=NOTA_L3),
    row("CE-32", "Desperdicio — obligación de hostelería",
        "El artículo específico para hostelería confirma el doggy bag universal con envases aptos, "
        "reutilizables o reciclables, remite a la Ley 7/2022 para plástico de un solo uso, y permite "
        "programas de sensibilización dirigidos al personal de cocina y comedor",
        fuente_titulo="Ley 1/2025, art. 8",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597", fiabilidad="alta", nota=NOTA_L3),
    row("CE-33", "Desperdicio — exención del plan de prevención",
        "Están exentos de tener plan de prevención del desperdicio los establecimientos de hasta 1.300 m² "
        "de superficie útil de exposición y venta (o de actividad si no venden al público); las "
        "microempresas quedan excluidas de las obligaciones del art. 6 (plan de prevención, promoción de "
        "convenios de donación), pero el doggy bag universal del art. 8 les sigue obligando igual que a "
        "cualquier otro establecimiento. Si varios locales bajo el mismo CIF suman juntos más de 1.300 "
        "m², sí quedan obligados aunque cada local individual sea menor",
        cifra="1.300 m²", fuente_titulo="Ley 1/2025, art. 6.4.c) y 6.6",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597", fiabilidad="alta",
        nota="Corrección D15c de la SPEC del Manual del Chef Ejecutivo (2026-09-06): nunca escribir «las "
        "microempresas quedan excluidas por completo de la Ley 1/2025» (frase en la lista negra, §8 de la "
        "SPEC) — quedan excluidas solo de las obligaciones del art. 6; el art. 8 (doggy bag) les sigue "
        "obligando. " + NOTA_L3),
    row("CE-34", "Desperdicio — convenios de donación",
        "El convenio de donación debe fijar condiciones de recogida, transporte y almacenamiento, "
        "compromisos de cada parte; el donante selecciona los alimentos a donar, no el receptor, que "
        "puede rechazar la donación de forma justificada",
        fuente_titulo="Ley 1/2025, art. 7",
        url="https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597", fiabilidad="alta", nota=NOTA_L3),
    row("CE-35", "Botulismo en envasado al vacío",
        "El Comité Científico de la AESAN evaluó en 2024 el riesgo de botulismo en alimentos de V gama "
        "(cocinados, envasados, ligeramente pasteurizados, listos para consumo) tras casos de botulismo "
        "en España en 2023. Recomendación clave: conservación por debajo de 4 °C, idealmente por debajo "
        "de 3,3 °C, para evitar el crecimiento de Clostridium botulinum no proteolítico. Informe aprobado "
        "en sesión plenaria del 12-12-2024, publicado en la Revista del Comité Científico de la AESAN, "
        "volumen 40 (2024), páginas 33-69",
        cifra="<4°C / <3,3°C",
        fuente_titulo="Informe del Comité Científico de la AESAN sobre botulismo en envasados al vacío, 2024",
        url="https://acsa.gencat.cat/es/detall/noticia/informe-botulisme", fiabilidad="media",
        nota=NOTA_L3 + " El PDF original de aesan.gob.es devuelve 404 hoy; contenido y fecha confirmados "
        "por dos fuentes independientes (ACSA/Generalitat de Catalunya y prensa especializada), no leído "
        "letra a letra en el documento original."),
    row("CE-36", "Guía de cocina al vacío",
        "Existe una «Guía de prácticas correctas de higiene específica para la cocina al vacío» publicada "
        "por la Agència de Salut Pública de Catalunya, aplicable tanto a restauración colectiva social "
        "como comercial. Se apoya en el sistema APPCC pero no cita un reglamento europeo concreto ni fija "
        "una cifra de días de vida útil por sí sola — remite a que cada establecimiento lo justifique",
        fuente_titulo="Agència de Salut Pública de Catalunya, Guía de cocina al vacío",
        url="", fiabilidad="baja",
        nota=NOTA_L3 + " No se pudo verificar la URL exacta del PDF; contenido resumido por intermediario, "
        "sin cotejo letra a letra. Pendiente citar el original cuando vuelva a estar accesible (SPEC §9, "
        "changelog 1.1)."),
    row("CE-37", "No existe cifra legal de días de vida útil",
        "No existe una tabla legal de «esta salsa dura X días»: el Reglamento 2073/2005 solo exige un "
        "estudio de vida útil cuando el producto favorece el crecimiento de Listeria monocytogenes "
        "(CE-08), y la única recomendación de temperatura para V gama es la de AESAN (CE-35). Cada "
        "establecimiento fija y documenta su propio criterio dentro del APPCC, salvo el caso ya regulado "
        "de la congelación (CE-13)",
        fuente_titulo="Síntesis de CE-08 + CE-13 + CE-35", url="", fiabilidad="alta",
        nota=NOTA_L3 + " La ausencia de norma es en sí misma el dato verificado. Lista negra: cualquier "
        "tabla que presente una cifra de días de vida útil sin congelar como si fuera norma inventa un dato."),
    row("CE-38", "Inspección — Madrid",
        "La Guía de requisitos de seguridad alimentaria para establecimientos de restauración de la "
        "Comunidad de Madrid, primera edición de febrero de 2024, cubre registro, higiene de "
        "instalaciones, agua, plagas, etiquetado y flexibilidad del APPCC en 53 páginas",
        cifra="53 páginas",
        fuente_titulo="Consejería de Sanidad de la Comunidad de Madrid, febrero 2024",
        url="https://gestiona3.madrid.org/bvirtual/BVCM051144.pdf", fiabilidad="alta", nota=NOTA_L3),
    row("CE-39", "Inspección — Cataluña",
        "Sistema propio de registro RSIPAC (Registre sanitari d'indústries i productes alimentaris de "
        "Catalunya) y Guies de Pràctiques Correctes d'Higiene (GPCH) con reconocimiento oficial de la "
        "Agència Catalana de Seguretat Alimentària, por sector. Estructura de registro e inspección "
        "confirmada; el contenido detallado de las guías no se verificó letra a letra",
        fuente_titulo="ACSA — Guies de Pràctiques Correctes d'Higiene",
        url="https://acsa.gencat.cat/ca/seguretat_alimentaria/restauracio/guies-de-bones-practiques-dhigiene/index.html",
        fiabilidad="media", nota=NOTA_L3),
    row("CE-40", "Inspección — Andalucía",
        "Doctrina propia de Plan General de Higiene (PGH) más sistema APPCC, con «Documento Orientativo "
        "de Especificaciones de los Sistemas de Autocontrol» de la Junta de Andalucía y un programa de "
        "supervisión y auditoría de esos sistemas desde 2007. Estructura confirmada, equivalente en el "
        "fondo al resto de comunidades aunque con nombre distinto; no se leyó el PDF completo",
        fuente_titulo="Junta de Andalucía — Documentación de sistemas de autocontrol",
        url="https://www.juntadeandalucia.es/organismos/saludyconsumo/areas/seguridad-alimentaria/normativa-publicaciones/paginas/documentacion-sistemas-autocontrol.html",
        fiabilidad="media", nota=NOTA_L3),
]

CS = [
    row("CS-01", "Índice de incidencia ATJT, CNAE 56, 2024",
        "Índice de incidencia de accidentes de trabajo con baja (ATJT), CNAE 56 «Servicios de comidas y "
        "bebidas», 2024: 2.646,5 por cada 100.000 personas trabajadoras (hombres 2.824,1, mujeres 2.481,8)",
        cifra="2.646,5 por 100.000",
        fuente_titulo="INSST, Informe anual de accidentes de trabajo en España. Datos 2024",
        url="https://www.insst.es/documents/94886/5326464/Informe+anual+de+accidentes+de+trabajo+en+Espa%C3%B1a.+Datos+2024.pdf",
        fiabilidad="alta", nota=NOTA_L4 + " Antes CE-01 en L4."),
    row("CS-02", "Accidentes de trabajo totales, España 2024",
        "647.200 accidentes de trabajo con baja en España en 2024 (556.385 en jornada, 90.815 in itínere)",
        cifra="647.200",
        fuente_titulo="INSST, Informe anual de accidentes de trabajo en España. Datos 2024",
        url="https://www.insst.es/documents/94886/5326464/Informe+anual+de+accidentes+de+trabajo+en+Espa%C3%B1a.+Datos+2024.pdf",
        fiabilidad="alta", nota=NOTA_L4 + " Antes CE-02 en L4."),
    row("CS-03", "Accidentes anuales del conjunto de hostelería",
        "Accidentes de trabajo anuales en el conjunto de hostelería (alojamiento + comidas y bebidas): "
        "aproximadamente 35.000/año, con un reparto aproximado del 31 % en alojamiento y el 69 % en "
        "comidas y bebidas",
        cifra="≈35.000/año",
        fuente_titulo="Prensa sectorial (prevensystem.com, rrhhdigital.com) citando «datos del sector»",
        url="", fiabilidad="media",
        nota=NOTA_L4 + " No se localizó la tabla primaria exacta que arroje ese reparto 31/69; no cotejado "
        "cifra a cifra contra el informe INSST 2024. Antes CE-03 en L4."),
    row("CS-04", "Accidentes en cocineros y ayudantes de cocina, por tipo",
        "Cifra que circula sobre 283 accidentes en cocineros y ayudantes de cocina con desglose por tipo "
        "(cortes, caídas, sobreesfuerzos, contacto con llamas, golpes)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Circula en medios sectoriales sin atribución rastreable a un informe "
        "primario localizado (candidatos no confirmados: Fremap, UGT-FeSMC, ASEPAL). Antes CE-04 en L4. " + NOTA_L4),
    row("CS-05", "Tipos de accidente más frecuentes, España 2024",
        "Tipos de accidente más frecuentes en el conjunto de la actividad económica española, 2024: "
        "sobreesfuerzos ~31 %, golpes o choques ~26 %, caídas al mismo nivel ~18 %",
        cifra="31% / 26% / 18%",
        fuente_titulo="INSST, Informe anual de accidentes de trabajo en España. Datos 2024 (síntesis de prensa)",
        url="", fiabilidad="media",
        nota=NOTA_L4 + " Síntesis de prensa sobre el informe, no tabla exacta cotejada dentro del PDF en "
        "este research. Antes CE-05 en L4."),
    row("CS-06", "Tasa de rotación laboral en hostelería",
        "Tasa de rotación laboral en hostelería del 63,8 %, citada por Revista Hostelería (30-04-2026) "
        "atribuyéndola de forma difusa a un análisis de «Linkers»; no aparece en la página de Randstad "
        "Research verificada directamente",
        cifra="63,8 %", fuente_titulo="Revista Hostelería, 30-04-2026 (atribución difusa)",
        url="", fiabilidad="baja",
        nota=NOTA_L4 + " Cifra ampliamente repetida en prensa sectorial 2026 pero sin fuente primaria "
        "confirmada en este research; usar solo con el matiz «cifra citada por prensa del sector», nunca "
        "como dato de autoridad. Antes CE-06 en L4."),
    row("CS-07", "Absentismo en hostelería",
        "Absentismo en hostelería: 7,9 horas al mes por incapacidad temporal sobre 132,9 horas pactadas "
        "en el primer trimestre de 2026, equivalente al 5,9 % (dato ya verificado como MM-56, reutilizado "
        "sin re-verificar el texto)",
        cifra="5,9 %", fuente_titulo="INE, ETCL tabla 6043, 1T 2026 (= MM-56)",
        url="https://www.ine.es/jaxiT3/Tabla.htm?t=6043", fiabilidad="alta",
        nota="Reutilizado de MM-56 (Research L3 del Manual del Manager). Antes CE-07 en L4. " + NOTA_L4),
    row("CS-08", "Abandono de la hostelería por jóvenes (UE)",
        "Abandono de la hostelería por parte de trabajadores jóvenes en los primeros 2 años de empleo en "
        "la Unión Europea: 38 %",
        cifra="38 %", fuente_titulo="Eurostat, citado en prensa sectorial", url="", fiabilidad="media",
        nota=NOTA_L4 + " Dato europeo, no específico de España. Antes CE-08 en L4."),
    row("CS-09", "Consumo energético de la cocina sobre el total",
        "La cocina concentra más del 50 % del gasto energético de un establecimiento hostelero",
        cifra=">50 %", fuente_titulo="TotalEnergies España (blog sectorial)", url="", fiabilidad="media",
        nota=NOTA_L4 + " Fuente secundaria; no se localizó el estudio IDAE primario con ese porcentaje "
        "exacto. Antes CE-09 en L4."),
    row("CS-10", "Consumo energético anual medio de un restaurante",
        "Consumo energético anual medio de un restaurante en España: aproximadamente 30.000 kWh/año, con "
        "la electricidad representando en torno al 65 % del total",
        cifra="≈30.000 kWh/año",
        fuente_titulo="Fuentes sectoriales (Diferencial.es, Aholuz, Dexma) que citan a IDAE sin enlazar el documento primario",
        url="", fiabilidad="media", nota=NOTA_L4 + " Antes CE-10 en L4."),
    row("CS-11", "Consumo energético de una freidora profesional",
        "Consumo energético de una freidora profesional: aproximadamente 11.000 kWh/año, con un uso "
        "estimado del 75 % del tiempo",
        cifra="≈11.000 kWh/año", fuente_titulo="TotalEnergies / Dexma", url="", fiabilidad="media",
        nota=NOTA_L4 + " Antes CE-11 en L4."),
    row("CS-12", "Peso energético del sector hostelero en España",
        "El sector hostelero representa aproximadamente el 7 % del consumo energético total de España",
        cifra="≈7 %",
        fuente_titulo="Fuentes sectoriales que citan a IDAE sin enlace al documento primario",
        url="", fiabilidad="media", nota=NOTA_L4 + " Antes CE-12 en L4."),
    row("CS-13", "Manual de eficiencia energética MITECO/GNF",
        "Documento técnico oficial: manual de eficiencia energética en hoteles y restaurantes (CNAE 55.1 "
        "y 56.1), que confirma que cocina, cuartos fríos y comedor son los mayores consumidores y detalla "
        "equipos (hornos, planchas, marmitas, cámaras), sin dar una cifra porcentual exacta verificada "
        "del peso de la cocina sobre el consumo total",
        cifra="", fuente_titulo="MITECO / Gas Natural Fenosa — Manual de eficiencia energética en hoteles y restaurantes",
        url="https://www.miteco.gob.es/content/dam/miteco/es/cambio-climatico/planes-y-estrategias/ManualEfEnergeticaPYMESHoteles_GNF_tcm30-70378.pdf",
        fiabilidad="alta",
        nota=NOTA_L4 + " Alta en existencia y contenido cualitativo; sin cifra porcentual exacta "
        "verificada dentro del propio documento. Antes CE-13 en L4."),
    row("CS-14", "Comida cocinada que acaba en la basura",
        "Cifra que circula sobre el porcentaje de comida cocinada en restaurantes españoles que acaba en "
        "la basura (hasta el 15 %)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Fuentes sectoriales (Prezo, TotalFoodControl) sin estudio primario "
        "identificado. Antes CE-14 en L4. " + NOTA_L4),
    row("CS-15", "Pérdida económica anual por desperdicio/mermas",
        "Cifra que circula sobre la pérdida económica anual del sector restauración español por "
        "desperdicio y mermas (≈255 millones de euros al año, ≈63.000 toneladas)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Cifra «zombi» repetida en múltiples blogs sectoriales desde un estudio de "
        "la UAB de 2013 sin confirmación directa. Antes CE-15 en L4. " + NOTA_L4),
    row("CS-16", "Rango de merma «sano» en cocina profesional",
        "Rango de merma «sano» en cocina profesional que citan proveedores de software de gestión de "
        "cocina (4-6 %)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Sin estudio académico citado. Antes CE-16 en L4. " + NOTA_L4),
    row("CS-17", "Pérdida mensual media por mermas",
        "Cifra que circula sobre la pérdida mensual media por mermas en un restaurante (400-600 €/mes), "
        "de una encuesta de 2025 a más de 250 profesionales de hostelería en España sin instituto "
        "identificado",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Antes CE-17 en L4. " + NOTA_L4),
    row("CS-18", "Ratio de cocineros por comensal/plaza",
        "Regla empírica del sector sobre el número de cocineros por comensal o plaza («1 cocinero cada "
        "20-25 comensales»; alta cocina 10-20; buffet 40-50)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Regla empírica de blogs de gestión de restaurantes, sin estudio académico "
        "o patronal citado. Antes CE-18 en L4. " + NOTA_L4),
    row("CS-19", "Coste de personal sobre ventas netas",
        "Coste de personal del equipo completo (no solo cocina) sobre ventas netas en un restaurante de "
        "servicio tradicional: 30-35 %, coincide con el dato ya verificado MM-41",
        cifra="30-35 %",
        fuente_titulo="Fuentes de gestión de restaurantes (Mapal, CaixaBank Lab, Barcelona Culinary Hub); coincide con MM-41",
        url="", fiabilidad="media",
        nota=NOTA_L4 + " No se ha encontrado desagregación oficial «solo cocina» frente a «sala + "
        "dirección»; el manual debe aclarar que la cifra es del equipo completo. Antes CE-19 en L4."),
    row("CS-20", "Sanciones por brote de toxiinfección alimentaria",
        "Rango de sanciones por seguridad alimentaria: leve desde 300 €, grave y muy grave hasta 600.000 "
        "€, con posible cierre cautelar y hasta 5 años de cierre temporal en los casos más graves",
        cifra="300 € - 600.000 €",
        fuente_titulo="Fuentes legales sectoriales (segurvillegas.com, dig.es), coherente con MM-35",
        url="", fiabilidad="media",
        nota=NOTA_L4 + " Las cifras superiores (300 € de mínimo, 5 años de cierre) no se han cotejado "
        "letra por letra contra la Ley 17/2011 o su desarrollo autonómico; el rango 5.000-600.000 € de "
        "MM-35 es el verificado con fiabilidad alta. Antes CE-20 en L4."),
    row("CS-21", "Coste directo de un brote alimentario",
        "No se ha localizado una cifra media en euros de coste directo por brote alimentario (limpieza, "
        "cierre, indemnizaciones, reputación) para el mercado español",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " El manual debe proponer que el lector calcule su propio coste potencial "
        "(días de cierre × facturación media diaria + sanción del rango legal + coste de gestión de "
        "crisis). Antes CE-21 en L4. " + NOTA_L4),
    row("CS-22", "Tiempo medio de pase",
        "No se ha localizado ningún estudio o encuesta sectorial española que mida de forma agregada el "
        "tiempo medio de pase (desde comanda hasta plato servido)",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Es una métrica que cada cocina mide internamente (ticket time del TPV); "
        "no existe benchmark nacional publicado. Antes CE-22 en L4. " + NOTA_L4),
    row("CS-23", "Horas de formación por trabajador de cocina/año",
        "No se ha localizado el dato de horas de formación desagregado por ocupación de cocina; sí "
        "existe el dato de inversión por trabajador en el conjunto de hostelería (MM-43: 20,14 € frente a "
        "76,49 € de media nacional), usado como proxy",
        cifra="", fuente_titulo="", url="", fiabilidad="baja",
        nota=BLACKLIST_NOTA + " Se puede citar MM-43 como proxy de inversión, nunca una cifra de horas por "
        "trabajador de cocina, que no existe. Antes CE-23 en L4. " + NOTA_L4),
]


def main():
    force = "--force" in sys.argv
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    existentes = {d["id"] for d in data["datos"]}

    nuevos = CE + CS
    ids_nuevos = [d["id"] for d in nuevos]

    # Colisión interna
    if len(ids_nuevos) != len(set(ids_nuevos)):
        vistos = set()
        dup = set()
        for i in ids_nuevos:
            if i in vistos:
                dup.add(i)
            vistos.add(i)
        print(f"ERROR: ids duplicados dentro del lote nuevo: {sorted(dup)}")
        sys.exit(1)

    ya_presentes = [i for i in ids_nuevos if i in existentes]
    if ya_presentes and not force:
        print(f"ERROR: {len(ya_presentes)} ids ya existen en el JSON (usa --force para sobrescribir): "
              f"{ya_presentes[:10]}{'…' if len(ya_presentes) > 10 else ''}")
        sys.exit(1)

    if force:
        data["datos"] = [d for d in data["datos"] if d["id"] not in set(ids_nuevos)]

    data["datos"].extend(nuevos)

    # Meta
    data["_meta"]["manual_chef_ejecutivo_2026_09_06"] = (
        "63 entradas añadidas para el Manual del Chef Ejecutivo (2026-09-06): CE-01..CE-40 "
        "(normativa de cocina, Research L3, numeración original) y CS-01..CS-23 (datos del "
        "sector, Research L4, renumerados desde el CE-01..CE-23 local de ese documento para no "
        "colisionar con los CE-* de L3). Correcciones D15a (CE-10, art. 30.2/30.5/30.7), D15b "
        "(CE-21, rango sedentario/ligero/pesado) y D15c (CE-33, microempresas excluidas del art. "
        "6, no de toda la Ley 1/2025) aplicadas al fusionar, según manual-chef-ejecutivo-SPEC.md §1 (D24)."
    )
    totales = data["_meta"].get("totales", {})
    totales["datos"] = len(data["datos"])
    fiab_count = {"alta": 0, "media": 0, "baja": 0}
    for d in data["datos"]:
        f = d.get("fiabilidad", "")
        if f in fiab_count:
            fiab_count[f] += 1
    totales.update(fiab_count)
    data["_meta"]["totales"] = totales

    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(nuevos)} entradas añadidas ({len(CE)} CE-*, {len(CS)} CS-*). Total: {len(data['datos'])}")


if __name__ == "__main__":
    main()
