#!/usr/bin/env python3
"""
documentos.py — Pipeline de DOCUMENTOS de la familia «Guías Cómo Montar» v2.0.

Implementa el **§5** de `guias-v2-SPEC.md` (§5.1-§5.6) y las decisiones
§7-bis.6 (la promesa de páginas SE CUMPLE), §7-bis.7 (una sola fuente de
cifras: los xlsx del propio producto), §7-bis.15 (el PDF y el DOCX salen del
MISMO Markdown), §7-bis.18 (la cifra de páginas se MIDE) y §7-bis.21 (las
cifras del sector sólo entran con fuente).

    python3 documentos.py --producto <pid> [--salida <dir>] [--json informe.json]
                          [--solo-capitulos 1,2,3] [--solo-bonus business-plan-modelo]
                          [--saltar-generacion] [--min-palabras-cap 900]

Es el ÚNICO bloque de la familia que **no post-procesa: produce**. Hoy no hay
nada que parchear —2.157 palabras para 22 capítulos en el representante, 255
palabras de «manual de servicio de sala», y en 6 de las 8 guías el PDF es una
portada de una página—, así que el texto se escribe de nuevo.

FLUJO (§5.3)
  guion_<pid>.py  →  por capítulo, N bloques de epígrafes
      → prompt a bridge.py **con las cifras y las tablas del xlsx ya
        RESUELTAS dentro del prompt** (el modelo no lee ficheros: se le dan
        los números medidos, y se le prohíbe inventar otros)
      → un .txt por bloque  →  .md por capítulo
      → barrido de no latinos + erratas (fechas caducas, «60 % cierra»)
      → ensamblado (portada, índice, PageBreak por capítulo, tablas reales)
      → DOCX (python-docx) **y** PDF (reportlab) desde el MISMO Markdown
      → gates §5.6 medidos con PyMuPDF / python-docx.

REGLAS DURAS QUE ESTE FICHERO RESPETA
  1. **PROHIBIDO escribir en `astro-site/public/dl/**`.** Los xlsx de ese
     directorio se abren SIEMPRE en modo lectura (`load_workbook(data_only=True)`)
     y son la única fuente de cifras del producto (§7-bis.7). La salida va
     donde diga `--salida`, y si esa ruta cae dentro de `public/dl/` el script
     ABORTA con exit 2.
  2. **Texto largo SIEMPRE con `bridge.py`.** Este módulo redacta el guion, las
     instrucciones al modelo, las tablas de cifras y el ensamblado; **ni una
     frase del cuerpo**. En este Mac el routing por defecto está desactualizado
     (enruta `content` a `deepseek-v4-pro` y trae `--max-tokens 4096`), así que
     `--model ~deepseek/deepseek-v4-flash-latest` y `--max-tokens 8192` NO son
     opcionales. Medido el 2026-08-29: una petición con `--max-tokens 8192`
     puede agotar el presupuesto razonando y devolver un fichero VACÍO; por eso
     `bridge()` reintenta con presupuestos menores y aborta si nunca hay texto.
  3. **Cifras del sector sólo desde `auditorias/guias-v2-research-sector.json`**,
     con su fuente citada en el texto. Un `id` sin `cifra` o con
     `fiabilidad: baja` es un hueco DELIBERADO: el prompt lo dice y el capítulo
     se reformula sin número.
  4. **Barrido de no latinos sobre cada .md antes de ensamblar** (§5.3.3), más
     `gate-no-latinos.py --only <salida>` al final, fuera de este script.

IDEMPOTENCIA / CACHÉ: cada bloque se cachea en `<salida>/txt/<pid>_capNN_bM.txt`
y no se vuelve a pedir si ya existe y cumple el mínimo de palabras. Para forzar
la regeneración de un capítulo corto basta con borrar sus .txt (o pasar
`--regenerar 9,13,14`), que es exactamente lo que pide §5.6.1: **se amplían los
capítulos más delgados; no se toca la cifra de la landing**.
"""
import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
import unicodedata

# Caracteres tipográficos de la familia, SIEMPRE por escape (CLAUDE.md): al
# pasar por un heredoc del shell degeneran en espacio y guion normales.
NARROW = ' '          # espacio fino antes de las unidades
NOBRK = '‑'           # guion no separable en los rangos

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(AQUI, '..', '..', '..'))
DL = os.path.join(REPO, 'astro-site', 'public', 'dl')
RESEARCH = os.path.join(AQUI, '..', 'auditorias', 'guias-v2-research-sector.json')
BRIDGE = '/Users/johnguerrero/chefbusiness-ai/bridge.py'
MODELO = '~deepseek/deepseek-v4-flash-latest'

# --------------------------------------------------------------------------
# 0. Guardas de seguridad
# --------------------------------------------------------------------------


def guarda_salida(salida):
    """REGLA DURA 1: nunca se escribe dentro de astro-site/public/dl/."""
    real = os.path.realpath(salida)
    if real.startswith(os.path.realpath(DL)):
        print(f'ABORTADO: {real} cae dentro de public/dl/ — los entregables de '
              'producción no se tocan desde aquí (SPEC §5, regla dura 1).',
              file=sys.stderr)
        raise SystemExit(2)
    os.makedirs(salida, exist_ok=True)
    return salida


def istats():
    """REGLA TÉRMICA: el Mac se apaga a 65 °C. Devuelve la temperatura o None."""
    try:
        out = subprocess.run(['istats', 'cpu', 'temp'], capture_output=True,
                             text=True, timeout=20).stdout
        m = re.search(r'([\d.]+)\s*°?C', out)
        return float(m.group(1)) if m else None
    except Exception:
        return None


def respirar(umbral=60.0, espera=90):
    t = istats()
    if t is not None and t >= umbral:
        print(f'  [térmica] {t} °C ≥ {umbral} — durmiendo {espera} s',
              flush=True)
        time.sleep(espera)
    return t


# --------------------------------------------------------------------------
# 1. Idioma y erratas — gates propios sobre el texto crudo (§5.3.3, §5.6.5/7)
# --------------------------------------------------------------------------
RX_NO_LATINOS = re.compile(
    r'[　-〿぀-ヿ㐀-䶿一-鿿'
    r'가-힯Ѐ-ӿ؀-ۿ֐-׿฀-๿]')

# Ventana alrededor del año, como el valida() de fase8c-libreria-assemble.py:
# mirar el texto entero tumbaría un «1982» legítimo de un bloque de historia.
RX_PRECIO = re.compile(
    r'(precio|coste|cuesta|€|EUR|euros|tarifa|presupuesto|inversión|factura|'
    r'tendencia|tendencias)', re.I)
# Citas legales: «RD 1021/2022», «Reglamento (CE) 853/2004», «art. 34.9».
# (Ojo: «RD 1420/2006» ya NO es cita legal aceptada — quedó derogado el
#  22-dic-2022 por el RD 1021/2022; sólo vale dentro de «que derogó el
#  RD 1420/2006». Gate: `motor.PROHIBIDAS`.)
RX_LEGAL_ANTES = re.compile(
    r'(RD|R\.D\.|Real\s+Decreto|RDL|Reglamento|Directiva|Ley|LIS|BOE|Estatuto|'
    r'art\.|artículo|CTE|UNE|ISO|edición|desde|Reg\.)[^.]{0,60}$', re.I)


