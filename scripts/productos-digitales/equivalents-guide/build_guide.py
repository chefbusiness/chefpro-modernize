#!/usr/bin/env python3
"""build_guide.py — genera el bonus común de la tienda EN:
«US · UK · Canada · Australia Hospitality Equivalents Guide» (docx, Letter).

    python3 scripts/productos-digitales/equivalents-guide/build_guide.py [--check]

- Contenido: contenido.json (misma carpeta). Fuentes oficiales: FUENTES.md.
- Plantilla de estilo: astro-site/public/dl/bar-business-plan/bar-business-plan.docx
  (se vacía el cuerpo y se conservan estilos, Letter, márgenes; se le quita la miniatura del bar).
- Salida: astro-site/public/dl/en-shared/hospitality-equivalents-us-uk-canada-australia.docx
- --check: reabre el docx y comprueba 0 caracteres no latinos, 0 restos de español
  (heurística de tienda-gate.py), 0 «€», y estima páginas.
"""
import copy
import datetime as dt
import json
import os
import re
import sys

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TEMPLATE = os.path.join(ROOT, 'astro-site', 'public', 'dl', 'bar-business-plan', 'bar-business-plan.docx')
OUT = os.path.join(ROOT, 'astro-site', 'public', 'dl', 'en-shared',
                   'hospitality-equivalents-us-uk-canada-australia.docx')

INK = RGBColor(0x1A, 0x1A, 0x1A)
GOLD = RGBColor(0xC6, 0xA6, 0x64)
GRAY = RGBColor(0x6B, 0x6B, 0x6B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RULE = '━' * 30
RULE_H1 = '━' * 50
TABLE_PT = 8
BODY_LS = 1.2  # interlineado del cuerpo (la plantilla usa 1.5; aquí se compacta para 10-16 págs.)


# ---------------------------------------------------------------- helpers
def run(p, text, font=None, size=None, color=None, bold=None, italic=None):
    r = p.add_run(text)
    if font:
        r.font.name = font
    if size:
        r.font.size = Pt(size)
    if color is not None:
        r.font.color.rgb = color
    if bold is not None:
        r.bold = bold
    if italic is not None:
        r.italic = italic
    return r


def rich(p, text, size=None, color=None):
    """Texto con **negrita** en línea."""
    for i, part in enumerate(re.split(r'\*\*', text)):
        if part:
            run(p, part, size=size, color=color, bold=True if i % 2 else None)


def para(doc, text='', align=None, before=None, after=None, style=None):
    p = doc.add_paragraph(style=style)
    if align is not None:
        p.alignment = align
    if before is not None:
        p.paragraph_format.space_before = Pt(before)
    if after is not None:
        p.paragraph_format.space_after = Pt(after)
    if text:
        rich(p, text)
    return p


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    mar = OxmlElement('w:tblCellMar')
    for side, val in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        el = OxmlElement('w:' + side)
        el.set(qn('w:w'), str(val))
        el.set(qn('w:type'), 'dxa')
        mar.append(el)
    tblPr.append(mar)


def borders(table, color='BFBFBF'):
    tblPr = table._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + side)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), color)
        b.append(el)
    tblPr.append(b)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    h = OxmlElement('w:tblHeader')
    h.set(qn('w:val'), 'true')
    trPr.append(h)
    cs = OxmlElement('w:cantSplit')
    trPr.append(cs)


def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:cantSplit'))


def cell_text(cell, text, bold_all=False, color=None, size=TABLE_PT):
    p = cell.paragraphs[0]
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.0
    if bold_all:
        run(p, text.replace('**', ''), size=size, color=color, bold=True)
    else:
        rich(p, text, size=size, color=color)


def table(doc, head, rows, widths, first_bold=True):
    t = doc.add_table(rows=1, cols=len(head))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    borders(t)
    cell_margins(t)
    hdr = t.rows[0]
    repeat_header(hdr)
    for i, h in enumerate(head):
        c = hdr.cells[i]
        shade(c, '1A1A1A')
        cell_text(c, h, bold_all=True, color=WHITE)
    for n, r in enumerate(rows):
        row = t.add_row()
        no_split(row)
        for i, val in enumerate(r):
            c = row.cells[i]
            if i == 0 and first_bold:
                shade(c, 'F3EBD8')
                cell_text(c, val, bold_all=True, color=INK)
            else:
                if n % 2:
                    shade(c, 'FAF7F0')
                cell_text(c, val, color=INK)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Inches(w)
    # tblW / gridCol coherentes con los anchos
    grid = t._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn('w:gridCol'))):
        gc.set(qn('w:w'), str(int(widths[i] * 1440)))
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.1
        rich(p, it)


