#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_guion.py — gate del GUION de «Cómo Montar una Churrería-Chocolatería»
(producto 51, pid `guia-churreria-chocolateria`) ANTES de escribir una sola
palabra de prosa.

Clon parametrizado del gate de la hermana (`guia-chocolateria/verificar_guion.py`,
12-09-2026) con las rutas de este producto, los OCHO libros del pack, la
estructura firmada en la D26 (16 capítulos + anexo + 2 + 3 = 22 bloques) y lo
que la hermana no comprobaba:

  A. ESTRUCTURA D26. 16 capítulos numerados y un anexo `sin_numerar`; las
     palabras de cada capítulo, las de la D26; un bloque por capítulo (también
     en los tres fundidos, 07, 11 y 14, que además llevan la palabra FRONTERA
     en sus puntos); los `gates` firmados de la guía y de los dos bonus; el
     business plan con ≥ 3.500 palabras y ≥ 9 tablas; 22 bloques en total.
  B. ANCLAS. Cada `C()` lleva la etiqueta del mapa del libro (`clave`) o el
     rótulo de su fila (`rotulo`), y cada tabla del xlsx su `ancla`/`anclas`.
     Si un generador mueve una celda, el gate dice «REFERENCIA MOVIDA» y dónde
     está ahora, en vez de dejar que el redactor cite la celda de al lado. Los
     mapas se leen SIEMPRE de `guia-churreria/build/mapa-*.json`.
  C. IDS. Patrón del producto (CHN, CHS, CUN, CUS, FC-IVA, con prefijo M, V o
     D). Todo id citado en CUALQUIER texto existe en el research; ningún id
     de `IDS_PROHIBIDOS` aparece en ningún texto (con frontera exacta: `CUS-31`
     a secas, no `CUS-31a`); ningún id de fiabilidad baja con cifra en los
     puntos (si no tiene cifra, aviso); y el bloque de research que de verdad
     llega al prompt (`documentos.bloque_research`) no lleva ninguna aguja de
     la lista negra.
  D. NÚMEROS SUELTOS. En puntos, globales y objetivos no queda ningún dígito
     después de quitar ids, normas (`12/2012`), artículos, capítulos,
     decisiones, epígrafes del impuesto (`644.6`), códigos de actividad
     (`47.81`), años, horas y fechas. Una cifra se nombra por su `C()` o por su
     id, nunca suelta.
  E. LISTA NEGRA. Las agujas del guion (`LISTA_NEGRA_AGUJAS`) más las de
     `datos_ejemplo.LISTA_NEGRA`, sobre todo lo que ve el redactor salvo las
     propias prohibiciones; y, sobre ABSOLUTAMENTE todo (prohibiciones
     incluidas), el patrón de R-21: «85-90», «85 y el 90» y sus variantes.
     Además, que la lista negra del §5 esté ÍNTEGRA (orígenes 5.1, 5.2, N-1…
     N-21 y 15.2) y que `NO_COMUN` vaya en las prohibiciones de cada capítulo
     de la guía y `NO_COMUN_BONUS` en las de cada capítulo de los bonus.
  F. REDACCIÓN SEGURA. Las frases de la verificación legal del 3-oct que cada
     capítulo legal tiene que llevar (art. 36.1 separado del plus, art. 3.3,
     «de utilización móvil», notas (2) y (3), Ley 7/1996 con el RD derogado,
     la celda verde de la taza…).
  G. SOLAPE (SR-21). Puntos frente a los del capítulo homólogo de la hermana
     (Jaccard de palabras ≥ 3 letras, sin tildes) y entre capítulos propios.
  H. COHERENCIA DEL LIBRO 6. Las cifras del business plan tienen que cuadrar
     entre hojas del plan financiero (resultado, contribución, inversión,
     verano). La columna «Base» de «Escenarios» se compara con el P&L: si no
     cuadra y el guion no la cita, es AVISO para los libros; si la cita, FALLO.

Y lo de la hermana: `celda()` y `construir_tabla()` sobre todo (cero
referencias rotas, vacías, fechas en crudo o tipos incompatibles), palabras
±3 %, epígrafes únicos, títulos sin miles ni raya larga (y sin siglas en los
titulares, SPEC §0), puntos por epígrafe, cero caracteres no latinos, claves
de `gates` y `erratas_permitidas` en la guía y en cada bonus.

Dónde lee los xlsx: `astro-site/public/dl/<pid>/` si existe; si no, el
`build/` del producto (lo dice al arrancar). `--dl` exige `dl/`; `--xlsx-dir
RUTA` fuerza otra carpeta. `--txt DIR` barre además los bloques ya redactados
(`*.txt`) con la lista negra, los ids prohibidos y el patrón R-21.

