#!/usr/bin/env python3
"""
Fase 7 — Vigilancia post-cutover de aichef.pro (hasta ~2026-08-16).

Chequeo de salud de PRODUCCIÓN vía curl (ligero, sin navegador):
  1. Home 200 + huella Astro (/_astro/) + meta robots index,follow
  2. verify-purchase same-origin → 400 unknown_product (dinero vivo)
  3. sitemap-index 200 con el nº de <loc> esperado (calculado del repo, los 6
     blogs incluidos) + /sitemap.xml → 301
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
#
# ⚠️ 2026-08-27: esto contaba SOLO el blog español y llevaba rojo de forma
# permanente desde que nacieron los blogs EN/IT/FR/DE/PT (decía 1.184 != 1.051).
# Una alarma siempre roja no avisa de nada — se generaliza a los 6 idiomas:
# por idioma, posts publicados + hub + páginas 2..n (POSTS_PER_PAGE = 24) + una
# archive por categoría CON posts (las vacías no se generan).
from pathlib import Path
_CONTENT = Path(__file__).resolve().parents[2] / 'astro-site/src/content/blog'
_blog_urls = 0
for _dir in sorted(p for p in _CONTENT.iterdir() if p.is_dir()):
    _txt = [f.read_text() for f in _dir.glob('*.md')]
    _txt = [t for t in _txt if not re.search(r'^draft:\s*true', t, re.M)]
    _n = len(_txt)
    _cats = {re.search(r'^category:\s*(\S+)', t, re.M).group(1) for t in _txt}
    _blog_urls += _n + 1 + max(0, -(-_n // 24) - 1) + len(_cats)
# F8: URLs nativas nuevas fuera del blog (mantener lista al día al crear páginas)
_F8_EXTRA = ['/precios', '/en/pricing', '/fr/tarifs', '/de/preise',
             '/it/prezzi', '/pt/precos', '/nl/prijzen',
             '/contacto', '/sobre-nosotros', '/faq',
             # 8C: los dos hubs de librerías de prompts (ES e EN)
             '/libreria-de-prompts', '/en/prompt-libraries']
EXPECTED = 696 + len(_F8_EXTRA) + _blog_urls
check(n == EXPECTED, f'sitemap: {n} URLs != {EXPECTED}')

st, robots = curl('/robots.txt')
# 2026-08-27: las reglas de la zona app van ancladas al PREFIJO de cada familia.
# El comodín suelto de antes bloqueaba /en/blog/prompt-library-… (26 posts).
check(st == 200 and 'Disallow: /kit-*-access' in robots
      and 'Disallow: /admin/' in robots, 'robots.txt alterado')

# 8B.5 cutover 2026-07-19: el subdominio blog debe 301-ear al path nuevo
# (TLS estricto: si el cert del subdominio caduca o se rompe, esto avisa).
#
# ⚠️ DETERMINISMO POR LOCALE (2026-07-28, VPS): en `/` la edge function
# lang-redirect se ejecuta ANTES que los redirects, así que un HUMANO con
# Accept-Language != es (o geo no-ES, p.ej. este VPS en Alemania) recibe
# 302 → blog.aichef.pro/{lang} y solo DESPUÉS el 301 al destino. La cadena
# termina bien y Googlebot recibe el 301 directo, pero el check original
# dependía de dónde corriera. Se fija UA de Googlebot (invariante SEO real)
# y se añade un check de que la cadena humana TERMINA en el destino.
GBOT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
for src, dst in [
    ('https://blog.aichef.pro/', 'https://aichef.pro/blog'),
    ('https://blog.aichef.pro/ia-para-cocinar', 'https://aichef.pro/blog/ia-para-cocinar'),
    ('https://blog.aichef.pro/wp-content/uploads/x.jpg', 'https://aichef.pro/blog-assets/x.jpg'),
]:
    r = subprocess.run(['curl', '-s', '-o', '/dev/null', '--max-time', '30',
                        '-A', GBOT, '-w', '%{http_code} %{redirect_url}', src],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    check(out == f'301 {dst}', f'subdominio {src} (Googlebot): {out!r} != 301 {dst}')

# La cadena de un humano (con lang-redirect por medio) debe acabar igualmente
# en el blog nuevo, en ≤3 saltos y sin bucles.
r = subprocess.run(['curl', '-s', '-o', '/dev/null', '--max-time', '30', '-L',
                    '--max-redirs', '3', '-A', 'Mozilla/5.0 (Macintosh)',
                    '-H', 'Accept-Language: de-DE,de;q=0.9',
                    '-w', '%{http_code} %{url_effective}',
                    'https://blog.aichef.pro/'], capture_output=True, text=True)
check(r.stdout.strip() == '200 https://aichef.pro/blog',
      f'subdominio cadena humana no-ES: {r.stdout.strip()!r} != 200 https://aichef.pro/blog')

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
