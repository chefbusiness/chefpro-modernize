#!/usr/bin/env python3
"""paginas-gate.py — ata las páginas ANUNCIADAS en la landing (.ts) de cada producto digital
con las páginas REALES del entregable servido en astro-site/public/dl/<slug>/.

Por qué (2026-09-10): la refutación del research de la Guía de Pastelería (hallazgo C1,
scripts/productos-digitales/auditorias/guia-pasteleria-research-REFUTACION-2026-09-09.md)
encontró que NADA ataba la promesa con el fichero servido: guia-restaurante-gastronomico.ts
anuncia «119 páginas» y el PDF real tiene 10. `documentos.py` mira `paginas_prometidas`
contra el GUION, no contra la landing, y `censo-entregables.py` no cuenta páginas. Este
gate cierra ese hueco.

    /usr/local/bin/python3 scripts/productos-digitales/paginas-gate.py
    /usr/local/bin/python3 scripts/productos-digitales/paginas-gate.py --only guia-restaurante-gastronomico
    /usr/local/bin/python3 scripts/productos-digitales/paginas-gate.py --json informe.json

Motor de PDF: PyMuPDF (fitz) si está instalado —el más fiable, mide `page_count` sin
renderizar—; si no, cae a `pypdf`. En el Mac usar SIEMPRE /usr/local/bin/python3 (tiene
openpyxl y PyMuPDF; el python3 del sistema no).

Qué hace:
  1. Recorre astro-site/src/data/productos/**/*.ts (guías, manuales, planes, kits, tareas;
     salta types.ts) y extrae con regex TODAS las menciones «N páginas / N+ páginas /
     +N páginas / N págs[.]» estén donde estén (checkItems, hero.description, grid.subtitle,
     bonus.items[].desc, cta.items, schema.productDescription, seo.description...).
  2. Por cada mención, ubica el bloque de nivel superior que la contiene (hero, bonus, cta...)
     para saber el campo y si hay pista de "bonus" (para emparejar con un BONUS-*.pdf en vez
     del entregable principal).
  3. Empareja con el fichero de astro-site/public/dl/<slug>/: el PRINCIPAL por defecto (el
     PDF/DOCX no numerado y no-BONUS cuyo nombre más se parece al slug, por difflib), o el
     BONUS correspondiente si el texto/campo lo pide (por nombre de fichero, con ratio de
     palabras significativas; si sólo hay un bonus, se asigna directo). Si no hay candidato,
     se reporta «SIN EMPAREJAR» — nunca se ignora en silencio.
  4. Mide páginas reales: PDF → `page_count` real. Si el producto es DOCX-only (línea
     "planes", sin PDF) o el PDF resulta ser una portada de pocas páginas mientras el DOCX
     tiene más contenido, también se estima con el DOCX: palabras de word/document.xml
     (zipfile + regex sobre <w:t>) ÷ 530 palabras/página. Se usa la MAYOR de las dos cifras
     para el veredicto, marcando «estimado desde DOCX» cuando esa es la que decide.
  5. Falla si CUALQUIER cifra anunciada SUPERA las páginas reales (o la estimación) del
     fichero emparejado, o si queda algo SIN EMPAREJAR.

Exit 0: todo lo anunciado cabe en lo real (o no hay menciones de páginas en el catálogo).
Exit 1: alguna cifra anunciada supera al entregable, o alguna mención no se pudo emparejar.

Térmica: leer `page_count` con PyMuPDF NO renderiza páginas (es barato), pero por regla
del proyecto se comprueba `istats cpu temp` antes de CADA apertura de PDF y se procesan
de uno en uno — nunca en paralelo. Si la CPU está a >=65°C se pausa y se vuelve a mirar
cada 15s hasta que baje.
"""
import argparse
import difflib
import json
import re
import subprocess
import sys
import time
import unicodedata
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ASTRO_DIR = REPO_ROOT / 'astro-site'
PRODUCTOS_DIR = ASTRO_DIR / 'src' / 'data' / 'productos'
DL_DIR = ASTRO_DIR / 'public' / 'dl'

