#!/usr/bin/env python3
"""Extrae el eBook Pro Prompts ES PUBLICADO a una estructura JSON (fuente del duplicado EN).

Por qué del PDF y no de un .docx: el PDF publicado (`public/dl/pp-7e48bcc611ef54e4.pdf`) salió de
`ProPrompts_eBook_v2_plain.docx` exportado con Google Docs, y ese .docx ya no existe. El que queda en
Descargas (`ProPrompts_eBook_AIChefPro_300.docx`) es una versión ANTERIOR con otra maquetación (tablas)
y ~150 palabras distintas. Regla de la tienda internacional: la fuente de un duplicado son los ficheros
PUBLICADOS.

Clasifica cada línea por su estilo (fuente, tamaño, color), medido sobre el PDF el 3-oct-2026:
  Bold 16 #1d3a5e  → encabezado de categoría      Italic 9.5 #666 → «Prompts #a – #b»
  Bold 11 #f5c741  → número del prompt («#001»)   Bold 11 #1a1a1a → título del prompt (misma línea)
  Regular 10 #333  → cuerpo del prompt            Bold/Italic 9 #666 → «App recomendada: …»
  Bold 14 #1d3a5e  → «BLOQUE X» (página de bloque) Bold 20 → título del bloque · Regular 11 #666 → rango
Cada categoría y cada bloque empiezan página nueva; la portada (p. 1), la bienvenida (p. 2) y el cierre
(última) se guardan como líneas con su estilo para que el maquetador EN las reproduzca.

Uso: python3 extraer_es.py  →  escribe es.json junto a este script y un resumen por stdout.
"""
import json
import re
import sys
from pathlib import Path

import fitz

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
PDF = RAIZ / 'astro-site/public/dl/pp-7e48bcc611ef54e4.pdf'


def estilo(s):
    f = s['font']
    peso = 'B' if 'Bold' in f else ('I' if 'Italic' in f else 'R')
    return peso, round(s['size'], 1), '#%06x' % s['color']


def lineas(pagina):
    """Líneas no vacías con (x, y, estilo del primer span, spans, texto)."""
    out = []
    for b in pagina.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            sp = [s for s in l['spans'] if s['text'].strip()]
            if not sp:
                continue
            out.append({'x': round(l['bbox'][0]), 'y': l['bbox'][1], 'y1': l['bbox'][3],
                        'st': estilo(sp[0]), 'spans': sp,
                        'text': ''.join(s['text'] for s in l['spans']).strip()})
    return out


def une(trozos):
    t = ' '.join(x.strip() for x in trozos)
    return re.sub(r'\s+', ' ', t).strip()


def parrafos(ls):
    """Agrupa líneas consecutivas del mismo estilo y sin hueco vertical en párrafos."""
    out = []
    for l in ls:
        if out and out[-1]['st'] == l['st'] and l['y'] - out[-1]['y1'] < 4 and out[-1]['x'] == l['x']:
            out[-1]['lineas'].append(l['text'])
            out[-1]['y1'] = l['y1']
        else:
            out.append({'st': l['st'], 'x': l['x'], 'y1': l['y1'], 'lineas': [l['text']]})
    return [{'estilo': '%s-%s-%s' % p['st'], 'centrado': p['x'] > 100, 'texto': une(p['lineas']),
             'lineas': p['lineas']} for p in out]


def main():
    d = fitz.open(PDF)
    n = len(d)
    doc = {'fuente': str(PDF.relative_to(RAIZ)), 'paginas': n,
           'portada': parrafos(lineas(d[0])), 'bienvenida': parrafos(lineas(d[1])),
           'cierre': parrafos(lineas(d[n - 1])), 'bloques': []}
    bloque = cat = prompt = None
    campo = None  # 'body' | 'apps' | 'intro'

    for pno in range(2, n - 1):
        for l in lineas(d[pno]):
            st, t = l['st'], l['text']
            if st[:2] == ('B', 14.0) and t.startswith('BLOQUE'):   # «BLOQUE A» (cada bloque, su color)
                bloque = {'etiqueta': t, 'color': st[2], 'titulo': '', 'rango': '', 'intro': [], 'categorias': []}
                doc['bloques'].append(bloque)
                cat = prompt = None
                campo = 'intro'
            elif st == ('B', 20.0, '#1a1a1a') and bloque is not None and not bloque['categorias']:
                bloque['titulo'] = une([bloque['titulo'], t])
            elif st == ('R', 11.0, '#666666') and bloque is not None and not bloque['categorias']:
                bloque['rango'] = t
            elif st == ('I', 10.0, '#666666') and campo == 'intro':
                bloque['intro'].append(t)
            elif st[:2] == ('B', 16.0):                            # «1. Cocina Creativa…» (color del bloque)
                cat = {'encabezado': t, 'color': st[2], 'rango': '', 'prompts': []}
                bloque['categorias'].append(cat)
                prompt = None
                campo = None
            elif st == ('I', 9.5, '#666666') and cat is not None and not cat['prompts']:
                cat['rango'] = t
            elif st == ('B', 11.0, '#f5c741'):                     # «#001  Título»
                num = l['spans'][0]['text'].strip()
                titulo = ''.join(s['text'] for s in l['spans'][1:]).strip()
                prompt = {'n': int(num.lstrip('#')), 'titulo': titulo, 'cuerpo': [], 'apps': []}
                cat['prompts'].append(prompt)
                campo = 'body'
            elif st == ('B', 11.0, '#1a1a1a') and campo == 'body' and not prompt['cuerpo']:
                prompt['titulo'] = une([prompt['titulo'], t])      # título partido en dos líneas
            elif st[1] == 9.0 and st[2] == '#666666':              # «App recomendada: …»
                txt = re.sub(r'^Apps? recomendadas?:\s*', '', t)
                prompt['apps'].append(txt)
                campo = 'apps'
            elif st == ('R', 10.0, '#333333') and prompt is not None:
                if campo == 'apps':
                    sys.exit(f'p.{pno + 1}: cuerpo después de la línea de apps en #{prompt["n"]:03d}: {t!r}')
                prompt['cuerpo'].append(t)
            else:
                sys.exit(f'p.{pno + 1}: línea sin clasificar {st} {t!r}')

    total = 0
    for b in doc['bloques']:
        b['intro'] = une(b['intro'])
        for c in b['categorias']:
            for p in c['prompts']:
                p['cuerpo'] = une(p['cuerpo'])
                p['apps'] = [a.strip() for a in re.split(r',\s*', une(p['apps'])) if a.strip()]
                total += 1
    nums = [p['n'] for b in doc['bloques'] for c in b['categorias'] for p in c['prompts']]
    assert nums == list(range(1, 301)), 'numeración rota'
    vacios = [p['n'] for b in doc['bloques'] for c in b['categorias'] for p in c['prompts']
              if not p['cuerpo'] or not p['apps'] or not p['titulo']]
    assert not vacios, f'prompts incompletos: {vacios}'
    (AQUI / 'es.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1))
    palabras = sum(len((p['titulo'] + ' ' + p['cuerpo']).split())
                   for b in doc['bloques'] for c in b['categorias'] for p in c['prompts'])
    print(f'OK · {len(doc["bloques"])} bloques · '
          f'{sum(len(b["categorias"]) for b in doc["bloques"])} categorías · {total} prompts · '
          f'{palabras} palabras en prompts')


if __name__ == '__main__':
    main()