Uso:  /usr/local/bin/python3 scripts/productos-digitales/guia-churreria/verificar_guion.py
En el Mac hay que usar `/usr/local/bin/python3`: el del sistema no trae openpyxl.
Via: Claude Code
"""
import argparse
import collections
import datetime as dt
import glob
import importlib.util
import json
import os
import re
import sys
import unicodedata

REPO = '/Users/johnguerrero/chefpro-modernize'
PID = 'guia-churreria-chocolateria'
PD = os.path.join(REPO, 'scripts', 'productos-digitales')
GUIAS = os.path.join(PD, 'guias-v2_0')
GUION_PY = os.path.join(GUIAS, f'guion_{PID.replace("-", "_")}.py')
HERMANA_PY = os.path.join(GUIAS, 'guion_guia_chocolateria_obrador.py')
PRODUCTO = os.path.join(PD, 'guia-churreria')
BUILD = os.path.join(PRODUCTO, 'build')
DATOS_PY = os.path.join(PRODUCTO, 'datos_ejemplo.py')
RESEARCH = os.path.join(PD, 'auditorias', 'guias-v2-research-sector.json')

LIBROS = (
    'produccion-hora-punta-y-local.xlsx',            # 1
    'calculadora-capex-churreria.xlsx',              # 2
    'carta-de-apertura-y-escandallo-churro.xlsx',    # 3
    'aceite-de-fritura-coste-y-cambio.xlsx',         # 4
    'temporada-franjas-y-ferias.xlsx',               # 5
    'plan-financiero-3-anos-churreria.xlsx',         # 6
    'checklist-legal-fritura-y-licencias.xlsx',      # 7
    'turnos-plantilla-y-madrugada.xlsx',             # 8
)
N_RESEARCH = 837

# ------------------------------------------------------------------ D26
PALABRAS_D26 = {1: 1600, 2: 1300, 3: 1600, 4: 1700, 5: 1700, 6: 1800,
                7: 2300, 8: 1600, 9: 1600, 10: 1600, 11: 2500, 12: 1600,
                13: 1700, 14: 2700, 15: 1300, 16: 1500, 17: 1200}
FUNDIDOS = (7, 11, 14)
NOMBRE_BP = 'business-plan-modelo-churreria-chocolateria'
NOMBRE_DEC = 'BONUS-12-decisiones-de-apertura'
GATES_D26 = {                        # paginas, palabras, min_palabras_cap
    'GUIA': (80, 29300, 1100),
    NOMBRE_BP: (9, 3500, 1200),
    NOMBRE_DEC: (20, 6600, 400),
}
CAPS_D26 = {'GUIA': 17, NOMBRE_BP: 2, NOMBRE_DEC: 3}
BLOQUES_D26 = 22
BP_MIN_PALABRAS, BP_MIN_TABLAS = 3500, 9

#: Umbrales por documento: epígrafes, C(), tablas, puntos por epígrafe y
#: puntos globales.
UMBRALES = {
    'GUIA': dict(epi=(4, 6), cifras=(4, 10), tablas=(1, 3), ppe=(2, 5), glob=(2, 3)),
    NOMBRE_BP: dict(epi=(4, 6), cifras=(6, 24), tablas=(4, 6), ppe=(2, 5), glob=(2, 3)),
    NOMBRE_DEC: dict(epi=(4, 4), cifras=(8, 16), tablas=(4, 4), ppe=(5, 6), glob=(2, 4)),
}

# ------------------------------------------------------------------ ids
#: El patrón de id de este producto (§2.3 de la SPEC; el mismo de
#: `datos_ejemplo.RX_ID`).
RX_ID = re.compile(r'\b(?:CHN|CHS|CUN|CUS|FC-IVA)-(?:[MVD])?[0-9]+[a-z]*\b')
#: Prohibidos en CUALQUIER texto del guion (verificación legal §6.11, SPEC
#: §5.2). `CUS-40` sólo estaría permitido sin cifra, y el guion no lo usa;
#: `CHS-37b`, la lectura antigua de Vallecas; `CUS-31` y `CHS-31`, a secas.
IDS_PROHIBIDOS = ('CUS-31h', 'CUS-31i', 'CUS-56', 'CUS-M05', 'CUS-05',
                  'CUS-40', 'CHS-37b', 'CUS-31', 'CHS-31')
RX_PROHIBIDO = {i: re.compile(r'(?<![A-Za-z0-9-])' + re.escape(i) + r'(?![0-9A-Za-z])')
                for i in IDS_PROHIBIDOS}

# ------------------------------------------------------------------ R-21
#: Refutación de los libros (R-21): el margen sobre materia de El Molinete es
#: una cifra calculada y se cita por su C(); «85-90 %» es la cifra vetada de
#: CHS-31. Se barre sobre TODO, prohibiciones incluidas.
RX_R21 = re.compile(r'(?<![\d.,])85\s*%?\s*(?:-|–|—|a|al|y|y el|e)\s*(?:el\s+)?90(?![\d])',
                    re.IGNORECASE)

# ------------------------------------------------------------------ texto
RX_MILES = re.compile(r'\b\d{1,3}(?:\.\d{3})+(?:,\d+)?\b')
RX_DIGITO = re.compile(r'\d')
RX_FECHA_CRUDA = re.compile(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}:\d{2}')
RAYA = '—'     # por escape: en un heredoc degeneraría en «-»
MESES = ('enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|'
         'octubre|noviembre|diciembre')
#: Lo que se quita antes de buscar números sueltos en los puntos.
PERMITIDOS_NUM = [
    RX_ID,
    re.compile(r'\b[\w.-]+\.xlsx\b'),                              # 09-control-….xlsx
    re.compile(r'\b\d+/\d{4}\b'),                                   # 12/2012
    re.compile(r'\b\d{1,2}\s+de\s+(?:' + MESES + r')(?:\s+de\s+\d{4})?', re.I),
    re.compile(r'\b\d{1,2}-\d{1,2}-\d{4}\b'),                       # 31-12-2025
    re.compile(r'\b(?:arts?\.|art[ií]culos?|apartados?|anexos?|cap[ií]tulos?|'
               r'libros?|grupos?|ep[ií]grafes?|decisi[oó]n(?:es)?|fases?|notas?|'
               r'tablas?|reglas?|clases?|niveles?|secci[oó]n|versi[oó]n)\s+'
               r'\d+(?:[.,]\d+)*(?:\s*(?:,|y|a|e|o)\s*\d+(?:[.,]\d+)*)*', re.I),
    re.compile(r'\bnotas?\s*\(\d\)(?:\s*y\s*\(\d\))?', re.I),       # nota (2)
    re.compile(r'\b\d{3}\.\d\b'),                                   # 644.6
    re.compile(r'\b\d{2}\.\d{2}\b'),                                # 47.81
    re.compile(r'\b67[1-6]\b'),                                     # grupo 676
    re.compile(r'\b(?:19|20)\d{2}\b'),                              # años
    re.compile(r'\b\d{1,2}:\d{2}\b'),                               # 4:30
    re.compile(r'\bF[1-6]\b'),                                      # fases
]
#: Siglas que no van en los titulares (SPEC §0: «sin siglas en titulares»).
SIGLAS_TITULAR = re.compile(r'\b(?:IAE|CNAE|RGSEAA|APPCC|CTE|SMI|ALEH|OCAS|RIPCI|'
                            r'REGCON|LER|ET|DB-SI|CAPEX|TPV|PRL)\b')

# ------------------------------------------------------------------ F
#: Frases de la redacción segura de la verificación legal (3-oct), por
#: capítulo. Se buscan sin mayúsculas ni tildes en lo que LEE el redactor
#: (objetivo, epígrafes, puntos, globales y cifras con su valor), no en las
#: notas de las tablas, que sólo ve el lector.
FRASES_SEGURAS = {
    1: ['chocolatería boutique & atelier'],
    3: ['celda verde', 'servicio de consumo', 'zona gris', 'aviso'],
    4: ['declaración responsable', 'licencia de obra', 'art. 3.3', 'art. 2.2',
        'ejemplo de madrid'],
    5: ['utilización móvil', 'nota (2)', 'nota (3)', 'gas o de parrilla',
        'clase f', 'ejemplo de madrid'],
    9: ['644.6', '663.1', '419.3', 'comunidad autónoma', 'art. 82.1',
        'rd 10/2025'],
    10: ['anexo 1', 'laboratorio', 'artículo 9', 'ley 7/2022',
         'pack plantillas appcc'],
    11: ['buena práctica', 'art. 2.3', 'rd 126/2015', 'rd 1021/2022',
         'registro de formación'],
    12: ['kit de escandallos pro', 'guía food cost'],
    13: ['art. 36.1', 'plus', 'revísalo con tu asesor', 'asimilación',
         'tablas de 2025', 'kit gestión de personal y turnos'],
    14: ['utilización móvil', 'derogado', 'ley 7/1996', 'arts. 53 a 55',
         'rd 1021/2022', 'plan de negocio: food truck'],
    15: ['art. 2.3', '3 de octubre de 2026'],
    16: ['antes de impuestos'],
    17: ['3 de octubre de 2026', 'derogad', 'regcon', 'eur-lex'],
}

# ------------------------------------------------------------------ G
#: Capítulo propio → capítulo(s) homólogo(s) de la hermana (SPEC §4: los «H»).
HOMOLOGOS = {1: [1], 2: [2], 3: [3], 6: [5], 7: [8, 13], 8: [4], 9: [9],
             11: [12], 12: [14], 13: [17], 14: [18], 16: [20], 17: [21]}
SOLAPE_HERMANA = 0.55
SOLAPE_INTERNO_AVISO, SOLAPE_INTERNO_FALLO = 0.55, 0.75

# ------------------------------------------------------------------ E
#: La lista negra del §5 tiene que estar ENTERA: estos orígenes, al menos.
ORIGENES_OBLIGATORIOS = (
    {f'5.1-{i}' for i in range(1, 13)}
    | {f'N-{i}' for i in range(1, 22)}
    | {'5.2-traspaso', '5.2-nocturno', '5.2-filtros', '5.2-bombona', '5.2-smi',
       '5.2-brecha', '5.2-50pct', '5.2-posicion1', '5.2-fuera-espana',
       '5.2-comparativa', '5.2-post', '5.2-casa', '5.2-metodo',
       '5.2-proyecciones'}
    | {'15.2-norm', '15.2-metodo'})


def _carga(nombre, ruta):
    sp = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def norm(s):
    """Minúsculas, sin tildes y con los espacios colapsados."""
    s = unicodedata.normalize('NFKD', str(s).casefold())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', s).strip()


def tokens(s):
    return {w for w in re.findall(r'[a-zñ]{3,}', norm(s))}


def jaccard(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
ap.add_argument('--dl', action='store_true',
                help='exige los xlsx en astro-site/public/dl/<pid>/')
ap.add_argument('--xlsx-dir', help='carpeta de los xlsx (por defecto, dl/ o build/)')
ap.add_argument('--txt', help='carpeta con los bloques ya redactados (*.txt)')
ap.add_argument('--guion', help='otro fichero de guion (para los canarios del gate)')
args = ap.parse_args()

d = _carga('d', os.path.join(GUIAS, 'documentos.py'))
datos = _carga('datos_ejemplo_churreria', DATOS_PY)

fallos, avisos = [], []


def falla(msg):
    fallos.append(msg)


def avisa(msg):
    avisos.append(msg)


# ------------------------------------------------------------- dónde leer
DL_DIR = os.path.join(d.DL, PID)
if args.xlsx_dir:
    XLSX_DIR = os.path.abspath(args.xlsx_dir)
elif args.dl or os.path.isdir(DL_DIR):
    XLSX_DIR = DL_DIR
else:
    XLSX_DIR = BUILD
print(f'xlsx: {XLSX_DIR}')
print(f'mapas: {BUILD}/mapa-*.json')
if not os.path.isdir(XLSX_DIR):
    print(f'FALLO: no existe {XLSX_DIR}')
    sys.exit(1)

# ---------------------------------------------------------------- importa
if args.guion:
    GUION_PY = os.path.abspath(args.guion)
    guion = _carga('guion_canario', GUION_PY)
else:
    guion = d.cargar_guion(PID)
GUIA, CAPITULOS, BONUS = guion.GUIA, guion.CAPITULOS, guion.BONUS
print(f'guion cargado: {GUIA["titulo"]} · {len(CAPITULOS)} capítulos · '
      f'{len(BONUS)} documento(s) de bonus')

RES = json.load(open(RESEARCH, encoding='utf-8'))
idx = d.indexar_research(RES)
print(f'research: {len(idx)} entradas (se esperaban {N_RESEARCH})')
if len(idx) < N_RESEARCH:
    falla(f'el research tiene {len(idx)} entradas y se esperaban al menos '
          f'{N_RESEARCH}')

MAPAS = {}
for f in LIBROS:
    ruta = os.path.join(BUILD, f'mapa-{f[:-5]}.json')
    if not os.path.exists(ruta):
        falla(f'falta el mapa {ruta}')
        continue
    MAPAS[f] = json.load(open(ruta, encoding='utf-8'))

FMT_NUMERICOS = tuple(k for k in d.FORMATOS if k != 'txt')
FMT_PCT = ('pct', 'pct0', 'pct1', 'pct2')

AGUJAS = []                     # (aguja, origen, es_regex, es_cifra)
for ag, origen in list(getattr(guion, 'LISTA_NEGRA_AGUJAS', ())) + list(datos.LISTA_NEGRA):
    if ag.startswith('re:'):
        AGUJAS.append((re.compile(ag[3:], re.I), origen, True, False))
    elif ag[:1].isdigit():
        # Una aguja numérica no puede casar dentro de otro número: «2.400» no
        # está en «12.400» ni «23,7» en «123,75».
        AGUJAS.append((re.compile(r'(?<![\d.,])' + re.escape(ag) + r'(?![\d])', re.I),
                       origen, True, True))
    else:
        AGUJAS.append((norm(ag), origen, False, False))


def agujas_en(texto):
    """Las agujas de la lista negra que aparecen en el texto."""
    n = norm(texto)
    hallados = []
    for ag, origen, es_rx, _cifra in AGUJAS:
        if es_rx:
            m = ag.search(texto) or ag.search(n)
            if m:
                hallados.append((m.group(0), origen))
        elif ag in n:
            hallados.append((ag, origen))
    return hallados


def quitar_permitidos(texto):
    for rx in PERMITIDOS_NUM:
        texto = rx.sub(' ', texto)
    return texto


n_cifras = n_tablas = n_filas = n_puntos = 0
TEXTO_REDACTOR = collections.defaultdict(list)   # (doc, n) → textos sin prohibido
TEXTO_PROMPT = collections.defaultdict(list)     # (doc, n) → lo que el redactor LEE
TEXTO_TODO = []                                  # absolutamente todo
REFS_CITADAS = []                                # refs de C() y rangos de tabla
PUNTOS_POR_CAP = {}                              # (doc, n) → [puntos]
VALORES_CIFRAS = {}                              # ref → valor


def revisa_ids(cid, textos, puntos=False):
    """Ids citados en el texto: existen, no están prohibidos y, si son de
    fiabilidad baja, no se citan como cifra."""
    for t in textos:
        if not isinstance(t, str):
            continue
        for pid_, rx in RX_PROHIBIDO.items():
            if rx.search(t):
                falla(f'{cid}: cita el id PROHIBIDO «{pid_}» '
                      f'({datos.IDS_PROHIBIDOS.get(pid_, "lista de la SPEC")}): '
                      f'«…{t[max(0, rx.search(t).start() - 40):rx.search(t).end() + 20]}…»')
        for sid in RX_ID.findall(t):
            ficha = idx.get(sid)
            if ficha is None:
                falla(f'{cid}: el texto cita un id que no existe en el research: «{sid}»')
                continue
            if puntos and ficha.get('fiabilidad') == 'baja':
                if ficha.get('cifra') not in (None, ''):
                    falla(f'{cid}: cita como CIFRA el id «{sid}», de fiabilidad BAJA')
                else:
                    avisa(f'{cid}: menciona «{sid}», de fiabilidad baja y sin cifra '
                          '(sólo como hecho cualitativo)')


def revisa_anclas_tabla(cid, t):
    anclas = list(t.get('anclas') or [])
    if t.get('ancla'):
        anclas.insert(0, t['ancla'])
    if not anclas:
        falla(f'{cid}: la tabla «{t.get("titulo", "")[:50]}» del xlsx no lleva '
              '«ancla»: si el generador mueve la fila, nadie se entera')
        return
    fichero, hoja = t['src']
    for coord, texto in anclas:
        try:
            v = d.celda(XLSX_DIR, f'{fichero}!{hoja}!{coord}')
        except Exception as e:
            falla(f'{cid}: ancla rota {fichero}!{hoja}!{coord} → {type(e).__name__}: {e}')
            continue
        if not norm(v).startswith(norm(texto)):
            falla(f'{cid}: TABLA MOVIDA «{t.get("titulo", "")[:50]}»: en '
                  f'{hoja}!{coord} se esperaba «{texto}» y hay «{str(v)[:60]}»')


def revisa(caps, doc, gates):
    """Recorre los capítulos de un documento y valida todo lo validable."""
    global n_cifras, n_tablas, n_filas, n_puntos
    u = UMBRALES[doc]
    suma = 0
    for cap in caps:
        cid = f'{doc if doc == "GUIA" else ("BP" if doc == NOMBRE_BP else "DEC")} cap {cap["n"]:02d} «{cap["titulo"][:46]}»'
        clave_cap = (doc, cap['n'])
        suma += cap['palabras']
        for k in ('n', 'titulo', 'resumen_indice', 'palabras', 'bloques',
                  'objetivo', 'epigrafes', 'puntos_por_epigrafe',
                  'puntos_globales', 'cifras', 'sector', 'tablas', 'prohibido'):
            if k not in cap or cap[k] in (None, '', [], {}):
                if not (k == 'sector' and cap.get(k) == []):
                    falla(f'{cid}: falta o está vacía la clave «{k}»')
        if cap.get('bloques') != 1:
            falla(f'{cid}: «bloques» = {cap.get("bloques")} (D26: uno por capítulo)')

        # --- epígrafes
        epis = cap['epigrafes']
        if len(epis) != len(set(epis)):
            falla(f'{cid}: epígrafes repetidos dentro del capítulo')
        if not u['epi'][0] <= len(epis) <= u['epi'][1]:
            falla(f'{cid}: {len(epis)} epígrafes (se exigen {u["epi"][0]}-{u["epi"][1]})')
        if cap.get('bloques', 1) > len(epis):
            falla(f'{cid}: {cap["bloques"]} bloques para {len(epis)} epígrafes')
        bloques = d.trocear(epis, cap.get('bloques', 1))
        for e in epis:
            if RAYA in e:
                falla(f'{cid}: el epígrafe «{e[:40]}» lleva raya larga')
            if RX_MILES.search(e):
                falla(f'{cid}: el epígrafe «{e[:40]}» lleva una cifra con separador de miles')
            if SIGLAS_TITULAR.search(e):
                falla(f'{cid}: el epígrafe «{e[:50]}» lleva una sigla '
                      f'«{SIGLAS_TITULAR.search(e).group(0)}» (sin siglas en titulares)')

        # --- puntos_por_epigrafe y puntos_globales
        ppe = cap.get('puntos_por_epigrafe') or {}
        huerfanas = [k for k in ppe if k not in set(epis)]
        if huerfanas:
            falla(f'{cid}: «puntos_por_epigrafe» con claves que no son epígrafes: '
                  + '; '.join(f'«{k}»' for k in huerfanas))
        todos_puntos = []
        for e in epis:
            ps = ppe.get(e) or []
            if not ps:
                falla(f'{cid}: el epígrafe «{e[:44]}» no tiene puntos')
            n_puntos += len(ps)
            if ps and not u['ppe'][0] <= len(ps) <= u['ppe'][1]:
                falla(f'{cid}: el epígrafe «{e[:44]}» tiene {len(ps)} puntos '
                      f'(se exigen {u["ppe"][0]}-{u["ppe"][1]})')
            todos_puntos += ps
        try:
            repartos = d.repartir_puntos(cap, bloques)
        except SystemExit as ex:
            falla(f'{cid}: repartir_puntos aborta → {ex}')
        else:
            if any(not r for r in repartos):
                falla(f'{cid}: algún bloque se queda sin puntos tras el reparto')
        globales = cap.get('puntos_globales') or []
        if not u['glob'][0] <= len(globales) <= u['glob'][1]:
            falla(f'{cid}: {len(globales)} «puntos_globales» (se exigen '
                  f'{u["glob"][0]}-{u["glob"][1]})')
        PUNTOS_POR_CAP[clave_cap] = list(todos_puntos)
        instrucciones = todos_puntos + list(globales) + [cap.get('objetivo', '')]
        revisa_ids(cid, instrucciones, puntos=True)
        revisa_ids(cid, [cap.get('titulo', ''), cap.get('resumen_indice', '')] + epis)
        revisa_ids(cid, cap.get('prohibido') or [])

        # números sueltos
        for t in instrucciones:
            resto = quitar_permitidos(t)
            if RX_DIGITO.search(resto):
                m = RX_DIGITO.search(resto)
                falla(f'{cid}: NÚMERO SUELTO en los puntos: «…{resto[max(0, m.start() - 50):m.end() + 30].strip()}…» '
                      '(nómbralo por su C() o por su id)')

        # fundidos: frontera explícita
        if doc == 'GUIA' and cap['n'] in FUNDIDOS:
            if not any('FRONTERA' in p for p in todos_puntos):
                falla(f'{cid}: capítulo FUNDIDO sin la palabra FRONTERA entre sus dos mitades')

        # --- título
        tit = cap['titulo']
        if RX_MILES.search(tit):
            falla(f'{cid}: el título lleva una cifra con separador de miles')
        if RAYA in tit:
            falla(f'{cid}: el título lleva raya larga')
        if RX_DIGITO.search(tit) and not cap.get('sin_numerar'):
            falla(f'{cid}: el título lleva dígitos (sólo el anexo puede, por su fecha)')
        if SIGLAS_TITULAR.search(tit):
            falla(f'{cid}: el título lleva la sigla «{SIGLAS_TITULAR.search(tit).group(0)}»')

        # --- cifras
        cifras = cap.get('cifras', [])
        if not u['cifras'][0] <= len(cifras) <= u['cifras'][1]:
            falla(f'{cid}: {len(cifras)} cifras C() (se exigen '
                  f'{u["cifras"][0]}-{u["cifras"][1]})')
        etiquetas_cap = []
        for etq, ref, fmt in cifras:
            n_cifras += 1
            REFS_CITADAS.append(ref)
            etiquetas_cap.append(etq)
            if fmt not in d.FORMATOS:
                falla(f'{cid}: formato desconocido «{fmt}» en «{etq}»')
            try:
                v = d.celda(XLSX_DIR, ref)
            except Exception as ex:
                falla(f'{cid}: REFERENCIA ROTA {ref} → {type(ex).__name__}: {ex}')
                continue
            VALORES_CIFRAS[ref] = v
            if v is None:
                falla(f'{cid}: CELDA VACÍA {ref} («{etq}»)')
                continue
            if isinstance(v, (dt.datetime, dt.date, dt.time)):
                falla(f'{cid}: {ref} devuelve una FECHA u HORA: se imprimiría «{v}»')
                continue
            if fmt in FMT_NUMERICOS and not isinstance(v, (int, float)):
                falla(f'{cid}: TIPO INCOMPATIBLE en {ref} («{etq}»): «{fmt}» es '
                      f'numérico y la celda es texto → «{str(v)[:50]}»')
                continue
            if fmt in FMT_PCT and isinstance(v, (int, float)) and abs(v) > 1.5:
                falla(f'{cid}: PORCENTAJE FUERA DE RANGO en {ref} («{etq}»): la '
                      f'celda vale {v} y «{fmt}» imprimiría {d.formatear(v, fmt)}')
            txt = d.formatear(v, fmt)
            if not str(txt).strip():
                falla(f'{cid}: valor formateado VACÍO en {ref} («{etq}»)')
            if RX_FECHA_CRUDA.search(str(txt)):
                falla(f'{cid}: {ref} imprime una fecha en crudo: «{txt}»')
            TEXTO_REDACTOR[clave_cap].append(f'{etq}: {txt}')
            TEXTO_PROMPT[clave_cap].append(f'{etq}: {txt}')

        # --- sector
        sector = cap.get('sector', [])
        for sid in sector:
            if sid not in idx:
                falla(f'{cid}: id de sector inexistente «{sid}»')
            for pid_, rx in RX_PROHIBIDO.items():
                if rx.fullmatch(sid):
                    falla(f'{cid}: «sector» trae el id PROHIBIDO «{pid_}»')
        # Lo que de verdad llega al prompt del research. Sus notas son del
        # research, no del guion, y las agujas que llevan son CORRECCIONES
        # («PROHIBIDO citar…», «corregida: CHS-37b decía…»): AVISO, no fallo.
        # El redactor las tiene vetadas en NO_COMUN y `--txt` las caza si se
        # cuelan en un bloque redactado.
        for sid in [s for s in sector if s in idx]:
            bloque_res, _u, _h = d.bloque_research(idx, [sid])
            for ag, origen in agujas_en(bloque_res):
                avisa(f'{cid}: la ficha {sid} que llega al prompt menciona «{ag}» '
                      f'({origen}) como corrección: vigilar con --txt')
            if RX_R21.search(bloque_res):
                avisa(f'{cid}: la ficha {sid} que llega al prompt menciona «85-90» '
                      '(R-21) como corrección: vigilar con --txt')
            for pid_, rx in RX_PROHIBIDO.items():
                if rx.search(bloque_res):
                    avisa(f'{cid}: la ficha {sid} que llega al prompt nombra el id '
                          f'prohibido «{pid_}» como corrección: vigilar con --txt')
        # ids que nombran los puntos y que el redactor no tiene en su research
        sector_set = set(sector)
        for t in todos_puntos + list(globales):
            for sid in RX_ID.findall(t):
                if sid in idx and sid not in sector_set:
                    avisa(f'{cid}: los puntos nombran «{sid}», que no está en su '
                          '«sector» (el redactor no verá su fuente)')

        # --- tablas
        tabs = cap.get('tablas', [])
        if not u['tablas'][0] <= len(tabs) <= u['tablas'][1]:
            falla(f'{cid}: {len(tabs)} tablas (se exigen {u["tablas"][0]}-{u["tablas"][1]})')
        for t in tabs:
            n_tablas += 1
            tit_t = t.get('titulo', '')
            if not tit_t:
                falla(f'{cid}: tabla sin título')
            if RAYA in tit_t:
                falla(f'{cid}: el título de la tabla «{tit_t[:40]}» lleva raya larga')
            if RX_MILES.search(tit_t):
                falla(f'{cid}: el título de la tabla «{tit_t[:40]}» lleva separador de miles')
            if 'src' in t:
                revisa_anclas_tabla(cid, t)
                fichero, hoja = t['src']
                ini, fin = t['filas']
                REFS_CITADAS.append(f'{fichero}!{hoja}!@{ini}-{fin}')
                for _tit, col, fmt in t['cols']:
                    if fmt in FMT_PCT and not col.startswith('='):
                        for r in range(ini, fin + 1):
                            if r in set(t.get('omitir_filas', ())):
                                continue
                            v = d.celda(XLSX_DIR, f'{fichero}!{hoja}!{col}{r}')
                            if isinstance(v, (int, float)) and abs(v) > 1.5:
                                falla(f'{cid}: la tabla «{tit_t[:40]}» imprime como '
                                      f'porcentaje {hoja}!{col}{r} = {v}')
            try:
                md, nf = d.construir_tabla(XLSX_DIR, t)
            except Exception as ex:
                falla(f'{cid}: TABLA ROTA «{tit_t[:40]}» → {type(ex).__name__}: {ex}')
                continue
            n_filas += nf
            if nf < 1:
                falla(f'{cid}: tabla «{tit_t[:40]}» con 0 filas')
            if RX_FECHA_CRUDA.search(md):
                falla(f'{cid}: la tabla «{tit_t[:40]}» imprime una fecha u hora en crudo')
            if re.search(r'\|\s*None\s*\|', md):
                falla(f'{cid}: la tabla «{tit_t[:40]}» imprime «None»')
            revisa_ids(cid, [md, tit_t, t.get('nota', '')])
            TEXTO_REDACTOR[clave_cap] += [tit_t, t.get('nota', ''), md]

        # --- prohibiciones
        prohib = cap.get('prohibido') or []
        if not prohib:
            falla(f'{cid}: sin lista de prohibiciones')
        base = guion.NO_COMUN if doc == 'GUIA' else guion.NO_COMUN_BONUS
        faltan = [x for x in base if x not in prohib]
        if faltan:
            falla(f'{cid}: «prohibido» no lleva {len(faltan)} entrada(s) de '
                  f'{"NO_COMUN" if doc == "GUIA" else "NO_COMUN_BONUS"}')

        TEXTO_REDACTOR[clave_cap] += ([cap['titulo'], cap.get('resumen_indice', ''),
                                       cap.get('objetivo', '')] + epis
                                      + todos_puntos + list(globales))
        # Lo que de verdad lee el redactor (documentos.prompt_bloque): objetivo,
        # epígrafes, puntos, globales y cifras. Las notas de tabla las ve el
        # lector, no el redactor.
        TEXTO_PROMPT[clave_cap] += ([cap.get('objetivo', '')] + epis + todos_puntos
                                    + list(globales))
        TEXTO_TODO.extend(TEXTO_REDACTOR[clave_cap] + list(prohib))

    obj = gates['palabras_objetivo']
    dif = abs(suma - obj) / obj
    print(f'  {doc}: {len(caps)} capítulos · {suma} palabras declaradas '
          f'(objetivo {obj}, desvío {dif * 100:.1f} %)')
    if dif > 0.03:
        falla(f'{doc}: la suma de palabras ({suma}) se desvía más del 3 % del objetivo ({obj})')
    return suma


# ================================================================ recorrido
print('\n--- validando la guía ---')
palabras_doc = {'GUIA': revisa(CAPITULOS, 'GUIA', GUIA['gates'])}
for b in BONUS:
    print(f'--- validando {b["nombre"]} ---')
    if b['nombre'] not in UMBRALES:
        falla(f'bonus desconocido «{b["nombre"]}»')
        continue
    palabras_doc[b['nombre']] = revisa(b['capitulos'], b['nombre'], b['gates'])

# ================================================================ A. D26
print('\n--- estructura D26 ---')
numerados = [c for c in CAPITULOS if not c.get('sin_numerar')]
anexos = [c for c in CAPITULOS if c.get('sin_numerar')]
if [c['n'] for c in numerados] != list(range(1, 17)):
    falla(f'capítulos numerados {[c["n"] for c in numerados]} (D26: del 1 al 16)')
if len(anexos) != 1 or anexos[0]['n'] != 17 or CAPITULOS[-1] is not anexos[0]:
    falla('D26: tiene que haber UN anexo `sin_numerar`, el último, con n = 17')
for c in CAPITULOS:
    if PALABRAS_D26.get(c['n']) != c['palabras']:
        falla(f'D26: el capítulo {c["n"]} declara {c["palabras"]} palabras y la '
              f'D26 dice {PALABRAS_D26.get(c["n"])}')
docs = {'GUIA': (GUIA['gates'], CAPITULOS)}
docs.update({b['nombre']: (b['gates'], b['capitulos']) for b in BONUS})
for nombre, (pag, pal, minc) in GATES_D26.items():
    if nombre not in docs:
        falla(f'D26: falta el documento «{nombre}»')
        continue
    g, caps = docs[nombre]
    real = (g.get('paginas_prometidas'), g.get('palabras_objetivo'), g.get('min_palabras_cap'))
    if real != (pag, pal, minc):
        falla(f'D26: gates de {nombre} = {real}, se esperaban {(pag, pal, minc)}')
    if len(caps) != CAPS_D26[nombre]:
        falla(f'D26: {nombre} tiene {len(caps)} capítulos y se esperaban {CAPS_D26[nombre]}')
    cortos = [c['n'] for c in caps if c['palabras'] < minc]
    if cortos:
        falla(f'{nombre}: capítulos por debajo de min_palabras_cap ({minc}): {cortos}')
if NOMBRE_BP in docs:
    _g, caps_bp = docs[NOMBRE_BP]
    pal_bp = sum(c['palabras'] for c in caps_bp)
    tab_bp = sum(len(c.get('tablas', [])) for c in caps_bp)
    print(f'  business plan: {pal_bp} palabras · {tab_bp} tablas')
    if pal_bp < BP_MIN_PALABRAS:
        falla(f'business plan con {pal_bp} palabras (D26: al menos {BP_MIN_PALABRAS})')
    if tab_bp < BP_MIN_TABLAS:
        falla(f'business plan con {tab_bp} tablas (D26: al menos {BP_MIN_TABLAS})')
    res = [p for p in PUNTOS_POR_CAP.get((NOMBRE_BP, 1), [])]
    if not any('antes de impuestos' in norm(p) for p in res):
        falla('business plan: el resumen ejecutivo no da el resultado (antes de impuestos)')
    if not any('punto de equilibrio' in norm(p) for p in res):
        falla('business plan: el resumen ejecutivo no da el punto de equilibrio')
bloques_tot = sum(len(d.trocear(c['epigrafes'], c.get('bloques', 1)))
                  for _n, (_g, caps) in docs.items() for c in caps)
if bloques_tot != BLOQUES_D26:
    falla(f'D26: el pipeline producirá {bloques_tot} bloques y la D26 dice {BLOQUES_D26}')

# portada de la guía
if GUIA.get('titulo') != 'Cómo Montar una Churrería-Chocolatería':
    falla(f'GUIA.titulo = «{GUIA.get("titulo")}»')
sub = GUIA.get('subtitulo', '')
for frag in ('churros, chocolate a la taza y números', 'Guía España 2026'):
    if frag not in sub:
        falla(f'GUIA.subtitulo no contiene «{frag}»')
if GUIA.get('version') != '1.0' or GUIA.get('fecha') != 'octubre de 2026':
    falla('GUIA: versión 1.0 y fecha «octubre de 2026»')
for k in ('bio', 'legal', 'portada_texto', 'tipo_doc', 'tipo_doc_art',
          'tipo_doc_dem', 'categoria_doc', 'cabecera'):
    if not GUIA.get(k):
        falla(f'GUIA: falta «{k}»')
for b in BONUS:
    for k in ('titulo', 'subtitulo', 'cabecera', 'tipo_doc', 'portada_texto'):
        if not b['guia'].get(k):
            falla(f'{b["nombre"]}.guia: falta «{k}»')

# ================================================================ B. anclas
print('\n--- anclas de las cifras ---')
anclas = list(getattr(guion, 'ANCLAS', []))
c_refs = collections.Counter(ref for ref in REFS_CITADAS if '!@' not in ref)
a_refs = collections.Counter(ref for ref, _c, _r in anclas)
sueltas = [r for r, n in c_refs.items() if n > a_refs.get(r, 0)]
if sueltas:
    falla(f'{len(sueltas)} cifra(s) escritas sin pasar por C(): {sueltas[:5]}')
movidas = 0
for ref, clave, rotulo in anclas:
    fichero, hoja, coord = ref.split('!')
    if clave is None and rotulo is None:
        falla(f'C() sin ancla: {ref} no lleva ni «clave» del mapa ni «rotulo»')
        continue
    if clave is not None:
        mapa = MAPAS.get(fichero)
        if mapa is None:
            falla(f'{ref}: no hay mapa de {fichero}')
        elif clave not in mapa:
            falla(f'{ref}: la etiqueta «{clave}» no existe en el mapa de {fichero}')
        else:
            ref_mapa = mapa[clave]['ref'] if isinstance(mapa[clave], dict) else mapa[clave]
            if ref_mapa != ref:
                movidas += 1
                falla(f'REFERENCIA MOVIDA «{clave}»: el guion cita {hoja}!{coord} y el '
                      f'mapa la pone en {ref_mapa.split("!", 1)[1]}')
    if rotulo is not None:
        rc, rtexto = rotulo
        try:
            v = d.celda(XLSX_DIR, f'{fichero}!{hoja}!{rc}')
        except Exception as ex:
            falla(f'{ref}: rótulo ilegible {hoja}!{rc} → {ex}')
            continue
        if not norm(v).startswith(norm(rtexto)):
            movidas += 1
            falla(f'RÓTULO MOVIDO {ref}: en {hoja}!{rc} se esperaba «{rtexto}» y hay '
                  f'«{str(v)[:60]}»')
print(f'  {len(anclas)} anclas de C() · {movidas} movidas')

# ================================================================ E. lista negra
print('\n--- lista negra ---')
origenes = {o for o, _t in guion.LISTA_NEGRA_GUION}
faltan_o = sorted(ORIGENES_OBLIGATORIOS - origenes)
if faltan_o:
    falla(f'LISTA_NEGRA_GUION no cubre {len(faltan_o)} origen(es) del §5: {faltan_o}')
if guion.NO_COMUN != [t for _o, t in guion.LISTA_NEGRA_GUION]:
    falla('NO_COMUN no es la lista de textos de LISTA_NEGRA_GUION')
if any(x not in guion.NO_COMUN_BONUS for x in guion.NO_COMUN):
    falla('NO_COMUN_BONUS no contiene NO_COMUN entero')
# Las prohibiciones van ESCRITAS CON LETRA y sin ids: lo prohibido no le
# llega al redactor con los dígitos que podría copiar.
for t in guion.NO_COMUN_BONUS:
    if RX_ID.search(t):
        falla(f'NO_COMUN cita el id «{RX_ID.search(t).group(0)}»: «{t[:70]}…»')
    for ag, origen, _rx, es_cifra in AGUJAS:
        if es_cifra and ag.search(t):
            falla(f'NO_COMUN escribe en dígitos la cifra vetada «{ag.search(t).group(0)}» '
                  f'({origen}): escríbela con letra')
golpes = 0
for (doc, n), textos in TEXTO_REDACTOR.items():
    for t in textos:
        for ag, origen in agujas_en(t):
            golpes += 1
            falla(f'{doc} cap {n:02d}: AGUJA de la lista negra «{ag}» ({origen}) en '
                  f'«…{str(t)[:90]}…»')
# R-21, sobre absolutamente todo
todo = TEXTO_TODO + list(guion.NO_COMUN_BONUS) + [GUIA.get('legal', ''),
                                                  GUIA.get('portada_texto', '')]
todo += [b['guia'].get('portada_texto', '') for b in BONUS]
for t in todo:
    m = RX_R21.search(str(t))
    if m:
        falla(f'R-21: «{m.group(0)}» en «…{str(t)[max(0, m.start() - 40):m.end() + 30]}…»')
print(f'  {len(AGUJAS)} agujas · {golpes} golpes en lo que ve el redactor')

# ================================================================ F. redacción segura
print('\n--- redacción segura ---')
for n, frases in FRASES_SEGURAS.items():
    textos = TEXTO_PROMPT.get(('GUIA', n), [])
    blob = norm(' '.join(str(x) for x in textos))
    for fr in frases:
        if norm(fr) not in blob:
            falla(f'GUIA cap {n:02d}: falta la redacción segura «{fr}»')

# ================================================================ G. solape
print('\n--- solape ---')
try:
    hermana = _carga('hermana', HERMANA_PY)
    caps_h = {c['n']: c for c in hermana.CAPITULOS}
except Exception as ex:                                   # pragma: no cover
    caps_h = {}
    avisa(f'no se pudo cargar el guion de la hermana: {ex}')


def puntos_de(cap):
    ppe = cap.get('puntos_por_epigrafe') or {}
    return [p for ps in ppe.values() for p in ps] or list(cap.get('puntos') or [])


pares_h = 0
for n, homs in HOMOLOGOS.items():
    nuestros = PUNTOS_POR_CAP.get(('GUIA', n), [])
    cap_n = next((c for c in CAPITULOS if c['n'] == n), None)
    for h in homs:
        ch = caps_h.get(h)
        if not ch:
            avisa(f'no encuentro el capítulo {h} de la hermana')
            continue
        suyos = puntos_de(ch)
        altos = [(jaccard(a, b), a, b) for a in nuestros for b in suyos]
        altos = [x for x in altos if x[0] >= SOLAPE_HERMANA]
        pares_h += len(altos)
        if len(altos) > 1:
            falla(f'GUIA cap {n:02d}: {len(altos)} puntos solapan con el cap {h} de la '
                  f'hermana (Jaccard ≥ {SOLAPE_HERMANA}): «{altos[0][1][:60]}…»')
        elif altos:
            avisa(f'GUIA cap {n:02d}: 1 punto solapa con el cap {h} de la hermana '
                  f'({altos[0][0]:.2f}): «{altos[0][1][:60]}…»')
        iguales = set(cap_n['epigrafes']) & set(ch.get('epigrafes', [])) if cap_n else set()
        if len(iguales) >= 2:
            falla(f'GUIA cap {n:02d}: {len(iguales)} epígrafes idénticos a los del cap {h} '
                  f'de la hermana: {sorted(iguales)}')
pares_i = 0
lista = [(n, p) for (doc, n), ps in PUNTOS_POR_CAP.items() if doc == 'GUIA' for p in ps]
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        (n1, p1), (n2, p2) = lista[i], lista[j]
        if n1 == n2:
            continue
        s = jaccard(p1, p2)
        if s >= SOLAPE_INTERNO_FALLO:
            falla(f'solape interno {s:.2f} entre los caps {n1} y {n2}: «{p1[:60]}…»')
        elif s >= SOLAPE_INTERNO_AVISO:
            pares_i += 1
            avisa(f'solape interno {s:.2f} entre los caps {n1} y {n2}: «{p1[:60]}…»')
print(f'  pares ≥ {SOLAPE_HERMANA} con la hermana: {pares_h} · internos ≥ '
      f'{SOLAPE_INTERNO_AVISO}: {pares_i}')

# ================================================================ H. libro 6
print('\n--- coherencia del libro 6 ---')
P6 = 'plan-financiero-3-anos-churreria.xlsx'


def v6(h, c):
    return d.celda(XLSX_DIR, f'{P6}!{h}!{c}')


def iguales(a, b, tol=0.01):
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False


CUADRES = [
    ('resultado del crucero: P&L = punto de equilibrio', v6('PyG 3 Años', 'C23'), v6('Punto de Equilibrio', 'B15')),
    ('resultado del crucero: P&L = suma mes a mes', v6('PyG 3 Años', 'C23'), v6('Punto de Equilibrio', 'H35')),
    ('resultado del crucero: P&L = canales', v6('PyG 3 Años', 'C23'), v6('Canales y Punto Muerto', 'C20')),
    ('contribución del crucero: P&L = punto de equilibrio', v6('PyG 3 Años', 'C15'), v6('Punto de Equilibrio', 'B7')),
    ('contribución del crucero: P&L = canales', v6('PyG 3 Años', 'C15'), v6('Canales y Punto Muerto', 'G12')),
    ('inversión total = CAPEX + fondo', v6('Inversión Inicial', 'B24'),
     (v6('Inversión Inicial', 'B22') or 0) + (v6('Inversión Inicial', 'B23') or 0)),
    ('inversión total = préstamo + propios', v6('Inversión Inicial', 'B24'),
     (v6('Inversión Inicial', 'B25') or 0) + (v6('Inversión Inicial', 'B26') or 0)),
    ('saldo del día de apertura = fondo de maniobra', v6('Tesorería 12 meses', 'B32'), v6('Inversión Inicial', 'B19')),
    ('verano elegido: escenarios = P&L', v6('Escenarios', 'B25'), v6('PyG 3 Años', 'C12')),
    ('verano con fijos = contribución - fijos', v6('Escenarios', 'D23'),
     (v6('Escenarios', 'B23') or 0) - (v6('Escenarios', 'C23') or 0)),
]
for nombre, a, b in CUADRES:
    if not iguales(a, b):
        falla(f'libro 6 NO CUADRA ({nombre}): {a} frente a {b}')
# la columna «Base» de Escenarios (filas 6-16) frente al P&L
base_ok = iguales(v6('Escenarios', 'C12'), v6('PyG 3 Años', 'C23'))
cita_base = any(r.startswith(f'{P6}!Escenarios!') and (
    re.search(r'![A-D](?:[6-9]|1[0-6])$', r) or re.search(r'!@(?:[6-9]|1[0-6])-', r))
    for r in REFS_CITADAS)
if not base_ok:
    msg = (f'libro 6, hoja «Escenarios»: la columna Base (C12 = '
           f'{v6("Escenarios", "C12"):.2f}) no es el resultado del crucero del P&L '
           f'(C23 = {v6("PyG 3 Años", "C23"):.2f}); C10 = C8 + C24 suma los fijos '
           'del verano. Es de los libros, no del guion')
    if cita_base:
        falla(msg + ': y el guion CITA esas filas')
    else:
        avisa(msg + ': el guion no cita las filas 6-16 de esa hoja')

# ================================================================ resto
crudo = open(GUION_PY, encoding='utf-8').read()
if d.guard_no_latinos(crudo, 'guion'):
    falla('caracteres no latinos en el propio guion')
g = GUIA['gates']
for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap',
          'cifras_extra', 'cifras_ignorar', 'erratas_permitidas',
          'mortalidad_permitida'):
    if k not in g:
        falla(f'GUIA.gates: falta la clave «{k}»')
if g.get('cifras_ignorar'):
    falla('GUIA.gates.cifras_ignorar NO va vacía: esa clave silencia el gate de '
          'coherencia (la lista negra va en NO_COMUN)')
if not g.get('erratas_permitidas'):
    falla('GUIA.gates: «erratas_permitidas» vacío')
for b in BONUS:
    for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap',
              'meta', 'erratas_permitidas', 'cifras_ignorar'):
        if k not in b['gates']:
            falla(f'{b["nombre"]}.gates: falta la clave «{k}»')
    if not b['gates'].get('erratas_permitidas'):
        falla(f'{b["nombre"]}: «erratas_permitidas» vacío')
    if b['gates'].get('cifras_ignorar'):
        falla(f'{b["nombre"]}: cifras_ignorar no va vacía')

# erratas del propio guion (aviso)
texto_erratas = '\n'.join(str(t) for t in TEXTO_TODO)
try:
    errs = d.erratas_ortograficas(texto_erratas, g.get('erratas_permitidas', ()))
except Exception as ex:                                   # pragma: no cover
    errs = []
    avisa(f'erratas_ortograficas no se pudo correr: {ex}')
for e in errs:
    avisa(f'posible errata «{e["errata"]}» (¿«{e["probable"]}»?) ×{e["veces"]}')

# los ocho libros
presentes = sorted(f for f in os.listdir(XLSX_DIR) if f.endswith('.xlsx'))
faltan_l = [f for f in LIBROS if f not in presentes]
print(f'\nlibros en {XLSX_DIR}: {len(presentes)}')
if faltan_l:
    falla(f'faltan libros: {faltan_l}')

# bloques ya redactados
if args.txt:
    txts = sorted(glob.glob(os.path.join(args.txt, '**', '*.txt'), recursive=True))
    print(f'bloques redactados en {args.txt}: {len(txts)}')
    for p in txts:
        t = open(p, encoding='utf-8').read()
        for ag, origen in agujas_en(t):
            falla(f'{os.path.basename(p)}: AGUJA «{ag}» ({origen})')
        m = RX_R21.search(t)
        if m:
            falla(f'{os.path.basename(p)}: R-21 «{m.group(0)}»')
        for pid_, rx in RX_PROHIBIDO.items():
            if rx.search(t):
                falla(f'{os.path.basename(p)}: id prohibido «{pid_}»')

# ================================================================ informe
ids = sorted({s for c in CAPITULOS for s in c.get('sector', [])}
             | {s for b in BONUS for c in b['capitulos'] for s in c.get('sector', [])})
bajas = [i for i in ids if (idx.get(i) or {}).get('fiabilidad') == 'baja']
pref = collections.Counter(re.match(r'[A-Z]+(?:-IVA)?', i).group(0) for i in ids)
bloques_guia = sum(len(d.trocear(c['epigrafes'], c.get('bloques', 1))) for c in CAPITULOS)
bloques_bonus = bloques_tot - bloques_guia
print('\n=== RESUMEN ===')
print(f'capítulos: guía {len(CAPITULOS)} (16 + anexo) · '
      + ' · '.join(f'{b["nombre"]} {len(b["capitulos"])}' for b in BONUS))
for c in CAPITULOS:
    etq_c = 'A ' if c.get('sin_numerar') else '%02d' % c['n']
    print(f'  {etq_c} · {c["palabras"]:>5} '
          f'palabras · {len(c["epigrafes"])} epígrafes · {len(c["cifras"])} C() · '
          f'{len(c["tablas"])} tablas · {c["titulo"]}')
for b in BONUS:
    for c in b['capitulos']:
        print(f'  {("BP" if b["nombre"] == NOMBRE_BP else "DEC")} {c["n"]} · {c["palabras"]:>5} '
              f'palabras · {len(c["epigrafes"])} epígrafes · {len(c["cifras"])} C() · '
              f'{len(c["tablas"])} tablas · {c["titulo"]}')
print(f'palabras por documento: ' + ' · '.join(f'{k} {v}' for k, v in palabras_doc.items()))
print(f'referencias C() totales: {n_cifras} (anclas {len(anclas)})')
print(f'tablas totales: {n_tablas} · filas construidas: {n_filas}')
print(f'puntos repartidos por epígrafe: {n_puntos}')
print(f'ids de sector distintos usados: {len(ids)} ('
      + ' · '.join(f'{k} {v}' for k, v in sorted(pref.items())) + ')')
print(f'de ellos, de fiabilidad baja (huecos declarados, nunca cifra): {len(bajas)} {bajas}')
print(f'bloques que producirá el pipeline: {bloques_guia} (guía) + {bloques_bonus} '
      f'(bonus) = {bloques_tot}')

if avisos:
    print(f'\nAVISOS ({len(avisos)}):')
    for a in avisos:
        print('  ·', a)

if fallos:
    print(f'\nFALLOS ({len(fallos)}):')
    for f in fallos:
        print('  ✗', f)
    sys.exit(1)

print('\nVERDE: 0 referencias rotas o movidas, 0 celdas vacías, 0 tablas rotas, '
      '0 ids inexistentes o prohibidos, 0 cifras de fiabilidad baja, 0 números '
      'sueltos, 0 agujas de la lista negra, 0 caracteres no latinos; D26 cumplida '
      f'({bloques_tot} bloques).')
