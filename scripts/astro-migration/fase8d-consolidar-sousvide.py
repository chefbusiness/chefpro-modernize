#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8D — Consolidación del clúster sous-vide en un solo pilar (2026-08-03).

POR QUÉ ESTE SCRIPT Y NO `fase8c-consolidar-301.py`: aquel aborta si un origen
de su MAPA ya no existe, y sus 24 orígenes están borrados desde el 2026-07-28.
Peor: si se le cambia el MAPA por otro, su bloque marcado en `_redirects` se
REESCRIBE ENTERO, así que las 24 reglas de julio desaparecerían sin un aviso.
Por eso esta tanda va en un script hermano, con su propia MARCA.

QUÉ SE CONSOLIDA Y POR QUÉ. El roadmap y la sesión del 2026-08-02 señalaban a
`tecnicas-de-coccion-al-vacio-sous-vide` como el duplicado a eliminar, con el
argumento de que pierde contra el pilar «pos. 85,6 frente a 40,3». Esas dos
posiciones son de URLs de `blog.aichef.pro`, el subdominio LEGACY ya 301-eado
(la trampa que el propio CLAUDE.md documenta). Las URLs MIGRADAS del clúster
suman 4 impresiones y 0 clics en 90 días: no hay canibalización medible, así que
el motivo real de consolidar es ESTRUCTURAL —tres páginas propias peleando una
keyword de 3.600/mes—, no una posición.

Y comparando los encabezados uno a uno, el duplicado de verdad era otro:

  · `sous-vide-avanzado-concepto-y-definicion` (1.521 pal.) es el MISMO guion
    que el pilar escrito por segunda vez —definición, origen, ventajas, tabla de
    temperaturas, sellado final, errores, FAQ—, con otros encabezados y otros
    números. Se llama «avanzado» pero no es más avanzado.
  · `tecnicas-de-coccion-al-vacio-sous-vide` (591 pal.) era el candidato del
    plan y resulta ser el ÚNICO con contenido que no está en ningún otro sitio:
    la taxonomía LTLT / pasteurización / HTST / infusión / regeneración. Se
    consolida igual, pero su taxonomía viaja al pilar (sección «Las cinco formas
    de trabajar al vacío») y sus dos infografías en PDF también, vía la clave
    `extra_final` de `fase8d-ampliar-glosario.py`. Sin ese rescate, los PDF se
    quedarían en /blog-assets sirviendo 200 sin un solo enlace en el sitio.

DESTINO = `sous-vide-concepto-definicion`, y no otro, porque «sous vide» son
3.600 búsquedas/mes y «sous vide avanzado» no lo teclea nadie.

Uso:
    python3 scripts/astro-migration/fase8d-consolidar-sousvide.py [--apply]
Sin --apply es dry-run.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
REDIRECTS = REPO / 'astro-site' / 'public' / '_redirects'
MARCA = '# ── Fase 8D: consolidación del clúster sous-vide (2026-08-03) ──'

DESTINO = 'sous-vide-concepto-definicion'
MAPA = {
    'sous-vide-avanzado-concepto-y-definicion': DESTINO,
    'tecnicas-de-coccion-al-vacio-sous-vide': DESTINO,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    slugs = {p.stem for p in CONTENT.glob('*.md')}
    errores = []
    for orig, dest in MAPA.items():
        if orig not in slugs:
            errores.append('origen inexistente: %s' % orig)
        if dest not in slugs:
            errores.append('DESTINO inexistente: %s' % dest)
        if dest in MAPA:
            errores.append('CADENA 301: %s → %s, que a su vez redirige' % (orig, dest))
        if orig == dest:
            errores.append('bucle: %s → sí mismo' % orig)
    if errores:
        for e in errores:
            print('  ❌ ' + e)
        sys.exit('abortado: %d problemas' % len(errores))

    # El pilar tiene que haberse ampliado ANTES: si se borran los orígenes
    # mientras el destino sigue siendo el de 1.518 palabras, se pierde la
    # taxonomía y los errores comunes que venían a rescatarse.
    destino_md = (CONTENT / (DESTINO + '.md')).read_text(encoding='utf-8')
    for senal, que in [('Las cinco formas', 'la taxonomía de tecnicas-de-coccion-al-vacio'),
                       ('Errores comunes', 'los errores comunes de sous-vide-avanzado'),
                       ('cocina-al-vacio-sous-vide-aichefpro.pdf', 'las infografías en PDF')]:
        if senal not in destino_md:
            sys.exit('el pilar NO ha absorbido %s (falta «%s»): amplíalo antes de '
                     'borrar los orígenes' % (que, senal))
    print('✅ el pilar ya absorbió la taxonomía, los errores comunes y los PDF')

    # Enlaces internos que apuntan a un origen → al destino, para no obligar a
    # cada enlace interno a pasar por un 301.
    reescritos, tocados = 0, {}
    for p in sorted(CONTENT.glob('*.md')):
        if p.stem in MAPA:
            continue
        txt = original = p.read_text(encoding='utf-8')
        for orig, dest in MAPA.items():
            for patron in ('https://aichef.pro/blog/%s' % orig, '/blog/%s' % orig):
                rx = re.compile(re.escape(patron) + r'(?=["\'/?#])')
                txt, n = rx.subn(patron.replace(orig, dest), txt)
                reescritos += n
        if txt != original:
            tocados[p] = txt
    print('   enlaces internos a reescribir: %d en %d posts' % (reescritos, len(tocados)))
    for p in tocados:
        print('     · %s' % p.name)

    reglas = [MARCA]
    for orig, dest in sorted(MAPA.items()):
        reglas.append('/blog/%s /blog/%s 301!' % (orig, dest))
        reglas.append('https://blog.aichef.pro/%s https://aichef.pro/blog/%s 301!' % (orig, dest))
    bloque = '\n'.join(reglas) + '\n'
    print('\n   reglas a emitir: %d' % (len(reglas) - 1))
    for orig in sorted(MAPA):
        print('     /blog/%-45s → %s' % (orig, MAPA[orig]))

    if not args.apply:
        print('\n(dry-run: no se ha escrito nada; usa --apply)')
        return

    for p, txt in tocados.items():
        p.write_text(txt, encoding='utf-8')
    for orig in MAPA:
        (CONTENT / (orig + '.md')).unlink()

    red = REDIRECTS.read_text(encoding='utf-8')
    if MARCA in red:
        red = re.sub(re.escape(MARCA) + r'.*?(?=\n#|\Z)', bloque.rstrip('\n'), red, flags=re.S)
    else:
        # ORDEN: Netlify resuelve por PRIMERA coincidencia. Estas reglas deben ir
        # antes de la genérica `/:slug → /blog/:slug`, o ésta las captura y no se
        # ejecutan nunca.
        ANCLA = '# Genérica: cualquier post A/B/C conserva su slug bajo /blog'
        if ANCLA not in red:
            sys.exit('no encuentro el ancla de la regla genérica en _redirects')
        red = red.replace(ANCLA, bloque + '\n' + ANCLA, 1)
    REDIRECTS.write_text(red, encoding='utf-8')

    print('\n✅ %d posts borrados · %d enlaces reescritos · %d reglas'
          % (len(MAPA), reescritos, len(reglas) - 1))
    print('   Ahora: fase8b-regen-lastmod.py, fase8b-auditar-301.py y build con '
           'rm -rf astro-site/.astro (la collection cachea los .md borrados)')


if __name__ == '__main__':
    main()
