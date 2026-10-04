#!/usr/bin/env python3
"""
bp2.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto restaurante +
panadería (BP_CONJUNTO=restpan): datos y salidas en ESTA carpeta (`business-plans-en-2/`). Sesión Claude Code,
4-oct-2026 (F2 tanda 1 de Restaurant + Bakery Business Plan Kit).

    python3 bp2.py mapas                         # autotest + cruce con censo_es.json (Mac o VPS)
    python3 bp2.py extraer_textos                # censo_es.json + textos_es.json (VPS: openpyxl)
    python3 bp2.py extraer_docx                  # docx_es_rest.json + docx_es_pan.json (VPS: python-docx)
    python3 bp2.py preparar_tandas               # tandas/*.entrada.json + textos_en/GM.json reutilizado (Mac)
    python3 bp2.py check_textos --todas          # validador de las tandas (Mac)
    python3 bp2.py aplicar_en --dry-run …        # (tanda siguiente) xlsx EN
    python3 bp2.py gates_en [--autotest] …       # (tanda siguiente) G1-G9
    python3 bp2.py ensamblar_docx --plan rest    # (tanda siguiente) docx EN

Sin argumentos de conjunto en los scripts: el mismo código sirve a food truck + cafetería (por defecto, en
`../business-plans-en/`) y a restaurante + panadería (con este lanzador).
"""
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx', 'comparar_publicados')

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPTS:
        raise SystemExit('uso: bp2.py {%s} [args…]' % '|'.join(SCRIPTS))
    os.environ['BP_CONJUNTO'] = 'restpan'
    nombre = sys.argv[1]
    ruta = os.path.join(AQUI if nombre == 'comparar_publicados' else BASE, nombre + '.py')
    sys.argv = [ruta] + sys.argv[2:]
    sys.path.insert(0, BASE)
    runpy.run_path(ruta, run_name='__main__')
