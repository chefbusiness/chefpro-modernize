#!/usr/bin/env python3
"""Maqueta el eBook EN (PDF) reproduciendo el diseño del PDF ES publicado (SPEC §4.4).

El ES salió de Google Docs y su .docx ya no existe, así que aquí se calca a partir de lo MEDIDO en el PDF
publicado (3-oct-2026, PyMuPDF): Letter 612×792, márgenes 72 pt, Arial (las mismas TTF del sistema), cuerpo
10/11,5 #333 con sangría 18 pt, número del prompt en oro #f5c741, título Bold 11, línea de agentes 9 pt #666,
separadores #eeeeee de 1 pt, encabezado de sección Bold 16 en el color del bloque (#1d3a5e · #2d794e · #c65c1a)
con filete de 1 pt, cada sección y cada bloque en página nueva, sin números de página.

Entrada: en/parte-1..4.json (gate_en.py en VERDE) + es.json (estructura y colores).
Salida:  ../../../astro-site/public/dl/ai-prompts-for-restaurants/gastro-pro-prompts-ebook.pdf  (o --salida).
Ligero: ~1 s de CPU en el Mac.
"""
import argparse
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer)
from reportlab.platypus.flowables import HRFlowable

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
SALIDA = RAIZ / 'astro-site/public/dl/ai-prompts-for-restaurants/gastro-pro-prompts-ebook.pdf'
FUENTES = Path('/System/Library/Fonts/Supplemental')

