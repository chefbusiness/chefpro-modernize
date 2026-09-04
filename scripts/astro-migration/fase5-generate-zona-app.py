#!/usr/bin/env python3
"""
Fase 5 — Generador determinista de la zona app post-pago en Astro.

Genera, para los 46 productos del registro astro-site/src/lib/zona-app.ts:
  - 46 páginas  astro-site/src/pages/<accessPath>.astro   (S1)
  - 46 wrappers astro-site/src/islands/library/<X>LibraryIsland.tsx (S2)
  - 46 páginas  astro-site/src/pages/<libraryPath>.astro  (S2)

Fuentes de verdad (se extrae VERBATIM, el registro solo indexa):
  - Props de ProtectedRoute (storageKey/redirectTo): src/App.tsx
  - <title> de cada dashboard: Helmet de src/pages/<Dashboard>.tsx
  - Los gates NO llevan props aquí: cada página importa el wrapper de la SPA
    (src/pages/*AccessGate.tsx) que ya trae su config hardcodeada.

Cross-checks (el script ABORTA si fallan):
  - 46 entradas en el registro; ficheros de gate y dashboard existen.
  - storageKey de App.tsx == storageKey del registro (46/46).
  - Exactamente 1 <title> por dashboard, sin comillas dobles.
  - pro-prompts: ProtectedRoute SIN props en App.tsx (defaults) — se replica igual.

Uso: python3 scripts/astro-migration/fase5-generate-zona-app.py [--check]
     --check: no escribe, solo verifica que lo generado coincide con lo que hay
              en disco (gate de regeneración byte-exacta).
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
REG = ROOT / 'astro-site/src/lib/zona-app.ts'
APP = ROOT / 'src/App.tsx'
SPA_PAGES = ROOT / 'src/pages'
OUT_PAGES = ROOT / 'astro-site/src/pages'
OUT_ISLANDS = ROOT / 'astro-site/src/islands/library'

CHECK = '--check' in sys.argv

ENTRY_RE = re.compile(
    r"\{ productId: '([^']+)', accessPath: '([^']+)', libraryPath: '([^']+)', "
    r"landingPath: '([^']+)', storageKey: '([^']+)', productLabel: '([^']+)', "
    r"gateComponent: '([^']+)', dashboardComponent: '([^']+)'"
)
FIELDS = ['productId', 'accessPath', 'libraryPath', 'landingPath',
          'storageKey', 'productLabel', 'gateComponent', 'dashboardComponent']

ACCESS_TPL = """---
// Fase 5 — access gate de {label} (GENERADO por scripts/astro-migration/
// fase5-generate-zona-app.py — editar el generador, no este fichero).
// Island client:only="react": el gate de la SPA se monta TAL CUAL (window/
// localStorage en cliente; sin pase SSR). Config de dinero: hardcodeada en el
// propio wrapper de la SPA. Title = ACCESS_TITLE verbatim del Helmet
// compartido (el shim de react-helmet-async anula el Helmet cliente).
import BaseLayout from '../layouts/BaseLayout.astro';
import FunctionsOriginPatch from '../components/FunctionsOriginPatch.astro';
import {{ ACCESS_TITLE }} from '../lib/zona-app';
import {gate} from '../../../src/pages/{gate}';
---

<BaseLayout title={{ACCESS_TITLE}} noindex>
  <FunctionsOriginPatch />
  <{gate} client:only="react" />
