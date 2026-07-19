#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Optimizador de medios del blog (macOS: sips) con guard térmico.

- JPG/JPEG > 250 KB → resample a máx 1200 px de ancho + calidad 75 (en sitio,
  misma ruta: sin cambios de referencias).
- PNG sin canal alfa → JPG calidad 80 máx 1200 px (capturas de app, fotos);
  se borra el PNG y se reescriben las referencias en los .md.
  PNG con alfa (logos) → solo resample a 1200, sigue PNG.
- Guard térmico: cada 60 ficheros comprueba `istats cpu temp`; si ≥62 °C,
  pausa 90 s (regla CPU <65 °C).

Uso: python3 scripts/astro-migration/fase8b-optimize-assets.py
"""
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ASSETS = REPO / 'astro-site' / 'public' / 'blog-assets'
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'
JPG_THRESHOLD = 250 * 1024
MAX_W = 1200


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def thermal_guard(counter):
    if counter % 60 != 0:
        return
    r = run(['istats', 'cpu', 'temp'])
    m = re.search(r'([\d.]+)', r.stdout or '')
    if m and float(m.group(1)) >= 62.0:
        print('  🌡️  %s°C — pausa 90 s' % m.group(1))
        time.sleep(90)


def sips_value(path, prop):
    r = run(['sips', '-g', prop, str(path)])
    m = re.search(prop + r':\s*(\S+)', r.stdout or '')
    return m.group(1) if m else None


def main():
    renames = {}  # ruta relativa vieja → nueva (png→jpg)
    n = 0

    for f in sorted(ASSETS.rglob('*')):
        if not f.is_file():
            continue
        ext = f.suffix.lower()
        size = f.stat().st_size
        n += 1
        thermal_guard(n)

        if ext in ('.jpg', '.jpeg') and size > JPG_THRESHOLD:
            w = sips_value(f, 'pixelWidth')
            cmd = ['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '75']
            if w and w.isdigit() and int(w) > MAX_W:
                cmd += ['--resampleWidth', str(MAX_W)]
            run(cmd + [str(f), '--out', str(f)])

        elif ext == '.png':
            has_alpha = sips_value(f, 'hasAlpha')
            w = sips_value(f, 'pixelWidth')
            if has_alpha == 'yes':
                if w and w.isdigit() and int(w) > MAX_W:
                    run(['sips', '--resampleWidth', str(MAX_W), str(f), '--out', str(f)])
                continue
            out = f.with_suffix('.jpg')
            cmd = ['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '80']
            if w and w.isdigit() and int(w) > MAX_W:
                cmd += ['--resampleWidth', str(MAX_W)]
            r = run(cmd + [str(f), '--out', str(out)])
            if out.exists() and out.stat().st_size > 0:
                f.unlink()
                rel_old = '/blog-assets/' + str(f.relative_to(ASSETS))
                renames[rel_old] = '/blog-assets/' + str(out.relative_to(ASSETS))
            else:
                print('  ⚠️  sips falló con %s: %s' % (f.name, (r.stderr or '')[:80]))

    # Reescritura de referencias png→jpg en los .md
    changed = 0
    if renames:
        for md in CONTENT.rglob('*.md'):
            txt = md.read_text(encoding='utf-8')
            new = txt
            for old, newref in renames.items():
                new = new.replace(old, newref)
            if new != txt:
                md.write_text(new, encoding='utf-8')
                changed += 1

    total = sum(x.stat().st_size for x in ASSETS.rglob('*') if x.is_file())
    print('Procesados %d ficheros · %d png→jpg · %d .md actualizados · total %.0f MB'
          % (n, len(renames), changed, total / 1048576.0))
    # Referencias .png que queden y ya no existan = error
    missing = 0
    for md in CONTENT.rglob('*.md'):
        for rel in re.findall(r'/blog-assets/([^"\'\s\)]+\.png)', md.read_text(encoding='utf-8')):
            if not (ASSETS / rel).exists():
                print('  🚨 ref rota %s en %s' % (rel, md.name))
                missing += 1
    if missing:
        sys.exit(1)
    print('✅ 0 referencias rotas')


if __name__ == '__main__':
    main()
