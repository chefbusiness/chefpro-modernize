#!/usr/bin/env python3
"""
bp3.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto «bar»
(BP_CONJUNTO=bar): datos y salidas en ESTA carpeta (`business-plans-en-3/`). Sesión Claude Code, 11-oct-2026 (F2,
paso 1 de Bar Business Plan Kit). Copia de `../business-plans-en-2/bp2.py` + dos subcomandos propios.

  Mac (solo JSON):
    python3 bp3.py mapas                          # autotest + cruce con censo_es.json + verificar (abajo)
    python3 bp3.py verificar                      # CELDA_PISTAS / POR_CELDA / DOCX_NOTAS sobre celdas que existen
    python3 bp3.py derivar_formulas               # formulas_bar.json (14 con gemela + 3 manuales)
    python3 bp3.py preparar_tandas                # tandas/*.entrada.json + textos_en/GM.json y GR.json (reutilizadas)
    python3 bp3.py check_textos --tanda GBAR-plan # validador de una tanda (o --todas)
  VPS (openpyxl / python-docx / pycel):
    python3 bp3.py extraer_textos                 # censo_es.json + textos_es.json
    python3 bp3.py extraer_docx                   # docx_es_bar.json
    python3 bp3.py aplicar_en --dry-run --parcial --salida /tmp/bar-dry   # ensayo (lo no traducido queda en ES)
    python3 bp3.py aplicar_en --idempotencia --json /tmp/bar-real.json    # real: 2 xlsx en dl/ + cifras_caso.json
    python3 bp3.py ensamblar_docx --plan bar      # docx EN (tras la tanda 2)
    python3 bp3.py gates_en [--dir …] [--parcial --solo G1,G3,…] · gates_en --autotest
"""
import json
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx')
PROPIOS = ('derivar_formulas', 'verificar')


def verificar():
    """Las claves por celda de datos_bar (pistas, POR_CELDA) y las notas del docx apuntan a algo que existe."""
    sys.path.insert(0, BASE)
    import mapas as M
    err, avi = [], []
    te_p = os.path.join(AQUI, 'textos_es.json')
    if not os.path.exists(te_p):
        print('verificar: falta textos_es.json (bp3.py extraer_textos en el VPS)')
        return 1
    te = json.load(open(te_p, encoding='utf-8'))
    occ = {(d['f'], d['h'], d['c']): c for c in te['cadenas'] for d in c['donde'] if d['t'] == 'celda'}
    for k in M.CELDA_PISTAS:
        if k not in occ:
            avi.append('CELDA_PISTAS %s!%s (%s): la celda no tiene texto en el ES (pista sin efecto)' % (k[1], k[2], k[0]))
        elif occ[k]['grupo'] not in M.GRUPOS_TRADUCTORES:
            avi.append('CELDA_PISTAS %s!%s: la cadena es %s (no va a los traductores): %r' % (
                k[1], k[2], occ[k]['grupo'], occ[k]['es'][:50]))
    for k, v in M.POR_CELDA.items():
        if k not in occ:
            err.append('POR_CELDA %s!%s (%s): la celda no tiene texto en el ES' % (k[1], k[2], k[0]))
    usados = set()
    for c in te['cadenas']:
        if c['tratamiento'] == 'regenerar':
            usados.add(c['es'])
    for k in M.FIJOS:
        if k not in usados and not k.startswith('Mes '):
            avi.append('FIJOS sin uso en el bar: %r' % k[:60])
    dp = os.path.join(AQUI, 'docx_es_bar.json')
    if os.path.exists(dp):
        de = json.load(open(dp, encoding='utf-8'))['parrafos']
        for i in M.DOCX_NOTAS.get('bar', {}):
            if not de.get(str(i), {}).get('traducir'):
                err.append('DOCX_NOTAS bar[%d]: el párrafo no se traduce' % i)
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('verificar: %s (%d errores, %d avisos)' % ('OK' if not err else 'ROJO', len(err), len(avi)))
    return 1 if err else 0


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPTS + PROPIOS:
        raise SystemExit('uso: bp3.py {%s} [args…]' % '|'.join(SCRIPTS + PROPIOS))
    os.environ['BP_CONJUNTO'] = 'bar'
    nombre = sys.argv[1]
    if nombre == 'verificar':
        sys.exit(verificar())
    if nombre == 'derivar_formulas':
        ruta = os.path.join(AQUI, 'derivar_formulas_bar.py')
    else:
        ruta = os.path.join(BASE, nombre + '.py')
    sys.argv = [ruta] + sys.argv[2:]
    sys.path.insert(0, BASE)
    if nombre == 'mapas':
        try:
            runpy.run_path(ruta, run_name='__main__')
        finally:
            verificar()
    else:
        runpy.run_path(ruta, run_name='__main__')
