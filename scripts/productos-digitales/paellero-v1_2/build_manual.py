#!/usr/bin/env python3
"""build_manual.py — Manual Técnico Paellero Profesional v1.2.

Abre el docx actual como plantilla (estilos, A4, márgenes, propiedades), conserva las
4 líneas de portada (con subtítulo actualizado) y sustituye el cuerpo por el Markdown.
Uso: build_manual.py <manual-v2.md> [docx-destino]
"""
import re, sys, copy
import docx
from docx.shared import Pt, RGBColor, Emu
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

DOCX = '/root/wt-manual/astro-site/public/dl/plan-negocio-paellero-eventos/manual-tecnico-paellero-profesional.docx'
SUBTITULO = 'Escalado y quemadores · Técnica del fuego · Caldos · Seguridad · Alérgenos · Cocción de 12 paellas'

md_path = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else DOCX
d = docx.Document(DOCX)
body = d.element.body

# Conservar 5 primeros elementos (4 líneas de portada + salto de página); borrar el resto salvo sectPr
kids = list(body)
for el in kids[5:]:
    if el.tag != qn('w:sectPr'):
        body.remove(el)
# Subtítulo
sub = d.paragraphs[1]
sub.runs[0].text = SUBTITULO
for r in sub.runs[1:]:
    r.text = ''

def fmt_heading(p, size):
    for r in p.runs:
        r.font.name = 'Cambria'
        r._element.rPr.rFonts.set(qn('w:hAnsi'), 'Cambria')
        r.font.bold = True
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0x0A, 0x09, 0x08)

def add_runs(p, text):
    # soporta **negrita** y *cursiva*
    for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text):
        if not part:
            continue
        if part.startswith('**'):
            p.add_run(part[2:-2]).bold = True
        elif part.startswith('*'):
            p.add_run(part[1:-1]).italic = True
        else:
            p.add_run(part)

def set_spacing_after(p, twips):
    pPr = p._p.get_or_add_pPr()
    sp = pPr.find(qn('w:spacing'))
    if sp is None:
        sp = OxmlElement('w:spacing'); pPr.append(sp)
    sp.set(qn('w:after'), str(twips))

TOTAL_W = 8277  # dxa útiles A4 con márgenes 3,2 cm

def add_table(rows):
    n = len(rows[0])
    t = d.add_table(rows=len(rows), cols=n)
    t.style = d.styles['Light Grid Accent 1']
    t.alignment = 1
    # anchuras: primera columna algo más ancha
    lens = [max(len(r[i]) for r in rows) for i in range(n)]
    w = [min(max(l, 6), 38) for l in lens]
    tot = sum(w)
    widths = [int(TOTAL_W * x / tot) for x in w]
    for ri, row in enumerate(rows):
        for ci, txt in enumerate(row):
            c = t.rows[ri].cells[ci]
            c.width = Emu(widths[ci] * 635)
            p = c.paragraphs[0]
            if ri == 0:
                r = p.add_run(txt); r.bold = True; r.font.color.rgb = RGBColor(0x0A, 0x09, 0x08)
            else:
                add_runs(p, txt)
            if n >= 8:
                for r in p.runs:
                    r.font.size = Pt(8.5)
            elif n >= 6:
                for r in p.runs:
                    r.font.size = Pt(9.5)
    # tblGrid acorde
    grid = t._tbl.tblGrid
    for gc, wv in zip(grid.findall(qn('w:gridCol')), widths):
        gc.set(qn('w:w'), str(wv))
    # espacio posterior
    sp = d.add_paragraph(); set_spacing_after(sp, 60)

lines = open(md_path, encoding='utf-8').read().split('\n')
i = 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith('# '):
        p = d.add_paragraph(style='Heading 1'); p.add_run(ln[2:].strip()); fmt_heading(p, 20)
        p.paragraph_format.space_before = Pt(18)
    elif ln.startswith('## '):
        p = d.add_paragraph(style='Heading 2'); p.add_run(ln[3:].strip()); fmt_heading(p, 15)
        p.paragraph_format.space_before = Pt(10)
    elif ln.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
                rows.append(cells)
            i += 1
        add_table(rows)
        continue
    elif ln.startswith('- '):
        p = d.add_paragraph(style='List Bullet'); add_runs(p, ln[2:].strip()); set_spacing_after(p, 40)
    elif re.match(r'\d+\. ', ln):
        p = d.add_paragraph(style='List Number'); add_runs(p, re.sub(r'^\d+\. ', '', ln).strip()); set_spacing_after(p, 40)
    elif ln.strip():
        p = d.add_paragraph(); add_runs(p, ln.strip()); set_spacing_after(p, 120)
    i += 1

# sectPr debe ser el último hijo
sect = body.find(qn('w:sectPr'))
if sect is not None:
    body.remove(sect); body.append(sect)

cp = d.core_properties
cp.author = 'AI Chef Pro'
cp.title = 'Manual Técnico Paellero Profesional · v1.2'
d.save(out)
print('guardado', out)
