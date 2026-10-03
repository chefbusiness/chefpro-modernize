#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
guion_guia_churreria_chocolateria.py — GUION CERRADO de «Cómo Montar una
Churrería-Chocolatería» v1.0 (producto 51, pid `guia-churreria-chocolateria`,
65 €). SPEC: `scripts/productos-digitales/guia-churreria-SPEC.md` (§1-§6) con
las decisiones firmadas de `guia-churreria-DECISIONES-2026-10-03.md`
(D1-D26 y V-01…V-06).

MANDA LA D26 (firmada el 3-oct por el orquestador) SOBRE EL §4 DE LA SPEC.
La SPEC trae 19 capítulos + anexo; para entrar en presupuesto se funden TRES
pares de capítulos afines y quedan 16 capítulos + anexo = 17 bloques, más el
business plan en 2 bloques y las «12 decisiones» en 3 bloques de 4 = 22
BLOQUES. Correspondencia con el §4 de la SPEC (cada capítulo hereda las
hojas, los ids y las reglas de los que absorbe):

    01 ← 01 · 02 ← 02 · 03 ← 03 · 04 ← 04 · 05 ← 05 · 06 ← 06
    07 ← 07 + 14 (maquinaria + proveedores)                  FUNDIDO
    08 ← 08 · 09 ← 09 · 10 ← 10
    11 ← 11 + 12 (acrilamida y alérgenos + autocontrol)      FUNDIDO
    12 ← 13 · 13 ← 15
    14 ← 16 + 17 (temporada + ferias)                        FUNDIDO
    15 ← 18 · 16 ← 19 · A ← A (anexo, entrada 17, sin numerar)

Un bloque por capítulo, también en los fundidos: son más largos, no se parten.
Los tres fundidos llevan en sus `puntos_por_epigrafe` una FRONTERA explícita
entre sus dos mitades y con los capítulos vecinos (el riesgo medido de
desduplicación del Manual del Chef Ejecutivo fue ≈ 2,2 M de tokens).

MISMO ESQUEMA QUE LA HERMANA (`guion_guia_chocolateria_obrador.py`): a un
redactor no se le pide un capítulo con un título, se le pide con un guion
CERRADO — (a) objetivo, (b) 4-6 epígrafes, (c) los puntos de CADA epígrafe en
`puntos_por_epigrafe` (cada capítulo declara primero su `PPE_nn` y usa
`list(PPE_nn)` como `epigrafes`, así que no pueden discrepar), (d) las cifras
del propio pack con `C(etiqueta, 'fichero.xlsx!Hoja!Celda', fmt)`, que
`documentos.py` resuelve con openpyxl `data_only` antes de escribir el prompt,
(e) los datos del sector por id de `auditorias/guias-v2-research-sector.json`
(837 entradas tras la fusión del 3-oct: `CUN-*` normativa y `CUS-*` sector de
este producto, `CHN-*`/`CHS-*` reutilizados de la hermana, `FC-IVA-*` de la
Guía Food Cost), (f) las tablas, que construye el maquetador desde el xlsx, y
(g) lo que NO debe decir.

FUENTE ÚNICA DE CIFRAS: los OCHO libros de
`astro-site/public/dl/guia-churreria-chocolateria/`, que se leen y no se tocan.
Mientras F2 los refuta, viven en `guia-churreria/build/`; sus mapas
(`build/mapa-<libro>.json`, etiqueta → `fichero.xlsx!Hoja!Celda`) son el
CONTRATO. Por eso `C()` lleva, además de la referencia, la ETIQUETA DEL MAPA
(`clave=`) o, si la celda no está en el mapa, el RÓTULO de su fila
(`rotulo=(celda, texto)`), y cada tabla del xlsx lleva su `ancla`: ninguna de
las dos cosas viaja a `documentos.py` (que sólo lee la tupla de tres y las
claves conocidas de la tabla); las usa `guia-churreria/verificar_guion.py`
para cazar cualquier referencia que se haya movido al regenerar un libro.

FUENTE ÚNICA DE LO LEGAL: `auditorias/guia-churreria-verificacion-legal-
2026-10-03.md` y `.json` (46 fichas `CUN-*`, cerrada el 3-oct con V-01…V-06
resueltas) y, para los `CHN-*` reutilizados, la de la hermana del 12-09-2026.
Los puntos legales de los capítulos 04, 05, 09, 10, 11, 13 y 14 y del anexo
usan la REDACCIÓN SEGURA de esas fichas (su `nota`), no la síntesis del
research. Lo que la verificación deja en `-EXCLUIDOS.json` (V-02, V-04,
humos fuera de Madrid, ruido, terrazas, vertido, calificación ambiental,
tablas de otras provincias, registro horario digital…) NO existe como
afirmación: se trata como «pregunta a tu ayuntamiento, a tu asesoría o a un
laboralista».

DESVIACIONES DECLARADAS (y por qué):
  · `cifras_ignorar` va VACÍA, aunque la SPEC §5 diga «lista negra como
    `cifras_ignorar` + `prohibido`». `coherencia_cifras()` de `documentos.py`
    trata esa clave como lista de SILENCIADO: lo que entra deja de saltar el
    gate. Meter ahí «107.000» o «85-90» sería blanquearlas (lección escrita en
    el guion de la hermana). La lista negra va ÍNTEGRA en `NO_COMUN` (cada
    entrada con su ORIGEN en `LISTA_NEGRA_GUION`, para que el gate compruebe
    que no falta ni una) y sus cadenas en `LISTA_NEGRA_AGUJAS`, que el gate
    barre sobre el guion y, con `--txt`, sobre los bloques ya redactados.
  · El business plan da el resultado ANTES de impuestos: el libro 6 no calcula
    Sociedades ni IRPF (dependen de la forma jurídica, `PyG 3 Años!E23`). El
    resumen ejecutivo lo dice así, junto al margen y al punto de equilibrio.
  · Ids del §4 de la SPEC que NO van en `sector`, porque su `dato` (que el
    redactor ve aunque sea como hueco) trae una cifra de la lista negra o
    choca con la cifra de la celda: `CUS-26` («540 kg/h», N-8), `CUS-30`
    (el «poquito más del 50 %» llega por su celda de `3!Los Dos Márgenes`,
    con su atribución), `CUS-58`/`CUS-59` (cálculos propios de fiabilidad
    baja: las dotaciones llegan por sus celdas del libro 2), `CUS-31f` (sin
    URL), `CUS-14` («150 franquicias»), `CUS-47` (el «desde 75.000»),
    `CUS-M16`/`CUS-M18` (facturaciones esperadas del franquiciador),
    `CUN-13` (la rebaja de cuota de temporada: entra sólo `CUN-10`, en una
    línea del capítulo 09, A3) y `CUS-10` («sin gluten» como argumento).
  · Ningún id de `IDS_PROHIBIDOS` (§2.3 de la SPEC) aparece en el guion, ni
    siquiera dentro de las prohibiciones: lo prohibido se describe en
    palabras, y las cifras vetadas van escritas con letra.

PRESUPUESTO (D26): guía 29.300 palabras en 16 capítulos + anexo (80 páginas
prometidas, mínimo 1.100 por capítulo); business plan 3.500 palabras en 2
bloques con 10 tablas; «12 decisiones» 6.600 palabras en 3 bloques de 4
(20 páginas prometidas, mínimo 400 por capítulo).

Gate de forma, que se corre ANTES de gastar un token de redacción:
    /usr/local/bin/python3 scripts/productos-digitales/guia-churreria/verificar_guion.py

Via: Claude Code
"""

PID = 'guia-churreria-chocolateria'

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
    'técnico de la extracción ni a ninguno de los que te va a pedir tu '
    'ayuntamiento. El marco normativo que se explica es el ESPAÑOL, y su '
    'estado se comprobó contra las fuentes oficiales —Boletín Oficial del '
    'Estado, Diario Oficial de la Unión Europea, Boletín Oficial de la '
    'Comunidad de Madrid, el Código Técnico de la Edificación y el registro de '
    'convenios colectivos— el 3 de octubre de 2026, salvo las normas que ya '
    'había verificado la guía hermana de chocolatería, que se comprobaron el '
    '12 de septiembre de 2026: cada afirmación legal lleva su norma y su '
    'artículo para que puedas comprobarla y para que sepas dónde mirar cuando '
    'cambie. Los ejemplos municipales y laborales (humos, horario y convenio) '
    'son los de la Comunidad de Madrid, el único marco que se ha verificado '
    'para este producto: no se extrapolan, y lo que depende de tu '
    'ayuntamiento o de tu comunidad —la licencia de obra, las terrazas, las '
    'tasas, el ruido, el vertido— se trata como una pregunta que tienes que '
    'hacer, nunca como un dato. Las superficies, importes, precios, gramajes, '
    'márgenes, plazos y horarios del caso que recorre el documento son '
    'valores de ejemplo de una churrería-chocolatería modelada, «El Molinete», '
    'que acompaña a este pack, y viven en celdas editables de las hojas de '
    'cálculo precisamente para que los sustituyas por los tuyos: ninguno es '
    'una previsión de tus resultados, ni un estándar del sector, ni una '
    'promesa de rentabilidad. Antes de firmar un alquiler, encargar una obra, '
    'presentar un trámite, fijar un precio o contratar a alguien, contrasta '
    'con tu ayuntamiento, con tu asesoría y con la autoridad sanitaria de tu '
    'comunidad.*')

GUIA = {
    'pid': PID,
    'titulo': 'Cómo Montar una Churrería-Chocolatería',
    'subtitulo': 'Local, freidora, churros, chocolate a la taza y números: el '
                 'dossier completo de apertura · Guía España 2026',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Cómo Montar una Churrería-Chocolatería',
    'fecha': 'octubre de 2026',
    'version': '1.0',
    'tipo_doc': 'guía',
    'tipo_doc_art': 'de la guía',
    'tipo_doc_dem': 'esta guía',
    'categoria_doc': 'Guía profesional',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        'Dieciséis capítulos, un anexo normativo fechado, ocho herramientas en '
        'Excel con fórmulas vivas, un business plan relleno y doce decisiones '
        'de apertura resueltas, para quien todavía NO ha abierto: quien quiere '
        'montar su primera churrería, quien va a coger el traspaso de un '
        'churrero que se jubila, el feriante que quiere un local y el que '
        'piensa en churros en invierno y helado en verano. No te enseña a '
        'freír, no es un recetario y no sustituye al proyecto técnico de la '
        'extracción: te dice qué decidir y en qué orden. Si ese local admite '
        'una freidora, cuánto cuesta abrir de verdad, a cuánto vender la '
        'ración y la taza, cuánta madrugada te toca y qué haces en verano. '
        'Todas las cifras del caso salen de los libros de este mismo pack, así '
        'que el texto y las hojas de cálculo dicen lo mismo; y cada afirmación '
        'legal va con su norma, su artículo y su enlace, comprobados el 3 de '
        'octubre de 2026.'),
    'gates': {
        # D26: 16 capítulos + anexo, 29.300 palabras de guion.
        'paginas_prometidas': 80,
        'palabras_objetivo': 29300,
        'min_palabras_cap': 1100,
        # Cifras con separador de miles que el texto puede escribir y que no
        # están en ninguna celda de los ocho libros ni en el research: hoy
        # ninguna. `valores_admitidos()` ya acepta todo número de una celda o
        # del `cifra`, la `cita_literal`, la `nota`, el `dato` o el
        # `fuente_titulo` de cualquier id.
        'cifras_extra': (),
        # VACÍA A PROPÓSITO (ver «DESVIACIONES DECLARADAS» arriba): esta clave
        # SILENCIA el gate de coherencia. La lista negra vive en NO_COMUN y en
        # LISTA_NEGRA_AGUJAS.
        'cifras_ignorar': (),
        # «cerrar en verano», «la tienda cierra a las 21:00»: horario y
        # temporada, no mortalidad de negocios. La guía no escribe ninguna
        # cifra de cierre ni de fracaso (lo prohíbe NO_COMUN).
        'mortalidad_permitida': ['cierra', 'cierran'],
        # Se rellena al FINAL del fichero con `_ERRATAS_OK`: a GUIA **y a cada
        # bonus por separado**, o el bonus se queda sin ella.
        'erratas_permitidas': (),
        'erratas_forzadas': {},
    },
}

# --------------------------------------------------------------------------
# Los ocho libros del pack (SPEC §2.1, nombres firmados). Se referencian por
# NOMBRE de fichero: documentos.py los busca en astro-site/public/dl/<pid>/.
# Cambiar un nombre rompe todas las referencias de este guion.
# --------------------------------------------------------------------------
X_PROD = 'produccion-hora-punta-y-local.xlsx'            # libro 1
X_CAPEX = 'calculadora-capex-churreria.xlsx'             # libro 2
X_CARTA = 'carta-de-apertura-y-escandallo-churro.xlsx'   # libro 3
X_ACEITE = 'aceite-de-fritura-coste-y-cambio.xlsx'       # libro 4
X_TEMP = 'temporada-franjas-y-ferias.xlsx'               # libro 5
X_PLAN = 'plan-financiero-3-anos-churreria.xlsx'         # libro 6
X_LEGAL = 'checklist-legal-fritura-y-licencias.xlsx'     # libro 7
X_TURNOS = 'turnos-plantilla-y-madrugada.xlsx'           # libro 8

# --------------------------------------------------------------------------
# Pie obligatorio de toda tabla que fije un dato legal. Fechas y URL de la
# verificación legal del 3-oct (CUN) y de la hermana del 12-sep (CHN).
# --------------------------------------------------------------------------
V_LEY12 = ('Verificado el 03-10-2026 · Ley 12/2012 (BOE-A-2012-15595), '
           'arts. 2.1, 2.2, 3.3 y 3.4 y su Anexo, que incluye el epígrafe 644.6 '
           'y ningún grupo de la agrupación de restauración · '
           'https://www.boe.es/buscar/act.php?id=BOE-A-2012-15595')
V_HORARIO = ('Verificado el 03-10-2026 · Orden de 21 de abril de 2022 de la '
             'Comunidad de Madrid sobre horarios de establecimientos abiertos '
             'al público (BOCM de 29-04-2022). Es el EJEMPLO de Madrid y no se '
             'extrapola · https://www.bocm.es/boletin/CM_Orden_BOCM/2022/04/29/'
             'BOCM-20220429-10.PDF')
V_CTE = ('Verificado el 03-10-2026 · Código Técnico de la Edificación, DB-SI, '
         'sección SI 1, tabla 2.1 y sus notas (2) y (3), y sección SI 4, '
         'tabla 1.1 · https://www.codigotecnico.org/pdf/Documentos/SI/DBSI.pdf')
V_OCAS = ('Verificado el 03-10-2026 · Ordenanza 4/2021 de Calidad del Aire y '
          'Sostenibilidad de Madrid, arts. 23, 24 y 33 (BOCM de 16-04-2021). '
          'Sólo Madrid está verificado · https://www.bocm.es/boletin/'
          'CM_Orden_BOCM/2021/04/16/BOCM-20210416-46.PDF')
V_ACEITE = ('Verificado el 03-10-2026 · Orden de 26 de enero de 1989, Norma de '
            'Calidad para los Aceites y Grasas Calentados (BOE-A-1989-2265), '
            'arts. 3, 6 y 9 y anexo 1; arts. 7, 8, 10, 11 y 12 derogados · '
            'https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265')
V_ACRIL = ('Verificado el 03-10-2026 · Reglamento (UE) 2017/2158, arts. 1.2, '
           '2.2 y 2.3 y anexo II, y Recomendación (UE) 2019/1888 · '
           'https://www.boe.es/doue/2017/304/L00024-00044.pdf')
V_IAE = ('Verificado el 03-10-2026 · RDLeg 1175/1990 (BOE-A-1990-23930), '
         'epígrafes 644.6, 663.1 y 419.3 y grupos 673, 675 y 676 con sus '
         'notas, y regla 4.ª de la Instrucción · '
         'https://www.boe.es/buscar/act.php?id=BOE-A-1990-23930')
V_SANITARIO = ('Verificado el 12-09-2026 (guía hermana) y el 03-10-2026 · '
               'RD 191/2011, art. 2.2, en la redacción del RD 1021/2022, y '
               'RD 1021/2022, arts. 2 y 3 · '
               'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681')
V_ET = ('Verificado el 03-10-2026 · Estatuto de los Trabajadores (RDLeg 2/2015, '
        'BOE-A-2015-11430), art. 36.1 · '
        'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430')
V_CONVENIO = ('Verificado el 03-10-2026 · Convenio de Hostelería y Actividades '
              'Turísticas de la Comunidad de Madrid, código 28002085011981 '
              '(BOCM de 06-04-2024), arts. 5, 26 y 27: vencido el 31-12-2025 '
              'y en negociación, se aplican sus tablas mientras no se publique '
              'el nuevo · https://www.bocm.es/boletin/CM_Orden_BOCM/2024/04/06/'
              'BOCM-20240406-2.PDF')
V_FERIAS = ('Verificado el 03-10-2026 · Ley 7/1996 de Ordenación del Comercio '
            'Minorista, arts. 53 a 55; RD 199/2010 DEROGADO desde el '
            '07-08-2021; RD 1021/2022, art. 2.2; Reglamento (CE) 852/2004, '
            'anexo II, capítulo III; RD 919/2006 · '
            'https://www.boe.es/buscar/act.php?id=BOE-A-1996-1072')


# --------------------------------------------------------------------------
# Cifras del pack. `C()` devuelve la tupla de TRES que lee documentos.py; el
# ancla (etiqueta del mapa o rótulo de la fila) se guarda aparte, en ANCLAS,
# para que verificar_guion.py cace una referencia que se haya movido.
# --------------------------------------------------------------------------
ANCLAS = []


def C(etiqueta, ref, fmt='eur2', clave=None, rotulo=None):
    """(etiqueta, 'fichero.xlsx!Hoja!Celda', formato).

    `clave`: etiqueta de la celda en `guia-churreria/build/mapa-<libro>.json`.
    `rotulo`: (celda, texto con el que empieza), para la celda que no está en
    el mapa: el gate lee ese rótulo en la misma hoja y comprueba que no se ha
    movido. Una de las dos es obligatoria (lo exige el gate)."""
    ANCLAS.append((ref, clave, rotulo))
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos, en el anexo y en
# los dos bonus. Cada entrada lleva su ORIGEN (sección de la SPEC, número de
# la lista negra del research o regla de la casa) para que verificar_guion.py
# compruebe que la lista negra del §5 está ÍNTEGRA. En este orden: (1) higiene
# de citación legal, (2) régimen de cifras, (3) las doce prohibiciones de la
# verificación legal del 3-oct (§5.1), (4) el resto de la lista negra (§5.2),
# (5) las cifras N-1 a N-21 y (6) las afirmaciones y errores de método del
# §15.2 del research, (7) el ámbito y las fronteras del producto y (8) el
# vocabulario del §6 y el tono. Las cifras vetadas van ESCRITAS CON LETRA y
# sin ids: lo prohibido no le llega al redactor con los dígitos que podría
# copiar.
# --------------------------------------------------------------------------
LISTA_NEGRA_GUION = [
    # ---- 1. Higiene de citación legal ------------------------------------
    ('cita-1',
     'Las letras y apartados de un artículo se escriben «letra c» o «apartado '
     '3», NUNCA «c)» ni «3)»: un paréntesis de cierre suelto se lee como una '
     'errata.'),
    ('cita-2',
     'Los números de las normas se copian TAL CUAL, sin separador de miles: '
     '«Ley 12/2012», «RDLeg 1175/1990», «RD 10/2025», «Ley 37/1992», «RD '
     '650/2011», «Ley 7/1996», «RD 1021/2022», «RD 191/2011», «RD 1086/2020», '
     '«Reglamento (CE) 852/2004», «Reglamento (UE) 2017/2158», «Recomendación '
     '(UE) 2019/1888», «RD 919/2006», «RD 513/2017», «Ley 7/2022», «RDLeg '
     '2/2015», «RD 1055/2003», «RD 126/2015», «Reglamento (UE) 1169/2011», «RD '
     '1007/2023», «RD 126/2026» y «Ordenanza 4/2021»; nunca «RD 1.055/2003».'),
    ('cita-3',
     'La norma española del chocolate tiene UN ARTÍCULO ÚNICO: sus divisiones '
     'son apartados de la Reglamentación técnico-sanitaria que aprueba. Se '
     'escribe «el apartado 1.11 de la Reglamentación del RD 1055/2003» y está '
     'PROHIBIDO «el artículo 11 del RD 1055/2003», que no existe.'),
    ('cita-4',
     'TODA afirmación legal va con su norma y su artículo la primera vez que '
     'aparece en el capítulo («el art. 36.1 del Estatuto de los '
     'Trabajadores», «el art. 3.3 de la Ley 12/2012»), nunca «es obligatorio» '
     'a secas. Y se dice «comprobado el 3 de octubre de 2026», que es la fecha '
     'de corte de esta edición (las normas que ya verificó la guía de '
     'chocolatería, el 12 de septiembre de 2026).'),
    ('cita-5',
     'Sólo se entrecomilla lo que está literalmente en el boletín o en el '
     'diario oficial. Lo que es interpretación se presenta como '
     'interpretación, con esas palabras y con su nivel («es una inferencia: '
     'confírmalo con tu ayuntamiento»), y lo que viene de una guía '
     'administrativa o de una nota sindical se cita como guía o como nota, '
     'nunca entrecomillado como si fuera articulado.'),
    ('cita-6',
     'NO cites una celda de una hoja de cálculo con la sintaxis de Excel '
     '(«Parámetros!B16», «Cuello de Botella!B7»). Se nombra el libro y la hoja '
     'en lenguaje normal: «la hoja Cuello de Botella del libro de producción y '
     'local».'),
    ('cita-7',
     'Lo que depende del ayuntamiento o de la comunidad autónoma (el modelo '
     'de licencia de actividad de un local con mesas, la licencia de obra, '
     'las terrazas, las tasas, el ruido, el vertido, la calificación '
     'ambiental) es una PREGUNTA que hace el lector, nunca un dato. El único '
     'marco municipal y laboral verificado es el de Madrid, y se presenta '
     'siempre como EJEMPLO que no se extrapola.'),
    # ---- 2. Régimen de cifras ---------------------------------------------
    ('cifras-1',
     'NO escribas ninguna cifra, porcentaje, temperatura, superficie, '
     'potencia, plazo, umbral, importe ni sanción que no esté en la lista de '
     'cifras del producto o en los datos del sector que te doy. Ni «ronda '
     'los», ni «suele estar en», ni un ejemplo inventado para ilustrar. Si '
     'necesitas un número y no lo tienes, la frase se escribe sin número.'),
    ('cifras-2',
     'NO hagas cuentas nuevas con las cifras que te doy: no sumes, no restes, '
     'no calcules porcentajes, no conviertas raciones en euros y no proyectes '
     'a doce meses para escribir un total que no te he dado. Los totales ya '
     'están calculados en los libros. La única excepción es la que un punto '
     'del capítulo autorice expresamente.'),
    ('cifras-3',
     'Un dato del sector marcado como HUECO, sin cifra o de fiabilidad baja, '
     'NO se rellena: se dice que no hay dato público y se explica qué habría '
     'que preguntar o medir para tenerlo. Eso es contenido, no una carencia.'),
    ('cifras-4',
     'NO cites ninguna encuesta, informe, escuela, consultora, foro ni '
     'proveedor de software que no venga en los datos del sector de este '
     'capítulo.'),
    ('cifras-5',
     'Los SUPUESTOS DECLARADOS del caso —los gramos por pieza, la absorción '
     'de aceite, la densidad del aceite, los días entre cambios de aceite, '
     'los kilos de masa por hora de la línea, las raciones de cada día, los '
     'coeficientes de cada mes, el reparto por franjas, el mix de canales, '
     'los gastos fijos y el horario— se escriben SIEMPRE como supuesto de El '
     'Molinete que el lector sustituye por el suyo, nunca como un dato del '
     'sector ni como «lo normal en una churrería».'),
    ('cifras-6',
     'Todo precio publicado de otra churrería va con su sitio y su año en la '
     'misma frase: una carta de una ciudad en un año no es «el precio de la '
     'ración en España».'),
    # ---- 3. Las doce prohibiciones de la verificación legal (SPEC §5.1) ----
    ('5.1-1',
     'PROHIBIDO escribir «la ley te obliga a controlar la acrilamida de los '
     'churros», «cumplimiento acrilamida» o que la parte B del reglamento de '
     'la acrilamida aplica «a las franquicias» sin sus tres condiciones. Lo '
     'que dice la norma: el churro no aparece en la lista del art. 1.2 del '
     'Reglamento (UE) 2017/2158, que no define «bollería», así que no se '
     'puede afirmar ni que entre ni que quede fuera; controlarla en el churro '
     'es BUENA PRÁCTICA; la parte A del anexo II te alcanza si fríes patatas '
     'frescas; y la parte B, sólo si operas bajo marca o licencia, como parte '
     'de un funcionamiento interconectado y siguiendo las instrucciones de '
     'quien te suministra de forma centralizada (art. 2.3).'),
    ('5.1-2',
     'PROHIBIDA CUALQUIER temperatura de fritura del churro, sea la que sea. '
     'No hay fuente primaria que la fije y este pack no da ninguna. La única '
     'temperatura de fritura que trae la norma es la de las PATATAS fritas '
     'del reglamento de la acrilamida: si la nombras, di en la misma frase '
     'que es para patatas y que para el churro no hay ninguna.'),
    ('5.1-3',
     'PROHIBIDO escribir en el texto un tipo de IVA para el chocolate a la '
     'taza para llevar (ni el reducido ni el general). Es una zona gris: con '
     'leche no encaja en la definición de bebida refrescante y con agua y un '
     'preparado azucarado podría leerse como tal; no hay consulta vinculante '
     'localizada. Se dice que el libro de la carta lo lleva en una CELDA '
     'VERDE con su aviso y que el tipo lo fija tu asesor.'),
    ('5.1-4',
     'PROHIBIDO escribir «el despacho va por declaración responsable» sin '
     'añadir en la misma frase que las obras que requieren proyecto —el '
     'conducto de extracción a cubierta incluido— siguen necesitando su '
     'licencia de obra y su técnico. Y PROHIBIDO «necesitas licencia» o «no '
     'necesitas licencia» sin decir de QUÉ: la actividad, la obra y la '
     'terraza son tres papeles distintos.'),
    ('5.1-5',
     'PROHIBIDO citar artículos del RD 199/2010 de venta ambulante (DEROGADO '
     'desde agosto de 2021) o de la orden de horarios de Madrid de 1998 '
     '(derogada por la de abril de 2022), y PROHIBIDO citar el art. 8 de la '
     'norma de los aceites calentados como regla de rellenado: está derogado, '
     'y el art. 9, que sigue vivo, prohíbe añadir sustancias extrañas al baño '
     'y vender el aceite usado para uso alimentario.'),
    ('5.1-6',
     'PROHIBIDO escribir «convenio de churrerías», «la categoría de '
     'churrero» o «no existe convenio de churrerías». La búsqueda no fue '
     'exhaustiva: no se puede afirmar ni que exista ni que no. Lo que se '
     'dice: el acuerdo estatal de hostelería nombra freidurías, quioscos y '
     'chocolaterías; el de Madrid es un EJEMPLO; al menos un convenio '
     'provincial nombra los obradores de masas fritas; y el puesto se encaja '
     'en un nivel por ASIMILACIÓN DE FUNCIONES, que confirma tu asesor.'),
    ('5.1-7',
     'PROHIBIDO escribir que el churrero que entra a las cuatro o a las '
     'cinco de la mañana es trabajador nocturno, y PROHIBIDO confundir el '
     'plus de nocturnidad del convenio con el trabajador nocturno del '
     'Estatuto. Son DOS figuras: trabajador nocturno es quien hace '
     'normalmente al menos tres horas diarias entre las 22:00 y las 6:00 (o '
     'un tercio de su jornada anual), y sólo a él le alcanzan la prohibición '
     'de horas extraordinarias y el tope de ocho horas de promedio; el plus '
     'lo paga el convenio por las horas de sus franjas. Quien entra a las '
     '4:30 tiene hora y media en el periodo del Estatuto: no es trabajador '
     'nocturno y sí cobra plus.'),
    ('5.1-8',
     'PROHIBIDO presentar la rebaja de cuota de los establecimientos de '
     'temporada del impuesto de actividades como salida del verano o como '
     'ahorro, PROHIBIDO dar ninguna cuota del impuesto de actividades y '
     'PROHIBIDO usar la tasa de feria de un pueblo pequeño como orden de '
     'magnitud. Casi nadie paga ese impuesto (exención por debajo del millón '
     'de euros de cifra de negocio) y cerrar julio y agosto no es abrir seis '
     'meses o menos.'),
    ('5.1-9',
     'PROHIBIDO dar los requisitos de humos de Barcelona, Sevilla o Valencia '
     '(sólo se ha verificado Madrid), escribir que el medidor de polares de '
     'mano «demuestra» que cumples el límite legal (el límite se prueba en '
     'laboratorio con el método del anexo 1 de la norma) y escribir que una '
     'bombona pequeña te evita la instalación receptora de gas en un local o '
     'en un despacho.'),
    ('5.1-10',
     'PROHIBIDO dar como regla cierta que «con un preparado que no cumple, '
     'ni chocolate a la taza ni chocolate» o que «la carta sólo puede '
     'llamarlo así si el preparado cumple»: de ningún artículo sale. La '
     'fórmula es «qué preparado compras y qué dice su etiqueta» y, con menos '
     'del mínimo de cacao o con grasa vegetal declarada, «consulta a tu '
     'servicio de consumo antes de imprimir la carta». PROHIBIDO también '
     '«sin gluten» como argumento de carta, «carnet de manipulador» y '
     'escribir que el cucurucho de cartón cumple la ley de plásticos sin '
     'conocer su composición.'),
    ('5.1-11',
     'PROHIBIDAS estas cifras: el margen del churro de ochenta y cinco a '
     'noventa por ciento; los traspasos de ciento siete mil y de ciento veinte '
     'mil euros y los anuncios reeditados durante años; el curso de doscientos '
     'noventa euros; el cincuenta por ciento usado como margen bruto o '
     'atribuido a «una dueña»; los sueldos de los agregadores de ofertas de '
     'empleo y el coste de personal del artículo de un proveedor de TPV; los '
     'quinientos cuarenta kilos por hora de un folleto; «absorbe un treinta '
     'por ciento menos» y «dura el doble»; la «docena a doce euros»; el '
     '«facturamos sesenta mil euros» de un feriante; los objetivos de '
     'expansión de un franquiciador («ciento cincuenta franquicias»); y '
     '«Maestro Churrero desde setenta y cinco mil euros».'),
    ('5.1-12',
     'PROHIBIDO escribir «no existe ninguna guía de pago» (se dice «no hemos '
     'encontrado» o «ninguna de las que hemos leído»), dar un número de '
     'churrerías de España (no existe: la clasificación de actividades no '
     'tiene clase propia) y escribir «verificado contra el BOE» como '
     'argumento comercial.'),
    # ---- 4. Resto de la lista negra (SPEC §5.2) ----------------------------
    ('5.2-traspaso',
     'El techo de traspaso con sala es el del anuncio de Vallecas: precio '
     'PEDIDO y negociable, leído en el anuncio y no reabierto. PROHIBIDO un '
     'techo de noventa y cinco mil euros y PROHIBIDO tomar la lectura antigua '
     'de ese mismo anuncio como cifra de traspaso.'),
    ('5.2-nocturno',
     'PROHIBIDO aplicar «sin horas extra» o «máximo ocho horas de media» a '
     'quien no es trabajador nocturno del Estatuto.'),
    ('5.2-filtros',
     'PROHIBIDO dar la distancia de los filtros de la campana al foco sin '
     'distinguir el aparato: más de un metro veinte si es de gas o de '
     'parrilla, más de medio metro si es de otro tipo. Una freidora de gas '
     'pide la mayor.'),
    ('5.2-bombona',
     'PROHIBIDA la excepción de la bombona pequeña sin las palabras «de '
     'utilización móvil» y fuera de la caseta de feria: es para un único '
     'envase conectado a un solo aparato MÓVIL, y una freidora fija de un '
     'local no lo es.'),
    ('5.2-smi',
     'PROHIBIDO un salario por debajo del salario mínimo sin decir que el '
     'coste usa el salario mínimo como suelo, y PROHIBIDO presentar las '
     'ofertas de mercado como tabla de convenio: son un rango con las pagas '
     'sin declarar.'),
    ('5.2-brecha',
     'PROHIBIDO decir que entre Granada y el centro de Madrid el ticket se '
     'multiplica por cuatro: con chocolate, la plaza mueve el ticket '
     'alrededor de la mitad, y las dos cifras son de años distintos.'),
    ('5.2-50pct',
     'PROHIBIDO usar el «un poquito más del cincuenta por ciento» como margen '
     'bruto de la cuenta de resultados (contaría dos veces la mano de obra) y '
     'PROHIBIDO atribuirlo a una dueña: lo dice de palabra Javier, gestor de '
     'La Artesana, y es rentabilidad, no un margen sobre materia prima. El '
     'margen del plan sale del escandallo.'),
    ('5.2-posicion1',
     'PROHIBIDO usar como argumento que un contenido nuestro aparece el '
     'primero en el buscador.'),
    ('5.2-fuera-espana',
     'PROHIBIDO escribir «fuera de España no hay demanda» sin el matiz de '
     'México: allí sí se busca maquinaria de churros. La adaptación fuera de '
     'España se ofrece como servicio, sin promesa.'),
    ('5.2-comparativa',
     'PROHIBIDO comparar marcas o tipos de aceite («este aceite dura el '
     'doble»): el pack trabaja con TU aceite, TU precio y TU registro.'),
    ('5.2-post',
     'PROHIBIDAS las horquillas de inversión, de beneficio y de licencias que '
     'circulan por los contenidos gratuitos (incluido un artículo antiguo de '
     'nuestro propio blog): se copian unas a otras y no salen de ninguna '
     'suma. El pack da el modelo que produce la cifra del lector.'),
    ('5.2-casa',
     'PROHIBIDO «cien por cien legal», «válido en toda Hispanoamérica» y '
     'decir que AI Chef Pro tiene plan gratuito: no lo tiene; si hay que '
     'nombrar la plataforma, se dice «desde 10 euros al mes».'),
    ('5.2-metodo',
     'PROHIBIDOS cinco errores de método: dar un veredicto con un ratio '
     'cuando la pregunta es en euros; mezclar precios con y sin IVA en la '
     'misma tabla o en el mismo párrafo; presentar un precio «desde» como '
     'cifra cerrada; presentar un precio PEDIDO de traspaso como precio de '
     'cierre; y citar como literal o como testimonio lo que dijo alguien en '
     'una noticia.'),
    ('5.2-proyecciones',
     'PROHIBIDO presentar la facturación esperada o el plazo de recuperación '
     'que publica un franquiciador como un dato: es una proyección suya.'),
    # ---- 5. Cifras que no entran (N-1 a N-21 del research, §15.1) ---------
    ('N-1',
     'N-1 · El «margen bruto del churro de ochenta y cinco a noventa por '
     'ciento» no aparece en la fuente que se le atribuye: no entra ni '
     'atribuido a nadie.'),
    ('N-2',
     'N-2 · El «beneficio de cuarenta a sesenta mil euros al año» es '
     'circular y sin método: no entra.'),
    ('N-3',
     'N-3 · «Montar una churrería cuesta entre doce mil y cincuenta mil '
     'euros» no sale ni de la tabla que lo publica: no entra.'),
    ('N-4',
     'N-4 · «Licencias y permisos, de dos mil a seis mil euros» no tiene '
     'fuente ni distingue despacho y sala: no entra.'),
    ('N-5',
     'N-5 · El personal de «dos mil cuatrocientos a tres mil euros al mes» '
     'para tres personas y el punto de equilibrio de «cincuenta y cinco '
     'raciones al día» del artículo de un proveedor de TPV no entran como '
     'cifra: sólo su MÉTODO (fijos entre lo que deja cada ración), con el '
     'personal real.'),
    ('N-6',
     'N-6 · Los casos del mismo proveedor de TPV (un food truck y un quiosco '
     'con su facturación mensual) son escenarios de un artículo, no negocios: '
     'no entran.'),
    ('N-7',
     'N-7 · «El aceite absorbe un treinta por ciento menos» o «dura el '
     'doble» son fichas comerciales: no entran.'),
    ('N-8',
     'N-8 · Los «quinientos cuarenta kilos por hora» de una dosificadora son '
     'el máximo del fabricante, no el ritmo de una línea: no entran. La '
     'capacidad se mide con tu masa y tu churrero.'),
    ('N-9',
     'N-9 · Maestro Churrero «desde setenta y cinco mil euros y cuarenta '
     'metros» no entra: de esa enseña sólo vale la inversión publicada por '
     'lexpress el 30 de junio de 2026, con su fecha.'),
    ('N-10',
     'N-10 · Valor con «tres locales propios y veintinueve franquiciados» '
     'está caducado: no entra.'),
    ('N-11',
     'N-11 · La «cuota de mercado de la mitad» de una marca de chocolate a '
     'la taza, el precio de una chocolatería famosa leído en un agregador y '
     'el precio de una freidora que dio un buscador y que la propia página '
     'contradice: no entran.'),
    ('N-12',
     'N-12 · La grasa de los churros de un estudio extranjero (churros de '
     'maíz, en gramos por cien gramos) no es la absorción de tu masa: no '
     'entra.'),
    ('N-13',
     'N-13 · Los traspasos reeditados durante más de dos años no son precio '
     'de mercado: no entran.'),
    ('N-14',
     'N-14 · La «docena a doce euros» (errata de un artículo), las dos '
     'facturaciones distintas de una cadena mexicana para el mismo año y el '
     'número de vacantes de un agregador de empleo: no entran.'),
    ('N-15',
     'N-15 · La «rentabilidad del setenta por ciento» del título de un foro '
     'no tiene fuente: sólo se usa como la objeción que la guía desmonta.'),
    ('N-16',
     'N-16 · El tamaño del «mercado mundial de churros» en millones de '
     'dólares no tiene autor ni método: no entra.'),
    ('N-17',
     'N-17 · «Maquinaria de ochocientos a mil quinientos euros» y «con '
     'treinta o cincuenta metros es suficiente» son de vendedores y '
     'contradicen las fichas: no entran.'),
    ('N-18',
     'N-18 · Las «multas por el extractor» y la «tasa por metro cuadrado y '
     'día» de municipios sin identificar son resultados de buscador sin '
     'abrir: no entran.'),
    ('N-19',
     'N-19 · La tasa de feria de un pueblo pequeño sólo vale como ejemplo de '
     'cómo se fija una tasa, nunca como orden de magnitud nacional.'),
    ('N-20',
     'N-20 · La temperatura de fritura del churro, el porcentaje de '
     'absorción, la vida del aceite, los churros por hora, la curva mensual y '
     'el mix de canales NO tienen fuente: en las hojas son supuestos '
     'declarados y en el texto se dicen como tales, nunca como dato.'),
    ('N-21',
     'N-21 · Ninguna cita de prensa entra como testimonio ni como reseña: lo '
     'que dice un churrero en una noticia es una noticia, con su medio y su '
     'fecha.'),
    # ---- 6. Afirmaciones y errores de método del research (§15.2) ---------
    ('15.2-norm',
     'Afirmaciones normativas falsas o caducas que NO se escriben: el carnet '
     'de manipulador; «la inspección de sanidad viene antes de la licencia»; '
     'el real decreto estatal de venta ambulante como vigente; la orden de '
     'horarios de Madrid de 1998 y «la chocolatería abre a las 6:00»; '
     '«necesitas licencia» sin formato; el art. 8 de la norma del aceite; '
     '«la acrilamida es obligatoria en los churros»; el «sin gluten»; «no '
     'existe convenio de churrerías» y «la categoría de churrero»; el código '
     '4781 de la clasificación antigua para un puesto (en la de 2025, el '
     '47.81 es venta de vehículos de motor); las ordenanzas que siguen '
     'citando el real decreto derogado de venta ambulante; el registro '
     'general sanitario para la caseta de feria; un tipo de IVA para el '
     'chocolate para llevar; los humos de Barcelona, Sevilla o Valencia.'),
    ('15.2-metodo',
     'Errores de método que NO se repiten: el veredicto por ratio cuando la '
     'pregunta es en euros; mezclar bases de IVA; un «desde» como cifra '
     'cerrada; la capacidad máxima de un fabricante como ritmo; el precio '
     'pedido como precio de cierre; citas de prensa resumida como literales; '
     'posiciones de buscador de páginas antiguas; constantes metidas dentro '
     'de las fórmulas; y dar por verificado lo que una fuente posterior ya '
     'contradijo.'),
    # ---- 7. Ámbito del producto y fronteras -------------------------------
    ('ambito-1',
     'Esta guía es para quien AÚN NO HA ABIERTO. No escribas nada dirigido a '
     'quien ya opera todos los días: ni control diario de producción, ni '
     'ingeniería de carta, ni gestión del día a día.'),
    ('ambito-2',
     'NO conviertas la guía en un recetario ni en un curso de churrero: no '
     'hay recetas, no hay técnica de amasado ni de fritura, no hay tiempos ni '
     'temperaturas. Los gramajes y las cantidades por kilo de masa son datos '
     'de EJEMPLO para que las fórmulas calculen, y se dice.'),
    ('ambito-3',
     'Los únicos productos de la casa que puedes nombrar, con su nombre '
     'exacto y para lo que sirven: «Cómo Montar una Chocolatería Boutique & '
     'Atelier» (sólo para decir que la bombonería es otro negocio y tiene su '
     'guía); el «Pack Plantillas APPCC» (el registro del aceite de fritura, '
     'fichero 09-control-aceite-fritura.xlsx, y el resto de registros de '
     'autocontrol); el «Kit Gestión de Personal y Turnos» (el cuadrante '
     'semana a semana y las nóminas); el «Plan de Negocio: Food Truck» y el '
     'kit «Tareas: Food Truck» (si la feria es tu negocio o vas en '
     'vehículo); el «Plan de Negocio: Cafetería» y el kit «Tareas: Cafetería '
     '/ Brunch» (churros dentro de una cafetería); y el «Kit de Escandallos '
     'Pro» y la «Guía Food Cost + Ingeniería de Menú» (el método general de '
     'escandallo, que NO costea masa frita por kilo). Ninguno más.'),
    ('ambito-4',
     'NO reproduzcas el registro del aceite del Pack APPCC ni el cuadrante '
     'semanal del Kit Gestión de Personal y Turnos: se citan por su fichero y '
     'su hoja, y la guía construye la decisión previa que esos productos no '
     'tienen.'),
    ('ambito-5',
     'El obrador que fabrica para otros negocios (masa, churro congelado o '
     'prefrito para cafeterías) queda FUERA del producto: como mucho, una '
     'línea para decir dónde está la frontera y que ahí dejas de ser '
     'minorista.'),
    ('ambito-6',
     'El marco legal es el ESPAÑOL. La estructura económica del pack sirve '
     'en cualquier país, pero el marco sanitario, fiscal y laboral hay que '
     'adaptarlo; la adaptación se ofrece como servicio, sin promesa.'),
    # ---- 8. Vocabulario (SPEC §6) y tono ----------------------------------
    ('voc-1',
     'VOCABULARIO de España. La equivalencia regional o de Hispanoamérica va '
     'UNA SOLA VEZ en todo el documento, en su PRIMERA mención (si tu '
     'capítulo no es el primero del documento, NO la repitas): «churro» y '
     '«porra» (el churro grueso), con «tejeringo», «calentito» y «jeringo» '
     'como nombres regionales; «chocolate a la taza», con «chocolate '
     'caliente» como el término de México y Chile, AVISANDO de que no es lo '
     'mismo (el de aquí lleva almidón y es espeso); «churrera» y '
     '«dosificadora», con «máquina de churros»; «escandallo» (costeo); '
     '«puesto», «caseta» y «remolque», con «carrito»; «montar» (en México, '
     '«poner»); «obrador»; «churrería-chocolatería». «Bajera» y «darle a la '
     'pala» sólo como color, nunca como término.'),
    ('voc-2',
     'Las siglas van dentro del texto y desarrolladas la primera vez (el '
     'impuesto sobre actividades económicas, la clasificación nacional de '
     'actividades económicas, el registro general sanitario, el Código '
     'Técnico de la Edificación, el análisis de peligros y puntos de control '
     'crítico), nunca en los títulos.'),
    ('tono-1',
     'TONO: de colega que ya ha montado esto y te lo cuenta, no de '
     'consultora. Prohibido el lenguaje corporativo, prohibidas las '
     'introducciones del tipo «en este capítulo veremos» y prohibidas las '
     'conclusiones que resumen lo ya dicho. Cada párrafo aporta un dato, un '
     'procedimiento o una decisión.'),
    ('tono-2',
     'PROHIBIDO prometer legalidad o rentabilidad: nunca «cumple la '
     'normativa», «quedarás legal» ni «con esto vas a ganar tanto». La '
     'fórmula segura es: aquí tienes el mapa normativo con la norma, el '
     'artículo y el enlace, y el modelo con el que calculas tu número.'),
    ('tono-3',
     'El caso que recorre el pack se llama «Churrería-Chocolatería El '
     'Molinete» la primera vez y «El Molinete» después. Es un caso MODELADO '
     'en una ciudad media española sin nombre, no un negocio real: no le '
     'atribuyas ciudad, dueños ni historia.'),
    ('tono-4',
     'No menciones el proceso de edición ni palabras como «maquetador», '
     '«prompt», «instrucciones», «guion» o «tramo»: el lector compra un '
     'libro, no ve el taller. Tampoco escribas tu propio razonamiento.'),
]

NO_COMUN = [texto for _origen, texto in LISTA_NEGRA_GUION]

# El business plan y las 12 decisiones heredan las mismas prohibiciones, más
# la suya (SPEC §4.3: `puntos_por_epigrafe` prohíbe repetir el capítulo).
NO_COMUN_BONUS = NO_COMUN + [
    'Este documento es un anexo del pack: NO repitas la explicación completa '
    'de un capítulo de la guía. Da el caso, la decisión, el número y la hoja, '
    'y remite al capítulo en una frase.',
]

# Cadenas de la lista negra que verificar_guion.py busca en TODO el guion
# fuera de las prohibiciones (y, con --txt, en los bloques ya redactados).
# Se suman a `LISTA_NEGRA` de guia-churreria/datos_ejemplo.py, que el gate
# importa. Una aguja que empieza por «re:» es una expresión regular.
LISTA_NEGRA_AGUJAS = (
    ('85-90', '§5.1.11 · N-1'),
    ('85 y 90', '§5.1.11 · N-1'),
    ('107.000', '§5.1.11 · D15'),
    ('120.000', '§5.1.11 · D15'),
    ('95.000', '§5.2 · SR-02'),
    ('290 €', '§5.1.11 · A10'),
    ('1.343', '§5.1.11 · A7'),
    ('16.116', '§5.1.11 · A7'),
    ('2.400', 'N-5'),
    ('55 raciones', 'N-5'),
    ('540 kg', 'N-8'),
    ('re:dura el doble', 'N-7'),
    ('re:absorbe un 30', 'N-7'),
    ('re:docena a 12', 'N-14'),
    ('re:12 euros la docena', 'N-14'),
    ('re:facturamos', '§5.1.11'),
    ('re:150 franquicias', '§5.1.11'),
    ('re:maestro churrero[^\n]{0,80}75[.]?000', 'N-9'),
    ('12.000-50.000', 'N-3'),
    ('40.000-60.000', 'N-2'),
    ('2.000-6.000', 'N-4'),
    ('re:\\b1[5-9][0-9]\\s?(°|º|grados)', 'V-02'),
    ('re:brecha', 'A8'),
    ('re:× ?4\\b', 'A8'),
    ('re:posici[oó]n 1\\b', 'D20'),
    ('re:primera posici[oó]n', 'D20'),
    ('re:carn[eé]t? de manipulador', 'CHN-69'),
    ('re:convenio de churrer', 'D9'),
    ('re:categor[ií]a de churrero', 'D9'),
    ('re:media cuota', 'D14'),
    ('re:cumplimiento acrilamida', 'D12'),
    ('re:entra a las [45]', 'A1'),
    ('re:verificado contra el boe', 'casa'),
    ('re:100 ?% legal', 'casa'),
    ('re:toda hispanoam[eé]rica', 'casa'),
    ('re:plan gratuito', 'casa'),
    ('re:comparativa de aceites', 'D4'),
    ('re:una due[ñn]a', 'SR-05'),
    ('re:no existe ninguna gu[ií]a', '§5.1.12'),
    ('1562/1998', 'CUN-34'),
    ('re:jooble', 'A7'),
    ('re:demuestra el 25', 'A12'),
    ('re:te evita la instalaci', 'A6'),
    ('re:cumple la ley de pl[aá]sticos', 'SR-08'),
    ('re:rentabilidad del 70', 'N-15'),
    ('750-3.000', 'N-18'),
    ('re:1,10 ?€/m', 'N-18'),
    ('23,7', 'N-12'),
    ('35,2', 'N-12'),
    ('4.228', 'N-11'),
    ('7.306', 'N-14'),
)


# --------------------------------------------------------------------------
# Los 16 capítulos + el anexo (D26). Cada capítulo declara PRIMERO su
# `PPE_nn` (epígrafe literal → puntos) y luego usa `list(PPE_nn)` como
# `epigrafes`: la lista de epígrafes y las claves del reparto no pueden
# discrepar. En los puntos no hay números sueltos: la cifra se nombra por su
# etiqueta de `cifras` o por el id del dato del sector.
# --------------------------------------------------------------------------

# ============================== CAPÍTULO 01 ===============================
PPE_01 = {
    'Seis formatos con el mismo nombre, y cuál te toca': [
        'Abrir con el mapa: la palabra «churrería» tapa seis negocios que se '
        'montan distinto. Presentarlos por lo que el pack le da a cada uno: el '
        'local con sala, terraza y despacho a calle (el caso cifrado); el '
        'despacho para llevar (columna de escenario, con su propio régimen de '
        'apertura); la caseta o el remolque de feria (papeles y punto muerto '
        'por evento, sin caso cifrado); la franquicia (comparador de lo que '
        'publican las enseñas, sin recomendar ninguna); los churros dentro de '
        'una cafetería o un bar (sólo lo que cambia al meter una freidora); y '
        'el obrador que fabrica para otros negocios (fuera, en una línea).',
        'Decir por qué el caso es el local con sala y no el despacho: es el '
        'negocio que define la venta —la taza con el churro—, es el formato '
        'con comparables publicados y es el más difícil; con él cifrado, el '
        'despacho sale como «lo que quitas», no al revés.',
        'Dar la dotación con precio de ficha de las tres variantes que la '
        'calculadora cifra —local con sala, despacho y caseta— y avisar de que '
        'NO son el presupuesto de apertura: les falta todo lo que ninguna ficha '
        'publica, que es la mayor parte del dinero y la cuenta el capítulo 8.',
    ],
    'El caso que recorre el pack: la Churrería-Chocolatería El Molinete': [
        'Presentar El Molinete en cinco líneas: un local con la superficie útil '
        'del caso, obrador de masa a la vista, fritura bajo campana, barra con '
        'despacho a calle, sala y una terraza aparte con su propia '
        'autorización; en una ciudad media española sin nombre; abre todos los '
        'días y madruga los fines de semana.',
        'Explicar las tres clases de cifra que el lector va a encontrar y cómo '
        'se distinguen en las hojas: las que tienen fuente (un id con su '
        'enlace), los SUPUESTOS DECLARADOS de El Molinete (celda verde con la '
        'nota «supuesto, pon el tuyo») y las que calcula el libro. Y la regla '
        'de los ejemplos de Madrid: horario, humos y convenio son el ejemplo '
        'verificado, no la norma de tu ciudad.',
        'Dar el orden de magnitud del caso con tres cifras del pack —el CAPEX '
        'sin fondo de maniobra y las raciones de un día tipo y de un día punta— '
        'y decir que todo lo demás se deriva de ellas en los libros.',
    ],
    'La bombonería es otro negocio, y tiene su propia guía': [
        'Decirlo arriba y en positivo, porque es una venta cruzada honesta: '
        'hacer bombones en un obrador es comercio con fabricación propia y no '
        'lleva freidora; servir chocolate a la taza con churros es hostelería '
        'con fritura. Quien quiera la bombonería tiene su guía, «Cómo Montar '
        'una Chocolatería Boutique & Atelier».',
        'Y el argumento legal que los separa, en una línea y sin venderlo como '
        'novedad (el desarrollo es del capítulo 4): el Anexo de la Ley 12/2012 '
        'no contiene ningún grupo de la agrupación de restauración, así que la '
        'sala con mesas queda fuera de la inexigibilidad de licencia de '
        'actividad; el despacho de masas fritas, epígrafe 644.6, está dentro '
        'porque el Anexo incluye el grupo 644 completo, como ya explicaba la '
        'guía de chocolatería.',
        'Qué hacer si quieres las dos cosas: las dos guías se enlazan, y la '
        'frontera práctica es la freidora, que trae humos, gas, aceite y otro '
        'riesgo de incendio.',
    ],
    'Qué incluye este pack, en qué orden se rellena y qué es de otro producto': [
        'Listar los ocho libros por su nombre de fichero y la pregunta que '
        'contesta cada uno —producción y local, inversión, carta y escandallo, '
        'aceite, temporada y ferias, plan financiero, checklist legal y '
        'turnos— y el ORDEN en que se rellenan, que no es el de su número: '
        'cada libro trae por celda verde, con una fila de cuadre que avisa si '
        'te equivocas, la cifra que necesita de otro.',
        'Decir qué NO construye este pack y dónde vive: el registro diario del '
        'aceite y el resto del autocontrol están en el Pack Plantillas APPCC; '
        'el cuadrante semana a semana y las nóminas, en el Kit Gestión de '
        'Personal y Turnos; la feria como negocio con vehículo, en el Plan de '
        'Negocio: Food Truck; la cafetería que mete churros, en el Plan de '
        'Negocio: Cafetería; y el método general de escandallo, en el Kit de '
        'Escandallos Pro y la Guía Food Cost + Ingeniería de Menú, que no '
        'costean masa frita por kilo.',
    ],
    'Lo que este pack no hace, y cómo llamamos a cada cosa': [
        'Decirlo sin adornos y antes de que el lector lo busque: no enseña a '
        'freír, no es un recetario ni un curso de churrero, no da ninguna '
        'temperatura de fritura del churro (no hay fuente primaria que la '
        'fije), no sustituye al proyecto técnico de la extracción ni a tu '
        'asesor, y no promete rentabilidad.',
        'Fijar el vocabulario de todo el documento, con la equivalencia una '
        'sola vez y aquí: churro y porra (tejeringo, calentito y jeringo como '
        'nombres regionales), chocolate a la taza (que no es el chocolate '
        'caliente de México y Chile: el de aquí lleva almidón y es espeso), '
        'churrera y dosificadora (la máquina de churros), escandallo (costeo), '
        'puesto, caseta y remolque (carrito), y montar (en México, poner).',
    ],
}

CAP_01 = {
    'n': 1,
    'titulo': 'Qué Negocio Estás Montando: Seis Formatos y Cuál te Toca',
    'resumen_indice': 'los seis formatos con el mismo nombre y cuál te toca, el caso de El Molinete, por qué la bombonería es otro negocio, qué incluye el pack y en qué orden se rellena, y lo que no hace.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector se sitúe en cinco minutos: cuál de los seis '
                'formatos de churrería está montando de verdad, qué compró y '
                'en qué orden se usa, por dónde entrar según su problema y qué '
                'NO hay aquí, para que no lo busque.',
    'epigrafes': list(PPE_01),
    'puntos_por_epigrafe': PPE_01,
    'puntos_globales': [
        'Este capítulo fija el vocabulario de TODO el documento: es la única '
        'mención de las equivalencias regionales y de Hispanoamérica; desde '
        'aquí, sólo la forma española.',
        'La frontera con la guía hermana y con los otros productos de la casa '
        'se dice ARRIBA y en positivo, nunca escondida al final.',
        'Tono de bienvenida sin autobombo: nada de «la guía definitiva». Se '
        'enseña qué hay dentro y qué no.',
    ],
    'cifras': [
        C('Superficie útil del local de El Molinete, en metros cuadrados', f'{X_PROD}!Parámetros!B6', 'num', clave='Superficie útil del local'),
        C('Metros cuadrados de producción (obrador de masa y fritura)', f'{X_PROD}!Zonas y m²!D17', 'num', clave='m² de producción'),
        C('Raciones de un día tipo, de lunes a viernes (supuesto de El Molinete)', f'{X_PROD}!Día Tipo y Día Punta!L7', 'num', clave='Raciones del día tipo'),
        C('Raciones de un día punta, sábado, domingo y festivo (supuesto de El Molinete)', f'{X_PROD}!Día Tipo y Día Punta!L8', 'num', clave='Raciones del día punta'),
        C('CAPEX de apertura de El Molinete, sin fondo de maniobra y sin IVA', f'{X_CAPEX}!Resumen!L5', 'eur', clave='CAPEX de apertura sin fondo de maniobra (origen de X10)'),
        C('Dotación con precio de ficha del local con sala, sin IVA y con el medidor de polares', f'{X_CAPEX}!Equipamiento Línea a Línea!X35', 'eur2', clave='Dotación con fuente del local con sala, con el medidor de polares'),
        C('Dotación con precio de ficha del despacho para llevar, sin IVA y con el medidor de polares', f'{X_CAPEX}!Equipamiento Línea a Línea!Y35', 'eur2', clave='Dotación con fuente del despacho, con el medidor de polares'),
        C('Dotación de la caseta de feria: el remolque con cartel, sin IVA', f'{X_CAPEX}!Variante del Formato!C8', 'eur', clave='Dotación de la caseta (equipo de feria elegido)'),
    ],
    'sector': ['CUN-09', 'CUN-11', 'CUN-12', 'CUN-35', 'CHN-49b', 'CHN-49c',
               'CUS-42'],
    'tablas': [
        {
            'titulo': 'Las cuatro variantes que compara la calculadora, con su dotación de ficha y su régimen de apertura (calculadora-capex-churreria.xlsx, hoja «Variante del Formato»)',
            'src': (X_CAPEX, 'Variante del Formato'),
            'cols': [('Variante', 'A', 'txt'), ('Superficie', 'B', 'txt'),
                     ('Dotación con precio de ficha, sin IVA', 'C', 'eur2'),
                     ('Régimen de apertura', 'E', 'txt'),
                     ('¿Caso cifrado?', 'G', 'txt'), ('Remite a', 'H', 'txt')],
            'filas': (6, 9),
            'ancla': ('A6', 'Local con sala'),
            'nota': 'La dotación con precio de ficha no es el presupuesto de apertura: le '
                    'faltan la obra, la extracción y todo lo que ninguna ficha publica, que la '
                    'calculadora presupuesta aparte. La franquicia no es una dotación: su '
                    'inversión publicada va en su propia hoja. ' + V_LEY12,
        },
        {
            'titulo': 'Tu problema, el capítulo que lo trata y el libro que lo resuelve',
            'cabecera': ['Si tu problema es…', 'Capítulo', 'Libro del pack'],
            'filas': [
                ['No sé si este local admite una freidora', '4, 5 y 6', 'produccion-hora-punta-y-local.xlsx'],
                ['No sé qué papeles me tocan ni en qué orden', '4 y 9', 'checklist-legal-fritura-y-licencias.xlsx'],
                ['No sé cuánto cuesta abrir', '7 y 8', 'calculadora-capex-churreria.xlsx'],
                ['No sé si me sale mejor un traspaso', '6 y 8', 'calculadora-capex-churreria.xlsx'],
                ['No sé qué poner en la carta ni qué IVA lleva cada cosa', '3', 'carta-de-apertura-y-escandallo-churro.xlsx'],
                ['No sé cuánto me cuesta una ración ni a cuánto venderla', '12', 'carta-de-apertura-y-escandallo-churro.xlsx'],
                ['No sé cuánto me cuesta el aceite ni cuándo cambiarlo', '10', 'aceite-de-fritura-coste-y-cambio.xlsx'],
                ['No sé si se me formará cola el domingo', '6', 'temporada-franjas-y-ferias.xlsx'],
                ['No sé de qué vivo en verano ni si me compensan las ferias', '14', 'temporada-franjas-y-ferias.xlsx'],
                ['No sé cuánta gente necesito ni cuánto me cuesta madrugar', '13', 'turnos-plantilla-y-madrugada.xlsx'],
                ['No sé qué alérgenos declaro ni qué me pedirán en la inspección', '11', 'checklist-legal-fritura-y-licencias.xlsx'],
                ['No sé si me conviene una franquicia', '15', 'calculadora-capex-churreria.xlsx'],
                ['No sé si el negocio se sostiene ni si el banco me lo financia', '16', 'plan-financiero-3-anos-churreria.xlsx'],
            ],
            'nota': 'Los ocho libros comparten el mismo juego de datos, así que puedes saltar '
                    'al capítulo que te interese sin perder el hilo de las cifras.',
        },
        {
            'titulo': 'El orden en que se rellenan los ocho libros (checklist-legal-fritura-y-licencias.xlsx, hoja «Instrucciones»)',
            'src': (X_LEGAL, 'Instrucciones'),
            'cols': [('Paso', 'A', 'num'), ('Libro', 'B', 'txt'),
                     ('Fichero', 'C', 'txt')],
            'filas': (22, 29),
            'ancla': ('C22', 'carta-de-apertura-y-escandallo-churro'),
            'nota': 'Cada libro copia por celda verde, con una fila de cuadre que avisa si '
                    'te equivocas, la cifra que necesita de otro: nunca hay una fórmula entre '
                    'ficheros. El libro legal no depende de ninguno y va el último.',
        },
    ],
    'prohibido': NO_COMUN + [
        'No des una cifra de inversión «de una churrería» sin decir de qué '
        'formato y con qué metros: es el error de método que este capítulo '
        'viene a corregir.',
        'No presentes el pack como curso, recetario ni sustituto del proyecto '
        'técnico de la extracción, de una asesoría o de un curso de oficio.',
        'No hables mal de la bombonería ni de la guía hermana: son otro '
        'negocio y otro producto, y se recomiendan con honestidad.',
    ],
}

# ============================== CAPÍTULO 02 ===============================
PPE_02 = {
    'No hay censo de churrerías, y eso también es un dato': [
        'Decir la verdad incómoda primero: no existe un número oficial de '
        'churrerías en España. La clasificación nacional de actividades no '
        'tiene una clase propia para la churrería y el directorio de empresas '
        'del INE sólo publica la hostelería agregada: quien te dé una cifra de '
        'churrerías se la ha inventado.',
        'Dar lo que sí tiene fuente y para qué sirve: los locales de '
        'hostelería de España, con su fecha (directorio del INE), son el orden '
        'de magnitud de la competencia por el desayuno y la merienda, no tu '
        'cuota. Y el informe de consumo alimentario del ministerio no tiene '
        'una línea de churros: no hay consumo de churros medido.',
        'Sacar la consecuencia: el mercado de una churrería es su calle, y se '
        'mide andando, no en un informe. El último epígrafe da el método.',
    ],
    'Desayuno, merienda y noche: las franjas que mandan': [
        'Explicar las franjas de El Molinete como lo que son, supuestos '
        'declarados del libro de temporada que el lector cambia por los suyos: '
        'el desayuno es la franja que más raciones se lleva de la semana, la '
        'merienda es la segunda franja, y la media mañana y la noche de los '
        'viernes y sábados son pequeñas.',
        'Dar las horas a la semana de cada franja y la hora punta de un día '
        'tipo y de un día punta en raciones por hora, y explicar por qué la '
        'hora punta importa más que el total del día: la línea de fritura se '
        'dimensiona para la peor hora, no para la media. La cola del domingo '
        'se resuelve en el capítulo 6.',
        'Avisar de la trampa de horario que va pegada al desayuno: abrir antes '
        'de las 8:00 tiene condiciones en el ejemplo de Madrid, que explica el '
        'capítulo 4. La franja vive sólo en el libro de temporada; el libro de '
        'turnos copia de ahí sus horas.',
    ],
    'Lo que cuesta un churro depende de la plaza': [
        'Presentar los precios publicados con su sitio y su año, uno por '
        'línea: la ración de seis churros y el chocolate a la taza en barra y '
        'en terraza de una churrería de Granada; la ración y la media ración '
        'de La Artesana, en Palma; el churro y la porra sueltos de una '
        'churrería de Vallecas; y el gasto por persona con chocolate en una '
        'chocolatería del centro de Madrid.',
        'Leerlos bien: con chocolate, de la ración más la taza de Granada al '
        'gasto por persona del centro de Madrid, la plaza mueve el ticket '
        'alrededor de la mitad, y los datos son de años distintos. En este '
        'capítulo SÍ puedes sumar la ración y la taza de la misma carta de '
        'Granada para dar su precio con chocolate: es la única suma '
        'permitida.',
        'Y la decisión que sale de ahí: no hay «precio de la ración en '
        'España». El ticket de El Molinete, sin IVA y con la carta de '
        'invierno, sale de su propia carta y de su mix, y el capítulo 3 '
        'explica cómo se fija.',
    ],
    'Qué mirar en la calle antes de firmar': [
        'Dar el método de una mañana de trabajo: contar churrerías, '
        'cafeterías y bares que sirven churros en el radio de caminata; mirar '
        'a qué hora abren y si hay cola el domingo; pedir la ración y la taza '
        'y apuntar el precio; y ver quién pasa a primera hora y quién a la '
        'hora de la merienda.',
        'Dar los volúmenes que publican negocios reales, con su medio y su '
        'fecha, como contraste y no como objetivo: lo que cuenta el gestor de '
        'La Artesana que venden entre semana y en fin de semana, y lo que '
        'llega a vender en sus días fuertes la churrería de Vallecas. Las '
        'raciones de El Molinete son un supuesto apoyado en el primero, y se '
        'dice.',
        'Cerrar con el criterio: una plaza sirve si su hora punta cabe en tu '
        'línea y su precio cabe en tu escandallo. Las dos cosas se comprueban '
        'en los libros de producción y de carta antes de firmar.',
    ],
}

CAP_02 = {
    'n': 2,
    'titulo': 'El Cliente, las Franjas y la Plaza',
    'resumen_indice': 'por qué no hay censo de churrerías, las franjas del desayuno, la merienda y la noche, lo que cuesta un churro según la plaza y qué mirar en la calle antes de firmar.',
    'palabras': 1300, 'bloques': 1,
    'objetivo': 'Que el lector sepa contra quién compite antes de elegir local '
                'y carta: qué datos de mercado existen y cuáles no, cómo se '
                'reparte el día de una churrería, cuánto mueve la plaza el '
                'precio de la ración y qué mirar en la calle antes de firmar.',
    'epigrafes': list(PPE_02),
    'puntos_por_epigrafe': PPE_02,
    'puntos_globales': [
        'Cada precio publicado va con su sitio y su año en la misma frase, y '
        'las cifras de fiabilidad limitada se presentan como orden de '
        'magnitud, con esa etiqueta.',
        'El capítulo termina en un criterio de plaza, no en un informe de '
        'mercado: qué mirar en la calle antes de firmar.',
    ],
    'cifras': [
        C('Parte de las raciones de la semana que se lleva el desayuno (supuesto de El Molinete)', f'{X_TEMP}!Franjas del Día!D53', 'pct0', clave='Parte de las raciones de la semana que se lleva el desayuno'),
        C('Parte de las raciones de la semana que se lleva la merienda (supuesto de El Molinete)', f'{X_TEMP}!Franjas del Día!D55', 'pct1', clave='Parte de las raciones de la semana que se lleva la merienda'),
        C('Horas a la semana de la franja de desayuno', f'{X_TEMP}!Franjas del Día!L5', 'num', clave='Horas a la semana de la franja desayuno (dato de referencia)'),
        C('Horas a la semana de la franja de merienda', f'{X_TEMP}!Franjas del Día!L7', 'num1', clave='Horas a la semana de la franja merienda (dato de referencia)'),
        C('Hora punta de un día tipo de un mes medio, en raciones por hora', f'{X_TEMP}!Franjas del Día!E14', 'num1', clave='Hora punta de un día tipo, mes medio (raciones/h)'),
        C('Hora punta de un día punta de un mes medio, en raciones por hora', f'{X_TEMP}!Franjas del Día!E15', 'num1', clave='Hora punta de un día punta, mes medio (raciones/h)'),
        C('Raciones de una semana de un mes medio', f'{X_TEMP}!Franjas del Día!C57', 'num', clave='Raciones de la semana (mes medio)'),
        C('Ticket medio sin IVA por ración de la carta de invierno de El Molinete', f'{X_CARTA}!Mix y Ticket Canal y Temporada!D6', 'eur2', clave='Ticket sin IVA por ración (invierno)'),
        C('Raciones de un día tipo (supuesto de El Molinete)', f'{X_PROD}!Día Tipo y Día Punta!L7', 'num', clave='Raciones del día tipo'),
        C('Raciones de un día punta (supuesto de El Molinete)', f'{X_PROD}!Día Tipo y Día Punta!L8', 'num', clave='Raciones del día punta'),
    ],
    'sector': ['CUS-06', 'CUS-07', 'CUS-08', 'CUS-13', 'CUS-15', 'CUS-16',
               'CUS-17', 'CUS-19', 'CUS-27'],
    'tablas': [
        {
            'titulo': 'Las cuatro franjas de la semana de El Molinete (temporada-franjas-y-ferias.xlsx, hoja «Franjas del Día»)',
            'src': (X_TEMP, 'Franjas del Día'),
            'cols': [('Franja', 'A', 'txt'), ('Horas a la semana', 'B', 'num1'),
                     ('Raciones a la semana, mes medio', 'C', 'num1'),
                     ('Parte de las raciones de la semana', 'D', 'pct1')],
            'filas': (53, 57),
            'ancla': ('A53', 'Desayuno'),
            'nota': 'Supuestos declarados de El Molinete: el reparto por franjas no tiene '
                    'fuente pública y se cambia por el tuyo en cuanto tengas dos semanas de '
                    'tiques. Es la única fuente de franjas del pack: el libro de turnos copia '
                    'de aquí sus horas.',
        },
        {
            'titulo': 'Lo que cuesta un churro según la plaza, con su sitio y su año',
            'cabecera': ['Dónde', 'Qué publica', 'Año', 'Id del dato'],
            'filas': [
                ['La Churrería, Granada', 'La ración de seis churros y el chocolate a la taza en barra y en terraza', '2026', 'CUS-15'],
                ['La Artesana, Palma', 'La ración y la media ración de churros', '2025', 'CUS-17'],
                ['Churrería Antonio, Vallecas (Madrid)', 'El churro suelto y la porra suelta', '2026', 'CUS-16'],
                ['Chocolatería 1902, centro de Madrid', 'El gasto por persona con chocolate', '2024', 'CUS-19'],
            ],
            'nota': 'Los importes de cada sitio están en el texto, con su fuente. No se '
                    'suman entre sí ni se convierten en un «precio de España»: cada carta es de '
                    'su ciudad y de su año.',
        },
        {
            'titulo': 'Los siete días de El Molinete: tipo de día, raciones, apertura y hora punta (temporada-franjas-y-ferias.xlsx, hoja «Franjas del Día»)',
            'src': (X_TEMP, 'Franjas del Día'),
            'cols': [('Día', 'A', 'txt'), ('Tipo de día', 'B', 'txt'),
                     ('Raciones del día, mes medio', 'C', 'num'),
                     ('Hora de apertura', 'D', 'num'),
                     ('Horas abiertas', 'F', 'num1'),
                     ('Hora punta, raciones por hora', 'H', 'num1')],
            'filas': (6, 12),
            'ancla': ('A6', 'Lunes'),
            'nota': 'Horario y raciones son supuestos de El Molinete. La hora de apertura '
                    'frente a la mínima del ejemplo de Madrid está en la misma hoja y la '
                    'explica el capítulo 4.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar un número de churrerías de España o una facturación '
        'media por churrería: no existe dato fiable, y el capítulo se escribe '
        'diciendo eso.',
        'PROHIBIDO escribir la cifra de facturación del cacao y el chocolate '
        'que acompaña al dato del informe de consumo: de esa fuente sólo '
        'entra su hallazgo, que no hay una línea de churros.',
        'PROHIBIDO presentar el reparto por franjas o las raciones de El '
        'Molinete como datos del sector: son supuestos declarados.',
    ],
}

# ============================== CAPÍTULO 03 ===============================
PPE_03 = {
    'Veinticuatro referencias en cinco familias, y el papel de cada una': [
        'Presentar la carta de El Molinete como un ejemplo declarado, no como '
        'un surtido recomendado: churros y porras (la ración, la media ración, '
        'la ración de porras, el churro y la porra sueltos, la docena y el '
        'kilo para llevar), dos rellenos y especiales, cinco formatos de '
        'chocolate a la taza, seis cafés y bebidas y cuatro referencias de '
        'carta de verano.',
        'Decir qué papel juega cada familia: el churro es el volumen y la '
        'materia más barata; la taza convierte la ración en un ticket con '
        'chocolate; los cafés llenan el desayuno; los rellenos suben ticket y '
        'redes; y la carta de verano es la que sostiene julio y agosto '
        '(capítulo 14).',
        'Dar el veredicto del libro sobre la carta entera —cuántas referencias '
        'salen con «mantener» y cuántas con «revisar precio»— y la regla con '
        'la que se toma: margen en EUROS por unidad y rotación, nunca el '
        'porcentaje. El churro suelto deja mucho por kilo de masa y poco por '
        'unidad, y por eso sale a revisar.',
    ],
    'Ración, docena y kilo: el formato también es precio': [
        'Explicar en pocas líneas por qué el mismo churro se vende en formatos '
        'distintos y qué papel cumple cada uno: la ración y la media ración en '
        'sala, la docena y el kilo para llevar y para el pedido grande del '
        'domingo. Lo que deja cada formato por kilo de masa se calcula en el '
        'capítulo 12: aquí sólo se decide qué formatos entran en la carta.',
        'Y el vaso de plástico o de papel plastificado para llevar: desde '
        'enero de 2023 se cobra aparte, con su línea propia en el tique (Ley '
        '7/2022, art. 55). En El Molinete va en la carta con su importe, que '
        'es un supuesto: la ley obliga a cobrarlo, no fija cuánto.',
    ],
    'El chocolate a la taza: qué preparado compras y qué dice su etiqueta': [
        'Explicar lo que define la norma, con su apartado: el RD 1055/2003 '
        'define el PRODUCTO «chocolate a la taza» —el polvo o la tableta— con '
        'un mínimo de cacao seco total y un máximo de harina o almidón '
        '(apartado 1.11 de su Reglamentación), y reserva esa denominación a '
        'los productos que lo cumplen. Lo que no dice es qué nombre puede '
        'llevar la bebida que sirves.',
        'Dar la fórmula de la guía, que es una interpretación de nivel B o C y '
        'se presenta así: la carta usa la denominación que figura en la '
        'etiqueta del preparado que compras; el libro de la carta te pide el '
        'cacao seco total de esa etiqueta y si declara grasa vegetal, y con '
        'menos del mínimo o con grasa vegetal te avisa: «consulta a tu '
        'servicio de consumo antes de imprimir la carta».',
        'Dar el caso de El Molinete: un preparado cuya etiqueta dice '
        '«chocolate a la taza», con el cacao seco que declara frente al '
        'mínimo, y el aviso que da el libro. Y lo que cuesta una taza con ese '
        'preparado y su leche, que el capítulo 12 usa en el escandallo.',
    ],
    'El IVA de lo que vendes: sala, para llevar y la zona gris de la taza': [
        'Dar las reglas con su norma: lo que se consume en barra, sala o '
        'terraza es servicio de hostelería y va al tipo reducido (art. 91 de '
        'la Ley 37/1992); los churros y las porras para llevar son la entrega '
        'de un alimento y van también al reducido.',
        'El granizado y la horchata para llevar, como AVISO y no como regla: '
        'desde el 1 de enero de 2021 las bebidas refrescantes con azúcares '
        'añadidos para llevar quedan fuera del tipo reducido, y no hay una '
        'consulta que diga si tu granizado o tu horchata lo son. El Molinete '
        'les pone el tipo general por prudencia; es zona gris: consúltalo con '
        'tu asesor y, si te confirma el reducido, cámbialo en esa celda. En '
        'sala siguen al reducido, como servicio de hostelería.',
        'La zona gris, sin dar un tipo en el texto: el chocolate a la taza '
        'para llevar y las demás bebidas para llevar. Con leche no encaja en '
        'la definición de bebida refrescante; con agua y un preparado '
        'azucarado podría leerse como tal; y no se ha localizado ninguna '
        'consulta vinculante. Por eso el libro de la carta lo lleva en una '
        'celda verde con su aviso, y el tipo lo decide tu asesor.',
        'Explicar dónde se aplica cada tipo: en el libro de la carta, por '
        'referencia y por canal; y el ticket que viaja al plan financiero va '
        'SIEMPRE sin IVA.',
    ],
    'El IVA de lo que compras: con o sin impuesto, siempre en base imponible': [
        'La regla dura del pack: toda línea de precio lleva al lado si el '
        'precio que tienes delante lleva IVA y a qué tipo. El preparado para '
        'masa, el aceite y el preparado de la taza se publican sin IVA en sus '
        'fichas; el cucurucho, con la base inferida, en una celda verde con '
        'aviso; y el equipamiento, la obra, los envases y los servicios van al '
        'tipo general.',
        'Y la consecuencia en el escandallo: el coste de materia se calcula '
        'SIEMPRE sobre base imponible en los dos lados del cociente, el del '
        'ingreso y el del coste. Mezclar un precio con IVA y otro sin IVA '
        'desvía el margen sin que se note. El IVA que adelantas al montar el '
        'local es caja, no inversión: lo explica el capítulo 8.',
    ],
}

CAP_03 = {
    'n': 3,
    'titulo': 'La Carta de Apertura y el IVA de Cada Cosa',
    'resumen_indice': 'veinticuatro referencias en cinco familias, la ración, la docena y el kilo, qué dice la etiqueta del preparado de la taza, el IVA de lo que vendes con su zona gris y el IVA de lo que compras.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector decida qué lleva su carta de apertura y qué IVA '
                'lleva cada cosa que vende y que compra, antes de que el libro '
                'de la carta y la calculadora de inversión apliquen esas '
                'reglas; y que resuelva el nombre de su chocolate a la taza con '
                'la etiqueta del preparado, no con una regla que no existe.',
    'epigrafes': list(PPE_03),
    'puntos_por_epigrafe': PPE_03,
    'puntos_globales': [
        'El IVA se explica AQUÍ y sólo aquí: es el capítulo que va antes de '
        'los libros que lo aplican (la carta y la inversión). Los capítulos '
        'siguientes lo citan de vuelta en una frase.',
        'Los precios de El Molinete marcados como supuesto son de ejemplo; los '
        'que tienen fuente van con su sitio y su año.',
        'Nada de recetas ni de técnica: las cantidades por taza o por kilo son '
        'lo que el modelo necesita para calcular, y se dice.',
    ],
    'cifras': [
        C('Referencias de la carta con veredicto «mantener»', f'{X_CARTA}!Decisión de Surtido!B34', 'num', clave='Referencias con veredicto Mantener'),
        C('Referencias de la carta con veredicto «revisar precio»', f'{X_CARTA}!Decisión de Surtido!B35', 'num', clave='Referencias con veredicto Revisar precio'),
        C('Ticket medio sin IVA por ración de la carta de invierno', f'{X_CARTA}!Mix y Ticket Canal y Temporada!D6', 'eur2', clave='Ticket sin IVA por ración (invierno)'),
        C('Cacao seco total que declara la etiqueta del preparado de El Molinete', f'{X_CARTA}!Chocolate a la Taza!B21', 'pct0', clave='Cacao seco total del preparado del ejemplo'),
        C('Cacao seco total mínimo del producto «chocolate a la taza» según el RD 1055/2003', f'{X_CARTA}!Chocolate a la Taza!B23', 'pct0', clave='Cacao seco total mínimo del chocolate a la taza'),
        C('Aviso que da el libro de la carta a El Molinete antes de imprimir la carta', f'{X_CARTA}!Chocolate a la Taza!B24', 'txt', clave='Aviso de la taza antes de imprimir la carta'),
        C('Coste de una taza de chocolate de El Molinete, sin IVA', f'{X_CARTA}!Chocolate a la Taza!B15', 'eur2', clave='Coste de una taza de chocolate'),
        C('IVA de lo que se consume en barra, sala y terraza', f'{X_CARTA}!Parámetros!B5', 'pct0', clave='IVA en sala'),
        C('IVA que El Molinete pone por prudencia al granizado y la horchata para llevar (aviso de zona gris, no regla: lo confirma tu asesor)', f'{X_CARTA}!Parámetros!B9', 'pct0', clave='IVA del granizado y la horchata para llevar'),
        C('Importe del vaso para llevar cobrado aparte en El Molinete (supuesto)', f'{X_CARTA}!Parámetros!B25', 'eur2', clave='Importe del vaso para llevar cobrado aparte'),
    ],
    'sector': ['CUS-09', 'CUS-11', 'CUS-15', 'CUS-17', 'CUS-20', 'CUS-21',
               'CUS-23', 'CUS-24', 'CUS-25', 'CHN-05', 'CUN-42', 'CUN-V06',
               'CUN-41', 'CUN-17', 'CUN-18', 'CHN-71c', 'FC-IVA-01',
               'FC-IVA-02', 'FC-IVA-04'],
    'tablas': [
        {
            'titulo': 'La carta de apertura de El Molinete: veinticuatro referencias con su precio, su fuente y su IVA (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Mix y Ticket Canal y Temporada»)',
            'src': (X_CARTA, 'Mix y Ticket Canal y Temporada'),
            'cols': [('Referencia', 'A', 'txt'), ('Familia', 'B', 'txt'),
                     ('Año del precio', 'C', 'txt'),
                     ('PVP con IVA', 'D', 'eur2'),
                     ('Fuente del precio', 'E', 'txt'),
                     ('IVA en sala', 'I', 'pct0'),
                     ('IVA para llevar', 'J', 'pct0')],
            'filas': (17, 40),
            'ancla': ('A17', 'CH1'),
            'nota': 'Los precios marcados «supuesto declarado» son de El Molinete, no del '
                    'sector. El IVA para llevar del chocolate y de las demás bebidas es la '
                    'celda verde del libro con su aviso: es una zona gris y el tipo lo decide '
                    'tu asesor. El vaso para llevar se cobra aparte, en su propia línea del '
                    'tique.',
        },
        {
            'titulo': 'El IVA de cada canal en el libro de la carta (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Parámetros»)',
            'src': (X_CARTA, 'Parámetros'),
            'cols': [('Qué vendes y dónde', 'A', 'txt'), ('Tipo', 'B', 'pct0'),
                     ('Norma o dato', 'D', 'txt')],
            'filas': (5, 11),
            'ancla': ('A5', 'IVA en sala'),
            'nota': 'Verificado el 03-10-2026 · Ley 37/1992, arts. 90 y 91. La línea del '
                    'chocolate y de las demás bebidas para llevar es una celda verde con '
                    'aviso, no un tipo afirmado: consulta a tu asesor · '
                    'https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740',
        },
        {
            'titulo': 'Los insumos con su base de IVA, como los publica cada ficha (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Parámetros»)',
            'src': (X_CARTA, 'Parámetros'),
            'cols': [('Insumo', 'A', 'txt'), ('Precio del formato', 'B', 'eur2'),
                     ('¿El precio lleva IVA?', 'C', 'txt'),
                     ('Tipo de IVA', 'D', 'pct0'),
                     ('Precio sin IVA por unidad', 'G', 'eur2'),
                     ('Fuente', 'H', 'txt')],
            'filas': (33, 37),
            'ancla': ('A33', 'Preparado para masa'),
            'nota': 'El preparado para masa, el aceite y el preparado de la taza declaran en '
                    'su ficha que el precio va sin impuestos; el cucurucho no lo declara y va '
                    'como base inferida, con aviso. El escandallo usa siempre la columna sin '
                    'IVA.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO escribir el tipo de IVA del chocolate a la taza para '
        'llevar o de las demás bebidas para llevar: celda verde con aviso, y '
        'lo decide el asesor.',
        'PROHIBIDO presentar como regla el tipo general del granizado y la '
        'horchata para llevar: es el aviso prudente del libro, en zona gris; '
        'se consulta al asesor y, si confirma el reducido, se cambia.',
        'PROHIBIDO presentar la carta de El Molinete como un surtido '
        'recomendado o sus precios supuestos como precios del sector.',
        'PROHIBIDO escribir que una bebida servida no puede llamarse '
        '«chocolate» o «chocolate a la taza» si el preparado no cumple el '
        'mínimo: es una interpretación abierta y se resuelve con la etiqueta y '
        'con tu servicio de consumo.',
        'No expliques aquí cómo se calcula el escandallo por kilo de masa: es '
        'del capítulo 12. Este capítulo decide QUÉ hay en la carta y QUÉ IVA '
        'lleva cada cosa.',
    ],
}

# ============================== CAPÍTULO 04 ===============================
PPE_04 = {
    'La primera pregunta no es la licencia: es si la extracción necesita proyecto': [
        'Explicar por qué la primera fila del checklist legal es ésta y no '
        '«¿licencia sí o no?»: freír pide campana y conducto, y si el conducto '
        'tiene que subir a cubierta o cruzar fachada o patio, casi siempre '
        'hace falta proyecto. Las obras que requieren proyecto siguen '
        'necesitando su licencia de obra y su técnico aunque la actividad vaya '
        'por declaración responsable (Ley 12/2012, art. 3.3 y 3.4).',
        'Dar la respuesta de El Molinete, que entra en un local sin salida de '
        'humos: la extracción necesita proyecto, así que licencia de obra y '
        'técnico. Es el caso más duro a propósito, y el que obliga a '
        'presupuestar el conducto aparte (capítulo 8).',
        'Frontera con el capítulo 5: aquí sólo se decide QUÉ papel te toca por '
        'la extracción; qué exige la norma a la campana, a los filtros y al '
        'conducto, y cómo se calcula el riesgo de incendio, es del capítulo '
        'siguiente.',
    ],
    'Despacho o sala: dos regímenes de apertura distintos': [
        'Dar la regla con su norma y su límite dentro: la ACTIVIDAD de un '
        'despacho de masas fritas para llevar, epígrafe 644.6, está en el '
        'Anexo de la Ley 12/2012, así que hasta su umbral de superficie útil '
        'de exposición y venta ninguna administración puede exigirle licencia '
        'previa de actividad y se abre por declaración responsable o '
        'comunicación previa (art. 2.1); y en la misma frase, que las obras '
        'con proyecto van con su licencia aparte.',
        'Y la otra mitad: con mesas o barra (grupo 676 de chocolaterías o '
        'grupo 673 de cafés y bares) la actividad sale del Anexo, que no '
        'contiene ningún grupo de la agrupación de restauración, y el modelo '
        '—licencia o declaración— lo fija tu ayuntamiento. Es la pregunta que '
        'hay que llevar escrita.',
        'Una inferencia declarada, con su nivel: que el obrador de masa anexo '
        'al despacho va dentro de la misma actividad lo sugiere la nota del '
        'epígrafe 644.6, que faculta para elaborar los productos de churrería '
        'en el propio establecimiento si se venden allí; confírmalo con tu '
        'ayuntamiento antes de firmar.',
    ],
    'La terraza y lo que sale a la calle van aparte': [
        'Explicar que la ocupación del dominio público —la terraza, un '
        'conducto o un rótulo sobre la vía pública— no entra en el régimen de '
        'la Ley 12/2012 (art. 2.2): va con su propia autorización municipal, '
        'aparte de la actividad. El Molinete tiene terraza y la pide aparte.',
        'Marcar la frontera de lo que no se puede afirmar: no se ha abierto '
        'ninguna ordenanza de terrazas, así que el plazo, la tasa y las '
        'condiciones son una pregunta para tu ayuntamiento, nunca un dato del '
        'libro.',
    ],
    'El horario: por qué una churrería de desayunos se clasifica como cafetería': [
        'Dar el ejemplo con su norma y sin extrapolarlo: la orden de horarios '
        'de la Comunidad de Madrid de abril de 2022 deja abrir a cafeterías, '
        'bares y cafés-bares desde las 6:00 y a chocolaterías, heladerías y '
        'salones de té desde las 8:00. Una churrería que vive del desayuno, en '
        'ese ejemplo, se clasifica como cafetería o bar, o no abre antes de '
        'las 8:00.',
        'Dar el caso: El Molinete abre a las 7:00 entre semana y a las 6:00 '
        'los sábados, domingos y festivos, así que en el ejemplo de Madrid se '
        'clasifica como cafetería o bar; el libro de temporada cuenta los días '
        'que abre antes de la hora de chocolatería y el libro legal guarda la '
        'norma.',
        'El despacho para llevar, como inferencia declarada: es comercio al '
        'por menor, y la ley de horarios comerciales da libertad horaria a los '
        'comercios por debajo de su umbral de superficie (Ley 1/2004, art. '
        '5.2); confírmalo con tu ayuntamiento, porque la sala sigue el horario '
        'de los establecimientos públicos de tu comunidad. Cada comunidad '
        'tiene su orden de horarios: busca la tuya.',
    ],
    'Las seis comprobaciones de la fase uno, en orden': [
        'Recorrer la primera fase del checklist legal, la de antes de firmar: '
        'si la extracción necesita proyecto, si tu actividad está en el '
        'Anexo, la salida de humos del local, la potencia de la freidora y el '
        'riesgo de incendio, el gas o la freidora eléctrica, y el horario que '
        'te permite tu clasificación. Cada una con su responsable y su plazo '
        'orientativo.',
        'Dar el tamaño del expediente entero y cuántos trámites cambian según '
        'la comunidad autónoma, y decir lo único que controlas del todo: pedir '
        'las cosas pronto. Los plazos dependen de terceros —el ayuntamiento, '
        'el técnico, el instalador, la comunidad de propietarios— y el libro '
        'los trata como orientativos.',
        'Frontera con el capítulo 9: las altas fiscales, el registro '
        'sanitario, el autocontrol y la formación son las fases siguientes del '
        'mismo checklist y tienen su capítulo; aquí sólo lo que hay que saber '
        'ANTES de firmar el alquiler.',
    ],
}

CAP_04 = {
    'n': 4,
    'titulo': 'Antes de Firmar: el Formato Decide el Régimen de Apertura, las Obras y el Horario',
    'resumen_indice': 'la extracción como primera pregunta, despacho o sala y sus dos regímenes de apertura, la terraza que va aparte, el horario del ejemplo de Madrid y las seis comprobaciones de la fase uno.',
    'palabras': 1700, 'bloques': 1,
    'objetivo': 'Que el lector sepa, antes de firmar el alquiler, qué papeles '
                'le tocan por el formato que monta: si la extracción le obliga '
                'a obra con proyecto y licencia, por qué régimen se abre su '
                'actividad (despacho o sala), qué va aparte (la terraza) y a '
                'qué hora puede abrir según cómo se clasifique.',
    'epigrafes': list(PPE_04),
    'puntos_por_epigrafe': PPE_04,
    'puntos_globales': [
        'Capítulo legal: cada afirmación con su norma, su artículo y '
        '«comprobado el 3 de octubre de 2026». Las inferencias van marcadas '
        'como inferencia, con la pregunta que hay que hacer.',
        'El orden del capítulo es el del checklist: primero la extracción, '
        'luego el régimen de la actividad, luego la terraza y el horario.',
        'Ni «necesitas licencia» ni «no la necesitas»: siempre de QUÉ papel '
        'se habla.',
    ],
    'cifras': [
        C('Respuesta de El Molinete a «¿la extracción necesita proyecto?», primera fila del checklist', f'{X_LEGAL}!Checklist Legal (F1-F6)!K7', 'txt', clave='¿La extracción necesita proyecto? (1.ª fila del checklist)'),
        C('Lo que le toca a El Molinete por la extracción', f'{X_LEGAL}!Checklist Legal (F1-F6)!L7', 'txt', clave='Lo que te toca por la extracción'),
        C('Lo que le toca a El Molinete por tener mesas y barra (segunda fila del checklist)', f'{X_LEGAL}!Checklist Legal (F1-F6)!L8', 'txt', clave='Lo que te toca por el Anexo'),
        C('Régimen de apertura de la actividad de El Molinete', f'{X_LEGAL}!Régimen de Apertura y Horario!B13', 'txt', clave='Tu actividad: régimen de apertura'),
        C('Las obras de El Molinete', f'{X_LEGAL}!Régimen de Apertura y Horario!B14', 'txt', clave='Tus obras: licencia aparte'),
        C('La terraza de El Molinete', f'{X_LEGAL}!Régimen de Apertura y Horario!B15', 'txt', clave='Tu terraza: autorización aparte'),
        C('Lo que significa el horario para el desayuno de El Molinete, en el ejemplo de Madrid', f'{X_LEGAL}!Régimen de Apertura y Horario!B25', 'txt', clave='Lo que significa el horario para tu desayuno'),
        C('Días a la semana que El Molinete abre antes de la hora mínima de chocolatería del ejemplo de Madrid', f'{X_TEMP}!Franjas del Día!E16', 'num', clave='Días que se abre antes de la hora mínima de chocolatería'),
        C('Trámites de todo el expediente del checklist legal', f'{X_LEGAL}!Checklist Legal (F1-F6)!D55', 'num', clave='Trámites del expediente'),
        C('Trámites del expediente que cambian según la comunidad autónoma', f'{X_LEGAL}!Checklist Legal (F1-F6)!D63', 'num', clave='Trámites que cambian según la comunidad autónoma'),
    ],
    'sector': ['CUN-35', 'CHN-49', 'CHN-49b', 'CHN-49c', 'CUN-09', 'CUN-14',
               'CUN-34', 'CHN-77', 'CUN-23'],
    'tablas': [
        {
            'titulo': 'La fase uno del checklist legal: lo que se comprueba antes de firmar (checklist-legal-fritura-y-licencias.xlsx, hoja «Checklist Legal (F1-F6)»)',
            'src': (X_LEGAL, 'Checklist Legal (F1-F6)'),
            'cols': [('Trámite', 'C', 'txt'), ('Responsable', 'D', 'txt'),
                     ('Plazo orientativo, días', 'E', 'num'),
                     ('¿Cambia por comunidad?', 'J', 'txt'),
                     ('Tu respuesta', 'K', 'txt'),
                     ('Lo que te toca', 'L', 'txt')],
            'filas': (7, 12),
            'ancla': ('C7', '¿La extracción necesita proyecto?'),
            'nota': V_LEY12,
        },
        {
            'titulo': 'Tu régimen de apertura, tus obras, tu terraza y tu horario (checklist-legal-fritura-y-licencias.xlsx, hoja «Régimen de Apertura y Horario»)',
            'src': (X_LEGAL, 'Régimen de Apertura y Horario'),
            'cols': [('Qué', 'A', 'txt'), ('Lo que te toca', 'B', 'txt')],
            'filas': (13, 27),
            'omitir_filas': (16, 17, 18, 19, 20, 21, 23, 24),
            'ancla': ('A13', 'Tu actividad'),
            'nota': 'El horario es el EJEMPLO de Madrid y no se extrapola. ' + V_HORARIO,
        },
        {
            'titulo': 'Actividad, obra y terraza: tres papeles distintos según el formato',
            'cabecera': ['Papel', 'Despacho para llevar (644.6)',
                         'Local con mesas o barra (676 o 673)', 'Norma'],
            'filas': [
                ['La actividad', 'Declaración responsable o comunicación previa, hasta el umbral de superficie del Anexo', 'Fuera del Anexo: el modelo, licencia o declaración, lo fija tu ayuntamiento', 'Ley 12/2012, art. 2.1 y Anexo'],
                ['Las obras con proyecto (el conducto a cubierta, casi siempre)', 'Licencia de obra y técnico', 'Licencia de obra y técnico', 'Ley 12/2012, art. 3.3 y 3.4'],
                ['La terraza y lo que ocupa la vía pública', 'Autorización municipal aparte', 'Autorización municipal aparte', 'Ley 12/2012, art. 2.2'],
                ['El horario (ejemplo de Madrid)', 'Comercio al por menor: libertad horaria por superficie, a confirmar con tu ayuntamiento', 'Cafetería o bar desde las 6:00; chocolatería desde las 8:00', 'Ley 1/2004, art. 5.2; orden de horarios de Madrid de abril de 2022'],
            ],
            'nota': V_LEY12,
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO escribir «sin licencia» o «con licencia» sin decir de qué '
        'papel: la actividad, la obra y la terraza van cada una por su lado.',
        'PROHIBIDO extrapolar el horario de Madrid a otra comunidad y '
        'PROHIBIDO escribir que una chocolatería puede abrir a las 6:00 en el '
        'ejemplo de Madrid.',
        'PROHIBIDO dar el trámite, la tasa o el plazo de un ayuntamiento '
        'concreto: no se ha abierto ninguna ordenanza de licencias ni de '
        'terrazas.',
        'No expliques aquí las exigencias técnicas de la campana, los filtros, '
        'el conducto o el gas: son del capítulo 5.',
    ],
}

# ============================== CAPÍTULO 05 ===============================
PPE_05 = {
    'Freír pide campana, filtro y conducto a cubierta: el ejemplo de Madrid': [
        'Dar lo que exige la ordenanza de calidad del aire de Madrid, el único '
        'municipio verificado, con su artículo: quien cocina tiene que tener '
        'captación, extracción forzada y filtrado de humos con recogida de '
        'grasas sobre toda la zona de emisión, evacuar por un conducto a '
        'cubierta y limpiarlo al menos una vez al año (Ordenanza 4/2021, art. '
        '23).',
        'La excepción que no te sirve, como inferencia declarada: sólo se '
        'libra del conducto a cubierta quien usa exclusivamente aparatos '
        'eléctricos que cocinan en su interior sin transmitir olores, por '
        'debajo de una potencia conjunta pequeña (art. 24). Una freidora de '
        'baño abierto no cocina «en su interior», así que no hay excepción '
        'para una churrería.',
        'Marcar la frontera de lo verificado: Barcelona, Sevilla o Valencia '
        'tienen sus propias ordenanzas y no se han abierto. Y las reglas de '
        'chimenea que circulan por internet suelen ser las de las viviendas: '
        'el documento de salubridad del Código Técnico sólo trata viviendas y '
        'garajes, y para un local remite al reglamento de instalaciones '
        'térmicas.',
    ],
    'Los litros de la freidora deciden el riesgo de incendio': [
        'Explicar la regla del Código Técnico, con su tabla: las freidoras se '
        'computan a un kilovatio por litro de cuba, tengan la potencia que '
        'tengan, y se suman los demás aparatos de cocción que computan, los '
        'destinados a preparar alimentos y capaces de provocar ignición '
        '(confirma con tu técnico si tus chocolateras al baño maría cuentan). '
        'Por encima del primer umbral la cocina es local de riesgo especial, '
        'bajo, medio o alto, y por encima del último la extinción automática '
        'es obligatoria (tabla 2.1 de la sección de propagación interior).',
        'Dar el caso de El Molinete con sus cifras: litros de cuba, '
        'kilovatios computables de la cocina, riesgo resultante y si la '
        'extinción automática le es obligatoria. Y lo que trae ser local de '
        'riesgo especial: campana separada de materiales combustibles, '
        'conductos resistentes al fuego y filtros a su distancia, que es obra '
        'con proyecto.',
        'Avisar de la compra que mueve los kilovatios: una segunda freidora. '
        'Antes de comprarla, vuelve a la hoja de potencia del libro de '
        'producción, porque los litros suben y con ellos el riesgo.',
    ],
    'Con extinción automática deja de ser local de riesgo especial, pero no te libra de la nota tres': [
        'Dar el matiz que casi nadie cuenta, con su nota: en usos distintos '
        'del hospitalario y del residencial público, una cocina con los '
        'aparatos protegidos por un sistema automático de extinción no se '
        'considera local de riesgo especial (nota (2) de la tabla 2.1), '
        'aunque le sigue aplicando la nota (3): la campana, los conductos y '
        'los filtros.',
        'Presentar las dos salidas con su coste en la calculadora de '
        'inversión: no instalarla y asumir el régimen de local de riesgo '
        'especial que te toque, o instalarla aunque no sea obligatoria; el '
        'libro de inversión suma su importe sólo cuando el libro de producción '
        'dice que la necesitas. La decisión 4 del bonus la resuelve para El '
        'Molinete.',
        'La distancia de los filtros al foco de calor depende del aparato: más '
        'de un metro veinte si es de gas o de parrilla, más de medio metro si '
        'es de otro tipo. El Molinete fríe con gas y le toca la mayor; con '
        'varias freidoras, manda la más exigente.',
    ],
    'Gas en un local: instalación receptora o freidora eléctrica, y nunca la bombona': [
        'Dar la regla con su norma: en un local o en un despacho, una freidora '
        'de gas va con instalación receptora, certificado del instalador e '
        'inspección periódica cada cinco años, que en las instalaciones '
        'pequeñas incluye los aparatos y comprueba la ventilación (RD '
        '919/2006). La alternativa es la freidora eléctrica, que no pide gas y '
        'sí potencia contratada.',
        'La excepción de la bombona, con sus palabras exactas y en su sitio: '
        'no es instalación receptora la que alimenta un único envase de gases '
        'licuados por debajo de su límite de peso, conectado a un solo aparato '
        'DE UTILIZACIÓN MÓVIL. Eso es el puesto de feria del capítulo 14; una '
        'freidora fija en un local no es un aparato móvil, y la bombona no te '
        'libra de nada.',
        'Frontera con el bonus: qué le conviene a El Molinete, gas o '
        'eléctrica, con el precio de ficha de las dos freidoras, es la '
        'decisión 4. Aquí, sólo lo que exige cada opción.',
    ],
    'Fuego de aceite: extintor de clase F y los riesgos de la línea': [
        'Dar la regla con su norma: los agentes extintores tienen que ser '
        'adecuados a la clase de fuego, y los fuegos de aceites y grasas de '
        'cocina son de clase F (reglamento de instalaciones de protección '
        'contra incendios, RD 513/2017). Junto a la freidora, un extintor de '
        'clase F; y nunca agua sobre aceite ardiendo.',
        'Presentar los riesgos de la línea de fritura del libro legal con su '
        'prioridad: quemaduras por salpicadura al cargar la freidora, fuego de '
        'la cuba y de la campana por grasa acumulada, fuga de gas, resbalones, '
        'sobreesfuerzos con sacos y garrafas, cortes en la amasadora, '
        'quemaduras al vaciar el aceite y fatiga de la madrugada. El veredicto '
        'del libro: no se abre la línea con un riesgo alto sin su medida '
        'puesta.',
        'Lo que no fija ni la norma ni el pack: el caudal, la sección y el '
        'trazado del conducto los fija el proyecto técnico, y las '
        'probabilidades y gravedades del libro son supuestos de la casa para '
        'ordenar las medidas, no una evaluación de riesgos laborales.',
    ],
}

CAP_05 = {
    'n': 5,
    'titulo': 'Humos, Extracción y Fuego de Aceite: lo que Exige la Norma y lo que Fija el Proyecto',
    'resumen_indice': 'la campana y el conducto del ejemplo de Madrid, los litros que deciden el riesgo de incendio, la extinción automática y la nota tres del Código Técnico, el gas sin la bombona y el fuego de aceite.',
    'palabras': 1700, 'bloques': 1,
    'objetivo': 'Que el lector entienda qué exige la norma a una cocina que '
                'fríe —campana, filtros, conducto, potencia, gas y extintor— y '
                'qué decide el proyecto técnico, para saber si un local admite '
                'su freidora y qué obra le va a pedir antes de comprar nada.',
    'epigrafes': list(PPE_05),
    'puntos_por_epigrafe': PPE_05,
    'puntos_globales': [
        'Capítulo legal y técnico: cada exigencia con su norma, su artículo o '
        'su nota, y «comprobado el 3 de octubre de 2026». Lo de Madrid, '
        'siempre como ejemplo.',
        'Frontera: el capítulo 4 dice qué papel te toca; éste, qué exige la '
        'norma a la campana, al conducto, a la potencia, al gas y al extintor; '
        'el capítulo 6 lo lleva a la visita del local; el capítulo 10 trata el '
        'aceite como '
        'insumo y como residuo.',
    ],
    'cifras': [
        C('Litros totales de cuba de El Molinete', f'{X_PROD}!Freidoras, Potencia y Riesgo!L5', 'num', clave='Litros totales de cuba'),
        C('Kilovatios de los demás aparatos de cocción de El Molinete (sus dos chocolateras)', f'{X_PROD}!Freidoras, Potencia y Riesgo!D11', 'num', clave='kW de los demás aparatos de cocción'),
        C('Kilovatios computables de la cocina de El Molinete', f'{X_PROD}!Freidoras, Potencia y Riesgo!D12', 'num', clave='kW computables de la cocina'),
        C('Riesgo de la cocina de El Molinete según el Código Técnico', f'{X_PROD}!Freidoras, Potencia y Riesgo!D13', 'txt', clave='Riesgo de la cocina'),
        C('¿Le es obligatoria la extinción automática a El Molinete?', f'{X_PROD}!Freidoras, Potencia y Riesgo!D15', 'txt', clave='¿Extinción automática obligatoria?'),
        C('Veredicto del Código Técnico para la cocina de El Molinete', f'{X_PROD}!Freidoras, Potencia y Riesgo!D20', 'txt', clave='Veredicto del Código Técnico para la cocina'),
        C('Distancia mínima del filtro al foco en El Molinete, en metros', f'{X_PROD}!Freidoras, Potencia y Riesgo!D22', 'num1', clave='Distancia mínima del filtro al foco'),
        C('Kilovatios por encima de los cuales la cocina es local de riesgo especial', f'{X_PROD}!Parámetros!B10', 'num', clave='Umbral de riesgo especial bajo'),
        C('Kilovatios por encima de los cuales el riesgo es alto y la extinción automática es obligatoria', f'{X_PROD}!Parámetros!B12', 'num', clave='Umbral de riesgo alto y extinción automática'),
        C('Importe de la extinción automática en la calculadora de inversión, si te toca (supuesto)', f'{X_CAPEX}!CAPEX por Bloque!H9', 'eur', clave='Importe de la extinción automática si te toca'),
    ],
    'sector': ['CUN-23', 'CUN-24', 'CUN-26', 'CUN-28', 'CUN-38', 'CHN-45',
               'CHN-46', 'CHN-48'],
    'tablas': [
        {
            'titulo': 'La potencia, el riesgo de incendio y la distancia de los filtros en El Molinete (produccion-hora-punta-y-local.xlsx, hoja «Freidoras, Potencia y Riesgo»)',
            'src': (X_PROD, 'Freidoras, Potencia y Riesgo'),
            'cols': [('Concepto', 'B', 'txt'), ('El Molinete', 'D', 'num1')],
            'filas': (9, 22),
            'omitir_filas': (14,),
            'ancla': ('B9', 'Litros totales de cuba'),
            'nota': 'Las freidoras se computan a un kilovatio por litro de cuba; los '
                    'umbrales del riesgo especial y de la extinción automática, la nota (2) y '
                    'la nota (3) son los del Código Técnico. ' + V_CTE,
        },
        {
            'titulo': 'Los papeles de obra, humos y gas que le tocan a El Molinete (checklist-legal-fritura-y-licencias.xlsx, hoja «Licencia, Humos y Gas»)',
            'src': (X_LEGAL, 'Licencia, Humos y Gas'),
            'cols': [('Papel', 'A', 'txt'), ('¿Te toca?', 'B', 'txt'),
                     ('Estado', 'C', 'txt'), ('Por qué', 'E', 'txt')],
            'filas': (25, 30),
            'ancla': ('A25', 'Licencia de obra del conducto'),
            'nota': V_OCAS + ' · Gas: RD 919/2006, inspección periódica de la '
                    'instalación receptora · Clase de fuego: RD 513/2017.',
        },
        {
            'titulo': 'Los riesgos de la línea de fritura, con su prioridad y su medida (checklist-legal-fritura-y-licencias.xlsx, hoja «PRL de la Fritura»)',
            'src': (X_LEGAL, 'PRL de la Fritura'),
            'cols': [('Riesgo', 'B', 'txt'), ('Dónde', 'C', 'txt'),
                     ('Medida', 'D', 'txt'), ('Nivel', 'G', 'num'),
                     ('Prioridad', 'H', 'txt')],
            'filas': (9, 18),
            'ancla': ('B9', 'Quemaduras por salpicadura'),
            'nota': 'Las probabilidades y gravedades son supuestos de la casa para ordenar '
                    'las medidas, no una evaluación de riesgos laborales: esa la firma tu '
                    'servicio de prevención.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar requisitos de humos de un municipio que no sea Madrid, '
        'y PROHIBIDO presentar los de Madrid como norma general.',
        'PROHIBIDO escribir que con poca potencia o con una freidora eléctrica '
        'no hace falta conducto: la excepción de Madrid es para aparatos que '
        'cocinan en su interior, y una freidora de baño abierto no lo hace.',
        'PROHIBIDO dar caudales, secciones o trazados de conducto: los fija '
        'el proyecto técnico.',
        'No expliques aquí qué papeles te tocan (licencia de obra, régimen de '
        'la actividad): son del capítulo 4. Este capítulo da las exigencias '
        'técnicas.',
    ],
}

# ============================== CAPÍTULO 06 ===============================
PPE_06 = {
    'Seis zonas en el local, y la que decide es la más pequeña': [
        'Presentar el reparto de El Molinete como un supuesto declarado: '
        'obrador de masa a la vista, fritura bajo campana, barra y despacho a '
        'calle, sala, aseos y vestuario, y almacén de harina, aceite, envase y '
        'bidón de aceite usado; con los metros de producción y los de atención '
        'al cliente, y la terraza aparte, que no suma a la superficie útil.',
        'La regla que da la hoja de zonas: la zona que decide si el local '
        'sirve es la más pequeña, la de fritura bajo campana, porque es la que '
        'pide conducto, gas o potencia y la que fija el riesgo de incendio. '
        'Antes de repartir el resto, se comprueba que esa zona tiene salida.',
        'Y dos comprobaciones que se hacen sobre el plano y casi nadie hace: '
        'el descuadre entre los metros repartidos y la superficie útil real '
        '(entre la construida y la útil se van con facilidad varios metros), y '
        'que el bidón del aceite usado tenga sitio en el almacén, fuera de la '
        'fritura y de la sala.',
    ],
    'La ficha de visita: cuatro eliminatorios antes que nada': [
        'Explicar el orden de la ficha de visita, que aplica lo que ya '
        'explicaron los capítulos 4 y 5: primero, si la extracción necesita '
        'proyecto; luego, si se puede llevar un conducto a cubierta, con el '
        'permiso de la comunidad de propietarios por escrito; luego, si hay '
        'gas o hay que llevarlo; y luego, si aguanta la potencia y el riesgo '
        'de incendio. Una respuesta que descarta en cualquiera de ellos tumba '
        'el local antes de seguir mirando.',
        'Después, lo que no descarta pero cuesta: la superficie útil, el aseo '
        'de público y el vestuario, el almacén con su bidón y la terraza en la '
        'acera. Dar el veredicto de El Molinete y cuántos ítems le obligan a '
        'obra con proyecto y licencia.',
        'Dar el uso práctico: la ficha se imprime y se lleva a cada visita, '
        'con el técnico si puede ser, y se rellena en el local, no en casa.',
    ],
    'Cuántas raciones por hora aguanta la línea, y quién manda': [
        'Explicar que la capacidad se mide en kilos de masa por hora y sólo al '
        'final se pasa a raciones: la línea de dosificado y fritura con su '
        'churrero, la freidora por tandas y la amasadora. El eslabón más lento '
        'marca el ritmo, y en El Molinete manda la línea con su churrero, no '
        'la máquina.',
        'Avisar de la trampa que más dinero hace perder: el máximo del folleto '
        'del fabricante no es el ritmo de una línea. Los kilos por hora del '
        'libro son un supuesto declarado; el bueno es el que midas tú un '
        'domingo, pesando la masa que entra en una hora.',
        'Dar las raciones por hora que aguanta el conjunto de El Molinete y '
        'qué hacer antes de comprar otra máquina: mejorar primero el eslabón '
        'que manda, porque comprar el segundo es dinero parado.',
    ],
    'La hora punta del domingo, mes a mes': [
        'Cruzar la capacidad de la línea con la hora punta de cada mes: dar el '
        'déficit de la peor hora de un día punta de diciembre frente a lo que '
        'da la línea, que el libro de temporada cuenta en raciones por hora y '
        'en minutos de espera al final de esa hora. La tabla dice en qué meses '
        'se forma cola el domingo.',
        'Dar las palancas en su orden, que no es subir el precio: masa '
        'preparada antes de abrir, una segunda persona en la línea esas '
        'mañanas (el refuerzo de Navidad y Reyes del capítulo 14) y, sólo si '
        'no basta, más línea.',
    ],
    'El traspaso que miras y la renta que pagas': [
        'Presentar los traspasos publicados como lo que son, precios PEDIDOS y '
        'no pagados, cada uno con su zona y sus metros: churrerías de barrio, '
        'cafeterías-churrería y la churrería-chocolatería con sala de '
        'Vallecas, con su renta y los equipos que declara incluidos. Un '
        'anuncio que lleva meses publicado es un precio que no se cierra.',
        'Dar la renta de El Molinete, que es la del anuncio de Vallecas, y '
        'decir qué hay que mirar en un traspaso además del precio: si la '
        'extracción y el conducto están legalizados, si hay gas con su '
        'inspección, si la actividad está a nombre de quien traspasa y qué '
        'equipos funcionan de verdad.',
        'Frontera con el capítulo 8 y con el bonus: lo que cuesta abrir en '
        'obra nueva está en el capítulo 8, y la comparación de dinero entre '
        'traspaso y obra nueva a cinco años es la decisión 2 del bonus.',
    ],
}

CAP_06 = {
    'n': 6,
    'titulo': 'El Local y la Hora Punta: Metros, Conducto, Ficha de Visita y la Cola del Domingo',
    'resumen_indice': 'las seis zonas y la que decide, la ficha de visita con sus cuatro eliminatorios, las raciones por hora que aguanta la línea, la cola del domingo mes a mes y lo que hay que mirar en un traspaso.',
    'palabras': 1800, 'bloques': 1,
    'objetivo': 'Que el lector sepa leer un local antes de firmar: si sus '
                'metros y sus zonas encajan, si pasa los cuatro eliminatorios '
                'de la ficha de visita, cuántas raciones por hora aguantará su '
                'línea y si se le formará cola el domingo; y qué mirar en un '
                'traspaso además del precio.',
    'epigrafes': list(PPE_06),
    'puntos_por_epigrafe': PPE_06,
    'puntos_globales': [
        'Este capítulo aplica en la visita lo que explicaron los capítulos 4 y '
        '5: '
        'remite a ellos en una frase y no repite la norma.',
        'Los metros por zona, los kilos por hora de la línea y las raciones de '
        'cada día son supuestos declarados de El Molinete, y se dicen así.',
    ],
    'cifras': [
        C('Superficie útil del local de El Molinete, en metros cuadrados', f'{X_PROD}!Parámetros!B6', 'num', clave='Superficie útil del local'),
        C('Metros cuadrados de producción (obrador de masa y fritura)', f'{X_PROD}!Zonas y m²!D17', 'num', clave='m² de producción'),
        C('Metros cuadrados de atención al cliente (barra, despacho y sala)', f'{X_PROD}!Zonas y m²!D19', 'num', clave='m² de atención al cliente'),
        C('Veredicto de la ficha de visita para el local de El Molinete', f'{X_PROD}!Ficha de Visita a Local!E21', 'txt', clave='Veredicto de la ficha de visita'),
        C('Ítems de la ficha que obligan a El Molinete a obra con proyecto y licencia', f'{X_PROD}!Ficha de Visita a Local!E17', 'num', clave='Ítems que obligan a obra con proyecto y licencia'),
        C('Eslabón que manda en la línea de El Molinete', f'{X_PROD}!Cuello de Botella!B7', 'txt', clave='Eslabón que manda'),
        C('Raciones por hora que aguanta el conjunto de la línea de El Molinete', f'{X_PROD}!Cuello de Botella!L5', 'num1', clave='Capacidad del conjunto en raciones por hora'),
        C('Déficit de la hora punta de un día punta de diciembre, en raciones por hora', f'{X_TEMP}!Capacidad contra el Pico!I18', 'num1', clave='Déficit de un día punta de diciembre (raciones/h)'),
        C('Espera al final de la hora punta del domingo de diciembre, en minutos', f'{X_TEMP}!Cola del Domingo!H18', 'num1', clave='Espera al final de la hora punta del domingo de diciembre (min)'),
        C('Renta mensual del local de El Molinete, sin IVA (la del anuncio de Vallecas)', f'{X_CAPEX}!Parámetros!L5', 'eur', clave='Renta mensual del local (origen de X18)'),
    ],
    'sector': ['CUS-02', 'CUS-31a', 'CUS-31b', 'CUS-31c', 'CUS-31d',
               'CUS-31e', 'CUS-31g', 'CUS-13', 'CUS-27', 'CUN-23', 'CUN-24'],
    'tablas': [
        {
            'titulo': 'Las seis zonas de El Molinete y lo que tiene que cumplir cada una (produccion-hora-punta-y-local.xlsx, hoja «Zonas y m²»)',
            'src': (X_PROD, 'Zonas y m²'),
            'cols': [('Zona', 'B', 'txt'), ('Bloque', 'C', 'txt'),
                     ('Metros cuadrados', 'D', 'num'),
                     ('Parte del local', 'E', 'pct1'),
                     ('Qué tiene que cumplir', 'F', 'txt')],
            'filas': (6, 11),
            'ancla': ('B6', 'Obrador de masa'),
            'nota': 'El reparto por zonas es un supuesto declarado de El Molinete. La '
                    'terraza va aparte de la superficie útil y con su propia autorización.',
        },
        {
            'titulo': 'La ficha de visita a local de El Molinete, con sus cuatro eliminatorios primero (produccion-hora-punta-y-local.xlsx, hoja «Ficha de Visita a Local»)',
            'src': (X_PROD, 'Ficha de Visita a Local'),
            'cols': [('Qué se comprueba', 'B', 'txt'),
                     ('¿Eliminatorio?', 'C', 'txt'),
                     ('Respuesta', 'E', 'txt'), ('Veredicto', 'I', 'txt')],
            'filas': (6, 13),
            'ancla': ('B6', '¿La extracción necesita proyecto?'),
            'nota': 'Una respuesta que descarta en cualquiera de los cuatro eliminatorios '
                    'tumba el local antes de seguir mirando. La terraza queda «por comprobar» '
                    'hasta que conteste el ayuntamiento.',
        },
        {
            'titulo': 'La cola del domingo, mes a mes (temporada-franjas-y-ferias.xlsx, hoja «Cola del Domingo»)',
            'src': (X_TEMP, 'Cola del Domingo'),
            'cols': [('Mes', 'A', 'txt'),
                     ('Raciones del domingo', 'C', 'num'),
                     ('Hora punta del domingo, raciones por hora', 'D', 'num1'),
                     ('Capacidad de la línea, raciones por hora', 'E', 'num1'),
                     ('Cola, raciones por hora sin servir', 'F', 'num1'),
                     ('¿Hay cola?', 'G', 'txt'),
                     ('Espera al final de la hora punta, minutos', 'H', 'num1')],
            'filas': (7, 18),
            'ancla': ('A7', 'Enero'),
            'nota': 'La cola no se arregla subiendo el precio: se arregla con masa preparada '
                    'antes de abrir y con una segunda persona en la línea esas mañanas.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO presentar un precio de traspaso pedido como precio de '
        'mercado o de cierre, y PROHIBIDO calcular una media o una mediana de '
        'los anuncios.',
        'PROHIBIDO dar el máximo de producción de un fabricante como '
        'capacidad de la línea.',
        'No vuelvas a explicar las normas de humos, potencia o gas: son de los '
        'capítulos 4 y 5; aquí se aplican en la visita.',
    ],
}

# ============================== CAPÍTULO 07 ===============================
# FUNDIDO (D26): 07 Maquinaria + 14 Proveedores de la SPEC. Mitad 1 = las
# máquinas (epígrafes 1-3); mitad 2 = a quién se le compra (epígrafes 4-6).
PPE_07 = {
    'La línea de churros con precio de ficha: dosificadora, freidora, amasadora y campana': [
        'Presentar el núcleo de la dotación de El Molinete con su precio de '
        'ficha sin IVA, máquina a máquina y con su fuente: la freidora de gas '
        'de una cuba, la dosificadora automática, la amasadora automática, la '
        'campana con turbina, las dos chocolateras, el escurridor y la '
        'balanza; y su suma, el núcleo del local con sala.',
        'Y el medidor de polares de mano, que se publica con IVA y cuya base '
        'sin IVA se calcula: sirve para decidir cuándo cambiar el aceite, no '
        'para demostrar el límite legal (capítulo 10). Con él, la dotación con '
        'fuente del local con sala.',
        'Las reglas de lectura de esos precios: son precios de tienda con '
        'descuento y con fecha, que caducan, así que se vuelven a pedir antes '
        'de comprar; un precio «desde» no es una cifra cerrada; y cada línea '
        'dice si su precio lleva IVA.',
    ],
    'Equipo completo o línea separada, y la dotación del despacho': [
        'Explicar las dos maneras de montar la línea: un equipo completo de '
        'churros, dosificador y caldero en una sola pieza, o máquinas '
        'separadas como las de El Molinete. Dar el precio de ficha del equipo '
        'completo de referencia y lo que cambia: el compacto ahorra dinero y '
        'sitio; la línea separada aguanta más kilos por hora y deja cambiar '
        'una pieza sin parar las demás.',
        'Dar el núcleo con fuente del despacho para llevar, que monta el '
        'equipo completo con caldero, pala y escurridor, y su diferencia '
        'frente al local con sala. Qué le conviene a El Molinete y a partir de '
        'qué hora punta se elige lo contrario es la decisión 3 del bonus: aquí '
        'sólo las máquinas.',
    ],
    'Chocolatera, cafetera y las partidas que ninguna ficha publica': [
        'Dar la chocolatera de El Molinete con su fuente y su número de '
        'unidades, y decir que un despacho puede bastarse con una sola.',
        'Enumerar las partidas que van como supuesto declarado porque no hay '
        'precio público verificable —la cafetera, el molinillo, el mostrador, '
        'la vitrina calefactada, las mesas de sala y de terraza, la vajilla, '
        'el lavavajillas, el frigorífico, el extintor de clase F, el filtrado '
        'del aceite, el TPV y el rótulo— y la que pesa más de todas, el '
        'conducto a cubierta con su obra y su proyecto, que presupuesta tu '
        'técnico. La rellenadora va sin cifra: no hay precio utilizable y el '
        'lector pone el suyo.',
        'Dar el método para convertir un supuesto en un número tuyo: tres '
        'presupuestos por partida, con la base del IVA por escrito y el plazo '
        'de entrega dentro.',
    ],
    'Fabricantes y distribuidores de maquinaria, y el plazo de entrega': [
        'FRONTERA del capítulo: lo anterior son las máquinas; desde aquí, a '
        'quién se le compra. Nombrar los fabricantes con catálogo para '
        'churrería y los distribuidores con o sin precios publicados, sin '
        'relación comercial y sólo los que tienen la web comprobada; los que '
        'sólo salen en directorios no se publican.',
        'Dar el plazo de entrega de la maquinaria crítica, que vive en un solo '
        'sitio del pack (el cronograma del libro legal) como supuesto '
        'declarado, y la holgura que le deja a El Molinete antes de mover la '
        'fecha de apertura. Se pide por escrito: si la maquinaria entra en la '
        'ruta crítica, tu apertura la manda el proveedor.',
    ],
    'Preparado para masa, harina, aceite y chocolate: a quién y en qué formato': [
        'Dar los insumos con su formato de compra, su precio sin IVA y su '
        'fuente: el preparado para masa de churro en caja de sacos y lo que '
        'rinde cada saco según el vendedor, el aceite de fritura en garrafa y '
        'el chocolate a la taza en polvo. Y el distribuidor que da formación '
        'con la compra de maquinaria, que es un gancho de venta, no un curso.',
        'Decir lo que no se publica y por qué: la harina especial para '
        'churros de un harinero aparece sin precio, y el chocolate a la taza '
        'en formato profesional de las marcas conocidas no tiene precio con '
        'fuente. El escandallo de esos insumos es del capítulo 12, y su IVA, '
        'del capítulo 3.',
    ],
    'Envase para llevar y gestor del aceite usado': [
        'Dar el cucurucho de cartón con su precio, cuya base sin IVA es '
        'inferida (celda verde, por defecto «no lleva»), y el vaso: el de '
        'plástico o papel plastificado se cobra aparte en el tique desde 2023 '
        '(Ley 7/2022). El cucurucho de cartón no se presenta como conforme a '
        'esa ley mientras no conozcas su composición: pregúntala por escrito.',
        'Elegir el gestor del aceite usado: tiene que ser un gestor '
        'autorizado, con contrato y justificante de cada retirada (la recogida '
        'separada del aceite de cocina usado de la hostelería es obligatoria '
        'desde junio de 2022, Ley 7/2022). Un ejemplo de Madrid, sin relación '
        'comercial, que recoge sin coste a cambio de obsequios o valoración. '
        'Cuánto aceite le llevas y cuánto te cuesta es del capítulo 10.',
    ],
}

CAP_07 = {
    'n': 7,
    'titulo': 'Maquinaria y Proveedores: Churrera, Dosificadora, Freidora, Chocolatera, Harina, Aceite, Envase y Gestor',
    'resumen_indice': 'la línea de churros con su precio de ficha, equipo completo o línea separada, las partidas sin precio publicado, fabricantes y plazo de entrega, el preparado y el aceite, y el envase y el gestor del aceite usado.',
    'palabras': 2300, 'bloques': 1,
    'objetivo': 'Que el lector sepa qué maquinaria necesita una churrería con '
                'sala y cuál un despacho, cuánto cuesta lo que tiene precio de '
                'ficha y qué tiene que presupuestar él, y a quién comprarle '
                'las máquinas, el preparado, el aceite, el envase y el '
                'servicio del gestor del aceite usado.',
    'epigrafes': list(PPE_07),
    'puntos_por_epigrafe': PPE_07,
    'puntos_globales': [
        'Capítulo FUNDIDO en dos mitades con frontera explícita: primero las '
        'máquinas (qué y cuánto), luego los proveedores (a quién y en qué '
        'formato). No repitas en la segunda lo que dijo la primera.',
        'Cada precio con su fuente, su fecha y su base de IVA en la misma '
        'frase; un «desde» se dice «desde».',
        'Frontera con los vecinos: el capítulo 8 suma la inversión entera y '
        'el capítulo 10 trata el aceite como coste y como residuo; aquí sólo se '
        'eligen '
        'máquinas, insumos y proveedores.',
    ],
    'cifras': [
        C('Núcleo con precio de ficha del local con sala, sin IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!X36', 'eur2', clave='Núcleo con precio de ficha del local con sala'),
        C('Medidor de polares de mano, base sin IVA calculada desde su precio con IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!O13', 'eur2', clave='Medidor de polares, base sin IVA'),
        C('Dotación con fuente del local con sala, sin IVA y con el medidor de polares', f'{X_CAPEX}!Equipamiento Línea a Línea!X35', 'eur2', clave='Dotación con fuente del local con sala, con el medidor de polares'),
        C('Núcleo con precio de ficha del despacho para llevar, sin IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!Y36', 'eur2', clave='Núcleo con precio de ficha del despacho'),
        C('Diferencia de dotación del despacho frente al local con sala', f'{X_CAPEX}!Variante del Formato!D7', 'eur2', clave='Diferencia de dotación del despacho frente al local con sala'),
        C('Conducto a cubierta, obra y proyecto: supuesto de El Molinete, sin IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!L20', 'eur', clave='Conducto a cubierta, obra y proyecto'),
        C('Precio de la caja de preparado para masa de churro, sin IVA', f'{X_CARTA}!Parámetros!B33', 'eur2', clave='Precio de la caja de preparado para masa'),
        C('Precio de la garrafa de aceite de fritura, sin IVA', f'{X_CARTA}!Parámetros!B34', 'eur2', clave='Precio del aceite por garrafa'),
        C('Plazo del pedido de la maquinaria crítica, en días (supuesto de El Molinete)', f'{X_LEGAL}!Checklist Legal (F1-F6)!E33', 'num', clave='Plazo en días del pedido de maquinaria crítica'),
        C('Holgura de la maquinaria en el cronograma de El Molinete, en meses', f'{X_LEGAL}!Cronograma y Ruta Crítica!C55', 'num1', clave='Holgura de la maquinaria (meses)'),
    ],
    'sector': ['CUS-32a', 'CUS-33a', 'CUS-34c', 'CUS-35a', 'CUS-36a',
               'CUS-36b', 'CUS-37a', 'CUS-38', 'CUS-39', 'CUS-41', 'CUS-43',
               'CUS-44a', 'CUS-44b', 'CUS-44e', 'CUS-44f', 'CUS-44h',
               'CUS-21', 'CUS-23', 'CUS-24', 'CUS-25', 'CUN-41', 'CUN-27'],
    'tablas': [
        {
            'titulo': 'La dotación con precio de ficha de El Molinete, máquina a máquina (calculadora-capex-churreria.xlsx, hoja «Equipamiento Línea a Línea»)',
            'src': (X_CAPEX, 'Equipamiento Línea a Línea'),
            'cols': [('Partida', 'C', 'txt'), ('Fuente', 'D', 'txt'),
                     ('Cómo publica la fuente el precio', 'E', 'txt'),
                     ('Precio de referencia sin IVA, por unidad', 'R', 'eur2'),
                     ('Unidades en el local con sala', 'V', 'num'),
                     ('Unidades en el despacho', 'W', 'num')],
            'filas': (6, 14),
            'ancla': ('C6', 'Freidora de churros de gas'),
            'nota': 'Precios de tienda con descuento, consultados el 3 de octubre de 2026: '
                    'vuelve a pedirlos antes de comprar. La rellenadora va sin cifra porque no '
                    'hay precio utilizable: pon tu presupuesto.',
        },
        {
            'titulo': 'Las alternativas con precio de ficha: el equipo completo, el amasado a mano y la freidora eléctrica (calculadora-capex-churreria.xlsx, hoja «Equipamiento Línea a Línea»)',
            'src': (X_CAPEX, 'Equipamiento Línea a Línea'),
            'cols': [('Partida', 'C', 'txt'), ('Fuente', 'D', 'txt'),
                     ('Cómo publica la fuente el precio', 'E', 'txt'),
                     ('Precio de referencia sin IVA', 'R', 'eur2'),
                     ('Unidades en el despacho', 'W', 'num')],
            'filas': (15, 19),
            'ancla': ('C15', 'Equipo completo de churros'),
            'nota': 'Un precio «desde» no es una cifra cerrada. La freidora eléctrica es la '
                    'otra salida de la decisión 4 del bonus.',
        },
        {
            'titulo': 'Los proveedores con la web comprobada (calculadora-capex-churreria.xlsx, hoja «Proveedores»)',
            'src': (X_CAPEX, 'Proveedores'),
            'cols': [('Proveedor', 'B', 'txt'), ('Qué ofrece', 'C', 'txt'),
                     ('Web', 'D', 'txt'), ('Id del dato', 'E', 'txt')],
            'filas': (6, 10),
            'ancla': ('B6', 'Churrofácil'),
            'nota': 'Sin relación comercial: están para pedir precio. No se publican los que '
                    'sólo salen en directorios.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar como dato un precio para la rellenadora, el conducto, '
        'la cafetera, la vitrina o el TPV: son supuestos o importes del '
        'lector.',
        'PROHIBIDO sumar o restar dotaciones con bases de IVA distintas, y '
        'PROHIBIDO presentar la dotación con precio de ficha como presupuesto '
        'de apertura.',
        'PROHIBIDO presentar la formación gratuita de un distribuidor como un '
        'curso de churrero.',
        'No expliques aquí el CAPEX por bloques ni el IVA que adelantas: son '
        'del capítulo 8; ni el escandallo de los insumos: es del 12.',
    ],
}

# ============================== CAPÍTULO 08 ===============================
PPE_08 = {
    'Por qué no damos un número de churrería, sino el modelo que da el tuyo': [
        'Empezar por el problema: las horquillas de inversión que circulan '
        'para «montar una churrería» se copian unas a otras, no dicen de qué '
        'formato hablan y no salen de ninguna suma. La guía no da otra '
        'horquilla: da once bloques con su importe, y el lector cambia los '
        'suyos.',
        'Dar las tres cifras de El Molinete que no hay que confundir —el CAPEX '
        'sin IVA y sin fondo de maniobra, el IVA que se adelanta y el '
        'desembolso total con IVA— y decir para qué sirve cada una.',
    ],
    'Los once bloques de la inversión, del local en bruto al marketing de apertura': [
        'Recorrer los bloques con su importe: la obra y el acondicionamiento '
        'del local en bruto, que es un supuesto por metro cuadrado y el bloque '
        'más grande; la extracción y el conducto; la fritura, la dosificación '
        'y el amasado; el chocolate y el café; la barra, la sala y la terraza; '
        'el control y la seguridad; el TPV y el rótulo; las licencias, el '
        'proyecto de actividad y las tasas; la fianza; el stock inicial y el '
        'envase; y el marketing de apertura.',
        'Explicar los bloques que más se olvidan: el de licencias, proyecto y '
        'tasas, que es un supuesto y nunca una horquilla copiada; la fianza, '
        'que se recupera y no se amortiza; el stock inicial, que se calcula '
        'con los precios del libro de la carta; y la línea de extinción '
        'automática, que sólo suma si el libro de producción dice que la '
        'necesitas (en El Molinete, no).',
        'Dar el inmovilizado amortizable y decir qué queda fuera: la fianza, '
        'el stock y el marketing no se amortizan.',
    ],
    'El IVA que adelantas no es inversión, es caja': [
        'Dar el IVA soportado de la inversión de El Molinete junto al '
        'desembolso con IVA, y explicar que sale de la cuenta el día que pagas '
        'y vuelve después, al ritmo al que factures, no en una fecha. Casi todo '
        'va al tipo general; sólo el stock de alimentos va al reducido. Las '
        'reglas del IVA están en el capítulo 3: aquí sólo su efecto en la '
        'caja.',
        'La consecuencia que se negocia con el banco: el desembolso con IVA es '
        'lo que tienes que poder pagar al abrir, aunque una parte vuelva. '
        'Cuéntalo aparte del préstamo.',
    ],
    'El fondo de maniobra no está aquí: se calcula en el plan financiero': [
        'Explicar la diferencia que más confusión crea: el fondo de maniobra '
        'NO es inversión, es caja para pagar los fijos mientras el negocio '
        'arranca y en el valle del verano. La calculadora de inversión no lo '
        'lleva a propósito; se calcula en el plan financiero, con los gastos '
        'fijos y los meses de colchón, y la inversión total es la suma de los '
        'dos.',
        'Dar el fondo de maniobra y la inversión total de El Molinete y '
        'remitir al capítulo 16 para cómo se financian.',
    ],
    'Contra qué contrastar tu cifra': [
        'Dar la única referencia de contraste que trae el pack: los equipos '
        'que declara incluidos el traspaso de Vallecas para un local de tamaño '
        'parecido, frente al equipamiento y el mobiliario de los bloques de El '
        'Molinete. No es una validación: es un orden de magnitud para saber si '
        'te has olvidado algo.',
        'Y el control que de verdad sirve: la desviación de tus importes '
        'contra el precio de referencia de cada línea, que el libro calcula en '
        'cuanto metes tus presupuestos. Una línea fuera de tu horquilla se '
        'mira antes de firmar el pedido.',
    ],
}

CAP_08 = {
    'n': 8,
    'titulo': 'Cuánto Cuesta Abrir, Partida a Partida',
    'resumen_indice': 'por qué no damos un número sino el modelo, los once bloques de la inversión, el IVA que adelantas como caja, el fondo de maniobra que se calcula aparte y contra qué contrastar tu cifra.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector construya su propia cifra de apertura bloque a '
                'bloque, sin horquillas copiadas: qué cuesta cada bloque en El '
                'Molinete, qué es supuesto y qué tiene fuente, cuánto IVA '
                'adelanta y por qué el fondo de maniobra se calcula en otro '
                'sitio.',
    'epigrafes': list(PPE_08),
    'puntos_por_epigrafe': PPE_08,
    'puntos_globales': [
        'Llega con la extracción, la obra, la maquinaria y el IVA ya '
        'explicados (capítulos 3 a 7): remite a ellos en una frase y suma.',
        'Todo en base imponible, con el IVA aparte y dicho como caja.',
    ],
    'cifras': [
        C('CAPEX total de El Molinete, sin IVA y sin fondo de maniobra', f'{X_CAPEX}!CAPEX por Bloque!E45', 'eur2', clave='CAPEX total sin fondo de maniobra'),
        C('IVA soportado del CAPEX, que se adelanta', f'{X_CAPEX}!CAPEX por Bloque!F45', 'eur2', clave='IVA soportado del CAPEX'),
        C('Desembolso total con IVA', f'{X_CAPEX}!CAPEX por Bloque!G45', 'eur2', clave='Desembolso total con IVA'),
        C('Inmovilizado amortizable', f'{X_CAPEX}!CAPEX por Bloque!I45', 'eur2', clave='Inmovilizado amortizable'),
        C('Bloque de obra y acondicionamiento del local en bruto, sin IVA', f'{X_CAPEX}!CAPEX por Bloque!K6', 'eur', clave='Obra y acondicionamiento del local'),
        C('Coste de obra por metro cuadrado de local en bruto (supuesto de El Molinete)', f'{X_CAPEX}!Parámetros!B11', 'eur', clave='Coste de obra por m²'),
        C('Bloque de licencias, proyecto de actividad y tasas, sin IVA (supuesto de El Molinete)', f'{X_CAPEX}!CAPEX por Bloque!E41', 'eur', clave='Bloque 8: Licencias, proyecto de actividad y tasas'),
        C('Equipamiento y mobiliario de los bloques dos a siete, sin IVA', f'{X_CAPEX}!Resumen!B22', 'eur2', rotulo=('A22', 'Equipamiento y mobiliario')),
        C('Fondo de maniobra de El Molinete, que calcula el plan financiero', f'{X_PLAN}!Inversión Inicial!B19', 'eur', clave='Fondo de maniobra'),
        C('Inversión total de El Molinete: CAPEX más fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B24', 'eur', clave='Inversión total (CAPEX más fondo de maniobra)'),
    ],
    'sector': ['CUS-02', 'CUS-32a', 'CUS-33a', 'CUS-34c', 'CUS-35a',
               'CUS-36a', 'CUS-36b', 'CUS-37a', 'CUS-38', 'CUS-39', 'CUS-41',
               'CUS-43', 'CHN-71c'],
    'tablas': [
        {
            'titulo': 'Los once bloques del CAPEX de El Molinete, sin fondo de maniobra (calculadora-capex-churreria.xlsx, hoja «CAPEX por Bloque»)',
            'src': (X_CAPEX, 'CAPEX por Bloque'),
            'cols': [('Bloque', 'B', 'txt'), ('Base sin IVA', 'E', 'eur'),
                     ('IVA soportado', 'F', 'eur'), ('Total con IVA', 'G', 'eur'),
                     ('Parte del CAPEX', 'H', 'pct1'),
                     ('Procedencia', 'J', 'txt')],
            'filas': (34, 45),
            'ancla': ('B34', 'Obra civil'),
            'nota': 'Los importes de obra, conducto, licencias, barra y sala, TPV y '
                    'marketing son supuestos declarados de El Molinete: cámbialos por tus '
                    'presupuestos. El fondo de maniobra no está aquí: lo calcula el plan '
                    'financiero.',
        },
        {
            'titulo': 'Lo que no es máquina: obra, proyecto, licencias, fianza, stock y marketing (calculadora-capex-churreria.xlsx, hoja «CAPEX por Bloque»)',
            'src': (X_CAPEX, 'CAPEX por Bloque'),
            'cols': [('Partida', 'C', 'txt'), ('Procedencia', 'D', 'txt'),
                     ('Tu importe', 'H', 'eur'),
                     ('¿Tu importe lleva IVA?', 'I', 'txt'),
                     ('Base sin IVA', 'K', 'eur'),
                     ('¿Se amortiza?', 'N', 'txt')],
            'filas': (6, 12),
            'ancla': ('C6', 'Obra y acondicionamiento'),
            'nota': 'La línea de la extinción automática sólo suma cuando el libro de '
                    'producción dice que tu cocina la necesita: en El Molinete su base es '
                    'cero. Las tasas y la fianza no llevan IVA.',
        },
        {
            'titulo': 'Las cifras que van al banco y al plan financiero (calculadora-capex-churreria.xlsx, hoja «Resumen»)',
            'src': (X_CAPEX, 'Resumen'),
            'cols': [('Cifra', 'A', 'txt'), ('Valor', 'B', 'eur'),
                     ('De dónde sale', 'C', 'txt')],
            'filas': (17, 22),
            'ancla': ('A17', 'CAPEX TOTAL'),
            'nota': 'El CAPEX sin fondo de maniobra es la cifra que copia el plan financiero; '
                    'el IVA vuelve al ritmo al que factures.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar una horquilla de inversión «de una churrería» o de '
        'licencias: el pack da once bloques con su importe y su procedencia.',
        'PROHIBIDO sumar el fondo de maniobra al CAPEX dentro de la '
        'calculadora o contarlo dos veces: se suma sólo en el plan '
        'financiero.',
        'No expliques las reglas del IVA (son del capítulo 3) ni el detalle de '
        'cada máquina (es del capítulo 7): aquí se suman.',
    ],
}

# ============================== CAPÍTULO 09 ===============================
PPE_09 = {
    'Cuatro casillas del impuesto para el churro, y la que te toca': [
        'Dar las casillas del impuesto sobre actividades económicas que tocan '
        'al churro, cada una con su nota y su formato: el epígrafe 644.6 '
        '(comercio al por menor de masas fritas), que faculta para elaborar '
        'los productos de churrería en el propio establecimiento si se venden '
        'allí; el epígrafe 663.1 (venta fuera de establecimiento permanente), '
        'con nota propia de churrería, para la caseta; el epígrafe 419.3 '
        '(industria de masas fritas), que marca la frontera del obrador que '
        'fabrica para otros; y la sala, en el grupo 676 de chocolaterías o en '
        'el grupo 673 de cafés y bares.',
        'La inferencia que se lleva al asesor, con su nivel: la nota que '
        'faculta a los grupos de restaurantes, cafeterías y bares para vender '
        'en su propio establecimiento los productos de su servicio no la lleva '
        'el grupo 676, y cada cuota faculta sólo para su actividad (regla 4.ª '
        'de la Instrucción). Así que una sala en el grupo 676 que además vende '
        'churros al peso para llevar puede necesitar también el epígrafe '
        '644.6: es una pregunta, no una afirmación.',
        'Dar el caso de El Molinete: dos formatos (sala y despacho), los '
        'epígrafes candidatos que lleva a su asesor y la respuesta del libro a '
        'si necesita el 644.6 además del de la sala.',
    ],
    'Alta sí, pago casi nunca': [
        'Dar la regla con su norma: el alta en el impuesto de actividades se '
        'hace igual, porque el epígrafe define lo que puedes hacer, pero están '
        'exentos los dos primeros años de actividad, todas las personas '
        'físicas y las sociedades por debajo del millón de euros de cifra de '
        'negocio (texto refundido de la Ley de Haciendas Locales, art. 82.1).',
        'Una sola línea, y aquí, sobre la nota del grupo de chocolaterías que '
        'rebaja la cuota a quien abre seis meses o menos al año: existe, pero '
        'con la exención casi nunca te toca, y cerrar julio y agosto no es '
        'abrir seis meses. No es una salida para el verano (capítulo 14).',
    ],
    'El código de actividad no sale de una tabla: es una pregunta para tu asesor': [
        'Decir la verdad: no hay una tabla oficial que lleve los epígrafes de '
        'la churrería a la clasificación nacional de actividades de 2025, y '
        'las notas explicativas del INE clasifican por actividad sin nombrar '
        'ni el churro ni la chocolatería. La correspondencia candidata es una '
        'inferencia, y el libro legal la da como pregunta redactada para tu '
        'asesor.',
        'Lo que sí es norma: al darte de alta comunicas el código de 2025 y, '
        'además, el de 2009, mientras no se adapte la tarifa de accidentes: '
        'dos códigos, no uno (RD 10/2025). Y la trampa verificada: quien copie '
        'el antiguo código de los puestos de venta de alimentos se encuentra '
        'en la clasificación de 2025 con la clase 47.81, que hoy es la venta '
        'de vehículos de motor.',
    ],
    'Registro sanitario: el de tu comunidad, no el general': [
        'Dar la regla con su norma: el comercio al por menor —y una churrería '
        'que vende al consumidor final en su local, su despacho o su caseta lo '
        'es— queda excluido del registro general sanitario y se inscribe en el '
        'registro de su comunidad autónoma por comunicación o declaración '
        'responsable, que no habilita por sí sola (RD 191/2011, art. 2.2, en '
        'la redacción del RD 1021/2022). El trámite cambia en cada comunidad.',
        'Marcar la frontera: lo que cambia las cosas es servir churros a OTRO '
        'negocio. La guía del registro de la Comunidad de Madrid pone como '
        'ejemplo de actividad restringida la churrería o pastelería que sirve '
        'a la cafetería, y servir a un establecimiento inscrito en el registro '
        'general rompe la excepción. El obrador que fabrica para otros queda '
        'fuera de este producto: si es tu caso, pregunta a tu comunidad.',
        'Desmontar una frase que circula: no es verdad que la inspección de '
        'sanidad venga antes de la licencia. El orden de los papeles es el del '
        'checklist.',
    ],
    'Las fases dos y cinco del expediente, en orden': [
        'Recorrer la fase dos del checklist legal —constituir la sociedad o '
        'darse de alta como autónomo, el alta censal con el doble código, el '
        'alta en el impuesto, el encargo del proyecto técnico de actividad y '
        'de la extracción, y la firma del arrendamiento con su fianza— con su '
        'responsable y su plazo orientativo. Y una línea sobre la facturación '
        'verificable: llega en 2027, para las sociedades en enero y para el '
        'resto en julio, así que el TPV que compres ya debe estar adaptado.',
        'Y la fase cinco, la sanitaria: la comunicación al registro '
        'autonómico, el plan de autocontrol con responsable y registro del '
        'aceite, los alérgenos por escrito, la acrilamida como buena práctica, '
        'el registro de formación, la denominación del chocolate según la '
        'etiqueta del preparado y el vaso cobrado aparte. Frontera: el detalle '
        'de cada una es de los capítulos 3, 10 y 11; aquí, sólo su sitio en el '
        'orden.',
    ],
}

CAP_09 = {
    'n': 9,
    'titulo': 'Alta Fiscal y Sanitaria de Cada Formato: Epígrafe, Código de Actividad y Registro',
    'resumen_indice': 'las casillas del impuesto de actividades para el churro, el alta que casi nunca paga, el código de actividad como pregunta al asesor, el registro sanitario autonómico y las fases dos y cinco del expediente.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector sepa con qué epígrafes se da de alta según su '
                'formato, por qué casi nunca paga el impuesto de actividades, '
                'por qué su código de actividad es una pregunta para el asesor '
                'y en qué registro sanitario se inscribe, y en qué orden van '
                'esos papeles.',
    'epigrafes': list(PPE_09),
    'puntos_por_epigrafe': PPE_09,
    'puntos_globales': [
        'Capítulo legal: cada epígrafe con su nota y su norma, y «comprobado '
        'el 3 de octubre de 2026». Las inferencias van como pregunta al '
        'asesor, con su nivel.',
        'Frontera: aquí se dan de alta el negocio y su registro; el capítulo 4 '
        'ya resolvió el régimen de apertura y el capítulo 11 resuelve el '
        'autocontrol.',
    ],
    'cifras': [
        C('Formatos que le tocan a El Molinete en el árbol del impuesto de actividades', f'{X_LEGAL}!Árbol IAE y CNAE por Formato!B21', 'num', clave='Formatos que te tocan'),
        C('Epígrafes candidatos que El Molinete lleva a su asesor', f'{X_LEGAL}!Árbol IAE y CNAE por Formato!B23', 'txt', clave='Epígrafes candidatos que llevas a tu asesor'),
        C('¿Necesita El Molinete el 644.6 además del epígrafe de la sala?', f'{X_LEGAL}!Árbol IAE y CNAE por Formato!B22', 'txt', clave='¿Necesitas el 644.6 además de la sala?'),
        C('¿Paga El Molinete el impuesto de actividades?', f'{X_LEGAL}!Árbol IAE y CNAE por Formato!B24', 'txt', clave='¿Pagas el impuesto? (exención)'),
        C('La pregunta del código de actividad, redactada para el asesor', f'{X_LEGAL}!Árbol IAE y CNAE por Formato!B25', 'txt', clave='La pregunta del CNAE para tu asesor'),
        C('Régimen sanitario de El Molinete', f'{X_LEGAL}!Árbol de Registro Sanitario!B11', 'txt', clave='Tu régimen sanitario'),
        C('El trámite sanitario que le toca a El Molinete', f'{X_LEGAL}!Árbol de Registro Sanitario!B12', 'txt', clave='El trámite sanitario que te toca'),
    ],
    # Fuera a propósito: CUN-10 y CUN-13 (su cifra viaja al prompt como
    # «condición de la media cuota», D14 / A3) — la nota del 676 va en una
    # línea de los puntos, sin esas palabras.
    'sector': ['CUN-09', 'CUN-11', 'CUN-12', 'CUN-14', 'CUN-15', 'CUN-16',
               'CUN-V03', 'CUN-21', 'CUN-30', 'CHN-39', 'CHN-41', 'CHN-73',
               'CHN-74b', 'CHN-94', 'CHN-75'],
    'tablas': [
        {
            'titulo': 'Los formatos y los epígrafes candidatos de cada uno (checklist-legal-fritura-y-licencias.xlsx, hoja «Árbol IAE y CNAE por Formato»)',
            'src': (X_LEGAL, 'Árbol IAE y CNAE por Formato'),
            'cols': [('Formato', 'A', 'txt'), ('¿Te toca?', 'B', 'txt'),
                     ('Epígrafe del impuesto, candidato', 'C', 'txt'),
                     ('Código de actividad para preguntar a tu asesor', 'D', 'txt')],
            'filas': (15, 18),
            'ancla': ('A15', 'Local con sala'),
            'nota': 'La correspondencia oficial entre el epígrafe del impuesto y la '
                    'clasificación de actividades de 2025 no está publicada para la churrería: '
                    'los códigos de la última columna son la pregunta para tu asesor, nunca un '
                    'dato. ' + V_IAE,
        },
        {
            'titulo': 'Dónde caes en el registro sanitario (checklist-legal-fritura-y-licencias.xlsx, hoja «Árbol de Registro Sanitario»)',
            'src': (X_LEGAL, 'Árbol de Registro Sanitario'),
            'cols': [('Tu situación', 'A', 'txt'), ('Lo que te toca', 'B', 'txt'),
                     ('Por qué', 'C', 'txt')],
            'filas': (18, 20),
            'ancla': ('A18', 'Vendes al consumidor final'),
            'nota': V_SANITARIO,
        },
        {
            'titulo': 'La fase dos del checklist: sociedad, altas fiscales y proyecto técnico (checklist-legal-fritura-y-licencias.xlsx, hoja «Checklist Legal (F1-F6)»)',
            'src': (X_LEGAL, 'Checklist Legal (F1-F6)'),
            'cols': [('Trámite', 'C', 'txt'), ('Responsable', 'D', 'txt'),
                     ('Plazo orientativo, días', 'E', 'num'),
                     ('¿Cambia por comunidad?', 'J', 'txt')],
            'filas': (16, 20),
            'ancla': ('C16', 'Constituir la sociedad'),
            'nota': 'Los plazos son orientativos y dependen de terceros: la gestoría, la '
                    'ingeniería y el arrendador.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar una cuota del impuesto de actividades o presentar la '
        'rebaja de cuota de temporada como ahorro o como salida del verano: '
        'una sola línea, en este capítulo, diciendo que casi nunca te toca.',
        'PROHIBIDO dar como dato el código de actividad que corresponde a cada '
        'epígrafe: es una pregunta para el asesor, con los dos códigos.',
        'PROHIBIDO escribir que la caseta de feria va al registro general '
        'sanitario o que la inspección de sanidad viene antes de la licencia.',
        'No desarrolles aquí el autocontrol, los alérgenos ni el aceite: son '
        'de los capítulos 10 y 11.',
    ],
}

# ============================== CAPÍTULO 10 ===============================
PPE_10 = {
    'La norma del aceite: compuestos polares por debajo del límite, medidos en laboratorio': [
        'Dar la regla con su norma y su ámbito: la norma de calidad de los '
        'aceites y grasas calentados es norma básica y alcanza a las '
        'freidurías, los bares, las cocinas de comida para llevar y los '
        'puestos de feria, permanentes o de temporada; el aceite de fritura '
        'tiene que tener los compuestos polares por debajo de su límite, '
        'determinados con el método de su anexo 1, una cromatografía en '
        'columna de laboratorio (Orden de 26 de enero de 1989, arts. 3 y 6).',
        'Lo que hace y lo que no hace el medidor de mano: te dice cuándo '
        'cambiar el aceite y su lectura se apunta en tu registro, pero el '
        'límite legal se prueba en laboratorio, con el método del anexo. El '
        'medidor no prueba que cumples.',
        'Lo derogado y lo vivo: los artículos de las manipulaciones permitidas '
        'están derogados, así que rellenar la cuba es una decisión de cocina, '
        'no un permiso de la norma; el artículo 9 sigue vivo y prohíbe añadir '
        'al baño sustancias extrañas y vender el aceite usado para uso '
        'alimentario.',
    ],
    'Dos aceites por ración: el que se lleva la masa y el que tiras al cambiar': [
        'Separar las dos partidas que casi todo el mundo mezcla: el aceite '
        'absorbido, que se queda en la masa y ya está dentro del coste de '
        'materia de la ración en el libro de la carta, y la renovación, el '
        'aceite que tiras al cambiar la cuba, que calcula el libro del aceite. '
        'El plan financiero suma las dos, cada una con su fuente; meter la '
        'renovación también en el escandallo la contaría dos veces.',
        'Dar las cifras de El Molinete: el aceite total por ración y qué parte '
        'de él es renovación, con el veredicto del libro. La lectura que '
        'importa: cuando el aceite que tiras al cambiar la cuba pesa más que '
        'el que se lleva la masa, cada día de cuba cuenta más que la '
        'absorción.',
    ],
    'Cada cuántos días cambias, y cuánto vale un día de cuba': [
        'Explicar el punto económico de cambio con el ciclo de El Molinete, '
        'que es un supuesto declarado: lo que cuesta al mes la renovación con '
        'su ciclo, lo que cuesta cambiar un día antes y lo que ahorra alargar '
        'un día si el medidor lo permite. El día del cambio lo decide la '
        'lectura del medidor, no la tabla: la tabla dice cuánto dinero hay en '
        'juego.',
        'Dónde vive el dato bueno: los días entre cambios del lector salen de '
        'su registro del aceite en el Pack Plantillas APPCC (fichero '
        '09-control-aceite-fritura.xlsx, hoja «Control Aceite»), contando los '
        'días entre dos cambios. Este libro no compara marcas ni tipos de '
        'aceite: trabaja con tu aceite, tu precio y tu registro.',
    ],
    'Si sube el aceite: lo que pierdes al mes y al año': [
        'Dar los tres escenarios de subida del precio del aceite del libro y '
        'lo que El Molinete pierde de margen al mes y al año en cada uno si no '
        'toca el precio de venta. El margen que se pierde sale del aceite que '
        'se COMPRA (la renovación más la reposición), no de las raciones.',
        'Dónde se cambia el precio: en una sola celda del libro de la carta, '
        'que lo pasa al libro del aceite y a la calculadora de inversión; '
        'nunca en dos sitios a la vez.',
    ],
    'El gestor del aceite usado: recogida separada, papeles y litros': [
        'Dar la obligación con su norma: el aceite de cocina usado de la '
        'hostelería tiene recogida separada obligatoria desde junio de 2022 '
        '(Ley 7/2022), así que hace falta contrato con un gestor autorizado y '
        'archivar el justificante de cada retirada. La prohibición de verterlo '
        'por el desagüe la fijan las ordenanzas municipales: mira la tuya.',
        'Dar los litros que El Molinete entrega al gestor cada mes, y que su '
        'gestor de ejemplo recoge sin coste. Cada retirada se anota en el '
        'registro del Pack APPCC (hoja «Retirada de aceite usado») y el libro '
        'del aceite sólo contrasta los litros del mes.',
    ],
}

CAP_10 = {
    'n': 10,
    'titulo': 'Aceite de Fritura: Calidad, Cambio, Coste y Gestor',
    'resumen_indice': 'la norma del aceite y el medidor de mano, los dos aceites de cada ración, cuánto vale un día de cuba, lo que te quita una subida del aceite y el gestor del aceite usado.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector sepa qué exige la norma al aceite de fritura y '
                'cómo se prueba, cuánto le cuesta el aceite por ración '
                'separando lo que se lleva la masa de lo que tira al cambiar, '
                'cuánto vale cada día de cuba, qué le hace una subida de '
                'precio y qué papeles le pide el aceite usado.',
    'epigrafes': list(PPE_10),
    'puntos_por_epigrafe': PPE_10,
    'puntos_globales': [
        'Capítulo legal y de dinero: la norma con su artículo y «comprobado el '
        '3 de octubre de 2026», y el coste con las cifras del libro del '
        'aceite.',
        'Frontera: el capítulo 7 eligió el aceite y el gestor; éste calcula lo '
        'que cuestan y cuándo se cambia; el capítulo 11 trata el aceite '
        'compartido como '
        'contaminación cruzada.',
    ],
    'cifras': [
        C('Límite legal de compuestos polares del aceite de fritura', f'{X_ACEITE}!Parámetros!B25', 'pct0', clave='Límite legal de compuestos polares'),
        C('Renovación del aceite por ración: lo que se tira al cambiar la cuba', f'{X_ACEITE}!Consumo y Reposición!L5', 'eur2', clave='Renovación de aceite por ración (origen de X12)'),
        C('Aceite total por ración: el absorbido por la masa más la renovación', f'{X_ACEITE}!Consumo y Reposición!B33', 'eur2', clave='Aceite total por ración (absorbido del libro 3 más renovación)'),
        C('Parte del aceite total por ración que es renovación', f'{X_ACEITE}!Consumo y Reposición!B34', 'pct0', clave='Parte del aceite total por ración que es renovación'),
        C('Días entre cambios de aceite de El Molinete (supuesto declarado)', f'{X_ACEITE}!Parámetros!B21', 'num', clave='Días entre cambios de aceite'),
        C('Veredicto del libro del aceite sobre el ciclo de cambio de El Molinete', f'{X_ACEITE}!Punto Económico de Cambio!F22', 'txt', clave='Veredicto del punto económico de cambio'),
        C('Lo que cuesta al mes cambiar el aceite un día antes', f'{X_ACEITE}!Punto Económico de Cambio!F19', 'eur2', clave='Coste de cambiar un día antes al mes'),
        C('Lo que se ahorra al mes alargando un día, si el medidor lo permite', f'{X_ACEITE}!Punto Económico de Cambio!F20', 'eur2', clave='Ahorro de alargar un día al mes'),
        C('Margen que se pierde al año con la primera subida del aceite del libro', f'{X_ACEITE}!Escenarios de Precio del Aceite!J8', 'eur2', clave='Margen que pierdes al año con el aceite un 10 % más caro'),
        C('Litros de aceite usado que El Molinete entrega al gestor cada mes', f'{X_ACEITE}!Gestor de Aceite Usado!B7', 'num1', clave='Litros al gestor al mes'),
    ],
    'sector': ['CUN-01', 'CUN-02', 'CUN-03', 'CUN-27', 'CUS-23', 'CUS-38',
               'CUS-44h'],
    'tablas': [
        {
            'titulo': 'Cuánto vale cada día de cuba: el punto económico de cambio de El Molinete (aceite-de-fritura-coste-y-cambio.xlsx, hoja «Punto Económico de Cambio»)',
            'src': (X_ACEITE, 'Punto Económico de Cambio'),
            'cols': [('Días entre cambios', 'A', 'num'),
                     ('Renovación por ración', 'D', 'eur2'),
                     ('Aceite total por ración', 'E', 'eur2'),
                     ('Renovación al mes', 'F', 'eur'),
                     ('Litros al gestor al mes', 'G', 'num1'),
                     ('Diferencia al mes frente a tu ciclo', 'H', 'eur'),
                     ('¿Es tu ciclo?', 'I', 'txt')],
            'filas': (7, 14),
            'ancla': ('A6', 'Días entre cambios'),
            'nota': 'El día del cambio lo decide la lectura del medidor de mano, anotada en '
                    'tu registro; el límite legal se prueba en laboratorio. ' + V_ACEITE,
        },
        {
            'titulo': 'Si sube el aceite: lo que pierdes al mes y al año (aceite-de-fritura-coste-y-cambio.xlsx, hoja «Escenarios de Precio del Aceite»)',
            'src': (X_ACEITE, 'Escenarios de Precio del Aceite'),
            # La subida (un porcentaje) va la ÚLTIMA a propósito: en la
            # segunda columna, `es_fila_porcentual()` daría la fila por
            # porcentual e imprimiría los euros como tantos por ciento.
            'cols': [('Escenario', 'A', 'txt'),
                     ('Precio del aceite por litro, sin IVA', 'C', 'eur2'),
                     ('Aceite total por ración', 'F', 'eur2'),
                     ('Aceite que compras al mes', 'G', 'eur'),
                     ('Margen que pierdes al mes', 'I', 'eur'),
                     ('Margen que pierdes al año', 'J', 'eur'),
                     ('Subida sobre el precio de hoy', 'B', 'pct0')],
            'filas': (7, 10),
            'ancla': ('A7', 'Hoy'),
            'nota': 'Sólo se mueve el aceite: el resto del escandallo se queda donde estaba. '
                    'Para no perder margen, el precio de venta sin IVA tendría que subir lo '
                    'mismo que sube el aceite por ración.',
        },
        {
            'titulo': 'Lo que es del libro del aceite y lo que es del registro del Pack APPCC',
            'cabecera': ['Qué', 'Dónde vive', 'Por qué ahí'],
            'filas': [
                ['Las lecturas del medidor y los cambios de cuba', 'Pack Plantillas APPCC, 09-control-aceite-fritura.xlsx, hoja «Control Aceite»', 'Es tu registro de autocontrol: lo que enseñas en una inspección'],
                ['Las retiradas del gestor', 'Pack Plantillas APPCC, 09-control-aceite-fritura.xlsx, hoja «Retirada de aceite usado»', 'Es el justificante de la recogida separada'],
                ['El coste del aceite por ración, el punto económico de cambio, las subidas de precio y los litros al gestor', 'aceite-de-fritura-coste-y-cambio.xlsx', 'Son decisiones de dinero, no registros'],
                ['El aceite que se lleva la masa', 'carta-de-apertura-y-escandallo-churro.xlsx', 'Ya está dentro del coste de materia de cada ración'],
            ],
            'nota': 'Este pack no duplica el registro: lo cita. Si tienes el Pack Plantillas '
                    'APPCC, tus días entre cambios y tus litros retirados salen de ahí.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDA cualquier temperatura de fritura del churro y cualquier '
        'temperatura del aceite como regla de cambio.',
        'PROHIBIDO decir cuánto dura un aceite o comparar aceites o marcas: el '
        'ciclo es un supuesto de El Molinete y el dato bueno es el de tu '
        'registro.',
        'PROHIBIDO reproducir el registro del aceite del Pack APPCC: se cita '
        'por su fichero y su hoja.',
        'No expliques aquí los alérgenos del aceite compartido ni la '
        'acrilamida: son del capítulo 11.',
    ],
}

# ============================== CAPÍTULO 11 ===============================
# FUNDIDO (D26): 11 Acrilamida, alérgenos y aceite compartido + 12
# Autocontrol, formación e inspección de la SPEC. Mitad 1 = los peligros del
# producto (epígrafes 1-3); mitad 2 = cómo se organiza y se demuestra el
# control (epígrafes 4-6).
PPE_11 = {
    'Acrilamida: buena práctica en el churro, obligación si fríes patatas': [
        'Dar lo que dice la norma, con su artículo y sin estirarla: el '
        'reglamento europeo de la acrilamida tiene una lista cerrada de '
        'alimentos en su art. 1.2 y el churro no aparece; el reglamento no '
        'define «bollería», así que no se puede afirmar ni que el churro entre '
        'ni que quede fuera. Controlarla en el churro es BUENA PRÁCTICA '
        '(Reglamento (UE) 2017/2158).',
        'Lo que sí obliga y a quién: si fríes patatas frescas —el epígrafe '
        '644.6 te faculta para hacerlo—, te toca la parte A de su anexo II, '
        'con sus medidas para las patatas; y la parte B sólo alcanza a quien '
        'opera bajo marca o licencia, como parte de un funcionamiento '
        'interconectado y siguiendo las instrucciones de quien le suministra '
        'de forma centralizada (art. 2.3). Nunca «a las franquicias» sin más.',
        'Lo que hay alrededor, con su nivel: una recomendación de la '
        'Comisión, no vinculante, incluye los churros entre los alimentos en '
        'los que conviene vigilarla; un estudio de las autoridades sanitarias '
        'recoge que no hay valor de referencia para las masas fritas; y la '
        'Comisión revisa el marco con niveles máximos por primera vez, en fase '
        'de consulta. Es un riesgo de caducidad: el anexo da la fecha de '
        'revisión.',
    ],
    'Alérgenos de una churrería: gluten siempre, leche en la taza y lo que diga cada etiqueta': [
        'Dar la regla con su norma: los catorce alérgenos son obligatorios, y '
        'en un establecimiento se pueden dar de palabra sólo si están por '
        'escrito, a disposición del personal, de la inspección y del cliente, '
        'con un cartel visible (RD 126/2015). En una churrería, el gluten está '
        'siempre en la masa de trigo y la leche, en la taza; lo demás depende '
        'de la etiqueta de cada producto que compras.',
        'Dar el estado de la tabla de alérgenos de El Molinete en el libro '
        'legal: qué declara por escrito y cuántas casillas siguen pendientes '
        'de leer en la etiqueta. Mientras no sean cero, la carta de alérgenos '
        'está incompleta; el mismo preparado para masa cambia de composición '
        'entre marcas.',
        'El «sin gluten»: es un umbral analítico del producto tal como se '
        'vende, no una declaración libre, y en una churrería con harina de '
        'trigo casi nunca se puede decir. No es un argumento de carta.',
    ],
    'El aceite compartido es contaminación cruzada': [
        'Dar la regla con su norma: el equipo que ha tocado un alérgeno no se '
        'usa para otros alimentos sin limpiarlo (Reglamento (CE) 852/2004, '
        'anexo II, capítulo IX). En fritura, el aceite es parte del equipo: lo '
        'que fríes en la misma cuba pasa al resto.',
        'Dar la decisión de El Molinete y su consecuencia: freidora dedicada '
        'al churro y a la porra, así que su aceite sólo lleva lo que lleva su '
        'masa. Si un día fríes patatas, rebozados o buñuelos de otra masa en '
        'la misma freidora, cambian tus alérgenos y, con las patatas, te entra '
        'la parte A de la acrilamida. FRONTERA con la segunda mitad del '
        'capítulo: aquí terminan los peligros del producto; desde aquí, cómo '
        'se organiza y se demuestra el control.',
    ],
    'El autocontrol simplificado, con un responsable con nombre': [
        'Dar la regla con su norma: el procedimiento de autocontrol basado en '
        'el análisis de peligros y puntos de control crítico puede ser '
        'simplificado, pero tiene que tener una persona responsable con '
        'nombre (RD 1021/2022, art. 20). Servir chocolate y churros en sala es '
        'elaborar comidas preparadas, con su zona de elaboración separada de '
        'la venta (RD 1086/2020).',
        'Decir dónde están los registros y por qué la guía no los copia: el '
        'registro del aceite, las limpiezas, las temperaturas de conservación '
        'y el resto están en el Pack Plantillas APPCC; el libro legal de este '
        'pack sólo trae las filas del checklist que te recuerdan llevarlos.',
    ],
    'Formación: lo que se acredita es el registro, no un carnet': [
        'Dar la regla con su norma: la obligación es del empresario, que tiene '
        'que garantizar la formación de cada persona según su puesto y poder '
        'demostrarla; ningún carné la sustituye. Lo que pide una inspección es '
        'el registro de formación, con el contenido y la fecha.',
        'Dar el registro de El Molinete: cuántas personas tienen la formación '
        'registrada, la validez que fija la casa (la norma no fija caducidad: '
        'es una decisión tuya) y el veredicto del libro.',
    ],
    'El día de la inspección: qué tener a mano': [
        'Dar la lista de lo que se enseña, en el orden en que se pide: la '
        'comunicación al registro sanitario de tu comunidad, el plan de '
        'autocontrol con su responsable, el registro del aceite con las '
        'lecturas y los justificantes de retirada del gestor, la carta de '
        'alérgenos por escrito y su cartel, y el registro de formación.',
        'Y lo que mira una inspección de consumo, que también llega: los '
        'precios a la vista, el vaso cobrado aparte en el tique y la '
        'denominación del chocolate según la etiqueta del preparado (capítulo '
        '3). La fecha de corte de todo esto está en el anexo.',
    ],
}

CAP_11 = {
    'n': 11,
    'titulo': 'Autocontrol, Alérgenos, Acrilamida y el Día de la Inspección',
    'resumen_indice': 'la acrilamida como buena práctica en el churro, los alérgenos de una churrería, el aceite compartido, el autocontrol simplificado con responsable, la formación que se acredita y el día de la inspección.',
    'palabras': 2500, 'bloques': 1,
    'objetivo': 'Que el lector sepa qué le obliga y qué no en acrilamida y '
                'alérgenos, por qué el aceite compartido es un problema de '
                'alérgenos, cómo organiza un autocontrol simplificado con su '
                'responsable y su registro de formación, y qué tiene que tener '
                'a mano el día que llega la inspección.',
    'epigrafes': list(PPE_11),
    'puntos_por_epigrafe': PPE_11,
    'puntos_globales': [
        'Capítulo FUNDIDO en dos mitades con frontera explícita: primero los '
        'peligros del producto (acrilamida, alérgenos y aceite compartido), '
        'luego cómo se organiza y se demuestra el control (autocontrol, '
        'formación e inspección). No repitas en la segunda lo que dijo la '
        'primera.',
        'Capítulo legal: cada regla con su norma y su artículo, y «comprobado '
        'el 3 de octubre de 2026» (las normas que ya verificó la guía de '
        'chocolatería, el 12 de septiembre de 2026).',
        'Frontera con los vecinos: el aceite como norma de calidad y como '
        'coste es del capítulo 10; el registro sanitario, del capítulo 9.',
    ],
    'cifras': [
        C('¿Freidora dedicada o compartida en El Molinete?', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B11', 'txt', clave='¿Freidora dedicada o compartida?'),
        C('Casillas de alérgenos de El Molinete pendientes de leer en la etiqueta', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B21', 'num', clave='Casillas de alérgenos pendientes de la etiqueta'),
        C('¿Declara El Molinete el gluten por escrito?', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B20', 'txt', clave='¿Declaras el gluten por escrito?'),
        C('Umbral del «sin gluten», en miligramos por kilo', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B25', 'num', clave='Umbral del «sin gluten» (mg/kg)'),
        C('Acrilamida, parte A del anexo II, en El Molinete', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B35', 'txt', clave='Acrilamida: parte A'),
        C('Acrilamida, parte B del anexo II, en El Molinete', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B36', 'txt', clave='Acrilamida: parte B'),
        C('Personas de El Molinete con la formación registrada', f'{X_LEGAL}!Registro de Formación!C22', 'num', clave='Personas con formación registrada'),
        C('Validez de la formación que fija la casa, en meses (supuesto: la norma no fija caducidad)', f'{X_LEGAL}!Registro de Formación!C17', 'num', clave='Validez de la formación en meses'),
        C('Veredicto del registro de formación de El Molinete', f'{X_LEGAL}!Registro de Formación!C25', 'txt', clave='Veredicto del registro de formación'),
    ],
    # Fuera a propósito: CUN-05 (su cifra es la temperatura de las patatas
    # del anexo II, y el prompt la pediría «fuente obligatoria»; V-02). Su
    # regla —parte A y parte B, art. 2.3— va en los puntos con su norma.
    'sector': ['CUN-04', 'CUN-06', 'CUN-07', 'CUN-08', 'CUN-09', 'CHN-32',
               'CHN-33', 'CHN-34', 'CHN-37', 'CHN-51', 'CHN-69'],
    'tablas': [
        {
            'titulo': 'Los alérgenos de la carta de El Molinete, por familia (checklist-legal-fritura-y-licencias.xlsx, hoja «Alérgenos y Aceite Compartido»)',
            'src': (X_LEGAL, 'Alérgenos y Aceite Compartido'),
            'cols': [('Familia de la carta', 'A', 'txt'), ('Gluten', 'B', 'txt'),
                     ('Leche', 'C', 'txt'), ('Huevo', 'D', 'txt'),
                     ('Soja', 'E', 'txt'), ('Frutos de cáscara', 'F', 'txt')],
            'filas': (15, 20),
            'ancla': ('A15', 'Churros y porras'),
            'nota': 'Cada casilla «revisa la etiqueta» se rellena con la etiqueta del '
                    'producto que compras: el mismo preparado para masa cambia de composición '
                    'entre marcas. Los catorce alérgenos son obligatorios y van por escrito '
                    '(RD 126/2015, verificado el 12-09-2026 en la guía hermana).',
        },
        {
            'titulo': 'La acrilamida en El Molinete: lo que es obligación y lo que es buena práctica (checklist-legal-fritura-y-licencias.xlsx, hoja «Alérgenos y Aceite Compartido»)',
            'src': (X_LEGAL, 'Alérgenos y Aceite Compartido'),
            'cols': [('Qué', 'A', 'txt'), ('Lo que te toca', 'B', 'txt')],
            'filas': (31, 36),
            'ancla': ('A31', 'El churro'),
            'nota': V_ACRIL,
        },
        {
            'titulo': 'El registro de formación de El Molinete (checklist-legal-fritura-y-licencias.xlsx, hoja «Registro de Formación»)',
            'src': (X_LEGAL, 'Registro de Formación'),
            'cols': [('Puesto', 'C', 'txt'), ('Jornada', 'D', 'num1'),
                     ('Contenido de la formación', 'E', 'txt'),
                     ('Estado', 'H', 'txt')],
            'filas': (7, 11),
            'ancla': ('C7', 'Titular'),
            'nota': 'Lo que vale ante una inspección es este registro, con el contenido y la '
                    'fecha de cada formación. La validez la fijas tú: la norma no pone '
                    'caducidad.',
        },
    ],
    'prohibido': NO_COMUN + [
        'No escribas la temperatura de fritura de las patatas del reglamento '
        'de la acrilamida: basta con decir que la parte A trae sus medidas '
        'para las patatas, y que para el churro no hay ninguna temperatura.',
        'PROHIBIDO presentar como obligatorio el control de la acrilamida en '
        'el churro, con cualquier fórmula: es buena práctica.',
        'PROHIBIDO dar como dato la matriz completa de alérgenos de una receta '
        'concreta: depende de la etiqueta de cada proveedor.',
        'PROHIBIDO reproducir los registros del Pack APPCC: se citan.',
    ],
}

# ============================== CAPÍTULO 12 ===============================
PPE_12 = {
    'Del kilo de masa a la pieza: el escandallo empieza en la masa': [
        'Explicar por qué en una churrería se escandalla el kilo de masa y no '
        'la ración: la masa es la misma para el churro, la porra y la docena, '
        'y lo que cambia es cuántas piezas salen y cuánta masa se fríe para '
        'venderlas. El libro de la carta parte del preparado comercial, con lo '
        'que declara el vendedor que rinde cada saco, y da el coste de un kilo '
        'de masa.',
        'Dar los supuestos con los que El Molinete pasa del kilo a la pieza, '
        'como supuestos y con el método para cambiarlos: los gramos de masa de '
        'un churro y de una porra (pesa diez piezas y divide), la merma que se '
        'fríe y no se vende, y los kilos fritos que salen de un kilo de masa. '
        'Y el resultado, formato a formato en la tabla: la masa que se fríe, '
        'el aceite que se lleva y la materia en sala y para llevar.',
        'Frontera: estas cantidades son datos de ejemplo para que el modelo '
        'calcule, no una receta. El Kit de Escandallos Pro y la Guía Food Cost '
        '+ Ingeniería de Menú enseñan el método general, pero no costean masa '
        'frita por kilo, que es lo que hace este libro.',
    ],
    'La absorción de aceite, en euros por kilo de masa': [
        'Explicar el cálculo sin cifras inventadas: la absorción es un '
        'supuesto declarado, en porcentaje del peso frito, y la densidad del '
        'aceite es otro; con los dos y el precio del aceite, el libro da los '
        'euros de aceite que se lleva cada kilo de masa y los mete en el coste '
        'de materia.',
        'Dar lo que pesa ese aceite en la materia de la ración media y el '
        'método para medir el tuyo: pesa una tanda de masa antes y después de '
        'freír. Cambiar de aceite o de freidora la mueve, y por eso no hay «la '
        'absorción del churro».',
    ],
    'Ración, docena o kilo: lo que deja cada formato por kilo de masa': [
        'Comparar los formatos por los euros sin IVA que deja cada kilo de '
        'masa: dar el formato que más deja y lo que deja, y lo que deja el que '
        'menos. La hoja explica por qué el kilo para llevar deja poco por kilo '
        'de masa: se vende por peso frito al precio más bajo por pieza. No es '
        'un error tenerlo: es el formato del pedido grande del domingo.',
        'Decir lo que la hoja deja decidir: cuánto cuesta cada formato en '
        'masa, en aceite y en freidora, para que el precio de cada uno sea una '
        'decisión y no una costumbre. Cuál le conviene a El Molinete es la '
        'decisión 7 del bonus.',
    ],
    'Los dos márgenes, cada uno con su definición': [
        'Dar los dos márgenes de El Molinete en invierno, con su definición en '
        'la misma frase: el margen sobre materia prima (el ticket sin IVA '
        'menos la materia y el aceite absorbido) y el margen tras aceite y '
        'mano de obra (además, la mano de obra de cada ración). Ninguno es la '
        'rentabilidad del negocio, que sale del plan financiero.',
        'Ponerlos al lado de las dos cifras que circulan, cada una con su '
        'definición y su fuente: los «márgenes superiores al sesenta por '
        'ciento en producto» de un proveedor de TPV son margen sobre materia, '
        'sin método publicado; y el «un poquito más del cincuenta por ciento» '
        'lo dice de palabra el gestor de La Artesana y es rentabilidad, no '
        'margen sobre materia, con fiabilidad baja. El margen sobre materia '
        'alto de El Molinete es normal en una churrería: la masa es barata.',
        'La regla del plan financiero, sin excepciones: toma el margen sobre '
        'materia de TU escandallo y resta la nómina aparte. Usar el «poquito '
        'más del cincuenta» como margen bruto contaría la mano de obra dos '
        'veces.',
    ],
    'La mano de obra por ración: por qué el margen alto no paga la madrugada': [
        'Dar el coste de mano de obra de cada ración de El Molinete, que sale '
        'del coste hora de su plantilla y de los minutos que lleva cada '
        'ración. Lo caro de una churrería no es la masa: es la madrugada.',
        'Explicar el cuadre: este libro va antes que el de turnos y supone el '
        'coste hora; cuando rellenes el de turnos, su fila de cuadre compara '
        'los dos y te avisa si se separan (capítulo 13).',
    ],
}

CAP_12 = {
    'n': 12,
    'titulo': 'Escandallo del Churro y de la Porra: Rendimiento, Absorción y los Dos Márgenes',
    'resumen_indice': 'del kilo de masa a la pieza, la absorción de aceite en euros, ración, docena o kilo, los dos márgenes con su definición y la mano de obra por ración.',
    'palabras': 1600, 'bloques': 1,
    'objetivo': 'Que el lector sepa cuánto le cuesta de verdad un churro, una '
                'porra y una ración, partiendo del kilo de masa y del aceite '
                'que se lleva; qué formato le deja más por kilo de masa; y qué '
                'miden los dos márgenes, para no comparar su escandallo con '
                'una cifra que mide otra cosa.',
    'epigrafes': list(PPE_12),
    'puntos_por_epigrafe': PPE_12,
    'puntos_globales': [
        'Todo en base imponible, en los dos lados del cociente: el ingreso sin '
        'IVA y la materia sin IVA.',
        'Cada margen se nombra con su definición en la misma frase, siempre.',
    ],
    'cifras': [
        C('Coste de un kilo de masa con el preparado comercial, sin IVA', f'{X_CARTA}!Escandallo por kg de Masa!E9', 'eur2', clave='Coste de 1 kg de masa con el preparado'),
        C('Euros de aceite absorbido por cada kilo de masa', f'{X_CARTA}!Absorción de Aceite y Merma!B11', 'eur2', clave='Euros de aceite absorbido por kilo de masa'),
        C('Peso del aceite absorbido en la materia de la ración media', f'{X_CARTA}!Absorción de Aceite y Merma!B22', 'pct1', clave='Peso del aceite absorbido en la materia de la ración'),
        C('Formato de la carta que más euros deja por kilo de masa', f'{X_CARTA}!Ración, Docena o Kilo!B16', 'txt', clave='Formato que más deja por kilo de masa'),
        C('Euros sin IVA que deja cada kilo de masa en el formato que más deja', f'{X_CARTA}!Ración, Docena o Kilo!B17', 'eur2', clave='Euros por kilo de masa del mejor formato'),
        C('Euros sin IVA que deja cada kilo de masa en el formato que menos deja', f'{X_CARTA}!Ración, Docena o Kilo!B19', 'eur2', clave='Euros por kilo de masa del peor formato'),
        C('Margen sobre materia prima de El Molinete en invierno', f'{X_CARTA}!Los Dos Márgenes!B6', 'pct1', clave='Margen sobre materia prima (invierno)'),
        C('Margen tras aceite y mano de obra de El Molinete en invierno', f'{X_CARTA}!Los Dos Márgenes!B7', 'pct1', clave='Margen tras aceite y mano de obra (invierno)'),
        C('«Un poquito más del…»: rentabilidad que declara de palabra el gestor de La Artesana (El Español, 2025), fiabilidad baja, sólo como contraste y nunca como margen', f'{X_CARTA}!Los Dos Márgenes!B14', 'pct0', clave='Cifra de contraste de La Artesana (CUS-30)'),
        C('Coste de mano de obra por ración de El Molinete', f'{X_CARTA}!Coste Hora!B8', 'eur2', clave='Coste de mano de obra por ración'),
    ],
    'sector': ['CUS-01', 'CUS-21', 'CUS-23', 'CUS-24', 'CUS-25'],
    'tablas': [
        {
            'titulo': 'De la masa a cada formato de churro y porra: la materia en sala y para llevar (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Escandallo por kg de Masa»)',
            'src': (X_CARTA, 'Escandallo por kg de Masa'),
            'cols': [('Referencia', 'A', 'txt'),
                     ('Piezas de la unidad', 'C', 'num'),
                     ('Masa que se fríe con merma, en kilos', 'G', 'num2'),
                     ('Coste de la masa', 'H', 'eur2'),
                     ('Aceite absorbido', 'L', 'eur2'),
                     ('Materia en sala, aceite incluido', 'M', 'eur2'),
                     ('Materia para llevar, con envase', 'N', 'eur2')],
            'filas': (35, 41),
            'ancla': ('A35', 'CH1'),
            'nota': 'Datos de ejemplo para que las fórmulas calculen: los gramos por pieza, '
                    'la merma y la absorción son supuestos de El Molinete. Todo sin IVA.',
        },
        {
            'titulo': 'Ración, docena o kilo: lo que deja cada formato por kilo de masa (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Ración, Docena o Kilo»)',
            'src': (X_CARTA, 'Ración, Docena o Kilo'),
            'cols': [('Formato', 'A', 'txt'), ('Piezas', 'B', 'num'),
                     ('PVP con IVA', 'C', 'eur2'),
                     ('Ingreso sin IVA', 'F', 'eur2'),
                     ('Materia, aceite incluido', 'G', 'eur2'),
                     ('Margen por unidad', 'H', 'eur2'),
                     ('Euros que deja cada kilo de masa', 'J', 'eur2'),
                     ('Año y fuente del precio', 'K', 'txt')],
            'filas': (7, 13),
            'ancla': ('A7', 'CH1'),
            'nota': 'El kilo es el formato con menos euros por kilo de masa porque se vende '
                    'por peso frito al precio más bajo por pieza: no es un error tenerlo, es '
                    'el pedido grande del domingo.',
        },
        {
            'titulo': 'Los dos márgenes de El Molinete, cada uno con su definición (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Los Dos Márgenes»)',
            'src': (X_CARTA, 'Los Dos Márgenes'),
            'cols': [('Margen', 'A', 'txt'), ('Invierno', 'B', 'pct1'),
                     ('Julio y agosto', 'C', 'pct1'),
                     ('Definición', 'D', 'txt')],
            'filas': (6, 7),
            'ancla': ('A6', '1. Margen sobre materia prima'),
            'nota': 'Las dos cifras con las que se suelen comparar están en la misma hoja, '
                    'cada una con su definición: «márgenes superiores al 60 % en producto» '
                    '(Loomis Pay) es margen sobre materia; «un poquito más del 50 %» (el '
                    'gestor de La Artesana, de palabra) es rentabilidad declarada. Ninguna de '
                    'las dos entra en el plan financiero.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO usar el margen sobre materia de El Molinete para dar por '
        'bueno el margen de ochenta y cinco a noventa por ciento que circula '
        'sin fuente: son cosas distintas y aquella cifra no está en su fuente.',
        'El margen sobre materia de El Molinete es una cifra CALCULADA y '
        'legítima: se cita con su valor exacto, tal como llega en las cifras, '
        'y con su definición en la misma frase; nunca redondeado ni como '
        'horquilla.',
        'PROHIBIDO presentar el margen tras aceite y mano de obra como '
        'rentabilidad del negocio: no incluye renta, suministros ni '
        'amortización.',
        'PROHIBIDO dar los gramos por pieza, la absorción o la merma como '
        'datos del sector, o como receta.',
        'No expliques aquí la carta ni el IVA (capítulo 3) ni el aceite que se '
        'tira al cambiar la cuba (capítulo 10).',
    ],
}

# ============================== CAPÍTULO 13 ===============================
PPE_13 = {
    'Cuántas personas hacen falta: la línea, la sala y el pico del fin de semana': [
        'Explicar de dónde sale la plantilla: no de una ratio, sino del '
        'cuadrante por franjas del libro de turnos, que pone un mínimo de '
        'personas en cada media hora de apertura y comprueba que ninguna queda '
        'sin cubrir. Las personas en la línea en el pico del fin de semana '
        'llegan del libro de producción y las horas de refuerzo de Navidad y '
        'Reyes, del libro de temporada.',
        'Dar la plantilla de El Molinete —el titular, dos churreros, un '
        'camarero de sala y un refuerzo de fin de semana a media jornada— con '
        'su coste anual de plantilla y el coste hora que sale de ella, que es '
        'el que tiene que usar el escandallo del capítulo 12. FRONTERA: el '
        'cuadrante semanal por empleado, las vacaciones y la rotación son del '
        'Kit Gestión de Personal y Turnos; aquí la plantilla se dimensiona y '
        'se cuesta para el plan financiero.',
    ],
    'Dos figuras que no se mezclan: el trabajador nocturno y el plus de nocturnidad': [
        'Dar la regla con su norma: trabajo nocturno es el que se hace entre '
        'las 22:00 y las 6:00, y trabajador nocturno es quien hace normalmente '
        'en ese periodo al menos tres horas de su jornada diaria, o se prevé '
        'que haga en él un tercio de su jornada anual (Estatuto de los '
        'Trabajadores, art. 36.1). Es una figura con límites y protección '
        'propios.',
        'El plus de nocturnidad es OTRA cosa: lo fija cada convenio, con sus '
        'franjas y su recargo sobre el salario base. En el convenio de Madrid, '
        'de ejemplo, una franja va de las 22:00 a las 0:00 con un recargo '
        'pequeño y otra de las 0:00 a las 8:00 con uno mayor (CUN-40). Se puede '
        'cobrar plus sin ser trabajador nocturno, y en una churrería es lo '
        'normal.',
        'El caso de El Molinete, con la hoja de nocturnidad: el turno que '
        'empieza a las 4:30 del fin de semana tiene hora y media en el periodo '
        'del Estatuto, así que no hace de ese churrero un trabajador nocturno, '
        'pero sí cobra plus por la madrugada; y quien cierra el viernes y el '
        'sábado a la 1:00 suma tres horas sólo dos días a la semana, así que el '
        'libro le pone «revísalo con tu asesor».',
    ],
    'Tu convenio: el de Madrid como ejemplo vencido y el método para encontrar el tuyo': [
        'Decir cómo se encuentra el convenio que te toca: el de hostelería de '
        'tu provincia o de tu comunidad, buscado en REGCON por denominación y '
        'ámbito; después, la clase o el grupo en que entra tu local y el nivel '
        'de cada puesto por sus funciones, que es una asimilación que se '
        'comprueba con el asesor. El acuerdo laboral estatal de hostelería '
        'nombra freidurías, quioscos y chocolaterías, la palabra «churrería» '
        'no aparece en él, y sigue vigente hasta el 31 de diciembre de 2030.',
        'El ejemplo de Madrid, con su estado real: el convenio de hostelería de '
        'la Comunidad de Madrid venció el 31 de diciembre de 2025, la comisión '
        'negociadora del nuevo se constituyó en diciembre de 2025 y, sin texto '
        'nuevo publicado a 3 de octubre de 2026, se siguen aplicando sus '
        'tablas de 2025. Toda cifra que sale de esas tablas lleva esa etiqueta '
        'en el libro de turnos.',
        'Y el método con otro convenio: el provincial de Toledo nombra los '
        'obradores de masas fritas, así que alcanza a un obrador de churros; '
        'que alcance a un despacho con sala es una interpretación que confirma '
        'un laboralista.',
    ],
    'El salario mínimo es el suelo, y las ofertas publicadas sólo un contraste': [
        'Dar la regla: el salario mínimo interprofesional de 2026 es el suelo '
        'de cada puesto a su jornada, con su cuantía anual de referencia. El '
        'libro compara el salario de convenio de cada puesto con ese suelo y '
        'se queda con el mayor de los dos; encima va la Seguridad Social de '
        'empresa de quien cotiza.',
        'Las ofertas publicadas son contraste, no obligación: un aprendiz de '
        'churrero y un ayudante de cocina de una churrería de Madrid, con su '
        'rango mensual y sin pagas declaradas (CUS-54, CUS-55). Leídas a doce '
        'pagas, la primera queda por debajo del salario mínimo anual: por eso '
        'cuenta el suelo y no el anuncio. Lo que obliga es tu convenio y, por '
        'debajo de todo, el salario mínimo.',
    ],
    'Las horas del titular y el registro de jornada': [
        'Las horas del titular de El Molinete: trabaja los siete días, con '
        'horas de más cada semana y la madrugada del fin de semana. El libro '
        'les pone valor al coste hora de la plantilla, que es lo que costaría '
        'pagárselas a otra persona y que no está en el coste de plantilla. Su '
        'retribución va en nómina como un puesto más, porque un plan que sólo '
        'cuadra si el titular trabaja gratis no sirve. Cuánta madrugada asume '
        'él es la decisión 10 del bonus.',
        'El registro de jornada: diario, con la hora de inicio y de fin de '
        'cada persona, y conservado cuatro años; la norma no impone formato ni '
        'sistema digital (Estatuto de los Trabajadores, art. 34.9). El registro '
        'horario digital está pendiente de desarrollo, y el anexo lo vigila.',
    ],
}

CAP_13 = {
    'n': 13,
    'titulo': 'El Equipo, los Turnos y la Madrugada',
    'resumen_indice': 'cuántas personas hacen falta, el trabajador nocturno y el plus de nocturnidad como dos figuras distintas, el convenio de Madrid como ejemplo vencido, el salario mínimo como suelo y las horas del titular.',
    'palabras': 1700, 'bloques': 1,
    'objetivo': 'Que el lector sepa dimensionar y costear su plantilla, '
                'distinga el trabajador nocturno del Estatuto del plus de '
                'nocturnidad de su convenio, encuentre su convenio con el '
                'método y no con un nombre que no existe, y no cuadre el plan '
                'con las horas gratis del titular.',
    'epigrafes': list(PPE_13),
    'puntos_por_epigrafe': PPE_13,
    'puntos_globales': [
        'Capítulo legal: cada regla con su norma y su artículo, y «comprobado '
        'el 3 de octubre de 2026». El artículo 36 del Estatuto y el plus del '
        'convenio van SIEMPRE separados, cada uno con su fuente.',
        'Frontera: el cuadrante semanal por empleado, las vacaciones y la '
        'rotación son del Kit Gestión de Personal y Turnos; este capítulo '
        'dimensiona y cuesta la plantilla para el plan financiero.',
    ],
    'cifras': [
        C('Coste anual de plantilla de El Molinete, con Seguridad Social, refuerzo y sustituciones', f'{X_TURNOS}!Coste de Plantilla!L5', 'eur', clave='Coste anual de plantilla (origen de X15)'),
        C('Coste hora de la plantilla, el que usa el escandallo', f'{X_TURNOS}!Coste de Plantilla!B19', 'eur2', clave='Coste hora de la plantilla'),
        C('¿Es trabajador nocturno del Estatuto el churrero del turno de las 4:30 del fin de semana?', f'{X_TURNOS}!Nocturnidad ET y Convenio!G10', 'txt', clave='¿Trabajador nocturno según el ET?: Churrero/a 2'),
        C('Horas a la semana de ese churrero en el periodo nocturno del Estatuto, de 22:00 a 6:00', f'{X_TURNOS}!Nocturnidad ET y Convenio!C10', 'num1', clave='Horas de 22:00 a 6:00 a la semana: Churrero/a 2'),
        C('¿Es trabajador nocturno del Estatuto quien cierra el viernes y el sábado?', f'{X_TURNOS}!Nocturnidad ET y Convenio!G11', 'txt', clave='¿Trabajador nocturno según el ET?: Camarero/a de sala'),
        C('Plus de nocturnidad del convenio de ejemplo que paga la plantilla al año', f'{X_TURNOS}!Coste de Plantilla!M14', 'eur', clave='Plus de nocturnidad de la plantilla al año'),
        C('Tablas salariales del convenio de ejemplo y su estado', f'{X_TURNOS}!Parámetros!B16', 'txt', clave='Tablas salariales del ejemplo'),
        C('Salario mínimo interprofesional anual de 2026, suelo de cada puesto a jornada completa', f'{X_TURNOS}!Parámetros!B20', 'eur', clave='SMI anual'),
        C('Horas a la semana del titular de El Molinete en el cuadrante', f'{X_TURNOS}!Horas del Titular!B6', 'num1', clave='Horas del titular a la semana'),
        C('Lo que valdrían al año las horas de más del titular, al coste hora de la plantilla', f'{X_TURNOS}!Horas del Titular!B14', 'eur', clave='Valor de las horas de más del titular al año'),
    ],
    'sector': ['CUN-29', 'CUN-31', 'CUN-32', 'CUN-39', 'CUN-40', 'CUN-V01',
               'CUN-V05', 'CHN-67', 'CHN-68', 'CHN-93', 'CUS-54', 'CUS-55'],
    'tablas': [
        {
            'titulo': 'Las dos figuras, persona a persona: el Estatuto y el plus del convenio (turnos-plantilla-y-madrugada.xlsx, hoja «Nocturnidad ET y Convenio»)',
            'src': (X_TURNOS, 'Nocturnidad ET y Convenio'),
            'cols': [('Puesto', 'B', 'txt'),
                     ('Horas de 22:00 a 6:00 a la semana', 'C', 'num1'),
                     ('Días con tres horas o más en ese periodo', 'E', 'num'),
                     ('Parte de su jornada en ese periodo', 'F', 'pct1'),
                     ('¿Trabajador nocturno? (Estatuto)', 'G', 'txt'),
                     ('Horas de 0:00 a 8:00 a la semana', 'I', 'num1'),
                     ('Plus del convenio al año', 'L', 'eur')],
            'filas': (8, 12),
            'ancla': ('B8', 'Titular'),
            'nota': 'Figura 1, el Estatuto: trabajador nocturno es quien hace normalmente tres '
                    'horas o más de su jornada diaria entre las 22:00 y las 6:00, o un tercio de '
                    'su jornada anual. Figura 2, el convenio: el plus por cada hora en sus '
                    'franjas, aunque no seas trabajador nocturno. El titular es autónomo y no '
                    'cobra plus. ' + V_ET,
        },
        {
            'titulo': 'El coste de cada puesto, con el salario mínimo como suelo (turnos-plantilla-y-madrugada.xlsx, hoja «Coste de Plantilla»)',
            'src': (X_TURNOS, 'Coste de Plantilla'),
            'cols': [('Puesto', 'B', 'txt'), ('Jornada (1 = completa)', 'C', 'num1'),
                     ('Nivel del convenio de ejemplo', 'D', 'txt'),
                     ('Salario anual', 'N', 'eur'),
                     ('Suelo: salario mínimo anual a su jornada', 'O', 'eur'),
                     ('Semáforo del salario mínimo', 'P', 'txt'),
                     ('Coste anual del puesto', 'Q', 'eur')],
            'filas': (9, 13),
            'ancla': ('B9', 'Titular'),
            'nota': 'Coste del puesto = el mayor entre su salario y el salario mínimo anual a su '
                    'jornada, más la Seguridad Social de empresa si cotiza. El nivel de cada '
                    'puesto es una asimilación de funciones que se comprueba con el asesor. '
                    + V_CONVENIO,
        },
        {
            'titulo': 'Cómo encontrar tu convenio, paso a paso, con Madrid como ejemplo (turnos-plantilla-y-madrugada.xlsx, hoja «Identifica tu Convenio»)',
            'src': (X_TURNOS, 'Identifica tu Convenio'),
            'cols': [('Paso', 'A', 'num'), ('Qué haces', 'B', 'txt'),
                     ('Cómo', 'C', 'txt'),
                     ('El ejemplo de El Molinete', 'D', 'txt')],
            'filas': (6, 14),
            'ancla': ('B6', 'Tu provincia'),
            'nota': 'Busca el tuyo en REGCON por denominación y ámbito: el de Madrid es sólo un '
                    'ejemplo del método, y sus tablas son las de 2025 de un convenio vencido y '
                    'en negociación.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO escribir como regla que el churrero de la madrugada es '
        'trabajador nocturno, o mezclar el trabajador nocturno del Estatuto '
        'con el plus del convenio: son dos figuras, cada una con su fuente.',
        'PROHIBIDO hablar de un convenio de churrerías, de una categoría de '
        'churrero o de que no existe convenio de churrerías: el convenio es el '
        'de hostelería de tu provincia, o el de un obrador si fabricas, y el '
        'nivel de cada puesto es una asimilación que confirma tu asesor.',
        'PROHIBIDO usar los sueldos de los anuncios como obligación o como '
        'dato del sector: son contraste.',
        'PROHIBIDO presentar las tablas de Madrid como vigentes sin su '
        'etiqueta: convenio vencido el 31 de diciembre de 2025, en '
        'negociación, con las tablas salariales de ese año.',
        'No reproduzcas el cuadrante semanal por empleado: es del Kit Gestión '
        'de Personal y Turnos.',
    ],
}

# ============================== CAPÍTULO 14 ===============================
# FUNDIDO (D26): 16 La temporada + 17 Ferias, casetas y venta ambulante de la
# SPEC. Mitad 1 = el año del local (epígrafes 1-3); mitad 2 = la caseta
# (epígrafes 4-6).
PPE_14 = {
    'El año de una churrería: de octubre a marzo, y diciembre por encima de todo': [
        'Explicar el método del libro de temporada: las raciones de un año '
        'normal salen de las de un día tipo y un día punta del libro de '
        'producción, y doce coeficientes las reparten por meses, con el uno '
        'como mes medio. Son supuestos declarados con la forma que describen '
        'las fuentes del sector: temporada alta en otoño, invierno y Navidad, '
        'y valle en verano. No hay una estadística de ventas de churrerías por '
        'meses: los coeficientes son el modelo, no un dato.',
        'Dar las cifras de El Molinete: las raciones del año y el peso de '
        'diciembre sobre ellas. Los coeficientes se cambian por los tuyos en '
        'cuanto tengas un año de ventas, y el libro los pasa al plan '
        'financiero.',
        'Un contraste con fecha de lo que mueve una fiesta grande: los puestos '
        'de churros autorizados en las Fallas de Valencia de 2026 (CUS-29).',
    ],
    'Navidad y Reyes: el refuerzo que pide la cola': [
        'La cola del domingo, mes a mes, ya está en el capítulo 6: aquí sólo '
        'su consecuencia. Donde hay cola, la respuesta no es una segunda '
        'churrera, sino masa preparada antes de abrir y una persona más en la '
        'línea (decisión 3 del bonus).',
        'El refuerzo de Navidad y Reyes, con su coste: días punta con una '
        'persona más por la mañana, sus horas al año y lo que cuestan al coste '
        'hora del escandallo. Esas horas viajan al libro de turnos y de ahí al '
        'coste de plantilla, así que no se cuentan dos veces.',
    ],
    'El verano tiene tres salidas, y se comparan en euros': [
        'Las tres salidas de julio y agosto, comparadas por lo que dejan: '
        'cerrar, que deja cero porque lo que pagas igual —renta, plantilla y '
        'gastos fijos— ya está en los fijos del año; abrir con carta de '
        'verano, con granizados, horchata, helado y algo de churro; o salir de '
        'ferias con el local cerrado. El libro da la contribución de cada una.',
        'Dar el caso: El Molinete elige la carta de verano, y el umbral que lo '
        'cambiaría son las raciones al día del local por debajo de las cuales '
        'la carta de verano deja menos que las ferias. Y dar el resultado de '
        'julio y agosto con los fijos dentro con esa salida: un verano en '
        'negativo es lo normal en una churrería, y lo pagan los meses buenos '
        '(capítulo 16).',
        'Dos formas reales de resolver el valle, como contraste: el local de '
        'heladería y churrería que vende helado en verano y churro en invierno '
        '(CUS-31e), y el que reparte el año entre una plaza de invierno y otra '
        'de verano (CUS-V17).',
    ],
    'Lo que es legal en una caseta: autorización, alta, registro, higiene y gas': [
        'FRONTERA del capítulo: hasta aquí, el año del local; desde aquí, la '
        'caseta. La autorización de venta ambulante la da el ayuntamiento, no '
        'puede ser indefinida, se adjudica por un procedimiento transparente y '
        'no se renueva sola (Ley 7/1996, arts. 53 a 55). El RD 199/2010, de '
        'venta ambulante, está derogado desde el 7 de agosto de 2021: si tu '
        'ordenanza todavía lo cita, la autorización la sigue dando tu '
        'ayuntamiento con su ordenanza.',
        'El alta y el registro: el puesto se da de alta en la casilla del '
        'impuesto de actividades que marca el libro legal —la venta fuera de '
        'establecimiento, con su nota de churrería, o la de quioscos y '
        'recintos feriales si pones mesas—; y la caseta, el tenderete o el '
        'remolque son comercio al por menor, así que van al registro sanitario '
        'de tu comunidad y no al general (RD 1021/2022, art. 2.2).',
        'La higiene del puesto: lavado de manos, superficies lisas y lavables, '
        'agua potable caliente y fría y eliminación higiénica de los desechos '
        '(Reglamento (CE) 852/2004, anexo II, capítulo III), y los alérgenos '
        'por escrito también en el puesto.',
        'El gas: la bombona única de menos de quince kilos sólo libra de la '
        'instalación receptora a un aparato DE UTILIZACIÓN MÓVIL (RD 919/2006), '
        'y eso sólo vale en la feria, nunca en el local (capítulo 5). Y el '
        'ejemplo de Madrid: cocinar en suelo de uso público pide autorización '
        'previa y captación y filtrado a distancia de cualquier hueco (CUN-25).',
    ],
    'Cuántas raciones necesita una feria para cubrirse': [
        'El punto muerto de cada evento: lo que cuesta ir —la tasa, el '
        'desplazamiento, el montaje y el personal que contratas sólo para el '
        'evento— entre lo que deja cada ración en la feria, que es el precio '
        'sin IVA menos la materia de una ración para llevar. La gente que pasa '
        'por delante del puesto en una hora y la parte que compra las cuentas '
        'tú un día normal de esa feria: es el supuesto que más mueve el '
        'resultado.',
        'Dar los eventos de ejemplo de El Molinete con las raciones que '
        'necesita cada uno para cubrirse, lo que deja y su orden. Y la '
        'advertencia del calendario de ferias: una feria que cae en temporada '
        'alta saca a gente del local justo cuando más vende.',
        'La tasa la fija la ordenanza fiscal de cada municipio: la de '
        'Ochavillo del Río (CUN-37) es un ejemplo, no un orden de magnitud. Y '
        'hay ordenanzas que no tratan el puesto de churros como ambulante y '
        'aún citan el real decreto derogado (CUN-36): se pregunta.',
    ],
    'Cuando la feria es tu negocio, y no un complemento': [
        'Cuándo deja de ser un complemento: si vas a vivir de ferias y '
        'mercados, con remolque propio y varias temporadas al año, es otro '
        'negocio con su propio plan, y lo cubren el Plan de Negocio: Food '
        'Truck y las Tareas: Food Truck. Este pack sólo cuesta la feria como '
        'salida del local.',
        'El equipo de feria tiene precio con fuente: el remolque de churrería, '
        'el carrito para eventos y la churrería portátil (CUS-42), y la '
        'dotación de la caseta en la calculadora de inversión. Con ese equipo '
        'y varias ferias al año, el negocio ya no es el local: es el del plan '
        'del food truck.',
    ],
}

CAP_14 = {
    'n': 14,
    'titulo': 'La Temporada y las Ferias: de Octubre a Marzo, el Verano y las Casetas',
    'resumen_indice': 'el año de una churrería mes a mes, el refuerzo de Navidad, las tres salidas del verano en euros, lo que es legal en una caseta, el punto muerto de cada feria y cuándo la feria es otro negocio.',
    'palabras': 2700, 'bloques': 1,
    'objetivo': 'Que el lector reparta su año por meses con un método, sepa '
                'qué hace con julio y agosto comparando las tres salidas en '
                'euros, y sepa qué papeles pide una caseta y cuántas raciones '
                'necesita cada feria para no perder dinero.',
    'epigrafes': list(PPE_14),
    'puntos_por_epigrafe': PPE_14,
    'puntos_globales': [
        'Capítulo FUNDIDO en dos mitades con frontera explícita: la temporada '
        'del local (el año, Navidad y el verano) y la caseta (lo legal, el '
        'punto muerto y cuándo es otro negocio). No repitas en la segunda lo '
        'que dijo la primera.',
        'La mitad de las ferias es legal: cada regla con su norma y '
        '«comprobado el 3 de octubre de 2026»; las ordenanzas de cada '
        'municipio se preguntan al ayuntamiento.',
        'Los veredictos, en euros de contribución; la fiscalidad no es una '
        'salida del verano.',
    ],
    'cifras': [
        C('Raciones de un año normal de El Molinete', f'{X_TEMP}!Peso sobre el Año!L5', 'num', clave='Raciones del año (origen de X13)'),
        C('Peso de diciembre sobre las raciones del año', f'{X_TEMP}!Peso sobre el Año!E29', 'pct1', clave='Peso de diciembre sobre el año'),
        C('Coste del refuerzo de Navidad y Reyes al año', f'{X_TEMP}!Refuerzo por Pico!B9', 'eur', clave='Coste del refuerzo de Navidad y Reyes al año'),
        C('Contribución de julio y agosto si se cierra', f'{X_TEMP}!El Verano (Tres Salidas)!B16', 'eur', clave='Contribución de julio y agosto si se cierra'),
        C('Contribución de julio y agosto con carta de verano', f'{X_TEMP}!El Verano (Tres Salidas)!C16', 'eur', clave='Contribución de julio y agosto con carta de verano'),
        C('Contribución de julio y agosto saliendo de ferias', f'{X_TEMP}!El Verano (Tres Salidas)!D16', 'eur', clave='Contribución de julio y agosto saliendo de ferias'),
        C('Raciones al día del local por debajo de las cuales la carta de verano deja menos que las ferias', f'{X_TEMP}!El Verano (Tres Salidas)!B24', 'num1', clave='Raciones al día por debajo de las cuales la carta de verano deja menos que las ferias'),
        C('Resultado de julio y agosto con los fijos dentro, con la carta de verano', f'{X_PLAN}!Escenarios!D23', 'eur', clave='Verano con fijos con la carta de verano'),
        C('Lo que deja el mercado navideño de ejemplo', f'{X_TEMP}!Punto Muerto por Evento!D35', 'eur', clave='Lo que deja el evento E3'),
        C('Alta en el impuesto de actividades de un puesto de feria, según el libro legal', f'{X_LEGAL}!Ferias y Venta Ambulante!A18', 'txt', rotulo=('A18', 'Alta en el IAE del puesto')),
    ],
    'sector': ['CUS-11', 'CUS-29', 'CUS-31e', 'CUS-V17', 'CUN-01', 'CUN-11',
               'CUN-19', 'CUN-20', 'CUN-21', 'CUN-22', 'CUN-25', 'CUN-28',
               'CUN-36', 'CUN-37', 'CUS-42', 'CHN-34'],
    # Fuera a propósito: CUS-50 (su nota lleva al prompt el titular de
    # facturación sin método que está en la lista negra).

    'tablas': [
        {
            'titulo': 'El año de El Molinete mes a mes (temporada-franjas-y-ferias.xlsx, hoja «Peso sobre el Año»)',
            'src': (X_TEMP, 'Peso sobre el Año'),
            'cols': [('Mes', 'A', 'txt'), ('Coeficiente (1 = un mes medio)', 'B', 'num2'),
                     ('Temporada', 'C', 'txt'), ('Raciones del mes', 'D', 'num'),
                     ('Peso sobre el año', 'E', 'pct1'),
                     ('Raciones de un día medio del mes', 'F', 'num')],
            'filas': (18, 29),
            'ancla': ('A18', 'Enero'),
            'nota': 'Coeficientes de El Molinete: supuestos declarados con la forma que describen '
                    'las fuentes del sector. Cámbialos por los tuyos con un año de ventas.',
        },
        {
            'titulo': 'Las tres salidas del verano, en euros de julio y agosto (temporada-franjas-y-ferias.xlsx, hoja «El Verano (Tres Salidas)»)',
            'src': (X_TEMP, 'El Verano (Tres Salidas)'),
            'cols': [('Concepto', 'A', 'txt'), ('Cerrar', 'B', 'eur'),
                     ('Carta de verano', 'C', 'eur'), ('Ferias', 'D', 'eur')],
            'filas': (12, 16),
            'ancla': ('A12', 'Ventas del local sin IVA'),
            'nota': 'Cerrar deja cero, no un número negativo: lo que pagas igual en julio y agosto '
                    'ya está en los fijos del año. El resultado del verano con los fijos dentro '
                    'está en el plan financiero, hoja «Escenarios».',
        },
        {
            'titulo': 'El punto muerto de cada feria de ejemplo (temporada-franjas-y-ferias.xlsx, hoja «Punto Muerto por Evento»)',
            'src': (X_TEMP, 'Punto Muerto por Evento'),
            'cols': [('Concepto', 'A', 'txt'),
                     ('Feria local de cinco días', 'B', 'num'),
                     ('Fiestas patronales de tres días', 'C', 'num'),
                     ('Mercado navideño de quince días', 'D', 'num'),
                     ('Romería de dos días', 'E', 'num'),
                     ('Unidad', 'F', 'txt')],
            'filas': (8, 37),
            'omitir_filas': tuple(r for r in range(9, 37) if r not in (25, 26, 31, 32, 35)),
            'anclas': [('A8', 'Días que dura'), ('B6', 'Feria local de cinco días'),
                       ('C6', 'Fiestas patronales de tres días'),
                       ('D6', 'Mercado navideño de quince días'),
                       ('E6', 'Romería de dos días'), ('A32', 'RACIONES PARA CUBRIR'),
                       ('A35', 'LO QUE DEJA EL EVENTO'), ('A37', 'Orden')],
            'nota': 'Las raciones para cubrir el evento son su punto muerto: lo que cuesta ir, sin '
                    'la materia, entre lo que deja cada ración. La gente que pasa y la parte que '
                    'compra son supuestos que cuentas tú en la feria. ' + V_FERIAS,
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO presentar una rebaja de cuota del impuesto de actividades '
        'como salida del verano.',
        'PROHIBIDO citar artículos del real decreto de venta ambulante '
        'derogado, o escribir que la autorización de una feria es indefinida o '
        'se renueva sola.',
        'PROHIBIDO escribir que la bombona libra de la instalación receptora '
        'en un local: sólo un aparato de utilización móvil, y sólo en la '
        'feria.',
        'PROHIBIDO usar la tasa de Ochavillo del Río o los puestos de las '
        'Fallas como orden de magnitud de lo que cuesta o rinde una feria.',
        'PROHIBIDO presentar los coeficientes mensuales como estadística del '
        'sector: son el modelo de El Molinete.',
        'No desarrolles el negocio de ferias como actividad principal: es del '
        'Plan de Negocio: Food Truck.',
    ],
}

# ============================== CAPÍTULO 15 ===============================
PPE_15 = {
    'Lo que publican las enseñas: un orden de magnitud con fecha, no un presupuesto': [
        'Explicar de dónde salen las cifras: la inversión que publica cada '
        'franquiciador a través de un agregador o de su dossier, consultada el '
        '3 de octubre de 2026. Cada enseña dice «inversión» a su manera —con o '
        'sin obra, con o sin IVA, con o sin canon, «desde»— y por eso la tabla '
        'dice qué incluye cada una. Es un orden de magnitud con fecha, no un '
        'presupuesto.',
        'Dar el abanico con sus extremos: la inversión publicada más baja, la '
        'más alta y cuántas enseñas la publican. La más baja no es una '
        'franquicia de churrería al uso: el negocio de esa marca es vender '
        'mezcla, máquinas y remolques (CUS-M23).',
        'Lo que NO es dato: la facturación esperada, el plazo de recuperación '
        'o el número de aperturas que anuncia un franquiciador son '
        'proyecciones suyas, y no entran en tu plan.',
    ],
    'Canon, royalty y publicidad: lo que se paga también en verano': [
        'Dar la mecánica con lo publicado: el canon de entrada, el royalty '
        'sobre las ventas y el canon de publicidad, cada uno con su enseña y su '
        'fuente (CUS-M12, CUS-M14, CUS-M15, CUS-M21, CUS-D6). El royalty se '
        'paga sobre las ventas de cada mes, también en julio y agosto, cuando '
        'una churrería vende menos: se pasa por el plan financiero mes a mes, '
        'no por la media del año.',
        'La duración del contrato también es una cifra: una enseña publica '
        'diez años renovables y otra cinco (CUS-M15, CUS-M21). Lo que firmas '
        'son años de contrato, no una compra.',
    ],
    'Tu inversión frente a las enseñas, con la misma base': [
        'Comparar con la misma base: tu inversión de apertura sin fondo de '
        'maniobra (capítulo 8) frente a las enseñas que publican una base '
        'comparable, el local en bruto con obra, maquinaria y mobiliario. El '
        'libro cuenta cuántas quedan por debajo y cuántas por encima de tu '
        'cifra; las que no publican la obra o el IVA no se comparan, se leen.',
        'La lectura: la franquicia compra marca, método y proveedor; la '
        'independiente se queda el royalty y la decisión. Ninguna es mejor en '
        'abstracto: lo es la que, con tus números en el plan financiero, paga '
        'sus fijos y el royalty en el peor mes. La decisión 12 del bonus lo '
        'resuelve para El Molinete.',
    ],
    'Antes de firmar: la acrilamida con marca, el contrato y las preguntas': [
        'La acrilamida con marca: la parte B del anexo II del reglamento sólo '
        'alcanza a quien opera bajo marca o licencia, como parte de un '
        'funcionamiento interconectado y siguiendo las instrucciones de quien '
        'le suministra de forma centralizada (Reglamento (UE) 2017/2158, art. '
        '2.3). Si tu franquiciador te sirve la masa, pregúntale qué te toca.',
        'Las preguntas antes de firmar, todas por escrito: qué incluye '
        'exactamente la inversión publicada, sobre qué ventas se calculan el '
        'royalty y la publicidad, qué proveedores son obligatorios y a qué '
        'precio, si te suministran la masa de forma centralizada, cuánto dura '
        'el contrato y qué pasa al terminar, y cuántos locales hay abiertos '
        'hoy. Y revisa el contrato con tu asesor antes de firmar.',
    ],
}

CAP_15 = {
    'n': 15,
    'titulo': 'Franquicia o Independiente',
    'resumen_indice': 'qué publican las enseñas y cómo leerlo, el canon, el royalty y la publicidad todo el año, tu inversión frente a las enseñas con la misma base y las preguntas antes de firmar.',
    'palabras': 1300, 'bloques': 1,
    'objetivo': 'Que el lector lea las inversiones publicadas por las enseñas '
                'como lo que son, sepa lo que pagaría cada mes por el canon y '
                'el royalty, compare su propia inversión con la misma base y '
                'llegue a la firma con las preguntas hechas.',
    'epigrafes': list(PPE_15),
    'puntos_por_epigrafe': PPE_15,
    'puntos_globales': [
        'Todas las cifras de enseñas con su fecha de consulta y como orden de '
        'magnitud publicado por el franquiciador, nunca como dato del sector.',
        'Tono neutro: ni a favor ni en contra de franquiciar; la decisión sale '
        'de los números del lector.',
    ],
    'cifras': [
        C('Inversión publicada más baja de las enseñas de la tabla', f'{X_CAPEX}!Franquicia o Independiente!B20', 'eur', clave='Franquicias: inversión publicada más baja'),
        C('Inversión publicada más alta de las enseñas de la tabla', f'{X_CAPEX}!Franquicia o Independiente!B21', 'eur', clave='Franquicias: inversión publicada más alta'),
        C('Enseñas con inversión publicada en la tabla', f'{X_CAPEX}!Franquicia o Independiente!B22', 'num', clave='Franquicias: enseñas con inversión publicada'),
        C('Enseñas de base comparable que publican una inversión por debajo de la de El Molinete', f'{X_CAPEX}!Franquicia o Independiente!B23', 'num', clave='Franquicias de base comparable por debajo de tu CAPEX'),
        C('Enseñas de base comparable que publican una inversión igual o por encima de la de El Molinete', f'{X_CAPEX}!Franquicia o Independiente!B24', 'num', rotulo=('A24', 'Enseñas de base comparable que publican una inversión igual o por enci')),
        C('Inversión de apertura de El Molinete sin fondo de maniobra', f'{X_CAPEX}!Resumen!L5', 'eur', clave='CAPEX de apertura sin fondo de maniobra (origen de X10)'),
    ],
    'sector': ['CUS-M12', 'CUS-M14', 'CUS-M15', 'CUS-M17', 'CUS-M19',
               'CUS-M20', 'CUS-M21', 'CUS-M22', 'CUS-M23', 'CUS-D6',
               'CUS-03'],
    'tablas': [
        {
            'titulo': 'Lo que publican las enseñas de churros y chocolate (calculadora-capex-churreria.xlsx, hoja «Franquicia o Independiente»)',
            'src': (X_CAPEX, 'Franquicia o Independiente'),
            'cols': [('Enseña', 'A', 'txt'), ('Inversión publicada', 'B', 'eur'),
                     ('Qué incluye, según la enseña', 'C', 'txt'),
                     ('Canon de entrada', 'D', 'eur'),
                     ('Royalty sobre ventas', 'E', 'pct0'),
                     ('Locales', 'F', 'txt'),
                     ('¿Base comparable con la tuya?', 'I', 'txt')],
            'filas': (6, 17),
            'ancla': ('A6', 'Chocolaterías Valor'),
            'nota': 'Inversión publicada por cada franquiciador, consultada el 3 de octubre de '
                    '2026: orden de magnitud, no presupuesto. Cada enseña dice «inversión» a su '
                    'manera; la columna «Qué incluye» manda.',
        },
        {
            'titulo': 'Las preguntas antes de firmar una franquicia',
            'cabecera': ['Pregunta', 'Por qué importa', 'Dónde se comprueba'],
            'filas': [
                ['¿Qué incluye exactamente la inversión publicada?', 'Unas enseñas cuentan la obra, el IVA o el canon y otras no', 'En el dossier, partida a partida, frente a tu calculadora de inversión'],
                ['¿Sobre qué ventas se calculan el royalty y la publicidad?', 'Se pagan también en julio y agosto, cuando vendes menos', 'En el contrato, y en el plan financiero mes a mes'],
                ['¿Qué proveedores son obligatorios y a qué precio?', 'La masa y el chocolate son tu coste de materia', 'En el contrato y en una lista de precios por escrito'],
                ['¿Te suministran la masa o el preparado de forma centralizada?', 'Con marca, funcionamiento interconectado e instrucciones de quien suministra, te alcanza la parte B de la acrilamida', 'Reglamento (UE) 2017/2158, art. 2.3'],
                ['¿Cuánto dura el contrato y qué pasa al terminar?', 'Lo que firmas son años, no una compra', 'En el contrato'],
                ['¿Cuántos locales hay abiertos hoy?', 'Las aperturas que se anuncian son un objetivo, no un dato', 'Pídelo por escrito a la enseña'],
            ],
            'nota': 'Todo por escrito y revisado con tu asesor antes de firmar.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO presentar como dato la facturación esperada, el plazo de '
        'recuperación o el número de aperturas que anuncia un franquiciador.',
        'PROHIBIDO escribir que la parte B de la acrilamida alcanza «a las '
        'franquicias» sin sus tres condiciones del art. 2.3.',
        'PROHIBIDO recomendar o desaconsejar una enseña concreta, o comparar '
        'su inversión con la tuya sin decir qué incluye cada una.',
        'PROHIBIDO usar la inversión «desde» de una enseña como si fuera su '
        'inversión total.',
    ],
}

# ============================== CAPÍTULO 16 ===============================
PPE_16 = {
    'La cuenta de resultados a tres años, con el año de crucero delante': [
        'Explicar la estructura del plan: el año uno con la rampa de '
        'arranque, el año dos de crucero —un año entero sin rampa, la foto de '
        'un año normal— y el año tres, que repite el crucero y sólo cambia los '
        'intereses. Todas las ventas van sin IVA, y el margen de cada ración '
        'sale del escandallo del libro de la carta, nunca de un porcentaje del '
        'sector.',
        'Dar el año de crucero de El Molinete: la contribución del año, los '
        'costes fijos —plantilla, renta, gastos fijos, amortización e '
        'intereses— y el resultado antes de impuestos, con su lectura en '
        'euros. El resultado sobre ventas es información, no veredicto. El '
        'impuesto de sociedades o el IRPF no están: dependen de tu forma '
        'jurídica y los calcula tu asesor.',
    ],
    'El punto de equilibrio en raciones al día, y los meses que no pagan sus fijos': [
        'El punto de equilibrio en la unidad que entiende una churrería: '
        'raciones al día. Dar el de El Molinete, las raciones que prevé '
        'vender de media y el margen de seguridad entre las dos.',
        'Mes a mes: dar cuántos meses del año de crucero no pagan sus fijos; '
        'la tabla dice cuáles. Esos meses los pagan los meses buenos, y por '
        'eso el fondo de maniobra se calcula sobre meses de fijos y no sobre la '
        'media del año.',
    ],
    'Qué canal paga los fijos: la sala, el para llevar o los dos': [
        'La pregunta que separa una churrería de una cafetería: si sólo '
        'tuvieras la sala, o sólo el para llevar, ¿pagarías los fijos del '
        'año? Dar, con la hoja de canales, lo que le sobra o le falta a la '
        'sala sola, y la lectura en euros de cada canal y de los dos juntos.',
        'Lo que eso significa para el formato: el mismo local vendiendo sólo '
        'para llevar se compara en la decisión 1 del bonus, con los mismos '
        'fijos.',
    ],
    'La caja: inversión total, fondo de maniobra, préstamo y el valle del primer año': [
        'La inversión total que le enseñas al banco: la inversión de apertura '
        'sin fondo de maniobra (capítulo 8) más el fondo de maniobra, que se '
        'calcula sólo aquí, sobre meses de fijos de caja. El préstamo y lo que '
        'pone el promotor salen de la estructura de financiación del libro; el '
        'IVA que adelantas no está aquí, porque es caja que recuperas.',
        'El valle de tesorería del primer año: el saldo más bajo de la cuenta, '
        'el mes en que llega y si el fondo lo aguanta. La carencia del '
        'préstamo hace que la cuota no se coma la caja durante la rampa; la '
        'cuota y lo que sobra en el peor año del préstamo están en la hoja de '
        'financiación.',
    ],
    'Los primeros noventa días: qué mirar cada semana': [
        'Con el plan delante: compara cada semana las raciones vendidas con '
        'las del punto de equilibrio, el ticket sin IVA con el del escandallo '
        'y los días entre cambios de aceite con los del libro del aceite; y '
        'cada mes, el saldo de caja con el de la hoja de tesorería. Si la '
        'rampa va más lenta de lo previsto, lo verás antes en la caja que en '
        'el resultado.',
        'Cuando tengas un año de ventas, sustituye los coeficientes de '
        'temporada por los tuyos y vuelve a pasar el plan; con la facturación '
        'verificable de 2027 en el horizonte (capítulo 9).',
    ],
}

CAP_16 = {
    'n': 16,
    'titulo': 'El Plan Financiero, el Punto de Equilibrio y los Primeros Noventa Días',
    'resumen_indice': 'la cuenta de resultados a tres años, el punto de equilibrio en raciones al día, qué canal paga los fijos, la inversión total con su fondo de maniobra, el valle de caja y qué vigilar los primeros noventa días.',
    'palabras': 1500, 'bloques': 1,
    'objetivo': 'Que el lector sepa leer su cuenta de resultados a tres años, '
                'cuántas raciones al día necesita para no perder dinero, qué '
                'canal paga sus fijos, cuánto dinero tiene que haber en la '
                'cuenta el día que abre y qué mirar cada semana al empezar.',
    'epigrafes': list(PPE_16),
    'puntos_por_epigrafe': PPE_16,
    'puntos_globales': [
        'Veredictos en euros: el resultado antes de impuestos, el punto de '
        'equilibrio en raciones al día y el valle de caja. Ningún porcentaje '
        'del sector sustituye a una cifra del libro.',
        'Frontera: el IVA es del capítulo 3, la inversión de apertura del '
        'capítulo 8 y el verano del capítulo 14; aquí se suman.',
    ],
    'cifras': [
        C('Contribución del año de crucero de El Molinete', f'{X_PLAN}!PyG 3 Años!C15', 'eur', clave='Contribución del año de crucero'),
        C('Resultado antes de impuestos del año de crucero', f'{X_PLAN}!PyG 3 Años!C23', 'eur', clave='Resultado antes de impuestos del año de crucero'),
        C('Punto de equilibrio en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B12', 'num', clave='Punto de equilibrio en raciones al día'),
        C('Raciones al día que prevé vender El Molinete, media del año', f'{X_PLAN}!Punto de Equilibrio!B13', 'num', clave='Raciones al día previstas (media del año)'),
        C('Margen de seguridad en raciones al día por encima del equilibrio', f'{X_PLAN}!Punto de Equilibrio!B14', 'num', clave='Margen de seguridad en raciones al día'),
        C('Meses del año de crucero que no pagan sus fijos', f'{X_PLAN}!Punto de Equilibrio!B36', 'num', clave='Meses del año de crucero que no pagan sus fijos'),
        C('La sala sola menos los fijos del año', f'{X_PLAN}!Canales y Punto Muerto!C17', 'eur', clave='La sala menos los fijos del año'),
        C('Inversión total: inversión de apertura más fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B24', 'eur', clave='Inversión total (CAPEX más fondo de maniobra)'),
        C('Saldo más bajo de la cuenta en el primer año, el valle', f'{X_PLAN}!Tesorería 12 meses!B34', 'eur', clave='Valle de tesorería del año 1'),
        C('Mes del valle de tesorería', f'{X_PLAN}!Tesorería 12 meses!B35', 'txt', clave='Mes del valle de tesorería'),
    ],
    'sector': ['CHN-75', 'CHN-71c', 'CUN-18'],
    'tablas': [
        {
            'titulo': 'La cuenta de resultados de El Molinete a tres años (plan-financiero-3-anos-churreria.xlsx, hoja «PyG 3 Años»)',
            'src': (X_PLAN, 'PyG 3 Años'),
            'cols': [('Concepto', 'A', 'txt'), ('Año 1, con rampa', 'B', 'eur'),
                     ('Año 2, crucero', 'C', 'eur'), ('Año 3', 'D', 'eur')],
            'filas': (9, 24),
            'ancla': ('A9', 'Ventas sin IVA de la carta de invierno'),
            'nota': 'Resultado ANTES de impuestos: el impuesto de sociedades o el IRPF dependen de '
                    'tu forma jurídica. Todo sin IVA.',
        },
        {
            'titulo': 'El año de crucero mes a mes: qué meses pagan sus fijos (plan-financiero-3-anos-churreria.xlsx, hoja «Punto de Equilibrio»)',
            'src': (X_PLAN, 'Punto de Equilibrio'),
            'cols': [('Mes', 'A', 'txt'), ('Raciones al día', 'E', 'num'),
                     ('Contribución del mes', 'F', 'eur'),
                     ('Fijos del mes', 'G', 'eur'),
                     ('Resultado del mes', 'H', 'eur'),
                     ('¿Paga sus fijos?', 'I', 'txt')],
            'filas': (23, 35),
            'ancla': ('A23', 'Enero'),
            'nota': 'Los meses que no pagan sus fijos los pagan los meses buenos: por eso el fondo '
                    'de maniobra se calcula sobre meses de fijos.',
        },
        {
            'titulo': '¿Qué canal paga los fijos? (plan-financiero-3-anos-churreria.xlsx, hoja «Canales y Punto Muerto»)',
            'src': (X_PLAN, 'Canales y Punto Muerto'),
            'cols': [('Si sólo tuvieras…', 'A', 'txt'),
                     ('Contribución del año', 'B', 'eur'),
                     ('Menos los fijos del año', 'C', 'eur'),
                     ('Lectura en euros', 'D', 'txt'),
                     ('Raciones al día de equilibrio si todas fueran de ese canal', 'E', 'num')],
            'filas': (17, 20),
            'ancla': ('A17', 'La sala'),
            'nota': 'Los mismos fijos del año para cada fila: la lectura dice si ese canal, solo o '
                    'con los demás, los paga.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO llamar «resultado neto» o «beneficio» al resultado antes de '
        'impuestos, o calcular un impuesto.',
        'PROHIBIDO dar la rentabilidad o el margen con un porcentaje del '
        'sector: los veredictos son los del libro, en euros.',
        'PROHIBIDO mezclar el IVA que adelantas con la inversión.',
        'No repitas la explicación del CAPEX (capítulo 8) ni la del verano '
        '(capítulo 14): aquí se suman.',
    ],
}

# ================================= ANEXO ==================================
PPE_A = {
    'Norma a norma: vigente, derogada o en revisión': [
        'Recorrer las normas del pack con su estado a 3 de octubre de 2026, '
        'una línea cada una y en el orden de los capítulos: la norma de '
        'calidad de los aceites calentados, en vigor y con los artículos de '
        'manipulaciones derogados; el reglamento europeo de la acrilamida y la '
        'recomendación de la Comisión; las tarifas del impuesto de '
        'actividades; la clasificación de actividades de 2025; los tipos de '
        'IVA; la ley de comercio minorista en su parte de venta ambulante y el '
        'real decreto de venta ambulante, derogado; el registro sanitario y el '
        'reglamento europeo de higiene; la Ley 12/2012; la ordenanza de '
        'calidad del aire y la orden de horarios de Madrid; el Código Técnico, '
        'el reglamento de protección contra incendios y el de gas; la ley de '
        'residuos; el Estatuto de los Trabajadores; el acuerdo laboral estatal '
        'de hostelería; el convenio de Madrid y el de Toledo; y la norma del '
        'chocolate.',
        'Cada norma con su fecha de última actualización vista y su riesgo de '
        'caducidad: alto para la revisión de la acrilamida, la Ley 12/2012 y '
        'el convenio de Madrid; medio para las tarifas del impuesto, el IVA de '
        'la taza para llevar, las ordenanzas de Madrid, la normativa técnica y '
        'la de plásticos; bajo para el resto.',
    ],
    'Lo que va a cambiar y cuándo': [
        'Lo que tiene fecha: la facturación verificable llega en 2027, para '
        'las sociedades en enero y para el resto en julio; la cuantía del '
        'salario mínimo es la de 2026; el convenio de Toledo de ejemplo rige '
        'hasta el 31 de diciembre de 2026; el acuerdo laboral estatal de '
        'hostelería sigue vigente hasta el 31 de diciembre de 2030; y el '
        'convenio de Madrid está vencido y en negociación, así que su texto '
        'nuevo cambiará el libro de turnos y el plan financiero.',
        'Lo que está en marcha sin fecha: la Comisión revisa el marco de la '
        'acrilamida con niveles máximos por primera vez, en fase de consulta y '
        'con fuente secundaria (CUN-08), y el registro horario digital está '
        'pendiente de desarrollo. Cuando cambien, cambia la versión del pack.',
    ],
    'Lo que no está verificado y se pregunta': [
        'Lo que este pack NO afirma, y a quién se le pregunta: las ordenanzas '
        'de humos, ruido, terrazas y vertido fuera de Madrid, al ayuntamiento; '
        'la correspondencia del epígrafe del impuesto con el código de '
        'actividad, al asesor; el tipo de IVA del chocolate y de las bebidas '
        'para llevar, al asesor; que el convenio de un obrador alcance a un '
        'despacho con sala, a un laboralista; la tasa de cada feria, a la '
        'ordenanza fiscal de cada municipio.',
        'Lo que no se pudo abrir el día de la verificación y queda como dato '
        'de anuncio sin volver a comprobar: los anuncios de traspaso y la '
        'renta de referencia. Por eso son precios pedidos, no pagados.',
    ],
    'Cómo se comprueba una norma en un minuto': [
        'El método: el texto consolidado del BOE, con la versión vigente y su '
        'fecha; el boletín de tu comunidad para su normativa; EUR-Lex para la '
        'europea; y REGCON para los convenios. Mira la fecha de la última '
        'modificación y, si es posterior a la de este anexo, lee el cambio '
        'antes de fiarte del libro.',
        'Y cuándo hacerlo: antes de firmar el local, antes de pedir el '
        'préstamo y en cada actualización del pack.',
    ],
}

CAP_A = {
    'n': 17,
    'sin_numerar': True,
    'titulo': 'Anexo Normativo, Actualizado a 3 de Octubre de 2026',
    'resumen_indice': 'las normas del pack con su estado, lo que va a cambiar y cuándo, lo que no está verificado y a quién se pregunta, y cómo se comprueba una norma.',
    'palabras': 1200, 'bloques': 1,
    'objetivo': 'Que el lector sepa en qué estado está cada norma que usa el '
                'pack a 3 de octubre de 2026, qué va a cambiar y cuándo, qué '
                'tiene que preguntar y a quién, y cómo comprobarlo él mismo.',
    'epigrafes': list(PPE_A),
    'puntos_por_epigrafe': PPE_A,
    'puntos_globales': [
        'Cada norma con su estado y su fecha; ninguna afirmación sin su '
        'fuente. Lo no verificado se dice como pregunta, con a quién se hace.',
        'El anexo no repite la explicación de los capítulos: da el estado de '
        'la norma y remite al capítulo en una frase.',
    ],
    'cifras': [
        C('Límite legal de compuestos polares del aceite de fritura', f'{X_ACEITE}!Parámetros!B25', 'pct0', clave='Límite legal de compuestos polares'),
        C('Umbral del «sin gluten», en miligramos por kilo', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B25', 'num', clave='Umbral del «sin gluten» (mg/kg)'),
        C('Salario mínimo interprofesional anual de 2026', f'{X_TURNOS}!Parámetros!B20', 'eur', clave='SMI anual'),
        C('Tablas salariales del convenio de ejemplo y su estado', f'{X_TURNOS}!Parámetros!B16', 'txt', clave='Tablas salariales del ejemplo'),
        C('Años entre inspecciones periódicas de la instalación de gas', f'{X_LEGAL}!Licencia, Humos y Gas!B11', 'num', clave='Años entre inspecciones del gas'),
        C('Kilos de la bombona por debajo de los cuales no hay instalación receptora, sólo con un aparato móvil y sólo en la feria', f'{X_LEGAL}!Licencia, Humos y Gas!B12', 'num', clave='Peso de bombona sin instalación receptora (kg)'),
        C('Hora mínima de apertura como chocolatería en el ejemplo de Madrid', f'{X_TEMP}!Parámetros!B28', 'num', clave='Hora mínima de apertura como chocolatería (ejemplo de Madrid)'),
        C('Hora mínima de apertura como cafetería o bar en el ejemplo de Madrid', f'{X_TEMP}!Parámetros!B29', 'num', clave='Hora mínima de apertura como cafetería o bar (ejemplo de Madrid)'),
        C('Potencia de la cocina por encima de la cual es local de riesgo especial bajo, en kW', f'{X_PROD}!Parámetros!B10', 'num', clave='Umbral de riesgo especial bajo'),
        C('Potencia de la cocina por encima de la cual el riesgo es alto y la extinción automática obligatoria, en kW', f'{X_PROD}!Parámetros!B12', 'num', clave='Umbral de riesgo alto y extinción automática'),
    ],
    'sector': ['CUN-02', 'CUN-08', 'CUN-19', 'CUN-26', 'CUN-32', 'CUN-34',
               'CUN-35', 'CUN-V01', 'CHN-67', 'CHN-68', 'CHN-75'],
    'tablas': [
        {
            'titulo': 'Las normas del pack y su estado a 3 de octubre de 2026',
            'cabecera': ['Norma', 'Estado', 'Capítulo', 'Riesgo de caducidad'],
            'filas': [
                ['Orden de 26 de enero de 1989, aceites y grasas calentados', 'En vigor; arts. 7, 8, 10, 11 y 12 derogados', '10', 'Bajo'],
                ['Reglamento (UE) 2017/2158 y Recomendación (UE) 2019/1888, acrilamida', 'En vigor; revisión con niveles máximos en consulta', '11 y 15', 'Alto'],
                ['RDLeg 1175/1990, tarifas del impuesto de actividades', 'En vigor', '9 y 14', 'Medio'],
                ['RD 10/2025, clasificación de actividades de 2025', 'En vigor', '9', 'Bajo'],
                ['Ley 37/1992 del IVA y RD 650/2011 de bebidas refrescantes', 'En vigor; la taza para llevar, en zona gris', '3', 'Medio'],
                ['Ley 7/1996 de comercio minorista, arts. 53 a 55', 'En vigor; el RD 199/2010 de venta ambulante, derogado desde el 7 de agosto de 2021', '14', 'Bajo'],
                ['RD 1021/2022 y Reglamento (CE) 852/2004', 'En vigor', '9, 11 y 14', 'Bajo'],
                ['Ley 12/2012, arts. 2 y 3 y su Anexo', 'En vigor', '4', 'Alto'],
                ['Ordenanza de Calidad del Aire de Madrid y Orden de horarios de Madrid', 'En vigor; modificaciones posteriores no comprobadas', '4 y 5', 'Medio'],
                ['Código Técnico de la Edificación, RIPCI y RD 919/2006 del gas', 'En vigor', '5', 'Medio'],
                ['Ley 7/2022 de residuos', 'En vigor', '3 y 10', 'Medio'],
                ['Estatuto de los Trabajadores, arts. 34.9 y 36.1', 'En vigor; registro horario digital pendiente', '13', 'Medio'],
                ['Convenio de hostelería de la Comunidad de Madrid', 'Vencido el 31 de diciembre de 2025, en negociación; tablas de 2025', '13', 'Alto'],
                ['RD 1055/2003, productos de cacao y chocolate', 'En vigor', '3', 'Bajo'],
            ],
            'nota': 'Estado comprobado el 3 de octubre de 2026 sobre el texto consolidado de cada '
                    'norma. Las ordenanzas municipales de humos, ruido, terrazas y vertido sólo '
                    'están comprobadas para Madrid.',
        },
        {
            'titulo': 'Lo que va a cambiar, con su fecha',
            'cabecera': ['Qué', 'Cuándo', 'Qué cambia en el pack'],
            'filas': [
                ['Facturación verificable, sociedades', 'Antes del 1 de enero de 2027', 'El TPV y el capítulo 9'],
                ['Facturación verificable, resto de obligados', 'Antes del 1 de julio de 2027', 'El TPV y el capítulo 9'],
                ['Salario mínimo interprofesional', 'Cuantía de 2026, hasta el 31 de diciembre de 2026', 'El suelo del libro de turnos'],
                ['Convenio de hostelería de Madrid', 'Texto nuevo en negociación', 'El libro de turnos y el plan financiero'],
                ['Convenio de Toledo, ejemplo del método', 'Hasta el 31 de diciembre de 2026', 'Sólo el ejemplo del capítulo 13'],
                ['Acuerdo laboral estatal de hostelería', 'Vigente hasta el 31 de diciembre de 2030', 'Nada mientras esté vigente'],
                ['Revisión del marco de la acrilamida', 'En consulta, sin fecha', 'El capítulo 11 y el libro legal'],
            ],
            'nota': 'Antes de cada nueva versión del pack se vuelve a comprobar cada fila.',
        },
    ],
    'prohibido': NO_COMUN + [
        'PROHIBIDO dar por vigente una norma sin su fecha de comprobación, o '
        'citar artículos de una norma derogada.',
        'PROHIBIDO afirmar requisitos municipales fuera de Madrid: se '
        'preguntan al ayuntamiento.',
        'No repitas la explicación de los capítulos: estado, fecha y remisión.',
    ],
}

CAPITULOS = [CAP_01, CAP_02, CAP_03, CAP_04, CAP_05, CAP_06, CAP_07, CAP_08,
             CAP_09, CAP_10, CAP_11, CAP_12, CAP_13, CAP_14, CAP_15, CAP_16,
             CAP_A]


# ==========================================================================
# BONUS 1 — Business plan modelo (2 bloques, D26). El resumen ejecutivo DA el
# resultado (antes de impuestos: el libro 6 no calcula Sociedades ni IRPF,
# desviación declarada), el margen y el punto de equilibrio. Tablas del
# libro 6 celda a celda, más las de canales y plantilla.
# ==========================================================================
PPE_BP1 = {
    'El proyecto en una página: qué se monta, dónde y para quién': [
        'Presentar el proyecto en registro de banco: una churrería-chocolatería '
        'con sala, barra, terraza y despacho a calle, en un local de barrio de '
        'una gran ciudad, abierta del desayuno a la merienda y la noche del fin '
        'de semana. El caso es El Molinete, modelado: no es un negocio real, y '
        'sus cifras salen de las ocho herramientas Excel del pack.',
        'Decir una sola vez, al principio, que cada cifra sale de una celda del '
        'pack que se puede abrir y cambiar por la propia: es una plantilla '
        'rellena, no una previsión de los resultados del lector.',
    ],
    'La inversión, su financiación y el resultado del año de crucero': [
        'Dar la inversión de apertura sin fondo de maniobra, el fondo de '
        'maniobra y la inversión total; y cómo se financia: el préstamo '
        'bancario y lo que pone el promotor.',
        'Dar EN ESTA PÁGINA el resultado del año de crucero ANTES de '
        'impuestos, el resultado sobre ventas y el punto de equilibrio en '
        'raciones al día frente a las que se prevé vender, con el margen de '
        'seguridad entre las dos. No se remite a la sección financiera para '
        'esto.',
        'Decir por qué el resultado va antes de impuestos: el impuesto de '
        'sociedades o el IRPF dependen de la forma jurídica, que el plan no '
        'fija.',
    ],
    'El mercado y la plaza: lo que se sabe y lo que no': [
        'Decir lo que no hay: ninguna estadística pública cuenta las '
        'churrerías ni sus ventas, así que el plan no da un tamaño de mercado; '
        'da la plaza. Los locales de hostelería del INE son el contexto '
        '(CUS-06), no el mercado de la churrería.',
        'Dar la plaza con precios publicados y su año: lo que cuesta la ración '
        'y la taza en las ciudades con dato (CUS-15, CUS-17, CUS-19), y las '
        'franjas que mandan: el desayuno y la merienda, más la noche del fin de '
        'semana.',
    ],
    'El concepto y la carta: churro, porra y chocolate a la taza, en sala y para llevar': [
        'El concepto: churros y porras fritos al momento, chocolate a la taza '
        'hecho con un preparado comercial cuya etiqueta manda en la '
        'denominación, cafés y una carta de verano para julio y agosto; con el '
        'peso de cada canal, sala y para llevar, en la tabla de canales.',
        'Dar el ticket medio sin IVA por ración de la carta de invierno y el '
        'margen sobre materia prima con su definición en la misma frase —el '
        'ticket sin IVA menos la materia y el aceite absorbido— y con su valor '
        'exacto. Y decir que no es la rentabilidad del negocio, que es el '
        'resultado del plan.',
    ],
    'Las operaciones: el local, la línea de fritura y la hora punta': [
        'El local: la superficie útil, con la extracción a cubierta como '
        'primera condición —licencia de obra y técnico— y la fritura en su '
        'zona bajo campana. La capacidad de la línea en raciones por hora y el '
        'veredicto del libro de temporada sobre si hace falta una segunda '
        'churrera.',
        'Las raciones de un año normal y cómo se reparten: temporada alta de '
        'octubre a marzo, diciembre por encima de todo y el valle de julio y '
        'agosto, con carta de verano.',
    ],
    'La plantilla, los turnos y el calendario de apertura': [
        'La plantilla y su coste anual, con el convenio de ejemplo en su '
        'estado real —tablas de 2025 de un convenio vencido y en negociación— '
        'y el salario mínimo como suelo; las horas de apertura con mínimo de '
        'cobertura cada semana, y el titular en nómina como un puesto más.',
        'El calendario: lo que dura el proyecto desde la búsqueda del local '
        'hasta la apertura, y el mes en que abre, con la ruta crítica del '
        'libro legal.',
    ],
}

PPE_BP2 = {
    'La cuenta de resultados a tres años': [
        'Dar los tres años con la tabla delante: el año uno con la rampa de '
        'arranque, el año dos de crucero y el año tres; la contribución, los '
        'costes fijos y el resultado antes de impuestos de cada uno, y la '
        'contribución por ración del crucero.',
        'Explicar en una frase cada línea de coste fijo: la plantilla del libro '
        'de turnos, la renta, los gastos fijos que nacen en el propio plan '
        '(con su tabla), la amortización, que no sale de la caja, y los '
        'intereses del cuadro del préstamo.',
    ],
    'El punto de equilibrio y el año mes a mes': [
        'Dar el punto de equilibrio contable y el de caja, en raciones al día, '
        'y cuántos meses del año de crucero no pagan sus fijos, con el '
        'resultado de agosto; la tabla mes a mes dice cuáles.',
        'La consecuencia para la caja: los meses malos los pagan los buenos, y '
        'por eso el fondo de maniobra se calcula sobre meses de fijos.',
    ],
    'La tesorería del primer año y el valle': [
        'Dar el saldo de caja el día que se abre, el valle del primer año con '
        'su mes y la lectura del libro, y el saldo al cierre del año uno.',
        'Explicar por qué el valle llega pronto: la rampa de arranque vende '
        'menos los primeros meses mientras los fijos se pagan enteros desde el '
        'primero, y la carencia del préstamo evita que la cuota se sume a ese '
        'esfuerzo.',
    ],
    'La financiación: el préstamo, la cuota y lo que sobra': [
        'Dar las condiciones del préstamo de la estructura —tipo nominal, plazo '
        'y carencia—, la cuota mensual y lo que sobra en el peor año después '
        'de pagar al banco, con el ratio de cobertura de la deuda más bajo como '
        'información para el banco.',
        'Pedir la oferta del banco por escrito y con su TAE: el tipo del plan '
        'es un supuesto heredado, no una oferta.',
    ],
    'Los riesgos, con su cifra y su respuesta': [
        'Riesgo de volumen: el margen de seguridad en raciones al día y las '
        'raciones al día que hacen falta sólo para pagar a las personas.',
        'Riesgo del verano: lo que deja la carta de verano frente a cerrar, y '
        'el resultado de julio y agosto con sus fijos dentro.',
        'Riesgo del aceite: el margen que se pierde al año con la subida más '
        'alta del libro del aceite si no se toca el precio de venta.',
        'Riesgo de formato y de convenio: el resultado del mismo local '
        'vendiendo sólo para llevar, con los mismos fijos; y unas tablas '
        'salariales de un convenio vencido y en negociación, cuyo texto nuevo '
        'cambiará la plantilla y el plan.',
    ],
}

BONUS = [
    {
        'nombre': 'business-plan-modelo-churreria-chocolateria',
        'guia': {
            'titulo': 'Business Plan Modelo de una Churrería-Chocolatería',
            'subtitulo': 'Bonus del pack «Cómo Montar una Churrería-Chocolatería» · el '
                         'caso completo relleno, con las cifras de las ocho '
                         'herramientas Excel',
            'cabecera': 'AI Chef Pro · Business Plan Modelo de una Churrería-Chocolatería',
            'tipo_doc': 'documento',
            'tipo_doc_art': 'del business plan',
            'tipo_doc_dem': 'este documento',
            'categoria_doc': 'Plantilla profesional',
            'portada_texto': (
                'El plan de negocio de una churrería-chocolatería modelada, '
                'relleno de principio a fin y en el formato que pide un banco: '
                'resumen ejecutivo, mercado y plaza, concepto y carta, '
                'operaciones, plan financiero a tres años, tesorería y riesgos. '
                'Todas las cifras salen de las ocho herramientas Excel del '
                'pack, así que puedes abrir la celda de la que sale cada una y '
                'cambiarla por la tuya. Es una plantilla rellena para que la '
                'copies, no una previsión de tus resultados.'),
        },
        'gates': {
            'paginas_prometidas': 9,
            'palabras_objetivo': 3500,
            'min_palabras_cap': 1200,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': 'Business Plan Modelo de una Churrería-Chocolatería',
                     'subject': 'Bonus del pack Cómo Montar una Churrería-Chocolatería · '
                                'Versión 1.0 · octubre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Resumen Ejecutivo, Mercado, Concepto y Operaciones',
                'resumen_indice': 'el proyecto en una página con su inversión, su financiación, su resultado y su punto de equilibrio; la plaza, la carta, el local, la línea y la plantilla.',
                'palabras': 1750, 'bloques': 1,
                'objetivo': 'Que quien lee el plan sepa en la primera página '
                            'qué proyecto es, cuánto dinero necesita, de dónde '
                            'sale, qué resultado da y cuántas raciones al día '
                            'necesita para no perder; y después, con qué '
                            'carta, qué local y qué plantilla se consigue.',
                'epigrafes': list(PPE_BP1),
                'puntos_por_epigrafe': PPE_BP1,
                'puntos_globales': [
                    'Registro de documento de banco: frases cortas, cifras '
                    'delante y cero lenguaje comercial.',
                    'El resultado (antes de impuestos), el margen y el punto de '
                    'equilibrio van EN EL RESUMEN EJECUTIVO, no se remiten a la '
                    'sección financiera.',
                    'Cada cifra sale de una celda del pack y se puede abrir: '
                    'eso se dice una vez, al principio del documento.',
                ],
                'cifras': [
                    C('Inversión de apertura sin fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B22', 'eur', rotulo=('A22', 'CAPEX sin fondo')),
                    C('Fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B19', 'eur', clave='Fondo de maniobra'),
                    C('Inversión total', f'{X_PLAN}!Inversión Inicial!B24', 'eur', clave='Inversión total (CAPEX más fondo de maniobra)'),
                    C('Préstamo bancario', f'{X_PLAN}!Inversión Inicial!B25', 'eur', rotulo=('A25', 'De ella, préstamo bancario')),
                    C('Recursos propios que pone el promotor', f'{X_PLAN}!Inversión Inicial!B26', 'eur', clave='Recursos propios que pone el promotor'),
                    C('Ventas sin IVA del año de crucero', f'{X_PLAN}!PyG 3 Años!C28', 'eur', clave='Ventas sin IVA del año de crucero (verano estimado)'),
                    C('Resultado antes de impuestos del año de crucero', f'{X_PLAN}!PyG 3 Años!C23', 'eur', clave='Resultado antes de impuestos del año de crucero'),
                    C('Resultado sobre ventas del año de crucero', f'{X_PLAN}!PyG 3 Años!C29', 'pct1', clave='Resultado sobre ventas del año de crucero'),
                    C('Punto de equilibrio en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B12', 'num', clave='Punto de equilibrio en raciones al día'),
                    C('Raciones al día previstas, media del año', f'{X_PLAN}!Punto de Equilibrio!B13', 'num', clave='Raciones al día previstas (media del año)'),
                    C('Margen de seguridad en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B14', 'num', clave='Margen de seguridad en raciones al día'),
                    C('Ticket medio sin IVA por ración de la carta de invierno', f'{X_CARTA}!Mix y Ticket Canal y Temporada!D6', 'eur2', clave='Ticket sin IVA por ración (invierno)'),
                    C('Margen sobre materia prima en invierno: el ticket sin IVA menos la materia y el aceite absorbido', f'{X_CARTA}!Los Dos Márgenes!B6', 'pct1', clave='Margen sobre materia prima (invierno)'),
                    C('Superficie útil del local', f'{X_PROD}!Parámetros!B6', 'num', clave='Superficie útil del local'),
                    C('Capacidad de la línea en raciones por hora', f'{X_PROD}!Cuello de Botella!L5', 'num', clave='Capacidad del conjunto en raciones por hora'),
                    C('Veredicto «¿una churrera o dos?»', f'{X_TEMP}!Capacidad contra el Pico!E23', 'txt', clave='Veredicto «¿Una churrera o dos?»'),
                    C('Raciones de un año normal', f'{X_TEMP}!Peso sobre el Año!L5', 'num', clave='Raciones del año (origen de X13)'),
                    C('Coste anual de la plantilla', f'{X_TURNOS}!Coste de Plantilla!L5', 'eur', clave='Coste anual de plantilla (origen de X15)'),
                    C('Horas de apertura a la semana con mínimo de cobertura', f'{X_TURNOS}!Cuadrante por Franja!B5', 'num1', clave='Horas de apertura con mínimo de cobertura a la semana'),
                    C('Meses que dura el proyecto hasta la apertura', f'{X_LEGAL}!Cronograma y Ruta Crítica!C47', 'num', clave='Duración total del proyecto (meses)'),
                    C('Mes de apertura', f'{X_LEGAL}!Cronograma y Ruta Crítica!C50', 'txt', clave='Nombre del mes de apertura'),
                ],
                'sector': ['CUS-06', 'CUS-07', 'CUS-15', 'CUS-17', 'CUS-19',
                           'CUN-35', 'CUN-39', 'CUN-V01'],
                'tablas': [
                    {
                        'titulo': 'La inversión y su financiación (plan-financiero-3-anos-churreria.xlsx, hoja «Inversión Inicial»)',
                        'src': (X_PLAN, 'Inversión Inicial'),
                        'cols': [('Concepto', 'A', 'txt'), ('Importe', 'B', 'eur')],
                        'filas': (22, 26),
                        'ancla': ('A22', 'CAPEX sin fondo'),
                        'nota': 'La inversión total es la cifra que se le enseña al banco. El IVA que '
                                'se adelanta al comprar el equipo y pagar la obra no está aquí: es caja '
                                'que se recupera.',
                    },
                    {
                        'titulo': 'El resultado de los tres años en tres líneas (plan-financiero-3-anos-churreria.xlsx, hoja «PyG 3 Años»)',
                        'src': (X_PLAN, 'PyG 3 Años'),
                        'cols': [('Concepto', 'A', 'txt'), ('Año 1, con rampa', 'B', 'eur'),
                                 ('Año 2, crucero', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                        'filas': (15, 24),
                        'omitir_filas': (16, 17, 18, 19, 20, 21),
                        'anclas': [('A15', 'CONTRIBUCIÓN DEL AÑO'), ('A22', 'TOTAL COSTES FIJOS'),
                                   ('A23', 'RESULTADO ANTES DE IMPUESTOS')],
                        'nota': 'Resultado antes de impuestos: el impuesto de sociedades o el IRPF '
                                'dependen de la forma jurídica. El año 2 es el de crucero, la '
                                'referencia de todo el plan.',
                    },
                    {
                        'titulo': 'El punto de equilibrio en raciones (plan-financiero-3-anos-churreria.xlsx, hoja «Punto de Equilibrio»)',
                        'src': (X_PLAN, 'Punto de Equilibrio'),
                        'cols': [('Concepto', 'A', 'txt'), ('Raciones', 'B', 'num')],
                        'filas': (11, 19),
                        'omitir_filas': (15, 16, 17, 18),
                        'anclas': [('A11', 'Raciones al año que pagan los fijos'),
                                   ('A12', 'PUNTO DE EQUILIBRIO'),
                                   ('A19', 'Punto de equilibrio de caja')],
                        'nota': 'El de caja no cuenta la amortización: dice cuántas raciones hacen '
                                'falta para no perder caja aunque contablemente se pierda.',
                    },
                    {
                        'titulo': 'Los dos canales de la carta de invierno (plan-financiero-3-anos-churreria.xlsx, hoja «Canales y Punto Muerto»)',
                        'src': (X_PLAN, 'Canales y Punto Muerto'),
                        'cols': [('Canal', 'A', 'txt'), ('Parte de las raciones', 'B', 'pct0'),
                                 ('Raciones del año', 'C', 'num'),
                                 ('Ticket sin IVA', 'D', 'eur2'),
                                 ('Materia por ración', 'E', 'eur2'),
                                 ('Contribución por ración', 'F', 'eur2'),
                                 ('Contribución del año', 'G', 'eur')],
                        'filas': (6, 8),
                        'ancla': ('A6', 'Sala'),
                        'nota': 'Carta de invierno del año de crucero; julio y agosto van aparte, con '
                                'la salida del verano que elige el plan.',
                    },
                    {
                        'titulo': 'La plantilla y el coste de cada puesto (turnos-plantilla-y-madrugada.xlsx, hoja «Coste de Plantilla»)',
                        'src': (X_TURNOS, 'Coste de Plantilla'),
                        'cols': [('Puesto', 'B', 'txt'), ('Jornada (1 = completa)', 'C', 'num1'),
                                 ('Nivel del convenio de ejemplo', 'D', 'txt'),
                                 ('Coste anual del puesto', 'Q', 'eur')],
                        'filas': (9, 13),
                        'ancla': ('B9', 'Titular'),
                        'nota': 'Convenio de hostelería de Madrid como ejemplo: vencido el 31-12-2025 y '
                                'en negociación, con las tablas salariales de ese año. El salario mínimo es el suelo '
                                'de cada puesto. El coste anual de plantilla suma además el refuerzo y '
                                'las sustituciones.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO llamar «resultado neto» o «beneficio neto» al '
                    'resultado antes de impuestos.',
                    'PROHIBIDO dar un tamaño de mercado de churrerías o un '
                    'número de churrerías en España: no existe con fuente.',
                    'PROHIBIDO presentar a El Molinete como un negocio real o '
                    'sus cifras como una previsión del lector.',
                ],
            },
            {
                'n': 2,
                'titulo': 'Plan Financiero a Tres Años, Tesorería y Riesgos',
                'resumen_indice': 'la cuenta de resultados a tres años, el punto de equilibrio mes a mes, la tesorería y su valle, la financiación y los riesgos con su cifra.',
                'palabras': 1750, 'bloques': 1,
                'objetivo': 'Que quien lee el plan vea los tres años, sepa en '
                            'qué meses el negocio no paga sus fijos, cuánto '
                            'baja la caja el primer año, si el negocio paga la '
                            'cuota del préstamo y qué riesgos tiene, cada uno '
                            'con su cifra y su respuesta.',
                'epigrafes': list(PPE_BP2),
                'puntos_por_epigrafe': PPE_BP2,
                'puntos_globales': [
                    'Registro de documento de banco: cada afirmación con su '
                    'cifra y su tabla; los veredictos, en euros.',
                    'Los escenarios de volumen se leen con el margen de '
                    'seguridad y el punto de equilibrio, no con porcentajes '
                    'inventados.',
                ],
                'cifras': [
                    C('Contribución del año de crucero', f'{X_PLAN}!PyG 3 Años!C15', 'eur', clave='Contribución del año de crucero'),
                    C('Costes fijos del año de crucero', f'{X_PLAN}!PyG 3 Años!C22', 'eur', clave='Costes fijos del año de crucero'),
                    C('Resultado antes de impuestos del año de crucero', f'{X_PLAN}!PyG 3 Años!C23', 'eur', clave='Resultado antes de impuestos del año de crucero'),
                    C('Contribución por ración del año de crucero', f'{X_PLAN}!PyG 3 Años!C30', 'eur2', clave='Contribución por ración, año de crucero'),
                    C('Punto de equilibrio en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B12', 'num', clave='Punto de equilibrio en raciones al día'),
                    C('Punto de equilibrio de caja en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B19', 'num', clave='Punto de equilibrio de caja en raciones al día'),
                    C('Margen de seguridad en raciones al día', f'{X_PLAN}!Punto de Equilibrio!B14', 'num', clave='Margen de seguridad en raciones al día'),
                    C('Meses del año de crucero que no pagan sus fijos', f'{X_PLAN}!Punto de Equilibrio!B36', 'num', clave='Meses del año de crucero que no pagan sus fijos'),
                    C('Resultado de agosto en el año de crucero', f'{X_PLAN}!Punto de Equilibrio!H30', 'eur', clave='Resultado de agosto en el año de crucero'),
                    C('Saldo de caja el día que se abre', f'{X_PLAN}!Tesorería 12 meses!B32', 'eur', clave='Saldo de caja el día que se abre'),
                    C('Valle de tesorería del primer año', f'{X_PLAN}!Tesorería 12 meses!B34', 'eur', clave='Valle de tesorería del año 1'),
                    C('Mes del valle de tesorería', f'{X_PLAN}!Tesorería 12 meses!B35', 'txt', clave='Mes del valle de tesorería'),
                    C('Saldo de caja al cierre del primer año', f'{X_PLAN}!Tesorería 12 meses!M29', 'eur', clave='Saldo de caja al cierre del año 1'),
                    C('Tipo de interés nominal anual del préstamo (supuesto)', f'{X_PLAN}!0. Supuestos!B60', 'pct1', clave='Tipo de interés nominal anual'),
                    C('Plazo del préstamo en meses', f'{X_PLAN}!0. Supuestos!B61', 'num', clave='Plazo del préstamo en meses'),
                    C('Carencia del préstamo en meses', f'{X_PLAN}!0. Supuestos!B62', 'num', clave='Carencia del préstamo en meses'),
                    C('Cuota mensual del préstamo', f'{X_PLAN}!Financiación!B24', 'eur', clave='Cuota mensual del préstamo'),
                    C('Lo que sobra en el peor año del préstamo, después de pagar al banco', f'{X_PLAN}!Financiación!B124', 'eur', clave='Lo que sobra en el peor año del préstamo'),
                    C('Ratio de cobertura de la deuda más bajo (información para el banco)', f'{X_PLAN}!Financiación!B127', 'num2', clave='DSCR más bajo'),
                    C('Raciones al día que hacen falta sólo para pagar a las personas', f'{X_PLAN}!Personal!B13', 'num', clave='Raciones al día sólo para pagar a las personas'),
                    C('Lo que deja la carta de verano frente a cerrar en julio y agosto', f'{X_PLAN}!Escenarios!B26', 'eur', clave='Lo que deja la salida elegida frente a cerrar'),
                    C('Resultado de julio y agosto con los fijos dentro, con la carta de verano', f'{X_PLAN}!Escenarios!D23', 'eur', clave='Verano con fijos con la carta de verano'),
                    C('Margen que se pierde al año con la subida más alta del aceite del libro', f'{X_ACEITE}!Escenarios de Precio del Aceite!J10', 'eur', clave='Margen que pierdes al año con el aceite un 30 % más caro'),
                    C('Resultado del mismo local vendiendo sólo para llevar, con los mismos fijos', f'{X_PLAN}!Escenarios!C39', 'eur', clave='Resultado del mismo local sólo como despacho'),
                ],
                'sector': ['CUN-39', 'CUN-V01', 'CHN-75'],
                'tablas': [
                    {
                        'titulo': 'La cuenta de resultados a tres años (plan-financiero-3-anos-churreria.xlsx, hoja «PyG 3 Años»)',
                        'src': (X_PLAN, 'PyG 3 Años'),
                        'cols': [('Concepto', 'A', 'txt'), ('Año 1, con rampa', 'B', 'eur'),
                                 ('Año 2, crucero', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                        'filas': (9, 24),
                        'ancla': ('A9', 'Ventas sin IVA de la carta de invierno'),
                        'nota': 'Todo sin IVA. Resultado antes de impuestos.',
                    },
                    {
                        'titulo': 'Los gastos fijos del mes, sin renta ni plantilla (plan-financiero-3-anos-churreria.xlsx, hoja «0. Supuestos»)',
                        'src': (X_PLAN, '0. Supuestos'),
                        'cols': [('Gasto fijo', 'A', 'txt'), ('Euros al mes, sin IVA', 'B', 'eur')],
                        'filas': (68, 83),
                        'anclas': [('A68', 'Suministros: gas de la freidora'),
                                   ('A83', 'TOTAL GASTOS FIJOS DEL MES')],
                        'nota': 'Supuestos declarados de El Molinete: cámbialos por tus presupuestos. '
                                'La renta llega de la calculadora de inversión y la plantilla del libro '
                                'de turnos.',
                    },
                    {
                        'titulo': 'El año de crucero mes a mes (plan-financiero-3-anos-churreria.xlsx, hoja «Punto de Equilibrio»)',
                        'src': (X_PLAN, 'Punto de Equilibrio'),
                        'cols': [('Mes', 'A', 'txt'), ('Raciones al día', 'E', 'num'),
                                 ('Contribución del mes', 'F', 'eur'),
                                 ('Fijos del mes', 'G', 'eur'),
                                 ('Resultado del mes', 'H', 'eur'),
                                 ('¿Paga sus fijos?', 'I', 'txt')],
                        'filas': (23, 35),
                        'ancla': ('A23', 'Enero'),
                        'nota': 'Los meses que no pagan sus fijos los pagan los meses buenos.',
                    },
                    {
                        'titulo': 'La caja del primer año: el día que se abre y el valle (plan-financiero-3-anos-churreria.xlsx, hoja «Tesorería 12 meses»)',
                        'src': (X_PLAN, 'Tesorería 12 meses'),
                        'cols': [('Concepto', 'A', 'txt'), ('Importe o lectura', 'B', 'eur')],
                        'filas': (32, 37),
                        'ancla': ('A32', 'Saldo el día que abres'),
                        'nota': 'El fondo de maniobra es el colchón con el que se abre; el valle dice '
                                'cuánto de él se come el arranque.',
                    },
                    {
                        'titulo': 'El préstamo año a año: ¿genera el negocio la cuota? (plan-financiero-3-anos-churreria.xlsx, hoja «Financiación»)',
                        'src': (X_PLAN, 'Financiación'),
                        'cols': [('Año', 'A', 'num'), ('Intereses', 'B', 'eur'),
                                 ('Devolución de principal', 'C', 'eur'),
                                 ('Servicio de la deuda', 'D', 'eur'),
                                 ('Caja antes de la deuda', 'E', 'eur'),
                                 ('Lo que sobra tras pagar al banco', 'F', 'eur'),
                                 ('Ratio de cobertura', 'G', 'num2')],
                        'filas': (117, 123),
                        'anclas': [('A116', 'Año'), ('B116', 'Intereses'), ('G116', 'DSCR')],
                        'nota': 'El año de la carencia sale holgado porque casi no se devuelve '
                                'principal. El ratio de cobertura es la caja antes de la deuda entre la '
                                'cuota: información para el banco, no veredicto.',
                    },
                    {
                        'titulo': 'El verano con los fijos dentro (plan-financiero-3-anos-churreria.xlsx, hoja «Escenarios»)',
                        'src': (X_PLAN, 'Escenarios'),
                        'cols': [('Salida del verano', 'A', 'txt'),
                                 ('Contribución de julio y agosto', 'B', 'eur'),
                                 ('Fijos de esos dos meses', 'C', 'eur'),
                                 ('Resultado con fijos', 'D', 'eur')],
                        'filas': (22, 26),
                        'ancla': ('A22', 'Cerrar en julio y agosto'),
                        'nota': 'Un verano con resultado negativo es lo normal en una churrería: lo que '
                                'importa es cuál de las tres salidas pierde menos.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO llamar «resultado neto» al resultado antes de '
                    'impuestos, o calcular un impuesto.',
                    'PROHIBIDO dar escenarios de volumen con porcentajes o '
                    'resultados que no estén en las cifras: el riesgo de volumen '
                    'se lee con el margen de seguridad y el punto de equilibrio.',
                    'PROHIBIDO presentar el tipo de interés del plan como una '
                    'oferta de banco: es un supuesto.',
                ],
            },
        ],
    },
]


# ==========================================================================
# BONUS 2 — 12 decisiones de apertura resueltas (D26: 3 bloques de 4, orden
# de la SPEC §4.3). Un capítulo por bloque, un epígrafe por decisión y seis
# puntos por decisión, siempre en el mismo orden: contexto · opciones ·
# criterio (sin repetir el capítulo) · el veredicto de El Molinete con su
# cifra y su hoja · el umbral para elegir lo contrario · la norma con su
# fecha, o «no hay norma». Una tabla por decisión.
# ==========================================================================
PG_DEC = [
    'Cada decisión se cierra con el veredicto de El Molinete y con el umbral '
    'que la haría cambiar. Un bonus de decisiones que no decide no sirve '
    'para nada.',
    'La hoja que resuelve la decisión se nombra en lenguaje de libro —el '
    'libro y la hoja—, nunca con la sintaxis de Excel.',
    'Cuando no hay norma que aplique, se dice que no la hay en vez de '
    'rellenar con normativa de adorno; cuando la hay, con su fecha de '
    'comprobación.',
    'No repitas la explicación del capítulo de origen: da el caso, la '
    'decisión, la cifra y la hoja, y remite al capítulo en una frase.',
]


def DEC(contexto, opciones, criterio, veredicto, umbral, norma):
    """Los seis puntos de una decisión, en el orden fijo del bonus 2."""
    return [contexto, opciones, criterio, veredicto, umbral, norma]


PPE_DEC1 = {
    'Decisión 1. Sala o sólo despacho para llevar': DEC(
        'El contexto: un despacho a calle es más barato de montar y de '
        'tramitar; una sala con barra y terraza vende más ticket y más rato. '
        'La pregunta es si el mismo barrio paga los fijos sin sala.',
        'Las opciones: A, local con sala, barra y terraza, con despacho a '
        'calle; B, sólo despacho para llevar, en menos metros y con menos '
        'dotación.',
        'El criterio: se decide por la contribución que deja cada formato '
        'frente a sus fijos, no por lo que cuesta abrir. El despacho ahorra '
        'dotación, pero pierde las raciones que se consumen en el local; y la '
        'sala cambia el régimen de apertura (capítulo 4).',
        'El veredicto de El Molinete, con sala: la diferencia de dotación del '
        'despacho frente al local con sala (calculadora de inversión) y el '
        'resultado del mismo local vendiendo sólo para llevar con los mismos '
        'fijos (plan financiero, hoja «Escenarios»).',
        'El umbral: elegirías el despacho si consigues unos fijos mucho más '
        'bajos —menos renta y menos plantilla—; el libro da el ahorro de fijos '
        'al año que necesitaría para no perder dinero.',
        'La norma: la actividad del despacho va por declaración responsable '
        'cuando está en el Anexo de la Ley 12/2012, pero las obras que '
        'requieren proyecto, el conducto a cubierta incluido, siguen '
        'necesitando licencia de obra y técnico (arts. 3.3 y 3.4); con mesas, '
        'el régimen general de tu ayuntamiento (CUN-35, comprobado el 3 de '
        'octubre de 2026).'),
    'Decisión 2. Traspaso u obra nueva': DEC(
        'El contexto: un traspaso con la churrería en marcha parece un atajo, '
        'con clientela, licencia y máquinas. Pero el precio de un traspaso es '
        'lo que te piden, no lo que se paga, y la comparación sólo vale con la '
        'misma base y en el mismo horizonte.',
        'Las opciones: A, el traspaso, al precio pedido más la adaptación que '
        'aún haría falta; B, obra nueva, con la inversión comparable de obra, '
        'extracción, maquinaria, barra, control, TPV y licencias.',
        'El criterio: dos comparaciones, la inversión y el coste en el '
        'horizonte, con la renta y los meses pagando renta sin facturar, que '
        'en un traspaso en marcha son menos. Lo que el dinero no ve —la '
        'clientela, la distribución, el estado del conducto— se apunta aparte.',
        'El veredicto de El Molinete: el de la inversión y el del horizonte '
        'frente al traspaso de referencia, el anuncio con sala de Vallecas con '
        'su precio pedido y negociable (CUS-02), y el precio por debajo del '
        'cual ganaría el traspaso, que es la cifra a la que hay que negociar '
        '(calculadora de inversión, hoja «Traspaso vs Obra Nueva»).',
        'El umbral: elegirías el traspaso si lo cierras por debajo de esa '
        'cifra, o si el local trae resuelto lo que más cuesta y más tarda, la '
        'extracción a cubierta con su licencia.',
        'La norma: no hay norma que decida esto. Sí hay una comprobación: que '
        'la licencia del local que traspasas cubra tu actividad y tu '
        'extracción; si no, la obra con proyecto vuelve a ser tuya (capítulo '
        '4).'),
    'Decisión 3. Equipo completo de churros o línea separada': DEC(
        'El contexto: hay equipos completos de churros —dosificador y sartén '
        'en un solo aparato— por mucho menos que una línea de dosificadora, '
        'freidora y amasadora por separado, y la tentación es empezar barato y '
        'ampliar después.',
        'Las opciones: A, el equipo completo, con su precio de ficha; B, la '
        'línea separada de El Molinete, con dosificadora automática, freidora '
        'de una cuba y amasadora.',
        'El criterio: se decide por la hora punta del domingo, no por el total '
        'del día. La capacidad se mide en kilos de masa por hora y la manda el '
        'eslabón más lento; si el equipo no aguanta la hora punta de tus meses '
        'fuertes, lo barato sale caro en cola.',
        'El veredicto de El Molinete, línea separada: el precio de ficha del '
        'equipo completo, la capacidad de su línea en raciones por hora, el '
        'eslabón que la manda y la hora punta de un día punta de diciembre '
        'frente a esa capacidad (libro de temporada, hoja «Capacidad contra el '
        'Pico»).',
        'El umbral: elegirías el equipo completo en un despacho de barrio o en '
        'una caseta con poca hora punta, o para empezar mientras validas la '
        'demanda. Y un déficit de diciembre no se arregla con una segunda '
        'churrera, sino con masa preparada antes de abrir y una persona más.',
        'La norma: no hay norma que elija la máquina. Sí la hay para lo que va '
        'bajo la campana: los litros de la freidora cuentan en la potencia que '
        'decide el riesgo de incendio (capítulo 5).'),
    'Decisión 4. Freidora de gas o eléctrica': DEC(
        'El contexto: la freidora de gas es la de casi todas las churrerías y '
        'la eléctrica cuesta algo más de ficha, pero la decisión no es de '
        'precio: decide si llevas el gas al local y cuánta potencia computa tu '
        'cocina.',
        'Las opciones: A, gas, con instalación receptora, certificado del '
        'instalador e inspección periódica; B, freidora eléctrica, con la '
        'potencia contratada que necesite. Lo que no es una opción en un '
        'local: la bombona.',
        'El criterio: los litros de cuba computan como potencia, y la potencia '
        'de la cocina decide si es local de riesgo especial y si la extinción '
        'automática es obligatoria. Con extinción automática deja de ser local '
        'de riesgo especial, pero sigue sujeta a la nota 3: campana, conductos '
        'y filtros.',
        'El veredicto de El Molinete, gas: los kW computables de su cocina, su '
        'riesgo y si la extinción automática es obligatoria (libro de '
        'producción); el precio de ficha de la freidora eléctrica de '
        'referencia frente a la de gas, y lo que costaría la extinción '
        'automática si le tocara (calculadora de inversión).',
        'El umbral: elegirías la eléctrica si el local no tiene gas o llevarlo '
        'es una obra que no compensa; y con una segunda freidora, mira cómo '
        'sube la potencia antes de comprar, porque puede cambiarte de riesgo.',
        'La norma: CTE DB-SI, tabla 2.1 y sus notas 2 y 3, y la instalación '
        'receptora de gas con su inspección periódica (RD 919/2006). La '
        'bombona única de menos de quince kilos sólo libra a un aparato de '
        'utilización móvil, en la feria (capítulo 14). Comprobado el 3 de '
        'octubre de 2026.'),
}

PPE_DEC2 = {
    'Decisión 5. Preparado comercial o mezcla propia': DEC(
        'El contexto: el preparado para masa de churros es cómodo y regular; '
        'la harina especial con sal y agua es más barata por kilo de masa. La '
        'diferencia parece pequeña por kilo y se nota al año.',
        'Las opciones: A, el preparado comercial, con lo que declara el '
        'vendedor que rinde cada saco; B, mezcla propia con harina especial '
        'para churros, sal y agua, con proporciones de ejemplo que no son una '
        'receta.',
        'El criterio: el ahorro por kilo de masa por los kilos del año, frente '
        'a lo que cuesta la regularidad: el tiempo de quien mezcla y las '
        'tandas que salen mal. Y la etiqueta: con el preparado, los alérgenos '
        'los declara el fabricante; con la mezcla propia, los declaras tú.',
        'El veredicto de El Molinete, preparado comercial: el coste de un kilo '
        'de masa con el preparado y con la mezcla propia, y el ahorro por kilo '
        '(libro de la carta, hoja «Escandallo por kg de Masa»).',
        'El umbral: elegirías la mezcla propia con un churrero con oficio que '
        'la haga igual todos los días y con mucha masa al año; con rotación de '
        'personal, el preparado.',
        'La norma: no hay norma que elija la masa. Sí la hay para lo que '
        'declaras: los alérgenos, por escrito, de tu masa y de cada producto '
        'que compras (RD 126/2015, capítulo 11).'),
    'Decisión 6. Qué preparado compras para la taza y qué dice su etiqueta': DEC(
        'El contexto: el chocolate a la taza de una churrería sale casi '
        'siempre de un preparado en polvo y leche, y lo que pone la carta '
        'depende de lo que dice la etiqueta de ese preparado, no del gusto ni '
        'de la costumbre.',
        'Las opciones: A, un preparado cuya etiqueta dice «chocolate a la '
        'taza», con el cacao seco total que declara; B, un preparado con otra '
        'denominación o con grasa vegetal distinta de la manteca de cacao.',
        'El criterio: la carta repite la denominación de la etiqueta. Si el '
        'cacao seco total está por debajo del mínimo del producto o la '
        'etiqueta declara grasa vegetal, el libro avisa: consulta a tu '
        'servicio de consumo antes de imprimir la carta. Y el coste por taza '
        'sale del formato que compras y de lo que rinde.',
        'El veredicto de El Molinete: el cacao seco total de su preparado '
        'frente al mínimo, el aviso del libro y el coste de una taza (libro de '
        'la carta, hoja «Chocolate a la Taza»).',
        'El umbral: cambiarías de preparado si su etiqueta dice otra cosa o '
        'declara grasa vegetal y quieres seguir llamándolo «chocolate a la '
        'taza»: primero la etiqueta, después el precio.',
        'La norma: el RD 1055/2003 define el producto, no la bebida servida, y '
        'de ningún artículo sale que no puedas escribir «chocolate» en la '
        'carta con un preparado que no cumpla: es una interpretación y se '
        'consulta (CUN-42, CUN-V06; comprobado el 3 de octubre de 2026).'),
    'Decisión 7. Ración, docena o kilo: qué formato empujas': DEC(
        'El contexto: la misma masa se vende en ración, media ración, docena, '
        'suelta o al kilo, y cada formato deja distinto por kilo de masa. La '
        'carta suele heredar los formatos de la competencia sin mirar cuál '
        'paga.',
        'Las opciones: A, empujar la ración y la media ración en sala; B, '
        'empujar la docena y el kilo para llevar, el pedido grande del '
        'domingo; C, revisar el precio del formato que menos deja.',
        'El criterio: los euros sin IVA que deja cada kilo de masa y la '
        'rotación. El libro marca un margen mínimo por unidad y una rotación '
        'mínima, criterio de la casa, para mantener, revisar el precio, '
        'vigilar o retirar cada referencia.',
        'El veredicto de El Molinete: lo que deja por kilo de masa la ración, '
        'la docena y el kilo, con su margen mínimo por unidad y su rotación '
        'mínima, y el veredicto de cada formato de churro y porra (libro de la '
        'carta, hojas «Ración, Docena o Kilo» y «Decisión de Surtido»).',
        'El umbral: empujarías el kilo si tu cola del domingo es de pedidos '
        'grandes para llevar y a tu línea le sobra capacidad; si no, cada kilo '
        'ocupa la línea con lo que menos deja.',
        'La norma: no hay norma que decida el formato. Sí la hay para cómo lo '
        'cobras: el vaso de plástico para llevar se cobra aparte, en su propia '
        'línea del tique (Ley 7/2022, CUN-41; comprobado el 3 de octubre de '
        '2026).'),
    'Decisión 8. Abrir antes de las 8:00': DEC(
        'El contexto: el desayuno es la franja que más raciones se lleva en una '
        'churrería, y en el ejemplo de Madrid una chocolatería no puede abrir '
        'antes de las 8:00, mientras que una cafetería o un bar sí puede '
        'hacerlo desde las 6:00. La hora a la que abres decide cómo te '
        'clasificas.',
        'Las opciones: A, abrir a las 6:00 o a las 7:00 clasificado como '
        'cafetería o bar; B, abrir a las 8:00 como chocolatería y renunciar a '
        'la primera hora del desayuno.',
        'El criterio: las raciones que se lleva el desayuno y la norma de '
        'horarios de TU comunidad, no la de Madrid, que es un ejemplo y no se '
        'extrapola. La clasificación horaria es una cosa y el epígrafe del '
        'impuesto, otra (capítulo 9).',
        'El veredicto de El Molinete: la parte de las raciones de la semana '
        'que se lleva el desayuno, la hora de apertura del sábado y los días '
        'que abre antes de la hora mínima de chocolatería (libro de temporada, '
        'hoja «Franjas del Día»), con lo que eso significa en el ejemplo de '
        'Madrid (libro legal).',
        'El umbral: abrirías a las 8:00 si tu barrio no desayuna churros —una '
        'zona de oficinas o de paso de tarde— o si tu comunidad no permite '
        'antes la clasificación que necesitas.',
        'La norma: Orden de 21 de abril de 2022 de la Comunidad de Madrid, con '
        'cafeterías y bares desde las 6:00 y chocolaterías desde las 8:00; es '
        'el ejemplo de Madrid y no se extrapola (CUN-34; comprobado el 3 de '
        'octubre de 2026). Pregunta la de tu comunidad.'),
}

PPE_DEC3 = {
    'Decisión 9. El verano: cerrar, carta de verano o ferias': DEC(
        'El contexto: julio y agosto son el valle de una churrería y la '
        'tentación es cerrar y descansar. Pero los fijos de esos dos meses se '
        'pagan igual, y la pregunta es qué salida deja más contribución para '
        'pagarlos.',
        'Las opciones: A, cerrar; B, abrir con carta de verano, con '
        'granizados, horchata, helado y algo de churro; C, cerrar el local y '
        'salir de ferias.',
        'El criterio: se comparan por la contribución de julio y agosto —las '
        'ventas sin IVA menos la materia y el personal extra, más lo que dejan '
        'las ferias—, porque los fijos son los mismos en las tres. La '
        'fiscalidad no es una salida.',
        'El veredicto de El Molinete, carta de verano: la contribución con '
        'carta de verano y saliendo de ferias, y el resultado de julio y '
        'agosto con los fijos dentro (libro de temporada, hoja «El Verano '
        '(Tres Salidas)», y plan financiero, hoja «Escenarios»).',
        'El umbral: elegirías las ferias si tu local vendiera en verano menos '
        'raciones al día que el umbral del libro; y cerrarías sólo si ni la '
        'carta de verano ni las ferias dejan contribución.',
        'La norma: si sales de ferias, la caseta tiene su autorización '
        'municipal, su alta y su registro (Ley 7/1996, arts. 53 a 55, y '
        'capítulo 14; comprobado el 3 de octubre de 2026).'),
    'Decisión 10. Cuánta madrugada asumes tú': DEC(
        'El contexto: el titular de una churrería suele ser el primero en '
        'llegar y el último en irse, y un plan que sólo cuadra con sus horas '
        'gratis no aguanta un año. La madrugada del fin de semana es la parte '
        'más dura.',
        'Las opciones: A, el titular abre la madrugada del fin de semana; B, '
        'la abre un churrero, con su plus de convenio, y el titular entra '
        'después; C, un relevo para que el titular descanse un día.',
        'El criterio: las horas del titular a la semana, sus horas de '
        'madrugada y lo que valdrían al año sus horas de más al coste hora de '
        'la plantilla. El titular autónomo no cobra plus ni es trabajador '
        'nocturno; el churrero que abre la madrugada cobra plus sin ser, por '
        'eso, trabajador nocturno (capítulo 13).',
        'El veredicto de El Molinete: el titular asume la madrugada del fin de '
        'semana desde las 6:00; sus horas a la semana, sus horas de madrugada, '
        'lo que valdrían al año sus horas de más y el veredicto del libro de '
        'turnos (hoja «Horas del Titular»).',
        'El umbral: contratarías el relevo cuando lo que valen tus horas de más '
        'al año se acerque al coste de un refuerzo, o antes si el veredicto '
        'dice que trabajas los siete días.',
        'La norma: el Estatuto de los Trabajadores, art. 36.1, para la '
        'plantilla, y el plus de nocturnidad del convenio de tu provincia; el '
        'titular autónomo queda fuera de las dos figuras (comprobado el 3 de '
        'octubre de 2026).'),
    'Decisión 11. Freidora dedicada o compartida': DEC(
        'El contexto: freír patatas, rebozados o buñuelos de otra masa en la '
        'freidora de los churros ahorra una máquina y amplía la carta, pero lo '
        'que fríes en la misma cuba pasa al resto.',
        'Las opciones: A, freidora dedicada al churro y a la porra; B, una sola '
        'freidora compartida con otros fritos; C, una segunda freidora para lo '
        'demás.',
        'El criterio: el aceite compartido es contaminación cruzada, así que '
        'tus alérgenos pasan a ser los de todo lo que fríes en esa cuba; si '
        'fríes patatas frescas, te entra la parte A del reglamento de la '
        'acrilamida; y la segunda freidora suma potencia y puede cambiarte de '
        'riesgo de incendio.',
        'El veredicto de El Molinete, dedicada: su decisión y su consecuencia '
        '(libro legal, hoja «Alérgenos y Aceite Compartido»), con la parte A '
        'de la acrilamida que no le alcanza y las casillas de alérgenos que '
        'aún tiene que leer en la etiqueta; y la potencia de su cocina con una '
        'sola freidora (libro de producción).',
        'El umbral: compartirías la freidora sólo con productos de la misma '
        'masa y sin alérgenos nuevos; para patatas o rebozados, segunda '
        'freidora, con su potencia en el cálculo del riesgo.',
        'La norma: Reglamento (CE) 852/2004, anexo II, capítulo IX, para el '
        'equipo que ha tocado un alérgeno; RD 126/2015, alérgenos por escrito; '
        'y Reglamento (UE) 2017/2158, anexo II, parte A, si fríes patatas '
        'frescas (comprobado el 3 de octubre de 2026).'),
    'Decisión 12. Franquicia o por tu cuenta': DEC(
        'El contexto: una franquicia de churros o de chocolate vende marca, '
        'método y proveedor, y publica una inversión que parece cerrada. Lo '
        'que no publica es lo que pagas cada mes ni lo que incluye de verdad.',
        'Las opciones: A, una enseña de base comparable, con su canon, su '
        'royalty y su publicidad; B, por tu cuenta, con tu inversión y tu '
        'marca.',
        'El criterio: con la misma base, tu inversión de apertura sin fondo de '
        'maniobra frente a las enseñas que publican local en bruto con obra, '
        'maquinaria y mobiliario; y el royalty pasado por el plan mes a mes, '
        'también en julio y agosto (capítulo 15).',
        'El veredicto de El Molinete, por su cuenta: su inversión total, el '
        'abanico publicado y cuántas enseñas de base comparable quedan por '
        'debajo de su inversión de apertura (calculadora de inversión, hoja '
        '«Franquicia o Independiente»).',
        'El umbral: elegirías la franquicia si no tienes oficio de churrero ni '
        'proveedor y tu plan aguanta el royalty en el peor mes, o si la enseña '
        'te da una ubicación que solo no conseguirías.',
        'La norma: si la enseña te suministra la masa de forma centralizada y '
        'operas bajo su marca, te alcanza la parte B del anexo II de la '
        'acrilamida (Reglamento (UE) 2017/2158, art. 2.3; comprobado el 3 de '
        'octubre de 2026).'),
}

BONUS += [
    {
        'nombre': 'BONUS-12-decisiones-de-apertura',
        'guia': {
            'titulo': '12 Decisiones de Apertura Resueltas',
            'subtitulo': 'Bonus del pack «Cómo Montar una Churrería-Chocolatería» · con '
                         'los datos de las ocho herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Decisiones de Apertura Resueltas',
            'tipo_doc': 'bonus',
            'tipo_doc_art': 'del bonus',
            'tipo_doc_dem': 'este bonus',
            'categoria_doc': 'Guía profesional',
            'portada_texto': (
                'Doce decisiones que hay que tomar antes de abrir una '
                'churrería-chocolatería: sala o despacho, traspaso u obra '
                'nueva, equipo completo o línea, gas o eléctrica, preparado o '
                'mezcla propia, qué dice la etiqueta de tu chocolate, qué '
                'formato empujas, a qué hora abres, qué haces en verano, '
                'cuánta madrugada asumes, si compartes la freidora y si '
                'franquicias. Cada una con su contexto, sus opciones, el '
                'criterio, el veredicto de El Molinete con su cifra, el umbral '
                'a partir del cual elegirías lo contrario y la norma cuando la '
                'hay. Ninguna cifra inventada: cada número sale de una celda '
                'que puedes abrir y comprobar.'),
        },
        'gates': {
            'paginas_prometidas': 20,
            'palabras_objetivo': 6600,
            'min_palabras_cap': 400,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': (),
            'meta': {'title': '12 Decisiones de Apertura Resueltas',
                     'subject': 'Bonus del pack Cómo Montar una Churrería-Chocolatería · '
                                'Versión 1.0 · octubre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Decisiones del Local y de la Línea',
                'resumen_indice': 'sala o despacho, traspaso u obra nueva, equipo completo o línea separada, y freidora de gas o eléctrica.',
                'palabras': 2200, 'bloques': 1,
                'objetivo': 'Resolver las cuatro decisiones que fijan el local '
                            'y la línea antes de firmar nada, cada una con el '
                            'veredicto de El Molinete y el umbral que lo '
                            'cambiaría.',
                'epigrafes': list(PPE_DEC1),
                'puntos_por_epigrafe': PPE_DEC1,
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Decisión 1 · Diferencia de dotación del despacho frente al local con sala', f'{X_CAPEX}!Variante del Formato!D7', 'eur', clave='Diferencia de dotación del despacho frente al local con sala'),
                    C('Decisión 1 · Resultado del mismo local vendiendo sólo para llevar, con los mismos fijos', f'{X_PLAN}!Escenarios!C39', 'eur', clave='Resultado del mismo local sólo como despacho'),
                    C('Decisión 1 · Ahorro de fijos al año que necesitaría el despacho para no perder dinero', f'{X_PLAN}!Escenarios!C41', 'eur', clave='Ahorro de fijos que necesitaría el despacho para no perder'),
                    C('Decisión 2 · Inversión del traspaso: precio pedido más adaptación', f'{X_CAPEX}!Traspaso vs Obra Nueva!B16', 'eur', clave='Inversión del traspaso (precio más adaptación)'),
                    C('Decisión 2 · Precio de traspaso por debajo del cual gana el traspaso', f'{X_CAPEX}!Traspaso vs Obra Nueva!B18', 'eur', clave='Precio de traspaso por debajo del cual gana el traspaso'),
                    C('Decisión 2 · Veredicto de la inversión', f'{X_CAPEX}!Traspaso vs Obra Nueva!B19', 'txt', clave='Veredicto de la inversión: traspaso u obra nueva'),
                    C('Decisión 2 · Veredicto en el horizonte, con la renta', f'{X_CAPEX}!Traspaso vs Obra Nueva!B24', 'txt', clave='Veredicto en el horizonte'),
                    C('Decisión 3 · Precio de ficha del equipo completo de churros, sin IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!I15', 'eur', rotulo=('C15', 'Equipo completo de churros')),
                    C('Decisión 3 · Capacidad de la línea separada en raciones por hora', f'{X_PROD}!Cuello de Botella!L5', 'num', clave='Capacidad del conjunto en raciones por hora'),
                    C('Decisión 3 · Eslabón que manda en la línea', f'{X_PROD}!Cuello de Botella!B7', 'txt', clave='Eslabón que manda'),
                    C('Decisión 3 · Hora punta de un día punta de diciembre, en raciones por hora', f'{X_TEMP}!Capacidad contra el Pico!F18', 'num1', clave='Hora punta de un día punta de diciembre (raciones/h)'),
                    C('Decisión 4 · kW computables de la cocina de El Molinete', f'{X_PROD}!Freidoras, Potencia y Riesgo!D12', 'num', clave='kW computables de la cocina'),
                    C('Decisión 4 · Riesgo de la cocina', f'{X_PROD}!Freidoras, Potencia y Riesgo!D13', 'txt', clave='Riesgo de la cocina'),
                    C('Decisión 4 · ¿Extinción automática obligatoria?', f'{X_PROD}!Freidoras, Potencia y Riesgo!D15', 'txt', clave='¿Extinción automática obligatoria?'),
                    C('Decisión 4 · Precio de ficha de la freidora eléctrica de referencia, sin IVA', f'{X_CAPEX}!Equipamiento Línea a Línea!R19', 'eur', clave='Freidora eléctrica de 25 L, referencia sin IVA'),
                    C('Decisión 4 · Importe de la extinción automática si te toca', f'{X_CAPEX}!CAPEX por Bloque!H9', 'eur', clave='Importe de la extinción automática si te toca'),
                ],
                'sector': ['CUN-35', 'CUS-02', 'CUS-32a', 'CUS-33a', 'CUS-33b',
                           'CUS-34c', 'CUS-35a', 'CUN-26', 'CUN-28', 'CHN-48'],
                'tablas': [
                    {
                        'titulo': 'Decisión 1 · El mismo local con sala o sólo para llevar (plan-financiero-3-anos-churreria.xlsx, hoja «Escenarios»)',
                        'src': (X_PLAN, 'Escenarios'),
                        'cols': [('Métrica', 'A', 'txt'), ('Local con sala', 'B', 'eur'),
                                 ('Sólo despacho para llevar', 'C', 'eur')],
                        'filas': (33, 41),
                        'anclas': [('A33', 'Contribución de la carta de invierno'),
                                   ('B30', 'Local con sala'), ('C30', 'Sólo despacho'),
                                   ('A39', 'RESULTADO ANTES DE IMPUESTOS')],
                        'nota': 'El despacho de esta hoja es el MISMO local vendiendo sólo para '
                                'llevar, con los mismos fijos: un despacho más pequeño necesitaría el '
                                'ahorro de fijos de la última fila.',
                    },
                    {
                        'titulo': 'Decisión 2 · Traspaso u obra nueva (calculadora-capex-churreria.xlsx, hoja «Traspaso vs Obra Nueva»)',
                        'src': (X_CAPEX, 'Traspaso vs Obra Nueva'),
                        'cols': [('Concepto', 'A', 'txt'), ('Importe o veredicto', 'B', 'eur')],
                        'filas': (16, 24),
                        'ancla': ('A16', 'Traspaso: precio pedido más adaptación'),
                        'nota': 'El precio de un traspaso es lo que te piden, no lo que se paga. La '
                                'comparación en el horizonte suma la renta y los meses pagando renta '
                                'sin facturar.',
                    },
                    {
                        'titulo': 'Decisión 3 · La línea contra la hora punta, mes a mes (temporada-franjas-y-ferias.xlsx, hoja «Capacidad contra el Pico»)',
                        'src': (X_TEMP, 'Capacidad contra el Pico'),
                        'cols': [('Mes', 'A', 'txt'),
                                 ('Hora punta de un día punta (raciones/h)', 'F', 'num1'),
                                 ('Capacidad de la línea (raciones/h)', 'G', 'num1'),
                                 ('Déficit en un día punta (raciones/h)', 'I', 'num1'),
                                 ('¿Aguanta la línea?', 'J', 'txt')],
                        'filas': (7, 18),
                        'ancla': ('A7', 'Enero'),
                        'nota': 'Un «no» no quiere decir que no puedas abrir ese mes: quiere decir que '
                                'hace falta masa preparada antes de abrir y una persona más en el pico.',
                    },
                    {
                        'titulo': 'Decisión 4 · La freidora de gas y la eléctrica, con su precio de ficha (calculadora-capex-churreria.xlsx, hoja «Equipamiento Línea a Línea»)',
                        'src': (X_CAPEX, 'Equipamiento Línea a Línea'),
                        'cols': [('Partida', 'C', 'txt'),
                                 ('Cómo publica la fuente el precio', 'E', 'txt'),
                                 ('Precio de referencia, sin IVA', 'I', 'eur')],
                        'filas': (6, 19),
                        'omitir_filas': tuple(range(7, 19)),
                        'anclas': [('C6', 'Freidora de churros de gas'),
                                   ('C19', 'Freidora de churros eléctrica')],
                        'nota': 'Precios de ficha consultados el 3 de octubre de 2026. La eléctrica no '
                                'necesita instalación receptora de gas, pero sí la potencia contratada.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO tratar el precio de un traspaso como precio '
                    'pagado, o usar el techo de otro anuncio que no sea el de la '
                    'hoja.',
                    'PROHIBIDO presentar la bombona como alternativa al gas en '
                    'un local.',
                ],
            },
            {
                'n': 2,
                'titulo': 'Decisiones de la Carta y del Horario',
                'resumen_indice': 'preparado o mezcla propia, qué preparado compras para la taza, qué formato empujas y si abres antes de las 8:00.',
                'palabras': 2200, 'bloques': 1,
                'objetivo': 'Resolver las cuatro decisiones de la carta y del '
                            'horario, cada una con el veredicto de El Molinete '
                            'y el umbral que lo cambiaría.',
                'epigrafes': list(PPE_DEC2),
                'puntos_por_epigrafe': PPE_DEC2,
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Decisión 5 · Coste de un kilo de masa con el preparado comercial', f'{X_CARTA}!Escandallo por kg de Masa!E9', 'eur2', clave='Coste de 1 kg de masa con el preparado'),
                    C('Decisión 5 · Coste de un kilo de masa con mezcla propia', f'{X_CARTA}!Escandallo por kg de Masa!E16', 'eur2', clave='Coste de 1 kg de masa con mix propio'),
                    C('Decisión 5 · Ahorro de la mezcla propia por kilo de masa', f'{X_CARTA}!Escandallo por kg de Masa!B18', 'eur2', clave='Ahorro del mix propio por kg de masa'),
                    C('Decisión 6 · Cacao seco total que declara la etiqueta del preparado de El Molinete', f'{X_CARTA}!Chocolate a la Taza!B21', 'pct0', clave='Cacao seco total del preparado del ejemplo'),
                    C('Decisión 6 · Cacao seco total mínimo del producto «chocolate a la taza»', f'{X_CARTA}!Chocolate a la Taza!B23', 'pct0', clave='Cacao seco total mínimo del chocolate a la taza'),
                    C('Decisión 6 · Aviso del libro antes de imprimir la carta', f'{X_CARTA}!Chocolate a la Taza!B24', 'txt', clave='Aviso de la taza antes de imprimir la carta'),
                    C('Decisión 6 · Coste de una taza de chocolate, sin IVA', f'{X_CARTA}!Chocolate a la Taza!B15', 'eur2', clave='Coste de una taza de chocolate'),
                    C('Decisión 7 · Euros sin IVA que deja cada kilo de masa la ración de churros', f'{X_CARTA}!Ración, Docena o Kilo!J7', 'eur2', clave='Euros por kilo de masa de Ración de churros (6 uds)'),
                    C('Decisión 7 · Euros sin IVA que deja cada kilo de masa la docena para llevar', f'{X_CARTA}!Ración, Docena o Kilo!J12', 'eur2', clave='Euros por kilo de masa de Docena de churros para llevar'),
                    C('Decisión 7 · Euros sin IVA que deja cada kilo de masa el kilo para llevar', f'{X_CARTA}!Ración, Docena o Kilo!J13', 'eur2', clave='Euros por kilo de masa de Kilo de churros para llevar'),
                    C('Decisión 7 · Margen mínimo por unidad para no revisar el precio (criterio de la casa)', f'{X_CARTA}!Parámetros!B28', 'eur2', rotulo=('A28', 'Margen mínimo por unidad')),
                    C('Decisión 7 · Rotación mínima, en % del mix, para no vigilar una referencia (criterio de la casa)', f'{X_CARTA}!Parámetros!B29', 'num', rotulo=('A29', 'Rotación mínima')),
                    C('Decisión 8 · Parte de las raciones de la semana que se lleva el desayuno', f'{X_TEMP}!Franjas del Día!D53', 'pct0', clave='Parte de las raciones de la semana que se lleva el desayuno'),
                    C('Decisión 8 · Hora de apertura del sábado de El Molinete', f'{X_TEMP}!Franjas del Día!D11', 'num', clave='Hora de apertura del sábado'),
                    C('Decisión 8 · Días a la semana que El Molinete abre antes de la hora mínima de chocolatería', f'{X_TEMP}!Franjas del Día!E16', 'num', clave='Días que se abre antes de la hora mínima de chocolatería'),
                    C('Decisión 8 · Lo que significa su horario para el desayuno, en el ejemplo de Madrid', f'{X_LEGAL}!Régimen de Apertura y Horario!B25', 'txt', clave='Lo que significa el horario para tu desayuno'),
                ],
                'sector': ['CUS-21', 'CUS-24', 'CHN-05', 'CUN-42', 'CUN-V06',
                           'CUS-15', 'CUS-16', 'CUS-17', 'CUN-41', 'CUN-34'],
                'tablas': [
                    {
                        'titulo': 'Decisión 5 · Un kilo de masa con el preparado y con mezcla propia (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Escandallo por kg de Masa»)',
                        'src': (X_CARTA, 'Escandallo por kg de Masa'),
                        'cols': [('Concepto', 'A', 'txt'),
                                 ('Cantidad por kilo de masa', 'B', 'num2'),
                                 ('Unidad', 'C', 'txt'),
                                 ('Precio sin IVA por unidad', 'D', 'eur2'),
                                 ('Importe', 'E', 'eur2')],
                        'filas': (7, 16),
                        'omitir_filas': (10, 11, 12),
                        'anclas': [('A7', 'Preparado para masa'), ('A13', 'Harina especial'),
                                   ('A16', 'COSTE DE 1 KG DE MASA CON MIX PROPIO')],
                        'nota': 'Proporciones de EJEMPLO para que la comparación calcule, no una '
                                'receta. Todo sin IVA.',
                    },
                    {
                        'titulo': 'Decisión 6 · Lo que dice la etiqueta del preparado de la taza (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Chocolate a la Taza»)',
                        'src': (X_CARTA, 'Chocolate a la Taza'),
                        'cols': [('Concepto', 'A', 'txt'), ('El Molinete', 'B', 'pct0')],
                        'filas': (20, 25),
                        'ancla': ('A20', 'Denominación que figura en la etiqueta'),
                        'nota': 'Ante un preparado por debajo del mínimo o con grasa vegetal, consulta '
                                'a tu servicio de consumo antes de imprimir la carta: es una '
                                'interpretación, no una regla del real decreto.',
                    },
                    {
                        'titulo': 'Decisión 7 · Los formatos de churro y porra contra los umbrales de la casa (carta-de-apertura-y-escandallo-churro.xlsx, hoja «Decisión de Surtido»)',
                        'src': (X_CARTA, 'Decisión de Surtido'),
                        'cols': [('Referencia', 'A', 'txt'),
                                 ('Margen por unidad', 'E', 'eur2'),
                                 ('Margen sobre ingreso', 'F', 'pct0'),
                                 ('Mix de invierno, en %', 'G', 'num'),
                                 ('¿Margen suficiente?', 'J', 'txt'),
                                 ('¿Rotación suficiente?', 'K', 'txt'),
                                 ('Veredicto', 'L', 'txt')],
                        'filas': (7, 13),
                        'ancla': ('A7', 'CH1'),
                        'nota': 'Los umbrales son criterio de la casa, no del sector: margen en euros '
                                'por unidad y peso en el mix. La pieza suelta deja poco por unidad y '
                                'mucho por kilo de masa.',
                    },
                    {
                        'titulo': 'Decisión 8 · El fin de semana de El Molinete, franja a franja (temporada-franjas-y-ferias.xlsx, hoja «Franjas del Día»)',
                        'src': (X_TEMP, 'Franjas del Día'),
                        'cols': [('Franja', 'A', 'txt'), ('Día', 'B', 'txt'),
                                 ('Empieza (16,5 = 16:30)', 'C', 'num1'),
                                 ('Acaba (25 = la 1:00 del día siguiente)', 'D', 'num1'),
                                 ('Parte de las raciones del día', 'F', 'pct0'),
                                 ('Raciones de la franja, mes medio', 'G', 'num')],
                        'filas': (42, 49),
                        'anclas': [('A42', 'Desayuno'), ('B42', 'Sábado'), ('B49', 'Domingo')],
                        'nota': 'La hora mínima de apertura es la del ejemplo de Madrid y no se '
                                'extrapola: pon la de tu comunidad en el libro legal.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO escribir que una taza no puede llamarse '
                    '«chocolate» o «chocolate a la taza» como regla cierta: se '
                    'consulta al servicio de consumo.',
                    'PROHIBIDO extrapolar el horario de Madrid a otras '
                    'comunidades.',
                    'PROHIBIDO dar la mezcla propia como receta.',
                ],
            },
            {
                'n': 3,
                'titulo': 'Decisiones del Verano, la Plantilla y el Modelo',
                'resumen_indice': 'qué haces en verano, cuánta madrugada asumes, si compartes la freidora y si franquicias.',
                'palabras': 2200, 'bloques': 1,
                'objetivo': 'Resolver las cuatro decisiones del verano, de la '
                            'plantilla y del modelo de negocio, cada una con el '
                            'veredicto de El Molinete y el umbral que lo '
                            'cambiaría.',
                'epigrafes': list(PPE_DEC3),
                'puntos_por_epigrafe': PPE_DEC3,
                'puntos_globales': PG_DEC,
                'cifras': [
                    C('Decisión 9 · Contribución de julio y agosto con carta de verano', f'{X_TEMP}!El Verano (Tres Salidas)!C16', 'eur', clave='Contribución de julio y agosto con carta de verano'),
                    C('Decisión 9 · Contribución de julio y agosto saliendo de ferias', f'{X_TEMP}!El Verano (Tres Salidas)!D16', 'eur', clave='Contribución de julio y agosto saliendo de ferias'),
                    C('Decisión 9 · Raciones al día del local por debajo de las cuales la carta de verano deja menos que las ferias', f'{X_TEMP}!El Verano (Tres Salidas)!B24', 'num1', clave='Raciones al día por debajo de las cuales la carta de verano deja menos que las ferias'),
                    C('Decisión 9 · Resultado de julio y agosto con los fijos dentro, con la carta de verano', f'{X_PLAN}!Escenarios!D23', 'eur', clave='Verano con fijos con la carta de verano'),
                    C('Decisión 10 · Horas del titular a la semana', f'{X_TURNOS}!Horas del Titular!B6', 'num1', clave='Horas del titular a la semana'),
                    C('Decisión 10 · Horas de madrugada del titular a la semana', f'{X_TURNOS}!Horas del Titular!B10', 'num1', clave='Horas de madrugada del titular a la semana'),
                    C('Decisión 10 · Lo que valdrían al año las horas de más del titular', f'{X_TURNOS}!Horas del Titular!B14', 'eur', clave='Valor de las horas de más del titular al año'),
                    C('Decisión 10 · Veredicto del libro de turnos sobre las horas del titular', f'{X_TURNOS}!Horas del Titular!B15', 'txt', clave='Veredicto de las horas del titular'),
                    C('Decisión 11 · ¿Freidora dedicada o compartida en El Molinete?', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B11', 'txt', clave='¿Freidora dedicada o compartida?'),
                    C('Decisión 11 · Acrilamida, parte A del anexo II, en El Molinete', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B35', 'txt', clave='Acrilamida: parte A'),
                    C('Decisión 11 · Casillas de alérgenos pendientes de leer en la etiqueta', f'{X_LEGAL}!Alérgenos y Aceite Compartido!B21', 'num', clave='Casillas de alérgenos pendientes de la etiqueta'),
                    C('Decisión 11 · kW computables de la cocina con una sola freidora', f'{X_PROD}!Freidoras, Potencia y Riesgo!D12', 'num', clave='kW computables de la cocina'),
                    C('Decisión 12 · Inversión total de El Molinete, con el fondo de maniobra', f'{X_PLAN}!Inversión Inicial!B24', 'eur', clave='Inversión total (CAPEX más fondo de maniobra)'),
                    C('Decisión 12 · Inversión publicada más baja de las enseñas', f'{X_CAPEX}!Franquicia o Independiente!B20', 'eur', clave='Franquicias: inversión publicada más baja'),
                    C('Decisión 12 · Inversión publicada más alta de las enseñas', f'{X_CAPEX}!Franquicia o Independiente!B21', 'eur', clave='Franquicias: inversión publicada más alta'),
                    C('Decisión 12 · Enseñas de base comparable por debajo de la inversión de apertura de El Molinete', f'{X_CAPEX}!Franquicia o Independiente!B23', 'num', clave='Franquicias de base comparable por debajo de tu CAPEX'),
                ],
                'sector': ['CUS-11', 'CUS-31e', 'CUN-29', 'CUN-40', 'CHN-33',
                           'CHN-34', 'CUN-04', 'CUS-M12', 'CUS-M14', 'CUS-M15',
                           'CUS-03'],
                'tablas': [
                    {
                        'titulo': 'Decisión 9 · El verano con los fijos dentro (plan-financiero-3-anos-churreria.xlsx, hoja «Escenarios»)',
                        'src': (X_PLAN, 'Escenarios'),
                        'cols': [('Salida del verano', 'A', 'txt'),
                                 ('Contribución de julio y agosto', 'B', 'eur'),
                                 ('Fijos de esos dos meses', 'C', 'eur'),
                                 ('Resultado con fijos', 'D', 'eur')],
                        'filas': (22, 26),
                        'ancla': ('A22', 'Cerrar en julio y agosto'),
                        'nota': 'Los fijos son los mismos en las tres salidas: por eso se elige por '
                                'contribución.',
                    },
                    {
                        'titulo': 'Decisión 10 · Las horas del titular (turnos-plantilla-y-madrugada.xlsx, hoja «Horas del Titular»)',
                        'src': (X_TURNOS, 'Horas del Titular'),
                        'cols': [('Concepto', 'A', 'txt'), ('Horas', 'B', 'num1')],
                        'filas': (6, 13),
                        'ancla': ('A6', 'Horas a la semana en el cuadrante'),
                        'nota': 'El titular autónomo está en nómina en el plan como un puesto más; '
                                'sus horas de más no se pagan aparte, y por eso se valoran.',
                    },
                    {
                        'titulo': 'Decisión 11 · Lo que fríe El Molinete en su freidora (checklist-legal-fritura-y-licencias.xlsx, hoja «Alérgenos y Aceite Compartido»)',
                        'src': (X_LEGAL, 'Alérgenos y Aceite Compartido'),
                        'cols': [('Lo que fríes', 'A', 'txt'),
                                 ('¿En la misma freidora?', 'B', 'txt')],
                        'filas': (7, 11),
                        'ancla': ('A7', 'Churros y porras'),
                        'nota': 'Lo que fríes en la misma cuba pasa al resto: tus alérgenos son los de '
                                'todo lo que fríes en ella.',
                    },
                    {
                        'titulo': 'Decisión 12 · La inversión que publican las enseñas, con su base (calculadora-capex-churreria.xlsx, hoja «Franquicia o Independiente»)',
                        'src': (X_CAPEX, 'Franquicia o Independiente'),
                        'cols': [('Enseña', 'A', 'txt'), ('Inversión publicada', 'B', 'eur'),
                                 ('Canon de entrada', 'D', 'eur'),
                                 ('Royalty sobre ventas', 'E', 'pct0'),
                                 ('¿Base comparable con la tuya?', 'I', 'txt')],
                        'filas': (6, 17),
                        'ancla': ('A6', 'Chocolaterías Valor'),
                        'nota': 'Inversión publicada por cada franquiciador, consultada el 3 de octubre '
                                'de 2026: orden de magnitud, no presupuesto.',
                    },
                ],
                'prohibido': NO_COMUN_BONUS + [
                    'PROHIBIDO presentar una rebaja fiscal como salida del '
                    'verano.',
                    'PROHIBIDO escribir que el churrero de la madrugada es '
                    'trabajador nocturno como regla.',
                    'PROHIBIDO recomendar una enseña concreta o usar la '
                    'facturación que anuncia un franquiciador.',
                ],
            },
        ],
    },
]


# ==========================================================================
# Palabras correctas que el léxico del detector no trae. Se asignan a la guía
# Y a cada bonus (regla de la casa). Base: la lista de la hermana, más el
# oficio de la churrería y los nombres propios de este pack.
# ==========================================================================
_ERRATAS_OK = (
    # Formas verbales y palabras correctas que el léxico no trae (heredadas)
    'podré', 'bañada', 'bañadas', 'respondió', 'auditado', 'bájalo',
    'cámbiala', 'cámbialo', 'coincidan', 'comprarte', 'costeos', 'deberán',
    'dejara', 'digan', 'empezara', 'existan', 'justifícalo', 'léelo',
    'librarte', 'llévala', 'llévate', 'móntalo', 'movió', 'planeado',
    'posventa', 'provisionado', 'ratos', 'recogió', 'reventa', 'rodando',
    'tales', 'telefonía', 'trasladado', 'trátala', 'tratara', 'vendía',
    'viajado', 'pregúntale', 'pregúntalo', 'mídela', 'pásalo', 'apúntalo',
    'cuéntala', 'fríes', 'fríe', 'fríen', 'freír', 'freírse', 'escandalla',
    'venció', 'fianzas', 'tocara',
    # El oficio de la churrería
    'churro', 'churros', 'churrera', 'churreras', 'churrero', 'churreros',
    'churrería', 'churrerías', 'churrería-chocolatería', 'porra', 'porras',
    'tejeringo', 'tejeringos', 'calentito', 'calentitos', 'jeringo',
    'jeringos', 'buñuelo', 'buñuelos', 'dosificadora', 'dosificadoras',
    'dosificador', 'dosificado', 'amasadora', 'amasadoras', 'amasador',
    'amasado', 'amasados', 'caldero', 'freidora', 'freidoras', 'fritura',
    'frituras', 'fritos', 'chocolatera', 'chocolateras', 'escurridor',
    'cuba', 'cubas', 'polares', 'acrilamida', 'extracción', 'conducto',
    'conductos', 'campana', 'campanas', 'caseta', 'casetas', 'remolque',
    'remolques', 'feriante', 'feriantes', 'quiosco', 'quioscos',
    'cucurucho', 'cucuruchos', 'granizado', 'granizados', 'horchata',
    'batido', 'batidos', 'antigrasa', 'rellenadora', 'reposición',
    'renovación', 'absorción', 'absorbido', 'freiduría', 'freidurías',
    'chocolatería', 'chocolaterías', 'chocolatero', 'chocolateros',
    'obrador', 'obradores', 'bombonería', 'bombonerías', 'cobertura',
    'preparado', 'preparados', 'cacao', 'romería', 'romerías', 'tenderete',
    'tenderetes', 'carrito', 'despacho', 'despachos', 'tique', 'tiques',
    # Local, obra e instalaciones
    'climatización', 'vitrina', 'vitrinas', 'mostrador', 'mostradores',
    'acometida', 'desagüe', 'lavamanos', 'fregadero', 'vestuario',
    'vestuarios', 'aseo', 'aseos', 'traspaso', 'traspasos', 'traspasado',
    'arrendamiento', 'fianza', 'urbanístico', 'ordenanza', 'ordenanzas',
    'visado', 'boletín', 'legalización', 'combustión', 'escaparate',
    'rótulo', 'extintor', 'extintores', 'portafiltros', 'receptora',
    'filtrado', 'captación', 'cubierta', 'kilovatio', 'kilovatios',
    # Sanitario y normativo
    'autocontrol', 'alérgeno', 'alérgenos', 'trazabilidad', 'minorista',
    'minoristas', 'titularidad', 'habilitante', 'derogado', 'derogada',
    'derogados', 'vigencia', 'vigente', 'vigentes', 'consolidado',
    'declaración', 'responsable', 'artesanal', 'acreditación', 'acreditable',
    'marginal', 'restringido', 'restringida', 'contaminante', 'analítica',
    'inscribirse', 'inscripción', 'precontractual', 'interconectado',
    'extrapola', 'extrapolar', 'ultraactividad', 'asimilación', 'laboralista',
    # Económico, fiscal y laboral
    'escandallo', 'escandallos', 'escandallar', 'costeo', 'costear', 'tanda',
    'tandas', 'merma', 'mermas', 'ponderado', 'ponderada', 'amortización',
    'amortizable', 'tesorería', 'circulante', 'carencia', 'principal',
    'cuota', 'cuotas', 'repercutido', 'soportado', 'liquidación', 'epígrafe',
    'epígrafes', 'convenio', 'convenios', 'cotización', 'jornada', 'jornadas',
    'contratación', 'dimensionado', 'estacionalidad', 'inmovilizado',
    'rotación', 'surtido', 'surtidos', 'refuerzo', 'refuerzos', 'granel',
    'royalty', 'royalties', 'canon', 'franquiciador', 'franquiciadores',
    'franquiciar', 'franquiciado', 'franquiciados', 'nocturnidad',
    'nocturno', 'nocturnos', 'cuadrante', 'cuadrantes', 'franja', 'franjas',
    'madrugada', 'madrugadas',
    # Palabras correctas que el corpus del blog no contiene
    'comprobable', 'defendible', 'medible', 'sustituible', 'editable',
    'modelado', 'modelada', 'acotado', 'eliminatorio', 'eliminatorios',
    'holgura', 'solape', 'anticipo', 'recogida', 'orientativo',
    'orientativos', 'orientativa',
    # Siglas y nombres propios que el léxico no conoce
    'APPCC', 'RGSEAA', 'BOE', 'BOCM', 'BOP', 'DOUE', 'CTE', 'DB-SI', 'IAE',
    'CNAE', 'SMI', 'REGCON', 'Verifactu', 'ALEH', 'OCAS', 'RIPCI', 'LER',
    'TPV', 'TAE', 'IRPF', 'INE', 'AESAN', 'EUR-Lex', 'Hosply',
    'Molinete', 'Artesana', 'Loomis', 'Vallecas', 'Ochavillo', 'Cehegín',
    'Montefrío', 'Valdemoro', 'Zaidín', 'Genil', 'Reseave', 'Churrofácil',
    'ChurroFácil', 'Mundigas', 'Inblan', 'Inhospan', 'Repagas', 'NTGAS',
    'Irimar', 'Testo', 'Baxtran', 'ClimaHosteleria', 'Infoagro', 'Harimsa',
    'Tardienta', 'Pinocho', 'Kukuchurro', 'ChurroWay', 'Churritopping',
    'Madrid1883', 'Tejeringo', 'Valor', 'Noia', 'Boiro', 'Padrón', 'Zarautz',
)
# Correctas que el detector de erratas marca (3-oct, ensayo de documentos.py): imperativos con tilde,
# «Si calcularas» (subjuntivo), «chocolater» (término de búsqueda citado), verbos del léxico común.
_ERRATAS_OK = _ERRATAS_OK + ('confírmalo', 'tómala', 'consúltalos', 'jubila', 'calcularas', 'chocolater', 'inferir', 'reflejado',
                             'compensado', 'modesta', 'peaje')
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
