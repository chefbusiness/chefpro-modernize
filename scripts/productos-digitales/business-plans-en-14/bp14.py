#!/usr/bin/env python3
"""
bp14.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto «sus»
(BP_CONJUNTO=sus): datos y salidas en ESTA carpeta (`business-plans-en-14/`). Sesión Claude Code, 31-oct-2026 (F2-EN
de Sushi Restaurant Business Plan Kit). Clon de `../business-plans-en-13/bp13.py` (Rotisserie EN): subcomando `calculadora`
(`calculadora_sus.py`, la calculadora ES del sushi bar traducida a unidades US) y `verificar` contra los sha256 del ES
final (`mapas_sus.SHA_ES`) y de los diccionarios del Taco EN (`mapas_sus.SHA_TAQ`), del Rotisserie EN (`SHA_POL`) y de
la Pizza EN (`SHA_PIZ`).

FUENTE ES: `astro-site/public/dl/plan-negocio-sushi-bar/` (el ES FINAL y revisado, F2 ES `51060183`; `SUS_FUENTE_ES=/ruta` solo para pruebas).

  Mac (solo JSON):
    python3 bp14.py mapas                          # autotest + cruce con censo_es.json + verificar (abajo)
    python3 bp14.py verificar                      # pistas / POR_CELDA / notas del docx + sha256 (ES, Taco, Rotisserie, Pizza)
    python3 bp14.py derivar_formulas               # formulas_sus.json (gemela TAQ → POL → PIZ → PAN/REST → BAR → FT/CAF + manuales)
    python3 bp14.py preparar_tandas                # tandas/*.entrada.json + textos_en/GM.json, GR.json y GRC.json (reutilizadas)
    python3 bp14.py check_textos --tanda GSUS-plan # validador de una tanda (o --todas)
  VPS (openpyxl / python-docx / pycel):
    python3 bp14.py extraer_textos                 # censo_es.json + textos_es.json
    python3 bp14.py extraer_docx                   # docx_es_sus.json (Word ES final; avisa de A4: el EN sale Letter)
    python3 bp14.py aplicar_en --dry-run --parcial --salida /root/tmp-sus-en/dry --json /root/tmp-sus-en/dry.json
    python3 bp14.py calibracion /root/tmp-sus-en/dry.json    # D15 (holgura, DSCR, saldo, cobertura, neto, umbrales)
    python3 bp14.py aplicar_en --idempotencia --json /tmp/sus-real.json    # real: 2 xlsx en dl/ + cifras_caso.json
    python3 bp14.py ensamblar_docx --plan sus      # docx EN (tras la tanda 2)
    python3 bp14.py calculadora --salida <dir> [--autotest]   # sushi-fish-rice-costing-calculator.xlsx (calculadora_sus.py)
    python3 bp14.py gates_en [--dir …] [--parcial --solo G1,G3,…] · gates_en --autotest
    python3 bp14.py barrido                        # barrido independiente de los 4 entregables → barrido_sus.json
"""
import hashlib
import json
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx')
PROPIOS = ('derivar_formulas', 'verificar', 'calculadora', 'barrido', 'calibracion')
FICHERO_PROPIO = {'derivar_formulas': 'derivar_formulas_sus.py', 'calculadora': 'calculadora_sus.py', 'barrido': 'barrido_sus.py',
                  'calibracion': 'calibracion_sus.py'}


def verificar():
    """Las claves por celda de datos_sus (pistas, POR_CELDA) y las notas del docx apuntan a algo que existe; el
    diccionario del Taco EN, del Rotisserie EN y de la Pizza EN no ha derivado (mapas_sus.SHA_*); la fuente ES es la del censo y la medida en F1."""
    sys.path.insert(0, BASE)
    import mapas as M
    import mapas_sus as MI
    err, avi = [], []
    te_p = os.path.join(AQUI, 'textos_es.json')
    if not os.path.exists(te_p):
        print('verificar: falta textos_es.json (bp14.py extraer_textos en el VPS)')
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
            avi.append('FIJOS sin uso en el sushi bar: %r' % k[:60])
    # D19: 12 filas × 4 columnas (35-46, = la taquería), todas en GSUS-plan y sin propuesta
    d19 = [c for c in te['cadenas'] if any(o.get('det') == 'D19' for o in c['donde'])]
    if any(c['grupo'] != 'GSUS-plan' or 'reuso' in c for c in d19):
        err.append('zona D19: hay celdas fuera de GSUS-plan o con propuesta')
    else:
        print('zona D19: %d cadenas en GSUS-plan, sin propuesta (sin propuesta)' % len(d19))
    dic = MI.diccionario_ok()
    err += ['diccionario (Taco EN / Rotisserie EN / Pizza EN): %s' % x for x in dic]
    if not dic:
        print('diccionarios del Taco EN, del Rotisserie EN y de la Pizza EN: %d sha256 OK' % (
            len(MI.SHA_TAQ) + len(MI.SHA_POL) + len(MI.SHA_PIZ)))
    repo = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
    for f, sha in MI.SHA_ES.items():
        p = os.path.join(repo, MI.FUENTE_ES, f) if not os.path.isabs(MI.FUENTE_ES) else os.path.join(MI.FUENTE_ES, f)
        if not os.path.exists(p):
            avi.append('fuente ES %s: no existe en este equipo (%s)' % (f, p))
        elif hashlib.sha256(open(p, 'rb').read()).hexdigest() != sha:
            err.append('fuente ES %s: sha256 distinto del medido en F1 (manda el ES nuevo: re-medir y avisar)' % f)
    cen_p = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(cen_p):
        for f, info in json.load(open(cen_p, encoding='utf-8'))['libros'].items():
            p = M.ruta_es(info['corto'], repo)
            if not os.path.exists(p):
                avi.append('fuente ES %s: no existe en este equipo (%s)' % (f, p))
            elif hashlib.sha256(open(p, 'rb').read()).hexdigest() != info['sha256']:
                err.append('fuente ES %s: sha256 distinto del censo: re-extrae (bp14.py extraer_textos)' % f)
        print('fuente ES: %s' % MI.FUENTE_ES)
    dp = os.path.join(AQUI, 'docx_es_sus.json')
    if not os.path.exists(dp):
        avi.append('falta docx_es_sus.json (bp14.py extraer_docx en el VPS)')
    else:
        de = json.load(open(dp, encoding='utf-8'))['parrafos']
        for i in M.DOCX_NOTAS.get('sus', {}):
            if not de.get(str(i), {}).get('traducir'):
                err.append('DOCX_NOTAS sus[%d]: el párrafo no se traduce' % i)
        sin = [k for k, e in de.items() if e.get('traducir') and int(k) not in M.DOCX_NOTAS.get('sus', {})]
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
        raise SystemExit('uso: bp14.py {%s} [args…]' % '|'.join(SCRIPTS + PROPIOS))
    os.environ['BP_CONJUNTO'] = 'sus'
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
