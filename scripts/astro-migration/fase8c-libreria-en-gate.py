#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate de la versión INGLESA de una librería de prompts (Fase 8C).

Nace de que el piloto de 2026-08-01 falló y el mensaje de error acusaba al modelo
de lo que era un fallo del parser. Aquí se comprueba contra el post ESPAÑOL, que
es la fuente: si el inglés perdió un bloque, un prompt, un tip o una imagen por el
camino, esto lo dice con nombre y apellidos.

Dos niveles, a propósito:
  ⛔ ERROR   — estructural y objetivo (faltan prompts, banner sin UTM, marcador sin
              sustituir, nombre del agente en español). Falla el gate.
  ⚠  REVISAR — editorial: lo que una máquina no puede sentenciar (posible normativa
              inventada, restos de métrico). Se lista para leerlo a ojo.

Uso:
    python3 scripts/astro-migration/fase8c-libreria-en-gate.py --slug id-alergenos
    python3 scripts/astro-migration/fase8c-libreria-en-gate.py --todos
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ES = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
EN = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en'
ASSETS = REPO / 'astro-site' / 'public'
MAPA = Path(__file__).parent / 'fase8c-agentes' / 'agentes-en.json'

# Lo que NUNCA puede aparecer en un post inglés. La normativa europea no rige para
# el lector estadounidense: traducirla sería publicar derecho que no le aplica.
# El tercer campo exime al interior de los banners: ahí el € es el precio REAL que
# cobra Stripe (los productos digitales solo tienen landing en español, decisión de
# John 2026-07-31). Convertirlo a dólares sería mentir sobre el cargo.
VETADO = [
    (r'\bAPPCC\b', 'APPCC (en inglés es HACCP)', False),
    (r'Reglamento\s+\(?UE\)?', 'Reglamento UE', False),
    (r'1169/2011', 'Reglamento 1169/2011 (norma de la UE)', False),
    (r'RD\s*126/2015', 'RD 126/2015 (norma española)', False),
    (r'\b14\s+(?:major\s+)?allerg', 'los 14 alérgenos de la UE (en EE. UU. son 9)', False),
    (r'€', 'euros fuera de un banner de producto', True),
    (r'[¿¡]', 'signos de apertura españoles', False),
]
BANNER = re.compile(r'<aside\b.*?</aside>', re.S)

# Guiños permitidos a otros mercados: se nombra al REGULADOR y la obligación
# general, nunca artículos, fechas ni umbrales. Si aparece una cifra cerca, a leerlo.
REGULADORES_GUINO = r"(FSA|Natasha'?s Law|FSANZ|FSSAI|Food Standards)"
CIFRA_NORMATIVA = r'(Article|Articles|Section|Regulation|Standard|Schedule)\s*\d'

METRICO = [(r'\d+\s*°C\b', '°C'), (r'\d+\s*kg\b', 'kg'), (r'\d+\s*ml\b', 'ml'),
           (r'\d+\s*litr', 'litros'), (r'\d+\s*cm\b', 'cm')]

# El inglés de cocina usa «sauté», «purée», «jalapeño»: los acentos no delatan
# español. Una acumulación de palabras función, sí.
FUNCION_ES = re.compile(r'\b(el|la|los|las|del|que|para|con|una|por|más|cómo|qué|tus?|'
                        r'este|esta|sus?|puede|cocina)\b', re.I)


