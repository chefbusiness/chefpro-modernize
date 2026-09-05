#!/usr/bin/env python3
"""
Gate transversal del flujo post-pago de los productos digitales de aichef.pro.

Cruza las 5 fuentes de verdad del flujo (que NO comparten código entre sí) y
verifica el estado LIVE de cada eslabón:

  1. astro-site/src/lib/zona-app.ts        → productId, accessPath, libraryPath, landingPath
  2. netlify/functions/verify-purchase.ts   → PRODUCTS (JWT + email de acceso)
  3. netlify/functions/resend-access.ts     → PRODUCTS (reenvío "¿ya compraste?")
  4. netlify/functions/get-download-urls.ts → PRODUCT_FILES (clave → /dl/…)
  5. src/pages/*Dashboard.tsx               → TEMPLATES[].key (tarjetas del dashboard)
  + astro-site/public/dl/ (disco) + git ls-files (trackeado) + HTTP LIVE.

Checks:
  A. Cada productId de zona-app existe en verify-purchase, resend-access y get-download-urls.
  B. Cada /dl/… de get-download-urls existe en disco, está trackeado en git y sirve 200
     con content-type binario (no text/html) y el mismo tamaño que en disco.
  C. Cada clave del dashboard tiene fichero en get-download-urls y viceversa (huérfanas).
  D. (2026-08-21) Validación producto↔sesión + webhook: netlify/shared/payment-links.ts cubre los 44
     productos y coincide con las env VITE_STRIPE_PAYMENT_LINK_* de Netlify (drift); stripe-webhook
     desplegado (LIVE: POST sin firma → 400; 501 = STRIPE_WEBHOOK_SECRET sin configurar → aviso);
     PURCHASE_VALIDATION informativo.
  D. LIVE: landing 200 con enlace buy.stripe.com (sin '#comprar'), -access y -library 200
     con <astro-island … client="only">.
  E. (2026-09-05) Pasarela cripto NOWPayments (piloto): netlify/shared/product-prices.ts cubre
     los mismos productIds que PRODUCTS y coincide con sync-product-prices.py --check (fichas +
     products-catalog.ts); existen las 4 functions (crypto-checkout, nowpayments-ipn,
     crypto-order-status, crypto-report) y netlify/shared/{nowpayments,crypto-orders}.ts;
     LIVE: NOWPAYMENTS_API_KEY/IPN_SECRET armadas, CRYPTO_PRODUCTS/API_BASE informativas,
     contrato HTTP de las 3 functions públicas. Ver PAGOS_CRYPTO_NOWPAYMENTS.md.

Uso:
  python3 scripts/productos-digitales/gate-flujo-postpago.py            # todo
  python3 scripts/productos-digitales/gate-flujo-postpago.py --offline  # sin HTTP
  python3 scripts/productos-digitales/gate-flujo-postpago.py --only kit-tareas-pasteleria
Salida: tabla por producto + lista de fallos; exit 1 si hay fallos.
"""
import argparse
import glob
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_URL = os.environ.get('AICP_BASE_URL', 'https://aichef.pro')
DL_DIR = os.path.join(ROOT, 'astro-site', 'public')
UA = {'User-Agent': 'Mozilla/5.0 (gate-flujo-postpago; +aichef.pro)'}


SITE_ID = os.environ.get('AICP_SITE_ID', 'ee5802cf-34bb-4354-90d9-aa9f628b4038')
ACCOUNT = os.environ.get('AICP_NETLIFY_ACCOUNT', 'chebfusiness')

# pro-prompts-ebook es el UNICO producto cuyas descargas NO salen de PRODUCT_FILES:
# get-download-urls.ts tiene una rama especial que las lee de estas 3 env vars.
# Sin esto el gate lo daba por bueno habiendo verificado CERO entregables suyos.
EBOOK_ENV = ('PDF_EBOOK_URL', 'PDF_BONUS1_URL', 'PDF_BONUS23_URL')
# Tarjetas de src/components/library/DownloadsSection.tsx (claves fijas del JSON).
EBOOK_CARDS = ('ebook', 'bonus1', 'bonus23')


