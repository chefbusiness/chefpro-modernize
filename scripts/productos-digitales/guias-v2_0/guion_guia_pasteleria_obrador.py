#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
guion_guia_pasteleria_obrador.py — GUION de «Cómo Montar una Pastelería» v1.0
(SPEC `guia-pasteleria-SPEC.md`, §4, §4.2 y §4.3).

Mismo esquema que los hermanos (`guion_manual_chef_ejecutivo.py`, del 6-sep, y
`guion_guia_food_cost_ingenieria_menu.py`, del 4-sep): un capítulo no se le pide
a un redactor con un título, se le pide con un guion CERRADO. Por capítulo van
(a) el objetivo, (b) 4-6 epígrafes, (c) los puntos concretos DE CADA EPÍGRAFE
—`puntos_por_epigrafe`, la forma preferida de `repartir_puntos()`—, (d) las
cifras del propio producto citadas por `fichero.xlsx!Hoja!Celda` —que
`documentos.py` resuelve con openpyxl `data_only` antes de escribir el prompt,
así que el redactor recibe el NÚMERO, no el fichero—, (e) los datos del sector
por `id` de `auditorias/guias-v2-research-sector.json` (ids `PA-*` normativa,
`PS-*` sector), (f) las tablas exigidas —que las construye el maquetador desde
el xlsx, no el redactor—, (g) el presupuesto de palabras y (h) lo que NO debe
decir.

ESTE GUION ES EL PRIMERO DE LA FAMILIA QUE USA `puntos_por_epigrafe` (D33).
Formato exacto: `cap['puntos_por_epigrafe'] = {'<epígrafe literal>': [punto, …]}`.
Para que una clave no pueda desviarse del epígrafe —`repartir_puntos()` aborta
con `SystemExit` si eso pasa, y esos puntos se perderían en silencio— cada
capítulo declara PRIMERO su dict `PPE_nn` y luego pone `'epigrafes': list(PPE_nn)`:
la lista de epígrafes SE DERIVA del dict, así que no hay dos sitios que puedan
discrepar. Lo que va entero a todos los tramos es `puntos_globales`, que NO se
reparte.

REGLA DE LA LÍNEA (John, 2026-09-04): el texto de los productos digitales ya NO
lo escribe `bridge.py`. `dump_prompts.py` vuelca los prompts exactos que
construye `documentos.py` y un subagente Anthropic escribe cada bloque en la
caché `txt/`, verificándolo con `check_bloque.py`. Medidor de solape antes de
ensamblar: `guias-v2_0/solape.py <dir_txt>`.

FUENTE ÚNICA DE CIFRAS: los OCHO libros de
`astro-site/public/dl/guia-pasteleria-obrador/`, que se LEEN y no se tocan. Sus
mapas de celdas (`guia-pasteleria/build/mapa-*.json`) son el CONTRATO: toda
coordenada de este guion sale de ahí o está verificada abriendo el libro con
`data_only`. El juego de datos del caso modelado —la pastelería «La Clara»— es
`guia-pasteleria/datos_ejemplo.py`.

FUENTE ÚNICA DE LO LEGAL: `auditorias/guia-pasteleria-verificacion-legal-2026-09-10.md`,
verificación independiente contra fuentes primarias (BOE, DOUE, BOCM, DOGV,
DOGC y el CTE) del 10 de septiembre de 2026. **Los puntos legales de los
capítulos 09, 10, 17, 19 y del anexo usan la columna «Redacción SEGURA para el
producto» de esa verificación, no la síntesis del research.** Lo que esa
verificación deja como NO VERIFICADO (PA-05, PA-06, PA-26b, PA-27c, PA-33b,
PA-35, PA-41, PA-42, PA-43) **no existe como id** y se trata como «pregunta a tu
ayuntamiento o a tu asesoría», nunca como afirmación.

Presupuesto (SPEC §2.1 y §9): 20 capítulos + anexo normativo, 70 páginas
prometidas, 37.500 palabras objetivo, 1.700-1.850 por capítulo, 2.100 los tres
legales (09, 10 y 19) y ~1.500 el anexo. Bloques por capítulo según la palanca 2
del §9 firmada por el orquestador el 10-sep: **1 bloque** en 01-08, 11, 14, 16,
20 y el anexo; **2 bloques** en 09, 10, 12, 13, 15, 17, 18 y 19. Bonus 1:
business plan modelo relleno, 6 secciones, 3.500 palabras y 9 tablas. Bonus 2:
12 decisiones de apertura resueltas, 800-900 palabras cada una.

DECISIONES DE LA SPEC QUE ESTE GUION MATERIALIZA (no se reabren aquí): D6 (un
solo nombre visible), D7 (lista blanca del art. 13.8 con sus CINCO letras y la
letra e autonómica), D8 (art. 3 con su puerta de entrada y sus dos vías
alternativas dentro de «marginal»), D9 (central y sucursales: la ventaja con su
deber pegado), D10 (4 °C y 8 °C son dos techos, no un conflicto), D11 (plazo
legal y vida útil declarada son dos salidas distintas), D13 (los tres límites
del art. 13.9), D15 (la exención de los 1.300 m² alcanza sólo al apartado 4 del
art. 6), D17 (la columna del IVA y la validación cruzada en UNA sola base),
D18 y D19 (no se menciona ninguna de las seis guías hermanas), D21 (ninguna
celda verde vacía), D22 (90 m², 5 personas y 3,5 jornadas con los nombres
literales de los 4 perfiles del kit), D23 (PS-60 fuera; una sola regla de
margen), D24 (nada de facturaciones medias inventadas), D27 (4 CCAA declaradas
como ejemplo), D28 (anexo normativo fechado como entrada 21), D33
(`puntos_por_epigrafe`), D34 (ids `PA-*` y `PS-*`) y D36 (los umbrales de
`verificar_guion.py`).

Gate de forma, que se corre ANTES de gastar un token de redacción:
    /usr/local/bin/python3 scripts/productos-digitales/guia-pasteleria/verificar_guion.py

