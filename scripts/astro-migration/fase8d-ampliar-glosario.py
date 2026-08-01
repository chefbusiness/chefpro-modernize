#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8D — Amplía entradas de glosario delgadas con la salida de bridge.py.

POR QUÉ: la mediana del glosario del blog son 1.285 palabras y estas entradas se
habían quedado en 350-420, lo justo para posicionar en la página 5 de una
keyword con demanda real. No es un problema de formato —un glosario puede ser
breve— sino de que la página no responde lo que la SERP pide.

QUÉ HACE: coge el `.md` publicado, le sustituye el cuerpo por el texto ampliado
que devolvió bridge, y de paso deja el post al estándar de contenido enriquecido:

  · **FAQ al FRONTMATTER**, no al cuerpo. Ahí es donde el layout la convierte en
    `FAQPage`; en el cuerpo son encabezados sueltos que no emiten schema.
  · **3 banners de producto** a tres alturas (política de John 2026-07-31),
    elegidos por relevancia temática y con UTM propio del post.
  · **Imágenes de contenido** generadas con Nano Banana, con la destacada
    distinta de las del cuerpo.
  · Tablas con `.table-scroll`, el arreglo que evita que el 72 % del contenido
    quede fuera de pantalla en móvil.

Lo que NO toca: bloques propios del post que no vienen de bridge (el reproductor
de podcast de `que-es-el-food-pairing` lleva un `.m4a` real y se conserva).

⚠️ REGENERAR PISA LAS EDICIONES MANUALES. El cuerpo se reconstruye ENTERO desde
el .txt de bridge, así que cualquier cosa añadida a mano al `.md` después de la
primera pasada desaparece sin avisar. Pasó al reparar las viñetas de
`cocina-molecular`: se llevó por delante los dos enlaces internos (`espumas` y
`esferificación`) que se le habían puesto luego. Antes de volver a correrlo sobre
un post ya publicado, comparar los enlaces con `git show HEAD:<fichero>`.

Uso:
    python3 scripts/astro-migration/fase8d-ampliar-glosario.py --slug <slug>
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ES = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
FUENTE = Path('/tmp/fase8d')

