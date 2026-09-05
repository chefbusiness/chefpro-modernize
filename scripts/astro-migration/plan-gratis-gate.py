#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plan-gratis-gate.py — AI Chef Pro NO tiene plan gratis desde el 2026-08-15.

El plan de entrada es «AI Chef Miembro»: 10 €/mes, 10.000 créditos, sin
permanencia. Este gate falla si alguna pieza del sitio vuelve a vender el SaaS
como gratuito.

POR QUE EXISTE
--------------
El 2026-09-05, cinco aplicadores dieron su zona por cerrada tras corregir 15
ficheros de blog; el barrido real encontró restos en 108. El censo previo había
buscado FRASES DE MARKETING EN PROSA y se le escaparon tres formas que no
contienen ninguna:

  (a) botones dentro de bloques HTML congelados de WordPress, donde el texto va
      pegado a 200 caracteres de CSS inline («PROBAR GRATIS →»);
  (b) celdas de tabla, donde el dato es sólo «0€/mes» o «No»;
  (c) las FAQ del frontmatter, que son las que emiten el FAQPage y salen SOLAS
      en el rich result de Google.

Por eso el gate busca PATRONES, no frases, y mira la proximidad con la marca.

QUE NO ES UN RESTO (y por eso no se marca)
------------------------------------------
  · las 8 herramientas gratuitas (/herramientas-gratuitas y sus 6 traducciones):
    siguen siendo gratis y sin registro;
  · la micro-sesión gratuita de mentoría;
  · «planes anuales con 2 meses gratis»;
  · «actualizaciones gratuitas / acceso de por vida» de los productos digitales;
  · «ChatGPT gratis» en las comparativas;
  · las OTRAS marcas del grupo: Miselup («Plan gratis para siempre»), Timlup,
    ChefBusiness, Hosply…;
  · los free tier de la COMPETENCIA (Slack, CostBrain, CookKeepBook).

Los últimos van en ALLOW porque comparten ventana con «AI Chef Pro».

USO
---
    python3 scripts/astro-migration/plan-gratis-gate.py          # todo el repo
    python3 scripts/astro-migration/plan-gratis-gate.py --v      # con contexto