def guard_no_latinos(texto, etiqueta=''):
    """Aborta con el fragmento de contexto (§5.3.3). Es el mismo defecto que
    puso una Amanita phalloides dentro de un prompt de garum en producción."""
    fallos = []
    for m in RX_NO_LATINOS.finditer(texto):
        ini = max(0, m.start() - 40)
        fallos.append({'char': m.group(0), 'codepoint': f'U+{ord(m.group(0)):04X}',
                       'contexto': texto[ini:m.end() + 40].replace('\n', ' ')})
    if fallos:
        print(f'ABORTADO [{etiqueta}]: {len(fallos)} caracteres no latinos.',
              file=sys.stderr)
        for f in fallos[:10]:
            print(f'   {f["codepoint"]} → …{f["contexto"]}…', file=sys.stderr)
    return fallos


def erratas_fechas(texto):
    """Ningún año anterior a 2026 a menos de 90 caracteres de lenguaje de
    precios o de «tendencias» (§5.6.7), sin tumbar las citas legales."""
    fallos = []
    for m in re.finditer(r'\b(19\d{2}|20[0-2]\d)\b', texto):
        anio = int(m.group(1))
        if anio >= 2026:
            continue
        antes = texto[max(0, m.start() - 60):m.start()]
        if RX_LEGAL_ANTES.search(antes) or re.search(r'\d+/$', antes):
            continue                      # «RD 1021/2022», «853/2004»
        ventana = texto[max(0, m.start() - 90):m.end() + 90]
        if RX_PRECIO.search(ventana):
            fallos.append({'anio': anio,
                           'contexto': ventana.replace('\n', ' ')})
    return fallos


# «el 60 % de los restaurantes cierra el primer año» y familia: cifra de
# mortalidad sin fuente. El research trae supervivencia del INE (SECT-09) y
# cierres (SECT-08); cualquier otra formulación se caza aquí (§5.4).
RX_MORTALIDAD = re.compile(
    r'(\d{1,3})\s*%[^.]{0,80}?(cierran?|fracasan?|no\s+sobreviv|desaparec|'
    r'quiebran?)', re.I)
RX_MORTALIDAD2 = re.compile(
    r'(cierran?|fracasan?|no\s+sobreviv|mueren)[^.]{0,60}?(\d{1,3})\s*%', re.I)


def erratas_mortalidad(texto, permitidos):
    fallos = []
    for rx in (RX_MORTALIDAD, RX_MORTALIDAD2):
        for m in rx.finditer(texto):
            frag = m.group(0)
            if any(p in frag for p in permitidos):
                continue
            fallos.append(frag.replace('\n', ' '))
    return fallos


# --------------------------------------------------------------------------
# 2. Lectura de los xlsx — la única fuente de cifras del producto (§7-bis.7)
# --------------------------------------------------------------------------
_WB = {}


def wb(xlsx_dir, fichero):
    """Workbook cacheado, SIEMPRE en data_only y SIEMPRE de sólo lectura."""
    if fichero not in _WB:
        from openpyxl import load_workbook
        ruta = os.path.join(xlsx_dir, fichero)
        if not os.path.exists(ruta):
            raise SystemExit(f'ABORTADO: falta {ruta}')
        _WB[fichero] = load_workbook(ruta, data_only=True)
    return _WB[fichero]


def celda(xlsx_dir, ref):
    """ref = 'fichero.xlsx!Hoja!C27' → valor. Cita fichero:hoja:celda."""
    fichero, hoja, coord = ref.split('!')
    ws = wb(xlsx_dir, fichero)[hoja]
    return ws[coord].value


def eur(v, dec=0):
    if v is None:
        return ''
    try:
        v = float(v)
    except (TypeError, ValueError):
        return str(v)
    s = f'{v:,.{dec}f}'.replace(',', '\x00').replace('.', ',').replace('\x00', '.')
    return f'{s}{NARROW}€'


def pct(v, dec=1):
    if v is None:
        return ''
    try:
        v = float(v)
    except (TypeError, ValueError):
        return str(v)
    s = f'{v * 100:,.{dec}f}'.replace(',', '\x00').replace('.', ',').replace('\x00', '.')
    return f'{s}{NARROW}%'


def num(v, dec=0):
    if v is None:
        return ''
    try:
        v = float(v)
    except (TypeError, ValueError):
        return str(v)
    return f'{v:,.{dec}f}'.replace(',', '\x00').replace('.', ',').replace('\x00', '.')


FORMATOS = {'eur': eur, 'eur2': lambda v: eur(v, 2), 'pct': pct, 'pct1': pct,
            'pct2': lambda v: pct(v, 2),
            'pct0': lambda v: pct(v, 0), 'num': num, 'num1': lambda v: num(v, 1),
            'num2': lambda v: num(v, 2), 'txt': lambda v: '' if v is None else str(v)}


def formatear(v, fmt):
    if v is None:
        return ''
    if fmt in FORMATOS:
        return FORMATOS[fmt](v)
    return str(v)


def resolver_cifras(xlsx_dir, cifras):
    """[(etiqueta, ref, fmt)] → [(etiqueta, valor_formateado, ref)]."""
    fuera = []
    for etiqueta, ref, fmt in cifras:
        v = celda(xlsx_dir, ref)
        fuera.append((etiqueta, formatear(v, fmt), ref, v))
    return fuera


def construir_tabla(xlsx_dir, t):
    """Devuelve (markdown, n_filas). Dos formas:
       - literal:  {'cabecera': [...], 'filas': [[...], ...]}
       - del xlsx: {'src': ('fichero.xlsx','Hoja'), 'cols': [(titulo, col, fmt)],
                    'filas': (fila_ini, fila_fin), 'saltar_vacias': True}
    """
    if 'cabecera' in t:
        cab, filas = t['cabecera'], [[str(c) for c in f] for f in t['filas']]
    else:
        fichero, hoja = t['src']
        ws = wb(xlsx_dir, fichero)[hoja]
        cab = [c[0] for c in t['cols']]
        filas = []
        ini, fin = t['filas']
        for r in range(ini, fin + 1):
            fila = []
            for _tit, col, fmt in t['cols']:
                if col.startswith('='):          # literal por columna
                    fila.append(col[1:])
                    continue
                fila.append(formatear(ws[f'{col}{r}'].value, fmt))
            if t.get('saltar_vacias', True) and not any(x for x in fila[1:]):
                continue
            filas.append(fila)
        for extra in t.get('extra_filas', []):
            filas.append([str(x) for x in extra])
    md = ['| ' + ' | '.join(cab) + ' |',
          '|' + '|'.join(['---'] * len(cab)) + '|']
    for f in filas:
        f = list(f) + [''] * (len(cab) - len(f))
        md.append('| ' + ' | '.join(x.replace('|', '/') for x in f[:len(cab)]) + ' |')
    return '\n'.join(md), len(filas)