def ebook_env_urls():
    """Lee PDF_*_URL del site de produccion via netlify CLI. {} si no se puede."""
    data = json.dumps({'account_id': ACCOUNT, 'site_id': SITE_ID})
    env = dict(os.environ, PATH=os.path.expanduser('~/Library/pnpm') + ':' + os.environ.get('PATH', ''))
    try:
        r = subprocess.run(['netlify', 'api', 'getEnvVars', '--data', data],
                           capture_output=True, text=True, timeout=60, env=env)
        vars_ = json.loads(r.stdout)
    except Exception:
        return {}
    out = {}
    for v in vars_:
        if v.get('key') in EBOOK_ENV:
            for val in v.get('values') or []:
                if val.get('value'):
                    out[v['key']] = val['value']
                    break
    return out


def netlify_env_vars():
    """Todas las env vars del site (valores solo de las no secretas). {} si no se puede."""
    data = json.dumps({'account_id': ACCOUNT, 'site_id': SITE_ID})
    env = dict(os.environ, PATH=os.path.expanduser('~/Library/pnpm') + ':' + os.environ.get('PATH', ''))
    try:
        r = subprocess.run(['netlify', 'api', 'getEnvVars', '--data', data],
                           capture_output=True, text=True, timeout=60, env=env)
        vars_ = json.loads(r.stdout)
    except Exception:
        return {}
    out = {}
    for v in vars_:
        vals = v.get('values') or []
        val = next((x.get('value') for x in vals if x.get('context') in ('production', 'all')), None) or (vals[0].get('value') if vals else None)
        out[v['key']] = {'value': val, 'secret': bool(v.get('is_secret')), 'scopes': v.get('scopes') or []}
    return out


def check_validacion_y_webhook(vp, offline):
    """Sección D. Devuelve (issues, warns, info)."""
    issues, warns, info = [], [], []
    # mapa productId → Payment Link congelado para las functions
    try:
        pl_src = read('netlify/shared/payment-links.ts')
    except FileNotFoundError:
        return (['falta netlify/shared/payment-links.ts (python3 scripts/productos-digitales/sync-payment-links.py)'], warns, info)
    links = dict(re.findall(r"^\s*'([^']+)':\s*'(https://buy\.stripe\.com/[^']+)'", pl_src, re.M))
    missing = sorted(set(vp) - set(links))
    extra = sorted(set(links) - set(vp))
    if missing:
        issues.append(f'productos de verify-purchase SIN Payment Link en payment-links.ts: {missing}')
    if extra:
        issues.append(f'payment-links.ts tiene productos que no existen en verify-purchase: {extra}')
    dup = {}
    for pid, u in links.items():
        dup.setdefault(u, []).append(pid)
    for u, pids in dup.items():
        if len(pids) > 1:
            issues.append(f'Payment Link compartido por {pids} (la validación no los distingue): {u}')
    for fn in ('netlify/functions/stripe-webhook.ts', 'netlify/shared/purchase-validation.ts'):
        if not os.path.exists(os.path.join(ROOT, fn)):
            issues.append(f'falta {fn}')
    for fn in ('verify-purchase', 'resend-access'):
        if 'validatePurchase(' not in read(f'netlify/functions/{fn}.ts'):
            issues.append(f'{fn}.ts no llama a validatePurchase(): la validación producto↔sesión no está cableada')
    if offline:
        warns.append('sección D: drift del mapa vs Netlify y estado del webhook SIN VERIFICAR en modo --offline')
        return issues, warns, info
    env = netlify_env_vars()
    if not env:
        warns.append('no se pudieron leer las env vars de Netlify (netlify CLI): drift y webhook sin verificar')
    else:
        # drift: el .ts congelado debe coincidir con las VITE_* del site
        src_map = {}
        for f in glob.glob(os.path.join(ROOT, 'astro-site/src/data/productos/*/*.ts')):
            if f.endswith('types.ts'):
                continue
            tt = open(f, encoding='utf-8').read()
            s = re.search(r"^\s*slug:\s*'([^']+)'", tt, re.M)
            k = re.search(r"^\s*stripeEnvKey:\s*'([^']+)'", tt, re.M)
            if s and k:
                src_map[s.group(1)] = k.group(1)
        src_map['pro-prompts-ebook'] = 'VITE_STRIPE_PAYMENT_LINK'
        src_map['mega-pack-tareas'] = 'VITE_STRIPE_PAYMENT_LINK_MEGA_PACK_TAREAS'
        for pid, key in sorted(src_map.items()):
            live = (env.get(key) or {}).get('value')
            if live and links.get(pid) and live != links[pid]:
                issues.append(f'DRIFT {pid}: Netlify {key}={live} ≠ payment-links.ts {links[pid]} (regenerar con sync-payment-links.py)')
            elif not live:
                issues.append(f'{pid}: env {key} no existe en Netlify')
        mode = (env.get('PURCHASE_VALIDATION') or {}).get('value') or 'soft (default)'
        info.append(f'PURCHASE_VALIDATION = {mode}')
        if 'STRIPE_WEBHOOK_SECRET' not in env:
            warns.append('STRIPE_WEBHOOK_SECRET no existe en el site: el webhook está INERTE (John: registrar endpoint en Stripe + env var)')
        elif 'functions' not in env['STRIPE_WEBHOOK_SECRET']['scopes']:
            issues.append("STRIPE_WEBHOOK_SECRET sin scope 'functions'")
    # el endpoint responde (400 sin firma = desplegado y armado; 501 = inerte)
    st, _, _, body = http_post(BASE_URL + '/.netlify/functions/stripe-webhook', '{}')
    if st == 400:
        info.append('stripe-webhook LIVE: 400 sin firma (desplegado y armado)')
    elif st == 501:
        warns.append('stripe-webhook LIVE responde 501: desplegado pero sin STRIPE_WEBHOOK_SECRET')
    else:
        issues.append(f'stripe-webhook LIVE → {st} (esperado 400/501): {body[:80]!r}')
    return issues, warns, info