WORDS_PER_PAGE = 530
THERMAL_LIMIT_C = 65.0
THERMAL_POLL_S = 15

# --------------------------------------------------------------------------------------
# Motor de PDF: PyMuPDF preferido, pypdf de respaldo.
# --------------------------------------------------------------------------------------
PDF_ENGINE = None
try:
    import fitz  # PyMuPDF
    PDF_ENGINE = 'pymupdf'
except ImportError:
    fitz = None
    try:
        import pypdf
        PDF_ENGINE = 'pypdf'
    except ImportError:
        pypdf = None


_TEMP_RE = re.compile(r'(\d+(?:\.\d+)?)\s*°?C')


def read_cpu_temp():
    """Lee `istats cpu temp`. Devuelve float o None si no está disponible."""
    try:
        out = subprocess.run(['istats', 'cpu', 'temp'], capture_output=True, text=True, timeout=10).stdout
        clean = re.sub(r'\x1b\[[0-9;]*m', '', out)  # quitar color ANSI
        m = _TEMP_RE.search(clean)
        return float(m.group(1)) if m else None
    except Exception:
        return None


def check_thermal(label=''):
    """Un PDF cada vez, comprobando térmica antes de abrirlo (regla del proyecto)."""
    temp = read_cpu_temp()
    if temp is None:
        return
    waited = False
    while temp is not None and temp >= THERMAL_LIMIT_C:
        waited = True
        print(f'  [térmica] {temp:.1f}°C >= {THERMAL_LIMIT_C}°C — pausando antes de {label}...', file=sys.stderr)
        time.sleep(THERMAL_POLL_S)
        temp = read_cpu_temp()
    if waited and temp is not None:
        print(f'  [térmica] reanudado a {temp:.1f}°C', file=sys.stderr)


def pdf_page_count(path):
    """(page_count, error). Comprueba térmica antes de abrir CADA PDF."""
    check_thermal(path.name)
    try:
        if PDF_ENGINE == 'pymupdf':
            doc = fitz.open(str(path))
            n = doc.page_count
            doc.close()
            return n, None
        elif PDF_ENGINE == 'pypdf':
            reader = pypdf.PdfReader(str(path))
            return len(reader.pages), None
        else:
            return None, 'sin motor PDF (ni PyMuPDF ni pypdf disponibles en este intérprete)'
    except Exception as e:
        return None, f'error abriendo PDF: {e}'


def docx_word_count(path):
    """(palabras, error) contando <w:t> de word/document.xml."""
    try:
        with zipfile.ZipFile(str(path)) as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        textos = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml, re.S)
        return sum(len(t.split()) for t in textos), None
    except Exception as e:
        return None, f'error leyendo DOCX: {e}'


# --------------------------------------------------------------------------------------
# Descubrir productos
# --------------------------------------------------------------------------------------

def discover_products(only=None):
    products = []
    for ts_file in sorted(PRODUCTOS_DIR.glob('*/*.ts')):
        if ts_file.name == 'types.ts':
            continue
        linea = ts_file.parent.name  # guias / manuales / planes / kits / tareas
        text = ts_file.read_text(encoding='utf-8')
        m = re.search(r"^\s*slug:\s*'([^']+)'", text, re.M)
        slug = m.group(1) if m else ts_file.stem
        if only and slug != only:
            continue
        products.append({'slug': slug, 'linea': linea, 'path': ts_file, 'text': text})
    return products


# --------------------------------------------------------------------------------------
# Regex de páginas anunciadas: "119 páginas", "60+ páginas", "+40 páginas", "N págs."
# --------------------------------------------------------------------------------------

PAGE_RE = re.compile(r'\+?\s*(\d+)\s*\+?\s*(páginas?|págs\.?)', re.IGNORECASE)


