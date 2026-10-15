#!/usr/bin/env python3
"""Maqueta los .md EN de la guía Food Cost en DOCX + PDF con documentos.maquetar() (SPEC D4).

    python3 render_en.py [--solo guia|bonus] [--md <fichero.md> --solo X] [--salida <dir>]

Entrada por defecto: en/food-cost-menu-engineering-guide.md y en/BONUS-solved-exercises.md
(los deja ensamblar_md.py). Salida por defecto: astro-site/public/dl/food-cost-menu-engineering-guide/.
Mismo maquetado que el ES (A4, Helvetica, mismo Markdown → DOCX y PDF); los metadatos se arman
como en documentos.construir_documento() pero con valores EN, el pie dice «Page N» y, como
construir_docx/construir_pdf no escriben keywords ni idioma, se ponen después (keywords de SPEC D3,
idioma en-US en el docx). Después, comprobaciones ligeras: páginas del PDF, palabras del DOCX
contra el .md, pie en inglés y residuo de español (gate_md_en.residuo) en el texto extraído.
Sale con 1 si alguna comprobación falla. Ligero (reportlab + python-docx; sin LibreOffice).
"""
import argparse
import re
import sys
from pathlib import Path

import gate_md_en as G          # importa también documentos.py (sin efectos al importar)

D = G.D
AQUI = Path(__file__).resolve().parent
SALIDA = G.REPO / 'astro-site' / 'public' / 'dl' / 'food-cost-menu-engineering-guide'

VERSION, FECHA = '1.0', 'October 2026'
URL = 'aichef.pro/en/digital-products/food-cost-menu-engineering-guide'
COMUN = {
    'author': 'John Guerrero · AI Chef Pro',
    'category': 'Professional guide',            # ES: 'Guía profesional'
    'pie': 'Version %s · %s · %s' % (VERSION, FECHA, URL),
    'comments': 'AI Chef Pro · aichef.pro',
    'language': 'en-US',
}
DOCS = {
    'guia': {'md': 'food-cost-menu-engineering-guide.md',
             'base': 'food-cost-menu-engineering-guide',
             'title': 'Food Cost + Menu Engineering Guide',
             # ES: subtítulo + « · Versión 1.0 · septiembre 2026» (construir_documento)
             'subject': 'Recipe costing, menu pricing and menu profitability · US edition 2026'
                        ' · Version %s · %s' % (VERSION, FECHA),
             'cabecera': 'AI Chef Pro · Food Cost + Menu Engineering Guide'},
    'bonus': {'md': 'BONUS-solved-exercises.md',
              'base': 'BONUS-solved-exercises',
              'title': '12 Solved Food Cost and Menu Engineering Exercises',
              'subject': 'Bonus to the Food Cost + Menu Engineering Guide'
                         ' · Version %s · %s' % (VERSION, FECHA),
              'cabecera': 'AI Chef Pro · 12 Solved Exercises'},
}


def keywords_spec():
    """Keywords de SPEC D3 («menu pricing 12.100 (picos) · how to calculate food cost 880 · …»)."""
    m = re.search(r'Keywords:\s*(.+?)\.\s*PAA', G.SPEC.read_text(encoding='utf-8'))
    if not m:
        sys.exit('ABORTADO: no encuentro las keywords de D3 en SPEC.md')
    kws = [re.sub(r'\s+[\d.]+(\s*\(.*?\))?\s*$', '', k).strip() for k in m.group(1).split('·')]
    return ', '.join(k for k in kws if k)


def meta_de(clave):
    meta = dict(COMUN)
    meta.update({k: v for k, v in DOCS[clave].items() if k not in ('md', 'base')})
    meta['keywords'] = keywords_spec()
    return meta


def metadatos_extra(docx_path, pdf_path, meta):
    """Lo que documentos.py no escribe: keywords e idioma (docx) y keywords (pdf)."""
    from docx import Document
    d = Document(docx_path)
    d.core_properties.keywords = meta['keywords']
    d.core_properties.language = meta['language']
    d.save(docx_path)
    try:
        import fitz
    except ImportError:
        return 'PyMuPDF no instalado: keywords del PDF sin poner'
    pdf = fitz.open(pdf_path)
    md = dict(pdf.metadata or {})
    md['keywords'] = meta['keywords']
    pdf.set_metadata(md)
    guardar = getattr(pdf, 'saveIncr', None) or getattr(pdf, 'save_incr')
    guardar()
    pdf.close()
    return None