CRYPTO_FUNCTIONS = ('crypto-checkout', 'nowpayments-ipn', 'crypto-order-status', 'crypto-report')
CRYPTO_SHARED = ('netlify/shared/nowpayments.ts', 'netlify/shared/crypto-orders.ts')


def check_pasarela_cripto(vp, offline):
    """Sección E — Pasarela cripto (NOWPayments). Devuelve (issues, warns, info).

    Ver PAGOS_CRYPTO_NOWPAYMENTS.md § Especificación de implementación v1 (piloto).
    Las 4 functions y netlify/shared/crypto-orders.ts pueden no existir todavía
    (piloto en construcción): eso se reporta como issue, nunca como excepción.
    """
    issues, warns, info = [], [], []
    # (a) netlify/shared/product-prices.ts cubre EXACTAMENTE los productIds de PRODUCTS
    # (el mismo `vp` que usa la sección D, parseado por parse_products_map()).
    try:
        pp_src = read('netlify/shared/product-prices.ts')
    except FileNotFoundError:
        issues.append('falta netlify/shared/product-prices.ts (python3 scripts/productos-digitales/sync-product-prices.py)')
        pp_src = None
    if pp_src is not None:
        pp_ids = set(re.findall(r"^\s*'([^']+)':\s*\{\s*eur:", pp_src, re.M))
        missing = sorted(set(vp) - pp_ids)
        extra = sorted(pp_ids - set(vp))
        if missing:
            issues.append(f'productos de verify-purchase SIN precio en product-prices.ts: {missing}')
        if extra:
            issues.append(f'product-prices.ts tiene productos que no existen en verify-purchase: {extra}')
    # (b) el generador está de acuerdo consigo mismo (fichas + catálogo de banners)
    sync_script = os.path.join(ROOT, 'scripts', 'productos-digitales', 'sync-product-prices.py')
    try:
        r = subprocess.run(['python3', sync_script, '--check'], capture_output=True, text=True,
                           timeout=60, cwd=ROOT)
        if r.returncode != 0:
            salida = (r.stdout + r.stderr).strip().splitlines()
            issues.append('sync-product-prices.py --check falló: ' + ' | '.join(salida[:10]))
    except Exception as e:  # noqa
        warns.append(f'no se pudo ejecutar sync-product-prices.py --check: {e}')
    # (c) las 4 functions + los 2 ficheros compartidos existen
    for fn in CRYPTO_FUNCTIONS:
        if not os.path.exists(os.path.join(ROOT, f'netlify/functions/{fn}.ts')):
            issues.append(f'falta netlify/functions/{fn}.ts: la pasarela cripto no está desplegada')
    for fn in CRYPTO_SHARED:
        if not os.path.exists(os.path.join(ROOT, fn)):
            issues.append(f'falta {fn}')
    if offline:
        warns.append('sección E: env vars y HTTP LIVE de la pasarela cripto SIN VERIFICAR en modo --offline')
        return issues, warns, info
    # (d) LIVE: env vars
    env = netlify_env_vars()
    if not env:
        warns.append('no se pudieron leer las env vars de Netlify (netlify CLI): pasarela cripto sin verificar en LIVE')
    else:
        for key in ('NOWPAYMENTS_API_KEY', 'NOWPAYMENTS_IPN_SECRET'):
            v = env.get(key)
            if not v or not v.get('value'):
                issues.append(f'{key} no existe en Netlify: la pasarela cripto está INERTE')
            elif not v['secret']:
                issues.append(f'{key} existe pero NO está marcada como secreta en Netlify')
            elif 'functions' not in v['scopes']:
                issues.append(f"{key} sin scope 'functions'")
        cp = (env.get('CRYPTO_PRODUCTS') or {}).get('value')
        if not cp or not cp.strip():
            warns.append('CRYPTO_PRODUCTS vacío o inexistente: el botón de pago cripto está APAGADO en todos los productos')
        elif cp.strip().lower() == 'all':
            info.append(f'CRYPTO_PRODUCTS = all (pasarela cripto activa en los {len(vp)} productos)')
        else:
            n = len([p for p in cp.split(',') if p.strip()])
            info.append(f'CRYPTO_PRODUCTS = lista explícita de {n} producto(s)')
        base = (env.get('NOWPAYMENTS_API_BASE') or {}).get('value')
        if base:
            info.append(f'NOWPAYMENTS_API_BASE = {base}')
            if 'sandbox' in base.lower():
                warns.append(f'NOWPAYMENTS_API_BASE apunta a SANDBOX: {base} (el piloto real necesita producción)')
    # (e) LIVE: contrato HTTP de las 3 functions públicas
    st, _, _, body = http_post(BASE_URL + '/.netlify/functions/nowpayments-ipn', '{}')
    if st == 400:
        info.append('nowpayments-ipn LIVE: 400 sin firma (desplegado y armado)')
    elif st == 501:
        warns.append('nowpayments-ipn LIVE responde 501: desplegado pero sin configurar (falta NOWPAYMENTS_IPN_SECRET/JWT_SECRET/RESEND_API_KEY)')
    elif st == 404:
        issues.append('nowpayments-ipn LIVE → 404: la function no está desplegada')
    else:
        issues.append(f'nowpayments-ipn LIVE → {st} (esperado 400/501): {body[:80]!r}')

    st2, ct2, _, body2 = http(BASE_URL + '/.netlify/functions/crypto-order-status?o=' + '0' * 32)
    if st2 == 404:
        html2 = body2.decode('utf-8', 'ignore')
        if 'text/html' in (ct2 or '') or html2.lstrip()[:15].lower().startswith('<!doctype html'):
            issues.append('crypto-order-status LIVE → 404 de Netlify (Function not found/HTML): la function no está desplegada')
        else:
            info.append('crypto-order-status LIVE: 404 (pedido inexistente devuelto por la function, desplegada)')
    else:
        issues.append(f'crypto-order-status LIVE → {st2} (esperado 404 para un orderId inexistente)')

    st3, _, _, body3 = http_post(BASE_URL + '/.netlify/functions/crypto-checkout', '{}')
    if st3 in (400, 501, 503):
        info.append(f'crypto-checkout LIVE: {st3} (desplegado)')
    elif st3 == 404:
        issues.append('crypto-checkout LIVE → 404: la function no está desplegada')
    else:
        issues.append(f'crypto-checkout LIVE → {st3} (esperado 400/501/503): {body3[:80]!r}')
    return issues, warns, info


