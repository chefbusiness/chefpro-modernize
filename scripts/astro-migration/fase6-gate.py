#!/usr/bin/env python3
"""
Fase 6 — Gate completo: marketing/legales portados + sitemap paridad exacta +
llms.txt + lang-redirect + schemas globales + rich results + anti-regresión.

Uso: python3 scripts/astro-migration/fase6-gate.py [BASE_URL]
     BASE_URL default: https://aichef-astro-staging.netlify.app
Fetch vía curl (Python de macOS sin CA certs — gotcha 2026-07-19).
"""
import hashlib
import html as html_mod
import json
import pathlib
import re
import subprocess
import sys
import time
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = sys.argv[1] if len(sys.argv) > 1 else 'https://aichef-astro-staging.netlify.app'
UA_BOT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
UA_HUMAN = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
SITE = 'https://aichef.pro'

failures = []
checked = 0


def check(cond, label):
    global checked
    checked += 1
    if not cond:
        failures.append(label)
        print(f'  ❌ {label}')


def curl(url, ua=UA_BOT, extra=None, attempts=4):
    for i in range(attempts):
        cmd = ['curl', '-s', '-A', ua, '--max-time', '30',
               '-w', '\n__HTTP__%{http_code}__LOC__%{redirect_url}']
        if extra:
            cmd += extra
        r = subprocess.run(cmd + [url], capture_output=True, text=True)
        body, sep, tail = r.stdout.rpartition('\n__HTTP__')
        if sep:
            code, _, loc = tail.partition('__LOC__')
            if code.strip().isdigit() and code.strip() != '000':
                return int(code.strip()), body, loc.strip()
        time.sleep(2 * (i + 1))
    return 0, '', ''


def title_of(h):
    m = re.search(r'<title>([^<]*)</title>', h)
    return html_mod.unescape(m.group(1)) if m else None


def desc_of(h):
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    return html_mod.unescape(m.group(1)) if m else None


# ── Resolución independiente de claves i18n (NO usa translations.ts)
DICTS = {l: json.loads((ROOT / f'src/i18n/locales/{l}.json').read_text()) for l in LANGS}


def resolve_key(lang, key):
    for d in (DICTS[lang], DICTS['es']):
        cur = d
        ok = True
        for part in key.split('.'):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break
        if ok and isinstance(cur, str):
            return cur
    return None


def expected_from_module(kebab, field, lang):
    """title/description esperado si el head module usa un t() simple."""
    src = (ROOT / f'astro-site/src/lib/marketing-heads/{kebab}.ts').read_text()
    m = re.search(rf"{field}:\s*t\(lang,\s*'([^']+)'\)", src)
    return resolve_key(lang, m.group(1)) if m else None


def schema_types(h):
    types = set()
    ok_json = True
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            data = json.loads(html_mod.unescape(m.group(1)))
        except ValueError:
            ok_json = False
            continue
        items = data if isinstance(data, list) else [data]
        for it in items:
            if isinstance(it, dict) and '@type' in it:
                types.add(it['@type'])
    return types, ok_json


