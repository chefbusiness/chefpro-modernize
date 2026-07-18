#!/bin/bash
# Regenera los inputs que necesitan los gates (se ejecuta DESDE esta carpeta o con path absoluto).
# 1) Listas canónicas de URLs desde el sitemap de la SPA. 2) Payment links desde la API de Netlify.
export PATH="$PATH:/usr/local/bin:/opt/homebrew/bin:$HOME/.nvm/versions/node/current/bin"
cd "$(dirname "$0")"
REPO="$(cd ../.. && pwd)"

python3 - <<EOF
import re, collections
xml = open('$REPO/public/sitemap.xml').read()
urls = [u.replace('https://aichef.pro','') for u in re.findall(r'<loc>\s*(https://aichef\.pro[^<\s]*)\s*</loc>', xml, re.DOTALL)]

# Use cases (441 = 7 idiomas x 63)
hubs = {'es':'usos','en':'use-cases','fr':'cas-d-usage','de':'anwendungsfaelle','it':'casi-uso','pt':'casos-uso','nl':'use-cases'}
uc = []
for u in urls:
    for lang, hub in hubs.items():
        p = f'/{hub}' if lang=='es' else f'/{lang}/{hub}'
        if u == p or u.startswith(p + '/'): uc.append(u); break
open('expected-use-case-urls.txt','w').write('\n'.join(sorted(set(uc))))
print('use cases:', len(set(uc)), '(esperado 441)')

# pSEO ciudades (76 = hub + 15 ciudades x 5 modifiers)
mods = ['abrir-restaurante','licencia-restaurante','software-gestion-restaurante','escandallo-restaurante','plan-negocio-restaurante']
city = [u for u in urls if u == '/seo-restaurantes-por-ciudad' or any(u.startswith('/'+m+'/') for m in mods)]
open('expected-city-urls.txt','w').write('\n'.join(sorted(city)))
print('pSEO ciudades:', len(city), '(esperado 76)')
EOF

# Payment links (NO se commitean — .gitignore de esta carpeta) desde el site de PRODUCCIÓN
ACC=$(netlify api getSite --data '{"site_id":"ee5802cf-34bb-4354-90d9-aa9f628b4038"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['account_slug'])")
netlify api getEnvVars --data "{\"accountId\":\"$ACC\",\"siteId\":\"ee5802cf-34bb-4354-90d9-aa9f628b4038\"}" | python3 -c "
import json,sys
env=json.load(sys.stdin)
data={}
for e in env:
    if e['key'].startswith('VITE_STRIPE_PAYMENT_LINK'):
        v=[x for x in e.get('values',[]) if x.get('context') in ('all','production')]
        data[e['key']]={'value': (v[0]['value'] if v else None), 'scopes': e.get('scopes')}
open('stripe-env-vars.json','w').write(json.dumps(data,indent=1))
print('payment links:', len(data), '(esperado 44)')"
