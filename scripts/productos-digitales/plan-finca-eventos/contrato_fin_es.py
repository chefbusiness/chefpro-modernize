#!/usr/bin/env python3
"""
contrato_fin_es.py — Plan de Negocio: Finca de Eventos y Bodas ES 1.0 (SPEC D10): `modelo-contrato-reserva-finca-eventos.docx`.
Abre el docx de modelos de contrato del parrillero como MOLDE FÍSICO (estilos `Normal` y `List Bullet`, A4, márgenes, fuentes),
vacía el cuerpo (conserva la sección) y escribe `textos/contrato_es.json`: lista de `{"estilo": …, "texto": …}`.

Estilos admitidos: Kicker · Title · Subtitle · H1 · H2 · Normal · List Bullet · Separador · Firma
(`Kicker`, `Title`, `Subtitle`, `H1`, `H2` y `Separador` reproducen el formato directo del molde sobre `Normal`; `Normal` y
`List Bullet` usan el estilo del molde). `**negrita**` dentro del texto. Gates: A4, 0 tokens `__nombre__`, sin caracteres no latinos.

    /root/venv-guias/bin/python contrato_fin_es.py --salida <dir> [--texto textos/contrato_es.json] [--molde <docx>]

Sesión Claude Code, 25-oct-2026.
"""
import argparse
import copy
import datetime
import json
import os
import re
import sys
import unicodedata

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Mm, Pt, RGBColor

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import fin_version                                                                 # noqa: E402  (VERSION 1.0 · noviembre 2026)

PID = 'plan-negocio-finca-eventos-bodas'
FICHERO = 'modelo-contrato-reserva-finca-eventos.docx'
MOLDE = os.path.join(os.path.dirname(os.path.dirname(AQUI)), '..', 'astro-site', 'public', 'dl',
                     'plan-negocio-parrillero-asador-eventos', 'modelos-contrato-parrillero-asador-eventos.docx')
TEXTO = os.path.join(AQUI, 'textos', 'contrato_es.json')
TITULO = 'Modelo de contrato de reserva de finca para bodas y eventos · v%s' % fin_version.VERSION
FECHA = datetime.datetime(2026, 10, 25)
#: formato directo del molde: (fuente, negrita, cursiva, color, medio-puntos)
FORMATO = {'Kicker': (None, True, False, 'B08D57', 9), 'Title': ('Playfair Display', True, False, '1F1B16', 28),
           'Subtitle': (None, False, True, '6B5E4D', 12), 'H1': ('Playfair Display', True, False, '1F1B16', 18),
           'H2': ('Inter', True, False, '1F1B16', 13), 'Separador': (None, False, False, 'B08D57', 11)}
ESTILOS = set(FORMATO) | {'Normal', 'List Bullet', 'Firma'}
RX_TOKEN = re.compile(r'__[A-Za-zÁ-ÿ][\w ]*__')
RX_NEGRITA = re.compile(r'(\*\*.+?\*\*)')


def no_latino(texto):
    """Caracteres de alfabetos no latinos (CJK, cirílico, griego, árabe, hebreo, hangul, tailandés…)."""
    return sorted({c for c in texto if c.isalpha() and 'LATIN' not in unicodedata.name(c, 'LATIN')})


def runs(p, texto, fmt=None):
    for trozo in RX_NEGRITA.split(texto):
        if not trozo:
            continue
        negrita = trozo.startswith('**') and trozo.endswith('**') and len(trozo) > 4
        r = p.add_run(trozo[2:-2] if negrita else trozo)
        if fmt:
            fuente, b, i, color, pt = fmt
            if fuente:
                r.font.name = fuente
            r.font.bold, r.font.italic, r.font.size = b or negrita or None, i or None, Pt(pt)
            r.font.color.rgb = RGBColor.from_string(color)
        elif negrita:
            r.font.bold = True


def generar(salida, texto=TEXTO, molde=MOLDE):
    items = json.load(open(texto, encoding='utf8'))
    err = []
    doc = Document(molde)
    body = doc.element.body
    for hijo in list(body):
        if not hijo.tag.endswith('}sectPr'):
            body.remove(hijo)
    for it in items:
        est, t = it['estilo'], it['texto']
        if est not in ESTILOS:
            err.append('estilo desconocido %r' % est)
            continue
        if est in ('Normal', 'List Bullet', 'Firma'):
            p = doc.add_paragraph(style='List Bullet' if est == 'List Bullet' else 'Normal')
            p.paragraph_format.space_after = Pt(4 if est == 'List Bullet' else 8)
            runs(p, t)
        else:
            p = doc.add_paragraph(style='Normal')
            if est == 'Separador':
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10 if est in ('H1', 'H2') else 0)
            runs(p, t or '·  ·  ·', FORMATO[est])
            if est in ('H1', 'H2', 'Kicker'):
                p.paragraph_format.keep_with_next = True
    sec = doc.sections[0]
    pr = doc.core_properties
    pr.title, pr.subject, pr.author, pr.last_modified_by = TITULO, '', 'AI Chef Pro', 'AI Chef Pro'
    pr.comments, pr.keywords = 'aichef.pro/%s' % PID, ''
    pr.created = pr.modified = FECHA
    os.makedirs(salida, exist_ok=True)
    destino = os.path.join(salida, FICHERO)
    doc.save(destino)
    # gates sobre el fichero escrito
    d2 = Document(destino)
    todo = '\n'.join(p.text for p in d2.paragraphs)
    s = d2.sections[0]
    if abs(s.page_width - Mm(210)) > Mm(1) or abs(s.page_height - Mm(297)) > Mm(1):
        err.append('no es A4: %.0f x %.0f mm' % (s.page_width.mm, s.page_height.mm))
    if RX_TOKEN.search(todo):
        err.append('tokens sin resolver: %r' % RX_TOKEN.findall(todo)[:5])
    if '**' in todo:
        err.append('negrita sin cerrar (**)')
    if no_latino(todo):
        err.append('caracteres no latinos: %r' % no_latino(todo))
    if d2.core_properties.author != 'AI Chef Pro' or d2.core_properties.created.year != 2026:
        err.append('docProps: autor o año')
    estilos = {p.style.name for p in d2.paragraphs}
    if not estilos <= {'Normal', 'List Bullet'}:
        err.append('estilos fuera del molde: %r' % estilos)
    palabras = len(todo.split())
    for e in err:
        print('ERROR', e)
    print('%s: %d párrafos · %d palabras · A4 · estilos %s · %s' % (FICHERO, len(d2.paragraphs), palabras, sorted(estilos),
                                                                  'VERDE' if not err else 'ROJO (%d errores)' % len(err)))
    return destino, 1 if err else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida', required=True)
    ap.add_argument('--texto', default=TEXTO)
    ap.add_argument('--molde', default=MOLDE)
    a = ap.parse_args()
    sys.exit(generar(a.salida, a.texto, a.molde)[1])