def palabras_md(md_text):
    """Palabras que el DOCX tendrá: texto de los bloques sin marcas de negrita/cursiva."""
    trozos = []
    for tipo, cont in D.sanear_bloques(D.parsear(md_text)):
        if tipo == 'table':
            trozos += [c for fila in cont for c in fila]
        elif isinstance(cont, list):
            trozos += cont
        elif isinstance(cont, str):
            trozos.append(cont)
    return D.palabras(' '.join(trozos).replace('*', ''))


def comprobar(md_text, docx_path, pdf_path):
    """Comprobaciones ligeras. Devuelve (fallos, notas)."""
    fallos, notas = [], []
    _, txt_docx = D.texto_docx(docx_path)
    pd, pm = D.palabras(txt_docx), palabras_md(md_text)
    notas.append('docx %d palabras · md %d (ratio %.3f)' % (pd, pm, pd / pm if pm else 0))
    if not pm or abs(pd / pm - 1) > 0.01:
        fallos.append('el DOCX no tiene las palabras del .md (%d vs %d)' % (pd, pm))
    for marca in ('**', '⟦', '€'):
        if marca in txt_docx:
            fallos.append('el DOCX contiene «%s»' % marca)
    for i, par in enumerate(p for p in txt_docx.split('\n') if p.strip()):
        errs, _ = G.residuo(par)
        if errs:
            fallos.append('DOCX párrafo %d: %s · «%s»' % (i + 1, errs[0], par[:60]))
    try:
        import fitz  # noqa: F401
    except ImportError:
        notas.append('PyMuPDF no instalado: sin recuento de páginas ni texto del PDF')
        return fallos, notas
    doc, txt_pdf = D.texto_pdf(pdf_path)
    notas.append('pdf %d páginas' % doc.page_count)
    primera = doc[0].get_text()
    if 'Page 1' not in primera or 'Página' in txt_pdf:
        fallos.append('el pie del PDF no dice «Page N»')
    for n, pagina in enumerate(doc, 1):
        errs, _ = G.residuo(re.sub(r'\s+', ' ', pagina.get_text()))  # celdas partidas en líneas: «Ribera del\nDuero»
        if errs:
            fallos.append('PDF pág. %d: %s' % (n, errs[0]))
    doc.close()
    return fallos, notas


def render(clave, md_path, salida):
    md_text = Path(md_path).read_text(encoding='utf-8')
    meta = meta_de(clave)
    salida.mkdir(parents=True, exist_ok=True)
    D.ETIQUETA_PAGINA = 'Page'
    docx_path, pdf_path, saneados = D.maquetar(md_text, str(salida / DOCS[clave]['base']), meta)
    aviso = metadatos_extra(docx_path, pdf_path, meta)
    fallos, notas = comprobar(md_text, docx_path, pdf_path)
    if aviso:
        notas.append(aviso)
    print('== %s → %s(.docx/.pdf)' % (clave, salida / DOCS[clave]['base']))
    print('   %s · %d caracteres saneados a WinAnsi' % (' · '.join(notas), saneados))
    for f in fallos[:20]:
        print('   FALLO %s' % f)
    if len(fallos) > 20:
        print('   … %d fallos más' % (len(fallos) - 20))
    print('   %s' % ('OK' if not fallos else 'FALLA (%d)' % len(fallos)))
    return not fallos


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--solo', choices=sorted(DOCS))
    ap.add_argument('--md', default=None, help='otro .md de entrada (exige --solo)')
    ap.add_argument('--salida', default=str(SALIDA))
    a = ap.parse_args()
    if a.md and not a.solo:
        sys.exit('--md exige --solo guia|bonus (decide los metadatos)')
    t = D.istats()
    if t is not None and t >= 62:
        sys.exit('ABORTADO: CPU a %.1f °C (≥ 62): espera a que baje' % t)
    ok = True
    for clave in DOCS:
        if a.solo and clave != a.solo:
            continue
        md = Path(a.md) if a.md else AQUI / 'en' / DOCS[clave]['md']
        if not md.exists():
            print('== %s: falta %s (corre ensamblar_md.py)' % (clave, md))
            ok = False
            continue
        ok = render(clave, md, Path(a.salida)) and ok
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
