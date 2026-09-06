#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
guion_manual_chef_ejecutivo.py — GUION del «Manual del Chef Ejecutivo» v1.0
(SPEC `manual-chef-ejecutivo-SPEC.md`, §4 y §4.2).

Mismo esquema que el hermano (`guion_manual_manager_restaurante.py`, del 5-sep):
un capítulo no se le pide a un redactor con un título, se le pide con un guion
CERRADO. Por capítulo van (a) el objetivo, (b) 4-6 epígrafes, (c) las **cifras
del propio producto** citadas por `fichero.xlsx!Hoja!Celda` —que `documentos.py`
resuelve con openpyxl `data_only` antes de escribir el prompt, así que el
redactor recibe el NÚMERO, no el fichero—, (d) los datos del sector por `id` de
`auditorias/guias-v2-research-sector.json` (ids `CE-*` normativa de cocina,
`CS-*` datos del sector, `MM-*` y `CONV-*` reutilizados), (e) las tablas
exigidas —que las construye el maquetador desde el xlsx, no el redactor—, (f) el
presupuesto de palabras y (g) lo que NO debe decir.

REGLA DE LA LÍNEA (John, 2026-09-04): el texto de los productos digitales ya NO
lo escribe `bridge.py`. `dump_prompts.py` vuelca los prompts exactos que
construye `documentos.py` y un subagente Anthropic escribe cada bloque en la
caché `txt/`, verificándolo con `check_bloque.py`.

FUENTE ÚNICA DE CIFRAS: los SIETE libros de
`astro-site/public/dl/manual-chef-ejecutivo/`, que se LEEN y no se tocan. Sus
mapas de celdas (`manual-chef-ejecutivo/build/mapa-*.json`) son el CONTRATO:
toda coordenada de este guion sale de ahí o está verificada abriendo el libro
con `data_only`. El juego de datos del caso modelado es
`manual-chef-ejecutivo/datos_ejemplo.py` (D8), que IMPORTA la plantilla, las
seis unidades y las 52 semanas del Manual del Manager y la carta de la Guía Food
Cost: los tres productos cuadran sin inventar una sola cifra de «La Encina».

Presupuesto (SPEC D25): 20 capítulos, 75 páginas prometidas, 34.000 palabras
objetivo, 1.600-1.700 por capítulo y 2.000 los cuatro legales (13, 14, 16 y 17).
Bonus: 12 situaciones resueltas de 790-800 palabras, 9.500 palabras y 25 páginas.

DECISIONES QUE ESTE GUION MATERIALIZA (no se reabren aquí): D3 (siete libros y
su cadencia declarada en el cap. 01), D4 (el coste se COPIA en celda verde, no
se recalcula), D5 (alérgenos DE PROCESO aquí, declaración de carta en el Pack
APPCC), D6 (multi-outlet con dos hojas: `Comparativa entre Unidades` e
`Histórico por Unidad`), D9 («partida», con «(estación)» sólo en la primera
mención del manual y en el glosario), D10 (los siete KPI como propuesta de la
casa, sin benchmark), D11 (frontera con el hermano leída en su guion; tabla en
`auditorias/manual-chef-ejecutivo-frontera-guion-2026-09-06.md`), D12 (cap. 10
mide merma agregada por partida; el rendimiento vive en la Guía Food Cost), D13
(el excedente cabe en una tabla de una página que cita al hermano), D15 (las
cinco temperaturas, la temperatura por categoría de trabajo y la exclusión de
las microempresas sólo del art. 6), D16 (salarios en bruto anual con la etiqueta
de cada tabla y +35,5 %), D19 (`Estado Normativo` en el libro 7), D25 (gates),
D26 (cada norma con su artículo, su enlace y la fecha en que se comprobó).

LAS CINCO CORRECCIONES DEL VERIFICADOR LEGAL (D23) QUE APUNTABAN AL GUION —
`auditorias/manual-chef-ejecutivo-verificacion-legal-2026-09-06.md` §2 — están
aplicadas aquí, no en el JSON:
  1. Plus de formación de Madrid (art. 31): lo paga la EMPRESA que no acredita
     haber formado, 20 euros al mes por persona; PRL y manipulación de alimentos
     NO cuentan como formación a estos efectos; mínimo 90 días de servicio al
     año; no se devenga si la persona rechaza la formación sin causa.
  2. Manutención: 59,21 euros es BARCELONA 2026, no «Cataluña» (el Maresme
     tiene 59,17 y Tarragona y Girona van por anexo propio); la opción metálico
     o especie es de la persona trabajadora, por escrito y con tres meses.
  3. Ropa de trabajo: Cataluña SÍ la regula (art. 41), y va más lejos que
     Madrid: conservación y lavado a cargo de la empresa, compensables con
     15,39 euros al mes en Barcelona 2026.
  4. Modificación del ALEH de 2026: SÍ modifica formalmente los arts. 15 a 17
     —reescribe los nombres con el sistema de cremallera— y NO altera ninguna
     función del art. 17; sólo 5 de los 10 puestos de cocina cambiaron de
     nombre, así que la lista de hoy es mixta y el libro 4 reproduce esa mezcla.
  5. El RD 1021/2022 es BOE-A-2022-21681 (la referencia del encargo apuntaba a
     otra norma).
Y las de fondo: CE-14 (el anisakis alcanza también a «cualquier otro tratamiento
insuficiente para matar las larvas», excluye el pescado de aguas continentales y
admite la excepción de acuicultura documentada), CE-23 (el Anexo III del RD
773/1997 es lista NO exhaustiva de actividades que PUEDEN requerir EPI; quien lo
convierte en obligación es la evaluación de riesgos, y la gratuidad del art. 3.c
sí es incondicional), CE-21 (50 metros cúbicos por hora «en los casos
restantes», no «en ambientes calurosos»), CE-07 (el Reglamento 828/2014 no
excluye la restauración) y CONV-02 (Madrid: «tabla salarial de 2025, la última
publicada en el BOCM; a 06-09-2026 no consta tabla posterior», nunca «en
ultraactividad»).