def limpia(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()


def trozos(md):
    txt = md.read_text(encoding='utf-8')
    return txt.split('---', 2)[1], txt.split('---', 2)[2]


def frase(texto, pos, radio=110):
    return limpia(texto[max(0, pos - radio):pos + radio])


IMPERIAL = re.compile(r'°F|\b(lbs?|pounds?|oz|ounces?|qts?|quarts?|gal|gallons?|pints?|'
                      r'fl\s*oz|cups?|inch|inches|foot|feet|tsp|tbsp)\b|\d\s*[‑-]?\s*(in|ft)\b',
                      re.I)


def con_imperial_al_lado(texto, pos, radio=70):
    """El molde pide imperial primero y métrico de apoyo, y eso se escribe de las
    dos formas: «440 lb (200 kg)» y «-12°C (10°F)». Mirar solo si el métrico va
    entre paréntesis marca como error la mitad de los casos correctos. Lo que
    importa es que la equivalencia imperial esté AL LADO, en el orden que sea."""
    return bool(IMPERIAL.search(texto[max(0, pos - radio):pos + radio]))


def revisa(slug, mapa, prods_ts):
    info = mapa[slug]
    md_es, md_en = ES / ('libreria-de-prompts-para-%s.md' % slug), EN / (info['slug_en'] + '.md')
    errores, avisos = [], []
    if not md_en.exists():
        return ['no existe %s' % md_en.name], []

    fm_es, cu_es = trozos(md_es)
    fm_en, cu_en = trozos(md_en)
    plano = limpia(cu_en)
    A = info['agente']

    # ── 1. Paridad estructural con el español ──────────────────────────────
    filas_es = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', cu_es, re.S)
    filas_en = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', cu_en, re.S)
    if len(filas_en) != len(filas_es):
        errores.append('prompts: %d en inglés vs %d en español' % (len(filas_en), len(filas_es)))
    tablas_es, tablas_en = cu_es.count('<table>'), cu_en.count('<table>')
    if tablas_en != tablas_es:
        errores.append('tablas: %d vs %d' % (tablas_en, tablas_es))
    if cu_en.count('tabla-prompts') != tablas_en:
        errores.append('%d de %d tablas sin la clase .tabla-prompts (el fix del scroll '
                       'horizontal que escondía el 72%% del contenido)'
                       % (tablas_en - cu_en.count('tabla-prompts'), tablas_en))
    faq_en = re.findall(r'^  - q: "(.*?)"\n    a: "(.*?)"$', fm_en, re.M | re.S)
    if len(faq_en) < 8:
        errores.append('FAQ con %d entradas (el molde son 10)' % len(faq_en))

    # ── 2. Nada de español donde debería haber inglés ──────────────────────
    # El frontmatter entra en la revisión: ahí viven title, description y la FAQ, que
    # se pinta en la página Y alimenta el FAQPage. En el piloto salieron las 10
    # preguntas en español con la respuesta en inglés y esto no lo veía.
    sin_banners = limpia(BANNER.sub(' ', cu_en)) + ' ' + fm_en
    for patron, que, exime_banner in VETADO:
        donde = sin_banners if exime_banner else plano + ' ' + fm_en
        for m in re.finditer(patron, donde, re.I):
            errores.append('%s → «%s»' % (que, frase(donde, m.start(), 70)))
            break
    for q, a in faq_en:
        for etiqueta, texto in (('pregunta', q), ('respuesta', a)):
            if len(set(m.group(0).lower() for m in FUNCION_ES.finditer(texto))) >= 3:
                errores.append('FAQ: %s en español → «%s»' % (etiqueta, texto[:90]))
    # El nombre español del agente sale del propio post ES ("Tips y Consejos de Uso
    # para X"). Los 12 de hotelería se llaman igual en los dos idiomas: ahí no aplica.
    m_es = re.search(r'<h[123][^>]*>Tips y Consejos de Uso para (.*?)</h[123]>', cu_es, re.S)
    nombre_es = limpia(m_es.group(1)) if m_es else ''
    if nombre_es and nombre_es != A and re.search(re.escape(nombre_es), plano):
        errores.append('aparece el nombre ESPAÑOL del agente («%s»); el lector inglés no lo '
                       'encuentra en su interfaz, que dice «%s»' % (nombre_es, A))
    if A not in plano:
        errores.append('no aparece el nombre del agente en inglés («%s»)' % A)

    # ── 3. Marcadores, imágenes y banners ─────────────────────────────────
    sobra = re.findall(r'<!--(?:IMG|BANNER)\d+-->', cu_en)
    if sobra:
        errores.append('marcadores sin sustituir: %s' % sobra)
    src_es = [s for s, _ in re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', cu_es)]
    src_en = [s for s, _ in re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', cu_en)]
    if src_en != src_es:
        errores.append('imágenes distintas del ES: %d vs %d' % (len(src_en), len(src_es)))
    destacada = re.search(r'^image: (.*)$', fm_en, re.M)
    if not destacada:
        errores.append('falta «image:» en el frontmatter')
    for s in src_en + ([destacada.group(1).strip()] if destacada else []):
        if not (ASSETS / s.lstrip('/')).exists():
            errores.append('imagen inexistente en public/: %s' % s)
    for alt in re.findall(r'<img[^>]*alt="([^"]*)"', cu_en):
        if re.search(r'[áéíóúñÁÉÍÓÚÑ]', alt):
            errores.append('alt en español: «%s»' % alt)

    banners = re.findall(r'utm_source=blog&amp;utm_medium=banner&amp;utm_content=([\w-]+)', cu_en)
    if len(banners) < 3:
        errores.append('%d banners de producto; la política pide mínimo 3' % len(banners))
    for b in set(banners):
        if b != info['slug_en']:
            errores.append('banner con UTM de otro post: %s (debería ser %s)' % (b, info['slug_en']))
    for p in info.get('productos', []):
        if p not in prods_ts:
            errores.append('producto inexistente en el catálogo: %s' % p)

    # ── 4. hreflang recíproco ─────────────────────────────────────────────
    if 'lang: en' not in fm_en:
        errores.append('falta «lang: en» en el frontmatter')
    if info['slug_en'] not in fm_es:
        errores.append('el post ES no declara la traducción inglesa: sin reciprocidad Google '
                       'ignora el hreflang')
    if ('libreria-de-prompts-para-%s' % slug) not in fm_en:
        errores.append('el post EN no declara la traducción española')

    # ── 5. Enlaces internos ───────────────────────────────────────────────
    for href in re.findall(r'href="https://aichef\.pro/en/blog/([\w/-]+)"', cu_en):
        if href.startswith('category/'):
            continue
        if not (EN / (href + '.md')).exists():
            errores.append('enlace interno a un post EN que no existe: /en/blog/%s' % href)
    if '<ul></ul>' in cu_en:
        errores.append('lista de enlaces vacía (<ul></ul>)')
    if re.search(r'<h1[^>]*>', cu_en):
        errores.append('hay un <h1> dentro del cuerpo: doble H1 con el del layout')

    # ── 6. Editorial: para leer a ojo ─────────────────────────────────────
    for m in re.finditer(REGULADORES_GUINO, plano):
        ventana = plano[m.start():m.start() + 220]
        c = re.search(CIFRA_NORMATIVA, ventana)
        if c:
            avisos.append('posible normativa inventada cerca de «%s»: %s'
                          % (m.group(1), limpia(ventana[:180])))
    # Solo molesta el métrico SIN equivalencia imperial al lado. Ojo: hay unidades
    # métricas que en EE. UU. son la designación real del producto (la botella de
    # 750 ml, el saco de 25 kg de harina) y salen aquí de todas formas: por eso es
    # un aviso para leer, no un error.
    for patron, que in METRICO:
        sueltos = [m for m in re.finditer(patron, plano)
                   if not con_imperial_al_lado(plano, m.start())]
        if sueltos:
            avisos.append('%d uso(s) de %s sin equivalencia imperial al lado: %s'
                          % (len(sueltos), que, frase(plano, sueltos[0].start(), 60)))
    palabras = len(plano.split())
    if palabras < 2500:
        avisos.append('solo %d palabras' % palabras)

    return errores, avisos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug')
    ap.add_argument('--todos', action='store_true')
    args = ap.parse_args()
    mapa = json.loads(MAPA.read_text(encoding='utf-8'))
    ts = (REPO / 'src' / 'data' / 'products-catalog.ts').read_text(encoding='utf-8')
    prods_ts = set(re.findall(r"id: '([^']+)'", ts))

    if args.todos:
        slugs = [s for s in sorted(mapa) if (EN / (mapa[s]['slug_en'] + '.md')).exists()]
        if not slugs:
            sys.exit('todavía no hay ninguna librería EN generada en %s'
                     % EN.relative_to(REPO))
    elif args.slug:
        slugs = [args.slug]
        if args.slug not in mapa:
            sys.exit('%s no está en %s' % (args.slug, MAPA.name))
    else:
        sys.exit('hace falta --slug o --todos')

    total_e = 0
    for s in slugs:
        errores, avisos = revisa(s, mapa, prods_ts)
        total_e += len(errores)
        estado = '✅ PASA' if not errores else '⛔ %d ERROR(ES)' % len(errores)
        print('\n%s  %s → %s' % (estado, s, mapa[s]['slug_en']))
        for e in errores:
            print('   ⛔ %s' % e)
        for a in avisos:
            print('   ⚠  %s' % a)
    print('\n%s' % ('─' * 70))
    print('%d post(s) · %d errores' % (len(slugs), total_e))
    sys.exit(1 if total_e else 0)


if __name__ == '__main__':
    main()