def check_marketing_page(entry, lang, path, is_alias=False):
    st, h, _ = curl(BASE + path)
    check(st == 200, f'{path}: HTTP {st}')
    if st != 200:
        return
    kebab = entry['kebab']
    # title / description: exacto si el módulo es t() simple; sanidad si no
    exp_t = expected_from_module(kebab, 'title', lang)
    got_t = title_of(h)
    if exp_t:
        check(got_t == exp_t, f'{path}: title {got_t!r} != {exp_t!r}')
    else:
        check(bool(got_t) and len(got_t) > 10 and 'undefined' not in got_t
              and not re.match(r'^[a-zA-Z.]+$', got_t),
              f'{path}: title sospechoso {got_t!r}')
    exp_d = expected_from_module(kebab, 'description', lang)
    got_d = desc_of(h)
    if exp_d:
        check(got_d == exp_d, f'{path}: description no coincide')
    else:
        check(bool(got_d) and len(got_d) > 20, f'{path}: description sospechosa {got_d!r}')
    # canonical
    if entry['kind'] == 'marketing':
        exp_canon = SITE + entry['alternates'][lang]
    else:
        bp = entry['basePath']
        exp_canon = SITE + (bp if lang == 'es' else f'/{lang}{bp}')
    m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    check(bool(m) and m.group(1) == exp_canon,
          f'{path}: canonical {m.group(1) if m else None!r} != {exp_canon!r}')
    # hreflang ×8 (7 idiomas + x-default)
    n_hl = len(re.findall(r'hreflang="', h))
    check(n_hl == 8, f'{path}: hreflang {n_hl} != 8')
    # sin noindex (páginas indexables; el noindex de staging va por cabecera)
    check('noindex' not in h, f'{path}: meta noindex inesperado')
    # island montado + chunk servido
    check('<astro-island' in h, f'{path}: sin astro-island')
    mc = re.search(r'component-url="([^"]+)"', h)
    check(bool(mc), f'{path}: sin component-url')
    if mc:
        cst, _, _ = curl(BASE + mc.group(1))
        check(cst == 200, f'{path}: chunk {mc.group(1)} HTTP {cst}')
    # JSON-LD: parsea + globales presentes
    types, ok_json = schema_types(h)
    check(ok_json, f'{path}: JSON-LD inválido (no parsea)')
    for t_ in ['Organization', 'WebSite', 'SoftwareApplication']:
        check(t_ in types, f'{path}: falta schema global {t_}')
    # schemas propios: si el módulo declara FAQPage/BreadcrumbList deben salir
    mod_src = (ROOT / f'astro-site/src/lib/marketing-heads/{kebab}.ts').read_text()
    for t_ in ['FAQPage', 'BreadcrumbList']:
        if f"'{t_}'" in mod_src:
            check(t_ in types, f'{path}: falta schema propio {t_}')


