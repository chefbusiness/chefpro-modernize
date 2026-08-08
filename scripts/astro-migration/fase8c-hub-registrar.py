#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registra en el hub de librerías un agente que ya tiene su post publicado.

POR QUÉ HACE FALTA UN SCRIPT. El catálogo vive DUPLICADO: la fuente declarada
es `fase8c-agentes/catalogo-hub.json`, pero la página que se renderiza
(`astro-site/src/pages/libreria-de-prompts.astro`) lleva su propia copia INLINE
—no importa el JSON—. Tocar sólo una de las dos deja el hub sin el enlace nuevo
o el JSON mintiendo, y ninguna de las dos cosas canta en el build: el hub sigue
compilando y el contador «X de Y con librería» simplemente no sube.

Comprueba además que el post EXISTA antes de enlazarlo, para no publicar en el
hub un enlace a un 404.

Uso:
    python3 scripts/astro-migration/fase8c-hub-registrar.py \
        --agente "Cocina Española" --post libreria-de-prompts-para-cocina-espanola-ai \
        [--apply]
Sin --apply es dry-run.
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
JSON = REPO / 'scripts' / 'astro-migration' / 'fase8c-agentes' / 'catalogo-hub.json'
ASTRO = REPO / 'astro-site' / 'src' / 'pages' / 'libreria-de-prompts.astro'
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--agente', required=True)
    ap.add_argument('--post', required=True)
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    if not (CONTENT / (args.post + '.md')).exists():
        sys.exit('❌ el post no existe todavía: %s.md — no lo enlazo en el hub' % args.post)

    # ── 1) el JSON declarado como fuente ────────────────────────────────────
    cat = json.loads(JSON.read_text(encoding='utf-8'))
    encontrado = False
    for bloque in cat:
        for a in bloque['agentes']:
            if a['nombre'] == args.agente:
                if a.get('post') and a['post'] != args.post:
                    sys.exit('❌ «%s» ya apunta a %s' % (args.agente, a['post']))
                a['post'] = args.post
                encontrado = True
                print('   json  · %-22s → %s' % (bloque['categoria'], args.post))
    if not encontrado:
        sys.exit('❌ «%s» no está en el catálogo. Ojo con el nombre exacto: la '
                 'fuente autorizada es la PLATAFORMA, no el repo.' % args.agente)

    # ── 2) la copia inline del .astro ───────────────────────────────────────
    txt = ASTRO.read_text(encoding='utf-8')
    # Sólo la entrada de ESTE agente, y sólo si sigue en null: el patrón ata
    # el nombre con su "post" inmediato para no pisar al agente de al lado.
    rx = re.compile(r'("nombre":\s*"%s",\s*\n\s*"post":\s*)null'
                    % re.escape(args.agente))
    txt2, n = rx.subn(lambda m: m.group(1) + '"%s"' % args.post, txt)
    if n != 1:
        sys.exit('❌ en el .astro esperaba 1 coincidencia de «%s» con post null, '
                 'encontré %d' % (args.agente, n))
    print('   astro · 1 entrada actualizada')

    con = sum(1 for b in cat for a in b['agentes'] if a.get('post'))
    total = sum(len(b['agentes']) for b in cat)
    print('\n   cobertura del hub: %d de %d agentes' % (con, total))

    if not args.apply:
        print('\n(dry-run: no se ha escrito nada; usa --apply)')
        return

    JSON.write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    ASTRO.write_text(txt2, encoding='utf-8')
    print('\n✅ registrado en las DOS copias del catálogo')


if __name__ == '__main__':
    main()
