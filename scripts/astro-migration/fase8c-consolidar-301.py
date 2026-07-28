#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8C — Consolidación SEO: 301 de las URLs duplicadas hacia su pilar refrescado.

CONTEXTO. El refresh Tier A dejó 82 pilares actualizados y, detrás, una cola de
posts que cubren la MISMA intención de búsqueda con peor contenido. Medido en
GSC (90 días, 2026-04-29 → 07-27) suman **1 clic entre los 24**: no hay
autoridad que preservar, sí canibalización que eliminar. John dio OK explícito
el 2026-07-28 ("el punto dos, adelante, decide tú").

QUÉ HACE:
  1. Verifica que cada destino existe y NO es a su vez un origen (sin cadenas).
  2. Reescribe los enlaces internos que apuntaban a un origen → al destino
     (si no, cada enlace interno pasaría por un 301 innecesario).
  3. Borra los .md de los orígenes.
  4. Emite las reglas 301 en astro-site/public/_redirects.

Uso:
    python3 scripts/astro-migration/fase8c-consolidar-301.py [--apply]
Sin --apply es dry-run.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
REDIRECTS = REPO / 'astro-site' / 'public' / '_redirects'
MARCA = '# ── Fase 8C: consolidación de duplicados Tier A (2026-07-28) ──'

