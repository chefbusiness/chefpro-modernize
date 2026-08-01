#!/usr/bin/env python3
"""
Fase 6 — Generador determinista de las páginas marketing/legales de Astro.

Entrada:  astro-site/src/lib/marketing-pages.json (registry con cross-checks,
          generado por fase6-registry-marketing.py) + head-modules en
          astro-site/src/lib/marketing-heads/<kebab>.ts (workflow Opus).
Salida:   22 island wrappers (astro-site/src/islands/marketing/) +
          155 páginas .astro (astro-site/src/pages/...).

Aborta si: falta un head-module, una página destino ya existe (colisión),
o el registry no cuadra. Modo --check: no escribe, solo valida.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASTRO = ROOT / 'astro-site/src'
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
CHECK = '--check' in sys.argv
# --force reescribe lo ya generado: necesario para propagar un cambio de molde
# (p.ej. el paso de client:only a SSR de 2026-08-01) a las 155 páginas.
FORCE = '--force' in sys.argv

registry = json.loads((ASTRO / 'lib/marketing-pages.json').read_text())
assert len(registry) == 22, f'registry: {len(registry)} entradas'

written = []


def write(path: pathlib.Path, content: str):
    if path.exists() and not FORCE:
        sys.exit(f'❌ ABORT: colisión, ya existe {path}')
    if not CHECK:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    written.append(path)


def rel(depth: int) -> str:
    return '../' * (depth + 1)


def page_astro(entry, lang: str, path: str) -> str:
    depth = path.strip('/').count('/')
    r = rel(depth)
    comp = entry['component']
    island = f'{comp}Island'
    if entry['kind'] == 'marketing':
        target = f'alternates={{{json.dumps(entry["alternates"], ensure_ascii=False)}}}'
        # Las 119 URLs indexables de marketing pasan por SSR desde 2026-08-01:
        # con client:only el HTML crudo salía con CERO texto visible. El island
        # necesita idioma y ubicación explícitos porque en servidor no hay window.
        montaje = 'client:load lang={lang} pathname={Astro.url.pathname}'
    else:
        target = f'basePath="{entry["basePath"]}"'
        # Legales: fuera del sitemap por decisión (D6, paridad con producción).
        montaje = 'client:only="react"'
    return f'''---
// GENERADO por scripts/astro-migration/fase6-generate-marketing.py — NO editar a mano.
// Fase 6: la página de la SPA (src/pages/{comp}.tsx) se monta como island (D5,
// patrón Fase 5); el head SEO sale server-side del head-module (claves i18n
// verbatim de la SPA — SEOHead/Helmet son la spec).
import BaseLayout from '{r}layouts/BaseLayout.astro';
import {{ SITE }} from '{r}i18n/config';
import {{ head }} from '{r}lib/marketing-heads/{entry["kebab"]}';
import {island} from '{r}islands/marketing/{island}';

const lang = '{lang}';
const h = head(lang);
---

<BaseLayout
  title={{h.title}}
  description={{h.description}}
  keywords={{h.keywords}}
  lang={{lang}}
  {target}
  ogImage={{`${{SITE}}${{h.ogImage ?? '/og-image.jpg'}}`}}
>
  {{h.schemas.map((s) => (
    <script type="application/ld+json" set:html={{JSON.stringify(s)}} />
  ))}}
  <{island} {montaje} />
</BaseLayout>
'''


def wrapper_tsx(entry) -> str:
    comp = entry['component']
    if entry['kind'] != 'marketing':
        return f'''// GENERADO por scripts/astro-migration/fase6-generate-marketing.py — NO editar a mano.
// Island full-page (Fase 6): reutiliza la página de la SPA TAL CUAL (D5, cero
// copias). El import de i18n/config inicializa i18next global como side effect
// ANTES de montar (en la SPA lo hace main.tsx). El idioma se sincroniza desde
// la URL por el propio useLanguage de la SPA (useParams del shim de router).
import '@/i18n/config';
export {{ default }} from '@/pages/{comp}';
'''
    return f'''// GENERADO por scripts/astro-migration/fase6-generate-marketing.py — NO editar a mano.
// Island full-page (Fase 6): reutiliza la página de la SPA TAL CUAL (D5, cero
// copias). El import de i18n/config inicializa i18next global como side effect
// ANTES de montar (en la SPA lo hace main.tsx).
// Desde 2026-08-01 pasa por SSR (client:load). MarketingShell hace las dos cosas
// que en el navegador se dan por supuestas y en servidor no: fijar el idioma
// —useLanguage lo sincroniza en un useEffect, que en SSR no corre, así que sin
// esto las seis versiones no españolas se renderizarían EN ESPAÑOL— e inyectar
// la ubicación, que el shim del router leía de window.
import '@/i18n/config';
import Page from '@/pages/{comp}';
import MarketingShell from '../MarketingShell';

export default function Island({{ lang, pathname }}: {{ lang: string; pathname: string }}) {{
  return (
    <MarketingShell lang={{lang}} pathname={{pathname}}>
      <Page />
    </MarketingShell>
  );
}}
'''


# 1) head-modules presentes
missing_heads = [e['kebab'] for e in registry
                 if not (ASTRO / 'lib/marketing-heads' / f'{e["kebab"]}.ts').is_file()]
if missing_heads:
    sys.exit(f'❌ ABORT: faltan head-modules: {missing_heads}')

# 2) wrappers + páginas
n_pages = 0
for e in registry:
    write(ASTRO / 'islands/marketing' / f'{e["component"]}Island.tsx', wrapper_tsx(e))
    if e['kind'] == 'marketing':
        pairs = [(l, e['alternates'][l]) for l in LANGS]
        for alias in e['aliasRoutes']:
            alias_lang = alias.strip('/').split('/')[0]
            pairs.append((alias_lang if alias_lang in LANGS else 'es', alias))
    else:
        bp = e['basePath']
        pairs = [('es', bp)] + [(l, f'/{l}{bp}') for l in LANGS if l != 'es']
    for lang, path in pairs:
        write(ASTRO / 'pages' / (path.strip('/') + '.astro'), page_astro(e, lang, path))
        n_pages += 1

mode = 'CHECK (nada escrito)' if CHECK else 'ESCRITO'
print(f'✅ {mode}: {len(registry)} wrappers + {n_pages} páginas '
      f'({len(written)} ficheros)')
