#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 12 — genera la landing de INTEGRACIONES en los 7 idiomas.

QUÉ HACE
  1. Valida los 7 JSON de copy (mismo esqueleto que el español, sin restos de
     otro alfabeto) y los copia a astro-site/src/data/integraciones-copy/, que es
     de donde tira el build.
  2. Emite los 7 envoltorios de src/pages/. Son finos a propósito: el markup vive
     en src/components/IntegracionesPage.astro y así un arreglo de maquetación se
     hace UNA vez. (El bug del footer inglés del hub de librerías salió justo de
     tener el mismo bloque duplicado por idioma.)
  3. Inyecta el bloque `integraciones.*` en los 7 locales de src/i18n/locales/,
     que es lo que lee la sección de la home. Sale del MISMO copy que la landing
     para que home y landing no se contradigan nunca.

DOS TRAMPAS DEL REPO QUE ESTE SCRIPT RESPETA (ver CLAUDE.md):
  · `basePath` va SIN prefijo de idioma —el layout antepone `/${lang}`—, pero
    además aquí se pasa el mapa `alternates` COMPLETO: con override para los 7
    locales, `urlFor()` no llega a usar `basePath` y el canonical no puede salir
    duplicado (`/en/en/...`).
  · Los slugs no pueden empezar por los prefijos de familia de producto
    (`kit- guia- mega- pack- plan- pro-`) ni acabar en `-access`/`-library`, o
    `robots.txt` los bloquearía y el sitemap los excluiría. `integraciones` y sus
    traducciones están limpias, pero el gate lo comprueba igualmente.

Uso:
    python3 fase12-integraciones.py            # dry-run
    python3 fase12-integraciones.py --aplicar
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
COPY_SRC = Path(__file__).parent / 'fase12-copy'
COPY_DST = RAIZ / 'astro-site' / 'src' / 'data' / 'integraciones-copy'
PAGES = RAIZ / 'astro-site' / 'src' / 'pages'
LOCALES = RAIZ / 'src' / 'i18n' / 'locales'

LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']

# fichero de destino dentro de src/pages/
DESTINOS = {
    'es': 'integraciones.astro',
    'en': 'en/integrations.astro',
    'fr': 'fr/integrations.astro',
    'de': 'de/integrationen.astro',
    'it': 'it/integrazioni.astro',
    'pt': 'pt/integracoes.astro',
    'nl': 'nl/integraties.astro',
}

# Prefijos de la zona de pago: robots.txt los bloquea (ver CLAUDE.md).
PREFIJOS_PROHIBIDOS = ('kit-', 'guia-', 'mega-', 'pack-', 'plan-', 'pro-')
SUFIJOS_PROHIBIDOS = ('-access', '-library')

SOSPECHOSO = re.compile(
    r'[　-鿿一-鿿Ѐ-ӿ가-힯'
    r'؀-ۿ֐-׿฀-๿぀-ヿ]')


def forma(o):
    if isinstance(o, dict):
        return {k: forma(v) for k, v in sorted(o.items())}
    if isinstance(o, list):
        return [forma(x) for x in o]
    return type(o).__name__


def textos(o, acc=None):
    acc = [] if acc is None else acc
    if isinstance(o, dict):
        for v in o.values():
            textos(v, acc)
    elif isinstance(o, list):
        for v in o:
            textos(v, acc)
    elif isinstance(o, str):
        acc.append(o)
    return acc


def cargar():
    """Lee y VALIDA los 7 copys. Aborta si alguno no cuadra."""
    base = json.loads((COPY_SRC / 'es.json').read_text(encoding='utf-8'))
    copys = {}
    for lang in LANGS:
        p = COPY_SRC / ('%s.json' % lang)
        if not p.exists():
            sys.exit('FALTA el copy de %s (%s). Genéralo con fase12-traducir-copy.py' % (lang, p))
        d = json.loads(p.read_text(encoding='utf-8'))

        if forma(d) != forma(base):
            sys.exit('%s: la estructura del copy NO coincide con el español' % lang)
        if d.get('lang') != lang:
            sys.exit('%s: el campo "lang" dice %r' % (lang, d.get('lang')))

        malos = [t for t in textos(d) if SOSPECHOSO.search(t)]
        if malos:
            sys.exit('%s: caracteres de otro alfabeto -> %r' % (lang, malos[0][:80]))

        slug = d['path'].rsplit('/', 1)[-1]
        if slug.startswith(PREFIJOS_PROHIBIDOS) or slug.endswith(SUFIJOS_PROHIBIDOS):
            sys.exit('%s: el slug %r cae en un patrón bloqueado por robots.txt' % (lang, slug))

        copys[lang] = d
    return copys


