#!/usr/bin/env python3
"""
bp9.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto «wed»
(BP_CONJUNTO=wed): datos y salidas en ESTA carpeta (`business-plans-en-9/`). Sesión Claude Code, 27-oct-2026 (F2-EN,
paso 1a de Wedding Venue Business Plan Kit). Copia de `../business-plans-en-8/bp8.py` + `check_contrato` (tanda del
contrato, D171) y `fijar_sha` (sha256 del diccionario de la Pizza EN).

FUENTE ES: `WED_FUENTE_ES=/ruta/a/plan-negocio-finca-eventos-bodas` o nada (ES LIVE en
`astro-site/public/dl/plan-negocio-finca-eventos-bodas/`). Ver `mapas_wed.FUENTE_ES`.

  Mac (solo JSON):
    python3 bp9.py mapas                          # autotest + cruce con censo_es.json + verificar (abajo)
    python3 bp9.py verificar [--fijar]            # pistas / POR_CELDA / notas del docx + sha256 del diccionario de la pizza
    python3 bp9.py derivar_formulas               # formulas_wed.json (gemela Pizza EN → FT/CAF → REST/PAN + manuales)
    python3 bp9.py preparar_tandas                # tandas/*.entrada.json + textos_en/GM.json y GR.json (reutilizadas)
    python3 bp9.py check_textos --tanda GWED-plan # validador de una tanda (o --todas)
    python3 bp9.py check_contrato --parte 1       # validador de una mitad del contrato (textos_en/contrato_en_<n>.json)
  VPS (openpyxl / python-docx / pycel):
    python3 bp9.py extraer_textos                 # censo_es.json + textos_es.json
    python3 bp9.py extraer_docx                   # docx_es_wed.json (Word ES de la finca)
    python3 bp9.py aplicar_en --dry-run --parcial --salida /tmp/wed-dry --json /tmp/wed-dry.json
    python3 bp9.py calibracion /tmp/wed-dry.json  # D15 de D160 (holgura, DSCR ≥ 1.30, saldo, cobertura, neto A3, fondos)
    python3 bp9.py aplicar_en --idempotencia --json /tmp/wed-real.json    # real: 2 xlsx en dl/ + cifras_caso.json
    python3 bp9.py ensamblar_docx --plan wed      # docx EN (tras la tanda 2)
    python3 bp9.py gates_en [--dir …] [--parcial --solo G1,G3,…] · gates_en --autotest
    python3 bp9.py barrido [--dir … --parcial]    # barrido independiente de los entregables → entregables_wed.json
"""
import json
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx')
PROPIOS = ('derivar_formulas', 'verificar', 'barrido', 'calibracion', 'check_contrato', 'calculadora', 'contrato')
FICHERO_PROPIO = {'derivar_formulas': 'derivar_formulas_wed.py', 'barrido': 'barrido_wed.py',
                  'calibracion': 'calibracion_wed.py', 'check_contrato': 'check_contrato.py',
                  'calculadora': 'calculadora_wed.py', 'contrato': 'contrato_wed.py'}


def verificar():
    """Las claves por celda de datos_wed (pistas, POR_CELDA) y las notas del docx apuntan a algo que existe; el
    diccionario de la Pizza EN no ha derivado (mapas_wed.SHA_PIZ, en sha_piz.json); la fuente ES es la del censo."""
    sys.path.insert(0, BASE)
    import mapas as M
    import mapas_wed as MW
    if '--fijar' in sys.argv:
        print('sha_piz.json fijado: %d ficheros' % len(MW.fijar_sha()))
        MW.SHA_PIZ.update(json.load(open(os.path.join(AQUI, 'sha_piz.json'), encoding='utf-8')))
    err, avi = [], []
    te_p = os.path.join(AQUI, 'textos_es.json')
    if not os.path.exists(te_p):
        print('verificar: falta textos_es.json (bp9.py extraer_textos en el VPS)')
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
            avi.append('FIJOS sin uso en la finca: %r' % k[:60])
    # D19: 14 filas × 4 columnas, todas en GWED-plan y sin propuesta
    d19 = [c for c in te['cadenas'] if any(o.get('det') == 'D19' for o in c['donde'])]
    if any(c['grupo'] != 'GWED-plan' or 'reuso' in c for c in d19):
        err.append('zona D19: hay celdas fuera de GWED-plan o con propuesta')
    else:
        print('zona D19: %d cadenas en GWED-plan, sin propuesta (D165)' % len(d19))
    dic = MW.diccionario_ok()
    err += ['diccionario de la Pizza EN: %s' % x for x in dic]
    if not dic:
        print('diccionario de la Pizza EN: %d sha256 OK' % len(MW.SHA_PIZ))
    cen_p = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(cen_p):
        import hashlib
        repo = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
        for f, info in json.load(open(cen_p, encoding='utf-8'))['libros'].items():
            p = M.ruta_es(info['corto'], repo)
            if not os.path.exists(p):
                avi.append('fuente ES %s: no existe en este equipo (%s)' % (f, p))
            elif hashlib.sha256(open(p, 'rb').read()).hexdigest() != info['sha256']:
                err.append('fuente ES %s: sha256 distinto del censo: re-extrae (bp9.py extraer_textos)' % f)
        print('fuente ES: %s' % MW.FUENTE_ES)
    dp = os.path.join(AQUI, 'docx_es_wed.json')
    if os.path.exists(dp):
        de = json.load(open(dp, encoding='utf-8'))['parrafos']
        for i in M.DOCX_NOTAS.get('wed', {}):
            if not de.get(str(i), {}).get('traducir'):
                err.append('DOCX_NOTAS wed[%d]: el párrafo no se traduce' % i)
        sin = [k for k, e in de.items() if e.get('traducir') and int(k) not in M.DOCX_NOTAS.get('wed', {})]
        if sin:
            avi.append('párrafos del docx sin nota: %s' % sin)
    else:
        avi.append('falta docx_es_wed.json (bp9.py extraer_docx en el VPS)')
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('verificar: %s (%d errores, %d avisos)' % ('OK' if not err else 'ROJO', len(err), len(avi)))
    return 1 if err else 0


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPTS + PROPIOS:
        raise SystemExit('uso: bp9.py {%s} [args…]' % '|'.join(SCRIPTS + PROPIOS))
    os.environ['BP_CONJUNTO'] = 'wed'
    nombre = sys.argv[1]
    if nombre == 'verificar':
        sys.exit(verificar())
    ruta = os.path.join(AQUI, FICHERO_PROPIO[nombre]) if nombre in FICHERO_PROPIO else os.path.join(BASE, nombre + '.py')
    sys.argv = [ruta] + sys.argv[2:]
    sys.path.insert(0, BASE)
    sys.path.insert(0, AQUI)
    if nombre == 'mapas':
        try:
            runpy.run_path(ruta, run_name='__main__')
        finally:
            verificar()
    else:
        runpy.run_path(ruta, run_name='__main__')
