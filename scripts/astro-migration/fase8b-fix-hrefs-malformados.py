#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Arregla los hrefs malformados heredados del conversor WP→MD.

BUG (detectado 2026-07-28, VPS): `fase8b-wp2md.py` no desescapó las comillas de
algunos enlaces de WordPress y dejó en el markdown final hrefs de la forma:

    <a href="https://\&quot;https://blog.aichef.pro/maillard/\&quot;">   (27 casos)
    <a href="\&quot;https://blog.aichef.pro/maillard/\&quot;">            (8 casos)

El valor del atributo NO es una URL válida, así que son **enlaces rotos en
producción**: el navegador los resuelve como ruta relativa y caen en 404.

Este script:
  1. Desenvuelve el href al URL real.
  2. Reescribe los que apuntan al subdominio viejo `blog.aichef.pro` a su
     destino nativo en `/blog/...` (mismo criterio que fase8b-redirects-blog.txt:
     slug→slug cuando el post existe; mapeo explícito cuando cambió de slug).
  3. Sustituye las 2 imágenes servidas por el CDN de Jetpack (i0.wp.com) por sus
     ficheros locales — ese CDN muere cuando se apague WordPress/Hostinger.

Uso:
    python3 scripts/astro-migration/fase8b-fix-hrefs-malformados.py [--apply]
Sin --apply hace dry-run y no escribe nada.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'

# Destinos del subdominio viejo cuyo slug NO coincide con un post de Astro.
# Verificado uno a uno contra la colección y contra el texto del enlace.
MAPEO_EXPLICITO = {
    'maillard': '/blog/maillard-concepto-y-definicion-2',
    'sous-vide': '/blog/sous-vide-concepto-definicion',
    'dry-aging': '/blog/ia-maduracion-carnes-manual-tecnico-control-optimizacion',
    'gestion-eficiente-de-inventario-en-cocinas-con-ia':
        '/blog/gestion-inventario-restaurantes-ia',
    'optimizacion-de-costes-restaurantes-ia':
        '/blog/inteligencia-artificial-rentabilidad-eficiencia-gestion-gastronomica',
    # Era una CATEGORÍA de WP, fusionada en "recetas" (fase8b-redirects-blog.txt:26)
    'recetario-pro-ai': '/blog/categoria/recetas',
    # Página de WP sin equivalente; el conversor ya mandó el resto de "roadmap"
    # al hub del blog — se mantiene ese criterio por coherencia.
    'roadmap': 'https://aichef.pro/blog',
}

# Imágenes servidas por el CDN de Jetpack → fichero local equivalente
CDN_JETPACK = {
    'https://i0.wp.com/www.aichef.pro/lovable-uploads/12abdf30-3381-42de-a8f1-2abe9342145f.png':
        '/lovable-uploads/12abdf30-3381-42de-a8f1-2abe9342145f.png',
    'https://i0.wp.com/www.aichef.pro/lovable-uploads/5863854b-f30c-47d7-89f0-6124f57cfacf.png':
        '/lovable-uploads/5863854b-f30c-47d7-89f0-6124f57cfacf.png',
}

MALFORMADO = re.compile(r'href="((?:https://)?\\&quot;[^"]*?\\&quot;)"')


def destino(url_real, slugs, avisos):
    """URL real (ya desenvuelta) → destino final."""
    m = re.match(r'https?://blog\.aichef\.pro/(.*)$', url_real)
    if not m:
        return url_real  # aichef.pro / app.aichef.pro: basta con desenvolver
    slug = m.group(1).split('?')[0].strip('/')
    if slug in slugs:
        return '/blog/' + slug
    if slug in MAPEO_EXPLICITO:
        return MAPEO_EXPLICITO[slug]
    avisos.append(slug)
    return 'https://aichef.pro/blog'  # catch-all, igual que el mapa 301


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='escribe los cambios')
    args = ap.parse_args()

    slugs = {p.stem for p in CONTENT.glob('*.md')}
    avisos = []
    n_href = n_img = 0
    tocados = {}

    for path in sorted(CONTENT.glob('*.md')):
        original = path.read_text(encoding='utf-8')
        texto = original

        def _fix(mm):
            nonlocal n_href
            crudo = mm.group(1)
            url_real = re.sub(r'^https://', '', crudo).replace('\\&quot;', '').strip()
            if not url_real.startswith('http'):
                url_real = 'https://' + url_real
            final = destino(url_real, slugs, avisos)
            n_href += 1
            print(f'  {path.name}\n      {crudo[:72]}\n   →  {final}')
            return 'href="%s"' % final

        texto = MALFORMADO.sub(_fix, texto)

        for cdn, local in CDN_JETPACK.items():
            if cdn in texto:
                # el src lleva query de Jetpack (?w=1290&#038;ssl=1): se elimina
                texto2 = re.sub(re.escape(cdn) + r'(\?[^"\']*)?', local, texto)
                n_img += texto.count(cdn)
                print(f'  {path.name}\n      IMG CDN Jetpack → {local}')
                texto = texto2

        if texto != original:
            tocados[path] = texto

    print(f'\n{n_href} hrefs malformados · {n_img} imágenes de CDN · '
          f'{len(tocados)} ficheros afectados')
    if avisos:
        print('⚠️  slugs sin destino conocido (van al hub):', sorted(set(avisos)))

    if not args.apply:
        print('\n(dry-run: no se ha escrito nada; usa --apply)')
        return

    for path, texto in tocados.items():
        path.write_text(texto, encoding='utf-8')
    print(f'✅ {len(tocados)} ficheros escritos')

    # Verificación: no debe quedar NINGUNO
    resto = sum(len(MALFORMADO.findall(p.read_text(encoding='utf-8')))
                for p in CONTENT.glob('*.md'))
    cdn = sum(p.read_text(encoding='utf-8').count('i0.wp.com')
              for p in CONTENT.glob('*.md'))
    print(f'verificación post-escritura: {resto} hrefs malformados · {cdn} refs a i0.wp.com')
    if resto or cdn:
        sys.exit('❌ quedan residuos')


if __name__ == '__main__':
    main()