Via: Claude Code
"""

PID = 'manual-chef-ejecutivo'

# --------------------------------------------------------------------------
# Cabecera del documento
# --------------------------------------------------------------------------
BIO = (
    'John Guerrero es CEO de AI Chef Pro y fundador de ChefBusiness Group. En '
    'cocina desde los 17 años y consultor gastronómico desde 2010, ha asesorado '
    'la apertura de más de 200 establecimientos, incluidos restaurantes con '
    'Estrella MICHELIN y Soles Repsol en España y Europa. Más sobre su trabajo '
    'en johnguerrero.es.')

LEGAL = (
    '*Este manual es un documento de trabajo profesional, no un dictamen '
    'laboral, sanitario, jurídico ni de prevención de riesgos. El marco '
    'normativo que se explica es el ESPAÑOL, y su estado se verificó contra las '
    'fuentes oficiales —Boletín Oficial del Estado, EUR-Lex, el Boletín Oficial '
    'de la Comunidad de Madrid y el Diari Oficial de la Generalitat de '
    'Catalunya— el 6 de septiembre de 2026: cada afirmación legal lleva su '
    'norma y su artículo para que puedas comprobarla y para que sepas dónde '
    'mirar cuando cambie. Las temperaturas, los umbrales, los plazos, los '
    'gramajes y las periodicidades viven en celdas editables de las hojas de '
    'cálculo precisamente porque cambian, y porque fuera de España cambian del '
    'todo: si cambia el dato, se cambia la celda y todo el libro se recalcula. '
    'Las producciones, mermas, tiempos, notas y importes son valores de ejemplo '
    'de una cocina modelada que acompaña a este pack y sirven para que los '
    'sustituyas por los tuyos: ninguno es una previsión de tus resultados ni un '
    'estándar del sector. La calificación de un caso concreto —si una '
    'obligación te alcanza, si un excedente es donable, si un equipo necesita '
    'un resguardo, qué tabla salarial te aplica— depende de los hechos de ese '
    'caso, de tu evaluación de riesgos y del convenio provincial que te '
    'corresponda. Antes de cambiar un procedimiento de seguridad alimentaria, '
    'de prevención de riesgos o de clasificación profesional, contrasta con tu '
    'servicio de prevención, con tu asesoría laboral y con la autoridad '
    'sanitaria de tu comunidad.*')

GUIA = {
    'pid': PID,
    'titulo': 'Manual del Chef Ejecutivo',
    'subtitulo': 'Brigada, producción, estándares y seguridad alimentaria: el '
                 'criterio de quien dirige la cocina, no de quien la cocina',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Manual del Chef Ejecutivo',
    'fecha': 'septiembre de 2026',
    'version': '1.0',
    'tipo_doc': 'manual',
    'tipo_doc_art': 'del manual',
    'tipo_doc_dem': 'este manual',
    'categoria_doc': 'Manual profesional',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        '20 capítulos, 7 herramientas en Excel con fórmulas vivas y un bonus de '
        '12 situaciones resueltas para dirigir una cocina que ya está abierta: '
        'la brigada, la producción del día, los estándares que hacen que el '
        'plato salga igual lo haga quien lo haga, y la seguridad alimentaria de '
        'la que respondes tú. No es un recetario, ni un curso de técnicas, ni '
        'una guía de apertura: es el criterio de quien dirige la cocina. Todas '
        'las cifras del caso salen de los libros de este mismo pack, así que el '
        'texto y las hojas de cálculo dicen lo mismo; y cada afirmación legal '
        'va con su norma, su artículo y su enlace, comprobados el 6 de '
        'septiembre de 2026.'),
    'gates': {
        'paginas_prometidas': 75,
        'palabras_objetivo': 34000,
        'min_palabras_cap': 1300,
        # Cifras con separador de miles que el texto puede escribir y que NO
        # están en ninguna celda de los siete libros ni en el JSON del research.
        # Se admiten UNA A UNA y por SIGNIFICADO (lección RD-21 del
        # representante). Todas salen del verificador legal independiente
        # (D23), leídas del PDF oficial del BOCM y del DOGC:
        #  · Escalera salarial de cocina de Madrid, Clase A, tabla de 2025
        #    (BOCM núm. 82, de 06-04-2024, Anexo I.c): 1.415,47 (nivel I),
        #    1.316,72 (II-A), 1.300,28 (II-B), 1.283,83 (III), 1.217,99 (IV) y
        #    1.152,15 (V) euros al mes de salario base, 14 pagas. Los niveles I
        #    y III ya llegan por CONV-03 y CONV-04; los otros cuatro, no.
        #  · 1.459,95 = nivel I de la CLASE D (catering) de Madrid, tabla de
        #    2025: un jefe o jefa de catering NO cobra por la columna A.
        #  · Escalera de Barcelona, Grup A, «Any 2026» (DOGC núm. 9630, de
        #    23-03-2026, Annex II, A.3): 1.577,05 (nivell V) es el único que no
        #    llega por CONV-06 ni CONV-07. Y los dos niveles que el research
        #    omite: 1.404,89 (nivell 5 bis, primera ocupación en el sector o
        #    sin experiencia) y 1.232,72 (nivell VI, marmitón de 16 y 17 años).
        #  · 21.920 y 21.920,00 = bruto ANUAL de convenio de un jefe o jefa de
        #    cocina en Madrid, Clase A: 1.415,47 x 14 pagas + 191,22 x 11 pagas
        #    de plus convenio. Recalculado por el verificador legal.
        #  · 29.698,06 = el mismo puesto en Barcelona, Grup A: 2.121,29 x 14.
        #    La diferencia entre los dos es el +35,5 % de la decisión D16; el
        #    «+49,9 %» que circulaba está PROHIBIDO (NO_COMUN).
        #  · 1.791 y 1.783 = jornada máxima anual de trabajo efectivo del
        #    convenio de Cataluña (art. 28.A): 1.791 horas en 2025 y 1.783 en
        #    2026, 2027 y 2028.
        # No se admite ninguna más.
        'cifras_extra': ('1.316,72', '1.300,28', '1.217,99', '1.152,15',
                         '1.459,95', '1.577,05', '1.404,89', '1.232,72',
                         '21.920', '21.920,00', '29.698,06', '1.791', '1.783'),
        'cifras_ignorar': (),
        # «el servicio cierra» y «la cocina cierra los lunes» no son mortalidad
        # de restaurantes: son horarios. Este manual NO escribe ninguna cifra de
        # cierre, quiebra ni fracaso (NO_COMUN).
        'mortalidad_permitida': ['cierra', 'cierran'],
        # Se rellena al FINAL del fichero con `_ERRATAS_OK` (ver el pie).
        'erratas_permitidas': (),
    },
}

# --------------------------------------------------------------------------
# Los siete libros del pack (SPEC §2.2). Se referencian por NOMBRE de fichero:
# documentos.py los busca en astro-site/public/dl/<pid>/.
# --------------------------------------------------------------------------
X_CUAD = 'cuadro-de-mando-cocina.xlsx'              # libro 1
X_PROD = 'planificacion-produccion-semanal.xlsx'    # libro 2
X_FICHA = 'ficha-tecnica-proceso.xlsx'              # libro 3
X_BRIG = 'brigada-puestos-y-evaluacion.xlsx'        # libro 4
X_CARTA = 'desarrollo-carta-control-calidad.xlsx'   # libro 5
X_BANQ = 'banquetes-comidas-testigo.xlsx'           # libro 6
X_AUD = 'auditoria-interna-cocina.xlsx'             # libro 7

# --------------------------------------------------------------------------
# Pie obligatorio de toda tabla que fije un dato legal (D26). Las URL son las
# mismas que llevan las notas de celda de los xlsx y las que verificó el
# verificador legal independiente el 06-09-2026.
# --------------------------------------------------------------------------
V_852 = ('Verificado el 06-09-2026 · Reglamento (CE) 852/2004, Anexo II, '
         'capítulos VIII, IX (punto 9), XI bis y XII, en la redacción del '
         'Reglamento (UE) 2021/382 · '
         'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324')
V_TEMP = ('Verificado el 06-09-2026 · Art. 30 del RD 1086/2020 en la redacción '
          'del RD 1021/2022 · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872')
V_TESTIGO = ('Verificado el 06-09-2026 · Art. 30, apartados 8, 9 y 10, del '
             'RD 1086/2020 en la redacción del RD 1021/2022 · '
             'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872')
V_1021 = ('Verificado el 06-09-2026 · RD 1021/2022 (BOE-A-2022-21681), '
          'arts. 5, 8, 11 y 18.5 · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_ALERG = ('Verificado el 06-09-2026 · Reglamento (UE) 1169/2011, Anexo II y '
           'art. 44.1, y RD 126/2015, art. 6.5 · '
           'https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293')
V_ALEH = ('Verificado el 06-09-2026 · ALEH VI (BOE-A-2023-6344), arts. 15, 16, '
          '17 y 19, modificado por la Resolución de 25-08-2026 '
          '(BOE-A-2026-18630) · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2023-6344')
V_PRL = ('Verificado el 06-09-2026 · RD 486/1997 (Anexo I, punto 3, y Anexo '
         'III, puntos 3 y 4), RD 773/1997 (arts. 3.c y 4 y Anexo III), '
         'RD 1215/1997 (art. 4 y Anexo I, punto 1.8), RD 487/1997 (Anexo y '
         'disposición final primera) y Ley 31/1995 (arts. 17.2 y 19.2) · '
         'https://www.boe.es/buscar/act.php?id=BOE-A-1997-8669')
V_DESP = ('Verificado el 06-09-2026 · Ley 1/2025, arts. 5, 6, 7 y 8 y '
          'disposición final vigésima, y art. 18.5 del RD 1021/2022 · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597')
V_CONV = ('Verificado el 06-09-2026 contra los PDF oficiales · Convenio de '
          'Hostelería y Actividades Turísticas de la Comunidad de Madrid, '
          'BOCM núm. 82, de 6 de abril de 2024, arts. 22, 23, 26, 28, 31 y 36 '
          'y Anexo I (tablas de 2025) · '
          'https://www.bocm.es/boletin/CM_Orden_BOCM/2024/04/06/BOCM-20240406-2.PDF '
          '— y Conveni col·lectiu interprovincial del sector de la indústria '
          'd\'hostaleria i turisme de Catalunya, DOGC núm. 9630, de 23 de marzo '
          'de 2026, arts. 28, 38, 41 y 43 y Annex II A (tablas «Any 2026» de '
          'Barcelona) · '
          'https://portaldogc.gencat.cat/utilsEADOP/PDF/9630/2141955.pdf')


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos y en las 12
# situaciones del bonus. Son, en este orden: (1) higiene de citación legal,
# (2) régimen de cifras, (3) la LISTA NEGRA íntegra de la SPEC §8 —que es el
# §14 del research más los añadidos de la refutación y las cinco correcciones
# del verificador legal—, (4) el ámbito del producto y la frontera con el
# hermano, y (5) el vocabulario de la D9 y el ámbito geográfico.
# --------------------------------------------------------------------------
NO_COMUN = [
    # ---- 1. Higiene de citación legal ------------------------------------
    'Las letras y apartados de un artículo de ley se escriben «letra g» o '
    '«apartado 2», NUNCA «g)» ni «2)»: un paréntesis de cierre suelto se lee '
    'como una errata.',
    'Los números de las normas y las referencias oficiales se copian TAL CUAL, '
    'sin separador de miles: se escribe «RD 1021/2022», «RD 1086/2020», '
    '«RD 486/1997», «RD 773/1997», «RD 1215/1997», «RD 487/1997», '
    '«Ley 31/1995», «Ley 1/2025», «Reglamento (CE) 852/2004», '
    '«Reglamento (UE) 1169/2011» y «BOE-A-2022-21681»; nunca «RD 1.021/2022» '
    'ni «Reglamento (CE) 852/2.004».',
    'TODA afirmación legal va con su norma y su artículo la primera vez que '
    'aparece en el capítulo («el art. 30.2 del RD 1086/2020», «el punto 9 del '
    'capítulo IX del anexo II del Reglamento (CE) 852/2004»), nunca «es '
    'obligatorio» a secas. Y cuando la norma sea de las verificadas para esta '
    'edición, se dice expresamente «comprobado el 6 de septiembre de 2026».',
    'NO cites nunca una celda de una hoja de cálculo con la sintaxis de Excel '
    '(«Parámetros!B7», «Semana!AF57»). Si hay que nombrar de dónde sale un '
    'dato, se nombra el libro y la hoja en lenguaje normal: «la hoja de '
    'parámetros del cuadro de mando de cocina».',
    # ---- 2. Régimen de cifras --------------------------------------------
    'NO escribas ninguna cifra, porcentaje, temperatura, gramaje, plazo, '
    'umbral, tiempo, importe ni sanción que no esté en la lista de cifras del '
    'producto o en los datos del sector que te doy. Ni «ronda el», ni «suele '
    'estar en», ni un ejemplo inventado para ilustrar. Si necesitas un número, '
    'es uno de los que tienes; si no lo tienes, la frase se escribe sin número.',
    'NO hagas cuentas nuevas con las cifras que te doy: no sumes, no restes, no '
    'calcules porcentajes, no conviertas kilos en euros y no proyectes a doce '
    'meses para escribir un total que no te he dado. Los totales ya están '
    'calculados en los libros.',
    'NO cites ninguna encuesta, informe, estudio, escuela ni proveedor de '
    'software que no venga en los datos del sector de este capítulo. En '
    'particular, NO escribas ningún porcentaje atribuido a Linkers, Randstad, '
    'Apicbase, tSpoonLab, Gstock, Barcelona Culinary Hub, qamarero, monouso, '
    'loomispay ni ingenieriademenu que no te haya llegado con su ficha y su '
    'fuente: para este documento esas cifras no están verificadas y no existen.',
    # ---- 3. Lista negra (SPEC §8 y §14 del research) — cifras -------------
    'PROHIBIDO escribir «283 accidentes en cocineros y ayudantes de cocina» ni '
    'su desglose por tipo de accidente: circula en prensa sectorial sin '
    'atribución rastreable a ningún informe primario. La siniestralidad de este '
    'manual es la que te llega en los datos del sector, con su etiqueta exacta, '
    'su año y su ámbito.',
    'PROHIBIDO dar cualquier benchmark de merma: no existe un rango «sano» de '
    'merma de cocina publicado por nadie. El 4-6 % lo publican proveedores de '
    'software sin un solo estudio citado. La merma se MIDE con la herramienta '
    'contra la producción propia; no se compara con una cifra de fuera.',
    'PROHIBIDO dar cualquier benchmark de tiempo de pase, de horas de formación '
    'por trabajador de cocina o de coste directo de un brote alimentario: está '
    'confirmado que no existe ninguno publicado en España. Se miden con la '
    'herramienta y se dice que se miden.',
    'PROHIBIDO escribir «255 millones de euros al año de pérdida del sector por '
    'mermas», «hasta el 15 % de lo cocinado acaba en la basura», «el 87 % de '
    'los restaurantes no tiene fichas técnicas», «del pulpo se obtiene un 50 % '
    'de merma» ni «un cocinero cada 20-25 comensales»: ninguna tiene fuente '
    'primaria. Si hace falta hablar de dotación, se dice que es una regla de '
    'partida orientativa que cada casa calibra con su producción.',
    'PROHIBIDO escribir la tasa de rotación del 63,8 % en hostelería: el '
    'informe original no está publicado y se le atribuyen dos emisores '
    'distintos. La rotación de la brigada se calcula con los datos del lector, '
    'que para eso está la herramienta.',
    'PROHIBIDO escribir «la cocina es más del 50 % del consumo energético», '
    '«30.000 kWh al año», «11.000 kWh una freidora» ni «el sector es el 7 % del '
    'consumo de España»: todas citan a un organismo sin enlazar el documento '
    'primario.',
    'PROHIBIDO dar un «salario del chef ejecutivo» como cifra única: las '
    'fuentes se contradicen y ninguna explica la diferencia. Lo único que se '
    'publica en este manual son las tablas de convenio que te llegan, con la '
    'etiqueta exacta de cada una.',
    'PROHIBIDO escribir «+49,9 %» ni comparar dos convenios en base mensual sin '
    'los pluses: la diferencia verificada entre un jefe o jefa de cocina de '
    'Madrid y de Barcelona, en bruto anual de convenio, es de +35,5 %, y es la '
    'única comparación autorizada.',
    'PROHIBIDO escribir «en ultraactividad» referido al convenio de Madrid: no '
    'se puede sostener desde la fuente, porque su art. 5 prevé prórroga '
    'automática si no hubo denuncia válida y en el boletín no consta el acto de '
    'denuncia. La etiqueta correcta y verificable es «tabla salarial de 2025, '
    'la última publicada en el boletín de la Comunidad de Madrid».',
    'PROHIBIDO decir que 59,21 euros de manutención son «de Cataluña»: son de '
    'BARCELONA en 2026. El Maresme tiene otra cuantía y Tarragona y Girona van '
    'por anexo propio. Lo mismo con las cinco cifras salariales del grupo A: '
    'son de Barcelona, no de Cataluña.',
    'PROHIBIDO decir que «el trabajador sin formación cobra el plus»: el plus '
    'compensatorio de formación del art. 31 del convenio de Madrid lo PAGA LA '
    'EMPRESA que no acredita haber formado, a cada persona trabajadora. Y no '
    'cuentan como formación a estos efectos la prevención de riesgos laborales '
    'ni la manipulación de alimentos.',
    'PROHIBIDO citar precios de cursos, escuelas o software como argumento de '
    'valor dentro del manual: el manual no se vende a sí mismo. Y prohibido '
    'escribir «55 euros», «110 euros» o «45-55 euros» en cualquier pieza de '
    'este producto.',
    'PROHIBIDO escribir «el mercado paga más por dirigir cocina que por dirigir '
    'sala» y «nadie sube el precio de un curso que no se llena»: las dos son '
    'inferencias, no datos.',
    # ---- 3-bis. Lista negra — normativa ----------------------------------
    'PROHIBIDO citar el RD 3484/2000 para las temperaturas y el RD 1420/2006 '
    'para el anisakis salvo para decir que están DEROGADOS desde el 22 de '
    'diciembre de 2022. Lo vigente son el art. 30 del RD 1086/2020 en la '
    'redacción del RD 1021/2022 y el art. 8 del RD 1021/2022.',
    'PROHIBIDO escribir «menos 20 grados durante 7 días» para el anisakis: son '
    '24 horas a menos 20 grados o 15 horas a menos 35 grados, en la totalidad '
    'del producto. Los siete días son criterio de otro país.',
    'PROHIBIDO decir que el Reglamento (CE) 852/2004 tiene un «capítulo de '
    'alérgenos»: no lo tiene. La obligación de no cruzar alérgenos es el punto '
    '9 del capítulo IX de su anexo II. El capítulo V bis es de redistribución '
    'de alimentos y el XI bis, de cultura de seguridad alimentaria.',
    'PROHIBIDO escribir que existe el carné de manipulador de alimentos: se '
    'derogó en 2010 y la obligación es del titular de la empresa, por puesto y '
    'de acuerdo con la actividad laboral de cada uno.',
    'PROHIBIDO decir que las comidas testigo sólo obligan a hospitales y '
    'colegios, y prohibido decir que obligan «siempre»: obligan en los '
    'supuestos tasados del art. 30.8, entre ellos cualquier encargo para grupos '
    'o eventos de más de 40 personas.',
    'PROHIBIDO escribir que poner «elaboración propia» es obligatorio, o que se '
    'puede poner por fraccionar, envasar, deshuesar carne fresca o limpiar '
    'pescado: la mención es voluntaria y esos supuestos están expresamente '
    'excluidos.',
    'PROHIBIDO publicar una tabla de días de vida útil como si fuera '
    'normativa: no existe cifra legal de días para una elaboración propia no '
    'congelada. Lo que existe es la obligación de estudio de vida útil cuando '
    'el producto listo para el consumo favorece a la Listeria.',
    'PROHIBIDO decir que un nivel de referencia de acrilamida es un límite '
    'sancionable, y prohibido escribir que el reglamento de acrilamida «no '
    'menciona la restauración» de forma que sugiera que un plato de carta queda '
    'fuera de todo. Lo mismo con el reglamento del gluten: su ámbito son los '
    'alimentos, sin excluir la restauración.',
    'PROHIBIDO escribir «la temperatura legal de la cocina es de 14 a 25 '
    'grados». La norma fija rangos POR CATEGORÍA DE TRABAJO —de 17 a 27 grados '
    'en trabajos sedentarios propios de oficinas o similares, y de 14 a 25 en '
    'trabajos ligeros—, no fija ningún rango para el trabajo pesado, la '
    'categoría la determina tu evaluación de riesgos y el propio anexo admite '
    'los condicionantes del local y del proceso.',
    'PROHIBIDO escribir que los 50 metros cúbicos por hora y trabajador de '
    'renovación de aire son «para ambientes calurosos»: la norma dice «en los '
    'casos restantes», y los 30 metros cúbicos son sólo para trabajo sedentario '
    'en ambiente no caluroso y sin humo de tabaco.',
    'PROHIBIDO escribir que el RD 487/1997 fija 25 kilos como peso máximo: la '
    'norma no contiene ninguna cifra en kilos ni en su articulado ni en su '
    'anexo, y ella misma remite los valores máximos «como referencia» a una '
    'guía técnica.',
    'PROHIBIDO escribir que el anexo III del RD 773/1997 «exige» un equipo de '
    'protección: es una lista NO exhaustiva de actividades que PUEDEN requerir '
    'equipo, y su propia nota dice que la evaluación de riesgos determina la '
    'necesidad. Lo que sí es incondicional es que el equipo se entrega gratis y '
    'se repone cuando hace falta.',
    'PROHIBIDO escribir que las microempresas quedan excluidas por completo de '
    'la Ley 1/2025: quedan excluidas de las obligaciones del art. 6. La '
    'obligación de facilitar que el cliente se lleve lo no consumido, del '
    'art. 8, les sigue alcanzando. Y prohibido decir que un local de menos de '
    '1.300 metros cuadrados está exento de la ley: la exención alcanza sólo a '
    'uno de los apartados de su art. 6.',
    'PROHIBIDO escribir que el ALEH tipifica al chef ejecutivo o al chef '
    'corporativo: no existen en el convenio. Prohibido escribir que se aplica '
    'el ALEH V —el vigente es el VI— y prohibido decir que la modificación de '
    '2026 no tocó los arts. 15 a 17: los modifica, aunque no altere ninguna '
    'función del art. 17.',
    'PROHIBIDO repetir el bloque laboral general del hermano —jornada de 40 '
    'horas, registro de jornada, contratación, permisos, despido, igualdad, '
    'acoso, desconexión digital— ni el bloque de local —ruido, música '
    'ambiental, horarios, terraza, perros de asistencia—: se CITAN por su '
    'capítulo y no se reescriben. Y prohibido escribir que la jornada máxima es '
    'de 37,5 horas, que el registro de jornada tiene que ser digital o que '
    'Verifactu obliga ya.',
    # ---- 4. Ámbito del producto y frontera -------------------------------
    'NO conviertas esto en un recetario ni en un curso de técnicas: aquí no se '
    'enseña a cocinar. El lector sabe cocinar y lleva años haciéndolo; lo que '
    'no le han enseñado es a dirigir. Y no lo conviertas en una guía de '
    'apertura: la cocina ya está abierta, con carta puesta y brigada '
    'contratada.',
    'NO expliques desde cero qué es una partida, un pase, una comanda, un '
    'mise en place o un 86: esto es para quien YA dirige una cocina o está a '
    'punto de hacerlo. Lo que aporta el capítulo es el criterio, el caso límite '
    'y la decisión, no la definición de oficio.',
    'NO reproduzcas los registros del Pack APPCC, ni los checklists del Kit de '
    'Tareas, ni el escandallo o la matriz de carta de la Guía Food Cost, ni las '
    'mermas por producto del Kit de Inventario, ni el cuadrante del Kit de '
    'Gestión de Personal, ni el cuadro de mando financiero, la matriz de '
    'polivalencia o el calendario legal del Manual del Manager: se CITAN por su '
    'nombre y se dice qué resuelven, no se copian. Este manual da el criterio '
    'que decide qué se hace con lo que sale de ellos.',
    'NO escribas ninguna cifra financiera del negocio —ventas, food cost, labor '
    'cost, prime cost, ticket medio, margen—: este manual no las tiene y su '
    'cuadro de mando no tiene ni una columna de dinero. Cuando el hilo lleve '
    'ahí, se remite al Manual del Manager y a la Guía Food Cost por su nombre.',
    'La cocina del caso es un local MODELADO, «La Encina», no un cliente real: '
    'no escribas que es un caso real, no le pongas ciudad concreta más allá de '
    'la provincia del convenio y no le atribuyas declaraciones a nadie. Los '
    'nombres de la brigada son de ejemplo.',
    'No prometas resultados («con este manual bajarás la merma», «reducirás el '
    'tiempo de pase»): el manual da método y herramientas, y el resultado '
    'depende de los datos y de la cocina del lector. Y no lo presentes como '
    'sustituto de un servicio de prevención, de una asesoría laboral ni de la '
    'autoridad sanitaria.',
    'Da el ejemplo POR ESCALA cuando el capítulo lo permita —una cocina de 4 a '
    '6 personas, un restaurante de 15 a 25, un hotel o grupo de más de 100— y '
    'no finjas que todo aplica igual en las tres. Una brigada de seis no está '
    '«mal» comparada con la brigada clásica de quince puestos: es otra cosa.',
    # ---- 5. Vocabulario D9 y ámbito geográfico ---------------------------
    'VOCABULARIO OBLIGATORIO (español de España, con la equivalencia de '
    'Hispanoamérica SÓLO la primera vez que el término aparece en el capítulo y '
    'nunca más): «chef ejecutivo (chef corporativo, cuando dirige varias '
    'cocinas)», «jefe de cocina (chef de cocina)», «jefe de partida (chef de '
    'partie)», «ficha técnica (receta estándar)», «escandallo (costeo)», «pase '
    '(despacho)», «merma (desperdicio, cuando es comida servible que se tira)», '
    '«carta (menú)», «ayudante de cocina (auxiliar de cocina)», «steward '
    '(friegaplatos, plonge)». Escrito el paréntesis una vez, el resto del '
    'capítulo usa la forma española a secas.',
    'El término de la unidad de trabajo es SIEMPRE «partida», nunca «estación». '
    'La glosa «partida (estación)» se escribe UNA SOLA VEZ EN TODO EL MANUAL, '
    'en el capítulo 1, y en el glosario: si estás escribiendo cualquier otro '
    'capítulo, escribe «partida» a secas.',
    'NO uses anglicismos que tengan término español asentado en el oficio: se '
    'escribe «merma», no «waste»; «brigada», no «staff»; «ficha técnica», no '
    '«recipe card»; «previsión», no «forecast». Sí se usan tal cual, porque son '
    'los del oficio, «mise en place», «pase», «brigada», «steward», «catering», '
    '«delivery», «take-away» y «86».',
    'El marco legal que se explica es el ESPAÑOL, y hay que decirlo cuando se '
    'entra en materia normativa. Lo que viaja fuera de España es el método y la '
    'herramienta, porque sus parámetros son casillas editables: se remite a '
    '«consulta tu normativa local» en vez de fingir que la regla española vale '
    'en todas partes.',
    'No cites años anteriores a 2026 junto a precios o tendencias. Un año '
    'pasado sólo aparece si va con su norma, su boletín oficial o su fuente '
    'fechada.',
    'No menciones el proceso de edición ni palabras como «maquetador», '
    '«prompt», «instrucciones», «guion» o «capítulo anterior»: el lector compra '
    'un libro, no ve el taller. Tampoco escribas tu propio razonamiento.',
]


# --------------------------------------------------------------------------
# Los 20 capítulos (SPEC §4, con los cambios de su tabla y con los que obligó
# la tabla de frontera D11). Presupuesto: 1.600 palabras la mayoría, 1.700 los
# caps. 1, 3, 19 y 20, y 2.000 los cuatro legales (13, 14, 16 y 17).
# Suma exacta: 34.000.
# --------------------------------------------------------------------------
CAPITULOS = [
    {
        'n': 1,
        'titulo': 'Qué es Exactamente un Chef Ejecutivo (y para Quién es Este Manual)',
        'resumen_indice': 'los puestos que el convenio sí nombra, la frontera con el Manual del Manager, y qué libro resuelve cada problema y cada cuánto se abre.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Que el lector sepa en cinco minutos si este manual le '
                    'sirve, por dónde entrar según el problema que tenga hoy y '
                    'con qué libro del pack se resuelve cada cosa. Y que sepa '
                    'lo que NO hay aquí —ni recetas, ni técnicas, ni apertura, '
                    'ni los números del negocio— para que no lo busque.',
        'epigrafes': [
            'Chef ejecutivo, jefe de cocina, segundo y jefe de partida: qué nombra el convenio y qué es uso de la casa',
            'El Manager lleva el negocio, este manual lleva la cocina',
            'Tu problema, su capítulo y su herramienta',
            'Los siete libros y cada cuánto se abre cada uno',
            'Qué no vas a encontrar aquí',
            'Cómo llamamos aquí a cada cosa',
        ],
        'puntos': [
            'Resolver el lío de nombres con el convenio en la mano: el acuerdo '
            'estatal de hostelería encuadra la cocina en su área funcional '
            'segunda y reparte diez puestos entre tres grupos profesionales. '
            '«Chef ejecutivo» y «chef corporativo» NO existen en ese texto —la '
            'palabra «chef» no aparece ni una vez—, y hay que decirlo con esas '
            'palabras: son denominaciones de uso del oficio, no categorías del '
            'convenio.',
            'Trazar la frontera con el hermano en la PRIMERA PÁGINA, con esta '
            'frase: «el Manual del Manager lleva el negocio, la sala y la ley; '
            'este manual lleva la cocina; si diriges las dos cosas, necesitas '
            'los dos». Y decir expresamente que aquí no hay ni una cifra '
            'financiera: ni ventas, ni food cost, ni prime cost, ni ticket '
            'medio.',
            'Presentar la cocina del caso —«La Encina», con su tipo de carta, '
            'sus partidas activas y su brigada— como el hilo que recorre el '
            'documento, y decir expresamente que es un caso modelado y no un '
            'cliente real. Es la misma cocina, la misma plantilla y las mismas '
            'semanas que las del Manual del Manager: quien tenga los dos no '
            'vuelve a teclear nada.',
            'Declarar la CADENCIA de cada libro, que es lo que evita que el '
            'pack se abra una vez y se quede en el disco: el cuadro de mando y '
            'la planificación de producción son SEMANALES; la ficha técnica se '
            'abre cuando nace o cambia un plato; el desarrollo de carta, al '
            'abrir temporada; la brigada, dos veces al año y cuando alguien '
            'entra o asciende; la auditoría, una vez al trimestre; y el libro '
            'de banquetes, sólo si haces eventos.',
            'Decir qué NO hay: no hay recetas, no hay técnicas de cocina, no '
            'hay licencias ni obra ni plan de negocio, no hay escandallo ni '
            'ingeniería de menú, y no hay registros diarios de APPCC. Cada una '
            'de esas cosas se nombra con el producto donde vive.',
            'Cerrar con el glosario mínimo y la equivalencia de Hispanoamérica, '
            'y con el aviso de que el marco legal que se explica es el español, '
            'con todas las casillas de las herramientas editables para quien '
            'trabaje fuera. Aquí es donde se escribe, UNA sola vez en todo el '
            'manual, «partida (estación)».',
        ],
        'cifras': [
            C('Nombre de la cocina del caso', f'{X_CUAD}!Parámetros!B5', 'txt'),
            C('Tipo de carta del caso', f'{X_CUAD}!Parámetros!B6', 'txt'),
            C('Partidas activas del caso', f'{X_CUAD}!Parámetros!B7', 'num'),
            C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
            C('Personas dadas de alta en el organigrama completo', f'{X_BRIG}!Organigrama!F40', 'num'),
            C('Cubiertos servidos en el año del caso', f'{X_CUAD}!Semana!D57', 'num'),
            C('Raciones producidas en el año del caso', f'{X_CUAD}!Semana!M57', 'num'),
            C('Platos de la carta registrados en el índice de fichas', f'{X_FICHA}!Índice de Fichas!C56', 'num'),
            C('Puntos de control de la auditoría interna de cocina', f'{X_AUD}!Resumen por Área!B12', 'num'),
        ],
        'sector': ['MM-14'],
        'tablas': [
            {
                'titulo': 'Tu problema, el capítulo que lo trata y la herramienta que lo resuelve',
                'cabecera': ['Si tu problema es…', 'Capítulo', 'Herramienta'],
                'filas': [
                    ['No sé quién manda sobre qué en mi propia cocina', '2', 'brigada-puestos-y-evaluacion.xlsx'],
                    ['No sé qué me obliga el convenio en cocina', '3', 'brigada-puestos-y-evaluacion.xlsx'],
                    ['Mando gritando y no quiero seguir así', '4', 'brigada-puestos-y-evaluacion.xlsx'],
                    ['El plato sale distinto según quién esté', '5 y 6', 'ficha-tecnica-proceso.xlsx'],
                    ['Escribimos las fichas y nadie las usa', '6', 'desarrollo-carta-control-calidad.xlsx'],
                    ['Producimos por costumbre y sobra o falta', '7', 'planificacion-produccion-semanal.xlsx'],
                    ['El pase se descontrola los viernes', '8', 'desarrollo-carta-control-calidad.xlsx'],
                    ['No sé qué números son míos y cuáles del gerente', '9', 'cuadro-de-mando-cocina.xlsx'],
                    ['La merma se dispara y no sé de qué partida sale', '10', 'cuadro-de-mando-cocina.xlsx'],
                    ['Compro sin especificar y me llega otra cosa', '11', 'ficha-tecnica-proceso.xlsx'],
                    ['La carta nueva llega tarde y sin fichas', '12', 'desarrollo-carta-control-calidad.xlsx'],
                    ['No sé de qué respondo yo en seguridad alimentaria', '13', 'auditoria-interna-cocina.xlsx'],
                    ['La alergia llega al pase con el plato montado', '14', 'ficha-tecnica-proceso.xlsx'],
                    ['No sé cuántos días dura lo que elaboro', '15', 'ficha-tecnica-proceso.xlsx'],
                    ['Me han encargado un banquete y no sé qué guardar', '16', 'banquetes-comidas-testigo.xlsx'],
                    ['Alguien se ha cortado y no sé qué me obliga', '17', 'auditoria-interna-cocina.xlsx'],
                    ['Sé quién cubre la partida, no si lo hace bien', '18', 'brigada-puestos-y-evaluacion.xlsx'],
                    ['Cocina y sala se echan la culpa', '19', 'brigada-puestos-y-evaluacion.xlsx'],
                    ['Llevo el gerente una propuesta y me la archivan', '19', 'cuadro-de-mando-cocina.xlsx'],
                    ['Dirijo varias cocinas y no rinden igual', '20', 'cuadro-de-mando-cocina.xlsx'],
                ],
                'nota': 'Los siete libros comparten la misma cocina modelada, la misma brigada y '
                        'las mismas 52 semanas, así que puedes saltar al capítulo que te interese '
                        'sin perder el hilo de las cifras.',
            },
            {
                'titulo': 'Los siete libros, qué decide cada uno y cada cuánto se abre',
                'cabecera': ['Libro', 'Qué decide', 'Cada cuánto se abre'],
                'filas': [
                    ['cuadro-de-mando-cocina.xlsx', 'Qué partida se está comiendo el margen y qué unidad va peor', 'Cada semana, quince minutos'],
                    ['planificacion-produccion-semanal.xlsx', 'Cuánto hay que producir hoy en cada partida', 'Cada semana, y la lista se imprime cada día'],
                    ['ficha-tecnica-proceso.xlsx', 'Que el plato salga igual lo haga quien lo haga', 'Cuando nace o cambia un plato'],
                    ['brigada-puestos-y-evaluacion.xlsx', 'A quién promocionar, a quién formar en qué y quién decide qué', 'Dos veces al año, y cuando alguien entra o asciende'],
                    ['desarrollo-carta-control-calidad.xlsx', 'Renovar la carta con método y comprobar que sale lo que dice la ficha', 'Al abrir temporada, y el muestreo del pase cada semana'],
                    ['banquetes-comidas-testigo.xlsx', 'Si este encargo dispara la obligación de comida testigo y cómo se produce', 'Sólo si haces eventos, y una vez por evento'],
                    ['auditoria-interna-cocina.xlsx', 'Puntuar la disciplina de la cocina con la misma vara y comparar cocinas', 'Una vez al trimestre'],
                ],
                'nota': 'Tres de los siete se abren cada semana y cuatro no: saberlo desde el '
                        'primer día es lo que evita que un pack de siete libros se convierta en '
                        'siete ficheros sin abrir.',
            },
            {
                'titulo': 'Qué trae este pack y qué está en otro producto del catálogo',
                'cabecera': ['Lo que necesitas', 'Dónde está', 'Qué hace este manual con ello'],
                'filas': [
                    ['Organigrama de cocina, fichas de puesto y matriz de decisiones', 'En este pack', 'Caps. 2, 4 y 19'],
                    ['Ficha técnica de proceso, con alérgenos de proceso', 'En este pack', 'Caps. 5, 6, 14 y 15'],
                    ['Planificación de producción y lista de producción diaria', 'En este pack', 'Cap. 7'],
                    ['Indicadores de cocina y comparativa entre unidades', 'En este pack', 'Caps. 9, 10 y 20'],
                    ['Desarrollo de carta y control de calidad del pase', 'En este pack', 'Caps. 6, 8 y 12'],
                    ['Comidas testigo y producción de banquetes', 'En este pack', 'Cap. 16'],
                    ['Evaluación técnica con prueba práctica y plan de desarrollo', 'En este pack', 'Cap. 18'],
                    ['Auditoría interna de cocina y estado normativo', 'En este pack', 'Caps. 13 y 17'],
                    ['Números del negocio: ventas, food cost, labor cost, prime cost', 'Manual del Manager de Restaurante', 'Se cita en los caps. 9 y 19; aquí no hay ninguna columna de dinero'],
                    ['Convenio general, jornada, contratación, permisos y despido', 'Manual del Manager de Restaurante', 'Se cita en los caps. 3 y 4'],
                    ['Matriz de polivalencia y plan de cross-training', 'Manual del Manager de Restaurante', 'Se cita en el cap. 18; aquí se mide la competencia, no la cobertura'],
                    ['Registros diarios de APPCC y matriz de alérgenos por plato', 'Pack APPCC', 'Se cita en los caps. 13 y 14'],
                    ['Escandallo, rendimiento del ingrediente e ingeniería de menú', 'Kit de Escandallos y Guía Food Cost', 'Se cita en los caps. 5, 10 y 12'],
                    ['Checklists de apertura, servicio y cierre por partida', 'Kit de Tareas', 'Se cita en el cap. 7'],
                    ['Recepción de mercancía y mermas por producto', 'Kit de Inventario', 'Se cita en los caps. 10 y 11'],
                ],
                'nota': 'Este manual no reproduce ninguna de las plantillas de la columna de la '
                        'derecha: las cita por su nombre y explica qué decisión se toma con lo que '
                        'sale de ellas. Quien tenga los dos manuales no duplica nada.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 2,
        'titulo': 'La Brigada Real: los Diez Puestos del Convenio y el Organigrama que Sí Tienes',
        'resumen_indice': 'las funciones literales del convenio puesto por puesto, los tres niveles que se leen en ellas y por qué una brigada de seis no está mal.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Dar al lector el único organigrama de cocina que puede '
                    'defender por escrito delante de cualquiera: el del '
                    'convenio, con las funciones literales de los diez puestos. '
                    'Y enseñarle a colapsarlo en su cocina real sin perder '
                    'ninguna responsabilidad por el camino.',
        'epigrafes': [
            'El área funcional de cocina y los diez puestos que el convenio sí nombra',
            'Las funciones literales, puesto por puesto: qué dice el texto y qué no dice',
            'Lo que cambió en 2026 y lo que no',
            'Por qué la brigada clásica de quince puestos no aplica a una cocina de seis',
            'Chef ejecutivo, chef corporativo y las denominaciones de uso',
        ],
        'puntos': [
            'La tesis del capítulo: el organigrama de una cocina no se dibuja, '
            'se cita. Existe un texto que dice qué hace cada puesto, está '
            'publicado en el boletín oficial y casi nadie del oficio lo ha '
            'abierto.',
            'Recorrer los diez puestos por lo que el convenio les encarga, no '
            'por lo que se supone que hacen: quién planifica, organiza y '
            'controla todo el departamento; quién lo hace de manera cualificada '
            'y responsable; quién participa con alguna autonomía pero bajo '
            'supervisión; y quién hace tareas sin cualificación. Esa gradación '
            'está en el propio texto y es la base de todo el capítulo 4.',
            'Contar lo que cambió en 2026 con precisión y sin inflarlo: la '
            'modificación SÍ modifica formalmente los artículos de '
            'clasificación —reescribe los nombres con un sistema de alternancia '
            'de género— y NO altera ninguna función. Y sólo cambiaron de nombre '
            'cinco de los diez puestos de cocina, así que hoy la lista es mixta '
            'y el libro de brigada la reproduce tal cual, sin inventar una '
            'homogeneidad que el boletín no tiene.',
            'El colapso de la brigada: en la cocina del caso hay seis personas y '
            'diez puestos posibles, así que varios están a cero. Explicar que '
            'eso no es un defecto: lo que no puede quedar a cero es la '
            'RESPONSABILIDAD. Enseñar cómo se reasignan las funciones de un '
            'puesto vacío a un puesto existente y cómo se deja escrito para que '
            'nadie tenga que adivinarlo.',
            'Cerrar con las denominaciones de uso: «chef ejecutivo», «chef '
            'corporativo» y «chef de cocina» no existen en el convenio, y por '
            'eso la ficha de puesto lleva una columna propia donde cada casa '
            'escribe cómo llama a lo que ya está tipificado. El equivalente por '
            'funciones sí existe, y es lo que hay que buscar.',
        ],
        'cifras': [
            C('Área funcional en la que el convenio encuadra la cocina', f'{X_BRIG}!Organigrama!C6', 'txt'),
            C('Personas encuadradas en los puestos del convenio', f'{X_BRIG}!Fichas de Puesto!G16', 'num'),
            C('Personas en el puesto de jefe o jefa de cocina', f'{X_BRIG}!Fichas de Puesto!G6', 'num'),
            C('Personas en el puesto de segundo o segunda de cocina', f'{X_BRIG}!Fichas de Puesto!G7', 'num'),
            C('Personas en el puesto de jefe o jefa de partida', f'{X_BRIG}!Fichas de Puesto!G9', 'num'),
            C('Personas en el puesto de cocinero o cocinera', f'{X_BRIG}!Fichas de Puesto!G10', 'num'),
            C('Personas en el puesto de ayudante de cocina', f'{X_BRIG}!Fichas de Puesto!G13', 'num'),
            C('Personas en el puesto de auxiliar de cocina y economato', f'{X_BRIG}!Fichas de Puesto!G15', 'num'),
            C('Partidas activas declaradas en el organigrama', f'{X_BRIG}!Organigrama!C5', 'num'),
        ],
        'sector': ['MM-14', 'CONV-01'],
        'tablas': [
            {
                'titulo': 'Los diez puestos de cocina del convenio, con sus funciones literales (brigada-puestos-y-evaluacion.xlsx, hoja «Fichas de Puesto»)',
                'src': (X_BRIG, 'Fichas de Puesto'),
                'cols': [('Puesto', 'A', 'txt'), ('Grupo', 'B', 'txt'),
                         ('Funciones del convenio (literal)', 'C', 'txt'),
                         ('Nivel de delegación', 'E', 'txt'),
                         ('Personas en el caso', 'G', 'num')],
                'filas': (6, 15),
                'nota': V_ALEH + ' — las funciones van copiadas del boletín tal cual, en '
                        'minúscula tras los dos puntos y con la errata del propio texto oficial '
                        'donde la hay; la columna de niveles es una LECTURA de esas funciones, no '
                        'una categoría del convenio.',
            },
            {
                'titulo': 'Cómo llamas tú a cada puesto y qué puesto del convenio le corresponde (brigada-puestos-y-evaluacion.xlsx, hoja «Fichas de Puesto»)',
                'src': (X_BRIG, 'Fichas de Puesto'),
                'cols': [('Denominación de uso', 'A', 'txt'),
                         ('¿Está en el convenio?', 'B', 'txt'),
                         ('Puesto equivalente por las funciones que hace', 'C', 'txt')],
                'filas': (29, 34),
                'nota': 'La equivalencia se hace por FUNCIONES, no por nombre: lo que decide el '
                        'encuadre es lo que la persona hace, no cómo la llama la casa.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 3,
        'titulo': 'Lo que tu Convenio Dice de la Cocina (y no del Resto del Restaurante)',
        'resumen_indice': 'movilidad entre partidas, turno partido y descanso reducido, manutención, ropa y plus de formación, y la escalera de cocina en bruto anual.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Sacar del convenio SÓLO lo que le toca a quien dirige una '
                    'cocina, y dárselo comprobable: qué puede hacer al mover '
                    'gente entre partidas, qué complementos se deben y casi '
                    'nadie reclama, y por qué el mismo puesto no cobra lo mismo '
                    'en dos provincias. La arquitectura general del convenio no '
                    'se explica aquí: se cita.',
        'epigrafes': [
            'Movilidad funcional: mover gente entre partidas sin salirse del convenio',
            'Turno partido, descanso reducido y jornada anual: lo que cambia en cocina',
            'Manutención y ropa de trabajo: dos complementos que se deben y casi nadie reclama',
            'El plus de formación lo paga la empresa que no forma',
            'La escalera de cocina en bruto anual: por qué el mismo puesto no cobra lo mismo',
            'Clases y grupos de establecimiento: por qué no se pueden comparar dos convenios',
        ],
        'puntos': [
            'Abrir con la frontera, en una frase: «la arquitectura del convenio '
            '—acuerdo estatal, convenio provincial y cómo se busca en el '
            'registro de convenios— está en el Manual del Manager, cap. 8; aquí '
            'sólo va lo que el convenio dice de la cocina». Y no se vuelve '
            'sobre ello.',
            'Movilidad funcional, que es la base legal de mover a alguien de '
            'partida: dentro del grupo profesional no tiene más límite que la '
            'pertenencia a ese grupo o la titulación; fuera del grupo hay causa '
            'y un tope de seis meses en un año u ocho en dos. Y las dos frases '
            'que protegen a la persona movida: si las funciones son de nivel '
            'inferior se mantiene la retribución de origen, y no cabe alegar '
            'ineptitud sobrevenida o falta de adaptación si la empresa no ha '
            'ofrecido un curso para adaptarse.',
            'Lo que el convenio provincial dice de la jornada de cocina, con el '
            'ejemplo de Cataluña, que es el más detallado: turnos de un máximo '
            'de cinco horas y un mínimo de tres, hora y media mínima entre '
            'turno y turno, veinte minutos de descanso computables como jornada '
            'en cualquier jornada superior a cinco horas, y la posibilidad de '
            'reducir a diez horas el descanso entre jornadas en zonas '
            'turísticas concretas, con catorce días de aviso previo y con '
            'exclusiones tasadas. Y la cifra dura para dimensionar la brigada: '
            'la jornada máxima anual de trabajo efectivo, que ese convenio fija '
            'en 1.791 horas para 2025 y en 1.783 para 2026, 2027 y 2028. Aviso '
            'importante: la polivalencia funcional que ese mismo artículo '
            'permite NO alcanza a cocina.',
            'Manutención: en Madrid, el complemento en especie puede sustituirse '
            'por 57,82 euros al mes a opción de la persona trabajadora, y sólo '
            'en establecimientos con servicio de restaurante o que elaboren '
            'comidas o cenas. En Barcelona son 59,21 euros al mes en 2026 —de '
            'BARCELONA, no de Cataluña: el Maresme tiene su cuantía y Tarragona '
            'y Girona van por anexo propio— y la opción entre metálico y '
            'especie se ejerce por escrito y con un mínimo de tres meses.',
            'Ropa de trabajo, que es donde más se equivoca el sector: en Madrid, '
            'si la empresa exige una determinada ropa y calzado, tiene '
            'obligación de facilitarla a su cargo y esos importes tienen '
            'carácter de suplidos. En Cataluña se va más lejos todavía: la '
            'conservación y la limpieza de uniformes y ropa de trabajo son a '
            'cargo de la empresa, y si no lo son se compensan con 15,39 euros '
            'al mes en Barcelona en 2026. Para una cocina —chaquetillas, '
            'delantales, paños— eso es dinero real todos los meses.',
            'El plus compensatorio de formación de Madrid, con el sujeto en su '
            'sitio: lo paga LA EMPRESA que no acredita haber hecho las acciones '
            'formativas, y son 20 euros al mes por persona. Tres condiciones '
            'que casi nunca se cuentan: sólo alcanza a quien preste servicios un '
            'mínimo de noventa días al año; NO computan como formación a estos '
            'efectos la prevención de riesgos laborales ni la manipulación de '
            'alimentos, así que el curso de manipulador no exime de pagarlo; y '
            'no se devenga si, ofrecida la formación, la persona la rechaza sin '
            'causa justificada.',
            'La escalera salarial, en BRUTO ANUAL y con la etiqueta de cada '
            'tabla, que es la única forma honesta de compararla. Estas cifras '
            'están autorizadas para este capítulo y se escriben tal cual: un '
            'jefe o jefa de cocina de la Clase A en Madrid suma 21.920,00 euros '
            'brutos al año —salario base de 1.415,47 euros por catorce pagas '
            'más el plus de convenio de 191,22 euros por once—, según la tabla '
            'salarial de 2025 (BOCM núm. 82, de 6 de abril de 2024), la '
            'última publicada en el boletín de la Comunidad de Madrid; a 6 '
            'de septiembre de 2026 no consta tabla posterior. El mismo puesto en el Grup A de Barcelona suma '
            '29.698,06 euros brutos al año —2.121,29 euros por catorce pagas— '
            'según la tabla «Any 2026» del convenio interprovincial de '
            'Cataluña. La diferencia es del 35,5 por ciento. Y el detalle que '
            'un chef usa al contratar: en Madrid existe una Clase D de catering '
            'con tabla propia y más alta que la Clase A (1.459,95 euros de '
            'salario base mensual en el nivel I), y en Barcelona existen dos '
            'niveles que casi nadie cita, 1.404,89 euros para quien accede a su '
            'primera ocupación en el sector o carece de experiencia y 1.232,72 '
            'euros para el marmitón de dieciséis y diecisiete años.',
            'Cerrar con la advertencia que evita el error de comparar: las '
            'clases de establecimiento NO son homologables entre convenios. '
            'Madrid clasifica en clases A, B y C más una D de catering; '
            'Cataluña, en grupos A a E, con la E de catering. Distinta '
            'enumeración y distinto número de columnas: comparar la columna A '
            'de uno con la A del otro es comparar dos cosas que no son la '
            'misma.',
        ],
        'cifras': [
            C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
            C('Personas en el puesto de jefe o jefa de cocina', f'{X_BRIG}!Fichas de Puesto!G6', 'num'),
            C('Personas en el puesto de cocinero o cocinera', f'{X_BRIG}!Fichas de Puesto!G10', 'num'),
            C('Personas en el puesto de ayudante de cocina', f'{X_BRIG}!Fichas de Puesto!G13', 'num'),
            C('Personas en el puesto de auxiliar de cocina y economato', f'{X_BRIG}!Fichas de Puesto!G15', 'num'),
            C('Horas de cocina trabajadas en el año del caso', f'{X_CUAD}!Semana!AM57', 'num'),
            C('Horas de cocina por cubierto en el año del caso', f'{X_CUAD}!Semana!AN57', 'num2'),
            C('Cubiertos servidos en el año del caso', f'{X_CUAD}!Semana!D57', 'num'),
        ],
        'sector': ['MM-15', 'CONV-01', 'CONV-02', 'CONV-05'],
        'tablas': [
            {
                'titulo': 'La escalera de cocina en bruto anual de convenio, con la etiqueta de cada tabla',
                'cabecera': ['Puesto', 'Madrid, Clase A (tabla de 2025)', 'Barcelona, Grup A (tabla Any 2026)', 'Qué hay que saber antes de compararlos'],
                'filas': [
                    ['Jefe o jefa de cocina (nivel I)', '1.415,47 € al mes de salario base, 14 pagas — 21.920,00 € brutos al año con el plus de convenio', '2.121,29 € al mes, 14 pagas — 29.698,06 € brutos al año', 'Es la única comparación en bruto anual verificada: +35,5 %'],
                    ['Segundo o segunda de cocina', '1.316,72 € (nivel II-A)', '1.864,51 € (nivell II)', 'En Barcelona comparte nivel con jefe o jefa de partida y con repostero o repostera'],
                    ['Jefe o jefa de partida', '1.300,28 € (nivel II-B)', '1.864,51 € (nivell II)', 'Madrid separa en II-A y II-B lo que Cataluña reúne en el nivell II'],
                    ['Cocinero o cocinera', '1.283,83 € (nivel III)', '1.803,05 € (nivell III)', 'Mismo nivel también para repostería y para encargado o encargada de economato'],
                    ['Ayudante de cocina', '1.217,99 € (nivel IV)', '1.607,25 € (nivell IV)', 'En Madrid incluye ayudante de repostería y ayudante de economato'],
                    ['Auxiliar de cocina y economato', '1.152,15 € (nivel V)', '1.577,05 € (nivell V)', 'Marmitón, pinche, fregador o fregadora, mozo de almacén y personal de platería'],
                    ['Jefe o jefa de catering', '1.459,95 € (nivel I de la Clase D, catering)', 'Grup E, càtering, con tabla propia', 'NO cobra por la columna A: el catering tiene su propia clase en los dos convenios'],
                    ['Primera ocupación en el sector, sin experiencia', 'Sin nivel propio en la tabla', '1.404,89 € (nivell 5 bis)', 'Es el nivel que se usa al contratar a alguien que empieza'],
                    ['Marmitón de dieciséis y diecisiete años', 'Sin nivel propio en la tabla', '1.232,72 € (nivell VI)', 'Existe sólo en el convenio catalán'],
                ],
                'nota': V_CONV + ' — las clases y los grupos de establecimiento NO son '
                        'homologables entre convenios: Madrid usa clases A, B y C más una D de '
                        'catering, y Cataluña grupos A a E con la E de catering. Y las cuantías '
                        'de Cataluña son de BARCELONA: el Maresme, Tarragona y Girona tienen '
                        'anexo propio. Busca tu convenio provincial antes de usar ninguna de '
                        'estas cifras.',
            },
            {
                'titulo': 'Lo que el convenio dice de la cocina, y en qué artículo lo dice',
                'cabecera': ['Qué te afecta como chef', 'Qué dice', 'Dónde está'],
                'filas': [
                    ['Mover a alguien de partida dentro de su grupo', 'Sin más límite que la pertenencia al grupo profesional o la titulación exigida', 'Art. 19.A del acuerdo estatal'],
                    ['Mover a alguien fuera de su grupo', 'Con causa, y sin superar seis meses en un año u ocho en dos', 'Art. 19.B del acuerdo estatal'],
                    ['Mover a alguien a funciones de nivel inferior', 'Se mantiene la retribución de origen', 'Art. 19.B del acuerdo estatal'],
                    ['Despedir por falta de adaptación tras un cambio', 'No cabe si la empresa no ha ofrecido un curso de adaptación', 'Art. 19.B del acuerdo estatal'],
                    ['Encargar funciones de categoría superior', 'Se cobra la superior en todos sus conceptos; pasados cuatro meses seguidos o seis alternos en doce, se aplica el Estatuto', 'Art. 22 del convenio de Madrid'],
                    ['Encargar funciones de categoría inferior', 'Máximo doce días seguidos o veinte alternos al año, con comunicación previa a la representación', 'Art. 23 del convenio de Madrid'],
                    ['Turno partido en cocina', 'Máximo cinco horas y mínimo tres por turno, con hora y media mínima entre turnos', 'Art. 28.B del convenio de Cataluña'],
                    ['Descanso de veinte minutos', 'Computa como jornada de trabajo en cualquier jornada superior a cinco horas', 'Art. 28.B del convenio de Cataluña'],
                    ['Descanso entre jornadas reducido a diez horas', 'Sólo en las zonas turísticas que enumera, con catorce días de aviso y con exclusiones tasadas', 'Art. 28.C del convenio de Cataluña'],
                    ['Jornada máxima anual de trabajo efectivo', '1.791 horas en 2025 y 1.783 en 2026, 2027 y 2028', 'Art. 28.A del convenio de Cataluña'],
                    ['Manutención', '57,82 € al mes en Madrid; 59,21 € al mes en Barcelona en 2026, a opción de la persona y por escrito', 'Art. 28 de Madrid y art. 38 de Cataluña'],
                    ['Ropa de trabajo', 'La facilita la empresa a su cargo; en Cataluña, además, su conservación y limpieza, o 15,39 € al mes en Barcelona en 2026', 'Art. 36 de Madrid y art. 41 de Cataluña'],
                    ['Plus compensatorio de formación', 'Lo paga la empresa que no acredita haber formado: 20 € al mes por persona con noventa días de servicio al año', 'Art. 31 del convenio de Madrid'],
                ],
                'nota': V_CONV + ' — los dos convenios provinciales que aparecen aquí son un '
                        'EJEMPLO de lo que hay que ir a buscar, no el tuyo: el que te aplica es '
                        'el de la provincia de tu centro de trabajo.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 4,
        'titulo': 'Mandar en una Cocina sin Gritar',
        'resumen_indice': 'los primeros treinta días del que asciende, delegar por nivel del convenio, cómo se canta y se confirma una orden, y qué se delega para que la cocina funcione sin ti.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Dar la parte de la autoridad que sí se puede escribir: a '
                    'quién se le puede encargar el resultado, a quién la tarea '
                    'con el estándar delante y a quién hay que enseñársela; '
                    'cómo se canta y se confirma una orden para que no haya que '
                    'repetirla a gritos; y qué tiene que estar delegado para '
                    'que la cocina no dependa de que tú estés en el pase.',
        'epigrafes': [
            'De compañero a jefe: los primeros treinta días al frente de la brigada',
            'Delegar por nivel del convenio, no por confianza',
            'La orden en cocina: quién canta, quién confirma y por qué gritar no es mandar',
            'Dar voz sin perder el mando: qué se hace con la propuesta de un cocinero',
            'El relevo: qué se delega para que la cocina funcione el día que tú no estás',
        ],
        'puntos': [
            'La tesis del capítulo: en una cocina la autoridad no se gana '
            'levantando la voz, se gana quitando ambigüedad. Casi todo lo que '
            'se resuelve gritando es una instrucción que nunca se dio con '
            'claridad, un estándar que no estaba escrito o una decisión que no '
            'se sabía de quién era.',
            'Los primeros treinta días del que asciende de segundo a jefe, que '
            'es la transición más dura del oficio: qué se cambia la primera '
            'semana (nada, salvo lo que sea peligroso), qué se observa, cuándo '
            'se habla con cada persona y cómo se anuncia la primera decisión '
            'impopular. Y el error clásico: intentar seguir siendo el compañero '
            'de todos y acabar sin ser el jefe de nadie.',
            'La delegación por nivel, que es lo que este manual añade y no está '
            'en ningún otro sitio: a quien el convenio describe como cualificado, '
            'autónomo y responsable se le encarga el RESULTADO y no se le '
            'supervisa el paso a paso; a quien describe con alguna autonomía '
            'bajo supervisión se le encarga la TAREA con el estándar escrito '
            'delante y se comprueba; y a quien describe sin cualificación se le '
            'enseña, se hace con él la primera vez y se comprueba siempre. '
            'Delegar por confianza en vez de por nivel es lo que produce el '
            'accidente y el plato mal hecho a la vez.',
            'El circuito de la orden en el pase: quién canta, quién confirma en '
            'voz alta y qué se hace cuando nadie confirma. Una orden que no se '
            'repite de vuelta no se ha dado. Y la regla de volumen: se sube la '
            'voz para que se oiga por encima de la campana, no para señalar a '
            'nadie.',
            'Qué se hace con la propuesta de un cocinero, que es la forma más '
            'barata de retener a alguien: se escucha entera, se prueba en un '
            'día flojo, se costea antes de decidir y se contesta siempre, '
            'también cuando la respuesta es no. Un equipo al que se le pregunta '
            'trae producto y trae ideas; un equipo al que no, sólo trae horas.',
            'El relevo: hacer la lista de lo que sólo sabe el chef y repartirla '
            'antes de necesitarla. Qué queda delegado por escrito para un día '
            'libre —qué se puede pedir, hasta qué importe, qué se puede quitar '
            'de la carta y a quién se llama— y qué no se delega nunca: la '
            'decisión sobre una persona, la firma de un registro obligatorio y '
            'parar el servicio por un riesgo alimentario.',
            'Frontera explícita, con esta frase: «la conversación de corrección, '
            'con su guion y su acuerdo escrito, está en el Manual del Manager, '
            'cap. 7; aquí interesa dónde y cuándo se corrige en una cocina, que '
            'no es lo mismo». En el pase se corrige el hecho, en corto y sin '
            'público; lo demás espera al final del servicio.',
        ],
        'cifras': [
            C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
            C('Responsable titular de la partida de pase y caliente', f'{X_BRIG}!Organigrama!E10', 'txt'),
            C('Personas asignadas a la partida de pase y caliente', f'{X_BRIG}!Organigrama!G10', 'num'),
            C('Responsable titular de la partida de fríos y entrantes', f'{X_BRIG}!Organigrama!E11', 'txt'),
            C('Personas asignadas a la partida de fríos y entrantes', f'{X_BRIG}!Organigrama!G11', 'num'),
            C('Personas en el puesto de jefe o jefa de partida', f'{X_BRIG}!Fichas de Puesto!G9', 'num'),
            C('Planes de desarrollo individual planificados', f'{X_BRIG}!Plan de Desarrollo Individual!C25', 'num'),
            C('Planes de desarrollo individual en curso', f'{X_BRIG}!Plan de Desarrollo Individual!C26', 'num'),
        ],
        'sector': ['MM-14'],
        'tablas': [
            {
                'titulo': 'Los tres niveles de delegación que se leen en el convenio (brigada-puestos-y-evaluacion.xlsx, hoja «Fichas de Puesto»)',
                'src': (X_BRIG, 'Fichas de Puesto'),
                'cols': [('Nivel', 'A', 'txt'), ('Puestos', 'C', 'txt'),
                         ('Cómo se manda en ese nivel', 'E', 'txt')],
                'filas': (23, 25),
                'nota': V_ALEH + ' — los tres niveles son una LECTURA de las funciones del '
                        'convenio, no una categoría que el convenio nombre.',
            },
            {
                'titulo': 'Qué se delega, qué se supervisa y qué no se delega nunca en una cocina',
                'cabecera': ['Decisión o tarea', 'Se delega', 'Con qué límite escrito'],
                'filas': [
                    ['Producción del día de una partida', 'Sí, al responsable de la partida', 'La lista de producción del día, sin cambiarla a ojo'],
                    ['Pedido de reposición a proveedor habitual', 'Sí, al responsable de economato o al segundo', 'Hasta el importe que la casa fije por escrito, y sólo de referencias ya especificadas'],
                    ['Compra fuera de escandallo por oportunidad', 'No sin consulta', 'Se consulta siempre: cambia el coste del plato y la ficha'],
                    ['Quitar un plato de la carta en mitad del servicio', 'Sí, al segundo o al responsable del pase', 'Se avisa a sala en el momento y se anota el motivo'],
                    ['Aceptar un encargo de grupo', 'No', 'Dispara producción, personal y, por encima del umbral, comida testigo'],
                    ['Cambiar el gramaje o el montaje de un plato en carta', 'No', 'Es una versión nueva de la ficha, con fecha y formación'],
                    ['Firmar un registro obligatorio', 'No', 'Responde quien firma'],
                    ['Parar el pase por una avería de frío o un riesgo alimentario', 'No, pero cualquiera puede activarlo', 'Cualquiera de la brigada puede parar; sólo el chef reanuda'],
                    ['Decidir sobre una persona: turno, corrección, promoción', 'No', 'Es del chef, y en lo laboral con la dirección'],
                ],
                'nota': 'La columna del límite es la que hace que la delegación funcione: delegar '
                        'sin decir hasta dónde no es delegar, es dejar de mirar.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 5,
        'titulo': 'La Ficha Técnica de Proceso: que el Plato Salga Igual lo Haga Quien lo Haga',
        'resumen_indice': 'qué lleva una ficha de proceso, por qué el coste se copia y no se recalcula, y los campos que la plantilla gratuita no tiene.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Que el lector distinga de una vez la ficha técnica del '
                    'escandallo y sepa exactamente qué campos hacen que un '
                    'plato sea reproducible por alguien que no estaba el día '
                    'que se creó. Y que entienda por qué el coste entra copiado '
                    'y no calculado.',
        'epigrafes': [
            'Ficha técnica y escandallo: dos documentos del mismo plato',
            'Lo que lleva una ficha de proceso y la plantilla de cinco campos no tiene',
            'El coste se copia, no se recalcula: la casilla verde de la ficha',
            'Temperatura de servicio, conservación, versión y fecha de revisión',
            'La ficha de un plato que se mantiene en caliente',
        ],
        'puntos': [
            'La tesis, que es la distinción número uno del manual: son dos '
            'documentos distintos del mismo plato. El escandallo dice cuánto '
            'CUESTA; la ficha técnica dice cómo se HACE. Se venden como si '
            'fueran lo mismo y no lo son, y por eso casi ninguna cocina tiene '
            'la segunda.',
            'Recorrer los campos de la ficha del ejemplo por lo que resuelve '
            'cada uno: pasos numerados con su punto de control, técnica, '
            'tiempos separados de elaboración previa y de pase, punto de '
            'cocción escrito con su temperatura en el centro, montaje con foto, '
            'alérgenos de proceso, conservación y vida útil por elaboración, '
            'versión y fecha de revisión. La plantilla gratuita más descargada '
            'que circula tiene cinco campos —número, nombre, ingredientes, '
            'instrucciones y notas— y ninguno de los que hacen falta.',
            'Por qué el coste por ración entra en una casilla verde que se COPIA '
            'del escandallo y no se calcula aquí: en todo este pack no hay ni '
            'una fórmula que apunte a otro fichero, a propósito. Si el '
            'escandallo cambia, se pega el número nuevo y se sube la versión de '
            'la ficha. Quien no tenga escandallo, lo tiene en el Kit de '
            'Escandallos y en la Guía Food Cost, y ahí es donde se calcula.',
            'La versión y la fecha de revisión como campos obligatorios y no '
            'decorativos: son lo único que impide que convivan tres versiones '
            'del mismo plato en tres partidas. La ficha del ejemplo va por su '
            'segunda versión, y ese número tiene que estar impreso donde la '
            'gente lo lee.',
            'El plato que se mantiene en caliente: si la elaboración va a estar '
            'esperando, la ficha escribe la temperatura mínima de mantenimiento '
            'y quién la comprueba. No es un detalle de la ficha, es lo que '
            'convierte una obligación legal en una casilla que alguien mira.',
            'Cerrar con la frontera: los alérgenos de PROCESO —los de esta '
            'elaboración concreta— van en esta ficha y se explican en el '
            'capítulo 14; la declaración de alérgenos plato a plato de la carta '
            'vive en el Pack APPCC, con sus catorce columnas, y no se '
            'reproduce aquí.',
        ],
        'cifras': [
            C('Código del plato de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B6', 'txt'),
            C('Nombre del plato de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B7', 'txt'),
            C('Partida que lo produce', f'{X_FICHA}!Ficha (ejemplo)!B9', 'txt'),
            C('Versión de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B11', 'txt'),
            C('Coste por ración copiado del escandallo', f'{X_FICHA}!Ficha (ejemplo)!B16', 'eur2'),
            C('Minutos de elaboración previa de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B40', 'num'),
            C('Minutos de pase de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B41', 'num'),
            C('Minutos totales de la elaboración de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B43', 'num'),
            C('Punto de cocción escrito en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B46', 'txt'),
            C('Temperatura mínima de mantenimiento en caliente de la ficha', f'{X_FICHA}!Ficha (ejemplo)!B47', 'num'),
        ],
        'sector': ['CE-06', 'CE-13'],
        'tablas': [
            {
                'titulo': 'Los pasos de la elaboración, con su punto de control (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
                'src': (X_FICHA, 'Ficha (ejemplo)'),
                'cols': [('Nº', 'A', 'num'), ('Operación', 'B', 'txt'),
                         ('Punto de control', 'F', 'txt')],
                'filas': (24, 31),
                'nota': 'La columna de la derecha es la que convierte una receta en una ficha: '
                        'sin punto de control, un paso es una descripción; con él, es algo que '
                        'alguien puede comprobar sin preguntar.',
            },
            {
                'titulo': 'Qué lleva una ficha técnica de proceso y qué no le toca',
                'cabecera': ['Campo', 'Qué resuelve', 'Dónde vive si no es aquí'],
                'filas': [
                    ['Pasos numerados con punto de control', 'Que el plato sea reproducible sin preguntar', 'En esta ficha'],
                    ['Técnica, tiempos y punto de cocción', 'Que el resultado no dependa de quién esté', 'En esta ficha'],
                    ['Montaje con foto', 'Que el plato se vea igual en las dos partidas', 'En esta ficha'],
                    ['Temperatura de servicio y de mantenimiento', 'Cumplir en el pase lo que la norma exige', 'En esta ficha'],
                    ['Alérgenos de proceso', 'Saber dónde entra el alérgeno EN ESTA elaboración', 'En esta ficha'],
                    ['Conservación y vida útil por elaboración', 'Saber qué se guarda, cómo y cuántos días', 'En esta ficha'],
                    ['Versión y fecha de revisión', 'Que no convivan tres versiones del mismo plato', 'En esta ficha'],
                    ['Coste por ración', 'Saber qué margen deja', 'Se COPIA del escandallo: Kit de Escandallos o Guía Food Cost'],
                    ['Rendimiento del ingrediente y merma de cocción', 'Saber cuánto producto neto sale de un bruto', 'Guía Food Cost'],
                    ['Precio de venta y posición en la matriz de carta', 'Decidir qué se queda y qué se cambia', 'Guía Food Cost'],
                    ['Declaración de alérgenos de todos los platos de la carta', 'Informar al cliente', 'Pack APPCC'],
                ],
                'nota': 'La regla que ordena la tabla: en esta ficha va lo que hace falta para '
                        'ELABORAR el plato; lo que hace falta para PONERLE PRECIO vive en el '
                        'escandallo, y lo que hace falta para INFORMAR al cliente, en el Pack '
                        'APPCC.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 6,
        'titulo': 'Estandarizar de Verdad: por Qué la Ficha Existe y Nadie la Sigue',
        'resumen_indice': 'quién aprueba la ficha, dónde vive, cómo se versiona, cómo se audita en el pase y qué se revisa cuando cambia el producto del proveedor.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Atacar el problema real, que no es escribir la ficha: es '
                    'hacerla vinculante. Que el lector salga con un circuito '
                    'de aprobación, un sitio físico donde la ficha vive, un '
                    'control de versiones y un muestreo del pase que le diga, '
                    'con un número, si se está siguiendo o no.',
        'epigrafes': [
            'Escribir la ficha no es estandarizar: quién la aprueba y dónde vive',
            'El control de versiones que evita tres versiones del mismo plato',
            'Formar en la ficha: por qué se enseña en el puesto y no en una reunión',
            'Auditar la ficha en el pase: el muestreo que dice si se sigue',
            'Cuando cambia el producto del proveedor: qué se revisa y en qué orden',
        ],
        'puntos': [
            'La tesis: una ficha guardada en una carpeta del ordenador del chef '
            'no es un estándar, es un documento. Lo que la convierte en '
            'estándar son cuatro cosas: alguien la aprueba, vive donde se '
            'trabaja, se enseña en el puesto y se comprueba en el pase.',
            'El circuito de aprobación en tres firmas: quien la redacta (el '
            'responsable de la partida), quien la aprueba (el chef) y quien '
            'confirma el coste (el escandallo). Un plato no sale a carta sin '
            'las tres, y ésa es una de las líneas de la auditoría interna.',
            'Dónde vive la ficha: en la partida que produce el plato, accesible '
            'sin pedir permiso a nadie, plastificada o en pantalla, y con la '
            'versión visible. El índice de fichas de la carta dice, de un '
            'vistazo, cuántos platos tienen ficha cerrada y cuántos no: en el '
            'caso son pocos, y ése es el punto de partida honesto de casi '
            'cualquier cocina.',
            'El control de versiones, con la regla que lo hace funcionar: una '
            'ficha nueva sustituye a la anterior EN TODAS LAS PARTIDAS el mismo '
            'día, y la anterior se retira físicamente. Convivir dos versiones '
            'una semana es lo que produce la queja de «hoy estaba distinto».',
            'Formar en la ficha en el puesto y no en una reunión: se hace el '
            'plato con la ficha delante, se compara el resultado con la foto y '
            'se pesa una ración. Media hora en la partida vale más que una hora '
            'de explicación en la oficina, y además deja la evidencia de que la '
            'formación se hizo.',
            'El muestreo del pase, que es la parte que casi nadie hace: se cogen '
            'platos al azar durante el servicio, se anota si son conformes con '
            'la ficha y se mide la temperatura de emplatado. Enseñar el '
            'resultado del caso —cuántos muestreos, cuántos no conformes, qué '
            'porcentaje de cumplimiento y cómo se lee contra el objetivo de la '
            'casa— y decir con todas las letras que el objetivo lo pone la '
            'casa, no un estándar de fuera.',
            'Qué se revisa cuando el proveedor cambia el producto, en este '
            'orden: primero los alérgenos, después el rendimiento y el gramaje, '
            'después el punto de cocción y sólo al final el coste. Cambiar el '
            'orden es lo que hace que un cambio de proveedor acabe en una '
            'incidencia de alérgeno.',
        ],
        'cifras': [
            C('Muestreos del pase hechos en el periodo', f'{X_CARTA}!Control de Calidad del Pase!D53', 'num'),
            C('Muestreos no conformes con la ficha', f'{X_CARTA}!Control de Calidad del Pase!D54', 'num'),
            C('Platos devueltos por el cliente en el muestreo', f'{X_CARTA}!Control de Calidad del Pase!D55', 'num'),
            C('Cumplimiento de ficha técnica en el pase, medido', f'{X_CARTA}!Control de Calidad del Pase!D52', 'pct1'),
            C('Objetivo de cumplimiento de ficha de la casa', f'{X_CARTA}!Control de Calidad del Pase!E52', 'pct1'),
            C('Lectura del cumplimiento de ficha', f'{X_CARTA}!Control de Calidad del Pase!F52', 'txt'),
            C('Platos de la carta registrados en el índice de fichas', f'{X_FICHA}!Índice de Fichas!C56', 'num'),
            C('Platos con la ficha cerrada', f'{X_FICHA}!Índice de Fichas!C52', 'num'),
            C('Porcentaje de platos de la carta con la ficha cerrada', f'{X_FICHA}!Índice de Fichas!C57', 'pct1'),
            C('Platos con ficha que toca revisar', f'{X_FICHA}!Índice de Fichas!C54', 'num'),
        ],
        'sector': ['CE-04', 'CE-05'],
        'tablas': [
            {
                'titulo': 'El índice de fichas de la carta, plato a plato (ficha-tecnica-proceso.xlsx, hoja «Índice de Fichas»)',
                'src': (X_FICHA, 'Índice de Fichas'),
                'cols': [('Código', 'A', 'txt'), ('Plato', 'B', 'txt'),
                         ('Partida que lo produce', 'C', 'txt'),
                         ('Familia', 'D', 'txt'), ('Versión', 'E', 'txt'),
                         ('¿Ficha cerrada?', 'H', 'txt'), ('Estado', 'J', 'txt')],
                'filas': (10, 21),
                'nota': 'La columna de estado es la que ordena el trabajo de las próximas '
                        'semanas: no se empieza por el plato que más gusta, se empieza por el que '
                        'más sale y no tiene ficha.',
            },
            {
                'titulo': 'El muestreo del pase, plato a plato (desarrollo-carta-control-calidad.xlsx, hoja «Control de Calidad del Pase»)',
                'src': (X_CARTA, 'Control de Calidad del Pase'),
                'cols': [('Servicio', 'B', 'txt'), ('Id del plato', 'C', 'txt'),
                         ('Familia', 'D', 'txt'),
                         ('Temperatura de emplatado (°C)', 'E', 'num'),
                         ('Tiempo de pase (min)', 'F', 'num'),
                         ('Conforme a la ficha', 'G', 'txt'),
                         ('¿Se mantiene en caliente?', 'L', 'txt')],
                'filas': (6, 20),
                'nota': 'Quince muestreos de un mismo periodo. No hace falta medir todos los '
                        'platos de todos los servicios: hace falta medir siempre igual y no dejar '
                        'de medir.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 7,
        'titulo': 'Mise en Place y Planificación de Producción',
        'resumen_indice': 'la diferencia entre tener el puesto montado y saber cuánto producir, la previsión de cubiertos y la lista que se imprime cada día.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Sustituir el «producir por costumbre» por una cuenta que '
                    'se hace en diez minutos: cubiertos previstos por el mix de '
                    'venta menos el stock ya elaborado. Y dejar montada la '
                    'lista de producción diaria, que es el checklist de este '
                    'manual.',
        'epigrafes': [
            'Tener el puesto montado no es haber planificado',
            'La previsión de cubiertos: reservas, histórico y el número con el que se produce',
            'Cuánto hay que producir hoy: cubiertos por mix menos stock elaborado',
            'La lista de producción diaria: el papel que se imprime y se cuelga',
            'El ajuste por desviación: qué se corrige al día siguiente',
        ],
        'puntos': [
            'La tesis: el mise en place es la preparación del puesto; la '
            'planificación de producción es saber CUÁNTO hay que producir. Se '
            'confunden todo el rato, y la consecuencia es la misma cocina que '
            'un martes tira producto y un sábado se queda corta.',
            'La previsión de cubiertos, con las tres columnas y su orden: '
            'reservas confirmadas, histórico del mismo servicio y previsión '
            'sugerida, que es la que propone la hoja. La cuarta columna es la '
            'que decide el chef, y puede apartarse de la sugerida: se aparta '
            'con criterio (una fecha señalada, una obra en la calle, un '
            'festivo) y se anota por qué. En el caso, las reservas de la semana '
            'son bastantes menos que los cubiertos que acaban entrando: '
            'producir sólo contra reservas es el error más caro de todo el '
            'capítulo.',
            'La cuenta, escrita para que se pueda hacer el mismo día: raciones '
            'previstas de un plato igual a cubiertos previstos por su mix de '
            'venta; cantidad a producir igual a raciones previstas menos stock '
            'ya elaborado. La hoja avisa cuando el stock elaborado supera lo '
            'previsto, que es la firma de la sobreproducción del día anterior.',
            'La lista de producción diaria: se imprime, se cuelga en la partida '
            'y se tacha. Es el checklist de este manual, y por eso no hay otro. '
            'Frontera explícita: los checklists de apertura, servicio y cierre '
            'por partida ya existen en el Kit de Tareas y responden a otra '
            'pregunta —¿se hizo o no se hizo?—; esta lista responde a cuánto '
            'hay que hacer.',
            'El ajuste por desviación: al día siguiente se compara lo previsto '
            'con lo servido y se corrige el mix, no la voluntad de nadie. Dos '
            'semanas de ajuste valen más que cualquier previsión teórica.',
            'Cerrar con el enlace al capítulo de merma: producir por costumbre '
            'es la causa raíz de la merma que se ve en el cuadro de mando, y la '
            'única forma de demostrarlo es tener la producción escrita antes '
            'del servicio.',
        ],
        'cifras': [
            C('Semana ISO que planifica el ejemplo', f'{X_PROD}!Previsión de Cubiertos!B6', 'num'),
            C('Días que cubre la planificación', f'{X_PROD}!Previsión de Cubiertos!B8', 'num'),
            C('Reservas confirmadas de la semana', f'{X_PROD}!Previsión de Cubiertos!C29', 'num'),
            C('Histórico de cubiertos de la misma semana', f'{X_PROD}!Previsión de Cubiertos!D29', 'num'),
            C('Previsión sugerida por la hoja', f'{X_PROD}!Previsión de Cubiertos!E29', 'num'),
            C('Cubiertos previstos que decide el chef', f'{X_PROD}!Previsión de Cubiertos!F29', 'num'),
            C('Raciones previstas de la semana, todas las partidas', f'{X_PROD}!Producción por Partida!G44', 'num'),
            C('Raciones de stock ya elaborado', f'{X_PROD}!Producción por Partida!H44', 'num'),
            C('Raciones que hay que producir esta semana', f'{X_PROD}!Producción por Partida!M44', 'num'),
            C('Raciones que hay que producir en el día de la lista', f'{X_PROD}!Lista de Producción Diaria!D34', 'num'),
        ],
        'sector': ['CE-10'],
        'tablas': [
            {
                'titulo': 'La previsión de la semana, día a día y servicio a servicio (planificacion-produccion-semanal.xlsx, hoja «Previsión de Cubiertos»)',
                'src': (X_PROD, 'Previsión de Cubiertos'),
                'cols': [('Día', 'A', 'txt'), ('Servicio', 'B', 'txt'),
                         ('Reservas confirmadas', 'C', 'num'),
                         ('Histórico del mismo servicio', 'D', 'num'),
                         ('Previsión sugerida', 'E', 'num'),
                         ('Previsión que decide el chef', 'F', 'num')],
                'filas': (15, 29),
                'nota': 'Compara la primera columna de números con la última: la distancia entre '
                        'lo reservado y lo que de verdad entra es distinta cada día de la semana, '
                        'y por eso no se puede producir con un porcentaje fijo sobre reservas.',
            },
            {
                'titulo': 'Lo que hay que producir esta semana, partida a partida (planificacion-produccion-semanal.xlsx, hoja «Producción por Partida»)',
                'src': (X_PROD, 'Producción por Partida'),
                'cols': [('Partida', 'A', 'txt'), ('Raciones previstas', 'B', 'num'),
                         ('Stock ya elaborado', 'C', 'num'),
                         ('Raciones a producir', 'D', 'num'),
                         ('Peso sobre lo que hay que producir', 'E', 'pct1')],
                'filas': (50, 58),
                'nota': 'Las dos últimas partidas no producen raciones, por eso van a cero: en '
                        'esta cocina son unidades de servicio, no de producción.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 8,
        'titulo': 'El Pase: Protocolo, no Cultura',
        'resumen_indice': 'quién canta, quién marcha y quién despacha, cómo se declara un 86, cómo se mide el pase sin cronómetro y qué sale por la puerta.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Convertir el pase en un procedimiento con roles y '
                    'secuencia, no en un rasgo de carácter del chef. Y dar la '
                    'forma de medirlo que no obliga a poner a nadie con un '
                    'cronómetro.',
        'epigrafes': [
            'Quién canta, quién marcha y quién despacha: los tres papeles del pase',
            'El 86: cómo se declara, quién lo autoriza y a quién se avisa',
            'Medir el pase sin cronómetro: el muestreo por familia de plato',
            'Devoluciones y retrabajos: dos cosas distintas que se cuentan aparte',
            'El plato que sale por la puerta',
        ],
        'puntos': [
            'La tesis: lo único que se publica en español sobre el pase son '
            'reglas de comportamiento del tipo «no digas ya casi». Eso no es un '
            'procedimiento. Un procedimiento dice quién hace qué, en qué orden '
            'y qué pasa cuando algo falla.',
            'Los tres papeles y su secuencia: quien canta la comanda, quien la '
            'marcha por partidas y quien despacha el plato terminado. Explicar '
            'la confirmación en voz alta como parte del protocolo y no como '
            'formalismo: una comanda que no se confirma de vuelta no está '
            'cantada.',
            'El 86 como procedimiento y no como grito: quién puede declararlo, '
            'quién lo autoriza, a quién se avisa —sala en el momento, y la '
            'carta física o digital si va a durar—, y cómo se cierra. La '
            'decisión de autorizar un 86 es una fila de la matriz del capítulo '
            '19 precisamente porque cruza a sala.',
            'Medir el tiempo de pase sin cronómetro: se muestrea. Se anotan los '
            'minutos entre comanda y salida de unos cuantos platos por '
            'servicio, separando entrantes, principales y postres, y se compara '
            'con el objetivo de la casa. Enseñar los tres tiempos medios del '
            'año del caso y los tres objetivos, y decir expresamente que esos '
            'objetivos son de la casa: no existe ningún benchmark español '
            'publicado de tiempo de pase, y quien lo dé se lo está inventando.',
            'Devueltos y retrabajados, que es una distinción que casi ninguna '
            'cocina hace: el devuelto es el plato que vuelve de la mesa; el '
            'retrabajado es el que se rehace ANTES de salir. El segundo no se '
            've en ninguna cuenta y suele costar más dinero, porque se paga dos '
            'veces el producto y las horas. Enseñar los dos del año del caso y '
            'el indicador conjunto por base de cubiertos.',
            'El plato que sale por la puerta: qué exige mantener en caliente lo '
            'que va a esperar, qué envase aguanta el trayecto, cuánto tiempo se '
            'acepta y —lo más importante— qué platos NO viajan. La regla que '
            'cierra el epígrafe: si un plato no puede llegar como salió, no '
            'sale; y si sale, la ficha lleva escrito el envase y el tiempo '
            'máximo, igual que lleva el punto de cocción.',
        ],
        'cifras': [
            C('Tiempo medio de pase de entrantes en el año del caso', f'{X_CUAD}!Semana!AG57', 'num1'),
            C('Tiempo medio de pase de principales en el año del caso', f'{X_CUAD}!Semana!AH57', 'num1'),
            C('Tiempo medio de pase de postres en el año del caso', f'{X_CUAD}!Semana!AI57', 'num1'),
            C('Objetivo de la casa para el pase de entrantes', f'{X_CUAD}!Parámetros!B29', 'num'),
            C('Objetivo de la casa para el pase de principales', f'{X_CUAD}!Parámetros!B30', 'num'),
            C('Objetivo de la casa para el pase de postres', f'{X_CUAD}!Parámetros!B31', 'num'),
            C('Platos devueltos en el año del caso', f'{X_CUAD}!Semana!AO57', 'num'),
            C('Platos retrabajados en el año del caso', f'{X_CUAD}!Semana!AP57', 'num'),
            C('Devueltos y retrabajados por base de cubiertos en el año', f'{X_CUAD}!Semana!AQ57', 'num1'),
            C('Temperatura mínima de mantenimiento en caliente del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D58', 'num'),
        ],
        'sector': ['CE-10', 'MM-38'],
        'tablas': [
            {
                'titulo': 'Los tiempos de pase medidos contra el objetivo de la casa (desarrollo-carta-control-calidad.xlsx, hoja «Control de Calidad del Pase»)',
                'src': (X_CARTA, 'Control de Calidad del Pase'),
                'cols': [('Indicador', 'A', 'txt'), ('Medido', 'D', 'num1'),
                         ('Objetivo de la casa', 'E', 'num1'), ('Lectura', 'F', 'txt')],
                'filas': (49, 51),
                'nota': 'Los tres objetivos son criterio de la casa, no una cifra publicada por '
                        'nadie: son casillas editables y lo primero que hay que hacer es poner '
                        'las tuyas.',
            },
            {
                'titulo': 'El plato que viaja: qué sale por la puerta y qué no',
                'cabecera': ['Decisión', 'Regla', 'Por qué'],
                'filas': [
                    ['Temperatura de salida', 'Si el plato se sirve caliente, sale y se mantiene a 63 °C o más', 'Es la temperatura de mantenimiento en caliente del art. 30.2 del RD 1086/2020'],
                    ['Envase', 'Estanco, apilable y que no condense sobre el producto', 'El vapor atrapado arruina el crujiente y baja la temperatura del centro'],
                    ['Recipiente del cliente', 'Se acepta el reutilizable que trae el cliente, y se puede rechazar si está manifiestamente sucio o es inadecuado', 'Ley 7/2022, art. 18.3'],
                    ['Tiempo máximo hasta la entrega', 'Se escribe en la ficha del plato, como el punto de cocción', 'Lo que no está escrito lo decide el repartidor'],
                    ['Fritos y masas crujientes', 'No viajan, o viajan con el elemento crujiente aparte', 'Llegan blandos y vuelven como queja'],
                    ['Platos con salsa emulsionada en caliente', 'No viajan', 'Se cortan con el movimiento y el descenso de temperatura'],
                    ['Crudos y semicrudos', 'Sólo si la cadena de frío del trayecto está resuelta y documentada', 'Es el mismo producto que obliga a congelación preventiva en cocina'],
                    ['Etiqueta', 'Identificación del plato y aviso de alérgenos, también fuera', 'La obligación de informar no se queda en la puerta'],
                ],
                'nota': V_TEMP + ' — el envase de plástico de un solo uso puede cobrarse aparte, '
                        'por el título V de la Ley 7/2022; la comida no.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 9,
        'titulo': 'Los KPI que Son de Cocina (y los que No)',
        'resumen_indice': 'los siete indicadores de la casa, uno a uno y con su error típico, y por qué el semáforo no se enciende hasta que pones tu objetivo.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Dar una lista corta y defendible de lo que un chef sí '
                    'puede medir, decir con honestidad que es una propuesta de '
                    'la casa y no un estándar, y enseñar a leer el semáforo sin '
                    'discutirlo cada lunes.',
        'epigrafes': [
            'Por qué esta lista es una propuesta de la casa y no un estándar',
            'Los siete indicadores, uno a uno, con su error típico',
            'Los que se venden como de cocina y son de sala, de marketing o de finanzas',
            'El objetivo lo pones tú: el semáforo no se enciende hasta que hay casilla',
            'Dónde acaba este manual y empieza la Guía Food Cost',
        ],
        'puntos': [
            'Abrir con la honestidad que ordena todo el capítulo: no existe un '
            'estándar publicado de indicadores de cocina en español. Ésta es '
            'nuestra lista, con el porqué de cada uno y su error típico. '
            'Presentarla como estándar sería exactamente lo que este manual '
            'critica del resto.',
            'Recorrer los siete por el error que corrigen, no por su fórmula: '
            'la merma por partida (mirar el total de la cocina la esconde, '
            'porque una partida compensa a otra), el tiempo de pase por familia '
            'de plato (una media única mezcla un postre con un arroz), las '
            'incidencias de alérgenos (contar sólo las que llegaron al cliente '
            'deja fuera justo las que enseñan dónde falla el proceso), las '
            'horas de cocina por cubierto (alimentarlo con las horas del '
            'contrato en vez de las del registro), el cumplimiento de ficha '
            '(preguntar si hay ficha en vez de si se ha seguido), los devueltos '
            'y retrabajados (registrar sólo la devolución del cliente) y la '
            'rotación de la brigada (mezclarla con la de sala).',
            'La línea que separa: de las listas de indicadores «de cocina» que '
            'circulan, casi todos son de sala, de marketing o de finanzas '
            '—ticket medio, rotación de mesas, reseñas, ocupación—. No son '
            'malos indicadores: no son del chef. Y el que sí cruza, el food '
            'cost, se mide en el cuadro del Manual del Manager y se decide en '
            'la Guía Food Cost.',
            'El semáforo: en este libro está gris mientras la casilla de tu '
            'objetivo esté vacía, a propósito. Un semáforo que se enciende con '
            'un umbral que no has decidido tú no te dice nada, y encima te '
            'acostumbra a discutirlo. Se decide una vez, se escribe y luego no '
            'se discute cada semana.',
            'Cerrar con la lectura del año del caso: cuántos indicadores '
            'terminaron fuera de objetivo y qué dice la lectura automática. Y '
            'con la advertencia de método: el total del año no es la media de '
            'las semanas, y una semana floja pesa lo que produjo.',
            'Frontera explícita, con esta frase: «los números del dinero —food '
            'cost, labor cost, prime cost, ticket medio— son del Manual del '
            'Manager, caps. 2 y 3; aquí no aparece ninguno». Este cuadro de '
            'mando no tiene ni una columna financiera, y eso es deliberado.',
        ],
        'cifras': [
            C('Merma global de la cocina en el año del caso', f'{X_CUAD}!Semana!AF57', 'pct1'),
            C('Tiempo medio de pase de principales en el año', f'{X_CUAD}!Semana!AH57', 'num1'),
            C('Incidencias de alérgenos por base de cubiertos en el año', f'{X_CUAD}!Semana!AL57', 'num2'),
            C('Objetivo de la casa para las incidencias de alérgenos', f'{X_CUAD}!Parámetros!B32', 'num2'),
            C('Horas de cocina por cubierto en el año', f'{X_CUAD}!Semana!AN57', 'num2'),
            C('Objetivo de la casa para las horas de cocina por cubierto', f'{X_CUAD}!Parámetros!B33', 'num2'),
            C('Devueltos y retrabajados por base de cubiertos en el año', f'{X_CUAD}!Semana!AQ57', 'num1'),
            C('Objetivo conjunto de la casa para devueltos y retrabajados', f'{X_CUAD}!Parámetros!B36', 'num1'),
            C('Indicadores fuera de objetivo en el año', f'{X_CUAD}!Semana!AR57', 'num'),
            C('Lectura automática del año', f'{X_CUAD}!Semana!AS57', 'txt'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'Los siete indicadores de cocina, con su error típico (cuadro-de-mando-cocina.xlsx, hoja «KPI y Definiciones»)',
                'src': (X_CUAD, 'KPI y Definiciones'),
                'cols': [('Indicador', 'A', 'txt'), ('Cómo se calcula', 'B', 'txt'),
                         ('Unidad', 'C', 'txt'), ('Error típico', 'D', 'txt'),
                         ('Objetivo de la casa', 'F', 'txt')],
                'filas': (5, 11),
                'nota': 'La columna del error típico es la que más se usa: casi todos los '
                        'indicadores de una cocina se estropean por cómo se alimentan, no por '
                        'cómo se calculan.',
            },
            {
                'titulo': 'Los objetivos de la casa de esta cocina modelada (cuadro-de-mando-cocina.xlsx, hoja «Parámetros»)',
                'src': (X_CUAD, 'Parámetros'),
                'cols': [('Indicador', 'A', 'txt'), ('Objetivo', 'B', 'num2'),
                         ('Unidad', 'C', 'txt'), ('Cómo se lee', 'D', 'txt')],
                'filas': (29, 36),
                'nota': 'Ninguno de estos números es un estándar del sector: son los objetivos '
                        'de esta cocina modelada y todos viven en casillas editables. Lo primero '
                        'que hay que hacer con el libro es sustituirlos por los tuyos.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 10,
        'titulo': 'La Merma de tu Partida',
        'resumen_indice': 'merma de proceso frente a desperdicio, merma por partida contra la producción, y las tres semanas malas que el promedio del mes esconde.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Enseñar a medir la merma donde se produce —en la partida, '
                    'contra lo que esa partida produjo— y a leerla semana a '
                    'semana. Y dejar dicho, con todas las letras, que este '
                    'manual no da ningún porcentaje de merma «normal».',
        'epigrafes': [
            'Merma de proceso y desperdicio: dos pérdidas que no se gestionan igual',
            'Merma por partida contra la producción, no por producto contra las compras',
            'Cómo se alimenta la fila de la semana en quince minutos',
            'La partida que se come el margen: leer la columna, no el total',
            'Por qué aquí no hay ningún porcentaje de merma normal',
        ],
        'puntos': [
            'La distinción que abre el capítulo: la merma es pérdida de '
            'RENDIMIENTO en el proceso —limpieza, cocción, evaporación, '
            'recortes—; el desperdicio es comida servible que se tira, y tiene '
            'su propia jerarquía legal, que se trata en el capítulo 16. Se '
            'mezclan siempre y se gestionan con la misma hoja, y por eso ni una '
            'ni otra se corrigen nunca.',
            'La frontera con los dos productos que rozan, dicha en dos frases '
            'exactas: «el rendimiento del ingrediente y la merma de cocción se '
            'calculan en la Guía Food Cost, con su libro de rendimiento y '
            'mermas por producto; aquí se mide la merma agregada de cada '
            'partida contra lo que esa partida produjo» y «la merma por '
            'producto y por categoría de compra la lleva el Kit de Inventario, '
            'contra las compras del mes». Este libro no reconstruye ninguno de '
            'los dos registros: toma un total pesado y lo divide por la '
            'producción.',
            'Cómo se alimenta la fila de la semana: se pesa la merma de cada '
            'partida —se pesa, no se estima—, se anota la producción en '
            'raciones y el libro hace el resto usando los kilos de materia '
            'prima neta por ración que están en parámetros. Quince minutos el '
            'lunes, con las cuatro columnas de la semana anterior.',
            'La lectura que justifica todo el capítulo: en el año del caso la '
            'merma global está en objetivo, y aun así hay tres semanas seguidas '
            'con la partida de fríos disparada. El promedio del año se las '
            'traga enteras. Enseñar la comparación entre la merma global de esa '
            'semana y la de la partida concreta, y las preguntas que se hacen '
            'ese lunes: qué producto entró, quién estuvo en la partida, qué se '
            'produjo de más y qué se tiró.',
            'Por qué no hay benchmark, dicho sin rodeos: el rango de merma '
            '«sano» que circula lo publican proveedores de software sin un solo '
            'estudio citado, y las cifras de pérdida del sector por mermas '
            'vienen de un trabajo de hace más de diez años sin confirmación '
            'directa. Tu cifra propia sale en cuatro semanas de pesar, y vale '
            'más que cualquiera de ésas.',
            'Cerrar con el objetivo por partida: no se pone el mismo a todas. '
            'Una partida de fríos con mucha limpieza de producto no puede tener '
            'el mismo objetivo que una de postres, y el libro trae una casilla '
            'por partida precisamente por eso.',
        ],
        'cifras': [
            C('Merma global de la cocina en el año del caso', f'{X_CUAD}!Semana!AF57', 'pct1'),
            C('Merma total del año en kilos', f'{X_CUAD}!Semana!V57', 'num'),
            C('Materia prima neta producida en el año, en kilos', f'{X_CUAD}!Semana!AE57', 'num'),
            C('Merma del año de la partida de pase y caliente', f'{X_CUAD}!Semana!W57', 'pct1'),
            C('Merma del año de la partida de fríos y entrantes', f'{X_CUAD}!Semana!X57', 'pct1'),
            C('Merma del año de la partida de postres y panadería', f'{X_CUAD}!Semana!Y57', 'pct1'),
            C('Merma del año de la partida de barra y bebidas', f'{X_CUAD}!Semana!Z57', 'pct1'),
            C('Objetivo de merma de la partida de pase y caliente', f'{X_CUAD}!Parámetros!D15', 'pct1'),
            C('Merma global de la primera semana mala', f'{X_CUAD}!Semana!AF37', 'pct1'),
            C('Merma de fríos y entrantes en esa misma semana', f'{X_CUAD}!Semana!X37', 'pct1'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'Siete semanas seguidas, con las tres malas en medio (cuadro-de-mando-cocina.xlsx, hoja «Semana»)',
                'src': (X_CUAD, 'Semana'),
                'cols': [('Semana ISO', 'A', 'num'), ('Cubiertos servidos', 'D', 'num'),
                         ('Merma global (%)', 'AF', 'pct1'),
                         ('Merma de pase y caliente (%)', 'W', 'pct1'),
                         ('Merma de fríos y entrantes (%)', 'X', 'pct1'),
                         ('Indicadores fuera de objetivo', 'AR', 'num'),
                         ('Lectura de la semana', 'AS', 'txt')],
                'filas': (35, 41),
                'nota': 'Mira la columna de fríos y entrantes, no la de la merma global: la '
                        'global apenas se mueve porque las otras partidas la compensan, y por eso '
                        'un cuadro de mando sin columna por partida no sirve para nada.',
            },
            {
                'titulo': 'Las partidas de la cocina y su objetivo propio de merma (cuadro-de-mando-cocina.xlsx, hoja «Parámetros»)',
                'src': (X_CUAD, 'Parámetros'),
                'cols': [('Partida', 'A', 'txt'), ('¿Produce raciones?', 'B', 'txt'),
                         ('Kg de materia prima neta por ración', 'C', 'num2'),
                         ('Objetivo de merma (%)', 'D', 'pct1'),
                         ('Qué produce', 'E', 'txt')],
                'filas': (15, 20),
                'nota': 'Los kilos por ración son el puente entre las raciones que produces y los '
                        'kilos que mermas: si esa casilla está mal, el porcentaje de merma está '
                        'mal aunque peses perfecto.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 11,
        'titulo': 'Compras y Especificaciones desde la Cocina',
        'resumen_indice': 'la especificación técnica que se le da al proveedor, lo que el convenio encarga al economato, y lo que te vincula al comprar.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Que el chef deje de negociar sólo el precio y empiece a '
                    'escribir lo que compra. Una especificación de media página '
                    'ahorra más discusiones que tres llamadas, y es lo que '
                    'permite rechazar una entrega sin abrir un conflicto.',
        'epigrafes': [
            'La especificación técnica: lo que le pides al proveedor además del precio',
            'El economato y lo que el convenio le encarga',
            'Lo que te vincula al comprar y no al elaborar',
            'Qué se guarda del albarán y por qué',
            'Cuando el proveedor cambia el calibre: qué se revisa antes de aceptarlo',
        ],
        'puntos': [
            'La tesis: el precio es la última línea de una compra, no la '
            'primera. Lo que decide si el plato sale como dice la ficha es el '
            'calibre, el corte, el grado de maduración, el formato de envío y '
            'la tolerancia que se acepta. Sin eso escrito, cada entrega es una '
            'negociación nueva.',
            'La especificación, campo a campo, con el ejemplo del plato de la '
            'ficha: qué producto, en qué calibre o peso por pieza, con qué '
            'corte, en qué formato de envío y con qué temperatura de recepción, '
            'con qué documentación y con qué tolerancia. Y la regla que la hace '
            'útil: se manda por escrito y se acepta por escrito.',
            'El papel del economato, que el convenio describe expresamente y '
            'casi nadie usa: entre sus funciones está elaborar peticiones de '
            'ofertas, evaluarlas y recomendar la adjudicación. Es decir, que la '
            'comparación de proveedores es trabajo de alguien, no una '
            'improvisación del chef entre servicios.',
            'La distinción que casi nadie hace y que evita un susto: hay '
            'obligaciones que te vinculan al COMPRAR, no al elaborar. Los '
            'límites de contaminantes se comprueban en la compra y en la '
            'documentación del proveedor; el reglamento que los fija sustituyó '
            'al anterior, y citar el derogado es lo que sigue haciendo medio '
            'sector.',
            'Trazabilidad práctica en la recepción: saber de quién viene cada '
            'producto y poder demostrarlo. Un paso atrás siempre; hacia '
            'adelante, sólo si suministras a otro establecimiento, no al '
            'consumidor final. Qué se guarda del albarán y durante cuánto: '
            'proveedor, producto, lote, cantidad y fecha, y la temperatura si '
            'venía refrigerado. Frontera: el registro de recepción con sus '
            'columnas está en el Kit de Inventario.',
            'El cambio de calibre, que es el caso más frecuente: el proveedor '
            'sirve otro formato y el plato cambia sin que nadie lo decida. El '
            'orden de revisión es siempre el mismo —alérgenos, rendimiento y '
            'gramaje, punto de cocción y, sólo al final, coste—, y el resultado '
            'es una versión nueva de la ficha o un rechazo. Aceptar «lo que '
            'había» sin revisar es cómo se rompe un estándar que costó meses.',
        ],
        'cifras': [
            C('Coste por ración copiado del escandallo en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B16', 'eur2'),
            C('Raciones vendidas al mes del plato de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B17', 'num'),
            C('Coste de materia prima al mes del plato de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B18', 'eur2'),
            C('Kilos de materia prima neta por ración en pase y caliente', f'{X_CUAD}!Parámetros!C15', 'num2'),
            C('Kilos de materia prima neta por ración en fríos y entrantes', f'{X_CUAD}!Parámetros!C16', 'num2'),
            C('Materia prima neta producida en el año, en kilos', f'{X_CUAD}!Semana!AE57', 'num'),
            C('Raciones producidas en el año del caso', f'{X_CUAD}!Semana!M57', 'num'),
            C('Merma total del año en kilos', f'{X_CUAD}!Semana!V57', 'num'),
        ],
        'sector': ['CE-18', 'CE-09', 'CE-16'],
        'tablas': [
            {
                'titulo': 'La especificación técnica de una referencia: qué se escribe y por qué',
                'cabecera': ['Campo de la especificación', 'Qué se escribe', 'Qué evita'],
                'filas': [
                    ['Producto y presentación', 'Denominación exacta, con la parte de la pieza si aplica', 'Que llegue otra cosa con el mismo nombre comercial'],
                    ['Calibre o peso por pieza', 'Rango aceptado, con máximo y mínimo', 'Que cambie el número de raciones por pieza'],
                    ['Corte y limpieza', 'Quién hace el trabajo, si viene limpio o entero', 'Que la merma pase del proveedor a tu partida sin avisar'],
                    ['Grado de maduración o punto', 'El estado en que se acepta el producto', 'Tener que tirarlo o esperarlo tres días'],
                    ['Formato de envío y envase', 'Caja, bandeja, vacío, número de piezas', 'Que no quepa en tu cámara o llegue aplastado'],
                    ['Temperatura de recepción', 'La que se exige y se comprueba al descargar', 'Aceptar una cadena de frío rota'],
                    ['Documentación', 'Albarán con lote y fecha, y los certificados que apliquen', 'No poder demostrar de dónde viene el producto'],
                    ['Tolerancia y qué se hace fuera de ella', 'Qué desviación se acepta y qué pasa si se supera', 'Discutir en la puerta, con el repartidor esperando'],
                ],
                'nota': 'Media página por referencia y sólo para las que más pesan en tu compra. '
                        'La especificación se manda por escrito y se acepta por escrito: eso es '
                        'lo que convierte un rechazo en un trámite y no en un conflicto.',
            },
            {
                'titulo': 'Qué te obliga al comprar y qué al elaborar',
                'cabecera': ['Obligación', 'Cuándo te alcanza', 'Qué hace la cocina'],
                'filas': [
                    ['Límites de contaminantes de los alimentos', 'Al comprar: el producto debe cumplirlos al ponerse en el mercado', 'Se exige al proveedor y se guarda su documentación'],
                    ['Trazabilidad de un paso atrás', 'Siempre', 'Se guarda el albarán con proveedor, producto, lote, cantidad y fecha'],
                    ['Trazabilidad de un paso adelante', 'Sólo si suministras a otro establecimiento', 'Un restaurante que sirve al consumidor final no está obligado'],
                    ['Congelación preventiva del producto de la pesca', 'Antes de servirlo crudo o con un tratamiento insuficiente', 'O la hace el proveedor y lo justifica por escrito, o la haces tú'],
                    ['Comprobación de la temperatura de recepción', 'Al descargar', 'Se mide y se anota; el registro está en el Kit de Inventario'],
                ],
                'nota': 'Verificado el 06-09-2026 · Reglamento (UE) 2023/915, que derogó al '
                        'Reglamento (CE) 1881/2006, y art. 18 del Reglamento (CE) 178/2002 · '
                        'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0915',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 12,
        'titulo': 'Desarrollo de Carta y Menús de Temporada con Criterio de Coste',
        'resumen_indice': 'los cinco hitos con fecha, el registro de pruebas, el plato que lleva demasiados días sin ficha y qué decide el chef y qué dirección.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Convertir la renovación de carta en un proceso con fechas '
                    'en vez de en una carrera de tres semanas antes de '
                    'temporada. Y dejar claro qué decisión es del chef y cuál '
                    'no lo es.',
        'epigrafes': [
            'Los cinco hitos: probar, costear, documentar, formar y lanzar',
            'El registro de pruebas: qué se anota de cada prueba y qué decide',
            'El plato que lleva demasiados días en prueba sin ficha cerrada',
            'Qué decide el chef y qué decide la dirección',
            'Dónde acaba el desarrollo y empieza la ingeniería de menú',
        ],
        'puntos': [
            'La tesis: una carta nueva no se cierra el día que el plato gusta. '
            'Se cierra cuando está costeado, documentado y la brigada sabe '
            'hacerlo. Los cinco hitos van en ese orden y cada uno tiene fecha; '
            'saltarse el tercero es lo que produce el plato estrella que sale '
            'distinto según el turno.',
            'El registro de pruebas, con lo que sí hace falta anotar: fecha, '
            'número de prueba, partida, resultado del uno al cinco, coste '
            'estimado por ración, decisión y observación. Enseñar el resumen '
            'del caso —cuántas pruebas registradas, resultado medio, coste '
            'medio estimado por ración y cuántas hubo que repetir— y explicar '
            'que repetir pruebas no es un fracaso: es la parte barata del '
            'desarrollo.',
            'La alerta de días en prueba, que es la que impide que un plato viva '
            'seis meses en el limbo: la hoja avisa cuando un plato supera los '
            'días máximos desde su primera prueba sin tener la ficha cerrada. '
            'En el caso hay uno, y hay que decir qué se hace con él: se cierra '
            'la ficha o se descarta, pero no se queda.',
            'El reparto de decisiones, que es lo que evita la mitad de los '
            'conflictos con dirección: la propuesta de plato y su ficha son del '
            'chef; el precio de venta, no. Se explica aquí en una línea y se '
            'desarrolla con la matriz del capítulo 19.',
            'Frontera con la Guía Food Cost, en una frase: «qué platos se quedan '
            'en la carta, con qué precio y en qué posición, se decide con la '
            'matriz de carta de la Guía Food Cost; aquí se decide cómo se '
            'desarrolla un plato hasta que puede entrar». Este capítulo es el '
            'proceso, no la decisión de mix.',
            'Cerrar con la lista de comprobación del lanzamiento: ficha cerrada '
            'y versionada, coste copiado del escandallo, alérgenos revisados, '
            'brigada formada en el puesto, sala informada y foto de montaje '
            'colgada. Sin las seis, el plato no sale a carta.',
        ],
        'cifras': [
            C('Platos en desarrollo en el calendario de temporada', f'{X_CARTA}!Calendario de Temporada!C28', 'num'),
            C('Platos con la ficha técnica cerrada', f'{X_CARTA}!Calendario de Temporada!C29', 'num'),
            C('Porcentaje de platos en desarrollo con ficha cerrada', f'{X_CARTA}!Calendario de Temporada!C30', 'pct1'),
            C('Platos que superan los días máximos en prueba', f'{X_CARTA}!Calendario de Temporada!C31', 'num'),
            C('Días máximos en prueba sin ficha cerrada que fija la casa', f'{X_CARTA}!Calendario de Temporada!C8', 'num'),
            C('Pruebas de plato registradas en total', f'{X_CARTA}!Registro de Pruebas de Plato!C39', 'num'),
            C('Resultado medio de todas las pruebas, de uno a cinco', f'{X_CARTA}!Registro de Pruebas de Plato!C40', 'num2'),
            C('Coste estimado medio por ración en las pruebas', f'{X_CARTA}!Registro de Pruebas de Plato!C41', 'eur2'),
            C('Pruebas que hubo que repetir', f'{X_CARTA}!Registro de Pruebas de Plato!C44', 'num'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'El calendario de temporada, plato a plato (desarrollo-carta-control-calidad.xlsx, hoja «Calendario de Temporada»)',
                'src': (X_CARTA, 'Calendario de Temporada'),
                'cols': [('Id', 'A', 'txt'), ('Plato', 'B', 'txt'),
                         ('Partida', 'C', 'txt'), ('Estado', 'I', 'txt'),
                         ('Ficha técnica cerrada', 'J', 'txt'),
                         ('Días desde la primera prueba', 'K', 'num'),
                         ('Aviso', 'M', 'txt')],
                'filas': (13, 24),
                'nota': 'La columna de días es la que hace el trabajo: un plato que lleva '
                        'demasiado tiempo probándose sin ficha cerrada no es un plato en '
                        'desarrollo, es un plato parado.',
            },
            {
                'titulo': 'Quién decide qué en una carta nueva',
                'cabecera': ['Decisión', 'Quién decide', 'Qué necesita antes de decidir'],
                'filas': [
                    ['Qué platos se prueban esta temporada', 'El chef', 'La estacionalidad, el hueco de la carta y lo que la brigada puede sostener'],
                    ['Si un plato pasa de prueba a desarrollo', 'El chef', 'Dos pruebas registradas y un coste estimado por ración'],
                    ['Cerrar la ficha técnica y su versión', 'El chef', 'Pasos, alérgenos, conservación y foto de montaje'],
                    ['Precio de venta del plato', 'La dirección, con la propuesta del chef', 'El escandallo cerrado y la posición del plato en la carta'],
                    ['Retirar un plato de la carta', 'La dirección, con informe del chef', 'Ventas, margen y carga de la partida'],
                    ['Fecha de lanzamiento', 'El chef con sala', 'Brigada formada, producto contratado y sala informada'],
                ],
                'nota': 'Esta tabla es un resumen: la matriz completa de las decisiones que '
                        'cruzan entre cocina, sala y dirección está en el capítulo 19, con quién '
                        'responde de cada una.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 13,
        'titulo': 'Seguridad Alimentaria: de lo que Respondes Tú, no el Propietario',
        'resumen_indice': 'la cultura de seguridad alimentaria como obligación de la dirección, las cinco temperaturas y el binomio, el anisakis, las tres fechas y qué se hace cuando se cae el frío.',
        'palabras': 2000, 'bloques': 3,
        'objetivo': 'Dejar al chef con las cifras vigentes en la cabeza y con '
                    'la frontera de su responsabilidad clara. Es el capítulo '
                    'que más citas caducadas corrige del oficio, y el que más '
                    'se juega en una inspección.',
        'epigrafes': [
            'La cultura de seguridad alimentaria es obligación de la dirección, y hay que demostrarla',
            'El autocontrol que sostiene el chef: responsable designado y revisión por cambio',
            'Las cinco temperaturas y el binomio de enfriamiento',
            'Anisakis: qué producto, qué tratamiento y qué justificante',
            'Las tres fechas al congelar, y qué no es elaboración propia',
            'Cuando se cae el frío: qué se tira, qué no y qué se apunta',
        ],
        'puntos': [
            'Abrir por donde nadie abre: desde la modificación de 2021, el '
            'titular tiene que establecer y mantener una cultura de seguridad '
            'alimentaria adecuada y PRESENTAR PRUEBAS de ello. Eso convierte al '
            'chef en el responsable de que exista, se comunique y se demuestre '
            '—no en el que rellena los partes—. Y el propio texto dice que la '
            'aplicación tiene en cuenta la naturaleza y el tamaño de la '
            'empresa: una cocina de seis personas no necesita el sistema de una '
            'cadena.',
            'El autocontrol como lo que el chef sostiene: un procedimiento '
            'permanente basado en los principios del sistema, con una persona '
            'designada, que se revisa cada vez que cambia un producto, un '
            'proceso o un proveedor. Los registros concretos —temperaturas, '
            'limpieza, plagas, trazabilidad— están en el Pack APPCC y no se '
            'repiten aquí: lo que aporta este capítulo es cuándo hay que '
            'revisar el sistema y quién responde de que se revise.',
            'Las CINCO temperaturas, escritas juntas por primera vez y cada una '
            'con su apartado: mantenimiento en caliente a 63 grados o más; '
            'refrigeración a 4 grados o menos si la comida se va a consumir en '
            'más de 24 horas y a 8 o menos si es en menos de 24; congelación a '
            'menos 18 o menos; y recalentado a 74 grados durante al menos '
            'quince segundos en el centro del alimento, en el plazo de una hora '
            'desde que sale del frigorífico. Más el binomio que casi nunca se '
            'escribe: de 60 a 10 grados en menos de dos horas al enfriar.',
            'Los dos matices del artículo que evitan un error caro. Primero: la '
            'norma permite trabajar con temperaturas distintas cuando se '
            'justifica con evidencia ante la autoridad, PERO ese apartado se '
            'refiere sólo a la refrigeración: no autoriza a bajar del '
            'mantenimiento en caliente ni a subir de la congelación. Segundo: '
            'el mismo artículo cierra diciendo que todo lo recalentado que no '
            'se consuma se descarta y no vuelve a calentarse ni a almacenarse.',
            'Anisakis, con el alcance corregido: congelar a menos 20 grados '
            'durante un mínimo de veinticuatro horas o a menos 35 durante un '
            'mínimo de quince, en la totalidad del producto. Alcanza a los '
            'productos de la pesca que se vayan a consumir crudos, escabechados, '
            'en salazón o sometidos a cualquier otro tratamiento insuficiente '
            'para matar las larvas —marinados, ahumados en frío, semicrudos—; '
            'excluye expresamente el pescado de aguas continentales; y la '
            'acuicultura marina queda exceptuada si cada lote lleva la '
            'declaración del operador de origen. La congelación puede haberla '
            'hecho una etapa anterior si está justificado documentalmente, y '
            'tampoco hace falta si antes del consumo se aplica un tratamiento '
            'térmico de al menos 60 grados durante al menos un minuto en el '
            'centro del producto. Y hay que informar al cliente por cartel o '
            'por la carta.',
            'Las tres fechas de la etiqueta al congelar una elaboración propia: '
            'fecha de elaboración o transformación, fecha de congelación y '
            'fecha de caducidad o consumo preferente del producto congelado. Y '
            'el detalle práctico: si toda esa información va en la etiqueta, no '
            'hace falta llevar además el registro aparte.',
            'Qué NO es elaboración propia, que es un mito que sale caro en la '
            'carta: la mención es voluntaria, y fraccionar o envasar un '
            'producto elaborado por otro, cortar o deshuesar carne fresca y '
            'limpiar o cortar pescado NO son elaboración. Y la contrapartida '
            'que casi nadie conoce: quien pone esa mención sólo puede vender '
            'esos alimentos en el establecimiento donde se elaboraron o en sus '
            'sucursales, cosa que importa mucho si hay obrador central.',
            'El epígrafe que no está en ningún otro sitio: cuando se cae el '
            'frío. Qué se hace en la primera hora (no abrir, medir, anotar la '
            'hora de la avería), qué producto se salva y cuál no según su '
            'temperatura y su naturaleza, por qué lo que ya se recalentó no '
            'vuelve a la cámara, qué se apunta —hora, temperatura medida, '
            'producto, decisión y quién la tomó— y por qué esa nota es lo que '
            'te permite justificar la decisión meses después.',
        ],
        'cifras': [
            C('Temperatura mínima de mantenimiento en caliente del muestreo del pase', f'{X_CARTA}!Control de Calidad del Pase!D58', 'num'),
            C('Muestras de elaboraciones que se mantienen en caliente', f'{X_CARTA}!Control de Calidad del Pase!D59', 'num'),
            C('De ellas, por debajo del mínimo de mantenimiento en caliente', f'{X_CARTA}!Control de Calidad del Pase!D60', 'num'),
            C('Temperatura de emplatado más baja del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D56', 'num1'),
            C('Temperatura de emplatado más alta del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D57', 'num1'),
            C('Temperatura mínima de mantenimiento en caliente de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B47', 'num'),
            C('Días tras los que el libro avisa de revisar el estado normativo', f'{X_AUD}!Estado Normativo!B9', 'num'),
            C('Aviso de revisión del estado normativo en la fecha del ejemplo', f'{X_AUD}!Estado Normativo!B10', 'txt'),
        ],
        'sector': ['CE-02', 'CE-10', 'CE-12', 'CE-13', 'CE-14', 'CE-09',
                   'MM-29', 'MM-32', 'MM-33'],
        'tablas': [
            {
                'titulo': 'Las cinco temperaturas y el binomio que rigen hoy en tu cocina',
                'cabecera': ['Situación', 'Valor vigente', 'Apartado'],
                'filas': [
                    ['Mantenimiento en caliente', '63 °C o más', 'Art. 30.2 del RD 1086/2020'],
                    ['Refrigeración de comidas que se consumen en menos de 24 horas', '8 °C o menos', 'Art. 30.3 del RD 1086/2020'],
                    ['Refrigeración de comidas que se consumen en más de 24 horas', '4 °C o menos', 'Art. 30.3 del RD 1086/2020'],
                    ['Congelación', 'Menos 18 °C o menos', 'Art. 30.4 del RD 1086/2020'],
                    ['Recalentado', '74 °C durante al menos 15 segundos en el centro del alimento, en el plazo de una hora desde que sale del frigorífico', 'Art. 30.7 del RD 1086/2020'],
                    ['Enfriamiento rápido tras la cocción', 'De 60 °C a 10 °C en menos de dos horas', 'Art. 30.6 del RD 1086/2020'],
                    ['Temperaturas distintas de las de refrigeración', 'Sólo con evidencia científica documentada ante la autoridad competente, y sólo para la refrigeración', 'Art. 30.5 del RD 1086/2020'],
                    ['Lo recalentado que no se consume', 'Se descarta: no vuelve a calentarse ni a almacenarse', 'Art. 30.7 del RD 1086/2020'],
                    ['Congelación preventiva del producto de la pesca', 'Menos 20 °C durante 24 horas como mínimo, o menos 35 °C durante 15 horas, en la totalidad del producto', 'Art. 8.1 del RD 1021/2022'],
                ],
                'nota': V_TEMP + ' y ' + V_1021 + ' — el RD 3484/2000 y el RD 1420/2006 están '
                        'DEROGADOS desde el 22 de diciembre de 2022: si tu documentación los '
                        'cita, está caducada.',
            },
            {
                'titulo': 'El estado de cada norma a la fecha de corte (auditoria-interna-cocina.xlsx, hoja «Estado Normativo»)',
                'src': (X_AUD, 'Estado Normativo'),
                'cols': [('Norma', 'A', 'txt'),
                         ('Estado a la fecha de corte', 'B', 'txt'),
                         ('Qué tiene que hacer el chef', 'C', 'txt')],
                'filas': (13, 26),
                'nota': 'La hoja lleva su fecha de corte en una casilla editable y avisa cuando '
                        'han pasado los días que tú decidas: la ley cambia, y lo que envejece es '
                        'el documento, no el método. Cada fila lleva en el propio libro su '
                        'artículo, su enlace y la fecha en que se comprobó.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 14,
        'titulo': 'Alérgenos desde Dentro de la Cocina',
        'resumen_indice': 'dónde está de verdad la obligación, el equipo y el recipiente compartidos, los alérgenos de proceso de la ficha y la alergia que llega con el plato montado.',
        'palabras': 2000, 'bloques': 3,
        'objetivo': 'Dar la parte de los alérgenos que sólo se ve desde dentro '
                    'de la cocina: dónde entra el alérgeno en cada elaboración, '
                    'qué se comparte y qué no, y qué se hace cuando la alergia '
                    'llega al pase con el plato ya montado.',
        'epigrafes': [
            'No hay un capítulo de alérgenos en el reglamento: dónde está la obligación',
            'Los catorce y el plato sin envasar: por qué el cartel no basta',
            'Alérgenos de proceso: equipo, recipiente y superficie compartidos',
            'Sin gluten y muy bajo en gluten: dos declaraciones con dos límites',
            'La alergia que llega al pase con el plato montado',
            'Qué se registra cuando ocurre una incidencia',
        ],
        'puntos': [
            'Empezar corrigiendo la cita que repite medio sector: el reglamento '
            'de higiene NO tiene un capítulo de alérgenos. La obligación de no '
            'cruzarlos es el punto 9 del capítulo IX de su anexo II, insertado '
            'en 2021, y dice que el equipo, los medios de transporte y los '
            'recipientes utilizados para transformar, manipular, transportar o '
            'almacenar una de esas sustancias no se utilizarán para otros '
            'alimentos a menos que se hayan limpiado. El capítulo V bis, que '
            'muchos suponen de alérgenos, es de redistribución de alimentos.',
            'Los catorce de declaración obligatoria y la regla del plato sin '
            'envasar: la información es obligatoria también ahí, y el cartel de '
            '«consulte al personal» no basta por sí solo. Hace falta que la '
            'información esté registrada por escrito o electrónicamente en el '
            'establecimiento y sea fácilmente accesible para el personal, para '
            'la autoridad de control y para el consumidor que la pida. Además, '
            'hay que indicar de forma visible dónde está esa información, en '
            'cada sección que venda esos alimentos —salvo que haya etiqueta por '
            'plato o el local sirva comidas adaptadas a personas alérgicas—.',
            'Los alérgenos DE PROCESO, que es lo que aporta este manual: por '
            'cada elaboración, qué alérgeno está presente como ingrediente, '
            'cuál puede llegar por traza EN ESTA elaboración concreta, con qué '
            'utensilio y en qué superficie se comparte, y qué sustitución es '
            'posible. Enseñar el recuento de la ficha del ejemplo: cuántos como '
            'ingrediente, cuántos por traza y cuántos por utensilio compartido. '
            'Esa tercera columna es la que ninguna plantilla trae y la que más '
            'incidencias evita.',
            'Frontera, dicha en una frase: «la declaración de alérgenos plato a '
            'plato de toda la carta, con sus catorce columnas, vive en el Pack '
            'APPCC; aquí va lo que pasa dentro de la elaboración». Nunca las '
            'dos declaraciones completas en dos sitios: es la forma más segura '
            'de que una de las dos quede desactualizada.',
            'Las dos declaraciones de gluten y sus dos límites: «sin gluten» '
            'sólo puede usarse cuando el alimento, tal como se vende al '
            'consumidor final, no contiene más de 20 miligramos por kilo, y '
            '«muy bajo en gluten», hasta 100. Y el matiz que casi nadie sabe: '
            'la avena de un producto así declarado no puede pasar de 20 '
            'miligramos por kilo. El ámbito del reglamento son los alimentos, '
            'sin excluir la restauración: anunciar un plato «sin gluten» te '
            'obliga a sostener ese límite y el proceso que lo garantiza.',
            'El protocolo de la alergia que llega tarde, paso a paso: la '
            'comanda con alergia llega marcada y se canta en voz alta; el plato '
            'se elabora con material limpio y reservado; sale identificado y se '
            'entrega en mano a la mesa. Y la regla de oro de la brigada: nadie '
            'dice «creo que no lleva». O se comprueba, o no se sirve. Enseñar '
            'las incidencias del año del caso, su gravedad máxima y la tasa por '
            'base de cubiertos contra el objetivo de la casa.',
            'Qué se registra cuando ocurre una incidencia y por qué se cuentan '
            'también las que NO llegaron al cliente: la que se detecta en el '
            'pase es la que enseña dónde falla el proceso. Contar sólo las que '
            'llegaron a la mesa es contar los accidentes y perderse todos los '
            'avisos. Y la nota de la auditoría de esta área en el caso, que es '
            'donde se ve si el protocolo se aplica o sólo está escrito.',
        ],
        'cifras': [
            C('Alérgenos presentes como ingrediente en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B79', 'num'),
            C('Alérgenos por traza en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B80', 'num'),
            C('Alérgenos por utensilio compartido en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B81', 'num'),
            C('Incidencias de alérgenos registradas en el año del caso', f'{X_CUAD}!Semana!AJ57', 'num'),
            C('Gravedad máxima registrada en el año, de cero a tres', f'{X_CUAD}!Semana!AK57', 'num'),
            C('Incidencias de alérgenos por base de cubiertos en el año', f'{X_CUAD}!Semana!AL57', 'num2'),
            C('Objetivo de la casa para las incidencias de alérgenos', f'{X_CUAD}!Parámetros!B32', 'num2'),
            C('Nota de la auditoría en el área de alérgenos en el pase', f'{X_AUD}!Resumen por Área!D10', 'num2'),
            C('Peso del área de alérgenos en el pase sobre el total de la auditoría', f'{X_AUD}!Resumen por Área!C10', 'num'),
            C('Cumplimiento del área de alérgenos en el pase', f'{X_AUD}!Resumen por Área!E10', 'pct1'),
        ],
        'sector': ['CE-01', 'CE-03', 'CE-06', 'CE-07', 'MM-31', 'CE-04'],
        'tablas': [
            {
                'titulo': 'Los alérgenos de proceso de la ficha de ejemplo (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
                'src': (X_FICHA, 'Ficha (ejemplo)'),
                'cols': [('Alérgeno', 'A', 'txt'),
                         ('Estado en esta elaboración', 'B', 'txt'),
                         ('Dónde entra en esta elaboración', 'C', 'txt'),
                         ('Sustitución posible', 'E', 'txt')],
                'filas': (60, 65),
                'nota': V_852 + ' — esta tabla NO sustituye a la declaración de alérgenos de la '
                        'carta, que va plato a plato y vive en el Pack APPCC: dice dónde entra el '
                        'alérgeno dentro de esta elaboración concreta.',
            },
            {
                'titulo': 'Qué quiere decir cada estado de la tabla de alérgenos de proceso (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
                'src': (X_FICHA, 'Ficha (ejemplo)'),
                'cols': [('Estado', 'A', 'txt'), ('Qué quiere decir', 'B', 'txt')],
                'filas': (74, 77),
                'nota': 'La diferencia entre «presente» y «por utensilio compartido» es la que '
                        'decide si el plato se puede adaptar o no se puede servir: por eso son '
                        'estados distintos y no una casilla de sí o no.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 15,
        'titulo': 'Vida Útil, Envasado al Vacío y lo que la Ley no Dice',
        'resumen_indice': 'por qué no existe una cifra legal de días, cuándo obliga el estudio de vida útil, qué pasa con la quinta gama y qué números sí tiene la fritura.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Quitar de la cabeza del lector las tablas de días que '
                    'circulan como si fueran normativa y dejarle en su lugar el '
                    'criterio real: qué obliga, qué es recomendación con su '
                    'nivel de fiabilidad, y cómo se fija la vida útil de una '
                    'elaboración propia sin inventarse un número.',
        'epigrafes': [
            'No existe una cifra legal de días: qué hay en su lugar',
            'Cuándo obliga un estudio de vida útil',
            'Envasado al vacío y quinta gama: lo verificado y lo que sólo es recomendación',
            'Fritura y aceite: lo único que sí tiene número',
            'Acrilamida y contaminantes: nivel de referencia no es límite',
            'Elaboración propia: qué cuenta y dónde puedes venderlo',
        ],
        'puntos': [
            'La tesis, dicha en la primera línea: no existe ninguna norma que '
            'diga cuántos días dura una salsa. Quien publica una tabla de días '
            'presentada como normativa se la está inventando. Lo que sí existe '
            'es la obligación de estudiar la vida útil en un supuesto concreto, '
            'y las reglas del producto congelado.',
            'Cuándo obliga el estudio: cuando el alimento está listo para el '
            'consumo y puede favorecer el crecimiento de Listeria '
            'monocytogenes. El reglamento de criterios microbiológicos alcanza '
            'a toda la cadena, incluida la venta al por menor, y ahí es donde '
            'un restaurante que envasa y conserva se lo encuentra.',
            'Cómo se fija entonces la vida útil de una elaboración propia sin '
            'inventar: se decide por escrito, con criterio y con margen, se '
            'anota en la ficha por elaboración, se comprueba organolépticamente '
            'y se acorta si hay dudas. Enseñar las vidas útiles del ejemplo '
            '—cada elaboración con la suya, no una para todas— y decir '
            'expresamente que son las de este caso modelado, no un estándar.',
            'La quinta gama y el vacío, con la honestidad de la fuente: la '
            'recomendación de mantener por debajo de 4 grados, e idealmente de '
            '3,3, viene de un informe de una agencia autonómica y aquí se marca '
            'como de fiabilidad media, no como norma. Y la regla operativa: el '
            'vacío no es una barrera contra todo, así que si baja la '
            'temperatura o se alarga el plazo, el riesgo cambia.',
            'La fritura, que es el único sitio de este capítulo con un número '
            'legal: el contenido de componentes polares del aceite debe ser '
            'inferior al 25 por ciento. Ese artículo sigue vigente, aunque otros '
            'de la misma orden estén derogados. Y el criterio de cocina: freír '
            'la patata por debajo de 175 grados es buena práctica, no una '
            'obligación con multa.',
            'Acrilamida y contaminantes, con la distinción que evita el susto: '
            'los niveles de referencia de acrilamida disparan la revisión de '
            'las medidas, no son límites sancionables, y el reglamento se '
            'dirige a fabricantes y, con requisitos extra, a franquicias con '
            'suministro centralizado. Los límites de contaminantes sí vinculan, '
            'y lo hacen al comprar: el reglamento que los fija sustituyó al '
            'anterior.',
            'Cerrar con «elaboración propia», que enlaza con el capítulo 13 y '
            'aporta lo nuevo: la mención es voluntaria, no cuenta fraccionar, '
            'envasar, deshuesar carne fresca ni limpiar pescado, y quien la '
            'usa sólo puede vender esos alimentos en el establecimiento que los '
            'elaboró o en sus sucursales. Para un obrador central que abastece '
            'a varias unidades, esa frase decide cómo se rotula la carta.',
        ],
        'cifras': [
            C('Vida útil del puré de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D88', 'num'),
            C('Vida útil de la salsa de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D89', 'num'),
            C('Vida útil del crujiente de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D90', 'num'),
            C('Vida útil de la pieza racionada de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D91', 'num'),
            C('Temperatura mínima de mantenimiento en caliente de la ficha', f'{X_FICHA}!Ficha (ejemplo)!B47', 'num'),
            C('Platos de la carta registrados en el índice de fichas', f'{X_FICHA}!Índice de Fichas!C56', 'num'),
            C('Platos con ficha que toca revisar', f'{X_FICHA}!Índice de Fichas!C54', 'num'),
            C('Minutos totales de la elaboración de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B43', 'num'),
        ],
        'sector': ['CE-08', 'CE-37', 'CE-35', 'CE-19', 'CE-20', 'CE-17',
                   'CE-12', 'CE-13'],
        'tablas': [
            {
                'titulo': 'Conservación y vida útil, elaboración por elaboración (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
                'src': (X_FICHA, 'Ficha (ejemplo)'),
                'cols': [('Elaboración', 'A', 'txt'), ('Conservación', 'B', 'txt'),
                         ('Vida útil (días)', 'D', 'num')],
                'filas': (88, 91),
                'nota': 'Cuatro elaboraciones del mismo plato y cuatro vidas útiles distintas: '
                        'ésa es exactamente la razón por la que no puede existir una tabla '
                        'general de días. Estos valores son los de este caso modelado y viven en '
                        'casillas editables.',
            },
            {
                'titulo': 'Qué fija la ley, qué recomienda y qué no dice',
                'cabecera': ['Asunto', 'Qué hay exactamente', 'Cómo se usa en cocina'],
                'filas': [
                    ['Días que dura una elaboración propia refrigerada', 'No hay cifra legal', 'Se decide por escrito, por elaboración, y se anota en la ficha'],
                    ['Estudio de vida útil', 'Obligatorio cuando el alimento listo para el consumo favorece el crecimiento de Listeria monocytogenes', 'Reglamento (CE) 2073/2005, art. 3 y Anexo II'],
                    ['Etiquetado de lo que congelas tú', 'Tres fechas: elaboración, congelación y caducidad o consumo preferente del congelado', 'Art. 5.3 del RD 1021/2022'],
                    ['Equipo de congelación', 'Debe alcanzar menos 18 °C en el centro con un descenso ininterrumpido', 'Art. 5.4 del RD 1021/2022'],
                    ['Quinta gama por debajo de 4 °C', 'Recomendación de una agencia autonómica, no norma estatal; fiabilidad media declarada', 'Se aplica como criterio propio y se dice que es criterio'],
                    ['Aceite de fritura', 'Componentes polares inferiores al 25 %', 'Art. 6.3 de la Orden de 26 de enero de 1989, vigente'],
                    ['Temperatura de fritura de la patata', 'Buena práctica por debajo de 175 °C; no es un límite sancionable', 'Reglamento (UE) 2017/2158'],
                    ['Niveles de referencia de acrilamida', 'Disparan la revisión de las medidas; no son límites con sanción', 'Reglamento (UE) 2017/2158'],
                    ['Límites de contaminantes', 'Vinculan al poner el producto en el mercado', 'Reglamento (UE) 2023/915, que sustituyó al anterior'],
                ],
                'nota': 'Verificado el 06-09-2026 · Reglamento (CE) 2073/2005, RD 1021/2022 '
                        '(BOE-A-2022-21681), Orden de 26 de enero de 1989 art. 6.3, Reglamento '
                        '(UE) 2017/2158 y Reglamento (UE) 2023/915 · '
                        'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 16,
        'titulo': 'Comidas Testigo y Banquetes (y Qué se Hace con el Excedente, en una Página)',
        'resumen_indice': 'quién está obligado a guardar comida testigo, la doble toma del catering, cómo se produce un evento y qué se hace con lo que sobra.',
        'palabras': 2000, 'bloques': 3,
        'objetivo': 'Poner encima de la mesa la obligación que casi ningún chef '
                    'conoce y que le alcanza en cuanto acepta un encargo '
                    'mediano, y dejar montada la producción de un evento de '
                    'principio a fin. El excedente se resuelve en una página '
                    'porque su bloque completo está en el manual hermano.',
        'epigrafes': [
            'Quién está obligado a guardar comida testigo, y por qué casi nadie lo sabe',
            'La muestra: cien gramos, siete días, cuatro grados y quién la recoge',
            'Elaboración y servicio en sitios distintos: dos testigos, no una',
            'Producir un banquete: del menú a las raciones por partida',
            'El timing del evento y el personal que lo sostiene',
            'El excedente del servicio, en una página',
        ],
        'puntos': [
            'La tesis, que es el hallazgo del research: las comidas testigo no '
            'son cosa de hospitales y colegios. La norma enumera supuestos, y '
            'entre ellos está cualquier encargo, de quien sea, para grupos o '
            'eventos de MÁS DE 40 PERSONAS. Cualquier chef de hotel, de '
            'catering o de banquetes que sirva un evento mediano está obligado, '
            'y casi ninguno lo sabe.',
            'Los parámetros de la muestra, cada uno con su apartado: ración '
            'individual de como mínimo cien gramos, identificada y fechada, '
            'conservada durante un mínimo de siete días en refrigeración a '
            'cuatro grados o menos, o en congelación a menos dieciocho o menos. '
            'Enseñar los del caso, que están en casillas editables porque la '
            'norma puede cambiar.',
            'La doble toma del catering, que no está en ningún producto del '
            'catálogo: cuando la elaboración y el servicio ocurren en '
            'establecimientos distintos, quien elabora recoge la testigo en el '
            'momento más próximo a la salida del establecimiento, y quien la '
            'sirve la recoge en el momento del servicio. Son dos muestras, no '
            'una, y el libro avisa cuando el evento está marcado como de '
            'elaboración y servicio separados.',
            'El evento del caso, con sus cifras: comensales, elaboraciones del '
            'menú, muestras registradas, cuántas faltan por tomar, cuántas '
            'están por debajo del gramaje y cuántas fuera de rango de '
            'temperatura. Y la cuenta atrás: la hoja calcula los días que '
            'faltan hasta poder destruir cada muestra, para que nadie las tire '
            'antes ni las guarde eternamente.',
            'La producción del banquete: del menú a las raciones por comensal, '
            'de ahí a las raciones a producir y de ahí a las unidades de '
            'producción por partida. Enseñar el reparto por partida del evento '
            'del caso y por qué el porcentaje importa: es lo que dice qué '
            'partida necesita refuerzo y cuál puede seguir con el servicio '
            'normal.',
            'El timing y el personal: los hitos con hora, el responsable de cada '
            'uno y las horas totales del evento, con las horas de cocina por '
            'comensal, que es la cifra con la que se dimensiona el siguiente. '
            'Y la regla que evita el desastre: el timing se escribe hacia atrás '
            'desde la hora de servicio, no hacia adelante desde la hora de '
            'entrada.',
            'El excedente, en una página y con la cita: «la jerarquía del '
            'excedente, el doggy bag y de qué está exento tu local están en el '
            'Manual del Manager, cap. 19; aquí sólo se decide qué se puede '
            'donar de una cocina caliente y qué no». Lo que aporta este manual '
            'es la decisión de cocina: qué producto se ha mantenido en '
            'temperatura y está identificado, qué se ha servido ya y no vuelve, '
            'qué se ha recalentado y por tanto se descarta, y qué se puede '
            'entregar en condiciones. Y los tres datos que la tabla añade y el '
            'hermano no tiene: la ley define microempresa como la que ocupa '
            'menos de diez personas y no supera dos millones de euros de '
            'volumen o balance; las obligaciones de su artículo 6 no eran '
            'exigibles hasta un año después de su publicación; y el doggy bag '
            'del artículo 8 obliga igualmente, y de hecho ya obligaba desde el '
            '22 de diciembre de 2022 por otra norma.',
        ],
        'cifras': [
            C('Comensales a partir de los que obliga la comida testigo', f'{X_BANQ}!Registro de Comidas Testigo!D7', 'num'),
            C('Gramos mínimos por elaboración guardada', f'{X_BANQ}!Registro de Comidas Testigo!D8', 'num'),
            C('Días mínimos de conservación de la muestra', f'{X_BANQ}!Registro de Comidas Testigo!D9', 'num'),
            C('Temperatura máxima en refrigeración de la muestra', f'{X_BANQ}!Registro de Comidas Testigo!D10', 'num'),
            C('Temperatura máxima en congelación de la muestra', f'{X_BANQ}!Registro de Comidas Testigo!D11', 'num'),
            C('Comensales del evento del caso', f'{X_BANQ}!Registro de Comidas Testigo!D22', 'num'),
            C('Elaboraciones del menú del evento', f'{X_BANQ}!Registro de Comidas Testigo!D55', 'num'),
            C('Muestras testigo registradas del evento', f'{X_BANQ}!Registro de Comidas Testigo!D54', 'num'),
            C('Raciones a producir en total para el evento', f'{X_BANQ}!Producción y Ficha de Banquete!F25', 'num'),
            C('Horas totales de personal del evento', f'{X_BANQ}!Producción y Ficha de Banquete!D64', 'num'),
        ],
        'sector': ['CE-11', 'CE-31', 'CE-32', 'CE-33', 'CE-34', 'CE-15', 'MM-36'],
        'tablas': [
            {
                'titulo': 'Los parámetros legales de la comida testigo (banquetes-comidas-testigo.xlsx, hoja «Registro de Comidas Testigo»)',
                'src': (X_BANQ, 'Registro de Comidas Testigo'),
                'cols': [('Parámetro', 'A', 'txt'), ('Valor', 'D', 'num')],
                'filas': (7, 11),
                'nota': V_TESTIGO + ' — los cinco valores viven en casillas editables porque son '
                        'los que cambian si cambia la norma; el libro enciende la alerta de '
                        'obligación con el primero de ellos.',
            },
            {
                'titulo': 'Los supuestos que disparan la obligación, y cuál te aplica (banquetes-comidas-testigo.xlsx, hoja «Registro de Comidas Testigo»)',
                'src': (X_BANQ, 'Registro de Comidas Testigo'),
                'cols': [('Supuesto', 'A', 'txt'), ('¿Te aplica?', 'D', 'txt')],
                'filas': (30, 34),
                'nota': V_TESTIGO + ' — el último supuesto es el que alcanza a un restaurante '
                        'normal: no hace falta ser un comedor colectivo para estar obligado, '
                        'basta con aceptar un encargo por encima del umbral.',
            },
            {
                'titulo': 'El excedente del servicio: qué se hace con él, en una página',
                'cabecera': ['Qué tienes delante', 'Qué se puede hacer', 'Qué lo decide'],
                'filas': [
                    ['Producto elaborado que no ha salido de cocina y ha estado en temperatura', 'Es donable o reutilizable si está identificado y en fecha', 'La temperatura mantenida y la trazabilidad, no la buena voluntad'],
                    ['Producto que se ha servido en mesa o en bufé', 'No vuelve a cocina ni se dona', 'Ha salido del control del establecimiento'],
                    ['Producto ya recalentado que no se ha consumido', 'Se descarta: no se recalienta otra vez ni se almacena', 'Art. 30.7 del RD 1086/2020'],
                    ['Lo que el cliente no ha consumido de su plato', 'Se le facilita que se lo lleve, sin coste adicional, salvo bufé libre o similares', 'Art. 18.5 del RD 1021/2022, desde el 22 de diciembre de 2022, y art. 8 de la Ley 1/2025'],
                    ['El envase de plástico de un solo uso para llevárselo', 'Se puede cobrar aparte', 'Título V de la Ley 7/2022'],
                    ['El excedente que no puede consumir una persona', 'Alimentación animal, subproductos industriales, reciclado o valorización energética, por ese orden', 'Art. 5.1 de la Ley 1/2025'],
                    ['El plan de prevención y el convenio de donación', 'No obligan a microempresas ni, en un apartado, a locales de 1.300 m² o menos', 'Art. 6.4.c y 6.6 de la Ley 1/2025; microempresa es la que ocupa menos de diez personas y no supera dos millones de euros'],
                ],
                'nota': V_DESP + ' — la jerarquía completa, la exención y el doggy bag están '
                        'explicados en el Manual del Manager, cap. 19; esta página sólo resuelve '
                        'la decisión de cocina. Y ojo: las microempresas quedan fuera del art. 6, '
                        'no de la ley: el art. 8 les sigue obligando.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 17,
        'titulo': 'Prevención de Riesgos en la Cocina: lo que la Evaluación de Riesgos Convierte en Obligación',
        'resumen_indice': 'temperatura y ventilación por categoría de trabajo, suelos, resguardos y comprobaciones, el uniforme, el mito de los veinticinco kilos y la siniestralidad real.',
        'palabras': 2000, 'bloques': 3,
        'objetivo': 'Dar al chef la parte de la prevención que se ve en su '
                    'cocina y que puede comprobar hoy mismo, con la norma '
                    'exacta de cada cosa y sin convertir en obligación legal lo '
                    'que no lo es. Es el capítulo que más mitos desmonta.',
        'epigrafes': [
            'La evaluación de riesgos es la que convierte una lista en obligación',
            'Temperatura y ventilación del local: qué dice la norma por categoría de trabajo',
            'Suelos, resguardos y comprobaciones documentadas de los equipos',
            'El uniforme no es una ley: son dos marcos que se suman',
            'El mito de los veinticinco kilos',
            'Lo que dicen los números de siniestralidad, y lo que no dicen',
        ],
        'puntos': [
            'La tesis que ordena el capítulo entero: casi nada de lo que se '
            'vende como «obligatorio en cocina» lo es por sí solo. La norma de '
            'equipos de protección trae una lista NO EXHAUSTIVA de actividades '
            'que PUEDEN requerir equipo, y su propia nota dice que la '
            'evaluación de riesgos determinará la necesidad. Lo que convierte '
            'esa lista en obligación es tu evaluación, no la lista. Decirlo así '
            'no relaja el control: te dice dónde mirar.',
            'Lo que sí es incondicional, y conviene saberlo: el empresario debe '
            'proporcionar GRATUITAMENTE los equipos de protección individual y '
            'reponerlos cuando resulte necesario. Y sólo se recurre al equipo '
            'individual cuando el riesgo no se puede evitar o limitar por '
            'protección colectiva o por organización del trabajo: primero se '
            'cambia el proceso, después se protege a la persona.',
            'Las dos actividades de la lista que una cocina activa casi por '
            'definición: la utilización regular de cuchillos de mano, que puede '
            'requerir guante de protección mecánica y delantal, polainas o '
            'pantalones resistentes a los cortes; y los trabajos en ambientes '
            'húmedos y en superficies resbaladizas, que pueden requerir calzado '
            'antideslizante. Y el dato honesto: entre los sectores que la lista '
            'enumera están la industria alimentaria, los mataderos y la '
            'limpieza; la hostelería no aparece por su nombre.',
            'Temperatura del local, escrita como está en la norma y no como se '
            'repite: de 17 a 27 grados en trabajos sedentarios propios de '
            'oficinas o similares, y de 14 a 25 en trabajos ligeros. NO HAY '
            'rango para el trabajo pesado. La categoría de tu cocina la fija tu '
            'evaluación de riesgos, y el propio anexo dice que hay que tener en '
            'cuenta las limitaciones y condicionantes del lugar de trabajo, de '
            'los procesos que se desarrollan en él y del clima de la zona. Por '
            'eso «la temperatura legal de la cocina es de 14 a 25 grados» es '
            'una frase falsa que repite todo el sector.',
            'Ventilación, con la corrección que casi nadie hace: son 30 metros '
            'cúbicos por hora y trabajador en trabajos sedentarios en ambientes '
            'no calurosos y no contaminados por humo de tabaco, y 50 EN LOS '
            'CASOS RESTANTES. Una cocina es siempre «los casos restantes», así '
            'que los 50 no dependen de que haga calor: dependen de que no sea '
            'una oficina.',
            'Suelos, resguardos y comprobaciones, que es la parte que se '
            'comprueba andando por la cocina: los suelos deben ser fijos, '
            'estables y no resbaladizos, sin irregularidades ni pendientes '
            'peligrosas; los elementos móviles con riesgo de contacto mecánico '
            '—cortadora, picadora, batidora— deben llevar resguardos o '
            'dispositivos que impidan el acceso; y las comprobaciones de los '
            'equipos las hace personal competente, se documentan y se conservan '
            'durante toda la vida útil del equipo. Añadir los dos supuestos que '
            'nadie recuerda: hay comprobación inicial tras la instalación y '
            'tras cada montaje en un emplazamiento nuevo, y comprobación '
            'adicional tras transformaciones, accidentes, fenómenos naturales o '
            'falta prolongada de uso, que es el caso literal de una cocina de '
            'temporada que reabre.',
            'El uniforme, que no tiene ley propia sino dos marcos que se suman: '
            'por higiene alimentaria, toda persona en zona de manipulación debe '
            'llevar vestimenta adecuada, limpia y, en su caso, protectora; por '
            'prevención, lo que la evaluación determine como equipo de '
            'protección va gratis y se repone. Y por convenio, según la '
            'provincia, la empresa facilita la ropa a su cargo y en algunos '
            'territorios paga también su lavado. Tres marcos distintos para la '
            'misma chaquetilla.',
            'El mito de los veinticinco kilos, desmontado con la propia norma: '
            'el real decreto de manipulación manual de cargas NO contiene '
            'ninguna cifra en kilos ni en su articulado ni en su anexo, que '
            'enumera factores cualitativos —peso, tamaño, agarre, distancia, '
            'suelo, temperatura, esfuerzo—. Es más: esa norma derogó las '
            'disposiciones antiguas que sí prohibían levantar más de un peso '
            'determinado, y su disposición final remite los valores máximos de '
            'carga COMO REFERENCIA a una guía técnica. Es decir, la propia '
            'norma dice que la cifra vive fuera de ella y es orientativa.',
            'Cerrar con la siniestralidad, con su etiqueta exacta y sin '
            'mezclar: son dos fuentes, dos años y dos ámbitos distintos, y hay '
            'que decirlo. La lectura para el chef no es alarmista: en '
            'hostelería hay muchos accidentes y pocos mortales, y los que hay '
            'se concentran en cortes, caídas y sobreesfuerzos, que son '
            'exactamente los tres que se corrigen con cuchillo afilado, suelo '
            'seco señalizado y carro.',
        ],
        'cifras': [
            C('Puntos de control de la auditoría interna de cocina', f'{X_AUD}!Resumen por Área!B12', 'num'),
            C('Peso total de los cincuenta puntos de la auditoría', f'{X_AUD}!Resumen por Área!C12', 'num'),
            C('Nota ponderada global de la visita del caso', f'{X_AUD}!Resumen por Área!D12', 'num2'),
            C('Cumplimiento global sobre la escala', f'{X_AUD}!Resumen por Área!E12', 'pct1'),
            C('Puntos de control del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!B9', 'num'),
            C('Peso del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!C9', 'num'),
            C('Nota de la visita en el área de prevención de riesgos', f'{X_AUD}!Resumen por Área!D9', 'num2'),
            C('Cumplimiento del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!E9', 'pct1'),
            C('Escala máxima de puntuación de la auditoría', f'{X_AUD}!Auditoría!D10', 'num'),
            C('Umbral de aviso ámbar de la auditoría', f'{X_AUD}!Auditoría!D11', 'num'),
        ],
        'sector': ['CE-05', 'CE-21', 'CE-22', 'CE-23', 'CE-24', 'CE-25',
                   'CE-26', 'CE-27', 'CE-28', 'CE-30', 'CS-01'],
        'tablas': [
            {
                'titulo': 'Los diez puntos de prevención de riesgos de la auditoría, con su norma (auditoria-interna-cocina.xlsx, hoja «Auditoría»)',
                'src': (X_AUD, 'Auditoría'),
                'cols': [('Nº', 'A', 'num'), ('Punto de control', 'C', 'txt'),
                         ('Peso (1 a 3)', 'D', 'num'),
                         ('Norma aplicable', 'G', 'txt')],
                'filas': (49, 58),
                'nota': V_PRL + ' — los puntos sin norma en la última columna son criterio de la '
                        'casa, y eso también hay que saberlo: no todo lo que se audita es una '
                        'obligación legal.',
            },
            {
                'titulo': 'Qué obliga, qué lo convierte en obligación y qué es buena práctica',
                'cabecera': ['Asunto', 'Qué dice exactamente la norma', 'Qué hace que te obligue'],
                'filas': [
                    ['Equipos de protección individual', 'El anexo es una lista NO exhaustiva de actividades que PUEDEN requerir equipo', 'Tu evaluación de riesgos, que determina la necesidad y las características'],
                    ['Gratuidad y reposición del equipo', 'Se proporcionan gratuitamente y se reponen cuando resulte necesario', 'Es incondicional: no depende de la evaluación'],
                    ['Orden de las medidas', 'Sólo se recurre al equipo individual cuando el riesgo no se ha podido evitar o limitar por protección colectiva u organización del trabajo', 'Primero se cambia el proceso; después se protege a la persona'],
                    ['Temperatura del local', 'De 17 a 27 °C en trabajos sedentarios de oficina o similares; de 14 a 25 °C en trabajos ligeros; sin rango para el pesado', 'La categoría de trabajo la fija tu evaluación, y el anexo admite condicionantes del local y del proceso'],
                    ['Renovación de aire', '30 m³ por hora y trabajador en sedentario no caluroso y sin humo de tabaco; 50 en los casos restantes', 'Una cocina es siempre «los casos restantes»'],
                    ['Suelos', 'Fijos, estables y no resbaladizos, sin irregularidades ni pendientes peligrosas', 'Obliga siempre'],
                    ['Resguardos en equipos con elementos móviles', 'Resguardos o dispositivos que impidan el acceso a las zonas peligrosas', 'Obliga siempre que haya riesgo de contacto mecánico'],
                    ['Comprobación de equipos', 'La hace personal competente; se documenta y se conserva toda la vida útil del equipo', 'Inicial, tras montaje en nuevo emplazamiento, y tras transformación, accidente o falta prolongada de uso'],
                    ['Peso máximo de una carga', 'La norma no contiene ninguna cifra en kilos: enumera factores cualitativos y remite los valores máximos como referencia a una guía técnica', 'La evaluación del puesto, no una cifra de curso'],
                    ['Vestimenta en zona de manipulación', 'Adecuada, limpia y, en su caso, protectora', 'Obliga siempre, por higiene alimentaria'],
                    ['Formación en prevención', 'Suficiente y adecuada al puesto, dentro de la jornada, y su coste no recae en ningún caso sobre la persona trabajadora', 'Obliga siempre'],
                ],
                'nota': V_PRL,
            },
        ],
        'prohibido': None,
    },
    {
        'n': 18,
        'titulo': 'Formar y Evaluar a la Brigada: Cobertura no es Competencia',
        'resumen_indice': 'las siete competencias técnicas y sus pesos por puesto, la prueba práctica, el plan de desarrollo y la formación de manipuladores sin carné.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Separar dos preguntas que el sector trata como una sola —si '
                    'alguien puede cubrir la partida y si lo hace bien— y dar '
                    'la herramienta que contesta la segunda: una rúbrica de '
                    'competencias técnicas con prueba práctica puntuada.',
        'epigrafes': [
            'Cobertura y competencia: dos preguntas distintas y dos herramientas distintas',
            'Las siete competencias técnicas y por qué pesan distinto en cada puesto',
            'La prueba práctica: qué es un cinco y qué es un uno',
            'El plan de desarrollo individual y la próxima partida a aprender',
            'Formación de manipuladores: por puesto, del titular y sin carné',
        ],
        'puntos': [
            'La tesis del capítulo, en dos preguntas: «¿puede sostener la '
            'partida en un servicio lleno?» es COBERTURA, y se responde con la '
            'matriz de polivalencia del Manual del Manager, sin prueba. '
            '«¿lo hace bien?» es COMPETENCIA, y se responde midiendo cortes, '
            'cocciones, fondos, emplatado, higiene, aplicación de la ficha y '
            'gestión de su merma. Creer que quien cubre sabe es lo que produce '
            'el plato distinto según el turno.',
            'Frontera explícita, con esta frase: «la cobertura de la partida y '
            'el plan de cross-training se llevan con la matriz de polivalencia '
            'del Manual del Manager, cap. 13; esto mide otra cosa». Y la otra '
            'frontera: la evaluación de desempeño genérica —puntualidad, trato, '
            'trabajo en equipo— está en el Kit de Gestión de Personal. Aquí se '
            'evalúa el OFICIO.',
            'Las siete competencias y el peso por puesto, que es lo que hace la '
            'rúbrica justa: un ayudante y un jefe de partida no se miden con la '
            'misma vara aunque se les evalúe en lo mismo. Explicar cómo se lee '
            'la media ponderada frente a la simple y por qué la ponderada es la '
            'que refleja lo que de verdad importa en ese puesto.',
            'La prueba práctica: siete pruebas con sus minutos, su material y, '
            'lo más importante, la descripción escrita de qué es un cinco y qué '
            'es un uno en cada una. Sin esas dos descripciones la puntuación es '
            'una opinión. Dar la duración total de la prueba del caso y la '
            'regla de uso: se hace en una mañana, con producto real y con la '
            'ficha delante.',
            'La lectura cruzada, que es donde está el valor: comparar el nivel '
            'técnico con el nivel de cobertura de la misma persona. Quien cubre '
            'una partida con nivel técnico bajo es un riesgo; quien tiene nivel '
            'técnico alto y no cubre ninguna es formación desaprovechada. La '
            'columna de lectura del libro dice cuál es cada caso.',
            'El plan de desarrollo individual: persona, objetivo, competencias a '
            'trabajar, acciones, responsable y fecha, con una columna que dice '
            'cuál es la próxima partida a aprender —que es la que enlaza con el '
            'plan de cross-training del hermano y no lo repite—. Dar cuántos '
            'planes hay abiertos en el caso y en qué estado.',
            'Cerrar con la formación obligatoria y el mito: el carné oficial de '
            'manipulador de alimentos NO existe desde 2010. La obligación es '
            'del titular de la empresa, la formación va de acuerdo con la '
            'actividad laboral de cada puesto y puede impartirla la propia '
            'empresa. Quien venda un «carné oficial homologado» está vendiendo '
            'algo que no existe. Y la formación en prevención va dentro de '
            'jornada y su coste no recae nunca sobre la persona trabajadora. '
            'Añadir el dato del sector sobre inversión en formación con su '
            'etiqueta exacta y usarlo como argumento de presupuesto, no como '
            'queja.',
        ],
        'cifras': [
            C('Personas evaluadas en la rúbrica de competencias', f'{X_BRIG}!Rúbrica de Competencias!M46', 'num'),
            C('Media ponderada de la brigada evaluada', f'{X_BRIG}!Rúbrica de Competencias!M47', 'num2'),
            C('Media ponderada de la primera persona evaluada', f'{X_BRIG}!Rúbrica de Competencias!M34', 'num2'),
            C('Nivel técnico de esa misma persona', f'{X_BRIG}!Rúbrica de Competencias!N34', 'num'),
            C('Lectura cruzada de cobertura y competencia de esa persona', f'{X_BRIG}!Rúbrica de Competencias!P34', 'txt'),
            C('Duración total de la prueba práctica, en minutos', f'{X_BRIG}!Prueba Práctica!C18', 'num'),
            C('Planes de desarrollo individual planificados', f'{X_BRIG}!Plan de Desarrollo Individual!C25', 'num'),
            C('Planes de desarrollo individual en curso', f'{X_BRIG}!Plan de Desarrollo Individual!C26', 'num'),
            C('Evaluaciones registradas en el histórico', f'{X_BRIG}!Histórico!E26', 'num'),
            C('Media ponderada de la última ronda de evaluación', f'{X_BRIG}!Histórico!E27', 'num2'),
        ],
        'sector': ['MM-43', 'MM-30', 'CE-04', 'CE-27'],
        'tablas': [
            {
                'titulo': 'Las siete competencias técnicas y qué significa cada nivel (brigada-puestos-y-evaluacion.xlsx, hoja «Rúbrica de Competencias»)',
                'src': (X_BRIG, 'Rúbrica de Competencias'),
                'cols': [('Competencia', 'A', 'txt'), ('Nivel 1', 'B', 'txt'),
                         ('Nivel 3', 'D', 'txt'), ('Nivel 5', 'F', 'txt')],
                'filas': (6, 12),
                'nota': 'Se muestran los niveles 1, 3 y 5 para que quepan; en el libro están los '
                        'cinco. Lo que hace utilizable una rúbrica es que el nivel esté descrito '
                        'con lo que se ve, no con adjetivos.',
            },
            {
                'titulo': 'El peso de cada competencia según el puesto (brigada-puestos-y-evaluacion.xlsx, hoja «Rúbrica de Competencias»)',
                'src': (X_BRIG, 'Rúbrica de Competencias'),
                'cols': [('Puesto', 'A', 'txt'), ('Cortes y manejo de cuchillo', 'B', 'num'),
                         ('Cocciones y puntos', 'C', 'num'),
                         ('Fondos, salsas y bases', 'D', 'num'),
                         ('Emplatado y montaje', 'E', 'num'),
                         ('Higiene y APPCC en el puesto', 'F', 'num'),
                         ('Aplicación de la ficha técnica', 'G', 'num'),
                         ('Gestión de la merma de su partida', 'H', 'num')],
                'filas': (16, 22),
                'nota': 'Los pesos son los de esta cocina modelada y son editables: si en la tuya '
                        'la partida que más pesa es la de postres, los pesos de esa fila cambian.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 19,
        'titulo': 'Cocina, Sala y Dirección: Quién Decide Qué, y Cómo Llevar la Cifra al Gerente',
        'resumen_indice': 'la matriz de las quince decisiones que cruzan, por qué sólo puede haber un responsable, y qué cifra de cocina sostiene cada propuesta.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Cerrar por escrito quién decide cada una de las cosas que '
                    'cruzan de cocina a sala y a dirección, y darle al chef que '
                    'no manda en el dinero lo único que sí controla: con qué '
                    'cifra entra en el despacho.',
        'epigrafes': [
            'Las quince decisiones que cruzan de cocina a sala y a dirección',
            'Qué quiere decir cada letra, y por qué sólo puede haber un responsable',
            'El 86, la ficha nueva, la compra fuera de escandallo y la incidencia de alérgeno',
            'La cifra de cocina que el gerente no tiene, y cómo se le lleva',
            'Lo que no se decide en cocina',
        ],
        'puntos': [
            'La tesis: la mitad de los conflictos entre cocina y sala no son de '
            'personas, son de decisiones sin dueño. Cuando cuatro personas '
            'creen que una decisión es suya, o nadie la toma o la toman dos '
            'veces en sentidos distintos. Una matriz de responsabilidades no es '
            'burocracia: es lo que permite discutir el criterio en vez de '
            'discutir de quién era.',
            'Cómo se lee la matriz, con la regla que la hace funcionar: puede '
            'haber varias personas que hagan el trabajo, pero sólo UNA que '
            'responda del resultado de cada decisión. Si hay dos, no hay '
            'ninguna. Y la diferencia entre consultar —antes de decidir— e '
            'informar —después—, que es la que evita la mitad de los enfados '
            'de sala.',
            'Recorrer las decisiones que más queman, una a una: autorizar un 86 '
            'en mitad del servicio, aprobar una ficha técnica nueva antes de '
            'que el plato suba a carta, fijar el precio de venta, aceptar un '
            'encargo de grupo por encima del umbral que dispara la comida '
            'testigo, gestionar una incidencia de alérgeno, comprar fuera de '
            'escandallo un producto de temporada, cambiar de proveedor en una '
            'familia, parar el pase por una avería de frío, autorizar horas '
            'extraordinarias un fin de semana y decidir el destino del '
            'excedente. En cada una, quién responde y a quién hay que avisar.',
            'La propuesta al gerente, con la frontera dicha: «el guion de la '
            'propuesta, en cuatro movimientos, está en el Manual del Manager, '
            'cap. 7». Lo que aporta este capítulo es la munición: qué cifra de '
            'COCINA sostiene cada petición, porque el gerente no la tiene en su '
            'cuadro de mando. Si pides una segunda persona en fríos, la cifra '
            'es la merma de esa partida y las horas de cocina por cubierto; si '
            'pides cambiar un proveedor, es la merma y los retrabajos; si pides '
            'un abatidor, son las temperaturas del muestreo del pase; si pides '
            'formación, es el cumplimiento de ficha y las incidencias de '
            'alérgenos. Una petición con la cifra de la semana se discute; una '
            'petición con una impresión se archiva.',
            'La regla de la sola propuesta: se lleva UNA cada vez, con la cifra '
            'que ha cambiado, qué la explica, qué se propone y qué te '
            'comprometes a medir dentro de un plazo concreto. Y se vuelve a la '
            'reunión siguiente con el resultado, se haya conseguido o no.',
            'Cerrar con lo que NO se decide en cocina, y con la cita: «el '
            'conflicto entre cocina y sala está diagnosticado en el Manual del '
            'Manager, cap. 16, y la conclusión es que casi nunca es de '
            'caracteres: es de protocolo de comunicación». Aquí se dan los '
            'protocolos concretos de los tres cruces que más fallan —cómo llega '
            'una alergia a cocina, cómo se canta una comanda modificada y cómo '
            'se comunica un 86— y no se repite el diagnóstico.',
        ],
        'cifras': [
            C('Cubiertos servidos en el año del caso', f'{X_CUAD}!Semana!D57', 'num'),
            C('Merma global de la cocina en el año', f'{X_CUAD}!Semana!AF57', 'pct1'),
            C('Merma del año de la partida de fríos y entrantes', f'{X_CUAD}!Semana!X57', 'pct1'),
            C('Tiempo medio de pase de principales en el año', f'{X_CUAD}!Semana!AH57', 'num1'),
            C('Horas de cocina por cubierto en el año', f'{X_CUAD}!Semana!AN57', 'num2'),
            C('Incidencias de alérgenos por base de cubiertos en el año', f'{X_CUAD}!Semana!AL57', 'num2'),
            C('Devueltos y retrabajados por base de cubiertos en el año', f'{X_CUAD}!Semana!AQ57', 'num1'),
            C('Comprobación de la fila del 86 en la matriz de decisiones', f'{X_BRIG}!Matriz RACI!J13', 'txt'),
            C('Comprobación de la fila de la incidencia de alérgeno', f'{X_BRIG}!Matriz RACI!J17', 'txt'),
        ],
        'sector': ['MM-14'],
        'tablas': [
            {
                'titulo': 'Qué quiere decir cada letra de la matriz (brigada-puestos-y-evaluacion.xlsx, hoja «Matriz RACI»)',
                'src': (X_BRIG, 'Matriz RACI'),
                'cols': [('Letra', 'A', 'txt'), ('Qué quiere decir', 'B', 'txt')],
                'filas': (6, 9),
                'nota': 'La segunda fila es la que hace el trabajo: si dos personas responden del '
                        'resultado de la misma decisión, en la práctica no responde ninguna.',
            },
            {
                'titulo': 'Las quince decisiones que cruzan entre cocina, sala y dirección (brigada-puestos-y-evaluacion.xlsx, hoja «Matriz RACI»)',
                'src': (X_BRIG, 'Matriz RACI'),
                'cols': [('Decisión', 'A', 'txt'), ('Chef ejecutivo', 'B', 'txt'),
                         ('Segundo de cocina', 'C', 'txt'),
                         ('Jefe de partida', 'D', 'txt'),
                         ('Jefe de sala', 'E', 'txt'),
                         ('Gerencia', 'F', 'txt'), ('Propiedad', 'G', 'txt')],
                'filas': (13, 27),
                'nota': 'Esta matriz es la de la cocina modelada: se imprime, se discute una vez '
                        'con sala y con dirección, se corrige lo que haga falta y se firma. Media '
                        'hora de discusión aquí ahorra un año de discusiones en el pase.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 20,
        'titulo': 'Varias Cocinas a la Vez — y los Noventa Días Siguientes',
        'resumen_indice': 'los mismos indicadores en todas las unidades, la misma auditoría cocina por cocina, la formación en cascada y qué se mide el primer día.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Dar al chef que dirige más de una cocina las dos '
                    'herramientas que le faltan —comparar indicadores y '
                    'comparar auditorías entre unidades— y cerrar el manual con '
                    'lo único que lo convierte en trabajo: qué se anota el '
                    'primer día para poder comparar a los noventa.',
        'epigrafes': [
            'Una cocina, con las herramientas para comparar varias',
            'Los mismos indicadores en todas las unidades: la comparativa del mes cerrado',
            'La misma auditoría, cocina por cocina',
            'Formación en cascada: tú formas a los jefes de cocina, no a los cocineros',
            'Dos comunidades, dos convenios: lo que no se puede estandarizar',
            'Qué se mide el primer día y qué a los noventa',
        ],
        'puntos': [
            'El posicionamiento, en una línea y sin humo: este pack está hecho '
            'para una cocina, y trae las herramientas para comparar varias. Si '
            'diriges cuatro cocinas no necesitas cuatro packs: necesitas los '
            'mismos indicadores medidos igual en las cuatro y dos hojas donde '
            'ponerlos al lado.',
            'La comparativa entre unidades: los mismos indicadores de cocina, un '
            'mes cerrado, el estándar del grupo en una fila y la desviación y '
            'el ranking calculados. Enseñar el caso: tres unidades, cuántos '
            'indicadores dentro del estándar tiene cada una y qué posición '
            'ocupa. Y la lectura que importa: la unidad que factura más '
            'cubiertos no es la que mejor va, y el ranking sirve para preguntar, '
            'no para señalar.',
            'La misma auditoría, cocina por cocina: las mismas cinco áreas, los '
            'mismos cincuenta puntos y la misma escala en cada unidad, con la '
            'desviación contra la media del grupo y contra el estándar que tú '
            'fijes. En el caso sólo está puntuada la unidad de referencia y las '
            'otras dos filas están en blanco a propósito: son las tuyas.',
            'La formación en cascada, que es lo que hace escalable el trabajo: '
            'el chef corporativo forma a los jefes de cocina y comprueba con la '
            'rúbrica; los jefes de cocina forman a sus brigadas. Intentar '
            'formar a todos los cocineros de todas las unidades es la forma más '
            'rápida de no formar a ninguno.',
            'Lo que NO se puede estandarizar entre unidades y hay que decirlo: '
            'si el grupo tiene centros en dos comunidades, hay dos convenios '
            'provinciales distintos, con tablas, complementos y jornada '
            'distintos, y las clases de establecimiento no son homologables. Y '
            'si hay obrador central, la mención de elaboración propia limita '
            'dónde se puede vender lo elaborado: sólo en el establecimiento '
            'elaborador o en sus sucursales.',
            'Frontera, con esta frase: «el plan de 90 días con veinte '
            'decisiones, responsable y semana se monta con el libro de '
            'reuniones y plan del Manual del Manager, cap. 20». Aquí no se '
            'repite: lo que se da es qué medir en cocina para poder comparar.',
            'El cierre del manual: las tres cifras que se anotan el primer día '
            'y se vuelven a mirar a los noventa —la merma de la partida peor, '
            'el cumplimiento de ficha en el pase y las horas de cocina por '
            'cubierto—, por qué esas tres y no otras, y la advertencia honesta '
            'de siempre: la ley cambia, y por eso cada afirmación de este libro '
            'lleva su norma y su fecha de corte, y cada parámetro de las '
            'herramientas vive en una casilla editable. Lo que envejece es el '
            'documento; el método y la herramienta, no.',
        ],
        'cifras': [
            C('Estándar del grupo para la merma global', f'{X_CUAD}!Comparativa entre Unidades!C12', 'pct1'),
            C('Merma global del mes de la unidad de referencia', f'{X_CUAD}!Comparativa entre Unidades!C17', 'pct1'),
            C('Merma global del mes de la segunda unidad', f'{X_CUAD}!Comparativa entre Unidades!C18', 'pct1'),
            C('Merma global del mes de la tercera unidad', f'{X_CUAD}!Comparativa entre Unidades!C19', 'pct1'),
            C('Cubiertos del mes de la tercera unidad', f'{X_CUAD}!Comparativa entre Unidades!B19', 'num'),
            C('Indicadores dentro del estándar de la unidad de referencia', f'{X_CUAD}!Comparativa entre Unidades!N17', 'num'),
            C('Indicadores dentro del estándar de la segunda unidad', f'{X_CUAD}!Comparativa entre Unidades!N18', 'num'),
            C('Posición de la unidad de referencia en el ranking', f'{X_CUAD}!Comparativa entre Unidades!O17', 'num'),
            C('Nota ponderada de auditoría de la unidad de referencia', f'{X_AUD}!Histórico por Unidad!H6', 'num2'),
            C('Estándar de grupo fijado para la auditoría', f'{X_AUD}!Histórico por Unidad!C14', 'num2'),
        ],
        'sector': ['MM-15', 'CE-12'],
        'tablas': [
            {
                'titulo': 'Los mismos indicadores en tres cocinas, en el mes cerrado (cuadro-de-mando-cocina.xlsx, hoja «Comparativa entre Unidades»)',
                'src': (X_CUAD, 'Comparativa entre Unidades'),
                'cols': [('Unidad', 'A', 'txt'), ('Cubiertos del mes', 'B', 'num'),
                         ('Merma global (%)', 'C', 'pct1'),
                         ('Pase de principales (min)', 'D', 'num1'),
                         ('Incidencias de alérgenos por base', 'E', 'num2'),
                         ('Horas de cocina por cubierto', 'F', 'num2'),
                         ('Indicadores dentro del estándar', 'N', 'num'),
                         ('Posición', 'O', 'num')],
                'filas': (17, 19),
                'nota': 'La unidad con más cubiertos no es la que mejor va: por eso se comparan '
                        'indicadores y no volumen. El estándar del grupo es una fila editable de '
                        'la misma hoja, no una cifra de fuera.',
            },
            {
                'titulo': 'La misma auditoría, cocina por cocina (auditoria-interna-cocina.xlsx, hoja «Histórico por Unidad»)',
                'src': (X_AUD, 'Histórico por Unidad'),
                'cols': [('Unidad o cocina', 'A', 'txt'),
                         ('Orden y mise en place', 'C', 'num2'),
                         ('Aplicación de fichas', 'D', 'num2'),
                         ('Mermas por partida', 'E', 'num2'),
                         ('Prevención de riesgos', 'F', 'num2'),
                         ('Alérgenos en el pase', 'G', 'num2'),
                         ('Nota ponderada', 'H', 'num2'), ('Lectura', 'L', 'txt')],
                'filas': (6, 8),
                'saltar_vacias': False,
                'nota': 'Las dos filas en blanco son las otras dos cocinas del grupo, y están '
                        'vacías a propósito: se rellenan con la misma auditoría, los mismos '
                        'cincuenta puntos y la misma escala. Lo que hace comparable una auditoría '
                        'no es la nota, es la vara.',
            },
        ],
        'prohibido': None,
    },
]


# --------------------------------------------------------------------------
# Prohibiciones ESPECÍFICAS por capítulo (1-3 cada uno). Se suman al NO_COMUN
# más abajo: `prohibido` = NO_COMUN + éstas. Varias salen directamente de la
# tabla de frontera (D11).
# --------------------------------------------------------------------------
ESPECIFICAS = {
    1: [
        'NO presentes este manual como sustituto de los otros productos del '
        'catálogo ni digas que hacen falta para usarlo: son complementarios y '
        'hay que decirlo así, con su nombre y con lo que aporta cada uno.',
        'NO repitas la taxonomía completa del convenio para todo el '
        'restaurante: aquí sólo entra el área funcional de cocina. Las seis '
        'áreas funcionales del negocio entero están en el Manual del Manager, '
        'cap. 1.',
        'Éste es el ÚNICO capítulo donde se escribe «partida (estación)». En '
        'los otros diecinueve se escribe «partida» a secas.',
    ],
    2: [
        'NO dibujes una brigada clásica de quince puestos con nombres '
        'franceses como si fuera el estándar del oficio: lo que se cita es el '
        'convenio, y hay que decir expresamente cuándo el modelo clásico no '
        'aplica.',
        'NO inventes una lista homogénea de nombres de puesto: la modificación '
        'de 2026 sólo renombró cinco de los diez, y hasta el propio boletín es '
        'incoherente entre artículos. Se reproduce la mezcla tal cual o se '
        'citan sólo los nombres del artículo de funciones.',
        'NO digas que el convenio tipifica al chef ejecutivo ni al chef '
        'corporativo: no aparecen. Son denominaciones de uso.',
    ],
    3: [
        'NO expliques la arquitectura del convenio —acuerdo estatal frente a '
        'convenio provincial, materias reservadas, cómo se busca en el registro '
        'de convenios, ultraactividad—: eso es el cap. 8 del Manual del '
        'Manager y aquí se cita en una frase.',
        'NO des ninguna cifra salarial que no esté en la tabla de este '
        'capítulo, y cuando la des, va SIEMPRE con la etiqueta de su tabla y de '
        'su boletín. Prohibido presentar las cuantías de Barcelona como «de '
        'Cataluña».',
        'NO escribas que el trabajador cobra el plus de formación por no tener '
        'formación: lo paga la empresa que no acredita haberla dado, y ni la '
        'prevención de riesgos ni la manipulación de alimentos computan como '
        'formación a estos efectos.',
    ],
    4: [
        'NO escribas sobre «autoridad formal frente a autoridad real», sobre '
        '«señales tempranas de que alguien se está quemando» ni sobre «la '
        'conversación difícil con su guion y su acuerdo escrito»: los tres son '
        'del cap. 7 del Manual del Manager y aquí se citan.',
        'NO conviertas el capítulo en psicología de equipos ni etiquetes a '
        'nadie: se describen conductas observables en el trabajo y decisiones '
        'que se toman en el pase.',
        'NO propongas «hablar las cosas» como solución de nada: lo que se '
        'cambia es el circuito —quién canta, quién confirma, quién decide—, no '
        'el carácter de las personas.',
    ],
    5: [
        'NO recalcules ningún coste en este capítulo ni expliques cómo se hace '
        'un escandallo: el coste entra copiado en una casilla verde y se remite '
        'al Kit de Escandallos y a la Guía Food Cost.',
        'NO metas aquí la declaración de alérgenos de la carta con sus catorce '
        'columnas: en esta ficha van los alérgenos DE PROCESO de esta '
        'elaboración, y la declaración de carta vive en el Pack APPCC.',
    ],
    6: [
        'NO des ningún porcentaje de cumplimiento de ficha «aceptable» ni '
        'ningún benchmark de calidad del pase: el objetivo es de la casa y vive '
        'en una casilla editable.',
        'NO escribas otro checklist de servicio: si aparece una lista, es de '
        'DECISIONES. Los checklists por partida están en el Kit de Tareas y se '
        'citan.',
    ],
    7: [
        'NO conviertas esto en un manual de mise en place ni expliques cómo se '
        'monta un puesto: el capítulo trata de cuánto hay que producir, no de '
        'cómo se prepara.',
        'NO des ninguna regla del tipo «produce un porcentaje por encima de las '
        'reservas»: la previsión sale de las reservas, del histórico y del '
        'criterio del chef, y se ajusta midiendo.',
    ],
    8: [
        'NO des ningún tiempo de pase «normal» ni ningún benchmark del sector: '
        'está verificado que no existe ninguno publicado en España. Los tres '
        'objetivos del caso son de la casa y se dicen con esas palabras.',
        'NO conviertas el pase en una lista de frases motivadoras ni en reglas '
        'de comportamiento: lo que se describe son roles, secuencia y '
        'protocolo.',
        'NO escribas que un plato de delivery puede salir por debajo de la '
        'temperatura de mantenimiento en caliente si va a llegar pronto: la '
        'obligación no cambia porque el trayecto sea corto.',
    ],
    9: [
        'NO presentes esta lista de siete indicadores como un estándar del '
        'sector: es una propuesta de la casa y hay que decirlo con esas '
        'palabras, empezando por el primer párrafo.',
        'NO escribas ningún indicador financiero —ventas, food cost, labor '
        'cost, prime cost, ticket medio, margen—: no están en este libro y son '
        'del Manual del Manager.',
        'NO des un objetivo recomendado para ninguno de los siete: el objetivo '
        'lo pone el lector y el semáforo está gris hasta que lo pone.',
    ],
    10: [
        'NO escribas ningún porcentaje de merma «sano», «normal» o «de '
        'referencia», ni siquiera para desmentirlo con un número. Lo que se '
        'dice es que no existe fuente y que la cifra propia sale de medir.',
        'NO reconstruyas el registro de mermas por producto ni el cálculo de '
        'rendimiento del ingrediente: son del Kit de Inventario y de la Guía '
        'Food Cost, y se citan por su nombre.',
        'NO mezcles merma con desperdicio alimentario: son dos cosas distintas '
        'y el desperdicio se trata en el capítulo de comidas testigo y '
        'banquetes.',
    ],
    11: [
        'NO des precios de producto, ni de mercado ni de proveedor: no hay '
        'ninguno en este pack y no se inventan.',
        'NO expliques el registro de recepción de mercancía con sus columnas: '
        'está en el Kit de Inventario. Aquí va la especificación y qué se '
        'guarda del albarán.',
        'NO cites el reglamento de contaminantes derogado como si fuera el '
        'vigente.',
    ],
    12: [
        'NO hagas ingeniería de menú: la matriz de carta, la clasificación de '
        'platos y la decisión de precio están en la Guía Food Cost y se citan.',
        'NO des un número de platos «que hay que renovar por temporada» ni un '
        'plazo estándar de desarrollo: los días máximos en prueba son una '
        'casilla editable de la casa.',
    ],
    13: [
        'NO cites el RD 3484/2000 ni el RD 1420/2006 más que para decir que '
        'están derogados: es el error de cita más repetido del oficio y aquí se '
        'corrige expresamente.',
        'NO escribas que la flexibilidad de temperaturas del artículo 30 '
        'permite bajar del mantenimiento en caliente o subir de la congelación: '
        'ese apartado se refiere sólo a la refrigeración.',
        'NO metas aquí el bloque del local —ruido, música ambiental, horarios, '
        'terraza, perros de asistencia— ni la carpeta documental de la '
        'inspección: son del cap. 19 del Manual del Manager.',
    ],
    14: [
        'NO escribas que el reglamento de higiene tiene un capítulo de '
        'alérgenos: no lo tiene, y este capítulo existe en buena parte para '
        'corregir esa frase.',
        'NO reproduzcas la declaración de alérgenos plato a plato de la carta: '
        'vive en el Pack APPCC. Aquí van los alérgenos de proceso de la '
        'elaboración.',
        'NO digas que el cartel de «consulte al personal» basta, y tampoco que '
        'está prohibido: la información oral es legal si además hay soporte '
        'escrito o electrónico accesible, y hay que indicar de forma visible '
        'dónde está.',
    ],
    15: [
        'NO publiques ninguna tabla de días de vida útil presentada como '
        'normativa ni des un número general de días para nada: las vidas útiles '
        'que aparecen son las de este caso modelado y son editables.',
        'NO presentes la recomendación de temperatura de la quinta gama como '
        'una norma: es un informe de una agencia autonómica y se declara su '
        'fiabilidad.',
        'NO digas que superar un nivel de referencia de acrilamida es ilegal ni '
        'sancionable.',
    ],
    16: [
        'NO vuelvas a explicar la jerarquía de prevención del desperdicio, el '
        'doggy bag y la exención de superficie como bloque: están en el cap. 19 '
        'del Manual del Manager. Aquí caben en UNA tabla de una página con la '
        'decisión de cocina.',
        'NO digas que las comidas testigo obligan siempre ni que sólo obligan a '
        'hospitales y colegios: obligan en los supuestos tasados, y el que '
        'alcanza a un restaurante normal es el del encargo por encima del '
        'umbral de comensales.',
        'NO olvides la doble toma cuando la elaboración y el servicio ocurren '
        'en establecimientos distintos: son dos muestras, no una, y es el caso '
        'literal del catering.',
    ],
    17: [
        'NO escribas «la temperatura legal de la cocina es de 14 a 25 grados» '
        'ni ninguna variante: la norma fija rangos por categoría de trabajo, no '
        'hay rango para el trabajo pesado y la categoría la fija la evaluación '
        'de riesgos.',
        'NO escribas que la lista del anexo de equipos de protección «exige» '
        'nada: es una lista no exhaustiva de actividades que pueden requerir '
        'equipo, y quien lo convierte en obligación es la evaluación de '
        'riesgos. La gratuidad y la reposición sí son incondicionales.',
        'NO repitas el bloque de documentos de prevención del cap. 15 del '
        'Manual del Manager —plan, evaluación, planificación, emergencias, '
        'reconocimiento médico—: se cita y se pasa al riesgo físico de la '
        'cocina.',
    ],
    18: [
        'NO vuelvas a preguntar si alguien «puede cubrir» una partida: eso es '
        'cobertura y se mide con la matriz de polivalencia del Manual del '
        'Manager. Aquí se mide si lo hace bien.',
        'NO llames «carné de manipulador» a la formación en manipulación de '
        'alimentos: no existe ese carné desde 2010 y la obligación es del '
        'titular de la empresa, por puesto.',
        'NO des ninguna cifra de horas de formación por trabajador de cocina: '
        'no existe ese dato desagregado. El dato de inversión en formación que '
        'te llega va con su etiqueta exacta.',
    ],
    19: [
        'NO diagnostiques el conflicto entre cocina y sala: está hecho en el '
        'cap. 16 del Manual del Manager y aquí se cita. Lo que se da son los '
        'protocolos concretos de los cruces que fallan.',
        'NO escribas el guion de la propuesta al gerente en cuatro movimientos: '
        'es del cap. 7 del Manual del Manager. Lo que aporta este capítulo es '
        'qué cifra de cocina sostiene cada petición.',
        'NO pongas dos responsables en la misma decisión ni escribas que «se '
        'decide entre todos»: la regla de la matriz es que sólo una persona '
        'responde del resultado de cada decisión.',
    ],
    20: [
        'NO montes aquí un plan de noventa días con decisiones, responsable y '
        'semana: es el cap. 20 del Manual del Manager y tiene su propia hoja. '
        'Aquí se dice qué medir en cocina para poder comparar.',
        'NO prometas un resultado a los noventa días: se enseña qué anotar el '
        'primer día para poder comparar, no cuánto se va a mejorar.',
        'NO digas que este pack sirve «para gestionar varias cocinas» sin el '
        'matiz: está hecho para una cocina y trae las herramientas para '
        'compararlas.',
    ],
}

for _cap in CAPITULOS:
    _cap['prohibido'] = NO_COMUN + ESPECIFICAS.get(_cap['n'], [])


# --------------------------------------------------------------------------
# El bonus: 12 situaciones resueltas en cocina (SPEC §4.2 y D14)
#
# Molde del bonus del hermano: los cinco epígrafes son los mismos en las doce,
# y ése es justamente el valor: el lector aprende el patrón de respuesta («qué
# NO hacer» antes que «qué hacer») y lo aplica a la situación 13, que será la
# suya. Tres de las doce rozan con el bonus del Manual del Manager (la 1 con su
# nº 10, la 3 con su nº 8 y la 11 con su nº 11): las tres están reescritas por
# el EJE, no por el enunciado, según la tabla de frontera D11.
# --------------------------------------------------------------------------
EPI_SIT = ['La situación',
           'Qué no hacer',
           'Protocolo paso a paso',
           'La norma que aplica',
           'La herramienta y el guion']

NO_COMUN_BONUS = NO_COMUN + [
    'Escribe la situación como una situación, no como un capítulo teórico: '
    'empieza por lo que está pasando, con la hora y el dato concretos, y '
    'termina con lo que el lector hace al salir de la cocina.',
    'El epígrafe «Qué no hacer» va ANTES del protocolo y es tan importante como '
    'él: son las reacciones reales que empeoran el caso, escritas en dos o tres '
    'frases cada una, no una lista de obviedades.',
    'El epígrafe «La norma que aplica» lleva la norma y el artículo, y cuando la '
    'norma sea de las verificadas para esta edición, la fecha: «comprobado el 6 '
    'de septiembre de 2026». Si en la situación no aplica ninguna norma, se dice '
    'expresamente que es criterio de gestión y no obligación legal.',
    'Cuando la situación pida una conversación, escribe el GUION LITERAL de las '
    'frases de apertura entre comillas, no un resumen de lo que habría que '
    'decir. Es lo que el lector va a usar tal cual.',
    'No remitas al lector a «el capítulo tal de este manual» por su número: '
    'puedes decir de qué trata, porque este documento se lee suelto. Sí se '
    'citan por su capítulo, en cambio, los OTROS productos del catálogo.',
]

BONUS = [
    {
        'nombre': 'BONUS-12-situaciones-resueltas-cocina',
        'guia': {
            'titulo': '12 Situaciones Resueltas en Cocina',
            'subtitulo': 'Bonus del pack «Manual del Chef Ejecutivo» · con los '
                         'datos de las siete herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Situaciones Resueltas en Cocina',
            'portada_texto': (
                'Doce situaciones que le pasan a cualquier chef: una alergia '
                'que llega con el plato montado, la cámara que se cae un '
                'domingo por la noche, un banquete de ciento veinte personas, '
                'un corte con la cortadora, un pase que se descontrola un '
                'viernes. Cada una con los datos del caso, lo que NO hay que '
                'hacer, el protocolo paso a paso, la norma que aplica con su '
                'artículo y la herramienta del pack que se usa; y cuando hay '
                'que hablar con alguien, el guion literal de la conversación. '
                'No hay ninguna cifra inventada: cada número sale de una celda '
                'que puedes abrir y comprobar.'),
        },
        'gates': {
            'paginas_prometidas': 25,
            'palabras_objetivo': 9500,
            'min_palabras_cap': 550,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': '12 Situaciones Resueltas en Cocina',
                     'subject': 'Bonus del pack Manual del Chef Ejecutivo · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Un Jefe de Partida se Va a Mitad de Temporada y Sólo Él Sabe la Partida de Pescados',
                'resumen_indice': 'cómo se certifica en dos semanas que el relevo sabe hacerlo, y qué se recorta de la carta mientras tanto.',
                'palabras': 800, 'bloques': 1,
                'objetivo': 'Separar dos problemas que llegan juntos y no se '
                            'resuelven igual: quién cubre la partida, que es un '
                            'problema de cuadrante, y quién sabe hacerla, que '
                            'es un problema de competencia técnica. Este bonus '
                            'resuelve el segundo.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: dos semanas de preaviso, mitad de temporada, '
                    'y la persona que se va sostiene una partida entera. Dar el '
                    'número de personas de la brigada, cuántas están evaluadas '
                    'en la rúbrica y cuál es la media ponderada del equipo.',
                    'Qué NO hacer: dar por bueno que quien más años lleva puede '
                    'sostener la partida, repartir los platos entre dos '
                    'personas sin decidir quién responde de cada uno, y dejar '
                    'que la persona que se va se lleve en la cabeza lo que no '
                    'está en ninguna ficha.',
                    'Protocolo: primero, mirar qué competencias exige esa '
                    'partida y con qué peso; segundo, evaluar con la prueba '
                    'práctica a los dos candidatos internos, no con una '
                    'conversación; tercero, usar las dos semanas de preaviso '
                    'para que quien se va cierre las fichas que faltan y forme '
                    'en el puesto, no en una reunión; y cuarto, si nadie llega '
                    'al nivel, recortar los platos de esa partida que exigen la '
                    'competencia que falta hasta que alguien la tenga.',
                    'La norma: aquí no hay obligación legal, y hay que decirlo. '
                    'Lo que sí obliga es la formación de manipulación de '
                    'alimentos de quien entre nuevo, que es del titular de la '
                    'empresa y por puesto, y la formación en prevención, que va '
                    'dentro de jornada y sin coste para la persona.',
                    'La herramienta y el guion: la rúbrica de competencias y la '
                    'prueba práctica, más el plan de desarrollo individual para '
                    'el que sube. Y la frase con la que se le pide a quien se '
                    'va que deje el conocimiento escrito, que no es «déjalo '
                    'todo apuntado» sino una lista concreta de fichas con '
                    'fecha. Frontera: quién puede cubrir la partida y cuánto '
                    'cuesta la baja se calculan con la matriz de polivalencia '
                    'del Manual del Manager.',
                ],
                'cifras': [
                    C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
                    C('Personas evaluadas en la rúbrica de competencias', f'{X_BRIG}!Rúbrica de Competencias!M46', 'num'),
                    C('Media ponderada de la brigada evaluada', f'{X_BRIG}!Rúbrica de Competencias!M47', 'num2'),
                    C('Duración total de la prueba práctica, en minutos', f'{X_BRIG}!Prueba Práctica!C18', 'num'),
                    C('Planes de desarrollo individual en curso', f'{X_BRIG}!Plan de Desarrollo Individual!C26', 'num'),
                    C('Responsable titular de la partida de fríos y entrantes', f'{X_BRIG}!Organigrama!E11', 'txt'),
                    C('Personas asignadas a la partida de fríos y entrantes', f'{X_BRIG}!Organigrama!G11', 'num'),
                ],
                'sector': ['CE-04', 'CE-27'],
                'tablas': [{
                    'titulo': 'Los planes de desarrollo abiertos y la próxima partida que aprende cada uno (brigada-puestos-y-evaluacion.xlsx, hoja «Plan de Desarrollo Individual»)',
                    'src': (X_BRIG, 'Plan de Desarrollo Individual'),
                    'cols': [('Id', 'A', 'txt'), ('Persona', 'B', 'txt'),
                             ('Objetivo', 'C', 'txt'),
                             ('Competencias a trabajar', 'D', 'txt'),
                             ('Estado', 'H', 'txt'),
                             ('Próxima partida a aprender', 'J', 'txt'),
                             ('Remite a', 'K', 'txt')],
                    'filas': (9, 12),
                    'nota': 'La última columna es la que evita duplicar trabajo: el plan de '
                            'desarrollo dice qué competencia hay que trabajar, y remite al plan '
                            'de cross-training del Manual del Manager para el calendario de '
                            'cobertura.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 2,
                'titulo': 'Un Comensal Declara una Alergia con el Plato ya Montado',
                'resumen_indice': 'qué se hace con el plato, qué se hace con la comanda y qué se apunta después.',
                'palabras': 790, 'bloques': 1,
                'objetivo': 'Dar el protocolo de los treinta segundos '
                            'siguientes, que es donde se decide si esto es una '
                            'anécdota o un incidente. Y dejar montado el '
                            'registro que convierte el susto en información.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: el plato está montado en el pase y sala '
                    'avisa de una alergia que no venía en la comanda. Dar las '
                    'incidencias del año del caso, su gravedad máxima y la tasa '
                    'por base de cubiertos.',
                    'Qué NO hacer: retirar el alérgeno del plato ya montado y '
                    'servirlo igual; preguntar a la partida «¿esto lleva…?» y '
                    'quedarse con un «creo que no»; y mandar el plato con la '
                    'advertencia verbal al camarero sin identificarlo.',
                    'Protocolo: el plato montado no se corrige, se descarta; se '
                    'consulta la ficha de proceso, que dice dónde entra cada '
                    'alérgeno en esa elaboración concreta y si hay sustitución '
                    'posible; se elabora de nuevo con material limpio y '
                    'reservado; sale identificado y se entrega en mano; y se '
                    'registra la incidencia aunque no haya llegado al cliente.',
                    'La norma: el equipo, los recipientes y las superficies '
                    'usados con un alérgeno no se usan para otros alimentos si '
                    'no se han limpiado; la información de alérgenos es '
                    'obligatoria también en el plato sin envasar y tiene que '
                    'estar por escrito y accesible, no sólo en un cartel.',
                    'La herramienta y el guion: la tabla de alérgenos de '
                    'proceso de la ficha técnica y el registro de incidencias '
                    'del cuadro de mando. Y las dos frases: la que se le dice a '
                    'sala para ganar los cinco minutos que hacen falta, y la '
                    'que se le dice a la partida para que nadie se lo tome como '
                    'un reproche. Frontera: la declaración de alérgenos de toda '
                    'la carta, plato a plato, vive en el Pack APPCC.',
                ],
                'cifras': [
                    C('Incidencias de alérgenos registradas en el año del caso', f'{X_CUAD}!Semana!AJ57', 'num'),
                    C('Gravedad máxima registrada en el año, de cero a tres', f'{X_CUAD}!Semana!AK57', 'num'),
                    C('Incidencias de alérgenos por base de cubiertos en el año', f'{X_CUAD}!Semana!AL57', 'num2'),
                    C('Objetivo de la casa para las incidencias de alérgenos', f'{X_CUAD}!Parámetros!B32', 'num2'),
                    C('Alérgenos presentes como ingrediente en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B79', 'num'),
                    C('Alérgenos por traza en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B80', 'num'),
                    C('Alérgenos por utensilio compartido en la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B81', 'num'),
                    C('Nota de la auditoría en el área de alérgenos en el pase', f'{X_AUD}!Resumen por Área!D10', 'num2'),
                ],
                'sector': ['CE-01', 'CE-06', 'MM-31'],
                'tablas': [{
                    'titulo': 'Los alérgenos de proceso de la ficha, y qué sustitución admite cada uno (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
                    'src': (X_FICHA, 'Ficha (ejemplo)'),
                    'cols': [('Alérgeno', 'A', 'txt'),
                             ('Estado en esta elaboración', 'B', 'txt'),
                             ('Dónde entra en esta elaboración', 'C', 'txt'),
                             ('Sustitución posible', 'E', 'txt')],
                    'filas': (60, 65),
                    'nota': V_852 + ' — la columna de sustitución es la que permite contestar en '
                            'treinta segundos si el plato se puede adaptar o no.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
        ],
    },
]

BONUS[0]['capitulos'] += [
    {
        'n': 3,
        'titulo': 'Sanidad se Presenta sin Avisar en Mitad del Servicio',
        'resumen_indice': 'quién sigue cocinando, quién acompaña y qué se enseña desde la cocina mientras el pase no para.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Resolver la parte que no puede resolver ningún manual de '
                    'gestión: qué hace la COCINA mientras el inspector mira y '
                    'el servicio sigue en marcha.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: dos personas con acreditación en la puerta de '
            'cocina, viernes, cuarenta comandas dentro. Dar los puntos de '
            'control de la auditoría interna, la nota ponderada de la última '
            'visita y el cumplimiento global, para situar en qué estado llega '
            'esta cocina a la visita.',
            'Qué NO hacer: parar el servicio entero y mandar a todo el mundo a '
            'limpiar delante del inspector; dejar que acompañe quien esté más '
            'cerca de la puerta; discutir una observación en caliente; y '
            'ponerse a rellenar registros atrasados mientras la inspección '
            'está dentro, que es lo único que convierte un incumplimiento '
            'formal en un problema serio.',
            'Protocolo: el pase no para —quien está cocinando sigue—; acompaña '
            'el chef o quien esté designado como responsable del autocontrol, '
            'nunca un ayudante; se enseña lo que se pide y sólo lo que se pide; '
            'se anota en el momento cada observación con la hora, textual; y '
            'al terminar el servicio se reúne la brigada cinco minutos antes de '
            'que se enfríe el recuerdo.',
            'Qué se enseña desde la cocina, que es lo que este bonus aporta: el '
            'procedimiento de autocontrol y quién está designado; las fichas '
            'técnicas con sus alérgenos de proceso; el registro de comidas '
            'testigo si hay eventos; las temperaturas del muestreo del pase; y '
            'la trazabilidad de un paso atrás de lo que hay en cámara. Los '
            'registros diarios de temperaturas, limpieza y plagas están en el '
            'Pack APPCC y se enseñan desde ahí.',
            'La norma: la cultura de seguridad alimentaria es obligación de la '
            'dirección y hay que poder demostrarla; el procedimiento de '
            'autocontrol tiene que ser permanente, con responsable designado y '
            'revisado cuando cambia un producto, un proceso o un proveedor.',
            'La herramienta y el guion: la auditoría interna de cocina, que es '
            'exactamente el ensayo de esta visita, y la hoja de estado '
            'normativo con su fecha de corte. Y la frase de apertura con la que '
            'se recibe a la inspección sin parecer que se esconde nada. '
            'Frontera: qué se firma, qué se responde y qué se hace con el acta '
            'después están en el Manual del Manager, cap. 19 y en su bonus.',
        ],
        'cifras': [
            C('Puntos de control de la auditoría interna de cocina', f'{X_AUD}!Resumen por Área!B12', 'num'),
            C('Nota ponderada global de la última visita', f'{X_AUD}!Resumen por Área!D12', 'num2'),
            C('Cumplimiento global sobre la escala', f'{X_AUD}!Resumen por Área!E12', 'pct1'),
            C('Escala máxima de puntuación de la auditoría', f'{X_AUD}!Auditoría!D10', 'num'),
            C('Días tras los que el libro avisa de revisar el estado normativo', f'{X_AUD}!Estado Normativo!B9', 'num'),
            C('Aviso de revisión del estado normativo en la fecha del ejemplo', f'{X_AUD}!Estado Normativo!B10', 'txt'),
            C('Platos de la carta con ficha técnica cerrada', f'{X_FICHA}!Índice de Fichas!C52', 'num'),
        ],
        'sector': ['CE-02', 'MM-29'],
        'tablas': [{
            'titulo': 'El estado de cada norma a la fecha de corte, que es lo que se enseña (auditoria-interna-cocina.xlsx, hoja «Estado Normativo»)',
            'src': (X_AUD, 'Estado Normativo'),
            'cols': [('Norma', 'A', 'txt'),
                     ('Estado a la fecha de corte', 'B', 'txt'),
                     ('Qué tiene que hacer el chef', 'C', 'txt')],
            'filas': (13, 26),
            'nota': 'Esta hoja no la pide ningún inspector: la usas tú para no llegar a la '
                    'visita citando una norma derogada, que es lo que más veces pasa.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 4,
        'titulo': 'Un Banquete de Ciento Veinte Personas: Qué Guardar, Cómo y Cuánto Tiempo',
        'resumen_indice': 'el umbral que dispara la obligación, los cien gramos por elaboración y la cuenta atrás de siete días.',
        'palabras': 800, 'bloques': 1,
        'objetivo': 'Que el lector salga sabiendo exactamente qué muestra '
                    'guardar de cada elaboración de un evento, dónde, a qué '
                    'temperatura y hasta cuándo. Es la obligación que más se '
                    'incumple sin saberlo.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: se acepta un banquete y nadie ha mirado si dispara '
            'la obligación de comida testigo. Dar los comensales del evento del '
            'caso, el umbral a partir del cual obliga, las elaboraciones del '
            'menú y las muestras que hay que recoger.',
            'Qué NO hacer: guardar una sola muestra «del menú»; guardarla en un '
            'táper sin identificar y sin fecha; tirarla cuando pasa el evento '
            'porque «ya no hace falta»; y dar por hecho que sólo obliga si el '
            'evento es en un salón de banquetes.',
            'Protocolo: comprobar el supuesto que te alcanza antes de aceptar '
            'el encargo; recoger una ración individual de al menos cien gramos '
            'POR ELABORACIÓN, no por menú; identificarla con el plato, el lote '
            'y la fecha; conservarla a cuatro grados o menos, o a menos '
            'dieciocho o menos; guardarla un mínimo de siete días; y destruirla '
            'sólo cuando la cuenta atrás lo diga.',
            'La doble toma, que es el caso del catering y casi nadie conoce: si '
            'la elaboración y el servicio ocurren en establecimientos '
            'distintos, quien elabora recoge la muestra en el momento más '
            'próximo a la salida y quien sirve la recoge en el momento del '
            'servicio. Son dos, no una.',
            'La norma: los supuestos que obligan, el gramaje, los siete días y '
            'las dos temperaturas están en los apartados 8, 9 y 10 del artículo '
            '30 del real decreto de higiene de la producción y comercialización '
            'de alimentos, en su redacción vigente.',
            'La herramienta y el guion: el libro de banquetes y comidas '
            'testigo, con su alerta de obligación, su cuenta atrás y su control '
            'de gramaje y temperatura. Y la frase con la que se le explica al '
            'cliente que su evento lleva un registro sanitario asociado, que en '
            'vez de asustar suele vender.',
        ],
        'cifras': [
            C('Comensales del evento del caso', f'{X_BANQ}!Registro de Comidas Testigo!D22', 'num'),
            C('Comensales a partir de los que obliga la comida testigo', f'{X_BANQ}!Registro de Comidas Testigo!D7', 'num'),
            C('Alerta que enciende el libro para este evento', f'{X_BANQ}!Registro de Comidas Testigo!D26', 'txt'),
            C('Gramos mínimos por elaboración guardada', f'{X_BANQ}!Registro de Comidas Testigo!D8', 'num'),
            C('Días mínimos de conservación de la muestra', f'{X_BANQ}!Registro de Comidas Testigo!D9', 'num'),
            C('Temperatura máxima en refrigeración de la muestra', f'{X_BANQ}!Registro de Comidas Testigo!D10', 'num'),
            C('Elaboraciones del menú del evento', f'{X_BANQ}!Registro de Comidas Testigo!D55', 'num'),
            C('Muestras testigo registradas del evento', f'{X_BANQ}!Registro de Comidas Testigo!D54', 'num'),
            C('Muestras que faltan por tomar', f'{X_BANQ}!Registro de Comidas Testigo!D56', 'num'),
            C('Muestras con aviso de doble toma', f'{X_BANQ}!Registro de Comidas Testigo!D60', 'num'),
        ],
        'sector': ['CE-11'],
        'tablas': [{
            'titulo': 'Las muestras testigo del evento, una por elaboración (banquetes-comidas-testigo.xlsx, hoja «Registro de Comidas Testigo»)',
            'src': (X_BANQ, 'Registro de Comidas Testigo'),
            'cols': [('Id de muestra', 'A', 'txt'), ('Elaboración', 'C', 'txt'),
                     ('Gramos', 'G', 'num'), ('Ubicación', 'H', 'txt'),
                     ('Temperatura (°C)', 'I', 'num'),
                     ('Conservación', 'J', 'txt'),
                     ('Días que faltan', 'L', 'num'), ('Estado', 'M', 'txt'),
                     ('Momento de la toma', 'Q', 'txt')],
            'filas': (39, 50),
            'nota': V_TESTIGO + ' — la columna de días que faltan es la que impide los dos '
                    'errores contrarios: tirarlas antes de tiempo y acumular meses de táperes '
                    'en la cámara.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 5,
        'titulo': 'El Pase se Descontrola un Viernes: Cuarenta Comandas y Veinticinco Minutos',
        'resumen_indice': 'qué se hace en los diez minutos siguientes, en qué orden se recupera el pase y qué se mide el lunes.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Dar una secuencia de recuperación en vez de una arenga, y '
                    'enseñar a distinguir el atasco puntual del problema '
                    'estructural que se ve en los datos del muestreo.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: viernes noche, el tiempo de principales se ha ido a '
            'más del doble del objetivo y siguen entrando comandas. Dar el '
            'tiempo medio de pase de principales del año y el objetivo de la '
            'casa para situar la distancia.',
            'Qué NO hacer: gritar más alto; empezar a montar platos fuera de '
            'orden para «sacar algo»; mandar a alguien de fríos a caliente sin '
            'decirle qué deja de hacer; y prometer a sala tiempos que no se van '
            'a cumplir.',
            'Protocolo: parar de aceptar comandas nuevas en el pase durante dos '
            'minutos y ordenar las que hay por hora de entrada; agrupar por '
            'técnica en vez de por mesa cuando el atasco es de plancha o de '
            'horno; declarar un 86 si hay un plato que está bloqueando la '
            'cadena; avisar a sala del tiempo REAL, una sola vez y con un '
            'número; y reforzar la posición del cuello de botella, no el pase '
            'entero.',
            'La norma: aquí no hay obligación legal y hay que decirlo, con una '
            'excepción que no se puede saltar por prisa: lo que se sirve '
            'caliente sigue teniendo que salir a la temperatura de '
            'mantenimiento, y un plato que ha esperado en el pase por debajo de '
            'ella no se envía, se rehace.',
            'La herramienta y el guion: el muestreo del pase, que el lunes dice '
            'si aquello fue un viernes malo o el síntoma de un tiempo que lleva '
            'semanas por encima; y el registro de devueltos y retrabajados, que '
            'es donde aparece el coste invisible de estas noches. Y las dos '
            'frases: la que se le dice a sala en el momento y la que se le dice '
            'a la brigada al terminar.',
        ],
        'cifras': [
            C('Tiempo medio de pase de principales en el año del caso', f'{X_CUAD}!Semana!AH57', 'num1'),
            C('Objetivo de la casa para el pase de principales', f'{X_CUAD}!Parámetros!B30', 'num'),
            C('Tiempo medio de pase de entrantes en el año', f'{X_CUAD}!Semana!AG57', 'num1'),
            C('Platos devueltos en el año del caso', f'{X_CUAD}!Semana!AO57', 'num'),
            C('Platos retrabajados en el año del caso', f'{X_CUAD}!Semana!AP57', 'num'),
            C('Devueltos y retrabajados por base de cubiertos en el año', f'{X_CUAD}!Semana!AQ57', 'num1'),
            C('Muestreos del pase hechos en el periodo', f'{X_CARTA}!Control de Calidad del Pase!D53', 'num'),
            C('Temperatura de emplatado más baja del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D56', 'num1'),
        ],
        'sector': ['CE-10'],
        'tablas': [{
            'titulo': 'Lo que dice el muestreo del pase cuando se mira el lunes (desarrollo-carta-control-calidad.xlsx, hoja «Control de Calidad del Pase»)',
            'src': (X_CARTA, 'Control de Calidad del Pase'),
            'cols': [('Indicador', 'A', 'txt'), ('Medido', 'D', 'num1'),
                     ('Objetivo de la casa', 'E', 'num1'), ('Lectura', 'F', 'txt')],
            'filas': (49, 51),
            'nota': 'Un viernes malo no mueve una media de treinta muestreos. Si la media ya '
                    'estaba por encima del objetivo, el viernes no fue la causa: fue el día en '
                    'que se notó.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
]

BONUS[0]['capitulos'] += [
    {
        'n': 6,
        'titulo': 'El Plato Estrella Sale Distinto Según Quién Esté de Turno',
        'resumen_indice': 'cómo se localiza en qué paso se separan las dos versiones, y qué se hace para que no vuelvan a separarse.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Convertir una queja subjetiva en un problema localizable: '
                    'no es que el plato salga distinto, es que hay un paso '
                    'concreto donde dos personas hacen dos cosas distintas.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: dos reseñas y un comentario de sala dicen que el '
            'plato más vendido no sabe igual según el día. Dar el nombre del '
            'plato del ejemplo, su versión de ficha, las raciones que vende al '
            'mes y su coste por ración copiado del escandallo.',
            'Qué NO hacer: reunir a las dos personas para que se expliquen; '
            'reescribir la ficha entera; decidir por gusto propio cuál de las '
            'dos versiones es la buena sin comparar ninguna de las dos con la '
            'ficha; y cambiar el plato de partida.',
            'Protocolo: hacer el plato dos veces, una con cada persona, con la '
            'ficha delante y sin decirles qué se busca; comparar paso a paso '
            'contra la ficha y anotar dónde se separan; pesar la ración de las '
            'dos; medir la temperatura de emplatado; y decidir cuál de las dos '
            'formas es la correcta, escribirla en la ficha con versión nueva y '
            'formar a las dos personas en el puesto, no en una reunión.',
            'Lo que casi siempre aparece: el paso donde se separan no está '
            'escrito en la ficha. No es un problema de disciplina, es un hueco '
            'de la ficha, y por eso la solución acaba siendo una versión nueva '
            'y no una bronca.',
            'La norma: aquí no hay obligación legal, y hay que decirlo. Lo '
            'único que sí obliga es que si el plato cambia de ingrediente '
            'cambie también su información de alérgenos.',
            'La herramienta y el guion: la ficha de proceso con sus pasos y sus '
            'puntos de control, el muestreo del pase para comprobar después que '
            'la desviación ha desaparecido, y el índice de fichas para subir la '
            'versión. Y la frase con la que se le dice a alguien que su forma '
            'de hacerlo no es la que va a quedar, sin que suene a que lo hace '
            'mal.',
        ],
        'cifras': [
            C('Nombre del plato de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B7', 'txt'),
            C('Versión actual de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B11', 'txt'),
            C('Raciones vendidas al mes del plato de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B17', 'num'),
            C('Coste por ración copiado del escandallo', f'{X_FICHA}!Ficha (ejemplo)!B16', 'eur2'),
            C('Punto de cocción escrito en la ficha', f'{X_FICHA}!Ficha (ejemplo)!B46', 'txt'),
            C('Cumplimiento de ficha técnica en el pase, medido', f'{X_CARTA}!Control de Calidad del Pase!D52', 'pct1'),
            C('Objetivo de cumplimiento de ficha de la casa', f'{X_CARTA}!Control de Calidad del Pase!E52', 'pct1'),
            C('Muestreos no conformes con la ficha', f'{X_CARTA}!Control de Calidad del Pase!D54', 'num'),
        ],
        'sector': ['CE-06'],
        'tablas': [{
            'titulo': 'Los pasos de la ficha, con su punto de control: aquí es donde se localiza la diferencia (ficha-tecnica-proceso.xlsx, hoja «Ficha (ejemplo)»)',
            'src': (X_FICHA, 'Ficha (ejemplo)'),
            'cols': [('Nº', 'A', 'num'), ('Operación', 'B', 'txt'),
                     ('Punto de control', 'F', 'txt')],
            'filas': (24, 31),
            'nota': 'Se recorre la lista con las dos personas por separado y se marca el primer '
                    'paso en el que no coinciden. Casi nunca hace falta llegar al final.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 7,
        'titulo': 'La Merma de la Partida de Fríos se Dispara Tres Semanas Seguidas',
        'resumen_indice': 'en qué orden se descartan las causas cuando una sola partida se desvía y el resto no.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Dar el orden de descarte que evita el error más caro de '
                    'esta situación: empezar por sospechar de la persona. Se '
                    'empieza por el dato, se sigue por el producto y por la '
                    'producción, y sólo al final se habla con alguien.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: tres semanas seguidas con la merma de una partida '
            'muy por encima de su objetivo mientras la merma global de la '
            'cocina apenas se mueve. Dar la merma global del año, la de la '
            'partida en el año, la de la semana peor y el objetivo de la casa '
            'para esa partida.',
            'Qué NO hacer: mirar sólo la merma global, que es donde el problema '
            'no se ve; deducir que alguien está tirando producto; bajar el '
            'objetivo de la partida para que el semáforo se ponga verde; y '
            'cambiar de proveedor sin comprobar primero si el dato está bien '
            'medido.',
            'Protocolo, en este orden: primero, comprobar que el dato es bueno '
            '—que se pesó y no se estimó, y que los kilos por ración de esa '
            'partida están bien puestos, porque si esa casilla está mal el '
            'porcentaje está mal aunque se pese perfecto—; segundo, mirar la '
            'producción, porque producir de más es la causa raíz más frecuente '
            'y se ve comparando lo producido con lo servido; tercero, mirar el '
            'producto, el calibre y el rendimiento de lo que entró esas tres '
            'semanas; y sólo al final, hablar con la partida, y hacerlo '
            'preguntando qué ha cambiado, no acusando.',
            'La norma: aquí no hay obligación legal y hay que decirlo. Lo que '
            'sí hay es una consecuencia que se cruza con la seguridad '
            'alimentaria: producto elaborado de más que se queda en cámara '
            'acaba tirándose por fecha, y eso es desperdicio, no merma.',
            'La herramienta y el guion: el cuadro de mando de cocina para ver '
            'la columna de esa partida semana a semana, la hoja de parámetros '
            'para comprobar los kilos por ración y el objetivo, y la '
            'planificación de producción para comprobar si se produjo de más. Y '
            'la frase con la que se abre la conversación con la partida, que no '
            'es «se os está yendo la merma».',
        ],
        'cifras': [
            C('Merma global de la cocina en el año del caso', f'{X_CUAD}!Semana!AF57', 'pct1'),
            C('Merma del año de la partida de fríos y entrantes', f'{X_CUAD}!Semana!X57', 'pct1'),
            C('Merma de esa partida en la peor de las tres semanas', f'{X_CUAD}!Semana!X37', 'pct1'),
            C('Merma global de la cocina en esa misma semana', f'{X_CUAD}!Semana!AF37', 'pct1'),
            C('Cubiertos servidos en esa semana', f'{X_CUAD}!Semana!D37', 'num'),
            C('Indicadores fuera de objetivo en esa semana', f'{X_CUAD}!Semana!AR37', 'num'),
            C('Kilos de materia prima neta por ración de esa partida', f'{X_CUAD}!Parámetros!C16', 'num2'),
            C('Merma total del año en kilos', f'{X_CUAD}!Semana!V57', 'num'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Siete semanas seguidas: la merma global no se mueve y la de una partida sí (cuadro-de-mando-cocina.xlsx, hoja «Semana»)',
            'src': (X_CUAD, 'Semana'),
            'cols': [('Semana ISO', 'A', 'num'), ('Cubiertos servidos', 'D', 'num'),
                     ('Merma global (%)', 'AF', 'pct1'),
                     ('Merma de pase y caliente (%)', 'W', 'pct1'),
                     ('Merma de fríos y entrantes (%)', 'X', 'pct1'),
                     ('Indicadores fuera de objetivo', 'AR', 'num'),
                     ('Lectura de la semana', 'AS', 'txt')],
            'filas': (35, 41),
            'nota': 'Ésta es la tabla que justifica todo el libro: sin columna por partida, '
                    'estas tres semanas no existen para nadie.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 8,
        'titulo': 'Se Cae la Cámara un Domingo por la Noche',
        'resumen_indice': 'qué se mide antes de abrir, qué producto se salva, qué se descarta sin discusión y qué se apunta.',
        'palabras': 800, 'bloques': 1,
        'objetivo': 'Dar una decisión defendible a las once de la noche de un '
                    'domingo, cuando no hay a quién llamar. Y dejar por escrito '
                    'lo que permitirá justificar esa decisión meses después.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: la cámara de refrigeración marca una temperatura muy '
            'por encima de la de conservación y no se sabe desde cuándo. '
            'Domingo por la noche, cocina cerrada, servicio del martes. Dar las '
            'temperaturas de referencia del libro para situar la distancia.',
            'Qué NO hacer: abrir la puerta para «ver cómo está» el producto; '
            'repartir lo dudoso entre la brigada para que no se pierda; '
            'meterlo todo en el congelador y decidir el martes; y tirarlo todo '
            'sin anotar nada, que es tan malo como no tirar nada.',
            'Protocolo: no abrir; medir la temperatura del aire y, sobre todo, '
            'la del centro de un producto testigo; anotar la hora de la medida '
            'y la última hora en la que consta que la cámara estaba bien; '
            'separar por familias —lo crudo de origen animal, lo elaborado '
            'listo para consumo y lo envasado sin abrir aguantan cosas '
            'distintas—; decidir con la temperatura y el tiempo, no con el olor '
            'ni con el aspecto; trasladar lo que se salva a otra cámara antes '
            'de seguir; y escribir la decisión producto a producto.',
            'Las dos reglas que no se negocian: lo que ya se recalentó y no se '
            'consumió no vuelve a la cámara ni se vuelve a calentar; y lo '
            'congelado que se ha descongelado no se vuelve a congelar como si '
            'nada, porque las tres fechas de su etiqueta ya no dicen la verdad.',
            'La norma: las temperaturas de conservación en refrigeración y en '
            'congelación y la regla de lo recalentado están en el artículo 30 '
            'del real decreto vigente; el etiquetado de lo que se congela en el '
            'establecimiento lleva tres fechas, y por eso lo que se descongela '
            'sin control pierde su trazabilidad.',
            'La herramienta y el guion: la hoja de estado normativo para '
            'comprobar qué temperatura rige y el registro del pack de seguridad '
            'alimentaria para dejar constancia; y la nota que se escribe en el '
            'momento —hora, temperatura medida, producto, decisión y quién la '
            'tomó—, que es exactamente lo que se va a pedir si alguna vez hay '
            'que justificarlo.',
        ],
        'cifras': [
            C('Temperatura máxima en refrigeración de la muestra testigo', f'{X_BANQ}!Registro de Comidas Testigo!D10', 'num'),
            C('Temperatura máxima en congelación de la muestra testigo', f'{X_BANQ}!Registro de Comidas Testigo!D11', 'num'),
            C('Temperatura mínima de mantenimiento en caliente del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D58', 'num'),
            C('Vida útil del puré de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D88', 'num'),
            C('Vida útil de la salsa de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D89', 'num'),
            C('Vida útil de la pieza racionada de la ficha de ejemplo, en días', f'{X_FICHA}!Ficha (ejemplo)!D91', 'num'),
            C('Días tras los que el libro avisa de revisar el estado normativo', f'{X_AUD}!Estado Normativo!B9', 'num'),
        ],
        'sector': ['CE-10', 'CE-13', 'CE-16'],
        'tablas': [{
            'titulo': 'Qué se salva, qué se descarta y qué se apunta cuando se cae el frío',
            'cabecera': ['Qué tienes en la cámara', 'Qué se hace', 'Por qué'],
            'filas': [
                ['Producto crudo de origen animal sin abrir, dentro de su envase', 'Se decide por la temperatura del centro y por el tiempo transcurrido, no por el aspecto', 'Es el que peor tolera la desviación y el que más riesgo tiene'],
                ['Elaboración propia lista para consumo', 'Se descarta si no se puede demostrar que se mantuvo en temperatura', 'Es el supuesto en el que la norma exige estudio de vida útil'],
                ['Producto ya recalentado que no se consumió', 'Se descarta siempre', 'La norma dice que no vuelve a calentarse ni a almacenarse'],
                ['Congelado que se ha descongelado', 'No se vuelve a congelar; se decide entre usarlo con tratamiento térmico inmediato o descartarlo', 'Sus tres fechas de etiqueta ya no describen el producto'],
                ['Envasado no perecedero y conservas', 'Se revisa el envase y se mantiene', 'La cadena de frío no es su barrera'],
                ['Vegetal crudo y fruta', 'Se valora por estado; suele salvarse', 'Su riesgo es de calidad antes que de seguridad'],
                ['Cualquier producto del que dudes', 'Se descarta y se anota', 'La duda no se resuelve con el olfato'],
                ['La decisión de cada producto', 'Se escribe: hora, temperatura medida, producto, decisión y quién la tomó', 'Es lo único que permite justificarla meses después'],
            ],
            'nota': V_TEMP + ' — esta tabla es criterio de cocina construido sobre las reglas '
                    'de temperatura de la norma, no una tabla oficial de decisión: la '
                    'valoración concreta de un producto en un incidente depende de su '
                    'naturaleza, del tiempo y de la temperatura alcanzada.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
]

BONUS[0]['capitulos'] += [
    {
        'n': 9,
        'titulo': 'Un Cocinero se Corta con la Cortadora de Fiambre',
        'resumen_indice': 'qué obliga la ley antes del accidente y qué después, y qué se comprueba esa misma noche.',
        'palabras': 800, 'bloques': 1,
        'objetivo': 'Que el lector sepa qué tenía que estar hecho ANTES —que es '
                    'donde se juega la responsabilidad— y qué hay que hacer '
                    'después, sin convertirlo en un manual de primeros auxilios '
                    'ni en un dictamen de prevención.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: corte profundo con la cortadora en pleno servicio, '
            'traslado a urgencias y una cocina que sigue funcionando. Situarla '
            'con los puntos de prevención de la auditoría, su peso y la nota de '
            'esa área en la última visita.',
            'Qué NO hacer: seguir usando la máquina «con cuidado» el resto del '
            'servicio; retirar el resguardo para limpiar y no volver a '
            'ponerlo; buscar culpable antes de saber si la máquina estaba '
            'protegida; y no dejar constancia porque «no ha sido nada».',
            'Protocolo de esa misma noche: atender y trasladar; parar la '
            'máquina y no volver a usarla hasta comprobarla; comprobar si el '
            'resguardo estaba puesto y en uso; comprobar si esa persona tenía '
            'la formación del puesto y el equipo de protección entregado; '
            'anotar hora, tarea, máquina, estado del resguardo y testigos; y '
            'comunicarlo por la vía que corresponda, con la dirección y el '
            'servicio de prevención.',
            'Lo que tenía que estar hecho ANTES, que es lo que decide la '
            'responsabilidad: los elementos móviles con riesgo de contacto '
            'mecánico llevan resguardos o dispositivos que impiden el acceso; '
            'las comprobaciones del equipo las hace personal competente, se '
            'documentan y se conservan durante toda su vida útil; el equipo de '
            'protección se entrega gratis y se repone; y la formación va dentro '
            'de jornada y su coste no recae nunca sobre la persona.',
            'La distinción que evita escribir una falsedad: la lista del anexo '
            'de equipos de protección no obliga por sí sola; es una lista NO '
            'exhaustiva de actividades que PUEDEN requerir equipo, y quien lo '
            'convierte en obligación es la evaluación de riesgos. Lo que sí es '
            'incondicional es la gratuidad y la reposición.',
            'La herramienta y el guion: los puntos de prevención de la '
            'auditoría interna, que son exactamente la lista de lo que había '
            'que tener comprobado, y la nota escrita del incidente. Y las dos '
            'frases: la que se le dice a la brigada al reanudar el servicio y '
            'la que se le dice a la persona cuando vuelve.',
        ],
        'cifras': [
            C('Puntos de control del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!B9', 'num'),
            C('Peso del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!C9', 'num'),
            C('Nota de la última visita en el área de prevención de riesgos', f'{X_AUD}!Resumen por Área!D9', 'num2'),
            C('Cumplimiento del área de prevención de riesgos', f'{X_AUD}!Resumen por Área!E9', 'pct1'),
            C('Escala máxima de puntuación de la auditoría', f'{X_AUD}!Auditoría!D10', 'num'),
            C('Umbral de aviso crítico de la auditoría', f'{X_AUD}!Auditoría!D12', 'num'),
            C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
        ],
        'sector': ['CE-23', 'CE-25', 'CE-26', 'CE-27', 'CE-28'],
        'tablas': [{
            'titulo': 'Los puntos de prevención que tenían que estar comprobados antes (auditoria-interna-cocina.xlsx, hoja «Auditoría»)',
            'src': (X_AUD, 'Auditoría'),
            'cols': [('Nº', 'A', 'num'), ('Punto de control', 'C', 'txt'),
                     ('Peso (1 a 3)', 'D', 'num'),
                     ('Norma aplicable', 'G', 'txt')],
            'filas': (49, 58),
            'nota': V_PRL + ' — esta lista no es un dictamen de prevención: es lo que un chef '
                    'puede comprobar andando por su cocina. El plan de prevención, la '
                    'evaluación de riesgos y la investigación del accidente son del servicio de '
                    'prevención y de la dirección.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 10,
        'titulo': 'El Plato que Sale por la Puerta: Delivery y Take-away desde la Cocina',
        'resumen_indice': 'qué temperatura sale, en qué envase, cuánto tiempo aguanta y qué platos no viajan.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Dar la carta paralela de lo que sale por la puerta con '
                    'criterio de cocina, no de marketing: qué se puede enviar '
                    'sin que deje de ser el plato que el cliente pagó, y qué se '
                    'queda dentro.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: la dirección quiere abrir el canal de reparto con la '
            'carta entera y sin cambiar nada de la cocina. Dar la temperatura '
            'mínima de mantenimiento en caliente y las temperaturas de '
            'emplatado más alta y más baja del muestreo del pase, que enseñan '
            'de dónde parte cada familia de plato.',
            'Qué NO hacer: mandar la carta entera; envasar en caliente y cerrar '
            'sin ventilación; medir el tiempo desde que el repartidor recoge en '
            'vez de desde que el plato se termina; y dar por hecho que la '
            'obligación de informar de alérgenos se queda en la puerta.',
            'Protocolo: decidir qué platos viajan probándolos con el trayecto '
            'real, no en la cocina; escribir en la ficha de cada uno el envase '
            'y el tiempo máximo, igual que se escribe el punto de cocción; '
            'mantener en caliente lo que se sirve caliente hasta que sale; '
            'etiquetar con el plato y el aviso de alérgenos; y separar '
            'físicamente la zona de montaje de reparto del pase de sala, porque '
            'si comparten espacio los dos van tarde.',
            'La norma: lo que se sirve caliente se mantiene a la temperatura de '
            'mantenimiento en caliente, y el canal de reparto no cambia eso; el '
            'establecimiento debe aceptar el recipiente reutilizable que trae '
            'el cliente, pudiendo rechazarlo si está manifiestamente sucio o es '
            'inadecuado; y el envase de plástico de un solo uso sí se puede '
            'cobrar aparte.',
            'La herramienta y el guion: la ficha de proceso, que es donde se '
            'escriben el envase y el tiempo máximo, y el índice de fichas para '
            'marcar qué platos están aprobados para viajar. Y la frase con la '
            'que se le explica a dirección por qué media carta se queda dentro, '
            'que no es «no se puede» sino qué llega y qué no llega.',
        ],
        'cifras': [
            C('Temperatura mínima de mantenimiento en caliente del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D58', 'num'),
            C('Temperatura de emplatado más alta del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D57', 'num1'),
            C('Temperatura de emplatado más baja del muestreo', f'{X_CARTA}!Control de Calidad del Pase!D56', 'num1'),
            C('Muestras de elaboraciones que se mantienen en caliente', f'{X_CARTA}!Control de Calidad del Pase!D59', 'num'),
            C('De ellas, por debajo del mínimo de mantenimiento en caliente', f'{X_CARTA}!Control de Calidad del Pase!D60', 'num'),
            C('Temperatura mínima de mantenimiento en caliente de la ficha', f'{X_FICHA}!Ficha (ejemplo)!B47', 'num'),
            C('Minutos de pase de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B41', 'num'),
            C('Platos de la carta registrados en el índice de fichas', f'{X_FICHA}!Índice de Fichas!C56', 'num'),
        ],
        'sector': ['CE-10', 'MM-38', 'CE-06'],
        'tablas': [{
            'titulo': 'Qué sale por la puerta y qué se queda dentro',
            'cabecera': ['Familia de plato', '¿Viaja?', 'Con qué condición'],
            'filas': [
                ['Guisos, arroces melosos y legumbres', 'Sí', 'Envase estanco, salen a la temperatura de mantenimiento en caliente y con tiempo máximo escrito'],
                ['Carnes y pescados a la plancha o al horno', 'Sí, con reservas', 'Sin salsa emulsionada encima y con la guarnición separada'],
                ['Fritos y rebozados', 'No, o con el elemento crujiente aparte', 'El vapor del propio plato los ablanda antes de llegar'],
                ['Salsas emulsionadas en caliente', 'No', 'Se cortan con el movimiento y el descenso de temperatura'],
                ['Ensaladas y platos fríos', 'Sí', 'Con el aliño aparte y a temperatura de refrigeración'],
                ['Crudos, marinados y semicrudos', 'Sólo con la cadena de frío del trayecto resuelta y documentada', 'Es el mismo producto que obliga a congelación preventiva en cocina'],
                ['Postres de plato con montaje', 'No como están en carta', 'Se rediseña el montaje para el envase o no se envía'],
                ['Cualquier plato aprobado para viajar', 'Sí', 'Con envase y tiempo máximo escritos en su ficha y con etiqueta de alérgenos'],
            ],
            'nota': V_TEMP + ' — el reparto no cambia ninguna obligación: cambia el tiempo que '
                    'pasa entre que el plato se termina y se come, y por eso la decisión de qué '
                    'viaja es de cocina y no de marketing.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
]

BONUS[0]['capitulos'] += [
    {
        'n': 11,
        'titulo': 'El Propietario Quiere Quitar de la Carta un Plato que a Ti te da Margen',
        'resumen_indice': 'de quién es esa decisión, qué arrastra quitar un plato y con qué datos se defiende.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Convertir una orden en una conversación técnica sin '
                    'convertirla en un pulso: enseñar qué arrastra quitar un '
                    'plato de la carta y con qué datos de cocina se sostiene la '
                    'propuesta contraria.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: el propietario quiere retirar un plato porque «no lo '
            'pide nadie» y ese plato es de los que mejor funcionan en la '
            'partida. Dar el nombre del plato del ejemplo, sus raciones '
            'vendidas al mes, su coste por ración y el coste de materia prima '
            'que mueve al mes.',
            'Qué NO hacer: decir que no sin datos; defender el plato porque te '
            'gusta; aceptar y quitarlo el mismo día sin mirar qué arrastra; y '
            'convertirlo en un pulso delante de la brigada.',
            'Protocolo: comprobar primero de quién es la decisión en la matriz '
            'de responsabilidades, para no discutir sobre eso; reunir lo que '
            'tienes —raciones vendidas, coste por ración, carga que da a su '
            'partida y qué elaboraciones comparte con otros platos—; enseñar '
            'qué arrastra quitarlo: si su elaboración previa alimenta a otro '
            'plato, quitar uno encarece al otro y sube la merma; proponer una '
            'alternativa medible con fecha de revisión; y aceptar la decisión '
            'si al final es de dirección, dejando escrito qué se va a medir.',
            'La distinción que ordena la conversación: la decisión de qué se '
            'queda en la carta es de dirección con informe del chef; la ficha, '
            'la producción y la carga de la partida son del chef. Discutir en '
            'la casilla equivocada es lo que hace que estas conversaciones '
            'acaben mal.',
            'La norma: aquí no hay obligación legal, y hay que decirlo. Lo '
            'único que sí obliga es que si el plato desaparece o cambia, cambie '
            'también su información al cliente y su ficha.',
            'La herramienta y el guion: la matriz de responsabilidades para '
            'situar la decisión, la ficha técnica y el índice de fichas para '
            'ver qué elaboraciones comparte, y el registro de pruebas si hay '
            'que proponer un sustituto. Y las frases con las que se abre la '
            'conversación. Frontera doble: si la decisión es de precio o de '
            'mix, se toma con la matriz de carta de la Guía Food Cost; y la '
            'conversación para subir la carta está resuelta en el bonus del '
            'Manual del Manager.',
        ],
        'cifras': [
            C('Nombre del plato de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B7', 'txt'),
            C('Partida que lo produce', f'{X_FICHA}!Ficha (ejemplo)!B9', 'txt'),
            C('Raciones vendidas al mes del plato de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B17', 'num'),
            C('Coste por ración copiado del escandallo', f'{X_FICHA}!Ficha (ejemplo)!B16', 'eur2'),
            C('Coste de materia prima al mes del plato de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B18', 'eur2'),
            C('Minutos de elaboración previa de la ficha de ejemplo', f'{X_FICHA}!Ficha (ejemplo)!B40', 'num'),
            C('Comprobación de la fila del precio de venta en la matriz de decisiones', f'{X_BRIG}!Matriz RACI!J13', 'txt'),
            C('Pruebas de plato registradas en total', f'{X_CARTA}!Registro de Pruebas de Plato!C39', 'num'),
        ],
        'sector': ['MM-14'],
        'tablas': [{
            'titulo': 'Las decisiones de carta que cruzan, y quién responde de cada una (brigada-puestos-y-evaluacion.xlsx, hoja «Matriz RACI»)',
            'src': (X_BRIG, 'Matriz RACI'),
            'cols': [('Decisión', 'A', 'txt'), ('Chef ejecutivo', 'B', 'txt'),
                     ('Jefe de sala', 'E', 'txt'), ('Gerencia', 'F', 'txt'),
                     ('Propiedad', 'G', 'txt')],
            'filas': (13, 27),
            'nota': 'Antes de discutir el fondo, se mira la fila: la mitad de estas '
                    'conversaciones se resuelven cuando las dos partes ven de quién es la '
                    'decisión y a quién había que consultar antes.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
    {
        'n': 12,
        'titulo': 'Un Segundo de Cocina Asciende a Jefe: los Primeros Treinta Días',
        'resumen_indice': 'qué se toca la primera semana, qué se mide desde el primer día y cómo se gana autoridad sobre quien ayer era compañero.',
        'palabras': 790, 'bloques': 1,
        'objetivo': 'Dar el plan de los primeros treinta días de quien acaba de '
                    'ascender, con lo que se toca, lo que no se toca y lo que '
                    'se empieza a medir desde el primer día para poder comparar '
                    'a los noventa.',
        'epigrafes': EPI_SIT,
        'puntos': [
            'La situación: el segundo asciende a jefe de cocina en la misma '
            'brigada. Dar el número de personas de la brigada, cuántas están '
            'encuadradas en cada puesto del convenio y cuántas están evaluadas '
            'en la rúbrica, para que se vea el punto de partida real.',
            'Qué NO hacer: cambiar la carta la primera semana; imponer un '
            'sistema nuevo antes de haber visto un servicio completo desde el '
            'otro lado; intentar seguir siendo el compañero de todos; y hablar '
            'mal de cómo se hacían las cosas antes.',
            'Protocolo de los treinta días: semana uno, no se cambia nada salvo '
            'lo que sea peligroso, y se observa un servicio entero desde el '
            'pase; semana dos, una conversación individual con cada persona, '
            'con dos preguntas fijas; semana tres, la primera decisión visible, '
            'que conviene que sea pequeña, útil y anunciada; semana cuatro, '
            'poner en marcha una sola medición —la que más falta haga— y '
            'anunciar en qué fecha se va a mirar.',
            'La autoridad sobre quien ayer era compañero, que es la parte más '
            'incómoda: no se gana con distancia, se gana con criterio '
            'previsible. Lo que cambia no es el trato, es que ahora hay una '
            'persona que responde del resultado, y eso se dice en voz alta la '
            'primera semana, una vez, y no se vuelve a mencionar.',
            'La norma: si el ascenso implica encuadrarse en otro puesto del '
            'convenio, cambia la clasificación y con ella la retribución; y '
            'encargar funciones de categoría superior tiene sus reglas de plazo '
            'según el convenio provincial. No es un detalle administrativo: es '
            'lo que evita un problema laboral seis meses después.',
            'La herramienta y el guion: las fichas de puesto para saber qué '
            'funciones asume, la matriz de responsabilidades para saber qué '
            'decide, el plan de desarrollo individual para lo que le falta y '
            'las tres cifras del primer día. Y el guion de la primera reunión '
            'con la brigada, con las frases literales de apertura y de cierre.',
        ],
        'cifras': [
            C('Personas de la brigada de cocina', f'{X_BRIG}!Organigrama!F39', 'num'),
            C('Personas encuadradas en los puestos del convenio', f'{X_BRIG}!Fichas de Puesto!G16', 'num'),
            C('Personas en el puesto de jefe o jefa de cocina', f'{X_BRIG}!Fichas de Puesto!G6', 'num'),
            C('Personas en el puesto de segundo o segunda de cocina', f'{X_BRIG}!Fichas de Puesto!G7', 'num'),
            C('Personas evaluadas en la rúbrica de competencias', f'{X_BRIG}!Rúbrica de Competencias!M46', 'num'),
            C('Media ponderada de la brigada evaluada', f'{X_BRIG}!Rúbrica de Competencias!M47', 'num2'),
            C('Merma global de la cocina en el año del caso', f'{X_CUAD}!Semana!AF57', 'pct1'),
            C('Cumplimiento de ficha técnica en el pase, medido', f'{X_CARTA}!Control de Calidad del Pase!D52', 'pct1'),
            C('Horas de cocina por cubierto en el año', f'{X_CUAD}!Semana!AN57', 'num2'),
        ],
        'sector': ['MM-14', 'CONV-01'],
        'tablas': [{
            'titulo': 'Los tres niveles de delegación, que es lo primero que cambia al ascender (brigada-puestos-y-evaluacion.xlsx, hoja «Fichas de Puesto»)',
            'src': (X_BRIG, 'Fichas de Puesto'),
            'cols': [('Nivel', 'A', 'txt'), ('Puestos', 'C', 'txt'),
                     ('Cómo se manda en ese nivel', 'E', 'txt')],
            'filas': (23, 25),
            'nota': V_ALEH + ' — quien asciende deja de ejecutar y empieza a encargar '
                    'resultados: la tabla dice a quién se le puede encargar qué.',
        }],
        'prohibido': NO_COMUN_BONUS,
    },
]


# --------------------------------------------------------------------------
# Erratas que el gate ortográfico marca y NO lo son: nombres propios, términos
# del oficio, vocabulario jurídico y sanitario y extranjerismos que no están en
# el léxico del blog. El gate normaliza los acentos antes de buscar, así que
# también propone «reparar» palabras bien escritas con tilde que el corpus
# nunca usó. Se arranca con la lista que quedó cerrada el 5-sep en el Manual
# del Manager y se le añade el vocabulario propio de una cocina.
# --------------------------------------------------------------------------
_ERRATAS_OK = (
    # Heredadas del Manual del Manager (2026-09-05)
    'actas', 'canta', 'cantó', 'canto', 'atendió', 'atendio', 'desapareció', 'desaparecio', 'rendía', 'rendia',
    'alegar', 'anular', 'auditado', 'califica', 'cometido', 'contó', 'conto', 'digan', 'emitió', 'emitio',
    'escribirá', 'escribira', 'fisco', 'libren', 'manía', 'mania', 'ofreció', 'ofrecio', 'proporcionales',
    'vicio', 'ocurrió', 'ocurrio', 'acusa', 'acusando', 'señalado', 'senalado',
    # Heredadas de la Guía Food Cost (2026-09-04)
    'esima', 'podar', 'tiraje', 'trasladado', 'anado', 'añado', 'arrancado',
    'coincidan', 'cumplio', 'cumplió', 'dependio', 'dependió', 'ensanchado',
    'levado', 'parta', 'costeado', 'manejado', 'puzles', 'pasterizada',
    'perdio', 'perdió',
    'escandallo', 'escandallos', 'escandallar', 'escandallado', 'costeo',
    'beverage', 'delivery', 'packaging', 'away', 'takeaway', 'catering',
    'buffet', 'Horeca', 'Hostelería', 'ponderado', 'ponderada',
    'auditable', 'trazabilidad', 'reformular', 'retirar', 'vinculante',
    'Repsol', 'Michelin',
    # Vocabulario del oficio y de la brigada, propio de este manual
    'partida', 'partidas', 'brigada', 'brigadas', 'pase', 'pases',
    'marmitón', 'marmiton', 'plonge', 'steward', 'stewards', 'economato',
    'economatos', 'repostero', 'repostera', 'repostería', 'reposteria',
    'emplatado', 'emplatar', 'cocciones', 'cocción', 'coccion', 'confitado',
    'confitar', 'abatidor', 'abatir', 'regenerar', 'regeneración',
    'gramaje', 'gramajes', 'racionado', 'racionar', 'raciones', 'cubeto',
    'cubetos', 'mise', 'place', 'comanda', 'comandas', 'cantó', 'marchar',
    'despachar', 'despacho', 'crujiente', 'crujientes', 'guarnición',
    'guarnicion', 'melosos', 'meloso', 'salsear', 'fondos', 'ibérico',
    'iberico', 'boniato', 'panceta', 'solomillo', 'pilpil', 'chistorra',
    'ventresca', 'cebolleta', 'coulant', 'torrija', 'alcachofas',
    'cefalópodos', 'cefalopodos', 'escabechados', 'salazón', 'salazon',
    'marinados', 'ahumados', 'anisakis', 'freidora', 'freidoras',
    'cortadora', 'picadora', 'batidora', 'resguardo', 'resguardos',
    'antideslizante', 'antideslizantes', 'polainas', 'chaquetilla',
    'chaquetillas', 'delantal', 'delantales', 'uniforme', 'uniformes',
    'Encina', 'Girona', 'Cataluña', 'Barcelona', 'Maresme', 'Tarragona',
    # Vocabulario sanitario y normativo
    'alérgenos', 'alergenos', 'alérgeno', 'alergeno', 'autocontrol',
    'trazable', 'testigo', 'testigos', 'refrigerados', 'refrigeración',
    'refrigeracion', 'congelados', 'congelación', 'congelacion',
    'recalentar', 'recalentado', 'recalentados', 'enfriamiento', 'abatimiento',
    'organolépticamente', 'organolepticamente', 'organoléptico',
    'microbiológicos', 'microbiologicos', 'Listeria', 'botulismo',
    'acrilamida', 'contaminantes', 'polares', 'gluten', 'envasado',
    'envasar', 'envases', 'reutilizable', 'reutilizables', 'donable',
    'donación', 'donacion', 'excedente', 'excedentes', 'desperdicio',
    'jerarquía', 'jerarquia', 'microempresa', 'microempresas',
    'derogado', 'derogados', 'derogada', 'vigencia', 'vigentes',
    'consolidado', 'exhaustiva', 'incondicional', 'preventiva',
    'siniestralidad', 'incidencia', 'incidencias', 'acreditada',
    'acreditado', 'sobreesfuerzos', 'ergonómico', 'ergonomico',
    # Vocabulario laboral y de convenio
    'convenio', 'convenios', 'convencional', 'cremallera', 'ultraactividad',
    'movilidad', 'polivalencia', 'delegación', 'delegacion', 'delegar',
    'encuadre', 'encuadrada', 'encuadradas', 'tipifica', 'tipificado',
    'manutención', 'manutencion', 'suplidos', 'devenga', 'devengado',
    'retribución', 'retribucion', 'retributivo', 'gratificaciones',
    'prórroga', 'prorroga', 'denuncia', 'preaviso', 'ascenso', 'asciende',
    'promocionar', 'cobertura', 'competencia', 'competencias', 'rúbrica',
    'rubrica', 'ponderada', 'evaluación', 'evaluacion',
    # Siglas y nombres propios que el léxico no conoce
    'ALEH', 'APPCC', 'REGCON', 'BOCM', 'DOGC', 'INSST', 'AESAN', 'RDLeg',
    'RACI', 'ISO',
    # Palabras correctas que el corpus del blog no contiene
    'reproducible', 'reproducibles', 'defendible', 'localizable',
    'comprobable', 'comprobables', 'escalable', 'reasignan', 'colapsar',
    'colapso', 'versiona', 'versionada', 'versionado', 'muestreo',
    'muestreos', 'muestrear', 'aterrizarlo', 'reescandallar',
    # Errata literal del boletín oficial en las funciones del convenio: si el
    # reparador la «corrige», la cita deja de ser literal.
    'cualifica',
)
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
