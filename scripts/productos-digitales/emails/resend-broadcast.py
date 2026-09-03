#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resend-broadcast.py — Programa (o prueba) un broadcast de AI Chef Pro en Resend por API.

    python3 scripts/productos-digitales/emails/resend-broadcast.py \
        --html scripts/productos-digitales/emails/broadcast-guia-food-cost-lanzamiento-es.html \
        --subject "Nuevo: Guía Food Cost + Ingeniería de Menú" \
        --name "Lanzamiento Guía Food Cost (ES)" \
        --scheduled-at 2026-09-04T08:00:00Z          # 10:00 Madrid (CEST = UTC+2)
        [--segment b2c581bd-81db-4ded-a174-2b339f7d3cc3]   # «AI Chef Pro ES» (skill resend-operaciones-grupo)
        [--test john@chefbusiness.co]  # envía UNA prueba transaccional y termina (no programa nada)
        [--dry-run]                    # valida y muestra el payload sin llamar a la API

CREDENCIAL: se lee de ~/.config/resend/claude-code-local.key (fichero 0600, fuera del repo,
creado por John desde su terminal). NUNCA se imprime. Al terminar la sesión, la key se borra del
panel (decisión de John, 2026-08-02).

GUARDAS antes de programar (todas bloquean):
  · no queda ningún token __PAGINAS__ en el HTML;
  · {{{RESEND_UNSUBSCRIBE_URL}}} está en el HTML (bloque de baja obligatorio);
  · toda imagen y todo enlace https://aichef.pro/... del HTML responde 200 en producción
    (no se manda tráfico a una landing o a una imagen que no existe);
  · la hora programada está en el futuro.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

API = 'https://api.resend.com'
KEY_FILE = os.path.expanduser('~/.config/resend/claude-code-local.key')
FROM = 'AI Chef Pro <hola@news.aichef.pro>'
REPLY_TO = 'info@aichef.pro'
SEGMENT_AICP_ES = 'b2c581bd-81db-4ded-a174-2b339f7d3cc3'


def leer_key():
    if not os.path.exists(KEY_FILE):
        sys.exit('falta la credencial: %s (créala desde tu terminal, permisos 600)' % KEY_FILE)
    k = open(KEY_FILE, encoding='utf-8').read().strip()
    if not k.startswith('re_'):
        sys.exit('la key de %s no parece de Resend' % KEY_FILE)
    return k


def http(method, path, key, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode('utf-8') if body is not None else None,
                                 headers={'Authorization': 'Bearer ' + key,
                                          'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode('utf-8') or '{}')
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode('utf-8') or '{}')


def vivo(url):
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'aichef-broadcast-gate'})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.headers.get('content-type', '')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:  # noqa
        return 0, str(e)


def guardas(html, scheduled_at):
    fallos = []
    if '__PAGINAS' in html:
        fallos.append('quedan tokens __PAGINAS__ en el HTML')
    if '{{{RESEND_UNSUBSCRIBE_URL}}}' not in html:
        fallos.append('falta el bloque de baja {{{RESEND_UNSUBSCRIBE_URL}}}')
    urls = set(re.findall(r'(?:href|src)="(https://aichef\.pro/[^"]+)"', html))
    for u in sorted(urls):
        u_plain = u.replace('&amp;', '&')
        st, ct = vivo(u_plain)
        img = u_plain.endswith(('.jpg', '.png', '.webp'))
        ok = st == 200 and (ct.startswith('image/') if img else True)
        print('  %s %s (%s %s)' % ('OK ' if ok else 'KO ', u_plain, st, ct.split(';')[0]))
        if not ok:
            fallos.append('no vivo: ' + u_plain)
    if scheduled_at:
        t = datetime.fromisoformat(scheduled_at.replace('Z', '+00:00'))
        if t <= datetime.now(timezone.utc):
            fallos.append('scheduled_at está en el pasado: ' + scheduled_at)
    return fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--html', required=True)
    ap.add_argument('--subject', required=True)
    ap.add_argument('--name', default=None)
    ap.add_argument('--segment', default=SEGMENT_AICP_ES)
    ap.add_argument('--scheduled-at', default=None, help='ISO 8601 UTC, p. ej. 2026-09-04T08:00:00Z')
    ap.add_argument('--test', default=None, help='email de prueba (envío transaccional, no programa)')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    html = open(a.html, encoding='utf-8').read()
    print('guardas:')
    fallos = guardas(html, a.scheduled_at)
    if fallos:
        sys.exit('ABORTADO:\n  - ' + '\n  - '.join(fallos))
    print('guardas OK')

    if a.dry_run:
        print(json.dumps({'segment_id': a.segment, 'from': FROM, 'reply_to': REPLY_TO,
                          'subject': a.subject, 'name': a.name, 'send': bool(a.scheduled_at),
                          'scheduled_at': a.scheduled_at, 'html_bytes': len(html)},
                         ensure_ascii=False, indent=1))
        return

    key = leer_key()
    if a.test:
        cuerpo = html.replace('{{{RESEND_UNSUBSCRIBE_URL}}}', 'https://aichef.pro/#prueba-sin-baja')
        st, r = http('POST', '/emails', key, {
            'from': FROM, 'to': [a.test], 'reply_to': REPLY_TO,
            'subject': '[PRUEBA] ' + a.subject, 'html': cuerpo,
            'tags': [{'name': 'kind', 'value': 'broadcast-test'}, {'name': 'app', 'value': 'aichef'}],
        })
        print('prueba →', st, r.get('id') or r)
        return

    if not a.scheduled_at:
        sys.exit('sin --scheduled-at no se programa nada (usa --dry-run o --test)')
    body = {'segment_id': a.segment, 'from': FROM, 'reply_to': REPLY_TO, 'subject': a.subject,
            'html': html, 'send': True, 'scheduled_at': a.scheduled_at}
    if a.name:
        body['name'] = a.name
    st, r = http('POST', '/broadcasts', key, body)
    print('broadcast →', st, json.dumps(r, ensure_ascii=False))
    if st not in (200, 201):
        sys.exit(1)
    bid = r.get('id')
    st2, r2 = http('GET', '/broadcasts/' + bid, key)
    print('estado →', st2, {k: r2.get(k) for k in ('id', 'status', 'scheduled_at', 'segment_id', 'subject')})


if __name__ == '__main__':
    main()