</BaseLayout>
"""

ISLAND_TPL_PROPS = """/**
 * Island de {lib} (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import {dash} from '../../../../src/pages/{dash}';

export default function {name}() {{
  return (
    <ProtectedRoute storageKey="{sk}" redirectTo="{rt}">
      <{dash} />
    </ProtectedRoute>
  );
}}
"""

ISLAND_TPL_DEFAULTS = """/**
 * Island de {lib} (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA: en App.tsx esta ruta usa
 * <ProtectedRoute> SIN props (defaults 'pro-prompts-jwt' / '/pro-prompts-ebook'
 * de ProtectedRoute.tsx) — se replica igual, sin hardcodear los defaults.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import {dash} from '../../../../src/pages/{dash}';

export default function {name}() {{
  return (
    <ProtectedRoute>
      <{dash} />
    </ProtectedRoute>
  );
}}
"""

LIBRARY_TPL = """---
// Fase 5 — dashboard post-pago de {label} (GENERADO por scripts/astro-migration/
// fase5-generate-zona-app.py — editar el generador, no este fichero).
// Island client:only="react": ProtectedRoute lee localStorage en render
// síncrono (ReferenceError bajo SSR) → sin pase SSR, igual que el shell SPA.
// Title verbatim del <title> del Helmet de {dash}.tsx (extraído por el generador).
// whatsapp={{false}}: el dashboard monta su PROPIO WhatsAppProductSupport (React,
// mensaje de soporte post-compra prerellenado). Sin esto saldría también el botón
// global que BaseLayout pinta desde 2026-09-03 y se verían DOS superpuestos.
import BaseLayout from '../layouts/BaseLayout.astro';
import FunctionsOriginPatch from '../components/FunctionsOriginPatch.astro';
import {island} from '../islands/library/{island}';
---

<BaseLayout title="{title}" noindex whatsapp={{false}}>
  <FunctionsOriginPatch />
  <{island} client:only="react" />
</BaseLayout>
"""


def fail(msg):
    print(f"❌ {msg}")
    sys.exit(1)


def extract_protected_props(app_src, library_path, product_id):
    """storageKey/redirectTo VERBATIM del <ProtectedRoute> de esta ruta en App.tsx."""
    needle = f'path="{library_path}"'
    idx = app_src.find(needle)
    if idx == -1:
        fail(f"{product_id}: ruta {library_path} no encontrada en App.tsx")
    if app_src.find(needle, idx + 1) != -1:
        fail(f"{product_id}: ruta {library_path} aparece más de una vez en App.tsx")
    window = app_src[idx: idx + 400]
    m = re.search(r'<ProtectedRoute\s+storageKey="([^"]+)"\s+redirectTo="([^"]+)"\s*>', window)
    if m:
        return m.group(1), m.group(2), False
    if re.search(r'<ProtectedRoute\s*>', window):
        return None, None, True
    fail(f"{product_id}: no se pudo extraer <ProtectedRoute ...> para {library_path}")


def extract_title(dash_component, product_id):
    f = SPA_PAGES / f'{dash_component}.tsx'
    if not f.exists():
        fail(f"{product_id}: no existe {f}")
    titles = re.findall(r'<title>([^<]+)</title>', f.read_text())
    if len(titles) != 1:
        fail(f"{product_id}: {dash_component}.tsx tiene {len(titles)} <title> (esperado 1)")
    if '"' in titles[0]:
        fail(f"{product_id}: el title contiene comillas dobles — ajustar plantilla")
    return titles[0]


def emit(path: pathlib.Path, content: str, changed: list, mismatches: list):
    if CHECK:
        if not path.exists():
            mismatches.append(f"FALTA {path}")
        elif path.read_text() != content:
            mismatches.append(f"DIFIERE {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != content:
        path.write_text(content)
        changed.append(str(path.relative_to(ROOT)))


def main():
    reg_src = REG.read_text()
    entries = [dict(zip(FIELDS, m.groups())) for m in ENTRY_RE.finditer(reg_src)]
    if len(entries) != 46:
        fail(f"registro: {len(entries)} entradas parseadas (esperado 46)")

    app_src = APP.read_text()
    changed, mismatches, notes = [], [], []

    for e in entries:
        pid = e['productId']
        gate_file = SPA_PAGES / f"{e['gateComponent']}.tsx"
        if not gate_file.exists():
            fail(f"{pid}: no existe {gate_file}")

        # --- S1: página -access ---
        access_page = OUT_PAGES / (e['accessPath'].lstrip('/') + '.astro')
        emit(access_page, ACCESS_TPL.format(label=e['productLabel'], gate=e['gateComponent']),
             changed, mismatches)

        # --- S2: island wrapper + página -library ---
        sk, rt, defaults = extract_protected_props(app_src, e['libraryPath'], pid)
        if defaults:
            if pid != 'pro-prompts-ebook':
                fail(f"{pid}: ProtectedRoute sin props en App.tsx — solo esperado en pro-prompts")
        else:
            if sk != e['storageKey']:
                fail(f"{pid}: storageKey App.tsx ({sk}) != registro ({e['storageKey']})")
            if rt != e['landingPath']:
                notes.append(f"{pid}: redirectTo de App.tsx ({rt}) != landingPath del registro "
                             f"({e['landingPath']}) — se usa el de App.tsx (fuente de verdad)")

        base = re.sub(r'Dashboard$', '', e['dashboardComponent'])
        island_name = f'{base}LibraryIsland'
        island_file = OUT_ISLANDS / f'{island_name}.tsx'
        tpl = ISLAND_TPL_DEFAULTS if defaults else ISLAND_TPL_PROPS
        emit(island_file,
             tpl.format(lib=e['libraryPath'], dash=e['dashboardComponent'],
                        name=island_name, sk=sk, rt=rt),
             changed, mismatches)

        title = extract_title(e['dashboardComponent'], pid)
        library_page = OUT_PAGES / (e['libraryPath'].lstrip('/') + '.astro')
        emit(library_page,
             LIBRARY_TPL.format(label=e['productLabel'], dash=e['dashboardComponent'],
                                island=island_name, title=title),
             changed, mismatches)

    for n in notes:
        print(f"ℹ️  {n}")
    if CHECK:
        if mismatches:
            for m in mismatches:
                print(f"❌ {m}")
            fail(f"--check: {len(mismatches)} desviaciones")
        print("✅ --check: 138 ficheros generables coinciden byte a byte con el disco")
    else:
        print(f"✅ Generados/actualizados {len(changed)} ficheros "
              f"(46 access + 46 islands + 46 library = 138 gestionados)")
        for c in changed:
            print(f"   {c}")


if __name__ == '__main__':
    main()
