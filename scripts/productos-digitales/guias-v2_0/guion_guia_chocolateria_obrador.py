#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
guion_guia_chocolateria_obrador.py — GUION de «Cómo Montar una Chocolatería»
v1.0 (SPEC `guia-chocolateria-SPEC.md`, §4, §4.2 y §4.3).

Mismo esquema que los hermanos (`guion_guia_pasteleria_obrador.py`, del 10-sep,
`guion_manual_chef_ejecutivo.py` y `guion_guia_food_cost_ingenieria_menu.py`):
un capítulo no se le pide a un redactor con un título, se le pide con un guion
CERRADO. Por capítulo van (a) el objetivo, (b) 4-6 epígrafes, (c) los puntos
concretos DE CADA EPÍGRAFE —`puntos_por_epigrafe`, la forma preferida de
`repartir_puntos()`—, (d) las cifras del propio producto citadas por
`fichero.xlsx!Hoja!Celda` —que `documentos.py` resuelve con openpyxl
`data_only` antes de escribir el prompt, así que el redactor recibe el NÚMERO,
no el fichero—, (e) los datos del sector por `id` de
`auditorias/guias-v2-research-sector.json` (ids `CHN-*` normativa, `CHS-*`
sector), (f) las tablas exigidas —que las construye el maquetador desde el
xlsx, no el redactor—, (g) el presupuesto de palabras y (h) lo que NO debe
decir.

Formato exacto de los puntos: `cap['puntos_por_epigrafe'] = {'<epígrafe
literal>': [punto, …]}`. Para que una clave no pueda desviarse del epígrafe
—`repartir_puntos()` aborta con `SystemExit` si eso pasa, y esos puntos se
perderían en silencio— cada capítulo declara PRIMERO su dict `PPE_nn` y luego
pone `'epigrafes': list(PPE_nn)`: la lista de epígrafes SE DERIVA del dict, así
que no hay dos sitios que puedan discrepar. Lo que va entero a todos los tramos
es `puntos_globales`, que NO se reparte.

REGLA DE LA LÍNEA (John, 2026-09-04): el texto de los productos digitales ya NO
lo escribe `bridge.py`. `dump_prompts.py` vuelca los prompts exactos que
construye `documentos.py` y un subagente Anthropic escribe cada bloque en la
caché `txt/`, verificándolo con `check_bloque.py`. Medidor de solape antes de
ensamblar: `guias-v2_0/solape.py <dir_txt>`.

FUENTE ÚNICA DE CIFRAS: los NUEVE libros de
`astro-site/public/dl/guia-chocolateria-obrador/`, que se LEEN y no se tocan.
Sus mapas de celdas (`guia-chocolateria/build/mapa-*.json`) son el CONTRATO:
toda coordenada de este guion sale de ahí o está verificada abriendo el libro
con `data_only` (12-09-2026, openpyxl `read_only`, un fichero cada vez). El
juego de datos del caso modelado —la bombonería «La Almendra»— es
`guia-chocolateria/datos_ejemplo.py`.

FUENTE ÚNICA DE LO LEGAL:
`auditorias/guia-chocolateria-verificacion-legal-2026-09-12.md` (109 fichas
`CHN-*`, verificación independiente contra fuentes primarias: BOE consolidado,
EUR-Lex consolidado, DOGC, Portal Jurídic, REGCON y la guía del RGSEAA).
**Los puntos legales de los capítulos 09, 10, 11, 12, 16, 19 y del anexo usan
la columna «Redacción SEGURA para el producto» de esa verificación, no la
síntesis del research.** Lo que esa verificación deja en `-EXCLUIDOS.json`
(`CHN-49d`, `CHN-50`, `CHN-70`, `CHN-79`, `CHN-80`, `CHN-98`…) **no existe como
afirmación** y se trata como «pregunta a tu ayuntamiento, a tu asesoría o a un
laboralista», nunca como dato.

UNIDAD DE CAPACIDAD DEL PAQUETE: el **bombón equivalente**. El libro 1 la
publica en su hoja «Cuello de Botella» (512 bombones al día que permite el
conjunto de equipos) y el libro 6 la recibe por celda verde en «Capacidad vs
Demanda del Pico». Una caja de 35 bombones es UNA venta y TREINTA Y SEIS
bombones equivalentes de obrador: por eso las piezas de venta y los bombones de
obrador NO son la misma cifra, y el texto lo dice con la etiqueta del mapa cada
vez que aparece (capítulos 05 y 07).

DOS FOOD COST, Y NO SE MEZCLAN: los libros 3 y 4 publican el food cost de cada
referencia SIN merma (el de escandallo puro, hoja «Coste de Cobertura» del
libro 3) y CON merma (el que sale de la merma de templado del libro 4, hojas
«Merma de Templado y Recortes» y «Coste Hora y Mano de Obra»). El capítulo 14
cita el de CON merma, que es el real; el capítulo 15 cita el de SIN merma sólo
cuando habla de sensibilidad al precio de la cobertura, y lo dice. Nunca se
citan los dos en el mismo párrafo sin decir cuál es cuál.

PERFILES LITERALES: **Chocolatero · Dependiente · Encargado**, que son los
NOMBRES DE HOJA de `kit-tareas-chocolateria/04-tareas-perfiles.xlsx`. Los
rótulos largos de ese mismo kit («Maestro Chocolatero / Obrador», «Dependiente
de Tienda», «Encargado de Turno») NO son los perfiles de la guía, y «maestro
chocolatero», «bombonero» y «oficial» están PROHIBIDOS como nombre de puesto.

Presupuesto (SPEC §4 y D50): 20 capítulos + anexo normativo, 90 páginas
prometidas, 37.000 palabras objetivo, 1.750 por capítulo, 2.100 los cuatro
legales largos (09, 10, 11 y 19) y 1.500 el anexo. `bloques`: **2** en 09, 10,
11, 12, 16 y 19; **1** en los catorce restantes y en el anexo. Bonus 1:
business plan modelo relleno, seis secciones, 3.500 palabras y once tablas.
Bonus 2: doce decisiones de apertura resueltas, 875 palabras cada una.

DECISIONES DE LA SPEC QUE ESTE GUION MATERIALIZA (no se reabren aquí): D1
(alcance, con la taza y los churros como epígrafe del cap. 01 y columna de
escenario), D2 (bean-to-bar como variante, sin cifras de maquinaria), D5 (EUDR
con operador posterior como INFERENCIA DECLARADA, el art. 2.15 ter como
condición y la fecha de revisión dentro), D10 (artesanía alimentaria como sexto
epígrafe del cap. 09), D17 (un solo nombre visible), D19 (el 644.5 siempre con
su límite, y la pregunta para el asesor en lugar de un epígrafe por canal),
D21 (art. 13.8 con sus cinco letras y la letra e autonómica), D22 (los
calificativos de calidad sin lista de palabras), D23 (ningún sumando sin fuente
y los dos escenarios como rango etiquetado), D24 (art. 6.6 excluye a la
microempresa de todo el art. 6, y el art. 8 no), D30 (la tabla de vidas útiles
es del kit: se cita, no se reescribe), D31 (cinco temperaturas únicas, las del
kit), D32 (los ocho cruces entre libros, por celda verde y fila de cuadre),
D34 (el art. 3 como árbol), D36 (el valle es agosto y para el obrador, no la
caja), D37 (denominaciones en dos capas y las DOS bases de cálculo), D38 (la
frontera con el Kit de Escandallos, que SÍ tiene hoja de tarta de chocolate),
D40 (dos tasas de merma), D41 (denominaciones y contaminantes reescritos),
D42 (trámites, IAE, CAPCA y plástico reescritos), D43 (no existe convenio
estatal del chocolate), D44 (los ids se citan SIEMPRE con su sufijo), D45
(`puntos_por_epigrafe` y los umbrales del gate), D47 (etiquetado o granel),
D48 (proveedores y clientes), D50 (palanca de bloques), D52 (28 referencias en
cinco familias) y D53 (los ocho alérgenos, con nota-puente al kit de 12 €).

Gate de forma, que se corre ANTES de gastar un token de redacción:
    /usr/local/bin/python3 scripts/productos-digitales/guia-chocolateria/verificar_guion.py

Via: Claude Code
"""

PID = 'guia-chocolateria-obrador'

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
    'Europea, Diari Oficial de la Generalitat de Catalunya, el registro de '
    'convenios colectivos del Ministerio de Trabajo y la guía informativa del '
    'registro sanitario— el 12 de septiembre de 2026: cada afirmación legal '
    'lleva su norma y su artículo para que puedas comprobarla y para que sepas '
    'dónde mirar cuando cambie. La norma del cacao que llega de la Unión '
    'Europea se ha modificado tres veces en doce meses, así que el anexo trae '
    'la fecha en la que toca volver a mirarla. Lo que depende de tu '
    'ayuntamiento —la licencia de obra, el planeamiento urbanístico, las '
    'tasas— cambia en cada uno de los municipios de España y aquí se trata '
    'como una pregunta que tienes que hacer, nunca como un dato. Las '
    'superficies, importes, precios, gramajes, márgenes y plazos del caso que '
    'recorre el documento son valores de ejemplo de una bombonería modelada '
    'que acompaña a este pack, y viven en celdas editables de las hojas de '
    'cálculo precisamente para que los sustituyas por los tuyos: ninguno es '
    'una previsión de tus resultados, ni un estándar del sector, ni una '
    'promesa de rentabilidad. Antes de firmar un alquiler, presentar un '
    'trámite, fijar el precio de una referencia, aceptar un pedido de empresa '
    'o contratar a alguien, contrasta con tu ayuntamiento, con tu asesoría y '
    'con la autoridad sanitaria de tu comunidad.*')

GUIA = {
    'pid': PID,
    'titulo': 'Cómo Montar una Chocolatería',
    'subtitulo': 'Obrador, denominaciones legales y números: el dossier '
                 'completo de apertura de una bombonería · Guía España 2026',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Cómo Montar una Chocolatería',
    'fecha': 'septiembre de 2026',
    'version': '1.0',
    'tipo_doc': 'guía',
    'tipo_doc_art': 'de la guía',
    'tipo_doc_dem': 'esta guía',
    'categoria_doc': 'Guía profesional',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        'Veinte capítulos, un anexo normativo fechado, nueve herramientas en '
        'Excel con fórmulas vivas, un business plan modelo relleno y doce '
        'decisiones de apertura resueltas, para quien todavía NO ha abierto: '
        'quien hace bombones en casa y quiere legalizarse, quien viene de otro '
        'oficio del dulce y quiere montar obrador propio, y la pastelería o la '
        'cafetería que añade un obrador de chocolate. No es un recetario, no '
        'es un curso de técnica de templado y no sustituye al proyecto técnico '
        'visado: es el orden en que se toman las decisiones y los números con '
        'los que se toman. Todas las cifras del caso salen de los libros de '
        'este mismo pack, así que el texto y las hojas de cálculo dicen lo '
        'mismo; y cada afirmación legal va con su norma, su artículo y su '
        'enlace, comprobados el 12 de septiembre de 2026.'),
    'gates': {
        'paginas_prometidas': 90,
        'palabras_objetivo': 37000,
        'min_palabras_cap': 1300,
        # Cifras con separador de miles que el texto puede escribir y que NO
        # están en ninguna celda de los nueve libros. Se admiten UNA A UNA y
        # por SIGNIFICADO. Ojo: `valores_admitidos()` ya acepta automáticamente
        # todo número que aparezca en el `cifra`, la `cita_literal`, la `nota`,
        # el `dato` o el `fuente_titulo` de cualquier id del research, así que
        # aquí sólo irían las que no salen de ahí.
        #  · Los números de norma (1055/2003, 1021/2022, 1169/2011, 2023/1115,
        #    1808/1991, 1175/1990, 12/2012, 7/2022, 1/2025) NO se escriben
        #    nunca con punto: lo prohíbe NO_COMUN, así que no hacen falta.
        #  · Hoy no hace falta NINGUNA: toda cifra con separador de miles que
        #    el texto puede escribir sale de una celda de los nueve libros o
        #    del `cifra`, la `nota` o el `dato` de un id del research.
        'cifras_extra': (),
        # La LISTA NEGRA del §5 de la SPEC NO va aquí. `coherencia_cifras()`
        # trata `cifras_ignorar` como una lista de SILENCIADO: lo que se mete
        # ahí deja de saltar el gate. Meter «3.000-4.500 dólares la tonelada» o
        # «80.000-250.000 euros de inversión» en esta clave sería blanquearlas,
        # que es exactamente lo contrario de lo que pide la SPEC. La lista
        # negra entera vive donde de verdad frena al redactor: en `NO_COMUN`,
        # como prohibiciones explícitas que viajan dentro de cada prompt. Se
        # deja vacía a propósito y documentado.
        'cifras_ignorar': (),
        # «la tienda cierra», «el obrador cierra en agosto» y «cierra el mes
        # con» son horarios y contabilidad, no mortalidad de negocios. Esta
        # guía NO escribe ninguna cifra de cierre, quiebra ni fracaso (lo
        # prohíbe NO_COMUN), así que cualquier coincidencia del patrón con un
        # número al lado es un defecto, no una excepción.
        'mortalidad_permitida': ['cierra', 'cierran'],
        # Se rellena al FINAL del fichero con `_ERRATAS_OK` (ver el pie): hay
        # que asignarla a GUIA **y a cada bonus por separado**, o el bonus se
        # queda sin ella.
        'erratas_permitidas': (),
        'erratas_forzadas': {},
    },
}

# --------------------------------------------------------------------------
# Los nueve libros del pack (SPEC §2.2). Se referencian por NOMBRE de fichero:
# documentos.py los busca en astro-site/public/dl/<pid>/. Los nombres quedaron
# firmados en la D49 y NO se renombran: cambiar uno rompe todas las
# referencias `fichero.xlsx!Hoja!Celda` de este guion.
# --------------------------------------------------------------------------
X_CAP = 'capacidad-obrador-y-clima.xlsx'                      # libro 1
X_CAPEX = 'calculadora-capex-chocolateria.xlsx'               # libro 2
X_CACAO = 'sensibilidad-al-precio-del-cacao.xlsx'             # libro 3
X_CARTA = 'carta-de-apertura-y-escandallo-chocolate.xlsx'     # libro 4
X_VIDA = 'vida-util-rellenos-y-rotacion.xlsx'                 # libro 5
X_CAMP = 'campanas-y-valle-del-ano.xlsx'                      # libro 6
X_PLAN = 'plan-financiero-3-anos-chocolateria.xlsx'           # libro 7
X_LEGAL = 'checklist-legal-licencias-y-cacao.xlsx'            # libro 8
X_EQUIP = 'checklist-equipamiento-y-proveedores-cacao.xlsx'   # libro 9

# --------------------------------------------------------------------------
# Pie obligatorio de toda tabla que fije un dato legal. Las URL y las fechas
# son las de la verificación legal independiente del 12-09-2026.
# --------------------------------------------------------------------------
V_CHOCO = ('Verificado el 12-09-2026 · RD 1055/2003 (BOE-A-2003-15599), '
           'artículo único y apartados 1, 2, 3, 4 y 6 de su Reglamentación '
           'técnico-sanitaria · '
           'https://www.boe.es/buscar/act.php?id=BOE-A-2003-15599')
V_DIRECTIVA = ('Verificado el 12-09-2026 · Directiva 2000/36/CE, art. 4 y '
               'Anexo I, parte A, puntos 1 a 13, en el consolidado de EUR-Lex '
               '· https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:'
               '02000L0036-20131118')
V_CONTAM = ('Verificado el 12-09-2026 · Reglamento (UE) 2023/915, Anexo I, '
            'apartados 1.2.16, 3.2.15 y 5.1, y arts. 2, 3 y 4 · '
            'https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:'
            '02023R0915-20250101')
V_EUDR = ('Verificado el 12-09-2026 · Reglamento (UE) 2023/1115, arts. 1, 2, '
          '4, 5, 37 y 38, en el consolidado de EUR-Lex. La norma se ha '
          'modificado tres veces en doce meses: comprueba su estado antes de '
          'comprar cacao · https://eur-lex.europa.eu/legal-content/ES/TXT/'
          '?uri=CELEX:02023R1115-20250101')
V_MINORISTA = ('Verificado el 12-09-2026 · RD 1021/2022 (BOE-A-2022-21681), '
               'arts. 3, 4, 5, 9, 11, 13 y 20, y RD 191/2011 art. 2.2 en la '
               'redacción de la disposición final primera del RD 1021/2022 · '
               'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_ETIQUETA = ('Verificado el 12-09-2026 · Reglamento (UE) 1169/2011 arts. 9.1 '
              'y 14, RD 126/2015 arts. 4, 5 y 6, y RD 1808/1991 '
              '(BOE-A-1991-30678), arts. 2 y 5, sin modificaciones · '
              'https://www.boe.es/buscar/act.php?id=BOE-A-1991-30678')
V_LICENCIA = ('Verificado el 12-09-2026 · Ley 12/2012 (BOE-A-2012-15595), '
              'arts. 2, 3 y 4 y su Anexo, que incluye el epígrafe 644.5 · '
              'https://www.boe.es/buscar/act.php?id=BOE-A-2012-15595')
V_IAE = ('Verificado el 12-09-2026 · RDLeg 1175/1990 (BOE-A-1990-23930), '
         'epígrafe 644.5 con su nota, grupo 676, epígrafe 421.1 y Regla 4.ª de '
         'la Instrucción · '
         'https://www.boe.es/buscar/act.php?id=BOE-A-1990-23930')
V_CONVENIO = ('Verificado el 12-09-2026 en el registro de convenios del '
              'Ministerio de Trabajo y en el BOCM · Convenio de Confiterías, '
              'Pastelerías y Repostería de la Comunidad de Madrid, código '
              '28001025011981, vigencia de 2024 a 2026, con revisión salarial '
              'publicada el 28-02-2026 · '
              'https://expinterweb.mites.gob.es/regcon/pub/consultaPublica')
V_PLASTICO = ('Verificado el 12-09-2026 · Ley 7/2022 (BOE-A-2022-5809), '
              'arts. 68, 72, 73, 75, 77, 78 y 82 · '
              'https://www.boe.es/buscar/act.php?id=BOE-A-2022-5809')


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos, en el anexo y en los
# dos bonus. En este orden: (1) higiene de citación legal, (2) régimen de
# cifras, (3) la LISTA NEGRA íntegra del §5 de la SPEC —las veintinueve
# prohibiciones de la verificación legal del 12-sep, las cuatro que añaden sus
# decisiones, las cifras N-1 a N-20 y los errores de método—, (4) el ámbito del
# producto y la frontera con el Kit de Tareas Chocolatería, y (5) el
# vocabulario del §6 y el tono.
# --------------------------------------------------------------------------
NO_COMUN = [
    # ---- 1. Higiene de citación legal ------------------------------------
    'Las letras y apartados de un artículo de ley se escriben «letra e» o '
    '«apartado 4», NUNCA «e)» ni «4)»: un paréntesis de cierre suelto se lee '
    'como una errata.',
    'Los números de las normas se copian TAL CUAL, sin separador de miles: se '
    'escribe «RD 1055/2003», «RD 1021/2022», «RD 348/2011», «RD 191/2011», '
    '«RD 126/2015», «RD 1808/1991», «RD 1055/2022», «RD 100/2011», '
    '«RD 919/2006», «RD 10/2025», «RDLeg 1175/1990», «Ley 37/1992», '
    '«Ley 12/2012», «Ley 7/2022», «Ley 1/2025», «Ley 1/2004», «Ley 7/1996», '
    '«Reglamento (CE) 852/2004», «Reglamento (UE) 1169/2011», '
    '«Reglamento (UE) 2023/915» y «Reglamento (UE) 2023/1115»; nunca '
    '«RD 1.055/2003».',
    'La norma española del chocolate tiene UN ARTÍCULO ÚNICO: sus divisiones '
    'son APARTADOS de la Reglamentación técnico-sanitaria que aprueba. Se '
    'escribe «el apartado 1.13 del RD 1055/2003», y está PROHIBIDO escribir '
    '«el artículo 6 del RD 1055/2003», que no existe.',
    'TODA afirmación legal va con su norma y su artículo la primera vez que '
    'aparece en el capítulo («el art. 3 del RD 1021/2022», «el apartado 1.13 '
    'del RD 1055/2003»), nunca «es obligatorio» a secas. Y se dice '
    'expresamente «comprobado el 12 de septiembre de 2026», que es la fecha de '
    'corte de esta edición.',
    'Sólo se entrecomilla lo que está literalmente en el boletín oficial o en '
    'el diario oficial europeo. Lo que es interpretación nuestra se presenta '
    'como interpretación, con esas palabras, y lo que viene de una guía '
    'administrativa o de una página ministerial se cita como guía o como '
    'página, NUNCA entrecomillado como si fuera articulado.',
    'NO cites nunca una celda de una hoja de cálculo con la sintaxis de Excel '
    '(«Parámetros!B16», «Cuello de Botella!B7»). Si hay que nombrar de dónde '
    'sale un dato, se nombra el libro y la hoja en lenguaje normal: «la hoja de '
    'cuello de botella de la calculadora de capacidad y clima».',
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
    'Un dato del sector marcado como HUECO, sin cifra o de fiabilidad baja, NO '
    'se rellena: se dice que no hay dato público y se explica qué habría que '
    'preguntar para tenerlo. Eso es contenido, no una carencia.',
    'NO cites ninguna encuesta, informe, escuela, consultora ni proveedor de '
    'software que no venga en los datos del sector de este capítulo.',
    # ---- 3. LISTA NEGRA: lo que la verificación legal prohíbe -------------
    'PROHIBIDO escribir «el reglamento europeo de deforestación te llega en '
    'junio de 2027 si eres pequeño y ya estabas abierto». El aplazamiento es '
    'para los OPERADORES, y una chocolatería que compra cobertura ya '
    'comercializada en la Unión Europea y amparada por una declaración de '
    'diligencia debida es OPERADOR POSTERIOR, no operador. Redacción '
    'obligatoria, y va como INFERENCIA DECLARADA, no como cita: «si tu '
    'cobertura llega ya comercializada en la Unión Europea y amparada por una '
    'declaración de diligencia debida, eres operador posterior y el '
    'aplazamiento no te alcanza: tu fecha es el 30 de diciembre de 2026. Si tu '
    'cobertura NO está amparada, la calificación deja de ser automática y hay '
    'que revisarla». PROHIBIDO también «siempre eres operador posterior» y «tu '
    'fecha es el 30 de diciembre de 2026 pase lo que pase».',
    'PROHIBIDO escribir «pide a todos tus proveedores el número de su '
    'declaración de diligencia debida»: sólo se le pide a quien sea OPERADOR. '
    'Un distribuidor que sea comerciante no tiene número que darte y no está '
    'obligado a dártelo. Y PROHIBIDO escribir «basta con registrar a tus '
    'proveedores»: hay que registrar TAMBIÉN a quién suministras, y conservarlo '
    'cinco años.',
    'PROHIBIDO escribir que lo que es chocolate para la denominación lo es '
    'para los contaminantes: la nota del reglamento de contaminantes remite '
    'sólo a tres puntos de la directiva del chocolate, y el bombón, el '
    'chocolate relleno, el blanco y el chocolate a la taza quedan FUERA.',
    'PROHIBIDO escribir «tu bombón tiene un límite de cadmio de tanto»: el '
    'bombón NO tiene límite propio. Se le aplica la regla de los alimentos '
    'compuestos, y lo que sí tiene que cumplir el límite es la cobertura que '
    'compras.',
    'PROHIBIDO escribir que «fino», «superior» y «extra» son las palabras que '
    'autoriza la norma española del chocolate. La norma NO da una lista de '
    'palabras: autoriza menciones o calificativos referentes a criterios de '
    'calidad, sólo sobre tres denominaciones y sólo por encima de unos '
    'umbrales reforzados. Y la denominación literal es «cobertura de '
    'chocolate», no «cobertura» a secas.',
    'PROHIBIDO escribir que «praliné» no significa nada legalmente: no tiene '
    'definición en la norma española, pero SÍ es denominación de venta europea '
    '—el mismo punto que el bombón de chocolate— y le obliga el mismo mínimo '
    'del veinticinco por ciento. «Trufa», en cambio, no tiene definición legal '
    'en ninguna de las dos.',
    'PROHIBIDO presentar la mención «para su consumo cocido» del chocolate a '
    'la taza como un requisito europeo: es una adición ESPAÑOLA, y la '
    'directiva lleva cláusula de armonización total. Se cumple en España '
    'porque es derecho vigente, y así se dice.',
    'PROHIBIDO escribir que el lote es una de las menciones obligatorias del '
    'Reglamento (UE) 1169/2011: no está entre las doce letras de su art. 9.1. '
    'El lote viene del RD 1808/1991. Y PROHIBIDO escribir que todos tus '
    'bombones necesitan lote: hay tres exenciones que le ahorran trabajo al '
    'lector.',
    'PROHIBIDO escribir «los cinco alérgenos de una bombonería son leche, '
    'frutos secos, soja, gluten y huevo». Son OCHO, porque cacahuetes, frutos '
    'de cáscara y granos de sésamo son entradas INDEPENDIENTES del anexo de '
    'alérgenos, más los sulfitos. Y la lecitina de soja cuenta.',
    'PROHIBIDO escribir «si eres microempresa te siguen obligando los '
    'apartados 2 y 5 del artículo 6 de la Ley 1/2025», y PROHIBIDO escribir '
    '«no te obliga nada de la ley de desperdicio». El apartado 6 deja a la '
    'microempresa fuera de TODO el artículo 6; lo que sigue en pie es que '
    'cualquier cláusula contractual que prohíba donar es nula de pleno '
    'derecho, y que el artículo 8 NO queda excluido: si sirves taza y tienes '
    'mesas, te obliga.',
    'PROHIBIDO escribir que el tostado de cacao está en el catálogo de '
    'actividades potencialmente contaminadoras de la atmósfera: el epígrafe '
    'dice «café o similares» y encajar ahí el cacao es INTERPRETACIÓN. Y '
    'PROHIBIDO escribir que la subida de grupo sólo pasa cerca de espacios '
    'protegidos: el primero de la lista son los núcleos de población, así que '
    'en ciudad esa condición se cumple siempre.',
    'PROHIBIDO escribir «con el epígrafe 644.5 puedes vender a hostelería, a '
    'empresas y por envío sin más». La nota de ese epígrafe condiciona la '
    'fabricación a que la comercialización se haga en las propias dependencias '
    'de venta. Y PROHIBIDO dar un epígrafe de actividades económicas por canal '
    'como veredicto: ninguna fuente lo da, y lo que se publica es LA PREGUNTA '
    'redactada para el asesor.',
    'PROHIBIDO escribir que un taller de bombonería está exento del impuesto '
    'sobre el valor añadido por ser formación: no lo está. Y PROHIBIDO '
    'publicar un tipo impositivo para el taller: eso es lo que queda abierto y '
    'se consulta con la asesoría antes de poner precio.',
    'PROHIBIDO escribir que una chocolatería tiene libertad horaria por el '
    'artículo 5.1 de la Ley 1/2004: no está en esa lista. Le viene por el '
    '5.2, por tener menos de trescientos metros cuadrados de superficie útil '
    'de exposición y venta. El resultado práctico es el mismo y el fundamento '
    'no, y eso importa el día que alguien te lo discuta.',
    'PROHIBIDO escribir que existe un convenio colectivo estatal del '
    'chocolate: está PROBADO que no existe. Y PROHIBIDA cualquier tabla '
    'salarial que no sea la de la Comunidad de Madrid, que se publica marcada '
    'como EJEMPLO y sustituible.',
    'PROHIBIDO escribir que la ley obliga a tener el obrador a una temperatura '
    'o a una humedad determinadas: no hay temperatura legal del chocolate. Las '
    'cinco ventanas que usa este pack son criterio TÉCNICO, salen del Kit de '
    'Tareas Chocolatería y se citan como tales.',
    'PROHIBIDO escribir «hacer bombones en casa para vender es ilegal en '
    'España». La fórmula correcta es: no entra en la lista estatal salvo que '
    'tu comunidad autónoma lo haya añadido por la vía de la letra e del art. '
    '13.8. Y PROHIBIDO usar el decreto catalán de artesanía alimentaria como '
    'prueba de qué es repostería: es otro registro, otra competencia y otro '
    'fin.',
    'PROHIBIDO escribir qué trámite de apertura pide Madrid, Barcelona o '
    'cualquier otro ayuntamiento: no se ha abierto ninguna ordenanza. Lo '
    'afirmable a nivel estatal es que ninguna administración puede exigir '
    'licencia previa de actividad a una bombonería de menos de setecientos '
    'cincuenta metros cuadrados, y que sigue haciendo falta licencia para las '
    'obras de edificación que la requieran.',
    'PROHIBIDO escribir «el impuesto al plástico no te afecta si compras los '
    'envases» y PROHIBIDO escribir «te afecta siempre». Lo paga quien fabrica, '
    'importa o adquiere en otro país de la Unión Europea, y la exención de '
    'cinco kilos al mes tiene dos límites: cubre la importación y la '
    'adquisición intracomunitaria pero NO la fabricación, y cubre unos envases '
    'concretos pero no los semielaborados ni los cierres.',
    'PROHIBIDO escribir que los moldes de policarbonato pagan el impuesto al '
    'plástico: no están sujetos, por dos razones distintas.',
    'PROHIBIDO remitir al RD 1334/1999 para el etiquetado, aunque lo hagan la '
    'norma del chocolate y la de los confites: está superado por el reglamento '
    'europeo de información al consumidor y por el RD 126/2015.',
    'PROHIBIDO escribir que la mención «cacao: tanto por ciento mínimo» es '
    'obligatoria en todos los chocolates: no la exige para el chocolate '
    'blanco, ni para el relleno, ni para el bombón. Ponerla no es ilegal; '
    'decir que es obligatoria sí sería falso.',
    'PROHIBIDO escribir que el veinticinco por ciento del bombón se calcula '
    'descontando el relleno: es justo al revés, se calcula sobre el peso TOTAL '
    'del producto acabado, con el relleno dentro. Invertir la base da un '
    'resultado más favorable que el legal.',
    'PROHIBIDO presentar el art. 4.2 del RD 1021/2022 como la regla de toda la '
    'vitrina: se aplica a la referencia que sale ENVASADA con su etiqueta. '
    'Para el bombón despachado a granel la referencia es tu propio sistema de '
    'autocontrol.',
    'PROHIBIDA cualquier cifra de ruido, de seguro de responsabilidad civil, '
    'de coste de proyecto técnico, de inversión de apertura o de exposición '
    'laboral presentada como dato verificado.',
    # ---- 3 bis. Cifras que no entran (N-1 a N-20 de la SPEC) -------------
    'PROHIBIDO dar una cotización del cacao como precio de compra, y '
    'PROHIBIDO el rango de tres mil a cuatro mil quinientos dólares la '
    'tonelada que circula por la prensa. Del cacao se explica CÓMO se modela '
    'la volatilidad, no cuánto vale hoy, y el precio que usa el pack es el de '
    'la cobertura que compras, que no es lo mismo que la bolsa.',
    'PROHIBIDA la horquilla de inversión de ochenta mil a doscientos cincuenta '
    'mil euros para una chocolatería artesanal premium, y PROHIBIDO todo su '
    'desglose, incluida la vitrina refrigerada de seis mil a dieciocho mil '
    'euros. Es una plantilla repetida, no una cifra investigada.',
    'PROHIBIDO dar un número de chocolaterías de España, y PROHIBIDAS las '
    'facturaciones agregadas de los directorios de empresas: lo que hay son '
    'empresas de grupos de actividad que mezclan fabricación industrial y '
    'comercio, y así se dice o no se dice.',
    'PROHIBIDO usar «ochenta y nueve unidades al día» como cifra de portada: '
    'es el punto de equilibrio de un escenario publicado por un tercero y sólo '
    'vale como MÉTODO.',
    'PROHIBIDA cualquier cifra de franquicia presentada como dato auditado. '
    'Las dos fichas admitidas entran con su marca, su portal y su fecha, y con '
    'la etiqueta «orden de magnitud publicado». De la franquicia de churrería '
    'y chocolatería sólo se puede nombrar la marca, sin cifras.',
    'PROHIBIDO presentar los precios de un distribuidor como precios con el '
    'impuesto sobre el valor añadido incluido cuando la ficha no lo declara, y '
    'PROHIBIDO presentar cualquier total de dotación como cifra fiscal.',
    'PROHIBIDA la serie completa de chocolateras de una marca cuando no es '
    'monótona, PROHIBIDOS los precios de coberturas sin formato de compra, '
    'PROHIBIDO el climatizador evaporativo con precio —además añade humedad, '
    'que es justo lo contrario de lo que necesita un obrador de chocolate— y '
    'PROHIBIDOS los precios de una tienda de otro país presentados como '
    'precios de aquí.',
    'PROHIBIDO cualquier ticket medio de chocolatería y cualquier reparto '
    'mensual de ventas presentado como dato: no existe dato público. Van en '
    'celda verde y la guía enseña a medirlos con el punto de venta en dos '
    'semanas.',
    'PROHIBIDAS las cifras de foros antiguos y de otros países, y PROHIBIDO '
    'usar cifras de inversión de una PASTELERÍA como inversión de una '
    'chocolatería: llevan hornos, y eso cambia el local, la licencia y la '
    'partida de obra.',
    'PROHIBIDO escribir que los bombones son el dieciocho coma dos por ciento '
    'de la categoría: ese dato es de 2022 y el vigente es otro. Si se cita el '
    'reparto por categorías, se cita el del año que traen los datos del sector.',
    'PROHIBIDO recomendar el chocolate de Dubái como decisión de surtido de '
    'apertura, PROHIBIDO publicar un número cerrado de miembros de la '
    'asociación de bean-to-bar —se escribe «más de cuarenta»— y PROHIBIDO '
    'atribuir a un negocio vivo una localidad, un propietario o una cifra que '
    'no venga en los datos del sector: publicarlo mal es un dato falso sobre '
    'un tercero.',
    'PROHIBIDO presentar los salarios de mercado por hora como si fueran una '
    'tabla de convenio: son orientativos, llevan su fiabilidad a la vista y se '
    'publican AL LADO de la tabla del convenio, nunca dentro.',
    'PROHIBIDO escribir «doce moldes por treinta euros», PROHIBIDO dar el '
    'mantenedor como precio cerrado —es un «desde»— y PROHIBIDO restar o '
    'comparar aritméticamente los dos escenarios de dotación: sus bases de '
    'impuesto son mixtas y sólo pueden publicarse como rango y con su '
    'etiqueta.',
    'PROHIBIDO el titular «factor cinco» entre la ganache fresca y la '
    'estabilizada: con los plazos del Kit de Tareas Chocolatería es un factor '
    'de TRES A CINCO, y ésa es la frase publicable.',
    'PROHIBIDO escribir «valle de junio a agosto», «un valle de tres meses» y '
    '«los fijos siguen corriendo con la caja parada». El valle es AGOSTO, un '
    'mes de doce; lo que para es el OBRADOR, no la caja; y la tienda sigue '
    'facturando menos, pero no cero.',
    'PROHIBIDO escribir que el Kit de Escandallos no tiene ninguna hoja de '
    'chocolate: tiene una de tarta de chocolate dentro de su libro de '
    'pastelería. Lo que no existe en el catálogo es el escandallo del obrador '
    'de bombonería, por molde y por tanda.',
    # ---- 3 ter. Errores de método ----------------------------------------
    'PROHIBIDO dar un número de inversión en vez del modelo que lo produce.',
    'PROHIBIDO mezclar precios con y sin impuesto en la misma tabla o en el '
    'mismo párrafo. El escandallo se calcula SIEMPRE sobre base imponible en '
    'los dos lados del cociente, y el precio de referencia de la cobertura de '
    'marca está declarado por su fuente CON impuesto incluido: quien lo use '
    'tal cual se sube el coste de materia casi un diez por ciento.',
    'PROHIBIDO confundir la temperatura de la SALA de tienda con la de la '
    'CÁMARA de conservación, con la de la VITRINA y con la de la NEVERA de '
    'rellenos: son cuatro cosas distintas, con cuatro ventanas distintas, y el '
    'pack las publica una a una.',
    'PROHIBIDO presentar el margen bruto y el food cost como dos reglas: son '
    'la misma regla dicha dos veces, y este pack usa UNA sola.',
    'PROHIBIDO copiar una redacción legal de otro producto de la casa sin su '
    'identificador y sin su fecha de verificación.',
    'PROHIBIDO reescribir una tabla que el Kit de Tareas Chocolatería ya '
    'publica. Se cita por fichero y por hoja, y la guía construye lo que el kit '
    'no tiene.',
    # ---- 4. Ámbito del producto y frontera con el kit --------------------
    'Esta guía es para quien AÚN NO HA ABIERTO. No escribas nada dirigido a '
    'quien ya está operando todos los días: ni control diario de producción, '
    'ni ingeniería de carta, ni gestión de la merma de vitrina del día a día.',
    'NO emitas ninguna curva de templado, ninguna ficha de moldeado, ningún '
    'plan de producción semanal, ningún calendario de tareas por temporada, '
    'ninguna ficha de tarea por perfil, ningún registro de autocontrol y '
    'ninguna matriz de alérgenos por referencia: todo eso ya lo entrega el Kit '
    'de Tareas Chocolatería o el Pack APPCC, y aquí se cita por el nombre del '
    'fichero y de la hoja, sin rehacerlo. Lo que construye la guía es la '
    'decisión previa: si el local sirve, cuántos bombones al día aguanta el '
    'equipo que vas a comprar, cuánto cuesta abrir y qué papeles hacen falta.',
    'Las curvas de templado son especialmente peligrosas: una curva mal '
    'publicada arruina producción. Están en el Kit de Tareas Chocolatería y '
    'esta guía NO las repite ni las resume.',
    'NO menciones ninguna otra guía de la línea «Cómo Montar»: ni de '
    'pastelería, ni de panadería, ni de cafetería, ni de bar, ni de '
    'restaurante, ni de food truck, ni de dark kitchen. Cuando haga falta '
    'remitir a otro producto de la casa, sólo pueden nombrarse el Kit de '
    'Tareas Chocolatería, el Kit de Escandallos, el Pack APPCC y la Guía Food '
    'Cost y de Ingeniería de Menú.',
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
    'paréntesis): «obrador (taller o laboratorio)», «escandallo (costeo)», '
    '«vitrina (exhibidor)», «tableta (barra)», «coste (costo)», «cobertura», '
    '«bombón», «bombonería», «chocolatería artesanal».',
    'Tres avisos de vocabulario que un chocolatero detecta en la primera '
    'página: «trufa» y «praliné» NO son sinónimos de bombón, son TIPOS de '
    'bombón; el «chocolate a la taza» español NO es el «chocolate caliente» de '
    'Hispanoamérica, porque lleva almidón y es espeso, y si se da la '
    'equivalencia se avisa de la diferencia; y «bean-to-bar» NO se traduce.',
    'PROHIBIDA la palabra «dulcería» en cualquier parte del texto: en México es '
    'la tienda de golosinas al por mayor, no una chocolatería. Se escribe '
    'siempre «artesanal», nunca «artesana» como sustantivo, y «templado», no '
    '«temperado».',
    'Usa el vocabulario real de quien va a montar el negocio: se «monta» una '
    'chocolatería (no se «abre» sin más), se habla de «la cobertura» (nunca de '
    '«chocolate de cocina»), de «templar», de «el punto de trabajo», de «la '
    'cámara», de «el bombón se raja», de «se me blanquea», de «la caja de '
    'doce» y de «el pedido de empresa».',
    'TONO: de colega que ya ha montado esto y te lo cuenta, no de consultora. '
    'Prohibido el lenguaje corporativo, prohibidas las introducciones del tipo '
    '«en este capítulo veremos» y prohibidas las conclusiones que resumen lo '
    'ya dicho. Cada párrafo aporta un dato, un procedimiento o una decisión.',
    'PROHIBIDO prometer legalidad o rentabilidad. Nunca escribas «cumple la '
    'normativa», «quedarás cien por cien legal» ni «con esto vas a ganar '
    'tanto». La fórmula segura es: aquí tienes el mapa normativo con la norma, '
    'el artículo y el enlace, y el modelo con el que calculas tu número.',
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
# Cada capítulo declara PRIMERO su `PPE_nn` (epígrafe literal → lista de
# puntos) y luego usa `list(PPE_nn)` como `epigrafes`: así la lista de
# epígrafes y las claves del reparto no pueden discrepar nunca. El recuento de
# puntos por epígrafe es EXACTAMENTE el que declara la tabla del §4 de la SPEC.
# --------------------------------------------------------------------------

PPE_01 = {
    'Las doce variantes del negocio, comparadas': [
        'Abrir con el mapa completo: la palabra «chocolatería» tapa doce '
        'negocios distintos, y no todos se montan igual ni cuestan lo mismo. '
        'Presentar la tabla de variantes como lo primero que hay que decidir, '
        'antes que el local y antes que la máquina.',
        'Explicar que el caso que recorre todo el documento es la variante '
        'central —bombonería artesanal con obrador propio y tienda a calle, en '
        'una ciudad media española sin nombre— y que las demás son '
        'desviaciones sobre ella, con su columna en la calculadora de '
        'inversión.',
        'Advertir de que sólo tres variantes tienen cifra en la calculadora, y '
        'de que el tren de bean-to-bar va SIN cifras de maquinaria a propósito: '
        'no hay precio público verificable, así que lo que se entrega es la '
        'lista de la compra y las cinco preguntas que hay que hacerle al '
        'fabricante. Decirlo en positivo: preguntar bien vale más que un '
        'número inventado.',
    ],
    'La chocolatería de taza y churros: por qué es otro negocio': [
        'Dejarlo claro de entrada, porque el lector que busca esto tiene que '
        'saber en la primera página si compró lo que quería: servir chocolate '
        'a la taza con churros es hostelería, y hacer bombones en un obrador '
        'es comercio con fabricación propia. Comparten el nombre y no comparten '
        'casi nada más.',
        'Y la norma los separa sola, que es el argumento que zanja la '
        'discusión: la Ley 12/2012 lista en su Anexo el epígrafe 644.5 del '
        'comercio al por menor de bombones y caramelos, y NO lista ningún '
        'grupo de la agrupación de servicios de hostelería, donde está el '
        'grupo 676 de chocolaterías, heladerías y horchaterías.',
        'Qué cambia en la práctica si añades la taza: freidora, campana y '
        'conducto si hay churros, otra categoría de aire, comidas preparadas, '
        'y una obligación extra de la ley de desperdicio alimentario si pones '
        'mesas. Todo eso tiene su capítulo, y aquí sólo se anuncia.',
        'Dónde vive esa variante dentro del pack: como columna de escenario en '
        'la calculadora de inversión y como columna contigua en la cuenta de '
        'resultados del plan financiero, con su ticket, su margen y su coste '
        'de personal propios. El lector puede verla al lado de la bombonería '
        'pura y decidir con las dos delante.',
    ],
    'Qué incluye este pack y qué es cross-sell': [
        'Listar los nueve libros de Excel por su nombre de fichero y decir en '
        'qué momento de la apertura se usa cada uno: primero capacidad y '
        'clima, luego inversión, luego el precio del cacao, la carta y el '
        'escandallo, la vida útil, las campañas, el plan financiero, el '
        'expediente legal y la compra de equipamiento.',
        'Decir con todas las letras qué NO construye este pack y dónde vive: '
        'las curvas de templado y las fichas de moldeado son del Kit de Tareas '
        'Chocolatería, los registros de autocontrol completos son del Pack '
        'APPCC, el escandallo unitario de una elaboración es del Kit de '
        'Escandallos —que tiene una hoja de tarta de chocolate— y la '
        'ingeniería de carta es de la Guía Food Cost y de Ingeniería de Menú.',
        'Explicar la frontera con una frase que el lector pueda repetir: el '
        'Kit de Tareas te dice qué hacer cada día cuando ya has abierto; esta '
        'guía es todo lo que hay que decidir antes de abrir. Y la frase que la '
        'completa: donde el kit ya publica un dato, la guía usa EL DEL KIT y '
        'lo cita, en vez de inventarse otro.',
    ],
    'Tu problema, su capítulo y su herramienta': [
        'Presentar el mapa de entrada: el lector no lee el documento de '
        'principio a fin, entra por su problema. Explicar cómo se usa la tabla '
        'de problema a capítulo y a herramienta que viene a continuación, y '
        'señalar las tres puertas de entrada más frecuentes: quien ya hace '
        'bombones en casa y quiere legalizarse, quien tiene un local a la '
        'vista y no sabe si sirve, y quien tiene el dinero contado y necesita '
        'saber si le llega.',
        'Insistir en que los nueve libros comparten el mismo juego de datos, '
        'así que se puede saltar al capítulo que interese sin perder el hilo '
        'de las cifras. Y avisar de la regla que hace que eso funcione: donde '
        'un libro necesita el número de otro, lo trae por celda editable y con '
        'una fila de cuadre que avisa si alguien lo cambia sólo en un sitio.',
    ],
    'Lo que NO vas a encontrar aquí, y cómo llamamos a cada cosa': [
        'Decirlo sin adornos: no hay recetas, no hay curvas de templado, no '
        'hay proyecto técnico visado, no hay la ordenanza de tu ayuntamiento y '
        'no hay una promesa de rentabilidad. Y explicar por qué cada una de '
        'esas ausencias es deliberada, empezando por la más importante: una '
        'curva de templado mal publicada arruina producción, así que vive donde '
        'se ejecuta, en el kit de tareas.',
        'Fijar el glosario mínimo con la equivalencia de Hispanoamérica en la '
        'primera mención: obrador y taller o laboratorio, escandallo y costeo, '
        'vitrina y exhibidor, tableta y barra, coste y costo. Y los tres '
        'avisos que un chocolatero detecta enseguida: trufa y praliné son '
        'tipos de bombón y no sinónimos, el chocolate a la taza español no es '
        'el chocolate caliente hispanoamericano, y «dulcería» no se usa aquí '
        'como sinónimo de nada.',
    ],
}

PPE_02 = {
    'El mercado crece en euros y se encoge en kilos': [
        'Abrir con el tamaño del mercado español de cacao y chocolate, con su '
        'fuente y su año, y explicar la lectura que de verdad importa a quien '
        'va a abrir: el valor sube y el volumen no acompaña, así que lo que '
        'crece es el precio medio, no el consumo.',
        'Sacar la consecuencia comercial, que es la tesis del capítulo: si el '
        'mercado premia el valor y no el volumen, un obrador pequeño compite '
        'en producto y en momento de compra, no en kilos.',
        'Aterrizarlo en el caso modelado: las ventas anuales sin impuesto en '
        'velocidad de crucero, el ticket medio y las piezas por ticket. '
        'Recordar que ese ticket lo produce el mix de la carta, no una media '
        'del sector, porque no existe dato público de ticket medio de '
        'chocolatería.',
    ],
    'El reparto por categorías y el peso del bombón': [
        'Dar el reparto por categorías del valor del mercado, con su fuente y '
        'su año, y decir qué parte le toca al bombón. Es el dato que dice si '
        'el escaparate que estás imaginando es el del mercado o el tuyo.',
        'Avisar de la trampa de este dato concreto: circula una cifra antigua '
        'del peso de los bombones que ya no es la vigente. Si se cita el '
        'reparto, se cita el del año que traen los datos del sector, y se dice '
        'el año.',
        'Traducirlo a decisión de surtido: el peso de cada categoría en el '
        'mercado no es el peso que debe tener en tu vitrina, porque tu vitrina '
        'compite por la ocasión de regalo y no por la compra semanal del '
        'supermercado. El capítulo de la carta lo resuelve con margen, no con '
        'cuota.',
    ],
    'El consumidor ya paga más por menos': [
        'Dar el consumo y el gasto por persona del mercado español con su '
        'fuente, y la subida de precio del año, y leerlos juntos: se compra '
        'menos cantidad y se gasta más dinero.',
        'Explicar por qué eso es una buena noticia para un obrador y una mala '
        'para el lineal: quien reduce cantidad y mantiene gasto está subiendo '
        'de gama, y la gama alta se vende explicada, en mostrador, no en un '
        'expositor de caja de supermercado.',
        'Cerrar con la decisión de plaza: antes de firmar nada, contar cuántos '
        'obradores con elaboración propia hay en el radio de caminata, y no '
        'cuántas chocolaterías aparecen en un buscador, porque ahí entran las '
        'de taza y churros, que son otro negocio y otro cliente.',
    ],
    'No existe un número oficial de chocolaterías': [
        'Decir la verdad incómoda con todas las letras: no hay censo de '
        'chocolaterías en España. Lo que hay son empresas de dos grupos de '
        'actividad que mezclan fabricación industrial y comercio minorista de '
        'alimentación, y ninguno de los dos es «las chocolaterías».',
        'Dar las dos cifras de empresas que sí tienen fuente, con el nombre '
        'exacto de lo que miden, y avisar de que sirven para el orden de '
        'magnitud del sector, no para calcular tu competencia ni tu cuota.',
        'Enseñar el método que sí funciona a nivel de calle, que es lo que se '
        'lleva el lector: contar puertas, mirar escaparates, entrar a comprar '
        'y anotar precios por pieza y por caja. Un censo nacional no te dice '
        'si tu barrio aguanta una bombonería; una mañana de trabajo, sí.',
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
        'año: cada referencia nueva es un molde, un relleno, una caducidad y '
        'una línea más en la matriz de alérgenos.',
        'Presentar el semáforo de surtido del libro de la carta: cuántas '
        'referencias salen con veredicto de mantener, cuántas con revisar '
        'precio y cuántas con retirar, y qué hace el lector con cada grupo. '
        'Ese semáforo se alimenta de dos umbrales que él fija: margen mínimo '
        'por pieza y rotación mínima.',
    ],
    'Las cinco familias y su papel': [
        'Explicar el papel de cada familia: los bombones de colección son la '
        'firma y el margen por pieza, las tabletas son la compra de impulso y '
        'la que más sufre cuando sube el cacao, el chocolate a la taza sostiene '
        'el invierno, los turrones y figuras concentran campaña, y las cajas '
        'son la unidad de venta real.',
        'Avisar de lo que la familia de tabletas tiene de trampa: es la que '
        'más cobertura lleva por pieza, así que es la primera que se rompe '
        'cuando sube el precio del cacao. El capítulo del precio del cacao lo '
        'demuestra con la referencia que primero se rompe.',
        'Recordar la regla de vocabulario que aquí se aplica por primera vez: '
        'trufa y praliné son TIPOS de bombón, no sinónimos, y praliné además '
        'es una denominación de venta europea con su propio mínimo. El '
        'capítulo de denominaciones lo desarrolla.',
    ],
    'La caja frente a la unidad': [
        'La decisión que más dinero mueve de todo el capítulo: la caja es la '
        'unidad de venta real de una bombonería, y casi nadie la escandalla '
        'como lo que es. Presentarla como una referencia propia, con su '
        'montaje, su packaging y su precio.',
        'Dar el precio por bombón dentro de la caja de doce y dentro de la de '
        'treinta y cinco, y el descuento implícito que eso supone. La caja '
        'grande no es una caja pequeña multiplicada: es un descuento por '
        'volumen que el cliente no ve como descuento.',
        'Y la lectura que el libro de la carta hace explícita: comparado con '
        'vender esos mismos bombones sueltos, la caja deja MENOS margen en '
        'euros. No es un error del modelo, es una decisión comercial, y hay '
        'razones buenas para tomarla: ticket más alto, regalo, y una venta que '
        'no existiría suelta.',
        'Cerrar con el criterio: se decide el descuento de la caja mirando el '
        'margen en euros por operación, no el porcentaje, y se revisa cuando '
        'cambia el coste de la cobertura. La hoja de unidad contra caja da las '
        'dos cifras al lado.',
    ],
    'El chocolate a la taza como familia de invierno que sube el ticket': [
        'Explicar qué aporta esta familia a una bombonería que NO monta '
        'hostelería: tableta para taza, sobres monodosis y, si hay barra, la '
        'taza servida. Es estacionalidad complementaria a la del bombón y '
        'entra por la puerta de la ocasión, no del regalo.',
        'Avisar del matiz legal que tiene esta familia y que casi nadie '
        'conoce: el chocolate a la taza tiene mínimos propios y una mención '
        'obligatoria en la etiqueta que las demás familias no llevan. Y si se '
        'sirve en sala, cambia el régimen de comidas preparadas. Los capítulos '
        'de denominaciones y de canales lo desarrollan.',
    ],
}

PPE_04 = {
    'Por qué las cifras publicadas varían por un factor diez': [
        'Empezar por el problema y no por la respuesta: las cifras de '
        'inversión que circulan para una chocolatería van desde la de un '
        'obrador de sobremesa hasta la de una tienda con tren profesional, y '
        'se publican sin decir cuál de las dos describen. Por eso no sirven.',
        'Dar los dos escenarios de dotación que sí tienen fuente, como RANGO y '
        'con su etiqueta pegada: son bases de impuesto mixtas y no son un '
        'presupuesto de apertura. Y decir lo único que se puede concluir de '
        'ellos: el arranque mínimo y el profesional de entrada se diferencian '
        'por un factor cuatro, así que una cifra publicada que no diga cuál '
        'describe no vale para nada.',
        'Explicar qué hace en cambio la calculadora de inversión: nueve '
        'bloques, importe por partida en celda editable, columna de impuesto '
        'línea a línea, y dos líneas de resumen que no se pueden confundir. '
        'El lector no busca una cifra, construye la suya.',
    ],
    'La columna del impuesto, o la inversión sale un veintiuno por ciento desviada': [
        'La regla dura del pack, y aquí se enuncia por primera vez: toda línea '
        'de precio lleva columna de si el precio que tienes delante incluye el '
        'impuesto y a qué tipo. Sin esa columna, una dotación mezcla bases y '
        'la desviación es del orden del tipo general.',
        'Por qué esto es peor en chocolate que en otros oficios: los '
        'distribuidores de maquinaria de chocolate publican unos con impuesto '
        'y otros sin, y hay fichas que no lo declaran. El pack marca esas '
        'líneas como base no declarada en vez de suponerla.',
        'La otra mitad de la regla, que se paga en caja: el impuesto soportado '
        'de la inversión se adelanta y vuelve después, no desaparece. Dar el '
        'importe que hay que adelantar en el caso modelado y explicar por qué '
        'eso no es inversión, es tesorería.',
    ],
    'Las partidas que ninguna fuente publica y cómo presupuestarlas': [
        'Nombrar una por una las partidas que van con valor supuesto porque no '
        'existe precio público verificable: obra y adecuación por metro '
        'cuadrado, cámara climatizada, nevera de rellenos, mobiliario, '
        'packaging del primer pedido, punto de venta y rótulo. Van en celda '
        'editable y declaradas como supuesto.',
        'Y la partida que casi nadie presupuesta y en chocolate es '
        'eliminatoria: la climatización con deshumidificación del obrador. '
        'Tiene bloque propio en la calculadora precisamente para que no se '
        'esconda dentro de la obra.',
        'Dar el método para convertir un supuesto en un número tuyo: tres '
        'presupuestos por partida, con la base del impuesto declarada por '
        'escrito y el plazo de entrega dentro. El libro de equipamiento tiene '
        'la columna para anotarlos.',
    ],
    'El colchón de tesorería como partida, no como propina': [
        'Explicar la diferencia que más confusión crea en los planes de '
        'apertura: el fondo de maniobra NO es inversión, es caja. Se necesita '
        'el día uno y no compra nada. Por eso la calculadora publica dos '
        'líneas separadas y una suma, en vez de un total único.',
        'Dar las tres cifras del caso modelado y decir para qué sirve cada '
        'una: la inversión sin el fondo, el fondo, y la inversión total. La '
        'primera es la que viaja al plan financiero; la segunda se calcula '
        'allí con los gastos fijos y los meses de colchón, y vuelve.',
        'Cerrar con el número que decide si el proyecto arranca: el desembolso '
        'total con impuesto incluido, frente a la financiación disponible. Lo '
        'que falte es aportación propia, y es mejor saberlo antes de firmar el '
        'alquiler que después.',
    ],
    'El impuesto al plástico aparece aquí como alerta y se explica entero más adelante': [
        'Decir qué hace la alerta y qué no: la hoja de impuesto y tesorería '
        'lleva un contador de kilos de plástico no reciclado importado o '
        'adquirido en otro país de la Unión Europea, con el umbral de la '
        'exención al lado, y avisa cuando se supera. No calcula tu impuesto: '
        'te dice si tienes que ir a mirarlo.',
        'Y remitir al capítulo de proveedores para la explicación completa, '
        'con las dos cosas que hay que saber de entrada: la exención no cubre '
        'la fabricación, sólo la importación y la adquisición intracomunitaria; '
        'y los moldes de policarbonato no están sujetos.',
    ],
}

PPE_05 = {
    'Las zonas de un obrador de chocolate, que no son las de una pastelería': [
        'Empezar por lo que cambia respecto a un obrador de dulce clásico, que '
        'es lo que hace que este capítulo exista: aquí no hay horno, no hay '
        'cámara de fermentación y no hay campana. Y sí hay una cámara '
        'climatizada de chocolate, que en pastelería no existe.',
        'Listar las seis zonas del caso modelado con sus metros y decir qué '
        'hace cada una: obrador de templado y moldeado, cámara de chocolate, '
        'almacén de cobertura y materias primas, envasado y packaging, tienda '
        'y mostrador, y aseos y vestuario.',
        'Avisar de que ese reparto es un supuesto declarado, no un estándar: '
        'lo que no es supuesto es la lógica de que las zonas no se pisen y de '
        'que la producción tenga más metros que la venta en un negocio que '
        'vive de fabricar.',
    ],
    'Superficies y marcha adelante': [
        'Explicar la marcha adelante en el lenguaje de este oficio: la '
        'cobertura entra por el almacén, pasa al obrador, de ahí a la cámara, '
        'de la cámara al envasado y del envasado a la tienda, y nunca vuelve '
        'hacia atrás. El vestuario no se cruza en medio.',
        'Dar la comprobación que hace la hoja de zonas y que casi nadie hace '
        'sobre un plano: los pasos numerados sin repetir y sin saltos, y el '
        'descuadre de metros contra la superficie declarada. Si el descuadre '
        'no es cero, o sobran metros o falta una zona.',
        'Sacar el criterio de reparto: qué parte del local tiene que ser '
        'producción para que el obrador no ahogue a la tienda ni al revés, con '
        'el porcentaje del caso modelado y el umbral mínimo que el propio '
        'libro se exige.',
    ],
    'La cámara climatizada como zona propia': [
        'Explicar por qué el chocolate necesita una zona de frío que no es una '
        'nevera: la cámara de conservación trabaja en una ventana templada, no '
        'fría, y la nevera de rellenos y ganaches trabaja en otra mucho más '
        'baja. Son dos equipos, dos zonas y dos objetivos distintos.',
        'Dar los metros de la cámara del caso modelado y decir qué manda en su '
        'dimensionado: los ciclos de cristalización y la rotación de producto '
        'acabado, no los litros. El libro de capacidad lo calcula por '
        'rotaciones.',
    ],
    'La potencia que de verdad hace falta': [
        'Dar la potencia eléctrica prevista del caso modelado y explicar de '
        'dónde sale: atemperadora, temperador, mantenedor, cámara, nevera, '
        'vitrina y climatización, que es la que más pesa. Un obrador de '
        'chocolate consume menos que uno con horno, y eso abre locales.',
        'Y el aviso práctico que ahorra un disgusto en la visita: la potencia '
        'contratable del local la dice el boletín eléctrico, no el anuncio. '
        'La ficha de visita del libro de capacidad la pide como dato medido y '
        'la compara con la que necesitas.',
    ],
}

PPE_06 = {
    'Las reglas de chimenea que circulan son las de las viviendas': [
        'Desmontar el error más caro de la fase de búsqueda de local: el '
        'documento básico de salubridad del Código Técnico que todo el mundo '
        'cita para hablar de salidas de humos tiene por ámbito las viviendas y '
        'los garajes, no un local comercial. Para el local, la referencia es el '
        'reglamento de instalaciones térmicas.',
        'Y la consecuencia, que es la mejor noticia de todo el capítulo: un '
        'obrador de chocolate no tiene horno, no tiene campana y no tiene '
        'combustión, así que el problema del conducto a cubierta directamente '
        'no se plantea. Puedes alquilar locales que una pastelería tendría que '
        'descartar.',
        'Avisar de dónde vuelve a aplicar: si montas la variante de taza y '
        'churros con freidora, vuelve todo el paquete de humos, y además la '
        'inspección periódica de la instalación de gas si es de gas. Es otra '
        'búsqueda de local, no la misma.',
    ],
    'Sin horno no hay campana, pero sí reglamento térmico por la climatización': [
        'Explicar lo que sí aplica: la atemperadora, la refinadora y la '
        'conchadora son equipo de proceso y quedan fuera del reglamento '
        'térmico, pero el equipo de climatización y deshumidificación del '
        'obrador está dentro. Es la instalación que hay que legalizar y '
        'mantener.',
        'Traducirlo a la conversación con el instalador: lo que se le pide no '
        'es sólo frío, es control de temperatura y de humedad a la vez, con '
        'puesta en marcha y equilibrado incluidos. El capítulo del clima trae '
        'la ficha de preguntas.',
        'Y el aviso de calendario: la climatización es de las partidas con '
        'plazo de entrega más largo y de las que más condicionan la fecha de '
        'apertura. El cronograma del expediente legal lo cuadra con el plazo '
        'real que teclees en el libro de equipamiento.',
    ],
    'Ningún ayuntamiento puede exigirte licencia previa de actividad hasta setecientos cincuenta metros cuadrados': [
        'Dar el dato con su norma y su umbral, porque es el argumento más '
        'limpio de todo el bloque legal: la Ley 12/2012 prohíbe exigir '
        'licencia previa de instalación, de funcionamiento o de actividad a '
        'las actividades de su Anexo en establecimientos hasta ese umbral de '
        'superficie útil de exposición y venta. Es ley estatal, no ordenanza.',
        'Y el detalle que lo hace aplicable a una bombonería: su Anexo incluye '
        'expresamente el epígrafe 644.5, el del comercio al por menor de '
        'bombones y caramelos. Lo que se presenta es una declaración '
        'responsable o una comunicación previa.',
        'Los dos límites del propio texto, que se dicen a la vez que la buena '
        'noticia: queda fuera lo que tenga impacto en el patrimonio '
        'histórico-artístico o en el dominio público, y SIGUE haciendo falta '
        'licencia para las obras de edificación que la requieran. La licencia '
        'de obra y la de actividad no son la misma cosa.',
        'Marcar la frontera de lo que no se puede afirmar, y decir por qué: '
        'qué trámite concreto pide tu ayuntamiento, qué tasa cobra y qué plazo '
        'tiene no está verificado en esta edición y cambia en cada municipio. '
        'Va como pregunta a tu ayuntamiento, con la lista de qué preguntar.',
    ],
    'Las tres puertas: local nuevo, traspaso o franquicia': [
        'Presentar la comparación de traspaso contra obra nueva como lo que '
        'es: una comparación de coste TOTAL en un horizonte de años, no de '
        'precio de entrada. Entran el precio pedido, la adecuación que aún '
        'hace falta, la renta y los meses que pagas sin facturar.',
        'Dar los ocho traspasos reales que el libro trae sembrados y la '
        'lectura honesta de esa muestra: cinco son de pastelería-bombonería y '
        'tres de churrería-chocolatería, que es otro negocio; y sólo tres '
        'publican la renta, que es justamente el dato que decide.',
        'Dar el veredicto del caso modelado y el criterio para leerlo: el '
        'veredicto compara dinero, y hay razones que no son dinero —la '
        'clientela heredada, el estado de la instalación eléctrica, la '
        'distribución que no admite marcha adelante— que pueden darle la '
        'vuelta.',
    ],
}


CAPITULOS = [
    {
        'n': 1,
        'titulo': 'Qué Negocio Estás Montando: las Doce Variantes y Cuál te Toca',
        'resumen_indice': 'las doce variantes del nicho comparadas, por qué la chocolatería de taza y churros es otro negocio, qué incluye este pack y qué es cross-sell, el mapa de problema a capítulo y a herramienta, y el glosario de España e Hispanoamérica.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector se sitúe en cinco minutos: cuál de las doce '
                    'variantes del negocio está montando de verdad, qué compró '
                    'exactamente, por dónde entrar según su problema y con qué '
                    'libro del pack se resuelve cada cosa. Y que sepa lo que NO '
                    'hay aquí, para que no lo busque.',
        'epigrafes': list(PPE_01),
        'puntos_por_epigrafe': PPE_01,
        'puntos_globales': [
            'Este capítulo fija el vocabulario de todo el documento: es la '
            'PRIMERA mención de «obrador (taller o laboratorio)», «escandallo '
            '(costeo)», «vitrina (exhibidor)», «tableta (barra)» y «coste '
            '(costo)». A partir de aquí se usa siempre la forma española.',
            'La frontera con el Kit de Tareas Chocolatería se dice ARRIBA y en '
            'positivo, no escondida al final: el kit es para cuando ya has '
            'abierto, esta guía es para decidir antes.',
            'Tono de bienvenida sin autobombo: nada de «la guía definitiva» ni '
            'de promesas. Se enseña el índice y se dice qué hay dentro.',
        ],
        'cifras': [
            C('Superficie total del local del caso modelado', f'{X_CAP}!Parámetros!B16', 'num'),
            C('Metros dedicados a producción en el caso modelado', f'{X_CAP}!Zonas y m2!D17', 'num'),
            C('Bombones equivalentes al día que salen del obrador en velocidad de crucero', f'{X_CAP}!Parámetros!B14', 'num'),
            C('Inversión total de la variante de bombonería con obrador y tienda', f'{X_CAPEX}!Variante del Formato!E7', 'eur'),
            C('Precio verificado de la chocolatera de la variante de taza', f'{X_CAPEX}!Variante del Formato!E37', 'eur'),
            C('Veredicto del bean-to-bar en el caso modelado', f'{X_CAPEX}!Variante del Formato!E33', 'txt'),
            C('Ventas anuales sin IVA del caso modelado en velocidad de crucero', f'{X_CAMP}!Parámetros!B7', 'eur'),
            C('Referencias de la carta con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!B37', 'num'),
        ],
        'sector': ['CHS-01', 'CHS-02', 'CHS-03', 'CHS-04', 'CHS-05', 'CHS-06',
                   'CHS-07', 'CHS-08', 'CHS-09', 'CHS-10', 'CHS-11', 'CHS-12',
                   'CHN-72', 'CHN-49c'],
        'tablas': [
            {
                'titulo': 'Las tres variantes que la calculadora cifra, y qué cambia en cada una (calculadora-capex-chocolateria.xlsx, hoja «Variante del Formato»)',
                'src': (X_CAPEX, 'Variante del Formato'),
                'cols': [('Variante', 'B', 'txt'), ('Id del research', 'C', 'txt'),
                         ('¿Es la tuya?', 'D', 'txt'),
                         ('Qué cambia, y qué NO se puede cifrar', 'H', 'txt')],
                'filas': (7, 9),
                'nota': 'El tren de bean-to-bar va SIN cifras de maquinaria a propósito: no '
                        'hay precio público verificable, y lo que se entrega es la lista de la '
                        'compra y las cinco preguntas al fabricante. La chocolatería de taza y '
                        'churros sólo tiene cifrada la chocolatera.',
            },
            {
                'titulo': 'Tu problema, el capítulo que lo trata y la herramienta que lo resuelve',
                'cabecera': ['Si tu problema es…', 'Capítulo', 'Herramienta del pack'],
                'filas': [
                    ['No sé si este local me sirve', '5 y 6', 'capacidad-obrador-y-clima.xlsx'],
                    ['No sé si podré mantener el obrador a punto en agosto', '7', 'capacidad-obrador-y-clima.xlsx'],
                    ['No sé cuántos bombones al día aguanta lo que voy a comprar', '8', 'capacidad-obrador-y-clima.xlsx'],
                    ['No sé cuánto cuesta abrir', '4', 'calculadora-capex-chocolateria.xlsx'],
                    ['No sé si me sale mejor un traspaso', '6', 'calculadora-capex-chocolateria.xlsx'],
                    ['No sé qué poner en la carta', '3', 'carta-de-apertura-y-escandallo-chocolate.xlsx'],
                    ['No sé a cuánto vender ni cuánto me cuesta', '14', 'carta-de-apertura-y-escandallo-chocolate.xlsx'],
                    ['No sé cómo puedo llamar legalmente a lo que vendo', '10', 'carta-de-apertura-y-escandallo-chocolate.xlsx'],
                    ['No sé qué hago si sube el cacao', '15', 'sensibilidad-al-precio-del-cacao.xlsx'],
                    ['No sé cuánto dura cada bombón ni de cuánto hago cada tanda', '16', 'vida-util-rellenos-y-rotacion.xlsx'],
                    ['No sé qué papeles me tocan ni en qué orden', '9 y 12', 'checklist-legal-licencias-y-cacao.xlsx'],
                    ['Quiero empezar en casa y no sé si puedo', '9', 'checklist-legal-licencias-y-cacao.xlsx'],
                    ['No sé qué papeles pedirle a mi proveedor de cacao', '11 y 13', 'checklist-equipamiento-y-proveedores-cacao.xlsx'],
                    ['No sé qué maquinaria comprar ni a quién', '8 y 13', 'checklist-equipamiento-y-proveedores-cacao.xlsx'],
                    ['No sé si aguanto Navidad ni de qué vivo en agosto', '18', 'campanas-y-valle-del-ano.xlsx'],
                    ['No sé cuánta gente necesito ni cuánto cuesta', '17', 'plan-financiero-3-anos-chocolateria.xlsx'],
                    ['No sé qué canal me conviene ni qué obligaciones me trae', '19', 'plan-financiero-3-anos-chocolateria.xlsx'],
                    ['No sé si el negocio se sostiene ni cuándo puedo abrir', '20', 'plan-financiero-3-anos-chocolateria.xlsx'],
                ],
                'nota': 'Los nueve libros comparten el mismo juego de datos, así que puedes '
                        'saltar al capítulo que te interese sin perder el hilo de las cifras.',
            },
        ],
        'prohibido': NO_COMUN + [
            'No prometas cobertura fuera de España: el marco normativo es el '
            'español y así se dice en este mismo capítulo. Lo que sirve en '
            'cualquier país es la estructura económica; el marco sanitario y '
            'fiscal hay que adaptarlo.',
            'No presentes el pack como sustituto de un proyecto técnico '
            'visado, de una asesoría ni de un curso de oficio.',
            'No des una cifra de inversión «de una chocolatería» sin decir de '
            'qué variante y con qué metros: es el error de método que este '
            'capítulo viene a corregir.',
        ],
    },
    {
        'n': 2,
        'titulo': 'El Cliente y la Plaza: Quién Compra Chocolate, Cuándo y a Qué Precio',
        'resumen_indice': 'un mercado que crece en euros y se encoge en kilos, el reparto por categorías y el peso del bombón, el consumidor que paga más por menos, y por qué no existe un número oficial de chocolaterías.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector entienda contra quién compite de verdad '
                    'antes de elegir plaza y carta, que vea la curva anual de '
                    'la demanda con números en vez de con intuición, y que sepa '
                    'qué datos de mercado NO existen, para que no los busque ni '
                    'se los crea cuando se los enseñen.',
        'epigrafes': list(PPE_02),
        'puntos_por_epigrafe': PPE_02,
        'puntos_globales': [
            'Cada cifra de mercado se cita con su fuente y su año dentro del '
            'texto. Las de fiabilidad limitada se presentan como orden de '
            'magnitud, con esa etiqueta.',
            'No hay ninguna cifra de censo de chocolaterías ni de facturación '
            'media: no existe dato fiable y el capítulo se escribe sin él, '
            'explicando por qué.',
            'El capítulo termina en una decisión: qué mirar en la plaza antes '
            'de firmar. No es un informe de mercado, es un criterio de '
            'ubicación.',
        ],
        'cifras': [
            C('Clientes al día del caso modelado en velocidad de crucero', f'{X_PLAN}!0. Supuestos!B6', 'num'),
            C('Piezas por ticket', f'{X_PLAN}!0. Supuestos!B7', 'num1'),
            C('Ticket medio sin IVA del caso modelado', f'{X_PLAN}!0. Supuestos!B10', 'eur2'),
            C('Ventas del mes más alto del año, diciembre', f'{X_CAMP}!Peso sobre el Año!E18', 'eur'),
            C('Ventas del mes más bajo del año, agosto', f'{X_CAMP}!Peso sobre el Año!E14', 'eur'),
            C('Peso de diciembre sobre las ventas del año', f'{X_CAMP}!Peso sobre el Año!F18', 'pct1'),
            C('Peso de agosto sobre las ventas del año', f'{X_CAMP}!Peso sobre el Año!F14', 'pct1'),
            C('Peso de las doce campañas sobre las ventas del año', f'{X_CAMP}!Peso sobre el Año!D35', 'pct1'),
        ],
        'sector': ['CHS-13', 'CHS-14', 'CHS-16', 'CHS-17', 'CHS-18', 'CHS-19',
                   'CHS-20', 'CHS-21', 'CHS-22', 'CHS-23'],
        'tablas': [
            {
                'titulo': 'El año mes a mes en el caso modelado (campanas-y-valle-del-ano.xlsx, hoja «Peso sobre el Año»)',
                'src': (X_CAMP, 'Peso sobre el Año'),
                'cols': [('Mes', 'A', 'txt'),
                         ('Temporada que declara el kit', 'B', 'txt'),
                         ('Coeficiente sobre el mes medio', 'C', 'num2'),
                         ('Ventas del mes sin IVA (€)', 'E', 'eur'),
                         ('Parte del año (%)', 'F', 'pct1'),
                         ('Veces un día medio', 'H', 'num2')],
                'filas': (7, 19),
                'nota': 'Los doce coeficientes son SUPUESTOS del caso modelado y suman doce, '
                        'de manera que la media del año coincide con la velocidad de crucero. '
                        'La temporada de cada mes NO es supuesta: es la que declara el '
                        'calendario del Kit de Tareas Chocolatería. Cámbialos por los tuyos en '
                        'cuanto tengas un año cerrado.',
            },
            {
                'titulo': 'Lo que dice el mercado español del cacao y del chocolate, y de dónde sale cada dato',
                'cabecera': ['Qué mide', 'Qué dice el dato', 'Id del research'],
                'filas': [
                    ['Tamaño del mercado de cacao y chocolate en España', 'Consumo y facturación del año, con su fuente', 'CHS-18'],
                    ['Reparto por categorías del valor', 'Qué parte se lleva cada categoría, con el año del dato', 'CHS-19'],
                    ['Facturación del sector del dulce español', 'El agregado en el que está dentro el chocolate', 'CHS-20'],
                    ['Consumo por persona en los hogares', 'Kilos por persona y año', 'CHS-21'],
                    ['Gasto por persona y evolución del mercado', 'Euros por persona y hacia dónde va', 'CHS-22'],
                    ['Precio medio del chocolate', 'La subida de precio del año', 'CHS-23'],
                    ['Empresas del grupo de fabricación de cacao, chocolate y confitería', 'Un agregado de fabricación, NO un censo de chocolaterías', 'CHS-16'],
                    ['Empresas del comercio minorista de pan, confitería y pastelería', 'Otro agregado, y tampoco es un censo de chocolaterías', 'CHS-17'],
                ],
                'nota': 'Ninguna de estas cifras es el número de chocolaterías de España, '
                        'porque ese dato no existe. Los dos últimos son grupos de actividad '
                        'que mezclan fabricación industrial y comercio, y sirven para el orden '
                        'de magnitud del sector, no para calcular tu competencia.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO dar un censo de chocolaterías de España o una '
            'facturación media por chocolatería: no existe dato fiable, y el '
            'capítulo se escribe diciendo eso.',
            'PROHIBIDO usar el peso de los bombones de un año antiguo como si '
            'fuera el vigente: si se cita el reparto por categorías, se cita '
            'el del año que traen los datos del sector, y se dice el año.',
            'PROHIBIDO dar un ticket medio de chocolatería como dato del '
            'sector: el del caso modelado sale del mix de su propia carta y se '
            'presenta así.',
        ],
    },
    {
        'n': 3,
        'titulo': 'La Carta de Apertura: las Referencias, las Familias y la Caja',
        'resumen_indice': 'cómo se decide un surtido de apertura, las cinco familias y el papel de cada una, la caja frente a la unidad y lo que de verdad deja cada una, y el chocolate a la taza como familia de invierno.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector decida su surtido de apertura con criterio '
                    'de margen y de capacidad, y no por gusto; y que entienda '
                    'que la caja es una referencia propia que hay que '
                    'escandallar como tal, porque es la unidad de venta real de '
                    'una bombonería.',
        'epigrafes': list(PPE_03),
        'puntos_por_epigrafe': PPE_03,
        'puntos_globales': [
            'Las referencias del caso modelado son datos de EJEMPLO '
            'declarados, no un surtido recomendado. Lo que se lleva el lector '
            'es el método y los dos umbrales con los que se decide.',
            'Aquí no se explica cómo se calcula el escandallo: eso es del '
            'capítulo 14. Este capítulo decide QUÉ hay en la vitrina; aquél '
            'calcula cuánto cuesta.',
            'Nada de recetas ni de técnica: los gramajes que aparecen son lo '
            'que el modelo necesita para calcular, y se dice.',
        ],
        'cifras': [
            C('PVP medio ponderado de la carta con IVA', f'{X_CARTA}!Mix y Ticket Medio!B37', 'eur2'),
            C('Ticket medio con IVA de todo el año', f'{X_CARTA}!Mix y Ticket Medio!B40', 'eur2'),
            C('Precio por bombón dentro de la caja de doce, con IVA', f'{X_CARTA}!Unidad vs Caja!C33', 'eur2'),
            C('Precio por bombón dentro de la caja de treinta y cinco, con IVA', f'{X_CARTA}!Unidad vs Caja!E33', 'eur2'),
            C('Descuento implícito de la caja de treinta y cinco', f'{X_CARTA}!Unidad vs Caja!E35', 'pct1'),
            C('Referencias con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!B37', 'num'),
            C('Referencias con veredicto de revisar precio', f'{X_CARTA}!Decisión de Surtido!B38', 'num'),
            C('Referencias con veredicto de retirar', f'{X_CARTA}!Decisión de Surtido!B39', 'num'),
            C('Margen de toda la carta al año', f'{X_CARTA}!Decisión de Surtido!G35', 'eur'),
        ],
        'sector': ['CHS-29', 'CHS-32', 'CHS-25c', 'CHS-11'],
        'tablas': [
            {
                'titulo': 'La caja frente a la unidad, caja a caja (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Unidad vs Caja»)',
                'src': (X_CARTA, 'Unidad vs Caja'),
                'cols': [('Concepto', 'A', 'txt'),
                         ('Caja de 12', 'C', 'eur2'),
                         ('Caja de 20', 'D', 'eur2'),
                         ('Caja de 35', 'E', 'eur2'),
                         ('Estuche corporativo de 24', 'F', 'eur2')],
                'filas': (28, 40),
                # La fila 35 («Descuento que le haces al cliente») es un
                # PORCENTAJE dentro de una columna de euros, y su etiqueta no
                # declara el porcentaje, así que `es_fila_porcentual()` no la
                # reconoce y se imprimiría «0,17 €» donde hay un 16,8 %. Se
                # omite de la tabla: el descuento va en las cifras del
                # capítulo, donde sí sale formateado como porcentaje.
                'omitir_filas': (35,),
                'nota': 'Las cifras van en euros por caja, salvo las dos de precio por bombón, '
                        'que van en euros por pieza; el descuento implícito de cada formato '
                        'está en el texto, en porcentaje. El veredicto de la última fila no es '
                        'una advertencia: es una decisión comercial que hay que tomar con el '
                        'margen en euros delante.',
            },
            {
                'titulo': 'Las cinco familias de la carta y el papel de cada una',
                'cabecera': ['Familia', 'Referencias del caso modelado', 'Qué aporta', 'Su riesgo'],
                'filas': [
                    ['Bombones de colección', '10', 'La firma de la casa y el margen por pieza', 'Vida útil corta si el relleno es fresco'],
                    ['Tabletas', '6', 'Compra de impulso y regalo pequeño', 'Es la familia que más cobertura lleva: la primera que se rompe si sube el cacao'],
                    ['Chocolate a la taza', '3', 'Sostiene el invierno y sube el ticket', 'Mínimos legales propios y una mención obligatoria en la etiqueta'],
                    ['Turrones, figuras y temporada', '5', 'Concentra campaña y permite precio alto', 'Moldes y packaging que se compran con meses de antelación'],
                    ['Cajas y regalo', '4', 'Es la unidad de venta real y el canal corporativo', 'Deja menos margen que vender esos bombones sueltos'],
                ],
                'nota': 'Veintiocho referencias en cinco familias. El número es un supuesto '
                        'declarado del caso modelado; lo que no es supuesto es la columna legal '
                        'de cada familia, que sale de la norma del chocolate y se explica en el '
                        'capítulo 10.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO recomendar una moda de producto como decisión de '
            'surtido de apertura: una referencia que no sabes si vas a poder '
            'sostener doce meses no entra en una carta de apertura.',
            'PROHIBIDO dar un ticket medio de chocolatería como dato del '
            'sector: no existe dato público.',
            'PROHIBIDO presentar trufa y praliné como sinónimos de bombón: son '
            'tipos, y praliné además es denominación de venta europea.',
        ],
    },
    {
        'n': 4,
        'titulo': 'Cuánto Cuesta Abrir: la Inversión Real, Partida a Partida',
        'resumen_indice': 'por qué las cifras publicadas varían por un factor diez, la columna del impuesto que descuadra la inversión entera, las partidas que ninguna fuente publica, el colchón de tesorería como partida propia y la alerta del impuesto al plástico.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector sustituya la horquilla que ha leído por ahí '
                    'por su propio modelo de inversión, partida a partida, con '
                    'la base del impuesto declarada en cada línea y el fondo de '
                    'maniobra separado de lo que de verdad se compra.',
        'epigrafes': list(PPE_04),
        'puntos_por_epigrafe': PPE_04,
        'puntos_globales': [
            'Ningún total de este capítulo es un presupuesto de apertura ni '
            'una cifra fiscal: son sumas de un modelo con supuestos '
            'declarados, y así se presentan.',
            'Los dos escenarios de dotación publicados entran SIEMPRE como '
            'rango y con su etiqueta de base mixta pegada. No se restan, no se '
            'comparan aritméticamente y no se presentan como presupuesto.',
            'La explicación completa del impuesto al plástico NO va aquí: aquí '
            'sólo se dice que la alerta existe, qué la dispara y dónde se '
            'explica.',
        ],
        'cifras': [
            C('Inversión total del caso modelado, sin IVA', f'{X_CAPEX}!CAPEX por Bloque!L40', 'eur'),
            C('Inversión sin el fondo de maniobra, que es la que viaja al plan financiero', f'{X_CAPEX}!CAPEX por Bloque!L44', 'eur'),
            C('Fondo de maniobra, que es caja y no inversión', f'{X_CAPEX}!CAPEX por Bloque!L45', 'eur'),
            C('Subtotal comparable con un presupuesto de obra y equipamiento', f'{X_CAPEX}!CAPEX por Bloque!L48', 'eur'),
            C('IVA soportado de toda la inversión', f'{X_CAPEX}!CAPEX por Bloque!M40', 'eur'),
            C('Desembolso total con IVA incluido', f'{X_CAPEX}!CAPEX por Bloque!N40', 'eur'),
            C('Aportación propia necesaria además de la financiación', f'{X_CAPEX}!IVA y Tesorería!B27', 'eur'),
            C('Kilos al mes de plástico no reciclado del caso modelado', f'{X_CAPEX}!Parámetros!B19', 'num1'),
            C('Umbral mensual de la exención del impuesto al plástico', f'{X_CAPEX}!Parámetros!B20', 'num'),
            C('Alerta del impuesto al plástico en el caso modelado', f'{X_CAPEX}!IVA y Tesorería!B37', 'txt'),
        ],
        'sector': ['CHS-03', 'CHS-47a', 'CHS-47b', 'CHS-58', 'CHN-62',
                   'CHN-62b', 'CHN-62c'],
        'tablas': [
            {
                'titulo': 'Los nueve bloques de la inversión, con su impuesto soportado (calculadora-capex-chocolateria.xlsx, hoja «IVA y Tesorería»)',
                'src': (X_CAPEX, 'IVA y Tesorería'),
                'cols': [('Bloque', 'A', 'txt'),
                         ('Base sin IVA (€)', 'B', 'eur'),
                         ('IVA soportado (€)', 'C', 'eur'),
                         ('Total con IVA (€)', 'D', 'eur')],
                'filas': (6, 15),
                'nota': 'Fianza y licencias, packaging y moldes, y fondo de maniobra quedan '
                        'FUERA de la comparación con cualquier presupuesto publicado: un '
                        'depósito, unas existencias y una caja no se comparan contra un '
                        'presupuesto de obra y equipamiento.',
            },
            {
                'titulo': 'Las dos líneas de dinero que no se pueden confundir (calculadora-capex-chocolateria.xlsx, hoja «CAPEX por Bloque»)',
                'src': (X_CAPEX, 'CAPEX por Bloque'),
                'cols': [('Concepto', 'C', 'txt'), ('Importe (€)', 'L', 'eur')],
                'filas': (40, 48),
                'nota': 'La inversión sin el fondo de maniobra es la que viaja al plan '
                        'financiero; el fondo se calcula allí, con los gastos fijos y los meses '
                        'de colchón de ese libro, y vuelve aquí ya calculado. Por eso las dos '
                        'inversiones totales del pack salen idénticas por construcción.',
            },
            {
                'titulo': 'Los dos escenarios de dotación publicados, con su etiqueta pegada (calculadora-capex-chocolateria.xlsx, hoja «CAPEX por Bloque»)',
                'src': (X_CAPEX, 'CAPEX por Bloque'),
                'cols': [('Escenario', 'C', 'txt'),
                         ('Mínimo publicado (€)', 'I', 'eur'),
                         ('Máximo publicado (€)', 'J', 'eur'),
                         ('Fuente', 'K', 'txt'),
                         ('Etiqueta', 'O', 'txt')],
                'filas': (58, 61),
                'nota': 'Son bases de impuesto MIXTAS y no son un presupuesto de apertura. Lo '
                        'único que se puede concluir de los dos es que el arranque mínimo y el '
                        'profesional de entrada se diferencian por un factor cuatro: restarlos '
                        'o compararlos como cifras fiscales está prohibido.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO comparar aritméticamente los dos escenarios de dotación '
            'o presentar cualquiera de sus totales como cifra fiscal.',
            'PROHIBIDO escribir «los moldes de policarbonato pagan el impuesto '
            'al plástico» y PROHIBIDO escribir «el impuesto al plástico no te '
            'afecta si compras los envases» o su contrario: la explicación '
            'entera va en el capítulo 13, y aquí sólo se dice que el semáforo '
            'existe y dónde se explica.',
            'PROHIBIDO dar una cifra de coste de proyecto técnico, de seguro o '
            'de tasas como dato verificado: van como supuesto declarado y con '
            'la instrucción de pedir presupuesto.',
        ],
    },
    {
        'n': 5,
        'titulo': 'El Local: Metros, Zonas y la Ficha de Visita',
        'resumen_indice': 'las zonas de un obrador de chocolate y en qué se diferencian de las de una pastelería, superficies y marcha adelante, la cámara climatizada como zona propia y la potencia que de verdad hace falta.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector sepa qué mirar en un local antes de '
                    'enamorarse de él: cuántas zonas tiene que meter dentro, '
                    'cómo se comprueba que no se pisan, y qué datos hay que '
                    'medir en la visita en lugar de creerse el anuncio.',
        'epigrafes': list(PPE_05),
        'puntos_por_epigrafe': PPE_05,
        'puntos_globales': [
            'Los metros por zona son SUPUESTO declarado del caso modelado, no '
            'un estándar del sector: lo que se lleva el lector es el criterio '
            'de reparto y la comprobación de marcha adelante.',
            'Todo lo que en este capítulo se cuenta en piezas se cuenta en '
            'BOMBONES EQUIVALENTES, que es la unidad de capacidad del pack: '
            'una caja de treinta y cinco bombones es una venta y treinta y seis '
            'bombones de obrador. Se dice la primera vez que aparece.',
            'Aquí NO se decide la maquinaria: se decide si el local admite la '
            'maquinaria que quieres. La compra es del capítulo 8.',
        ],
        'cifras': [
            C('Superficie total del local del caso modelado', f'{X_CAP}!Parámetros!B16', 'num'),
            C('Metros del obrador de templado y moldeado', f'{X_CAP}!Zonas y m2!D6', 'num'),
            C('Metros de la cámara de chocolate', f'{X_CAP}!Zonas y m2!D7', 'num'),
            C('Metros de tienda y mostrador', f'{X_CAP}!Zonas y m2!D19', 'num'),
            C('Parte del local dedicada a producción', f'{X_CAP}!Zonas y m2!D18', 'pct0'),
            C('Veredicto del reparto de metros', f'{X_CAP}!Zonas y m2!D22', 'txt'),
            C('Veredicto de la marcha adelante', f'{X_CAP}!Zonas y m2!D34', 'txt'),
            C('Potencia eléctrica instalada prevista', f'{X_CAP}!Parámetros!B18', 'num'),
            C('Ítems eliminatorios de la ficha de visita', f'{X_CAP}!Ficha de Visita a Local!E26', 'num'),
        ],
        'sector': ['CHS-03', 'CHS-58', 'CHS-37a', 'CHS-38a'],
        'tablas': [
            {
                'titulo': 'Las seis zonas del caso modelado, con sus metros y su paso en el recorrido (capacidad-obrador-y-clima.xlsx, hoja «Zonas y m2»)',
                'src': (X_CAP, 'Zonas y m2'),
                'cols': [('Zona', 'B', 'txt'), ('Bloque', 'C', 'txt'),
                         ('m2', 'D', 'num1'), ('% del local', 'E', 'pct1'),
                         ('Paso del recorrido', 'F', 'num'),
                         ('Qué tiene que cumplir', 'G', 'txt')],
                'filas': (6, 11),
                'nota': 'Los metros son supuesto declarado. Lo que no es supuesto es que las '
                        'zonas no se pisen y que el recorrido vaya en un solo sentido: eso se '
                        'comprueba con los pasos numerados, y la hoja avisa si se repiten o '
                        'hay saltos.',
            },
            {
                'titulo': 'Lo que una pastelería tiene y un obrador de chocolate no, y al revés',
                'cabecera': ['Zona o instalación', '¿La tiene una pastelería?', '¿La tiene un obrador de chocolate?', 'Qué cambia en la búsqueda de local'],
                'filas': [
                    ['Horno y campana de extracción', 'Sí', 'No', 'Se abre el abanico de locales: sin combustión no hay conducto a cubierta'],
                    ['Cámara de fermentación', 'Sí', 'No', 'Menos metros de frío y menos potencia'],
                    ['Cámara climatizada de chocolate', 'No', 'Sí', 'Zona propia, templada y con humedad controlada: es la que nadie presupuesta'],
                    ['Nevera de rellenos y ganaches', 'Sí', 'Sí', 'Es otra ventana de temperatura, mucho más baja que la cámara'],
                    ['Sala de tienda con su propia temperatura', 'Sí', 'Sí', 'En chocolate manda más: por encima de cierto punto la vitrina pierde brillo'],
                    ['Zona de envasado y montaje de cajas', 'Menor', 'Sí, y es cuello de botella', 'Es la zona que nadie dibuja en el plano y la que limita el día de Navidad'],
                ],
                'nota': 'Copiar el reparto de zonas de una pastelería es el error de método más '
                        'repetido al montar un obrador de chocolate: son dos oficios con dos '
                        'plantas distintas.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO copiar el reparto de zonas de una pastelería o '
            'presentar los metros por zona como dato medido del sector: son '
            'supuesto declarado.',
            'PROHIBIDO confundir la cámara de conservación de chocolate con la '
            'nevera de rellenos: son dos equipos con dos ventanas distintas.',
            'PROHIBIDO dar una cifra de potencia, de caudal o de superficie '
            'que no esté en las cifras del producto.',
        ],
    },
    {
        'n': 6,
        'titulo': 'Antes de Firmar: el Obrador sin Humos Cambia la Conversación de la Licencia',
        'resumen_indice': 'las reglas de chimenea que circulan y por qué no son las tuyas, qué sí aplica por la climatización, el umbral estatal por debajo del cual no se puede exigir licencia previa de actividad, y las tres puertas de entrada al local.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector no firme un local imposible ni descarte uno '
                    'que sí le vale: qué le aplica de verdad sin horno, qué le '
                    'puede exigir un ayuntamiento y qué no, y cómo se compara '
                    'un traspaso con una obra nueva en dinero total.',
        'epigrafes': list(PPE_06),
        'puntos_por_epigrafe': PPE_06,
        'puntos_globales': [
            'Aquí se afirma SÓLO lo que es estatal y está verificado. Todo lo '
            'municipal —la ordenanza, la tasa, el trámite concreto— va como '
            'pregunta a tu ayuntamiento, con la lista de qué preguntar.',
            'La ventaja de no tener humos se dice en positivo y con su límite '
            'al lado: abre locales, y no exime de la licencia de obra.',
            'Las cifras de traspaso son de anuncios reales publicados, con su '
            'identificador y su fecha: son orden de magnitud de un mercado, no '
            'una tasación.',
        ],
        'cifras': [
            C('Umbral estatal de superficie por debajo del cual no cabe exigir licencia previa de actividad', f'{X_CAP}!Parámetros!B24', 'num'),
            C('Superficie de exposición y venta medida en el local del caso', f'{X_CAP}!Ficha de Visita a Local!F10', 'num'),
            C('Ítems de la ficha de visita a local', f'{X_CAP}!Ficha de Visita a Local!E25', 'num'),
            C('Motivos de descarte del local en el caso modelado', f'{X_CAP}!Ficha de Visita a Local!E27', 'num'),
            C('Ítems pendientes de comprobar', f'{X_CAP}!Ficha de Visita a Local!E29', 'num'),
            C('Veredicto del local del caso modelado', f'{X_CAP}!Ficha de Visita a Local!E32', 'txt'),
            C('Coste total del traspaso en el horizonte de comparación', f'{X_CAPEX}!Traspaso vs Obra Nueva!C19', 'eur'),
            C('Coste total de la obra nueva en el mismo horizonte', f'{X_CAPEX}!Traspaso vs Obra Nueva!C20', 'eur'),
            C('Veredicto de traspaso contra obra nueva', f'{X_CAPEX}!Traspaso vs Obra Nueva!C22', 'txt'),
            C('Traspasos de la muestra que publican la renta', f'{X_CAPEX}!Traspaso vs Obra Nueva!D34', 'num'),
        ],
        'sector': ['CHN-45', 'CHN-46', 'CHN-49', 'CHN-49b', 'CHN-91',
                   'CHS-37a', 'CHS-37b', 'CHS-37c', 'CHS-38a', 'CHS-38b',
                   'CHS-38c', 'CHS-38d', 'CHS-38e', 'CHS-58'],
        'tablas': [
            {
                'titulo': 'La ficha de visita a local, ítem a ítem (capacidad-obrador-y-clima.xlsx, hoja «Ficha de Visita a Local»)',
                'src': (X_CAP, 'Ficha de Visita a Local'),
                'cols': [('Nº', 'A', 'num'), ('Qué se comprueba', 'B', 'txt'),
                         ('¿Eliminatorio?', 'C', 'txt'),
                         ('Respuesta del caso', 'E', 'txt'),
                         ('Veredicto', 'I', 'txt')],
                'filas': (6, 23),
                'nota': 'Imprímela y llévala a cada visita. Los seis ítems eliminatorios no '
                        'son opinión: si uno sale mal, ese local no es. ' + V_LICENCIA,
            },
            {
                'titulo': 'Ocho traspasos reales publicados, para ver la dispersión del mercado (calculadora-capex-chocolateria.xlsx, hoja «Traspaso vs Obra Nueva»)',
                'src': (X_CAPEX, 'Traspaso vs Obra Nueva'),
                'cols': [('Ciudad o zona', 'A', 'txt'), ('Tipo de negocio', 'B', 'txt'),
                         ('m2', 'C', 'num'), ('Precio pedido (€)', 'D', 'eur'),
                         ('Renta mensual (€)', 'E', 'eur'),
                         ('Fuente', 'H', 'txt'), ('¿Mismo formato?', 'I', 'txt')],
                'filas': (26, 33),
                'nota': 'Cinco son de pastelería-bombonería y tres de '
                        'churrería-chocolatería, que es otro negocio y por eso van marcadas. '
                        'Sólo tres publican la renta, que es justamente el dato que decide la '
                        'comparación: lo que no se publica, se pregunta.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir qué trámite de apertura pide Madrid, Barcelona '
            'o cualquier otro ayuntamiento: no se ha abierto ninguna '
            'ordenanza en esta edición.',
            'PROHIBIDO presentar cualquier cifra de franquicia como dato '
            'auditado: entra con su marca, su portal y su fecha, y con la '
            'etiqueta de orden de magnitud publicado.',
            'PROHIBIDO citar el documento básico de salubridad del Código '
            'Técnico como si regulase la ventilación de un local comercial, y '
            'PROHIBIDO reproducir las reglas de distancia de boca de expulsión '
            'de las viviendas.',
        ],
    },
]


PPE_07 = {
    'Sala y cámara son dos cosas distintas': [
        'Poner orden en lo que casi siempre se cuenta mezclado: en un obrador '
        'de chocolate hay CINCO ventanas de temperatura distintas, y cada una '
        'tiene su equipo. Obrador al templar, cámara de conservación, nevera '
        'de rellenos, sala de tienda y vitrina.',
        'Dar las cinco con su rango y su humedad, diciendo de dónde salen: son '
        'las que publica el Kit de Tareas Chocolatería, que es producto '
        'vendido de la casa, y la guía usa ÉSAS en vez de inventarse otras. '
        'Citarlas por fichero y hoja.',
        'Y la comprobación que hace la hoja de clima y que nadie hace a mano: '
        'que las cinco ventanas sean coherentes ENTRE SÍ. La cámara por debajo '
        'del obrador, la sala por encima, la vitrina por debajo de la sala y la '
        'nevera de rellenos por debajo de todas. Si una no cuadra, el problema '
        'no es el equipo: es el objetivo.',
    ],
    'Ninguna norma obliga a una temperatura de obrador: la declaras tú y la justificas': [
        'Decirlo con todas las letras, porque circula lo contrario: la tabla '
        'de temperaturas de conservación del RD 1021/2022 NO tiene fila para '
        'el chocolate, y las palabras «chocolate», «cacao», «bombón» y '
        '«confitería» no aparecen ni una vez en toda esa norma.',
        'Lo que sí hay, y es lo que de verdad obliga: la temperatura de '
        'conservación la fija quien produce y envasa, en su etiqueta; y para '
        'lo que se despacha a granel, la referencia es tu propio sistema de '
        'autocontrol, donde la declaras tú. El capítulo 16 lo desarrolla '
        'referencia a referencia.',
        'La consecuencia práctica, que es ventaja y trampa a la vez: eliges tú '
        'la ventana, y luego tienes que poder mantenerla. Si declaras una '
        'temperatura, tienes que sostenerla también el día que el termómetro '
        'de la calle marca lo que marca en agosto.',
    ],
    'Fat bloom y sugar bloom': [
        'Explicar los dos defectos con el vocabulario del oficio y sin '
        'convertir el capítulo en técnica: el fat bloom viene del calor y de '
        'los ciclos de temperatura, y el sugar bloom viene del agua, de la '
        'condensación al pasar de frío a caliente sin atemperar.',
        'Traducirlo a decisiones de local y de equipo, que es lo que aquí '
        'toca: control de humedad tan importante como el de temperatura, nada '
        'de meter el producto acabado en una nevera doméstica, y una cámara '
        'que no condense al abrir.',
        'Y el enlace con el dinero: un bombón blanqueado no es un bombón '
        'peligroso, es un bombón invendible. Es merma por calidad, y se paga '
        'igual que la de caducidad. El libro de vida útil la cuantifica.',
    ],
    'Lo que hay que preguntarle al instalador': [
        'Explicar por qué esta hoja NO calcula carga térmica y por qué eso es '
        'una decisión de honestidad, no una carencia: no hay ningún '
        'coeficiente con fuente pública para un obrador de chocolate, y la '
        'alternativa sería inventarse constantes o dejar celdas que el lector '
        'no sabe rellenar.',
        'Lo que sí hace, que es más útil: un semáforo de coherencia entre la '
        'temperatura objetivo, la temperatura exterior de tu ciudad en agosto '
        'y la potencia frigorífica que te OFRECE el instalador, más el salto '
        'de diseño que él declare. Tres cifras que casi nadie pone juntas.',
        'Y la ficha de preguntas, que es la que cambia la conversación: '
        'volumen tomado para el cálculo, salto de diseño, aportes internos, '
        'renovaciones de aire, capacidad de deshumidificación, si deshumidifica '
        'sin bajar de más la temperatura, si lleva evaporativo —tiene que ser '
        'que no—, si incluye puesta en marcha y equilibrado, garantía y '
        'consumo en agosto.',
    ],
}

PPE_08 = {
    'La escalera de atemperadoras y el cruce de kilos por semana con máquina': [
        'Presentar la decisión de máquina como lo que es: no se elige por '
        'marca ni por presupuesto, se elige por kilos de cobertura a la semana '
        'y por si el negocio va a tener una o dos líneas de templado.',
        'Dar la escalera completa de atemperadoras, una a una y con su '
        'capacidad, desde la de sobremesa de arranque hasta las continuas '
        'grandes. Cada una con su identificador propio: la escalera se cita '
        'máquina a máquina, nunca como un rango agregado.',
        'Cruzarla con la capacidad: la hoja de capacidad por equipo convierte '
        'cada máquina en bombones al día y dice cuál limita. Y la sorpresa que '
        'casi siempre da ese cruce: la atemperadora no suele ser el cuello de '
        'botella; lo son las manos y el puesto de envasado.',
        'Sacar el criterio de compra: comprar la máquina para el pico de '
        'Navidad es caro y comprarla para el día medio es quedarse corto en '
        'diciembre. La salida es adelantar producción de lo que aguanta, que '
        'es lo que calcula el libro de campañas.',
    ],
    'La trampa del impuesto: unos distribuidores publican con y otros sin, y nunca se suman': [
        'Contar el problema real del mercado de maquinaria de chocolate: hay '
        'fichas que publican el precio sin impuesto, otras con impuesto y '
        'otras que no lo declaran. Sumarlas todas da un total que no es de '
        'nadie.',
        'Qué hace el pack con eso: cada línea del checklist de equipamiento '
        'lleva la base declarada por la fuente y su tipo, y las que no lo '
        'declaran van marcadas como no declarada, no supuestas. El total se '
        'publica en base imponible.',
        'Y dos líneas que merecen mención aparte porque se publican distinto: '
        'los moldes van como RANGO por unidad, no como precio cerrado, y el '
        'mantenedor va como un «desde», que es un suelo comercial y no un '
        'precio. Se presupuestan, no se copian.',
    ],
    'La vitrina de chocolate no es la de pastelería': [
        'La diferencia que hay que entender antes de comprar: una vitrina de '
        'pastelería trabaja en frío positivo bajo, y el chocolate a esa '
        'temperatura condensa al salir. La vitrina de bombonería es templada y '
        'controla humedad.',
        'Distinguir dos cosas que se confunden todo el rato: el OBJETIVO '
        'operativo del negocio —el que publica el kit y el que usa el pack— y '
        'el RANGO DE TRABAJO del equipo que te ofrece un fabricante concreto. '
        'Son dos números distintos, y el semáforo del libro de vida útil sólo '
        'avisa cuando la temperatura se va de verdad por arriba.',
    ],
    'Plazos de entrega y segunda mano': [
        'Dar el plazo crítico de entrega del caso modelado y decir qué línea '
        'lo marca, porque es la cifra que de verdad mueve la fecha de '
        'apertura: no la firma del alquiler, la máquina.',
        'Explicar cómo se usa: el cronograma del expediente legal trae ese '
        'plazo por celda editable y avisa si la ruta crítica del papeleo es '
        'más corta que la entrega. Quien no lo cuadra abre con la tienda '
        'montada y sin atemperadora.',
        'Y la segunda mano, con el criterio honesto: en templado y frío se '
        'compra con garantía y con puesta en marcha, porque lo que falla no es '
        'la chapa, es la electrónica y el control de temperatura. Los datos '
        'del sector no traen precios de segunda mano, así que no se publican.',
    ],
}

PPE_09 = {
    'Una chocolatería minorista no va al registro general, y tener obrador no te saca de minorista': [
        'Corregir el error número dos del nicho, y hacerlo con la norma '
        'delante: quien vende al consumidor final en su propio establecimiento '
        'está EXCLUIDO del registro general sanitario por el art. 2.2 del '
        'RD 191/2011, en la redacción que le dio el RD 1021/2022.',
        'Decir qué hay en su lugar: una comunicación o declaración responsable '
        'al registro de tu comunidad autónoma. Y decir lo que casi nadie dice, '
        'que es lo que evita el disgusto: ese trámite NO te habilita para '
        'abrir. No esperas respuesta, y no te protege si el resto no está en '
        'regla.',
        'Cerrar el otro bulo, el que venden algunas consultoras: tener obrador '
        'y transformar producto NO te saca de la condición de minorista. Lo '
        'que te saca es A QUIÉN vendes, no lo que haces.',
        'Explicar cómo se resuelve en el pack: el árbol de registro sanitario '
        'son cuatro preguntas y un veredicto, y el veredicto dice el trámite, '
        'si habilita y cuándo se presenta.',
    ],
    'Cuándo sí vuelve: tres condiciones acumulativas y dos vías dentro de «marginal»': [
        'Empezar por la puerta de entrada, que es lo que el noventa por ciento '
        'de los textos se salta: el art. 3 del RD 1021/2022 sólo se activa si '
        'suministras a otros establecimientos minoristas de DISTINTA '
        'titularidad. Si no lo haces, todo lo que viene detrás no te aplica.',
        'Dar las tres condiciones y decir que son ACUMULATIVAS: marginal, '
        'localizado y restringido. Basta fallar una para caer en el registro '
        'general.',
        'Desarrollar «marginal», que tiene DOS vías alternativas y no un solo '
        'umbral: hasta un porcentaje del volumen anual O hasta un máximo de '
        'kilos a la semana. Basta cumplir una de las dos, y las dos se miden '
        'SÓLO sobre lo que sirves a otros minoristas.',
        'Desarrollar «restringido», que es el que de verdad mata a una '
        'chocolatería que crece: basta con que UNO solo de tus clientes esté '
        'inscrito en el registro general para perderlo. Y el regalo '
        'corporativo es justo la línea que lo rompe.',
    ],
    'Central y sucursales': [
        'Explicar el esquema y su ventaja: un obrador central que abastece a '
        'tus propios despachos no es suministro a otros minoristas, porque no '
        'hay distinta titularidad. Es la vía natural para crecer sin cambiar '
        'de régimen.',
        'Y el deber pegado, que se dice en la misma frase: cada despacho se '
        'inscribe por separado en el registro autonómico, aunque el suministro '
        'entre ellos no cuente como venta a otras tiendas.',
    ],
    'La ruta doméstica y la lista de cinco letras': [
        'Plantear la pregunta como llega: mucha gente empieza haciendo '
        'bombones en casa y quiere legalizarse sin montar local. La respuesta '
        'honesta empieza por una lista cerrada, la del art. 13.8 del '
        'RD 1021/2022, que tiene CINCO letras.',
        'Dar las cinco letras y qué permite cada una, y decir con cuidado la '
        'conclusión: por defecto el bombón no encaja en la letra de panadería '
        'y repostería. Eso es INTERPRETACIÓN nuestra, y así se presenta.',
        'Y la letra que lo cambia todo, que es la quinta: otros alimentos que '
        'las autoridades competentes de las comunidades autónomas permitan en '
        'sus territorios. Es una lista abierta, y hay comunidades que ya la '
        'han ejercido. Por eso la hoja empieza preguntando por tu comunidad.',
        'Los TRES requisitos del art. 13.9, que sólo entran en juego si tu '
        'comunidad ha abierto la puerta: volumen proporcional al tamaño de las '
        'instalaciones —que es el que de verdad limita—, un tope de kilos a la '
        'semana, y que se pueda demostrar documentalmente.',
        'Cerrar con la frase que hay que poder repetir sin equivocarse: no '
        'entra en la lista estatal salvo que tu comunidad lo haya añadido. '
        'Nunca «es ilegal en España».',
    ],
    'La clave del registro general cuando sí toca': [
        'Decir qué pasa el día que sí te toca: el registro general tiene un '
        'cajón concreto para el chocolate, con su clave y sus actividades, y '
        'saberlo ahorra una consultoría.',
        'Y marcar el nivel de la fuente, porque es honestidad y es útil: el '
        'catálogo de claves no está en ningún boletín oficial, está en una '
        'guía informativa de la administración. Se cita como guía, no como '
        'norma.',
        'Explicar el orden correcto de la conversación con la asesoría: '
        'primero se resuelve el árbol, y sólo si el veredicto es registro '
        'general se habla de claves. Al revés se paga por tramitar algo que no '
        'hacía falta.',
    ],
    'Artesanía alimentaria: qué es, qué no es y dónde se pide': [
        'Separar dos cosas que se mezclan siempre: la artesanía alimentaria es '
        'una acreditación autonómica VOLUNTARIA, y no tiene nada que ver con '
        'el registro sanitario ni con la norma de calidad del chocolate. Son '
        'tres cosas distintas.',
        'Dar el dato verificado y su límite: en Cataluña el chocolate está '
        'expresamente dentro del repertorio de artesanía alimentaria; en el '
        'resto, el enlace es el registro de tu comunidad. Y la prohibición '
        'expresa: NO se puede escribir que sin esa acreditación no puedas '
        'llamarte artesano, porque es voluntaria.',
    ],
}

PPE_10 = {
    'La tabla de mínimos y las dos bases de cálculo': [
        'Abrir con la idea que ordena el capítulo entero: la norma del '
        'chocolate no trabaja con «porcentaje de cacao», sino con TRES '
        'magnitudes —materia seca total de cacao, manteca de cacao y materia '
        'seca desgrasada— y la bolsa de cobertura que compras sólo publica '
        'una.',
        'Dar la tabla de mínimos por denominación, que está cotejada fila a '
        'fila contra el texto consolidado, y explicar cómo se lee: cada '
        'denominación tiene sus umbrales, y cumplirlos es lo que te da derecho '
        'a usar ese nombre.',
        'Y el punto que más errores produce: hay DOS bases de cálculo en la '
        'misma norma. En las tabletas con frutos secos los mínimos se calculan '
        'DESCONTANDO los ingredientes añadidos; en el chocolate relleno y en '
        'el bombón, el contenido de chocolate se calcula sobre el PESO TOTAL '
        'del producto acabado, con el relleno dentro.',
        'Decir qué pasa si se invierten, porque es la trampa cara: calcular el '
        'mínimo del bombón descontando el relleno da un resultado más '
        'favorable que el legal, y deja pasar por el semáforo una referencia '
        'que no cumple.',
    ],
    '«Bombón de chocolate o praliné» es el mismo punto de la norma': [
        'Dar la definición legal del bombón y su mínimo sobre el peso total, y '
        'el dato de rigor que la acompaña: la palabra «bombón» aparece una '
        'sola vez en toda la norma española.',
        'Y la corrección que casi nadie hace: «praliné» no tiene definición en '
        'la norma española, pero SÍ es denominación de venta europea, en el '
        'mismo punto que el bombón de chocolate y con el mismo mínimo. Si lo '
        'llamas praliné, te obliga igual.',
        'Cerrar con «trufa», que es el contraejemplo: no tiene definición '
        'legal en ninguna de las dos normas. Se puede usar como nombre '
        'comercial, y no da derecho a nada.',
    ],
    'La mención del porcentaje de cacao no es universal': [
        'Desmontar la creencia: la mención «cacao: tanto por ciento mínimo» NO '
        'se exige para todos los productos. La norma la pide para unos '
        'apartados concretos y deja fuera al chocolate blanco, al relleno y al '
        'bombón.',
        'Dar la frase segura para el producto: ponerla no es ilegal; decir que '
        'es obligatoria sí sería falso. Y añadir que el reglamento europeo '
        'dice lo mismo.',
        'Explicar la consecuencia práctica en la vitrina: si la pones en unas '
        'referencias y en otras no, que sea por decisión y no por descuido, '
        'porque el cliente compara cartelitos.',
    ],
    'Los calificativos de calidad, sin lista de palabras': [
        'Contar lo que de verdad dice la norma, que no es lo que circula: '
        'autoriza completar tres denominaciones con menciones o calificativos '
        'referentes a criterios de calidad, y NO enumera ninguna palabra.',
        'Dar el dato de la búsqueda exhaustiva, que es lo que convierte esto '
        'en afirmable: «calidad» aparece una sola vez en todo el real decreto, '
        'justo ahí; «fino» y «superior», cero veces; y «extra», sólo dentro de '
        'otras palabras.',
        'Y la condición que hace que la mención valga algo: sólo cabe sobre '
        'esas tres denominaciones y sólo por encima de unos umbrales '
        'reforzados de materia seca. La denominación literal, además, es '
        '«cobertura de chocolate», no «cobertura» a secas.',
    ],
    'Sucedáneo no es chocolate, y las grasas vegetales con su mención': [
        'Explicar la frontera con precisión: si la manteca de cacao está '
        'SUSTITUIDA, es sucedáneo y así se etiqueta; si sólo se AÑADE un '
        'pequeño porcentaje de unas grasas vegetales tasadas, sigue siendo '
        'chocolate.',
        'Dar el detalle que la mayoría de los textos no trae: esa adición sólo '
        'cabe en unos apartados concretos, y ni el chocolate relleno ni el '
        'bombón están en esa lista.',
        'Y la mención obligatoria que la acompaña, con su formato: cuando se '
        'usan esas grasas, la etiqueta tiene que decirlo, y el sitio y la '
        'forma también están reglados. Es una de esas cosas que sólo se '
        'descubren cuando llega la inspección.',
    ],
}

PPE_11 = {
    'El cadmio sube con el porcentaje de cacao y castiga al negro premium': [
        'Plantear el problema en el lenguaje del negocio: el límite de cadmio '
        'sube cuanto más cacao lleva el producto, así que la referencia más '
        'expuesta es justamente la que quieres que sea tu firma, la tableta de '
        'origen con alto porcentaje.',
        'Decir de quién es el papel: lo que tiene que cumplir el límite es la '
        'cobertura que compras, y quien tiene que enseñarte analíticas es tu '
        'proveedor. Tu primera línea de defensa es el boletín de análisis, no '
        'la analítica que pagues tú.',
        'Dar las tres obligaciones que sí son tuyas y no de tu proveedor: no '
        'usar como ingrediente lo que pase de límite, no diluir mezclando, y '
        'poder justificar los factores de concentración o dilución ante el '
        'control oficial. Eso último es un papel que se guarda.',
    ],
    'Lo que es chocolate para la denominación no lo es para los contaminantes': [
        'Dar la corrección grande de este capítulo, porque cambia el '
        'veredicto: la nota del reglamento de contaminantes remite SÓLO a tres '
        'puntos de la directiva del chocolate. Quedan fuera la manteca de '
        'cacao, el chocolate familiar con leche, el blanco, el relleno, el '
        'chocolate a la taza y el bombón.',
        'Sacar la consecuencia con todas las letras: tu bombón NO tiene límite '
        'propio de cadmio. Se le aplica la regla general de los alimentos '
        'compuestos, que es otra cosa y se justifica de otra manera.',
        'Y la regla de escritura que se lleva el lector: dos normas pueden '
        'hablar del mismo producto con definiciones distintas, y suponer que '
        'coinciden es la manera más rápida de publicar una falsedad. Aquí no '
        'coinciden.',
    ],
    'Eres operador posterior si tu cobertura llega amparada, y ese paso es una inferencia declarada': [
        'Explicar el reglamento de deforestación en dos frases y con su '
        'alcance real: el chocolate terminado está dentro, no sólo el grano; y '
        'exportar cajas fuera de la Unión Europea también está sujeto.',
        'Dar la figura que importa, con su definición: quien introduce en el '
        'mercado productos que YA han sido comercializados y están amparados '
        'por una declaración de diligencia debida es OPERADOR POSTERIOR, no '
        'operador.',
        'Y aquí va la frase exacta, presentada como lo que es —una inferencia '
        'nuestra, no una cita—: si tu cobertura llega ya comercializada en la '
        'Unión Europea y amparada por una declaración de diligencia debida, '
        'eres operador posterior y el aplazamiento, que es para operadores, no '
        'te alcanza; tu fecha es el 30 de diciembre de 2026. Si tu cobertura '
        'NO está amparada, la calificación deja de ser automática y hay que '
        'revisarla.',
        'Cerrar con el aviso de rigor que casi ningún texto da: la definición '
        'exige que TODOS los insumos estén amparados. Con cobertura anterior a '
        'la norma, o con un proveedor que no lo acredita, no se puede dar por '
        'hecho nada.',
    ],
    'El aplazamiento a junio de 2027 no te sirve si abres ahora': [
        'Desmontar la lectura tranquilizadora que circula: el aplazamiento del '
        'art. 38.3 es para OPERADORES, personas físicas, microempresas o '
        'pequeñas empresas que estuviesen establecidas como tales a una fecha '
        'concreta de 2024. Quien abre ahora no cumple ni siquiera esa '
        'condición.',
        'Dar la otra mitad, que es la que hace que esto importe: una '
        'chocolatería que compra cobertura es operador posterior, y el '
        'aplazamiento no está escrito para ella. Su fecha es la general.',
        'Y lo que sí le toca a una pyme, que es menos de lo que se teme: no se '
        'registra en el sistema de información y no le alcanza el deber de '
        'verificación de la cadena. Lo que sí le alcanza entero son los '
        'deberes de recogida y conservación de información durante cinco '
        'años.',
    ],
    'Bean-to-bar: eres operador, y el tostado te mete en otro catálogo': [
        'Cambiar de figura y decirlo claro: quien importa grano de cacao es '
        'OPERADOR, con diligencia debida completa, declaración presentada '
        'ANTES de comercializar, responsabilidad asumida y registro de cinco '
        'años. Es otro papel y otro trabajo.',
        'Avisar del régimen simplificado que muchos confunden con una exención '
        'para pequeños: no lo es, exige estar establecido en un país de riesgo '
        'bajo, y confundirlo es un error grave.',
        'Y la segunda consecuencia, que es ambiental y no de cacao: si tuestas '
        'tú el grano, entras en el catálogo de actividades potencialmente '
        'contaminadoras de la atmósfera por un epígrafe que habla de café «o '
        'similares», lo cual es interpretación; y la nota que sube de grupo '
        'incluye los núcleos de población, así que en ciudad esa condición se '
        'cumple siempre. Va como pregunta a tu comunidad autónoma.',
    ],
}

PPE_12 = {
    'El autocontrol simplificado es legal y exige responsable designado con nombre': [
        'Quitar el miedo y poner el requisito: un obrador pequeño puede '
        'trabajar con un sistema de autocontrol simplificado, basado en guías, '
        'y eso es perfectamente legal. Lo que no es opcional es que haya un '
        'responsable designado con nombre y apellidos.',
        'Explicar qué tiene que haber encima de la mesa el día de la '
        'inspección, sin convertir el capítulo en un manual de autocontrol: el '
        'plan, los registros que ese plan diga, el registro de formación y la '
        'documentación de proveedores.',
        'Marcar la frontera con el Pack APPCC, que es producto de la casa: los '
        'registros completos y la matriz de alérgenos por referencia están '
        'allí. Aquí se decide QUÉ tiene que existir, no se rellena.',
    ],
    'Los peligros de un obrador de chocolate no son los de una pastelería': [
        'Dar la diferencia de perfil de riesgo, que es lo que hace que un plan '
        'copiado de una pastelería no sirva: en chocolate baja el peligro '
        'microbiológico y suben el alérgeno cruzado y el cuerpo extraño '
        'metálico.',
        'Traducirlo a prerrequisitos concretos: la temperatura y la humedad '
        'del obrador entran como prerrequisito, no como punto de control '
        'crítico; y la limpieza entre coberturas y entre rellenos es el punto '
        'que de verdad protege.',
        'Y el aviso de alérgenos que un obrador de chocolate tiene todos los '
        'días: la atemperadora, la manga, el molde y la espátula que han '
        'tocado avellana no se vuelven a usar sin limpiar. Y el capítulo del '
        'reglamento de higiene donde eso vive no es «el capítulo de '
        'alérgenos», que no existe: es un punto concreto del capítulo de '
        'productos alimenticios.',
    ],
    'Los alérgenos de una bombonería son ocho': [
        'Corregir la lista corta que circula, con el anexo delante: son OCHO, '
        'porque cacahuetes, frutos de cáscara y granos de sésamo son entradas '
        'INDEPENDIENTES del anexo de alérgenos, no una sola categoría de '
        '«frutos secos».',
        'Darlos uno a uno —gluten, huevo, cacahuete, soja, leche, frutos de '
        'cáscara, sésamo y sulfitos— y explicar por qué la lecitina de soja '
        'cuenta: las exenciones de ese punto son otras cosas, no la lecitina.',
        'Añadir la nota-puente para quien ya tenga el Kit de Tareas '
        'Chocolatería, escrita tal cual: si usas el kit, desglosa la celda de '
        '«frutos secos» en cacahuetes, frutos de cáscara y sésamo, que son '
        'entradas independientes del anexo de alérgenos.',
        'Y el dato práctico que resuelve el problema de la caja surtida: en un '
        'mostrador atendido, la información de alérgenos del producto sin '
        'envasar puede darse por escrito en el establecimiento y con cartel '
        'visible. Todo menos la fecha puede ir en cartel.',
    ],
    'El lote: qué norma lo manda de verdad y sus tres exenciones': [
        'Corregir el error de citación más repetido del sector: el lote NO '
        'está entre las doce menciones obligatorias del reglamento europeo de '
        'información al consumidor. Viene de una norma española propia, el '
        'RD 1808/1991, que sigue sin modificaciones.',
        'Dar las tres exenciones, porque le ahorran trabajo al lector: el '
        'producto no envasado, el envasado a petición del cliente y el '
        'envasado para venta inmediata no necesitan lote; tampoco los '
        'envoltorios muy pequeños; y una etiqueta que lleve fecha con día y '
        'mes puede prescindir de él.',
        'Aterrizarlo en la vitrina: el bombón despachado a granel y la caja '
        'que se llena delante del cliente caen de lleno en la primera '
        'exención. La tableta envasada con su etiqueta, no.',
        'Y el criterio de gestión, que es lo que importa cuando crece el '
        'negocio: aunque estés exento, un identificador de lote propio es lo '
        'que te permite retirar UNA tanda en lugar de todo el escaparate.',
    ],
    '«Sin gluten» es un umbral analítico, no una declaración libre': [
        'Explicarlo con el número delante: es un umbral analítico medido en el '
        'producto tal como se vende, no una declaración de intenciones sobre '
        'los ingredientes.',
        'Dar la ventaja de partida de una chocolatería y su límite: sin harina '
        'en el obrador, casi todo el riesgo de gluten viene del ingrediente '
        'comprado —barquillo, galleta, cereal—, así que el control está en la '
        'ficha técnica del proveedor y en la limpieza.',
    ],
}

PPE_13 = {
    'Los proveedores verificados, por categoría': [
        'Presentar la lista por lo que es: seis proveedores con la dirección '
        'web comprobada en la fecha de corte de esta edición, y no una '
        'recomendación comercial. Lo que el research recogió sin poder '
        'verificar NO se publica.',
        'Recorrer las categorías y decir qué hay que negociar en cada una: '
        'cobertura y chocolate profesional, grano para bean-to-bar, '
        'maquinaria, moldes y utensilios, packaging y regalo corporativo.',
        'Dar el método de la primera compra: empieza por dos o tres '
        'proveedores, no por seis. Abrir ficha con un proveedor cuesta tiempo, '
        'pedido mínimo y dinero parado en el almacén.',
    ],
    'La asociación de bean-to-bar como vía fiable para el grano': [
        'Explicar por qué el grano es el bloque de riesgo más alto de la '
        'compra: es donde menos precios públicos hay, donde más cambian los '
        'orígenes y donde más papeles te van a pedir.',
        'Dar la vía que sí es fiable y por qué: el listado público de una '
        'asociación sectorial permite identificar a los fabricantes y a los '
        'importadores, y se publica como «más de cuarenta miembros», sin '
        'cifra cerrada.',
        'Y la advertencia de método: las páginas individuales de los '
        'proveedores de grano no se han abierto, así que no se publica ninguno '
        'con nombre. Preferimos una lista corta verificada a una larga de '
        'oídas.',
    ],
    'Las dos preguntas que separan a quien compra de quien sabe lo que compra': [
        'Presentarlas juntas porque se hacen en el mismo correo: el boletín de '
        'análisis de metales pesados, y el papel del proveedor en la cadena '
        'del reglamento de deforestación.',
        'Explicar la segunda con precisión, porque un semáforo mal montado '
        'suspende a proveedores que cumplen: la pregunta correcta NO es «dame '
        'tu número de declaración», es «¿eres operador, operador posterior o '
        'comerciante?». Sólo al primero se le pide el número, y sólo él está '
        'obligado a dártelo.',
        'Dar la otra mitad del mismo artículo, que no estaba en ninguna lente '
        'y que cierra el círculo: hay que registrar también a los operadores '
        'posteriores y comerciantes a los que TÚ suministras. Es la segunda '
        'tabla del libro de equipamiento, y se conserva cinco años.',
        'Aterrizarlo en el correo que hay que escribir: nombre del proveedor, '
        'qué te vende, su papel en la cadena, su número si es operador, '
        'boletín de cadmio, boletín de hidrocarburos si compras grano, pedido '
        'mínimo y plazo. Ocho columnas y una respuesta por escrito.',
    ],
    'El impuesto al plástico si compras estuches fuera de España': [
        'Decir quién lo paga, que es lo que casi todo el mundo se salta: NO lo '
        'paga quien compra envases en España. Lo paga quien los fabrica, los '
        'importa o los adquiere en otro país de la Unión Europea. Y una '
        'chocolatería compra fuera más que casi cualquier otro obrador: '
        'blísteres, cápsulas, estuches y bolsas.',
        'Dar los dos límites de la exención, que es donde se equivocan hasta '
        'las guías: cubre la importación y la adquisición intracomunitaria '
        'pero NO la fabricación, y cubre unos envases concretos pero no los '
        'semielaborados ni los cierres. Si el pequeño adquirente exento tiene '
        'que inscribirse en el registro territorial depende de una orden '
        'ministerial: eso es pregunta para la asesoría, no afirmación.',
        'Y la buena noticia, con sus dos razones: los moldes de policarbonato, '
        'las guitarras y las hojas de transferencia NO pagan. Primero porque '
        'el ámbito son los envases no reutilizables, y además porque están '
        'expresamente no sujetos.',
    ],
}

PPE_14 = {
    'La unidad de costeo es el molde y la tanda, no la pieza': [
        'Explicar por qué un escandallo de bombonería no se parece a uno de '
        'restaurante: no se costea una pieza, se costea una TANDA de moldes, '
        'porque el templado, el llenado, la cristalización y el desmoldeo se '
        'hacen por tandas y el tiempo se reparte entre las piezas buenas.',
        'Dar la cadena de cálculo con las cifras del caso: piezas por molde, '
        'moldes por tanda, minutos de la tanda, piezas buenas y minutos por '
        'pieza buena. De ahí sale el coste de mano de obra por pieza, que en '
        'bombonería pesa más de lo que casi nadie cree.',
        'Marcar la frontera con el Kit de Escandallos, y hacerlo bien: ese kit '
        'trae una hoja de tarta de chocolate dentro de su libro de pastelería, '
        'y costea una elaboración por unidad. Lo que no existe en el catálogo '
        'es el escandallo del obrador de bombonería por molde y por tanda, con '
        'merma de templado y la caja como unidad de venta. Eso es esto.',
    ],
    'El chocolate limpio se refunde; el que lleva ganache o fruta, a residuo': [
        'Dar la regla del oficio que el Kit de Tareas Chocolatería ya enuncia '
        'y que aquí se cuantifica: el chocolate sin relleno y sin contaminar '
        'se puede refundir; el que lleva ganache o fruta, a residuo.',
        'Sacar la consecuencia de modelo, que es la diferencia con cualquier '
        'otro escandallo: hay DOS tasas de merma, no una. La recuperable '
        'vuelve a la cuba y NO encarece la materia; la no recuperable se '
        'reparte entre las piezas buenas y sí la encarece.',
        'Dar las dos cifras del año en el caso modelado —kilos que vuelven a '
        'la cuba y kilos que van a residuo— y el coste anual de la segunda. '
        'Es dinero que casi nadie mide y que se puede bajar cambiando el orden '
        'de trabajo.',
        'Y el aviso de método para quien venga de otro oficio: meter las dos '
        'mermas en una sola tasa infla el coste de las referencias limpias y '
        'abarata las rellenas. Sale una carta mal priorizada.',
    ],
    'El coste hora de obrador imputado por pieza': [
        'Explicar de dónde sale el coste de la hora de obrador: del coste de '
        'empresa de las personas que producen, no del bruto; y repartido sobre '
        'las horas PRODUCTIVAS, no sobre las horas de contrato.',
        'Dar la cifra del caso modelado y decir qué la mueve: las pagas del '
        'convenio, la cotización a cargo de la empresa y la parte de la '
        'jornada que de verdad se pasa a pie de mesa. Cambiar cualquiera de '
        'las tres cambia todos los escandallos a la vez.',
        'Aterrizarlo en la decisión: hay referencias que sólo son rentables si '
        'se hacen en tandas grandes, porque su coste de mano de obra por pieza '
        'se desploma con el tamaño de tanda. Ésa es la conversación que hay '
        'que tener antes de meterlas en la carta.',
    ],
    'Margen bruto y food cost son la misma regla dicha dos veces': [
        'Zanjar la confusión más común de las cartas: el food cost y el margen '
        'bruto son el mismo número visto del derecho y del revés. Este pack '
        'usa UNA sola regla, y de ahí se deriva la otra.',
        'Y dar el matiz que este producto sí distingue, porque son dos cifras '
        'distintas y no se mezclan nunca: el food cost de escandallo puro y el '
        'food cost CON merma, que es el que de verdad paga el negocio y el que '
        'viaja al plan financiero.',
    ],
}


CAPITULOS += [
    {
        'n': 7,
        'titulo': 'El Clima del Obrador: por Qué el Chocolate Manda Sobre el Local',
        'resumen_indice': 'las cinco ventanas de temperatura y por qué sala y cámara no son lo mismo, por qué no hay temperatura legal del chocolate, el fat bloom y el sugar bloom traducidos a dinero, y la ficha de preguntas al instalador.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector dimensione el aire antes que la máquina: '
                    'que sepa cuántas ventanas de temperatura tiene que '
                    'sostener, que entienda que ninguna se la impone la ley '
                    'sino su propio sistema de autocontrol, y que salga a '
                    'pedir presupuesto de climatización con diez preguntas '
                    'por escrito en la mano.',
        'epigrafes': list(PPE_07),
        'puntos_por_epigrafe': PPE_07,
        'puntos_globales': [
            'Las cinco ventanas de temperatura salen del Kit de Tareas '
            'Chocolatería, que es producto vendido de la casa, y se citan por '
            'fichero y por hoja. La guía NO se inventa otras.',
            'Esta hoja NO calcula carga térmica, y eso se explica en positivo: '
            'no hay coeficientes con fuente pública para un obrador de '
            'chocolate, y lo que sí es construible es el semáforo de '
            'coherencia y la ficha de preguntas.',
            'Nada de técnica de templado: las curvas están en el kit y una '
            'curva mal publicada arruina producción.',
        ],
        'cifras': [
            C('Temperatura mínima objetivo del obrador al templar', f'{X_CAP}!Clima del Obrador!B7', 'num'),
            C('Temperatura máxima objetivo del obrador al templar', f'{X_CAP}!Clima del Obrador!C7', 'num'),
            C('Humedad máxima objetivo del obrador', f'{X_CAP}!Clima del Obrador!E7', 'num'),
            C('Temperatura máxima objetivo de la cámara de conservación', f'{X_CAP}!Clima del Obrador!C8', 'num'),
            C('Temperatura máxima objetivo de la vitrina', f'{X_CAP}!Clima del Obrador!C11', 'num'),
            C('Ventanas climáticas incoherentes entre sí en el caso modelado', f'{X_CAP}!Clima del Obrador!F20', 'num'),
            C('Salto de temperatura que tiene que vencer el equipo en agosto', f'{X_CAP}!Clima del Obrador!F25', 'num'),
            C('Semáforo de coherencia del clima en el caso modelado', f'{X_CAP}!Clima del Obrador!F33', 'txt'),
            C('Preguntas de la ficha del instalador', f'{X_CAP}!Clima del Obrador!F48', 'num'),
            C('Veredicto de la ficha del instalador', f'{X_CAP}!Clima del Obrador!F51', 'txt'),
        ],
        'sector': ['CHN-30', 'CHN-87', 'CHN-30b', 'CHS-44', 'CHS-43'],
        'tablas': [
            {
                'titulo': 'Las cinco ventanas de temperatura del obrador, y de dónde sale cada una (capacidad-obrador-y-clima.xlsx, hoja «Clima del Obrador»)',
                'src': (X_CAP, 'Clima del Obrador'),
                'cols': [('Dónde', 'A', 'txt'), ('T mínima', 'B', 'num'),
                         ('T máxima', 'C', 'num'), ('HR mínima', 'D', 'num'),
                         ('HR máxima', 'E', 'num'),
                         ('De dónde sale', 'F', 'txt')],
                'filas': (7, 11),
                'nota': 'Ninguna de estas cinco ventanas es una exigencia legal: son criterio '
                        'TÉCNICO y salen del Kit de Tareas Chocolatería. ' + V_MINORISTA,
            },
            {
                'titulo': 'La ficha de preguntas al instalador, pregunta a pregunta (capacidad-obrador-y-clima.xlsx, hoja «Clima del Obrador»)',
                'src': (X_CAP, 'Clima del Obrador'),
                'cols': [('Qué le preguntas', 'A', 'txt'), ('Unidad', 'B', 'txt'),
                         ('Respuesta del caso', 'C', 'txt'),
                         ('¿Por escrito?', 'D', 'txt')],
                'filas': (37, 46),
                'nota': 'La columna de «por escrito» es la que vale: una respuesta de palabra '
                        'no sirve para reclamar. Y hay una que sólo admite una contestación: '
                        'el equipo NO puede llevar climatizador evaporativo, porque añade '
                        'humedad al aire, que es justo lo contrario de lo que necesita un '
                        'obrador de chocolate.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir que la ley obliga a tener el obrador a una '
            'temperatura o a una humedad determinadas.',
            'PROHIBIDO calcular carga térmica o dar cualquier coeficiente de '
            'transmitancia, de aportes o de renovaciones: no hay fuente '
            'pública y la hoja no lo hace.',
            'PROHIBIDO recomendar un climatizador evaporativo, y PROHIBIDO '
            'dar su precio: añade humedad.',
            'PROHIBIDO meter cifras de temperatura en el título del capítulo: '
            'un cambio de dato no puede obligar a renombrarlo.',
        ],
    },
    {
        'n': 8,
        'titulo': 'Maquinaria: Atemperadora, Enrobadora y Moldes',
        'resumen_indice': 'la escalera de atemperadoras cruzada con los kilos por semana, la trampa de los precios con y sin impuesto, por qué la vitrina de chocolate no es la de pastelería, y los plazos de entrega que mueven la fecha de apertura.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector negocie con precios y plazos en la mano: '
                    'que sepa qué máquina le toca por kilos y no por catálogo, '
                    'que no sume precios de bases distintas, y que pida primero '
                    'lo que más tarda en llegar.',
        'epigrafes': list(PPE_08),
        'puntos_por_epigrafe': PPE_08,
        'puntos_globales': [
            'Las máquinas se citan UNA A UNA, con su capacidad y su fuente: '
            'nunca como un rango agregado ni como «la escalera» en bloque.',
            'Toda línea de precio lleva su base de impuesto declarada. Las '
            'fichas que no la declaran van marcadas como no declarada, no '
            'supuestas, y los totales se publican en base imponible.',
            'Los moldes van como rango por unidad y el mantenedor como un '
            '«desde»: no son precios cerrados y no se presentan como tales.',
        ],
        'cifras': [
            C('Precio de referencia de la atemperadora continua de sobremesa', f'{X_EQUIP}!Equipamiento!I15', 'eur'),
            C('Bombones al día de obrador que permite esa atemperadora', f'{X_CAP}!Capacidad por Equipo!M6', 'num'),
            C('Total de referencia sin IVA de las líneas críticas', f'{X_EQUIP}!Equipamiento!I35', 'eur'),
            C('Total de referencia sin IVA de todas las líneas', f'{X_EQUIP}!Equipamiento!I36', 'eur'),
            C('IVA soportado sobre el precio real de la compra', f'{X_EQUIP}!Equipamiento!I40', 'eur'),
            C('Desembolso real con IVA de la dotación', f'{X_EQUIP}!Equipamiento!I41', 'eur'),
            C('Líneas que sólo pueden publicarse como rango', f'{X_EQUIP}!Equipamiento!I42', 'num'),
            C('Líneas que son un «desde» y hay que presupuestar', f'{X_EQUIP}!Equipamiento!I43', 'num'),
            C('Plazo crítico de entrega, en semanas', f'{X_EQUIP}!Equipamiento!I53', 'num'),
            C('Línea que marca el plazo crítico', f'{X_EQUIP}!Equipamiento!I54', 'txt'),
        ],
        'sector': ['CHS-41a', 'CHS-41b', 'CHS-41c', 'CHS-41d', 'CHS-41e',
                   'CHS-41f', 'CHS-41g', 'CHS-41h', 'CHS-41i', 'CHS-41j',
                   'CHS-42a', 'CHS-42b', 'CHS-42i', 'CHS-43', 'CHS-45a',
                   'CHS-46a', 'CHS-48'],
        'tablas': [
            {
                'titulo': 'La dotación completa, línea a línea, con su base de impuesto y su plazo (checklist-equipamiento-y-proveedores-cacao.xlsx, hoja «Equipamiento»)',
                'src': (X_EQUIP, 'Equipamiento'),
                'cols': [('Partida', 'C', 'txt'), ('Prioridad', 'H', 'txt'),
                         ('Precio de referencia sin IVA (€)', 'L', 'eur'),
                         ('Base declarada por la fuente', 'J', 'txt'),
                         ('Plazo de entrega (semanas)', 'R', 'num')],
                'filas': (15, 31),
                'nota': 'Las líneas marcadas como opcionales vienen desmarcadas a propósito: '
                        'son decisiones, no dotación mínima. Y las que dicen «no declarada» '
                        'son exactamente eso: la ficha del distribuidor no dice si el precio '
                        'lleva impuesto, y no se supone.',
            },
            {
                'titulo': 'Qué bombones al día permite cada equipo, y cuál limita de verdad (capacidad-obrador-y-clima.xlsx, hoja «Capacidad por Equipo»)',
                'src': (X_CAP, 'Capacidad por Equipo'),
                'cols': [('Equipo o puesto', 'B', 'txt'), ('Categoría', 'C', 'txt'),
                         ('¿Lo tienes?', 'D', 'txt'),
                         ('Bombones al día del equipo', 'K', 'num'),
                         ('Bombones al día de obrador que permite', 'M', 'num')],
                'filas': (6, 16),
                'nota': 'Todo se cuenta en bombones equivalentes de obrador. La última columna '
                        'no es la anterior: corrige por la parte del surtido que pasa por ese '
                        'equipo, y por eso una máquina que sólo toca el dieciocho por ciento '
                        'de la carta permite muchos más bombones al día de los que ella misma '
                        'produce.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO dar el precio del tren de bean-to-bar o de cualquiera '
            'de sus equipos: no existe precio público verificado, y lo que se '
            'entrega es la lista de la compra y las preguntas.',
            'PROHIBIDO escribir «doce moldes por treinta euros» o cualquier '
            'multiplicación de ese tipo: el dato medido es un rango por '
            'unidad.',
            'PROHIBIDO publicar precios de segunda mano o precios de tiendas '
            'de otros países: no están en los datos del sector.',
        ],
    },
    {
        'n': 9,
        'titulo': 'Licencias, Sanidad y Registro: el Camino Completo',
        'resumen_indice': 'por qué una chocolatería minorista no va al registro general, cuándo sí vuelve y con qué tres condiciones acumulativas, central y sucursales, la ruta doméstica con la lista de cinco letras, la clave del registro general cuando toca y la artesanía alimentaria.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector sepa exactamente qué papel sanitario le '
                    'toca, en qué orden, y qué es lo que de verdad se lo '
                    'cambia: no lo que fabrica, sino a quién vende. Y que sepa '
                    'decir la frase de la ruta doméstica sin equivocarse.',
        'epigrafes': list(PPE_09),
        'puntos_por_epigrafe': PPE_09,
        'puntos_globales': [
            'Todo lo legal de este capítulo va con su norma, su artículo y la '
            'fecha de comprobación. Lo que no está verificado se dice que no '
            'lo está y se convierte en pregunta a tu comunidad autónoma.',
            'Las tres condiciones del art. 3 son ACUMULATIVAS y «marginal» '
            'tiene DOS vías alternativas: las dos cosas se repiten cada vez '
            'que aparecen, porque son las dos que más se cuentan mal.',
            'Ninguna frase de este capítulo puede leerse como «esto es ilegal '
            'en España». La fórmula es siempre: no entra en la lista estatal '
            'salvo que tu comunidad lo haya añadido.',
        ],
        'cifras': [
            C('Régimen sanitario del caso modelado', f'{X_LEGAL}!Árbol de Registro Sanitario!B12', 'txt'),
            C('Trámite sanitario que le toca', f'{X_LEGAL}!Árbol de Registro Sanitario!B13', 'txt'),
            C('¿Ese trámite habilita para abrir?', f'{X_LEGAL}!Árbol de Registro Sanitario!B14', 'txt'),
            C('Umbral de la primera vía de marginalidad, sobre el volumen anual', f'{X_LEGAL}!Suministro a Otros Minoristas!B20', 'pct0'),
            C('Umbral de la segunda vía de marginalidad, en kilos a la semana', f'{X_LEGAL}!Suministro a Otros Minoristas!B23', 'num'),
            C('Veredicto del artículo 3 en el caso modelado', f'{X_LEGAL}!Suministro a Otros Minoristas!B41', 'txt'),
            C('Tope absoluto de kilos a la semana de la ruta doméstica', f'{X_LEGAL}!Ruta Doméstica!B23', 'num'),
            C('Veredicto de la ruta doméstica en el caso modelado', f'{X_LEGAL}!Ruta Doméstica!B32', 'txt'),
            C('Trámites del expediente legal completo', f'{X_LEGAL}!Checklist Legal (F1-F6)!D58', 'num'),
            C('Trámites que cambian según la comunidad autónoma', f'{X_LEGAL}!Checklist Legal (F1-F6)!D66', 'num'),
        ],
        'sector': ['CHN-39', 'CHN-40', 'CHN-40b', 'CHN-41', 'CHN-42', 'CHN-43',
                   'CHN-44', 'CHN-44-int', 'CHN-44b', 'CHN-90', 'CHN-52',
                   'CHN-53', 'CHN-87', 'PA-29c'],
        'tablas': [
            {
                'titulo': 'Los tres casos del registro sanitario, y dónde caes tú (checklist-legal-licencias-y-cacao.xlsx, hoja «Árbol de Registro Sanitario»)',
                'src': (X_LEGAL, 'Árbol de Registro Sanitario'),
                'cols': [('Tu situación', 'A', 'txt'), ('Lo que te toca', 'B', 'txt'),
                         ('Por qué', 'C', 'txt')],
                'filas': (20, 22),
                'nota': 'Basta con fallar UNA de las tres condiciones para pasar del segundo '
                        'caso al tercero: son acumulativas. ' + V_MINORISTA,
            },
            {
                'titulo': 'Las cinco letras de la lista estatal del obrador en vivienda (checklist-legal-licencias-y-cacao.xlsx, hoja «Ruta Doméstica»)',
                'src': (X_LEGAL, 'Ruta Doméstica'),
                'cols': [('Letra', 'A', 'txt'), ('Qué permite', 'B', 'txt'),
                         ('Qué NO cubre, y por qué importa aquí', 'C', 'txt')],
                'filas': (13, 17),
                'nota': 'La quinta letra es la que lo cambia todo: es una lista abierta que '
                        'cada comunidad autónoma puede ampliar. Por eso la hoja empieza '
                        'preguntando por la tuya, y no por los kilos. ' + V_MINORISTA,
            },
            {
                'titulo': 'Artesanía alimentaria: tres cosas que no son la misma',
                'cabecera': ['Qué es', 'Qué te da', 'Qué NO te da', 'Dónde se pide'],
                'filas': [
                    ['Acreditación autonómica de artesanía alimentaria',
                     'Un distintivo y un carné de persona artesana, con requisitos de experiencia y formación',
                     'No sustituye al registro sanitario ni cambia lo que puedes llamar a tu producto',
                     'En el registro de artesanía de tu comunidad autónoma'],
                    ['Registro sanitario autonómico',
                     'Es el trámite que te toca como minorista, y es obligatorio',
                     'No te habilita para abrir por sí solo',
                     'En el registro sanitario de tu comunidad autónoma'],
                    ['Norma de calidad del chocolate',
                     'Define qué puedes llamar chocolate, bombón o cobertura de chocolate',
                     'No contiene las palabras «artesano», «artesanal» ni «casero»',
                     'No se pide: se cumple'],
                ],
                'nota': 'La acreditación de artesanía es VOLUNTARIA: nadie puede decirte que '
                        'sin ella no puedas llamarte artesano. En Cataluña el chocolate está '
                        'expresamente dentro de su repertorio; en el resto, comprueba el '
                        'registro de la tuya.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir «necesitas el registro general sanitario para '
            'abrir una chocolatería».',
            'PROHIBIDO escribir «los quinientos kilos incluyen el mostrador»: '
            'el artículo sólo habla del suministro a otros minoristas de '
            'distinta titularidad, y las dos vías de marginalidad son '
            'ALTERNATIVAS, no acumulativas entre sí.',
            'PROHIBIDO escribir «hacer bombones en casa para vender es ilegal '
            'en España» y PROHIBIDO afirmar que una comunidad concreta permite '
            'el chocolate desde vivienda si su lista dice otra palabra.',
            'PROHIBIDO usar el decreto catalán de artesanía alimentaria como '
            'prueba de qué es repostería a efectos sanitarios: es otro '
            'registro, otra competencia y otro fin.',
        ],
    },
    {
        'n': 10,
        'titulo': 'Cómo Puedes Llamar a lo que Vendes: las Denominaciones Legales del Cacao',
        'resumen_indice': 'la tabla de mínimos y las dos bases de cálculo que casi todo el mundo invierte, praliné como denominación europea, la mención del porcentaje de cacao que no es universal, los calificativos de calidad sin lista de palabras, y la frontera del sucedáneo.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector no rotule mal la vitrina: que sepa qué '
                    'nombre puede usar en cada referencia, con qué mínimos, '
                    'con qué base de cálculo y con qué menciones obligatorias; '
                    'y que sepa qué tres magnitudes tiene que pedirle a su '
                    'proveedor porque la bolsa no las trae.',
        'epigrafes': list(PPE_10),
        'puntos_por_epigrafe': PPE_10,
        'puntos_globales': [
            'Sólo se entrecomilla lo que está literalmente en el boletín '
            'oficial o en el diario oficial europeo. Lo que es interpretación '
            'se presenta como interpretación.',
            'La norma española del chocolate tiene UN artículo único: sus '
            'divisiones son apartados, y se citan como apartados.',
            'Este capítulo va ANTES que el del escandallo a propósito: el '
            'semáforo del veinticinco por ciento que calcula el libro de la '
            'carta necesita que esta decisión esté tomada.',
        ],
        'cifras': [
            C('Chocolate mínimo sobre el peso total del bombón', f'{X_CARTA}!Denominaciones y Mínimos!B38', 'pct0'),
            C('Materia seca total de cacao mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B39', 'pct0'),
            C('Manteca de cacao mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B40', 'pct0'),
            C('Materia seca desgrasada mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B41', 'pct0'),
            C('Chocolate sobre el peso total del bombón de ganache negra', f'{X_CARTA}!Denominaciones y Mínimos!L7', 'pct1'),
            C('Chocolate sobre el peso total de la trufa', f'{X_CARTA}!Denominaciones y Mínimos!L11', 'pct1'),
            C('Chocolate sobre el peso total de la tableta rellena', f'{X_CARTA}!Denominaciones y Mínimos!L22', 'pct1'),
            C('Materia seca total de cacao de la cobertura negra del caso', f'{X_CARTA}!Denominaciones y Mínimos!B45', 'pct1'),
            C('Manteca de cacao de esa misma cobertura', f'{X_CARTA}!Denominaciones y Mínimos!C45', 'pct1'),
            C('Materia seca desgrasada de esa misma cobertura', f'{X_CARTA}!Denominaciones y Mínimos!D45', 'pct1'),
        ],
        'sector': ['CHN-01', 'CHN-02', 'CHN-03', 'CHN-03b', 'CHN-04', 'CHN-05',
                   'CHN-06', 'CHN-06b', 'CHN-07', 'CHN-08', 'CHN-09', 'CHN-10',
                   'CHN-11', 'CHN-12', 'CHN-13', 'CHN-14', 'CHN-15', 'CHN-15b',
                   'CHN-53', 'CHN-55', 'CHN-81', 'CHN-82', 'CHN-83'],
        'tablas': [
            {
                'titulo': 'Qué puedes llamar legalmente a cada referencia de la carta (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Denominaciones y Mínimos»)',
                'src': (X_CARTA, 'Denominaciones y Mínimos'),
                'cols': [('Id', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Denominación legal', 'D', 'txt'),
                         ('Mínimo aplicable', 'F', 'txt'),
                         ('¿Obliga la mención del porcentaje?', 'G', 'txt'),
                         ('¿Le aplica el veinticinco por ciento?', 'M', 'txt')],
                'filas': (7, 34),
                'nota': 'Fíjate en la columna del mínimo: en unas denominaciones se calcula '
                        'descontando los ingredientes añadidos y en otras sobre el peso total '
                        'del producto acabado. Son dos bases opuestas dentro de la misma '
                        'norma. ' + V_CHOCO,
            },
            {
                'titulo': 'Las tres magnitudes que la bolsa no trae y hay que pedirle al proveedor (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Denominaciones y Mínimos»)',
                'src': (X_CARTA, 'Denominaciones y Mínimos'),
                'cols': [('Cobertura', 'A', 'txt'),
                         ('Materia seca total de cacao', 'B', 'pct1'),
                         ('Manteca de cacao', 'C', 'pct1'),
                         ('Materia seca desgrasada', 'D', 'pct1'),
                         ('¿Llega a los tres umbrales?', 'E', 'txt')],
                'filas': (45, 48),
                'nota': 'Una bolsa de cobertura publica un solo porcentaje y la norma trabaja '
                        'con tres magnitudes. Estas tres celdas se COPIAN de la ficha técnica '
                        'del proveedor: pídesela por escrito, porque es el papel que sostiene '
                        'lo que escribes en el cartel. ' + V_DIRECTIVA,
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir que «fino», «superior» y «extra» son las '
            'palabras que autoriza la norma: no da lista de palabras.',
            'PROHIBIDO escribir que «praliné» no significa nada legalmente, y '
            'PROHIBIDO presentar «trufa» como denominación legal.',
            'PROHIBIDO presentar la mención «para su consumo cocido» como '
            'requisito europeo: es una adición española.',
            'PROHIBIDO citar «el artículo 6 del RD 1055/2003», que no existe, '
            'y PROHIBIDO remitir al RD 1334/1999 para el etiquetado.',
        ],
    },
    {
        'n': 11,
        'titulo': 'Cacao, Cadmio y Deforestación: Qué te Pide la Norma y Qué le Pides a tu Proveedor',
        'resumen_indice': 'el cadmio que sube con el porcentaje de cacao, por qué lo que es chocolate para la denominación no lo es para los contaminantes, qué figura de la cadena eres y por qué ese paso es una inferencia declarada, el aplazamiento que no te sirve, y qué cambia si tuestas tú el grano.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector compre cacao con los papeles en la mano: '
                    'que sepa qué límites le aplican de verdad, qué papel '
                    'ocupa en la cadena, qué fecha le corre y qué documentación '
                    'tiene que pedir a cada tipo de proveedor.',
        'epigrafes': list(PPE_11),
        'puntos_por_epigrafe': PPE_11,
        'puntos_globales': [
            'El paso de «compro cobertura» a «soy operador posterior» es una '
            'INFERENCIA declarada, no una cita, y se escribe siempre con su '
            'condición delante. La norma se ha modificado tres veces en doce '
            'meses: la fecha de revisión va dentro del capítulo.',
            'Ninguna página ministerial se entrecomilla como si fuera '
            'articulado: se cita como página, con su nivel de fuente.',
            'Este capítulo va ANTES que el de proveedores a propósito: el '
            'árbol de proveedores del libro de equipamiento necesita que el '
            'lector sepa ya qué figura es cada uno.',
        ],
        'cifras': [
            C('¿Tiene el bombón límite propio de cadmio?', f'{X_LEGAL}!Cadmio y Analíticas!B9', 'txt'),
            C('Analíticas propias al año en el caso modelado', f'{X_LEGAL}!Cadmio y Analíticas!B22', 'num'),
            C('Coste anual de esas analíticas', f'{X_LEGAL}!Cadmio y Analíticas!B23', 'eur'),
            C('Parte de tus lotes que cubren esas analíticas', f'{X_LEGAL}!Cadmio y Analíticas!B24', 'pct1'),
            C('Veredicto del cadmio en el caso modelado', f'{X_LEGAL}!Cadmio y Analíticas!B25', 'txt'),
            C('Fecha de verificación de la hoja del reglamento de deforestación', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B6', 'txt'),
            C('De dónde viene el cacao en el caso modelado', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B12', 'txt'),
            C('¿Llega tu cobertura amparada por una declaración?', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B13', 'txt'),
            C('Estado de la hoja antes de que rellenes tu papel', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B18', 'txt'),
            C('Qué documentación te toca una vez resuelto tu papel', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B20', 'txt'),
        ],
        'sector': ['CHN-16', 'CHN-16b', 'CHN-17', 'CHN-18', 'CHN-19', 'CHN-20',
                   'CHN-21', 'CHN-22', 'CHN-23', 'CHN-24', 'CHN-25', 'CHN-26',
                   'CHN-27', 'CHN-28', 'CHN-29', 'CHN-47', 'CHN-47b', 'CHN-60',
                   'CHN-84', 'CHN-85', 'CHN-86'],
        'tablas': [
            {
                'titulo': 'Qué vendes y si tiene límite propio de cadmio (checklist-legal-licencias-y-cacao.xlsx, hoja «Cadmio y Analíticas»)',
                'src': (X_LEGAL, 'Cadmio y Analíticas'),
                'cols': [('Lo que vendes', 'A', 'txt'),
                         ('¿Límite propio de cadmio?', 'B', 'txt'),
                         ('Por qué', 'C', 'txt')],
                'filas': (7, 11),
                'nota': 'La nota del reglamento de contaminantes remite sólo a tres puntos de '
                        'la directiva del chocolate, y el bombón no es uno de ellos: se le '
                        'aplica la regla de los alimentos compuestos. ' + V_CONTAM,
            },
            {
                'titulo': 'Los tres papeles de la cadena y qué le pides a cada uno (checklist-legal-licencias-y-cacao.xlsx, hoja del reglamento de deforestación)',
                'src': (X_LEGAL, 'EUDR — Tu Papel en la Cadena'),
                'cols': [('Papel', 'A', 'txt'),
                         ('¿Le pides el número de su declaración?', 'B', 'txt'),
                         ('Qué significa', 'C', 'txt')],
                'filas': (25, 27),
                'nota': 'Pedirle el número a todo el mundo pondría en rojo a proveedores que '
                        'cumplen: un comerciante no tiene número que darte y no está obligado '
                        'a dártelo. ' + V_EUDR,
            },
            {
                'titulo': 'Las fechas de la norma del cacao, y qué habría que rehacer con cada una',
                'cabecera': ['Qué cambia', 'Fecha conocida', 'Qué hay que rehacer cuando llegue'],
                'filas': [
                    ['Fecha general de aplicación para quien no es operador aplazado',
                     '30 de diciembre de 2026',
                     'La hoja de tu papel en la cadena y la documentación que pides a cada proveedor'],
                    ['Fin del aplazamiento de los operadores establecidos como tales antes del corte',
                     '30 de junio de 2027',
                     'Nada tuyo si compras cobertura: ese aplazamiento no está escrito para ti'],
                    ['Derogación de la norma europea anterior de diligencia debida',
                     '30 de diciembre de 2026',
                     'Las referencias normativas de tus contratos de compra'],
                    ['Revisión de la propia hoja, que el libro calcula sola',
                     'A los meses que tú fijes desde la verificación',
                     'Abrir el texto consolidado y comprobar si ha habido una cuarta modificación'],
                ],
                'nota': 'Esta norma se ha tocado tres veces en doce meses: dos reglamentos y '
                        'una corrección de errores. Comprueba su estado ANTES de comprar '
                        'cacao, no después. ' + V_EUDR,
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir «tu bombón tiene un límite de cadmio de '
            'tanto».',
            'PROHIBIDO escribir «el reglamento de deforestación te llega en '
            'junio de 2027 si eres pequeño», y PROHIBIDO escribir «siempre '
            'eres operador posterior» o «tu fecha es el 30 de diciembre de '
            '2026 pase lo que pase».',
            'PROHIBIDO escribir «pide a todos tus proveedores el número de su '
            'declaración de diligencia debida».',
            'PROHIBIDO escribir que el tostado de cacao está en el catálogo de '
            'actividades contaminadoras como si fuera mención expresa, y '
            'PROHIBIDO decir que la subida de grupo sólo pasa cerca de '
            'espacios protegidos.',
        ],
    },
    {
        'n': 12,
        'titulo': 'Autocontrol, Alérgenos y Formación: Qué Tener el Día de la Inspección',
        'resumen_indice': 'el autocontrol simplificado con responsable designado, los peligros propios de un obrador de chocolate, los ocho alérgenos de una bombonería, qué norma manda de verdad el lote y sus tres exenciones, y el umbral analítico del sin gluten.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Que el lector llegue a la inspección con la carpeta hecha '
                    'y sin papeles de más: qué documentos tienen que existir, '
                    'quién los firma, cuántos alérgenos declara de verdad una '
                    'bombonería y qué referencias necesitan lote y cuáles no.',
        'epigrafes': list(PPE_12),
        'puntos_por_epigrafe': PPE_12,
        'puntos_globales': [
            'Aquí NO se rellena ningún registro de autocontrol ni ninguna '
            'matriz de alérgenos por referencia: eso es del Pack APPCC y del '
            'Kit de Tareas Chocolatería, y se cita por su nombre.',
            'La lista de ocho alérgenos se da entera cada vez que aparece: es '
            'la corrección más importante del capítulo y la que más circula '
            'mal.',
            'El «carnet de manipulador» no existe: lo que se pide es el '
            'registro de formación, y se dice así siempre.',
        ],
        'cifras': [
            C('Personas con formación registrada en el caso modelado', f'{X_LEGAL}!Registro de Formación!C20', 'num'),
            C('Formaciones caducadas', f'{X_LEGAL}!Registro de Formación!C21', 'num'),
            C('Validez en meses que fija el propio negocio a su formación', f'{X_LEGAL}!Registro de Formación!C15', 'num'),
            C('Veredicto del registro de formación', f'{X_LEGAL}!Registro de Formación!C23', 'txt'),
            C('Trámites de la fase de autocontrol, alérgenos y formación', f'{X_LEGAL}!Checklist Legal (F1-F6)!E45', 'num'),
            C('Referencias que salen envasadas con etiqueta', f'{X_VIDA}!Etiquetado o Granel!C44', 'num'),
            C('Referencias que se despachan a granel', f'{X_VIDA}!Etiquetado o Granel!E44', 'num'),
            C('Vida útil más corta de toda la carta, en días', f'{X_VIDA}!Vida Útil Declarada!G44', 'num'),
        ],
        'sector': ['CHN-32', 'CHN-33', 'CHN-34', 'CHN-34b', 'CHN-35', 'CHN-36',
                   'CHN-37', 'CHN-38', 'CHN-69', 'CHN-89', 'CHN-31'],
        'tablas': [
            {
                'titulo': 'Los ocho alérgenos de una bombonería, y por qué son ocho y no cinco',
                'cabecera': ['Alérgeno', 'Punto del anexo', 'De dónde entra en un obrador de chocolate'],
                'filas': [
                    ['Cereales con gluten', '1', 'Barquillo, galleta, cereal inflado y cualquier crujiente comprado'],
                    ['Huevo', '3', 'Merengues, algunos rellenos y glaseados'],
                    ['Cacahuetes', '5', 'Praliné de cacahuete y frutos secos garrapiñados: es una entrada PROPIA del anexo'],
                    ['Soja', '6', 'La lecitina de casi toda la cobertura, y sí cuenta'],
                    ['Leche', '7', 'Cobertura con leche, cobertura blanca, nata, mantequilla y gianduja'],
                    ['Frutos de cáscara', '8', 'Avellana, almendra y demás: otra entrada distinta de la del cacahuete'],
                    ['Granos de sésamo', '11', 'Crujientes y coberturas con sésamo: TERCERA entrada independiente'],
                    ['Dióxido de azufre y sulfitos', '12', 'Fruta confitada y algunos licores y jarabes'],
                ],
                'nota': 'Si usas el Kit de Tareas Chocolatería, desglosa la celda de «frutos '
                        'secos» en cacahuetes, frutos de cáscara y sésamo, que son entradas '
                        'independientes del anexo. ' + V_ETIQUETA,
            },
            {
                'titulo': 'Envasado con etiqueta o a granel: no es el mismo régimen (vida-util-rellenos-y-rotacion.xlsx, hoja «Etiquetado o Granel»)',
                'src': (X_VIDA, 'Etiquetado o Granel'),
                'cols': [('Vía', 'A', 'txt'), ('Qué significa', 'B', 'txt'),
                         ('La referencia normativa que te toca', 'F', 'txt')],
                'filas': (7, 8),
                'nota': 'La temperatura de conservación que pone en una etiqueta te obliga a '
                        'ti. Para lo que se despacha a granel no hay etiqueta, así que la '
                        'referencia es tu propio sistema de autocontrol. ' + V_MINORISTA,
            },
            {
                'titulo': 'El registro de formación, persona a persona (checklist-legal-licencias-y-cacao.xlsx, hoja «Registro de Formación»)',
                'src': (X_LEGAL, 'Registro de Formación'),
                'cols': [('Persona', 'B', 'txt'), ('Perfil', 'C', 'txt'),
                         ('Contenido de la formación', 'E', 'txt'),
                         ('Estado', 'H', 'txt')],
                'filas': (7, 9),
                'nota': 'La norma NO fija una caducidad de la formación: los meses de validez '
                        'los fijas tú y los escribes en tu plan. Lo que sí obliga es que el '
                        'empresario garantice la formación y pueda acreditarla.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO hablar del «carnet de manipulador de alimentos» como '
            'requisito legal.',
            'PROHIBIDO escribir que el lote es una mención del reglamento '
            'europeo de información al consumidor, y PROHIBIDO escribir que '
            'todos tus bombones necesitan lote.',
            'PROHIBIDO escribir «los cinco alérgenos de una bombonería».',
            'PROHIBIDO duplicar la matriz de alérgenos por referencia ni los '
            'registros de autocontrol del Pack APPCC.',
        ],
    },
    {
        'n': 13,
        'titulo': 'Proveedores: Cobertura, Cacao, Packaging y Plazos',
        'resumen_indice': 'los proveedores verificados por categoría, la vía fiable para el grano, las dos preguntas que hay que hacer por escrito antes de comprar, y el impuesto al plástico cuando compras estuches fuera de España.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector compare tres presupuestos de verdad y '
                    'monte su cartera de proveedores con los papeles pedidos '
                    'desde el primer correo, en vez de descubrir a mitad de '
                    'campaña que le falta un boletín.',
        'epigrafes': list(PPE_13),
        'puntos_por_epigrafe': PPE_13,
        'puntos_globales': [
            'Sólo se publican proveedores con dirección web comprobada en la '
            'fecha de corte. Lo que el research no pudo verificar no aparece, '
            'y se dice que no aparece.',
            'Los pedidos mínimos y los plazos que trae el libro son SUPUESTOS '
            'sembrados para que la hoja tenga forma: se sustituyen por los '
            'reales en la primera llamada.',
            'Aquí se explica el impuesto al plástico entero. El capítulo 4 '
            'sólo dice que la alerta existe y remite aquí.',
        ],
        'cifras': [
            C('Proveedores publicados con dirección comprobada', f'{X_EQUIP}!Proveedores y EUDR!F15', 'num'),
            C('Proveedores todavía sin clasificar en la cadena', f'{X_EQUIP}!Proveedores y EUDR!F20', 'num'),
            C('Operadores que te deben el número de su declaración, que salen cero mientras no hayas clasificado a ninguno', f'{X_EQUIP}!Proveedores y EUDR!F21', 'num'),
            C('Pedido mínimo acumulado si pides a todos a la vez', f'{X_EQUIP}!Proveedores y EUDR!F24', 'eur'),
            C('Plazo medio de entrega comprometido, en días', f'{X_EQUIP}!Proveedores y EUDR!F25', 'num'),
            C('Veredicto de la documentación de proveedores', f'{X_EQUIP}!Proveedores y EUDR!F26', 'txt'),
            C('Kilos al mes de plástico no reciclado del caso modelado', f'{X_CAPEX}!Parámetros!B19', 'num1'),
            C('Umbral mensual de la exención', f'{X_CAPEX}!Parámetros!B20', 'num'),
            C('Tipo del impuesto por kilo de plástico no reciclado', f'{X_CAPEX}!Parámetros!B21', 'eur2'),
            C('¿Supera el caso modelado el umbral de la exención?', f'{X_CAPEX}!IVA y Tesorería!B34', 'txt'),
        ],
        'sector': ['CHS-50', 'CHS-51', 'CHS-52', 'CHS-53', 'CHS-54', 'CHS-55',
                   'CHN-24', 'CHN-59', 'CHN-61', 'CHN-62', 'CHN-62b',
                   'CHN-62c'],
        'tablas': [
            {
                'titulo': 'Los proveedores verificados y qué papeles le toca a cada uno (checklist-equipamiento-y-proveedores-cacao.xlsx, hoja «Proveedores y EUDR»)',
                'src': (X_EQUIP, 'Proveedores y EUDR'),
                'cols': [('Proveedor', 'B', 'txt'), ('Qué te vende', 'C', 'txt'),
                         ('Dirección', 'D', 'txt'), ('Id del research', 'E', 'txt'),
                         ('Qué papeles le tocan a él', 'N', 'txt')],
                'filas': (7, 12),
                'nota': 'Seis proveedores con dirección comprobada en la fecha de corte. La '
                        'columna de papeles no está resuelta a propósito: la resuelve su '
                        'respuesta por escrito, no nuestra suposición.',
            },
            {
                'titulo': 'El impuesto al plástico: qué paga, qué no y quién lo paga',
                'cabecera': ['Qué compras', '¿Está sujeto?', 'Quién lo paga', 'Qué tienes que hacer tú'],
                'filas': [
                    ['Estuches y cajas de bombones comprados a un proveedor español',
                     'Sí, el envase lo está',
                     'El fabricante o el importador, no tú',
                     'Exigirle la documentación que acredita que cumple, y guardarla'],
                    ['Los mismos estuches comprados en otro país de la Unión Europea',
                     'Sí',
                     'TÚ, como adquirente intracomunitario',
                     'Contar los kilos de plástico no reciclado al mes y llevarlo a tu asesoría'],
                    ['Semielaborados y cierres',
                     'Sí, y quedan FUERA de la exención de los kilos mensuales',
                     'Quien los fabrica, importa o adquiere fuera',
                     'No dar por hecho que la exención te cubre: no cubre estas dos familias'],
                    ['Moldes de policarbonato, guitarras y hojas de transferencia',
                     'NO están sujetos',
                     'Nadie',
                     'Nada: no son envases no reutilizables y además están expresamente no sujetos'],
                ],
                'nota': 'La exención mensual cubre la importación y la adquisición '
                        'intracomunitaria, pero NO la fabricación. Y si el pequeño adquirente '
                        'exento tiene que inscribirse en el registro territorial depende de '
                        'una orden ministerial: eso se pregunta a la asesoría, no se afirma. '
                        + V_PLASTICO,
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO publicar proveedores que no estén en los datos del '
            'sector con dirección comprobada.',
            'PROHIBIDO publicar un número cerrado de miembros de la asociación '
            'de bean-to-bar: se escribe «más de cuarenta».',
            'PROHIBIDO atribuir a un negocio vivo una localidad, un '
            'propietario o una cifra que no venga en los datos del sector.',
        ],
    },
    {
        'n': 14,
        'titulo': 'Escandallo del Chocolate: la Merma de Templado, el Recorte que Vuelve y la Caja',
        'resumen_indice': 'por qué la unidad de costeo es el molde y la tanda, las dos tasas de merma que produce el chocolate, el coste hora de obrador imputado por pieza, y por qué margen bruto y food cost son la misma regla.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector deje de regalar su trabajo: que costee por '
                    'tanda y no por pieza, que separe la merma que vuelve a la '
                    'cuba de la que va a residuo, y que sepa cuál de sus dos '
                    'food cost es el que tiene que mirar.',
        'epigrafes': list(PPE_14),
        'puntos_por_epigrafe': PPE_14,
        'puntos_globales': [
            'El food cost de este capítulo es el food cost CON merma, que es '
            'el que paga el negocio. El de escandallo puro aparece sólo para '
            'compararlos, y se dice cuál es cuál cada vez.',
            'Todos los precios de materia se usan en BASE IMPONIBLE, en los '
            'dos lados del cociente. El precio de referencia de la cobertura '
            'de marca viene declarado con impuesto incluido por su fuente, y '
            'usarlo tal cual sube el coste de materia casi un diez por ciento.',
            'Los gramajes y las fórmulas de relleno son datos de EJEMPLO '
            'declarados para que el modelo tenga qué calcular: no son recetas '
            'ni recomendaciones de formulación.',
        ],
        'cifras': [
            C('Coste de una hora de obrador', f'{X_CARTA}!Parámetros!B15', 'eur2'),
            C('Coste por kilo de la ganache negra fresca', f'{X_CARTA}!Escandallo por Molde y Tanda!B52', 'eur2'),
            C('Kilos al año de chocolate limpio que vuelven a la cuba', f'{X_CARTA}!Merma de Templado y Recortes!M35', 'num1'),
            C('Kilos al año que van a residuo por llevar relleno o fruta', f'{X_CARTA}!Merma de Templado y Recortes!N35', 'num1'),
            C('Coste anual de la merma no recuperable', f'{X_CARTA}!Merma de Templado y Recortes!O35', 'eur'),
            C('Food cost de escandallo de la carta', f'{X_CARTA}!Mix y Ticket Medio!B43', 'pct1'),
            C('Food cost servido, el que va al plan financiero', f'{X_CARTA}!Mix y Ticket Medio!B46', 'pct1'),
            C('Margen bruto medio con el mix de todo el año', f'{X_CARTA}!Mix y Ticket Medio!B48', 'pct1'),
            C('Margen de la caja de doce bombones', f'{X_CARTA}!Unidad vs Caja!C37', 'eur2'),
        ],
        'sector': ['CHS-28a', 'CHS-28c', 'CHS-29'],
        'tablas': [
            {
                'titulo': 'Escandallo por tanda de los diez bombones de colección (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Coste Hora y Mano de Obra»)',
                'src': (X_CARTA, 'Coste Hora y Mano de Obra'),
                'cols': [('Id', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Piezas por tanda', 'E', 'num'),
                         ('Minutos por pieza buena', 'H', 'num2'),
                         ('Coste de mano de obra por pieza (€)', 'K', 'eur2'),
                         ('Coste de materia con merma (€)', 'L', 'eur2'),
                         ('Coste total por pieza (€)', 'M', 'eur2')],
                'filas': (7, 16),
                'nota': 'Los minutos por pieza buena son los de la tanda repartidos entre las '
                        'piezas que salen bien. Por eso una tanda más grande baja el coste de '
                        'mano de obra por pieza, y por eso hay referencias que sólo son '
                        'rentables a partir de cierto tamaño de tanda.',
            },
            {
                'titulo': 'Las dos tasas de merma, referencia a referencia (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Merma de Templado y Recortes»)',
                'src': (X_CARTA, 'Merma de Templado y Recortes'),
                'cols': [('Id', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('¿Lleva ganache, relleno o fruta?', 'C', 'txt'),
                         ('Merma recuperable', 'D', 'pct1'),
                         ('Merma NO recuperable', 'E', 'pct1'),
                         ('Sobrecoste de la merma (€)', 'H', 'eur2'),
                         ('Sobrecoste sobre el coste', 'I', 'pct1')],
                'filas': (7, 16),
                'nota': 'La merma recuperable no encarece la materia: el chocolate limpio '
                        'vuelve a la cuba. La que encarece es la otra, y por eso las '
                        'referencias con relleno tienen su tasa propia. Meter las dos en una '
                        'sola infla el coste de las referencias limpias y abarata las '
                        'rellenas.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir que el Kit de Escandallos no tiene ninguna '
            'hoja de chocolate: tiene una de tarta de chocolate.',
            'PROHIBIDO presentar el margen bruto y el food cost como dos '
            'reglas distintas, y PROHIBIDO mezclar en el mismo párrafo el food '
            'cost de escandallo y el food cost con merma sin decir cuál es '
            'cuál.',
            'PROHIBIDO trabajar con una sola tasa de merma: son dos.',
            'PROHIBIDO convertir este capítulo en un recetario: las fórmulas '
            'de relleno son datos de ejemplo declarados.',
        ],
    },
]


PPE_15 = {
    'El cacao cayó a la mitad y el chocolate subió: la cobertura no baja cuando baja la bolsa': [
        'Empezar por la observación que descoloca a todo el mundo: la '
        'cotización del cacao puede caer con fuerza y el precio de tu '
        'cobertura no se mueve, o incluso sigue subiendo. No es una anomalía: '
        'es cómo funciona la cadena.',
        'Explicar por qué, sin inventar números: entre la bolsa y tu saco de '
        'cinco kilos hay coberturas de compra a plazo, stock del fabricante, '
        'coste de transformación y tarifa de distribuidor. La bolsa es una '
        'señal de tendencia, no tu precio de compra.',
        'Y la consecuencia operativa, que es la tesis del capítulo: no se '
        'planifica con la cotización, se planifica con ESCENARIOS sobre el '
        'precio que hoy tienes en tu tarifa. Por eso el libro parte de tu '
        'precio y no del mercado.',
    ],
    'El ciclo real de revisión es semestral': [
        'Dar el ritmo al que de verdad se mueven las tarifas de cobertura, y '
        'lo que eso significa para una carta: quien revisa precios una vez al '
        'año come dos subidas antes de reaccionar.',
        'Traducirlo a rutina: una revisión de escandallo por temporada, '
        'coincidiendo con el cambio de carta, y una alarma cuando la tarifa '
        'nueva llega. El libro del precio del cacao está hecho para hacer eso '
        'en diez minutos.',
        'Y el aviso de stock, que es la otra cara: comprar de más para '
        'protegerse del precio inmoviliza dinero y ocupa almacén. El libro '
        'calcula los euros parados y el coste financiero de esa decisión, para '
        'que se tome con las dos cifras delante.',
    ],
    'Los cuatro caminos con su número: precio, gramaje, cobertura, margen': [
        'Presentar los cuatro caminos que existen cuando sube el cacao, y '
        'decir que son cuatro y no uno: subir el precio de venta, bajar el '
        'gramaje, cambiar de cobertura o aceptar menos margen.',
        'Dar la subida media de precio que haría falta en el escenario de '
        'trabajo del caso, y la lectura que la acompaña: repartida por el mix, '
        'suele ser mucho menor de lo que la gente teme.',
        'Dar el número de referencias que se rompen en cada escenario y '
        'nombrar la que se rompe primero. Ésa es la que hay que reformular o '
        'retirar antes que ninguna, y casi siempre es la que más cobertura '
        'lleva por pieza.',
        'Explicar el camino del gramaje con su límite legal, que casi nadie '
        'vincula: bajar gramos de chocolate en un bombón puede sacarte del '
        'mínimo del veinticinco por ciento sobre el peso total, y entonces ya '
        'no es una decisión comercial, es un cambio de denominación. El '
        'capítulo 10 tiene la regla.',
    ],
    'Cómo se comunica una subida': [
        'Dar el criterio que funciona en mostrador: se sube por referencia y '
        'con redondeo comercial, no un porcentaje plano a toda la carta; y se '
        'sube antes de campaña, nunca en mitad de ella.',
        'Y el aviso legal que pega de lleno en una chocolatería estacional: '
        'la regla del precio anterior obliga a que el precio tachado sea el '
        'más bajo aplicado en los treinta días anteriores, así que subir en '
        'noviembre para «rebajar» en diciembre no cumple. Y esa regla no está '
        'donde casi todos la citan.',
    ],
}

PPE_16 = {
    'Entre la ganache fresca y la estabilizada hay un factor de tres a cinco': [
        'Dar el dato que ordena todo el capítulo, con la tabla del Kit de '
        'Tareas Chocolatería como fuente y citada por fichero y hoja: los '
        'plazos orientativos por familia, desde los meses de una tableta hasta '
        'los días de una ganache con nata fresca.',
        'Y la lectura que convierte eso en decisión: entre la ganache fresca y '
        'la estabilizada hay un factor de tres a cinco, y esa es una decisión '
        'de MODELO DE NEGOCIO, no técnica. Quien elige fresco elige rotar '
        'rápido; quien elige estabilizado elige poder vender por envío y en '
        'campaña.',
        'Explicar el porqué, que es lo que el kit no desarrolla: lo que manda '
        'es el agua disponible del relleno. Por eso el libro de vida útil '
        'empieza por la actividad de agua y no por el calendario.',
    ],
    'La vida útil la declaras tú y consta en tu plan de autocontrol': [
        'Decir la regla dura con todas las letras: la vida útil la DECLARA el '
        'operador en su sistema de autocontrol. Este libro no la calcula y no '
        'la presenta como norma: es una celda que rellenas tú.',
        'Dar las dos vidas útiles declaradas del caso modelado —la de la '
        'ganache fresca y la de la estabilizada— y decir de dónde salen: del '
        'extremo bajo del plazo orientativo del kit, como supuesto de partida '
        'declarado.',
        'Explicar qué hace el libro con eso, que es lo que el kit no tiene: '
        'convierte la vida útil en fecha de etiqueta, en tamaño de lote y en '
        'merma por caducidad en euros al año. Del plazo a la decisión.',
        'Y el aviso de la caja surtida, que es una trampa clásica: la caja '
        'caduca cuando caduca la pieza más corta que lleva dentro. El libro lo '
        'calcula y avisa.',
    ],
    'Envasado con etiqueta o a granel: no es el mismo régimen': [
        'Plantear la distinción que casi nadie hace y que cambia el papel que '
        'te toca: una misma referencia puede salir envasada con su etiqueta o '
        'despacharse a granel desde la vitrina, y no están bajo la misma regla.',
        'Lo envasado con etiqueta: la temperatura de conservación que TÚ has '
        'puesto en esa etiqueta te obliga a ti, porque la fija quien produce y '
        'envasa. Lo que escribes es lo que tienes que poder mantener.',
        'Lo despachado a granel: no hay etiqueta, así que la referencia no es '
        'ese artículo sino tu sistema de autocontrol, donde la temperatura y '
        'la vida útil constan porque las has declarado tú.',
        'Dar el reparto del caso modelado entre las dos vías y sacar la '
        'consecuencia práctica: cada referencia que pasa de granel a envasada '
        'suma obligaciones de etiquetado, así que envasar no es sólo una '
        'decisión de packaging.',
    ],
    'La vitrina de chocolate no es la de pastelería': [
        'Dar la ventana de la vitrina de bombonería y su humedad, con su '
        'fuente en el kit, y explicar por qué es tan estrecha: por encima de '
        'cierto punto la manteca funde y el bombón pierde brillo; por debajo, '
        'condensa al sacarlo.',
        'Distinguir otra vez, porque aquí se paga: el objetivo operativo del '
        'negocio no es el rango de trabajo del equipo que te venden. El '
        'semáforo se alimenta del rango que tecleas tú y sólo avisa cuando se '
        'va de verdad por arriba.',
        'Dar las referencias del caso que NO van a vitrina sino a nevera, y '
        'por qué: el relleno fresco manda sobre el chocolate. Es una decisión '
        'de colocación que se toma con la actividad de agua delante.',
    ],
    'Las tres vías del huevo, donde aún aplican': [
        'Acotar de entrada para no asustar: en una bombonería el huevo crudo '
        'aparece en pocas cosas, pero aparece. Merengues, algunas trufas con '
        'yema, mazapanes y glaseados.',
        'Dar las tres vías con su consecuencia: tratamiento térmico suficiente, '
        'ovoproducto, o producto con vida útil muy corta y registro de fecha y '
        'hora de elaboración. La vía practicable en un obrador pequeño suele '
        'ser el ovoproducto, y se dice por qué.',
    ],
}

PPE_17 = {
    'Los tres perfiles del obrador': [
        'Presentar la plantilla del caso modelado y decir qué hace cada uno: '
        'Encargado, Chocolatero y Dependiente. Son los nombres literales de '
        'las hojas del Kit de Tareas Chocolatería, y se usan ésos para que el '
        'kit y la guía hablen el mismo idioma.',
        'Dar la dimensión en jornadas equivalentes y explicar por qué no '
        'coincide con el número de personas: media jornada de mostrador es '
        'media jornada, y el titular cuenta como una.',
        'Y el aviso de vocabulario, que aquí vale dinero: «maestro '
        'chocolatero», «bombonero» y «oficial» son etiquetas de otras fuentes '
        '—de convenios y de portales salariales—, no nombres de puesto de esta '
        'plantilla. Si se citan, se citan entrecomilladas y con su '
        'equivalencia al lado.',
    ],
    'Del bruto al coste empresa, con la cotización dentro': [
        'Dar el salto que descoloca en el primer plan financiero: del bruto '
        'mensual del convenio al coste de empresa hay un tercio largo más, y '
        'ese tercio es la cotización a cargo de la empresa.',
        'Dar las tres piezas del cálculo del caso: bruto del grupo de '
        'convenio, número de pagas al año y porcentaje de cotización. Cambiar '
        'cualquiera de las tres mueve el coste de la hora de obrador y, con '
        'él, todos los escandallos.',
        'Y el coste de la hora de obrador como cifra puente entre este '
        'capítulo y el del escandallo: se calcula sobre las horas PRODUCTIVAS, '
        'no sobre las de contrato, porque el resto del tiempo es recepción, '
        'limpieza y mostrador.',
    ],
    'No existe convenio estatal del chocolate, y esto es lo que sí existe': [
        'Dar el hallazgo con su método, porque es la diferencia entre «no lo '
        'he encontrado» y «no existe»: la consulta al registro de convenios '
        'con ámbito estatal devuelve cero resultados para chocolate, bombones, '
        'confitería y pastelería, y la consulta de control con otro producto '
        'sí devuelve resultados. La herramienta funciona; el convenio no está.',
        'Decir qué sí existe: cuatro convenios de ámbito provincial o '
        'autonómico que nombran chocolates o bombones, con su código. Entran '
        'como MÉTODO de búsqueda, no como tablas: no se publica ninguna tabla '
        'salarial distinta de la del ejemplo.',
        'Dar la tabla de referencia del caso —la de la Comunidad de Madrid— '
        'marcada como EJEMPLO y sustituible, con sus grupos y sus brutos, y '
        'decir la vigencia y cuándo caduca.',
        'Y el matiz que un laboralista agradecerá y que nadie publica: en ese '
        'convenio el despacho de bombones está dentro sin condiciones y la '
        'FABRICACIÓN va condicionada. Determinar si tu obrador encaja es una '
        'cuestión de ámbito funcional, y eso se pregunta, no se decide leyendo '
        'un blog.',
    ],
    'Cómo identificar tu convenio': [
        'Dar el procedimiento paso a paso: registro de convenios, ámbito '
        'funcional, provincia, y comprobación de la vigencia y de la última '
        'revisión salarial publicada. Cinco minutos bien empleados.',
        'Y el aviso que ahorra la búsqueda fallida: el nombre con el que el '
        'convenio está registrado NO es el que aparece en su articulado, así '
        'que buscar por la denominación que te suena puede devolver cero '
        'resultados aunque el convenio exista. Se busca por código y por '
        'ámbito.',
    ],
}

PPE_18 = {
    'San Valentín y el peso de un solo evento': [
        'Abrir con la cifra que cambia la planificación de un obrador: hay '
        'campañas que concentran en pocos días una parte del año '
        'desproporcionada, y en bombonería eso es la norma, no la excepción.',
        'Dar el peso de las doce campañas sobre el año en el caso modelado y '
        'el de la mayor de todas, y explicar la diferencia entre facturación '
        'de campaña y facturación INCREMENTAL: parte de lo que vendes esos '
        'días lo habrías vendido igual.',
        'Sacar la consecuencia de capacidad: la demanda de un día de campaña '
        'se mide en bombones de obrador, no en tickets, y ahí es donde el '
        'obrador dice si aguanta. La hoja lo compara campaña a campaña.',
    ],
    'La producción de Navidad se paga en octubre y se cobra en diciembre': [
        'Explicar el desfase de tesorería que hunde a los que no lo ven '
        'venir: los moldes, el packaging y la materia prima de la campaña '
        'grande se compran con semanas o meses de antelación, y la caja llega '
        'después.',
        'Dar la tesorería inmovilizada en moldes y packaging de temporada del '
        'caso modelado y su coste financiero, y decir que esa cifra es la que '
        'hay que tener provisionada antes de octubre.',
        'Y la fecha límite que el plan financiero calcula hacia atrás desde la '
        'capacidad del obrador: hay un día a partir del cual aceptar un pedido '
        'más de Navidad significa no poder servirlo. Saber ese día con '
        'antelación es lo que permite decir que no a tiempo.',
    ],
    'Las comuniones son una campaña propia y sostienen tres meses': [
        'Sacarlas del cajón de Pascua, que es donde casi todo el mundo las '
        'mete: las comuniones son una campaña PROPIA, con antelación de pedido '
        'distinta y con detalle de mesa personalizado.',
        'Explicar qué cambia en el obrador: no es un pico de un día, es un '
        'goteo de pedidos cerrados con semanas de antelación, y eso permite '
        'adelantar producción de lo que aguanta.',
        'Y el papel que juegan en el año: sostienen abril, mayo y junio, que '
        'es justo el tramo en el que el bombón de regalo baja y todavía no ha '
        'llegado el verano.',
    ],
    'Lo que para en agosto es el obrador, no la caja': [
        'Decirlo de entrada y con precisión, porque es la corrección más '
        'importante del capítulo: el valle es AGOSTO, un mes de doce, y lo que '
        'para es el obrador. La tienda sigue abierta.',
        'Dar los números del mes: cuánto factura agosto frente a un mes medio, '
        'y el resultado del mes con los gastos fijos corriendo enteros. Ver '
        'esa cifra en septiembre es un disgusto; verla en enero es una '
        'provisión.',
        'Explicar el cambio de mix, que es la palanca que sí existe: menos '
        'ganache fresca y más tableta y producto estable. Eso baja un poco el '
        'margen y sube mucho la tranquilidad, y el libro calcula la caída '
        'exacta.',
        'Y separar lo que de verdad se para: los envíos, que es una decisión '
        'de CANAL ONLINE y no de mostrador, se apagan en verano porque el '
        'producto no aguanta el transporte. Eso es distinto de cerrar la '
        'tienda.',
    ],
    'Las dos respuestas contraestacionales': [
        'Dar la primera: los talleres y las catas, que funcionan justo cuando '
        'el obrador está parado y no dependen del precio del cacao. El '
        'capítulo 19 pone los números.',
        'Y la segunda, que es de producto: el turista de julio y agosto compra '
        'formato souvenir y producto estable, no ganache fresca. Es el mismo '
        'obrador con otra carta, y el libro lo modela con un segundo mix.',
    ],
}

PPE_19 = {
    'Los tres canales que se salen de la nota del epígrafe minorista, y la pregunta exacta para el asesor': [
        'Poner el marco fiscal en una frase que el lector pueda repetir: el '
        'epígrafe minorista de bombones y caramelos SÍ faculta para fabricar, '
        'pero su nota lo condiciona a que la comercialización se realice en '
        'las propias dependencias de venta.',
        'Dar la consecuencia con los cinco canales delante: mostrador y '
        'talleres caben en esa nota sin discusión; el envío con transporte, el '
        'suministro a hostelería y el regalo corporativo son los tres que '
        'salen fuera de esa condición y hay que consultar.',
        'Decir lo que NO se puede hacer, y por qué: ninguna fuente da un '
        'epígrafe por canal. Lo que el libro publica no es un veredicto, es la '
        'PREGUNTA redactada para el asesor, con la nota literal delante y la '
        'regla de la instrucción que obliga a leerla con su condición.',
        'Y el aviso de la salida fácil, para que nadie la tome sin saber lo '
        'que cuesta: la única alta que cubriría los cinco canales de una vez '
        'es la industrial, y con ella se pierde el amparo de la ley que '
        'prohíbe exigirte licencia previa de actividad, porque su anexo lista '
        'el epígrafe minorista y no el industrial.',
    ],
    'Cuándo el B2B te obliga a inscribirte, y por qué el regalo corporativo es la línea que lo rompe': [
        'Enlazar con el capítulo de licencias sin repetirlo: el suministro a '
        'otros minoristas activa el artículo que ya conoce, con sus tres '
        'condiciones acumulativas.',
        'Dar el dato que decide: basta con que UNO de tus clientes esté '
        'inscrito en el registro general para perder la condición de '
        'restringido, y ahí se acabó la excepción. Un hotel, una cadena o un '
        'obrador industrial lo están casi siempre.',
        'Explicar por qué el regalo corporativo es la línea más peligrosa: es '
        'el canal que más crece sin que te des cuenta, el que más lejos '
        'envía y el que más probablemente te pone delante un cliente '
        'inscrito.',
        'Dar el margen de contribución de cada canal y el punto muerto con y '
        'sin el canal de hostelería, para que la decisión no sea sólo legal: '
        'hay canales que traen obligaciones y dejan menos margen que el '
        'mostrador.',
    ],
    'Vender online sigue siendo minorista, pero te responsabiliza de la temperatura en el camión': [
        'Dar la buena noticia primero, con su fundamento: vender al '
        'consumidor final por internet SIGUE siendo comercio al por menor a '
        'efectos fiscales, porque lo define el destino y comprende el '
        'realizado sin establecimiento. Y no cambia dónde te inscribes '
        'sanitariamente.',
        'Dar lo que sí cambia, que es lo que casi nadie ve venir: te '
        'conviertes en envasador de la caja de envío, respondes de la '
        'temperatura durante el transporte y tienes que dar toda la '
        'información obligatoria ANTES de que el cliente pague.',
        'Y el número que decide si el canal existe: el coste del envío '
        'refrigerado sobre el pedido medio y el margen de contribución que '
        'queda después. El libro lo calcula y da su veredicto.',
    ],
    'A quién le vendes también hay que registrarlo': [
        'Dar la mitad del artículo que casi nunca se cita: además de guardar '
        'los datos de tus proveedores, hay que registrar a los operadores '
        'posteriores y comerciantes a los que TÚ has suministrado producto.',
        'Explicar qué tiene que constar y cuánto se conserva: nombre, '
        'dirección y producto suministrado, durante cinco años. Es la segunda '
        'tabla del libro de equipamiento, y no existe en ningún otro libro del '
        'catálogo.',
        'Cerrar el círculo con el epígrafe minorista: los canales que se salen '
        'de su nota son justo los que hay que registrar. Una misma tabla '
        'resuelve dos obligaciones de dos normas distintas.',
    ],
    'Los talleres, la única línea que funciona en agosto': [
        'Dar las dos cifras que convierten el taller en decisión y no en '
        'ilusión: cuántos asistentes hacen falta para cubrir su coste, y '
        'cuántos contando también la materia.',
        'Y la pregunta de verdad, que es la que casi nadie se hace: cuánto '
        'deja una hora de sala dando taller frente a esa misma hora de sala '
        'vendiendo. Si el taller ocupa el espacio de venta en hora punta, '
        'puede salir caro aunque llene.',
        'Cerrar con el aviso fiscal, sin cifra: un taller de bombonería NO '
        'está exento del impuesto sobre el valor añadido por ser formación. El '
        'tipo aplicable es lo que queda abierto y se consulta con la asesoría '
        'antes de poner precio, no después de haberlo cobrado.',
    ],
}

PPE_20 = {
    'Cuenta de resultados a tres años con estacionalidad y rampa': [
        'Explicar el modelo en tres frases: el año dos es el de crucero, el '
        'año uno va con rampa de arranque y el año tres crece poco. Todo lo '
        'demás sale de ahí.',
        'Dar las cifras del año de crucero —ingresos, margen bruto, costes '
        'fijos y resultado neto— y el margen neto, y decir cómo se lee: el '
        'margen neto de una bombonería con tienda es estrecho, y lo que lo '
        'mueve es el peso del personal sobre las ventas.',
        'Y el aviso sobre el escenario pesimista, que es el que hay que mirar '
        'antes de firmar: con los mismos costes fijos y menos tráfico, el '
        'resultado se va a negativo. Saber cuánto aguantas es más útil que '
        'saber cuánto ganarías.',
    ],
    'Punto muerto con la regla única de margen': [
        'Dar los dos puntos de equilibrio y decir por qué son dos y no uno: el '
        'contable incluye la amortización y el de caja incluye la devolución '
        'del principal del préstamo, que no es gasto pero sale del banco.',
        'Dar los clientes al día y los ingresos al mes que hacen falta para '
        'cada uno, y la holgura sobre lo previsto. Esa holgura es el colchón '
        'real del proyecto.',
        'Explicar la regla única de margen que usa todo el pack y por qué es '
        'una sola: el food cost objetivo y el margen bruto objetivo son el '
        'mismo número, y todos los libros se alimentan de él.',
    ],
    'El sueldo del propietario como renglón propio': [
        'Decir lo que casi ningún plan dice: el trabajo del titular tiene que '
        'estar dentro de los costes, con nombre y con importe. Un plan que se '
        'sostiene sólo porque el dueño no cobra no se sostiene.',
        'Dar cómo aparece en el modelo y por qué va en renglón propio: se ve, '
        'se cambia y se puede comparar con lo que costaría contratar a alguien '
        'que hiciera ese trabajo.',
        'Y el cruce con el capítulo del equipo: el coste de la hora de obrador '
        'que usan todos los escandallos sale de esa misma plantilla. Si el '
        'titular no está dentro, los escandallos mienten.',
    ],
    'Impuesto, facturación verificable y libertad horaria como decisión del día uno': [
        'Dar el tipo que le toca al chocolate y explicarlo bien, porque el '
        'razonamiento importa: va al tipo reducido no porque haya un precepto '
        'que lo nombre, sino porque no está en la lista cerrada del '
        'superreducido y no está excluido del reducido.',
        'Dar la trampa del punto de venta que hay que montar bien desde el '
        'primer día: la misma botella cambia de tipo según se consuma en la '
        'mesa o se la lleve el cliente. Y la facturación verificable no es de '
        'este año, pero el sistema que compres hoy ya tiene que estar '
        'adaptado.',
        'Cerrar con la libertad horaria y su fundamento correcto: una '
        'chocolatería NO está en la lista del artículo que casi todos citan; '
        'le viene por el siguiente, por superficie. El resultado práctico es '
        'el mismo y el fundamento es distinto, y eso importa el día que '
        'alguien te lo discuta.',
    ],
    'Qué se mide en el mes cero y en el mes tres': [
        'Dar la lista corta de lo que hay que medir desde el primer día con el '
        'punto de venta: ticket medio, piezas por ticket, mix por familia y '
        'peso de cada canal. Son los cuatro supuestos que el plan tiene en '
        'celda editable.',
        'Y el hábito que convierte el plan en herramienta: al mes tres se '
        'sustituyen los supuestos por lo medido y se vuelve a leer el punto '
        'muerto. A partir de ahí el plan deja de ser una previsión y pasa a '
        'ser un cuadro de mando.',
    ],
}

PPE_21 = {
    'Qué está vigente y qué está derogado': [
        'Abrir con la utilidad de este anexo: no introduce nada nuevo, da '
        'ESTADO. Sirve para comprobar dentro de un año qué sigue en pie de '
        'todo lo que has leído, y para no citar normas muertas.',
        'Recorrer el cuadro norma a norma con su fecha de comprobación, '
        'empezando por las dos que sostienen el producto: la norma de calidad '
        'del chocolate, que sigue sin una sola modificación desde su '
        'publicación, y la directiva europea, cuyos porcentajes no se han '
        'tocado.',
        'Señalar la que más se mueve, y por qué hay que vigilarla: la norma '
        'europea de deforestación se ha modificado dos veces y ha tenido una '
        'corrección de errores en doce meses.',
        'Y el bloque de las derogadas que siguen circulando por internet, que '
        'es donde más daño hace un contenido viejo: si una web te cita una '
        'norma de esta lista para decirte lo que tienes que hacer, esa web no '
        'se ha actualizado.',
    ],
    'Las fechas que ya sabemos que se mueven': [
        'Dar la lista de fechas conocidas y qué habría que rehacer con cada '
        'una, para que el lector sepa qué parte del pack toca revisar y no '
        'todo el pack.',
        'La más cercana y la más importante para este oficio: la fecha general '
        'de la norma del cacao, que es la que le corre a quien compra '
        'cobertura amparada.',
        'Las de fin de año: el salario mínimo y la tabla del convenio de '
        'referencia, que caducan a la vez y viven en celda editable '
        'precisamente por eso.',
        'Y las de más adelante: la facturación verificable en sus dos tramos, '
        'la obligación de bebida en envase reutilizable y el calendario de '
        'accesibilidad para establecimientos privados.',
    ],
    'Las diez normas cuyo cambio invalidaría algo': [
        'Dar la lista corta de normas críticas y decir qué sostiene cada una '
        'dentro del pack: qué capítulo y qué hoja de qué libro dejarían de ser '
        'correctos si esa norma cambia.',
        'Y el criterio de mantenimiento, que es lo que convierte esto en '
        'herramienta: no hay que revisar el pack entero cada año, hay que '
        'revisar estas normas y, con ellas, sólo las celdas que dependen de '
        'ellas.',
    ],
    'Cómo comprobar una vigencia en un minuto': [
        'Dar el procedimiento para la norma española: ficha del boletín '
        'oficial, línea de última modificación, y texto consolidado. Si la '
        'línea dice que no hay modificaciones, no hay más que mirar.',
        'Y el de la norma europea: consolidado del diario oficial, versión y '
        'marcas de modificación, que dicen de qué acto viene cada párrafo. Es '
        'lo que permite ver que dos artículos han cambiado a la vez y por la '
        'misma reforma, que es justo lo que pasa con la norma del cacao.',
    ],
}


CAPITULOS += [
    {
        'n': 15,
        'titulo': 'El Precio del Cacao: Qué Haces Cuando Sube y Quién Paga la Subida',
        'resumen_indice': 'por qué la cobertura no baja cuando baja la bolsa, el ciclo real de revisión de tarifas, los cuatro caminos con su número cuando sube el cacao, y cómo se comunica una subida sin incumplir la regla del precio anterior.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector tenga los cuatro caminos con su número '
                    'delante antes de que llegue la subida: cuánto tendría que '
                    'subir de precio, cuánto gramaje podría recortar sin salirse '
                    'de la denominación, qué cobertura le vale a qué precio y '
                    'qué referencia se le rompe primero.',
        'epigrafes': list(PPE_15),
        'puntos_por_epigrafe': PPE_15,
        'puntos_globales': [
            'Nunca se da una cotización del cacao como precio de compra: se '
            'trabaja con escenarios sobre TU tarifa, que es el precio que '
            'tienes delante.',
            'El food cost que usa este capítulo es el de MATERIA, para aislar '
            'el efecto del precio de la cobertura. Cuando se compare con el '
            'del plan financiero, se dice que son dos cifras distintas y por '
            'qué.',
            'El precio de la cobertura vive en UN solo sitio de todo el pack. '
            'Si se cambia allí, cambian el escandallo y el plan financiero; si '
            'se cambia en dos sitios, el pack deja de cuadrar y las filas de '
            'cuadre lo dicen.',
        ],
        'cifras': [
            C('Precio de la cobertura negra como lo trae la fuente, con IVA', f'{X_CACAO}!Coste de Cobertura!D7', 'eur2'),
            C('Precio de esa misma cobertura en base imponible, que es el que usa todo el pack', f'{X_CACAO}!Coste de Cobertura!G7', 'eur2'),
            C('Precio de la cobertura de origen en base imponible', f'{X_CACAO}!Coste de Cobertura!G8', 'eur2'),
            C('Coste de toda la cobertura del año', f'{X_CACAO}!Coste de Cobertura!Q44', 'eur'),
            C('Parte del coste de materia que es cobertura', f'{X_CACAO}!Coste de Cobertura!D47', 'pct1'),
            C('Precio de la cobertura negra en el escenario de subida fuerte', f'{X_CACAO}!Escenarios de Precio!E9', 'eur2'),
            C('Referencias que se rompen en el escenario de subida fuerte', f'{X_CACAO}!Escenarios de Precio!K44', 'num'),
            C('La referencia que primero se rompe', f'{X_CACAO}!Repercusión al PVP!C46', 'txt'),
            C('Subida media de PVP que haría falta en el escenario elegido', f'{X_CACAO}!Repercusión al PVP!C49', 'pct1'),
            C('Euros parados en el almacén de cobertura', f'{X_CACAO}!Stock y Cobertura de Compra!H11', 'eur'),
        ],
        'sector': ['CHS-23', 'CHS-24a', 'CHS-24b', 'CHS-28a', 'CHS-28c',
                   'CHN-76'],
        'tablas': [
            {
                'titulo': 'Los cinco escenarios sobre el mismo precio de partida (sensibilidad-al-precio-del-cacao.xlsx, hoja «Escenarios de Precio»)',
                'src': (X_CACAO, 'Escenarios de Precio'),
                'cols': [('Escenario', 'A', 'txt'), ('Qué es', 'B', 'txt'),
                         ('Subida sobre el precio de hoy', 'C', 'pct0'),
                         ('Cobertura negra (€/kg)', 'E', 'eur2'),
                         ('Cobertura de origen (€/kg)', 'F', 'eur2'),
                         ('Cobertura con leche (€/kg)', 'G', 'eur2'),
                         ('Cobertura blanca (€/kg)', 'H', 'eur2')],
                'filas': (7, 11),
                'nota': 'La última fila es tuya: escribe ahí la subida que te ha comunicado tu '
                        'proveedor y toda la hoja se recalcula. Los cuatro precios de partida '
                        'están en base imponible.',
            },
            {
                'titulo': 'Cuánto dinero tienes parado en cobertura, y cuándo hay que volver a pedir (sensibilidad-al-precio-del-cacao.xlsx, hoja «Stock y Cobertura de Compra»)',
                'src': (X_CACAO, 'Stock y Cobertura de Compra'),
                'cols': [('Cobertura', 'B', 'txt'),
                         ('Consumo al año (kg)', 'C', 'num1'),
                         ('Stock objetivo (kg)', 'F', 'num1'),
                         ('Euros parados en el almacén', 'H', 'eur'),
                         ('Punto de recompra (kg)', 'M', 'num1'),
                         ('¿Cubre tu stock el plazo de entrega?', 'N', 'txt')],
                'filas': (7, 11),
                'nota': 'Comprar de más para protegerse de una subida inmoviliza dinero y '
                        'ocupa almacén. La hoja pone las dos cosas al lado para que la '
                        'decisión se tome con las dos cifras delante, no con una.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO dar una cotización del cacao como precio de compra o '
            'como cifra de portada.',
            'PROHIBIDO presentar una bajada de la bolsa como una bajada de tu '
            'coste: la cobertura no baja cuando baja la bolsa, y el capítulo '
            'explica por qué.',
            'PROHIBIDO proponer un recorte de gramaje sin decir que puede '
            'sacarte del mínimo de la denominación: eso deja de ser una '
            'decisión comercial.',
        ],
    },
    {
        'n': 16,
        'titulo': 'Vida Útil del Relleno: Actividad de Agua, Vitrina y Tamaño de Lote',
        'resumen_indice': 'el factor de tres a cinco entre la ganache fresca y la estabilizada, la vida útil que declaras tú y consta en tu autocontrol, envasado con etiqueta o a granel, la vitrina de chocolate frente a la de pastelería y las tres vías del huevo.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Que el lector decida su MODELO DE NEGOCIO y no su '
                    'técnica: cuánto quiere que dure cada referencia, qué '
                    'papel legal le toca según salga envasada o a granel, y de '
                    'cuánto hace cada tanda para no tirar producto.',
        'epigrafes': list(PPE_16),
        'puntos_por_epigrafe': PPE_16,
        'puntos_globales': [
            'Los diez plazos orientativos por familia son los del Kit de '
            'Tareas Chocolatería: se CITAN por fichero y por hoja, y no se '
            'reescriben. Lo que la guía construye es lo que el kit no tiene.',
            'La vida útil NO la calcula este libro: la declara el operador en '
            'su sistema de autocontrol, y aquí es una celda que rellenas tú '
            'con un valor de partida declarado como supuesto.',
            'El semáforo de la vitrina sólo avisa por encima del punto en el '
            'que la manteca empieza a sufrir: NUNCA pone en rojo el objetivo '
            'que publica el propio kit.',
        ],
        'cifras': [
            C('Umbral de vigilancia de la actividad de agua', f'{X_VIDA}!Parámetros!B11', 'num2'),
            C('Actividad de agua de la ganache de nata fresca', f'{X_VIDA}!Tipo de Relleno y aw!E16', 'num2'),
            C('Actividad de agua de la ganache estabilizada', f'{X_VIDA}!Tipo de Relleno y aw!E17', 'num2'),
            C('Referencias con el agua disponible por encima del umbral', f'{X_VIDA}!Tipo de Relleno y aw!E44', 'num'),
            C('Vida útil declarada de la ganache de nata fresca, en días', f'{X_VIDA}!Vida Útil Declarada!G16', 'num'),
            C('Vida útil declarada de la ganache estabilizada, en días', f'{X_VIDA}!Vida Útil Declarada!G17', 'num'),
            C('Temperatura a la que salta la alarma de la vitrina', f'{X_VIDA}!Parámetros!B12', 'num'),
            C('Humedad máxima de trabajo de la vitrina', f'{X_VIDA}!Parámetros!B13', 'num'),
            C('Merma por caducidad de toda la carta al año', f'{X_VIDA}!Lote y Merma por Caducidad!Q44', 'eur'),
            C('Lo que cuesta al año la ganache fresca frente a la estabilizada', f'{X_VIDA}!Lote y Merma por Caducidad!D48', 'eur'),
        ],
        'sector': ['CHN-30', 'CHN-30b', 'CHN-31', 'CHN-38', 'CHN-88',
                   'CHN-87', 'CHS-56', 'CHS-43'],
        'tablas': [
            {
                'titulo': 'Los diez plazos orientativos por familia, tal como los publica el Kit de Tareas Chocolatería (vida-util-rellenos-y-rotacion.xlsx, hoja «Vida Útil Declarada»)',
                'src': (X_VIDA, 'Vida Útil Declarada'),
                'cols': [('Familia', 'A', 'txt'), ('Plazo', 'D', 'txt'),
                         ('Lo que dice el kit', 'F', 'txt')],
                'filas': (48, 57),
                'nota': 'Esta tabla NO es de la guía: es del Kit de Tareas Chocolatería, se '
                        'cita fila a fila y no se reescribe. Lo que construye la guía es la '
                        'actividad de agua, la vida útil que declaras tú, el tamaño de lote y '
                        'la merma por caducidad en euros.',
            },
            {
                'titulo': 'Actividad de agua y familia de vida útil de los diez bombones de colección (vida-util-rellenos-y-rotacion.xlsx, hoja «Tipo de Relleno y aw»)',
                'src': (X_VIDA, 'Tipo de Relleno y aw'),
                'cols': [('Id', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                         ('Tipo de relleno', 'D', 'txt'),
                         ('Actividad de agua', 'E', 'num2'),
                         ('Familia de vida útil del kit', 'G', 'txt'),
                         ('De qué va a morir esta referencia', 'I', 'txt')],
                'filas': (16, 25),
                'nota': 'Mientras la columna de actividades de agua medidas de verdad siga a '
                        'cero, todas estas cifras son estimaciones tuyas: valen para decidir, '
                        'no para declarar en un expediente.',
            },
            {
                'titulo': 'Las cinco temperaturas del kit, y cuál le toca a tu vitrina (vida-util-rellenos-y-rotacion.xlsx, hoja «Temperatura y Vitrina»)',
                'src': (X_VIDA, 'Temperatura y Vitrina'),
                'cols': [('Zona', 'A', 'txt'), ('Temperatura objetivo', 'C', 'txt'),
                         ('Humedad', 'D', 'txt'), ('De dónde sale', 'E', 'txt')],
                'filas': (7, 11),
                'nota': 'Confundir la temperatura de la sala de tienda con la de la cámara, la '
                        'de la vitrina o la de la nevera de rellenos es el error de método más '
                        'caro de este capítulo: son cuatro equipos y cuatro ventanas. '
                        + V_MINORISTA,
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO reescribir la tabla de vidas útiles del Kit de Tareas '
            'Chocolatería: se cita por fichero y por hoja.',
            'PROHIBIDO el titular «factor cinco»: es un factor de tres a '
            'cinco.',
            'PROHIBIDO escribir que los bombones van a cuatro grados porque lo '
            'diga una norma, y PROHIBIDO presentar el artículo de la '
            'temperatura de conservación como la regla de toda la vitrina.',
            'PROHIBIDO calcular la vida útil: la declara el operador en su '
            'sistema de autocontrol.',
        ],
    },
    {
        'n': 17,
        'titulo': 'El Equipo: Cuántos, Qué Perfiles y Qué Cuestan',
        'resumen_indice': 'los tres perfiles del obrador con los nombres del kit, el salto del bruto al coste de empresa, la prueba de que no existe convenio estatal del chocolate y el método para identificar el tuyo.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector vea el salto de bruto a coste de empresa '
                    'antes de contratar, que sepa qué convenio le aplica y '
                    'cómo buscarlo, y que entienda por qué el coste de la hora '
                    'de obrador afecta a todos los escandallos del pack.',
        'epigrafes': list(PPE_17),
        'puntos_por_epigrafe': PPE_17,
        'puntos_globales': [
            'Los perfiles literales son Chocolatero, Dependiente y Encargado, '
            'que son los nombres de hoja del Kit de Tareas Chocolatería. '
            '«Maestro chocolatero», «bombonero» y «oficial» son etiquetas de '
            'otras fuentes y NUNCA nombres de puesto de esta plantilla.',
            'La tabla salarial que aparece es la de UNA comunidad autónoma, '
            'marcada como EJEMPLO y sustituible. No se publica ninguna otra.',
            'Los salarios de mercado por hora van AL LADO de la tabla del '
            'convenio, nunca dentro, y con su fiabilidad a la vista: son '
            'orientativos y no son un convenio.',
        ],
        'cifras': [
            C('Coste de personal del año de crucero', f'{X_PLAN}!Personal!I9', 'eur'),
            C('Jornadas completas equivalentes de la plantilla', f'{X_PLAN}!Personal!B41', 'num1'),
            C('Coste de una hora de obrador', f'{X_PLAN}!Personal!B45', 'eur2'),
            C('Peso del coste de personal sobre las ventas', f'{X_PLAN}!PyG 3 Años!C46', 'pct1'),
            C('Referencia anual del salario mínimo', f'{X_PLAN}!Personal!B22', 'eur'),
            C('Bruto mensual del grupo de convenio más bajo', f'{X_CAMP}!Parámetros!B19', 'eur2'),
            C('Pagas al año del convenio de referencia', f'{X_CARTA}!Parámetros!B11', 'num'),
            C('Cotización a cargo de la empresa sobre el bruto', f'{X_CARTA}!Parámetros!B12', 'pct0'),
            C('Coste por hora pagada del personal de refuerzo de campaña', f'{X_CAMP}!Parámetros!B23', 'eur2'),
        ],
        'sector': ['CHN-65', 'CHN-65b', 'CHN-65c', 'CHN-66', 'CHN-93',
                   'CHN-67', 'CHN-68', 'CHN-69', 'CHS-69a', 'CHS-69b',
                   'CHS-69c', 'CHS-69d', 'CHS-70'],
        'tablas': [
            {
                'titulo': 'La plantilla del caso modelado, del bruto al coste de empresa (plan-financiero-3-anos-chocolateria.xlsx, hoja «Personal»)',
                'src': (X_PLAN, 'Personal'),
                'cols': [('Persona y perfil', 'A', 'txt'), ('Jornada', 'C', 'num1'),
                         ('Grupo de convenio', 'D', 'txt'),
                         ('Bruto mes del puesto (€)', 'F', 'eur2'),
                         ('Coste mes (€)', 'H', 'eur2'),
                         ('Coste año (€)', 'I', 'eur')],
                'filas': (6, 9),
                'nota': 'Tres personas y dos jornadas y media: el Dependiente entra a media '
                        'jornada. Los nombres de perfil son los literales del Kit de Tareas '
                        'Chocolatería, para que el kit y la guía hablen el mismo idioma.',
            },
            {
                'titulo': 'Los grupos del convenio de referencia, marcado como ejemplo y sustituible (plan-financiero-3-anos-chocolateria.xlsx, hoja «Personal»)',
                'src': (X_PLAN, 'Personal'),
                'cols': [('Grupo', 'A', 'txt'), ('Denominación del grupo', 'B', 'txt'),
                         ('Bruto mes (€)', 'E', 'eur2'),
                         ('Bruto año (€)', 'F', 'eur'),
                         ('Áreas funcionales', 'G', 'txt')],
                'filas': (13, 18),
                'nota': 'Es la tabla de UNA comunidad autónoma y está marcada como ejemplo: '
                        'sustitúyela por la del convenio que te aplique. No existe convenio '
                        'estatal del chocolate. ' + V_CONVENIO,
            },
            {
                'titulo': 'Salarios de mercado, orientativos y con su etiqueta de fuente (plan-financiero-3-anos-chocolateria.xlsx, hoja «Personal»)',
                'src': (X_PLAN, 'Personal'),
                'cols': [('Etiqueta de la fuente salarial', 'A', 'txt'),
                         ('Mínimo (€/h)', 'B', 'num2'),
                         ('Máximo (€/h)', 'C', 'num2'),
                         ('Equivale a', 'D', 'txt'),
                         ('Coste año a jornada completa (€)', 'E', 'eur')],
                'filas': (27, 30),
                'nota': 'Las etiquetas de la primera columna son de la FUENTE salarial, no '
                        'perfiles de esta plantilla: por eso van entrecomilladas y con su '
                        'equivalencia al lado. Son orientativos y NO son una tabla de '
                        'convenio.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir que existe un convenio estatal del chocolate, '
            'y PROHIBIDA cualquier tabla salarial distinta de la de ejemplo.',
            'PROHIBIDO usar «maestro chocolatero», «bombonero» u «oficial» '
            'como nombre de puesto de la plantilla.',
            'PROHIBIDO presentar los salarios de mercado por hora como una '
            'tabla de convenio.',
            'PROHIBIDO dar una fecha de reforma del registro de jornada '
            'digital: a la fecha de corte no hay norma publicada.',
        ],
    },
    {
        'n': 18,
        'titulo': 'Las Campañas y el Valle: de Navidad a Agosto',
        'resumen_indice': 'el peso de un solo evento, la producción de Navidad que se paga en octubre, las comuniones como campaña propia, por qué en agosto para el obrador y no la caja, y las dos respuestas contraestacionales.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector sepa de qué vive en julio y en agosto, qué '
                    'campaña le da de verdad dinero y cuál sólo le da trabajo, '
                    'y cuánta tesorería tiene que tener provisionada antes de '
                    'la campaña grande.',
        'epigrafes': list(PPE_18),
        'puntos_por_epigrafe': PPE_18,
        'puntos_globales': [
            'El calendario de campañas con sus fechas, acciones y productos '
            'destacados es del Kit de Tareas Chocolatería y NO se repite aquí: '
            'este capítulo sólo narra los euros.',
            'El valle es AGOSTO, un mes de doce, y lo que para es el obrador. '
            'La tienda sigue abierta y sigue facturando menos, no cero. Los '
            'envíos son una decisión de canal online aparte.',
            'Toda la capacidad se cuenta en bombones equivalentes de obrador, '
            'que no son las piezas de venta: una caja es una venta y muchos '
            'bombones.',
        ],
        'cifras': [
            C('Facturación sin IVA de la campaña de Navidad', f'{X_CAMP}!Calendario de Campañas!N18', 'eur'),
            C('Resultado incremental de la campaña de Navidad', f'{X_CAMP}!Refuerzo y Tesorería!N18', 'eur'),
            C('Resultado incremental de las doce campañas del año', f'{X_CAMP}!Refuerzo y Tesorería!N19', 'eur'),
            C('Tesorería inmovilizada en moldes y packaging de temporada', f'{X_CAMP}!Refuerzo y Tesorería!J19', 'eur'),
            C('Coste del refuerzo de personal de todo el año', f'{X_CAMP}!Refuerzo y Tesorería!E19', 'eur'),
            C('Campañas que el obrador no aguanta sin adelantar producción', f'{X_CAMP}!Capacidad vs Demanda del Pico!B26', 'num'),
            C('Ventas de agosto sin IVA', f'{X_CAMP}!Peso sobre el Año!E14', 'eur'),
            C('Resultado de agosto', f'{X_CAMP}!El Valle de Agosto!B20', 'eur'),
            C('Lo que cuesta agosto frente a un mes medio', f'{X_CAMP}!El Valle de Agosto!B22', 'eur'),
            C('Veredicto de agosto', f'{X_CAMP}!El Valle de Agosto!B23', 'txt'),
        ],
        'sector': ['CHS-34', 'CHS-35', 'CHS-36', 'CHS-30', 'CHS-55', 'CHS-10'],
        'tablas': [
            {
                'titulo': 'Las doce campañas del año y lo que factura cada una (campanas-y-valle-del-ano.xlsx, hoja «Calendario de Campañas»)',
                'src': (X_CAMP, 'Calendario de Campañas'),
                'cols': [('Mes', 'A', 'txt'),
                         ('Temporada que declara el kit', 'B', 'txt'),
                         ('Campaña', 'C', 'txt'),
                         ('¿Campaña propia?', 'D', 'txt'),
                         ('Días de campaña', 'J', 'num'),
                         ('Facturación sin IVA (€)', 'N', 'eur'),
                         ('Facturación INCREMENTAL sin IVA (€)', 'O', 'eur')],
                'filas': (7, 19),
                'nota': 'Las fechas, las acciones clave y los productos destacados son del Kit '
                        'de Tareas Chocolatería y no se repiten aquí. La diferencia entre las '
                        'dos últimas columnas es lo que de verdad añade la campaña: parte de '
                        'lo que vendes esos días lo habrías vendido igual.',
            },
            {
                'titulo': 'Lo que cuesta cada campaña antes de cobrarla (campanas-y-valle-del-ano.xlsx, hoja «Refuerzo y Tesorería»)',
                'src': (X_CAMP, 'Refuerzo y Tesorería'),
                'cols': [('Mes', 'A', 'txt'),
                         ('Personas de refuerzo', 'C', 'num'),
                         ('Coste del refuerzo (€)', 'E', 'eur'),
                         ('Inversión en moldes de temporada (€)', 'G', 'eur'),
                         ('Inversión en packaging de temporada (€)', 'I', 'eur'),
                         ('Resultado incremental (€)', 'N', 'eur')],
                'filas': (7, 19),
                'nota': 'Los moldes y el packaging de temporada se compran semanas antes de la '
                        'campaña: es dinero parado, y la hoja calcula lo que cuesta tenerlo '
                        'parado. El resultado incremental es lo que la campaña deja DESPUÉS '
                        'de pagar refuerzo, inmovilizado y financiación.',
            },
            {
                'titulo': 'El mes de agosto, en euros (campanas-y-valle-del-ano.xlsx, hoja «El Valle de Agosto»)',
                'src': (X_CAMP, 'El Valle de Agosto'),
                'cols': [('Concepto', 'A', 'txt'), ('Valor', 'B', 'eur'),
                         ('De dónde sale', 'D', 'txt')],
                'filas': (17, 23),
                'nota': 'Un agosto en negativo NO es motivo para cerrar: es una cifra que se '
                        'provisiona. Lo que para es el obrador; la tienda sigue abierta, con '
                        'otro mix y con turista.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir «valle de junio a agosto» o «un valle de tres '
            'meses», y PROHIBIDO escribir que los fijos siguen corriendo con '
            'la caja parada.',
            'PROHIBIDO repetir el calendario de tareas del Kit de Tareas '
            'Chocolatería: aquí sólo van los euros.',
            'PROHIBIDO dar una cifra de variación de mercado por campaña que '
            'no venga en los datos del sector.',
        ],
    },
    {
        'n': 19,
        'titulo': 'Canales: Mostrador, Envío, Hostelería, Corporativo y Talleres',
        'resumen_indice': 'los tres canales que se salen de la nota del epígrafe minorista y la pregunta exacta para el asesor, cuándo el suministro a hostelería te obliga a inscribirte, por qué vender online sigue siendo minorista, la obligación de registrar a quién vendes y los talleres como línea de agosto.',
        'palabras': 2100, 'bloques': 2,
        'objetivo': 'Que el lector sepa qué canal le cambia las obligaciones '
                    'antes de abrirlo, no después: qué tiene que preguntar a '
                    'su asesor y con qué redacción, qué le obliga a '
                    'inscribirse, qué papeles genera cada canal y cuál de '
                    'ellos deja de verdad margen.',
        'epigrafes': list(PPE_19),
        'puntos_por_epigrafe': PPE_19,
        'puntos_globales': [
            'Este capítulo NO emite ningún epígrafe de actividades económicas '
            'por canal: ninguna fuente lo da. Lo que se entrega es la pregunta '
            'redactada para el asesor, con la nota literal delante.',
            'Los porcentajes de reparto por canal del caso son SUPUESTOS '
            'declarados: lo que no es supuesto es que cada canal tiene su '
            'margen de contribución y sus obligaciones.',
            'El tipo impositivo del taller va SIN CIFRA: lo único cerrado es '
            'que no está exento.',
        ],
        'cifras': [
            C('Margen de contribución medio ponderado de los cinco canales', f'{X_PLAN}!Canales y Punto Muerto!B16', 'pct1'),
            C('Punto muerto mensual con todos los canales', f'{X_PLAN}!Canales y Punto Muerto!B19', 'eur'),
            C('Punto muerto mensual sin el canal de hostelería', f'{X_PLAN}!Canales y Punto Muerto!B20', 'eur'),
            C('Canal que sostiene el negocio', f'{X_PLAN}!Canales y Punto Muerto!B22', 'txt'),
            C('Canales que hay que consultar con el asesor', f'{X_PLAN}!Canales y Punto Muerto!B26', 'num'),
            C('Margen de contribución del canal online después del envío', f'{X_PLAN}!Canales y Punto Muerto!B39', 'pct1'),
            C('Veredicto del canal online', f'{X_PLAN}!Canales y Punto Muerto!B40', 'txt'),
            C('Asistentes necesarios para cubrir el coste del taller', f'{X_PLAN}!Talleres y Regalo Corporativo!B19', 'num1'),
            C('Margen por hora de sala dando taller', f'{X_PLAN}!Talleres y Regalo Corporativo!B26', 'eur2'),
            C('Margen por hora de sala vendiendo', f'{X_PLAN}!Talleres y Regalo Corporativo!B29', 'eur2'),
        ],
        'sector': ['CHN-41', 'CHN-56', 'CHN-57', 'CHN-59', 'CHN-60', 'CHN-24',
                   'CHN-72', 'CHN-94', 'CHN-95', 'CHN-96', 'CHN-71b',
                   'CHN-88', 'CHS-30', 'CHS-55', 'CHS-10'],
        'tablas': [
            {
                'titulo': 'Los cinco canales y lo que deja cada uno (plan-financiero-3-anos-chocolateria.xlsx, hoja «Canales y Punto Muerto»)',
                'src': (X_PLAN, 'Canales y Punto Muerto'),
                # ⚠️ El ORDEN de estas columnas no es estético: si la SEGUNDA
                # columna impresa fuese un porcentaje puro, `es_fila_porcentual()`
                # tomaría la fila entera por una fila de porcentajes y
                # reformatearía los euros y los días de cobro como tantos por
                # ciento (las ventas del canal saldrían como «123.434,5 %»).
                # Por eso la segunda columna es la de euros.
                'cols': [('Canal', 'A', 'txt'),
                         ('Ventas del año de crucero (€)', 'I', 'eur'),
                         ('% de las ventas', 'B', 'pct0'),
                         ('Margen bruto', 'C', 'pct0'),
                         ('Margen de contribución', 'H', 'pct1'),
                         ('Margen de contribución (€)', 'J', 'eur'),
                         ('Días de cobro', 'G', 'num')],
                'filas': (6, 11),
                'nota': 'El margen de contribución es lo que queda después de servir, cobrar y '
                        'enviar, que no es lo mismo que el margen bruto. Los días de cobro son '
                        'la otra mitad del problema: un canal con buen margen y cuarenta y '
                        'cinco días de cobro lo financias tú.',
            },
            {
                'titulo': 'Canal a canal: ¿te saca de la nota del epígrafe minorista? (checklist-legal-licencias-y-cacao.xlsx, hoja «Checklist Legal»)',
                'src': (X_LEGAL, 'Checklist Legal (F1-F6)'),
                'cols': [('Canal', 'B', 'txt'),
                         ('¿Vas a vender por él?', 'C', 'txt'),
                         ('¿Te saca de la nota?', 'D', 'txt'),
                         ('Fuente verificada', 'E', 'txt')],
                'filas': (74, 78),
                'nota': 'La columna del veredicto admite «no lo sé», y eso no es un fallo de '
                        'la hoja: es la respuesta honesta para tres de los cinco canales. La '
                        'hoja entrega además la pregunta redactada para llevársela al asesor. '
                        + V_IAE,
            },
            {
                'titulo': 'El taller, en números (plan-financiero-3-anos-chocolateria.xlsx, hoja «Talleres y Regalo Corporativo»)',
                'src': (X_PLAN, 'Talleres y Regalo Corporativo'),
                'cols': [('Concepto', 'A', 'txt'), ('Valor', 'B', 'num2'),
                         ('Unidad', 'C', 'txt')],
                'filas': (6, 16),
                'nota': 'El precio por persona y la duración son rango publicado de mercado; '
                        'el aforo, las horas de docente y el coste de materia por asistente '
                        'son supuestos declarados. El tipo impositivo del taller va sin cifra '
                        'a propósito: lo único cerrado es que no está exento.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir «con el epígrafe minorista puedes vender a '
            'hostelería, a empresas y por envío sin más», y PROHIBIDO dar un '
            'epígrafe de actividades económicas por canal como veredicto.',
            'PROHIBIDO escribir que un taller de bombonería está exento del '
            'impuesto sobre el valor añadido, y PROHIBIDO publicar un tipo '
            'impositivo para el taller.',
            'PROHIBIDO escribir «basta con registrar a tus proveedores»: hay '
            'que registrar también a quién suministras.',
            'PROHIBIDO decir que vender online cambia tu registro sanitario o '
            'que deja de ser comercio al por menor.',
        ],
    },
    {
        'n': 20,
        'titulo': 'El Plan Financiero, el Dinero Hasta el Punto de Equilibrio y los Primeros Noventa Días',
        'resumen_indice': 'la cuenta de resultados a tres años con rampa y estacionalidad, los dos puntos de equilibrio, el sueldo del propietario como renglón propio, impuesto y libertad horaria como decisiones del día uno, y qué se mide en el mes cero y en el mes tres.',
        'palabras': 1750, 'bloques': 1,
        'objetivo': 'Que el lector vea la rentabilidad real del proyecto y no '
                    'la que le gustaría: cuánto necesita facturar para no '
                    'perder dinero, cuánta holgura tiene, y qué cuatro cosas '
                    'tiene que medir desde el primer día para que el plan deje '
                    'de ser una previsión.',
        'epigrafes': list(PPE_20),
        'puntos_por_epigrafe': PPE_20,
        'puntos_globales': [
            'El año dos es el año de crucero, y todas las cifras de referencia '
            'del pack salen de esa columna. Se dice cada vez que se cita una.',
            'Ninguna cifra de este capítulo es una previsión de los resultados '
            'del lector: son las de una bombonería modelada con supuestos '
            'declarados, y viven en celdas editables para que las sustituya.',
            'El sueldo del titular está DENTRO de los costes. Un plan que se '
            'sostiene porque el dueño no cobra no se sostiene.',
        ],
        'cifras': [
            C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
            C('Margen bruto del año de crucero', f'{X_PLAN}!PyG 3 Años!C15', 'eur'),
            C('Total de costes fijos del año de crucero', f'{X_PLAN}!PyG 3 Años!C31', 'eur'),
            C('Resultado neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C41', 'eur'),
            C('Margen neto del año de crucero', f'{X_PLAN}!PyG 3 Años!E41', 'pct1'),
            C('Clientes al día necesarios para el equilibrio contable', f'{X_PLAN}!Punto de Equilibrio!C16', 'num1'),
            C('Ingresos mensuales necesarios para el equilibrio contable', f'{X_PLAN}!Punto de Equilibrio!C18', 'eur'),
            C('Holgura sobre el equilibrio de caja en el año de crucero', f'{X_PLAN}!Punto de Equilibrio!C26', 'pct1'),
            C('Cuota mensual del préstamo', f'{X_PLAN}!Financiación!B22', 'eur2'),
            C('Saldo mínimo de caja del primer año', f'{X_PLAN}!Tesorería 12 meses!B24', 'eur'),
        ],
        'sector': ['CHS-40', 'CHN-71', 'CHN-71c', 'CHN-73', 'CHN-74',
                   'CHN-74b', 'CHN-75', 'CHN-76', 'CHN-77', 'CHN-78'],
        'tablas': [
            {
                'titulo': 'La cuenta de resultados a tres años (plan-financiero-3-anos-chocolateria.xlsx, hoja «PyG 3 Años»)',
                'src': (X_PLAN, 'PyG 3 Años'),
                'cols': [('Concepto', 'A', 'txt'), ('Año 1 (arranque)', 'B', 'eur'),
                         ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur'),
                         ('% sobre ventas (año 2)', 'E', 'pct1')],
                'filas': (11, 34),
                'nota': 'El año 1 lleva rampa de arranque, así que sus ingresos no son los de '
                        'crucero. Los costes fijos casi no cambian entre años: es justo lo que '
                        'hace que el punto de equilibrio sea una cifra estable y el margen, no.',
            },
            {
                'titulo': 'Los tres escenarios, con los mismos costes fijos (plan-financiero-3-anos-chocolateria.xlsx, hoja «Escenarios»)',
                'src': (X_PLAN, 'Escenarios'),
                'cols': [('Métrica', 'A', 'txt'), ('Pesimista', 'B', 'eur'),
                         ('Realista', 'C', 'eur'), ('Optimista', 'D', 'eur')],
                'filas': (9, 16),
                'nota': 'Los dos extremos son supuestos y la columna central LEE el año de '
                        'crucero: no es un escenario aparte. Lo que hay que mirar antes de '
                        'firmar es la primera columna, no la tercera.',
            },
            {
                'titulo': 'Qué se mide el mes cero y qué se mide el mes tres',
                'cabecera': ['Qué se mide', 'Cuándo', 'Con qué', 'Qué celda del pack sustituye'],
                'filas': [
                    ['Ticket medio sin impuesto', 'Desde el primer día', 'Punto de venta, media de dos semanas completas', 'El supuesto de ticket medio del plan financiero'],
                    ['Piezas por ticket', 'Desde el primer día', 'Punto de venta', 'El supuesto de piezas por ticket'],
                    ['Mix por familia', 'Mes uno', 'Ventas por referencia del punto de venta', 'El mix de la hoja de carta, que recalcula el food cost'],
                    ['Peso de cada canal', 'Mes tres', 'Facturación por canal', 'El reparto por canal del plan financiero'],
                    ['Merma real, recuperable y no recuperable', 'Mes tres', 'Pesada del recorte al cerrar el obrador', 'Las dos tasas de merma del libro de escandallo'],
                    ['Referencias que no rotan', 'Mes tres', 'Ventas por referencia', 'La decisión de surtido: revisar precio o retirar'],
                ],
                'nota': 'Al mes tres se sustituyen los supuestos por lo medido y se vuelve a '
                        'leer el punto muerto. A partir de ahí el plan deja de ser una '
                        'previsión y pasa a ser un cuadro de mando.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO usar el punto de equilibrio de un escenario publicado '
            'por un tercero como cifra de portada.',
            'PROHIBIDO decir que la facturación verificable es obligatoria '
            'este año, y PROHIBIDO dar una fecha concreta para el fabricante '
            'del programa.',
            'PROHIBIDO escribir que una chocolatería tiene libertad horaria '
            'por el artículo que casi todos citan: le viene por el siguiente, '
            'por superficie.',
            'PROHIBIDO escribir que hay que pedir permiso para abrir en '
            'domingo.',
        ],
    },
    {
        'n': 21,
        'titulo': 'Anexo normativo, actualizado a 12 de septiembre de 2026',
        # D45: va como entrada 21 para que el pipeline lo escriba, pero NO se
        # numera como capítulo. La portada dice «veinte capítulos + anexo».
        'sin_numerar': True,
        'resumen_indice': 'qué sigue vigente y qué está derogado con fecha de corte, las fechas que ya sabemos que se mueven, las normas cuyo cambio invalidaría algo del pack y cómo comprobar una vigencia en un minuto.',
        'palabras': 1500, 'bloques': 1,
        'objetivo': 'Que el lector pueda comprobar por su cuenta, dentro de un '
                    'año, qué sigue vigente de todo lo que ha leído: estado '
                    'norma a norma con fecha de corte, las fechas que ya '
                    'sabemos que se mueven, y cómo se comprueba una vigencia '
                    'en un minuto.',
        'epigrafes': list(PPE_21),
        'puntos_por_epigrafe': PPE_21,
        'puntos_globales': [
            'Este anexo NO se numera como capítulo y no introduce ninguna '
            'afirmación nueva: todo lo que aparece aquí ya se ha dicho en un '
            'capítulo, y aquí sólo se da su estado.',
            'Aquí no entra ninguna cifra de sector, ningún precio y ningún '
            'dato de mercado: sólo normas, artículos, fechas y umbrales '
            'normativos.',
            'La fecha de corte se repite al principio y al final: es lo que '
            'convierte este anexo en útil dentro de un año.',
        ],
        'cifras': [
            C('Chocolate mínimo sobre el peso total del bombón', f'{X_CARTA}!Denominaciones y Mínimos!B38', 'pct0'),
            C('Materia seca total de cacao mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B39', 'pct0'),
            C('Manteca de cacao mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B40', 'pct0'),
            C('Materia seca desgrasada mínima del chocolate a la taza', f'{X_CARTA}!Denominaciones y Mínimos!B41', 'pct0'),
            C('Umbral de la primera vía de marginalidad, sobre el volumen anual', f'{X_LEGAL}!Suministro a Otros Minoristas!B20', 'pct0'),
            C('Umbral de la segunda vía de marginalidad, en kilos a la semana', f'{X_LEGAL}!Suministro a Otros Minoristas!B23', 'num'),
            C('Tope absoluto de kilos a la semana del obrador en vivienda', f'{X_LEGAL}!Ruta Doméstica!B23', 'num'),
            C('Umbral estatal de superficie de la licencia previa de actividad', f'{X_CAP}!Parámetros!B24', 'num'),
            C('Umbral mensual de la exención del impuesto al plástico', f'{X_CAPEX}!Parámetros!B20', 'num'),
            C('Referencia anual del salario mínimo', f'{X_PLAN}!Personal!B22', 'eur'),
        ],
        'sector': ['CHN-01', 'CHN-14', 'CHN-36', 'CHN-39', 'CHN-44',
                   'CHN-49', 'CHN-62', 'CHN-64', 'CHN-65c', 'CHN-67',
                   'CHN-75', 'CHN-76', 'CHN-77', 'CHN-78', 'CHN-86'],
        'tablas': [
            {
                'titulo': 'Estado de vigencia norma a norma, con fecha de corte de 12-09-2026',
                'cabecera': ['Norma', 'Qué sostiene en esta guía', 'Estado comprobado el 12-09-2026'],
                'filas': [
                    ['RD 1055/2003 (BOE-A-2003-15599)', 'Qué puedes llamar chocolate, bombón, cobertura de chocolate y chocolate a la taza, y con qué mínimos', 'Vigente, SIN una sola modificación desde 2003'],
                    ['Directiva 2000/36/CE', 'La definición europea de bombón y praliné, y la cláusula de armonización total', 'Vigente; sus porcentajes no se han tocado desde el año 2000'],
                    ['RD 348/2011', 'Confites, grageas y fruta bañada en chocolate', 'Vigente, sin modificaciones'],
                    ['Reglamento (UE) 2023/915', 'Cadmio, ocratoxina A e hidrocarburos aromáticos policíclicos en cacao y chocolate', 'Vigente; la nota que define «producto de cacao y de chocolate» remite sólo a tres puntos de la directiva'],
                    ['Reglamento (UE) 2023/1115', 'Diligencia debida del cacao, papeles del proveedor y registro de clientes', 'Vigente y MUY vivo: dos modificaciones y una corrección de errores en doce meses'],
                    ['RD 1021/2022 (BOE-A-2022-21681)', 'Registro del minorista, suministro a otras tiendas, temperaturas, obrador en vivienda y autocontrol', 'Vigente; no nombra el chocolate ni una sola vez'],
                    ['RD 191/2011, art. 2.2', 'La exclusión del registro general para el minorista', 'Vigente, en la redacción de la disposición final primera del RD 1021/2022'],
                    ['Reglamento (CE) 852/2004', 'Higiene, alérgenos de proceso y formación del personal', 'Vigente, en la redacción del Reglamento (UE) 2021/382'],
                    ['Reglamento (UE) 1169/2011', 'Menciones obligatorias del producto envasado y venta a distancia', 'Vigente; el lote NO está entre sus doce menciones'],
                    ['RD 126/2015', 'Alérgenos e información en producto no envasado', 'Vigente, sin modificaciones'],
                    ['RD 1808/1991 (BOE-A-1991-30678)', 'El lote y sus tres exenciones', 'Vigente, sin modificaciones'],
                    ['Reglamento de Ejecución (UE) 828/2014', 'El umbral analítico del sin gluten', 'Vigente'],
                    ['Ley 12/2012 (BOE-A-2012-15595)', 'Que no te puedan exigir licencia previa de actividad por debajo del umbral de superficie', 'Vigente; su Anexo lista el epígrafe minorista de bombones y caramelos'],
                    ['RDLeg 1175/1990', 'El epígrafe minorista, su nota de fabricación y las reglas de la Instrucción', 'Vigente, última modificación de marzo de 2026'],
                    ['RD 100/2011', 'Catálogo de actividades potencialmente contaminadoras de la atmósfera, si tuestas grano', 'Vigente; ni «cacao» ni «chocolate» aparecen en él'],
                    ['Ley 37/1992, arts. 90 y 91', 'El tipo impositivo del chocolate y el de la taza servida', 'Vigente, última modificación de febrero de 2026'],
                    ['Ley 7/2022 (BOE-A-2022-5809)', 'Impuesto sobre envases de plástico no reutilizables', 'Vigente, última modificación de abril de 2025'],
                    ['RD 1055/2022', 'Envases de servicio, recipiente del cliente y bebida reutilizable', 'Vigente, sin modificaciones'],
                    ['Ley 1/2025', 'Desperdicio alimentario', 'Vigente; el art. 6.6 deja a la microempresa fuera de todo el art. 6, y el art. 8 NO queda excluido'],
                    ['RD 1007/2023', 'Facturación verificable', 'Vigente; sus plazos son de 2027, no de este año'],
                    ['Ley 1/2004, art. 5.2', 'Libertad horaria por superficie', 'Vigente, última modificación de octubre de 2014'],
                    ['Ley 7/1996, art. 20', 'La regla de los treinta días del precio anterior', 'Vigente, en la redacción del RD-ley 24/2021'],
                    ['RD 193/2023', 'Accesibilidad', 'Vigente; calendario privado en 2029 y 2030'],
                    ['RD 919/2006, ITC-ICG 07', 'Inspección periódica de la instalación de gas, sólo si montas freidora de gas', 'Vigente, última modificación de septiembre de 2025'],
                    ['RD 10/2025', 'Los dos códigos de actividad que se comunican en el alta', 'Vigente, sin modificaciones'],
                    ['Decreto 85/2024 de la Generalitat de Catalunya', 'Artesanía alimentaria, con el chocolate expresamente dentro', 'En vigor; la acreditación es VOLUNTARIA'],
                    ['RD 1334/1999', 'Etiquetado general, que la norma del chocolate todavía cita', 'Superado por el reglamento europeo de información al consumidor y por el RD 126/2015: no se remite a él'],
                    ['RD 1254/1991', 'Huevo y ovoproductos', 'DEROGADO; sigue citándose en contenidos que circulan'],
                    ['RD 3484/2000', 'Comidas preparadas', 'DEROGADO'],
                    ['RD 202/2000', 'Manipuladores de alimentos', 'DEROGADO: el carnet de manipulador no existe'],
                ],
                'nota': 'Comprobado el 12 de septiembre de 2026 contra los textos consolidados '
                        'oficiales. Sólo se ha verificado el estado de una comunidad autónoma '
                        'en materia de artesanía alimentaria, así que ese cuadro no es '
                        'completo: comprueba el registro de la tuya.',
            },
            {
                'titulo': 'Las fechas que ya sabemos que se mueven, y qué hay que rehacer con cada una',
                'cabecera': ['Qué cambia', 'Fecha conocida', 'Qué hay que rehacer cuando llegue'],
                'filas': [
                    ['Fecha general de la norma del cacao para quien no es operador aplazado', '30 de diciembre de 2026', 'La hoja de tu papel en la cadena y la documentación que pides a cada proveedor'],
                    ['Derogación de la norma europea anterior de diligencia debida', '30 de diciembre de 2026', 'Las referencias normativas de tus contratos de compra'],
                    ['Salario mínimo del año y tabla del convenio de referencia', '31 de diciembre de 2026', 'Los parámetros de convenio de la hoja de personal del plan financiero'],
                    ['Fin del aplazamiento de los operadores establecidos antes del corte', '30 de junio de 2027', 'Nada tuyo si compras cobertura: ese aplazamiento no está escrito para ti'],
                    ['Facturación verificable para sociedades', '1 de enero de 2027', 'El apartado de punto de venta del capítulo financiero'],
                    ['Facturación verificable para el resto de obligados', '1 de julio de 2027', 'El mismo apartado, con la fecha que corresponda a tu forma jurídica'],
                    ['Bebida en envase reutilizable por debajo del umbral de superficie', '1 de enero de 2027', 'El apartado de envases: la obligación pasa de futura a presente'],
                    ['Accesibilidad de bienes y servicios privados nuevos', '1 de enero de 2029', 'La ficha de visita a local y el capítulo del local'],
                    ['Accesibilidad de bienes y servicios privados ya existentes', '1 de enero de 2030', 'Lo mismo, para quien haya abierto antes'],
                ],
                'nota': 'Todas estas cifras viven en celda de parámetro en los libros de '
                        'Excel, nunca cosidas en el texto: por eso una edición nueva se arregla '
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
# BONUS 1 — `business-plan-modelo-chocolateria` (SPEC §4.2)
#
# El caso completo de «La Almendra» CON CIFRAS, en el formato que pide un
# banco o una línea de financiación pública: seis secciones, 3.500 palabras y
# ONCE tablas, todas construidas desde el libro 7 y, donde toca, desde el 4, el
# 3, el 2 y el 1, celda a celda.
#
# ⚠️ POR QUÉ SON SEIS ENTRADAS Y NO UNA (decisión de construcción, declarada):
# `documentos.py` sólo admite bonus con `capitulos`, y el gate exige 1-3 tablas
# POR CAPÍTULO. Con las seis secciones metidas en una sola entrada, el
# documento no podría pasar de tres tablas y el entregable exige NUEVE como
# mínimo (§2.1). Por eso cada sección es una entrada de un bloque, igual que en
# el guion de la hermana: seis bloques de redactor en vez de uno, y el recuento
# de la D50 pasa de 40 a 45 bloques. Es la única desviación de esa decisión, y
# se hace para que el documento pueda entregar lo que promete.
#
# DEFECTO HEREDADO QUE AQUÍ NO SE REPITE (B2 de la refutación de Pastelería):
# el resumen ejecutivo DA el resultado neto, el margen y el punto de
# equilibrio. No remite a la sección financiera: un banco lee la primera página
# y decide si sigue leyendo.
# ==========================================================================

PPE_BP1 = {
    'El proyecto en una página': [
        'Abrir con la ficha del proyecto: qué se monta, dónde, con qué '
        'superficie y con qué plantilla, en cinco líneas y sin adjetivos. Un '
        'banco lee esto y decide si sigue leyendo.',
        'Dar el formato exacto: bombonería artesanal con obrador propio y '
        'tienda a calle, en ciudad media, con los metros repartidos entre '
        'obrador, cámara de chocolate, almacén, envasado, tienda y servicios.',
    ],
    'La inversión y su financiación': [
        'Dar la inversión sin el fondo de maniobra, el fondo, la inversión '
        'total y la necesidad total de caja al arranque, y explicar en una '
        'frase la diferencia entre las cuatro: lo que se compra, lo que se '
        'reserva, la suma y lo que sale de la cuenta el día de la firma.',
        'Dar el reparto entre recursos propios y préstamo, y decir '
        'expresamente qué parte del desembolso es impuesto que se recupera '
        'después.',
    ],
    'El resultado, el margen y el punto de equilibrio': [
        'DARLOS AQUÍ, no remitir a la sección financiera: ingresos del año de '
        'crucero, resultado neto y margen neto. Es lo que decide si la primera '
        'página convence.',
        'Y el punto de equilibrio en la misma página: cuántos ingresos al mes '
        'hacen falta para no perder dinero, y qué holgura hay sobre lo '
        'previsto. Un plan que no dice su punto muerto en la primera página '
        'obliga al lector a buscarlo, y el lector no busca.',
    ],
    'Qué se pide y para qué': [
        'Decir con todas las letras qué se solicita, a qué plazo y para qué '
        'partidas. Un plan que no pide nada concreto no es un plan, es una '
        'presentación.',
        'Cerrar con la frase de trazabilidad que da credibilidad a todo lo '
        'demás: cada cifra de este documento sale de una celda de las '
        'herramientas del pack, y se puede abrir y comprobar una a una.',
    ],
}

PPE_BP2 = {
    'El mercado y su dirección': [
        'Dar el tamaño del mercado español de cacao y chocolate con su fuente '
        'y su año, y la lectura que importa: crece en valor y no en volumen.',
        'Sacar la consecuencia para este proyecto: se entra por producto y por '
        'ocasión de compra, no por precio ni por volumen.',
    ],
    'La plaza y el cliente': [
        'Describir la plaza sin inventar datos: ciudad media, tienda a calle, '
        'y el método con el que se ha validado —contar obradores con '
        'elaboración propia en el radio de caminata—, porque no existe censo '
        'de chocolaterías.',
        'Dar el perfil de compra del caso: clientes al día, piezas por ticket '
        'y ticket medio, y decir que ese ticket lo produce el mix de la carta.',
    ],
    'La estacionalidad de la demanda': [
        'Dar la curva del año con el mes más alto y el más bajo, y su peso '
        'sobre las ventas. Un negocio con esa curva se planifica por '
        'tesorería, no por media mensual.',
        'Dar el peso de las campañas sobre el año y decir qué parte de eso es '
        'incremental: no todo lo que se vende en campaña es venta nueva.',
    ],
    'Las barreras de entrada': [
        'Nombrar las que de verdad protegen a este negocio: el oficio del '
        'templado, la inversión en clima y frío, y la cartera de pedidos '
        'corporativos, que tarda en construirse.',
        'Y la que no protege: la marca. En bombonería la marca se construye '
        'con años de campañas, así que el plan no la usa como supuesto de '
        'ingresos.',
    ],
}

PPE_BP3 = {
    'El concepto y la carta': [
        'Describir el concepto en dos frases y la carta en cifras: número de '
        'referencias, cinco familias y a qué juega cada una.',
        'Dar el precio medio ponderado de la carta y el ticket medio, y decir '
        'que ambos salen del mix, no de una media del sector.',
    ],
    'El margen de la carta': [
        'Dar el food cost de escandallo y el food cost servido, y explicar en '
        'una línea por qué son dos cifras distintas: la segunda incluye '
        'packaging y merma, y es la que va al plan financiero.',
        'Dar el margen bruto medio del año y decir contra qué regla se '
        'compara: la regla única de margen del proyecto.',
    ],
    'La decisión de surtido': [
        'Dar el reparto de referencias por veredicto —mantener, revisar precio '
        'y retirar— y explicar los dos umbrales que lo producen: margen mínimo '
        'por pieza y rotación mínima.',
        'Dar el margen anual de toda la carta y decir qué familia lo aporta: '
        'es la cifra que un banco usa para entender de dónde sale el margen '
        'bruto de la cuenta de resultados.',
    ],
    'La materia prima y su riesgo': [
        'Dar el precio de las coberturas en base imponible y la parte del '
        'coste de materia que representa la cobertura. Es la exposición real '
        'del proyecto al precio del cacao.',
        'Y decir cómo se gestiona, sin dramatizar: escenarios de precio '
        'calculados, cuatro caminos de respuesta y una referencia identificada '
        'como la primera que se rompe.',
    ],
}

PPE_BP4 = {
    'El local y sus zonas': [
        'Dar la superficie total y el reparto por zonas, con el porcentaje '
        'dedicado a producción, y decir por qué en este negocio la producción '
        'pesa más que la venta.',
        'Dar la comprobación de marcha adelante como garantía de que el plano '
        'funciona: la cobertura entra por el almacén y el producto acabado '
        'sale a la tienda sin volver atrás.',
    ],
    'El clima, que en este oficio es una partida': [
        'Explicar en dos frases por qué la climatización con deshumidificación '
        'tiene bloque propio en la inversión: sin ventana de temperatura y '
        'humedad estable no hay templado fiable, y sin templado fiable no hay '
        'producto.',
        'Y decir qué NO se ha calculado y por qué: no hay coeficientes con '
        'fuente pública para un obrador de chocolate, así que el proyecto '
        'trabaja con la potencia ofertada por el instalador y un semáforo de '
        'coherencia, no con una carga térmica inventada.',
    ],
    'La capacidad del obrador': [
        'Dar los bombones equivalentes al día que pide el plan y los que '
        'permite el conjunto de equipos, y nombrar el equipo que limita. Es la '
        'cifra que dice si el plan de ventas es ejecutable.',
        'Dar la holgura sobre el día normal y explicar qué pasa en campaña: el '
        'pico no se cubre con máquina, se cubre adelantando producción de lo '
        'que aguanta.',
    ],
    'La plantilla': [
        'Dar las personas, las jornadas equivalentes y el coste anual de '
        'personal, con los tres perfiles nombrados.',
        'Dar el coste de una hora de obrador y decir para qué sirve: es la '
        'cifra que entra en todos los escandallos del proyecto.',
    ],
}

PPE_BP5 = {
    'La cuenta de resultados a tres años': [
        'Dar ingresos, margen bruto, costes fijos y resultado neto de los tres '
        'años, y explicar la rampa del primero.',
        'Dar el peso del personal sobre las ventas y el del alquiler, que son '
        'los dos ratios que un analista mira primero en un negocio con tienda.',
    ],
    'La tesorería del primer año': [
        'Dar el saldo mínimo de caja del primer año y el mes en el que la caja '
        'toca fondo. Es el dato que justifica el fondo de maniobra.',
        'Dar el saldo al cierre del mes doce y decir qué lo produce: el fondo '
        'inicial más el resultado del año, menos el servicio de la deuda.',
    ],
    'La financiación y su servicio': [
        'Dar el principal, la cuota mensual y el ratio de cobertura del '
        'servicio de la deuda en su punto más bajo. Un banco mira ese ratio '
        'antes que el beneficio.',
        'Decir qué parte de la cuota es gasto y qué parte no: sólo los '
        'intereses van a la cuenta de resultados, y la devolución del '
        'principal sale de la caja.',
    ],
    'El punto de equilibrio': [
        'Dar los dos puntos de equilibrio, el contable y el de caja, con sus '
        'clientes al día y sus ingresos al mes, y explicar por qué el segundo '
        'es más alto.',
        'Dar la holgura sobre lo previsto y leerla sin adornos: es cuánto '
        'puede caer el proyecto antes de empezar a consumir caja.',
    ],
}

PPE_BP6 = {
    'Los tres escenarios': [
        'Dar el resultado neto en el escenario pesimista, en el realista y en '
        'el optimista, y decir que los tres comparten los MISMOS costes fijos: '
        'es lo que hace que el pesimista duela tanto.',
        'Leer el pesimista como lo que es: la pregunta que hay que saber '
        'responder antes de firmar, no un ejercicio de prudencia decorativo.',
    ],
    'El riesgo de materia prima': [
        'Dar lo que costaría al año una subida fuerte del precio del cacao y '
        'el margen neto que quedaría después. Es el riesgo específico de este '
        'oficio y el que más fácil se cuantifica.',
        'Dar la respuesta prevista en cuatro palancas —precio, gramaje, '
        'cobertura y margen— y decir cuál se activa primero.',
    ],
    'El riesgo de estacionalidad': [
        'Dar el resultado del mes de agosto y lo que cuesta frente a un mes '
        'medio, y decir que es una cifra que se provisiona, no una sorpresa.',
        'Dar las campañas que el obrador no aguanta sin adelantar producción y '
        'explicar la palanca: adelantar lo que aguanta, reforzar con personal '
        'temporal y cerrar pedidos con fecha límite.',
    ],
    'El riesgo regulatorio y el de ejecución': [
        'Nombrar el regulatorio con precisión y sin alarmismo: la norma '
        'europea del cacao se ha modificado tres veces en doce meses, y el '
        'proyecto lleva dentro una fecha de revisión y un papel definido en la '
        'cadena.',
        'Y el de ejecución, que es el más probable: el plazo de entrega de la '
        'maquinaria crítica frente a la ruta crítica del expediente. El '
        'proyecto lo cuadra y publica el margen entre los dos.',
    ],
}

BONUS = [
    {
        'nombre': 'business-plan-modelo-chocolateria',
        'guia': {
            'titulo': 'Business Plan Modelo de una Chocolatería',
            'subtitulo': 'Bonus del pack «Cómo Montar una Chocolatería» · el '
                         'caso completo relleno, con las cifras de las nueve '
                         'herramientas Excel',
            'cabecera': 'AI Chef Pro · Business Plan Modelo de una Chocolatería',
            'tipo_doc': 'documento',
            'tipo_doc_art': 'del business plan',
            'tipo_doc_dem': 'este documento',
            'categoria_doc': 'Plantilla profesional',
            'portada_texto': (
                'El plan de negocio de una bombonería modelada, relleno de '
                'principio a fin y en el formato que pide un banco o una línea '
                'de financiación pública: resumen ejecutivo, mercado y plaza, '
                'concepto y carta, plan de operaciones, plan financiero a tres '
                'años y análisis de riesgos con escenarios. Todas las cifras '
                'salen de las nueve herramientas Excel del pack, así que '
                'puedes abrir la celda de la que sale cada una y sustituirla '
                'por la tuya. Es una plantilla rellena para que la copies, no '
                'una previsión de tus resultados.'),
        },
        'gates': {
            'paginas_prometidas': 9,
            'palabras_objetivo': 3500,
            'min_palabras_cap': 450,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': 'Business Plan Modelo de una Chocolatería',
                     'subject': 'Bonus del pack Cómo Montar una Chocolatería · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Resumen Ejecutivo',
                'resumen_indice': 'el proyecto en una página: qué se monta, cuánto cuesta, cómo se financia, qué resultado da y dónde está su punto de equilibrio.',
                'palabras': 700, 'bloques': 1,
                'objetivo': 'Que quien lee el plan sepa en una página qué '
                            'proyecto es, cuánto dinero necesita, de dónde '
                            'sale, qué deja y a partir de qué facturación deja '
                            'de perder. Sin adjetivos y sin promesas.',
                'epigrafes': list(PPE_BP1),
                'puntos_por_epigrafe': PPE_BP1,
                'puntos_globales': [
                    'Registro de documento de banco: frases cortas, cifras '
                    'delante y cero lenguaje comercial.',
                    'El resultado neto, el margen y el punto de equilibrio van '
                    'EN ESTA PÁGINA. No se remite a la sección financiera.',
                    'Cada cifra sale de una celda del pack y se puede abrir: '
                    'eso se dice una vez, al principio del documento.',
                ],
                'cifras': [
                    C('Inversión sin el fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B19', 'eur'),
                    C('Fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B16', 'eur'),
                    C('Inversión total', f'{X_PLAN}!Inversión Inicial!B21', 'eur'),
                    C('IVA soportado sobre la inversión', f'{X_PLAN}!Inversión Inicial!B22', 'eur'),
                    C('Necesidad total de caja al arranque', f'{X_PLAN}!Inversión Inicial!B23', 'eur'),
                    C('Recursos propios aportados', f'{X_PLAN}!0. Supuestos!B40', 'eur'),
                    C('Principal del préstamo solicitado', f'{X_PLAN}!0. Supuestos!B41', 'eur'),
                    C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
                    C('Resultado neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C41', 'eur'),
                    C('Margen neto del año de crucero', f'{X_PLAN}!PyG 3 Años!E41', 'pct1'),
                    C('Ingresos mensuales necesarios para el equilibrio contable', f'{X_PLAN}!Punto de Equilibrio!C18', 'eur'),
                ],
                'sector': ['CHS-03', 'CHS-18'],
                'tablas': [
                    {
                        'titulo': 'La inversión y la necesidad de caja al arranque (plan-financiero-3-anos-chocolateria.xlsx, hoja «Inversión Inicial»)',
                        'src': (X_PLAN, 'Inversión Inicial'),
                        'cols': [('Concepto', 'A', 'txt'), ('Importe (€)', 'B', 'eur')],
                        'filas': (19, 23),
                        'nota': 'La necesidad total de caja es la cifra que hay que cubrir el día '
                                'que se firma: incluye el impuesto que se adelanta y el fondo de '
                                'maniobra, que no es inversión pero sale de la cuenta.',
                    },
                    {
                        'titulo': 'Ingresos y margen bruto de los tres años (plan-financiero-3-anos-chocolateria.xlsx, hoja «PyG 3 Años»)',
                        'src': (X_PLAN, 'PyG 3 Años'),
                        'cols': [('Concepto', 'A', 'txt'), ('Año 1', 'B', 'eur'),
                                 ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                        'filas': (11, 15),
                        'nota': 'El año 2 es el de crucero y es la columna de referencia de todo '
                                'el plan. El año 1 va con rampa de arranque.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No adornes: un resumen ejecutivo con adjetivos es un '
                    'resumen ejecutivo que no se cree nadie.',
                    'No remitas a otra sección para dar el resultado, el '
                    'margen o el punto de equilibrio: van aquí.',
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
                    'Ninguna cifra de censo de chocolaterías ni de facturación '
                    'media: no existe dato fiable, y se dice.',
                ],
                'cifras': [
                    C('Ventas anuales sin IVA en velocidad de crucero', f'{X_CAMP}!Parámetros!B7', 'eur'),
                    C('Clientes al día en velocidad de crucero', f'{X_PLAN}!0. Supuestos!B6', 'num'),
                    C('Piezas por ticket', f'{X_PLAN}!0. Supuestos!B7', 'num1'),
                    C('Ticket medio sin IVA', f'{X_PLAN}!0. Supuestos!B10', 'eur2'),
                    C('Días de apertura al año', f'{X_PLAN}!0. Supuestos!B11', 'num'),
                    C('Peso del mes más alto sobre el año', f'{X_CAMP}!Peso sobre el Año!F18', 'pct1'),
                    C('Peso del mes más bajo sobre el año', f'{X_CAMP}!Peso sobre el Año!F14', 'pct1'),
                    C('Peso de las doce campañas sobre el año', f'{X_CAMP}!Peso sobre el Año!D35', 'pct1'),
                ],
                'sector': ['CHS-18', 'CHS-19', 'CHS-21', 'CHS-22', 'CHS-23',
                           'CHS-03'],
                'tablas': [{
                    'titulo': 'La curva de la demanda mes a mes (campanas-y-valle-del-ano.xlsx, hoja «Peso sobre el Año»)',
                    'src': (X_CAMP, 'Peso sobre el Año'),
                    'cols': [('Mes', 'A', 'txt'), ('Temporada', 'B', 'txt'),
                             ('Coeficiente', 'C', 'num2'),
                             ('Ventas del mes sin IVA (€)', 'E', 'eur'),
                             ('Parte del año (%)', 'F', 'pct1')],
                    'filas': (7, 19),
                    'nota': 'Los coeficientes son supuestos del caso modelado y suman doce, de '
                            'manera que la media coincide con la velocidad de crucero. La '
                            'temporada de cada mes es la que declara el calendario del kit de '
                            'tareas de la casa.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'No des ningún censo de chocolaterías ni ninguna '
                    'facturación media del sector.',
                ],
            },
            {
                'n': 3,
                'titulo': 'Concepto y Carta',
                'resumen_indice': 'el concepto y la carta en cifras, el margen que produce, la decisión de surtido y la exposición al precio de la materia prima.',
                'palabras': 550, 'bloques': 1,
                'objetivo': 'Que el lector del plan entienda qué se vende, a '
                            'qué precio, con qué margen y con qué riesgo de '
                            'materia prima, sin necesidad de leer el escandallo '
                            'completo.',
                'epigrafes': list(PPE_BP3),
                'puntos_por_epigrafe': PPE_BP3,
                'puntos_globales': [
                    'Las referencias son datos de ejemplo declarados del caso '
                    'modelado, no un surtido recomendado.',
                    'El food cost de escandallo y el food cost servido son dos '
                    'cifras distintas y se dice cuál es cuál cada vez que '
                    'aparecen.',
                ],
                'cifras': [
                    C('PVP medio ponderado de la carta con IVA', f'{X_CARTA}!Mix y Ticket Medio!B37', 'eur2'),
                    C('Food cost de escandallo de la carta', f'{X_CARTA}!Mix y Ticket Medio!B43', 'pct1'),
                    C('Food cost servido, el que va al plan financiero', f'{X_CARTA}!Mix y Ticket Medio!B46', 'pct1'),
                    C('Margen bruto medio con el mix del año', f'{X_CARTA}!Mix y Ticket Medio!B48', 'pct1'),
                    C('Referencias con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!B37', 'num'),
                    C('Referencias con veredicto de retirar', f'{X_CARTA}!Decisión de Surtido!B39', 'num'),
                    C('Margen de toda la carta al año', f'{X_CARTA}!Decisión de Surtido!G35', 'eur'),
                    C('Parte del coste de materia que es cobertura', f'{X_CACAO}!Coste de Cobertura!D47', 'pct1'),
                ],
                'sector': ['CHS-29', 'CHS-28a', 'CHS-28c', 'CHS-32'],
                'tablas': [
                    {
                        'titulo': 'La decisión de surtido de los diez bombones de colección (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Decisión de Surtido»)',
                        'src': (X_CARTA, 'Decisión de Surtido'),
                        'cols': [('Id', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                                 ('Margen por pieza (€)', 'D', 'eur2'),
                                 ('Margen sobre PVP', 'E', 'pct1'),
                                 ('Margen al año (€)', 'G', 'eur'),
                                 ('Veredicto', 'K', 'txt')],
                        'filas': (7, 16),
                        'nota': 'El veredicto sale de dos umbrales que fija el proyecto: margen '
                                'mínimo por pieza y rotación mínima sobre el mix.',
                    },
                    {
                        'titulo': 'Las cuatro coberturas y su precio en base imponible (sensibilidad-al-precio-del-cacao.xlsx, hoja «Coste de Cobertura»)',
                        'src': (X_CACAO, 'Coste de Cobertura'),
                        'cols': [('Cobertura', 'B', 'txt'),
                                 ('Formato de compra', 'C', 'txt'),
                                 ('Precio como lo trae la fuente (€/kg)', 'D', 'eur2'),
                                 ('Base declarada', 'E', 'txt'),
                                 ('Precio en base imponible (€/kg)', 'G', 'eur2')],
                        'filas': (7, 10),
                        'nota': 'El escandallo del proyecto usa SIEMPRE la columna de base '
                                'imponible: el precio de referencia de la cobertura de marca '
                                'viene declarado con impuesto incluido por su fuente.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No mezcles el food cost de escandallo con el food cost '
                    'servido sin decir cuál es cuál.',
                ],
            },
            {
                'n': 4,
                'titulo': 'Plan de Operaciones',
                'resumen_indice': 'el local y sus zonas, el clima como partida propia, la capacidad real del obrador y la plantilla que lo mueve.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Demostrar que el plan de ventas es ejecutable con '
                            'el local, el equipo y la plantilla previstos, y '
                            'que el proyecto sabe cuál es su cuello de botella '
                            'antes de abrir.',
                'epigrafes': list(PPE_BP4),
                'puntos_por_epigrafe': PPE_BP4,
                'puntos_globales': [
                    'La capacidad se cuenta en bombones equivalentes de '
                    'obrador, que no son piezas de venta: se dice la primera '
                    'vez que aparece.',
                    'Los metros por zona y las duraciones son supuestos '
                    'declarados del caso modelado.',
                ],
                'cifras': [
                    C('Superficie total del local', f'{X_CAP}!Parámetros!B16', 'num'),
                    C('Metros de zona de producción', f'{X_CAP}!Zonas y m2!D17', 'num'),
                    C('Parte del local dedicada a producción', f'{X_CAP}!Zonas y m2!D18', 'pct0'),
                    C('Bombones al día que pide el plan', f'{X_CAP}!Cuello de Botella!B6', 'num'),
                    C('Bombones al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
                    C('El equipo que limita', f'{X_CAP}!Cuello de Botella!B8', 'txt'),
                    C('Holgura sobre el día normal', f'{X_CAP}!Cuello de Botella!B10', 'pct1'),
                    C('Jornadas completas equivalentes de la plantilla', f'{X_PLAN}!Personal!B41', 'num1'),
                    C('Coste de personal al año', f'{X_PLAN}!Personal!I9', 'eur'),
                    C('Coste de una hora de obrador', f'{X_PLAN}!Personal!B45', 'eur2'),
                ],
                'sector': ['CHS-03', 'CHS-70', 'CHS-44'],
                'tablas': [
                    {
                        'titulo': 'Las seis zonas del local (capacidad-obrador-y-clima.xlsx, hoja «Zonas y m2»)',
                        'src': (X_CAP, 'Zonas y m2'),
                        'cols': [('Zona', 'B', 'txt'), ('Bloque', 'C', 'txt'),
                                 ('m2', 'D', 'num1'), ('% del local', 'E', 'pct1'),
                                 ('Paso del recorrido', 'F', 'num')],
                        'filas': (6, 11),
                        'nota': 'El recorrido va en un solo sentido: la cobertura entra por el '
                                'almacén y el producto acabado sale a la tienda sin volver atrás.',
                    },
                    {
                        'titulo': 'Capacidad equipo a equipo, y cuál limita (capacidad-obrador-y-clima.xlsx, hoja «Capacidad por Equipo»)',
                        'src': (X_CAP, 'Capacidad por Equipo'),
                        'cols': [('Equipo o puesto', 'B', 'txt'), ('Categoría', 'C', 'txt'),
                                 ('¿Lo tienes?', 'D', 'txt'),
                                 ('Bombones al día de obrador que permite', 'M', 'num')],
                        'filas': (6, 16),
                        'nota': 'El cuello de botella de una bombonería casi nunca es la máquina '
                                'de templar: son las manos y el puesto de envasado.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No presentes los metros por zona ni las duraciones como '
                    'datos medidos del sector.',
                ],
            },
            {
                'n': 5,
                'titulo': 'Plan Financiero a Tres Años',
                'resumen_indice': 'la cuenta de resultados de los tres años, la tesorería del primero, la financiación y su servicio, y los dos puntos de equilibrio.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Dar al analista todo lo que necesita para decidir: '
                            'resultado, ratios, caja mes a mes, servicio de la '
                            'deuda y punto de equilibrio, sin que tenga que '
                            'calcular nada por su cuenta.',
                'epigrafes': list(PPE_BP5),
                'puntos_por_epigrafe': PPE_BP5,
                'puntos_globales': [
                    'El año 2 es el año de crucero y es la columna de '
                    'referencia: se dice cada vez que se cita una cifra.',
                    'Ninguna cifra es una previsión de los resultados del '
                    'lector: son las de una bombonería modelada con supuestos '
                    'declarados.',
                ],
                'cifras': [
                    C('Ingresos del año 1', f'{X_PLAN}!PyG 3 Años!B11', 'eur'),
                    C('Ingresos del año de crucero', f'{X_PLAN}!PyG 3 Años!C11', 'eur'),
                    C('Ingresos del año 3', f'{X_PLAN}!PyG 3 Años!D11', 'eur'),
                    C('Total de costes fijos del año de crucero', f'{X_PLAN}!PyG 3 Años!C31', 'eur'),
                    C('Resultado neto del año de crucero', f'{X_PLAN}!PyG 3 Años!C41', 'eur'),
                    C('Peso del coste de personal sobre las ventas', f'{X_PLAN}!PyG 3 Años!C46', 'pct1'),
                    C('Cuota mensual del préstamo', f'{X_PLAN}!Financiación!B22', 'eur2'),
                    C('Ratio de cobertura del servicio de la deuda, en su punto más bajo', f'{X_PLAN}!Financiación!B123', 'num2'),
                    C('Saldo mínimo de caja del primer año', f'{X_PLAN}!Tesorería 12 meses!B24', 'eur'),
                    C('Saldo de caja al cierre del mes doce', f'{X_PLAN}!Tesorería 12 meses!M23', 'eur'),
                    C('Clientes al día necesarios para el equilibrio de caja', f'{X_PLAN}!Punto de Equilibrio!C22', 'num1'),
                ],
                'sector': ['CHS-40', 'CHN-71'],
                'tablas': [
                    {
                        'titulo': 'Costes fijos y resultado del año de crucero (plan-financiero-3-anos-chocolateria.xlsx, hoja «PyG 3 Años»)',
                        'src': (X_PLAN, 'PyG 3 Años'),
                        'cols': [('Concepto', 'A', 'txt'), ('Año 1', 'B', 'eur'),
                                 ('Año 2 (crucero)', 'C', 'eur'), ('Año 3', 'D', 'eur'),
                                 ('% sobre ventas (año 2)', 'E', 'pct1')],
                        'filas': (17, 34),
                        'nota': 'El sueldo del titular está DENTRO de los costes fijos, en '
                                'renglón propio. Un plan que se sostiene porque el promotor no '
                                'cobra no se sostiene.',
                    },
                    {
                        'titulo': 'Los tres escenarios, con los mismos costes fijos (plan-financiero-3-anos-chocolateria.xlsx, hoja «Escenarios»)',
                        'src': (X_PLAN, 'Escenarios'),
                        'cols': [('Métrica', 'A', 'txt'), ('Pesimista', 'B', 'eur'),
                                 ('Realista', 'C', 'eur'), ('Optimista', 'D', 'eur')],
                        'filas': (9, 16),
                        'nota': 'La columna central LEE el año de crucero: no es un escenario '
                                'aparte, es el mismo plan.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No presentes ninguna cifra de este plan como previsión de '
                    'los resultados del lector.',
                ],
            },
            {
                'n': 6,
                'titulo': 'Riesgos y Escenarios',
                'resumen_indice': 'los tres escenarios, el riesgo de materia prima con su número, el riesgo de estacionalidad y los riesgos regulatorio y de ejecución.',
                'palabras': 500, 'bloques': 1,
                'objetivo': 'Demostrar que el proyecto ha cuantificado sus '
                            'riesgos en lugar de enumerarlos, y que tiene una '
                            'respuesta prevista para cada uno.',
                'epigrafes': list(PPE_BP6),
                'puntos_por_epigrafe': PPE_BP6,
                'puntos_globales': [
                    'Un riesgo sin número no es un riesgo, es una frase. Cada '
                    'uno de los cuatro va con su cifra o con su fecha.',
                    'Nada de tremendismo ni de optimismo: el escenario que hay '
                    'que saber responder es el pesimista.',
                ],
                'cifras': [
                    C('Resultado neto del escenario pesimista', f'{X_PLAN}!Escenarios!B16', 'eur'),
                    C('Resultado neto del escenario optimista', f'{X_PLAN}!Escenarios!D16', 'eur'),
                    C('Lo que costaría al año una subida fuerte del cacao', f'{X_PLAN}!PyG 3 Años!B79', 'eur'),
                    C('Margen neto del año de crucero tras esa subida', f'{X_PLAN}!PyG 3 Años!B80', 'pct1'),
                    C('Resultado del mes de agosto', f'{X_CAMP}!El Valle de Agosto!B20', 'eur'),
                    C('Lo que cuesta agosto frente a un mes medio', f'{X_CAMP}!El Valle de Agosto!B22', 'eur'),
                    C('Campañas que el obrador no aguanta sin adelantar producción', f'{X_CAMP}!Capacidad vs Demanda del Pico!B26', 'num'),
                    C('Margen entre la ruta crítica y el plazo de la maquinaria, en meses', f'{X_LEGAL}!Cronograma y Ruta Crítica!C52', 'num1'),
                ],
                'sector': ['CHS-24a', 'CHS-24b', 'CHN-22', 'CHN-23', 'CHN-86'],
                'tablas': [
                    {
                        'titulo': 'Los cinco escenarios de precio de la cobertura (sensibilidad-al-precio-del-cacao.xlsx, hoja «Escenarios de Precio»)',
                        'src': (X_CACAO, 'Escenarios de Precio'),
                        # La columna de texto va SEGUNDA a propósito: con el
                        # porcentaje ahí, `es_fila_porcentual()` daría la fila
                        # por porcentual y los euros por kilo saldrían
                        # impresos como tantos por ciento.
                        'cols': [('Escenario', 'A', 'txt'), ('Qué es', 'B', 'txt'),
                                 ('Subida sobre el precio de hoy', 'C', 'pct0'),
                                 ('Cobertura negra (€/kg)', 'E', 'eur2'),
                                 ('Cobertura de origen (€/kg)', 'F', 'eur2')],
                        'filas': (7, 11),
                        'nota': 'Los escenarios se construyen sobre la tarifa que el proyecto '
                                'tiene hoy, no sobre la cotización del cacao: entre la bolsa y el '
                                'saco de cinco kilos hay una cadena entera.',
                    },
                    {
                        'titulo': 'Los cuatro riesgos del proyecto, con su número y su respuesta',
                        'cabecera': ['Riesgo', 'Cómo se mide en este plan', 'Respuesta prevista'],
                        'filas': [
                            ['Precio de la materia prima',
                             'Coste anual de una subida fuerte del cacao y margen neto que queda después',
                             'Cuatro palancas por orden: precio, gramaje dentro del mínimo legal, cobertura y margen'],
                            ['Estacionalidad',
                             'Resultado del mes más bajo y campañas que el obrador no aguanta sin adelantar',
                             'Provisión del mes bajo, cambio de mix en verano y adelanto de producción de lo que aguanta'],
                            ['Regulatorio',
                             'Fecha de revisión dentro del propio libro legal y papel definido en la cadena del cacao',
                             'Revisión periódica del texto consolidado y documentación pedida por escrito a cada proveedor'],
                            ['Ejecución',
                             'Margen en meses entre la ruta crítica del expediente y el plazo de entrega de la maquinaria',
                             'Pedir primero la línea de mayor plazo y cuadrar la fecha de apertura con ella'],
                        ],
                        'nota': 'Los cuatro están cuantificados en las herramientas del pack, y '
                                'los cuatro se vuelven a leer cuando cambia cualquiera de sus '
                                'supuestos.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'No cierres con una promesa de rentabilidad ni con un '
                    'resumen de lo ya dicho.',
                    'No enumeres riesgos sin número: cada uno va con su cifra '
                    'o con su fecha.',
                ],
            },
        ],
    },
]


# ==========================================================================
# BONUS 2 — «12 decisiones de apertura resueltas» (SPEC §4.3)
#
# Molde probado tres veces en la familia: doce bloques de un redactor cada uno,
# 875 palabras y una tabla. Los cinco epígrafes son FIJOS y se declaran una
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
            'subtitulo': 'Bonus del pack «Cómo Montar una Chocolatería» · con '
                         'los datos de las nueve herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Decisiones de Apertura Resueltas',
            'tipo_doc': 'bonus',
            'tipo_doc_art': 'del bonus',
            'tipo_doc_dem': 'este bonus',
            'categoria_doc': 'Guía profesional',
            'portada_texto': (
                'Doce decisiones que hay que tomar antes de abrir una '
                'chocolatería y que casi nunca se resuelven con un número: '
                'comprar la atemperadora continua o empezar con la de '
                'sobremesa, abrir con quince referencias o con veintiocho, '
                'vender la caja o la unidad, aceptar el primer pedido '
                'corporativo sin histórico, parar el obrador en agosto, '
                'empezar en casa dentro de la legalidad. Cada una con su '
                'contexto, sus opciones, el criterio con el que se decide, la '
                'celda del pack que la resuelve y la norma que aplica cuando '
                'la hay. No hay ninguna cifra inventada: cada número sale de '
                'una celda que puedes abrir y comprobar.'),
        },
        'gates': {
            'paginas_prometidas': 30,
            'palabras_objetivo': 10500,
            'min_palabras_cap': 600,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': '12 Decisiones de Apertura Resueltas',
                     'subject': 'Bonus del pack Cómo Montar una Chocolatería · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Bombonería o Bean-to-bar',
                'resumen_indice': 'comprar cobertura o partir del grano, y qué papel te da cada camino en la cadena del cacao.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver la decisión de fondo del proyecto: '
                            'comprar cobertura y trabajarla, o partir del grano '
                            'y hacer el chocolate. No son dos niveles del mismo '
                            'oficio: son dos negocios con dos regímenes '
                            'distintos.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: alguien que templa bien y que empieza a '
                     'pensar que el siguiente paso natural es tostar su propio '
                     'grano. Casi nunca lo es, y casi nunca por el motivo que '
                     'se cree.',
                     'Lo que casi nadie calcula antes de decidir: el tren de '
                     'bean-to-bar no tiene precio público verificable, así que '
                     'la primera consecuencia de elegirlo es que hay que '
                     'presupuestarlo pieza a pieza antes de saber si cabe.'],
                    ['Opción A: bombonería que compra cobertura profesional y '
                     'la trabaja. Opción B: bean-to-bar que importa grano y '
                     'hace su propio chocolate. Opción C: bombonería con una '
                     'línea pequeña de bean-to-bar como producto de firma.',
                     'Lo que cambia en cada una: la inversión, el espacio, el '
                     'papel que ocupas en la cadena del cacao, los papeles que '
                     'te piden y el catálogo ambiental en el que entras si '
                     'tuestas.'],
                    ['La regla: se decide por el papel en la cadena, no por el '
                     'romanticismo del producto. Comprar cobertura te deja en '
                     'una figura con obligaciones de conservar información; '
                     'importar grano te convierte en operador, con diligencia '
                     'debida completa y declaración presentada antes de '
                     'comercializar.',
                     'El segundo filtro es de capacidad: el tren de '
                     'bean-to-bar ocupa metros y horas que el obrador de '
                     'bombonería necesita para producir, y compite con ellos en '
                     'campaña.'],
                    ['La hoja de variante del formato del libro de '
                     'equipamiento trae la lista de la compra del tren y las '
                     'cinco preguntas que hay que hacerle al fabricante, con '
                     'una columna para anotar quién las ha contestado por '
                     'escrito.',
                     'Y la calculadora de inversión trae la columna de esa '
                     'variante SIN cifras de maquinaria a propósito: mientras '
                     'no tengas presupuestos por escrito, ese bloque se queda '
                     'en blanco y el veredicto lo dice.'],
                    ['Si compras cobertura ya comercializada en la Unión '
                     'Europea y amparada por una declaración de diligencia '
                     'debida, eres operador posterior. Ese paso es una '
                     'inferencia declarada, con la definición del reglamento '
                     'como condición, y así se escribe.',
                     'Si importas grano, eres OPERADOR: diligencia debida '
                     'completa, declaración antes de comercializar, '
                     'responsabilidad asumida y registro de cinco años. Y si '
                     'además tuestas, hay que preguntar a tu comunidad '
                     'autónoma por el catálogo de actividades potencialmente '
                     'contaminadoras.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Equipos del tren de bean-to-bar que el caso dice necesitar', f'{X_CAPEX}!Variante del Formato!E31', 'num'),
                    C('Veredicto del bean-to-bar en la calculadora de inversión', f'{X_CAPEX}!Variante del Formato!E33', 'txt'),
                    C('Equipos del tren marcados como necesarios en el libro de equipamiento', f'{X_EQUIP}!Variante del Formato!C20', 'num'),
                    C('Preguntas al fabricante contestadas por escrito', f'{X_EQUIP}!Variante del Formato!C29', 'num'),
                    C('Veredicto del bean-to-bar en el libro de equipamiento', f'{X_EQUIP}!Variante del Formato!C30', 'txt'),
                    C('De dónde viene el cacao en el caso modelado', f'{X_LEGAL}!EUDR — Tu Papel en la Cadena!B12', 'txt'),
                ],
                'sector': ['CHN-23', 'CHN-25', 'CHN-27', 'CHN-47', 'CHN-47b',
                           'CHS-48', 'CHS-51'],
                'tablas': [{
                    'titulo': 'La lista de la compra del tren de bean-to-bar, sin precios y con sus preguntas (checklist-equipamiento-y-proveedores-cacao.xlsx, hoja «Variante del Formato»)',
                    'src': (X_EQUIP, 'Variante del Formato'),
                    'cols': [('Nº', 'A', 'num'), ('Equipo del tren', 'B', 'txt'),
                             ('¿Lo necesitas?', 'C', 'txt'),
                             ('¿Tienes precio por escrito?', 'D', 'txt')],
                    'filas': (11, 19),
                    'nota': 'Va sin precios a propósito: no hay precio público verificable para '
                            'este equipamiento, y publicar una cifra inventada aquí sería peor '
                            'que no publicar ninguna.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO dar el precio del tren de bean-to-bar o de '
                    'cualquiera de sus equipos.',
                ],
            },
            {
                'n': 2,
                'titulo': 'Comprar la Continua o Empezar con la de Sobremesa',
                'resumen_indice': 'la decisión de máquina de templado, resuelta por kilos a la semana y por cuello de botella, no por catálogo.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver la compra que más dinero concentra de '
                            'toda la dotación: si se entra con una atemperadora '
                            'continua desde el primer día o se arranca con una '
                            'de sobremesa.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: el presupuesto no da para todo y la '
                     'atemperadora es la partida más visible. La tentación es '
                     'recortar ahí porque se puede templar a mano.',
                     'Lo que casi nadie calcula: cuántos bombones al día '
                     'permite cada opción, y si la que limita la producción es '
                     'de verdad la máquina o es otra cosa.'],
                    ['Opción A: atemperadora continua de sobremesa desde el '
                     'principio, con su embalaje, transporte y puesta en '
                     'marcha. Opción B: atemperadora de arranque pequeña y '
                     'crecer después. Opción C: empezar con la pequeña y '
                     'sumar un temperador de baño maría como segunda línea.',
                     'Lo que cambia en cada una: el desembolso, los kilos por '
                     'carga, el número de coberturas que puedes tener a punto '
                     'a la vez y el plazo de entrega, que en la continua es el '
                     'más largo de toda la dotación.'],
                    ['La regla: se cruza la capacidad de cada máquina con la '
                     'producción que pide tu plan, en bombones equivalentes de '
                     'obrador, y se mira quién limita DESPUÉS de ese cruce.',
                     'Y el hallazgo que casi siempre da la vuelta a la '
                     'decisión: en una bombonería pequeña el cuello de botella '
                     'casi nunca es el templado. Son las manos y el puesto de '
                     'envasado, y ninguna máquina de templar los arregla.'],
                    ['La hoja de capacidad por equipo del libro de capacidad y '
                     'clima convierte cada máquina en bombones al día y dice '
                     'cuál limita el conjunto.',
                     'Y la hoja de equipamiento del libro de compra trae el '
                     'plazo de entrega de cada línea: la continua es la que '
                     'marca el plazo crítico, así que si se elige, se pide '
                     'primero.'],
                    ['Aquí no hay norma que decida: es una decisión económica y '
                     'de capacidad, y se dice que no la hay.',
                     'Lo único normativo que roza esta decisión es el papeleo '
                     'de la instalación eléctrica y la potencia contratada, '
                     'que se comprueba en la ficha de visita a local antes de '
                     'firmar.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Precio de referencia de la atemperadora continua', f'{X_EQUIP}!Equipamiento!I15', 'eur'),
                    C('Plazo de entrega de la atemperadora continua, en semanas', f'{X_EQUIP}!Equipamiento!R15', 'num'),
                    C('Bombones al día de obrador que permite la atemperadora continua', f'{X_CAP}!Capacidad por Equipo!M6', 'num'),
                    C('Bombones al día de obrador que permite la atemperadora de arranque', f'{X_CAP}!Capacidad por Equipo!M16', 'num'),
                    C('Bombones al día que permite el conjunto de equipos', f'{X_CAP}!Cuello de Botella!B7', 'num'),
                    C('El equipo que limita de verdad', f'{X_CAP}!Cuello de Botella!B8', 'txt'),
                ],
                'sector': ['CHS-41a', 'CHS-41h', 'CHS-41i', 'CHS-41j'],
                'tablas': [{
                    'titulo': 'Las dos puertas de entrada al templado, comparadas',
                    'cabecera': ['Qué comparas', 'Atemperadora continua de sobremesa', 'Atemperadora de arranque'],
                    'filas': [
                        ['Kilos de cobertura por carga', 'Carga grande: permite trabajar una cobertura toda la jornada', 'Carga pequeña: hay que recargar varias veces al día'],
                        ['Coberturas a punto a la vez', 'Una, salvo que sumes temperador o mantenedor', 'Una, y con menos margen de maniobra'],
                        ['Plazo de entrega', 'Es la línea que marca el plazo crítico de toda la dotación', 'Corto: se consigue en semanas'],
                        ['Qué pasa en campaña', 'Aguanta el pico si el resto del obrador acompaña', 'Obliga a más recargas y más horas de obrador'],
                        ['Cuándo tiene sentido', 'Cuando el plan pide producción sostenida y hay financiación', 'Cuando el arranque es corto de caja y la producción va a crecer despacio'],
                        ['Qué NO arregla ninguna de las dos', 'El puesto de moldeado y el de envasado, que es donde suele estar el cuello', 'Lo mismo'],
                    ],
                    'nota': 'Los precios de las dos y de todas las máquinas de la escalera están '
                            'en el libro de equipamiento, cada una con su ficha y su base de '
                            'impuesto declarada.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO citar la escalera de atemperadoras como un '
                    'rango agregado: se citan una a una.',
                ],
            },
            {
                'n': 3,
                'titulo': 'Abrir con Quince Referencias o con Veintiocho',
                'resumen_indice': 'cuántas referencias aguanta de verdad un obrador que acaba de abrir, y qué cuesta cada una de más.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver el tamaño de la carta de apertura, que '
                            'es la decisión que más silenciosamente encarece un '
                            'obrador nuevo.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: se abre con todo lo que se sabe hacer, '
                     'porque parece que una vitrina llena vende más. Y la '
                     'vitrina llena de referencias que no rotan es una vitrina '
                     'de merma.',
                     'Lo que casi nadie calcula: cada referencia nueva es un '
                     'molde, un relleno, una caducidad propia, una línea más '
                     'en la declaración de alérgenos y una tanda que hay que '
                     'poner en marcha.'],
                    ['Opción A: abrir con una carta corta y ampliarla con lo '
                     'que pida el mostrador. Opción B: abrir con la carta '
                     'completa y podarla a los tres meses. Opción C: carta '
                     'corta fija más una referencia rotatoria de temporada.',
                     'Lo que cambia en cada una: el inmovilizado en moldes y '
                     'packaging, la merma por caducidad del primer trimestre y '
                     'la capacidad de decir a cada cliente qué es cada cosa.'],
                    ['La regla: la carta se decide por margen y por rotación, '
                     'no por variedad. Dos umbrales, margen mínimo por pieza y '
                     'peso mínimo en el mix, y todo lo que no los pasa entra '
                     'en revisión.',
                     'El segundo filtro es de vida útil: una referencia de '
                     'rotación baja y caducidad corta pierde dinero dos veces, '
                     'y esas son las primeras que sobran.'],
                    ['La hoja de decisión de surtido del libro de la carta da '
                     'el veredicto referencia a referencia: mantener, revisar '
                     'precio o retirar, con el margen anual de cada una al '
                     'lado.',
                     'Y la hoja de lote y merma por caducidad del libro de '
                     'vida útil dice cuáles tienen la tanda demasiado grande '
                     'para lo que duran, que es el otro lado del mismo '
                     'problema.'],
                    ['No hay norma que limite el número de referencias, y se '
                     'dice.',
                     'Lo que sí crece con cada referencia es la obligación de '
                     'información: alérgenos, denominación legal correcta y, '
                     'en lo envasado, etiqueta completa. Veintiocho '
                     'referencias son veintiocho decisiones de denominación.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Referencias con veredicto de mantener', f'{X_CARTA}!Decisión de Surtido!B37', 'num'),
                    C('Referencias con veredicto de revisar precio', f'{X_CARTA}!Decisión de Surtido!B38', 'num'),
                    C('Referencias con veredicto de retirar', f'{X_CARTA}!Decisión de Surtido!B39', 'num'),
                    C('Margen de toda la carta al año', f'{X_CARTA}!Decisión de Surtido!G35', 'eur'),
                    C('PVP medio ponderado de la carta con IVA', f'{X_CARTA}!Mix y Ticket Medio!B37', 'eur2'),
                    C('Referencias que llevan fecha de caducidad', f'{X_VIDA}!Vida Útil Declarada!H44', 'num'),
                    C('Referencias con la tanda demasiado grande para lo que duran', f'{X_VIDA}!Lote y Merma por Caducidad!D46', 'num'),
                ],
                'sector': ['CHS-29', 'CHS-32', 'CHS-25c'],
                'tablas': [{
                    'titulo': 'Qué cuesta cada referencia de más, y qué se gana con ella',
                    'cabecera': ['Lo que suma una referencia nueva', 'Coste que no se ve', 'Cuándo compensa'],
                    'filas': [
                        ['Un molde o un juego de moldes', 'Inmovilizado que sólo se usa si esa referencia rota', 'Si el molde sirve para varias referencias o para campaña'],
                        ['Un relleno propio', 'Una tanda mínima, una caducidad propia y merma si no se vende', 'Si comparte relleno con otra referencia que ya rota'],
                        ['Una línea en la declaración de alérgenos', 'Tiempo de gestión y riesgo de error en mostrador', 'Si no añade ningún alérgeno nuevo al obrador'],
                        ['Una decisión de denominación legal', 'Comprobar mínimos y menciones obligatorias de esa familia', 'Si cae dentro de una denominación que ya has resuelto'],
                        ['Un hueco en la vitrina', 'Menos espacio para lo que sí rota', 'Si sube el ticket medio o abre una ocasión de compra nueva'],
                    ],
                    'nota': 'La carta del caso modelado tiene veintiocho referencias en cinco '
                            'familias, y es un supuesto declarado: lo que se lleva el lector es '
                            'el criterio, no el número.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO recomendar una moda de producto como referencia '
                    'de apertura.',
                ],
            },
            {
                'n': 4,
                'titulo': 'Vender la Caja o la Unidad',
                'resumen_indice': 'la caja es la unidad de venta real de una bombonería, y casi nadie la escandalla como una referencia propia.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver la decisión que más dinero mueve en el '
                            'mostrador: qué descuento implícito lleva cada '
                            'formato de caja y si compensa.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: se pone un precio redondo a la caja de '
                     'doce, otro a la de veinte y otro a la de treinta y '
                     'cinco, sin comprobar qué descuento por bombón supone cada '
                     'uno.',
                     'Lo que casi nadie calcula: la caja tiene coste propio de '
                     'montaje y de packaging, y el precio por bombón dentro de '
                     'la caja grande puede quedar muy por debajo del suelto.'],
                    ['Opción A: precio por caja con descuento creciente por '
                     'tamaño. Opción B: precio por bombón igual en todos los '
                     'formatos y la caja como envase que se cobra aparte. '
                     'Opción C: caja pequeña sin descuento y descuento sólo en '
                     'la grande.',
                     'Lo que cambia en cada una: el ticket medio, el margen en '
                     'euros por operación y la percepción de regalo, que es lo '
                     'que de verdad compra el cliente de caja.'],
                    ['La regla: se decide con el margen en EUROS por '
                     'operación, no con el porcentaje. Una caja puede tener '
                     'peor porcentaje y dejar más euros que tres bombones '
                     'sueltos.',
                     'Y el dato incómodo que hay que mirar de frente: '
                     'comparada con vender esos mismos bombones sueltos, la '
                     'caja deja menos margen. No es un error, es un descuento '
                     'por volumen que el cliente no ve como descuento, y hay '
                     'razones buenas para darlo.'],
                    ['La hoja de unidad contra caja del libro de la carta pone '
                     'las dos cifras al lado: el margen de la caja y el margen '
                     'de esos mismos bombones vendidos sueltos.',
                     'Y da el precio por bombón dentro de cada formato, que es '
                     'la cifra con la que se compara contra el mercado y con '
                     'la que se decide el descuento.'],
                    ['Aquí hay una norma que casi nadie asocia a esta '
                     'decisión: la caja surtida tiene regla propia de '
                     'etiquetado, y permite una sola lista de ingredientes '
                     'para todo el surtido.',
                     'Y otra de vida útil: la caja caduca cuando caduca la '
                     'pieza más corta que lleva dentro. Eso limita qué se '
                     'puede meter en una caja de regalo.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Precio por bombón dentro de la caja de doce, con IVA', f'{X_CARTA}!Unidad vs Caja!C33', 'eur2'),
                    C('Precio por bombón dentro de la caja de treinta y cinco, con IVA', f'{X_CARTA}!Unidad vs Caja!E33', 'eur2'),
                    C('Descuento implícito de la caja de doce', f'{X_CARTA}!Unidad vs Caja!C35', 'pct1'),
                    C('Descuento implícito de la caja de treinta y cinco', f'{X_CARTA}!Unidad vs Caja!E35', 'pct1'),
                    C('Coste total de la caja de doce', f'{X_CARTA}!Unidad vs Caja!C28', 'eur2'),
                    C('Coste total de la caja de treinta y cinco', f'{X_CARTA}!Unidad vs Caja!E28', 'eur2'),
                    C('Margen de la caja de doce', f'{X_CARTA}!Unidad vs Caja!C37', 'eur2'),
                    C('Margen de la caja de treinta y cinco', f'{X_CARTA}!Unidad vs Caja!E37', 'eur2'),
                ],
                'sector': ['CHS-29', 'CHN-13'],
                'tablas': [{
                    'titulo': 'Precio por bombón y margen de cada formato de caja (carta-de-apertura-y-escandallo-chocolate.xlsx, hoja «Unidad vs Caja»)',
                    'src': (X_CARTA, 'Unidad vs Caja'),
                    'cols': [('Concepto', 'A', 'txt'), ('Caja de 12', 'C', 'eur2'),
                             ('Caja de 20', 'D', 'eur2'), ('Caja de 35', 'E', 'eur2'),
                             ('Estuche corporativo de 24', 'F', 'eur2')],
                    'filas': (33, 40),
                    # La fila del descuento es un porcentaje dentro de una
                    # columna de euros y su etiqueta no lo declara: se
                    # imprimiría «0,17 €» donde hay un 16,8 %. Va en las
                    # cifras de este bloque, formateada como porcentaje.
                    'omitir_filas': (35,),
                    'nota': 'Todas las cifras van en euros: por caja, salvo las dos filas de '
                            'precio por bombón, que van por pieza. El descuento implícito de '
                            'cada formato está en el texto, en porcentaje. El veredicto de la '
                            'última fila no es una advertencia: es la decisión comercial que hay '
                            'que tomar a la vista del margen en euros.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO presentar el descuento de la caja como un error '
                    'del modelo: es una decisión comercial con razones buenas.',
                ],
            },
            {
                'n': 5,
                'titulo': 'Cobertura de Marca o Cobertura de Origen',
                'resumen_indice': 'la decisión de posicionamiento más cara del negocio, resuelta con el coste por pieza y con la referencia que primero se rompe.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver con qué cobertura se trabaja, que es la '
                            'decisión que fija el coste de materia de casi toda '
                            'la carta y el discurso de la tienda.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: se prueba una cobertura de origen, se '
                     'nota la diferencia en boca y se decide trabajar con ella '
                     'sin llevar el precio al escandallo.',
                     'Lo que casi nadie calcula: entre una cobertura '
                     'profesional de marca y una de origen hay un factor que '
                     'multiplica el coste de materia de cada pieza que la '
                     'lleve.'],
                    ['Opción A: una sola cobertura de marca para toda la '
                     'carta. Opción B: cobertura de origen en toda la carta. '
                     'Opción C: la de marca como base y la de origen sólo en '
                     'la línea de tabletas y en la referencia de firma.',
                     'Lo que cambia en cada una: el coste de materia por '
                     'pieza, el precio de venta que hay que sostener, la '
                     'exposición a una subida del cacao y el discurso de '
                     'mostrador.'],
                    ['La regla: se decide por referencia, no por casa. La '
                     'cobertura cara tiene sentido donde el cliente puede '
                     'notarla y el precio puede subir; en un bombón relleno, '
                     'el relleno tapa buena parte de lo que has pagado.',
                     'Y el filtro de riesgo: la referencia que más cobertura '
                     'lleva por pieza es la que primero se rompe cuando sube '
                     'el cacao, así que poner la de origen ahí concentra todo '
                     'el riesgo en la misma pieza.'],
                    ['La hoja de coste de cobertura del libro de sensibilidad '
                     'al precio del cacao da el coste de cobertura por pieza de '
                     'cada referencia y el food cost de materia que produce.',
                     'Y la hoja de repercusión al precio dice qué referencia se '
                     'rompe primero y qué subida aguanta cada una antes de '
                     'pasarse del food cost máximo que te has puesto.'],
                    ['La norma no te obliga a usar una cobertura ni otra, pero '
                     'sí condiciona lo que puedes escribir: los calificativos '
                     'de calidad sólo caben sobre tres denominaciones y por '
                     'encima de unos umbrales reforzados.',
                     'Y las tres magnitudes que la bolsa no publica —materia '
                     'seca total, manteca y desgrasada— hay que pedírselas al '
                     'proveedor si vas a apoyarte en la calidad del producto '
                     'para justificar el precio.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Precio de la cobertura de marca como lo trae la fuente, con IVA', f'{X_CACAO}!Coste de Cobertura!D7', 'eur2'),
                    C('Precio de esa cobertura en base imponible', f'{X_CACAO}!Coste de Cobertura!G7', 'eur2'),
                    C('Precio de la cobertura de origen en base imponible', f'{X_CACAO}!Coste de Cobertura!G8', 'eur2'),
                    C('Coste de cobertura por pieza de la tableta de origen', f'{X_CACAO}!Coste de Cobertura!K26', 'eur2'),
                    C('Food cost de materia de esa misma tableta', f'{X_CACAO}!Coste de Cobertura!U26', 'pct1'),
                    C('La referencia que primero se rompe si sube el cacao', f'{X_CACAO}!Repercusión al PVP!C46', 'txt'),
                ],
                'sector': ['CHS-28a', 'CHS-28c', 'CHN-08', 'CHN-02'],
                'tablas': [{
                    'titulo': 'Las cuatro coberturas del caso, en las dos bases de precio (sensibilidad-al-precio-del-cacao.xlsx, hoja «Coste de Cobertura»)',
                    'src': (X_CACAO, 'Coste de Cobertura'),
                    'cols': [('Cobertura', 'B', 'txt'), ('Formato de compra', 'C', 'txt'),
                             ('Precio como lo trae la fuente (€/kg)', 'D', 'eur2'),
                             ('Base declarada por la fuente', 'E', 'txt'),
                             ('Precio en base imponible (€/kg)', 'G', 'eur2')],
                    'filas': (7, 10),
                    'nota': 'El escandallo usa SIEMPRE la columna de base imponible. La primera '
                            'fila viene declarada con impuesto incluido por su fuente: usarla tal '
                            'cual sube el coste de materia casi un diez por ciento.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO mezclar las dos bases de precio en el mismo '
                    'cálculo.',
                ],
            },
            {
                'n': 6,
                'titulo': 'Vitrina Refrigerada o Vitrina Climatizada',
                'resumen_indice': 'qué mueble aguanta el chocolate, qué referencias pueden ir en él y cuáles tienen que ir a nevera.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver la compra del mueble que enseña el '
                            'producto, y decidir qué referencias pueden vivir '
                            'en él y cuáles no.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: se hereda o se compra una vitrina de '
                     'pastelería porque es lo que hay, y el bombón condensa al '
                     'salir o se blanquea dentro.',
                     'Lo que casi nadie calcula: el chocolate tiene una '
                     'ventana estrecha por arriba y por abajo, y el relleno '
                     'fresco tiene otra completamente distinta.'],
                    ['Opción A: vitrina específica para chocolate, templada y '
                     'con control de humedad. Opción B: vitrina de pastelería '
                     'en frío positivo bajo. Opción C: vitrina templada para '
                     'el bombón y nevera aparte para las referencias con '
                     'relleno fresco.',
                     'Lo que cambia en cada una: el brillo del producto en '
                     'mostrador, la condensación al despachar, la vida útil '
                     'real de los rellenos y qué referencias puedes exponer.'],
                    ['La regla: manda el relleno, no el chocolate. Una '
                     'referencia con actividad de agua alta va a nevera aunque '
                     'esté cubierta de chocolate; una tableta aguanta en '
                     'vitrina templada sin problema.',
                     'Y el criterio de compra: se compara el rango de trabajo '
                     'que declara el fabricante con el objetivo operativo que '
                     'tú te fijas, y se compra el que cubre el objetivo, no el '
                     'que lo roza.'],
                    ['La hoja de temperatura y vitrina del libro de vida útil '
                     'trae las cinco ventanas del oficio y las contrasta con '
                     'el rango de TU vitrina, y dice qué referencias van a '
                     'nevera en lugar de a vitrina.',
                     'El semáforo sólo avisa por encima del punto en el que la '
                     'manteca empieza a sufrir: no pone en rojo el objetivo '
                     'operativo que publica el kit de tareas de la casa.'],
                    ['No hay temperatura legal del chocolate, y se dice: la '
                     'tabla de temperaturas de conservación de la norma '
                     'higiénica no tiene fila para él.',
                     'Lo que sí obliga es lo que TÚ declares: en lo envasado, '
                     'la temperatura que pongas en la etiqueta; en lo que se '
                     'despacha a granel, lo que conste en tu sistema de '
                     'autocontrol.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Temperatura mínima de trabajo de la vitrina del caso', f'{X_VIDA}!Temperatura y Vitrina!D15', 'num'),
                    C('Temperatura máxima de trabajo de la vitrina del caso', f'{X_VIDA}!Temperatura y Vitrina!D16', 'num'),
                    C('Veredicto de la vitrina del caso', f'{X_VIDA}!Temperatura y Vitrina!F16', 'txt'),
                    C('Temperatura a la que salta la alarma', f'{X_VIDA}!Parámetros!B12', 'num'),
                    C('Humedad máxima de trabajo de la vitrina', f'{X_VIDA}!Parámetros!B13', 'num'),
                    C('Referencias por encima de la alarma de la vitrina', f'{X_VIDA}!Temperatura y Vitrina!D50', 'num'),
                    C('Referencias que van a nevera y no a vitrina', f'{X_VIDA}!Temperatura y Vitrina!F50', 'num'),
                ],
                'sector': ['CHS-43', 'CHN-30', 'CHN-87'],
                'tablas': [{
                    'titulo': 'Las cinco ventanas del oficio, y cuál le toca a la vitrina (vida-util-rellenos-y-rotacion.xlsx, hoja «Temperatura y Vitrina»)',
                    'src': (X_VIDA, 'Temperatura y Vitrina'),
                    'cols': [('Zona', 'A', 'txt'), ('Temperatura objetivo', 'C', 'txt'),
                             ('Humedad', 'D', 'txt'), ('De dónde sale', 'E', 'txt')],
                    'filas': (7, 11),
                    'nota': 'Cinco equipos y cinco ventanas: confundir la de la sala con la de '
                            'la vitrina o con la de la nevera de rellenos es el error que más '
                            'producto estropea.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO presentar el objetivo operativo del kit como si '
                    'estuviera fuera de rango.',
                ],
            },
            {
                'n': 7,
                'titulo': 'Aceptar el Primer Pedido Corporativo sin Histórico',
                'resumen_indice': 'el pedido que llena diciembre, y el que puede cambiarte de régimen sanitario sin que te des cuenta.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver qué hacer con el primer pedido grande de '
                            'empresa: si se acepta, con qué condiciones y qué '
                            'obligaciones arrastra.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: llega una empresa en noviembre pidiendo '
                     'estuches personalizados para el dieciocho de diciembre, y '
                     'la tentación de decir que sí es enorme.',
                     'Lo que casi nadie calcula: el plazo mínimo desde que '
                     'aprueban la muestra, el mínimo de fabricación y los días '
                     'que vas a tardar en cobrar.'],
                    ['Opción A: aceptarlo con un mínimo de pedido y un plazo '
                     'de aceptación cerrado. Opción B: rechazarlo y ofrecer '
                     'producto de catálogo sin personalizar. Opción C: '
                     'aceptarlo con anticipo y con fecha límite de aprobación '
                     'de la muestra.',
                     'Lo que cambia en cada una: el margen, la caja '
                     'inmovilizada por el aplazamiento de cobro y el riesgo de '
                     'comerte la campaña de mostrador con un pedido que ocupa '
                     'el obrador.'],
                    ['La regla: el pedido corporativo se cierra por FECHA, no '
                     'por precio. Hay un día a partir del cual aceptar '
                     'significa no poder servir, y ese día se calcula hacia '
                     'atrás desde la capacidad del obrador.',
                     'Y el filtro que casi nadie aplica: preguntar quién es el '
                     'cliente. Si es una empresa que va a revender, o un hotel '
                     'inscrito en el registro general, la operación deja de ser '
                     'sólo comercial.'],
                    ['La hoja de talleres y regalo corporativo del plan '
                     'financiero da la fecha límite para aceptar un pedido '
                     'corporativo y la caja que te inmoviliza el aplazamiento.',
                     'Y la tabla de clientes del libro de equipamiento es '
                     'donde se anota: nombre, dirección, producto y si está '
                     'inscrito en el registro general. Esa tabla se conserva '
                     'cinco años.'],
                    ['La norma que decide: basta con que UNO de tus clientes '
                     'esté inscrito en el registro general para perder el '
                     'requisito de restringido, y con él la excepción que te '
                     'mantiene fuera de ese registro.',
                     'Y la que casi nadie cita: hay que registrar a quién '
                     'suministras, no sólo a quién compras. El regalo '
                     'corporativo es justo el canal que activa las dos cosas a '
                     'la vez.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Clientes registrados en la tabla del caso', f'{X_EQUIP}!Clientes a los que Suministras!E20', 'num'),
                    C('De ellos, clientes de hostelería', f'{X_EQUIP}!Clientes a los que Suministras!E21', 'num'),
                    C('De ellos, de regalo corporativo', f'{X_EQUIP}!Clientes a los que Suministras!E22', 'num'),
                    C('De ellos, minoristas de distinta titularidad', f'{X_EQUIP}!Clientes a los que Suministras!E23', 'num'),
                    C('Clientes inscritos en el registro general', f'{X_EQUIP}!Clientes a los que Suministras!E24', 'num'),
                    C('Veredicto del registro de clientes', f'{X_EQUIP}!Clientes a los que Suministras!E26', 'txt'),
                    C('¿Sigues cumpliendo el requisito de restringido?', f'{X_LEGAL}!Suministro a Otros Minoristas!B37', 'txt'),
                    C('Caja inmovilizada por el aplazamiento de cobro corporativo', f'{X_PLAN}!Talleres y Regalo Corporativo!B54', 'eur'),
                ],
                'sector': ['CHN-41', 'CHN-24', 'CHS-55'],
                'tablas': [{
                    'titulo': 'La tabla de clientes que obliga a llevar la norma del cacao (checklist-equipamiento-y-proveedores-cacao.xlsx, hoja «Clientes a los que Suministras»)',
                    'src': (X_EQUIP, 'Clientes a los que Suministras'),
                    'cols': [('Nombre del cliente', 'B', 'txt'), ('Tipo', 'D', 'txt'),
                             ('Canal', 'E', 'txt'),
                             ('Producto suministrado', 'F', 'txt'),
                             ('¿Inscrito en el registro general?', 'H', 'txt')],
                    'filas': (10, 13),
                    'nota': 'Los cuatro clientes son ficticios y están declarados como tales. Lo '
                            'que no es ficticio es la obligación de llevar esta tabla y '
                            'conservarla cinco años, ni el efecto del cuarto: un minorista de '
                            'distinta titularidad activa las tres condiciones del régimen '
                            'sanitario.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO escribir «basta con registrar a tus '
                    'proveedores».',
                ],
            },
            {
                'n': 8,
                'titulo': 'Envío a Domicilio en Verano: Cuándo Dices que No',
                'resumen_indice': 'el canal que parece gratis y responde de la temperatura en el camión.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver si se mantiene el envío a domicilio en '
                            'los meses de calor, con qué producto y con qué '
                            'coste.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: la tienda online funciona en Navidad y '
                     'se deja abierta todo el año. Llega julio, sale un pedido '
                     'de bombones de ganache y llega derretido.',
                     'Lo que casi nadie calcula: el coste del envío '
                     'refrigerado sobre el pedido medio, y lo que queda de '
                     'margen después de pagarlo.'],
                    ['Opción A: apagar el canal de junio a septiembre. Opción '
                     'B: mantenerlo sólo con producto estable, sin ganache '
                     'fresca. Opción C: mantenerlo entero con envío '
                     'refrigerado y recargo.',
                     'Lo que cambia en cada una: el margen de contribución del '
                     'canal, la reputación cuando un pedido llega mal y la '
                     'carga de trabajo del obrador en el mes de menos '
                     'producción.'],
                    ['La regla: el envío se decide por el producto, no por el '
                     'calendario. Lo que aguanta el transporte se envía todo '
                     'el año; lo que no aguanta no se envía nunca, ni en '
                     'enero.',
                     'Y el número que decide si el canal existe: el margen de '
                     'contribución del online DESPUÉS de pagar el envío. Si no '
                     'aguanta ese descuento, el canal no es rentable, es '
                     'publicidad cara.'],
                    ['La hoja de canales del plan financiero da el margen de '
                     'contribución del canal online después del envío, y su '
                     'veredicto.',
                     'Y la hoja de temperatura y vitrina del libro de vida '
                     'útil dice qué referencias van a nevera: ésas son '
                     'exactamente las que no salen en un paquete.'],
                    ['La norma que aplica y casi nadie asocia a este canal: '
                     'fijar tú la temperatura de conservación es la ventaja y '
                     'la trampa, porque respondes de mantenerla también '
                     'durante el transporte.',
                     'Y la de información: en venta a distancia todo lo '
                     'obligatorio menos la fecha tiene que estar disponible '
                     'ANTES de que el cliente pague, alérgenos incluidos.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Margen de contribución del canal online después del envío', f'{X_PLAN}!Canales y Punto Muerto!B39', 'pct1'),
                    C('Veredicto del canal online', f'{X_PLAN}!Canales y Punto Muerto!B40', 'txt'),
                    C('Vida útil más corta de toda la carta, en días', f'{X_VIDA}!Vida Útil Declarada!G44', 'num'),
                    C('Referencias que van a nevera y no a vitrina', f'{X_VIDA}!Temperatura y Vitrina!F50', 'num'),
                    C('Peso de agosto sobre las ventas del año', f'{X_CAMP}!Peso sobre el Año!F14', 'pct1'),
                ],
                'sector': ['CHN-88', 'CHN-57', 'CHN-59', 'CHN-90', 'CHS-10'],
                'tablas': [{
                    'titulo': 'Qué sale en un paquete y qué no, y qué obligación arrastra cada caso',
                    'cabecera': ['Qué envías', '¿Aguanta el transporte?', 'Qué tienes que poder sostener', 'Qué haces en verano'],
                    'filas': [
                        ['Tableta y chocolate sin relleno', 'Sí, con embalaje aislante', 'La temperatura que hayas declarado en la etiqueta', 'Se mantiene, con embalaje reforzado'],
                        ['Bombón de praliné o gianduja', 'Sí, con cuidado', 'Lo mismo, y evitar cambios bruscos', 'Se mantiene con envío refrigerado'],
                        ['Bombón de ganache con nata fresca', 'No', 'Sería imposible sostener la cadena de frío puerta a puerta', 'No se envía, ni en enero'],
                        ['Caja surtida con ganache dentro', 'No', 'La caja caduca con la pieza más corta que lleva', 'Se sustituye por surtido estable'],
                        ['Figuras huecas y piezas grandes', 'Sí, si el embalaje las protege', 'El riesgo aquí es la rotura, no la temperatura', 'Se mantiene'],
                    ],
                    'nota': 'La decisión es de producto, no de calendario: lo que no aguanta el '
                            'transporte no se envía nunca. Vender por internet, además, te '
                            'convierte en envasador de la caja de envío.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO decir que vender online cambia tu registro '
                    'sanitario.',
                ],
            },
            {
                'n': 9,
                'titulo': 'Parar el Obrador en Agosto o No Pararlo',
                'resumen_indice': 'un mes de doce, con los fijos corriendo y la tienda abierta.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver qué se hace en el mes más bajo del año: '
                            'si se para el obrador, si se cierra la tienda y '
                            'qué se vende mientras tanto.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: llega agosto, baja la venta y se decide '
                     'cerrar tres semanas. Y al volver hay que arrancar el '
                     'obrador desde cero justo antes de la temporada alta.',
                     'Lo que casi nadie calcula: cuánto cuesta ese mes '
                     'exactamente, con los gastos fijos corriendo enteros y la '
                     'facturación a una fracción de la de un mes medio.'],
                    ['Opción A: parar el obrador y mantener la tienda abierta '
                     'con producto estable. Opción B: cerrar todo y hacer '
                     'vacaciones de plantilla. Opción C: mantener producción a '
                     'media máquina para adelantar campaña de otoño.',
                     'Lo que cambia en cada una: el resultado del mes, el '
                     'aprovechamiento de las vacaciones del equipo y el estado '
                     'del stock cuando arranca la temporada.'],
                    ['La regla: lo que para es el OBRADOR, no la caja. La '
                     'tienda sigue facturando menos, no cero, y ese menos paga '
                     'una parte de los fijos que si cierras pagas igual.',
                     'Y la palanca que sí existe: cambiar el mix. Menos '
                     'ganache fresca y más tableta y producto estable baja un '
                     'poco el margen porcentual y quita casi toda la merma.'],
                    ['La hoja del valle de agosto del libro de campañas da el '
                     'resultado del mes y lo que cuesta frente a un mes medio. '
                     'Es una cifra que se provisiona en enero, no una sorpresa '
                     'de septiembre.',
                     'Y la hoja de peso sobre el año dice cuánto factura '
                     'agosto respecto a un mes medio, que es lo que hay que '
                     'mirar antes de decidir si merece la pena abrir.'],
                    ['Aquí no hay norma que decida, y se dice: cerrar o no '
                     'cerrar en agosto es una decisión de negocio.',
                     'Lo que sí hay es un matiz laboral que conviene planificar '
                     'con la asesoría: las vacaciones del equipo se concentran '
                     'de forma natural en este mes, y es la única ventana del '
                     'año en la que eso no compite con una campaña.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Ventas de agosto frente a un mes medio', f'{X_CAMP}!El Valle de Agosto!B13', 'num2'),
                    C('Ventas de agosto sin IVA', f'{X_CAMP}!Peso sobre el Año!E14', 'eur'),
                    C('Caída del margen al cambiar el mix en verano', f'{X_CAMP}!El Valle de Agosto!B16', 'pct2'),
                    C('Resultado del mes de agosto', f'{X_CAMP}!El Valle de Agosto!B20', 'eur'),
                    C('Lo que cuesta agosto frente a un mes medio', f'{X_CAMP}!El Valle de Agosto!B22', 'eur'),
                    C('Veredicto de agosto', f'{X_CAMP}!El Valle de Agosto!B23', 'txt'),
                ],
                'sector': ['CHS-10', 'CHS-11', 'CHS-34'],
                'tablas': [{
                    'titulo': 'Julio, agosto y septiembre en el caso modelado (campanas-y-valle-del-ano.xlsx, hoja «Peso sobre el Año»)',
                    'src': (X_CAMP, 'Peso sobre el Año'),
                    'cols': [('Mes', 'A', 'txt'), ('Temporada que declara el kit', 'B', 'txt'),
                             ('Coeficiente sobre el mes medio', 'C', 'num2'),
                             ('Ventas del mes sin IVA (€)', 'E', 'eur'),
                             ('Parte del año (%)', 'F', 'pct1')],
                    'filas': (13, 15),
                    'nota': 'Agosto es el ÚNICO mes de temporada baja de los doce. Julio y '
                            'septiembre son de temporada media, así que el verano no es un '
                            'agujero de tres meses: es un mes bajo entre dos medios.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO escribir «valle de junio a agosto» o «un valle '
                    'de tres meses».',
                ],
            },
            {
                'n': 10,
                'titulo': 'El Taller: Línea de Negocio o Marketing',
                'resumen_indice': 'la única línea que funciona en agosto y no depende del precio del cacao, medida por hora de sala.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver si los talleres y las catas son una '
                            'línea de negocio o una herramienta de marketing, y '
                            'con qué números se sostiene cada lectura.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: se montan talleres porque llenan '
                     'Instagram, y nadie calcula si la hora de sala ocupada '
                     'por doce personas deja más o menos que esa misma hora '
                     'vendiendo.',
                     'Lo que casi nadie calcula: cuántos asistentes hacen '
                     'falta sólo para cubrir el coste del docente, y cuántos '
                     'contando también el material.'],
                    ['Opción A: taller como línea de negocio, con calendario '
                     'fijo y precio de mercado. Opción B: taller como '
                     'marketing, puntual y a precio de coste. Opción C: taller '
                     'privado para empresas, que es otro cliente y otro '
                     'precio.',
                     'Lo que cambia en cada una: el aprovechamiento de la sala '
                     'en hora punta, la carga de trabajo del obrador y el '
                     'perfil de cliente que entra por la puerta.'],
                    ['La regla: se compara el margen por HORA DE SALA dando '
                     'taller contra el margen por hora de sala vendiendo. Si '
                     'el taller ocupa el espacio de venta en hora punta, puede '
                     'salir caro aunque llene.',
                     'Y el criterio estacional, que es lo que lo hace '
                     'interesante en este oficio: es la única línea que '
                     'funciona en agosto y la única que no depende del precio '
                     'del cacao.'],
                    ['La hoja de talleres y regalo corporativo del plan '
                     'financiero da los asistentes necesarios para cubrir el '
                     'coste y el margen por hora de sala en las dos '
                     'situaciones, con su veredicto.',
                     'Y da la comprobación interna: cuántos talleres al mes '
                     'hacen falta para que la línea pese lo que el plan dice '
                     'que pesa.'],
                    ['La norma que aplica, y con su límite dicho: un taller de '
                     'bombonería NO está exento del impuesto sobre el valor '
                     'añadido por ser formación. Eso está cerrado.',
                     'Lo que NO está cerrado es el tipo aplicable, y por eso '
                     'este documento no publica ninguno: se consulta con la '
                     'asesoría antes de poner precio, no después de haberlo '
                     'cobrado.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Precio por persona que cobra el caso modelado', f'{X_PLAN}!Talleres y Regalo Corporativo!B8', 'eur2'),
                    C('Aforo del taller', f'{X_PLAN}!Talleres y Regalo Corporativo!B9', 'num'),
                    C('Asistentes necesarios para cubrir el coste del docente', f'{X_PLAN}!Talleres y Regalo Corporativo!B19', 'num1'),
                    C('Asistentes necesarios contando también el material', f'{X_PLAN}!Talleres y Regalo Corporativo!B20', 'num1'),
                    C('Margen por hora de sala dando taller', f'{X_PLAN}!Talleres y Regalo Corporativo!B26', 'eur2'),
                    C('Margen por hora de sala vendiendo', f'{X_PLAN}!Talleres y Regalo Corporativo!B29', 'eur2'),
                    C('Veredicto de la hora de sala', f'{X_PLAN}!Talleres y Regalo Corporativo!B31', 'txt'),
                    C('Ingresos de talleres al año', f'{X_PLAN}!Talleres y Regalo Corporativo!B36', 'eur'),
                    C('Tipo de impuesto del taller que usa el plan', f'{X_PLAN}!0. Supuestos!B17', 'txt'),
                ],
                'sector': ['CHS-30', 'CHS-11', 'CHN-71b'],
                'tablas': [{
                    'titulo': 'El taller, del precio por persona al margen por hora de sala (plan-financiero-3-anos-chocolateria.xlsx, hoja «Talleres y Regalo Corporativo»)',
                    'src': (X_PLAN, 'Talleres y Regalo Corporativo'),
                    'cols': [('Concepto', 'A', 'txt'), ('Valor', 'B', 'num2'),
                             ('Unidad', 'C', 'txt')],
                    'filas': (23, 31),
                    'nota': 'La comparación que decide es la de las dos últimas filas de margen '
                            'por hora. El tipo impositivo del taller va sin cifra a propósito: '
                            'lo único cerrado es que no está exento.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO publicar un tipo impositivo para el taller.',
                ],
            },
            {
                'n': 11,
                'titulo': 'Empezar en Casa Dentro de la Legalidad',
                'resumen_indice': 'qué puedes vender desde una vivienda, qué no, y de qué depende que la puerta esté abierta.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver la pregunta con la que llega media '
                            'audiencia de este producto: si se puede empezar '
                            'haciendo bombones en casa y venderlos, y bajo qué '
                            'condiciones.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: alguien lleva dos años haciendo bombones '
                     'por encargo en su cocina y quiere facturar sin montar '
                     'local. Busca en internet y encuentra dos respuestas '
                     'opuestas, las dos tajantes.',
                     'Lo que casi nadie explica bien: la respuesta no es sí ni '
                     'no, es «depende de tu comunidad autónoma», y el motivo '
                     'está en una lista cerrada con una letra abierta al '
                     'final.'],
                    ['Opción A: esperar y montar obrador. Opción B: comprobar '
                     'si tu comunidad ha ampliado la lista y, si lo ha hecho, '
                     'seguir esa vía. Opción C: alquilar horas de un obrador '
                     'ajeno legalizado, que es la salida que casi nadie '
                     'menciona.',
                     'Lo que cambia en cada una: el tiempo hasta la primera '
                     'factura, la inversión y el techo de producción, que en '
                     'la vía doméstica es bajo por definición.'],
                    ['La regla: se empieza por la pregunta de la comunidad '
                     'autónoma, no por los kilos. Si tu comunidad no ha '
                     'ampliado la lista, los umbrales de producción no se '
                     'llegan a activar.',
                     'Y el criterio de crecimiento: la vía doméstica tiene un '
                     'techo de volumen proporcional al tamaño de las '
                     'instalaciones, así que es una rampa de salida, no un '
                     'destino.'],
                    ['La hoja de ruta doméstica del libro legal empieza '
                     'preguntando por tu comunidad y sólo activa los tres '
                     'requisitos de producción si la respuesta abre la puerta.',
                     'Y da el veredicto escrito, que es la frase que hay que '
                     'poder repetir delante de un inspector sin equivocarse.'],
                    ['La lista estatal tiene CINCO letras, y por defecto el '
                     'bombón no encaja en la de panadería y repostería. Ese '
                     'paso es una interpretación nuestra y así se presenta.',
                     'La quinta letra es la que decide: otros alimentos que '
                     'las autoridades competentes de las comunidades autónomas '
                     'permitan en sus territorios. Hay comunidades que ya la '
                     'han ejercido, y la palabra exacta de su lista importa.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('¿Ha ampliado tu comunidad la lista por la letra abierta?', f'{X_LEGAL}!Ruta Doméstica!B7', 'txt'),
                    C('Lectura de esa respuesta', f'{X_LEGAL}!Ruta Doméstica!B9', 'txt'),
                    C('Tope absoluto de kilos a la semana', f'{X_LEGAL}!Ruta Doméstica!B23', 'num'),
                    C('Kilos por metro cuadrado que saldrían en el caso', f'{X_LEGAL}!Ruta Doméstica!B25', 'num2'),
                    C('Lectura del requisito de proporcionalidad', f'{X_LEGAL}!Ruta Doméstica!B26', 'txt'),
                    C('Veredicto de la ruta doméstica', f'{X_LEGAL}!Ruta Doméstica!B32', 'txt'),
                ],
                'sector': ['CHN-44', 'CHN-44-int', 'CHN-44b', 'CHN-87',
                           'PA-29c'],
                'tablas': [{
                    'titulo': 'Los tres requisitos de la vía doméstica, y en qué orden se comprueban',
                    'cabecera': ['Paso', 'Qué se comprueba', 'Si la respuesta es no'],
                    'filas': [
                        ['1. La puerta', '¿Tu comunidad autónoma ha ampliado la lista estatal por la letra abierta?', 'La vía doméstica no está abierta para el bombón: los pasos siguientes no llegan a activarse'],
                        ['2. El volumen proporcional', '¿La producción prevista es proporcional al tamaño de las instalaciones, de manera que se garanticen las prácticas correctas de higiene?', 'Hay que reducir la producción prevista o cambiar de vía: es el requisito que de verdad limita'],
                        ['3. El tope absoluto', '¿Estás por debajo del tope de kilos a la semana?', 'Fuera de la vía doméstica: ese tope es un techo, no un objetivo'],
                        ['4. La prueba', '¿Puedes demostrarlo documentalmente, con registro de producción y albaranes?', 'Sin poder demostrarlo, los otros dos requisitos no valen'],
                    ],
                    'nota': 'El orden importa: empezar por los kilos y no por la comunidad '
                            'autónoma sugiere que la vía existe cuando puede no existir. Y la '
                            'frase que hay que poder repetir es «no entra en la lista estatal '
                            'salvo que mi comunidad lo haya añadido», nunca «es ilegal en '
                            'España».',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO escribir «hacer bombones en casa para vender es '
                    'ilegal en España».',
                ],
            },
            {
                'n': 12,
                'titulo': 'Qué Haces con el Chocolate que no se Vende',
                'resumen_indice': 'refundir, donar o tirar, y qué te obliga la ley del desperdicio si eres microempresa.',
                'palabras': 875, 'bloques': 1,
                'objetivo': 'Resolver qué se hace con el producto que sobra: '
                            'qué vuelve a la cuba, qué se puede donar, qué se '
                            'tira y qué obligaciones hay detrás de cada opción.',
                'epigrafes': list(EPI_DEC),
                'puntos_por_epigrafe': PPE_DEC(
                    ['El caso típico: termina la campaña y quedan figuras, '
                     'cajas montadas y bombones a punto de caducar. Y la '
                     'decisión se toma con prisa, que es cuando peor se toma.',
                     'Lo que casi nadie calcula: cuánto cuesta al año esa '
                     'merma por caducidad, referencia a referencia. Medida, '
                     'casi siempre es menor de lo que se teme y está '
                     'concentrada en dos o tres referencias.'],
                    ['Opción A: refundir lo que se puede refundir. Opción B: '
                     'vender con descuento antes de la fecha. Opción C: donar '
                     'lo que siga siendo apto. Opción D: tirar, que es la '
                     'única que no recupera nada.',
                     'Lo que cambia en cada una: el valor recuperado, el '
                     'efecto sobre el precio percibido de tu producto y las '
                     'obligaciones documentales.'],
                    ['La regla del oficio, que es física y no opinable: el '
                     'chocolate sin relleno y sin contaminar se puede refundir; '
                     'el que lleva ganache o fruta, a residuo. Eso separa el '
                     'problema en dos mucho antes que cualquier norma.',
                     'Y la regla de negocio: la merma por caducidad no se '
                     'arregla al final, se arregla ajustando el tamaño de '
                     'tanda al principio. Lo que caduca es lo que se hizo de '
                     'más.'],
                    ['La hoja de lote y merma por caducidad del libro de vida '
                     'útil da la merma anual en euros y las referencias con la '
                     'tanda demasiado grande para lo que duran.',
                     'Y la hoja de merma de templado del libro de la carta da '
                     'los kilos que vuelven a la cuba y los que van a residuo, '
                     'con el coste de estos últimos.'],
                    ['La norma del desperdicio alimentario, bien leída: si '
                     'eres microempresa, el apartado que cierra ese artículo '
                     'te deja fuera de TODO él, plan de prevención y convenios '
                     'de donación incluidos. Lo que sigue en pie no es una '
                     'obligación tuya: es que cualquier cláusula contractual '
                     'que prohíba donar es nula de pleno derecho.',
                     'Y la otra cara, que casi nadie cuenta: esa exclusión NO '
                     'alcanza al artículo que obliga a facilitar que el cliente '
                     'se lleve lo que no ha consumido. Si sirves chocolate a '
                     'la taza y tienes mesas, ése te obliga aunque seas '
                     'microempresa.'],
                ),
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Merma por caducidad de toda la carta al año', f'{X_VIDA}!Lote y Merma por Caducidad!Q44', 'eur'),
                    C('Piezas que se caducan al año en toda la carta', f'{X_VIDA}!Lote y Merma por Caducidad!P44', 'num'),
                    C('Peso de esa merma sobre el coste de materia del año', f'{X_VIDA}!Lote y Merma por Caducidad!D47', 'pct1'),
                    C('Referencias con la tanda demasiado grande para lo que duran', f'{X_VIDA}!Lote y Merma por Caducidad!D46', 'num'),
                    C('Kilos al año de chocolate limpio que vuelven a la cuba', f'{X_CARTA}!Merma de Templado y Recortes!M35', 'num1'),
                    C('Coste anual de la merma que no se puede recuperar', f'{X_CARTA}!Merma de Templado y Recortes!O35', 'eur'),
                    C('Vida útil más corta de toda la carta, en días', f'{X_VIDA}!Vida Útil Declarada!G44', 'num'),
                ],
                'sector': ['CHN-64', 'CHN-92', 'CHN-38', 'CHN-63'],
                'tablas': [{
                    'titulo': 'Las cuatro salidas del producto que sobra, y qué obliga cada una',
                    'cabecera': ['Salida', 'Qué producto admite', 'Qué recuperas', 'Qué tienes que tener en cuenta'],
                    'filas': [
                        ['Refundir', 'Chocolate sin relleno y sin contaminar, recortes limpios de templado', 'Casi todo el valor de la materia', 'Es una regla física, no legal: el que lleva ganache o fruta no vuelve a la cuba'],
                        ['Vender con descuento antes de la fecha', 'Cualquier referencia apta, dentro de su vida útil declarada', 'Parte del margen', 'La regla del precio anterior condiciona cómo se anuncia un precio tachado'],
                        ['Donar', 'Producto apto para el consumo, dentro de su vida útil', 'Nada en caja, sí en destino', 'Si eres microempresa, el artículo del plan de prevención NO te obliga; y ninguna cláusula puede prohibirte donar'],
                        ['Residuo', 'Lo que lleva relleno, fruta o está fuera de fecha', 'Nada', 'Es el coste que la hoja de merma cuantifica, y el que se baja ajustando el tamaño de tanda'],
                    ],
                    'nota': 'Si sirves chocolate a la taza y tienes mesas, hay un artículo de la '
                            'misma ley que SÍ te obliga aunque seas microempresa: facilitar que '
                            'el cliente se lleve lo que no ha consumido.',
                }],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO escribir «si eres microempresa te siguen '
                    'obligando los apartados 2 y 5 del artículo 6» y '
                    'PROHIBIDO escribir «no te obliga nada de la ley de '
                    'desperdicio».',
                ],
            },
        ],
    },
]


# --------------------------------------------------------------------------
# Erratas permitidas: el detector de `documentos.py` toma por errata palabras
# correctas poco frecuentes en el corpus del blog. Se amplía MIRANDO EL
# CONTEXTO, nunca «corrigiendo» a ciegas. Hay que asignarla a GUIA **y a cada
# bonus por separado** (`_ERRATAS_OK` NO es una clave de `documentos.py`: es
# una variable local de este guion).
# --------------------------------------------------------------------------
_ERRATAS_OK = (
    # Vocabulario del oficio del chocolate
    'obrador', 'obradores', 'bombonería', 'bomboneria', 'bombonerías',
    'bombonerias', 'bombón', 'bombon', 'bombones', 'chocolatería',
    'chocolateria', 'chocolaterías', 'chocolaterias', 'chocolatero',
    'chocolatera', 'chocolateros', 'cobertura', 'coberturas',
    'atemperadora', 'atemperadoras', 'atemperar', 'atemperado', 'templado',
    'templar', 'temperador', 'mantenedor', 'enrobadora', 'enrobadoras',
    'enrobar', 'enrobado', 'bañado', 'banado', 'bañadora', 'moldeado',
    'moldear', 'desmoldeo', 'desmoldar', 'molde', 'moldes', 'policarbonato',
    'ganache', 'ganaches', 'praliné', 'praline', 'pralinés', 'pralines',
    'gianduja', 'trufa', 'trufas', 'garrapiñado', 'garrapinado',
    'garrapiñadas', 'confitada', 'confitadas', 'confite', 'confites',
    'gragea', 'grageas', 'tableta', 'tabletas', 'tableteado', 'cascarilla',
    'conchadora', 'concha', 'conchado', 'refinadora', 'melanger', 'winnower',
    'descascarilladora', 'tostador', 'tostado', 'sucedáneo', 'sucedaneo',
    'sucedáneos', 'manteca', 'desgrasada', 'cristalización', 'cristalizacion',
    'cristalizar', 'cristalizados', 'blanquea', 'blanqueado', 'brillo',
    'sorbitol', 'sorbato', 'glucosa', 'lecitina', 'barquillo', 'barquillos',
    'crujiente', 'crujientes', 'monodosis', 'mona', 'monas', 'roscón',
    'roscon', 'turrón', 'turron', 'turrones', 'panellets', 'mazapán',
    'mazapan', 'mazapanes', 'merengue', 'merengues', 'avellana', 'avellanas',
    'cacahuete', 'cacahuetes', 'sésamo', 'sesamo', 'marcona',
    # Vocabulario de local, obra e instalaciones
    'climatización', 'climatizacion', 'climatizada', 'climatizado',
    'deshumidificación', 'deshumidificacion', 'deshumidificar',
    'evaporativo', 'frigorífica', 'frigorifica', 'vitrina', 'vitrinas',
    'mostrador', 'mostradores', 'cámara', 'camara', 'nevera', 'abatidor',
    'acometida', 'desagüe', 'desague', 'lavamanos', 'fregadero', 'vestuario',
    'vestuarios', 'aseo', 'aseos', 'traspaso', 'traspasos', 'arrendamiento',
    'fianza', 'planeamiento', 'urbanístico', 'urbanistico', 'ordenanza',
    'ordenanzas', 'visado', 'boletín', 'boletin', 'legalización',
    'legalizacion', 'accesibilidad', 'estanquidad', 'combustión', 'combustion',
    'recirculación', 'recirculacion', 'transmitancia', 'renovaciones',
    'equilibrado', 'escaparate', 'rótulo', 'rotulo',
    # Vocabulario sanitario y normativo
    'autocontrol', 'alérgeno', 'alergeno', 'alérgenos', 'alergenos',
    'manipulador', 'manipuladores', 'ovoproducto', 'ovoproductos',
    'pasteurizado', 'congelación', 'congelacion', 'congelar', 'congelado',
    'descongelado', 'refrigerada', 'refrigerado', 'refrigeración',
    'refrigeracion', 'trazabilidad', 'trazable', 'perecedero', 'perecederos',
    'minorista', 'minoristas', 'sucursal', 'sucursales', 'titularidad',
    'habilitante', 'derogado', 'derogada', 'derogados', 'vigencia', 'vigente',
    'vigentes', 'consolidado', 'articulado', 'preceptivas', 'declaración',
    'declaracion', 'responsable', 'excedente', 'excedentes', 'donación',
    'donacion', 'donable', 'donar', 'redistribución', 'redistribucion',
    'desperdicio', 'microempresa', 'microempresas', 'reutilizable',
    'reutilizables', 'envasador', 'envasadora', 'envasar', 'envasado',
    'fraccionar', 'fraccionamiento', 'artesanal', 'artesanía', 'artesania',
    'acreditación', 'acreditacion', 'acreditable', 'acumulativas',
    'alternativas', 'marginal', 'localizado', 'restringido', 'cadmio',
    'ocratoxina', 'contaminante', 'contaminantes', 'analítica', 'analitica',
    'analíticas', 'analiticas', 'deforestación', 'deforestacion', 'diligencia',
    'debida', 'operador', 'operadores', 'comerciante', 'comerciantes',
    'importador', 'importadores', 'intracomunitaria', 'inscribirse',
    'inscrita', 'inscritos', 'inscripción', 'inscripcion',
    # Vocabulario económico, fiscal y laboral
    'escandallo', 'escandallos', 'escandallar', 'escandallada', 'costeo',
    'exhibidor', 'exhibidores', 'gramaje', 'gramajes', 'tanda', 'tandas',
    'merma', 'mermas', 'ponderado', 'ponderada', 'amortización',
    'amortizacion', 'amortizable', 'tesorería', 'tesoreria', 'circulante',
    'carencia', 'principal', 'cuota', 'cuotas', 'apalancamiento',
    'repercutido', 'soportado', 'liquidación', 'liquidacion', 'devengo',
    'epígrafe', 'epigrafe', 'epígrafes', 'epigrafes', 'convenio', 'convenios',
    'cotización', 'cotizacion', 'jornada', 'jornadas', 'contratación',
    'contratacion', 'dimensionado', 'estacionalidad', 'desestacionalizar',
    'inmovilizado', 'inmovilizada', 'incremental', 'payback', 'estimada',
    'proyectada', 'rotación', 'rotacion', 'surtido', 'surtidos',
    'antelación', 'antelacion', 'refuerzo', 'refuerzos', 'granel',
    'packaging', 'estuche', 'estuches', 'blíster', 'blister', 'blísteres',
    'blisteres', 'cápsula', 'capsula', 'cápsulas', 'capsulas',
    # Palabras correctas que el corpus del blog no contiene
    'comprobable', 'comprobables', 'defendible', 'refutable', 'medible',
    'escalable', 'reproducible', 'sustituible', 'sustituibles', 'editable',
    'editables', 'calibrado', 'calibradas', 'modelado', 'modelada',
    'tabulada', 'tabuladas', 'acotado', 'acotada', 'cribado', 'eliminatorio',
    'eliminatorios', 'holgura', 'solape', 'solapan', 'anticipo', 'anticipos',
    'anulación', 'anulacion', 'recogida', 'cupo', 'cupos', 'táper', 'taper',
    'meseta', 'papeleos', 'contraestacional', 'contraestacionales',
    'orientativo', 'orientativos', 'orientativas',
    # Siglas y nombres propios que el léxico no conoce
    'APPCC', 'RGSEAA', 'BOE', 'BOCM', 'DOGC', 'DOUE', 'CTE', 'RITE', 'IAE',
    'SMI', 'REGCON', 'Verifactu', 'Hosply', 'Almendra', 'Callebaut',
    'Valrhona', 'Selmi', 'Pavoni', 'Ugolini', 'Docriluc', 'Utilcentre',
    'Chocolate', 'World', 'RestorHome', 'SelfPackaging', 'Martellato',
)
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