# --------------------------------------------------------------------------
# 3. Research del sector (§7-bis.21) — sin fuente, no entra
# --------------------------------------------------------------------------


def cargar_research(path=RESEARCH, esperar_min=20):
    """Espera con sleep(60) hasta `esperar_min` minutos si aún no existe."""
    esperado = 0
    while not os.path.exists(path) and esperado < esperar_min * 60:
        print(f'  [research] aún no existe {path}; esperando 60 s '
              f'({esperado // 60}/{esperar_min} min)', flush=True)
        time.sleep(60)
        esperado += 60
    if not os.path.exists(path):
        print('  [research] NO llegó: los capítulos se escriben sin cifra de '
              'sector (reformuladas). Anotado en el informe.', flush=True)
        return {'_meta': {'ausente': True}, 'datos': []}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def indexar_research(res):
    return {d['id']: d for d in res.get('datos', [])}


def bloque_research(idx, ids, breve=False):
    """Texto para el prompt: cada cifra con su fuente. Los ids sin cifra o de
    fiabilidad baja se declaran como HUECO y el modelo debe reformular."""
    lineas, usados, huecos = [], [], []
    for i in ids:
        d = idx.get(i)
        if d is None:
            huecos.append(i)
            continue
        if d.get('cifra') is None or d.get('fiabilidad') == 'baja' or not d.get('url'):
            huecos.append(i)
            lineas.append(f'- [{i}] HUECO SIN FUENTE — «{d["dato"]}»: NO escribas '
                          'ninguna cifra sobre esto; formúlalo en cualitativo.')
            continue
        cifra = d['cifra']
        unidad = d.get('unidad') or ''
        lineas.append(
            f'- [{i}] {d["dato"]}: **{cifra} {unidad}**. Fuente obligatoria a citar '
            f'en el texto: «{d["fuente_titulo"][:110]}» '
            f'({d.get("fecha_publicacion") or d.get("anio_del_dato")}). '
            + ('' if breve else f'Nota: {(d.get("nota") or "-")[:240]}'))
        usados.append(i)
    return '\n'.join(lineas), usados, huecos


# --------------------------------------------------------------------------
# 4. bridge.py — el motor de redacción (regla capital)
# --------------------------------------------------------------------------
SYSTEM = (
    'Eres John Guerrero, chef desde los 17 años y consultor gastronómico desde '
    '2010, con más de 200 aperturas asesoradas en España. Escribes en español '
    'de España, en primera persona del plural o impersonal, con tono humano y '
    'profesional, para un lector que va a jugarse su dinero. '
    'REGLAS ABSOLUTAS: (1) NO inventes NINGUNA cifra: usa exclusivamente las '
    'que te doy en el prompt, con el mismo formato; si necesitas un número que '
    'no está en la lista, escribe la frase en cualitativo. (2) Escribe SOLO en '
    'alfabeto latino: ni un carácter chino, japonés, coreano, cirílico, árabe, '
    'hebreo ni tailandés, ni siquiera dentro de un paréntesis o de una cita. '
    '(3) Nada de introducciones meta ("en este capítulo veremos"), nada de '
    'conclusiones que resuman lo dicho, nada de adjetivos de relleno. Prosa '
    'densa: cada párrafo tiene que aportar un dato, un procedimiento o una '
    'decisión. (4) No escribas tablas Markdown ni encabezados de nivel 1 o 2: '
    'las tablas y los títulos los pone el maquetador. (5) No cites años '
    'anteriores a 2026 junto a precios ni a tendencias. (6) Nunca digas que un '
    'porcentaje de restaurantes "cierra" o "fracasa" salvo que la cifra te la '
    'haya dado yo con su fuente.')


_MT_QUE_FUNCIONA = []


def bridge(prompt, salida_txt, palabras_min, max_tokens=8192, intentos=6,
           temperatura=0.45, verbose=True, prompt_corto=None):
    """Llama a bridge.py. Medido el 2026-08-29: con --max-tokens 8192 el modelo
    puede agotar el presupuesto razonando y devolver un fichero VACÍO, y la API
    devuelve contenido vacío con rc=0 de forma intermitente (tres veces
    seguidas en el capítulo 1, y el MISMO prompt funcionó a la cuarta). Por eso
    se reintenta con presupuestos distintos, con espera entre intentos y
    variando la temperatura: un vacío no es un fallo del prompt."""
    # MEDIDO el 2026-08-29 en este Mac: con `--max-tokens 8192` este modelo
    # devuelve contenido VACÍO de forma sistemática (0 palabras en TODOS los
    # primeros intentos de los 4 primeros capítulos) y con 6000 responde. Se
    # intenta primero el presupuesto que ya funcionó en esta ejecución para no
    # quemar una llamada por bloque; si aún no hay ninguno, se prueba 8192
    # (que es lo que manda la regla) y se cae a 6000.
    presupuestos = [max_tokens, 6000, 8192, 5000, 7000, 4500][:intentos]
    if _MT_QUE_FUNCIONA:
        pref = _MT_QUE_FUNCIONA[-1]
        presupuestos = [pref] + [x for x in presupuestos if x != pref]
    texto = ''
    for k, mt in enumerate(presupuestos):
        if k:
            time.sleep(15)
        respirar()
        cmd = [sys.executable, BRIDGE, '--task', 'content', '--domain', 'aichef',
               '--lang', 'es', '--model', MODELO, '--max-tokens', str(mt),
               '--temperature', str(round(temperatura + 0.05 * (k % 3), 2)),
               '--system', SYSTEM,
               # a partir del 3.er intento se manda la versión CORTA del guion:
               # los prompts que más fallan son los que llevan 18 fichas de
               # research con sus notas, y acortar el prompt los desatasca.
               '--prompt', (prompt_corto or prompt) if k >= 2 else prompt,
               '--output', salida_txt]
        r = subprocess.run(cmd, capture_output=True, text=True)
        texto = ''
        if os.path.exists(salida_txt):
            with open(salida_txt, encoding='utf-8') as f:
                texto = f.read().strip()
        n = len(texto.split())
        if verbose:
            print(f'    bridge intento {k + 1}/{len(presupuestos)} '
                  f'(max_tokens={mt}) → {n} palabras', flush=True)
        if n >= palabras_min:
            if mt not in _MT_QUE_FUNCIONA:
                _MT_QUE_FUNCIONA.append(mt)
            return texto
        if r.returncode != 0 and verbose:
            print(f'    bridge rc={r.returncode} :: {r.stderr.strip()[:300]}',
                  flush=True)
    if texto:
        return texto                      # corto pero no vacío: se avisa arriba
    raise SystemExit(f'ABORTADO: bridge.py no devolvió texto para {salida_txt}')


# --------------------------------------------------------------------------
# 5. Prompts de capítulo (§5.2) — el guion cerrado, no un título
# --------------------------------------------------------------------------


