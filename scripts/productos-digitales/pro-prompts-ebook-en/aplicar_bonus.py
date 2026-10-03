#!/usr/bin/env python3
"""Bonos del eBook EN: traducción EN SITIO de los ficheros ES publicados (SPEC §4.5).

  python3 aplicar_bonus.py --extraer   → entrada/bonus-es.json  (cada run de texto del .docx y cada celda de texto del .xlsx, con id)
  python3 aplicar_bonus.py --aplicar   → lee en/bonus-en.json (mismos ids) y escribe los dos ficheros EN en
                                          astro-site/public/dl/ai-prompts-for-restaurants/

Se traduce NODO DE TEXTO a nodo (<w:t>, no párrafo a párrafo) para conservar la negrita de «1. ROL» o «→ "…"» del .docx, y celda a celda en el
.xlsx, así que estilos, anchos, combinaciones y colores quedan los del ES byte a byte salvo el texto. Los runs sin letras
(«1. », «→  ») no se extraen. El gate final es el mismo de las partes: sin español, sin no latinos, sin euros.
"""
import argparse
import json
import re
import sys
from pathlib import Path

import docx
import openpyxl
from docx.oxml.ns import qn

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
DOCX_ES = RAIZ / 'astro-site/public/dl/b1-7e48bcc611ef54e4.docx'
XLSX_ES = RAIZ / 'astro-site/public/dl/b23-7e48bcc611ef54e4.xlsx'
DESTINO = RAIZ / 'astro-site/public/dl/ai-prompts-for-restaurants'
DOCX_EN = DESTINO / 'bonus-1-prompt-engineering-guide.docx'
XLSX_EN = DESTINO / 'bonus-2-3-templates-cheat-sheet.xlsx'
LETRA = re.compile(r'[A-Za-zÁÉÍÓÚÑáéíóúñü]')


def runs_docx(d):
    """Cada nodo de texto <w:t> del cuerpo, en orden de documento.

    Antes se iba por párrafos y runs de python-docx deduplicando las celdas con id(p._p): los proxies de lxml no son
    estables, id() se reutilizaba y se saltaban 20 textos de las tablas BIEN/MAL sin avisar (cazado el 3-oct por el
    barrido de idioma). Ir al nodo w:t no depende de la estructura (tablas, celdas combinadas, hipervínculos).
    """
    for i, t in enumerate(d.element.body.iter(qn('w:t'))):
        if t.text and LETRA.search(t.text):
            yield f't{i}', t


def celdas_xlsx(wb):
    for ws in wb.worksheets:
        for fila in ws.iter_rows():
            for c in fila:
                if isinstance(c.value, str) and LETRA.search(c.value) and not c.value.startswith('='):
                    yield f'{ws.title}!{c.coordinate}', c


def extraer():
    d = docx.Document(DOCX_ES)
    wb = openpyxl.load_workbook(XLSX_ES)
    out = {'docx_titulo': d.core_properties.title or '',
           'docx': [{'id': i, 'texto': r.text} for i, r in runs_docx(d)],
           'hojas': [ws.title for ws in wb.worksheets],
           'xlsx': [{'id': i, 'texto': c.value} for i, c in celdas_xlsx(wb)]}
    (AQUI / 'entrada').mkdir(exist_ok=True)
    (AQUI / 'entrada/bonus-es.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"OK · docx {len(out['docx'])} runs · xlsx {len(out['xlsx'])} celdas · hojas {out['hojas']}")


def aplicar():
    es = json.loads((AQUI / 'entrada/bonus-es.json').read_text())
    en = json.loads((AQUI / 'en/bonus-en.json').read_text())
    for k in ('docx', 'xlsx'):
        ids_es, ids_en = [x['id'] for x in es[k]], [x['id'] for x in en[k]]
        if ids_es != ids_en:
            sys.exit(f'{k}: los ids EN no coinciden con los ES ({len(ids_en)} vs {len(ids_es)})')
    if len(en['hojas']) != len(es['hojas']):
        sys.exit('hojas: distinto número')
    tdoc = {x['id']: x['texto'] for x in en['docx']}
    txls = {x['id']: x['texto'] for x in en['xlsx']}

    d = docx.Document(DOCX_ES)
    for i, r in runs_docx(d):
        r.text = tdoc[i]
        r.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    d.core_properties.title = en.get('docx_titulo') or 'Bonus 1 — Restaurant Prompt Engineering Guide'
    d.core_properties.language = 'en-US'
    for st in d.styles:                      # corrector ortográfico en inglés al abrirlo en Word
        try:
            rpr = st.element.get_or_add_rPr()
            lang = rpr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}lang')
            if lang is not None:
                lang.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'en-US')
        except AttributeError:
            pass

    wb = openpyxl.load_workbook(XLSX_ES)
    for i, c in list(celdas_xlsx(wb)):
        c.value = txls[i]
    for ws, nombre in zip(wb.worksheets, en['hojas']):
        ws.title = nombre[:31]
    wb.properties.title = 'Bonus 2 & 3 — Prompt Templates + Cheat Sheet'

    DESTINO.mkdir(parents=True, exist_ok=True)
    d.save(DOCX_EN)
    wb.save(XLSX_EN)
    print(f'OK · {DOCX_EN.name} {DOCX_EN.stat().st_size:,} B · {XLSX_EN.name} {XLSX_EN.stat().st_size:,} B')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--extraer', action='store_true')
    g.add_argument('--aplicar', action='store_true')
    a = ap.parse_args()
    extraer() if a.extraer else aplicar()
