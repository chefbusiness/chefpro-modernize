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

CREDENCIAL: RESEND_API_KEY del entorno, o ~/.config/resend/claude-code-local.key, o la
RESEND_API_KEY de ~/michelin-leads/.env (cuenta única del grupo; acceso completo verificado el
2026-09-04). NUNCA se imprime ni se commitea.

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
from datetime import datetime, timezone

API = 'https://api.resend.com'
KEY_FILE = os.path.expanduser('~/.config/resend/claude-code-local.key')
FROM = 'AI Chef Pro <hola@news.aichef.pro>'
REPLY_TO = 'info@aichef.pro'
SEGMENT_AICP_ES = 'b2c581bd-81db-4ded-a174-2b339f7d3cc3'


def leer_key():
    """Credencial de la cuenta Resend del grupo. Orden: RESEND_API_KEY en el entorno →
    ~/.config/resend/claude-code-local.key → RESEND_API_KEY de ~/michelin-leads/.env
    (la key de AI Chef que ya usan las sesiones de prospección; skill local
    .claude/skills/resend-aichef/SKILL.md). Nunca se imprime."""
    k = os.environ.get('RESEND_API_KEY', '').strip()
    if not k and os.path.exists(KEY_FILE):
        k = open(KEY_FILE, encoding='utf-8').read().strip()
    if not k:
        env = os.path.expanduser('~/michelin-leads/.env')
        if os.path.exists(env):
            m = re.search(r'^RESEND_API_KEY\s*=\s*"?([^"\n]+)"?', open(env, encoding='utf-8').read(), re.M)
            k = m.group(1).strip() if m else ''
    if not k.startswith('re_'):
        sys.exit('sin credencial de Resend (ver docstring de leer_key)')
    return k


def http(method, path, key, body=None):
    """curl, no urllib: el python de este Mac falla el handshake TLS (skill generate-images)."""
    import subprocess, tempfile
    cmd = ['curl', '-s', '-o', '-', '-w', '\n%{http_code}', '-X', method, API + path,
           '-H', 'Authorization: Bearer ' + key, '-H', 'Content-Type: application/json']
    tmp = None
    if body is not None:
        tmp = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8')
        json.dump(body, tmp, ensure_ascii=False); tmp.close()
        cmd += ['--data-binary', '@' + tmp.name]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    if tmp:
        os.unlink(tmp.name)
    cuerpo, _, status = out.rpartition('\n')
    try:
        data = json.loads(cuerpo or '{}')
    except json.JSONDecodeError:
        data = {'raw': cuerpo[:300]}
    return int(status or 0), data


def vivo(url):
    import subprocess
    out = subprocess.run(['curl', '-s', '-I', '-o', '/dev/null', '-w', '%{http_code} %{content_type}',
                          '-A', 'aichef-broadcast-gate', url], capture_output=True, text=True, timeout=60).stdout
    st, _, ct = out.partition(' ')
    return int(st or 0), ct


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