# origen → destino. Cada destino es un pilar YA refrescado que cubre la misma
# intención de búsqueda. Mapeado uno a uno leyendo ambos títulos.
MAPA = {
    # ── Los 14 que John había marcado ──
    '10-herramientas-de-ia-imprescindibles-para-los-chefs-de-hoy':
        '15-herramientas-de-ia-que-todo-chef-deberia-conocer',
    'branding-gastronomico-con-ia':
        'branding-gastronomico-ia-marca-restaurante',
    'gestion-de-franquicias-gastronomicas-con-ia':
        'ia-franquicias-restaurantes-escalar-cadena',
    'como-usar-ai-chef-pro-para-revolucionar-tu-servicio-de-catering':
        'ia-catering-empresas-eventos-corporativos',
    'tecnologia-de-seguridad-alimentaria-con-ia-transformando-practicas-culinarias':
        'como-la-ia-esta-mejorando-la-seguridad-alimentaria-en-restaurantes',
    'generador-de-menus-con-ia':
        'ia-para-crear-menus',
    # intención = "¿ChatGPT sirve para esto?" → el pilar de límites de ChatGPT
    'puede-chatgpt-disenar-el-menu-o-la-carta-de-un-restaurante':
        'chatgpt-restaurantes-vs-ai-chef-pro-comparativa',
    'puede-la-ia-reemplazar-a-los-chefs-transforma-tu-cocina-con-ai-chef-pro':
        'puede-la-ia-reemplazar-a-los-chefs-descubre-con-ai-chef-pro',
    'fotografia-culinaria-mejorada-por-ia':
        'fotografia-gastronomica-ia-instagram',
    'automatizacion-inteligente-en-hosteleria':
        'automatizacion-en-cocinas-profesionales-el-impacto-de-la-ia',
    'ia-en-artes-culinarias-personalizando-tu-experiencia-gastronomica':
        'personalizacion-de-experiencias-gastronomicas-con-inteligencia-artificial',
    'la-ia-en-la-alta-cocina-aplicaciones-con-ai-chef-pro':
        'ia-para-restaurantes-de-estrella-michelin',
    'ai-chef-pro-intro':
        'como-configurar-tu-cuenta-en-ai-chef-pro-paso-a-paso',
    'introduccion-a-ai-chef-pro':
        'como-configurar-tu-cuenta-en-ai-chef-pro-paso-a-paso',

    # ── Clúster "funciones de AI Chef Pro": 7 posts, 0 clics y 2 impresiones ──
    'ai-chef-pro-revolucionando-la-cocina-mas-alla-de-los-metodos-tradicionales':
        'como-se-utiliza-la-ia-en-la-gastronomia-con-ai-chef-pro-2',
    'desbloquea-las-funciones-de-ai-chef-pro-para-una-planificacion-de-comidas-sin-esfuerzo':
        'ia-para-crear-menus-semanales',
    'desbloqueando-las-funciones-de-ai-chef-pro-para-alcanzar-el-dominio-culinario':
        'ai-chef-pro-advanced-funciones-ocultas-que-solo-usan-los-top-chefs',
    'desbloqueando-las-funciones-de-ai-chef-pro-para-sugerencias-de-recetas':
        'mejor-ia-para-cocinar-en-2025',
    'desbloqueando-los-beneficios-de-ai-chef-pro-revolucion-tecnologica-en-la-cocina-profesional':
        'ai-chef-pro-advanced-funciones-ocultas-que-solo-usan-los-top-chefs',
    'descubre-las-mejores-funciones-de-ai-chef-pro-guia-completa-2025':
        'ai-chef-pro-advanced-funciones-ocultas-que-solo-usan-los-top-chefs',
    'inteligencia-artificial-para-restaurantes-con-ai-chef-pro-2':
        'mejores-ia-restaurantes-2026',

    # ── Notas de changelog (329-616 palabras, 0 clics y 0 impresiones) ──
    'actualizacion-sobre-ai-chef-pro-y-nuevos-modulos-16-2-26':
        'ai-chef-pro-advanced-funciones-ocultas-que-solo-usan-los-top-chefs',
    'ai-chef-pro-actualizacion-v-1-7':
        'ai-chef-pro-advanced-funciones-ocultas-que-solo-usan-los-top-chefs',
    'ai-chef-pro-version-en-ingles':
        'como-configurar-tu-cuenta-en-ai-chef-pro-paso-a-paso',
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    slugs = {p.stem for p in CONTENT.glob('*.md')}
    errores = []

    # ── 1. Validaciones que ABORTAN ──
    for orig, dest in MAPA.items():
        if orig not in slugs:
            errores.append('origen inexistente: %s' % orig)
        if dest not in slugs:
            errores.append('DESTINO inexistente: %s (de %s)' % (dest, orig))
        if dest in MAPA:
            errores.append('CADENA 301: %s → %s, que a su vez redirige' % (orig, dest))
        if orig == dest:
            errores.append('bucle: %s → sí mismo' % orig)
    if errores:
        for e in errores:
            print('  ❌ ' + e)
        sys.exit('abortado: %d problemas en el mapa' % len(errores))
    print('✅ mapa válido: %d orígenes, %d destinos distintos, sin cadenas ni bucles'
          % (len(MAPA), len(set(MAPA.values()))))

    # ── 2. Enlaces internos que apuntan a un origen ──
    reescritos = 0
    ficheros_tocados = {}
    for p in sorted(CONTENT.glob('*.md')):
        if p.stem in MAPA:
            continue  # se va a borrar igualmente
        txt = original = p.read_text(encoding='utf-8')
        for orig, dest in MAPA.items():
            for patron in ('https://aichef.pro/blog/%s' % orig, '/blog/%s' % orig):
                # sólo el enlace exacto, no un slug que empiece igual
                rx = re.compile(re.escape(patron) + r'(?=["\'/?#])')
                txt, n = rx.subn(patron.replace(orig, dest), txt)
                reescritos += n
        if txt != original:
            ficheros_tocados[p] = txt
    print('   enlaces internos a reescribir: %d en %d posts'
          % (reescritos, len(ficheros_tocados)))

    # ── 3. Reglas de redirección ──
    reglas = [MARCA]
    for orig, dest in sorted(MAPA.items()):
        reglas.append('/blog/%s /blog/%s 301!' % (orig, dest))
        # el subdominio viejo tenía su propia regla genérica slug→slug: se
        # adelanta la específica para no encadenar 301 sobre 301
        reglas.append('https://blog.aichef.pro/%s https://aichef.pro/blog/%s 301!'
                      % (orig, dest))
    bloque = '\n'.join(reglas) + '\n'

    print('\n   reglas a emitir: %d (%d rutas + %d del subdominio viejo)'
          % (len(reglas) - 1, len(MAPA), len(MAPA)))
    for orig, dest in sorted(MAPA.items()):
        print('     /blog/%-72s → %s' % (orig[:72], dest))

    if not args.apply:
        print('\n(dry-run: no se ha escrito nada; usa --apply)')
        return

    for p, txt in ficheros_tocados.items():
        p.write_text(txt, encoding='utf-8')
    for orig in MAPA:
        (CONTENT / (orig + '.md')).unlink()

    red = REDIRECTS.read_text(encoding='utf-8')
    if MARCA in red:
        red = re.sub(re.escape(MARCA) + r'.*?(?=\n#|\Z)', bloque.rstrip('\n'), red, flags=re.S)
    else:
        # ⚠️ ORDEN: Netlify resuelve por primera coincidencia. Las reglas del
        # subdominio DEBEN ir antes de la genérica `/:slug → /blog/:slug`, o
        # ésta las captura y nunca se ejecutan (además, así se evita la cadena
        # 301→301 que resultaría de pasar por el slug viejo).
        ANCLA = '# Genérica: cualquier post A/B/C conserva su slug bajo /blog'
        if ANCLA not in red:
            sys.exit('no encuentro el ancla de la regla genérica en _redirects; '
                     'revisa el fichero antes de insertar')
        red = red.replace(ANCLA, bloque + '\n' + ANCLA, 1)
    REDIRECTS.write_text(red, encoding='utf-8')

    print('\n✅ %d posts borrados · %d enlaces internos reescritos · '
          '%d reglas en _redirects' % (len(MAPA), reescritos, len(reglas) - 1))
    print('   Recuerda: fase8b-regen-lastmod.py + fase8b-gate.py')


if __name__ == '__main__':
    main()
