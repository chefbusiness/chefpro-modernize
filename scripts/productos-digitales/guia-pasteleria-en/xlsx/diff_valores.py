#!/usr/bin/env python3
"""Qué cifras cambian entre los xlsx ES publicados y los EN recalculados (SPEC D7, D8, D12, D13).

Compara celda a celda los valores cacheados (data_only) de cada libro ES con su gemelo EN (mismo libro tras
`aplicar_en.py` + `inject_cache.py`), con las pestañas casadas por `config_en.LIBROS[libro]['hojas']`. Escribe:
  - cifras_cambiadas.json: [{libro, hoja, celda, fila, columna, es, en}] (diferencia relativa > 1e-9);
  - CIFRAS-RECALCULADAS.md: por tanda ES, cada cifra del texto que coincide con un valor ES que ha cambiado,
    con su valor EN en formato US y la celda de origen. Es el mapa §3-bis de DECISIONES-TANDAS.md.

    python3 diff_valores.py <dir_es> <dir_en>        # en el VPS, tras inject_cache.py
"""
import json
import os
import re
import sys
from pathlib import Path

import openpyxl

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import config_en as C  # noqa: E402

TANDAS_ES = AQUI.parent / 'tandas' / 'es'


def etiqueta(ws, celda):
    """Primera celda de texto de la fila (a la izquierda) y la cabecera más cercana por encima."""
    fila = col = ''
    for c in ws[celda.row]:
        if c.column >= celda.column:
            break
        if isinstance(c.value, str) and c.value.strip():
            fila = c.value.strip()
    for r in range(celda.row - 1, 0, -1):
        v = ws.cell(r, celda.column).value
        if isinstance(v, str) and v.strip():
            col = v.strip()
            break
    return fila[:70], col[:50]


def comparar(dir_es, dir_en):
    cambios = []
    for libro, cfg in C.LIBROS.items():
        es = openpyxl.load_workbook(os.path.join(dir_es, libro), data_only=True)
        es_f = openpyxl.load_workbook(os.path.join(dir_es, libro))
        en = openpyxl.load_workbook(os.path.join(dir_en, cfg['out']), data_only=True)
        for hoja_es, hoja_en in cfg['hojas'].items():
            a, b, f = es[hoja_es], en[hoja_en], es_f[hoja_es]
            for fila in a.iter_rows():
                for c in fila:
                    v1 = c.value
                    if not isinstance(v1, (int, float)) or isinstance(v1, bool):
                        continue
                    v2 = b[c.coordinate].value
                    if not isinstance(v2, (int, float)) or isinstance(v2, bool):
                        if v2 is None or isinstance(v2, str):
                            cambios.append({'libro': libro, 'hoja': hoja_es, 'celda': c.coordinate,
                                            'fila': etiqueta(a, c)[0], 'columna': etiqueta(a, c)[1],
                                            'es': v1, 'en': v2, 'formula': isinstance(f[c.coordinate].value, str)
                                            and f[c.coordinate].value.startswith('=')})
                        continue
                    if abs(v1 - v2) <= 1e-9 * max(1.0, abs(v1)):
                        continue
                    fl, co = etiqueta(a, c)
                    cambios.append({'libro': libro, 'hoja': hoja_es, 'celda': c.coordinate, 'fila': fl,
                                    'columna': co, 'es': v1, 'en': v2,
                                    'formula': isinstance(f[c.coordinate].value, str)
                                    and f[c.coordinate].value.startswith('=')})
    return cambios


def formatos_es(v):
    """Cómo puede aparecer v en el texto ES (0, 1 y 2 decimales; miles con punto, decimal con coma)."""
    out = {}
    for d in (0, 1, 2):
        s = f'{v:,.{d}f}'.replace(',', '§').replace('.', ',').replace('§', '.')
        if d == 0 and abs(v - round(v)) > 0.005:
            continue
        out[s] = d
        if abs(v) >= 1000 and d == 0:
            out[s.replace('.', '')] = d          # «1780» sin separador
    return out


def formato_en(v, d):
    return f'{v:,.{d}f}' if isinstance(v, (int, float)) else str(v)


def localizar(cambios):
    textos = {p.stem: p.read_text(encoding='utf-8') for p in sorted(TANDAS_ES.glob('*.md'))}
    filas = []
    vistos = set()
    for ch in cambios:
        if not isinstance(ch['es'], (int, float)) or abs(ch['es']) < 1:
            continue                                   # tipos (0,10…) y fracciones: las cubre la regla de D7
        for s, d in formatos_es(ch['es']).items():
            rx = re.compile(r'(?<![\d.,])' + re.escape(s) + r'(?![\d]|,\d)')
            for tanda, txt in textos.items():
                for m in rx.finditer(txt):
                    clave = (tanda, s, ch['libro'], ch['hoja'], ch['celda'])
                    if clave in vistos:
                        continue
                    vistos.add(clave)
                    ctx = txt[max(0, m.start() - 50):m.end() + 30].replace('\n', ' ').replace('|', '/')
                    filas.append((tanda, s, formato_en(ch['en'], d) if ch['en'] is not None else '—',
                                  '%s!%s' % (ch['hoja'], ch['celda']), ch['fila'], ctx))
    return filas


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    cambios = comparar(sys.argv[1], sys.argv[2])
    (AQUI / 'cifras_cambiadas.json').write_text(json.dumps(cambios, ensure_ascii=False, indent=1), encoding='utf-8')
    filas = localizar(cambios)
    por_libro = {}
    for ch in cambios:
        por_libro[ch['libro']] = por_libro.get(ch['libro'], 0) + 1
    lineas = ['# Cifras recalculadas ES → EN (mapa §3-bis de DECISIONES-TANDAS.md)', '',
              'Generado por `xlsx/diff_valores.py`. Celdas que cambian por libro: ' +
              ' · '.join('%s %d' % (k, v) for k, v in por_libro.items()), '',
              'Cada fila: una cifra del texto ES que coincide con un valor del Excel que cambia en EN. **Ojo**: '
              'que coincida el número no prueba que el texto hable de esa celda; mira el contexto y la etiqueta.', '',
              '| Tanda | ES (texto) | EN | Celda ES | Etiqueta de fila | Contexto ES |', '|---|---|---|---|---|---|']
    for t, s, e, cel, fl, ctx in sorted(filas):
        lineas.append('| %s | %s | %s | %s | %s | …%s… |' % (t, s, e, cel, fl.replace('|', '/'), ctx))
    (AQUI / 'CIFRAS-RECALCULADAS.md').write_text('\n'.join(lineas) + '\n', encoding='utf-8')
    print('%d celdas cambian (%s); %d coincidencias en el texto ES → CIFRAS-RECALCULADAS.md'
          % (len(cambios), ', '.join('%s %d' % kv for kv in por_libro.items()), len(filas)))


if __name__ == '__main__':
    main()
