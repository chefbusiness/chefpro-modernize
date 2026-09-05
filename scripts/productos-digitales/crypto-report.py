#!/usr/bin/env python3
"""
CLI del informe admin de la pasarela cripto (NOWPayments) — endpoint `crypto-report`.

Mismo patrón que scripts/productos-digitales/buscador-report.py: la contraseña admin
se resuelve de ADMIN_PASSWORD / `netlify env:get` / `netlify api getEnvVars` (en ese
orden), y el HTTP va por `curl` en subprocess (el python3 del Mac no trae CA bundle y
`urllib` revienta con SSL) con la contraseña en un fichero de config leído por STDIN,
NUNCA en argv (no aparece en `ps`).

Contrato (PAGOS_CRYPTO_NOWPAYMENTS.md § Especificación de implementación v1, piloto):
  GET /.netlify/functions/crypto-report?days=30[&format=csv][&purge_unpaid_before=YYYY-MM-DD]
  con cabecera x-admin-password -> JSON/CSV; 401; 429.
El libro de pedidos (Netlify Blobs, store `crypto-orders`) trae por pedido:
  orderId, productId, email, priceEur, currency, country, geoCountry, createdAt,
  status, invoiceId, paymentId, payCurrency, payAmount, actuallyPaid, delivered,
  deliveredAt, flags[]. Estados oficiales de NOWPayments (9): waiting, confirming,
  confirmed, sending, partially_paid, finished, failed, refunded, expired; un pedido
  sin paymentId todavía está en `created` (el comprador no eligió moneda).

Uso:
  python3 scripts/productos-digitales/crypto-report.py                      # ultimos 30 dias, tabla
  python3 scripts/productos-digitales/crypto-report.py --days 7
  python3 scripts/productos-digitales/crypto-report.py --csv                # CSV crudo (format=csv)
  python3 scripts/productos-digitales/crypto-report.py --pendientes         # con paymentId sin entregar, o partially_paid
  python3 scripts/productos-digitales/crypto-report.py --purge-unpaid-before 2026-08-01 [--yes]
  python3 scripts/productos-digitales/crypto-report.py --base https://deploy-preview-123--aichefpro.netlify.app

⚠️ La function `crypto-report` todavía no existe en producción (piloto en construcción,
ver PAGOS_CRYPTO_NOWPAYMENTS.md): este script solo se ha verificado con
`python3 -m py_compile`, NUNCA ejecutado contra el endpoint real.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_URL_DEFAULT = 'https://aichef.pro'
ENDPOINT = '/.netlify/functions/crypto-report'

SITE_ID = os.environ.get('AICP_SITE_ID', 'ee5802cf-34bb-4354-90d9-aa9f628b4038')
ACCOUNT = os.environ.get('AICP_NETLIFY_ACCOUNT', 'chebfusiness')


# ── Credencial (idéntico a buscador-report.py) ───────────────────────────────
def netlify_env():
    """PATH con el pnpm del Mac (donde vive el CLI de Netlify)."""
    return dict(os.environ, PATH=os.path.expanduser('~/Library/pnpm') + ':' + os.environ.get('PATH', ''))


def admin_password():
    pw = os.environ.get('ADMIN_PASSWORD')
    if pw:
        return pw.strip()
    env = netlify_env()
    # 1) netlify env:get (necesita el site enlazado en la carpeta)
    try:
        r = subprocess.run(['netlify', 'env:get', 'ADMIN_PASSWORD'], capture_output=True, text=True,
                           timeout=60, env=env, cwd=ROOT)
        for ln in reversed((r.stdout or '').split('\n')):
            ln = ln.strip().strip('│').strip()
            if ln and not ln.startswith(('┌', '└', '├', '─', 'Value', '.Env', 'No value')) and ' ' not in ln:
                return ln
    except Exception:
        pass
    # 2) netlify api getEnvVars (patrón ya probado en este repo)
    try:
        data = json.dumps({'account_id': ACCOUNT, 'site_id': SITE_ID})
        r = subprocess.run(['netlify', 'api', 'getEnvVars', '--data', data], capture_output=True,
                           text=True, timeout=60, env=env)
        for v in json.loads(r.stdout):
            if v.get('key') == 'ADMIN_PASSWORD':
                for val in v.get('values') or []:
                    if val.get('value'):
                        return val['value']
    except Exception:
        pass
    return None


# ── HTTP (curl; la contraseña por stdin, nunca en argv) ──────────────────────
def pedir_informe(base_url, pw, params, as_csv=False):
    qs = '&'.join(f'{k}={v}' for k, v in params.items() if v is not None and v != '')
    url = f'{base_url}{ENDPOINT}' + (f'?{qs}' if qs else '')
    esc = lambda s: s.replace('\\', '\\\\').replace('"', '\\"')  # noqa: E731
    config = (
        f'url = "{esc(url)}"\n'
        f'header = "x-admin-password: {esc(pw)}"\n'
        'max-time = 120\n'
        'silent\n'
        'show-error\n'
        'write-out = "\\nHTTP_STATUS:%{http_code}\\n"\n'
    )
    try:
        r = subprocess.run(['curl', '-K', '-'], input=config.encode('utf-8'),
                           capture_output=True, timeout=180)
    except Exception as e:  # noqa
        return None, -1, str(e)
    salida = r.stdout.decode('utf-8', 'ignore')
    m = re.search(r'HTTP_STATUS:(\d+)\s*$', salida)
    status = int(m.group(1)) if m else -1
    cuerpo = salida[:m.start()] if m else salida
    if status != 200:
        return None, status, (r.stderr.decode('utf-8', 'ignore') + cuerpo)[:300]
    if as_csv:
        return cuerpo, status, ''
    try:
        return json.loads(cuerpo), status, ''
    except Exception as e:  # noqa
        return None, status, f'respuesta no-JSON: {e}: {cuerpo[:200]!r}'


# ── Forma de la respuesta ─────────────────────────────────────────────────────
def extraer_pedidos(data):
    """La function puede devolver una lista pelada o un objeto envoltorio
    ({orders:[...]}, {pedidos:[...]}, {rows:[...]}, {data:[...]}) — se acepta
    cualquiera de las dos formas sin romper si cambia el nombre de la clave."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ('orders', 'pedidos', 'rows', 'data', 'items', 'results'):
            v = data.get(k)
            if isinstance(v, list):
                return v
    return []


