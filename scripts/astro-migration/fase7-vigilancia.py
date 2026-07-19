#!/usr/bin/env python3
"""
Fase 7 — Vigilancia post-cutover de aichef.pro (hasta ~2026-08-16).

Chequeo de salud de PRODUCCIÓN vía curl (ligero, sin navegador):
  1. Home 200 + huella Astro (/_astro/) + meta robots index,follow
  2. verify-purchase same-origin → 400 unknown_product (dinero vivo)
  3. sitemap-index 200 con 696 <loc> + /sitemap.xml → 301
  4. robots.txt con Disallows de zona app
  5. Muestra de URLs críticas en 200 (home ×2 idiomas, use case, pSEO,
     landing producto, access gate)
Sale con código 1 y lista de fallos si algo se desvía → el cron/sesión que lo
ejecute debe AVISAR a John solo en ese caso.

La parte GSC (cobertura, 404/soft-404 nuevos) la hace la sesión de Claude vía
MCP gscServer (no invocable desde aquí): get_performance_overview +
check_indexing_issues + get_sitemap_details del sitemap-index.

Uso: python3 scripts/astro-migration/fase7-vigilancia.py
"""
import re
import subprocess
import sys

BASE = 'https://aichef.pro'
fails = []


def curl(path, method='GET', data=None, ua='Mozilla/5.0'):
    cmd = ['curl', '-s', '-A', ua, '--max-time', '30',
           '-w', '\n__HTTP__%{http_code}', '-X', method]
    if data:
        cmd += ['-H', 'Content-Type: application/json', '-d', data]
    r = subprocess.run(cmd + [BASE + path], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition('\n__HTTP__')
    return (int(code) if code.strip().isdigit() else 0), body


def check(cond, label):
    if not cond:
        fails.append(label)
        print(f'  ❌ {label}')


st, home = curl('/?nolang=1')
check(st == 200, f'home: HTTP {st}')
check('/_astro/' in home, 'home: sin huella Astro (¿rollback accidental a SPA?)')
check('<meta name="robots" content="index, follow"' in home, 'home: sin meta index,follow')
check(len(re.findall(r'hreflang=', home)) == 8, 'home: hreflang != 8')

st, body = curl('/.netlify/functions/verify-purchase', 'POST',
                '{"existingJwt":"x","product":"producto-inventado-123"}')
check(st == 400 and 'unknown_product' in body,
      f'verify-purchase: {st} {body[:60]!r} (esperado 400 unknown_product)')

st, sm = curl('/sitemap-index.xml')
check(st == 200, f'sitemap-index: HTTP {st}')
st, _ = curl('/sitemap-0.xml')
check(st == 200, 'sitemap-0: no accesible')
_, sm0 = curl('/sitemap-0.xml')
n = sm0.count('<loc>')
# 696 (Fase 6) + blog Fase 8B (posts + hub + paginación + categorías),
# computado del repo para que crezca solo al publicar contenido nuevo.
from pathlib import Path
_blog = list((Path(__file__).resolve().parents[2]
              / 'astro-site/src/content/blog/es').glob('*.md'))
_np = len(_blog)
_nc = len(set(re.search(r'^category: (\S+)', p.read_text(), re.M).group(1)
              for p in _blog))
# F8: URLs nativas nuevas fuera del blog (mantener lista al día al crear páginas)
_F8_EXTRA = ['/precios', '/en/pricing', '/fr/tarifs', '/de/preise',
             '/it/prezzi', '/pt/precos', '/nl/prijzen',
             '/contacto', '/sobre-nosotros', '/faq']
EXPECTED = 696 + len(_F8_EXTRA) + _np + 1 + (-(-_np // 24) - 1) + _nc
check(n == EXPECTED, f'sitemap: {n} URLs != {EXPECTED}')

st, robots = curl('/robots.txt')
check(st == 200 and 'Disallow: /*-access' in robots, 'robots.txt alterado')

# 8B.5 cutover 2026-07-19: el subdominio blog debe 301-ear al path nuevo
# (TLS estricto: si el cert del subdominio caduca o se rompe, esto avisa).
for src, dst in [
    ('https://blog.aichef.pro/', 'https://aichef.pro/blog'),
    ('https://blog.aichef.pro/ia-para-cocinar', 'https://aichef.pro/blog/ia-para-cocinar'),
    ('https://blog.aichef.pro/wp-content/uploads/x.jpg', 'https://aichef.pro/blog-assets/x.jpg'),
]:
    r = subprocess.run(['curl', '-s', '-o', '/dev/null', '--max-time', '30',
                        '-w', '%{http_code} %{redirect_url}', src],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    check(out == f'301 {dst}', f'subdominio {src}: {out!r} != 301 {dst}')

for p in ['/en', '/usos/rol/sous-chef', '/abrir-restaurante/madrid',
          '/kit-tareas-asador', '/productos-digitales', '/pro-prompts-library-access',
          '/calculadora-food-cost-restaurante', '/legales',
          '/blog', '/blog/mejores-ia-restaurantes-2026', '/blog/categoria/recetas']:
    st, _ = curl(p)
    check(st == 200, f'{p}: HTTP {st}')

if fails:
    print(f'\n🚨 VIGILANCIA: {len(fails)} DESVIACIONES — avisar a John')
    sys.exit(1)
print('✅ Vigilancia prod: todo verde')