def prompt_bloque(cap, bloque_epigrafes, palabras, ctx_cifras, ctx_sector,
                  guia, es_ultimo):
    partes = []
    partes.append(
        f'Escribe un tramo del capítulo {cap["n"]} — «{cap["titulo"]}» de la '
        f'guía profesional «{guia["titulo"]}» ({guia["subtitulo"]}).')
    partes.append(f'OBJETIVO DEL CAPÍTULO: {cap["objetivo"]}')
    partes.append(
        'ESCRIBE EXACTAMENTE ESTOS EPÍGRAFES, cada uno como encabezado '
        'Markdown de nivel 3 (### ) con ese título literal, en este orden:\n'
        + '\n'.join(f'  ### {e}' for e in bloque_epigrafes))
    partes.append(f'EXTENSIÓN: unas {palabras} palabras en total para este tramo, '
                  'repartidas entre esos epígrafes. Prosa + listas con viñetas '
                  'cuando aporten; nunca tablas.')
    if cap.get('puntos'):
        partes.append('PUNTOS OBLIGATORIOS (tienen que aparecer, con su detalle '
                      'operativo):\n' + '\n'.join(f'  - {p}' for p in cap['puntos']))
    if ctx_cifras:
        partes.append(
            'CIFRAS DEL PROPIO PRODUCTO — son las ÚNICAS cifras de negocio que '
            'puedes escribir, y van tal cual (mismo separador de miles y misma '
            'coma decimal). Salen de las plantillas Excel que el lector tiene '
            'en el mismo pack, así que el texto y las hojas de cálculo tienen '
            'que decir lo mismo:\n' + ctx_cifras)
    if ctx_sector:
        partes.append(
            'DATOS DEL SECTOR — cada uno se cita CON SU FUENTE dentro del texto '
            '(entre paréntesis, con el nombre de la fuente y el año). Los '
            'marcados como HUECO SIN FUENTE no se escriben con número:\n'
            + ctx_sector)
    if cap.get('tablas_anunciadas'):
        partes.append(
            'En este capítulo el maquetador insertará estas tablas DESPUÉS de '
            'tu texto: ' + '; '.join(cap['tablas_anunciadas']) +
            '. Puedes referirte a ellas («la tabla de abajo»), pero NO las '
            'escribas tú.')
    if cap.get('prohibido'):
        partes.append('LO QUE NO DEBES DECIR (son errores reales de la edición '
                      'anterior de esta guía y no se pueden repetir):\n'
                      + '\n'.join(f'  - {p}' for p in cap['prohibido']))
    partes.append(
        'FORMATO: empieza directamente por el primer «### ». No pongas título '
        'de capítulo, ni resumen inicial, ni cierre.'
        + ('' if es_ultimo else ' No cierres el capítulo: sigue otro tramo.'))
    return '\n\n'.join(partes)


def trocear(epigrafes, n_bloques):
    n_bloques = max(1, min(n_bloques, len(epigrafes)))
    tam = (len(epigrafes) + n_bloques - 1) // n_bloques
    return [epigrafes[i:i + tam] for i in range(0, len(epigrafes), tam)]


def limpiar_bloque(texto):
    """El modelo a veces devuelve H1/H2, una tabla o un preámbulo meta."""
    lineas = []
    for ln in texto.split('\n'):
        s = ln.strip()
        if s.startswith('# ') or s.startswith('## '):
            s = '### ' + s.lstrip('#').strip()
            ln = s
        if s.startswith('```'):
            continue
        lineas.append(ln)
    txt = '\n'.join(lineas)
    txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
    # quita un preámbulo antes del primer ###
    i = txt.find('### ')
    if i > 0:
        txt = txt[i:]
    return txt


# --------------------------------------------------------------------------
# 6. Generación y ensamblado
# --------------------------------------------------------------------------


def generar_capitulo(cap, guia, xlsx_dir, idx_research, dir_txt, forzar=False):
    cifras = resolver_cifras(xlsx_dir, cap.get('cifras', []))
    ctx_cifras = '\n'.join(f'  - {e}: {v}   [fuente: {r}]' for e, v, r, _ in cifras)
    ctx_sector, usados, huecos = bloque_research(idx_research, cap.get('sector', []))
    ctx_sector_breve, _, _ = bloque_research(idx_research, cap.get('sector', []),
                                             breve=True)

    tablas = []
    for t in cap.get('tablas', []):
        md, nf = construir_tabla(xlsx_dir, t)
        tablas.append((t.get('titulo', ''), md, nf, t.get('nota')))
    cap['tablas_anunciadas'] = [t[0] for t in tablas]

    bloques = trocear(cap['epigrafes'], cap.get('bloques', 2))
    por_bloque = max(500, int(cap['palabras'] / len(bloques)))
    piezas = []
    for i, epis in enumerate(bloques):
        ruta = os.path.join(dir_txt, f'cap{cap["n"]:02d}_b{i + 1}.txt')
        if os.path.exists(ruta) and not forzar:
            with open(ruta, encoding='utf-8') as f:
                t = f.read().strip()
            if len(t.split()) >= por_bloque * 0.6:
                print(f'  cap {cap["n"]:02d} bloque {i + 1}: caché '
                      f'({len(t.split())} palabras)', flush=True)
                piezas.append(limpiar_bloque(t))
                continue
        p = prompt_bloque(cap, epis, por_bloque, ctx_cifras, ctx_sector, guia,
                          es_ultimo=(i == len(bloques) - 1))
        print(f'  cap {cap["n"]:02d} bloque {i + 1}/{len(bloques)} '
              f'({por_bloque} palabras objetivo)', flush=True)
        p_corto = prompt_bloque(cap, epis, por_bloque, ctx_cifras,
                                ctx_sector_breve, guia,
                                es_ultimo=(i == len(bloques) - 1))
        t = bridge(p, ruta, palabras_min=int(por_bloque * 0.72),
                   prompt_corto=p_corto)
        piezas.append(limpiar_bloque(t))

    cuerpo = '\n\n'.join(piezas)
    md = [f'## {cap["n"]}. {cap["titulo"]}', '', cuerpo]
    for titulo, tabla_md, _nf, nota in tablas:
        md += ['', f'**{titulo}**', '', tabla_md]
        if nota:
            md += ['', f'*{nota}*']
    return '\n'.join(md) + '\n', {'n': cap['n'], 'titulo': cap['titulo'],
                                  'tablas': len(tablas), 'sector_usado': usados,
                                  'sector_huecos': huecos,
                                  'cifras': [(e, v, r) for e, v, r, _ in cifras]}


def portada_e_indice(guia, capitulos):
    hoy = guia.get('fecha', 'agosto de 2026')
    p = [f'# {guia["titulo"]}', '',
         f'**{guia["subtitulo"]}**', '',
         f'*{guia["autor_linea"]}*', '',
         guia['portada_texto'], '',
         f'**Versión 2.0 · {hoy} · aichef.pro/{guia["pid"]}**', '',
         '---', '', '## Índice', '']
    for c in capitulos:
        p.append(f'{c["n"]}. **{c["titulo"]}** — {c["resumen_indice"]}')
    p += ['', '---', '']
    return '\n'.join(p)