Via: Claude Code
"""

PID = 'guia-pasteleria-obrador'

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
    '*Esta guía es un documento de trabajo profesional, no un dictamen '
    'jurídico, sanitario, fiscal ni laboral, y no sustituye al proyecto '
    'técnico visado que te va a pedir tu ayuntamiento. El marco normativo que '
    'se explica es el ESPAÑOL, y su estado se verificó contra las fuentes '
    'oficiales —Boletín Oficial del Estado, Diario Oficial de la Unión '
    'Europea, Boletín Oficial de la Comunidad de Madrid, Diari Oficial de la '
    'Generalitat de Catalunya, Diari Oficial de la Generalitat Valenciana y el '
    'Código Técnico de la Edificación— el 10 de septiembre de 2026: cada '
    'afirmación legal lleva su norma y su artículo para que puedas comprobarla '
    'y para que sepas dónde mirar cuando cambie. Lo que depende de tu '
    'ayuntamiento —la ordenanza de humos, la de ruido, el planeamiento '
    'urbanístico, las tasas— cambia en cada uno de los municipios de España y '
    'aquí se trata como una pregunta que tienes que hacer, nunca como un dato. '
    'Las cuatro comunidades autónomas que aparecen en los cuadros son '
    'EJEMPLOS: comprueba el decreto de la tuya. Las superficies, importes, '
    'precios, gramajes, márgenes y plazos del caso que recorre el documento '
    'son valores de ejemplo de una pastelería modelada que acompaña a este '
    'pack, y viven en celdas editables de las hojas de cálculo precisamente '
    'para que los sustituyas por los tuyos: ninguno es una previsión de tus '
    'resultados, ni un estándar del sector, ni una promesa de rentabilidad. '
    'Antes de firmar un alquiler, presentar un trámite, fijar el precio de una '
    'referencia o contratar a alguien, contrasta con tu ayuntamiento, con tu '
    'asesoría y con la autoridad sanitaria de tu comunidad.*')

GUIA = {
    'pid': PID,
    'titulo': 'Cómo Montar una Pastelería',
    'subtitulo': 'Obrador, licencias y números: el dossier completo de '
                 'apertura · Guía España 2026',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Cómo Montar una Pastelería',
    'fecha': 'septiembre de 2026',
    'version': '1.0.1',
    'tipo_doc': 'guía',
    'tipo_doc_art': 'de la guía',
    'tipo_doc_dem': 'esta guía',
    'categoria_doc': 'Guía profesional',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        'Veinte capítulos, un anexo normativo fechado, ocho herramientas en '
        'Excel con fórmulas vivas, un business plan modelo relleno y doce '
        'decisiones de apertura resueltas, para quien todavía NO ha abierto: '
        'la repostera que vende desde casa y quiere legalizarse, quien ya '
        'vende y no se atreve con el local, quien cambia de vida y quien ya '
        'tiene local y va a por la licencia. No es un recetario, no es un '
        'curso de técnica y no sustituye al proyecto técnico visado: es el '
        'orden en que se toman las decisiones y los números con los que se '
        'toman. Todas las cifras del caso salen de los libros de este mismo '
        'pack, así que el texto y las hojas de cálculo dicen lo mismo; y cada '
        'afirmación legal va con su norma, su artículo y su enlace, '
        'comprobados el 10 de septiembre de 2026.'),
    'gates': {
        'paginas_prometidas': 70,
        'palabras_objetivo': 37500,
        'min_palabras_cap': 1300,
        # Cifras con separador de miles que el texto puede escribir y que NO
        # están en ninguna celda de los ocho libros. Se admiten UNA A UNA y por
        # SIGNIFICADO (lección RD-21 del representante). Ojo: `valores_admitidos()`
        # ya acepta automáticamente todo número que aparezca en el `cifra`, la
        # `cita_literal`, la `nota`, el `dato` o el `fuente_titulo` de cualquier
        # id del research, así que aquí sólo van las que no salen de ahí.
        #  · 1.334/1999 y 2.207/1995 NO se escriben nunca con punto (lo prohíbe
        #    NO_COMUN), así que no hacen falta.
        #  · Hoy no hace falta NINGUNA: toda cifra con separador de miles que el
        #    texto puede escribir sale de una celda de los ocho libros o de la
        #    cita, la nota o el dato de un id del research. El número de
        #    municipios de España, que estuvo aquí en un borrador, se sacó del
        #    guion: no tenía fuente y la frase se reformuló sin cifra.
        #  · 1.021 y 1.086 se escribirían mal (los números de norma van sin
        #    separador); quedan fuera a propósito para que el gate los cace.
        'cifras_extra': (),
        # La LISTA NEGRA del §5 de la SPEC NO va aquí. `coherencia_cifras()`
        # trata `cifras_ignorar` como una lista de SILENCIADO: lo que se mete
        # ahí deja de saltar el gate. Meter «11.729 pastelerías» o
        # «1,08 M€ de facturación media» en esta clave sería blanquearlas, que
        # es exactamente lo contrario de lo que pide la SPEC. La lista negra
        # entera vive donde de verdad frena al redactor: en `NO_COMUN`, como
        # prohibiciones explícitas que viajan dentro de cada prompt. Se deja
        # vacía a propósito y documentado.
        'cifras_ignorar': (),
        # «la pastelería cierra los domingos», «el obrador cierra en agosto» y
        # «cierra el mes con» son horarios y contabilidad, no mortalidad de
        # negocios. Esta guía NO escribe ninguna cifra de cierre, quiebra ni
        # fracaso (lo prohíbe NO_COMUN), así que cualquier coincidencia del
        # patrón con un número al lado es un defecto, no una excepción.
        'mortalidad_permitida': ['cierra', 'cierran'],
        # Se rellena al FINAL del fichero con `_ERRATAS_OK` (ver el pie): hay
        # que asignarla a GUIA **y a cada bonus por separado**, o el bonus se
        # queda sin ella.
        'erratas_permitidas': (),
        'erratas_forzadas': {},
    },
}

# --------------------------------------------------------------------------
# Los ocho libros del pack (SPEC §2.2). Se referencian por NOMBRE de fichero:
# documentos.py los busca en astro-site/public/dl/<pid>/.
# --------------------------------------------------------------------------
X_CAP = 'capacidad-obrador-y-local.xlsx'                 # libro 1
X_CAPEX = 'calculadora-capex-pasteleria.xlsx'            # libro 2
X_EST = 'estacionalidad-y-picos.xlsx'                    # libro 3
X_CARTA = 'carta-de-apertura-y-escandallo.xlsx'          # libro 4
X_PLAN = 'plan-financiero-3-anos-pasteleria.xlsx'        # libro 5
X_LEGAL = 'checklist-legal-y-licencias.xlsx'             # libro 6
X_EQUIP = 'checklist-equipamiento-y-proveedores.xlsx'    # libro 7
X_TURNOS = 'plantilla-turnos-y-coste-personal.xlsx'      # libro 8

# --------------------------------------------------------------------------
# Pie obligatorio de toda tabla que fije un dato legal. Las URL y las fechas
# son las de la verificación legal independiente del 10-09-2026.
# --------------------------------------------------------------------------
V_1021 = ('Verificado el 10-09-2026 · RD 1021/2022 (BOE-A-2022-21681), '
          'arts. 2, 3, 4, 5, 9, 10, 11, 13, 16, 17, 18 y 20 · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_REG = ('Verificado el 10-09-2026 · RD 191/2011 art. 2.2 en la redacción de la '
         'disposición final primera del RD 1021/2022, y Decreto 26/2026 de la '
         'Comunidad de Madrid (BOCM núm. 73 de 27-03-2026) · '
         'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_VIVIENDA = ('Verificado el 10-09-2026 · RD 1021/2022 art. 13, apartados 2 a '
              '10, y Decreto 13/2025 del Consell (DOGV núm. 10036 de '
              '30-01-2025), que ya ha ejercido la letra e del art. 13.8 · '
              'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_TEMP = ('Verificado el 10-09-2026 · RD 1021/2022, art. 4.1 fila 9 (producto '
          'de pastelería relleno, 4 °C o menos, salvo estable a temperatura '
          'ambiente) y art. 9, apartados 1, 2 y 3 · '
          'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_FORMA = ('Verificado el 10-09-2026 · Reglamento (CE) 852/2004, Anexo II, '
           'Cap. XII, en la redacción del Reglamento (UE) 2021/382, y '
           'RD 1021/2022 art. 20. El RD 202/2000 está derogado por el '
           'RD 109/2010 · '
           'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324')
V_IVA = ('Verificado el 10-09-2026 · Ley 37/1992, arts. 90.Uno, 91.Uno.1.1, '
         '91.Uno.2.2 y 91.Dos.1.1, y Resolución vinculante de la Dirección '
         'General de Tributos de 24-02-2025 (BOE-A-2025-3950) · '
         'https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740')
V_CONV = ('Verificado el 10-09-2026 contra el PDF oficial · Revisión salarial '
          '2026 del Convenio del Sector de Comercio e Industria de Confitería, '
          'Pastelería, Bollería, Repostería, Heladería y Platos Cocinados de la '
          'Comunidad de Madrid (código 28001025011981), BOCM núm. 50 de '
          '28-02-2026 · '
          'https://www.bocm.es/boletin/CM_Orden_BOCM/2026/02/28/BOCM-20260228-2.PDF')


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos, en el anexo y en los
# dos bonus. En este orden: (1) higiene de citación legal, (2) régimen de
# cifras, (3) la LISTA NEGRA íntegra del §5 de la SPEC —que es el §15 del
# research más los añadidos de la refutación y las trece prohibiciones nuevas
# del verificador legal del 10-sep—, (4) el ámbito del producto y la frontera
# con el Kit de Tareas Pastelería, y (5) el vocabulario del §6 y el tono.
# --------------------------------------------------------------------------
NO_COMUN = [
    # ---- 1. Higiene de citación legal ------------------------------------
    'Las letras y apartados de un artículo de ley se escriben «letra e» o '
    '«apartado 4», NUNCA «e)» ni «4)»: un paréntesis de cierre suelto se lee '
    'como una errata.',
    'Los números de las normas se copian TAL CUAL, sin separador de miles: se '
    'escribe «RD 1021/2022», «RD 1086/2020», «RD 1055/2022», «RD 496/2010», '
    '«RD 308/2019», «RD 1007/2023», «RD 193/2023», «RD 126/2015», '
    '«RD 126/2026», «Ley 37/1992», «Ley 7/1996», «Ley 1/2004», «Ley 1/2025», '
    '«Reglamento (CE) 852/2004», «Reglamento (UE) 1169/2011» y '
    '«BOE-A-2022-21681»; nunca «RD 1.021/2022».',
    'TODA afirmación legal va con su norma y su artículo la primera vez que '
    'aparece en el capítulo («el art. 4.1 del RD 1021/2022», «el art. 91.Dos '
    'de la Ley 37/1992»), nunca «es obligatorio» a secas. Y se dice '
    'expresamente «comprobado el 10 de septiembre de 2026», que es la fecha de '
    'corte de esta edición.',
    'NO cites nunca una celda de una hoja de cálculo con la sintaxis de Excel '
    '(«Parámetros!B16», «Cuello de Botella!B8»). Si hay que nombrar de dónde '
    'sale un dato, se nombra el libro y la hoja en lenguaje normal: «la hoja de '
    'cuello de botella de la calculadora de capacidad».',
    # ---- 2. Régimen de cifras --------------------------------------------
    'NO escribas ninguna cifra, porcentaje, temperatura, superficie, potencia, '
    'plazo, umbral, importe ni sanción que no esté en la lista de cifras del '
    'producto o en los datos del sector que te doy. Ni «ronda los», ni «suele '
    'estar en», ni un ejemplo inventado para ilustrar. Si necesitas un número '
    'y no lo tienes, la frase se escribe sin número.',
    'NO hagas cuentas nuevas con las cifras que te doy: no sumes, no restes, no '
    'calcules porcentajes, no conviertas piezas en euros y no proyectes a doce '
    'meses para escribir un total que no te he dado. Los totales ya están '
    'calculados en los libros.',
    'NO cites ninguna encuesta, informe, escuela, consultora ni proveedor de '
    'software que no venga en los datos del sector de este capítulo.',
    # ---- 3. LISTA NEGRA (SPEC §5) ----------------------------------------
    'PROHIBIDO dar un censo de pastelerías de España: ni «11.729», ni ninguna '
    'cifra del código nacional de actividades presentada como «número de '
    'pastelerías». Lo que hay son empresas de un grupo de actividad que mezcla '
    'fabricación industrial y comercio, y así se dice o no se dice.',
    'PROHIBIDO escribir ninguna facturación media por pastelería, ni por '
    'obrador, ni por tienda. En particular está prohibido «1,08 millones de '
    'euros de facturación media» y está prohibido el rango «entre 84.000 y '
    '180.000 euros al año», que salía de multiplicar por doce dos cifras de '
    'PUNTO MUERTO: convierte el suelo de beneficio cero en el techo de '
    'facturación. Si hace falta contraste, se usan sólo las empresas con '
    'nombre que te lleguen en los datos del sector.',
    'PROHIBIDO presentar cualquier cifra de franquicia como dato auditado, y '
    'PROHIBIDO decir que Cientotreinta grados es una franquicia de Oriol '
    'Balaguer o que Manolo Bakes franquicia hoy: ni lo uno ni lo otro es '
    'cierto.',
    'PROHIBIDO dar un precio puntual de cacao: hay cuatro valores distintos '
    'para el mismo año y ninguno es citable. Del cacao y de la mantequilla se '
    'explica CÓMO se modela la volatilidad, no cuánto valen hoy. Y no mezcles '
    'la cotización de la mantequilla a granel con el precio de una mantequilla '
    'de laminado de 82 a 84 por ciento de materia grasa: son dos cosas '
    'distintas.',
    'PROHIBIDO escribir precios de materia prima sin fecha ni formato de '
    'compra, el reparto de canal del total alimentario como si fuera el de '
    'bollería, un ticket medio de pastelería (no existe dato público), un '
    'reparto de ventas por día de la semana, un precio por ración de tarta '
    'tomado de un foro, y los umbrales de potencia o de superficie que '
    'circulan por foros de hace años.',
    'PROHIBIDO dar el escenario de costes de un solo distribuidor como si '
    'fuera el coste general de abrir: entra sólo como «escenario publicado por '
    'un tercero», con esa etiqueta y con su desviación frente al modelo.',
    'PROHIBIDO usar los tres pares de gastos fijos y facturación de equilibrio '
    'que circulan como escenarios de pastelería pequeña, mediana y grande: '
    'implican márgenes incompatibles entre sí y con la regla única de margen '
    'que este mismo producto usa. El punto muerto se calcula con la regla '
    'única, y como contraste sólo vale el par que cuadra con ella.',
    'PROHIBIDO decir que el juego de datos «coincide exactamente con los '
    'cuatro perfiles del kit», y PROHIBIDA la palabra «oficial» como nombre de '
    'un puesto de la plantilla: los perfiles se llaman Jefe Pastelero, '
    'Pastelero, Ayudante y Dependiente Vitrina, y de este último hay dos '
    'personas.',
    'PROHIBIDO hablar de un local de 110 metros cuadrados: el caso modelado '
    'tiene 90, y toda la validación económica está hecha sobre esos 90.',
    'PROHIBIDO afirmar que el mercado de producto sin gluten crece un tanto '
    'por ciento, que Todos los Santos sube la venta un tanto por ciento, o '
    'cualquier variación de mercado que no te llegue en los datos del sector.',
    # ---- 3 bis. Afirmaciones normativas falsas o caducas ------------------
    'PROHIBIDO decir que una pastelería que vende al consumidor final necesita '
    'inscribirse en el Registro General Sanitario de Empresas Alimentarias y '
    'Alimentos. Está EXCLUIDA por el art. 2.2 del RD 191/2011 en la redacción '
    'del RD 1021/2022: lo que hay es una comunicación o declaración '
    'responsable al registro de su comunidad autónoma, y esa comunicación NO '
    'habilita para abrir.',
    'PROHIBIDO escribir «los 500 kilos incluyen el mostrador, así que puedes '
    'pasarte sin hacer un solo suministro a otras tiendas». Es falso por '
    'partida doble: el art. 3 del RD 1021/2022 sólo se activa si suministras a '
    'otros comercios minoristas de distinta titularidad, y los 500 kilos por '
    'semana son una vía ALTERNATIVA al 25 por ciento del volumen anual, no un '
    'techo acumulativo.',
    'PROHIBIDO escribir «la tarta de nata por encargo desde casa no es legal '
    'en España» como afirmación nacional. La forma correcta es: no entra en la '
    'lista del art. 13.8 del RD 1021/2022 SALVO que tu comunidad autónoma la '
    'haya añadido por la vía de la letra e, y hay comunidades que ya han '
    'ejercido esa letra.',
    'PROHIBIDO citar el RD 1254/1991 para el huevo, el RD 3484/2000 para las '
    'temperaturas, el RD 1420/2006 para el anisakis, el RD 202/2000 para el '
    'manipulador y el RD 2207/1995 para la higiene: los cinco están derogados. '
    'Sólo pueden aparecer en el anexo normativo, y dentro de la frase «está '
    'derogado».',
    'PROHIBIDO presentar los 4 °C y los 8 °C como «un conflicto que nadie ha '
    'resuelto». Son DOS TECHOS de dos artículos distintos y manda el más bajo. '
    'Lo que de verdad aprieta del art. 9.3 son las 24 horas de vida útil y la '
    'obligación de registrar fecha y hora de elaboración.',
    'PROHIBIDO hablar del «carnet de manipulador de alimentos» como requisito '
    'legal: no existe desde que el RD 109/2010 derogó el RD 202/2000. Lo que '
    'obliga es que el empresario garantice la formación y pueda acreditarla '
    'con un registro.',
    'PROHIBIDO decir que Verifactu es obligatorio en 2026: las fechas son el 1 '
    'de enero de 2027 para sociedades y el 1 de julio de 2027 para el resto de '
    'obligados. Y PROHIBIDO dar una fecha concreta para el fabricante del '
    'programa: el real decreto habla de un plazo, no de un día.',
    'PROHIBIDO citar el CTE, Documento Básico HS, Sección HS 3, como si '
    'regulase la ventilación de un obrador: su ámbito son las viviendas y los '
    'garajes, y para un local comercial remite al Reglamento de Instalaciones '
    'Térmicas en los Edificios. Las reglas de «boca de expulsión a tres metros '
    'de cualquier toma de aire» son de vivienda y no se citan aquí.',
    'PROHIBIDO decir que el pan especial va al 10 por ciento: desde la '
    'Resolución vinculante de la Dirección General de Tributos de 24-02-2025, '
    'todo lo que regula el RD 308/2019 va al 4 por ciento.',
    'PROHIBIDO decir que una pastelería con obrador necesita dos altas de '
    'actividades económicas, una industrial y otra minorista: la nota del '
    'epígrafe minorista ya faculta para fabricar en el propio establecimiento '
    'si vendes lo que haces en tus propias dependencias.',
    'PROHIBIDO decir que envasar tu producto te obliga a inscribirte en el '
    'registro de productores, y PROHIBIDO decir que no te afecta. Para los '
    'envases de servicio, quien se inscribe es el fabricante o el distribuidor '
    'de esos envases; lo que te toca a ti es exigirle la documentación que '
    'acredita que cumple por ti, y guardarla.',
    'PROHIBIDO decir que aceptar el recipiente del cliente es opcional: lo es '
    'en el RD 1021/2022, pero el art. 9.3 del RD 1055/2022 lo hace obligatorio '
    'para todo establecimiento de alimentación que venda a granel.',
    'PROHIBIDO dar cualquier fecha de una reforma del registro horario '
    'digital: a la fecha de corte de esta edición no hay norma publicada. Como '
    'mucho se dice que hay un proyecto en tramitación y que conviene comprobar '
    'su estado antes de comprar un sistema.',
    'PROHIBIDO escribir «la Ley 1/2025 te obliga a tener un plan de '
    'prevención» y PROHIBIDO escribir «tu pastelería está exenta del artículo '
    '6». Las dos son falsas: la exención por superficie alcanza sólo al '
    'apartado 4, y siguen obligando los apartados 2, 3 y 5.',
    'PROHIBIDO decir que la mención «ELABORACIÓN PROPIA» es obligatoria, y '
    'PROHIBIDO decir que se puede usar si fraccionas o envasas producto de '
    'otro fabricante: es voluntaria y el fraccionamiento no es elaboración.',
    'PROHIBIDO decir que con harina de arroz ya se puede anunciar «sin '
    'gluten»: es un umbral analítico de 20 miligramos por kilo en el producto '
    'tal como se vende.',
    'PROHIBIDO decir que el decreto catalán de artesanía alimentaria prohíbe '
    'llamarse artesano: lo que regula es un sistema de acreditación '
    'voluntario. Y PROHIBIDO decir que existe una definición estatal de '
    '«pastelería artesana»: la norma de calidad que define pastelería, '
    'bollería, confitería y repostería no contiene las palabras «artesano», '
    '«artesanal» ni «casero», comprobado palabra por palabra.',
    'PROHIBIDO decir que una pastelería tiene que pedir permiso para abrir en '
    'domingo, y PROHIBIDO dar «dieciséis domingos» como mínimo: la pastelería '
    'va por el régimen de libertad horaria del art. 5.1 de la Ley 1/2004 '
    'siempre que sea la actividad PRINCIPAL, y ese matiz se escribe.',
    'PROHIBIDO atribuir la regla de los treinta días del precio anterior al '
    'texto refundido de consumidores: está en el art. 20 de la Ley 7/1996, en '
    'la redacción del RD-ley 24/2021.',
    'PROHIBIDO afirmar nada sobre desistimiento de compra online, protección '
    'de datos, seguro de responsabilidad civil, ruido, prevención de riesgos, '
    'clasificación urbanística del obrador, convenios de fuera de Madrid ni '
    'trámite de declaración responsable municipal: nada de eso está verificado '
    'en esta edición. Se trata como pregunta a tu ayuntamiento, a tu asesoría '
    'o a tu servicio de prevención, con la lista de qué preguntar.',
    # ---- 4. Ámbito del producto y frontera con el kit --------------------
    'Esta guía es para quien AÚN NO HA ABIERTO. No escribas nada dirigido a '
    'quien ya está operando todos los días: ni gestión de mermas de vitrina '
    'del día a día, ni ingeniería de carta, ni control diario de producción.',
    'NO emitas ningún plan de producción semanal, ninguna ficha de encargo, '
    'ningún registro de encargos, ninguna matriz de alérgenos de vitrina, '
    'ningún registro de temperaturas y ningún calendario de tareas: todo eso '
    'ya lo entrega el Kit de Tareas Pastelería y aquí se cita por el nombre '
    'del fichero, sin rehacerlo. Lo que construye la guía es la decisión '
    'previa: si el local sirve, cuántas piezas al día permite el equipo que '
    'vas a comprar, cuánto cuesta abrir y qué papeles hacen falta.',
    'NO menciones ninguna otra guía de la línea «Cómo Montar»: ni de '
    'panadería, ni de cafetería, ni de bar, ni de restaurante, ni de food '
    'truck, ni de dark kitchen. Cuando haga falta remitir a otro producto de '
    'la casa, sólo pueden nombrarse el Kit de Tareas Pastelería, el Kit de '
    'Escandallos, el Pack APPCC y la Guía Food Cost y de Ingeniería de Menú.',
    'NO expliques ingeniería de menú ni el método de costeo por lote: eso es '
    'de la Guía Food Cost y de Ingeniería de Menú, y se remite a ella.',
    'NO conviertas esta guía en un recetario: no hay recetas, no hay técnicas '
    'de elaboración y no hay procesos de obrador paso a paso. Los gramajes y '
    'los escandallos que aparecen son datos de ejemplo para que el modelo '
    'tenga qué calcular, y se dice.',
    # ---- 5. Vocabulario y tono -------------------------------------------
    'VOCABULARIO OBLIGATORIO (español de España, con la equivalencia de '
    'Hispanoamérica sólo la PRIMERA vez que aparezca el término en el '
    'capítulo, y después siempre la forma española, sin repetir el '
    'paréntesis): «pastelería (repostería)», «obrador (taller o laboratorio)», '
    '«escandallo (costeo)», «vitrina (exhibidor)», «tarta (pastel o torta)», '
    '«encargo (pedido)», «coste (costo)», «partida».',
    'PROHIBIDA la palabra «dulcería» en cualquier parte del texto: en México '
    'es la tienda de golosinas, no una pastelería. Y se escribe siempre '
    '«artesanal», nunca «artesana».',
    'Usa el vocabulario real de quien va a montar el negocio: se «monta» una '
    'pastelería (no se «abre» sin más), se habla de «la salida de humos» (no '
    'de «evacuación de gases»), de «obrador a puerta cerrada», de «las '
    'licencias preceptivas», de «tartas por encargo», de la «ración» como '
    'unidad de precio de la tarta y de «el ingeniero del ayuntamiento».',
    'TONO: de colega que ya ha montado esto y te lo cuenta, no de consultora. '
    'Prohibido el lenguaje corporativo, prohibidas las introducciones del tipo '
    '«en este capítulo veremos» y prohibidas las conclusiones que resumen lo '
    'ya dicho. Cada párrafo aporta un dato, un procedimiento o una decisión.',
    'PROHIBIDO prometer legalidad o rentabilidad. Nunca escribas «cumple la '
    'normativa», «quedarás cien por cien legal» ni «con esto vas a ganar X». '
    'La fórmula segura es: aquí tienes el mapa normativo con la norma, el '
    'artículo y el enlace, y el modelo con el que calculas tu número.',
    'PROHIBIDO decir que AI Chef Pro tiene plan gratuito: no lo tiene. Si hay '
    'que nombrar la plataforma, se dice «desde 10 euros al mes».',
    'No menciones el proceso de edición ni palabras como «maquetador», '
    '«prompt», «instrucciones», «guion» o «tramo»: el lector compra un libro, '
    'no ve el taller. Tampoco escribas tu propio razonamiento.',
]

# El bonus 2 y el business plan heredan las mismas prohibiciones, más la suya.
NO_COMUN_BONUS = NO_COMUN + [
    'Este documento es un anexo del pack: no repitas la explicación completa '
    'de un capítulo de la guía. Da el caso, la decisión y el número, y remite '
    'al capítulo en una frase.',
]


# --------------------------------------------------------------------------
# Los 20 capítulos + el anexo (SPEC §4).
#
# Cada capítulo declara PRIMERO su `PPE_nn` (epígrafe literal → lista de puntos)
# y luego usa `list(PPE_nn)` como `epigrafes`: así la lista de epígrafes y las
# claves del reparto no pueden discrepar nunca.
# --------------------------------------------------------------------------

PPE_01 = {
    'Las once variantes del negocio, comparadas': [
        'Abrir con el mapa completo: la palabra «pastelería» tapa once '
        'negocios distintos, y la inversión de apertura va desde la del '
        'obrador en casa hasta la del local céntrico o grande. Presentar la '
        'tabla de variantes como lo primero que hay que decidir, antes que el '
        'local y antes que la maquinaria.',
        'Explicar que el caso que recorre todo el documento es la variante '
        'central —obrador propio con despacho a calle, ciudad media española '
        'sin nombre— y que las demás son desviaciones tabuladas sobre ella, '
        'con su coeficiente de obra, de equipamiento, de tienda y de '
        'licencias.',
        'Advertir de que los rangos publicados que aparecen en la tabla son de '
        'terceros y que sólo ocho de las once variantes tienen rango '
        'publicado: las otras tres no lo tienen, y eso se dice en vez de '
        'rellenarlo a ojo.',
    ],
    'Qué incluye este pack y qué es cross-sell': [
        'Listar los ocho libros de Excel por su nombre de fichero y decir en '
        'qué momento de la apertura se usa cada uno: primero capacidad y '
        'local, luego inversión, luego carta y escandallo, luego licencias, '
        'luego personal y por último el plan financiero.',
        'Decir con todas las letras qué NO construye este pack y dónde vive: '
        'el control diario del obrador ya abierto es del Kit de Tareas '
        'Pastelería, los registros de autocontrol son del Pack APPCC, el '
        'escandallo unitario de tres elaboraciones es del Kit de Escandallos y '
        'la ingeniería de carta es de la Guía Food Cost.',
        'Explicar la frontera con una frase que el lector pueda repetir: el '
        'Kit de Tareas te dice qué hacer cada día cuando ya has abierto; esta '
        'guía es todo lo que hay que decidir antes.',
    ],
    'Tu problema, su capítulo y su herramienta': [
        'Presentar el mapa de entrada: el lector no lee el documento de '
        'principio a fin, entra por su problema. Explicar cómo se usa la tabla '
        'de problema a capítulo y a herramienta que viene a continuación.',
        'Señalar las tres puertas de entrada más frecuentes según el perfil: '
        'la de quien ya vende desde casa y quiere legalizarse, la de quien '
        'tiene un local a la vista y no sabe si sirve, y la de quien tiene el '
        'dinero contado y necesita saber si le llega.',
        'Insistir en que los ocho libros comparten el mismo juego de datos, así '
        'que se puede saltar al capítulo que interese sin perder el hilo de '
        'las cifras.',
    ],
    'Lo que NO vas a encontrar aquí': [
        'Decirlo sin adornos: no hay recetas, no hay técnicas de pastelería, no '
        'hay proyecto técnico visado, no hay la ordenanza de tu ayuntamiento y '
        'no hay una promesa de rentabilidad. Y explicar por qué cada una de '
        'esas cuatro ausencias es deliberada.',
        'Explicar el alcance geográfico: el marco normativo es el español y las '
        'cuatro comunidades autónomas que aparecen en los cuadros son '
        'ejemplos. La estructura económica sirve en cualquier país; el marco '
        'sanitario hay que adaptarlo.',
    ],
    'Cómo llamamos aquí a cada cosa': [
        'Fijar el glosario mínimo con la equivalencia de Hispanoamérica en la '
        'primera mención: pastelería y repostería, obrador y taller o '
        'laboratorio, escandallo y costeo, vitrina y exhibidor, tarta y pastel '
        'o torta, encargo y pedido, coste y costo.',
        'Avisar de la palabra más peligrosa del vocabulario: «tarta» se dice '
        'de tres maneras distintas según el país, y en México «torta» es un '
        'bocadillo. Y avisar de que «dulcería» no se usa aquí como sinónimo, '
        'porque en México es la tienda de golosinas.',
    ],
}

PPE_02 = {
    'El consumo en los hogares y la brecha por renta': [
        'Abrir con el volumen y el valor del consumo de bollería y pastelería '
        'en los hogares españoles, con su fuente y su año, y explicar qué '
        'significa para quien va a abrir: hay demanda estable, pero es un '
        'gasto de repetición pequeña, no de ticket alto.',
        'Explicar la brecha por nivel de renta y qué decisión cambia: la plaza '
        'que elijas mueve más el ticket medio que la carta que pongas.',
        'Aterrizarlo en el caso modelado: las ventas anuales sin IVA en '
        'velocidad de crucero, el ticket medio sin IVA y las piezas por '
        'ticket. Recordar que ese ticket lo produce el mix de la carta, no una '
        'media del sector, porque no existe dato público de ticket medio de '
        'pastelería.',
    ],
    'Sólo una parte pequeña del gasto pasa por el comercio especializado': [
        'Dar el reparto de canal del que hay dato, con su fuente, y marcarlo '
        'como lo que es: un dato de fiabilidad limitada que sirve para el '
        'orden de magnitud, no para dimensionar un negocio.',
        'Sacar la consecuencia comercial: la tienda especializada no compite '
        'por la compra semanal de la familia, compite por la ocasión. Eso '
        'explica por qué el fin de semana y las campañas pesan tanto y por qué '
        'el lunes pesa tan poco.',
        'Advertir de que el reparto de canal del total alimentario NO es el '
        'reparto de canal de la bollería, y que confundirlos es uno de los '
        'errores más repetidos de lo que se lee gratis.',
    ],
    'El competidor real es la masa congelada': [
        'Explicar el dato que cambia la conversación: la producción y la '
        'facturación de bollería y pastelería congelada, con su variación, y '
        'la comparación con la serie larga. Quien te quita al cliente de la '
        'mañana no es la pastelería de enfrente, es el punto caliente del '
        'supermercado y el bar que hornea congelado.',
        'Sacar la decisión: contra eso no se compite en precio ni en volumen. '
        'Se compite en producto que no aguanta el proceso industrial, en '
        'encargo y en campaña.',
        'Enlazar con la palanca de escaparate que sí es tuya y que es '
        'gratuita: la mención de elaboración propia, que sólo puede llevarla '
        'quien elabora, con las condiciones que se explican en el capítulo de '
        'canales.',
    ],
    'Por qué el obrador no compite en volumen': [
        'Traducirlo a capacidad: el conjunto de equipos del caso modelado tiene '
        'un techo de piezas al día, y ese techo es lo que hay. La palanca no '
        'es hacer más piezas, es que cada pieza deje más.',
        'Explicar la estacionalidad del año con la tabla mes a mes: el mes más '
        'alto y el mes más bajo del caso modelado, y qué pesa cada uno sobre '
        'el año. Un negocio con esa curva se planifica por tesorería, no por '
        'media mensual.',
        'Cerrar con la decisión de plaza: antes de firmar nada, contar cuántos '
        'obradores con elaboración propia hay en el radio de caminata, y no '
        'cuántas pastelerías aparecen en un buscador, porque ahí entran los '
        'puntos calientes.',
    ],
}

PPE_03 = {
    'Cómo se decide un surtido de apertura': [
        'La tesis del capítulo: un surtido de apertura no se decide por gusto '
        'ni por lo que sabes hacer, se decide por lo que cabe en el obrador, '
        'lo que aguanta en vitrina y lo que deja margen. Los tres filtros, en '
        'ese orden.',
        'Explicar el número de referencias del caso modelado y su reparto en '
        'cinco familias, y por qué abrir con menos referencias de las que '
        'crees que necesitas es casi siempre la decisión correcta el primer '
        'año.',
        'Presentar el semáforo de surtido del libro de la carta: cuántas '
        'referencias salen con veredicto de mantener, cuántas con revisar '
        'precio y cuántas con retirar, y qué hace el lector con cada grupo.',
    ],
    'Las cinco familias y el papel de cada una': [
        'Explicar el papel de cada familia: la bollería trae la mañana y la '
        'repetición, la pastelería individual sube el ticket, las tartas y '
        'entremets son el encargo y la campaña, el pan de acompañamiento es '
        'tráfico y va a otro tipo de IVA, y la temporada es donde se juega el '
        'año.',
        'Advertir de que meter pan cambia dos cosas de golpe: entra otro real '
        'decreto de calidad y entra otro tipo de IVA. Remitir al capítulo '
        'fiscal para el segundo y al anexo normativo para el primero.',
        'Explicar cómo se usa la columna de mix: el porcentaje de unidades de '
        'cada referencia es una celda editable, y el ticket medio y el food '
        'cost de la carta salen de ahí, no de una media del sector.',
    ],
    'Un solo producto puede llevarse casi un tercio de la caja': [
        'Contar el caso documentado de la pastelería en la que una sola '
        'referencia representa cerca de un tercio de las ventas, con su fuente, '
        'y explicar por qué eso no es un accidente: en pastelería la '
        'concentración es la norma.',
        'Sacar la consecuencia operativa: si una referencia se lleva esa parte '
        'de la caja, su escandallo, su proveedor y su capacidad de producción '
        'dejan de ser un detalle y pasan a ser riesgo de negocio.',
        'Explicar la lectura del margen ponderado: no importa el margen de la '
        'referencia, importa el margen multiplicado por su peso en el mix, y '
        'eso es lo que ordena la tabla de decisión de surtido.',
    ],
    'El margen por familia: la galleta rinde el doble que la tarta': [
        'Dar el food cost de materia de la carta completa y el food cost '
        'servido, con la merma y el packaging dentro, y explicar la diferencia '
        'entre los dos: es la primera vez que el lector ve que el escandallo '
        'de la pieza no es el coste del negocio.',
        'Explicar por qué la pieza pequeña y repetitiva suele rendir más que '
        'la tarta: la tarta lleva mucha mano de obra por unidad vendida, y eso '
        'se ve en el capítulo del escandallo.',
        'Cerrar con la regla de decisión: se retira lo que no llega ni a '
        'margen ni a rotación, se revisa el precio de lo que tiene margen bajo '
        'pero rota, y no se toca lo que rota y deja.',
    ],
}

PPE_04 = {
    'Por qué las cifras publicadas se contradicen y qué hipótesis lleva cada una': [
        'Abrir con el problema real: lo que se lee gratis da horquillas de '
        'inversión que se separan por un factor enorme y ninguna declara los '
        'metros, la plaza, si el local viene vacío o traspasado, ni si el '
        'colchón de tesorería está dentro. Sin esas cuatro hipótesis, una '
        'cifra de inversión no significa nada.',
        'Declarar las hipótesis del caso modelado antes de dar ningún número: '
        'los metros del local, el escenario de obra elegido, que el local '
        'viene vacío, y que el fondo de maniobra está dentro del desembolso.',
        'Explicar la validación cruzada como lo que es: el subtotal comparable '
        'del modelo frente al escenario publicado por un tercero para un local '
        'del mismo tamaño, con la desviación escrita. Dos fuentes '
        'independientes en el mismo orden de magnitud, dicho así y no como una '
        'coincidencia.',
    ],
    'Los tres escenarios de obra': [
        'Explicar los tres precios por metro cuadrado de obra civil que trae '
        'la calculadora y qué diferencia real hay entre ellos: el escenario '
        'bajo asume que el local ya tiene instalaciones aprovechables, el alto '
        'asume que hay que hacerlo todo.',
        'Dar la obra civil calculada del escenario medio para el caso modelado '
        'y advertir de que ese número escala con los metros: cambiar la '
        'superficie mueve la partida más grande del presupuesto.',
        'Avisar de lo que NO entra en el precio por metro cuadrado y hay que '
        'presupuestar aparte: el conducto de extracción hasta cubierta, la '
        'subida de potencia eléctrica y la legalización de las instalaciones.',
    ],
    'La columna del IVA, o el CAPEX sale desviado': [
        'Explicar el defecto que arruina cualquier presupuesto casero: unos '
        'distribuidores publican con IVA y otros sin, y sumar las dos cosas en '
        'la misma tabla desvía el total. Por eso cada línea de la calculadora '
        'lleva su columna de si el precio lleva IVA y su tipo.',
        'Dar el CAPEX total sin IVA, el IVA soportado y el desembolso total con '
        'IVA del caso modelado, y explicar que los tres números son distintos '
        'y sirven para cosas distintas: el primero para el balance, el tercero '
        'para la caja.',
        'Advertir de las partidas que no llevan IVA y que la gente mete en el '
        'mismo saco: las tasas municipales y la fianza del arrendamiento.',
    ],
    'El colchón de tesorería es una partida, no una propina': [
        'Explicar el fondo de maniobra como lo que es: los meses de gastos '
        'fijos que puedes pagar sin facturar un euro. Dar el importe calculado '
        'y los meses que cubre en el caso modelado.',
        'Explicar el reparto entre financiación bancaria disponible y '
        'aportación propia necesaria, y por qué el veredicto de la caja es el '
        'primer número que hay que mirar de toda la calculadora.',
        'Cerrar con el orden de decisión: primero se calcula el desembolso con '
        'IVA, después se resta lo que aporta el banco, y sólo entonces se sabe '
        'si el proyecto cabe en el dinero que hay. Al revés se firma un '
        'alquiler que no se puede sostener.',
    ],
}

PPE_05 = {
    'Las siete zonas obligatorias y el principio de marcha adelante': [
        'Enumerar las siete zonas del obrador con sus metros en el caso '
        'modelado y explicar que no son una recomendación de diseño: son las '
        'que exige separar la higiene de proceso, y el proyecto técnico las va '
        'a dibujar igual.',
        'Explicar la marcha adelante en una frase que se entienda: la materia '
        'prima entra por un extremo, el producto terminado sale por el otro y '
        'los caminos no se cruzan. Y explicar el error típico, que es el '
        'residuo pasando por el obrador.',
        'Dar el reparto de metros entre obrador y zona de venta del caso '
        'modelado y explicar la regla de la casa: por debajo de cierta parte '
        'de local dedicada a obrador, el local no sirve por mucho escaparate '
        'que tenga.',
    ],
    'Superficies, encuentros redondeados y lavamanos no manual': [
        'Explicar los requisitos de acabado que aparecen siempre en el informe '
        'sanitario: superficies lisas, lavables e impermeables, encuentros '
        'entre pared y suelo resueltos y lavamanos de accionamiento no manual '
        'en el obrador.',
        'Explicar por qué esto es una decisión de presupuesto y no de gusto: un '
        'local con azulejo roto o con encuentros en ángulo recto se convierte '
        'en obra, y la obra es la partida más grande del capítulo anterior.',
        'Avisar del aseo y vestuario de personal, que es lo que más veces se '
        'olvida al medir un local pequeño y lo que más veces obliga a rehacer '
        'el plano.',
    ],
    'La potencia que piden los hornos y el caudal de la campana': [
        'Dar la potencia sólo de los hornos y la potencia instalada total del '
        'caso modelado, y explicar que la primera cifra es la que descarta '
        'locales: un local con la potencia de un comercio normal no aguanta un '
        'obrador sin ampliación.',
        'Dar el caudal de campana necesario del caso modelado y explicar de '
        'dónde sale la regla de dimensionado, marcándola como criterio de '
        'proyecto y no como norma.',
        'Explicar lo que sí es norma y hay que verificar en el local: el aire '
        'de la campana no se puede recircular ni compartir conducto de '
        'expulsión con el aire del despacho o de los aseos, así que el obrador '
        'necesita su propia salida.',
    ],
    'Altura libre y carga del forjado': [
        'Dar la altura libre mínima que exige la ficha de visita y explicar por '
        'qué: campana, conducto y falso techo se comen una parte que casi '
        'nadie descuenta al mirar el local.',
        'Cerrar con los ítems de la ficha de visita y cuántos de ellos son '
        'eliminatorios: la ficha no puntúa el local, lo descarta. Y explicar '
        'que se imprime y se lleva a cada visita, porque medir de memoria es '
        'como no medir.',
    ],
}

PPE_06 = {
    'El checklist de cribado eliminatorio': [
        'Explicar la lógica del cribado: hay comprobaciones que no admiten '
        'compensación. Un local sin posibilidad de salida de humos hasta '
        'cubierta no se arregla con un buen precio de alquiler.',
        'Dar el número de ítems de la ficha y cuántos son eliminatorios, y '
        'explicar cómo se lee el veredicto cuando quedan pendientes de '
        'comprobar: mientras haya un eliminatorio sin respuesta, el veredicto '
        'es no decidas todavía.',
        'Dar el orden de las visitas: la primera es para descartar, la segunda '
        'es con el instalador o el técnico, y la tercera es para negociar. '
        'Nadie firma en la primera.',
    ],
    'La salida de humos hasta cubierta y la comunidad de propietarios': [
        'Explicar el requisito con el vocabulario del oficio y su base real: la '
        'expulsión tiene que llegar a cubierta, no puede recircular ni '
        'compartir conducto, y la altura sobre la cumbrera la fija la '
        'ordenanza municipal, no el código técnico de edificación.',
        'Explicar el riesgo que tumba más proyectos que la propia norma: los '
        'estatutos de la comunidad de propietarios. Una prohibición '
        'estatutaria inscrita vale más que cualquier informe técnico, y se '
        'pide por escrito antes de firmar.',
        'Dar la lista de lo que se pide y a quién: plano de instalaciones al '
        'propietario, estatutos inscritos y acta a la comunidad, y ficha del '
        'extractor al instalador.',
    ],
    'La pregunta al ayuntamiento antes de firmar': [
        'Explicar que el planeamiento urbanístico decide si en ese local cabe '
        'una actividad con obrador, y que eso NO está en ninguna norma '
        'estatal: se pregunta al ayuntamiento con una consulta de '
        'compatibilidad urbanística, por escrito, y se guarda la respuesta.',
        'Dar el guion literal de la consulta y las tres cosas que hay que '
        'preguntar siempre: si el uso admite elaboración, qué trámite exige el '
        'ayuntamiento para esa actividad y qué exige la ordenanza de humos y '
        'de ruido de ese municipio.',
    ],
    'Las tres puertas: local nuevo, traspaso o franquicia': [
        'Presentar la comparación de traspaso frente a obra nueva del caso '
        'modelado: el precio de traspaso que piden, la renta mensual, el coste '
        'total de cada vía en el horizonte de comparación y la diferencia '
        'entre las dos.',
        'Explicar por qué la comparación correcta no es «precio de traspaso '
        'contra coste de obra», sino «coste total en varios años, con la renta '
        'y con los meses sin facturar dentro». Es el consejo que da un '
        'pastelero con casi cincuenta empleados, y es el hallazgo que no cubre '
        'ninguna guía de la competencia.',
        'Advertir con todas las letras de la naturaleza de los quince '
        'traspasos de la tabla: son precios PEDIDOS en anuncios, no precios '
        'pagados, y sólo cinco publican la renta. Dar el precio pedido medio '
        'como referencia de negociación, nunca como valor de mercado.',
        'Cerrar con la franquicia: existe como tercera puerta, pero las cifras '
        'de inversión que publican las enseñas no son datos auditados y aquí '
        'no se presentan como tales. Lo que sí se puede decir es qué preguntas '
        'hay que hacerle a una enseña antes de firmar.',
    ],
}


CAPITULOS = [
    {
        'n': 1,
        'titulo': 'Qué Negocio Estás Montando: las Once Variantes y Cuál te Toca',
        'resumen_indice': 'las once variantes del nicho comparadas, qué incluye este pack y qué es cross-sell, el mapa de problema a capítulo y a herramienta, y el glosario de España e Hispanoamérica.',
        'palabras': 1700, 'bloques': 1,
        'objetivo': 'Que el lector se sitúe en cinco minutos: cuál de las once '
                    'variantes del negocio está montando de verdad, qué compró '
                    'exactamente, por dónde entrar según su problema y con qué '
                    'libro del pack se resuelve cada cosa. Y que sepa lo que NO '
                    'hay aquí, para que no lo busque.',
        'epigrafes': list(PPE_01),
        'puntos_por_epigrafe': PPE_01,
        'puntos_globales': [
            'Este capítulo fija el vocabulario de todo el documento: es la '
            'PRIMERA mención de «pastelería (repostería)», «obrador (taller o '
            'laboratorio)», «escandallo (costeo)», «vitrina (exhibidor)», '
            '«tarta (pastel o torta)» y «coste (costo)». A partir de aquí se '
            'usa siempre la forma española.',
            'La frontera con el Kit de Tareas Pastelería se dice ARRIBA y en '
            'positivo, no escondida al final: el kit es para cuando ya has '
            'abierto, esta guía es para decidir antes.',
            'Tono de bienvenida sin autobombo: nada de «esta guía definitiva» '
            'ni de promesas. Se enseña el índice y se dice qué hay dentro.',
        ],
        'cifras': [
            C('Inversión de apertura de la variante central, la pastelería mediana con obrador y tienda', f'{X_CAPEX}!Variante del Formato!I15', 'eur'),
            C('Inversión total de esa misma variante, con el fondo de maniobra dentro', f'{X_CAPEX}!Variante del Formato!J15', 'eur'),
            C('Inversión de apertura de la variante de obrador en casa', f'{X_CAPEX}!Variante del Formato!I16', 'eur'),
            C('Inversión de apertura del punto caliente pequeño', f'{X_CAPEX}!Variante del Formato!I20', 'eur'),
            C('Inversión de apertura de la pastelería sin salida de humos', f'{X_CAPEX}!Variante del Formato!I24', 'eur'),
            C('Variantes que tienen rango de inversión publicado por un tercero', f'{X_CAPEX}!Variante del Formato!I26', 'num'),
            C('Superficie total del local del caso modelado', f'{X_CAP}!Parámetros!B14', 'num'),
            C('Metros dedicados a obrador en el caso modelado', f'{X_CAP}!Zonas y m2!D18', 'num'),
        ],
        'sector': ['PS-01', 'PS-02', 'PS-03', 'PS-04', 'PS-05', 'PS-06',
                   'PS-07', 'PS-08', 'PS-09', 'PS-11'],
        'tablas': [
            {
                'titulo': 'Las once variantes del negocio y lo que cuesta abrir cada una (calculadora-capex-pasteleria.xlsx, hoja «Variante del Formato»)',
                'src': (X_CAPEX, 'Variante del Formato'),
                'cols': [('Variante', 'B', 'txt'), ('Id del research', 'C', 'txt'),
                         ('Inversión de apertura (€)', 'I', 'eur'),
                         ('Con fondo de maniobra (€)', 'J', 'eur'),
                         ('Publicado mínimo (€)', 'K', 'eur'),
                         ('Publicado máximo (€)', 'L', 'eur'),
                         ('Qué cambia además', 'N', 'txt')],
                'filas': (15, 24),
                'nota': 'Los coeficientes que producen cada variante son SUPUESTOS del modelo, '
                        'y las dos últimas filas no traen rango publicado porque no existe. Las '
                        'columnas de publicado son de terceros y sirven de contraste, no de '
                        'objetivo.',
            },
            {
                'titulo': 'Tu problema, el capítulo que lo trata y la herramienta que lo resuelve',
                'cabecera': ['Si tu problema es…', 'Capítulo', 'Herramienta del pack'],
                'filas': [
                    ['No sé si este local me sirve', '5 y 6', 'capacidad-obrador-y-local.xlsx'],
                    ['No sé cuántas piezas al día aguanta lo que voy a comprar', '7', 'capacidad-obrador-y-local.xlsx'],
                    ['No sé cuánto cuesta abrir', '4', 'calculadora-capex-pasteleria.xlsx'],
                    ['No sé si me sale mejor un traspaso', '6', 'calculadora-capex-pasteleria.xlsx'],
                    ['No sé qué poner en la carta', '3', 'carta-de-apertura-y-escandallo.xlsx'],
                    ['No sé a cuánto vender ni cuánto me cuesta', '12', 'carta-de-apertura-y-escandallo.xlsx'],
                    ['No sé qué papeles me tocan ni en qué orden', '9 y 10', 'checklist-legal-y-licencias.xlsx'],
                    ['Quiero empezar en casa y no sé si puedo', '9', 'checklist-legal-y-licencias.xlsx'],
                    ['No sé qué maquinaria comprar ni a quién', '8 y 11', 'checklist-equipamiento-y-proveedores.xlsx'],
                    ['No sé cuánta gente necesito ni cuánto cuesta', '13 y 14', 'plantilla-turnos-y-coste-personal.xlsx'],
                    ['No sé si aguanto Reyes', '15', 'estacionalidad-y-picos.xlsx'],
                    ['No sé si el negocio se sostiene', '18 y 19', 'plan-financiero-3-anos-pasteleria.xlsx'],
                    ['No sé cuándo puedo abrir', '20', 'checklist-legal-y-licencias.xlsx'],
                ],
                'nota': 'Los ocho libros comparten el mismo juego de datos, así que puedes '
                        'saltar al capítulo que te interese sin perder el hilo de las cifras.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No prometas cobertura fuera de España: el marco normativo es el '
            'español y así se dice en este mismo capítulo.',
            'No presentes el pack como sustituto de un proyecto técnico '
            'visado, de una asesoría ni de un curso de oficio.',
            'No des una cifra de inversión «de una pastelería» sin decir de '
            'qué variante y con qué metros: es el error de método que este '
            'capítulo viene a corregir.',
        ],
    },
    {
        'n': 2,
        'titulo': 'El Cliente y la Plaza: Quién Compra Pastelería y Cuándo',
        'resumen_indice': 'consumo en los hogares y brecha por renta, el peso real del comercio especializado, el competidor que te quita ventas y la curva del año.',
        'palabras': 1700, 'bloques': 1,
        'objetivo': 'Que el lector entienda contra quién compite de verdad '
                    'antes de elegir plaza y carta, y que vea la curva anual de '
                    'la demanda con números en vez de con intuición.',
        'epigrafes': list(PPE_02),
        'puntos_por_epigrafe': PPE_02,
        'puntos_globales': [
            'Cada cifra de mercado se cita con su fuente y su año dentro del '
            'texto. Las de fiabilidad limitada se presentan como orden de '
            'magnitud, con esa etiqueta.',
            'No hay ninguna cifra de censo de pastelerías ni de facturación '
            'media: no existe dato fiable y el capítulo se escribe sin él.',
            'El capítulo termina en una decisión: qué mirar en la plaza antes '
            'de firmar. No es un informe de mercado, es un criterio de '
            'ubicación.',
        ],
        'cifras': [
            C('Ventas anuales sin IVA del caso modelado en velocidad de crucero', f'{X_EST}!Parámetros!B6', 'eur'),
            C('Ventas del mes más alto del año, enero', f'{X_EST}!Peso sobre el Año!C6', 'eur'),
            C('Ventas del mes más bajo del año, agosto', f'{X_EST}!Peso sobre el Año!C13', 'eur'),
            C('Peso de enero sobre las ventas del año', f'{X_EST}!Peso sobre el Año!D6', 'pct1'),
            C('Peso de agosto sobre las ventas del año', f'{X_EST}!Peso sobre el Año!D13', 'pct1'),
            C('Facturación de un día medio del año', f'{X_EST}!Peso sobre el Año!H24', 'eur'),
            C('Ticket medio sin IVA del caso modelado', f'{X_PLAN}!0. Supuestos!B10', 'eur2'),
            C('Piezas por ticket', f'{X_PLAN}!0. Supuestos!B7', 'num1'),
        ],
        'sector': ['PS-28', 'PS-29', 'PS-33', 'PS-26c', 'PS-26d', 'PS-26f',
                   'PS-26i', 'PS-42'],
        'tablas': [
            {
                'titulo': 'El año mes a mes en el caso modelado (estacionalidad-y-picos.xlsx, hoja «Peso sobre el Año»)',
                'src': (X_EST, 'Peso sobre el Año'),
                'cols': [('Mes', 'A', 'txt'), ('Coeficiente sobre el mes medio', 'B', 'num2'),
                         ('Ventas del mes sin IVA (€)', 'C', 'eur'),
                         ('Parte del año (%)', 'D', 'pct1'),
                         ('Campañas que caen en el mes', 'E', 'txt')],
                'filas': (6, 18),
                'nota': 'Los doce coeficientes son SUPUESTOS del caso modelado y suman doce, '
                        'de manera que la media del año coincide con la velocidad de crucero. '
                        'Cámbialos por los tuyos en cuanto tengas un año cerrado.',
            },
            {
                'titulo': 'Lo que dice el consumo en los hogares, y de dónde sale cada dato',
                'cabecera': ['Qué mide', 'Qué dice el dato', 'Id del research'],
                'filas': [
                    ['Consumo de bollería y pastelería en los hogares', 'Volumen y valor del año, con precio medio por kilo', 'PS-28'],
                    ['Brecha de consumo por nivel de renta', 'La renta alta consume bastante más que la baja, en kilos por persona', 'PS-29'],
                    ['Reparto por canal de venta', 'Dato de fiabilidad limitada: sirve para el orden de magnitud, no para dimensionar', 'PS-33'],
                    ['Producción de bollería y pastelería congelada', 'Producción del año y su variación interanual', 'PS-26c'],
                    ['Facturación del sector de masas congeladas', 'Facturación del año y su variación interanual', 'PS-26d'],
                    ['Variación de la facturación de bollería congelada', 'Crecimiento interanual del canal industrial', 'PS-26f'],
                    ['Serie larga de la producción de pastelería congelada', 'La categoría que más ha crecido de la serie', 'PS-26i'],
                    ['Comparación con el consumo doméstico', 'El congelado industrial crece por encima del consumo en hogares', 'PS-42'],
                ],
                'nota': 'Cada fila se escribe en el texto con su fuente y su año. Ninguna de '
                        'estas cifras es un objetivo para tu negocio: son el tamaño y la '
                        'dirección del mercado en el que vas a entrar.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No des ningún censo de pastelerías de España ni ninguna '
            'facturación media por establecimiento.',
            'No presentes el reparto de canal del total alimentario como si '
            'fuera el reparto de canal de la bollería y la pastelería.',
            'No escribas ningún ticket medio «del sector»: no existe dato '
            'público y el del caso modelado sale del mix de su propia carta.',
        ],
    },
    {
        'n': 3,
        'titulo': 'La Carta de Apertura: Treinta Referencias y por Qué Esas',
        'resumen_indice': 'cómo se decide un surtido de apertura, el papel de cada una de las cinco familias, la concentración de la caja en pocas referencias y el margen por familia.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector decida su surtido de apertura con criterio '
                    'de margen y de capacidad, no por gusto ni por inercia, y '
                    'que sepa qué referencia mantiene, cuál revisa de precio y '
                    'cuál no debería abrir.',
        'epigrafes': list(PPE_03),
        'puntos_por_epigrafe': PPE_03,
        'puntos_globales': [
            'Las treinta referencias del caso modelado son DATOS DE EJEMPLO y '
            'hay que decirlo: tres de ellas están copiadas del Kit de '
            'Escandallos para que un cliente que tenga los dos productos no '
            'vea dos costes distintos del mismo croissant, y las otras son '
            'supuestos.',
            'Esto no es un recetario: no hay gramajes de receta, no hay '
            'procesos y no hay técnica. Lo que se decide aquí es qué se vende '
            'y con qué margen.',
            'La ingeniería de menú NO se explica en este capítulo: se remite a '
            'la Guía Food Cost y de Ingeniería de Menú, que es donde vive.',
        ],
        'cifras': [
            C('Referencias de la carta con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!E39', 'num'),
            C('Referencias con veredicto de revisar precio', f'{X_CARTA}!Decisión de Surtido!E40', 'num'),
            C('Referencias con veredicto de retirar', f'{X_CARTA}!Decisión de Surtido!E41', 'num'),
            C('Margen de contribución medio por pieza de la carta', f'{X_CARTA}!Mix y Ticket Medio!F47', 'eur2'),
            C('Precio de venta medio ponderado con IVA', f'{X_CARTA}!Mix y Ticket Medio!F39', 'eur2'),
            C('Ticket medio con IVA del caso modelado', f'{X_CARTA}!Mix y Ticket Medio!F41', 'eur2'),
            C('Ticket medio sin IVA del caso modelado', f'{X_CARTA}!Mix y Ticket Medio!F42', 'eur2'),
            C('Food cost de materia de la carta completa', f'{X_CARTA}!Mix y Ticket Medio!F44', 'pct1'),
            C('Food cost servido, con la merma y el packaging dentro', f'{X_CARTA}!Mix y Ticket Medio!F45', 'pct1'),
        ],
        'sector': ['PS-43', 'PS-44'],
        'tablas': [
            {
                'titulo': 'Las treinta referencias, su margen y su veredicto de surtido (carta-de-apertura-y-escandallo.xlsx, hoja «Decisión de Surtido»)',
                'src': (X_CARTA, 'Decisión de Surtido'),
                'cols': [('Ref', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Familia', 'C', 'txt'), ('Food cost (%)', 'D', 'pct1'),
                         ('Margen por unidad (€)', 'E', 'eur2'),
                         ('Mix (% de las unidades)', 'F', 'num1'),
                         ('Margen ponderado (€)', 'G', 'eur2'),
                         ('Veredicto', 'J', 'txt')],
                'filas': (6, 35),
                'nota': 'El veredicto cruza margen con rotación: manda el margen PONDERADO por '
                        'el mix, no el margen de la pieza. Los precios de venta y los gramajes '
                        'son datos de ejemplo del caso modelado.',
            },
            {
                'titulo': 'Las cinco familias de la carta de apertura y el papel de cada una',
                'cabecera': ['Familia', 'Referencias', 'Para qué está en la carta'],
                'filas': [
                    ['Bollería', '6', 'Trae la mañana y la compra de repetición; es el tráfico de lunes a viernes'],
                    ['Pastelería individual', '6', 'Sube el ticket sin ocupar más vitrina refrigerada'],
                    ['Tartas y entremets', '6', 'Es el encargo, la celebración y la campaña: ticket alto y mano de obra alta'],
                    ['Panes de acompañamiento', '4', 'Tráfico y compra diaria; ojo, entra otra norma de calidad y otro tipo de IVA'],
                    ['Temporada', '8', 'Donde se juega el año: Reyes, Semana Santa y Todos los Santos'],
                ],
                'nota': 'El reparto es el del caso modelado. Abrir con menos referencias de las '
                        'que crees que necesitas es casi siempre la decisión correcta el primer '
                        'año: cada referencia añade compra, merma y espacio de vitrina.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No des ningún ticket medio de pastelería tomado de fuera: no '
            'existe dato público y el del caso modelado sale de su propio mix.',
            'No presentes los treinta escandallos como recetas: son datos de '
            'ejemplo y hay que decirlo en el capítulo.',
            'No expliques la matriz de ingeniería de menú: pertenece a otra '
            'guía del catálogo y aquí sólo se remite a ella.',
        ],
    },
    {
        'n': 4,
        'titulo': 'Cuánto Cuesta Abrir: el CAPEX Real, Partida a Partida',
        'resumen_indice': 'por qué las cifras publicadas se contradicen, los tres escenarios de obra, la columna del IVA que descuadra cualquier presupuesto y el colchón de tesorería como partida.',
        'palabras': 1800, 'bloques': 1,
        'objetivo': 'Que el lector sustituya la horquilla que ha leído por su '
                    'propio modelo: sus metros, su escenario de obra, sus '
                    'precios con y sin IVA y su colchón de tesorería, y que '
                    'sepa cuánta aportación propia necesita antes de firmar '
                    'nada.',
        'epigrafes': list(PPE_04),
        'puntos_por_epigrafe': PPE_04,
        'puntos_globales': [
            'La tesis del capítulo es de método: no se da un número de '
            'inversión, se da el modelo que produce el número del lector, con '
            'la hipótesis declarada.',
            'Toda cifra de equipamiento que aparezca lleva pegado si el precio '
            'es con IVA o sin IVA. Mezclar las dos bases en la misma tabla es '
            'el defecto que este capítulo denuncia.',
            'Las partidas que el modelo trae como supuesto se dicen supuestas, '
            'una a una: no se disfrazan de precio de mercado.',
        ],
        'cifras': [
            C('CAPEX total sin IVA del caso modelado', f'{X_CAPEX}!CAPEX por Bloque!K47', 'eur'),
            C('IVA soportado total de la inversión', f'{X_CAPEX}!CAPEX por Bloque!L47', 'eur'),
            C('Desembolso total con IVA', f'{X_CAPEX}!CAPEX por Bloque!M47', 'eur'),
            C('Precio por metro cuadrado del escenario de obra bajo', f'{X_CAPEX}!Parámetros!B7', 'eur'),
            C('Precio por metro cuadrado del escenario de obra alto', f'{X_CAPEX}!Parámetros!B9', 'eur'),
            C('Obra civil calculada en el escenario medio', f'{X_CAPEX}!Parámetros!B12', 'eur'),
            C('Fondo de maniobra calculado', f'{X_CAPEX}!Parámetros!B19', 'eur'),
            C('Meses de gastos fijos que cubre ese fondo', f'{X_CAPEX}!IVA y Tesorería!B27', 'num'),
            C('Subtotal comparable con el escenario publicado por un tercero', f'{X_CAPEX}!CAPEX por Bloque!K51', 'eur'),
            C('Desviación del modelo sobre ese escenario publicado', f'{X_CAPEX}!CAPEX por Bloque!K53', 'pct1'),
        ],
        'sector': ['PS-85a', 'PS-85b', 'PS-85c', 'PS-85e', 'PS-85f', 'PS-85g',
                   'PS-85h', 'PS-49', 'PS-50', 'PS-05'],
        'tablas': [
            {
                'titulo': 'El CAPEX por bloque del caso modelado (calculadora-capex-pasteleria.xlsx, hoja «CAPEX por Bloque»)',
                'src': (X_CAPEX, 'CAPEX por Bloque'),
                'cols': [('Bloque', 'C', 'txt'), ('Base sin IVA (€)', 'K', 'eur'),
                         ('IVA soportado (€)', 'L', 'eur'),
                         ('Total con IVA (€)', 'M', 'eur'),
                         ('Parte del total (%)', 'N', 'pct1')],
                'filas': (39, 47),
                'nota': 'La fianza, las tasas municipales y el fondo de maniobra no llevan IVA, '
                        'y por eso su columna de IVA sale a cero. El fondo de maniobra no es '
                        'una compra: es la caja que te permite pagar los fijos hasta que '
                        'factures.',
            },
            {
                'titulo': 'La inversión línea a línea, con su base fiscal y su procedencia (calculadora-capex-pasteleria.xlsx, hoja «CAPEX por Bloque»)',
                'src': (X_CAPEX, 'CAPEX por Bloque'),
                'cols': [('Bloque', 'B', 'txt'), ('Partida', 'C', 'txt'),
                         ('¿La compras?', 'D', 'txt'),
                         ('Procedencia', 'E', 'txt'),
                         ('¿El precio lleva IVA?', 'F', 'txt'),
                         ('Tu importe (€)', 'J', 'eur'),
                         ('Base sin IVA (€)', 'K', 'eur'),
                         ('Total con IVA (€)', 'M', 'eur')],
                'filas': (6, 36),
                'nota': 'Las líneas marcadas como supuesto NO son precios de ficha de '
                        'distribuidor: son valores por defecto para que el modelo funcione, y '
                        'hay que sustituirlos por los tres presupuestos que pidas. Las que '
                        'vienen con «no» en la columna de si la compras quedan fuera del total '
                        'a propósito.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No presentes el escenario de costes publicado por un distribuidor '
            'como el coste general de abrir una pastelería: entra sólo como '
            'escenario publicado por un tercero, con su desviación escrita.',
            'No mezcles importes con IVA y sin IVA en la misma suma, ni '
            'siquiera para redondear un total.',
            'No des un precio de horno, de abatidor ni de cámara en este '
            'capítulo sin decir de qué línea de la calculadora sale: los '
            'precios con marca y modelo se trabajan en el capítulo de '
            'maquinaria.',
            'No cites ningún descuento de campaña de un distribuidor sin '
            'decir que caduca y que hay que fecharlo.',
        ],
    },
    {
        'n': 5,
        'titulo': 'El Local: Metros, Zonas y la Ficha de Visita',
        'resumen_indice': 'las siete zonas obligatorias y la marcha adelante, los acabados que pide sanidad, la potencia y el caudal de campana, y la altura libre.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector sepa exactamente qué mirar y qué medir antes '
                    'de enamorarse de un local, y que salga del capítulo con la '
                    'ficha de visita impresa y con los cuatro números que '
                    'descartan un local en la primera vuelta.',
        'epigrafes': list(PPE_05),
        'puntos_por_epigrafe': PPE_05,
        'puntos_globales': [
            'Todo lo que sea competencia municipal —la altura de la chimenea '
            'sobre la cumbrera, el ruido, el planeamiento— se escribe como '
            'pregunta al ayuntamiento, nunca como umbral.',
            'Las reglas de dimensionado que no son norma se etiquetan como '
            'criterio de proyecto: el lector tiene que poder distinguir lo que '
            'le obliga de lo que le recomendamos.',
            'El capítulo se cierra siempre en la misma acción: imprimir la '
            'ficha de visita y llevarla al local. Es el entregable del '
            'capítulo.',
        ],
        'cifras': [
            C('Superficie total del local del caso modelado', f'{X_CAP}!Parámetros!B14', 'num'),
            C('Metros de obrador', f'{X_CAP}!Zonas y m2!D18', 'num'),
            C('Parte del local dedicada a obrador', f'{X_CAP}!Zonas y m2!D19', 'pct0'),
            C('Metros de zona de venta', f'{X_CAP}!Zonas y m2!D20', 'num'),
            C('Potencia sólo de los hornos', f'{X_CAP}!Parámetros!B16', 'num'),
            C('Potencia instalada total del obrador', f'{X_CAP}!Parámetros!B17', 'num'),
            C('Caudal de campana necesario', f'{X_CAP}!Parámetros!B21', 'num'),
            C('Altura libre mínima que exige la ficha de visita', f'{X_CAP}!Parámetros!B22', 'num1'),
            C('Ítems de la ficha de visita a local', f'{X_CAP}!Ficha de Visita a Local!E25', 'num'),
            C('De ellos, cuántos son eliminatorios', f'{X_CAP}!Ficha de Visita a Local!E26', 'num'),
        ],
        'sector': ['PS-86a', 'PS-86b', 'PS-86c', 'PS-86d', 'PS-86e'],
        'tablas': [
            {
                'titulo': 'Las siete zonas del obrador, sus metros y lo que tiene que cumplir cada una (capacidad-obrador-y-local.xlsx, hoja «Zonas y m2»)',
                'src': (X_CAP, 'Zonas y m2'),
                'cols': [('Nº', 'A', 'num'), ('Zona', 'B', 'txt'),
                         ('Bloque', 'C', 'txt'), ('Metros cuadrados', 'D', 'num'),
                         ('Parte del local (%)', 'E', 'pct1'),
                         ('Paso del recorrido', 'F', 'num'),
                         ('Qué tiene que cumplir', 'G', 'txt')],
                'filas': (6, 12),
                'nota': V_1021 + ' — la columna del paso del recorrido es la que comprueba la '
                        'marcha adelante: la materia prima entra por el paso uno y el residuo '
                        'sale por el último, sin cruzarse con el producto terminado.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No cites los umbrales de potencia ni de superficie mínima que '
            'circulan por foros de hace años: no tienen fuente y no son norma.',
            'No cites el Documento Básico HS del código técnico como si '
            'regulase la ventilación del obrador.',
            'No des una superficie mínima legal para abrir una pastelería: no '
            'existe como umbral estatal, y lo que manda es que quepan las '
            'zonas con marcha adelante.',
        ],
    },
    {
        'n': 6,
        'titulo': 'Antes de Firmar el Alquiler: el Capítulo que Ahorra el Dinero',
        'resumen_indice': 'el cribado eliminatorio, la salida de humos y la comunidad de propietarios, la consulta al ayuntamiento y la comparación entre local nuevo, traspaso y franquicia.',
        'palabras': 1800, 'bloques': 1,
        'objetivo': 'Que el lector no firme un local imposible. Darle el orden '
                    'de comprobaciones, el guion literal de lo que hay que '
                    'preguntar y por escrito a quién, y la comparación '
                    'económica entre traspaso y obra nueva a varios años.',
        'epigrafes': list(PPE_06),
        'puntos_por_epigrafe': PPE_06,
        'puntos_globales': [
            'Este capítulo se escribe en imperativo y en orden: es una '
            'secuencia de comprobaciones, no un ensayo. Cada apartado termina '
            'en qué se pide, a quién y por escrito.',
            'Todo lo municipal va como pregunta, con el guion de la consulta, '
            'y nunca como requisito general: la ordenanza cambia en cada uno '
            'de los municipios de España.',
            'Las cifras de traspaso son precios PEDIDOS en anuncios, no '
            'precios pagados, y eso se repite cada vez que aparecen.',
        ],
        'cifras': [
            C('Ítems eliminatorios de la ficha de visita', f'{X_CAP}!Ficha de Visita a Local!E26', 'num'),
            C('Motivos de descarte del local en el caso modelado', f'{X_CAP}!Ficha de Visita a Local!E27', 'num'),
            C('Puntos pendientes de comprobar', f'{X_CAP}!Ficha de Visita a Local!E29', 'num'),
            C('Precio de traspaso que piden por el local del caso modelado', f'{X_CAPEX}!Traspaso vs Obra Nueva!C6', 'eur'),
            C('Renta mensual de ese local traspasado', f'{X_CAPEX}!Traspaso vs Obra Nueva!C8', 'eur'),
            C('Coste total del traspaso en el horizonte de comparación', f'{X_CAPEX}!Traspaso vs Obra Nueva!C19', 'eur'),
            C('Coste total de la obra nueva en el mismo horizonte', f'{X_CAPEX}!Traspaso vs Obra Nueva!C20', 'eur'),
            C('Diferencia entre las dos vías', f'{X_CAPEX}!Traspaso vs Obra Nueva!C21', 'eur'),
            C('Precio pedido medio de los quince traspasos censados', f'{X_CAPEX}!Traspaso vs Obra Nueva!D44', 'eur'),
            C('De esos quince, cuántos publican la renta', f'{X_CAPEX}!Traspaso vs Obra Nueva!D41', 'num'),
        ],
        'sector': ['PS-69', 'PS-70', 'PS-08', 'PS-103', 'PA-07', 'PA-07b'],
        'tablas': [
            {
                'titulo': 'La ficha de visita a local, punto por punto (capacidad-obrador-y-local.xlsx, hoja «Ficha de Visita a Local»)',
                'src': (X_CAP, 'Ficha de Visita a Local'),
                'cols': [('Nº', 'A', 'num'), ('Qué se comprueba', 'B', 'txt'),
                         ('¿Eliminatorio?', 'C', 'txt'),
                         ('Cómo se comprueba', 'D', 'txt'),
                         ('Veredicto en el caso modelado', 'I', 'txt')],
                'filas': (6, 23),
                'nota': 'Mientras quede un solo ítem eliminatorio sin respuesta, el veredicto '
                        'del local es «no decidas todavía». La ficha no puntúa: descarta.',
            },
            {
                'titulo': 'Traspaso contra obra nueva en el horizonte de comparación (calculadora-capex-pasteleria.xlsx, hoja «Traspaso vs Obra Nueva»)',
                'src': (X_CAPEX, 'Traspaso vs Obra Nueva'),
                'cols': [('Concepto', 'A', 'txt'), ('Importe (€)', 'C', 'eur')],
                'filas': (15, 21),
                'nota': 'La comparación correcta no es «precio de traspaso contra coste de '
                        'obra»: es el coste total a varios años, con la renta pagada y con los '
                        'meses sin facturar dentro. Los meses de obra sin facturar son un '
                        'supuesto del modelo.',
            },
            {
                'titulo': 'Quince traspasos reales, para calibrar lo que te piden (calculadora-capex-pasteleria.xlsx, hoja «Traspaso vs Obra Nueva»)',
                'src': (X_CAPEX, 'Traspaso vs Obra Nueva'),
                'cols': [('Ciudad o zona', 'A', 'txt'), ('Tipo de negocio', 'B', 'txt'),
                         ('Metros cuadrados', 'C', 'num'),
                         ('Precio pedido (€)', 'D', 'eur'),
                         ('Renta mensual (€)', 'E', 'eur'),
                         ('Euros por metro cuadrado', 'F', 'eur'),
                         ('Fuente', 'H', 'txt')],
                'filas': (26, 40),
                'nota': 'Son precios PEDIDOS en anuncios, no precios pagados, y sólo cinco de '
                        'los quince publican la renta. Sirven para negociar, nunca como valor '
                        'de mercado. Y ninguno dice por qué se traspasa el negocio: esa es la '
                        'primera pregunta.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No presentes ninguna cifra de inversión de franquicia como dato '
            'auditado, y no digas que una enseña franquicia si no lo hace hoy.',
            'No afirmes nada sobre la clasificación urbanística de un obrador: '
            'no está verificado y va como consulta al ayuntamiento.',
            'No conviertas los precios pedidos de los traspasos en un precio '
            'de mercado ni en una media del sector.',
        ],
    },
]


PPE_07 = {
    'Por qué la pastelería gira sobre el frío negativo y no sobre el horno': [
        'La tesis del capítulo: en una pastelería el horno casi nunca es el '
        'cuello de botella. Lo que manda el ritmo es el frío, y dentro del '
        'frío, el abatidor y la cámara de fermentación controlada.',
        'Explicar por qué: el frío es lo que permite desacoplar la producción '
        'de la venta, hacer de noche lo que se vende de día y sostener una '
        'campaña sin doblar la plantilla.',
        'Dar la cifra que lo demuestra en el caso modelado: cuál es el equipo '
        'que limita y cuántas piezas al día permite frente a las que quiere '
        'sacar el negocio.',
    ],
    'Abatidor, cámara de fermentación controlada y congelación de entremets': [
        'Explicar qué hace cada uno de los tres equipos en el flujo real de un '
        'obrador de pastelería, sin entrar en técnica de elaboración: el '
        'abatidor baja la temperatura del centro deprisa, la cámara de '
        'fermentación te devuelve el control del horario y la congelación de '
        'entremets es lo que hace posible una campaña.',
        'Dar la parte del surtido que pasa por el abatidor en el caso modelado '
        'y las piezas al día que permite cada uno de los tres equipos, para '
        'que el lector vea de dónde sale el techo.',
        'Explicar la decisión de compra que sale de aquí: el abatidor es la '
        'compra más cara del obrador y la que más veces se pospone, y '
        'posponerla tiene un coste de capacidad que se puede calcular.',
    ],
    'Un arcón doméstico no es un abatidor': [
        'Explicar la diferencia con la norma en la mano: la congelación exige '
        'alcanzar los grados bajo cero en el centro del producto con un '
        'descenso ininterrumpido, y sólo se puede congelar en un arcón o '
        'cámara de mantenimiento si se garantiza que cumple eso.',
        'Explicar la consecuencia documental: hay que etiquetar con la fecha '
        'de elaboración, la de congelación y la de caducidad o consumo '
        'preferente, y el registro de congelación se puede sustituir por la '
        'etiqueta si la etiqueta lleva toda esa información.',
        'Cerrar con lo que no se puede hacer: recongelar lo descongelado, '
        'salvo transformación posterior; y vender como fresco lo que se '
        'vendió descongelado, que tiene que ir acompañado de esa palabra.',
    ],
    'Capacidad por equipo y cuál te limita': [
        'Explicar cómo se calcula la capacidad de cada equipo: piezas por '
        'ciclo, minutos por ciclo, ciclos al día y parte del surtido que pasa '
        'por él. Y por qué un equipo por el que sólo pasa una parte del '
        'surtido rinde más piezas de obrador de las que hace por sí mismo.',
        'Dar los minutos productivos disponibles al día del caso modelado y '
        'explicar de dónde salen: no son las horas de turno, son las horas de '
        'turno por la parte de la jornada que de verdad se pasa produciendo.',
        'Sacar la decisión de compra: si el equipo que limita es el que estás '
        'a punto de comprar en su versión pequeña, el ahorro de hoy es el '
        'techo de facturación de los próximos años. Remitir al capítulo de las '
        'campañas para ver ese techo cuando llega Reyes.',
    ],
}

PPE_08 = {
    'Precios reales por gama, con marca y modelo': [
        'Presentar la dotación completa del caso modelado con marca, modelo y '
        'precio de referencia, y separar con claridad las líneas que tienen '
        'precio publicado por un distribuidor de las que son supuesto del '
        'modelo.',
        'Dar el total de referencia sin IVA de las líneas críticas y el de '
        'toda la dotación, y explicar la diferencia: lo crítico es lo que hace '
        'falta para poder abrir, y lo demás puede esperar.',
        'Explicar qué se compra el día uno, qué se alquila o se renegocia y '
        'qué se puede esperar a tener sin que la carta se resienta.',
        'Advertir de que ninguna de estas cifras es una cotización: son '
        'precios de ficha o supuestos, y hay que pedir tres presupuestos por '
        'línea crítica.',
    ],
    'La trampa del IVA: unos distribuidores publican con y otros sin': [
        'Explicar el defecto concreto: el mismo listado puede mezclar precios '
        'con y sin IVA, y hay fichas que ni siquiera lo declaran. Por eso la '
        'hoja lleva una columna que dice de cada línea si su precio lleva IVA '
        'o no, y una tercera opción para cuando el distribuidor no lo dice.',
        'Dar el IVA soportado sobre el equipamiento y el desembolso real con '
        'IVA del caso modelado, y explicar que el segundo es el que sale de la '
        'cuenta corriente aunque el primero se recupere después.',
        'Dar la regla de negociación: se compara siempre base sin IVA contra '
        'base sin IVA, y se pide el presupuesto desglosado.',
    ],
    'Sin salida de humos como ventaja de negocio': [
        'Explicar la variante sin salida de humos como decisión de negocio y '
        'no como detalle técnico: cambia el abanico de locales que puedes '
        'mirar y el precio del alquiler al que puedes acceder, y cambia la '
        'inversión de referencia del equipamiento.',
        'Dar la inversión de referencia de esa variante frente a la del caso '
        'base y explicar qué se pierde por el camino en producto y en '
        'capacidad.',
    ],
    'Segunda mano y plazos de entrega que mueven la apertura': [
        'Explicar el criterio de la segunda mano: dónde tiene sentido y dónde '
        'no, y qué hay que pedir siempre —factura, historial de mantenimiento '
        'y, si es de gas, el certificado de la instalación—.',
        'Dar el plazo crítico de entrega del caso modelado, la línea que lo '
        'marca y el margen que queda hasta la apertura prevista, y explicar '
        'que ese número no es logística: es la fecha de apertura.',
        'Cerrar con la regla operativa: el equipamiento se pide en cuanto hay '
        'licencia y proyecto, no cuando acaba la obra, porque va en paralelo. '
        'Remitir al capítulo del cronograma.',
    ],
}

PPE_09 = {
    'El registro que te toca: comunicación autonómica, no registro general': [
        'Corregir el error número uno del nicho con la norma en la mano: una '
        'pastelería que vende al consumidor final está EXCLUIDA del Registro '
        'General Sanitario de Empresas Alimentarias y Alimentos por el art. '
        '2.2 del RD 191/2011 en la redacción de la disposición final primera '
        'del RD 1021/2022.',
        'Explicar qué hay en su lugar: inscripción en el registro de tu '
        'comunidad autónoma mediante comunicación —o declaración responsable '
        'si elaboras en vivienda— que, en los términos de la propia norma, NO '
        'es habilitante.',
        'Explicar qué significa «no habilitante» en la práctica y por qué no '
        'es una buena noticia: no te da permiso para abrir, así que el permiso '
        'viene de otro sitio, que es la licencia o la declaración responsable '
        'de actividad de tu ayuntamiento.',
        'Dar el número de trámites del expediente completo del caso modelado y '
        'cuántos de ellos cambian según la comunidad autónoma, y remitir a la '
        'hoja de trámites del libro de licencias.',
    ],
    'Cuándo sí vuelve el registro general: la puerta de entrada y las tres condiciones': [
        'Poner la PUERTA DE ENTRADA delante de todo lo demás: el art. 3 del RD '
        '1021/2022 sólo se activa si suministras alimentos de producción '
        'propia a establecimientos de comercio al por menor DE DISTINTA '
        'TITULARIDAD. Si sólo despachas a tu clientela, nada de este apartado '
        'te aplica.',
        'Explicar que, si entras, las tres condiciones son ACUMULATIVAS: '
        'marginal Y localizado Y restringido, y que basta con fallar una para '
        'perderlas todas.',
        'Explicar que dentro de «marginal» hay DOS VÍAS ALTERNATIVAS y basta '
        'con cumplir una: o el suministro a otros minoristas no pasa del '
        'umbral sobre el volumen anual, o el total comercializado a la semana '
        '—incluyendo el mostrador— no pasa del tope en kilos. Un obrador que '
        'despacha mucho sigue siendo marginal si su suministro a otras tiendas '
        'no llega al umbral porcentual.',
        'Explicar «localizado» con su radio entre comunidades autónomas y su '
        'condición de que los registros autonómicos sean públicos y '
        'consultables; y «restringido», que es el que más fácil se rompe: '
        'basta con servir a un solo cliente inscrito en el registro general '
        'para perderlo. Y añadir la obligación documental que va con ello: '
        'declaración responsable y registro de a quién, cuánto y cuándo.',
    ],
    'Central y sucursales: una unidad comercial, pero cada una se inscribe aparte': [
        'Dar la palanca de crecimiento que casi ninguna fuente explica: el '
        'obrador central y sus sucursales de la misma titularidad son una '
        'única unidad comercial, y lo que va del obrador a tus despachos NO '
        'cuenta como suministro entre minoristas.',
        'Pegarle inmediatamente la obligación, que es la parte que nadie '
        'cuenta: cada sucursal se inscribe en el registro autonómico de manera '
        'independiente. Y recordar las tres condiciones del esquema: misma '
        'titularidad, mismo municipio o zona de salud, y obrador cerrado al '
        'público.',
    ],
    'Cuatro comunidades de ejemplo, y cómo encontrar la tuya': [
        'Declarar el alcance antes de dar ningún dato: aquí hay cuatro '
        'comunidades autónomas como EJEMPLO, no las diecisiete, porque las '
        'comunidades se están adaptando ahora mismo y un cuadro completo '
        'caducaría en meses.',
        'Contar el caso de Madrid con su fecha: el decreto que crea el '
        'registro de minoristas, que la comunicación se presenta al mismo '
        'tiempo que se inicia la actividad y no antes, que no habilita, y que '
        'quien ya estaba abierto tiene un período transitorio de un año.',
        'Dar el método para encontrar el decreto de cualquier comunidad en '
        'cinco minutos, con los términos exactos de búsqueda y con la ficha de '
        'vigencia del boletín oficial correspondiente, y advertir de que el '
        'trámite puede llevar tasa en unas comunidades y no en otras.',
    ],
    'La ruta doméstica y la lista blanca de cinco letras': [
        'Explicar el régimen de la vivienda: las zonas de la casa dedicadas a '
        'la actividad pasan a tener consideración de establecimiento de '
        'comercio al por menor, con declaración responsable que incluye '
        'horario, productos y plano.',
        'Publicar la lista blanca del art. 13.8 con sus CINCO letras, la '
        'quinta incluida: otros alimentos que las autoridades competentes de '
        'las comunidades autónomas permitan en sus territorios. Y explicar la '
        'consecuencia: por defecto sólo entra la repostería estable a '
        'temperatura ambiente, y una tarta rellena de nata no entra SALVO que '
        'tu comunidad la haya añadido por esa quinta letra.',
        'Dar la prueba de que esa quinta letra se usa: una comunidad ya la ha '
        'ejercido y ha ampliado la lista, la venta en el propio domicilio y el '
        'territorio de reparto; y decir con la misma claridad lo que NO ha '
        'ampliado, que es la refrigeración.',
        'Poner las cinco prohibiciones del art. 13.5 en su sitio: sólo la de '
        'suministrar a colectividades y en eventos es incondicional; las de '
        'consumo en el sitio, venta en el propio establecimiento y suministro '
        'a otras tiendas llevan cláusula de escape autonómica; y la de '
        'congelar no admite salvedad, aunque sí se puede mantener en '
        'congelación la materia prima que se compre ya congelada.',
        'Cerrar con los TRES límites del art. 13.9, no uno: proporcionalidad '
        'con el tamaño de las instalaciones, tope de kilos a la semana y '
        'obligación de demostrarlo documentalmente. Dar los metros útiles y '
        'los kilos del ejemplo y su relación por metro cuadrado, y advertir de '
        'que el tope de kilos casi nunca se alcanza en una cocina doméstica: '
        'el que se incumple es el de proporcionalidad, y el que te pide un '
        'inspector es el tercero. Y la etiqueta obligatoria, con la mención de '
        'elaborado en vivienda particular y la fecha de elaboración.',
    ],
}

PPE_10 = {
    'El plan de autocontrol simplificado es legal, y necesita una persona responsable con nombre': [
        'Dar la buena noticia con su artículo: el procedimiento permanente '
        'basado en los principios del análisis de peligros y puntos de control '
        'crítico se puede aplicar DE MANERA SIMPLIFICADA en el comercio '
        'minorista, y el propio artículo remite a la comunicación de la '
        'Comisión que lo desarrolla.',
        'Dar la condición que casi nadie cumple: hay que designar una persona '
        'responsable de su aplicación, con nombre y apellidos, y esa '
        'designación tiene que estar escrita.',
        'Aclarar el estatus de las guías sectoriales: son VOLUNTARIAS, ayudan '
        'y no obligan, y usar una no exime de tener tu propio plan.',
        'Dar el coste previsto del plan en el caso modelado y el número de '
        'trámites de la fase de sanidad, autocontrol y formación, y remitir al '
        'Pack APPCC para los registros del día a día, que esta guía no rehace.',
    ],
    'El carnet de manipulador no existe: lo que hace falta es un registro de formación': [
        'Desmontarlo con las dos piezas: el real decreto que exigía el carnet '
        'está derogado desde hace años, y el real decreto de higiene del '
        'minorista no tiene ni un artículo sobre formación de manipuladores.',
        'Explicar qué sí obliga: el reglamento europeo de higiene pide que los '
        'manipuladores estén supervisados e instruidos o formados de acuerdo '
        'con su actividad laboral, y la obligación es del empresario.',
        'Traducirlo a entregable: lo que te pide una inspección es un REGISTRO '
        'de formación por persona, con contenido, horas y fecha. Un '
        'certificado de curso sirve como evidencia; el carnet plastificado no '
        'es el requisito.',
        'Dar las personas con formación registrada del caso modelado, las '
        'formaciones caducadas y la validez que se da la casa a cada '
        'formación, y aclarar que esa validez es un criterio propio, no un '
        'plazo legal.',
    ],
    'Alérgenos de obrador frente a alérgenos de vitrina': [
        'Separar las dos cosas de una vez: en vitrina hay una obligación de '
        'INFORMACIÓN al consumidor; en el obrador hay una obligación de '
        'PRODUCCIÓN, que es no usar el equipo, los recipientes ni las '
        'superficies de un alérgeno con otros alimentos si no se han limpiado.',
        'Dar el régimen de la vitrina con precisión: los alérgenos son '
        'obligatorios siempre y se pueden dar de palabra, pero sólo si la '
        'información está por escrito en el establecimiento, accesible al '
        'personal, a la inspección y a quien la pida, con cartel visible en '
        'cada sección diciendo dónde está, y todo al menos en castellano.',
        'Explicar qué construye esta guía y qué no: la matriz de alérgenos de '
        'OBRADOR, que cruza materias primas por alérgenos y por orden de '
        'elaboración, es nuestra; la declaración de vitrina, plato a plato, la '
        'entrega el Kit de Tareas Pastelería y no se duplica aquí. Nunca dos '
        'declaraciones completas de alérgenos en el mismo catálogo.',
        'Dar el número de referencias de la carta que necesitan vitrina '
        'refrigerada y explicar por qué esa frontera —relleno frente a estable '
        'a temperatura ambiente— es la que decide el mueble que compras y el '
        'orden de elaboración del obrador.',
    ],
    'Sin gluten es un umbral analítico, no una declaración libre': [
        'Dar el umbral con su unidad y su norma, y la segunda declaración '
        'posible con el suyo, y decir que se miden en el producto TAL COMO SE '
        'VENDE al consumidor final.',
        'Sacar la consecuencia para un obrador de pastelería: con harina de '
        'trigo en el aire no se puede declarar sin gluten sin validar que se '
        'está por debajo del umbral. Cambiar la harina no basta.',
        'Aclarar el papel de la certificación privada: es voluntaria y '
        'ADICIONAL, no sustituye al reglamento ni exime de la validación.',
        'Cerrar con la decisión de negocio: si el sin gluten no se puede '
        'sostener con un obrador separado y con analítica, se vende otra cosa '
        'y no se anuncia. Anunciarlo sin poder demostrarlo es el riesgo más '
        'caro de todo el capítulo.',
    ],
}

PPE_11 = {
    'Los nueve proveedores verificados, por categoría': [
        'Presentar los nueve proveedores con su categoría y su enlace, y decir '
        'con todas las letras por qué son nueve y no treinta: los demás no '
        'tienen ficha comprobable y no se publican.',
        'Explicar la lógica de reparto por categoría: ingredientes técnicos, '
        'masas madre y mejorantes, chocolate y coberturas, mantequilla y nata, '
        'harinas y distribución general. Con dos o tres se arranca; con nueve '
        'se negocia.',
        'Dar el pedido mínimo acumulado si se pide a los nueve y el plazo medio '
        'comprometido, y explicar que el pedido mínimo es dinero parado en el '
        'almacén el día que abres.',
    ],
    'Cómo pedir tres presupuestos comparables': [
        'Dar el método: mismo formato de compra, misma unidad, mismo plazo de '
        'entrega y mismas condiciones de pago en las tres peticiones. Sin eso '
        'no se comparan precios, se comparan sensaciones.',
        'Dar la lista de lo que se pide siempre por escrito: precio por unidad '
        'de compra, pedido mínimo, plazo, portes, condiciones de pago y quién '
        'es el comercial que responde.',
        'Explicar cuántas líneas de equipamiento del caso modelado están '
        'todavía sin proveedor asignado y por qué eso es lo normal al empezar: '
        'la hoja de proveedores se rellena a lo largo de las semanas previas, '
        'no en un día.',
    ],
    'El packaging es una partida, no un detalle': [
        'Dar el peso del packaging sobre el coste del producto que usa el caso '
        'modelado y el importe del primer pedido dentro de la inversión, y '
        'explicar que es una de las partidas que más se subestima.',
        'Explicar la decisión: el packaging se compra por mínimos de '
        'proveedor, así que la primera compra es más grande de lo que '
        'necesitas y hay que tenerla en la caja del arranque.',
    ],
    'Cómo modelar la volatilidad de la mantequilla y del cacao': [
        'Explicar el problema de método: fijar hoy un precio de mantequilla o '
        'de cacao en un documento es garantizar que dentro de unos meses el '
        'documento miente. Lo que se enseña es dónde mirar la referencia y con '
        'qué frecuencia revisarla.',
        'Explicar la referencia pública de la mantequilla a granel que sí se '
        'puede citar, con su fuente, y advertir de que NO es el precio de una '
        'mantequilla de laminado de alto contenido en materia grasa: son dos '
        'productos y dos mercados distintos.',
        'Explicar por qué del cacao no se da ninguna cifra puntual: hay varios '
        'valores distintos circulando para el mismo año y ninguno es citable.',
        'Cerrar con el mecanismo práctico: el precio de compra vive en celda '
        'verde en el libro de la carta, la merma objetivo también, y revisar '
        'esas dos celdas cada trimestre es lo que mantiene vivo el escandallo. '
        'Remitir al capítulo del escandallo.',
    ],
}

PPE_12 = {
    'La unidad de costeo es la tanda, no la pieza': [
        'La tesis del capítulo: en pastelería no se cocina de uno en uno. El '
        'escandallo por pieza que sale de dividir la receta entre las unidades '
        'esconde la mano de obra, que es donde de verdad se va el dinero.',
        'Explicar cómo se monta un escandallo por tanda: unidades por tanda, '
        'materia de la tanda, minutos de mano de obra de la tanda, y de ahí a '
        'la pieza. Dar el coste de mano de obra de las treinta tandas del caso '
        'modelado.',
        'Explicar que esa unidad es también la que permite decidir la '
        'producción: cambiar el tamaño de la tanda cambia el coste por pieza '
        'sin tocar la receta.',
    ],
    'El coste hora de obrador, imputado por pieza': [
        'Explicar de dónde sale el coste hora de obrador, paso a paso: brutos '
        'de convenio de los perfiles de obrador, pagas, seguridad social a '
        'cargo de la empresa, horas anuales de contrato y la parte de la '
        'jornada que de verdad es productiva. Dar el resultado del caso '
        'modelado.',
        'Explicar por qué la parte productiva de la jornada no es el cien por '
        'cien y por qué inflarla es la manera más fácil de engañarse: el '
        'obrador limpia, recibe género y monta la vitrina.',
        'Dar el peso medio de la mano de obra sobre el coste total de las '
        'treinta referencias y dejar que el número hable: en pastelería el '
        'ingrediente casi nunca es la parte grande del coste.',
    ],
    'Margen bruto y food cost son la misma regla, pero cuidado con la base': [
        'Decirlo sin rodeos: el margen bruto SOBRE PRECIO DE VENTA y el food '
        'cost son el mismo número visto del derecho y del revés. Presentarlos '
        'como dos objetivos independientes hace que el lector intente cumplir '
        'los dos y se vuelva loco.',
        'Avisar de la base, que es donde está la trampa: un «65-70 % de margen '
        'bruto» SOBRE COSTE no es lo mismo que sobre precio de venta —equivale '
        'a un food cost del 59-61 %, no del 30-35 %—. Antes de comparar tu '
        'margen con el de nadie, preguntar sobre qué base está calculado.',
        'Dar el food cost objetivo del caso modelado y el margen bruto que se '
        'deriva de él, y explicar que en el libro sólo se pide UNO de los dos '
        'y el otro se calcula solo.',
        'Explicar la brecha que el lector va a ver y que nadie le explica: el '
        'escandallo de las piezas da un food cost muy por debajo de la regla '
        'del sector porque la regla incluye lo que el escandallo de la pieza '
        'deja fuera —producto de terceros que revende el despacho, merma real, '
        'packaging y subida de la materia prima—. Por eso el plan financiero '
        'se proyecta con la regla y no con el escandallo, y la diferencia '
        'entre los dos números es el colchón.',
    ],
    'El precio por ración de la tarta por encargo, y el miedo a subir precios': [
        'Explicar por qué la tarta se cotiza por ración y no por unidad, y qué '
        'cambia eso en la conversación con el cliente: la ración es '
        'comparable, la tarta entera no.',
        'Dar el ejemplo completo de una referencia del caso modelado: coste de '
        'materia por unidad, coste de mano de obra por unidad, coste total y '
        'margen por unidad, y enseñar cuánto pesa cada parte.',
        'Dar el antídoto numérico contra el miedo a subir precios: con el '
        'margen por unidad y el mix delante se puede calcular cuántas '
        'unidades se pueden perder tras una subida sin perder margen total. Es '
        'una cuenta, no una opinión, y el libro la trae hecha.',
    ],
    # B1 (2026-09-10): la SPEC vende la hoja de decisión de huevo como el
    # diferencial del pack y el objetivo de este capítulo la nombra, pero
    # «ovoproducto», «huevo crudo» y «70 °C» salían CERO veces en los 21
    # capítulos: el comprador abría el libro 4 y encontraba una hoja que el
    # libro no le había enseñado a usar.
    'Las tres vías del huevo, y por qué decides una por elaboración': [
        'Dar las tres vías del art. 9 del RD 1021/2022 con su literal y su '
        'apartado: 70 °C durante 2 segundos en el centro o efecto equivalente '
        '(9.1.a), 63 °C durante 20 segundos CON consumo inmediato (9.1.b) y '
        'sustituir el huevo crudo por ovoproducto de establecimiento '
        'autorizado (9.2). Todo lo que no pase por una de las tres no se hace '
        'con huevo crudo.',
        'Explicar por qué la vía de los 63 °C no es la de una pastelería: '
        'exige servir para consumo inmediato, y lo que va a vitrina no lo es.',
        'Explicar las consecuencias que arrastra la vía elegida: lo de la vía '
        '1.a) que no sea estable a temperatura ambiente y todo lo hecho con '
        'ovoproducto se conserva a 8 °C o menos y se consume en 24 horas desde '
        'su elaboración, con registro de fecha y hora (art. 9.3); si además es '
        'producto de pastelería relleno, le aplica la fila 9 del art. 4.1 '
        '(4 °C) y manda el techo más bajo.',
        'Cerrar con la razón de que el libro 4 devuelva DOS salidas separadas: '
        'el plazo legal, que lo fija el art. 9.3, y la vida útil, que la '
        'declara el lector en su APPCC y que el real decreto no establece.',
    ],
}

PPE_13 = {
    'Los seis grupos del convenio y sus áreas funcionales': [
        'Explicar que la pastelería tiene convenio PROPIO en algunas '
        'provincias y que no es el de hostelería, y que el que se usa en el '
        'caso modelado es uno concreto, con su código y su boletín, tomado '
        'como ejemplo y sustituible por el del lector en celda verde.',
        'Presentar los seis grupos con su denominación y sus áreas '
        'funcionales, y dónde encaja cada perfil del obrador y del despacho.',
        'Advertir de que las tablas de otras provincias NO se publican aquí '
        'porque no están verificadas, y dar el método para encontrar la del '
        'lector en el boletín de su provincia.',
    ],
    'El convenio manda sobre el salario mínimo': [
        'Dar el bruto anual del grupo más bajo del convenio de referencia '
        'frente a la referencia anual del salario mínimo, y sacar la '
        'conclusión: en este sector manda el convenio, no el mínimo '
        'interprofesional.',
        'Explicar por qué esto importa al montar: quien presupuesta la nómina '
        'con el salario mínimo se queda corto desde el primer mes, y la '
        'desviación se arrastra a todo el plan financiero.',
        'Advertir de la caducidad: la tabla salarial y el salario mínimo son '
        'anuales, así que las dos cifras tienen fecha de caducidad y viven en '
        'celda editable. Remitir al anexo normativo.',
    ],
    'De bruto a coste de empresa: el dato que más sorprende': [
        'Enseñar la cadena completa con el caso modelado: bruto mensual del '
        'grupo, jornada equivalente, bruto mensual ajustado, seguridad social '
        'a cargo de la empresa y coste de empresa al año, persona a persona.',
        'Dar los tres números que resumen el capítulo: la suma de los brutos '
        'anuales, lo que cuesta la seguridad social al año y el coste de '
        'personal al año en velocidad de crucero.',
        'Explicar el dimensionado del caso modelado: cinco personas y las '
        'jornadas completas equivalentes que suman, con los cuatro perfiles '
        'del Kit de Tareas Pastelería y dos personas en el de vitrina. La guía '
        'construye el DIMENSIONADO; las fichas de tarea de cada perfil las '
        'entrega el kit y no se rehacen aquí.',
        'Dar el coste de personal al mes y explicar cómo se lee contra las '
        'ventas: es el ratio que más veces hunde un plan de pastelería.',
    ],
    'El problema estructural: no se encuentra personal': [
        'Contar el dolor con la voz de quien lo sufre y su fuente: es un '
        'oficio de fines de semana, de festivos y de levantarse pronto cuando '
        'los demás disfrutan, y encontrar gente es el problema que más se '
        'repite.',
        'Sacar la decisión de montaje: si el oficio no lo tienes tú, o lo '
        'contratas o lo aprendes, y las dos cosas tienen fecha y coste que hay '
        'que meter en el cronograma. Remitir al capítulo del cronograma.',
    ],
}

PPE_14 = {
    'El registro de jornada hoy: papel o una hoja de cálculo valen': [
        'Dar la obligación tal cual está: registro diario con hora concreta de '
        'inicio y de fin para cada persona, conservación durante cuatro años y '
        'a disposición de la plantilla, de sus representantes y de la '
        'inspección.',
        'Dar la parte que casi nadie dice: la ley NO exige ningún sistema '
        'digital. El artículo dice que el registro se organiza y se documenta '
        'por negociación colectiva o por decisión de la empresa, y no impone '
        'formato.',
        'Avisar de lo que hay que vigilar sin dar fechas: hay un proyecto de '
        'reforma en tramitación y a la fecha de corte de esta edición no hay '
        'norma publicada, así que conviene comprobar su estado antes de '
        'comprar un sistema. Remitir al anexo normativo.',
    ],
    'El turno de obrador frente al de despacho, y cómo se solapan en el pico': [
        'Explicar la lógica de los turnos del caso modelado: madrugada en el '
        'obrador, mañana y tarde en el despacho, y el solape que garantiza que '
        'nunca haya un día abierto sin nadie en el mostrador.',
        'Dar las horas planificadas a la semana, las jornadas equivalentes y '
        'los días abiertos sin cobertura, y explicar que ese último número '
        'tiene que valer cero antes de firmar ningún contrato.',
        'Explicar cómo cambia el cuadrante en campaña y por qué el refuerzo se '
        'planifica con semanas de antelación y no el día antes. Remitir al '
        'capítulo de las campañas.',
    ],
    'La prevención de riesgos en el obrador': [
        'Plantearlo como lo que es en esta edición: un bloque que NO está '
        'verificado aquí y que se trata dando la lista de qué preguntar a tu '
        'servicio de prevención, no afirmando umbrales.',
        'Dar la lista de lo que hay que llevar a esa conversación: exposición '
        'a polvo de harina, manipulación manual de cargas con sacos, trabajo '
        'con superficies calientes y con maquinaria con partes móviles, y '
        'turnos de noche. Sin cifras y sin citar norma.',
    ],
    'El horario del dueño es una decisión de vida': [
        'Poner el tema encima de la mesa sin adornos: el madrugón no es una '
        'anécdota del oficio, es la variable que más gente saca del negocio, y '
        'se decide al diseñar el cuadrante, no después.',
        'Contar el caso documentado de quien redujo plantilla y ganó más, con '
        'su fuente, y usarlo para lo que sirve: para demostrar que el tamaño '
        'no es el objetivo.',
        'Dar las tres decisiones concretas que fijan el horario del dueño: qué '
        'día cierra el despacho, qué parte de la producción se adelanta con '
        'frío y quién abre cuando el dueño no está.',
        'Cerrar con la frontera: el plan de producción semanal que reparte el '
        'trabajo dentro del obrador ya abierto es del Kit de Tareas '
        'Pastelería. Aquí se decide el dimensionado y el turno, no el parte '
        'diario.',
    ],
}


CAPITULOS += [
    {
        'n': 7,
        'titulo': 'El Obrador por Dentro: Frío, Calor y Flujo de Trabajo',
        'resumen_indice': 'por qué manda el frío negativo, qué hacen el abatidor y la cámara de fermentación, por qué un arcón no es un abatidor y cómo se calcula el equipo que te limita.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector dimensione el obrador por el cuello de '
                    'botella y no por el catálogo: que sepa qué equipo le '
                    'limita, cuántas piezas al día le permite el conjunto y qué '
                    'compra no puede posponer.',
        'epigrafes': list(PPE_07),
        'puntos_por_epigrafe': PPE_07,
        'puntos_globales': [
            'Nada de técnica de elaboración: no se explica cómo se hace un '
            'hojaldre ni cómo se atempera chocolate. Se explica qué decide '
            'cada equipo en la capacidad y en el coste.',
            'Las capacidades por equipo del caso modelado son SUPUESTOS de '
            'modelado calibrados con fichas de distribuidor, y se dicen '
            'supuestos.',
            'El capítulo no rehace el plan de producción semanal: eso es del '
            'Kit de Tareas Pastelería y aquí se cita por su nombre de fichero.',
        ],
        'cifras': [
            C('Piezas al día que quiere sacar el caso modelado en velocidad de crucero', f'{X_CAP}!Cuello de Botella!B6', 'num'),
            C('Piezas al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
            C('Holgura sobre el día normal', f'{X_CAP}!Cuello de Botella!B9', 'num'),
            C('Piezas al día de obrador que permite el abatidor', f'{X_CAP}!Capacidad por Equipo!M12', 'num'),
            C('Piezas al día que permite la cámara de fermentación controlada', f'{X_CAP}!Capacidad por Equipo!M11', 'num'),
            C('Piezas al día que permite el horno de convección de seis bandejas', f'{X_CAP}!Capacidad por Equipo!M9', 'num'),
            C('Minutos productivos disponibles al día en el obrador', f'{X_CAP}!Parámetros!B9', 'num'),
            C('Parte del surtido que pasa por el abatidor', f'{X_CAP}!Capacidad por Equipo!L12', 'pct0'),
            C('Equipos dados de alta en el caso modelado', f'{X_CAP}!Capacidad por Equipo!E18', 'num'),
        ],
        'sector': ['PA-13', 'PA-12', 'PS-78', 'PS-83'],
        'tablas': [
            {
                'titulo': 'Qué piezas al día permite cada equipo del obrador (capacidad-obrador-y-local.xlsx, hoja «Capacidad por Equipo»)',
                'src': (X_CAP, 'Capacidad por Equipo'),
                'cols': [('Equipo', 'B', 'txt'), ('Categoría', 'C', 'txt'),
                         ('¿Lo tienes?', 'D', 'txt'),
                         ('Piezas por ciclo', 'H', 'num'),
                         ('Minutos por ciclo', 'I', 'num'),
                         ('Ciclos al día', 'J', 'num'),
                         ('Parte del surtido que pasa (%)', 'L', 'pct0'),
                         ('Piezas al día de obrador que permite', 'M', 'num')],
                'filas': (6, 15),
                'nota': 'La última columna no es la capacidad del equipo: es cuántas piezas de '
                        'obrador permite sacar, teniendo en cuenta que sólo una parte del '
                        'surtido pasa por él. Por eso el equipo con menos piezas por ciclo no '
                        'es necesariamente el que limita.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No emitas ningún plan de producción semanal ni ningún reparto de '
            'tareas por partida: eso es del Kit de Tareas Pastelería.',
            'No des recetas, tiempos de fermentación ni temperaturas de horno: '
            'esto no es un manual técnico de obrador.',
            'No presentes las capacidades por equipo como datos de fabricante: '
            'son supuestos de modelado calibrados, y así se dice.',
        ],
    },
    {
        'n': 8,
        'titulo': 'Maquinaria: Qué Compras, Qué Alquilas y Qué Esperas a Tener',
        'resumen_indice': 'precios por gama con marca y modelo, la trampa del IVA en las fichas de distribuidor, la variante sin salida de humos y los plazos de entrega que mueven la apertura.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector se siente a negociar con precios, marcas, '
                    'modelos y plazos en la mano, sabiendo qué línea es crítica '
                    'para poder abrir y cuál puede esperar sin tocar la carta.',
        'epigrafes': list(PPE_08),
        'puntos_por_epigrafe': PPE_08,
        'puntos_globales': [
            'Toda cifra de maquinaria va con la etiqueta de si el precio lleva '
            'IVA o no. Si el distribuidor no lo declara, se dice que no lo '
            'declara.',
            'Se distingue en todo momento entre precio publicado en ficha de '
            'distribuidor y supuesto del modelo: son dos cosas distintas y el '
            'lector tiene que poder verlo.',
            'El capítulo termina en una acción: pedir tres presupuestos por '
            'cada línea crítica, con el plazo de entrega por escrito.',
        ],
        'cifras': [
            C('Líneas del checklist de equipamiento', f'{X_EQUIP}!Equipamiento!I40', 'num'),
            C('Total de referencia sin IVA de las líneas críticas', f'{X_EQUIP}!Equipamiento!I41', 'eur'),
            C('Total de referencia sin IVA de toda la dotación', f'{X_EQUIP}!Equipamiento!I42', 'eur'),
            C('IVA soportado sobre el equipamiento', f'{X_EQUIP}!Equipamiento!I46', 'eur'),
            C('Desembolso real del equipamiento con IVA', f'{X_EQUIP}!Equipamiento!I47', 'eur'),
            C('Plazo crítico de entrega, en semanas', f'{X_EQUIP}!Equipamiento!I53', 'num'),
            C('Semanas que faltan hasta la apertura prevista', f'{X_EQUIP}!Equipamiento!C11', 'num'),
            C('Inversión de referencia de la variante sin salida de humos', f'{X_EQUIP}!Variante del Formato!K39', 'eur'),
            C('Inversión de referencia del caso base con venta', f'{X_EQUIP}!Variante del Formato!G39', 'eur'),
        ],
        'sector': ['PS-72', 'PS-74', 'PS-76', 'PS-77', 'PS-78', 'PS-79',
                   'PS-81', 'PS-82', 'PS-83', 'PS-84'],
        'tablas': [
            {
                'titulo': 'La dotación completa, línea a línea, con marca, modelo, base fiscal y plazo (checklist-equipamiento-y-proveedores.xlsx, hoja «Equipamiento»)',
                'src': (X_EQUIP, 'Equipamiento'),
                'cols': [('Partida', 'C', 'txt'), ('Marca', 'D', 'txt'),
                         ('Modelo', 'E', 'txt'), ('Prioridad', 'H', 'txt'),
                         ('Precio de referencia (€)', 'I', 'eur2'),
                         ('¿Lleva IVA?', 'J', 'txt'),
                         ('Precio sin IVA (€)', 'L', 'eur2'),
                         ('Plazo de entrega (semanas)', 'R', 'num')],
                'filas': (16, 37),
                'nota': 'Las líneas sin marca ni modelo son SUPUESTOS del modelo, no precios de '
                        'ficha: se sustituyen por los tres presupuestos que pidas. La columna de '
                        'si el precio lleva IVA tiene tres valores, y uno de ellos es que el '
                        'distribuidor no lo declara.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No des ningún precio de horno, amasadora o cámara que no esté en '
            'la lista de cifras del capítulo, y no inventes precios para las '
            'marcas que no publican tarifa.',
            'No cites un descuento de campaña sin decir que caduca y sin '
            'fecharlo.',
            'No presentes la variante sin salida de humos como una solución '
            'universal: cambia el producto que puedes hacer y hay que decirlo.',
        ],
    },
    {
        'n': 9,
        'titulo': 'Licencias, Sanidad y Registro: el Camino Completo',
        'resumen_indice': 'por qué la pastelería minorista no va al registro general, cuándo sí vuelve, el esquema de central y sucursales, cuatro comunidades de ejemplo y la ruta doméstica completa.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Corregir el error número uno del nicho y dejar al lector '
                    'con el árbol de decisión resuelto: qué registro le toca, '
                    'qué trámite concreto, si le habilita para abrir y qué pasa '
                    'si además quiere vender a otras tiendas o empezar desde '
                    'casa.',
        'epigrafes': list(PPE_09),
        'puntos_por_epigrafe': PPE_09,
        'puntos_globales': [
            'Cada afirmación de este capítulo va con su norma, su artículo y '
            'la frase «comprobado el 10 de septiembre de 2026». Es el capítulo '
            'que sostiene el producto y no admite una sola frase sin '
            'referencia.',
            'Las cuatro comunidades autónomas son EJEMPLOS declarados, y cada '
            'vez que aparecen se dice. Lo municipal —el trámite de actividad, '
            'las tasas, la ordenanza— va como pregunta al ayuntamiento: la '
            'ordenanza cambia en cada uno de los miles de municipios de '
            'España y esta guía no puede traer la de ninguno.',
            'Tono de quien te acompaña al trámite, no de despacho: frases '
            'cortas, orden claro y siempre el siguiente paso. El lector de '
            'este capítulo tiene miedo, y el miedo se quita con secuencia.',
        ],
        'cifras': [
            C('Trámites del expediente completo del caso modelado', f'{X_LEGAL}!Checklist Legal (F1-F6)!D55', 'num'),
            C('Trámites que cambian según la comunidad autónoma', f'{X_LEGAL}!Checklist Legal (F1-F6)!D63', 'num'),
            C('Coste previsto de la comunicación al registro sanitario autonómico', f'{X_LEGAL}!Checklist Legal (F1-F6)!F37', 'eur'),
            C('Umbral de la primera vía del artículo 3, sobre el volumen anual', f'{X_LEGAL}!Suministro a Otros Minoristas!B20', 'pct0'),
            C('Umbral de la segunda vía del artículo 3, en kilos a la semana', f'{X_LEGAL}!Suministro a Otros Minoristas!B23', 'num'),
            C('Radio máximo entre comunidades autónomas, en kilómetros', f'{X_LEGAL}!Suministro a Otros Minoristas!B30', 'num'),
            C('Tope absoluto de kilos a la semana del artículo 13.9', f'{X_LEGAL}!Ruta Doméstica!B13', 'num'),
            C('Metros útiles dedicados a la actividad en el ejemplo doméstico', f'{X_LEGAL}!Ruta Doméstica!B6', 'num'),
            C('Kilos a la semana del ejemplo doméstico', f'{X_LEGAL}!Ruta Doméstica!B7', 'num'),
            C('Kilos por metro cuadrado útil y semana del ejemplo doméstico', f'{X_LEGAL}!Ruta Doméstica!B16', 'num1'),
        ],
        'sector': ['PA-01', 'PA-01b', 'PA-02', 'PA-02b', 'PA-02c', 'PA-02d',
                   'PA-03', 'PA-03b', 'PA-04', 'PA-29'],
        'tablas': [
            {
                'titulo': 'Los tres casos del registro sanitario, para que se vea la frontera (checklist-legal-y-licencias.xlsx, hoja «Árbol de Registro Sanitario»)',
                'src': (X_LEGAL, 'Árbol de Registro Sanitario'),
                'cols': [('Tu situación', 'A', 'txt'), ('Lo que te toca', 'B', 'txt'),
                         ('Por qué', 'C', 'txt')],
                'filas': (20, 22),
                'nota': V_REG,
            },
            {
                'titulo': 'La lista blanca de la vivienda: las cinco letras del artículo 13.8 (checklist-legal-y-licencias.xlsx, hoja «Ruta Doméstica»)',
                'src': (X_LEGAL, 'Ruta Doméstica'),
                'cols': [('Letra y qué permite', 'A', 'txt'),
                         ('Qué NO entra por ahí', 'C', 'txt')],
                'filas': (22, 26),
                'nota': V_VIVIENDA,
            },
            {
                'titulo': 'Las cinco prohibiciones del artículo 13.5, y cuál es la única incondicional (checklist-legal-y-licencias.xlsx, hoja «Ruta Doméstica»)',
                'src': (X_LEGAL, 'Ruta Doméstica'),
                'cols': [('Letra', 'A', 'txt'), ('Qué prohíbe', 'B', 'txt'),
                         ('Régimen', 'C', 'txt')],
                'filas': (31, 33),
                'nota': V_VIVIENDA,
            },
        ],
        'prohibido': NO_COMUN + [
            'No escribas este capítulo sin la norma y el artículo pegados a '
            'cada afirmación: es el capítulo por el que se compra el producto '
            'y una sola frase sin referencia lo tumba.',
            'No conviertas el cuadro de cuatro comunidades autónomas en un '
            'cuadro nacional: se dice que son ejemplos cada vez que aparecen.',
            'No des ningún plazo, tasa ni requisito municipal como si fuera '
            'general.',
        ],
    },
    {
        'n': 10,
        'titulo': 'Autocontrol, Alérgenos y Formación: Qué Tener el Día de la Inspección',
        'resumen_indice': 'el plan simplificado y la persona responsable, el registro de formación que sustituye al carnet, los alérgenos de obrador frente a los de vitrina y el umbral del sin gluten.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector llegue al día de la inspección con la '
                    'carpeta hecha: qué documento le van a pedir, quién lo '
                    'firma, dónde vive y qué norma lo exige.',
        'epigrafes': list(PPE_10),
        'puntos_por_epigrafe': PPE_10,
        'puntos_globales': [
            'Cada afirmación va con su norma y su artículo y con la fecha de '
            'comprobación. Y donde la norma no dice nada, se dice que no dice '
            'nada en vez de rellenarlo.',
            'La frontera con el Pack APPCC y con el Kit de Tareas Pastelería '
            'se repite en cada apartado: aquí se explica qué hay que tener y '
            'por qué; los registros del día a día y la declaración de '
            'alérgenos de vitrina los entregan esos productos.',
            'Nada de miedo comercial: no se venden sanciones. Se da la lista '
            'de documentos y el orden en el que se montan.',
        ],
        'cifras': [
            C('Personas con formación registrada en el caso modelado', f'{X_LEGAL}!Registro de Formación!B17', 'num'),
            C('Formaciones caducadas', f'{X_LEGAL}!Registro de Formación!B18', 'num'),
            C('Validez interna que se da la casa a cada formación, en días', f'{X_LEGAL}!Registro de Formación!B13', 'num'),
            C('Coste previsto del plan de autocontrol en el caso modelado', f'{X_LEGAL}!Checklist Legal (F1-F6)!F39', 'eur'),
            C('Coste previsto de la formación de manipuladores', f'{X_LEGAL}!Checklist Legal (F1-F6)!F40', 'eur'),
            C('Trámites de la fase de sanidad, autocontrol y formación', f'{X_LEGAL}!Checklist Legal (F1-F6)!E43', 'num'),
            C('Umbral analítico para poder declarar sin gluten, en miligramos por kilo', f'{X_CARTA}!Parámetros!B31', 'num'),
            C('Referencias de la carta que necesitan vitrina refrigerada', f'{X_CARTA}!Decisión de Huevo y Temperatura!G38', 'num'),
        ],
        'sector': ['PA-09', 'PA-10', 'PA-11', 'PA-21', 'PA-22', 'PA-23',
                   'PA-16', 'PA-16c'],
        'tablas': [
            {
                'titulo': 'El registro de formación del caso modelado, persona a persona (checklist-legal-y-licencias.xlsx, hoja «Registro de Formación»)',
                'src': (X_LEGAL, 'Registro de Formación'),
                'cols': [('Persona', 'A', 'txt'), ('Área', 'B', 'txt'),
                         ('Contenido de la formación', 'C', 'txt'),
                         ('Horas', 'D', 'num')],
                'filas': (6, 10),
                'nota': V_FORMA + ' — el contenido y las horas son un supuesto de la casa: la '
                        'norma no fija ni un temario ni una duración, fija que el empresario '
                        'garantice la formación y pueda acreditarla.',
            },
            {
                'titulo': 'Los trámites de sanidad, autocontrol y formación, en orden (checklist-legal-y-licencias.xlsx, hoja «Checklist Legal (F1-F6)»)',
                'src': (X_LEGAL, 'Checklist Legal (F1-F6)'),
                'cols': [('Fase', 'B', 'txt'), ('Trámite', 'C', 'txt'),
                         ('Responsable', 'D', 'txt'),
                         ('Plazo (días)', 'E', 'num'),
                         ('Coste previsto', 'F', 'eur'),
                         ('¿Cambia por comunidad autónoma?', 'J', 'txt')],
                'filas': (37, 42),
                'nota': 'Los plazos son supuestos de planificación, no plazos legales de '
                        'resolución: sirven para montar el cronograma. Donde pone «a '
                        'presupuestar» es porque el importe depende de tu municipio o de tu '
                        'proveedor.',
            },
            {
                'titulo': 'Qué documento te va a pedir cada inspección, y dónde vive',
                'cabecera': ['Qué te piden', 'Dónde vive', 'Base normativa'],
                'filas': [
                    ['Justificante de la comunicación o declaración responsable al registro autonómico', 'Carpeta del expediente, fase de sanidad', 'RD 191/2011 art. 2.2 en la redacción del RD 1021/2022'],
                    ['Plan de autocontrol, con su persona responsable designada por escrito', 'Carpeta del expediente; los registros diarios, en el Pack APPCC', 'RD 1021/2022 art. 20'],
                    ['Registro de formación de cada persona, con contenido, horas y fecha', 'Hoja de registro de formación del libro de licencias', 'Rgto. (CE) 852/2004, Anexo II, Cap. XII'],
                    ['Información de alérgenos por escrito y accesible, con cartel en cada sección', 'Kit de Tareas Pastelería, matriz de alérgenos de vitrina', 'RD 126/2015 arts. 4.1, 6.2 y 6.5'],
                    ['Matriz de alérgenos de obrador, por materia prima y orden de elaboración', 'Este pack', 'Rgto. (CE) 852/2004, Anexo II, Cap. IX punto 9'],
                    ['Registro de temperaturas y de recepción', 'Kit de Tareas Pastelería', 'RD 1021/2022 arts. 4 y 5'],
                    ['Registro de fecha y hora de elaboración de lo que va por la vía del huevo', 'Hoja de decisión de huevo y temperatura de este pack', 'RD 1021/2022 art. 9.3'],
                    ['Etiquetado del producto envasado por ti para venta inmediata', 'Este pack, capítulo de canales', 'RD 126/2015 art. 5.1'],
                ],
                'nota': 'Comprobado el 10 de septiembre de 2026. Ninguna de estas filas es una '
                        'lista cerrada de lo que puede pedirte una inspección: es lo que se '
                        'pide siempre, y por eso se monta antes de abrir.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No duplicar la matriz de alérgenos de vitrina: la entrega el Kit '
            'de Tareas Pastelería y aquí sólo se cita.',
            'No vender sanciones ni cifras de multas: este capítulo da la '
            'lista de documentos, no miedo.',
            'No afirmar que existe un temario o una duración mínima obligatoria '
            'de la formación de manipuladores: la norma no los fija.',
        ],
    },
    {
        'n': 11,
        'titulo': 'Proveedores: Materia Prima, Packaging y Plazos',
        'resumen_indice': 'los nueve proveedores verificados por categoría, cómo pedir tres presupuestos comparables, el peso del packaging y cómo modelar la volatilidad de la mantequilla y del cacao.',
        'palabras': 1700, 'bloques': 1,
        'objetivo': 'Que el lector salga con una lista de proveedores '
                    'comprobables, un método para comparar tres presupuestos de '
                    'verdad y un mecanismo para que la subida de la materia '
                    'prima no le pille con el escandallo de hace un año.',
        'epigrafes': list(PPE_11),
        'puntos_por_epigrafe': PPE_11,
        'puntos_globales': [
            'Nueve proveedores con enlace comprobado, y se dice expresamente '
            'que los que no se pudieron comprobar no se publican. La lista es '
            'un punto de partida, no una recomendación de compra.',
            'Ninguna cifra de precio de materia prima entra sin fecha y sin '
            'formato de compra. Del cacao no se da ninguna.',
            'Este capítulo enlaza con el directorio de proveedores de '
            'hostelería del grupo, Hosply, como sitio donde seguir buscando '
            'por categoría y por zona.',
        ],
        'cifras': [
            C('Proveedores verificados que se publican', f'{X_EQUIP}!Proveedores!F16', 'num'),
            C('Pedido mínimo acumulado si pides a los nueve', f'{X_EQUIP}!Proveedores!F18', 'eur'),
            C('Plazo medio de entrega comprometido, en días', f'{X_EQUIP}!Proveedores!F19', 'num'),
            C('Primer pedido de packaging dentro de la inversión', f'{X_CAPEX}!CAPEX por Bloque!K44', 'eur'),
            C('Peso del packaging sobre el coste del producto en el caso modelado', f'{X_CARTA}!Parámetros!B35', 'pct0'),
            C('Merma objetivo del caso modelado', f'{X_CARTA}!Parámetros!B34', 'pct0'),
            C('Coste de materia de una tanda de cada una de las treinta referencias', f'{X_CARTA}!Escandallo por Tanda!F266', 'eur2'),
            C('Líneas de equipamiento todavía sin proveedor asignado', f'{X_EQUIP}!Contador!B45', 'num'),
        ],
        # PS-59 (el packaging entre el 5 y el 15 % del coste) llega al prompt
        # como HUECO SIN FUENTE a propósito: es de fiabilidad baja, así que el
        # redactor NO puede escribir ese rango. El porcentaje que sí se escribe
        # es el del caso modelado, que sale de una celda del libro de la carta.
        'sector': ['PS-87', 'PS-88', 'PS-89', 'PS-90', 'PS-91', 'PS-92',
                   'PS-93', 'PS-94', 'PS-95', 'PS-66', 'PS-59'],
        'tablas': [
            {
                'titulo': 'Los nueve proveedores verificados, con categoría, pedido mínimo y plazo (checklist-equipamiento-y-proveedores.xlsx, hoja «Proveedores»)',
                'src': (X_EQUIP, 'Proveedores'),
                'cols': [('Nº', 'A', 'num'), ('Proveedor', 'B', 'txt'),
                         ('Qué te vende', 'C', 'txt'), ('Enlace', 'D', 'txt'),
                         ('Pedido mínimo (€)', 'H', 'eur'),
                         ('Plazo (días)', 'I', 'num')],
                'filas': (7, 15),
                'nota': 'Los pedidos mínimos, los plazos y las condiciones de pago de esta tabla '
                        'son SUPUESTOS de partida para que puedas presupuestar: se sustituyen '
                        'por lo que te diga cada comercial. Lo verificado es quién es cada '
                        'proveedor y qué vende.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No publiques ningún proveedor que no esté en la tabla: los que no '
            'se pudieron comprobar quedan fuera a propósito.',
            'No des ninguna cifra puntual de cacao, y no mezcles la cotización '
            'de la mantequilla a granel con el precio de una mantequilla de '
            'laminado.',
            'No presentes los pedidos mínimos ni los plazos como condiciones '
            'reales de esos proveedores: son supuestos de partida.',
        ],
    },
    {
        'n': 12,
        'titulo': 'Escandallo y Precios: por Qué la Mano de Obra Manda',
        'resumen_indice': 'la tanda como unidad de costeo, el coste hora de obrador imputado por pieza, la regla única de margen y el precio por ración de la tarta por encargo.',
        'palabras': 1800, 'bloques': 2,
        'objetivo': 'Que el lector deje de regalar su trabajo: que sepa qué le '
                    'cuesta de verdad cada pieza con la mano de obra dentro, '
                    'que entienda que margen y food cost son la misma regla, y '
                    'que tenga el antídoto numérico contra el miedo a subir '
                    'precios.',
        'epigrafes': list(PPE_12),
        'puntos_por_epigrafe': PPE_12,
        'puntos_globales': [
            'Una sola regla de margen en todo el capítulo: se pide el food '
            'cost objetivo o el margen bruto objetivo, nunca los dos, y el '
            'otro se deriva.',
            'El método de costeo por lote y la ingeniería de carta NO se '
            'explican aquí: se remite a la Guía Food Cost y de Ingeniería de '
            'Menú y al Kit de Escandallos, que traen el escandallo unitario de '
            'tres elaboraciones de pastelería.',
            'Los escandallos del caso modelado son datos de ejemplo. Tres de '
            'las referencias están copiadas del Kit de Escandallos para que las '
            'cifras cuadren entre los dos productos, y se dice.',
        ],
        'cifras': [
            C('Coste hora de obrador del caso modelado', f'{X_CARTA}!Parámetros!B16', 'eur2'),
            C('Horas productivas del obrador al año', f'{X_CARTA}!Parámetros!B15', 'num'),
            C('Coste de empresa anual del personal de obrador', f'{X_CARTA}!Parámetros!F9', 'eur'),
            C('Peso medio de la mano de obra sobre el coste total', f'{X_CARTA}!Coste Hora y Mano de Obra!R36', 'pct1'),
            C('Coste de mano de obra de las treinta tandas', f'{X_CARTA}!Coste Hora y Mano de Obra!H36', 'eur2'),
            C('Food cost objetivo del caso modelado', f'{X_CARTA}!Parámetros!B24', 'pct0'),
            C('Margen bruto objetivo derivado de ese food cost', f'{X_CARTA}!Parámetros!B25', 'pct0'),
            C('Coste total por unidad del croissant de mantequilla', f'{X_CARTA}!Coste Hora y Mano de Obra!K6', 'eur2'),
            C('Coste de mano de obra por unidad del croissant', f'{X_CARTA}!Coste Hora y Mano de Obra!I6', 'eur2'),
            C('Margen por unidad del croissant', f'{X_CARTA}!Coste Hora y Mano de Obra!Q6', 'eur2'),
        ],
        'sector': ['PS-55', 'PS-56'],
        'tablas': [
            {
                'titulo': 'El escandallo por tanda de las treinta referencias, con la mano de obra dentro (carta-de-apertura-y-escandallo.xlsx, hoja «Coste Hora y Mano de Obra»)',
                'src': (X_CARTA, 'Coste Hora y Mano de Obra'),
                'cols': [('Ref', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Unidades por tanda', 'D', 'num'),
                         ('Minutos de mano de obra por tanda', 'E', 'num'),
                         ('Mano de obra por unidad (€)', 'I', 'eur2'),
                         ('Materia por unidad (€)', 'J', 'eur2'),
                         ('Coste total por unidad (€)', 'K', 'eur2'),
                         ('Food cost (%)', 'O', 'pct1')],
                'filas': (6, 35),
                'nota': 'Los minutos de mano de obra y los gramajes son datos de ejemplo. Tres '
                        'referencias están copiadas del Kit de Escandallos para que un cliente '
                        'que tenga los dos productos no vea dos costes distintos del mismo '
                        'croissant.',
            },
            {
                'titulo': 'De dónde sale el coste hora de obrador, parámetro a parámetro (carta-de-apertura-y-escandallo.xlsx, hoja «Parámetros»)',
                'src': (X_CARTA, 'Parámetros'),
                'cols': [('Parámetro', 'A', 'txt'), ('Valor', 'B', 'num2'),
                         ('Unidad', 'C', 'txt'), ('De dónde sale', 'D', 'txt'),
                         ('Coste de empresa al año (€)', 'F', 'eur2')],
                'filas': (9, 16),
                'omitir_filas': (11, 12),
                'nota': 'La cadena se sigue entera de arriba abajo: las 2,5 jornadas '
                        'equivalentes de obrador (Jefe 1,0 + Pastelero 1,0 + Ayudante 0,5) '
                        'por las horas de contrato y por la parte productiva de la jornada '
                        'dan las horas productivas del año; el coste de empresa anual de esas '
                        '2,5 jornadas dividido entre esas horas da el coste hora. Sin la fila '
                        'de las jornadas, la multiplicación no cuadra. El coste de empresa es '
                        'el bruto de convenio por sus pagas más la Seguridad Social a cargo '
                        'de la empresa, y sale de la hoja de personal del mismo libro. La '
                        'parte productiva de la jornada es un supuesto y es la palanca más '
                        'sensible de toda la hoja: subirla baja el coste hora y hace que la '
                        'carta parezca más rentable de lo que es.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No presentes margen bruto y food cost como dos reglas '
            'independientes ni pidas los dos números al lector.',
            'No des ningún precio por ración tomado de un foro ni ninguna '
            'referencia de precio de mercado que no esté en las cifras del '
            'capítulo.',
            'No expliques la matriz de ingeniería de menú ni el método de '
            'costeo por lote: viven en otro producto del catálogo.',
        ],
    },
    {
        'n': 13,
        'titulo': 'El Equipo: Cuántos, Qué Perfiles y Qué Cuestan',
        'resumen_indice': 'los seis grupos del convenio, por qué el convenio manda sobre el salario mínimo, el salto de bruto a coste de empresa y el problema de encontrar personal.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Que el lector dimensione la plantilla con los perfiles y '
                    'los brutos reales de un convenio de pastelería, y que vea '
                    'el salto de bruto a coste de empresa antes de firmar el '
                    'primer contrato.',
        'epigrafes': list(PPE_13),
        'puntos_por_epigrafe': PPE_13,
        'puntos_globales': [
            'Los cuatro perfiles se llaman Jefe Pastelero, Pastelero, Ayudante '
            'y Dependiente Vitrina, y de este último hay dos personas. La '
            'palabra «oficial» no se usa como nombre de puesto en ningún '
            'momento.',
            'El convenio que aparece es un EJEMPLO con su código y su boletín, '
            'y vive en celda editable: el lector lo sustituye por el de su '
            'provincia. No se publican tablas de otras provincias porque no '
            'están verificadas.',
            'La guía construye el dimensionado y el plan de contratación; las '
            'fichas de tarea de cada perfil las entrega el Kit de Tareas '
            'Pastelería y no se rehacen aquí.',
        ],
        'cifras': [
            C('Bruto mensual del grupo más alto del convenio de referencia', f'{X_TURNOS}!Parámetros!C8', 'eur2'),
            C('Bruto mensual del grupo más bajo del convenio de referencia', f'{X_TURNOS}!Parámetros!C13', 'eur2'),
            C('Bruto anual del grupo más bajo', f'{X_TURNOS}!Parámetros!C16', 'eur2'),
            C('Referencia anual del salario mínimo', f'{X_TURNOS}!Parámetros!C17', 'eur'),
            C('Seguridad Social a cargo de la empresa', f'{X_TURNOS}!Parámetros!C21', 'pct0'),
            C('Coste de personal al mes del caso modelado', f'{X_TURNOS}!Horas y Coste!E15', 'eur2'),
            C('Coste de personal al año en velocidad de crucero', f'{X_TURNOS}!Horas y Coste!E16', 'eur'),
            C('Lo que cuesta la Seguridad Social al año', f'{X_TURNOS}!Horas y Coste!E19', 'eur'),
            C('Suma de los brutos anuales de la plantilla', f'{X_TURNOS}!Horas y Coste!E20', 'eur'),
            C('Jornadas completas equivalentes de la plantilla', f'{X_TURNOS}!Horas y Coste!E17', 'num1'),
        ],
        'sector': ['PA-32', 'PA-33', 'PS-104', 'PS-105', 'PS-54'],
        'tablas': [
            {
                'titulo': 'De bruto de convenio a coste de empresa, persona a persona (plantilla-turnos-y-coste-personal.xlsx, hoja «Horas y Coste»)',
                'src': (X_TURNOS, 'Horas y Coste'),
                'cols': [('Id', 'A', 'txt'), ('Persona', 'B', 'txt'),
                         ('Área', 'C', 'txt'), ('Grupo de convenio', 'D', 'txt'),
                         ('Bruto mensual del grupo (€)', 'E', 'eur2'),
                         ('Jornada equivalente', 'F', 'num1'),
                         ('Bruto anual (€)', 'I', 'eur'),
                         ('Coste de empresa al año (€)', 'K', 'eur'),
                         ('Coste por hora (€)', 'L', 'eur2')],
                'filas': (7, 12),
                'nota': V_CONV + ' — la diferencia entre la columna de bruto anual y la de '
                        'coste de empresa es la Seguridad Social a cargo de la empresa, y es el '
                        'número que más sorprende al montar la primera nómina.',
            },
            {
                'titulo': 'Los seis grupos del convenio de referencia y sus áreas funcionales (plan-financiero-3-anos-pasteleria.xlsx, hoja «Personal»)',
                'src': (X_PLAN, 'Personal'),
                'cols': [('Grupo', 'A', 'txt'), ('Denominación', 'B', 'txt'),
                         ('Bruto mes (€)', 'E', 'eur2'),
                         ('Bruto año (€)', 'F', 'eur'),
                         ('Áreas funcionales', 'G', 'txt'),
                         ('Puestos que cita el convenio', 'I', 'txt')],
                'filas': (15, 20),
                'nota': V_CONV + ' — la tabla caduca a final del año de la edición, y el '
                        'convenio entra entonces en renegociación. Vive en celda editable por '
                        'eso.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDA la palabra «oficial» como nombre de un puesto de la '
            'plantilla del caso modelado.',
            'No publiques tablas salariales de provincias distintas de la del '
            'convenio de referencia: no están verificadas en esta edición.',
            'No rehagas las fichas de tarea de cada perfil: las entrega el Kit '
            'de Tareas Pastelería.',
            'No uses ningún escenario de gastos fijos de terceros para '
            'comprobar el coste de personal del caso modelado.',
        ],
    },
    {
        'n': 14,
        'titulo': 'Turnos de Madrugada y Jornada Legal',
        'resumen_indice': 'el registro de jornada tal y como está hoy, el turno de obrador frente al de despacho, qué preguntar al servicio de prevención y el horario del dueño.',
        'palabras': 1700, 'bloques': 1,
        'objetivo': 'Que el lector diseñe su cuadrante con los ojos abiertos: '
                    'que sepa qué le obliga el registro de jornada, cómo se '
                    'solapan obrador y despacho, y que decida su propio horario '
                    'antes de que lo decida el negocio por él.',
        'epigrafes': list(PPE_14),
        'puntos_por_epigrafe': PPE_14,
        'puntos_globales': [
            'De prevención de riesgos NO se afirma nada: no está verificado en '
            'esta edición y va como lista de qué preguntar al servicio de '
            'prevención, sin cifras y sin citar articulado.',
            'No se da ninguna fecha de la reforma del registro horario '
            'digital: a la fecha de corte no hay norma publicada.',
            'El capítulo termina en un cuadrante concreto, no en una '
            'reflexión: días de apertura, turnos y quién cubre cada franja.',
        ],
        'cifras': [
            C('Horas planificadas a la semana en el caso modelado', f'{X_TURNOS}!Turnos Semanales!E22', 'num'),
            C('Jornadas equivalentes de la plantilla', f'{X_TURNOS}!Turnos Semanales!E23', 'num1'),
            C('Días abiertos sin nadie en el mostrador', f'{X_TURNOS}!Turnos Semanales!E26', 'num'),
            C('Días de apertura a la semana', f'{X_TURNOS}!Parámetros!C24', 'num'),
            C('Horas semanales de jornada completa', f'{X_TURNOS}!Parámetros!C22', 'num'),
            C('Horas anuales de contrato', f'{X_TURNOS}!Parámetros!C23', 'num'),
            C('Horas semanales planificadas del Jefe Pastelero', f'{X_TURNOS}!Turnos Semanales!L11', 'num'),
            C('Horas semanales planificadas del Dependiente Vitrina de tarde', f'{X_TURNOS}!Turnos Semanales!L15', 'num'),
        ],
        'sector': ['PA-34', 'PS-97', 'PS-54'],
        'tablas': [
            {
                'titulo': 'El cuadrante semanal del caso modelado (plantilla-turnos-y-coste-personal.xlsx, hoja «Turnos Semanales»)',
                'src': (X_TURNOS, 'Turnos Semanales'),
                'cols': [('Persona', 'B', 'txt'), ('Área', 'C', 'txt'),
                         ('Turno', 'D', 'txt'),
                         ('Horas planificadas a la semana', 'L', 'num'),
                         ('Horas contratadas a la semana', 'M', 'num'),
                         ('Diferencia', 'N', 'num')],
                'filas': (11, 16),
                'nota': 'La columna de diferencia tiene que valer cero antes de firmar ningún '
                        'contrato: si sale positiva, estás planificando más horas de las que '
                        'contratas.',
            },
            {
                'titulo': 'Cobertura de obrador y de despacho, día a día (plantilla-turnos-y-coste-personal.xlsx, hoja «Turnos Semanales»)',
                'src': (X_TURNOS, 'Turnos Semanales'),
                'cols': [('Concepto', 'A', 'txt'), ('Lunes', 'E', 'num'),
                         ('Martes', 'F', 'num'), ('Miércoles', 'G', 'num'),
                         ('Jueves', 'H', 'num'), ('Viernes', 'I', 'num'),
                         ('Sábado', 'J', 'num'), ('Domingo', 'K', 'num')],
                'filas': (16, 19),
                'nota': 'El día de cierre del despacho es un supuesto del caso modelado. La '
                        'fila de cobertura es la que hay que mirar antes de cerrar el '
                        'cuadrante: ningún día abierto puede quedar sin nadie en el mostrador.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No des ninguna fecha ni ningún requisito de la reforma del '
            'registro horario digital.',
            'No cites articulado ni cifras de prevención de riesgos: no está '
            'verificado en esta edición.',
            'No conviertas el cuadrante del caso modelado en una recomendación '
            'universal de horarios: es un supuesto y se dice.',
        ],
    },
]


PPE_15 = {
    'El pico multiplica la producción con el mismo equipo': [
        'Abrir con el caso documentado de un obrador que pasa de un centenar '
        'de piezas al día a varios cientos en campaña con el mismo equipo, con '
        'su fuente, y explicar que eso no es una anécdota: es la forma del año '
        'en pastelería.',
        'Dar el factor de campaña y la demanda de piezas al día en la campaña '
        'grande del caso modelado frente a lo que permite el conjunto de '
        'equipos, y enseñar el déficit diario.',
        'Explicar la consecuencia de compra: la maquinaria no se dimensiona '
        'para el día normal, se dimensiona sabiendo cuánto déficit se está '
        'aceptando en campaña y cómo se cubre.',
    ],
    'Cuánto pesa cada campaña sobre el año': [
        'Dar el peso conjunto de las seis campañas sobre las ventas del año y '
        'la facturación que suman, y separar facturación total de facturación '
        'INCREMENTAL, que es la que de verdad añade la campaña.',
        'Dar el peso de la campaña grande y cuántas veces factura uno de sus '
        'días lo que un día normal, y explicar por qué eso convierte una '
        'semana en el mes más importante del año.',
        'Advertir del caso contrario, que es el que sorprende: hay campañas '
        'con nombre propio que pesan muy poco sobre el año, y planificar como '
        'si todas fueran iguales es lo que descuadra la compra.',
    ],
    'El déficit de capacidad y el refuerzo': [
        'Dar el número de campañas que el obrador del caso modelado NO aguanta '
        'y explicar cómo se lee: no significa que el negocio no funcione, '
        'significa que hay que decidir qué palanca se usa en cada una.',
        'Enumerar las palancas en orden de coste: adelantar producción con '
        'frío, alargar el turno, reforzar con personal y, sólo al final, '
        'limitar el encargo. Y decir cuál se puede usar en cada campaña según '
        'lo que se puede congelar.',
        'Dar el coste del refuerzo de todo el año y explicar de dónde sale: '
        'horas de refuerzo por coste hora de empresa, no por bruto. Remitir al '
        'capítulo del equipo.',
    ],
    'La tesorería inmovilizada en el stock de temporada': [
        'Explicar el mecanismo que nadie cuenta: la materia prima de la '
        'campaña se compra semanas antes de cobrarla, y eso es dinero parado '
        'en el almacén justo cuando más se necesita la caja.',
        'Dar la tesorería inmovilizada en materia de campaña del caso modelado '
        'y los días que el dinero está parado en la campaña grande.',
        'Sacar la decisión: la antelación de compra de cada campaña es una '
        'celda editable, y bajarla una semana cambia la caja aunque no cambie '
        'ni una venta.',
    ],
    'Desestacionalizar: qué se puede y qué no': [
        'Explicar qué se puede desestacionalizar de verdad: el encargo con '
        'antelación, el producto de temporada que se vende fuera de temporada '
        'y la venta a otras tiendas. Y qué no: la fecha del calendario.',
        'Cerrar con la frontera: las fechas y el qué hacer en cada campaña los '
        'da el calendario anual del Kit de Tareas Pastelería. Lo que da esta '
        'guía son los euros y la respuesta a si aguantas.',
    ],
}

PPE_16 = {
    'Captación y demanda validada': [
        'Explicar por qué el encargo es la línea con mejor margen y peor '
        'planificación: se capta por boca a boca y por redes, y casi nunca se '
        'mide. Dar el peso del canal sobre las ventas del caso modelado.',
        'Dar el margen bruto y el margen de contribución del canal de encargos '
        'y compararlo con el del mostrador: la diferencia es el coste de '
        'servir, y hay que verlo antes de decir que el encargo es más '
        'rentable.',
        'Explicar la validación de demanda antes de abrir: quien ya vende por '
        'encargo desde casa llega con la demanda validada y con una lista de '
        'clientes, y eso es un activo que hay que contar en el plan.',
    ],
    'Anticipo y señal': [
        'Dar la regla operativa: el encargo se reserva con anticipo, y el '
        'anticipo no es desconfianza, es lo que financia la compra de materia '
        'prima de la campaña.',
        'Explicar cómo cambia la caja: con anticipo, el canal de encargos '
        'cobra antes de producir; sin él, se produce con el dinero de uno '
        'mismo. Remitir a la tesorería de la campaña.',
        'Dar el criterio para fijar el porcentaje de anticipo según el tamaño '
        'del encargo y la antelación, y decir que en el libro es una celda '
        'editable.',
    ],
    'Calendario de entrega y riesgo de anulación': [
        'Explicar el riesgo real: una anulación de un encargo grande a pocos '
        'días es materia prima comprada y horas de obrador reservadas. Dar los '
        'días de campaña y los días con el dinero parado de la campaña de '
        'comuniones, que es la más larga.',
        'Dar la política mínima que hay que escribir antes de aceptar el '
        'primer encargo: plazo de anulación, qué parte del anticipo se '
        'devuelve y qué pasa si el cliente no recoge.',
        'Explicar la frontera: la ficha y el registro de encargos, con su '
        'agenda y sus encargos del día, los entrega el Kit de Tareas '
        'Pastelería. Aquí se decide el modelo de negocio del canal, no la '
        'herramienta.',
    ],
    'Qué se acepta y qué no sin histórico': [
        'Dar el criterio del primer año: se acepta lo que cabe en la capacidad '
        'del obrador ese día concreto, no lo que cabe en el calendario. '
        'Remitir al capítulo de las campañas.',
        'Enumerar lo que NO se acepta sin histórico: encargos con montaje en '
        'el sitio, entregas con horario cerrado en día de campaña y volúmenes '
        'que obliguen a comprar formato que no usas el resto del año.',
        'Cerrar con el mecanismo de aprendizaje: cada encargo aceptado se '
        'anota con horas reales y con incidencias, y a los seis meses eso ya '
        'es un histórico con el que decidir.',
    ],
}

PPE_17 = {
    'Cobro al contado y cobro a crédito: dos negocios distintos': [
        'Dar el reparto de cobro documentado del sector, con su fuente, y '
        'explicar la consecuencia: el mostrador cobra al instante y el '
        'suministro a otras tiendas cobra a plazo, así que dos canales con el '
        'mismo margen no valen lo mismo para la caja.',
        'Dar los días medios de cobro ponderados del caso modelado y explicar '
        'qué pasa cuando ese número sube: no cambia el resultado, cambia la '
        'necesidad de circulante.',
        'Dar el margen de contribución medio ponderado de todos los canales y '
        'lo que se llevan servir, cobrar y las comisiones, que es la '
        'diferencia entre el margen bruto y el de contribución.',
    ],
    'Cuándo el B2B te obliga a inscribirte en el registro general': [
        'Repetir la puerta de entrada, porque este es el capítulo donde el '
        'lector decide abrir el canal: el artículo que regula esto sólo se '
        'activa si suministras a comercios minoristas de DISTINTA titularidad.',
        'Recordar las tres condiciones acumulativas y las dos vías '
        'alternativas dentro de la primera, sin repetir el desarrollo del '
        'capítulo legal: aquí se aplica al número concreto del plan.',
        'Dar el peso del suministro a otras tiendas sobre las ventas del caso '
        'modelado y la lectura que hace el libro sobre la primera vía, y '
        'explicar cuándo saltaría la alarma.',
        'Dar la obligación documental que viene con el canal: declaración '
        'responsable y registro de a quién, cuánto y cuándo, y el punto que '
        'más fácil se rompe, que es servir a un cliente inscrito en el '
        'registro general.',
    ],
    'Venta a distancia: ya eres minorista, y la información va antes de la compra': [
        'Dar la buena noticia con su base: la definición legal de minorista ya '
        'incluye la entrega a distancia, así que vender online al consumidor '
        'final no te saca de tu régimen ni te obliga al registro general, y el '
        'radio que aplica al suministro entre comercios no te alcanza.',
        'Dar la obligación real, que es de información: en venta a distancia '
        'toda la información obligatoria tiene que estar disponible ANTES de '
        'la compra, con la única excepción de la fecha de duración, y completa '
        'en la entrega; y no se le puede cobrar al cliente por dársela. Para '
        'producto no envasado, lo que es obligatorio antes de comprar son los '
        'alérgenos.',
        'Dar el segundo efecto que casi nadie ve: vender online te convierte '
        'en envasador de la caja de envío a efectos de la normativa de '
        'envases. Remitir al capítulo de envases y tesorería.',
    ],
    'Qué producto viaja y cuál no': [
        'Dar el criterio verdadero, que no es jurídico sino de cadena de frío: '
        'la temperatura de conservación tiene que mantenerse durante todo el '
        'transporte hasta el consumidor final, y eso es lo que decide qué '
        'referencia se puede enviar.',
        'Traducirlo a la carta del caso modelado con la tabla de decisión: qué '
        'referencias van a vitrina refrigerada y cuáles a vitrina de ambiente, '
        'y explicar que las primeras sólo viajan con frío garantizado y dentro '
        'de su plazo.',
    ],
}

PPE_18 = {
    'La cuenta de resultados a tres años, con estacionalidad y rampa de arranque': [
        'Explicar la estructura del plan: el año uno arranca por debajo de la '
        'velocidad de crucero, el año dos es el año de crucero y el tres '
        'crece. Y explicar por qué el año uno no es una fracción del dos: hay '
        'rampa y hay estacionalidad.',
        'Dar los ingresos del año de crucero, el margen bruto y el total de '
        'costes fijos, y enseñar que la partida grande de un obrador con '
        'despacho es el personal, no la materia prima.',
        'Explicar el supuesto conservador que usa el plan: la cuenta de '
        'resultados se proyecta con la regla única de margen y no con el '
        'escandallo de las piezas, porque la regla incluye lo que el '
        'escandallo deja fuera. Remitir al capítulo del escandallo.',
    ],
    'El punto muerto con la regla única de margen': [
        'Explicar los dos puntos de equilibrio y por qué no dicen lo mismo: el '
        'contable incluye la amortización y el de caja incluye la devolución '
        'del principal del préstamo, que no es gasto pero sale de la cuenta.',
        'Dar los tickets al día que hacen falta para cada uno y la holgura '
        'sobre el equilibrio de caja en el año de crucero, y explicar cómo se '
        'lee esa holgura: es cuánto puedes caer sobre lo previsto sin entrar '
        'en pérdidas de caja.',
        'Usar como contraste el único par publicado de gastos fijos y '
        'facturación de equilibrio que cuadra con la regla única, con su '
        'fuente, y explicar por qué los demás pares que circulan no se pueden '
        'usar.',
    ],
    'El sueldo del propietario es un renglón propio': [
        'Explicarlo sin rodeos: si el sueldo del que monta el negocio no está '
        'en la cuenta de resultados, el plan miente. Dar la retribución anual '
        'del propietario del caso modelado y decir que es una celda editable.',
        'Explicar la diferencia entre retribución y beneficio, y por qué '
        'confundirlas es lo que produce el caso de facturar mucho y no ganar.',
        'Contar el caso documentado de quien facturaba una cifra alta y se '
        'quedaba con muy poco, con su fuente, y usarlo para lo que sirve: para '
        'demostrar que el margen no crece con el tamaño.',
    ],
    'La cifra honesta: entre ocho y doce por ciento neto': [
        'Dar el margen neto del año de crucero del caso modelado y la banda de '
        'referencia declarada por un profesional del sector con nombre y '
        'empresa, con su fuente.',
        'Dar los resultados netos de los tres años y explicar por qué el '
        'primero es tan bajo: la rampa y los costes fijos completos desde el '
        'primer mes.',
        'Cerrar con la advertencia de método: si tu plan sale muy por encima '
        'de esa banda, el error está en los supuestos, no en el negocio. Y '
        'decir con todas las letras que ni esa banda ni el resultado del caso '
        'modelado son una previsión de los resultados del lector.',
    ],
}

PPE_19 = {
    'Financiación y servicio de la deuda': [
        'Dar los términos del préstamo del caso modelado —principal y tipo '
        'nominal anual— y la cuota mensual que sale, y explicar que la cuota '
        'no es gasto: sólo los intereses lo son.',
        'Dar los intereses del año uno y la cobertura del servicio de la deuda '
        'más ajustada de todo el cuadro, y explicar qué mira un banco cuando '
        'la pide.',
        'Explicar la decisión que casi nadie plantea: la carencia infla la '
        'cobertura del primer año y la traslada a los siguientes, así que hay '
        'que mirar el peor año del cuadro y no el primero.',
    ],
    'El IVA por familia de producto': [
        'Dar los tipos que aplican en una pastelería con su artículo: el pan '
        'del real decreto de calidad va al tipo del cuatro por ciento y todo '
        'lo demás de la vitrina, al diez.',
        'Explicar el razonamiento correcto, que es el que sostiene la '
        'afirmación: el tipo del cuatro por ciento es una lista CERRADA de '
        'siete letras y la pastelería no está en ella, así que va al tipo '
        'general de alimentos. Dicho así es exacto y defendible.',
        'Dar la corrección que casi nadie ha incorporado: desde una resolución '
        'vinculante de la Dirección General de Tributos, TODOS los productos '
        'del real decreto del pan van al cuatro por ciento, también el pan '
        'especial y el pan sin gluten. Lo que no cambia es la frontera: el '
        'cruasán sigue al diez.',
        'Explicar el caso de la zona de degustación y el de la venta para '
        'llevar: en la mesa se presta un servicio y todo va al diez, alcohol '
        'incluido; para llevar o a domicilio, la comida sigue al diez pero la '
        'bebida alcohólica y el refresco azucarado van al general. Y decir que '
        'esto hay que montarlo en el punto de venta desde el primer día. Dar '
        'el IVA medio ponderado de la carta del caso modelado.',
    ],
    'Verifactu: las dos fechas de 2027 y el software que compras hoy': [
        'Dar las dos fechas exactas y a quién alcanza cada una: sociedades por '
        'un lado y el resto de obligados por otro. Y decir con todas las '
        'letras que no es una obligación de este año.',
        'Dar la vuelta que sí importa al montar: la obligación del fabricante '
        'del programa es anterior a la tuya, así que el punto de venta que '
        'compres hoy ya tiene que estar adaptado. Es de las primeras compras '
        'que se hacen y es la que más cara sale de cambiar.',
        'Advertir de que el calendario ya se ha aplazado dos veces, así que la '
        'fecha es un dato que hay que comprobar antes de comprar. Remitir al '
        'anexo normativo.',
    ],
    'Envases: la caja de la tarta, el táper del cliente y la bebida reutilizable': [
        'Explicar qué es un envase de servicio con su definición: la caja de '
        'la tarta, la bandeja, la bolsa y el vaso del café son envases que tú '
        'llenas en el mostrador.',
        'Dar la respuesta acotada a la pregunta cara: sí, al meter la tarta en '
        'su caja eres envasador a efectos de la norma; pero para los envases '
        'de servicio quien se inscribe en el registro es el fabricante o el '
        'distribuidor de esos envases. Lo que te toca a ti es una sola cosa: '
        'exigirle la documentación que acredita que cumple por ti y guardarla, '
        'con su número de registro en la documentación comercial.',
        'Dar las dos obligaciones que sí son tuyas: aceptar el recipiente '
        'reutilizable del cliente si vendes a granel, con el matiz de que '
        'puedes rechazarlo si no está en condiciones y de que no respondes de '
        'los problemas que se deriven; y ofrecer al menos una referencia de '
        'bebida en envase reutilizable a partir de la fecha que fija la norma '
        'si tu superficie está por debajo del umbral, con servicio de retorno.',
    ],
    'Desperdicio alimentario: de qué estás exento exactamente': [
        'Dar la fecha desde la que las obligaciones son exigibles y decir que '
        'ya lo son, sin dramatizar.',
        'Dar el alcance exacto de la exención, que es lo que casi todo el '
        'mundo escribe mal: estás exento del PLAN de prevención y del deber de '
        'promover convenios de donación —el apartado cuarto del artículo— si '
        'tu superficie no pasa del umbral; y si además eres microempresa, '
        'quedas fuera del artículo entero.',
        'Decir qué te sigue obligando en el primer caso, que es lo que nadie '
        'cuenta: aplicar las medidas de reducción, no poder firmar una '
        'cláusula que te prohíba donar —sería nula de pleno derecho— y no '
        'estropear a propósito lo que sobra.',
        'Dar la palanca comercial que va con esto y que tiene base legal '
        'propia: se puede vender producto con defecto de forma, de tamaño, de '
        'etiquetado o de envasado, informando al cliente y bajo tu '
        'responsabilidad; y lo que rebajes para no tirar producto próximo a '
        'caducar no cuenta como precio anterior a efectos de la regla de los '
        'treinta días.',
    ],
}

PPE_20 = {
    'La ruta crítica y la fecha de apertura': [
        'Explicar qué es la ruta crítica en una apertura y por qué importa: '
        'son los hitos que, si se retrasan un día, retrasan la apertura un '
        'día. Dar cuántos son en el caso modelado y la duración total del '
        'proyecto.',
        'Dar el mes de apertura que sale del cronograma del caso modelado y '
        'explicar de dónde sale: no es una fecha elegida, es el resultado de '
        'encadenar los hitos con sus dependencias.',
        'Explicar el hito que va en paralelo y por qué: el pedido y la entrega '
        'del equipamiento no espera a que acabe la obra, y esa decisión es la '
        'que puede ahorrar más semanas de todo el calendario.',
    ],
    'Abrir fuera de campaña y llegar rodado a Reyes': [
        'Dar el criterio: abrir dentro de una campaña es el peor escenario '
        'posible, porque se estrena equipo, plantilla y proveedores el día que '
        'más producción hay. El cronograma avisa si la fecha cae dentro de una '
        'campaña.',
        'Explicar la estrategia completa: abrir con margen suficiente antes de '
        'la campaña grande para llegar con el obrador rodado y con el '
        'cuadrante probado. Remitir al capítulo de las campañas.',
        'Dar el aviso del cronograma del caso modelado sobre su mes de '
        'apertura y qué margen deja hasta la primera campaña.',
    ],
    'La libertad horaria por ley como decisión comercial del primer día': [
        'Dar la palanca con su base: los establecimientos dedicados '
        'principalmente a la venta de pastelería y repostería tienen plena '
        'libertad para determinar los días y las horas en que abren, en todo '
        'el territorio nacional, y no consumen ninguno de los domingos '
        'habilitados.',
        'Dar el matiz que hace que la palanca sea real o no: la ley exige que '
        'la venta de pastelería sea la actividad PRINCIPAL, así que una '
        'pastelería con cafetería que facture más de cafetería puede quedarse '
        'fuera del régimen. Es una decisión de modelo de negocio, no de '
        'horario.',
        'Sacar la decisión comercial: el domingo es el día de la tarta, y '
        'decidir si se abre y con qué plantilla es una decisión del primer '
        'día, no del segundo año. Remitir al capítulo de turnos.',
    ],
    'Qué se mide en el mes cero y en el mes tres': [
        'Dar el cuadro de arranque: qué se mide el primer mes, con qué '
        'frecuencia y quién es el responsable de cada medición. Sin '
        'indicadores no hay corrección posible.',
        'Explicar el ajuste del mes tres: con tres meses de datos ya se puede '
        'corregir el mix de la carta, la producción por referencia y el '
        'cuadrante. Y remitir a las herramientas del pack que se rellenan con '
        'esos datos.',
        'Cerrar el documento con la frontera y con el siguiente paso: a partir '
        'de aquí el negocio ya está abierto, y lo que viene —el plan de '
        'producción semanal, el control de encargos, los registros diarios— lo '
        'entrega el Kit de Tareas Pastelería, con la ingeniería de carta en la '
        'Guía Food Cost y los registros de autocontrol en el Pack APPCC.',
    ],
}

PPE_21 = {
    'Qué está vigente y qué está derogado': [
        'Explicar para qué sirve este anexo: es la foto del estado normativo '
        'el día que se cerró la edición, para que el lector pueda comprobar '
        'por su cuenta qué sigue en pie cuando vuelva al documento dentro de '
        'un año.',
        'Recorrer las normas que sostienen la guía diciendo de cada una su '
        'estado y su última modificación, sin repetir el contenido: aquí no se '
        'explica qué dice cada norma, se dice si sigue viva.',
        'Advertir del caso de la norma de calidad de pastelería, que lleva '
        'muchos años sin una sola modificación y cuyo apartado de etiquetado '
        'remite a una norma anterior al reglamento europeo de información al '
        'consumidor: se cita para las definiciones, no para el etiquetado.',
        'Dar el aviso de alcance: sólo se ha verificado el estado de tres '
        'comunidades autónomas, así que el cuadro autonómico no puede '
        'presentarse como completo.',
    ],
    'Las fechas que ya sabemos que se mueven': [
        'Presentar las fechas de caducidad conocidas y por qué se agrupan '
        'aquí y no dentro de los capítulos: para que la edición siguiente se '
        'arregle cambiando un bloque y no veinte capítulos.',
        'Explicar qué se rompe con cada una: la tabla salarial y el salario '
        'mínimo se renuevan cada año, el calendario de facturación tiene dos '
        'fechas escalonadas, la obligación de bebida en envase reutilizable '
        'pasa de futura a presente, el período transitorio de una comunidad '
        'autónoma vence, y el calendario de accesibilidad de bienes y '
        'servicios privados tiene dos fechas, 2029 para los establecimientos '
        'nuevos y 2030 para los ya existentes: cinco bloques y siete fechas, '
        'y el recuento tiene que cuadrar con la tabla.',
        'Dar la regla de uso: todas esas cifras viven en celda de parámetro en '
        'los libros, nunca cosidas en la prosa, y por eso cambiar una no '
        'obliga a rehacer nada más.',
    ],
    'Las normas que la SERP sigue citando y están muertas': [
        'Explicar el problema y por qué merece su propio apartado: hay '
        'contenidos gratuitos muy bien posicionados que siguen citando normas '
        'derogadas, y quien las lee monta su obrador sobre una regla que ya no '
        'existe.',
        'Enumerar las derogadas con el año de la derogación y con la norma que '
        'las sustituye, y decir en cada caso qué regla falsa produce cada una '
        'de ellas.',
        'Dar el caso más peligroso de los cinco: el de las temperaturas y el '
        'plazo del huevo, porque la regla derogada es más laxa que la vigente '
        'y quien la aplica se queda corto justo en el punto que más mira una '
        'inspección.',
    ],
    'Cómo abrir la ficha de vigencia del Boletín Oficial del Estado en un minuto': [
        'Dar el procedimiento paso a paso, sin capturas: cómo se llega al '
        'texto consolidado de una norma, dónde está la línea de última '
        'modificación y cómo se leen las notas de vigencia de un artículo '
        'concreto.',
        'Dar el consejo que ahorra errores: se comprueba el artículo, no la '
        'norma. Una norma puede estar vigente y tener ese artículo modificado '
        'o derogado, y es exactamente lo que ha pasado con varias de las que '
        'aparecen en esta guía.',
    ],
}


CAPITULOS += [
    {
        'n': 15,
        'titulo': 'Los Seis Picos del Año',
        'resumen_indice': 'el multiplicador de la campaña, cuánto pesa cada una sobre el año, el déficit de capacidad y el refuerzo, la tesorería inmovilizada y qué se puede desestacionalizar.',
        'palabras': 1800, 'bloques': 2,
        'objetivo': 'Que el lector sepa si aguanta la campaña grande antes de '
                    'que llegue, y que vea el dinero que cada campaña '
                    'inmoviliza además del que le hace ganar.',
        'epigrafes': list(PPE_15),
        'puntos_por_epigrafe': PPE_15,
        'puntos_globales': [
            'Este capítulo NO repite el calendario de tareas por campaña: las '
            'fechas y el qué hacer los da el Kit de Tareas Pastelería. Aquí '
            'van los euros, la capacidad y la caja.',
            'Se distingue siempre entre facturación de la campaña y '
            'facturación INCREMENTAL: la segunda es la que añade la campaña '
            'sobre lo que se habría vendido igualmente.',
            'Los factores de campaña del caso modelado son supuestos '
            'calibrados con casos publicados, y se dicen supuestos.',
        ],
        'cifras': [
            C('Peso de las seis campañas sobre las ventas del año', f'{X_EST}!Peso sobre el Año!D30', 'pct1'),
            C('Facturación de las seis campañas sin IVA', f'{X_EST}!Calendario de 6 Picos!N13', 'eur'),
            C('Facturación incremental de las seis campañas', f'{X_EST}!Calendario de 6 Picos!O13', 'eur'),
            C('Peso de la campaña de Reyes sobre las ventas del año', f'{X_EST}!Peso sobre el Año!D24', 'pct1'),
            C('Cuántas veces factura un día de Reyes lo que un día normal', f'{X_EST}!Peso sobre el Año!I24', 'num1'),
            C('Demanda de piezas al día en Reyes', f'{X_EST}!Capacidad vs Demanda del Pico!D6', 'num'),
            C('Déficit diario de piezas en Reyes', f'{X_EST}!Capacidad vs Demanda del Pico!H6', 'num'),
            C('Campañas que no aguanta el obrador del caso modelado', f'{X_EST}!Capacidad vs Demanda del Pico!N13', 'num'),
            C('Coste del refuerzo de todo el año', f'{X_EST}!Refuerzo y Tesorería!F13', 'eur2'),
            C('Tesorería inmovilizada en materia de campaña', f'{X_EST}!Refuerzo y Tesorería!K13', 'eur2'),
        ],
        'sector': ['PS-41', 'PS-35', 'PS-36', 'PS-37', 'PS-38', 'PS-44', 'PS-46'],
        'tablas': [
            {
                'titulo': 'Lo que pesa cada campaña sobre el año (estacionalidad-y-picos.xlsx, hoja «Peso sobre el Año»)',
                'src': (X_EST, 'Peso sobre el Año'),
                'cols': [('Campaña', 'A', 'txt'), ('Días de campaña', 'B', 'num'),
                         ('Facturación de la campaña sin IVA (€)', 'C', 'eur'),
                         ('Parte del año (%)', 'D', 'pct1'),
                         ('Facturación incremental sin IVA (€)', 'E', 'eur'),
                         ('Euros por día de campaña', 'G', 'eur'),
                         ('Veces que factura un día normal', 'I', 'num1')],
                'filas': (24, 30),
                'nota': 'La facturación de la campaña incluye lo que se habría vendido igual; '
                        'la incremental es lo que añade la campaña. Para decidir refuerzo y '
                        'compra manda la incremental.',
            },
            {
                'titulo': 'Capacidad contra demanda, campaña a campaña (estacionalidad-y-picos.xlsx, hoja «Capacidad vs Demanda del Pico»)',
                'src': (X_EST, 'Capacidad vs Demanda del Pico'),
                'cols': [('Campaña', 'A', 'txt'), ('Factor sobre el crucero', 'C', 'num1'),
                         ('Demanda de piezas al día', 'D', 'num'),
                         ('Capacidad en campaña', 'G', 'num'),
                         ('Déficit diario', 'H', 'num'),
                         ('Horas de obrador que harían falta', 'M', 'num1'),
                         ('¿Aguantas?', 'N', 'txt'),
                         ('Personas de refuerzo necesarias', 'P', 'num')],
                'filas': (6, 11),
                'nota': 'La capacidad en campaña ya cuenta con el turno alargado. Cuando las '
                        'horas que harían falta se van por encima de las que tiene un día, la '
                        'campaña no cabe ni trabajando el día entero: hay que adelantar '
                        'producción con frío o limitar el encargo.',
            },
            {
                'titulo': 'Lo que cuesta cada campaña y lo que inmoviliza (estacionalidad-y-picos.xlsx, hoja «Refuerzo y Tesorería»)',
                'src': (X_EST, 'Refuerzo y Tesorería'),
                'cols': [('Campaña', 'A', 'txt'), ('Personas de refuerzo', 'B', 'num'),
                         ('Personas que pediría el déficit', 'G', 'num'),
                         ('¿Cubre el refuerzo?', 'H', 'txt'),
                         ('Horas totales de refuerzo', 'D', 'num'),
                         ('Coste del refuerzo (€)', 'F', 'eur2'),
                         ('Compra de materia de la campaña (€)', 'K', 'eur2'),
                         ('Días con el dinero parado', 'M', 'num'),
                         ('Resultado incremental (€)', 'Q', 'eur2')],
                'filas': (6, 11),
                'nota': 'Las personas de refuerzo son las que CONTRATAS; las que pediría el '
                        'déficit son las que haría falta meter para cerrarlo entero. Cuando '
                        'no coinciden no es un descuadre, es una decisión: en San Valentín se '
                        'cubre con la plantilla base y en Reyes se acepta quedarse una '
                        'persona corto y compensarlo adelantando producción con frío. El '
                        'coste hora del refuerzo es coste de EMPRESA, con la Seguridad Social '
                        'dentro, no bruto. Y el resultado incremental descuenta el refuerzo, '
                        'la materia de las unidades incrementales y el coste financiero del '
                        'dinero parado.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No repitas el calendario de tareas por campaña: lo entrega el Kit '
            'de Tareas Pastelería y aquí se cita.',
            'No des ninguna cifra de variación de ventas por festividad que no '
            'esté en los datos del sector del capítulo.',
            'No presentes los factores de campaña como datos del sector: son '
            'supuestos calibrados del caso modelado.',
        ],
    },
    {
        'n': 16,
        'titulo': 'Encargos y Comuniones como Línea de Negocio',
        'resumen_indice': 'captación y demanda validada, anticipo y señal, calendario de entrega y riesgo de anulación, y qué se acepta sin histórico.',
        'palabras': 1700, 'bloques': 1,
        'objetivo': 'Que el lector monte el canal de encargos como una línea de '
                    'negocio con su margen, su anticipo y su política de '
                    'anulación, en vez de aceptarlos según llegan.',
        'epigrafes': list(PPE_16),
        'puntos_por_epigrafe': PPE_16,
        'puntos_globales': [
            'La ficha de encargo, el registro y la agenda los entrega el Kit '
            'de Tareas Pastelería: aquí se decide el modelo de negocio del '
            'canal, nunca la herramienta.',
            'Los porcentajes de anticipo y de anulación son criterios de la '
            'casa, no norma, y se dicen como tales.',
            'Todo lo que se decida aquí tiene que caber en la capacidad del '
            'obrador del día concreto: se remite al capítulo de las campañas '
            'en vez de repetir sus cifras.',
        ],
        'cifras': [
            C('Peso del canal de encargos sobre las ventas', f'{X_PLAN}!Canales y Punto Muerto!B7', 'pct0'),
            C('Margen bruto del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!C7', 'pct0'),
            C('Coste de servir del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!D7', 'pct0'),
            C('Margen de contribución del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!G7', 'pct0'),
            C('Ventas anuales del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!H7', 'eur'),
            C('Margen de contribución en euros del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!I7', 'eur'),
            C('Facturación sin IVA de la campaña de comuniones', f'{X_EST}!Calendario de 6 Picos!N10', 'eur2'),
            C('Días que dura la campaña de comuniones', f'{X_EST}!Calendario de 6 Picos!E10', 'num'),
            C('Días con el dinero parado en la campaña de comuniones', f'{X_EST}!Refuerzo y Tesorería!M10', 'num'),
        ],
        'sector': ['PS-53', 'PS-44', 'PS-46'],
        'tablas': [
            {
                'titulo': 'Qué encargo se acepta y cuál no cuando todavía no tienes histórico',
                'cabecera': ['Tipo de encargo', '¿Se acepta el primer año?', 'Condición para aceptarlo'],
                'filas': [
                    ['Tarta por raciones de la carta habitual', 'Sí', 'Con anticipo y con la referencia ya escandallada'],
                    ['Tarta personalizada con decoración nueva', 'Sí, con límite semanal', 'Se cuenta el tiempo real de montaje y se cobra como mano de obra'],
                    ['Encargo en día de campaña', 'Sólo hasta el cupo del día', 'El cupo sale de la capacidad del obrador de ese día, no del calendario'],
                    ['Encargo con montaje en el lugar del evento', 'No', 'Sin histórico no se puede estimar el tiempo ni el riesgo de transporte'],
                    ['Entrega con hora cerrada en día de campaña', 'No', 'Comprometer una hora concreta el día de más producción es asumir el fallo'],
                    ['Volumen que obliga a comprar formato que no usas', 'No', 'El sobrante de ese formato se queda en el almacén todo el año'],
                    ['Encargo de producto que no está en la carta', 'No', 'Sin escandallo no hay precio, y sin precio hay regalo'],
                ],
                'nota': 'Es una política de partida, no una norma: se revisa a los seis meses '
                        'con las horas reales anotadas de cada encargo aceptado.',
            },
            {
                'titulo': 'El canal de encargos dentro del mix de canales (plan-financiero-3-anos-pasteleria.xlsx, hoja «Canales y Punto Muerto»)',
                'src': (X_PLAN, 'Canales y Punto Muerto'),
                'cols': [('Canal', 'A', 'txt'),
                         ('Ventas del año de crucero (€)', 'H', 'eur'),
                         ('Parte de las ventas (%)', 'B', 'pct0'),
                         ('Margen bruto (%)', 'C', 'pct0'),
                         ('Coste de servir (%)', 'D', 'pct0'),
                         ('Margen de contribución (%)', 'G', 'pct0'),
                         ('Margen de contribución (€)', 'I', 'eur'),
                         ('Días de cobro', 'F', 'num')],
                'filas': (6, 10),
                'nota': 'El reparto entre canales es un supuesto del caso modelado salvo el '
                        'peso del suministro a otras tiendas, que sale de un caso publicado. El '
                        'anticipo del encargo no aparece como margen: aparece como días de '
                        'cobro.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No rehagas la ficha ni el registro de encargos: los entrega el '
            'Kit de Tareas Pastelería.',
            'No des ningún precio por ración ni ningún importe de anticipo que '
            'no salga de las cifras del capítulo.',
            'No prometas que el encargo es siempre más rentable que el '
            'mostrador: depende del coste de servir, y el libro lo calcula.',
        ],
    },
    {
        'n': 17,
        'titulo': 'Canales: Mostrador, Encargos, B2B y Envío',
        'resumen_indice': 'cobro al contado frente a cobro a crédito, cuándo el suministro a otras tiendas te obliga a inscribirte, la venta a distancia y qué producto puede viajar.',
        'palabras': 1800, 'bloques': 2,
        'objetivo': 'Que el lector sepa qué canal le sostiene el negocio, qué '
                    'canal le cambia el régimen de registro y qué producto de '
                    'su carta puede enviar sin romper la cadena de frío.',
        'epigrafes': list(PPE_17),
        'puntos_por_epigrafe': PPE_17,
        'puntos_globales': [
            'La estructura del artículo que regula el suministro a otras '
            'tiendas se aplica aquí, no se vuelve a explicar: se remite al '
            'capítulo de licencias y se usa con el número del plan.',
            'De venta a distancia sólo se afirma lo verificado: régimen de '
            'registro, información antes de la compra y cadena de frío. Nada '
            'de desistimiento, de protección de datos ni de comercio '
            'electrónico.',
            'Cada canal se juzga por su margen de CONTRIBUCIÓN, no por su '
            'margen bruto: la diferencia es el coste de servir y de cobrar.',
        ],
        'cifras': [
            C('Margen de contribución medio ponderado de todos los canales', f'{X_PLAN}!Canales y Punto Muerto!B15', 'pct1'),
            C('Lo que se llevan servir, cobrar y las comisiones', f'{X_PLAN}!Canales y Punto Muerto!B17', 'pct1'),
            C('Punto muerto mensual con todos los canales', f'{X_PLAN}!Canales y Punto Muerto!B18', 'eur2'),
            C('Punto muerto mensual sin el canal de suministro a otras tiendas', f'{X_PLAN}!Canales y Punto Muerto!B19', 'eur2'),
            C('Diferencia del punto muerto al quitar ese canal', f'{X_PLAN}!Canales y Punto Muerto!B20', 'eur2'),
            C('Aporte del canal que sostiene el negocio', f'{X_PLAN}!Canales y Punto Muerto!B22', 'pct1'),
            C('Peso del suministro a otras tiendas sobre las ventas', f'{X_PLAN}!Canales y Punto Muerto!B25', 'pct0'),
            C('Días medios de cobro ponderados', f'{X_PLAN}!Canales y Punto Muerto!B29', 'num2'),
            C('Margen de contribución del canal de venta online y envío', f'{X_PLAN}!Canales y Punto Muerto!G9', 'pct0'),
            C('Temperatura que manda en el producto de pastelería relleno', f'{X_CARTA}!Parámetros!B28', 'num'),
        ],
        'sector': ['PS-53', 'PA-01b', 'PA-02', 'PA-02b', 'PA-27', 'PA-27b', 'PA-28'],
        'tablas': [
            {
                'titulo': 'Los cuatro canales, con su margen de contribución y sus días de cobro (plan-financiero-3-anos-pasteleria.xlsx, hoja «Canales y Punto Muerto»)',
                'src': (X_PLAN, 'Canales y Punto Muerto'),
                'cols': [('Canal', 'A', 'txt'),
                         ('Ventas del año de crucero (€)', 'H', 'eur'),
                         ('Parte de las ventas (%)', 'B', 'pct0'),
                         ('Margen bruto (%)', 'C', 'pct0'),
                         ('Coste de servir (%)', 'D', 'pct0'),
                         ('Comisión de plataforma (%)', 'E', 'pct0'),
                         ('Margen de contribución (%)', 'G', 'pct0'),
                         ('Días de cobro', 'F', 'num')],
                'filas': (6, 10),
                'nota': 'Los porcentajes de esta hoja son supuestos del caso modelado salvo el '
                        'peso del suministro a otras tiendas, que sale de un caso publicado. La '
                        'comisión de plataforma va a cero porque el canal online del caso es '
                        'web propia.',
            },
            {
                'titulo': 'Qué referencia puede viajar y cuál no, según su temperatura y su plazo (carta-de-apertura-y-escandallo.xlsx, hoja «Decisión de Huevo y Temperatura»)',
                'src': (X_CARTA, 'Decisión de Huevo y Temperatura'),
                'cols': [('Ref', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Vía legal del huevo', 'D', 'txt'),
                         ('¿Estable a temperatura ambiente?', 'F', 'txt'),
                         ('Temperatura de conservación (grados)', 'I', 'num'),
                         ('Plazo legal en horas', 'K', 'num'),
                         ('Dónde va en el mostrador', 'M', 'txt')],
                'filas': (6, 35),
                'nota': V_TEMP + ' — el plazo legal es el del artículo 9.3 y sólo alcanza a lo '
                        'elaborado por su vía; la vida útil de las demás referencias la '
                        'declaras tú en tu plan de autocontrol. Lo que va a vitrina refrigerada '
                        'sólo viaja con frío garantizado durante todo el transporte.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No afirmes nada sobre derecho de desistimiento, protección de '
            'datos ni comercio electrónico: no está verificado en esta '
            'edición.',
            'No repitas el error del tope en kilos ni presentes las dos vías '
            'de «marginal» como si fueran acumulativas.',
            'No des el radio entre comunidades autónomas como si aplicase a la '
            'venta al consumidor final: no le aplica.',
        ],
    },
    {
        'n': 18,
        'titulo': 'El Plan Financiero y el Dinero Hasta el Punto de Equilibrio',
        'resumen_indice': 'la cuenta de resultados a tres años con rampa y estacionalidad, el punto muerto contable y el de caja, el sueldo del propietario y la cifra honesta de rentabilidad.',
        'palabras': 1850, 'bloques': 2,
        'objetivo': 'Que el lector vea la rentabilidad real de una pastelería y '
                    'no la de folleto: qué gana el año uno, cuándo llega al '
                    'equilibrio y cuánta holgura tiene sobre él.',
        'epigrafes': list(PPE_18),
        'puntos_por_epigrafe': PPE_18,
        'puntos_globales': [
            'Ninguna cifra de este capítulo es una previsión de los resultados '
            'del lector, y se dice al menos una vez con esas palabras.',
            'El punto muerto se calcula SIEMPRE con la regla única de margen. '
            'Los escenarios de terceros que implican márgenes incompatibles '
            'con esa regla no entran.',
            'El sueldo del propietario aparece como renglón propio en todas '
            'las lecturas del resultado, no escondido en el beneficio.',
        ],
        'cifras': [
            C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
            C('Margen bruto del año de crucero', f'{X_PLAN}!PyG 3 Años!C17', 'eur'),
            C('Total de costes fijos del año de crucero', f'{X_PLAN}!PyG 3 Años!C33', 'eur'),
            C('Resultado neto del año uno', f'{X_PLAN}!PyG 3 Años!B43', 'eur'),
            C('Resultado neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C43', 'eur'),
            C('Margen neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C50', 'pct1'),
            C('Retribución anual del propietario', f'{X_PLAN}!PyG 3 Años!C20', 'eur'),
            C('Tickets al día para el equilibrio contable', f'{X_PLAN}!Punto de Equilibrio!C16', 'num1'),
            C('Tickets al día para el equilibrio de caja', f'{X_PLAN}!Punto de Equilibrio!C22', 'num1'),
            C('Holgura sobre el equilibrio de caja en el año de crucero', f'{X_PLAN}!Punto de Equilibrio!C26', 'pct1'),
        ],
        'sector': ['PS-48', 'PS-58', 'PS-62', 'PS-97', 'PS-51', 'PS-52'],
        'tablas': [
            {
                'titulo': 'La cuenta de resultados a tres años del caso modelado (plan-financiero-3-anos-pasteleria.xlsx, hoja «PyG 3 Años»)',
                'src': (X_PLAN, 'PyG 3 Años'),
                'cols': [('Concepto', 'A', 'txt'), ('Año 1 (arranque)', 'B', 'eur'),
                         ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur'),
                         ('Parte de las ventas del año 2 (%)', 'E', 'pct1')],
                'filas': (11, 36),
                # B12 (2026-09-10): las dos filas de IVA soportado iban entre
                # TOTAL COSTES FIJOS y el resultado sin participar en la resta.
                # Quien las sumaba obtenía otro número.
                'omitir_filas': (34, 35),
                'nota': 'Todas las cifras van sin IVA. El coste de ventas se proyecta con la '
                        'regla única de margen, no con el escandallo de las piezas: es el '
                        'supuesto conservador, y la diferencia entre los dos números es tu '
                        'colchón.',
            },
            {
                'titulo': 'Memoria de IVA soportado, que no afecta al resultado (plan-financiero-3-anos-pasteleria.xlsx, hoja «PyG 3 Años»)',
                'src': (X_PLAN, 'PyG 3 Años'),
                'cols': [('Concepto', 'A', 'txt'), ('Año 1 (arranque)', 'B', 'eur'),
                         ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                'filas': (34, 35),
                'nota': 'Va aparte a propósito: la cuenta de resultados de arriba está sin '
                        'IVA de principio a fin y estas dos líneas no entran en ninguna de '
                        'sus restas. Se publican porque el IVA soportado SÍ sale de la caja '
                        'y hay que tenerlo previsto, que es lo que mide la hoja de tesorería.',
            },
            {
                'titulo': 'Los tres escenarios, con la misma plantilla y los mismos fijos (plan-financiero-3-anos-pasteleria.xlsx, hoja «Escenarios»)',
                'src': (X_PLAN, 'Escenarios'),
                'cols': [('Métrica', 'A', 'txt'), ('Pesimista', 'B', 'eur'),
                         ('Realista', 'C', 'eur'), ('Optimista', 'D', 'eur')],
                'filas': (9, 17),
                'nota': 'Los dos extremos son SUPUESTOS; la columna del medio lee el año de '
                        'crucero del plan. Los costes fijos no cambian entre escenarios porque '
                        'la plantilla es la misma: por eso el pesimista duele tanto.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No uses ningún escenario de gastos fijos y facturación de '
            'equilibrio que implique un margen distinto de la regla única del '
            'producto.',
            'No des ninguna facturación media por pastelería ni ningún rango '
            'de facturación anual del sector.',
            'No presentes la banda de rentabilidad neta como una promesa: es '
            'una referencia declarada por un profesional con nombre, y se cita '
            'así.',
        ],
    },
    {
        'n': 19,
        'titulo': 'Financiación, IVA, Envases y Tesorería del Arranque',
        'resumen_indice': 'el servicio de la deuda, los tipos de IVA por familia y por canal, las dos fechas de la facturación verificable, los envases y el alcance real de la exención de desperdicio.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector no se estrelle en el primer trimestre: que '
                    'sepa qué le cuesta la deuda, qué IVA repercute en cada '
                    'línea y en cada canal, qué le obliga en envases y de qué '
                    'está exento exactamente en desperdicio alimentario.',
        'epigrafes': list(PPE_19),
        'puntos_por_epigrafe': PPE_19,
        'puntos_globales': [
            'Cada afirmación fiscal y de envases va con su artículo y con la '
            'fecha de comprobación. Es, con el capítulo de licencias, el otro '
            'capítulo que no admite una frase sin referencia.',
            'Las fechas que se mueven no se cosen en la prosa: se dan con su '
            'norma y se remite al anexo normativo, que es donde se '
            'actualizarán.',
            'De la exención de desperdicio se da SIEMPRE el alcance exacto por '
            'apartados, nunca «estás exento» a secas.',
        ],
        'cifras': [
            C('Principal del préstamo del caso modelado', f'{X_PLAN}!0. Supuestos!B37', 'eur'),
            C('Tipo de interés nominal anual', f'{X_PLAN}!0. Supuestos!B38', 'pct1'),
            C('Cuota mensual del préstamo', f'{X_PLAN}!Financiación!B22', 'eur2'),
            C('Intereses del año uno', f'{X_PLAN}!Financiación!B116', 'eur2'),
            C('Cobertura del servicio de la deuda más ajustada del cuadro', f'{X_PLAN}!Financiación!B123', 'num2'),
            C('IVA soportado que hay que adelantar en la inversión', f'{X_CAPEX}!IVA y Tesorería!B18', 'eur'),
            C('Meses hasta recuperar ese IVA', f'{X_CAPEX}!IVA y Tesorería!B17', 'num'),
            C('Tipo de IVA de la pastelería y la bollería', f'{X_CARTA}!Parámetros!B19', 'pct0'),
            C('Tipo de IVA del pan', f'{X_CARTA}!Parámetros!B20', 'pct0'),
            C('IVA medio ponderado de la carta del caso modelado', f'{X_PLAN}!0. Supuestos!B20', 'pct1'),
        ],
        'sector': ['PA-36', 'PA-36b', 'PA-36c', 'PA-36d', 'PA-37', 'PA-30',
                   'PA-30b', 'PA-30c', 'PA-31', 'PA-31b'],
        'tablas': [
            {
                'titulo': 'El IVA de la inversión, bloque a bloque, y cuándo vuelve (calculadora-capex-pasteleria.xlsx, hoja «IVA y Tesorería»)',
                'src': (X_CAPEX, 'IVA y Tesorería'),
                'cols': [('Bloque', 'A', 'txt'), ('Base sin IVA (€)', 'B', 'eur'),
                         ('IVA soportado (€)', 'C', 'eur'),
                         ('Total con IVA (€)', 'D', 'eur')],
                'filas': (6, 14),
                'nota': 'La fianza, las tasas y el fondo de maniobra no llevan IVA. El IVA que '
                        'aparece aquí lo adelantas tú y vuelve con la declaración del período, '
                        'así que es caja aunque no sea coste.',
            },
            {
                'titulo': 'El servicio de la deuda año a año y su cobertura (plan-financiero-3-anos-pasteleria.xlsx, hoja «Financiación»)',
                'src': (X_PLAN, 'Financiación'),
                'cols': [('Año', 'A', 'txt'), ('Intereses (€)', 'B', 'eur2'),
                         ('Principal devuelto (€)', 'C', 'eur2'),
                         ('Cuota total (€)', 'D', 'eur2'),
                         ('Flujo disponible para la deuda (€)', 'E', 'eur2'),
                         ('Cobertura del servicio de la deuda', 'F', 'num2')],
                'filas': (116, 122),
                'nota': 'Sólo los intereses son gasto de la cuenta de resultados; el principal '
                        'devuelto sale de la caja y no aparece en el resultado. En este caso '
                        'el equilibrio de caja queda POR DEBAJO del contable, porque la '
                        'amortización que se descuenta pesa más que el principal que se '
                        'añade.',
            },
            {
                'titulo': 'Qué tipo de IVA repercutes en cada línea y en cada canal',
                'cabecera': ['Qué vendes', 'Dónde o cómo', 'Tipo', 'Base normativa'],
                'filas': [
                    ['Pan común, pan especial y semielaborados del RD 308/2019, con o sin gluten', 'Mostrador o para llevar', '4 %', 'Art. 91.Dos.1.1 letra a de la Ley 37/1992 y Resolución vinculante de la DGT de 24-02-2025'],
                    ['Bollería, pastelería, confitería, repostería y chocolate', 'Mostrador o para llevar', '10 %', 'Art. 91.Uno.1.1 de la Ley 37/1992: el 4 % es lista cerrada y no los incluye'],
                    ['Café, infusión y cualquier producto consumido en la mesa', 'Zona de degustación', '10 %', 'Art. 91.Uno.2.2 de la Ley 37/1992: es servicio de hostelería'],
                    ['Cerveza, vino y refresco azucarado consumidos en la mesa', 'Zona de degustación', '10 %', 'Art. 91.Uno.2.2 de la Ley 37/1992: el servicio no excluye ninguna bebida'],
                    ['Cerveza, vino y refresco azucarado', 'Para llevar o a domicilio', '21 %', 'Exclusiones del art. 91.Uno.1.1 y art. 90.Uno de la Ley 37/1992'],
                    ['Comida y pastelería', 'Para llevar o a domicilio', '10 %', 'Art. 91.Uno.1.1 de la Ley 37/1992: es entrega de bienes de alimentación'],
                ],
                'nota': V_IVA + ' — la misma botella cambia de tipo según dónde se la beba el '
                        'cliente, y eso hay que tenerlo montado en el punto de venta desde el '
                        'primer día.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No digas que el pan especial va al tipo del diez por ciento.',
            'No des ninguna fecha de la facturación verificable distinta de '
            'las dos que fija la norma, ni una fecha concreta para el '
            'fabricante del programa.',
            'No escribas «tu pastelería está exenta del artículo 6» a secas ni '
            '«la ley te obliga a un plan de prevención»: el alcance va por '
            'apartados.',
            'No digas que tienes que inscribirte en el registro de productores '
            'por envasar tu producto, ni que la normativa de envases no te '
            'afecta.',
        ],
    },
    {
        'n': 20,
        'titulo': 'Cronograma, Apertura y los Primeros Noventa Días',
        'resumen_indice': 'la ruta crítica y la fecha de apertura, por qué se abre fuera de campaña, la libertad horaria como decisión comercial y qué se mide en el mes cero y en el mes tres.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector ponga fecha, responsable y métrica: que sepa '
                    'cuándo puede abrir de verdad, qué hito no puede '
                    'retrasarse y qué va a medir los tres primeros meses.',
        'epigrafes': list(PPE_20),
        'puntos_por_epigrafe': PPE_20,
        'puntos_globales': [
            'Los plazos del cronograma son supuestos de planificación, no '
            'plazos legales de resolución, y se dice: el de la licencia '
            'depende de cada ayuntamiento.',
            'Este es el capítulo de cierre del documento: termina remitiendo a '
            'las herramientas del día a día, con la frontera dicha en una '
            'frase.',
            'Cada indicador del cuadro de arranque lleva responsable y '
            'frecuencia; un indicador sin dueño no se mide.',
        ],
        'cifras': [
            C('Duración total del proyecto, en meses', f'{X_LEGAL}!Cronograma y Ruta Crítica!C38', 'num1'),
            C('Hitos que están en la ruta crítica', f'{X_LEGAL}!Cronograma y Ruta Crítica!C39', 'num'),
            C('Mes natural en el que abre el caso modelado', f'{X_LEGAL}!Cronograma y Ruta Crítica!C40', 'num'),
            C('Trámites del expediente completo', f'{X_LEGAL}!Checklist Legal (F1-F6)!D55', 'num'),
            C('Coste previsto total del expediente y de la obra', f'{X_LEGAL}!Checklist Legal (F1-F6)!D59', 'eur'),
            C('Trámites sin importe conocido todavía', f'{X_LEGAL}!Checklist Legal (F1-F6)!D62', 'num'),
            C('Plazo crítico de entrega del equipamiento, en semanas', f'{X_EQUIP}!Equipamiento!I53', 'num'),
            C('Margen de ese plazo crítico hasta la apertura, en semanas', f'{X_EQUIP}!Equipamiento!I55', 'num'),
        ],
        'sector': ['PA-39', 'PA-40', 'PA-04'],
        'tablas': [
            {
                'titulo': 'Los doce hitos de la apertura, con su duración, su holgura y su ruta crítica (checklist-legal-y-licencias.xlsx, hoja «Cronograma y Ruta Crítica»)',
                'src': (X_LEGAL, 'Cronograma y Ruta Crítica'),
                'cols': [('Id', 'A', 'txt'), ('Hito', 'B', 'txt'),
                         ('Duración (meses)', 'C', 'num1'),
                         ('Depende de', 'D', 'txt'),
                         ('Empieza (mes del proyecto)', 'G', 'num1'),
                         ('Acaba (mes del proyecto)', 'H', 'num1'),
                         ('Holgura (meses)', 'I', 'num1'),
                         ('¿Ruta crítica?', 'J', 'txt'),
                         ('Mes natural de fin', 'K', 'txt')],
                'filas': (9, 20),
                'nota': 'Las duraciones son supuestos de planificación. El único hito con '
                        'holgura del caso modelado es el pedido de equipamiento, porque va en '
                        'paralelo a la obra: todos los demás son ruta crítica y retrasan la '
                        'apertura día por día.',
            },
            {
                'titulo': 'Qué se mide en el mes cero y en el mes tres, con responsable y frecuencia',
                'cabecera': ['Qué se mide', 'Cuándo', 'Con qué herramienta del pack', 'Quién responde'],
                'filas': [
                    ['Piezas producidas al día contra la capacidad del cuello de botella', 'Diario desde el día uno', 'capacidad-obrador-y-local.xlsx', 'Jefe Pastelero'],
                    ['Tickets al día y ticket medio', 'Semanal desde el día uno', 'plan-financiero-3-anos-pasteleria.xlsx', 'Propietario'],
                    ['Mix real de la carta contra el mix previsto', 'Mensual desde el mes uno', 'carta-de-apertura-y-escandallo.xlsx', 'Propietario'],
                    ['Horas planificadas contra horas reales', 'Semanal desde el día uno', 'plantilla-turnos-y-coste-personal.xlsx', 'Propietario'],
                    ['Desviación del gasto real contra el CAPEX previsto', 'Al cierre de la obra', 'calculadora-capex-pasteleria.xlsx', 'Propietario'],
                    ['Saldo de caja contra la previsión mensual', 'Mensual desde el mes uno', 'plan-financiero-3-anos-pasteleria.xlsx', 'Propietario'],
                    ['Referencias con veredicto de retirar o revisar precio', 'Al cierre del mes tres', 'carta-de-apertura-y-escandallo.xlsx', 'Propietario'],
                    ['Encargos aceptados con sus horas reales', 'Mensual desde el mes uno', 'Kit de Tareas Pastelería', 'Jefe Pastelero'],
                ],
                'nota': 'Con tres meses de datos ya se puede corregir el mix, la producción por '
                        'referencia y el cuadrante. Antes de eso, cualquier cambio es una '
                        'corazonada.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No des ningún plazo de resolución de licencia como si fuera '
            'general: depende de cada ayuntamiento y es un supuesto de '
            'planificación.',
            'No digas que hay que pedir permiso para abrir en domingo, y no '
            'des ningún número mínimo de domingos habilitados.',
            'No cierres el documento prometiendo resultados ni resumiendo lo '
            'ya dicho: se cierra con la acción siguiente y con la frontera.',
        ],
    },
    {
        'n': 21,
        'titulo': 'Anexo normativo, actualizado a 10 de septiembre de 2026',
        # D28: va como entrada 21 para que el pipeline lo escriba, pero NO se
        # numera como capítulo. La portada dice «veinte capítulos» (B6).
        'sin_numerar': True,
        'resumen_indice': 'qué norma sigue vigente y desde cuándo, las fechas que ya sabemos que se mueven, las cinco normas muertas que la SERP sigue citando y cómo comprobar la ficha de vigencia del BOE en un minuto',
        'palabras': 1500, 'bloques': 1,
        'objetivo': 'Que el lector pueda comprobar por su cuenta, dentro de un '
                    'año, qué sigue vigente de todo lo que ha leído: estado '
                    'norma a norma con fecha de corte, las fechas que ya '
                    'sabemos que se mueven, las normas muertas que siguen '
                    'circulando y cómo se comprueba una vigencia en un minuto.',
        'epigrafes': list(PPE_21),
        'puntos_por_epigrafe': PPE_21,
        'puntos_globales': [
            'Este anexo NO se numera como capítulo y no introduce ninguna '
            'afirmación nueva: todo lo que aparece aquí ya se ha dicho en un '
            'capítulo, y aquí sólo se da su estado.',
            'Aquí no entra ninguna cifra de sector: sólo normas, artículos, '
            'fechas y umbrales normativos.',
            'La fecha de corte se repite al principio y al final: es lo que '
            'convierte este anexo en útil dentro de un año.',
        ],
        'cifras': [
            C('Techo de temperatura de la fila nueve del artículo 4.1', f'{X_CARTA}!Parámetros!B28', 'num'),
            C('Techo de temperatura del artículo 9.3', f'{X_CARTA}!Parámetros!B29', 'num'),
            C('Plazo de consumo del artículo 9.3, en horas', f'{X_CARTA}!Parámetros!B30', 'num'),
            C('Umbral analítico de sin gluten, en miligramos por kilo', f'{X_CARTA}!Parámetros!B31', 'num'),
            C('Tope de kilos a la semana del artículo 13.9', f'{X_LEGAL}!Ruta Doméstica!B13', 'num'),
            C('Umbral de la primera vía del artículo 3, sobre el volumen anual', f'{X_LEGAL}!Suministro a Otros Minoristas!B20', 'pct0'),
            C('Umbral de la segunda vía del artículo 3, en kilos a la semana', f'{X_LEGAL}!Suministro a Otros Minoristas!B23', 'num'),
            C('Referencia anual del salario mínimo', f'{X_TURNOS}!Parámetros!C17', 'eur'),
        ],
        'sector': ['PA-04', 'PA-11', 'PA-12', 'PA-15', 'PA-29', 'PA-30c',
                   'PA-31b', 'PA-33', 'PA-37', 'PA-40'],
        'tablas': [
            {
                'titulo': 'Estado de vigencia norma a norma, con fecha de corte de 10-09-2026',
                'cabecera': ['Norma', 'Qué sostiene en esta guía', 'Estado comprobado el 10-09-2026'],
                'filas': [
                    ['RD 1021/2022 (BOE-A-2022-21681)', 'Registro del minorista, suministro a otras tiendas, temperaturas, huevo, congelación, vivienda y autocontrol', 'Vigente, sin modificaciones'],
                    ['RD 191/2011, art. 2.2', 'La exclusión del registro general para el minorista', 'Vigente, en la redacción de la disposición final primera del RD 1021/2022'],
                    ['RD 1086/2020, art. 30', 'Comidas preparadas y zona de degustación', 'Vigente, última modificación de 02-07-2025'],
                    ['Reglamento (CE) 852/2004', 'Higiene, alérgenos de proceso, formación y redistribución', 'Vigente, en la redacción del Reglamento (UE) 2021/382'],
                    ['Reglamento (UE) 1169/2011, art. 14', 'Información obligatoria en venta a distancia', 'Vigente'],
                    ['RD 126/2015', 'Alérgenos e información en producto no envasado', 'Vigente, sin modificaciones'],
                    ['Reglamento de Ejecución (UE) 828/2014', 'El umbral analítico del sin gluten', 'Vigente'],
                    ['RD 496/2010', 'Definiciones de confitería, bollería, pastelería y repostería', 'Vigente, sin modificaciones desde su publicación; su apartado de etiquetado remite a una norma superada'],
                    ['RD 308/2019', 'Pan común, pan especial, masa madre y pan artesano', 'Vigente, última modificación de 27-02-2026'],
                    ['RD 1055/2022', 'Envases de servicio, recipiente del cliente y bebida reutilizable', 'Vigente, sin modificaciones'],
                    ['Ley 1/2025', 'Desperdicio alimentario', 'Vigente; las obligaciones del art. 6 son exigibles desde el 02-04-2026'],
                    ['Ley 37/1992, arts. 90 y 91', 'Tipos de IVA por familia y por canal', 'Vigente, última modificación de 28-02-2026'],
                    ['Resolución de la DGT de 24-02-2025 (BOE-A-2025-3950)', 'Todo el pan del RD 308/2019 al tipo del cuatro por ciento', 'Vinculante para la Administración tributaria'],
                    ['RD 1007/2023', 'Facturación verificable', 'Vigente, última modificación de 03-12-2025; plazos en 2027'],
                    ['RDLeg 2/2015, art. 34.9', 'Registro de jornada', 'Vigente con la redacción de 2019: no exige sistema digital'],
                    ['RD 126/2026', 'Salario mínimo del año en curso', 'Vigente; es un real decreto anual'],
                    ['Ley 1/2004, art. 5.1', 'Libertad horaria de la pastelería', 'Vigente'],
                    ['Ley 7/1996, art. 20', 'La regla de los treinta días del precio anterior', 'Vigente, en la redacción del RD-ley 24/2021'],
                    ['RD 193/2023', 'Accesibilidad', 'Vigente, sin modificaciones; calendario privado en 2029 y 2030'],
                    ['RD 919/2006, ITC-ICG 07', 'Inspección periódica de la instalación de gas', 'Vigente, última modificación de 03-09-2025'],
                    ['RD 1027/2007 (RITE)', 'Categoría del aire del obrador y de la campana', 'Vigente, última modificación de 02-08-2022'],
                    ['Decreto 26/2026 de la Comunidad de Madrid', 'Registro autonómico de minoristas', 'En vigor desde el 28-03-2026, con período transitorio de un año'],
                    ['Decreto 13/2025 del Consell', 'Ampliación autonómica de la lista de la vivienda', 'En vigor desde el 31-01-2025'],
                    ['Decreto 85/2024 de la Generalitat de Catalunya', 'Acreditación voluntaria de artesanía alimentaria', 'En vigor'],
                    ['RD 1254/1991', 'Huevo y ovoproductos', 'DEROGADO con efectos de 22-12-2022; sigue citándose en contenidos que circulan'],
                    ['RD 3484/2000', 'Comidas preparadas', 'DEROGADO; la materia la regulan hoy el RD 1021/2022 y el art. 30 del RD 1086/2020'],
                    ['RD 1420/2006', 'Anisakis', 'DEROGADO'],
                    ['RD 202/2000', 'Manipuladores de alimentos', 'DEROGADO por el RD 109/2010: el carnet no existe'],
                    ['RD 2207/1995', 'Higiene de los productos alimenticios', 'DEROGADO'],
                ],
                'nota': 'Comprobado el 10 de septiembre de 2026 contra los textos consolidados '
                        'oficiales. Sólo se ha verificado el estado de tres comunidades '
                        'autónomas, así que el cuadro autonómico no es completo: comprueba el '
                        'decreto de la tuya.',
            },
            {
                'titulo': 'Las fechas que ya sabemos que se mueven, y qué hay que rehacer con cada una',
                'cabecera': ['Qué cambia', 'Fecha conocida', 'Qué hay que rehacer cuando llegue'],
                'filas': [
                    ['Salario mínimo del año y tabla del convenio de referencia', '31-12-2026', 'Los parámetros de convenio del libro de turnos y del plan financiero'],
                    ['Facturación verificable para sociedades', '01-01-2027', 'El apartado de punto de venta del capítulo de financiación e IVA'],
                    ['Facturación verificable para el resto de obligados', '01-07-2027', 'El mismo apartado, con la fecha que corresponda a tu forma jurídica'],
                    ['Bebida en envase reutilizable por debajo del umbral de superficie', '01-01-2027', 'El apartado de envases: la obligación pasa de futura a presente'],
                    ['Fin del período transitorio del registro autonómico de una comunidad de ejemplo', '28-03-2027', 'El cuadro de comunidades autónomas del capítulo de licencias'],
                    ['Accesibilidad de bienes y servicios privados nuevos', '01-01-2029', 'La ficha de visita a local y el capítulo del local'],
                    ['Accesibilidad de bienes y servicios privados ya existentes', '01-01-2030', 'Lo mismo, para quien haya abierto antes'],
                ],
                'nota': 'Todas estas cifras viven en celda de parámetro en los libros de Excel, '
                        'nunca cosidas en el texto: por eso una edición nueva se arregla '
                        'cambiando este bloque y esas celdas.',
            },
        ],
        'prohibido': NO_COMUN + [
            'Aquí NO entra ninguna cifra de sector, ningún precio y ningún '
            'dato de mercado: sólo normas, artículos, fechas y umbrales '
            'normativos.',
            'No introduzcas ninguna afirmación normativa nueva que no esté ya '
            'en un capítulo: este anexo da estado, no doctrina.',
            'No numeres este bloque como capítulo veintiuno ni lo llames '
            'capítulo: es un anexo.',
        ],
    },
]


# ==========================================================================
# BONUS 1 — `business-plan-modelo-pasteleria` (SPEC §4.2)
#
# El caso completo de «La Clara» CON CIFRAS, en el formato que pide un banco o
# una línea de financiación pública: seis secciones, 3.500 palabras y NUEVE
# tablas, todas construidas desde el libro 5 y el libro 4, celda a celda.
# `documentos.py` sólo admite bonus con `capitulos`, así que las seis secciones
# se declaran como seis «capítulos» de un bloque cada uno; el entregable que se
# vende es el DOCX.
# ==========================================================================

PPE_BP1 = {
    'El proyecto en una página': [
        'Abrir con la ficha del proyecto: qué se monta, dónde, con qué '
        'superficie y con qué plantilla, en cinco líneas y sin adjetivos. Un '
        'banco lee esto y decide si sigue leyendo.',
        'Dar el formato exacto: obrador propio con despacho a calle, en ciudad '
        'media, con los metros repartidos entre obrador, despacho, cámara y '
        'almacén, y aseos y vestuario.',
    ],
    'La inversión y su financiación': [
        'Dar el subtotal de inversión sin el fondo de maniobra, el fondo, la '
        'inversión total y la necesidad total de caja al arranque, y explicar '
        'en una frase la diferencia entre los cuatro.',
        'Dar el reparto entre recursos propios y préstamo, y decir '
        'expresamente qué parte del desembolso es IVA que se recupera.',
    ],
    'La previsión a tres años': [
        'Dar los ingresos del año de crucero, el resultado neto de los tres '
        'años y el margen neto del de crucero, sin comentario y sin adjetivos.',
        'Decir en una línea cuándo llega el negocio al equilibrio y con cuánta '
        'holgura, y remitir a la sección financiera.',
    ],
    'Qué se pide y para qué': [
        'Cerrar con la petición concreta: importe del préstamo, plazo, destino '
        'y garantía prevista, y con la frase que un banco necesita leer, que '
        'es para qué se usa cada euro.',
        'Declarar el alcance del documento: es un modelo relleno con el caso '
        'de una pastelería modelada, para que el lector lo use de plantilla '
        'sustituyendo cada cifra por la suya. No es una previsión de sus '
        'resultados.',
    ],
}

PPE_BP2 = {
    'El mercado en el que entra el proyecto': [
        'Dar el tamaño y la dirección del mercado con las fuentes del sector: '
        'consumo en los hogares, brecha por renta y crecimiento del canal '
        'industrial congelado.',
        'Explicar en dos frases la posición del proyecto: no compite en '
        'volumen con el congelado industrial, compite en producto que no '
        'aguanta ese proceso y en encargo.',
    ],
    'La plaza y el cliente': [
        'Describir la plaza del caso modelado y el perfil de cliente al que '
        'sirve, y decir qué se ha comprobado en el radio de caminata antes de '
        'elegirla.',
        'Dar el ticket medio sin IVA y las piezas por ticket, y explicar que '
        'salen del mix de la propia carta y no de una media del sector, porque '
        'no existe dato público.',
    ],
    'La estacionalidad de la demanda': [
        'Dar la curva del año con el mes más alto y el más bajo y su peso, y '
        'explicar qué significa para la caja: el negocio se planifica por '
        'tesorería, no por media mensual.',
        'Dar el peso conjunto de las campañas sobre las ventas del año y '
        'remitir a la sección de operaciones para la capacidad.',
    ],
    'Competencia y barreras de entrada': [
        'Enumerar los competidores reales por tipo, no por nombre: obrador con '
        'elaboración propia, punto caliente, supermercado y bar que hornea '
        'congelado, y qué le quita cada uno.',
        'Dar la barrera de entrada que sí es del proyecto y es gratuita: la '
        'mención de elaboración propia sólo puede llevarla quien elabora, con '
        'sus condiciones.',
    ],
}

PPE_BP3 = {
    'El concepto y la propuesta de valor': [
        'Describir el concepto en términos de negocio y no de gusto: qué se '
        'elabora, qué no, y por qué esa elección encaja con la capacidad del '
        'obrador y con la plaza.',
        'Declarar lo que el proyecto NO va a hacer, que es tan importante para '
        'un banco como lo que va a hacer.',
    ],
    'La carta de apertura y su margen': [
        'Dar el número de referencias, su reparto en cinco familias y el '
        'margen de contribución medio por pieza, y remitir a la tabla.',
        'Dar el food cost de materia de la carta y el food cost servido, y '
        'explicar la diferencia en una frase.',
    ],
    'Los canales de venta y su margen de contribución': [
        'Presentar los cuatro canales con su peso, su margen de contribución y '
        'sus días de cobro, y decir cuál sostiene el negocio.',
        'Explicar la consecuencia financiera de los días de cobro: dos canales '
        'con el mismo margen no valen lo mismo para la caja.',
    ],
    'La política de precios': [
        'Explicar la regla única de margen que usa todo el plan: se fija el '
        'food cost objetivo y el margen bruto se deriva de él, nunca al revés '
        'ni las dos cosas a la vez.',
        'Dar el precio de venta medio ponderado con IVA y el ticket medio, y '
        'decir que los precios de la carta son datos de ejemplo del caso '
        'modelado.',
    ],
}

PPE_BP4 = {
    'El local y sus zonas': [
        'Dar la superficie total y el reparto por zonas con sus metros, y '
        'explicar en una frase el principio de marcha adelante, que es lo que '
        'justifica el reparto.',
        'Dar la parte del local dedicada a obrador y a venta, que es el ratio '
        'que un técnico mira primero.',
    ],
    'La capacidad de producción y su cuello de botella': [
        'Dar las piezas al día que quiere sacar el negocio y las que permite '
        'el conjunto de equipos, nombrar el equipo que limita y dar la holgura '
        'sobre el día normal.',
        'Explicar qué pasa en campaña y con qué palancas se cubre el déficit, '
        'remitiendo a la sección de riesgos.',
    ],
    'La plantilla y su coste': [
        'Dar las personas, las jornadas equivalentes y el coste de personal al '
        'año con la Seguridad Social dentro, y el ratio de coste de personal '
        'sobre ventas del año de crucero.',
        'Explicar la política de contratación: quién entra antes de abrir, '
        'quién el día de la apertura y quién después, y por qué el primer año '
        'no cuesta lo mismo que el de crucero.',
    ],
    'El calendario de puesta en marcha': [
        'Dar la duración total del proyecto en meses, el número de hitos en '
        'ruta crítica y el mes de apertura previsto.',
        'Explicar el criterio de la fecha: se abre fuera de campaña para '
        'llegar rodado a la grande, y el cronograma avisa si la fecha cae '
        'dentro de una.',
    ],
}

PPE_BP5 = {
    'Los supuestos del plan': [
        'Declarar los supuestos antes de dar ninguna proyección: tickets al '
        'día, ticket medio sin IVA, días de apertura, rampa de arranque y '
        'estacionalidad mensual. Un plan sin supuestos declarados no se '
        'defiende.',
        'Declarar el supuesto de margen: el coste de ventas se proyecta con la '
        'regla única y no con el escandallo de las piezas, y explicar por qué '
        'es el supuesto conservador.',
    ],
    'La cuenta de resultados a tres años': [
        'Dar la cuenta de resultados con su tabla y comentar sólo tres cosas: '
        'la partida grande de costes fijos, la retribución del propietario '
        'como renglón propio y el resultado neto de cada año.',
        'Dar el margen neto del año de crucero y contrastarlo con la banda de '
        'referencia declarada por un profesional del sector, con su fuente.',
    ],
    'El punto de equilibrio': [
        'Dar los tickets al día que hacen falta para el equilibrio contable y '
        'para el de caja, y explicar por qué el segundo está por encima: la '
        'devolución del principal sale de la caja y no del resultado.',
        'Dar la holgura sobre el equilibrio de caja en el año de crucero, que '
        'es la cifra que responde a la pregunta de cuánto puede caer la '
        'previsión sin romper nada.',
    ],
    'La tesorería de los doce primeros meses': [
        'Dar el saldo mínimo de caja del primer año y el mes en el que la caja '
        'toca fondo, que es la pregunta que de verdad hace un banco.',
        'Explicar el efecto del IVA de la inversión: se adelanta y vuelve con '
        'la liquidación del período, así que es caja aunque no sea coste.',
    ],
    'La financiación y el servicio de la deuda': [
        'Dar el origen de fondos, el principal del préstamo, la cuota mensual '
        'y los intereses del primer año.',
        'Dar la cobertura del servicio de la deuda más ajustada de todo el '
        'cuadro y explicar que es el peor año, no el primero, el que hay que '
        'mirar.',
    ],
}

PPE_BP6 = {
    'Los tres escenarios': [
        'Presentar el escenario pesimista, el realista y el optimista con sus '
        'ingresos y su resultado neto, y decir cuáles son supuestos y cuál lee '
        'el plan.',
        'Explicar por qué el pesimista duele tanto: los costes fijos no bajan '
        'con las ventas porque la plantilla es la misma en los tres.',
    ],
    'Los riesgos de apertura y su mitigación': [
        'Enumerar los riesgos con fecha: que el local no admita salida de '
        'humos, que la licencia se retrase, que el equipamiento llegue tarde y '
        'que la obra se desvíe del presupuesto.',
        'Dar la mitigación concreta de cada uno con la herramienta del pack '
        'que la sostiene, y el margen del plazo crítico de entrega.',
    ],
    'Los riesgos de explotación': [
        'Enumerar los de después de abrir: que la campaña grande no quepa en '
        'el obrador, que el coste de personal se coma el margen, que la '
        'materia prima suba y que no se encuentre personal.',
        'Dar la mitigación de cada uno y el número que la mide, remitiendo a '
        'la herramienta correspondiente.',
    ],
    'El plan de contingencia': [
        'Dar las tres palancas que se activan si el escenario pesimista se '
        'materializa, en orden: recortar referencias de margen bajo, ajustar '
        'el cuadrante y renegociar el plazo de la deuda.',
        'Cerrar declarando otra vez el alcance: este es un modelo relleno para '
        'que el lector lo use de plantilla, y ninguna de sus cifras es una '
        'previsión de sus resultados.',
    ],
}

BONUS = [
    {
        'nombre': 'business-plan-modelo-pasteleria',
        'guia': {
            'titulo': 'Business Plan Modelo de una Pastelería',
            'subtitulo': 'Bonus del pack «Cómo Montar una Pastelería» · el caso '
                         'completo relleno, con las cifras de las ocho '
                         'herramientas Excel',
            'cabecera': 'AI Chef Pro · Business Plan Modelo de una Pastelería',
            'tipo_doc': 'documento',
            'tipo_doc_art': 'del business plan',
            'tipo_doc_dem': 'este documento',
            'categoria_doc': 'Plantilla profesional',
            'portada_texto': (
                'El plan de negocio de una pastelería modelada, relleno de '
                'principio a fin y en el formato que pide un banco o una línea '
                'de financiación pública: resumen ejecutivo, mercado y plaza, '
                'concepto y carta, plan de operaciones, plan financiero a tres '
                'años y análisis de riesgos con escenarios. Todas las cifras '
                'salen de las ocho herramientas Excel del pack, así que puedes '
                'abrir la celda de la que sale cada una y sustituirla por la '
                'tuya. Es una plantilla rellena para que la copies, no una '
                'previsión de tus resultados.'),
        },
        'gates': {
            'paginas_prometidas': 8,
            'palabras_objetivo': 3500,
            'min_palabras_cap': 450,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': 'Business Plan Modelo de una Pastelería',
                     'subject': 'Bonus del pack Cómo Montar una Pastelería · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Resumen Ejecutivo',
                'resumen_indice': 'el proyecto en una página: qué se monta, cuánto cuesta, cómo se financia y qué se pide.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Que quien lee el plan sepa en una página qué '
                            'proyecto es, cuánto dinero necesita, de dónde sale '
                            'y qué devuelve. Sin adjetivos y sin promesas.',
                'epigrafes': list(PPE_BP1),
                'puntos_por_epigrafe': PPE_BP1,
                'puntos_globales': [
                    'Registro de documento de banco: frases cortas, cifras '
                    'delante y cero lenguaje comercial.',
                    'Cada cifra sale de una celda del pack y se puede abrir: '
                    'eso se dice una vez, al principio del documento.',
                ],
                'cifras': [
                    C('Subtotal de inversión sin el fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B17', 'eur'),
                    C('Fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B18', 'eur'),
                    C('Inversión total', f'{X_PLAN}!Inversión Inicial!B19', 'eur'),
                    C('IVA soportado sobre la inversión', f'{X_PLAN}!Inversión Inicial!B21', 'eur'),
                    C('Necesidad total de caja al arranque', f'{X_PLAN}!Inversión Inicial!B22', 'eur'),
                    C('Recursos propios aportados', f'{X_PLAN}!0. Supuestos!B36', 'eur'),
                    C('Principal del préstamo', f'{X_PLAN}!0. Supuestos!B37', 'eur'),
                    C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
                ],
                'sector': ['PS-05', 'PS-48'],
                'tablas': [{
                    'titulo': 'La inversión y la necesidad de caja al arranque (plan-financiero-3-anos-pasteleria.xlsx, hoja «Inversión Inicial»)',
                    'src': (X_PLAN, 'Inversión Inicial'),
                    'cols': [('Concepto', 'A', 'txt'), ('Importe sin IVA (€)', 'B', 'eur')],
                    'filas': (17, 22),
                    'nota': 'La necesidad total de caja es la cifra que hay que cubrir el día '
                            'que se firma: incluye el IVA que se adelanta y el fondo de '
                            'maniobra, que no son inversión pero salen de la cuenta.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'No adornes: un resumen ejecutivo con adjetivos es un '
                    'resumen ejecutivo que no se cree nadie.',
                ],
            },
            {
                'n': 2,
                'titulo': 'Mercado y Plaza',
                'resumen_indice': 'tamaño y dirección del mercado, la plaza y el cliente, la estacionalidad de la demanda y las barreras de entrada.',
                'palabras': 550, 'bloques': 1,
                'objetivo': 'Demostrar que el proyecto conoce el mercado en el '
                            'que entra y que ha elegido la plaza con criterio, '
                            'con datos de fuente citable y sin inflar nada.',
                'epigrafes': list(PPE_BP2),
                'puntos_por_epigrafe': PPE_BP2,
                'puntos_globales': [
                    'Cada dato de mercado con su fuente y su año dentro del '
                    'texto. Los de fiabilidad limitada, con esa etiqueta.',
                    'Ninguna cifra de censo de pastelerías ni de facturación '
                    'media: no existe dato fiable.',
                ],
                'cifras': [
                    C('Ventas anuales sin IVA en velocidad de crucero', f'{X_EST}!Parámetros!B6', 'eur'),
                    C('Ticket medio sin IVA', f'{X_PLAN}!0. Supuestos!B10', 'eur2'),
                    C('Piezas por ticket', f'{X_PLAN}!0. Supuestos!B7', 'num1'),
                    C('Tickets al día en velocidad de crucero', f'{X_PLAN}!0. Supuestos!B6', 'num'),
                    C('Días de apertura al año', f'{X_PLAN}!0. Supuestos!B11', 'num'),
                    C('Peso del mes más alto sobre el año', f'{X_EST}!Peso sobre el Año!D6', 'pct1'),
                    C('Peso del mes más bajo sobre el año', f'{X_EST}!Peso sobre el Año!D13', 'pct1'),
                    C('Peso de las seis campañas sobre el año', f'{X_EST}!Peso sobre el Año!D30', 'pct1'),
                ],
                'sector': ['PS-28', 'PS-29', 'PS-26c', 'PS-26d', 'PS-26i', 'PS-42'],
                'tablas': [{
                    'titulo': 'La curva de la demanda mes a mes (estacionalidad-y-picos.xlsx, hoja «Peso sobre el Año»)',
                    'src': (X_EST, 'Peso sobre el Año'),
                    'cols': [('Mes', 'A', 'txt'), ('Coeficiente sobre el mes medio', 'B', 'num2'),
                             ('Ventas del mes sin IVA (€)', 'C', 'eur'),
                             ('Parte del año (%)', 'D', 'pct1'),
                             ('Campañas del mes', 'E', 'txt')],
                    'filas': (6, 18),
                    'nota': 'Los coeficientes son supuestos del caso modelado y suman doce, de '
                            'manera que la media coincide con la velocidad de crucero.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'No des ningún tamaño de mercado que no venga de los datos '
                    'del sector de esta sección.',
                ],
            },
            {
                'n': 3,
                'titulo': 'Concepto y Carta',
                'resumen_indice': 'el concepto y su propuesta de valor, la carta de apertura y su margen, los canales de venta y la política de precios.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Explicar qué se vende, a quién, por qué canal y '
                            'con qué margen, con la carta completa detrás y con '
                            'una sola regla de margen.',
                'epigrafes': list(PPE_BP3),
                'puntos_por_epigrafe': PPE_BP3,
                'puntos_globales': [
                    'Una sola regla de margen en todo el documento: food cost '
                    'objetivo, y el margen bruto derivado.',
                    'Los precios y los gramajes de la carta son datos de '
                    'ejemplo del caso modelado, y se dice.',
                ],
                'cifras': [
                    C('Margen de contribución medio por pieza', f'{X_CARTA}!Mix y Ticket Medio!F47', 'eur2'),
                    C('Precio de venta medio ponderado con IVA', f'{X_CARTA}!Mix y Ticket Medio!F39', 'eur2'),
                    C('Ticket medio con IVA', f'{X_CARTA}!Mix y Ticket Medio!F41', 'eur2'),
                    C('Food cost de materia de la carta', f'{X_CARTA}!Mix y Ticket Medio!F44', 'pct1'),
                    C('Food cost servido, con merma y packaging', f'{X_CARTA}!Mix y Ticket Medio!F45', 'pct1'),
                    C('Food cost objetivo del plan', f'{X_CARTA}!Parámetros!B24', 'pct0'),
                    C('Margen bruto objetivo derivado', f'{X_CARTA}!Parámetros!B25', 'pct0'),
                    C('Margen de contribución medio ponderado de los canales', f'{X_PLAN}!Canales y Punto Muerto!B15', 'pct1'),
                ],
                'sector': ['PS-43', 'PS-53', 'PS-55', 'PS-56'],
                'tablas': [
                    {
                        'titulo': 'Cómo queda la carta después del filtro de margen y rotación (carta-de-apertura-y-escandallo.xlsx, hoja «Decisión de Surtido»)',
                        'src': (X_CARTA, 'Decisión de Surtido'),
                        'cols': [('Concepto', 'B', 'txt'), ('Referencias', 'E', 'num'),
                                 ('Margen ponderado (€)', 'F', 'eur2')],
                        'filas': (39, 41),
                        'nota': 'El margen ponderado suma lo que aporta cada grupo de '
                                'referencias al margen de cien piezas vendidas con el mix '
                                'previsto. El margen ponderado MEDIO por referencia de la '
                                'carta es otra cosa y son 0,04 €; el de las cien piezas '
                                'vendidas con este mix, 1,07 €.',
                    },
                    {
                        'titulo': 'Los cuatro canales de venta y su margen de contribución (plan-financiero-3-anos-pasteleria.xlsx, hoja «Canales y Punto Muerto»)',
                        'src': (X_PLAN, 'Canales y Punto Muerto'),
                        'cols': [('Canal', 'A', 'txt'),
                                 ('Ventas del año de crucero (€)', 'H', 'eur'),
                                 ('Parte de las ventas (%)', 'B', 'pct0'),
                                 ('Margen bruto (%)', 'C', 'pct0'),
                                 ('Margen de contribución (%)', 'G', 'pct0'),
                                 ('Margen de contribución (€)', 'I', 'eur'),
                                 ('Días de cobro', 'F', 'num')],
                        'filas': (6, 10),
                        'nota': 'Dos canales con el mismo margen no valen lo mismo para la '
                                'caja: la columna de días de cobro es la que lo explica.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No presentes margen bruto y food cost como dos objetivos '
                    'independientes.',
                ],
            },
            {
                'n': 4,
                'titulo': 'Plan de Operaciones',
                'resumen_indice': 'el local y sus zonas, la capacidad de producción y su cuello de botella, la plantilla y su coste, y el calendario de puesta en marcha.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Demostrar que el proyecto sabe producir lo que '
                            'dice que va a vender, con qué equipo, con cuánta '
                            'gente y en qué plazo.',
                'epigrafes': list(PPE_BP4),
                'puntos_por_epigrafe': PPE_BP4,
                'puntos_globales': [
                    'Los nombres de los cuatro perfiles son los del pack: Jefe '
                    'Pastelero, Pastelero, Ayudante y Dependiente Vitrina, con '
                    'dos personas en el último.',
                    'Las duraciones del cronograma son supuestos de '
                    'planificación, no plazos legales de resolución.',
                ],
                'cifras': [
                    C('Superficie total del local', f'{X_CAP}!Parámetros!B14', 'num'),
                    C('Metros de obrador', f'{X_CAP}!Zonas y m2!D18', 'num'),
                    C('Piezas al día objetivo en velocidad de crucero', f'{X_CAP}!Cuello de Botella!B6', 'num'),
                    C('Piezas al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
                    C('Personas de la plantilla', f'{X_PLAN}!Personal!B11', 'num'),
                    C('Jornadas completas equivalentes', f'{X_PLAN}!Personal!C11', 'num1'),
                    C('Coste de personal al año', f'{X_PLAN}!Personal!I11', 'eur'),
                    C('Coste de personal sobre ventas en el año de crucero', f'{X_PLAN}!PyG 3 Años!C48', 'pct1'),
                    C('Duración total del proyecto, en meses', f'{X_LEGAL}!Cronograma y Ruta Crítica!C38', 'num1'),
                    C('Hitos en la ruta crítica', f'{X_LEGAL}!Cronograma y Ruta Crítica!C39', 'num'),
                ],
                'sector': ['PS-86d', 'PA-33'],
                'tablas': [
                    {
                        'titulo': 'Las siete zonas del local y su superficie (capacidad-obrador-y-local.xlsx, hoja «Zonas y m2»)',
                        'src': (X_CAP, 'Zonas y m2'),
                        'cols': [('Nº', 'A', 'num'), ('Zona', 'B', 'txt'),
                                 ('Bloque', 'C', 'txt'),
                                 ('Metros cuadrados', 'D', 'num'),
                                 ('Parte del local (%)', 'E', 'pct1'),
                                 ('Paso del recorrido', 'F', 'num')],
                        'filas': (6, 12),
                        'nota': 'El orden del recorrido es el que demuestra la marcha adelante: '
                                'materia prima primero, residuo al final.',
                    },
                    {
                        'titulo': 'La plantilla y su coste de empresa (plantilla-turnos-y-coste-personal.xlsx, hoja «Horas y Coste»)',
                        'src': (X_TURNOS, 'Horas y Coste'),
                        'cols': [('Id', 'A', 'txt'), ('Persona', 'B', 'txt'),
                                 ('Área', 'C', 'txt'),
                                 ('Bruto mensual del grupo (€)', 'E', 'eur2'),
                                 ('Jornada equivalente', 'F', 'num1'),
                                 ('Bruto anual (€)', 'I', 'eur'),
                                 ('Coste de empresa al año (€)', 'K', 'eur')],
                        'filas': (7, 12),
                        'nota': V_CONV,
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDA la palabra «oficial» como nombre de puesto.',
                ],
            },
            {
                'n': 5,
                'titulo': 'Plan Financiero a Tres Años',
                'resumen_indice': 'los supuestos declarados, la cuenta de resultados, el punto de equilibrio, la tesorería de los doce primeros meses y el servicio de la deuda.',
                'palabras': 650, 'bloques': 1,
                'objetivo': 'Dar la parte del plan que un banco lee entera: '
                            'supuestos, cuenta de resultados, punto de '
                            'equilibrio, caja mes a mes y cobertura de la '
                            'deuda.',
                'epigrafes': list(PPE_BP5),
                'puntos_por_epigrafe': PPE_BP5,
                'puntos_globales': [
                    'Los supuestos van SIEMPRE antes que las proyecciones, no '
                    'en un anexo al final.',
                    'La retribución del propietario aparece como renglón '
                    'propio en todas las lecturas del resultado.',
                ],
                'cifras': [
                    C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
                    C('Resultado neto del año uno', f'{X_PLAN}!PyG 3 Años!B43', 'eur'),
                    C('Resultado neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C43', 'eur'),
                    C('Margen neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C50', 'pct1'),
                    C('Tickets al día para el equilibrio de caja', f'{X_PLAN}!Punto de Equilibrio!C22', 'num1'),
                    C('Holgura sobre el equilibrio de caja', f'{X_PLAN}!Punto de Equilibrio!C26', 'pct1'),
                    C('Saldo mínimo de caja del año uno', f'{X_PLAN}!Tesorería 12 meses!B24', 'eur'),
                    C('Mes en el que la caja toca fondo', f'{X_PLAN}!Tesorería 12 meses!B25', 'num'),
                    C('Cuota mensual del préstamo', f'{X_PLAN}!Financiación!B22', 'eur2'),
                    C('Cobertura del servicio de la deuda más ajustada', f'{X_PLAN}!Financiación!B123', 'num2'),
                ],
                'sector': ['PS-48', 'PS-58'],
                'tablas': [
                    {
                        'titulo': 'La cuenta de resultados a tres años (plan-financiero-3-anos-pasteleria.xlsx, hoja «PyG 3 Años»)',
                        'src': (X_PLAN, 'PyG 3 Años'),
                        'cols': [('Concepto', 'A', 'txt'), ('Año 1', 'B', 'eur'),
                                 ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur'),
                                 ('Parte de las ventas del año 2 (%)', 'E', 'pct1')],
                        'filas': (11, 36),
                        # B12 (2026-09-10): fuera las dos filas de IVA
                        # soportado, que no participan en la resta.
                        'omitir_filas': (34, 35),
                        'nota': 'Todas las cifras van sin IVA y el coste de ventas se proyecta '
                                'con la regla única de margen, que es el supuesto conservador. '
                                'Las dos líneas de IVA soportado que la hoja «PyG 3 Años» lleva '
                                'como memoria (filas 34 y 35) no se imprimen aquí ni entran en '
                                'la resta del resultado; su efecto sobre la caja está en la '
                                'hoja de tesorería.',
                    },
                    {
                        'titulo': 'La caja de los doce primeros meses (plan-financiero-3-anos-pasteleria.xlsx, hoja «Tesorería 12 meses»)',
                        'src': (X_PLAN, 'Tesorería 12 meses'),
                        'cols': [('Concepto', 'A', 'txt'), ('Mes 1 (€)', 'B', 'eur'),
                                 ('Mes 3 (€)', 'D', 'eur'), ('Mes 6 (€)', 'G', 'eur'),
                                 ('Mes 9 (€)', 'J', 'eur'), ('Mes 12 (€)', 'M', 'eur'),
                                 ('Año (€)', 'N', 'eur')],
                        'filas': (10, 23),
                        'nota': 'La cuenta de resultados dice si el negocio gana; esta hoja dice '
                                'si llega a fin de mes. El mes en el que la caja toca fondo es '
                                'la pregunta que hace un banco. Las compras del mes 1 salen a '
                                'cero porque el supuesto es pago a 30 días: la primera factura '
                                'de materia prima se paga en el mes 2, y el pedido de arranque '
                                'ya está dentro de la inversión inicial como packaging.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No presentes ninguna proyección sin declarar antes su '
                    'supuesto.',
                ],
            },
            {
                'n': 6,
                'titulo': 'Riesgos y Escenarios',
                'resumen_indice': 'los tres escenarios, los riesgos de apertura y los de explotación con su mitigación, y el plan de contingencia.',
                'palabras': 500, 'bloques': 1,
                'objetivo': 'Cerrar el plan con los tres escenarios y con la '
                            'lista de riesgos y mitigaciones, que es la sección '
                            'que separa un plan creíble de un folleto.',
                'epigrafes': list(PPE_BP6),
                'puntos_por_epigrafe': PPE_BP6,
                'puntos_globales': [
                    'Cada riesgo lleva su mitigación y la herramienta del pack '
                    'que la sostiene. Un riesgo sin mitigación es una excusa '
                    'anticipada.',
                    'El documento se cierra declarando su alcance: es una '
                    'plantilla rellena, no una previsión de resultados.',
                ],
                'cifras': [
                    C('Ingresos del escenario pesimista', f'{X_PLAN}!Escenarios!B9', 'eur'),
                    C('Resultado neto del escenario pesimista', f'{X_PLAN}!Escenarios!B16', 'eur'),
                    C('Resultado neto del escenario optimista', f'{X_PLAN}!Escenarios!D16', 'eur'),
                    C('Coste de personal sobre ventas en el escenario pesimista', f'{X_PLAN}!Escenarios!B20', 'pct1'),
                    C('Campañas que no aguanta el obrador', f'{X_EST}!Capacidad vs Demanda del Pico!N13', 'num'),
                    C('Margen del plazo crítico de entrega, en semanas', f'{X_EQUIP}!Equipamiento!I55', 'num'),
                ],
                'sector': ['PS-97', 'PS-41'],
                'tablas': [{
                    'titulo': 'Los tres escenarios, con la misma plantilla y los mismos costes fijos (plan-financiero-3-anos-pasteleria.xlsx, hoja «Escenarios»)',
                    'src': (X_PLAN, 'Escenarios'),
                    'cols': [('Métrica', 'A', 'txt'), ('Pesimista', 'B', 'eur'),
                             ('Realista', 'C', 'eur'), ('Optimista', 'D', 'eur')],
                    'filas': (9, 17),
                    'nota': 'Los dos extremos son supuestos; la columna del medio lee el año de '
                            'crucero del plan. Los costes fijos no cambian entre escenarios '
                            'porque la plantilla es la misma.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'No cierres con una promesa de rentabilidad ni con un '
                    'resumen de lo ya dicho.',
                ],
            },
        ],
    },
]


# ==========================================================================
# BONUS 2 — «12 decisiones de apertura resueltas» (SPEC §4.3)
#
# Molde probado dos veces en la familia: doce bloques de un redactor cada uno,
# 800-900 palabras y una tabla. Los cinco epígrafes son FIJOS y se declaran una
# sola vez, para que `puntos_por_epigrafe` no pueda desviarse ni una letra del
# literal del epígrafe.
# ==========================================================================

EPI_DEC = [
    'El contexto de la decisión',
    'Las opciones sobre la mesa',
    'El criterio con el que se decide',
    'La celda que lo resuelve',
    'La norma que aplica cuando la hay',
]


def PPE_DEC(contexto, opciones, criterio, celda, norma):
    """Dict epígrafe → puntos con los cinco epígrafes fijos del bonus 2."""
    return {EPI_DEC[0]: contexto, EPI_DEC[1]: opciones,
            EPI_DEC[2]: criterio, EPI_DEC[3]: celda, EPI_DEC[4]: norma}


PG_DEC = [
    'Cada decisión se cierra con una recomendación explícita y con la '
    'condición que la haría cambiar. Un bonus de decisiones que no decide no '
    'sirve para nada.',
    'La celda que resuelve la decisión se nombra en lenguaje de libro —el '
    'libro y la hoja—, nunca con la sintaxis de Excel.',
    'Cuando no hay norma que aplique, se dice que no la hay en vez de '
    'rellenar el epígrafe con normativa de adorno.',
]

BONUS += [
    {
        'nombre': 'BONUS-12-decisiones-de-apertura',
        'guia': {
            'titulo': '12 Decisiones de Apertura Resueltas',
            'subtitulo': 'Bonus del pack «Cómo Montar una Pastelería» · con los '
                         'datos de las ocho herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Decisiones de Apertura Resueltas',
            'tipo_doc': 'bonus',
            'tipo_doc_art': 'del bonus',
            'tipo_doc_dem': 'este bonus',
            'categoria_doc': 'Guía profesional',
            'portada_texto': (
                'Doce decisiones que hay que tomar antes de abrir una '
                'pastelería y que casi nunca se resuelven con un número: '
                'comprar el abatidor o esperar, abrir con veinte referencias o '
                'con cuarenta, aceptar el primer encargo de comunión sin '
                'histórico, empezar en casa dentro de la legalidad, firmar el '
                'primer contrato con otra tienda. Cada una con su contexto, sus '
                'opciones, el criterio con el que se decide, la celda del pack '
                'que la resuelve y la norma que aplica cuando la hay. No hay '
                'ninguna cifra inventada: cada número sale de una celda que '
                'puedes abrir y comprobar.'),
        },
        'gates': {
            'paginas_prometidas': 25,
            'palabras_objetivo': 10000,
            'min_palabras_cap': 600,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': '12 Decisiones de Apertura Resueltas',
                     'subject': 'Bonus del pack Cómo Montar una Pastelería · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Local con Obrador o Obrador Aparte',
                'resumen_indice': 'cuándo compensa meter el obrador en el mismo local y cuándo sale mejor separarlo del punto de venta.',
                'palabras': 850, 'bloques': 1,
                'objetivo': 'Resolver la primera decisión de formato: obrador y '
                            'despacho en el mismo local, o obrador a puerta '
                            'cerrada con el punto de venta en otro sitio.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: el local que gusta por escaparate no tiene '
                     'metros para el obrador, y el que tiene metros está en una '
                     'calle sin paso.',
                     'Lo que casi nadie calcula antes de decidir: el obrador '
                     'necesita una parte del local que no vende nada, y esa '
                     'parte se paga con la renta del escaparate.'],
                    ['Opción A: todo en un local, con el obrador ocupando la '
                     'parte de atrás. Opción B: obrador a puerta cerrada en zona '
                     'barata y despacho pequeño en zona de paso. Opción C: '
                     'empezar sin obrador propio, comprando elaborado.',
                     'Lo que cambia en cada una: la inversión de apertura, la '
                     'renta total, el transporte diario y el régimen de '
                     'registro si el despacho es una sucursal.'],
                    ['La regla: se compara el coste total a varios años, no la '
                     'renta mensual. Y se comprueba que en la opción A quepan '
                     'las siete zonas con marcha adelante, porque si no caben, '
                     'la opción A no existe.',
                     'El segundo filtro es de producto: sin obrador propio no se '
                     'puede usar la mención de elaboración propia.'],
                    ['La hoja de variantes de la calculadora de inversión da la '
                     'inversión de apertura de cada formato, y la de zonas dice '
                     'si las siete zonas caben en los metros que estás mirando.',
                     'Si eliges obrador y sucursal, la hoja del árbol de '
                     'registro te dice qué inscribe cada uno.'],
                    ['El obrador es, por definición legal, la parte del '
                     'establecimiento inaccesible al público y de la misma '
                     'titularidad, y para que el esquema de central y sucursales '
                     'funcione tienen que estar en el mismo municipio o zona de '
                     'salud.',
                     'Y la parte que se olvida: cada sucursal se inscribe en el '
                     'registro autonómico de manera independiente, aunque el '
                     'suministro entre ellas no cuente como venta a otras '
                     'tiendas.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Inversión de apertura del caso central, obrador y tienda en el mismo local', f'{X_CAPEX}!Variante del Formato!I15', 'eur'),
                    C('Inversión de apertura del obrador a puerta cerrada', f'{X_CAPEX}!Variante del Formato!I17', 'eur'),
                    C('Inversión de apertura del local con venta sin obrador', f'{X_CAPEX}!Variante del Formato!I18', 'eur'),
                    C('Superficie total del local del caso modelado', f'{X_CAP}!Parámetros!B14', 'num'),
                    C('Metros de obrador', f'{X_CAP}!Zonas y m2!D18', 'num'),
                    C('Parte del local dedicada a obrador', f'{X_CAP}!Zonas y m2!D19', 'pct0'),
                ],
                'sector': ['PS-02', 'PS-03', 'PS-05', 'PA-03', 'PA-03b'],
                'tablas': [{
                    'titulo': 'Qué cuesta abrir cada formato (calculadora-capex-pasteleria.xlsx, hoja «Variante del Formato»)',
                    'src': (X_CAPEX, 'Variante del Formato'),
                    'cols': [('Variante', 'B', 'txt'),
                             ('Inversión de apertura (€)', 'I', 'eur'),
                             ('Con fondo de maniobra (€)', 'J', 'eur'),
                             ('Qué cambia además', 'N', 'txt')],
                    'filas': (15, 19),
                    'nota': 'Los coeficientes que producen cada variante son supuestos del '
                            'modelo: sirven para comparar formatos entre sí, no como '
                            'presupuesto.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 2,
                'titulo': 'Comprar el Abatidor o Esperar',
                'resumen_indice': 'qué techo de producción te pone posponer la compra más cara del obrador, y cuándo compensa esperar.',
                'palabras': 830, 'bloques': 1,
                'objetivo': 'Poner número a la compra que más se pospone: qué '
                            'capacidad se pierde sin abatidor y qué producto '
                            'deja de poder hacerse.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['Es la partida más cara del equipamiento de obrador y la '
                     'primera que se cae del presupuesto cuando las cuentas no '
                     'salen.',
                     'El argumento que se oye siempre: «el primer año hago menos '
                     'producto y ya lo compraré». Lo que hay que ver es cuánto '
                     'techo de producción se está comprando con esa frase.'],
                    ['Opción A: comprarlo el día uno. Opción B: abrir sin él y '
                     'limitar el surtido a lo que no lo necesita. Opción C: '
                     'comprar uno de menos bandejas y cambiarlo cuando el '
                     'negocio lo pida.',
                     'Lo que cambia: las piezas al día del conjunto, la parte '
                     'del surtido que puedes hacer y la capacidad en campaña.'],
                    ['La regla: se mira el equipo que limita, no el equipo más '
                     'caro. Si el abatidor es el cuello de botella del conjunto, '
                     'comprarlo pequeño es fijar el techo del negocio.',
                     'El segundo criterio es de campaña: sin abatidor no se '
                     'adelanta producción, y sin adelantar producción la campaña '
                     'grande no cabe.'],
                    ['La hoja de capacidad por equipo da las piezas al día que '
                     'permite cada uno, y la de cuello de botella dice cuál '
                     'limita y con cuánta holgura.',
                     'La calculadora de inversión trae la línea del abatidor con '
                     'su precio de referencia y su base fiscal.'],
                    ['La congelación exige alcanzar la temperatura negativa en el '
                     'centro del producto con un descenso ininterrumpido, y sólo '
                     'se puede congelar en un arcón o cámara de mantenimiento si '
                     'se garantiza que se cumple.',
                     'Y lo que se congela va etiquetado con fecha de '
                     'elaboración, de congelación y de caducidad o consumo '
                     'preferente.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Piezas al día de obrador que permite el abatidor', f'{X_CAP}!Capacidad por Equipo!M12', 'num'),
                    C('Piezas al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
                    C('Holgura sobre el día normal', f'{X_CAP}!Cuello de Botella!B9', 'num'),
                    C('Parte del surtido que pasa por el abatidor', f'{X_CAP}!Capacidad por Equipo!L12', 'pct0'),
                    C('Importe del abatidor en la calculadora de inversión', f'{X_CAPEX}!CAPEX por Bloque!J11', 'eur'),
                    C('Piezas al día que permite el segundo equipo más justo', f'{X_CAP}!Cuello de Botella!B13', 'num'),
                ],
                'sector': ['PA-13', 'PS-78'],
                'tablas': [{
                    'titulo': 'Qué permite cada equipo del obrador, y cuál limita (capacidad-obrador-y-local.xlsx, hoja «Capacidad por Equipo»)',
                    'src': (X_CAP, 'Capacidad por Equipo'),
                    'cols': [('Equipo', 'B', 'txt'), ('Categoría', 'C', 'txt'),
                             ('¿Lo tienes?', 'D', 'txt'),
                             ('Parte del surtido que pasa (%)', 'L', 'pct0'),
                             ('Piezas al día de obrador que permite', 'M', 'num')],
                    'filas': (6, 15),
                    'nota': 'Las capacidades son supuestos de modelado calibrados con fichas de '
                            'distribuidor. Cámbialas por las del equipo que vayas a comprar.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 3,
                'titulo': 'Abrir con Veinte Referencias o con Cuarenta',
                'resumen_indice': 'cuántas referencias caben en el primer año, y qué se gana quitando en vez de añadir.',
                'palabras': 850, 'bloques': 1,
                'objetivo': 'Resolver la decisión de amplitud del surtido con el '
                            'filtro de margen y rotación, y no con la ilusión de '
                            'ofrecer de todo.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['La tentación del primer año es abrir con la carta más '
                     'grande posible para no perder ninguna venta, y es la '
                     'manera más rápida de multiplicar la merma y la compra.',
                     'Cada referencia añade proveedor, formato de compra, '
                     'espacio de vitrina y tiempo de obrador, y todo eso se paga '
                     'aunque la referencia venda poco.'],
                    ['Opción A: abrir con una carta corta y ampliar con datos a '
                     'los tres meses. Opción B: abrir con la carta completa y '
                     'podar después. Opción C: carta corta fija más una rotación '
                     'de temporada.',
                     'Lo que cambia: la merma, la compra inicial, la carga de '
                     'obrador en el arranque y la claridad del escaparate.'],
                    ['La regla: manda el margen PONDERADO por el mix, no el '
                     'margen de la pieza. Una referencia con buen margen que no '
                     'rota aporta menos que una de margen medio que rota mucho.',
                     'El segundo criterio es de capacidad: la carta tiene que '
                     'caber en las piezas al día del cuello de botella, no sólo '
                     'en la vitrina.'],
                    ['La hoja de decisión de surtido del libro de la carta da el '
                     'veredicto de cada referencia y el margen ponderado que '
                     'aporta cada grupo.',
                     'La hoja de mix y ticket medio dice cómo cambia el ticket '
                     'al mover el mix.'],
                    ['Aquí no hay norma que decida la amplitud de la carta, y '
                     'hay que decirlo: es una decisión de negocio y de '
                     'capacidad, no un requisito.',
                     'Lo que sí obliga, referencia a referencia, es tener '
                     'resuelta su información de alérgenos antes de ponerla en '
                     'vitrina, y saber si va a vitrina refrigerada o de '
                     'ambiente: cada referencia nueva es una fila más en las '
                     'dos cosas.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Referencias con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!E39', 'num'),
                    C('Referencias con veredicto de revisar precio', f'{X_CARTA}!Decisión de Surtido!E40', 'num'),
                    C('Referencias con veredicto de retirar', f'{X_CARTA}!Decisión de Surtido!E41', 'num'),
                    C('Margen ponderado de las referencias que se mantienen', f'{X_CARTA}!Decisión de Surtido!F39', 'eur2'),
                    C('Margen ponderado de las referencias a retirar', f'{X_CARTA}!Decisión de Surtido!F41', 'eur2'),
                    C('Margen de contribución medio por pieza de la carta', f'{X_CARTA}!Mix y Ticket Medio!F47', 'eur2'),
                ],
                'sector': ['PS-43', 'PA-21'],
                'tablas': [{
                    'titulo': 'Cómo queda la carta tras el filtro de margen y rotación (carta-de-apertura-y-escandallo.xlsx, hoja «Decisión de Surtido»)',
                    'src': (X_CARTA, 'Decisión de Surtido'),
                    'cols': [('Concepto', 'B', 'txt'), ('Referencias', 'E', 'num'),
                             ('Margen ponderado (€)', 'F', 'eur2')],
                    'filas': (39, 41),
                    'nota': 'El margen ponderado mide lo que aporta cada grupo al margen de '
                            'cien piezas vendidas con el mix previsto. Retirar dos referencias '
                            'de margen ponderado bajo casi no se nota en la caja y sí en la '
                            'compra. El margen ponderado medio por referencia de la carta es '
                            'de 0,04 €; el de las cien piezas vendidas con este mix, 1,07 €.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 4,
                'titulo': 'Producto de Terceros al Arrancar: Cuándo Sí y Qué te Prohíbe Decir',
                'resumen_indice': 'cuándo tiene sentido comprar elaborado el primer año, y qué no puedes poner en el escaparate si lo haces.',
                'palabras': 830, 'bloques': 1,
                'objetivo': 'Resolver una decisión que casi siempre se toma sin '
                            'saber que tiene consecuencias de etiquetado y de '
                            'escaparate.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['Comprar elaborado el primer año es la manera más rápida de '
                     'abrir con carta amplia y con poca inversión, y hay '
                     'formatos enteros del sector que funcionan así.',
                     'Lo que casi nadie sabe es que la decisión afecta a lo que '
                     'puedes escribir en el escaparate, y eso tiene definición '
                     'legal.'],
                    ['Opción A: todo de elaboración propia desde el día uno. '
                     'Opción B: base propia y complementos comprados. Opción C: '
                     'comprar elaborado y hornear en el local.',
                     'Lo que cambia: la inversión de equipamiento, el margen por '
                     'pieza, la carga de obrador y la mención que puedes usar.'],
                    ['La regla: se compara el margen por pieza del producto '
                     'propio contra el comprado, contando la mano de obra, no '
                     'sólo la materia. Muchas veces el comprado deja más euros '
                     'por pieza y menos diferenciación.',
                     'El segundo criterio es de posicionamiento: si el argumento '
                     'del negocio es la elaboración propia, comprar elaborado se '
                     'lo come.'],
                    ['La hoja de coste hora y mano de obra da el coste total por '
                     'unidad de cada referencia propia, con la mano de obra '
                     'dentro, que es la cifra con la que se compara un producto '
                     'comprado.',
                     'La hoja de variantes del checklist de equipamiento dice '
                     'qué dotación deja de hacer falta en cada formato.'],
                    ['La mención de elaboración propia es VOLUNTARIA y tiene dos '
                     'condiciones escritas: sólo puede venderse en el '
                     'establecimiento donde se elaboró o en sus sucursales, y '
                     'fraccionar o envasar producto de otro fabricante NO es '
                     'elaborar.',
                     'Consecuencia práctica: descongelar y hornear producto de '
                     'otro no te da derecho a esa mención, y ponerla igual es '
                     'una práctica engañosa.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Coste total por unidad del croissant de mantequilla', f'{X_CARTA}!Coste Hora y Mano de Obra!K6', 'eur2'),
                    C('Coste de mano de obra por unidad del croissant', f'{X_CARTA}!Coste Hora y Mano de Obra!I6', 'eur2'),
                    C('Peso medio de la mano de obra sobre el coste total', f'{X_CARTA}!Coste Hora y Mano de Obra!R36', 'pct1'),
                    C('Inversión de referencia de la variante de punto caliente', f'{X_EQUIP}!Variante del Formato!I39', 'eur'),
                    C('Inversión de referencia del caso base con obrador', f'{X_EQUIP}!Variante del Formato!G39', 'eur'),
                    C('Coste hora de obrador', f'{X_CARTA}!Parámetros!B16', 'eur2'),
                ],
                'sector': ['PA-17', 'PA-24', 'PS-06'],
                'tablas': [{
                    'titulo': 'Qué puedes escribir en el escaparate según lo que hagas',
                    'cabecera': ['Lo que haces', '¿Puedes usar «ELABORACIÓN PROPIA»?', 'Dónde puedes venderlo con esa mención'],
                    'filas': [
                        ['Elaboras la pieza entera en tu obrador', 'Sí, si quieres: es voluntaria', 'En el local donde la elaboraste y en tus sucursales'],
                        ['Elaboras la base y compras el relleno o la cobertura', 'Depende de qué se considere la elaboración de esa pieza: hay que poder justificarlo', 'Igual que arriba'],
                        ['Compras congelado de otro fabricante y lo horneas', 'No: hornear producto ajeno no es elaborar', 'No aplica'],
                        ['Compras elaborado y lo fraccionas o lo envasas', 'No: la norma dice expresamente que fraccionar o envasar no es elaborar', 'No aplica'],
                        ['Elaboras en tu obrador central y vendes en tu sucursal', 'Sí', 'En el central y en las sucursales de la misma titularidad'],
                        ['Elaboras para otra tienda de distinta titularidad', 'Esa tienda no puede usar la mención', 'Sólo tú, en tus propios establecimientos'],
                    ],
                    'nota': 'Comprobado el 10 de septiembre de 2026 sobre el art. 11 del '
                            'RD 1021/2022. La mención es gratuita y voluntaria: nadie te obliga '
                            'a ponerla, pero si la pones tiene que ser verdad.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 5,
                'titulo': 'Cuánto Roscón Produzco el Primer Año',
                'resumen_indice': 'cómo se dimensiona la campaña grande sin histórico, y qué palanca se usa cuando no cabe en el obrador.',
                'palabras': 850, 'bloques': 1,
                'objetivo': 'Resolver la decisión de volumen de la campaña que '
                            'decide el año, con la capacidad real del obrador '
                            'delante y sin histórico de ventas.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['La campaña grande concentra en unos pocos días una parte '
                     'enorme de la facturación del año, y el primer año se '
                     'dimensiona a ciegas porque no hay histórico.',
                     'Producir de menos deja ventas en la calle; producir de más '
                     'convierte el producto estrella en merma el día siguiente.'],
                    ['Opción A: producir contra encargo con fecha límite de '
                     'reserva. Opción B: producir un cupo cerrado y venderlo '
                     'hasta agotar. Opción C: mezcla de las dos, con un cupo '
                     'reservado para mostrador.',
                     'Lo que cambia: el riesgo de merma, la caja adelantada en '
                     'materia prima y la necesidad de refuerzo.'],
                    ['La regla: el cupo lo pone la capacidad del obrador de esos '
                     'días concretos, no la ambición. Se calcula el déficit '
                     'diario y se decide qué palanca lo cubre.',
                     'El segundo criterio es de caja: la materia prima de la '
                     'campaña se compra semanas antes de cobrarla, y eso hay que '
                     'poder financiarlo.'],
                    ['La hoja de capacidad contra demanda del pico da la demanda '
                     'diaria, el déficit y las horas de obrador que harían '
                     'falta; la de refuerzo y tesorería da el coste del refuerzo '
                     'y el dinero inmovilizado.',
                     'El calendario de fechas y de tareas de cada campaña está '
                     'en el Kit de Tareas Pastelería, no aquí.'],
                    ['No hay norma que limite cuánto puedes producir, pero sí la '
                     'hay sobre CÓMO: lo que se adelanta con frío tiene que '
                     'alcanzar la temperatura negativa en el centro con un '
                     'descenso ininterrumpido, y sale etiquetado con la fecha '
                     'de elaboración, la de congelación y la de caducidad o '
                     'consumo preferente.',
                     'Y el producto relleno que no sea estable a temperatura '
                     'ambiente tiene su techo de temperatura de conservación, '
                     'que manda sobre cualquier plan de producción: si no cabe '
                     'en la vitrina refrigerada, no se produce.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Demanda de piezas al día en la campaña grande', f'{X_EST}!Capacidad vs Demanda del Pico!D6', 'num'),
                    C('Déficit diario de piezas en esa campaña', f'{X_EST}!Capacidad vs Demanda del Pico!H6', 'num'),
                    C('Horas de obrador al día que harían falta', f'{X_EST}!Capacidad vs Demanda del Pico!M6', 'num1'),
                    C('Facturación incremental de la campaña sin IVA', f'{X_EST}!Calendario de 6 Picos!O6', 'eur'),
                    C('Coste del refuerzo de la campaña', f'{X_EST}!Refuerzo y Tesorería!F6', 'eur2'),
                    C('Tesorería inmovilizada en la campaña', f'{X_EST}!Refuerzo y Tesorería!K6', 'eur2'),
                ],
                'sector': ['PS-41', 'PS-35', 'PS-37', 'PS-46'],
                'tablas': [{
                    'titulo': 'Capacidad contra demanda en las seis campañas (estacionalidad-y-picos.xlsx, hoja «Capacidad vs Demanda del Pico»)',
                    'src': (X_EST, 'Capacidad vs Demanda del Pico'),
                    'cols': [('Campaña', 'A', 'txt'), ('Días', 'B', 'num'),
                             ('Demanda de piezas al día', 'D', 'num'),
                             ('Capacidad en campaña', 'G', 'num'),
                             ('Déficit diario', 'H', 'num'),
                             ('Piezas que puedes adelantar', 'K', 'num'),
                             ('¿Aguantas?', 'N', 'txt')],
                    'filas': (6, 11),
                    'nota': 'Los factores de campaña son supuestos calibrados con casos '
                            'publicados. Lo que no se puede adelantar con frío es lo que marca '
                            'el techo real del cupo.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 6,
                'titulo': 'Aceptar el Primer Encargo de Comunión sin Histórico',
                'resumen_indice': 'qué encargo se acepta cuando todavía no sabes cuánto tardas, y con qué anticipo.',
                'palabras': 830, 'bloques': 1,
                'objetivo': 'Resolver la decisión que más veces sale cara el '
                            'primer año: aceptar un encargo grande sin saber '
                            'cuánto ocupa ni cuánto cuesta.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['La temporada de comuniones no es un pico de tres días: es '
                     'una meseta de semanas, y llega justo cuando el obrador '
                     'todavía se está rodando.',
                     'El primer encargo grande se acepta por ilusión y se '
                     'produce por la noche. Lo que hay que decidir antes es '
                     'cuánto de eso cabe.'],
                    ['Opción A: aceptar todo lo que entre. Opción B: aceptar '
                     'hasta un cupo diario cerrado. Opción C: aceptar sólo '
                     'referencias que ya están en la carta y escandalladas.',
                     'Lo que cambia: las horas de obrador comprometidas, el '
                     'riesgo de anulación y la merma si el cliente no recoge.'],
                    ['La regla: sin histórico se acepta lo que cabe en la '
                     'capacidad del obrador de ESE día, y sólo referencias con '
                     'escandallo hecho. Sin escandallo no hay precio, y sin '
                     'precio hay regalo.',
                     'El segundo criterio es el anticipo: cubre la materia prima '
                     'y filtra al cliente que no va a recoger.'],
                    ['La hoja de refuerzo y tesorería da los días con el dinero '
                     'parado y el coste del refuerzo de la meseta de '
                     'comuniones; la de canales da el margen de contribución del '
                     'canal de encargos.',
                     'La ficha y el registro de encargos, con su agenda, los '
                     'entrega el Kit de Tareas Pastelería.'],
                    ['No hay norma sobre anticipos ni sobre anulaciones, y hay '
                     'que decirlo: es política de la casa y tiene que estar '
                     'escrita antes del primer encargo.',
                     'Lo que sí obliga es la información de alérgenos, también '
                     'en el encargo, y el plazo legal del producto elaborado por '
                     'la vía del huevo.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Días que dura la campaña de comuniones', f'{X_EST}!Calendario de 6 Picos!E10', 'num'),
                    C('Días con el dinero parado en esa campaña', f'{X_EST}!Refuerzo y Tesorería!M10', 'num'),
                    C('Coste del refuerzo de la campaña de comuniones', f'{X_EST}!Refuerzo y Tesorería!F10', 'eur2'),
                    C('Margen de contribución del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!G7', 'pct0'),
                    C('Ventas anuales del canal de encargos', f'{X_PLAN}!Canales y Punto Muerto!H7', 'eur'),
                    C('Piezas al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
                ],
                'sector': ['PS-53', 'PA-21', 'PA-15'],
                'tablas': [{
                    'titulo': 'El coste y la caja de cada campaña (estacionalidad-y-picos.xlsx, hoja «Refuerzo y Tesorería»)',
                    'src': (X_EST, 'Refuerzo y Tesorería'),
                    'cols': [('Campaña', 'A', 'txt'), ('Personas de refuerzo', 'B', 'num'),
                             ('Coste del refuerzo (€)', 'F', 'eur2'),
                             ('Compra de materia de la campaña (€)', 'K', 'eur2'),
                             ('Días con el dinero parado', 'M', 'num'),
                             ('Resultado incremental (€)', 'Q', 'eur2')],
                    'filas': (6, 11),
                    'nota': 'La meseta de comuniones es la campaña con más días de dinero '
                            'parado del año: se compra pronto y se cobra tarde.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 7,
                'titulo': 'El Primer Contrato con Otra Tienda: a Qué Precio y en Qué Momento Cambia tu Registro',
                'resumen_indice': 'cuándo compensa vender a cafeterías y restaurantes, y cuándo ese canal te obliga a inscribirte en el registro general.',
                'palabras': 850, 'bloques': 1,
                'objetivo': 'Resolver la decisión de abrir el canal de '
                            'suministro a otras tiendas sabiendo qué margen deja '
                            'de verdad y qué régimen de registro activa.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El primer contrato con una cafetería llega solo y parece '
                     'dinero gratis: volumen fijo, sin escaparate y sin merma de '
                     'vitrina.',
                     'Lo que no se ve el primer día: el precio es más bajo, el '
                     'cobro es a plazo y el canal puede cambiarte el régimen de '
                     'registro sanitario.'],
                    ['Opción A: no abrir el canal. Opción B: abrirlo con un tope '
                     'consciente por debajo del umbral. Opción C: abrirlo sin '
                     'tope y asumir la inscripción en el registro general.',
                     'Lo que cambia: el margen medio ponderado, los días de '
                     'cobro, el punto muerto y los papeles.'],
                    ['La regla: el canal se juzga por su margen de CONTRIBUCIÓN, '
                     'no por su margen bruto, y se mira qué le pasa al punto '
                     'muerto al quitarlo. Si el punto muerto baja al quitarlo, '
                     'el canal está restando.',
                     'El segundo criterio es de riesgo: un solo cliente que sea '
                     'grande concentra el cobro y el volumen en una sola firma.'],
                    ['La hoja de canales y punto muerto da el margen de '
                     'contribución de cada canal, el punto muerto con y sin ese '
                     'canal y su peso sobre las ventas.',
                     'La hoja de suministro a otras tiendas del libro de '
                     'licencias resuelve el árbol completo con tus kilos y tus '
                     'destinatarios.'],
                    ['La puerta de entrada primero: el artículo sólo se activa si '
                     'suministras a comercios minoristas de DISTINTA '
                     'titularidad. Si entras, las tres condiciones son '
                     'acumulativas, y dentro de «marginal» hay dos vías '
                     'alternativas de las que basta cumplir una.',
                     'La que más fácil se rompe es «restringido»: basta con '
                     'servir a un solo cliente inscrito en el registro general. '
                     'Y con el canal abierto vienen la declaración responsable y '
                     'el registro de a quién, cuánto y cuándo.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Peso del suministro a otras tiendas sobre las ventas', f'{X_PLAN}!Canales y Punto Muerto!B25', 'pct0'),
                    C('Margen de contribución de ese canal', f'{X_PLAN}!Canales y Punto Muerto!G8', 'pct0'),
                    C('Punto muerto mensual con todos los canales', f'{X_PLAN}!Canales y Punto Muerto!B18', 'eur2'),
                    C('Punto muerto mensual sin ese canal', f'{X_PLAN}!Canales y Punto Muerto!B19', 'eur2'),
                    C('Umbral de la primera vía del artículo 3', f'{X_LEGAL}!Suministro a Otros Minoristas!B20', 'pct0'),
                    C('Umbral de la segunda vía del artículo 3, en kilos a la semana', f'{X_LEGAL}!Suministro a Otros Minoristas!B23', 'num'),
                ],
                'sector': ['PS-53', 'PA-02', 'PA-02b', 'PA-02c', 'PA-02d'],
                'tablas': [{
                    'titulo': 'Los cuatro canales y lo que deja cada uno (plan-financiero-3-anos-pasteleria.xlsx, hoja «Canales y Punto Muerto»)',
                    'src': (X_PLAN, 'Canales y Punto Muerto'),
                    'cols': [('Canal', 'A', 'txt'),
                             ('Ventas del año de crucero (€)', 'H', 'eur'),
                             ('Parte de las ventas (%)', 'B', 'pct0'),
                             ('Margen bruto (%)', 'C', 'pct0'),
                             ('Margen de contribución (%)', 'G', 'pct0'),
                             ('Días de cobro', 'F', 'num')],
                    'filas': (6, 10),
                    'nota': 'El peso del canal de suministro a otras tiendas sale de un caso '
                            'publicado; el resto del reparto es un supuesto del caso modelado.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 8,
                'titulo': 'Contratar Pastelero o Tirar de Ayudante',
                'resumen_indice': 'qué cuesta cada perfil con la Seguridad Social dentro, y qué se pierde bajando de categoría.',
                'palabras': 830, 'bloques': 1,
                'objetivo': 'Resolver la decisión de plantilla que más veces se '
                            'toma por precio: cubrir el obrador con un perfil '
                            'más barato y descubrir después lo que no cubre.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El obrador necesita alguien que sostenga la producción '
                     'cuando el dueño no está, y ese alguien tiene precio de '
                     'convenio.',
                     'La tentación es cubrirlo con media jornada de un perfil de '
                     'apoyo, porque la diferencia de bruto parece pequeña.'],
                    ['Opción A: contratar un perfil especialista a jornada '
                     'completa. Opción B: dos medias jornadas de perfiles de '
                     'apoyo. Opción C: jornada completa de apoyo y formación '
                     'interna.',
                     'Lo que cambia: el coste de empresa al año, la autonomía '
                     'del obrador y el riesgo de que el negocio dependa de una '
                     'sola persona.'],
                    ['La regla: se compara COSTE DE EMPRESA, no bruto, y se '
                     'compara por hora de obrador cubierta, no por nómina. La '
                     'Seguridad Social a cargo de la empresa cambia el orden de '
                     'la comparación.',
                     'El segundo criterio es de cobertura: dos medias jornadas '
                     'no cubren un turno de madrugada completo, y eso se ve en '
                     'el cuadrante antes que en la nómina.'],
                    ['La hoja de horas y coste del libro de turnos da el coste de '
                     'empresa al año y el coste por hora de cada perfil, y la de '
                     'turnos semanales dice si el cuadrante queda cubierto.',
                     'Las fichas de tarea de cada perfil las entrega el Kit de '
                     'Tareas Pastelería.'],
                    ['El convenio provincial fija el grupo y el bruto de cada '
                     'puesto, y en este sector manda el convenio sobre el '
                     'salario mínimo: el grupo más bajo del convenio de '
                     'referencia ya está por encima de la referencia anual del '
                     'mínimo.',
                     'Y la formación de quien entre nuevo es obligación del '
                     'empresario, con registro, desde el primer día.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Coste de empresa al año del perfil especialista de obrador', f'{X_TURNOS}!Horas y Coste!K8', 'eur'),
                    C('Coste de empresa al año del perfil de apoyo a media jornada', f'{X_TURNOS}!Horas y Coste!K9', 'eur'),
                    C('Coste por hora del perfil especialista', f'{X_TURNOS}!Horas y Coste!L8', 'eur2'),
                    C('Coste por hora del perfil de apoyo', f'{X_TURNOS}!Horas y Coste!L9', 'eur2'),
                    C('Coste de personal al año de toda la plantilla', f'{X_TURNOS}!Horas y Coste!E16', 'eur'),
                    C('Bruto anual del grupo más bajo del convenio', f'{X_TURNOS}!Parámetros!C16', 'eur2'),
                    C('Referencia anual del salario mínimo', f'{X_TURNOS}!Parámetros!C17', 'eur'),
                ],
                'sector': ['PA-32', 'PA-33', 'PS-104', 'PS-105'],
                'tablas': [{
                    'titulo': 'Coste de empresa por perfil y por hora (plantilla-turnos-y-coste-personal.xlsx, hoja «Horas y Coste»)',
                    'src': (X_TURNOS, 'Horas y Coste'),
                    'cols': [('Id', 'A', 'txt'), ('Persona', 'B', 'txt'),
                             ('Grupo de convenio', 'D', 'txt'),
                             ('Bruto mensual del grupo (€)', 'E', 'eur2'),
                             ('Jornada equivalente', 'F', 'num1'),
                             ('Coste de empresa al año (€)', 'K', 'eur'),
                             ('Coste por hora (€)', 'L', 'eur2')],
                    'filas': (7, 12),
                    'nota': V_CONV,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 9,
                'titulo': 'Abrir en Septiembre o en Febrero',
                'resumen_indice': 'cómo se elige el mes de apertura con la ruta crítica y el calendario de campañas delante.',
                'palabras': 820, 'bloques': 1,
                'objetivo': 'Resolver la decisión de fecha: no se elige el mes '
                            'de apertura, se calcula, y luego se comprueba que '
                            'no cae dentro de una campaña.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['Todo el mundo quiere abrir cuanto antes, y la fecha de '
                     'apertura no es una decisión: es el resultado de encadenar '
                     'los hitos con sus dependencias.',
                     'Lo que sí es decisión es cuándo se arranca el proyecto, '
                     'porque eso mueve el mes de apertura entero.'],
                    ['Opción A: arrancar ya y abrir cuando salga. Opción B: '
                     'calcular hacia atrás desde el mes en el que quieres abrir. '
                     'Opción C: retrasar la apertura para llegar rodado a la '
                     'campaña grande.',
                     'Lo que cambia: los meses de renta pagada sin facturar, la '
                     'presión sobre el equipo en el estreno y la caja del primer '
                     'trimestre.'],
                    ['La regla: no se abre dentro de una campaña. Estrenar '
                     'equipo, plantilla y proveedores el día que más producción '
                     'hay es acumular los tres riesgos a la vez.',
                     'El segundo criterio es de rodaje: hay que dejar margen '
                     'suficiente entre la apertura y la campaña grande para '
                     'haber probado el cuadrante y la producción.'],
                    ['La hoja de cronograma y ruta crítica del libro de licencias '
                     'da la duración total, los hitos sin holgura, el mes de '
                     'apertura y el aviso de si cae dentro de una campaña.',
                     'El plazo crítico de entrega del equipamiento sale del '
                     'checklist de equipamiento y es el que más veces mueve la '
                     'fecha.'],
                    ['No hay norma que fije cuándo se abre, pero sí plazos que no '
                     'controlas: el trámite de actividad depende de tu '
                     'ayuntamiento y la comunicación sanitaria autonómica no '
                     'habilita para abrir.',
                     'Y en la comunidad de ejemplo, quien ya estaba abierto '
                     'tiene un período transitorio para inscribirse que vence en '
                     'una fecha concreta.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Duración total del proyecto, en meses', f'{X_LEGAL}!Cronograma y Ruta Crítica!C38', 'num1'),
                    C('Hitos sin holgura en la ruta crítica', f'{X_LEGAL}!Cronograma y Ruta Crítica!C39', 'num'),
                    C('Mes natural en el que abre el caso modelado', f'{X_LEGAL}!Cronograma y Ruta Crítica!C40', 'num'),
                    C('Plazo crítico de entrega del equipamiento, en semanas', f'{X_EQUIP}!Equipamiento!I53', 'num'),
                    C('Margen de ese plazo hasta la apertura, en semanas', f'{X_EQUIP}!Equipamiento!I55', 'num'),
                    C('Peso de la campaña grande sobre las ventas del año', f'{X_EST}!Peso sobre el Año!D24', 'pct1'),
                ],
                'sector': ['PA-04', 'PA-39'],
                'tablas': [{
                    'titulo': 'Los doce hitos y su ruta crítica (checklist-legal-y-licencias.xlsx, hoja «Cronograma y Ruta Crítica»)',
                    'src': (X_LEGAL, 'Cronograma y Ruta Crítica'),
                    'cols': [('Id', 'A', 'txt'), ('Hito', 'B', 'txt'),
                             ('Duración (meses)', 'C', 'num1'),
                             ('Depende de', 'D', 'txt'),
                             ('Acaba (mes del proyecto)', 'H', 'num1'),
                             ('Holgura (meses)', 'I', 'num1'),
                             ('¿Ruta crítica?', 'J', 'txt')],
                    'filas': (9, 20),
                    'nota': 'Las duraciones son supuestos de planificación. El plazo del '
                            'trámite de actividad depende de tu ayuntamiento y es el que más '
                            'varía.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 10,
                'titulo': 'Empezar en Casa Dentro de la Legalidad: Qué Puedo Vender y Qué No',
                'resumen_indice': 'la lista blanca de la vivienda, las prohibiciones que sí tienen salvedad autonómica y los tres límites del volumen.',
                'palabras': 820, 'bloques': 1,
                'objetivo': 'Resolver la decisión del segmento con más búsqueda '
                            'del nicho: qué se puede elaborar y vender desde una '
                            'vivienda, y qué no, sin afirmar de más ni de menos.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['Es la puerta de entrada más frecuente al oficio: se vende '
                     'por encargo desde casa, con clientela por mensajería y por '
                     'redes, y llega el momento de legalizarlo.',
                     'El miedo real no es el trámite, es descubrir que lo que ya '
                     'se está vendiendo no entra en la lista de lo que se puede '
                     'elaborar en una vivienda.'],
                    ['Opción A: legalizar la vivienda con declaración '
                     'responsable y ajustar el catálogo a lo permitido. Opción '
                     'B: usar un obrador compartido. Opción C: dar el salto '
                     'directamente a un local pequeño.',
                     'Lo que cambia: la inversión, el catálogo que puedes '
                     'vender, los canales por los que puedes vender y el tope de '
                     'volumen.'],
                    ['La regla: primero se comprueba si tu producto entra en la '
                     'lista blanca, y sólo después se hace el trámite. Al revés '
                     'se legaliza una actividad que luego hay que recortar.',
                     'El segundo criterio es de crecimiento: la vivienda tiene '
                     'un techo de volumen que no se puede negociar, así que si '
                     'el plan es crecer, la vivienda es una etapa y no un '
                     'destino.'],
                    ['La hoja de ruta doméstica del libro de licencias da los '
                     'tres semáforos: el del tope de kilos, el de '
                     'proporcionalidad con los metros útiles y el aviso de que '
                     'hay que demostrarlo documentalmente.',
                     'La hoja de variantes de la calculadora de inversión da lo '
                     'que cuesta esa opción frente a las demás.'],
                    ['Por defecto sólo entra la repostería estable a temperatura '
                     'ambiente: una tarta rellena de nata NO entra en la lista '
                     'del art. 13.8 SALVO que tu comunidad autónoma la haya '
                     'añadido por la vía de la letra e, y hay comunidades que ya '
                     'han ejercido esa letra ampliando la lista y los canales.',
                     'De las cinco prohibiciones, sólo la de colectividades y '
                     'eventos es incondicional; las otras tres tienen salvedad '
                     'autonómica y la de congelar admite mantener en congelación '
                     'la materia prima comprada ya congelada. Y todo lo que sale '
                     'de una vivienda va etiquetado con la mención de elaborado '
                     'en vivienda particular y la fecha de elaboración.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Tope absoluto de kilos a la semana del artículo 13.9', f'{X_LEGAL}!Ruta Doméstica!B13', 'num'),
                    C('Metros útiles del ejemplo doméstico', f'{X_LEGAL}!Ruta Doméstica!B6', 'num'),
                    C('Kilos a la semana del ejemplo doméstico', f'{X_LEGAL}!Ruta Doméstica!B7', 'num'),
                    C('Kilos por metro cuadrado útil y semana', f'{X_LEGAL}!Ruta Doméstica!B16', 'num1'),
                    C('Criterio propio de proporcionalidad de la casa', f'{X_LEGAL}!Ruta Doméstica!B15', 'num'),
                    C('Inversión de apertura de la variante de obrador en casa', f'{X_CAPEX}!Variante del Formato!I16', 'eur'),
                ],
                'sector': ['PA-29', 'PA-29b', 'PA-29c', 'PA-29d', 'PS-01'],
                'tablas': [{
                    'titulo': 'La lista blanca de la vivienda, letra a letra (checklist-legal-y-licencias.xlsx, hoja «Ruta Doméstica»)',
                    'src': (X_LEGAL, 'Ruta Doméstica'),
                    'cols': [('Letra y qué permite', 'A', 'txt'),
                             ('Qué NO entra por ahí', 'C', 'txt')],
                    'filas': (22, 26),
                    'nota': V_VIVIENDA,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 11,
                'titulo': 'Envío a Domicilio: Qué Producto Viaja y Cuál No',
                'resumen_indice': 'el criterio real del envío no es jurídico, es de cadena de frío, y la carta dice cuál aguanta.',
                'palabras': 820, 'bloques': 1,
                'objetivo': 'Resolver la decisión de abrir el canal de envío '
                            'sabiendo qué referencias pueden viajar y qué '
                            'obligaciones de información trae la venta a '
                            'distancia.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El envío parece la manera barata de ampliar mercado sin '
                     'abrir otra tienda, y en pastelería choca con la física '
                     'antes que con la ley.',
                     'La pregunta correcta no es si puedes vender online, que '
                     'puedes, sino qué referencia de tu carta llega en '
                     'condiciones.'],
                    ['Opción A: enviar sólo producto estable a temperatura '
                     'ambiente. Opción B: enviar refrigerado con transporte '
                     'controlado. Opción C: no enviar y usar la web sólo para '
                     'recoger en tienda.',
                     'Lo que cambia: el coste de servir, el margen de '
                     'contribución del canal y el riesgo de reclamación.'],
                    ['La regla: viaja lo que aguanta su temperatura de '
                     'conservación durante todo el trayecto, no lo que aguanta '
                     'la caja. Y el plazo legal del producto elaborado por la '
                     'vía del huevo se cuenta desde la elaboración, no desde el '
                     'envío.',
                     'El segundo criterio es económico: el coste de servir del '
                     'canal se come una parte del margen, y hay que verlo antes '
                     'de fijar el precio de envío.'],
                    ['La hoja de decisión de huevo y temperatura del libro de la '
                     'carta clasifica las treinta referencias en vitrina '
                     'refrigerada o de ambiente y da el plazo legal de cada una.',
                     'La hoja de canales da el margen de contribución del canal '
                     'de envío con su coste de servir dentro.'],
                    ['Vender online al consumidor final NO te obliga al registro '
                     'general ni te aplica el radio del suministro entre '
                     'comercios: la definición legal de minorista ya incluye la '
                     'entrega a distancia.',
                     'Lo que sí obliga: mantener la temperatura durante todo el '
                     'transporte, tener toda la información obligatoria '
                     'disponible ANTES de la compra —con la única excepción de '
                     'la fecha de duración— y completa en la entrega, sin '
                     'cobrarla. Para producto no envasado, lo obligatorio antes '
                     'de comprar son los alérgenos. Y la caja de envío te '
                     'convierte en envasador a efectos de la normativa de '
                     'envases.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Referencias que necesitan vitrina refrigerada', f'{X_CARTA}!Decisión de Huevo y Temperatura!G38', 'num'),
                    C('Referencias que van en vitrina de ambiente', f'{X_CARTA}!Decisión de Huevo y Temperatura!G39', 'num'),
                    C('Referencias con plazo legal de veinticuatro horas', f'{X_CARTA}!Decisión de Huevo y Temperatura!G43', 'num'),
                    C('Temperatura que manda en el producto relleno', f'{X_CARTA}!Parámetros!B28', 'num'),
                    C('Margen de contribución del canal de envío y online', f'{X_PLAN}!Canales y Punto Muerto!G9', 'pct0'),
                    C('Coste de servir del canal de envío y online', f'{X_PLAN}!Canales y Punto Muerto!D9', 'pct0'),
                ],
                'sector': ['PA-01b', 'PA-27', 'PA-27b', 'PA-28', 'PA-12'],
                'tablas': [{
                    'titulo': 'Qué sale de la hoja de huevo y temperatura (carta-de-apertura-y-escandallo.xlsx, hoja «Decisión de Huevo y Temperatura»)',
                    'src': (X_CARTA, 'Decisión de Huevo y Temperatura'),
                    'cols': [('Lo que mide', 'B', 'txt'), ('Referencias', 'G', 'num'),
                             ('Para qué sirve', 'J', 'txt')],
                    'filas': (38, 45),
                    'nota': V_TEMP,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 12,
                'titulo': 'Qué Hago con lo que no se Vende Hoy',
                'resumen_indice': 'el rincón del producto con defecto, la donación y el alcance exacto de la exención en desperdicio alimentario.',
                'palabras': 820, 'bloques': 1,
                'objetivo': 'Resolver la decisión diaria que más dinero tira a '
                            'la basura, con la base legal que la permite y con '
                            'el alcance exacto de lo que obliga.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['En pastelería el producto no vendido no espera al día '
                     'siguiente, y el primer año la merma es alta porque todavía '
                     'no se conoce la demanda por referencia.',
                     'Se tira producto que se podría vender, y se vende producto '
                     'que no se debería vender: las dos cosas pasan por no tener '
                     'la política escrita.'],
                    ['Opción A: tirar. Opción B: vender con descuento en un '
                     'rincón identificado. Opción C: donar. Opción D: usar como '
                     'consumo de personal.',
                     'Lo que cambia: los euros recuperados, la percepción de la '
                     'marca y las obligaciones que se activan con cada una.'],
                    ['La regla: primero se reduce la producción con datos —la '
                     'merma se mide por referencia— y sólo después se decide qué '
                     'hacer con lo que sobra. Descontar sin medir convierte el '
                     'descuento en política de precios.',
                     'El segundo criterio es de precio de referencia: rebajar '
                     'para no tirar no debe estropear el precio anterior de tu '
                     'carta, y la norma tiene una excepción escrita para eso.'],
                    ['La merma objetivo del caso modelado está en la hoja de '
                     'parámetros del libro de la carta, y el food cost servido '
                     'la incluye: la diferencia entre el food cost de materia y '
                     'el servido es lo que se está yendo.',
                     'El registro diario de lo producido contra lo vendido lo '
                     'entrega el Kit de Tareas Pastelería.'],
                    ['Vender producto con defecto de forma, de tamaño, de '
                     'etiquetado o de envasado es legal, bajo tu '
                     'responsabilidad, informando al cliente y con dos '
                     'exclusiones. Donar excedente también es legal y está '
                     'regulado.',
                     'En desperdicio alimentario, la exención por superficie '
                     'alcanza SÓLO al apartado del plan de prevención y de los '
                     'convenios de donación; siguen obligando los otros tres, '
                     'entre ellos que ninguna cláusula de contrato pueda '
                     'prohibirte donar. Y lo que rebajes para no tirar producto '
                     'próximo a caducar no cuenta como precio anterior a efectos '
                     'de la regla de los treinta días.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Merma objetivo del caso modelado', f'{X_CARTA}!Parámetros!B34', 'pct0'),
                    C('Food cost de materia de la carta', f'{X_CARTA}!Mix y Ticket Medio!F44', 'pct1'),
                    C('Food cost servido, con merma y packaging', f'{X_CARTA}!Mix y Ticket Medio!F45', 'pct1'),
                    C('Margen de contribución medio por pieza', f'{X_CARTA}!Mix y Ticket Medio!F47', 'eur2'),
                    C('Referencias que van en vitrina refrigerada', f'{X_CARTA}!Decisión de Huevo y Temperatura!G38', 'num'),
                    C('Referencias con plazo legal de veinticuatro horas', f'{X_CARTA}!Decisión de Huevo y Temperatura!G43', 'num'),
                ],
                'sector': ['PA-20', 'PA-19', 'PA-31', 'PA-31b', 'PA-44'],
                'tablas': [{
                    'titulo': 'Qué puedes hacer con lo que no se ha vendido, y qué obligación trae cada vía',
                    'cabecera': ['Vía', '¿Es legal?', 'Con qué condición', 'Base normativa'],
                    'filas': [
                        ['Vender con defecto de forma o de tamaño', 'Sí', 'Informando al cliente y bajo tu responsabilidad; no aplica a frutas y hortalizas', 'Art. 17 del RD 1021/2022'],
                        ['Vender con defecto de etiquetado o de envasado', 'Sí', 'Igual, salvo conservas con abombamiento', 'Art. 17 del RD 1021/2022'],
                        ['Rebajar producto próximo a la fecha de consumo', 'Sí', 'Esa rebaja no cuenta como precio anterior a efectos de la regla de los treinta días', 'Art. 20.1 de la Ley 7/1996 en la redacción del RD-ley 24/2021'],
                        ['Donar excedente', 'Sí', 'Conforme al capítulo de redistribución del reglamento europeo de higiene', 'Art. 16 del RD 1021/2022'],
                        ['Firmar un contrato que te prohíba donar', 'No', 'Esa cláusula es nula de pleno derecho', 'Art. 6.3 de la Ley 1/2025'],
                        ['Estropear a propósito lo que sobra para que no se use', 'No', 'Prohibido con independencia de tu superficie', 'Art. 6.5 de la Ley 1/2025'],
                        ['Tener plan de prevención de desperdicio', 'Depende', 'Exento por debajo del umbral de superficie; si además eres microempresa, fuera del artículo entero', 'Art. 6.4 y 6.6 de la Ley 1/2025'],
                    ],
                    'nota': 'Comprobado el 10 de septiembre de 2026. La exención por superficie '
                            'alcanza sólo al apartado del plan y de los convenios de donación: '
                            'los demás apartados siguen obligando.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
        ],
    },
]


# --------------------------------------------------------------------------
# Erratas permitidas: el detector de `documentos.py` toma por errata palabras
# correctas poco frecuentes en el corpus del blog. Se amplía MIRANDO EL
# CONTEXTO, nunca «corrigiendo» a ciegas. Hay que asignarla a GUIA **y a cada
# bonus por separado** (`_ERRATAS_OK` NO es una clave de `documentos.py`: es una
# variable local de este guion).
# --------------------------------------------------------------------------
_ERRATAS_OK = (
    # 2026-09-10, falsos positivos del detector en la primera pasada (todas correctas en contexto):
    'harían', 'harian', 'llévala', 'llevala', 'actualizará', 'actualizara', 'apuntado', 'cometido',
    'contratarlo', 'digan', 'librado', 'pinte', 'salda', 'tales', 'tardará', 'tardara', 'telefonía',
    'telefonia', 'trasposición', 'trasposicion', 'trátala', 'tratala', 'cámbialas', 'cambialas',
    'compraré', 'comprare', 'confíe', 'confie', 'rodar', 'rodando',
    # Vocabulario del oficio de pastelería y panadería
    'obrador', 'obradores', 'obrar', 'abatidor', 'abatidores', 'abatir',
    'laminadora', 'laminadoras', 'laminado', 'amasadora', 'amasadoras',
    'amasada', 'amasado', 'planetaria', 'fermentación', 'fermentacion',
    'fermentada', 'fermentado', 'levado', 'pastón', 'paston', 'pastones',
    'hojaldre', 'hojaldres', 'bollería', 'bolleria', 'repostería',
    'reposteria', 'repostero', 'repostera', 'confitería', 'confiteria',
    'pastelería', 'pasteleria', 'pastelero', 'pastelera', 'entremet',
    'entremets', 'croissant', 'croissants', 'viennoiserie', 'ensaimada',
    'ensaimadas', 'napolitana', 'napolitanas', 'caracola', 'caracolas',
    'milhojas', 'macaron', 'macarons', 'tartaleta', 'tartaletas', 'lionesa',
    'lionesas', 'profiterol', 'profiteroles', 'palmera', 'palmeras',
    'roscón', 'roscon', 'roscones', 'torrija', 'torrijas', 'buñuelo',
    'bunuelo', 'buñuelos', 'panellets', 'polvorón', 'polvoron', 'polvorones',
    'mantecado', 'mantecados', 'turrón', 'turron', 'turrones', 'chapata',
    'hogaza', 'sacher', 'crema', 'nata', 'ganache', 'cobertura', 'coberturas',
    'atemperadora', 'atemperar', 'templado', 'bombonería', 'bomboneria',
    'gramaje', 'gramajes', 'tanda', 'tandas', 'merma', 'mermas', 'vitrina',
    'vitrinas', 'mostrador', 'mostradores', 'despacho', 'partida', 'partidas',
    'escandallo', 'escandallos', 'escandallar', 'escandallada',
    'escandalladas', 'costeo', 'exhibidor', 'exhibidores',
    # Vocabulario de local, obra e instalaciones
    'cubierta', 'cumbrera', 'campana', 'campanas', 'conducto', 'conductos',
    'extracción', 'extraccion', 'extractor', 'caudal', 'forjado', 'acometida',
    'desagüe', 'desague', 'lavamanos', 'fregadero', 'vestuario', 'vestuarios',
    'aseo', 'aseos', 'traspaso', 'traspasos', 'arrendamiento', 'fianza',
    'planeamiento', 'urbanístico', 'urbanistico', 'ordenanza', 'ordenanzas',
    'estatutos', 'inscrita', 'inscritos', 'visado', 'boletín', 'boletin',
    'legalización', 'legalizacion', 'accesibilidad', 'estanquidad',
    'combustión', 'combustion', 'recirculación', 'recirculacion',
    'recircular', 'climatización', 'climatizacion',
    # Vocabulario sanitario y normativo
    'autocontrol', 'alérgeno', 'alergeno', 'alérgenos', 'alergenos',
    'manipulador', 'manipuladores', 'ovoproducto', 'ovoproductos',
    'pasteurizado', 'pasterizada', 'congelación', 'congelacion', 'congelar',
    'congelado', 'congelados', 'descongelado', 'recongelar', 'refrigerada',
    'refrigerado', 'refrigeración', 'refrigeracion', 'trazabilidad',
    'trazable', 'perecedero', 'perecederos', 'minorista', 'minoristas',
    'sucursal', 'sucursales', 'titularidad', 'habilitante', 'derogado',
    'derogada', 'derogados', 'vigencia', 'vigente', 'vigentes',
    'consolidado', 'articulado', 'preceptivas', 'declaración', 'declaracion',
    'responsable', 'excedente', 'excedentes', 'donación', 'donacion',
    'donable', 'redistribución', 'redistribucion', 'desperdicio',
    'microempresa', 'microempresas', 'reutilizable', 'reutilizables',
    'envasador', 'envasadora', 'envasar', 'envasado', 'fraccionar',
    'fraccionamiento', 'artesanal', 'artesanía', 'artesania', 'acreditación',
    'acreditacion', 'acreditable', 'incondicional', 'acumulativas',
    'alternativas', 'marginal', 'localizado', 'restringido',
    # Vocabulario económico, fiscal y laboral
    'escandallado', 'ponderado', 'ponderada', 'amortización', 'amortizacion',
    'amortizable', 'tesorería', 'tesoreria', 'circulante', 'carencia',
    'principal', 'cuota', 'cuotas', 'apalancamiento', 'repercutido',
    'soportado', 'liquidación', 'liquidacion', 'devengo', 'devenga',
    'epígrafe', 'epigrafe', 'epígrafes', 'epigrafes', 'convenio', 'convenios',
    'cotización', 'cotizacion', 'jornada', 'jornadas', 'cuadrante',
    'cuadrantes', 'polivalencia', 'contratación', 'contratacion',
    'dimensionado', 'estacionalidad', 'desestacionalizar', 'inmovilizado',
    'inmovilizada', 'incremental', 'payback', 'estimada', 'proyectada',
    # Palabras correctas que el corpus del blog no contiene
    'comprobable', 'comprobables', 'defendible', 'refutable', 'medible',
    'escalable', 'reproducible', 'sustituible', 'sustituibles', 'editable',
    'editables', 'calibrado', 'calibradas', 'modelado', 'modelada',
    'tabulada', 'tabuladas', 'acotado', 'acotada', 'cribado', 'eliminatorio',
    'eliminatorios', 'holgura', 'solape', 'solapan', 'anticipo', 'anticipos',
    'anulación', 'anulacion', 'recogida', 'reserva', 'cupo', 'cupos',
    'táper', 'taper', 'granel', 'rotación', 'rotacion', 'surtido',
    'antelación', 'antelacion', 'refuerzo', 'refuerzos', 'meseta',
    'madrugón', 'madrugon', 'papeleos', 'ración', 'racion', 'raciones',
    # Siglas y nombres propios que el léxico no conoce
    'APPCC', 'RGSEAA', 'BOE', 'BOCM', 'DOGC', 'DOGV', 'DOUE', 'CTE', 'RITE',
    'IAE', 'SMI', 'DGT', 'Verifactu', 'Hosply', 'Clara', 'Sosa', 'Puratos',
    'Callebaut', 'Valrhona', 'Debic', 'Coromina', 'Cospan', 'Docriluc',
    'Irinox', 'Sammic', 'Salva', 'Selmi', 'Unox', 'Smeg',
)
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