def es_pendiente(p):
    """Con paymentId (ya eligió moneda) y no entregado, o partially_paid (infrapago
    a la espera de que John decida)."""
    tiene_pago = bool(p.get('paymentId'))
    entregado = bool(p.get('delivered'))
    estado = str(p.get('status') or '').lower()
    return (tiene_pago and not entregado) or estado == 'partially_paid'


def fecha_corta(v):
    s = str(v or '').strip()
    return s[:10] if s else '—'


def orderid_corto(v, n=10):
    s = str(v or '')
    return (s[:n] + '…') if len(s) > n else (s or '—')


def precio_txt(v):
    if v is None or v == '':
        return '—'
    try:
        return f'{float(v):.2f}'
    except (TypeError, ValueError):
        return str(v)


def recorta(s, n):
    s = str(s if s is not None else '—')
    return s if len(s) <= n else s[: n - 1] + '…'


def imprimir_tabla(pedidos, base_url, days, solo_pendientes):
    titulo = ' (solo pendientes)' if solo_pendientes else ''
    print(f'\n💳 Pasarela cripto (NOWPayments) — {base_url} · últimos {days} días{titulo}')
    print(f'   {len(pedidos)} pedido(s)')
    if not pedidos:
        print('\n   (sin pedidos en esta ventana)\n')
        return
    print(f'\n{"fecha":10} {"orderId":11} {"producto":32} {"EUR":>7} {"país":5} '
          f'{"estado":14} {"entreg.":7} moneda')
    print('─' * 100)
    for p in sorted(pedidos, key=lambda x: str(x.get('createdAt') or ''), reverse=True):
        pais = p.get('country') or p.get('geoCountry') or '—'
        print(f'{fecha_corta(p.get("createdAt")):10} '
              f'{orderid_corto(p.get("orderId")):11} '
              f'{recorta(p.get("productId"), 32):32} '
              f'{precio_txt(p.get("priceEur")):>7} '
              f'{recorta(pais, 5):5} '
              f'{recorta(p.get("status"), 14):14} '
              f'{"sí" if p.get("delivered") else "no":7} '
              f'{p.get("payCurrency") or "—"}')
    print()