def cierre(guia):
    return '\n'.join([
        '', '---', '', '## Sobre el autor y condiciones de uso', '',
        guia['bio'], '',
        f'**Versión 2.0 · agosto de 2026 · aichef.pro/{guia["pid"]} · info@aichef.pro**', '',
        guia['legal'], ''])


# --------------------------------------------------------------------------
# 7. Maquetado — DOCX + PDF desde el MISMO Markdown (§7-bis.15)
#    Patrón de kit-escandallos-v2_0/bono_guia.py, extendido con PageBreak,
#    portada, índice y metadatos.
# --------------------------------------------------------------------------
GOLD = '#B8860B'
DARK = '#1A1A1A'

MAPA_WINANSI = {
    '☐': '[  ]', '☑': '[X]', '☒': '[X]', '✅': 'OK',
    '✔': 'OK', '❌': 'X', '✖': 'X', '⭐': '*', '★': '*',
    '→': '->', '←': '<-', '─': '-', '━': '-',
    '−': '-', ' ': ' ', ' ': ' ',
    NARROW: ' ', NOBRK: '-',
    '–': '-', '—': '-', '…': '...',
    '\U0001F534': '', '\U0001F7E2': '', '\U0001F7E1': '',
}


def sanear(texto):
    if not isinstance(texto, str):
        return texto
    fuera = []
    for ch in texto:
        if ch in MAPA_WINANSI:
            fuera.append(MAPA_WINANSI[ch])
            continue
        try:
            ch.encode('cp1252')
        except UnicodeEncodeError:
            # último recurso: descomponer (ǎ → a) antes de descartar
            d = unicodedata.normalize('NFKD', ch).encode('ascii', 'ignore').decode()
            fuera.append(d)
            continue
        fuera.append(ch)
    return ''.join(fuera)


def sanear_bloques(bloques):
    fuera = []
    for tipo, contenido in bloques:
        if isinstance(contenido, str):
            contenido = sanear(contenido)
        elif tipo == 'table':
            contenido = [[re.sub(r'\s{2,}', ' ', sanear(c)).strip() for c in fila]
                         for fila in contenido]
        elif isinstance(contenido, list):
            contenido = [sanear(x) for x in contenido]
        fuera.append((tipo, contenido))
    return fuera


def restos_no_winansi(bloques):
    malos = {}
    for _, contenido in bloques:
        if isinstance(contenido, str):
            trozos = [contenido]
        elif isinstance(contenido, list) and contenido and isinstance(contenido[0], list):
            trozos = [c for fila in contenido for c in fila]
        elif isinstance(contenido, list):
            trozos = [x for x in contenido if isinstance(x, str)]
        else:
            continue
        for t in trozos:
            for ch in t:
                try:
                    ch.encode('cp1252')
                except UnicodeEncodeError:
                    malos[ch] = malos.get(ch, 0) + 1
    return malos


def parsear(md_text):
    lineas = md_text.split('\n')
    bloques = []
    i, n = 0, len(lineas)
    while i < n:
        linea = lineas[i].rstrip()
        if not linea.strip():
            i += 1
            continue
        if linea.strip() == '---':
            bloques.append(('hr', None))
            i += 1
            continue
        if linea.startswith('#### '):
            bloques.append(('h4', linea[5:].strip())); i += 1; continue
        if linea.startswith('### '):
            bloques.append(('h3', linea[4:].strip())); i += 1; continue
        if linea.startswith('## '):
            bloques.append(('h2', linea[3:].strip())); i += 1; continue
        if linea.startswith('# '):
            bloques.append(('h1', linea[2:].strip())); i += 1; continue
        if linea.strip().startswith('```'):
            codigo = []
            i += 1
            while i < n and not lineas[i].strip().startswith('```'):
                codigo.append(lineas[i]); i += 1
            i += 1
            bloques.append(('code', '\n'.join(codigo)))
            continue
        if linea.strip().startswith('|') and i + 1 < n and \
                re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lineas[i + 1]) and '-' in lineas[i + 1]:
            filas = [linea]
            i += 2
            while i < n and lineas[i].strip().startswith('|'):
                filas.append(lineas[i]); i += 1
            tabla = [[c.strip() for c in f.strip().strip('|').split('|')] for f in filas]
            bloques.append(('table', tabla))
            continue
        if re.match(r'^\s*[-*]\s+', linea):
            items = []
            while i < n and re.match(r'^\s*[-*]\s+', lineas[i]):
                items.append(re.sub(r'^\s*[-*]\s+', '', lineas[i].rstrip())); i += 1
            bloques.append(('ul', items))
            continue
        if re.match(r'^\s*\d+\.\s+', linea):
            items = []
            while i < n and re.match(r'^\s*\d+\.\s+', lineas[i]):
                items.append(re.sub(r'^\s*\d+\.\s+', '', lineas[i].rstrip())); i += 1
            bloques.append(('ol', items))
            continue
        parrafo = [linea]
        i += 1
        while i < n and lineas[i].strip() and not lineas[i].startswith('#') and \
                lineas[i].strip() != '---' and not lineas[i].strip().startswith('```') and \
                not lineas[i].strip().startswith('|') and \
                not re.match(r'^\s*[-*]\s+', lineas[i]) and \
                not re.match(r'^\s*\d+\.\s+', lineas[i]):
            parrafo.append(lineas[i].rstrip()); i += 1
        bloques.append(('p', ' '.join(parrafo)))
    return bloques


RX_CURSIVA_PARRAFO = re.compile(r'^\*(?!\*)(.+?)(?<!\*)\*$', re.S)


def cursiva_entera(texto):
    if not isinstance(texto, str):
        return texto, False
    m = RX_CURSIVA_PARRAFO.match(texto.strip())
    if m and '*' not in m.group(1):
        return m.group(1).strip(), True
    return texto, False


def negrita_runs(texto):
    partes = re.split(r'(\*\*[^*]+\*\*)', texto)
    runs = []
    for p in partes:
        if not p:
            continue
        if p.startswith('**') and p.endswith('**'):
            runs.append((p[2:-2], True))
        else:
            runs.append((p, False))
    return runs