def find_page_mentions(text):
    mentions = []
    for m in PAGE_RE.finditer(text):
        num = int(m.group(1))
        line_no = text.count('\n', 0, m.start()) + 1
        line_start = text.rfind('\n', 0, m.start()) + 1
        line_end = text.find('\n', m.end())
        if line_end == -1:
            line_end = len(text)
        line_text = text[line_start:line_end].strip()
        mentions.append({'num': num, 'line_no': line_no, 'line_text': line_text, 'match_text': m.group(0).strip()})
    return mentions


# --------------------------------------------------------------------------------------
# Bloques de nivel superior del objeto TS (para saber el "campo" y si hay pista de bonus).
# Los ficheros de productos indentan sus claves de nivel superior con EXACTAMENTE 2
# espacios y las cierran con `  },` / `  ],` al mismo nivel — verificado a mano contra
# guias/manuales/planes/kits antes de escribir esto.
# --------------------------------------------------------------------------------------

OPEN_RE = re.compile(r'^  (\w+):\s*[\{\[]')
CLOSE_RE = re.compile(r'^  [\}\]]')
KEYVAL_RE = re.compile(r"^\s*(\w+):\s*")
ARRAY_OPEN_RE = re.compile(r'(\w+):\s*\[\s*$')


def top_level_blocks(text):
    lines = text.split('\n')
    blocks = []
    i = 0
    while i < len(lines):
        m = OPEN_RE.match(lines[i])
        if m:
            start = i
            j = i + 1
            end = len(lines) - 1
            while j < len(lines):
                if CLOSE_RE.match(lines[j]):
                    end = j
                    break
                j += 1
            blocks.append({'key': m.group(1), 'start': start, 'end': end})
            i = end + 1
        else:
            i += 1
    return blocks


def field_context(text, blocks, line_no):
    """line_no es 1-based. Devuelve (top_level_key, campo_local, bonus_hint)."""
    lines = text.split('\n')
    idx = line_no - 1
    top_key = None
    block_start = None
    for b in blocks:
        if b['start'] <= idx <= b['end']:
            top_key = b['key']
            block_start = b['start']
            break
    local_key = None
    m = KEYVAL_RE.match(lines[idx])
    if m:
        local_key = m.group(1)
    elif block_start is not None:
        for k in range(idx - 1, block_start, -1):
            am = ARRAY_OPEN_RE.search(lines[k])
            if am:
                local_key = am.group(1)
                break
    bonus_hint = (top_key == 'bonus') or ('bonus' in lines[idx].lower())
    return top_key, local_key, bonus_hint


# --------------------------------------------------------------------------------------
# Emparejar mención → fichero(s) de dl/<slug>/
# --------------------------------------------------------------------------------------

STOPWORDS = {
    'de', 'la', 'el', 'los', 'las', 'en', 'con', 'y', 'o', 'a', 'un', 'una', 'del', 'para',
    'que', 'tu', 'su', 'paso', 'incluye', 'completo', 'completa', 'editable', 'pdf', 'docx',
    'bonus', 'capitulos', 'capitulo', 'capítulos', 'capítulo', 'paginas', 'páginas', 'pag',
    'pags', 'guia', 'guía', 'manual', 'resueltos', 'resuelto', 'resuelta', 'resueltas',
}


