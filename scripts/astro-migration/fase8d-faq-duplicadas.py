#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecta preguntas duplicadas dentro del `faq:` de un mismo post.

POR QUÉ IMPORTA. Cada `q:` del frontmatter se convierte en una `Question` del
`FAQPage` que emite `BlogPost.astro`, y en un rich result **cada Question
aparece sola**. Dos formulaciones de la misma pregunta no sólo inflan el schema:
sus respuestas suelen estar escritas para leerse en secuencia, y entonces una de
ellas no dice nada por su cuenta. El caso que lo destapó (2026-08-04) fue
`chili-crisp`, con CUATRO variantes de «qué es» y una respuesta que abría con
«Es exactamente lo mismo».

CÓMO COMPARA. No por igualdad de cadena: los duplicados vienen de recoger varias
formulaciones del People Also Ask, que difieren en tildes, artículos, orden y
hasta en la grafía del término («chilli» / «chili»). Se normaliza —minúsculas,
sin diacríticos, sin signos, sin palabras vacías— y se cruzan dos medidas:
Jaccard de tokens y ratio de secuencia.

TRES NIVELES, porque el ruido es alto: dos preguntas sobre el mismo tema
comparten casi todo el vocabulario sin ser la misma pregunta («¿qué es X?» y
«¿es seguro X?» dan Jaccard 0,67 y son distintas).

  IDENTICA  mismo conjunto de tokens de contenido → duplicado seguro
  DEFINICION  las dos son del tipo «qué es …» sobre el mismo sujeto → casi seguro
  PARECIDA  similitud alta pero distinto pronombre interrogativo → revisar a mano

Uso:
    python3 scripts/astro-migration/fase8d-faq-duplicadas.py [--lang es|en|todos]
                                                             [--nivel identica|definicion|parecida]
