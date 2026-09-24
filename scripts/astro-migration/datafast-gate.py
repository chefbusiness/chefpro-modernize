#!/usr/bin/env python3
"""Gate de DataFast (20-sep-2026): el cargador está exactamente UNA vez en cada
página servida, con el website-id y el dominio correctos, y las dos variantes
del script (cookies / cookieless) siguen descargándose desde datafa.st.

Uso:  python3 scripts/astro-migration/datafast-gate.py [--base https://aichef.pro]
Contra un deploy preview:  --base https://deploy-preview-N--aichefpro.netlify.app
(el cargador se emite igual en el preview; en runtime se autodesactiva fuera de
aichef.pro, así que el panel no se ensucia).
"""
import argparse, re, sys, urllib.request

WEBSITE_ID = 'dfid_QU6VBDPW3GqyxYmZoQvw0'
DOMAIN = 'aichef.pro'
# Muestra transversal: 7 portadas, precios, blog ES/EN, hub y landing de producto,
# integraciones, legal, contacto y zona app (gate de acceso).
# Tienda EN (25-sep-2026): hub, landing, gate de acceso ANIDADO y vuelta de cripto. El gate
# de acceso es donde DataFast lee `?session_id=` para atribuir el Payment Link. Contra
# producción, las tres rutas de food-cost-templates dan 404 hasta el merge: correr con
# --base <deploy preview> antes.
PAGINAS = ['/', '/en', '/fr', '/de', '/it', '/pt', '/nl', '/precios', '/en/pricing',
           '/blog', '/en/blog', '/productos-digitales', '/kit-escandallos', '/integraciones',
           '/contacto', '/privacidad', '/kit-escandallos-access',
           '/en/digital-products', '/en/digital-products/food-cost-templates',
           '/en/digital-products/food-cost-templates/access', '/en/crypto-payment']
SCRIPTS = ['https://datafa.st/js/script.js', 'https://datafa.st/js/script.cookieless.js']

def get(url, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent': 'datafast-gate/1.0'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers.get('content-type', ''), r.read().decode('utf-8', 'replace')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--base', default='https://aichef.pro')
    base = ap.parse_args().base.rstrip('/')
    errores = []
    for path in PAGINAS:
        url = base + path
        try:
            st, ct, html = get(url)
        except Exception as e:
            errores.append(f'{path}: no se pudo leer ({e})'); continue
        n_id = html.count(WEBSITE_ID)
        n_dom = len(re.findall(r"DOMAIN\s*=\s*['\"]" + re.escape(DOMAIN) + r"['\"]", html))
        n_src = html.count("'https://datafa.st/js/'")
        plano = len(re.findall(r'<script[^>]*data-website-id=', html))  # snippet plano duplicado
        if n_id != 1 or n_dom != 1 or n_src != 1 or plano != 0:
            errores.append(f'{path}: id×{n_id} dominio×{n_dom} src×{n_src} snippet-plano×{plano} (esperado 1/1/1/0)')
    for s in SCRIPTS:
        try:
            st, ct, js = get(s)
            if 'javascript' not in ct or 'currentScript' not in js:
                errores.append(f'{s}: {ct} sin currentScript')
        except Exception as e:
            errores.append(f'{s}: no se descarga ({e})')
    if errores:
        print('✗ GATE DataFast: FALLA'); [print('  ·', e) for e in errores]; sys.exit(1)
    print(f'✓ GATE DataFast: {len(PAGINAS)}/{len(PAGINAS)} páginas con el cargador exactamente una vez '
          f'({WEBSITE_ID}, {DOMAIN}) y {len(SCRIPTS)}/{len(SCRIPTS)} scripts descargables desde datafa.st')

if __name__ == '__main__':
    main()
