#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulta DataForSEO: volúmenes de búsqueda (Google Ads) y SERP orgánica en vivo.

POR QUÉ EXISTE: la REGLA CAPITAL exige keyword research + análisis SERP antes de
escribir una sola línea, y DataForSEO es la única fuente contratada que sirve
datos (Keywords Everywhere devuelve 0 hasta para «pizza» y la API de Brave da
401/422 — ver `CLAUDE.md`). No había helper en este repo ni en `chefbusiness-ai`,
así que cada sesión lo reescribía desde cero.

CREDENCIALES: nunca aquí. Salen de `DATAFORSEO_LOGIN` (email) y
`DATAFORSEO_PASSWORD` (la *API password* del panel, no la del login) del `.env`
de `chefbusiness-ai`, que está fuera de este repo —que es PÚBLICO— y gitignorado.
Se puede apuntar a otro fichero con la variable de entorno DATAFORSEO_ENV.

Uso:
    python3 scripts/dataforseo.py vol "que es un token" "token ia" ...
    python3 scripts/dataforseo.py serp "que es un llm"
    python3 scripts/dataforseo.py serp "best ai for chefs" --pais 2826 --idioma en

QUÉ MIRAR EN LA SALIDA, por si sirve de recordatorio:
  · El VOLUMEN de la keyword genérica miente si la intención no es la tuya. «qué
    es un token» son 1.600/mes de CRIPTOMONEDAS: la SERP lo dijo, el volumen no.
  · Si hay `ai_overview`, cada sección del post debe abrir con una respuesta
    directa y citable en 1-2 frases.
  · El People Also Ask es el guion de la FAQ, y las búsquedas relacionadas
    delatan las ambigüedades (LLM → «LLM en Derecho»).
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Rutas del `.env` por máquina (este repo se trabaja desde el Mac y desde el VPS).
ENV_CANDIDATOS = [
    Path(os.environ['DATAFORSEO_ENV']) if os.environ.get('DATAFORSEO_ENV') else None,
    Path('/root/chefbusiness-ai/.env'),                        # VPS
    Path.home() / 'chefbusiness-ai' / '.env',                  # Mac
]

LOC_ES, LANG_ES = 2724, 'es'   # España / español


def credenciales():
    if os.environ.get('DATAFORSEO_LOGIN') and os.environ.get('DATAFORSEO_PASSWORD'):
        login, pwd = os.environ['DATAFORSEO_LOGIN'], os.environ['DATAFORSEO_PASSWORD']
    else:
        ruta = next((p for p in ENV_CANDIDATOS if p and p.is_file()), None)
        if not ruta:
            sys.exit('no encuentro el .env con las credenciales; probé: %s'
                     % ', '.join(str(p) for p in ENV_CANDIDATOS if p))
        vals = {}
        for linea in ruta.read_text(encoding='utf-8').splitlines():
            if linea.strip().startswith(('DATAFORSEO_LOGIN=', 'DATAFORSEO_PASSWORD=')):
                k, v = linea.strip().split('=', 1)
                vals[k] = v.strip().strip('"\'')
        login, pwd = vals.get('DATAFORSEO_LOGIN'), vals.get('DATAFORSEO_PASSWORD')
        if not (login and pwd):
            sys.exit('faltan DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD en %s' % ruta)
    return base64.b64encode(('%s:%s' % (login, pwd)).encode()).decode()


def post(ruta, payload):
    req = urllib.request.Request(
        'https://api.dataforseo.com/v3/' + ruta,
        data=json.dumps(payload).encode(),
        headers={'Authorization': 'Basic ' + credenciales(),
                 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit('HTTP %s de DataForSEO: %s' % (e.code, e.read()[:300].decode('utf-8', 'replace')))
    tarea = (d.get('tasks') or [{}])[0]
    if tarea.get('status_code') != 20000:
        sys.exit('DataForSEO: %s' % tarea.get('status_message'))
    return tarea


def volumen(kws, loc, lang):
    tarea = post('keywords_data/google_ads/search_volume/live',
                 [{'keywords': kws, 'location_code': loc,
                   'language_code': lang, 'sort_by': 'search_volume'}])
    print('%-52s %9s %8s  %s' % ('KEYWORD', 'VOL/MES', 'COMP', 'ÚLTIMOS 6 MESES'))
    print('-' * 100)
    for it in tarea.get('result') or []:
        meses = it.get('monthly_searches') or []
        serie = ', '.join(str(m['search_volume']) for m in meses[:6])
        print('%-52s %9s %8s  %s' % (it['keyword'], it.get('search_volume'),
                                     it.get('competition') or '-', serie))
    print('\n⚠️  El volumen no dice la INTENCIÓN. Confírmala con `serp` antes de escribir.')


def serp(kw, loc, lang):
    tarea = post('serp/google/organic/live/advanced',
                 [{'keyword': kw, 'location_code': loc, 'language_code': lang,
                   'device': 'desktop', 'depth': 20, 'people_also_ask_click_depth': 2}])
    res = (tarea.get('result') or [{}])[0]
    items = res.get('items') or []
    tipos = {}
    for it in items:
        tipos[it['type']] = tipos.get(it['type'], 0) + 1
    print('### SERP «%s» — %s resultados' % (kw, res.get('se_results_count')))
    print('### Bloques: %s' % json.dumps(tipos, ensure_ascii=False))
    if 'ai_overview' in tipos:
        print('### ⚠️ HAY AI OVERVIEW: cada sección debe abrir con una respuesta citable.\n')
    for it in items:
        t = it['type']
        if t == 'organic':
            print('%2s. %s\n    %s' % (it.get('rank_group'), it.get('title'), it.get('url')))
            if it.get('description'):
                print('    %s' % it['description'][:180])
        elif t == 'people_also_ask':
            print('\n--- PEOPLE ALSO ASK (el guion de tu FAQ) ---')
            for q in it.get('items') or []:
                print('  ? %s' % q.get('title'))
        elif t in ('ai_overview', 'featured_snippet'):
            print('\n--- %s ---' % t.upper())
            print('   ', (it.get('markdown') or json.dumps(it, ensure_ascii=False))[:600])
        elif t == 'related_searches':
            print('\n--- RELACIONADAS (delatan ambigüedades) ---')
            print('   ', ' · '.join(it.get('items') or []))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('modo', choices=['vol', 'serp'])
    ap.add_argument('keywords', nargs='+')
    ap.add_argument('--pais', type=int, default=LOC_ES, help='location_code (2724=ES, 2826=UK, 2840=US)')
    ap.add_argument('--idioma', default=LANG_ES, help='language_code (es, en, fr…)')
    a = ap.parse_args()
    if a.modo == 'vol':
        volumen(a.keywords, a.pais, a.idioma)
    else:
        serp(a.keywords[0], a.pais, a.idioma)