def construir_docx(bloques, salida_docx, meta):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.shared import Pt, Cm, RGBColor

    doc = Document()
    est = doc.styles['Normal']
    est.font.name = 'Calibri'
    est.font.size = Pt(10.5)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(2.2)
        s.left_margin = s.right_margin = Cm(2.2)

    def runs(p, texto, negrita_base=False):
        for t, b in negrita_runs(texto):
            r = p.add_run(t)
            r.bold = b or negrita_base

    primero_h1 = True
    for tipo, contenido in bloques:
        if tipo == 'h1':
            if primero_h1:
                h = doc.add_heading(contenido, level=0)
                h.alignment = WD_ALIGN_PARAGRAPH.CENTER
                primero_h1 = False
            else:
                doc.add_heading(contenido, level=1)
        elif tipo == 'h2':
            doc.add_heading(contenido, level=1)
        elif tipo == 'h3':
            doc.add_heading(contenido, level=2)
        elif tipo == 'h4':
            doc.add_heading(contenido, level=3)
        elif tipo == 'p':
            limpio, es_cursiva = cursiva_entera(contenido)
            p = doc.add_paragraph()
            if es_cursiva:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(limpio)
                r.italic = True
                r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
            else:
                runs(p, contenido)
        elif tipo == 'ul':
            for it in contenido:
                runs(doc.add_paragraph(style='List Bullet'), it)
        elif tipo == 'ol':
            for it in contenido:
                runs(doc.add_paragraph(style='List Number'), it)
        elif tipo == 'code':
            p = doc.add_paragraph()
            r = p.add_run(contenido)
            r.font.name = 'Courier New'
            r.font.size = Pt(9.5)
        elif tipo == 'table':
            filas = contenido
            ncols = len(filas[0])
            tabla = doc.add_table(rows=0, cols=ncols)
            tabla.style = 'Light Grid Accent 1'
            for fi, fila in enumerate(filas):
                row = tabla.add_row()
                for ci in range(ncols):
                    valor = fila[ci] if ci < len(fila) else ''
                    cell = row.cells[ci]
                    cell.text = ''
                    runs(cell.paragraphs[0], valor, negrita_base=(fi == 0))
            doc.add_paragraph()
        elif tipo == 'hr':
            # §7-bis.15: el salto de página es el MISMO en los dos formatos
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    cp = doc.core_properties
    cp.author = meta['author']
    cp.last_modified_by = meta['author']
    cp.title = meta['title']
    cp.subject = meta['subject']
    cp.category = meta.get('category', 'Guía profesional')
    cp.comments = meta.get('comments', '')
    doc.save(salida_docx)
    return salida_docx


def _md_a_html(texto):
    texto = texto.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    texto = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', texto)
    texto = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', texto)
    return texto


def construir_pdf(bloques, salida_pdf, meta):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import cm
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                    TableStyle, ListFlowable, ListItem,
                                    Preformatted, PageBreak, KeepTogether)

    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('H1c', parent=styles['Title'], fontName='Helvetica-Bold',
                        fontSize=24, leading=29, textColor=colors.HexColor(DARK),
                        spaceAfter=6, alignment=1)
    h2 = ParagraphStyle('H2c', parent=styles['Heading2'], fontName='Helvetica-Bold',
                        fontSize=16, leading=20, textColor=colors.HexColor(GOLD),
                        spaceBefore=12, spaceAfter=9)
    h3 = ParagraphStyle('H3c', parent=styles['Heading3'], fontName='Helvetica-Bold',
                        fontSize=12.5, leading=16, textColor=colors.HexColor(DARK),
                        spaceBefore=10, spaceAfter=6)
    h4 = ParagraphStyle('H4c', parent=h3, fontSize=11, leading=14,
                        textColor=colors.HexColor('#444444'))
    pst = ParagraphStyle('Pc', parent=styles['Normal'], fontName='Helvetica',
                         fontSize=10.2, leading=14.5, spaceAfter=8, alignment=4)
    li = ParagraphStyle('Lic', parent=pst, spaceAfter=3)
    firma = ParagraphStyle('Firma', parent=pst, fontName='Helvetica-Oblique',
                           alignment=1, textColor=colors.HexColor('#444444'),
                           spaceBefore=10)
    code = ParagraphStyle('Codec', parent=styles['Code'], fontName='Courier',
                          fontSize=9, leading=12,
                          backColor=colors.HexColor('#F5F5F5'),
                          borderPadding=6, spaceAfter=10)

    flujo = []
    primero_h1 = True
    for tipo, contenido in bloques:
        if tipo == 'h1':
            flujo.append(Paragraph(_md_a_html(contenido), h1 if primero_h1 else h2))
            primero_h1 = False
        elif tipo == 'h2':
            flujo.append(Paragraph(_md_a_html(contenido), h2))
        elif tipo == 'h3':
            flujo.append(Paragraph(_md_a_html(contenido), h3))
        elif tipo == 'h4':
            flujo.append(Paragraph(_md_a_html(contenido), h4))
        elif tipo == 'p':
            limpio, es_cursiva = cursiva_entera(contenido)
            flujo.append(Paragraph(_md_a_html(limpio), firma if es_cursiva else pst))
        elif tipo == 'ul':
            flujo.append(ListFlowable(
                [ListItem(Paragraph(_md_a_html(x), li), leftIndent=6) for x in contenido],
                bulletType='bullet', start='•', leftIndent=16, spaceAfter=8))
        elif tipo == 'ol':
            flujo.append(ListFlowable(
                [ListItem(Paragraph(_md_a_html(x), li), leftIndent=6) for x in contenido],
                bulletType='1', leftIndent=16, spaceAfter=8))
        elif tipo == 'code':
            flujo.append(Preformatted(contenido, code))
        elif tipo == 'table':
            filas = contenido
            ncols = max(len(f) for f in filas)
            fs = 8.6 if ncols <= 5 else (7.6 if ncols <= 7 else 6.8)
            data = [[Paragraph(_md_a_html(f[c] if c < len(f) else ''),
                               ParagraphStyle('Cellc', parent=pst, fontSize=fs,
                                              leading=fs + 2.4, alignment=0,
                                              spaceAfter=0,
                                              fontName='Helvetica-Bold' if fi == 0
                                              else 'Helvetica'))
                     for c in range(ncols)] for fi, f in enumerate(filas)]
            ancho = A4[0] - 4 * cm
            t = Table(data, colWidths=[ancho / ncols] * ncols, repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(GOLD)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#DDDDDD')),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1),
                 [colors.white, colors.HexColor('#FAFAFA')]),
                ('LEFTPADDING', (0, 0), (-1, -1), 4),
                ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 3),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ]))
            flujo.append(t)
            flujo.append(Spacer(1, 10))
        elif tipo == 'hr':
            flujo.append(PageBreak())

    def cabecera_pie(canv, doc_):
        canv.saveState()
        ancho, alto = A4
        canv.setFont('Helvetica', 8)
        canv.setFillColor(colors.HexColor('#888888'))
        canv.drawString(2 * cm, alto - 1.3 * cm, meta['cabecera'])
        canv.drawRightString(ancho - 2 * cm, 1.2 * cm, f'Página {doc_.page}')
        canv.drawString(2 * cm, 1.2 * cm, meta['pie'])
        canv.setStrokeColor(colors.HexColor('#DDDDDD'))
        canv.line(2 * cm, alto - 1.5 * cm, ancho - 2 * cm, alto - 1.5 * cm)
        canv.restoreState()

    doc = SimpleDocTemplate(salida_pdf, pagesize=A4, topMargin=2.2 * cm,
                            bottomMargin=2 * cm, leftMargin=2 * cm,
                            rightMargin=2 * cm, title=meta['title'],
                            author=meta['author'], subject=meta['subject'],
                            creator=meta['author'])
    doc.build(flujo, onFirstPage=cabecera_pie, onLaterPages=cabecera_pie)
    return salida_pdf


