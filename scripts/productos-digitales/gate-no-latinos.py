#!/usr/bin/env python3
"""gate-no-latinos.py — barrido de caracteres no latinos (inyección de idioma del modelo) en los
entregables vendidos: docx, xlsx y pdf de astro-site/public/dl/.

    python3 scripts/productos-digitales/gate-no-latinos.py [--only <pid|carpeta>] [--json out.json]
    → exit 0 si 0 ocurrencias; exit 1 si hay alguna (imprime fichero, parte y contexto).

Por qué existe (2026-08-29): 7 docx de 6 planes de negocio llevaban 43 fragmentos chinos/cirílicos/
árabes en mitad de frases («押入れ器具 menores», «calidad продукти», «bebida ضمن paquete») y se
vendían así. CLAUDE.md ya documentaba la inyección en el blog; en los entregables nadie la medía.

Gotchas que este script ya tiene en cuenta:
- Rangos: CJK (一-鿿, 㐀-䶿), kana (぀-ヿ), hangul, cirílico, árabe, hebreo, tailandés Y la puntuación
  CJK U+3000-303F (la coma ideográfica «、» se escapó al primer barrido).
- En un docx SOLO se mira word/document.xml + header*/footer*/footnotes: theme1.xml y fontTable.xml
  llevan nombres de fuente asiáticos de serie (ＭＳ ゴシック, 宋体, 맑은 고딕): 32 falsos positivos
  por fichero si se escanea el zip entero.
- xlsx: sharedStrings + hojas (strings inline). pdf: PyPDF2 si está instalado; si no, se avisa.
"""
import argparse, glob, json, os, re, sys, zipfile

RX = re.compile(r'[　-〿぀-ヿ㐀-䶿一-鿿가-힯Ѐ-ӿ'
                r'؀-ۿ֐-׿฀-๿]')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'astro-site', 'public', 'dl')


def _ctx(text, m, n=30):
    return text[max(0, m.start() - n):m.end() + n].replace('\n', ' ')


def scan_xml_text(raw):
    return re.sub(r'<[^>]+>', ' ', raw)


def scan_docx(path):
    z = zipfile.ZipFile(path)
    for p in z.namelist():
        if p == 'word/document.xml' or re.match(r'word/(header|footer|footnotes|endnotes)\d*\.xml$', p):
            t = scan_xml_text(z.read(p).decode('utf8', 'ignore'))
            for m in RX.finditer(t):
                yield p.split('/')[-1], _ctx(t, m)


def scan_xlsx(path):
    z = zipfile.ZipFile(path)
    for p in z.namelist():
        if p == 'xl/sharedStrings.xml' or p.startswith('xl/worksheets/sheet'):
            t = scan_xml_text(z.read(p).decode('utf8', 'ignore'))
            for m in RX.finditer(t):
                yield p.split('/')[-1], _ctx(t, m)


def scan_pdf(path):
    try:
        import PyPDF2
    except ImportError:
        print(f'  aviso: PyPDF2 no instalado, {os.path.basename(path)} sin escanear', file=sys.stderr)
        return
    t = '\n'.join((pg.extract_text() or '') for pg in PyPDF2.PdfReader(path).pages)
    for m in RX.finditer(t):
        yield 'pdf', _ctx(t, m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', help='productId o carpeta')
    ap.add_argument('--json')
    a = ap.parse_args()
    base = a.only if a.only and os.path.isdir(a.only) else os.path.join(ROOT, a.only) if a.only else ROOT
    hits = {}
    files = sorted(glob.glob(os.path.join(base, '**', '*.*'), recursive=True))
    for f in files:
        ext = f.rsplit('.', 1)[-1].lower()
        fn = {'docx': scan_docx, 'xlsx': scan_xlsx, 'pdf': scan_pdf}.get(ext)
        if not fn:
            continue
        try:
            found = list(fn(f))
        except Exception as e:  # zip roto, etc.
            found = [('ERROR', str(e))]
        if found:
            hits[os.path.relpath(f, ROOT)] = found
    total = sum(len(v) for v in hits.values())
    for f, v in hits.items():
        print(f'\n== {f} ({len(v)})')
        for parte, ctx in v[:8]:
            print(f'   {parte} | {ctx}')
    print(f'\n{len(files)} ficheros escaneados · {len(hits)} con no-latinos · {total} caracteres')
    if a.json:
        json.dump({'ficheros': len(files), 'hits': hits}, open(a.json, 'w'), ensure_ascii=False, indent=1)
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main())