for nombre, fichero in (('Arial', 'Arial.ttf'), ('Arial-Bold', 'Arial Bold.ttf'),
                        ('Arial-Italic', 'Arial Italic.ttf'), ('Arial-BoldItalic', 'Arial Bold Italic.ttf')):
    pdfmetrics.registerFont(TTFont(nombre, str(FUENTES / fichero)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold', italic='Arial-Italic',
                              boldItalic='Arial-BoldItalic')

NEGRO, GRIS, CUERPO, ORO = '#1a1a1a', '#666666', '#333333', '#f5c741'
NAVY = '#1d3a5e'
ANCHO = 468


def st(nombre, fuente='Arial', tam=10, color=NEGRO, leading=None, align=TA_LEFT, **kw):
    return ParagraphStyle(nombre, fontName=fuente, fontSize=tam, textColor=HexColor(color),
                          leading=leading or tam * 1.15, alignment=align, **kw)


S = {
    'marca': st('marca', 'Arial-Bold', 36, NEGRO, 41, TA_CENTER),
    'titulo': st('titulo', 'Arial-Bold', 24, NAVY, 28, TA_CENTER),
    'sub': st('sub', 'Arial-Italic', 12, GRIS, 14, TA_CENTER),
    'stats': st('stats', 'Arial-Bold', 11, NEGRO, 13, TA_CENTER),
    'publico': st('publico', 'Arial-Italic', 10, GRIS, 13.5, TA_CENTER),
    'url12': st('url12', 'Arial-Bold', 12, NEGRO, 14, TA_CENTER),
    'h_bienv': st('h_bienv', 'Arial-Bold', 16, NEGRO, 19),
    'p_bienv': st('p_bienv', 'Arial', 10, NEGRO, 11.5),
    'h2_bienv': st('h2_bienv', 'Arial-Bold', 13, NEGRO, 15),
    'nota': st('nota', 'Arial-Italic', 10, GRIS, 11.5),
    'paso': st('paso', 'Arial', 10, NEGRO, 14.5),
    'bloque_et': lambda c: st('bloque_et', 'Arial-Bold', 14, c, 17, TA_CENTER),
    'bloque_tit': st('bloque_tit', 'Arial-Bold', 20, NEGRO, 23, TA_CENTER),
    'bloque_rango': st('bloque_rango', 'Arial', 11, GRIS, 13, TA_CENTER),
    'bloque_intro': st('bloque_intro', 'Arial-Italic', 10, GRIS, 11.5),
    'sec': lambda c: st('sec', 'Arial-Bold', 16, c, 18.5),
    'sec_rango': st('sec_rango', 'Arial-Italic', 9.5, GRIS, 12),
    'num': st('num', 'Arial-Bold', 11, NEGRO, 12.5),
    'cuerpo': st('cuerpo', 'Arial', 10, CUERPO, 11.5, leftIndent=18),
    'apps': st('apps', 'Arial', 9, GRIS, 12.5, leftIndent=18),
    'gracias': st('gracias', 'Arial-Bold', 18, NEGRO, 21, TA_CENTER),
    'cierre_p': st('cierre_p', 'Arial', 11, GRIS, 14, TA_CENTER),
    'cierre_i': st('cierre_i', 'Arial-Italic', 11, NAVY, 14, TA_CENTER),
    'url14': st('url14', 'Arial-Bold', 14, NEGRO, 16, TA_CENTER),
}


def P(texto, estilo):
    return Paragraph(escape(texto), estilo)


def regla(color, grosor=1, antes=0, despues=0):
    return HRFlowable(width=ANCHO, thickness=grosor, color=HexColor(color), spaceBefore=antes, spaceAfter=despues,
                      hAlign='LEFT')


def carga(desde_es=False):
    es = json.loads((AQUI / 'es.json').read_text())
    patron = 'entrada/es-parte-{}.json' if desde_es else 'en/parte-{}.json'
    partes = [json.loads((AQUI / patron.format(i)).read_text()) for i in range(1, 5)]
    front = partes[0]
    prompts = {p['n']: p for parte in partes for p in parte['prompts']}
    return es, front, prompts


def portada(front):
    t = [x['texto'] for x in front['portada']]
    # Espaciados calibrados contra las líneas base del PDF ES (±1 pt).
    return [Spacer(1, 30), P(t[0], S['marca']), Spacer(1, 3.6), P(t[1], S['titulo']),
            Spacer(1, 33.4), regla(ORO, 2, 0, 17.3), P(t[2], S['sub']), Spacer(1, 22.6),
            Paragraph(escape(t[3]).replace('  ', '&nbsp;&nbsp;'), S['stats']),
            Spacer(1, 22.3), P(f'{t[4]} {t[5]}', S['publico']), Spacer(1, 25.5), P(t[6], S['url12']), PageBreak()]


def bienvenida(front):
    t = [x['texto'] for x in front['bienvenida']]
    out = [Spacer(1, 23.7), P(t[0], S['h_bienv']), regla('#dddddd', 1, 16.8, 15), P(t[1], S['p_bienv']),
           Spacer(1, 28.4), P(t[2], S['h2_bienv']), Spacer(1, 3.2)]
    for linea, nota in ((t[3], t[4]), (t[5], t[6]), (t[7], t[8])):
        out += [P(linea, S['p_bienv']), Spacer(1, 3), P(nota, S['nota']), Spacer(1, 16)]
    out += [Spacer(1, 12.4), P(t[9], S['h2_bienv']), Spacer(1, 3.2)]
    pasos = [x.strip() for x in re.split(r'\s(?=[1-9]\.\s)', t[10]) if x.strip()]
    out += [P(p, S['paso']) for p in pasos]
    return out + [PageBreak()]


def pagina_bloque(b_es, b_en):
    c = b_es['color']
    return [Spacer(1, 12), P(b_en['etiqueta'], S['bloque_et'](c)), Spacer(1, 6), P(b_en['titulo'], S['bloque_tit']),
            Spacer(1, 4), P(b_en['rango'], S['bloque_rango']), Spacer(1, 4), regla(c, 2, 14, 16),
            P(b_en['intro'], S['bloque_intro']), PageBreak()]


def prompt(p, ultimo):
    apps = p['apps']
    etiqueta = 'Recommended agent:' if len(apps) == 1 else 'Recommended agents:'
    if any(ord(ch) > 127 for ch in p['titulo'] + p['cuerpo']) and 'ó' in p['cuerpo'] + p['titulo']:
        etiqueta = 'App recomendada:'  # solo en la prueba de fidelidad con el texto ES
    cab = Paragraph(f'<font color="{ORO}">#{p["n"]:03d}&nbsp;&nbsp;</font>{escape(p["titulo"])}', S['num'])
    cuerpo = Paragraph(escape(p['cuerpo']), S['cuerpo'])
    linea = Paragraph(f'<b>{escape(etiqueta)}</b> <i>{escape(", ".join(apps))}</i>', S['apps'])
    # Cabecera pegada a las primeras líneas del cuerpo (el ES nunca deja un título huérfano al pie).
    out = [KeepTogether([cab, Spacer(1, 4.1), cuerpo, Spacer(1, 1.1), linea])]
    if not ultimo:
        out += [regla('#eeeeee', 1, 15.7, 8.4)]
    return out


def seccion(c_es, s_en, prompts):
    color = c_es['color']
    out = [P(s_en['encabezado'], S['sec'](color)), Spacer(1, 3), P(s_en['rango'], S['sec_rango']),
           regla(color, 1, 15, 9.5)]
    ns = [p['n'] for p in c_es['prompts']]
    for i, n in enumerate(ns):
        out += prompt(prompts[n], i == len(ns) - 1)
    return out + [PageBreak()]


def cierre(front):
    t = [x['texto'] for x in front['cierre']]
    return [Spacer(1, 49.3), P(t[0], S['gracias']), Spacer(1, 3.2), P(t[1], S['cierre_p']), Spacer(1, 1.6),
            P(t[2], S['cierre_i']), Spacer(1, 37.3), P(t[3], S['url14'])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida', default=str(SALIDA))
    ap.add_argument('--desde-es', action='store_true',
                    help='maqueta el texto ES con este diseño para compararlo con el PDF publicado (fidelidad)')
    a = ap.parse_args()
    es, front, prompts = carga(a.desde_es)
    historia = portada(front) + bienvenida(front)
    k = 0
    for bi, b_es in enumerate(es['bloques']):
        historia += pagina_bloque(b_es, front['bloques'][bi])
        for c_es in b_es['categorias']:
            historia += seccion(c_es, front['secciones'][k], prompts)
            k += 1
    historia += cierre(front)
    salida = Path(a.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(salida), pagesize=letter, leftMargin=66, rightMargin=66, topMargin=66,
                            bottomMargin=66, title='Gastro Pro Prompts eBook — 300 AI Prompts for Restaurants & Hospitality',
                            author='AI Chef Pro', subject='AI Chef Pro · aichef.pro', creator='AI Chef Pro')
    doc.build(historia)
    print(f'OK · {salida} · {salida.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