def maquetar(md_text, base_sin_ext, meta):
    """Markdown → (docx, pdf). Los DOS salen del MISMO Markdown (§7-bis.15)."""
    bloques = parsear(md_text)
    antes = restos_no_winansi(bloques)
    bloques = sanear_bloques(bloques)
    quedan = restos_no_winansi(bloques)
    if quedan:
        detalle = ', '.join(f'{c!r} (U+{ord(c):04X}) x{n}' for c, n in sorted(quedan.items()))
        print('ABORTADO: caracteres que Helvetica pintaría como cuadrado negro '
              f'→ {detalle}. Añádelos a MAPA_WINANSI.', file=sys.stderr)
        raise SystemExit(3)
    docx = construir_docx(bloques, base_sin_ext + '.docx', meta)
    pdf = construir_pdf(bloques, base_sin_ext + '.pdf', meta)
    return docx, pdf, sum(antes.values())


# --------------------------------------------------------------------------
# 8. Gates §5.6 — medidos, no estimados
# --------------------------------------------------------------------------


def texto_pdf(path):
    import fitz
    doc = fitz.open(path)
    return doc, '\n'.join(p.get_text() for p in doc)


def texto_docx(path):
    from docx import Document
    d = Document(path)
    partes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            partes += [c.text for c in row.cells]
    return d, '\n'.join(partes)


def palabras(t):
    return len([w for w in re.split(r'\s+', t) if w.strip()])


def valores_admitidos(xlsx_dir, idx_research, extra=()):
    """Toda cifra del texto tiene que existir en una celda de los xlsx del
    producto o en el research (§5.6.8). Se generan las variantes de formato
    con las que un redactor la escribiría."""
    vals = set()

    def mete(v):
        if v is None or isinstance(v, bool):
            return
        try:
            f = float(v)
        except (TypeError, ValueError):
            return
        if abs(f) < 1e-9:
            return
        for dec in (0, 1, 2):
            vals.add(num(f, dec))
            vals.add(num(round(f), 0))
        if 0 < abs(f) <= 1:
            for dec in (0, 1, 2):
                vals.add(num(f * 100, dec))
        if abs(f) >= 1000:
            vals.add(num(f / 1000, 0)); vals.add(num(f / 1000, 1))
            vals.add(num(f / 1000, 2))
        if abs(f) >= 1_000_000:
            vals.add(num(f / 1_000_000, 0)); vals.add(num(f / 1_000_000, 1))
            vals.add(num(f / 1_000_000, 2))

    import glob
    from openpyxl import load_workbook
    for ruta in sorted(glob.glob(os.path.join(xlsx_dir, '*.xlsx'))):
        w = load_workbook(ruta, data_only=True)
        for ws in w.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    mete(c.value)
                    if isinstance(c.value, str):
                        for m in re.finditer(r'\d[\d.,]*', c.value):
                            vals.add(m.group(0))
    for d in idx_research.values():
        mete(d.get('cifra'))
        if isinstance(d.get('cifra'), str):
            for m in re.finditer(r'\d[\d.,]*', d['cifra']):
                vals.add(m.group(0))
    for e in extra:
        vals.add(str(e))
        mete(e)
    return vals


RX_CIFRA_GRANDE = re.compile(r'\b\d{1,3}(?:\.\d{3})+(?:,\d+)?\b')


def coherencia_cifras(md_text, admitidos, ignorar=()):
    """Cada cifra «de dinero» del texto (con separador de miles) tiene que
    existir en una celda del xlsx o en el research. Devuelve la lista de las
    que no, con su contexto: es un informe, no una adivinanza."""
    fallos, vistas = [], set()
    for m in RX_CIFRA_GRANDE.finditer(md_text):
        s = m.group(0)
        if s in admitidos or s in ignorar or s in vistas:
            continue
        vistas.add(s)
        ini = max(0, m.start() - 70)
        fallos.append({'cifra': s,
                       'contexto': md_text[ini:m.end() + 70].replace('\n', ' ')})
    return fallos


def gates(md_text, docx_path, pdf_path, cfg, xlsx_dir, idx_research):
    doc_pdf, t_pdf = texto_pdf(pdf_path)
    d_docx, t_docx = texto_docx(docx_path)
    n_pdf, n_docx = palabras(t_pdf), palabras(t_docx)
    caps = re.findall(r'^## (\d+)\. (.+)$', md_text, re.M)
    tablas_md = len(re.findall(r'^\|[^\n]*\|\s*\n\|[\s:|-]+\|', md_text, re.M))

    # palabras por capítulo
    trozos = re.split(r'^## ', md_text, flags=re.M)
    por_cap = {}
    for tr in trozos[1:]:
        m = re.match(r'(\d+)\. (.+)', tr.split('\n')[0])
        if m:
            por_cap[int(m.group(1))] = palabras(tr)
    cortos = {k: v for k, v in por_cap.items() if v < cfg.get('min_palabras_cap', 900)}

    # tablas ancladas: ninguna tabla después del último ##
    ult = md_text.rfind('\n## ')
    cola = md_text[ult:] if ult > 0 else ''
    tabla_en_cola = bool(re.search(r'^\|[^\n]*\|\s*\n\|[\s:|-]+\|', cola, re.M))
    ult_tabla = md_text.rfind('\n| ')
    tabla_tras_ultimo_cap = ult_tabla > ult and ult > 0 and \
        'Sobre el autor' not in md_text[ult:ult + 80]

    # títulos de capítulo presentes en el PDF
    norm = lambda s: re.sub(r'\s+', ' ', s).strip().lower()
    t_pdf_n = norm(t_pdf)
    faltan_en_pdf = [t for _, t in caps if norm(t)[:38] not in t_pdf_n]

    admitidos = valores_admitidos(xlsx_dir, idx_research, cfg.get('cifras_extra', ()))
    incoherentes = coherencia_cifras(md_text, admitidos, cfg.get('cifras_ignorar', ()))

    r = {
        'paginas_pdf': doc_pdf.page_count,
        'paginas_prometidas': cfg['paginas_prometidas'],
        'palabras_md': palabras(md_text),
        'palabras_pdf': n_pdf,
        'palabras_docx': n_docx,
        'palabras_objetivo': cfg['palabras_objetivo'],
        'capitulos': len(caps),
        'tablas_md': tablas_md,
        'tablas_docx': len(d_docx.tables),
        'capitulos_cortos': cortos,
        'no_latinos_md': len(guard_no_latinos(md_text, 'md')),
        'no_latinos_pdf': len(RX_NO_LATINOS.findall(t_pdf)),
        'no_latinos_docx': len(RX_NO_LATINOS.findall(t_docx)),
        'fechas_caducas': erratas_fechas(md_text),
        'mortalidad_sin_fuente': erratas_mortalidad(
            md_text, cfg.get('mortalidad_permitida', [])),
        'tabla_tras_ultimo_capitulo': bool(tabla_tras_ultimo_cap and tabla_en_cola),
        'titulos_ausentes_en_pdf': faltan_en_pdf,
        'cifras_no_encontradas': incoherentes,
        'meta_pdf': {'author': doc_pdf.metadata.get('author'),
                     'title': doc_pdf.metadata.get('title')},
    }
    d = __import__('docx').Document(docx_path).core_properties
    r['meta_docx'] = {'author': d.author, 'title': d.title}
    dif = abs(n_pdf - n_docx) / max(1, max(n_pdf, n_docx))
    r['paridad_palabras_pct'] = round(dif * 100, 2)

    r['ok'] = {
        'paginas': doc_pdf.page_count >= cfg['paginas_prometidas'],
        'palabras_pdf': n_pdf >= cfg['palabras_objetivo'] * 0.95,
        'palabras_docx': n_docx >= cfg['palabras_objetivo'] * 0.95,
        'sin_capitulos_cortos': not cortos,
        'paridad': dif < 0.02 and len(d_docx.tables) == tablas_md,
        'tablas_ancladas': not r['tabla_tras_ultimo_capitulo'] and not faltan_en_pdf,
        'no_latinos': (r['no_latinos_md'] + r['no_latinos_pdf'] + r['no_latinos_docx']) == 0,
        'fechas': not r['fechas_caducas'],
        'mortalidad': not r['mortalidad_sin_fuente'],
        'metadata': (r['meta_pdf']['author'] == 'AI Chef Pro'
                     and bool(r['meta_pdf']['title'])
                     and r['meta_docx']['author'] == 'AI Chef Pro'
                     and bool(r['meta_docx']['title'])),
        'coherencia_cifras': not incoherentes,
    }
    r['verde'] = all(r['ok'].values())
    return r