def note(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement('w:' + side)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '18' if side == 'left' else '4')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'C6A664')
        b.append(el)
    tblPr.append(b)
    cell_margins(t, 100, 100, 160, 160)
    c = t.rows[0].cells[0]
    c.width = Inches(6.3)
    shade(c, 'FBF7EE')
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.2
    rich(p, text, size=9.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def hyperlink(p, text, url, size=None):
    r_id = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement('w:hyperlink')
    h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    col = OxmlElement('w:color')
    col.set(qn('w:val'), '8A6D2B')
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(col)
    rPr.append(u)
    if size:
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(int(size * 2)))
        rPr.append(sz)
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    h.append(r)
    p._p.append(h)


def links(doc, items):
    for label, url in items:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.0
        run(p, label + ': ', size=9, bold=True)
        hyperlink(p, url.replace('https://', ''), url, size=8.5)


def page_field(p, size=8):
    for kind, text in (('begin', None), (None, ' PAGE '), ('end', None)):
        r = p.add_run()
        r.font.size = Pt(size)
        r.font.color.rgb = GRAY
        if kind:
            fc = OxmlElement('w:fldChar')
            fc.set(qn('w:fldCharType'), kind)
            r._r.append(fc)
        else:
            it = OxmlElement('w:instrText')
            it.set(qn('xml:space'), 'preserve')
            it.text = text
            r._r.append(it)


# ---------------------------------------------------------------- build
def build():
    data = json.load(open(os.path.join(HERE, 'contenido.json'), encoding='utf8'))
    meta = data['meta']
    doc = docx.Document(TEMPLATE)

    # 1. Vaciar el cuerpo (se conserva el sectPr: Letter + márgenes de la plantilla)
    body = doc.element.body
    for child in list(body):
        if child.tag != qn('w:sectPr'):
            body.remove(child)
    # 2. Quitar la miniatura del plan del bar (docProps/thumbnail.jpeg)
    pkg = doc.part.package
    for r_id, rel in list(pkg.rels.items()):
        if rel.reltype.endswith('/thumbnail'):
            del pkg.rels[r_id]

    sec = doc.sections[0]
    sec.different_first_page_header_footer = True  # portada sin pie
    sec.footer.is_linked_to_previous = False
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(fp, meta['footer'] + '  ·  ', size=8, color=GRAY)
    page_field(fp)

    # ---- Portada (mismo patrón tipográfico que la plantilla)
    for _ in range(5):
        doc.add_paragraph()
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, meta['kicker'], 'Georgia', 30, INK, True)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
    run(p, 'US · UK · Canada · Australia', 'Georgia', 24, GOLD, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, 'Hospitality Equivalents Guide', 'Georgia', 28, GOLD, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, RULE, 'Georgia', 14, GOLD, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, before=24)
    run(p, meta['subtitle'], 'Calibri', 14, GRAY, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, before=6)
    run(p, meta['bonus_line'], 'Calibri', 12, INK, True)
    for _ in range(5):
        doc.add_paragraph()
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, 'AI Chef Pro', 'Georgia', 14, INK, True)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, 'aichef.pro', 'Calibri', 11, GOLD, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, meta['date_line'], 'Calibri', 11, GRAY, False)
    page_break(doc)

    # ---- Aviso legal + índice en la misma página
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER)
    run(p, meta['legal_title'], 'Georgia', 14, INK, True)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    run(p, meta['legal'], size=9, color=GRAY)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, after=18)
    run(p, meta['copyright'], 'Calibri', 9, GOLD, False)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, before=12)
    run(p, 'CONTENTS', 'Georgia', 22, INK, True)
    doc.add_paragraph()
    for s in data['sections']:
        num, _, title = s['h1'].partition('. ')
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        run(p, f'{num}.  {title}', 'Georgia', 12.5, INK)
    p = para(doc, before=14)
    run(p, meta['contents_note'], size=10, color=GRAY, italic=True)

    # ---- Secciones
    for n, s in enumerate(data['sections']):
        h1 = doc.add_paragraph(s['h1'], style='Heading 1')
        # Heading 1 de la plantilla salta de página; aquí solo la primera sección (tras el índice):
        # el resto fluye para que la guía quede en 10-16 páginas Letter.
        h1.paragraph_format.page_break_before = (n == 0)
        h1.paragraph_format.space_before = Pt(0 if n == 0 else 22)
        h1.paragraph_format.keep_with_next = True
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        run(p, RULE_H1, size=8, color=GOLD)
        for b in s['blocks']:
            t = b['t']
            if t == 'p':
                para(doc, b['x']).paragraph_format.line_spacing = BODY_LS
            elif t == 'h2':
                doc.add_paragraph(b['x'], style='Heading 2').paragraph_format.space_before = Pt(14)
            elif t == 'bullets':
                bullets(doc, b['x'])
            elif t in ('table', 'table2', 'table3'):
                table(doc, b['head'], b['rows'], b['widths'], first_bold=(t != 'table3'))
            elif t == 'note':
                note(doc, b['x'])
            elif t == 'links':
                links(doc, b['x'])
            else:
                raise ValueError(t)

    # ---- docProps
    cp = doc.core_properties
    cp.title = meta['core_title']
    cp.subject = meta['core_subject']
    cp.author = 'AI Chef Pro'
    cp.last_modified_by = 'AI Chef Pro'
    cp.keywords = meta['core_keywords']
    cp.category = 'Bonus guide'
    cp.comments = 'Bonus included with every English edition. Updated October 2026.'
    cp.language = 'en-US'
    now = dt.datetime(2026, 10, 13, 12, 0, 0)
    cp.created = now
    cp.modified = now
    cp.revision = 1

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print('OK', os.path.relpath(OUT, ROOT), os.path.getsize(OUT), 'bytes')