"""
import argparse
import difflib
import itertools
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'

# Artículos, preposiciones y auxiliares: no distinguen una pregunta de otra.
VACIAS_ES = {'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'del',
             'en', 'y', 'o', 'que', 'es', 'son', 'al', 'para', 'con', 'por',
             'se', 'su', 'sus', 'lo', 'a', 'mi', 'hay', 'ser', 'esta', 'este'}
VACIAS_EN = {'the', 'a', 'an', 'of', 'in', 'and', 'or', 'that', 'is', 'are',
             'to', 'for', 'with', 'by', 'its', 'it', 'this', 'be', 'what'}
# 2026-08-08 — blog italiano. Ojo a los apóstrofos: en italiano «l'haccp» y
# «un'etichetta» son una sola palabra para el lector pero dos para un split
# ingenuo, así que las formas elididas entran también en la lista.
VACIAS_IT = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'del',
             'della', 'dei', 'delle', 'in', 'e', 'o', 'che', 'è', 'sono', 'al',
             'per', 'con', 'da', 'si', 'suo', 'sua', 'a', 'ci', 'quali', 'quale',
             'cosa', "l'", "un'", 'come', 'ha', 'essere', 'questo', 'questa'}

# Arranques que marcan una pregunta de DEFINICIÓN.
DEFINICION = (
    re.compile(r'^(que es|que son|que significa|en que consiste)\b'),
    re.compile(r'^(what is|what are|what does .* mean)\b'),
)


def sin_tildes(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def tokens(q, vacias):
    s = re.sub(r'[^a-z0-9ñ ]', ' ', sin_tildes(q))
    return [t for t in s.split() if t not in vacias]


def es_definicion(q):
    # El sujeto se compara aparte: «¿qué es X?» y «¿qué es Y?» no son duplicados.
    plano = re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9ñ ]', ' ', sin_tildes(q))).strip()
    for rx in DEFINICION:
        m = rx.match(plano)
        if m:
            return plano[m.end():].strip()
    # «¿Chili Crisp qué es?» — el PAA también invierte el orden.
    if re.search(r'\bque es\b\s*$', plano):
        return plano[:plano.rfind('que es')].strip()
    return None


RX_FAQ_H = re.compile(
    r'<h([23])[^>]*>\s*(?:<[^>]+>\s*)*[^<]*?[Pp]reguntas\s+[Ff]recuentes', re.S)


def _zona_faq(cuerpo):
    """Recorta la sección de la FAQ del cuerpo.

    ACOTAR PRIMERO NO ES OPCIONAL. Un regex de pregunta lanzado sobre el cuerpo
    entero no falla: acierta en el sitio equivocado (encabezados de otras
    secciones, del bloque de relacionados congelado de WordPress…). Se corta
    desde el encabezado de la FAQ hasta el siguiente encabezado del MISMO nivel
    o superior, y si no hay, hasta el final.
    """
    m = RX_FAQ_H.search(cuerpo)
    if not m:
        return None
    nivel = int(m.group(1))
    resto = cuerpo[m.end():]
    cierre = re.search(r'<h[1-%d][^>]*>' % nivel, resto)
    return resto[:cierre.start()] if cierre else resto


def preguntas_de(md):
    """(fuente, preguntas). El frontmatter manda: es lo que emite el FAQPage."""
    fm, cuerpo = md.split('\n---\n', 1)
    qs = re.findall(r'^  - q: ["\'](.*)["\']\s*$', fm, re.M)
    if qs:
        return 'frontmatter', qs

    zona = _zona_faq(cuerpo)
    if zona is None:
        return None, []

    # Molde A: <h3>¿pregunta?</h3><p>respuesta</p>
    qs = [re.sub(r'<[^>]+>', '', q).strip()
          for q in re.findall(r'<h[34][^>]*>(.*?)</h[34]>', zona, re.S)]
    # Molde B: <p><strong>¿pregunta?</strong><br /> respuesta</p>
    if not qs:
        qs = [re.sub(r'<[^>]+>', '', q).strip()
              for q in re.findall(r'<p[^>]*>\s*<strong>(.*?)</strong>', zona, re.S)]
    return 'cuerpo', [q for q in qs if q]


def clasifica(a, b, vacias):
    ta, tb = tokens(a, vacias), tokens(b, vacias)
    if not ta or not tb:
        return None, 0.0
    sa, sb = set(ta), set(tb)
    jac = len(sa & sb) / len(sa | sb)
    rat = difflib.SequenceMatcher(None, ' '.join(ta), ' '.join(tb)).ratio()
    if sa == sb:
        return 'IDENTICA', max(jac, rat)
    da, db = es_definicion(a), es_definicion(b)
    if da is not None and db is not None:
        # Las dos preguntan «qué es»: duplicado si el SUJETO es el mismo.
        # El sujeto se compara TAMBIÉN por ratio de secuencia, no sólo por
        # tokens: las variantes de grafía —que es de donde salen la mitad de
        # estos duplicados— no comparten token ninguno. «chilli crisp» y
        # «chili crisp» dan Jaccard 0,33 y se colaban.
        sda, sdb = set(tokens(da, vacias)), set(tokens(db, vacias))
        if not (sda and sdb):
            pass
        elif (len(sda & sdb) / len(sda | sdb) >= 0.5
              or difflib.SequenceMatcher(None, sin_tildes(da), sin_tildes(db)).ratio() >= 0.8):
            return 'DEFINICION', max(jac, rat)
    if jac >= 0.55 or rat >= 0.75:
        return 'PARECIDA', max(jac, rat)
    return None, max(jac, rat)


ORDEN = {'IDENTICA': 0, 'DEFINICION': 1, 'PARECIDA': 2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='es', choices=['es', 'en', 'it', 'todos'])
    ap.add_argument('--nivel', default='definicion',
                    choices=['identica', 'definicion', 'parecida'],
                    help='hasta qué nivel reportar (por defecto, sin las PARECIDA)')
    args = ap.parse_args()

    idiomas = ['es', 'en', 'it'] if args.lang == 'todos' else [args.lang]
    tope = ORDEN[args.nivel.upper()] if args.nivel.upper() in ORDEN else 1
    total = {'posts': 0, 'frontmatter': 0, 'cuerpo': 0, 'sin_faq': 0}
    hallazgos = []

    for lang in idiomas:
        vacias = {'en': VACIAS_EN, 'it': VACIAS_IT}.get(lang, VACIAS_ES)
        for p in sorted((CONTENT / lang).glob('*.md')):
            total['posts'] += 1
            fuente, qs = preguntas_de(p.read_text(encoding='utf-8'))
            if not qs:
                total['sin_faq'] += 1
                continue
            total[fuente] += 1
            for (i, a), (j, b) in itertools.combinations(list(enumerate(qs)), 2):
                nivel, score = clasifica(a, b, vacias)
                if nivel and ORDEN[nivel] <= tope:
                    hallazgos.append((ORDEN[nivel], nivel, lang, p.stem, fuente,
                                      len(qs), i + 1, a, j + 1, b, score))

    print('%(posts)d posts · %(frontmatter)d con `faq:` en frontmatter · '
          '%(cuerpo)d con FAQ sólo en el cuerpo · %(sin_faq)d sin FAQ' % total)
    print('%d pares marcados hasta el nivel %s\n' % (len(hallazgos), args.nivel.upper()))

    actual = None
    for _, nivel, lang, slug, fuente, n, i, a, j, b, score in sorted(hallazgos):
        if nivel != actual:
            actual = nivel
            print('── %s ' % nivel + '─' * (68 - len(nivel)))
        # El frontmatter emite FAQPage; el cuerpo sólo se ve en pantalla.
        marca = '★ schema' if fuente == 'frontmatter' else '  cuerpo'
        print('  [%s] %s/%s  (%d preguntas · %.2f)' % (marca, lang, slug, n, score))
        print('     #%-2d %s' % (i, a))
        print('     #%-2d %s' % (j, b))

    return 1 if any(h[0] <= 1 for h in hallazgos) else 0


if __name__ == '__main__':
    sys.exit(main())