CONFIG = {
    'cocina-molecular-concepto-y-definicion': {
        'bridge': 'molecular.txt',
        'productos': ['kit-tareas-restaurante-creativo', 'kit-escandallos',
                      'guia-restaurante-gastronomico'],
        'imagenes': [
            ('/blog-assets/2026/08/molecular-esferificacion.jpg',
             'Esferificación en proceso: gotas de puré de fruta cayendo en un baño de calcio '
             'sobre una encimera de cocina profesional'),
            ('/blog-assets/2026/08/molecular-hidrocoloides.jpg',
             'Mise en place de cocina molecular con hidrocoloides en cuencos de cristal y una '
             'balanza de precisión'),
        ],
        'preservar': [],
    },
    'que-es-el-food-pairing': {
        'bridge': 'foodpairing.txt',
        'productos': ['kit-tareas-restaurante-creativo', 'pro-prompts-ebook',
                      'guia-restaurante-gastronomico'],
        'imagenes': [
            ('/blog-assets/2026/08/foodpairing-afinidades.jpg',
             'Parejas de ingredientes agrupadas por afinidad aromática sobre mármol: fresa y '
             'albahaca, tomate y vainilla, café y cerdo, chocolate y queso azul'),
            ('/blog-assets/2026/08/foodpairing-emplatado.jpg',
             'Emplatado en el pase de una cocina profesional: unas pinzas colocan una hoja de '
             'albahaca sobre un plato de fresa'),
        ],
        # El reproductor del podcast lleva un .m4a real: se conserva tal cual.
        'preservar': ['<figure class="wp-block-image', '<figure class="wp-block-audio'],
    },
    # — Tanda 2 (2026-08-01, noche). Las dos entradas más delgadas del glosario: 49 y 78
    #   palabras, sin una sola imagen y con la FAQ inexistente. La SERP mandó el
    #   enfoque: en «token» la keyword genérica es de criptomonedas y no se pelea;
    #   en «LLM» el top lo ocupan IBM y AWS, así que el valor está en la capa que
    #   ninguno cubre (qué NO sabe hacer un LLM en una cocina).
    'token-unidad-inteligencia-artificial': {
        'bridge': 'token.txt',
        'productos': ['pro-prompts-ebook', 'kit-escandallos', 'pack-appcc'],
        'imagenes': [
            ('/blog-assets/2026/08/token-troceado.jpg',
             'Una receta impresa recortada en decenas de tiras de papel ordenadas en filas '
             'sobre una encimera de roble, junto a un cuchillo cebollero y unas hierbas frescas'),
            ('/blog-assets/2026/08/token-ventana-contexto.jpg',
             'Una tablet junto a una pila alta de fichas técnicas impresas y un portapapeles '
             'sobre el pase de madera de una cocina profesional'),
        ],
        'preservar': [],
    },
    'llm-large-language-model-cocina': {
        'bridge': 'llm.txt',
        'productos': ['pro-prompts-ebook', 'pack-appcc', 'kit-tareas-restaurante-creativo'],
        'imagenes': [
            ('/blog-assets/2026/08/llm-validacion-chef.jpg',
             'Las manos de un chef corrigiendo a bolígrafo una ficha técnica impresa sobre '
             'una encimera de roble, con una tablet encendida al lado'),
            ('/blog-assets/2026/08/llm-asistente-cocina.jpg',
             'Una tablet apoyada en el pase de una cocina profesional entre cuencos de mise '
             'en place y una sartén, con luz natural de ventana'),
        ],
        'preservar': [],
    },
}


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def parsea(txt):
    """Devuelve (bloques, faq). Un bloque es ('h2'|'h3'|'p'|'lista'|'tabla', contenido)."""
    bloques, faq = [], []
    tabla, lista, en_faq = None, None, False

    def cierra():
        """Vuelca la tabla o la lista que estuviera abierta."""
        nonlocal tabla, lista
        if tabla:
            bloques.append(('tabla', tabla)); tabla = None
        if lista:
            bloques.append(('lista', lista)); lista = None

    for linea in txt.splitlines():
        l = linea.strip()
        if not l:
            continue
        if l.startswith('==='):                      # marcador de tabla
            cierra()
            tabla = []
            continue
        m = re.match(r'\[H([23])\]\s*(.+)', l)
        if m:
            cierra()
            en_faq = bool(re.search(r'preguntas frecuentes|^faq$', m.group(2), re.I))
            if not en_faq:
                bloques.append(('h%s' % m.group(1), m.group(2)))
            continue
        # Viñetas. Sin este caso caían al `else` y se servían como párrafos
        # sueltos empezados por «- », sin <ul>: así se publicaron las 7 del
        # equipamiento de `cocina-molecular` (cazado el 2026-08-01).
        v = re.match(r'[-*•]\s+(.+)', l)
        if v and not en_faq:
            if tabla:
                bloques.append(('tabla', tabla)); tabla = None
            if lista is None:
                lista = []
            lista.append(v.group(1).strip())
            continue
        if '|' in l:
            if en_faq:
                q, a = l.split('|', 1)
                faq.append((q.strip(), a.strip()))
            else:
                if lista:
                    bloques.append(('lista', lista)); lista = None
                if tabla is None:
                    tabla = []
                tabla.append([c.strip() for c in l.split('|')])
            continue
        cierra()
        bloques.append(('p', l))
    cierra()
    return bloques, faq