def http_post(url, data):
    args = ['curl', '-sS', '-A', UA['User-Agent'], '--max-time', '30', '-D', '-', '-X', 'POST',
            '-H', 'Content-Type: application/json', '--data', data, url]
    try:
        r = subprocess.run(args, capture_output=True, timeout=40)
    except Exception as e:  # noqa
        return -1, str(e), None, b''
    raw = r.stdout
    sep = raw.find(b'\r\n\r\n')
    if r.returncode != 0 or sep == -1:
        return -1, '', None, b''
    lines = raw[:sep].decode('latin-1').split('\r\n')
    status = int(lines[0].split()[1]) if len(lines[0].split()) > 1 else -1
    return status, '', None, raw[sep + 4:]


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()


def parse_zona_app():
    src = read('astro-site/src/lib/zona-app.ts')
    out = []
    for m in re.finditer(r"\{\s*productId:\s*'([^']+)'.*?\}", src, re.S):
        blk = m.group(0)
        d = {'productId': m.group(1)}
        for k in ('accessPath', 'libraryPath', 'landingPath', 'storageKey', 'dashboardComponent', 'gateComponent'):
            mm = re.search(rf"{k}:\s*'([^']+)'", blk)
            d[k] = mm.group(1) if mm else None
        out.append(d)
    return out


