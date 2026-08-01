#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanza la tanda inglesa de librerías de prompts (Fase 8C).

Sale de la lista de agentes-en.json y de lo que el extractor sea capaz de leer:
los posts de molde WordPress antiguo abortan solos con su razón y quedan para la
segunda tanda, no hay que mantener una lista a mano que se desincronice.

Ejecuta en paralelo porque el cuello de botella es la API (bridge/DeepSeek), no la
CPU: en el VPS no aplica la restricción térmica del Mac. Aun así el paralelismo es
bajo a propósito, para no encadenar rate limits.

Al terminar rehace el interenlazado (--reenlazar): el bloque de "hermanas" se
escribe una sola vez, así que sin esta pasada el primero de la tanda se queda sin
enlaces y el último con todos.

Uso:
    python3 scripts/astro-migration/fase8c-libreria-en-tanda.py --dry-run
    python3 scripts/astro-migration/fase8c-libreria-en-tanda.py --paralelo 3
    python3 scripts/astro-migration/fase8c-libreria-en-tanda.py --slugs a,b,c
"""
import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[1]
EN = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en'
GEN = AQUI / 'fase8c-libreria-en.py'
GATE = AQUI / 'fase8c-libreria-en-gate.py'
MAPA = AQUI / 'fase8c-agentes' / 'agentes-en.json'
LOGS = Path('/tmp/fase8c-tanda-en')


def genera(slug):
    LOGS.mkdir(exist_ok=True)
    log = LOGS / ('%s.log' % slug)
    with log.open('w', encoding='utf-8') as f:
        r = subprocess.run([sys.executable, '-u', str(GEN), '--slug', slug],
                           stdout=f, stderr=subprocess.STDOUT, cwd=str(REPO))
    return slug, r.returncode, log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--paralelo', type=int, default=3)
    ap.add_argument('--slugs', help='lista separada por comas; por defecto, todos los pendientes')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--rehacer', action='store_true', help='incluye los que ya tienen .md')
    args = ap.parse_args()

    mapa = json.loads(MAPA.read_text(encoding='utf-8'))
    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(',') if s.strip()]
        for s in slugs:
            if s not in mapa:
                sys.exit('%s no está en %s' % (s, MAPA.name))
    else:
        slugs = [s for s in sorted(mapa)
                 if args.rehacer or not (EN / (mapa[s]['slug_en'] + '.md')).exists()]

    print('%d agente(s) en cola, %d en paralelo' % (len(slugs), args.paralelo))
    for s in slugs:
        print('   · %-32s → %s' % (s, mapa[s]['slug_en']))
    if args.dry_run:
        return

    hechos, fallidos = [], []
    with ThreadPoolExecutor(max_workers=args.paralelo) as pool:
        for slug, rc, log in pool.map(genera, slugs):
            if rc == 0:
                hechos.append(slug)
                print('✅ %s' % slug, flush=True)
            else:
                fallidos.append(slug)
                cola = log.read_text(encoding='utf-8').strip().splitlines()[-4:]
                print('⛔ %s (rc=%d)\n     %s' % (slug, rc, '\n     '.join(cola)), flush=True)

    print('\n%s\n%d generadas · %d fallidas' % ('─' * 70, len(hechos), len(fallidos)))
    if fallidos:
        print('fallidas: %s' % ', '.join(fallidos))
        print('logs en %s' % LOGS)

    if hechos:
        print('\n↔ rehaciendo el interenlazado…')
        subprocess.run([sys.executable, str(GEN), '--reenlazar'], cwd=str(REPO))
        print('\n🔍 gate:')
        subprocess.run([sys.executable, str(GATE), '--todos'], cwd=str(REPO))


if __name__ == '__main__':
    main()
