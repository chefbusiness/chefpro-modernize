#!/usr/bin/env python3
"""Gate de robots.txt — que un comodín de la zona app no vuelva a borrar el blog.

CONTEXTO (2026-08-27). `astro-site/public/robots.txt` protegía la zona app
post-pago con `Disallow: /*-access` y `Disallow: /*-library`. En robots.txt un
patrón SIN `$` no significa «acaba en», sino «casa con el PREFIJO de la URL una
vez expandido el comodín»: `/*-library` casaba también con
`/en/blog/prompt-library-barista-consulting`. Resultado: los 26 posts ingleses
de librerías de prompts y su categoría llevaban desde el 1-ago sin poder
rastrearse (GSC: «Blocked by robots.txt» / «URL is unknown to Google») mientras
sus gemelos españoles estaban indexados. El sitemap los declaraba; Googlebot no
podía entrar. Nadie se enteró porque un bloqueo de robots.txt no rompe el build,
no rompe la página y no sale en ningún diff.

QUÉ COMPRUEBA, para CADA user-agent declarado en el fichero:

  1. Toda ruta de la zona app (las páginas `*-access.astro` / `*-library.astro`
     de `astro-site/src/pages/`, más `/admin/…`) está BLOQUEADA.
  2. Toda URL pública es RASTREABLE. La lista sale del `dist/` si hay build
     reciente (fuente más fiable: son las páginas que se publican de verdad) y,
     si no, del sitemap de producción.

El matcher implementa la spec de Google (RFC 9309): comodín `*`, ancla `$`,
gana la regla de path más largo y, en empate, gana Allow. Sin dependencias:
`pip install protego` en el VPS choca con PEP 668, y este gate tiene que poder
correrse siempre. Se validó carácter a carácter contra Protego el 2026-08-27
sobre las 1.183 URLs del sitemap y las 88 rutas de la zona app: veredicto
idéntico en todas.

Uso:
    python3 scripts/astro-migration/robots-gate.py            # dist si existe
    python3 scripts/astro-migration/robots-gate.py --live     # fuerza sitemap de prod
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROBOTS = REPO / "astro-site" / "public" / "robots.txt"
PAGES = REPO / "astro-site" / "src" / "pages"
DIST = REPO / "astro-site" / "dist"
SITEMAP_INDEX = "https://aichef.pro/sitemap-index.xml"


# ---------------------------------------------------------------- robots.txt

class Group:
    def __init__(self, agents: list[str]) -> None:
        self.agents = agents
        self.rules: list[tuple[bool, str]] = []  # (allow?, path pattern)


def parse_robots(text: str) -> list[Group]:
    """Agrupa por user-agent. Varias líneas User-agent seguidas = un solo grupo."""
    groups: list[Group] = []
    current: Group | None = None
    starting_group = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, _, value = line.partition(":")
        field = field.strip().lower()
        value = value.strip()
        if field == "user-agent":
            if current is None or not starting_group:
                current = Group([])
                groups.append(current)
                starting_group = True
            current.agents.append(value.lower())
        elif field in ("allow", "disallow"):
            if current is None:
                continue
            starting_group = False
            # Un Disallow vacío equivale a Allow: / (no bloquea nada).
            if field == "disallow" and value == "":
                continue
            current.rules.append((field == "allow", value))
    return groups


def _pattern_to_regex(pattern: str) -> re.Pattern[str]:
    anchored = pattern.endswith("$")
    body = pattern[:-1] if anchored else pattern
    regex = "".join(".*" if ch == "*" else re.escape(ch) for ch in body)
    return re.compile("^" + regex + ("$" if anchored else ""))


def group_for(groups: list[Group], agent: str) -> Group | None:
    agent = agent.lower()
    fallback = None
    for g in groups:
        for a in g.agents:
            if a == "*":
                fallback = fallback or g
            # Google casa por prefijo del token del user-agent (googlebot-news
            # cae en el grupo de googlebot). Aquí basta con la igualdad y el
            # prefijo, que es lo que usan las implementaciones de referencia.
            elif agent == a or agent.startswith(a):
                return g
    return fallback


def can_fetch(groups: list[Group], agent: str, path: str) -> bool:
    group = group_for(groups, agent)
    if group is None:
        return True
    best_allow, best_len = True, -1
    for allow, pattern in group.rules:
        if not _pattern_to_regex(pattern).match(path):
            continue
        length = len(pattern)
        # Gana el path más largo; en empate, gana Allow (spec de Google).
        if length > best_len or (length == best_len and allow):
            best_allow, best_len = allow, length
    return True if best_len < 0 else best_allow


# ------------------------------------------------------------------ censos

def app_zone_paths() -> list[str]:
    """Ground truth de la zona app: los ficheros del repo, no una lista a mano."""
    paths = sorted(
        "/" + p.name[: -len(".astro")]
        for p in PAGES.glob("*.astro")
        if p.stem.endswith("-access") or p.stem.endswith("-library")
    )
    # Rutas de /admin declaradas en el robots.
    paths += ["/admin/", "/admin/dashboard"]
    return paths


def dist_paths() -> list[str]:
    out = []
    for html in DIST.rglob("*.html"):
        rel = html.relative_to(DIST).as_posix()
        rel = rel[: -len(".html")]
        if rel == "index":
            out.append("/")
        elif rel.endswith("/index"):
            out.append("/" + rel[: -len("/index")])
        else:
            out.append("/" + rel)
    return sorted(set(out))


def live_paths() -> list[str]:
    def fetch(url: str) -> str:
        req = urllib.request.Request(url, headers={"User-Agent": "robots-gate"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")

    index = fetch(SITEMAP_INDEX)
    children = re.findall(r"<loc>([^<]+)</loc>", index)
    locs: list[str] = []
    for child in children:
        locs += re.findall(r"<loc>([^<]+)</loc>", fetch(child))
    return sorted({re.sub(r"^https://[^/]+", "", u).rstrip("/") or "/" for u in locs})


# -------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="usa el sitemap de producción")
    args = ap.parse_args()

    groups = parse_robots(ROBOTS.read_text(encoding="utf-8"))
    agents = sorted({a for g in groups for a in g.agents})
    print(f"robots.txt: {len(groups)} grupos · user-agents: {', '.join(agents)}")

    private = app_zone_paths()
    if args.live or not DIST.exists():
        source, public = "sitemap de producción", live_paths()
    else:
        source, public = "dist/ local", dist_paths()
    private_set = set(private)
    public = [p for p in public if p not in private_set and not p.startswith("/admin")]
    print(f"censo: {len(public)} URLs públicas ({source}) · {len(private)} rutas privadas\n")

    fugas: list[str] = []     # privada rastreable
    bloqueos: list[str] = []  # pública bloqueada
    for agent in agents:
        for path in private:
            if can_fetch(groups, agent, path):
                fugas.append(f"{agent}: {path}")
        for path in public:
            if not can_fetch(groups, agent, path):
                bloqueos.append(f"{agent}: {path}")

    ok = True
    if bloqueos:
        ok = False
        print(f"❌ {len(bloqueos)} URL(s) PÚBLICAS bloqueadas por robots.txt:")
        for x in bloqueos[:40]:
            print("   ", x)
        if len(bloqueos) > 40:
            print(f"    … y {len(bloqueos) - 40} más")
    else:
        print("✅ ninguna URL pública bloqueada")

    if fugas:
        ok = False
        print(f"\n❌ {len(fugas)} ruta(s) de la ZONA APP rastreables:")
        for x in fugas[:40]:
            print("   ", x)
        if len(fugas) > 40:
            print(f"    … y {len(fugas) - 40} más")
    else:
        print("✅ toda la zona app bloqueada")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
