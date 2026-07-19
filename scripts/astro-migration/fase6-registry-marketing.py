#!/usr/bin/env python3
"""
Fase 6 — Registry de las páginas marketing/legales que faltan en Astro.

Extrae VERBATIM (la SPA es la spec):
  - rutas por componente de src/App.tsx (<Route path element>)
  - LANG_SLUGS del propio componente (normalizados a path con / inicial)
Cross-checks que ABORTAN:
  - rutas App.tsx == LANG_SLUGS normalizados (los extras se registran como
    aliasRoutes y solo se admite el conocido /en/ai-food-cost-calculator)
  - cada path de marketing existe en el sitemap de producción LIVE
    (fichero prod-paths.txt generado por el censo; los legales NO están en el
    sitemap de prod → se comprueba su AUSENCIA, quedarán excluidos del de Astro)

Salida: astro-site/src/lib/marketing-pages.json (consumido por el generador
fase6-generate-marketing.py y por el gate).

Uso: python3 scripts/astro-migration/fase6-registry-marketing.py PROD_PATHS_TXT
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']

MARKETING = [
    'CalculadoraBrigada', 'CalculadoraFoodCost', 'CalendarioContenidos',
    'ChatGPTRestaurantes', 'DetectorAlergenos', 'EscandallosRestaurante',
    'GeneradorMenuDegustacion', 'GeneradorTextosCarta', 'HerramientasGratuitas',
    'HerramientasIARestaurantes', 'MarketingRestaurante', 'MenuRestaurante',
    'RecetasIARestaurantes', 'ReducirCostesRestaurante', 'SimuladorRentabilidad',
    'SoftwareGestionCocina', 'TestDigitalizacion',
]
LEGAL = ['Legal', 'Cookies', 'Privacy', 'Terms', 'SistemaCreditos']
KNOWN_ALIASES = {'/en/ai-food-cost-calculator'}


def kebab(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def die(msg):
    print(f'❌ ABORT: {msg}')
    sys.exit(1)


def norm_slug(raw, lang):
    """'calculadora-x' | 'en/y' | '/en/y' → path canónico '/...' """
    s = raw.strip().strip('/')
    if lang != 'es' and not s.startswith(f'{lang}/'):
        s = f'{lang}/{s}'
    return '/' + s


def main():
    prod_paths = set(pathlib.Path(sys.argv[1]).read_text().split())

    app = (ROOT / 'src/App.tsx').read_text()
    route_re = re.compile(r'<Route\s+path="([^"]+)"\s+element=\{<(\w+)')
    comp_routes = {}
    for path, comp in route_re.findall(app):
        comp_routes.setdefault(comp, []).append(path)

    registry = []

    for name in MARKETING:
        src = (ROOT / 'src/pages' / f'{name}.tsx').read_text()
        m = re.search(r'const LANG_SLUGS[^=]*=\s*\{([^}]*)\}', src, re.S)
        if not m:
            die(f'{name}: sin LANG_SLUGS')
        entries = re.findall(r"(\w+):\s*'([^']+)'", m.group(1))
        slugs = {l: norm_slug(v, l) for l, v in entries}
        if sorted(slugs) != sorted(LANGS):
            die(f'{name}: LANG_SLUGS idiomas {sorted(slugs)} != {sorted(LANGS)}')

        routes = comp_routes.get(name)
        if not routes:
            die(f'{name}: sin rutas en App.tsx')
        # Rutas concretas del componente (las :lang no aplican a marketing: todas
        # sus rutas son literales en App.tsx)
        concrete = [r for r in routes if ':' not in r]
        if len(concrete) != len(routes):
            die(f'{name}: rutas con parámetros inesperadas: {routes}')

        slug_set = set(slugs.values())
        route_set = set(concrete)
        aliases = route_set - slug_set
        missing = slug_set - route_set
        if missing:
            die(f'{name}: LANG_SLUGS sin ruta en App.tsx: {sorted(missing)}')
        if aliases - KNOWN_ALIASES:
            die(f'{name}: rutas extra no registradas: {sorted(aliases - KNOWN_ALIASES)}')

        # Cross-check sitemap prod: todas las URLs de marketing están
        not_in_sitemap = slug_set - prod_paths
        if not_in_sitemap:
            die(f'{name}: paths fuera del sitemap de prod: {sorted(not_in_sitemap)}')

        registry.append({
            'component': name,
            'kind': 'marketing',
            'kebab': kebab(name),
            'alternates': slugs,           # lang -> path (BaseLayout alternates)
            'aliasRoutes': sorted(aliases),  # páginas extra: canonical al primario
            'inSitemap': True,
        })

    for name in LEGAL:
        routes = comp_routes.get(name)
        if not routes:
            die(f'{name}: sin rutas en App.tsx')
        base = [r for r in routes if ':' not in r]
        langv = [r for r in routes if r.startswith('/:lang/')]
        if len(base) != 1 or len(langv) != 1:
            die(f'{name}: esperaba 1 ruta base + 1 /:lang/, hay: {routes}')
        base_path = base[0]
        if langv[0] != f'/:lang{base_path}':
            die(f'{name}: ruta :lang {langv[0]} no casa con base {base_path}')
        in_sitemap = {base_path} | {f'/{l}{base_path}' for l in LANGS if l != 'es'}
        overlap = in_sitemap & prod_paths
        if overlap:
            die(f'{name}: legal presente en sitemap prod (inesperado): {overlap}')
        registry.append({
            'component': name,
            'kind': 'legal',
            'kebab': kebab(name),
            'basePath': base_path,         # mismo slug en los 7 idiomas
            'aliasRoutes': [],
            'inSitemap': False,
        })

    out = ROOT / 'astro-site/src/lib/marketing-pages.json'
    out.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n')
    n_urls = sum(len(LANGS) + len(e['aliasRoutes']) for e in registry)
    print(f'✅ Registry: {len(registry)} componentes → {n_urls} URLs → {out}')
    for e in registry:
        extra = f' (+alias {e["aliasRoutes"]})' if e['aliasRoutes'] else ''
        print(f'   {e["component"]:28s} {e["kind"]:9s}{extra}')


if __name__ == '__main__':
    main()
