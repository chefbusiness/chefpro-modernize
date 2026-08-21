#!/usr/bin/env python3
"""
Mapa productId → URL del Payment Link de Stripe, generado desde las env vars
VITE_STRIPE_PAYMENT_LINK_* del site de producción (Netlify API; NO son secretas:
Vite las inlina en el HTML de cada landing).

Lo consumen las functions (verify-purchase / resend-access / stripe-webhook) para
VALIDAR que la sesión pagada corresponde al producto pedido — las env VITE_* tienen
scope «builds» (límite 4 KB de Lambda) y NO existen en runtime, por eso se congela
en netlify/shared/payment-links.ts (fuera de netlify/functions/ para que el bundler
de Netlify nunca lo tome por una function) y se commitea.

Uso:
  python3 scripts/productos-digitales/sync-payment-links.py          # regenera el .ts
  python3 scripts/productos-digitales/sync-payment-links.py --check  # exit 1 si el .ts difiere de Netlify
Fuente del mapa productId → envKey: `slug` + `stripeEnvKey` de astro-site/src/data/productos/**/*.ts
(+ pro-prompts-ebook → VITE_STRIPE_PAYMENT_LINK, mega-pack-tareas → VITE_STRIPE_PAYMENT_LINK_MEGA_PACK_TAREAS,
que no tienen data file tipado). Se cruza con PRODUCTS de verify-purchase.ts: deben ser los mismos 44.
"""
import glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE_ID = os.environ.get('AICP_SITE_ID', 'ee5802cf-34bb-4354-90d9-aa9f628b4038')
ACCOUNT = os.environ.get('AICP_NETLIFY_ACCOUNT', 'chebfusiness')
OUT = os.path.join(ROOT, 'netlify', 'shared', 'payment-links.ts')
SPECIAL = {
    'pro-prompts-ebook': 'VITE_STRIPE_PAYMENT_LINK',
    'mega-pack-tareas': 'VITE_STRIPE_PAYMENT_LINK_MEGA_PACK_TAREAS',
}


def product_env_keys():
    m = dict(SPECIAL)
    for f in glob.glob(os.path.join(ROOT, 'astro-site/src/data/productos/*/*.ts')):
        if f.endswith('types.ts'):
            continue
        t = open(f, encoding='utf-8').read()
        slug = re.search(r"^\s*slug:\s*'([^']+)'", t, re.M)
        key = re.search(r"^\s*stripeEnvKey:\s*'([^']+)'", t, re.M)
        if slug and key:
            m[slug.group(1)] = key.group(1)
    return m


def verify_purchase_products():
    t = open(os.path.join(ROOT, 'netlify/functions/verify-purchase.ts'), encoding='utf-8').read()
    block = t.split('const PRODUCTS', 1)[1].split('\n};', 1)[0]
    return set(re.findall(r"^\s{2}'([a-z0-9-]+)':\s*\{", block, re.M))


def netlify_env():
    data = json.dumps({'account_id': ACCOUNT, 'site_id': SITE_ID})
    out = subprocess.run(['netlify', 'api', 'getEnvVars', '--data', data], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f'netlify api getEnvVars falló: {out.stderr.strip()[:300]}')
    env = {}
    for v in json.loads(out.stdout):
        vals = v.get('values') or []
        # preferir el contexto de producción; si no, el primero
        val = next((x.get('value') for x in vals if x.get('context') in ('production', 'all')), None) or (vals[0].get('value') if vals else None)
        env[v['key']] = val
    return env


def render(links):
    lines = [
        '// GENERADO por scripts/productos-digitales/sync-payment-links.py — NO editar a mano.',
        '// productId → URL pública del Payment Link de Stripe (la misma que Vite inlina en la landing).',
        '// Regenerar tras cambiar cualquier VITE_STRIPE_PAYMENT_LINK_* en Netlify; el gate --check avisa del drift.',
        'export const PAYMENT_LINKS: Record<string, string> = {',
    ]
    for pid in sorted(links):
        lines.append(f"  '{pid}': '{links[pid]}',")
    lines.append('};')
    lines.append('')
    lines.append('/** URL → productId (para el webhook: la sesión trae payment_link, no el producto). */')
    lines.append('export const PRODUCT_BY_LINK: Record<string, string> = Object.fromEntries(')
    lines.append('  Object.entries(PAYMENT_LINKS).map(([pid, url]) => [url, pid]),')
    lines.append(');')
    lines.append('')
    return '\n'.join(lines)


def main():
    check = '--check' in sys.argv
    keys = product_env_keys()
    vp = verify_purchase_products()
    errors = []
    if set(keys) != vp:
        errors.append(f'productIds con stripeEnvKey ≠ PRODUCTS de verify-purchase: solo_data={sorted(set(keys)-vp)} solo_vp={sorted(vp-set(keys))}')
    env = netlify_env()
    links = {}
    for pid, key in sorted(keys.items()):
        url = env.get(key)
        if not url or not url.startswith('https://buy.stripe.com/'):
            errors.append(f'{pid}: env {key} ausente o no es buy.stripe.com ({url!r})')
        else:
            links[pid] = url
    dup = {}
    for pid, url in links.items():
        dup.setdefault(url, []).append(pid)
    for url, pids in dup.items():
        if len(pids) > 1:
            errors.append(f'Payment Link compartido por {pids}: {url} (la validación no puede distinguirlos)')
    if errors:
        for e in errors:
            print('✗', e)
        sys.exit(1)
    content = render(links)
    if check:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        if cur != content:
            print(f'✗ {os.path.relpath(OUT, ROOT)} difiere de Netlify: regenerar con sync-payment-links.py y commitear')
            sys.exit(1)
        print(f'✓ payment-links.ts al día ({len(links)} productos)')
        return
    open(OUT, 'w', encoding='utf-8').write(content)
    print(f'✓ escrito {os.path.relpath(OUT, ROOT)} con {len(links)} productos')


if __name__ == '__main__':
    main()