def parse_products_map(path):
    """PRODUCTS: Record<string, ProductConfig> = { 'id': { accessPath: '…', … }, … }"""
    src = read(path)
    m = re.search(r"const PRODUCTS[^=]*=\s*\{(.*?)\n\};", src, re.S)
    body = m.group(1)
    return {k: v for k, v in re.findall(r"\n  '([^']+)':\s*\{[^}]*?accessPath:\s*'([^']+)'", body)}


def parse_product_files():
    src = read('netlify/functions/get-download-urls.ts')
    m = re.search(r"const PRODUCT_FILES[^=]*=\s*\{(.*?)\n\};", src, re.S)
    body = m.group(1)
    products = {}
    cur = None
    for line in body.split('\n'):
        mp = re.match(r"^  '([^']+)':\s*\{", line)
        if mp:
            cur = mp.group(1)
            products[cur] = {}
            continue
        mf = re.match(r"^    '([^']+)':\s*'([^']+)'", line)
        if mf and cur:
            products[cur][mf.group(1)] = mf.group(2)
    return products


def parse_dashboard_keys(component):
    path = os.path.join(ROOT, 'src', 'pages', component + '.tsx')
    if not os.path.exists(path):
        return None
    src = open(path, encoding='utf-8').read()
    if component == 'MegaPackTareasDashboard':
        # Composición `${kit.id}__${tpl.key}` (MegaPackTareasDashboard.tsx:249) sobre
        # una lista inline de kits con sus templates.
        keys = []
        for m in re.finditer(r"\{\s*id:\s*'([^']+)'.*?templates:\s*\[(.*?)\]\s*\}", src, re.S):
            kit = m.group(1)
            keys += [f"{kit}__{k}" for k in re.findall(r"\bkey:\s*'([^']+)'", m.group(2))]
        return keys
    return re.findall(r"\bkey:\s*'([^']+)'", src)


def git_tracked(rel_paths):
    res = subprocess.run(['git', 'ls-files', '--', 'astro-site/public/dl'], cwd=ROOT, capture_output=True, text=True)
    tracked = set(res.stdout.split('\n'))
    return {p: (('astro-site/public' + p) in tracked) for p in rel_paths}


def http(url, method='GET', max_bytes=None):
    """HTTP vía curl (el python3 del sistema no trae CA bundle → urllib falla con SSL)."""
    args = ['curl', '-sS', '-A', UA['User-Agent'], '--max-time', '30', '-D', '-']
    if method == 'HEAD':
        args += ['-I']
    args += [url]
    try:
        r = subprocess.run(args, capture_output=True, timeout=40)
    except Exception as e:  # noqa
        return -1, str(e), None, b''
    raw = r.stdout
    if r.returncode != 0 or not raw:
        return -1, r.stderr.decode('utf-8', 'ignore')[:120], None, b''
    # separar cabeceras (puede haber varias en redirects; nos quedamos con el último bloque)
    sep = raw.find(b'\r\n\r\n')
    if sep == -1:
        return -1, 'no-headers', None, b''
    head, body = raw[:sep], raw[sep + 4:]
    # curl -I: la body queda vacía; para GET, si hubo 3xx sin -L, body es la del 3xx
    lines = head.decode('latin-1').split('\r\n')
    status = int(lines[0].split()[1]) if len(lines[0].split()) > 1 else -1
    hdrs = {}
    for ln in lines[1:]:
        if ':' in ln:
            k, v = ln.split(':', 1)
            hdrs[k.strip().lower()] = v.strip()
    return status, hdrs.get('content-type', ''), hdrs.get('content-length'), body