PLANTILLA = '''---
// GENERADO por scripts/astro-migration/fase12-integraciones.py — NO editar a mano.
// El copy está en src/data/integraciones-copy/%(lang)s.json y el markup en
// src/components/IntegracionesPage.astro (uno solo para los 7 idiomas).
import BaseLayout from '%(rel)slayouts/BaseLayout.astro';
import IntegracionesPage from '%(rel)scomponents/IntegracionesPage.astro';
import { SITE } from '%(rel)si18n/config';
import { INTEGRACIONES } from '%(rel)sdata/integraciones';
import copy from '%(rel)sdata/integraciones-copy/%(lang)s.json';

const lang = '%(lang)s';
// SIN prefijo de idioma: el layout lo antepone. Aun así los `alternates` de
// abajo cubren los 7 locales, así que el canonical sale siempre de ahí.
const basePath = '%(basePath)s';
const alternates = %(alternates)s;

const url = `${SITE}%(path)s`;

// Los @id enlazan WebPage y BreadcrumbList para que Google los lea como una
// sola página y no como bloques sueltos.
//
// NO se emite aquí un SoftwareApplication: BaseLayout ya publica el global
// del SaaS, con sus `offers` y precios reales. Emitir otro dejaba DOS nodos
// SoftwareApplication llamados «AI Chef Pro» en la misma página, y el mío era
// el pobre (sin ofertas). Las 16 plataformas las declara el ItemList.
const schemas = [
  {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    '@id': `${url}#webpage`,
    url,
    name: copy.seo.title,
    description: copy.seo.description,
    inLanguage: '%(lang)s',
    isPartOf: { '@type': 'WebSite', '@id': `${SITE}#website`, name: 'AI Chef Pro', url: SITE },
    breadcrumb: { '@id': `${url}#breadcrumb` },
    primaryImageOfPage: { '@type': 'ImageObject', url: `${SITE}/og-integraciones.jpg` },
  },
  {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${url}#breadcrumb`,
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE },
      { '@type': 'ListItem', position: 2, name: copy.breadcrumb, item: url },
    ],
  },
  {
    // El catálogo de plataformas, explícito. Sin precios ni valoraciones
    // inventadas: solo lo que la página realmente enseña.
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    '@id': `${url}#integraciones`,
    name: copy.catalogo.title,
    numberOfItems: INTEGRACIONES.length,
    itemListOrder: 'https://schema.org/ItemListUnordered',
    itemListElement: INTEGRACIONES.map((i, n) => ({
      '@type': 'ListItem',
      position: n + 1,
      name: i.name,
    })),
  },
  {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    '@id': `${url}#faq`,
    mainEntity: copy.faq.items.map((f: { q: string; a: string }) => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  },
];
---

<BaseLayout
  title={copy.seo.title}
  description={copy.seo.description}
  keywords={copy.seo.keywords}
  lang={lang}
  basePath={basePath}
  alternates={alternates}
  ogImage={`${SITE}/og-integraciones.jpg`}
>
  <Fragment slot="head">
    {schemas.map((s) => <script type="application/ld+json" set:html={JSON.stringify(s)} />)}
  </Fragment>

  <IntegracionesPage lang={lang} copy={copy} />
</BaseLayout>
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()

    copys = cargar()
    alternates = {l: copys[l]['path'] for l in LANGS}
    alt_js = json.dumps(alternates, ensure_ascii=False, indent=2).replace('\n', '\n')

    print('copys validados: %d/7' % len(copys))

    for lang in LANGS:
        d = copys[lang]
        destino = PAGES / DESTINOS[lang]
        rel = '../' if lang == 'es' else '../../'
        base_path = '/' + d['path'].rsplit('/', 1)[-1]
        page = PLANTILLA % {
            'lang': lang, 'rel': rel, 'basePath': base_path,
            'alternates': alt_js, 'path': d['path'],
        }
        print('  · %-28s (%s)' % (DESTINOS[lang], d['path']))
        if args.aplicar:
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(page, encoding='utf-8')
            COPY_DST.mkdir(parents=True, exist_ok=True)
            shutil.copy2(COPY_SRC / ('%s.json' % lang), COPY_DST / ('%s.json' % lang))

    # Bloque i18n de la sección de home
    print('\ni18n (integraciones.* para la home):')
    for lang in LANGS:
        p = LOCALES / ('%s.json' % lang)
        data = json.loads(p.read_text(encoding='utf-8'))
        home = copys[lang]['home']
        cambia = data.get('integraciones') != home
        print('  · %s %s' % (lang, 'actualiza' if cambia else 'sin cambios'))
        if args.aplicar and cambia:
            data['integraciones'] = home
            p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n',
                         encoding='utf-8')

    print('\n%s' % ('APLICADO' if args.aplicar else 'DRY-RUN — usa --aplicar'))


if __name__ == '__main__':
    main()
