#!/usr/bin/env python3
"""
check_revision.py — valida la revisión de las cadenas REUTILIZADAS de una tanda (`textos_en/<G>.revision.json`, G =
GR en la tanda GBUR-plan · GRC en la tanda GBUR-check) SIN tocar ficheros compartidos: fusiona `textos_en/<G>.json` +
la revisión en un temporal propio y pasa `bp15.py check_textos --tanda <G> --fichero <temporal>`. Comprueba además que
la revisión es un JSON {id: EN} que solo trae ids de <G>. Solo JSON (Mac). Sesión Claude Code, 29-oct-2026 (F2-EN,
paso 1a de Burger Restaurant Business Plan Kit): así dos traductores en paralelo validan su revisión sin correr
`preparar_tandas` (que reescribe GM/GR/GRC.json y las entradas de las tandas: lo corre el orquestador al cerrar).

    python3 scripts/productos-digitales/business-plans-en-15/check_revision.py GR      # tanda (a) GBUR-plan
    python3 scripts/productos-digitales/business-plans-en-15/check_revision.py GRC     # tanda (b) GBUR-check
"""
import json
import os
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('GR', 'GRC'):
        raise SystemExit('uso: check_revision.py {GR|GRC}')
    g = sys.argv[1]
    base = json.load(open(os.path.join(AQUI, 'textos_en', g + '.json'), encoding='utf-8'))
    rp = os.path.join(AQUI, 'textos_en', g + '.revision.json')
    if os.path.exists(rp):
        try:
            rev = json.load(open(rp, encoding='utf-8'))
        except json.JSONDecodeError as ex:
            print('ERROR %s.revision.json: JSON inválido: %s' % (g, ex))
            return 1
        if not isinstance(rev, dict) or not all(isinstance(v, str) and v.strip() for v in rev.values()):
            print('ERROR %s.revision.json: tiene que ser {"<id>": "<EN corregido>"} con textos no vacíos' % g)
            return 1
    else:
        rev = {}
        print('AVISO falta textos_en/%s.revision.json: si no corriges ninguna, escribe {} (se valida el EN actual)' % g)
    ajenos = sorted(k for k in rev if k not in base)
    if ajenos:
        print('ERROR %s.revision.json trae ids que no son de %s: %s' % (g, g, ajenos[:10]))
        return 1
    fusion = dict(base)
    fusion.update(rev)
    fd, tmp = tempfile.mkstemp(prefix='bur-%s-' % g, suffix='.json')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as fh:
            json.dump(fusion, fh, ensure_ascii=False, indent=1)
        print('%s: %d reutilizadas · %d corregidas en la revisión' % (g, len(base), len(rev)))
        return subprocess.call([sys.executable, os.path.join(AQUI, 'bp15.py'), 'check_textos', '--tanda', g,
                                '--fichero', tmp])
    finally:
        os.unlink(tmp)


if __name__ == '__main__':
    sys.exit(main())