# --------------------------------------------------------------------------
# 9. Orquestación por producto
# --------------------------------------------------------------------------


def cargar_guion(pid):
    ruta = os.path.join(AQUI, f'guion_{pid.replace("-", "_")}.py')
    if not os.path.exists(ruta):
        raise SystemExit(f'ABORTADO: no existe {ruta}')
    spec = importlib.util.spec_from_file_location(f'guion_{pid}', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def construir_documento(nombre, guia, capitulos, xlsx_dir, idx_research,
                        salida, dir_txt, forzar, cfg_extra=None):
    """Genera <nombre>.md/.docx/.pdf y devuelve (gates, detalle)."""
    detalle = []
    partes = [portada_e_indice(guia, capitulos)]
    for cap in capitulos:
        md, det = generar_capitulo(cap, guia, xlsx_dir, idx_research, dir_txt,
                                   forzar=(cap['n'] in forzar))
        f = guard_no_latinos(md, f'cap {cap["n"]}')
        if f:
            raise SystemExit(4)
        partes.append(md)
        partes.append('\n---\n')
        detalle.append(det)
    partes.append(cierre(guia))
    md_text = '\n'.join(partes)

    ruta_md = os.path.join(salida, nombre + '.md')
    with open(ruta_md, 'w', encoding='utf-8') as f:
        f.write(md_text)

    meta = {'author': 'AI Chef Pro',
            'title': guia['titulo'],
            'subject': guia['subtitulo'] + ' · Versión 2.0 · agosto 2026',
            'cabecera': guia['cabecera'],
            'pie': f'Versión 2.0 · aichef.pro/{guia["pid"]}',
            'comments': 'AI Chef Pro · aichef.pro'}
    if cfg_extra and cfg_extra.get('meta'):
        meta.update(cfg_extra['meta'])
    docx_path, pdf_path, saneados = maquetar(md_text,
                                             os.path.join(salida, nombre), meta)
    cfg = dict(guia['gates'])
    if cfg_extra:
        cfg.update({k: v for k, v in cfg_extra.items() if k != 'meta'})
    g = gates(md_text, docx_path, pdf_path, cfg, xlsx_dir, idx_research)
    g['saneados_winansi'] = saneados
    g['ficheros'] = {'md': ruta_md, 'docx': docx_path, 'pdf': pdf_path}
    return g, detalle


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--producto', required=True)
    ap.add_argument('--salida', default=None)
    ap.add_argument('--json', default=None)
    ap.add_argument('--solo-capitulos', default=None,
                    help='1,2,3 — genera sólo esos capítulos (para depurar)')
    ap.add_argument('--regenerar', default='',
                    help='ns de capítulo cuyo caché se ignora (capítulos cortos)')
    ap.add_argument('--sin-bonus', action='store_true')
    ap.add_argument('--solo-bonus', default=None)
    ap.add_argument('--min-palabras-cap', type=int, default=900)
    args = ap.parse_args()

    pid = args.producto
    guion = cargar_guion(pid)
    guia = guion.GUIA
    guia['gates']['min_palabras_cap'] = args.min_palabras_cap
    xlsx_dir = os.path.join(DL, pid)
    scratch = os.environ.get(
        'GUIAS_SCRATCH',
        '/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/'
        '9a6ebdb7-5d45-4ab1-9e93-10b86cb95c42/scratchpad/guias/docs/build')
    salida = guarda_salida(args.salida or os.path.join(scratch, pid))
    dir_txt = os.path.join(salida, 'txt')
    os.makedirs(dir_txt, exist_ok=True)

    res = cargar_research()
    idx = indexar_research(res)
    forzar = {int(x) for x in args.regenerar.split(',') if x.strip()}

    capitulos = guion.CAPITULOS
    if args.solo_capitulos:
        pedidos = {int(x) for x in args.solo_capitulos.split(',')}
        capitulos = [c for c in capitulos if c['n'] in pedidos]

    informe = {'_meta': {'pid': pid, 'generado': time.strftime('%Y-%m-%d %H:%M'),
                         'salida': salida, 'xlsx_dir': xlsx_dir,
                         'modelo': MODELO,
                         'research': res.get('_meta', {}).get('generado'),
                         'research_ausente': res.get('_meta', {}).get('ausente', False)},
               'documentos': {}}

    print(f'== GUÍA {pid} — {len(capitulos)} capítulos', flush=True)
    g, det = construir_documento(pid, guia, capitulos, xlsx_dir, idx, salida,
                                 dir_txt, forzar)
    informe['documentos'][pid] = {'gates': g, 'capitulos': det}
    print(json.dumps(g['ok'], ensure_ascii=False, indent=2), flush=True)

    if not args.sin_bonus:
        for b in guion.BONUS:
            if args.solo_bonus and b['nombre'] != args.solo_bonus:
                continue
            print(f'== BONUS {b["nombre"]}', flush=True)
            gb = dict(guia)
            gb.update(b['guia'])
            dtxt = os.path.join(dir_txt, b['nombre'])
            os.makedirs(dtxt, exist_ok=True)
            gg, dd = construir_documento(b['nombre'], gb, b['capitulos'], xlsx_dir,
                                         idx, salida, dtxt, forzar,
                                         cfg_extra=b['gates'])
            informe['documentos'][b['nombre']] = {'gates': gg, 'capitulos': dd}
            print(json.dumps(gg['ok'], ensure_ascii=False, indent=2), flush=True)

    ruta_json = args.json or os.path.join(salida, f'{pid}-documentos.json')
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(informe, f, ensure_ascii=False, indent=2)
    print(f'informe: {ruta_json}', flush=True)
    verde = all(d['gates']['verde'] for d in informe['documentos'].values())
    raise SystemExit(0 if verde else 1)


if __name__ == '__main__':
    main()
