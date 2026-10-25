#!/usr/bin/env python3
"""
bp8.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto «piz»
(BP_CONJUNTO=piz): datos y salidas en ESTA carpeta (`business-plans-en-8/`). Sesión Claude Code, 25-oct-2026 (F2-EN,
paso 1a de Pizza Shop Business Plan Kit). Copia de `../business-plans-en-3/bp3.py` + los subcomandos `calculadora` y
`barrido` de `../business-plans-en-7/bp7.py` + `calibracion` (D15 de D137).

FUENTE ES: `PIZ_FUENTE_ES=/ruta/a/plan-negocio-pizzeria` (dry-run, paso 1a) o nada (ES FINAL en
`astro-site/public/dl/plan-negocio-pizzeria/`, paso 1c). Ver `mapas_piz.FUENTE_ES` y F2-NOTAS §6.

  Mac (solo JSON):
    python3 bp8.py mapas                          # autotest + cruce con censo_es.json + verificar (abajo)
    python3 bp8.py verificar                      # pistas / POR_CELDA / notas del docx + sha256 del diccionario del Bar
    python3 bp8.py derivar_formulas               # formulas_piz.json (gemela Bar → FT/CAF → REST/PAN + manuales)
    python3 bp8.py preparar_tandas                # tandas/*.entrada.json + textos_en/GM.json y GR.json (reutilizadas)
    python3 bp8.py check_textos --tanda GPIZ-plan # validador de una tanda (o --todas)
  VPS (openpyxl / python-docx / pycel):
    python3 bp8.py extraer_textos                 # censo_es.json + textos_es.json
    python3 bp8.py extraer_docx                   # docx_es_piz.json (cuando exista el Word ES)
    python3 bp8.py aplicar_en --dry-run --parcial --salida /root/tmp-pizen/dry --json /root/tmp-pizen/dry.json
    python3 bp8.py calibracion /root/tmp-pizen/dry.json   # D15 de D137 (holgura, DSCR, saldo, cobertura, neto, D142)
    python3 bp8.py aplicar_en --idempotencia --json /tmp/piz-real.json    # real: 2 xlsx en dl/ + cifras_caso.json
    python3 bp8.py ensamblar_docx --plan piz      # docx EN (tras la tanda 2)
    python3 bp8.py gates_en [--dir …] [--parcial --solo G1,G3,…] · gates_en --autotest
    python3 bp8.py calculadora [--autotest]       # pizza-dough-food-cost-calculator.xlsx (D145, otro agente)
    python3 bp8.py barrido                        # barrido independiente de los 4 entregables → entregables_piz.json
"""
import json
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx')
PROPIOS = ('derivar_formulas', 'verificar', 'calculadora', 'barrido', 'calibracion')
FICHERO_PROPIO = {'derivar_formulas': 'derivar_formulas_piz.py', 'calculadora': 'calculadora_piz.py',
                  'barrido': 'barrido_piz.py', 'calibracion': 'calibracion_piz.py'}


def verificar():
    """Las claves por celda de datos_piz (pistas, POR_CELDA) y las notas del docx apuntan a algo que existe; el
    diccionario del Bar EN no ha derivado (mapas_piz.SHA_BAR); la fuente ES es la del censo."""
    sys.path.insert(0, BASE)
    import mapas as M
    import mapas_piz as MP
    err, avi = [], []
    te_p = os.path.join(AQUI, 'textos_es.json')
    if not os.path.exists(te_p):
        print('verificar: falta textos_es.json (bp8.py extraer_textos en el VPS)')
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
    usados = {c['es'] for c in te['cadenas'] if c['tratamiento'] == 'regenerar'}
    for k in M.FIJOS:
        if k not in usados and not k.startswith('Mes '):
            avi.append('FIJOS sin uso en la pizzería: %r' % k[:60])
    # D19: 13 filas × 4 columnas, todas en GPIZ-plan y sin propuesta
    d19 = [c for c in te['cadenas'] if any(o.get('det') == 'D19' for o in c['donde'])]
    if any(c['grupo'] != 'GPIZ-plan' or 'reuso' in c for c in d19):
        err.append('zona D19: hay celdas fuera de GPIZ-plan o con propuesta')
    else:
        print('zona D19: %d cadenas en GPIZ-plan, sin propuesta (D142)' % len(d19))
    dic = MP.diccionario_ok()
    err += ['diccionario del Bar EN: %s' % x for x in dic]
    if not dic:
        print('diccionario del Bar EN: %d sha256 OK' % len(MP.SHA_BAR))
    cen_p = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(cen_p):
        import hashlib
        repo = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
        for f, info in json.load(open(cen_p, encoding='utf-8'))['libros'].items():
            p = M.ruta_es(info['corto'], repo)
            if not os.path.exists(p):
                avi.append('fuente ES %s: no existe en este equipo (%s)' % (f, p))
            elif hashlib.sha256(open(p, 'rb').read()).hexdigest() != info['sha256']:
                err.append('fuente ES %s: sha256 distinto del censo: re-extrae (bp8.py extraer_textos)' % f)
        print('fuente ES: %s' % MP.FUENTE_ES)
    dp = os.path.join(AQUI, 'docx_es_piz.json')
    if os.path.exists(dp):
        dj = json.load(open(dp, encoding='utf-8'))
        if dj.get('meta', {}).get('pendiente'):
            avi.append('docx_es_piz.json es el marcador «pendiente»: falta el Word ES (paso 1c: bp8.py extraer_docx)')
        else:
            de = dj['parrafos']
            for i in M.DOCX_NOTAS.get('piz', {}):
                if not de.get(str(i), {}).get('traducir'):
                    err.append('DOCX_NOTAS piz[%d]: el párrafo no se traduce' % i)
            sin = [k for k, e in de.items() if e.get('traducir') and int(k) not in M.DOCX_NOTAS.get('piz', {})]
            if sin:
                avi.append('párrafos del docx sin nota: %s' % sin)
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('verificar: %s (%d errores, %d avisos)' % ('OK' if not err else 'ROJO', len(err), len(avi)))
    return 1 if err else 0


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPTS + PROPIOS:
        raise SystemExit('uso: bp8.py {%s} [args…]' % '|'.join(SCRIPTS + PROPIOS))
    os.environ['BP_CONJUNTO'] = 'piz'
    nombre = sys.argv[1]
    if nombre == 'verificar':
        sys.exit(verificar())
    ruta = os.path.join(AQUI, FICHERO_PROPIO[nombre]) if nombre in FICHERO_PROPIO else os.path.join(BASE, nombre + '.py')
    sys.argv = [ruta] + sys.argv[2:]
    sys.path.insert(0, BASE)
    if nombre == 'mapas':
        try:
            runpy.run_path(ruta, run_name='__main__')
        finally:
            verificar()
    else:
        runpy.run_path(ruta, run_name='__main__')