Sale con código 1 si encuentra algo. Correrlo al publicar contenido nuevo y
siempre que se toque el copy de precios.
"""
from __future__ import print_function
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VENTANA = 300          # caracteres a cada lado para buscar la marca
EU = u'€'         # € por escape: escribirlo degenera al pasar por heredocs

ZONAS = [
    'astro-site/src/content/blog',
    'astro-site/src/pages',
    'astro-site/src/components',
    'astro-site/src/layouts',
    'src/components', 'src/pages', 'src/data', 'src/i18n', 'src/lib',
]
EXT = ('.md', '.astro', '.tsx', '.ts', '.json')

MARCA = ['ai chef pro', 'aichef.pro', 'ai chef miembro', 'plan miembro',
         'member plan', 'ai chef member']

# ─────────────────────────────────────────────────────────────────────────────
# Dos clases de patrón, y la distinción es la que hace útil al gate.
#
# INCONDICIONALES: sólo pueden referirse a nuestro plan de entrada, así que se
# marcan estén donde estén. Es la clase que salva los dos casos donde la marca
# NO comparte sitio con el resto: la celda de tabla («Miembro (Gratis)» vive en
# un <tr> cuya cabecera es «Plan | Precio | Ideal para», sin marca a la vista) y
# el botón dentro del bloque congelado de WordPress.
#
# CONDICIONALES: existen legítimamente para otros productos (el free tier de
# Slack, el plan gratis de Miselup), así que exigen la marca cerca.
#
# La ventana se mide sobre el TEXTO ENTERO, no sobre la línea: en el frontmatter
# la pregunta lleva «AI Chef Pro» y la respuesta el resto, y en las fichas de
# producto del blog inglés el <h3> con el nombre está 13 líneas por encima.
# Medir por línea daba 1 de 4 defectos inyectados; medir por texto, 4 de 4.
# ─────────────────────────────────────────────────────────────────────────────

# (patron, exige_no_digito_antes)
INCONDICIONALES = [
    (u'probar gratis', False),
    (u'empieza gratis', False),
    (u'empezar gratis', False),
    (u'comenzar ahora gratis', False),
    (u'comenzar prueba gratuita', False),
    (u'crear cuenta gratuita', False),
    (u'start free trial', False),
    (u'miembro (gratis)', False),
    (u'member (free)', False),
    (u'3.000 cr' + u'é' + u'ditos', False),
    (u'3,000 credits', False),
    (u'chef pro gratuitamente', False),
    (u'gratuitamente a ai chef', False),
    (u'plataforma de forma gratuita', False),
    (u'con tarjeta de cr' + u'é' + u'dito ' + u'•', False),   # microcopy invertido
    (u'0' + EU + u'/mes', True),
    (u'0 ' + EU + u'/mes', True),
    (EU + u'0/mes', False),
    (EU + u' 0/mes', False),
    (u'desde 0' + EU, False),
    (u'geen abonnement', False),

    # Fraseos que SOLO se usan para describir el plan de un producto concreto en
    # prosa; los de la competencia van en posesivo («Slack's free tier») o en una
    # celda de tabla, y esos quedan en CONDICIONALES + ALLOW. Sin estos, la ficha
    # de producto del blog ingles («Pricing: Free tier available») no se detecta:
    # su <h3> con el nombre esta a mas de 300 caracteres.
    (u'free tier available', False),
    (u'the free tier', False),
    (u'free tier with 10 uses', False),
    (u'free tier of 10 uses', False),
    (u'free tier provides', False),
]

CONDICIONALES = [
    (u'free tier', False),
    (u'free trial', False),
    (u'free plan', False),
    (u'no credit card', False),
    (u'sin tarjeta de cr', False),
    (u' es gratis', False),          # con espacio: «meses gratis» no es un resto
    (u'gratuitamente', False),
    (u'kostenlos testen', False),
]

# Ficheros verificados a mano: hablan de OTRAS marcas del grupo de principio a fin.
FICHEROS_OK = [
    'src/components/shared/SaasCrossSellBanners.tsx',   # Miselup y Timlup
]

# Excepciones verificadas a mano el 2026-09-05: comparten ventana con la marca
# pero hablan de OTRO producto. Si añades una, di de quién es el plan gratis.
ALLOW = [
    u"costbrain’s unlimited free tier",          # competidor
    u'costbrain&#8217;s unlimited free tier',         # idem, entidad HTML
    u'a free tier where one exists',                  # generico, no es AICP
    u'slack’s free tier',                        # competidor
    u'slack&#8217;s free tier',
    u'entry-level tools like slack offer free tiers',
    u'plan gratis para siempre',                      # Miselup (marca hermana)
    u'crear mi cuenta gratis',                        # Timlup (marca hermana)
    u'plan gratuito de chatgpt',                      # comparativa con ChatGPT
    u'chatgpt tiene plan gratuito',
    u'data-image-title="gratis-a-pro',                # nombre de fichero de imagen
    u'blog/de-gratis-a-pro',                          # slug del post
    u'blog/ia-para-recetas-de-cocina-gratis',         # slug del post
    u'utm_content=ia-para-recetas-de-cocina-gratis',
    # ── verificados el 2026-09-05 ──
    u'excel es gratis',                               # Excel, no AI Chef Pro
    u'chef gpt es gratis',                            # ChatGPT
    u'empezar gratis con timlup',                     # Timlup (marca hermana)
    u'plan gratis sin tarjeta',                       # Miselup
    u'plan gratis siempre',                           # Timlup
    u'meses gratis',                                  # planes anuales: 2 meses gratis
    u'<td>free tier;',                                # celda de tabla: competidor
    u'<th>free tier</th>',                            # cabecera de columna
    u'<td>free trial</td>',                           # celda: meez
    u'<td>free tier available</td>',                 # celda: Slack
    u'free trials or freemium tiers',                 # el mercado en general
    u'pintando «empezar gratis» en un plan de pago',  # comentario del propio fix
    u'calendario editorial de 30 dias',               # herramienta gratuita (PT/ES)
    u'calend' + u'á' + u'rio editorial de 30 dias',
]

DIG = u'0123456789'


# ─────────────────────────────────────────────────────────────────────────────
# Comprobacion ESTRUCTURAL, no por palabras.
#
# La fila «Tarjeta requerida» de la tabla comparativa de las 7 paginas de precios
# tenia «No» en la columna del plan Miembro, contradiciendo la FAQ de la misma
# pagina 200 lineas mas abajo. Ningun censo por palabras lo vio: la celda solo
# contiene «No». Aqui se comprueba la celda por POSICION (la primera <td> tras
# el <th> de la fila), que es donde vive el error.
# ─────────────────────────────────────────────────────────────────────────────
FILA_TARJETA = [
    ('astro-site/src/pages/precios.astro',      u'Tarjeta requerida',        u'Sí'),
    ('astro-site/src/pages/en/pricing.astro',   u'Card required',            u'Yes'),
    ('astro-site/src/pages/fr/tarifs.astro',    u'Carte requise',            u'Oui'),
    ('astro-site/src/pages/de/preise.astro',    u'Kreditkarte erforderlich', u'Ja'),
    ('astro-site/src/pages/it/prezzi.astro',    u'Carta richiesta',          u'Sì'),
    ('astro-site/src/pages/pt/precos.astro',    u'Cartão necessário',        u'Sim'),
    ('astro-site/src/pages/nl/prijzen.astro',   u'Creditcard vereist',       u'Ja'),
]


def revisa_fila_tarjeta():
    """Todos los planes se pagan con tarjeta: la primera celda no puede negarlo."""
    import re
    fallos = []
    for rel, etiqueta, esperado in FILA_TARJETA:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            fallos.append((rel, 0, 'fila-tarjeta', 'fichero inexistente')); continue
        t = io.open(p, encoding='utf-8').read()
        q = t.find(etiqueta + '</th>')
        if q == -1:
            fallos.append((rel, 0, 'fila-tarjeta',
                           u'no encuentro la fila «%s»' % etiqueta)); continue
        m = re.search(r'<td[^>]*>(.*?)</td>', t[q:q + 900], re.S)
        celda = m.group(1).strip() if m else u'(sin celda)'
        if celda != esperado:
            nlin = t.count('\n', 0, q) + 1
            fallos.append((rel, nlin, 'fila-tarjeta',
                           u'plan de entrada dice «%s», deberia decir «%s»'
                           % (celda, esperado)))
    return fallos


def ficheros():
    for z in ZONAS:
        base = os.path.join(ROOT, z)
        if not os.path.isdir(base):
            continue
        for dp, dns, fns in os.walk(base):
            dns[:] = [d for d in dns if d not in ('node_modules', '.astro', 'dist')]
            for fn in fns:
                if fn.endswith(EXT):
                    yield os.path.join(dp, fn)


def main():
    verbose = '--v' in sys.argv or '--verbose' in sys.argv
    fallos = []
    n_fich = 0
    for p in ficheros():
        n_fich += 1
        try:
            texto = io.open(p, encoding='utf-8').read()
        except Exception:
            continue
        rel = os.path.relpath(p, ROOT)
        if rel.replace(os.sep, '/') in FICHEROS_OK:
            continue
        low = texto.lower()
        cortes = [0]                       # offsets de inicio de cada linea
        for i, ch in enumerate(texto):
            if ch == '\n':
                cortes.append(i + 1)

        def linea_de(off):
            lo, hi = 0, len(cortes) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if cortes[mid] <= off:
                    lo = mid
                else:
                    hi = mid - 1
            return lo + 1

        for pat, no_digito, exige_marca in (
                [(a, b, False) for a, b in INCONDICIONALES] +
                [(a, b, True) for a, b in CONDICIONALES]):
            q = low.find(pat)
            while q != -1:
                pre = low[q - 1] if q else u' '
                if no_digito and pre in DIG:
                    q = low.find(pat, q + 1); continue
                # ALLOW se evalua sobre un fragmento CORTO: si mirase toda la
                # ventana, una excepcion legitima taparia un resto vecino.
                tight = low[max(0, q - 120):q + len(pat) + 120]
                if any(a in tight for a in ALLOW):
                    q = low.find(pat, q + 1); continue
                if exige_marca:
                    win = low[max(0, q - VENTANA):q + len(pat) + VENTANA]
                    if not any(m in win for m in MARCA):
                        q = low.find(pat, q + 1); continue
                frag = texto[max(0, q - 90):q + len(pat) + 90].replace('\n', ' ').strip()
                fallos.append((rel, linea_de(q), pat, frag))
                q = low.find(pat, q + 1)

    fallos.extend(revisa_fila_tarjeta())

    print('plan-gratis-gate: %d ficheros analizados' % n_fich)
    if not fallos:
        print('OK — ninguna pieza vende AI Chef Pro como gratis.')
        return 0
    print('FALLO — %d restos del plan gratis:' % len(fallos))
    for rel, nlin, pat, frag in fallos:
        print('  %s:%d  [%s]' % (rel, nlin, pat))
        if verbose:
            print('      %s' % frag[:220])
    print('\nEl plan de entrada es AI Chef Miembro: 10 %s/mes, 10.000 creditos, '
          'sin permanencia.' % EU)
    return 1


if __name__ == '__main__':
    sys.exit(main())
