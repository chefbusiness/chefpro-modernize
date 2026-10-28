#!/usr/bin/env python3
"""
bp11.py — lanza un script del código común (`../business-plans-en/<script>.py`) con el conjunto «cof»
(BP_CONJUNTO=cof): datos y salidas en ESTA carpeta (`business-plans-en-11/`). Sesión Claude Code, 28-oct-2026 (F1 +
paso 1a de Coffee Cart Business Plan Kit). Clon de `../business-plans-en-7/bp7.py` + subcomandos propios (calibración
D15 y contrato de `-9/`; calculadora = paso 1b, D227).

  Mac (solo JSON):
    python3 bp11.py mapas                         # autotest + cruce con censo_es.json + verificar (abajo)
    python3 bp11.py verificar                     # CELDA_PISTAS / POR_CELDA / DOCX_NOTAS sobre celdas que existen
    python3 bp11.py preparar_tandas               # tandas/*.entrada.json + textos_en/GM.json, GRP-plan.json y GLP-check.json (reutilizadas)
    python3 bp11.py check_textos --tanda GCF-plan # validador de una tanda (o --todas)
    python3 bp11.py check_contrato --preparar|--todas   # tanda del contrato (D230)
    python3 bp11.py calibracion /root/tmp-cof/dry.json  # D15 sobre el informe de aplicar_en --json (D220)
  VPS (openpyxl / python-docx / pycel):
    python3 bp11.py extraer_textos                # censo_es.json + textos_es.json (fuente: FOOD TRUCK ES)
    python3 bp11.py extraer_docx                  # docx_es_cof.json
    python3 bp11.py fuente                        # fuente_es_cof.json (cafetería móvil ES 1.0: checklist, docx por ranura, calculadora, contrato)
    python3 bp11.py aplicar_en --dry-run --parcial --salida /root/tmp-cof/dry --json /root/tmp-cof/dry.json
    python3 bp11.py aplicar_en --idempotencia --json /root/tmp-cof/real.json # real: 2 xlsx en dl/ + cifras_caso.json
    python3 bp11.py ensamblar_docx --plan cof     # docx EN (tras la tanda 2)
    python3 bp11.py gates_en [--dir …] [--parcial --solo G1,G3,…] · gates_en --autotest
    python3 bp11.py calculadora [--autotest]      # coffee-cart-pricing-calculator.xlsx (D227, paso 1b) + autotest pycel
    python3 bp11.py contrato --salida <dir> [--pdf]  # coffee-catering-service-agreement-template.docx (D230)
    python3 bp11.py barrido [--dir …]             # barrido independiente de los 5 entregables → entregables_cof.json
"""
import json
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
SCRIPTS = ('mapas', 'extraer_textos', 'extraer_docx', 'preparar_tandas', 'check_textos', 'aplicar_en', 'gates_en',
           'ensamblar_docx')
PROPIOS = ('verificar', 'calculadora', 'fuente', 'barrido', 'calibracion', 'contrato', 'check_contrato')


def verificar():
    """Las claves por celda de datos_cof (pistas, POR_CELDA) y las notas del docx apuntan a algo que existe; el
    diccionario en cadena (10 de la paella + 8 del catering) no ha derivado (18 sha256 fijados en mapas_cof, D221)."""
    sys.path.insert(0, BASE)
    import mapas as M
    err, avi = [], []
    te_p = os.path.join(AQUI, 'textos_es.json')
    if not os.path.exists(te_p):
        print('verificar: falta textos_es.json (bp11.py extraer_textos en el VPS)')
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
            avi.append('FIJOS sin uso en el café: %r' % k[:60])
    # las 68 tareas × 4 columnas: una cadena por celda, en GCF-check (cambia) o GLP-check (la propuesta de la paella vale)
    zona = [c for c in te['cadenas'] if any(o.get('det') == 'TAREA' for o in c['donde'])]
    if len(zona) != 68 * 4 or any(c['grupo'] not in ('GCF-check', 'GLP-check') for c in zona):
        err.append('zona TAREA: %d cadenas (esperadas 272, en GCF-check o GLP-check)' % len(zona))
    else:
        n_pa = sum(1 for c in zona if c['grupo'] == 'GCF-check')
        print('zona TAREA: 272 celdas = %d GCF-check (a la tanda) + %d GLP-check (propuesta de la paella tal cual)' % (
            n_pa, 272 - n_pa))
    import mapas_cof as MM
    dic = MM.diccionario_ok()
    err += ['diccionario en cadena: %s' % x for x in dic]
    if not dic:
        print('diccionario en cadena: 18 sha256 OK (10 paella + 8 catering)')
    dp = os.path.join(AQUI, 'docx_es_cof.json')
    if os.path.exists(dp):
        de = json.load(open(dp, encoding='utf-8'))['parrafos']
        for i in M.DOCX_NOTAS.get('cof', {}):
            if not de.get(str(i), {}).get('traducir'):
                err.append('DOCX_NOTAS cof[%d]: el párrafo no se traduce' % i)
        sin = [k for k, e in de.items() if e.get('traducir') and int(k) not in M.DOCX_NOTAS.get('cof', {})]
        if sin:
            avi.append('párrafos del docx sin nota de café: %s' % sin)
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('verificar: %s (%d errores, %d avisos)' % ('OK' if not err else 'ROJO', len(err), len(avi)))
    return 1 if err else 0


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPTS + PROPIOS:
        raise SystemExit('uso: bp11.py {%s} [args…]' % '|'.join(SCRIPTS + PROPIOS))
    os.environ['BP_CONJUNTO'] = 'cof'
    nombre = sys.argv[1]
    if nombre == 'verificar':
        sys.exit(verificar())
    if nombre in ('calculadora', 'fuente', 'barrido', 'calibracion', 'contrato', 'check_contrato'):
        ruta = os.path.join(AQUI, {'calculadora': 'calculadora_cof.py', 'fuente': 'fuente_cof.py',
                                   'barrido': 'barrido_cof.py', 'calibracion': 'calibracion_cof.py',
                                   'contrato': 'contrato_cof.py', 'check_contrato': 'check_contrato.py'}[nombre])
        if not os.path.exists(ruta):
            raise SystemExit('%s: aún no existe (%s; ver SPEC-delta D227 / F2-NOTAS)' % (os.path.basename(ruta), nombre))
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
