#!/usr/bin/env python3
"""
resync_es.py — vuelve a dejar REGENERABLES los conjuntos EN de planes ya publicados cuando se parchea el ES LIVE
(origen: PR #186, 30-oct-2026, notas de holgura + literales troceados + desplegable ✓,☐,N/A en los ES; sin esto los
`aplicar_en --dry-run` abortan con «textos_es.json dice … y el ES trae …»). Sesión Claude Code, 31-oct-2026.

    VPS:  /root/venv-guias/bin/python resync_es.py [--solo business-plans-en-8,business-plans-en-12]

1. Por conjunto, en ORDEN DE CADENA (grupo_de / reuso_de leen los textos_es + textos_en de los hermanos):
   `extraer_textos --fijar-clasificacion <textos_es.json publicado>` en su carpeta → mismos ids y la clasificación
   (grupo, tratamiento) con la que se construyó el EN LIVE; aborta si un id cambia de apariciones.
2. Re-mide los sha256 fijados que apuntan a los diccionarios de los hermanos y a la fuente ES (SHA_* de mapas_*,
   business-plans-en-9/sha_piz.json), para que `bpN.py mapas` / `verificar` vuelvan a verde.
NO toca textos_en/: el EN de las cadenas ES corregidas tiene que estar ya al día (en #186 lo estaba).
Después: la regresión del último conjunto (dry-run de los 13 + docx) y `comparar_sem.py` contra dl/ (el canon de bytes
ya no basta tras un parche XML: el alto de fila y el punto de troceo de un literal difieren sin cambiar nada visible).
Un conjunto nuevo (p. ej. business-plans-en-14) se añade a CONJUNTOS y, si fija sha de hermanos, a BLOQUES.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
P = os.path.dirname(AQUI)
REPO = os.path.abspath(os.path.join(P, '..', '..'))
DL = os.path.join(REPO, 'astro-site', 'public', 'dl')

CONJUNTOS = [('business-plans-en', 'extraer_textos.py')] + [
    ('business-plans-en-%d' % n, 'bp%d.py' % n) for n in range(2, 14)]

# (fichero mapas, variable OrderedDict de sha, carpeta de las claves)
BLOQUES = [
    ('business-plans-en-5/mapas_mbar.py', 'SHA_DICCIONARIO', os.path.join(P, 'business-plans-en-4')),
    ('business-plans-en-6/mapas_bbq.py', 'SHA_DICCIONARIO', os.path.join(P, 'business-plans-en-4')),
    ('business-plans-en-7/mapas_pael.py', 'SHA_BBQ', os.path.join(P, 'business-plans-en-6')),
    ('business-plans-en-7/mapas_pael.py', 'SHA_DICCIONARIO', os.path.join(P, 'business-plans-en-4')),
    ('business-plans-en-8/mapas_piz.py', 'SHA_BAR', os.path.join(P, 'business-plans-en-3')),
    ('business-plans-en-10/mapas_ice.py', 'SHA_PIZ', os.path.join(P, 'business-plans-en-8')),
    ('business-plans-en-10/mapas_ice.py', 'SHA_ES', os.path.join(DL, 'plan-negocio-heladeria')),
    ('business-plans-en-11/mapas_cof.py', 'SHA_PAEL', os.path.join(P, 'business-plans-en-7')),
    ('business-plans-en-11/mapas_cof.py', 'SHA_DICCIONARIO', os.path.join(P, 'business-plans-en-4')),
    ('business-plans-en-12/mapas_taq.py', 'SHA_PIZ', os.path.join(P, 'business-plans-en-8')),
    ('business-plans-en-12/mapas_taq.py', 'SHA_ES', os.path.join(DL, 'plan-negocio-taqueria')),
    ('business-plans-en-13/mapas_pol.py', 'SHA_TAQ', os.path.join(P, 'business-plans-en-12')),
    ('business-plans-en-13/mapas_pol.py', 'SHA_PIZ', os.path.join(P, 'business-plans-en-8')),
    ('business-plans-en-13/mapas_pol.py', 'SHA_ES', os.path.join(DL, 'plan-negocio-polleria')),
]
SHA_JSON = [('business-plans-en-9/sha_piz.json', os.path.join(P, 'business-plans-en-8'))]
RX_PAR = re.compile(r"\('([^']+)', '([0-9a-f]{64})'\)")


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def reextraer(solo):
    env = {k: v for k, v in os.environ.items() if not k.endswith('_FUENTE_ES')}   # la fuente ES = el LIVE de dl/
    tmp = tempfile.mkdtemp(prefix='resync-es-')
    try:
        for carpeta, lanzador in CONJUNTOS:
            if solo and carpeta not in solo:
                continue
            d = os.path.join(P, carpeta)
            pub = os.path.join(tmp, carpeta + '.textos_es.json')
            shutil.copyfile(os.path.join(d, 'textos_es.json'), pub)
            cmd = [sys.executable, lanzador] + ([] if lanzador == 'extraer_textos.py' else ['extraer_textos'])
            r = subprocess.run(cmd + ['--fijar-clasificacion', pub], cwd=d, env=env, capture_output=True, text=True)
            lineas = [x for x in r.stdout.splitlines() if 'clasificación publicada' in x or x.startswith('--fijar')]
            print('%-20s rc=%d · %s' % (carpeta, r.returncode, ' | '.join(x.strip() for x in lineas)))
            if r.returncode:
                sys.exit(r.stderr[-2000:] + r.stdout[-1000:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def remedir():
    n = 0
    for rel, var, base in BLOQUES:
        p = os.path.join(P, rel)
        src = open(p, encoding='utf-8').read()
        m = re.search(r'^%s = OrderedDict\(\[\n(.*?)^\]\)' % var, src, re.S | re.M)
        if not m:
            sys.exit('sin bloque %s en %s' % (var, rel))
        bloque = nuevo = m.group(1)
        for k, viejo in RX_PAR.findall(bloque):
            actual = sha(os.path.join(base, k))
            if actual != viejo:
                print('  sha %s %s %s: %s → %s' % (rel, var, k, viejo[:12], actual[:12]))
                nuevo = nuevo.replace("('%s', '%s')" % (k, viejo), "('%s', '%s')" % (k, actual))
                n += 1
        if nuevo != bloque:
            open(p, 'w', encoding='utf-8').write(src[:m.start(1)] + nuevo + src[m.end(1):])
    for rel, base in SHA_JSON:
        p = os.path.join(P, rel)
        raw = open(p, encoding='utf-8').read()
        for k, viejo in json.loads(raw).items():
            actual = sha(os.path.join(base, k))
            if actual != viejo:
                print('  sha %s %s: %s → %s' % (rel, k, viejo[:12], actual[:12]))
                raw = raw.replace('"%s": "%s"' % (k, viejo), '"%s": "%s"' % (k, actual))
                n += 1
        open(p, 'w', encoding='utf-8').write(raw)
    print('sha fijados re-medidos: %d' % n)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--solo', default='', help='carpetas separadas por comas (por defecto, los 13 conjuntos)')
    args = ap.parse_args()
    reextraer({x for x in args.solo.split(',') if x})
    remedir()


if __name__ == '__main__':
    main()