def normalize(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    return s


def significant_words(s):
    if not s:
        return set()
    return {w for w in normalize(s).split() if w not in STOPWORDS and not w.isdigit() and len(w) > 2}


def is_numbered(f):
    return re.match(r'^\d+[-_]', f.name) is not None


def is_bonus(f):
    return f.name.upper().startswith('BONUS')


def list_deliverable_files(slug):
    d = DL_DIR / slug
    if not d.is_dir():
        return None
    files = [f for f in d.iterdir() if f.is_file()]
    main = [f for f in files if f.suffix.lower() in ('.pdf', '.docx') and not is_numbered(f) and not is_bonus(f)]
    bonus = [f for f in files if f.suffix.lower() in ('.pdf', '.docx') and is_bonus(f)]
    return {'dir': d, 'main': main, 'bonus': bonus}


def group_by_basename(files):
    groups = {}
    for f in files:
        base = re.sub(r'\.(pdf|docx)$', '', f.name, flags=re.I)
        groups.setdefault(base, {})[f.suffix.lower()] = f
    return groups


def resolve_principal(slug, main_files):
    """Elige, entre los candidatos principales, el grupo (pdf/docx del mismo nombre base)
    cuyo nombre más se parece al slug (difflib). Devuelve (pdf_path|None, docx_path|None, score)."""
    if not main_files:
        return None, None, 0.0
    groups = group_by_basename(main_files)
    best_base, best_score = None, -1.0
    for base in groups:
        score = difflib.SequenceMatcher(None, slug, base).ratio()
        if score > best_score:
            best_base, best_score = base, score
    group = groups[best_base]
    return group.get('.pdf'), group.get('.docx'), best_score


def resolve_bonus(mention_text, bonus_files, title_hint=None):
    """Empareja una mención "de bonus" con el BONUS-*.pdf/.docx correspondiente.
    Si sólo hay un bonus en el producto, se asigna directo (score=1.0, sin ambigüedad
    posible). Si hay varios, se compara por solape de palabras significativas contra el
    nombre de fichero (y el 'title' del bonus si venía en la misma línea)."""
    if not bonus_files:
        return None, None, 0.0
    groups = group_by_basename(bonus_files)
    if len(groups) == 1:
        base = next(iter(groups))
        group = groups[base]
        return group.get('.pdf'), group.get('.docx'), 1.0

    target = significant_words(mention_text) | significant_words(title_hint)
    best_base, best_score = None, -1.0
    for base in groups:
        base_words = significant_words(re.sub(r'^BONUS[-_]?', '', base, flags=re.I).replace('-', ' '))
        if not target or not base_words:
            score = 0.0
        else:
            score = len(target & base_words) / len(target | base_words)
        if score > best_score:
            best_base, best_score = base, score
    if best_score <= 0:
        return None, None, 0.0
    group = groups[best_base]
    return group.get('.pdf'), group.get('.docx'), best_score


# --------------------------------------------------------------------------------------
# Análisis por producto
# --------------------------------------------------------------------------------------

def analyze_product(p, measure_cache):
    slug, linea, path, text = p['slug'], p['linea'], p['path'], p['text']
    mentions = find_page_mentions(text)
    if not mentions:
        return {'slug': slug, 'linea': linea, 'rows': [], 'has_mentions': False}

    blocks = top_level_blocks(text)
    files = list_deliverable_files(slug)
    principal_pdf = principal_docx = None
    principal_score = 0.0
    if files:
        principal_pdf, principal_docx, principal_score = resolve_principal(slug, files['main'])

    def get_pdf_pages(fpath):
        key = str(fpath)
        if key not in measure_cache:
            measure_cache[key] = pdf_page_count(fpath)
        return measure_cache[key]

    def get_docx_words(fpath):
        key = str(fpath)
        if key not in measure_cache:
            measure_cache[key] = docx_word_count(fpath)
        return measure_cache[key]

    rows = []
    for mention in mentions:
        top_key, local_key, bonus_hint = field_context(text, blocks, mention['line_no'])
        campo = f'{top_key}.{local_key}' if local_key else (top_key or '?')
        try:
            rel_path = path.relative_to(REPO_ROOT)
        except ValueError:
            rel_path = path
        row = {
            'slug': slug,
            'linea_producto': linea,
            'fichero': f'{rel_path}:{mention["line_no"]}',
            'campo': campo,
            'texto': mention['line_text'][:150],
            'anunciado': mention['num'],
        }

        pdf_path = docx_path = None
        match_kind = match_score = None
        if bonus_hint and files and files['bonus']:
            title_hint = None
            tm = re.search(r"title:\s*'([^']*)'", mention['line_text'])
            if tm:
                title_hint = tm.group(1)
            pdf_path, docx_path, match_score = resolve_bonus(mention['line_text'], files['bonus'], title_hint)
            if pdf_path or docx_path:
                match_kind = 'bonus'

        if pdf_path is None and docx_path is None:
            if principal_pdf or principal_docx:
                pdf_path, docx_path, match_score = principal_pdf, principal_docx, principal_score
                match_kind = 'principal'

        if pdf_path is None and docx_path is None:
            row.update(pdf='—', paginas_reales=None, veredicto='SIN EMPAREJAR',
                       nota='sin PDF/DOCX candidato en dl/<slug>/' if files else f'no existe {DL_DIR.name}/{slug}/')
            rows.append(row)
            continue

        real_pdf_pages = pdf_err = None
        if pdf_path:
            real_pdf_pages, pdf_err = get_pdf_pages(pdf_path)
        est_docx_pages = docx_err = None
        if docx_path:
            words, docx_err = get_docx_words(docx_path)
            if words is not None:
                est_docx_pages = round(words / WORDS_PER_PAGE, 1)

        candidatos = [v for v in (real_pdf_pages, est_docx_pages) if v is not None]
        if not candidatos:
            row.update(pdf=(pdf_path or docx_path).name, paginas_reales=None, veredicto='ERROR',
                       nota=pdf_err or docx_err or 'no se pudo medir')
            rows.append(row)
            continue

        resolved = max(candidatos)
        estimado_docx = est_docx_pages is not None and resolved == est_docx_pages and (
            real_pdf_pages is None or est_docx_pages > real_pdf_pages)

        etiqueta_fichero = (pdf_path or docx_path).name
        if estimado_docx and pdf_path and docx_path:
            etiqueta_fichero += f' (estimado desde {docx_path.name}: {est_docx_pages}p vs PDF {real_pdf_pages}p)'
        elif estimado_docx:
            etiqueta_fichero += f' (estimado desde DOCX: {est_docx_pages}p, sin PDF real)'

        row.update(
            pdf=etiqueta_fichero,
            paginas_reales=resolved,
            match_kind=match_kind,
            match_score=round(match_score, 2) if match_score is not None else None,
            estimado_docx=estimado_docx,
            veredicto='FALLA' if mention['num'] > resolved else 'OK',
        )
        if row['veredicto'] == 'FALLA':
            row['exceso'] = round(mention['num'] - resolved, 1)
        rows.append(row)

    return {'slug': slug, 'linea': linea, 'rows': rows, 'has_mentions': True}


# --------------------------------------------------------------------------------------
# Salida
# --------------------------------------------------------------------------------------

def print_table(rows):
    if not rows:
        print('(sin menciones de páginas)')
        return
    headers = ['slug', 'fichero:línea', 'campo', 'anunciado', 'pdf/docx emparejado', 'páginas reales', 'veredicto']
    data = []
    for r in rows:
        data.append([
            r['slug'], r['fichero'], r['campo'], str(r['anunciado']),
            r.get('pdf', '—'),
            str(r['paginas_reales']) if r.get('paginas_reales') is not None else '—',
            r['veredicto'] + (f" (+{r['exceso']})" if r.get('exceso') else ''),
        ])
    widths = [max(len(h), max((len(row[i]) for row in data), default=0)) for i, h in enumerate(headers)]
    def fmt(cells):
        return ' | '.join(c.ljust(w) for c, w in zip(cells, widths))
    print(fmt(headers))
    print('-|-'.join('-' * w for w in widths))
    for row in data:
        print(fmt(row))


def build_markdown(all_results, args):
    lines = []
    lines.append('# Gate de páginas anunciadas vs páginas reales — 2026-09-10')
    lines.append('')
    lines.append('Generado por `scripts/productos-digitales/paginas-gate.py`. Ata cada cifra de páginas que')
    lines.append('anuncia la landing (`astro-site/src/data/productos/**/*.ts`) con las páginas reales del')
    lines.append('entregable en `astro-site/public/dl/<slug>/`. Motivo: hallazgo C1 de la refutación del')
    lines.append('research de la Guía de Pastelería (`guia-pasteleria-research-REFUTACION-2026-09-09.md`).')
    lines.append('')

    all_rows = [r for res in all_results for r in res['rows']]
    con_mencion = [res for res in all_results if res['has_mentions']]
    ok = [r for r in all_rows if r['veredicto'] == 'OK']
    falla = [r for r in all_rows if r['veredicto'] == 'FALLA']
    sin_emparejar = [r for r in all_rows if r['veredicto'] == 'SIN EMPAREJAR']
    error = [r for r in all_rows if r['veredicto'] == 'ERROR']

    lines.append('## Resumen')
    lines.append('')
    lines.append(f'- Productos escaneados: **{len(all_results)}**')
    lines.append(f'- Productos que anuncian páginas: **{len(con_mencion)}**')
    lines.append(f'- Menciones de página evaluadas: **{len(all_rows)}**')
    lines.append(f'- OK (cabe en lo real): **{len(ok)}**')
    lines.append(f'- FALLA (anunciado > real): **{len(falla)}**')
    lines.append(f'- SIN EMPAREJAR (no se pudo verificar): **{len(sin_emparejar)}**')
    if error:
        lines.append(f'- ERROR (no se pudo medir el fichero): **{len(error)}**')
    if falla:
        total_exceso = round(sum(r.get('exceso', 0) for r in falla), 1)
        peor = max(falla, key=lambda r: r.get('exceso', 0))
        lines.append(f'- Exceso total sumado en las FALLA: **{total_exceso} páginas**')
        lines.append(f"- Peor caso: `{peor['slug']}` anuncia {peor['anunciado']} y el entregable tiene "
                      f"{peor['paginas_reales']} (exceso {peor['exceso']})")
    lines.append('')

    if falla:
        lines.append('## Fallan (anunciado > real)')
        lines.append('')
        lines.append('| slug | fichero:línea | campo | anunciado | pdf/docx emparejado | páginas reales | exceso |')
        lines.append('|---|---|---|---|---|---|---|')
        for r in sorted(falla, key=lambda r: -r.get('exceso', 0)):
            lines.append(f"| {r['slug']} | `{r['fichero']}` | {r['campo']} | {r['anunciado']} | "
                          f"{r.get('pdf', '—')} | {r['paginas_reales']} | {r['exceso']} |")
        lines.append('')

    if sin_emparejar:
        lines.append('## Sin emparejar (no se pudo atar a ningún entregable)')
        lines.append('')
        lines.append('| slug | fichero:línea | campo | anunciado | texto | nota |')
        lines.append('|---|---|---|---|---|---|')
        for r in sin_emparejar:
            texto = r['texto'].replace('|', '\\|')
            lines.append(f"| {r['slug']} | `{r['fichero']}` | {r['campo']} | {r['anunciado']} | {texto} | {r.get('nota', '')} |")
        lines.append('')

    if error:
        lines.append('## Error al medir')
        lines.append('')
        lines.append('| slug | fichero:línea | pdf/docx | nota |')
        lines.append('|---|---|---|---|')
        for r in error:
            lines.append(f"| {r['slug']} | `{r['fichero']}` | {r.get('pdf', '—')} | {r.get('nota', '')} |")
        lines.append('')

    lines.append('## Tabla completa')
    lines.append('')
    lines.append('| slug | línea | fichero:línea | campo | texto | anunciado | pdf/docx emparejado | páginas reales | veredicto |')
    lines.append('|---|---|---|---|---|---|---|---|---|')
    for res in all_results:
        for r in res['rows']:
            texto = r['texto'].replace('|', '\\|')
            lines.append(f"| {r['slug']} | {res['linea']} | `{r['fichero']}` | {r['campo']} | {texto} | "
                          f"{r['anunciado']} | {r.get('pdf', '—')} | "
                          f"{r['paginas_reales'] if r.get('paginas_reales') is not None else '—'} | {r['veredicto']} |")
    lines.append('')

    lines.append('## Limitaciones conocidas')
    lines.append('')
    lines.append('- El emparejamiento "principal vs bonus" es heurístico (difflib contra el slug / solape de')
    lines.append('  palabras contra el nombre de fichero BONUS-*). Revisar la columna `match_score` en el JSON')
    lines.append('  cuando el veredicto sorprenda.')
    lines.append(f'- La estimación desde DOCX usa {WORDS_PER_PAGE} palabras/página, una convergencia razonable')
    lines.append('  pero no exacta: sirve para no dar una FALLA falsa por culpa de un PDF-portada de 1 página,')
    lines.append('  no como cifra de marketing.')
    lines.append('- Sólo entiende los patrones "N páginas", "N+ páginas", "+N páginas" y "N págs[.]". Una cifra')
    lines.append('  de páginas escrita en palabras ("ciento diecinueve páginas") no se detecta.')
    lines.append('')
    lines.append('Via: Claude Code')
    lines.append('')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--only', default=None, help='Sólo este slug de producto')
    ap.add_argument('--json', default=None, help='Vuelca el detalle completo aquí')
    ap.add_argument('--informe', default=None,
                    help='Ruta del informe .md (por defecto, auditorias/paginas-gate-2026-09-10.md)')
    ap.add_argument('--quiet', action='store_true', help='No imprime la tabla completa, sólo fallas y resumen')
    args = ap.parse_args()

    if PDF_ENGINE is None:
        print('AVISO: ni PyMuPDF ni pypdf están disponibles en este intérprete — usar '
              '/usr/local/bin/python3.', file=sys.stderr)

    products = discover_products(only=args.only)
    if not products:
        print(f'0 productos encontrados (only={args.only!r}) en {PRODUCTOS_DIR}', file=sys.stderr)
        sys.exit(2)

    measure_cache = {}
    all_results = []
    for p in products:
        all_results.append(analyze_product(p, measure_cache))

    all_rows = [r for res in all_results for r in res['rows']]

    if not args.quiet:
        print_table(all_rows)
        print()

    con_mencion = [res for res in all_results if res['has_mentions']]
    ok = [r for r in all_rows if r['veredicto'] == 'OK']
    falla = [r for r in all_rows if r['veredicto'] == 'FALLA']
    sin_emparejar = [r for r in all_rows if r['veredicto'] == 'SIN EMPAREJAR']
    error = [r for r in all_rows if r['veredicto'] == 'ERROR']

    print(f'{len(products)} productos escaneados, {len(con_mencion)} anuncian páginas, '
          f'{len(all_rows)} menciones — OK={len(ok)} FALLA={len(falla)} '
          f'SIN_EMPAREJAR={len(sin_emparejar)} ERROR={len(error)}')

    if falla:
        print('\nFALLA (anunciado > real):', file=sys.stderr)
        for r in sorted(falla, key=lambda r: -r.get('exceso', 0)):
            print(f"  {r['slug']} · {r['fichero']} · anuncia {r['anunciado']} · real {r['paginas_reales']} "
                  f"({r.get('pdf', '—')}) · exceso {r['exceso']}", file=sys.stderr)
    if sin_emparejar:
        print('\nSIN EMPAREJAR (no verificado):', file=sys.stderr)
        for r in sin_emparejar:
            print(f"  {r['slug']} · {r['fichero']} · {r['texto'][:80]!r} · {r.get('nota', '')}", file=sys.stderr)
    if error:
        print('\nERROR al medir:', file=sys.stderr)
        for r in error:
            print(f"  {r['slug']} · {r['fichero']} · {r.get('pdf', '—')} · {r.get('nota', '')}", file=sys.stderr)

    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(all_rows, f, ensure_ascii=False, indent=2)
        print(f'\nJSON escrito: {args.json} ({len(all_rows)} filas)')

    if not args.only:
        informe_path = Path(args.informe) if args.informe else (
            REPO_ROOT / 'scripts' / 'productos-digitales' / 'auditorias' / 'paginas-gate-2026-09-10.md')
        informe_path.parent.mkdir(parents=True, exist_ok=True)
        informe_path.write_text(build_markdown(all_results, args), encoding='utf-8')
        print(f'Informe escrito: {informe_path.relative_to(REPO_ROOT)}')

    sys.exit(1 if (falla or sin_emparejar) else 0)


if __name__ == '__main__':
    main()