def check_dl(path):
    disk = os.path.join(DL_DIR, path.lstrip('/'))
    on_disk = os.path.exists(disk)
    size_disk = os.path.getsize(disk) if on_disk else None
    st, ct, cl, _ = http(BASE_URL + path, method='HEAD')
    ok = st == 200 and 'text/html' not in ct and (cl is None or size_disk is None or int(cl) == size_disk)
    return {'path': path, 'disk': on_disk, 'size_disk': size_disk, 'status': st, 'ct': ct.split(';')[0], 'cl': cl, 'ok': ok}


def check_page(path, kind):
    st, ct, _, body = http(BASE_URL + path)
    html = body.decode('utf-8', 'ignore')
    if kind == 'landing':
        ok = st == 200 and 'buy.stripe.com' in html and 'href="#comprar"' not in html
        detail = 'stripe' if 'buy.stripe.com' in html else ('#comprar' if '#comprar' in html else 'no-buy-link')
    else:
        m = re.search(r'<astro-island[^>]*component-url="([^"]+)"[^>]*client="only"', html)
        ok = st == 200 and bool(m)
        detail = m.group(1) if m else 'no-island'
    return {'path': path, 'status': st, 'ok': ok, 'detail': detail}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--offline', action='store_true')
    ap.add_argument('--only', help='productId')
    ap.add_argument('--json', help='ruta para volcar el informe JSON')
    args = ap.parse_args()

    zona = parse_zona_app()
    vp = parse_products_map('netlify/functions/verify-purchase.ts')
    ra = parse_products_map('netlify/functions/resend-access.ts')
    files = parse_product_files()
    if args.only:
        zona = [z for z in zona if z['productId'] == args.only]

    fails = []
    warns = []
    report = []
    all_dl = []
    for z in zona:
        pid = z['productId']
        row = {'productId': pid, 'issues': [], 'warns': []}
        # A. presencia en mapas
        if pid not in vp:
            row['issues'].append('falta en verify-purchase PRODUCTS')
        elif vp[pid] != z['accessPath']:
            row['issues'].append(f"accessPath verify-purchase {vp[pid]} != zona-app {z['accessPath']}")
        if pid not in ra:
            row['issues'].append('falta en resend-access PRODUCTS')
        elif ra[pid] != z['accessPath']:
            row['issues'].append(f"accessPath resend-access {ra[pid]} != zona-app {z['accessPath']}")
        pf = files.get(pid)
        if pid == 'pro-prompts-ebook':
            # Rama especial de get-download-urls.ts: 3 env vars en lugar de PRODUCT_FILES.
            pf = dict(pf or {})
            if args.offline:
                row['warns'].append('descargas por env var: SIN VERIFICAR en modo --offline (correr sin --offline)')
            else:
                urls = ebook_env_urls()
                faltan = [k for k in EBOOK_ENV if not urls.get(k)]
                if faltan:
                    row['issues'].append(
                        'no se pudieron leer %s del site (netlify CLI logueado?) -> el dashboard '
                        'mostraria "No disponible"' % ', '.join(faltan))
                for k, card in zip(EBOOK_ENV, EBOOK_CARDS):
                    u = urls.get(k)
                    if not u:
                        continue
                    if u.startswith(BASE_URL + '/'):
                        pf[card] = u[len(BASE_URL):]
                    else:
                        row['issues'].append('%s apunta fuera de %s (%s): no se puede cotejar con disco/git'
                                             % (k, BASE_URL, u))
                row['n_cards'] = len(EBOOK_CARDS)
                sin_url = [c for c in EBOOK_CARDS if c not in pf]
                if sin_url:
                    row['issues'].append('tarjetas de DownloadsSection sin URL verificable: %s' % sin_url)
        elif pf is None:
            row['issues'].append('falta en get-download-urls PRODUCT_FILES')
            pf = {}
        row['n_files'] = len(pf)
        # C. dashboard keys
        dkeys = parse_dashboard_keys(z['dashboardComponent']) if z.get('dashboardComponent') else None
        if dkeys is not None and pid != 'pro-prompts-ebook':
            missing_in_files = [k for k in dkeys if k not in pf]
            missing_in_dash = [k for k in pf if k not in dkeys]
            if missing_in_files:
                row['issues'].append(f"claves del dashboard sin fichero: {missing_in_files}")
            if missing_in_dash:
                row['issues'].append(f"ficheros sin tarjeta en dashboard: {missing_in_dash}")
            row['n_cards'] = len(dkeys)
        # B. disco/git
        tracked = git_tracked(list(pf.values()))
        for k, p in pf.items():
            disk = os.path.join(DL_DIR, p.lstrip('/'))
            if not os.path.exists(disk):
                row['issues'].append(f"NO en disco: {p}")
            elif not tracked.get(p):
                row['issues'].append(f"NO trackeado en git: {p}")
            all_dl.append((pid, p))
        report.append(row)

    if not args.offline:
        with cf.ThreadPoolExecutor(max_workers=8) as ex:
            dl_res = list(ex.map(lambda t: (t[0], check_dl(t[1])), all_dl))
            pages = []
            for z in zona:
                pages.append((z['productId'], 'landing', z['landingPath']))
                pages.append((z['productId'], 'access', z['accessPath']))
                pages.append((z['productId'], 'library', z['libraryPath']))
            pg_res = list(ex.map(lambda t: (t[0], t[1], check_page(t[2], t[1])), pages))
        by_pid = {r['productId']: r for r in report}
        for pid, r in dl_res:
            by_pid[pid].setdefault('dl_ok', 0)
            if r['ok']:
                by_pid[pid]['dl_ok'] += 1
            else:
                by_pid[pid]['issues'].append(f"LIVE {r['path']} → {r['status']} {r['ct']} cl={r['cl']} disco={r['size_disk']}")
        for pid, kind, r in pg_res:
            by_pid[pid][kind] = f"{r['status']}{'' if r['ok'] else ' ✗ ' + r['detail']}"
            if not r['ok']:
                by_pid[pid]['issues'].append(f"LIVE {kind} {r['path']} → {r['status']} {r['detail']}")

    # salida
    print(f"{'productId':42s} {'files':>5s} {'cards':>5s} {'dl_ok':>5s} {'landing':>8s} {'access':>7s} {'library':>8s}  issues")
    for r in report:
        print(f"{r['productId']:42s} {r.get('n_files', 0):5d} {str(r.get('n_cards', '-')):>5s} {str(r.get('dl_ok', '-')):>5s} "
              f"{str(r.get('landing', '-')):>8s} {str(r.get('access', '-')):>7s} {str(r.get('library', '-')):>8s}  {len(r['issues'])}")
        for i in r['issues']:
            print(f"    ✗ {i}")
        for w in r.get('warns', []):
            print(f"    ⚠ {w}")
        fails.extend(r['issues'])
        warns.extend(r.get('warns', []))
    # D. validación producto↔sesión + webhook (transversal, no por producto)
    d_issues, d_warns, d_info = check_validacion_y_webhook(vp, args.offline)
    print('\nValidación producto↔sesión + webhook:')
    for i in d_info:
        print(f'    · {i}')
    for i in d_issues:
        print(f'    ✗ {i}')
    for w in d_warns:
        print(f'    ⚠ {w}')
    if not d_issues and not d_warns:
        print('    ✓ mapa de 44 Payment Links al día, validación cableada, webhook armado')
    fails.extend(d_issues)
    warns.extend(d_warns)
    # E. pasarela cripto NOWPayments (transversal, no por producto)
    e_issues, e_warns, e_info = check_pasarela_cripto(vp, args.offline)
    print('\nPasarela cripto (NOWPayments):')
    for i in e_info:
        print(f'    · {i}')
    for i in e_issues:
        print(f'    ✗ {i}')
    for w in e_warns:
        print(f'    ⚠ {w}')
    if not e_issues and not e_warns:
        print('    ✓ product-prices.ts al día, 4 functions desplegadas, env vars armadas, contrato HTTP OK')
    fails.extend(e_issues)
    warns.extend(e_warns)
    print(f"\nProductos: {len(report)} · entregables: {len(all_dl)} · fallos: {len(fails)} · avisos: {len(warns)}")
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