def html_tabla(filas):
    envoltorio = ('<figure class="wp-block-table"><div class="table-scroll"><table>%s'
                  '</table></div></figure>')
    # Las tablas de DOS columnas del glosario son clave-valor («Origen | 1992,
    # Kurti y This»): no tienen fila de cabeceras, así que tratar la primera como
    # <th> convertía un dato en encabezado. Se renderiza cada clave como th de fila.
    if all(len(f) == 2 for f in filas):
        return envoltorio % ('<tbody>%s</tbody>' % ''.join(
            '<tr><th scope="row">%s</th><td>%s</td></tr>' % (esc(f[0]), esc(f[1])) for f in filas))
    cab, cuerpo = filas[0], filas[1:]
    return envoltorio % ('<thead><tr>%s</tr></thead><tbody>%s</tbody>'
                         % (''.join('<th>%s</th>' % esc(c) for c in cab),
                            ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % esc(c) for c in f)
                                    for f in cuerpo)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', required=True)
    args = ap.parse_args()
    cfg = CONFIG.get(args.slug) or sys.exit('sin configuración para %s' % args.slug)

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'gen', Path(__file__).parent / 'fase8c-libreria-assemble.py')
    gen = importlib.util.module_from_spec(spec)
    guardado, sys.argv = sys.argv, ['gen']
    try:
        spec.loader.exec_module(gen)
    finally:
        sys.argv = guardado
    prods = gen.catalogo_productos()

    md = ES / ('%s.md' % args.slug)
    cabeza, fm, viejo = md.read_text(encoding='utf-8').split('---', 2)
    bloques, faq = parsea((FUENTE / cfg['bridge']).read_text(encoding='utf-8'))
    if len(faq) < 6:
        sys.exit('solo %d preguntas de FAQ: bridge no devolvió la sección completa' % len(faq))

    # Se conserva del post original lo que no viene de bridge (podcast, audio).
    partes = []
    for marca in cfg['preservar']:
        i = viejo.find(marca)
        if i < 0:
            sys.exit('no encuentro el bloque a preservar: %s' % marca)
        partes.append(viejo[i:viejo.find('</figure>', i) + len('</figure>')])

    # Reparto: banners a tres alturas e imágenes espaciadas entre los h2.
    # Se reparten sobre TODOS los bloques, no solo sobre los h2: `que-es-el-food-pairing`
    # solo tiene 3 secciones y una regla atada a los h2 dejaba el post con CERO
    # banners, incumpliendo la política de 3 en silencio.
    def reparte(cuantos):
        sitios = {}
        for k in range(cuantos):
            i = max(1, min(len(bloques) - 1, round((k + 1) * len(bloques) / (cuantos + 1))))
            while i in sitios and i < len(bloques) - 1:
                i += 1
            sitios[i] = k
        return sitios

    donde_banner = reparte(3)
    donde_img = reparte(len(cfg['imagenes']))

    for i, (tipo, cont) in enumerate(bloques):
        if i in donde_img:
            src, alt = cfg['imagenes'][donde_img[i]]
            partes.append(gen.figura(src, alt))
        if i in donde_banner:
            partes.append(gen.banner(cfg['productos'][donde_banner[i]], prods, args.slug, 'es'))
        if tipo == 'tabla':
            partes.append(html_tabla(cont))
        elif tipo == 'lista':
            # `wp-block-list` es la convención del corpus (1.489 usos frente a
            # 946 de `<ul>` pelado). Sin escapar, igual que los párrafos: bridge
            # devuelve enlaces internos y <strong> dentro de las viñetas.
            partes.append('<ul class="wp-block-list">%s</ul>'
                          % ''.join('<li>%s</li>' % x for x in cont))
        elif tipo in ('h2', 'h3'):
            partes.append('<%s class="wp-block-heading">%s</%s>' % (tipo, esc(cont), tipo))
        else:
            partes.append('<p class="wp-block-paragraph">%s</p>' % cont)

    cuerpo = '\n'.join(partes)
    for n, (src, _) in enumerate(cfg['imagenes']):
        if src not in cuerpo:
            sys.exit('la imagen %d no se colocó: revisa el reparto' % (n + 1))

    # FAQ al frontmatter (de ahí sale el FAQPage), reemplazando la que hubiera.
    y = lambda s: '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').strip()
    fm = re.sub(r'\nfaq:\n(?:  - q: .*\n    a: .*\n)+', '\n', fm)
    bloque_faq = 'faq:\n' + ''.join('  - q: %s\n    a: %s\n' % (y(q), y(a)) for q, a in faq)
    fm = re.sub(r'^modDate: .*$', 'modDate: %s' % date.today().isoformat(), fm, flags=re.M)
    fm = fm.rstrip('\n') + '\n' + bloque_faq

    md.write_text('---'.join([cabeza, fm, '\n' + cuerpo + '\n']), encoding='utf-8')
    print('✅ %s\n   %d palabras · %d tablas · %d FAQ · %d banners · %d imágenes'
          % (md.name, len(re.sub(r'<[^>]+>', ' ', cuerpo).split()),
             cuerpo.count('<table>'), len(faq),
             cuerpo.count('utm_medium=banner'), cuerpo.count('<img')))


if __name__ == '__main__':
    main()
