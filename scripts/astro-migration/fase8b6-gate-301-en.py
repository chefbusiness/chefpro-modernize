#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B.6 — Batería 301 del cutover de enblog.aichef.pro.

Equivalente a la batería 7/7 que se pasó en el cutover del subdominio ES (8B.5).
Se ejecuta DESPUÉS de apuntar el DNS: comprueba que cada familia de URLs del
WordPress inglés aterriza donde debe en aichef.pro, con 301 (permanente, no 302)
y con el destino en 200.

ANTES del cutover falla a propósito: el subdominio sigue sirviendo el WordPress,
así que verás "sirve el WP" en vez de un 301 a aichef.pro. Eso NO es un bug del
script, es el estado esperado hasta que enblog.aichef.pro sea alias del site en
Netlify. Ver CUTOVER_ENBLOG_PENDIENTE.md.

Uso:
    python3 scripts/astro-migration/fase8b6-gate-301-en.py
Sale con 0 si las 7 comprobaciones pasan, 1 si alguna falla.
"""
import subprocess
import sys

SRC = 'https://enblog.aichef.pro'
DST = 'https://aichef.pro'

# (qué es, path de origen, destino esperado)
CASOS = [
    ('portada',        '/',                                          DST + '/en/blog'),
    ('post migrado',   '/ai-menu-engineering-software',              DST + '/en/blog/ai-menu-engineering-software'),
    ('guía de ciudad', '/ai-recipe-costing-for-chefs-in-sydney',     DST + '/en/blog'),
    ('archive categ.', '/category/ai-in-gastronomy/',                DST + '/en/blog/category/ai-in-gastronomy'),
    ('feed',           '/feed',                                      DST + '/en/blog/rss.xml'),
    ('medios',         '/wp-content/uploads/2026/02/menu-engineering-ipad.jpg',
                       DST + '/blog-assets/en/2026/02/menu-engineering-ipad.jpg'),
    ('catch-all',      '/2026/02/algo/que/no/existe',                DST + '/en/blog'),
]


def curl(url, seguir=False):
    """(código, location) del primer salto; con seguir=True, el código final."""
    cmd = ['curl', '-s', '-o', '/dev/null', '--max-time', '30',
           '-w', '%{http_code} %{redirect_url}']
    if seguir:
        cmd.append('-L')
    r = subprocess.run(cmd + [url], capture_output=True, text=True)
    code, _, loc = r.stdout.strip().partition(' ')
    return code, loc.strip()


def main():
    fallos = []
    for nombre, origen, esperado in CASOS:
        code, loc = curl(SRC + origen)
        if code != '301':
            fallos.append('%-15s %s → %s (se esperaba 301 a %s)'
                          % (nombre, origen, code, esperado))
            continue
        # WordPress se redirige a sí mismo (barra final, canonical): eso es que
        # el DNS todavía no ha cambiado, no un 301 nuestro.
        if loc.startswith(SRC):
            fallos.append('%-15s %s → sigue sirviendo el WP (%s)' % (nombre, origen, loc))
            continue
        if loc.rstrip('/') != esperado.rstrip('/'):
            fallos.append('%-15s %s → %s (se esperaba %s)' % (nombre, origen, loc, esperado))
            continue
        destino, _ = curl(loc, seguir=True)
        if destino != '200':
            fallos.append('%-15s destino %s responde %s' % (nombre, loc, destino))
            continue
        print('  ✅ %-15s %s → %s' % (nombre, origen, loc))

    print('\n%d/%d comprobaciones OK' % (len(CASOS) - len(fallos), len(CASOS)))
    if fallos:
        print('\nFALLOS:')
        for f in fallos:
            print('  ❌ ' + f)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
