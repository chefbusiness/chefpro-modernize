#!/usr/bin/env python3
"""
Fase 5 — Gate S1+S2: verificación de las 88 URLs de zona app en staging.

Para cada uno de los 44 productos del registro (astro-site/src/lib/zona-app.ts):
  -access : 200 · title == ACCESS_TITLE · meta robots noindex server-side ·
            0 canonical/hreflang · astro-island presente · patch de functions
            inline presente · chunk JS del island en 200
  -library: 200 · title == <title> re-derivado del Helmet del dashboard de la
            SPA (derivación INDEPENDIENTE del generador) · noindex · island ·
            patch · chunk 200

Extra: robots.txt con los Disallow en los 5 grupos · sitemap sin -access/-library ·
anti-regresión (home, landing Fase 4, spoke Fase 2).

Uso: python3 scripts/astro-migration/fase5-gate-s1-s2.py [BASE_URL]
     BASE_URL default: https://aichef-astro-staging.netlify.app
"""
import html as html_mod
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = sys.argv[1] if len(sys.argv) > 1 else 'https://aichef-astro-staging.netlify.app'
UA = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
ACCESS_TITLE = 'Verificando acceso... | AI Chef Pro'

ENTRY_RE = re.compile(
    r"\{ productId: '([^']+)', accessPath: '([^']+)', libraryPath: '([^']+)'")

failures = []
checked = 0


def fetch(path, attempts=4):
    """GET vía curl (NO urllib: el Python de esta máquina no tiene los CA
    certificates de macOS → CERTIFICATE_VERIFY_FAILED intermitente/total,
    visto 2026-07-19; curl usa el trust store del sistema). Con reintentos."""
    for i in range(attempts):
        r = subprocess.run(
            ['curl', '-s', '-A', UA, '--max-time', '30',
             '-w', '\n__HTTP__%{http_code}', BASE + path],
            capture_output=True, text=True)
        body, sep, code = r.stdout.rpartition('\n__HTTP__')
        if sep and code.strip().isdigit() and code.strip() != '000':
            return int(code.strip()), body
        time.sleep(2 * (i + 1))
    print(f'  ⚠️  {path}: reintentos agotados (curl rc={r.returncode})')
    return 0, ''


def check(cond, label):
    global checked
    checked += 1
    if not cond:
        failures.append(label)
        print(f'  ❌ {label}')


def title_of(html):
    """Título del HTML crudo, DES-ESCAPADO: Astro emite 'F&B' como 'F&amp;B'
    (HTML correcto); se compara el TEXTO, no la serialización."""
    m = re.search(r'<title>([^<]*)</title>', html)
    return html_mod.unescape(m.group(1)) if m else None


def dash_title(component):
    src = (ROOT / 'src/pages' / f'{component}.tsx').read_text()
    titles = re.findall(r'<title>([^<]+)</title>', src)
    return titles[0] if len(titles) == 1 else None


def check_page(path, expected_title, kind):
    status, html = fetch(path)
    check(status == 200, f'{path}: HTTP {status}')
    if status != 200:
        return
    check(title_of(html) == expected_title,
          f'{path}: title {title_of(html)!r} != {expected_title!r}')
    check('<meta name="robots" content="noindex, nofollow"' in html,
          f'{path}: sin meta robots noindex server-side')
    check('rel="canonical"' not in html and 'hreflang' not in html,
          f'{path}: emite canonical/hreflang (no debe)')
    check('<astro-island' in html, f'{path}: sin astro-island')
    check('aichef-astro-staging.netlify.app' in html and '/.netlify/functions/' in html,
          f'{path}: patch de functions (FunctionsOriginPatch) no presente')
    m = re.search(r'component-url="([^"]+)"', html)
    check(bool(m), f'{path}: sin component-url en astro-island')
    if m:
        cst, _ = fetch(m.group(1))
        check(cst == 200, f'{path}: chunk {m.group(1)} HTTP {cst}')


def main():
    reg = (ROOT / 'astro-site/src/lib/zona-app.ts').read_text()
    entries = ENTRY_RE.findall(reg)
    assert len(entries) == 44, f'registro: {len(entries)} entradas'

    # dashboardComponent por productId (para re-derivar titles)
    dash_re = re.compile(r"\{ productId: '([^']+)'.*?dashboardComponent: '([^']+)'")
    dash_map = dict(dash_re.findall(reg))

    print(f'== Gate S1+S2 contra {BASE} ==')
    for pid, access, library in entries:
        print(f'-- {pid}')
        time.sleep(0.1)  # pacing: no martillear el CDN
        check_page(access, ACCESS_TITLE, 'access')
        exp = dash_title(dash_map[pid])
        check(exp is not None, f'{pid}: no pude re-derivar title del dashboard')
        if exp:
            check_page(library, exp, 'library')

    print('-- admin (S3)')
    check_page('/admin/generar-acceso', 'Admin: Generar Acceso Manual | AI Chef Pro', 'admin')

    print('-- robots.txt')
    st, robots = fetch('/robots.txt')
    check(st == 200, f'/robots.txt: HTTP {st}')
    for ua in ['Googlebot', 'Bingbot', 'Twitterbot', 'facebookexternalhit', '*']:
        block = re.search(
            rf'User-agent: {re.escape(ua)}\n(.*?)(?:\n\n|\Z)', robots, re.S)
        ok = block and all(d in block.group(1) for d in
                           ['Disallow: /*-access', 'Disallow: /*-library', 'Disallow: /admin/'])
        check(bool(ok), f'robots.txt: grupo {ua} sin los 3 Disallow')

    print('-- sitemap')
    sm = ''
    for smp in ['/sitemap-index.xml', '/sitemap-0.xml']:
        _, body = fetch(smp)
        sm += body
    check(re.search(r'-access</loc>|-library</loc>', sm) is None,
          'sitemap: contiene URLs -access/-library')

    print('-- anti-regresión')
    _, home = fetch('/')
    check('AI Chef Pro' in (title_of(home) or ''), 'home: title roto')
    check(home.count('hreflang=') == 8, f'home: hreflang {home.count("hreflang=")} != 8')
    st, l4 = fetch('/kit-tareas-asador')
    check(st == 200 and 'hreflang' in l4, '/kit-tareas-asador (landing F4): regresión')
    st, _ = fetch('/usos')
    check(st == 200, '/usos (hub F2): regresión')

    print()
    if failures:
        print(f'❌ GATE S1+S2: {len(failures)} fallos de {checked} checks')
        sys.exit(1)
    print(f'✅ GATE S1+S2 VERDE: {checked} checks, 0 fallos '
          f'(88 URLs × título/noindex/island/patch/chunk + robots + sitemap + anti-regresión)')


if __name__ == '__main__':
    main()
