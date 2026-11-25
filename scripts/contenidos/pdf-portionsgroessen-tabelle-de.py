#!/usr/bin/env python3
"""PDF gratuito (1 página A4) «Portionsgrößen-Tabelle für die Gastronomie».

Fuente única: astro-site/src/content/blog/de/portionsgroessen-tabelle.md.
La tabla y las reglas se EXTRAEN del post (parser de <table> y frases ancladas);
si algo no aparece, el script falla, así el PDF nunca se separa del post.
Uso: python3 scripts/contenidos/pdf-portionsgroessen-tabelle-de.py
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POST = ROOT / 'astro-site/src/content/blog/de/portionsgroessen-tabelle.md'
PDF = ROOT / 'astro-site/public/descargas/portionsgroessen-tabelle-gastronomie-aichef.pdf'
NOTA = 'Richtwerte für Erwachsene. Planen Sie mit Ihren eigenen Rezepturen und Garverlusten.'
PIE = 'Kostenlose Tabelle von AI Chef Pro · Artikel: <a href="https://aichef.pro/de/blog/portionsgroessen-tabelle" color="#0563C1">aichef.pro/de/blog/portionsgroessen-tabelle</a>'


class Tablas(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tablas, self._t, self._f, self._c = [], None, None, None

    def handle_starttag(self, tag, a):
        if tag == 'table': self._t = []
        elif tag == 'tr' and self._t is not None: self._f = []
        elif tag in ('td', 'th') and self._f is not None: self._c = ''

    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self._c is not None:
            self._f.append(' '.join(self._c.split())); self._c = None
        elif tag == 'tr' and self._f is not None:
            self._t.append(self._f); self._f = None
        elif tag == 'table' and self._t is not None:
            self.tablas.append(self._t); self._t = None

    def handle_data(self, d):
        if self._c is not None: self._c += d


def texto_plano(fragmento):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', '', fragmento)).split())


def main():
    src = POST.read_text(encoding='utf-8')
    cuerpo = src.split('\n---\n', 1)[1]
    p = Tablas(); p.feed(cuerpo)
    tabla = next((t for t in p.tablas if t[0][:2] == ['Komponente', 'Portion pro Person']), None)
    if not tabla: sys.exit('FALLO: tabla «Komponente / Portion pro Person» no encontrada en el post')
    if len(tabla) < 10: sys.exit(f'FALLO: la tabla tiene {len(tabla)} filas, se esperaban 10 (cabecera + 9)')

    frases = []
    for par in re.findall(r'<p>(.*?)</p>', cuerpo, re.S):
        t = texto_plano(par)
        frases += re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', t)

    def frase(ancla):
        r = [f for f in frases if f.startswith(ancla)]
        if len(r) != 1: sys.exit(f'FALLO: frase «{ancla}» encontrada {len(r)} veces en el post')
        return r[0]

    garverlust = [frase('Fleisch verliert beim Garen'), frase('Nudeln verdoppeln ihr Gewicht'), frase('Reis verdreifacht sein Gewicht')]
    reglas = [
        ('Menü', frase('Im Menü mit drei oder mehr Gängen')),
        ('Buffet', frase('Für das Abendbuffet gilt')),
        ('Fingerfood', frase('Wenn der Empfang das Abendessen ersetzt') + ' ' + frase('Wird das Fingerfood nur als Aperitif')),
        ('Senioren und Kinder', frase('Für Senioren rechnen Sie') + ' ' + frase('Bei Kindern hängt die Menge')),
    ]
    # El texto del post usa la forma «Für Senioren rechnen Sie rund 20 Prozent ...»; si cambia, falla arriba.

    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    gris, negro = colors.HexColor('#999999'), colors.HexColor('#111111')
    base = ParagraphStyle('b', fontName='Helvetica', fontSize=9, leading=11.5)
    cab = ParagraphStyle('c', parent=base, fontName='Helvetica-Bold')
    h = ParagraphStyle('h', parent=base, fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=negro, spaceBefore=8, spaceAfter=4)
    cur = ParagraphStyle('i', parent=base, fontName='Helvetica-Oblique', fontSize=8.5, leading=11)
    esc = lambda s: html.escape(s, quote=False)

    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=12 * mm, bottomMargin=12 * mm,
                            title='Portionsgrößen-Tabelle für die Gastronomie', author='AI Chef Pro')
    W = A4[0] - 28 * mm
    el = []
    band = Table([['Portionsgrößen-Tabelle für die Gastronomie']], colWidths=[W])
    band.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), negro), ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#FFD700')),
                              ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 16),
                              ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8), ('LEFTPADDING', (0, 0), (-1, -1), 8)]))
    el += [band, Spacer(1, 4), Paragraph('Wie viel Gramm pro Person? Richtwerte à la carte', h)]
    filas = [[Paragraph(esc(c), cab) for c in tabla[0]]] + [[Paragraph(esc(c), cab if i == 0 else base) for i, c in enumerate(f)] for f in tabla[1:]]
    t = Table(filas, colWidths=[W * 0.27, W * 0.23, W * 0.50], repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, gris), ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F3F3F3')),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    el += [t, Paragraph('Roh oder gegart? Das Garen verändert das Gewicht', h)]
    el += [Paragraph('– ' + esc(g), base) for g in garverlust]
    el += [Paragraph('Menü, Buffet und mehr', h)]
    rt = Table([[Paragraph(esc(k), cab), Paragraph(esc(v), base)] for k, v in reglas], colWidths=[W * 0.2, W * 0.8])
    rt.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, gris), ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F3F3F3')),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    el += [rt, Spacer(1, 8), Paragraph(esc(NOTA), cur), Spacer(1, 3), Paragraph(PIE, cur)]
    doc.build(el)

    from pypdf import PdfReader
    r = PdfReader(str(PDF))
    txt = ' '.join(' '.join(pg.extract_text().split()) for pg in r.pages)
    assert len(r.pages) == 1, f'{len(r.pages)} páginas'
    for k in ('Kartoffeln', '200 bis 250 g', 'Gemüse', '20 bis 25 Prozent', '500 bis 600 g'):
        assert k in txt, f'falta «{k}» en el PDF'
    print(f'OK {PDF.relative_to(ROOT)} · {len(r.pages)} Seite · {len(tabla) - 1} Zeilen')


main()