# ---------------------------------------------------------------- check
RESTOS_ES = [' para ', ' con ', ' los ', ' las ', ' del ', ' una ', 'Comprar', 'COMPRAR', 'Garantía',
             'Garantia', 'escandallo', 'Escandallo', 'Productos Digitales', 'Preguntas', 'Reenviar',
             'ñ', 'á', 'é', 'í', 'ó', 'ú', '¿', '¡']
EXENTOS = ['entrée', 'Entrée']  # préstamo del inglés de carta (mismo exento que tienda-gate.py)
NO_LATINOS = re.compile(r'[Ѐ-ӿ֐-׿؀-ۿ฀-๿぀-ヿ㐀-鿿가-힯　-〿]')
EXTRA_ES = re.compile(r'\b(que|por|pero|cocina|carta|plato|impuesto|precio|también|según|horas|semana)\b', re.I)


def check():
    d = docx.Document(OUT)
    parts = [p.text for p in d.paragraphs]
    ncells = 0
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                ncells += 1
                parts.append(c.text)
    for s in d.sections:
        parts += [p.text for p in s.footer.paragraphs]
    txt = '\n'.join(parts)
    # texto de los hiperenlaces (python-docx no los devuelve en p.text en 0.8)
    xml = d.element.xml
    txt_all = txt + '\n' + ' '.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml))
    errors = []
    m = NO_LATINOS.search(txt_all)
    if m:
        errors.append('no latino: %r' % txt_all[max(0, m.start() - 40):m.end() + 40])
    limpio = txt_all
    for e in EXENTOS:
        limpio = limpio.replace(e, '')
    for w in RESTOS_ES:
        if w in limpio:
            i = limpio.index(w)
            errors.append('resto de español %r: %r' % (w, limpio[max(0, i - 40):i + 40]))
    m = EXTRA_ES.search(limpio)
    if m:
        errors.append('palabra española %r: %r' % (m.group(0), limpio[max(0, m.start() - 40):m.end() + 40]))
    if '€' in txt_all:
        errors.append('símbolo €')
    if '£' in txt_all:
        errors.append('símbolo £ (se prefiere «pounds»)')
    words = len(re.findall(r"[A-Za-z0-9]+", txt))
    n_h1 = sum(1 for p in d.paragraphs if p.style.name == 'Heading 1')
    n_tables = len(d.tables)
    rows = sum(len(t.rows) for t in d.tables)
    cp = d.core_properties
    print('abre con python-docx: OK · secciones H1:', n_h1, '· tablas:', n_tables, '· filas:', rows,
          '· celdas:', ncells, '· palabras:', words)
    print('docProps: title=%r author=%r keywords=%r' % (cp.title, cp.author, cp.keywords[:60]))
    s = d.sections[0]
    print('página: %.2f x %.2f in · márgenes L%.2f R%.2f T%.2f B%.2f' % (
        s.page_width.inches, s.page_height.inches, s.left_margin.inches, s.right_margin.inches,
        s.top_margin.inches, s.bottom_margin.inches))
    if errors:
        print('ERRORES:')
        for e in errors:
            print('  -', e)
        return 1
    print('0 caracteres no latinos · 0 restos de español · 0 € · 0 £')
    return 0


if __name__ == '__main__':
    if '--check' not in sys.argv or '--build' in sys.argv:
        build()
    sys.exit(check())
