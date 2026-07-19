#!/usr/bin/env python3
"""
Fase 6 — Mapa lastmod por URL para el sitemap nativo de Astro.

Extrae los <lastmod> del sitemap de PRODUCCIÓN (la SPA los mantiene a mano) y
los persiste en astro-site/src/lib/sitemap-lastmod.json, que astro.config.mjs
consume en serialize() para que el sitemap de Astro no pierda las fechas.

Re-ejecutable (p.ej. justo antes del cutover) para refrescar el snapshot:
    python3 scripts/astro-migration/fase6-lastmod-map.py
Fetch vía curl (el Python de esta máquina no tiene CA certs de macOS).
"""
import json
import pathlib
import re
import subprocess
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'astro-site/src/lib/sitemap-lastmod.json'

r = subprocess.run(['curl', '-s', '--max-time', '60', 'https://aichef.pro/sitemap.xml'],
                   capture_output=True, text=True)
if r.returncode != 0 or '<urlset' not in r.stdout:
    sys.exit('❌ no pude descargar el sitemap de producción')

mapping = {}
for block in re.findall(r'<url>(.*?)</url>', r.stdout, re.S):
    loc = re.search(r'<loc>([^<]+)</loc>', block)
    lm = re.search(r'<lastmod>([^<]+)</lastmod>', block)
    if loc and lm:
        p = urlparse(loc.group(1).strip()).path or '/'
        if p != '/' and p.endswith('/'):
            p = p[:-1]
        mapping[p] = lm.group(1).strip()

OUT.write_text(json.dumps(mapping, indent=1, ensure_ascii=False, sort_keys=True) + '\n')
print(f'✅ {len(mapping)} lastmod → {OUT}')