def main():
    registry = json.loads((ROOT / 'astro-site/src/lib/marketing-pages.json').read_text())
    assert len(registry) == 22

    print(f'== Gate Fase 6 contra {BASE} ==')

    print('-- A. Marketing + legales (155 URLs)')
    for e in registry:
        print(f'   {e["component"]}')
        if e['kind'] == 'marketing':
            pairs = [(l, e['alternates'][l]) for l in LANGS]
            pairs += [(a.strip('/').split('/')[0], a) for a in e['aliasRoutes']]
        else:
            bp = e['basePath']
            pairs = [('es', bp)] + [(l, f'/{l}{bp}') for l in LANGS if l != 'es']
        for lang, path in pairs:
            time.sleep(0.05)
            check_marketing_page(e, lang, path)

    # alias canonical → primario EN
    alias_entry = next(e for e in registry if e['aliasRoutes'])
    _, h, _ = curl(BASE + alias_entry['aliasRoutes'][0])
    check(f'<link rel="canonical" href="{SITE}{alias_entry["alternates"]["en"]}"' in h,
          'alias: canonical no apunta al primario EN')

    print('-- B. Sitemap: diff EXACTO vs producción LIVE')
    _, prod_xml, _ = curl(f'{SITE}/sitemap.xml')
    prod = {}
    for blk in re.findall(r'<url>(.*?)</url>', prod_xml, re.S):
        lm_ = re.search(r'<loc>([^<]+)</loc>', blk)
        lmod = re.search(r'<lastmod>([^<]+)</lastmod>', blk)
        if lm_:
            p = urlparse(lm_.group(1).strip()).path.rstrip('/') or '/'
            prod[p] = lmod.group(1) if lmod else None
    _, idx, _ = curl(f'{BASE}/sitemap-index.xml')
    stg = {}
    for part in re.findall(r'<loc>([^<]+)</loc>', idx):
        _, px, _ = curl(BASE + urlparse(part).path)
        for blk in re.findall(r'<url>(.*?)</url>', px, re.S):
            lm_ = re.search(r'<loc>([^<]+)</loc>', blk)
            lmod = re.search(r'<lastmod>([^<]+)</lastmod>', blk)
            if lm_:
                p = urlparse(lm_.group(1).strip()).path.rstrip('/') or '/'
                stg[p] = lmod.group(1) if lmod else None
    lost = set(prod) - set(stg)
    new = set(stg) - set(prod)
    exp_lost = {'/services'} | {f'/{l}/services' for l in LANGS if l != 'es'}
    check(lost == exp_lost,
          f'sitemap: perdidas {sorted(lost ^ exp_lost)} (esperado SOLO /services ×7)')
    check(len(new) == 45, f'sitemap: nuevas {len(new)} != 45 (productos)')
    check(all(p.count("/") == 1 for p in new),
          'sitemap: URLs nuevas con path inesperado (no producto raíz)')
    check('/productos-digitales' in new, 'sitemap: falta /productos-digitales')
    for p in ['/legales', '/en/ai-food-cost-calculator', '/admin/generar-acceso']:
        check(p not in stg, f'sitemap: {p} NO debería estar')
    check(re.search(r'-access</loc>|-library</loc>', str(sorted(stg))) is None,
          'sitemap: fuga -access/-library')
    no_lm = [p for p, v in stg.items() if not v]
    check(not no_lm, f'sitemap: {len(no_lm)} URLs sin lastmod')
    # @astrojs/sitemap emite W3C datetime completo (2026-03-02T00:00:00.000Z);
    # prod emite fecha pelada. Se compara la FECHA (semánticamente idéntico,
    # Google acepta ambos formatos).
    same = [p for p in list(prod)[:200]
            if p in stg and prod[p] and (stg[p] or '')[:10] != prod[p][:10]]
    check(not same, f'sitemap: lastmod (fecha) difiere de prod en {same[:5]}')

    print('-- C. llms.txt')
    for f in ['llms.txt', 'llms-full.txt']:
        st, body, _ = curl(f'{BASE}/{f}')
        local = (ROOT / 'astro-site/public' / f).read_bytes()
        check(st == 200, f'/{f}: HTTP {st}')
        check(hashlib.sha1(body.encode()).hexdigest() ==
              hashlib.sha1(local).hexdigest(), f'/{f}: contenido != repo')

    print('-- D. /sitemap.xml → 301 sitemap-index')
    st, _, loc = curl(f'{BASE}/sitemap.xml', extra=['-o', '/dev/null'])
    check(st == 301 and loc.endswith('/sitemap-index.xml'),
          f'/sitemap.xml: {st} → {loc!r} (esperado 301 a sitemap-index.xml)')

    print('-- E. lang-redirect en staging')
    st, _, loc = curl(BASE + '/', ua=UA_HUMAN, extra=['-H', 'Accept-Language: fr-FR,fr;q=0.9'])
    check(st == 302 and loc.endswith('/fr'), f'/: humano AL=fr → {st} {loc!r} (esperado 302 /fr)')
    st, _, _ = curl(BASE + '/', ua=UA_BOT)
    check(st == 200, f'/: Googlebot → {st} (esperado 200, sin redirect)')
    st, _, _ = curl(BASE + '/?nolang=1', ua=UA_HUMAN, extra=['-H', 'Accept-Language: fr'])
    check(st == 200, f'/?nolang=1 → {st} (esperado 200)')
    st, _, loc = curl(BASE + '/', ua=UA_HUMAN,
                      extra=['-H', 'Accept-Language: fr', '-H', 'Cookie: preferred-lang=de'])
    check(st == 302 and loc.endswith('/de'), f'/: cookie de → {st} {loc!r} (esperado 302 /de)')

    print('-- F. Rich results (muestras)')
    _, h, _ = curl(BASE + '/')
    types, okj = schema_types(h)
    check(okj and {'Organization', 'WebSite', 'SoftwareApplication'} <= types,
          f'home: schemas globales {sorted(types)}')
    _, h, _ = curl(BASE + '/usos/rol/sous-chef')
    types, okj = schema_types(h)
    check(okj and 'FAQPage' in types, f'spoke: FAQPage no presente ({sorted(types)})')
    _, h, _ = curl(BASE + '/kit-tareas-asador')
    types, okj = schema_types(h)
    check(okj and 'Product' in types, f'kit landing: Product no presente ({sorted(types)})')

    print('-- G. Anti-regresión')
    _, home, _ = curl(BASE + '/')
    check('AI Chef Pro' in (title_of(home) or ''), 'home: title roto')
    check(len(re.findall(r'hreflang="', home)) == 8, 'home: hreflang != 8')
    for p in ['/usos', '/kit-tareas-asador', '/en', '/abrir-restaurante/madrid']:
        st, _, _ = curl(BASE + p)
        check(st == 200, f'{p}: HTTP {st} (regresión)')
    # Quirk Fase 5: el gate del eBook es /pro-prompts-library-access (D6).
    st, h, _ = curl(BASE + '/pro-prompts-library-access')
    check(st == 200 and 'noindex' in h and 'rel="canonical"' not in h,
          'zona app: gate access alterado (regresión Fase 5)')

    print()
    if failures:
        print(f'❌ GATE FASE 6: {len(failures)} fallos de {checked} checks')
        sys.exit(1)
    print(f'✅ GATE FASE 6 VERDE: {checked} checks, 0 fallos')


if __name__ == '__main__':
    main()