def main():
    ap = argparse.ArgumentParser(description='Informe admin de la pasarela cripto NOWPayments (crypto-report).')
    ap.add_argument('--base', default=BASE_URL_DEFAULT, help=f'base del site (por defecto {BASE_URL_DEFAULT})')
    ap.add_argument('--days', type=int, default=30, help='ventana en días (1-365, por defecto 30)')
    ap.add_argument('--csv', action='store_true', help='imprime el CSV crudo (format=csv) tal cual lo sirve la function')
    ap.add_argument('--pendientes', action='store_true',
                    help='solo pedidos con paymentId y no entregados, o partially_paid')
    ap.add_argument('--purge-unpaid-before', metavar='YYYY-MM-DD',
                    help='purga pedidos created/expired anteriores a esta fecha (pide confirmación)')
    ap.add_argument('--yes', action='store_true', help='no pedir confirmación para --purge-unpaid-before')
    args = ap.parse_args()

    days = max(1, min(365, args.days))
    base_url = args.base.rstrip('/')

    if args.purge_unpaid_before:
        try:
            datetime.datetime.strptime(args.purge_unpaid_before, '%Y-%m-%d')
        except ValueError:
            print(f'✖ --purge-unpaid-before espera YYYY-MM-DD, recibido: {args.purge_unpaid_before!r}',
                  file=sys.stderr)
            return 2

    pw = admin_password()
    if not pw:
        print('✖ No hay ADMIN_PASSWORD. Exporta la variable o autentica el CLI de Netlify:\n'
              '   export ADMIN_PASSWORD=…   (o `netlify link` en el repo)', file=sys.stderr)
        return 2

    if args.purge_unpaid_before:
        if not args.yes:
            resp = input(f'¿Purgar pedidos created/expired anteriores a {args.purge_unpaid_before} '
                         f'en {base_url}? [s/N] ').strip().lower()
            if resp != 's':
                print('Cancelado.')
                return 0
        data, status, err = pedir_informe(base_url, pw, {'days': days, 'purge_unpaid_before': args.purge_unpaid_before})
        if data is None:
            print(f'✖ La purga falló (HTTP {status}): {err}', file=sys.stderr)
            return 1
        print(json.dumps(data, ensure_ascii=False, indent=2) if isinstance(data, (dict, list)) else data)
        return 0

    if args.csv:
        cuerpo, status, err = pedir_informe(base_url, pw, {'days': days, 'format': 'csv'}, as_csv=True)
        if cuerpo is None:
            print(f'✖ El informe falló (HTTP {status}): {err}', file=sys.stderr)
            return 1
        sys.stdout.write(cuerpo if cuerpo.endswith('\n') else cuerpo + '\n')
        return 0

    data, status, err = pedir_informe(base_url, pw, {'days': days})
    if data is None:
        print(f'✖ El informe falló (HTTP {status}): {err}', file=sys.stderr)
        if status == 401:
            print('  → ADMIN_PASSWORD no coincide con la del site.', file=sys.stderr)
        if status == 404:
            print('  → ¿está desplegada netlify/functions/crypto-report.ts?', file=sys.stderr)
        return 1

    pedidos = extraer_pedidos(data)
    if args.pendientes:
        pedidos = [p for p in pedidos if es_pendiente(p)]
    imprimir_tabla(pedidos, base_url, days, args.pendientes)
    return 0


if __name__ == '__main__':
    sys.exit(main())
