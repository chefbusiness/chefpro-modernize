#!/usr/bin/env python3
"""
Auditoría de los Payment Links de Stripe de AI Chef Pro (44 productos) con el Stripe CLI.

Comprueba, para cada Payment Link del mapa netlify/shared/payment-links.ts:
  - que existe y está activo en Stripe;
  - que su «after completion» es un REDIRECT a
      https://aichef.pro<accessPath>?session_id={CHECKOUT_SESSION_ID}
    (accessPath = el de PRODUCTS en netlify/functions/verify-purchase.ts). Sin ese redirect el
    cliente nunca llega al gate y, sin webhook, nadie le manda el email de acceso.
  - y lista los links activos de la cuenta que NO están en el mapa (productos huérfanos).

Requisito: el CLI logueado en la cuenta de AI Chef Pro bajo un project-name propio
(el `default` del Mac es Miselup). Consulta en modo LIVE (`--live`): el CLI usa TEST por
defecto y ahí no existe ningún Payment Link — los 44 salían como «NO existe» (STRIPE_LIVE=0 para test):
    stripe login --project-name aichefpro
Uso:
    python3 scripts/productos-digitales/audit-payment-links.py              # tabla
    python3 scripts/productos-digitales/audit-payment-links.py --sessions cliente@dominio.com
        → sesiones de Checkout de ese email (producto según payment_link, estado, fecha)
Exit 1 si algún link falla el redirect.
"""
import json, os, re, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT = os.environ.get('STRIPE_PROJECT', 'aichefpro')
BASE = 'https://aichef.pro'


LIVE = os.environ.get('STRIPE_LIVE', '1') != '0'  # el CLI consulta TEST por defecto; los links viven en LIVE


def stripe(*args):
    cmd = ['stripe', '--project-name', PROJECT, *args, *(['--live'] if LIVE else [])]  # --live va tras el subcomando
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        err = r.stderr.strip()
        if 'not logged in' in err.lower() or 'no api key' in err.lower() or 'login' in err.lower():
            sys.exit(f"✗ Stripe CLI sin sesión para el proyecto «{PROJECT}». Ejecuta: stripe login --project-name {PROJECT}\n{err[:300]}")
        sys.exit(f'✗ {" ".join(cmd)} → {err[:400]}')
    return json.loads(r.stdout)


def payment_links_map():
    t = open(os.path.join(ROOT, 'netlify/shared/payment-links.ts'), encoding='utf-8').read()
    return dict(re.findall(r"^\s*'([^']+)':\s*'(https://buy\.stripe\.com/[^']+)'", t, re.M))


def access_paths():
    t = open(os.path.join(ROOT, 'netlify/functions/verify-purchase.ts'), encoding='utf-8').read()
    body = t.split('const PRODUCTS', 1)[1].split('\n};', 1)[0]
    return dict(re.findall(r"\n  '([^']+)':\s*\{[^}]*?accessPath:\s*'([^']+)'", body))


def list_all(resource, **params):
    out, starting_after = [], None
    while True:
        args = [resource, 'list', '--limit', '100']
        for k, v in params.items():
            args += [f'--{k}', v]
        if starting_after:
            args += ['--starting-after', starting_after]
        page = stripe(*args)
        out.extend(page.get('data', []))
        if not page.get('has_more'):
            return out
        starting_after = out[-1]['id']


def norm(u):
    return (u or '').split('#')[0].split('?')[0].rstrip('/')


def main():
    if '--sessions' in sys.argv:
        email = sys.argv[sys.argv.index('--sessions') + 1]
        links = {norm(v): k for k, v in payment_links_map().items()}
        sessions = stripe('checkout_sessions', 'list', '--limit', '100', '-d', f'customer_details[email]={email}').get('data', [])
        print(f'{len(sessions)} sesiones para {email}')
        for s in sessions:
            pl = s.get('payment_link')
            url = None
            if pl:
                url = norm(stripe('payment_links', 'retrieve', pl).get('url'))
            ts = datetime.datetime.utcfromtimestamp(s['created']).strftime('%Y-%m-%d %H:%M')
            print(f"  {ts}  {s['id']}  {s.get('payment_status'):8s}  {s.get('amount_total', 0)/100:.2f} {s.get('currency','').upper()}  {links.get(url, '¿?')}  {url or 'sin payment_link'}")
        return

    links = payment_links_map()
    paths = access_paths()
    live = {norm(l.get('url')): l for l in list_all('payment_links')}
    fails = 0
    print(f"{'productId':42s} {'activo':6s} {'after_completion':18s} ok  detalle")
    for pid in sorted(links):
        url = norm(links[pid])
        l = live.get(url)
        if not l:
            print(f'{pid:42s} {"—":6s} {"—":18s} ✗   link {url} NO existe en esta cuenta de Stripe')
            fails += 1
            continue
        ac = l.get('after_completion') or {}
        typ = ac.get('type')
        redirect = (ac.get('redirect') or {}).get('url') or ''
        expected = f"{BASE}{paths.get(pid, '?')}?session_id={{CHECKOUT_SESSION_ID}}"
        ok = bool(l.get('active')) and typ == 'redirect' and redirect == expected
        fails += 0 if ok else 1
        detail = '' if ok else (f'inactivo; ' if not l.get('active') else '') + (f'{typ} → {redirect or "(sin url)"} ≠ {expected}' if not (typ == 'redirect' and redirect == expected) else '')
        print(f"{pid:42s} {str(bool(l.get('active'))):6s} {str(typ):18s} {'✓' if ok else '✗'}   {detail}")
    mapped = {norm(v) for v in links.values()}
    extra = [l for u, l in live.items() if u not in mapped and l.get('active')]
    if extra:
        print(f'\n⚠ {len(extra)} Payment Links activos en Stripe que NO están en el mapa (huérfanos o productos nuevos sin cablear):')
        for l in extra:
            print(f"   {l['id']}  {l.get('url')}  {((l.get('metadata') or {}).get('product') or '')}")
    print(f'\n{len(links)} links · fallos de redirect/activo: {fails}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
