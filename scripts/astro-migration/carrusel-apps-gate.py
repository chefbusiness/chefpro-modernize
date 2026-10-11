#!/usr/bin/env python3
"""
carrusel-apps-gate.py — Toda landing de producto pinta el carrusel «Imprime, Delega y Controla» con los 9 logos.

John (11-oct-2026): «tienen que salir todos los logos». Las 5 landings de business plans EN enseñaban solo Excel y
Word (una revisión recortó el carrusel por idioma) y 11 landings ES no lo tenían. Ningún build ni gate lo veía.

    python3 scripts/astro-migration/carrusel-apps-gate.py                      # producción
    python3 scripts/astro-migration/carrusel-apps-gate.py --base https://deploy-preview-N--aichefpro.netlify.app

Landings = los `landingPath` de astro-site/src/lib/zona-app.ts. Exit 1 si a alguna le falta algún logo.
"""
import argparse, concurrent.futures as cf, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGOS = {'aichefpro-icon', 'openai', 'gemini', 'google-sheets', 'excel', 'word', 'pdf', 'google', 'perplexity'}


def landings():
    t = open(os.path.join(ROOT, 'astro-site/src/lib/zona-app.ts'), encoding='utf-8').read()
    return re.findall(r"landingPath:\s*'([^']+)'", t)


def logos(base, path):
    req = urllib.request.Request(base + path, headers={'User-Agent': 'carrusel-apps-gate'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    return set(re.findall(r'src="/logos/([a-z0-9-]+)\.png"', html))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='https://aichef.pro')
    base = ap.parse_args().base.rstrip('/')
    paths = landings()
    with cf.ThreadPoolExecutor(6) as ex:
        res = dict(zip(paths, ex.map(lambda p: logos(base, p), paths)))
    malas = {p: sorted(LOGOS - v) for p, v in res.items() if LOGOS - v}
    for p, falta in malas.items():
        print(f'❌ {p}: faltan {", ".join(falta)}')
    print(f'{len(paths)} landings · {len(malas)} sin el carrusel completo')
    sys.exit(1 if malas else 0)


if __name__ == '__main__':
    main()
