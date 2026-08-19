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
    python3 scripts/astro-migration/fase8d-faq-duplicadas.py [--lang es|en|it|fr|de|pt|todos]
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
# 2026-08-16 — blog francés. La elisión es MÁS frecuente que en italiano y aquí
# hay un detalle que la lista italiana no vio: tokens() borra el apóstrofo
# (`[^a-z0-9ñ ]` → espacio), así que «qu'est-ce que l'HACCP» se parte en
# «qu / est / ce / que / l / haccp». Poner "l'" en la lista NO sirve de nada
# —ese token no existe nunca—; lo que hay que listar son las formas SUELTAS
# (l, d, qu, n, s, c, j, m, t). Se listan las dos por si algún día tokens()
# deja de comerse el apóstrofo.
VACIAS_FR = {'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'au', 'aux',
             'en', 'et', 'ou', 'que', 'qui', 'quoi', 'est', 'sont', 'a', 'ce',
             'cet', 'cette', 'ces', 'pour', 'avec', 'par', 'dans', 'sur', 'se',
             'son', 'sa', 'ses', 'il', 'elle', 'on', 'y', 'ne', 'pas', 'plus',
             'comment', 'quel', 'quelle', 'quels', 'quelles', 'etre', 'faire',
             'l', 'd', 'qu', 'n', 's', 'c', 'j', 'm', 't',
             "l'", "d'", "qu'", "n'", "s'", "c'", "j'", "m'", "t'"}
# 2026-08-18 — blog alemán. Los tokens llegan ya normalizados por sin_tildes():
# las diéresis caen (für→fur, müssen→mussen) y el ß se transcribe a ss ANTES del
# regex de tokens() — sin esa transcripción «heißt» quedaría partido en
# «hei / t», porque el ß no se descompone en NFD y el filtro [^a-z…] lo borra.
# Por eso la lista se escribe SIN diéresis y con ss.
VACIAS_DE = {'der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine', 'einen',
             'einem', 'einer', 'eines', 'und', 'oder', 'in', 'im', 'an', 'am',
             'auf', 'fur', 'mit', 'von', 'vom', 'zu', 'zum', 'zur', 'bei',
             'ist', 'sind', 'was', 'wie', 'welche', 'welcher', 'welches',
             'man', 'kann', 'darf', 'muss', 'soll', 'sollte', 'es', 'sich',
             'nicht', 'nach', 'aus', 'uber', 'wird', 'werden', 'sein', 'hat',
             'haben', 'gibt', 'viel', 'viele', 'lange', 'oft', 'wann', 'wo',
             'warum', 'wozu', 'wer', 'ich', 'sie', 'ihr', 'ihre', 'ihren'}
# 2026-08-19 — blog portugués. Los tokens llegan normalizados por sin_tildes():
# las tildes y la cedilla caen en NFD (ã→a, ç→c, é→e), así que la lista se
# escribe SIN diacríticos («nao», «sao», «e» cubre «é»). El PT-PT contrae
# preposición+artículo con formas propias (no/na/nos/nas = em+o…, ao/a =
# a+o…, pelo/pela = por+o…, dum/duma) que el ES no tiene.
VACIAS_PT = {'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas', 'de', 'do',
             'da', 'dos', 'das', 'em', 'no', 'na', 'nos', 'nas', 'e', 'ou',
             'que', 'ao', 'aos', 'pelo', 'pela', 'para', 'com', 'por', 'se',
             'seu', 'sua', 'seus', 'suas', 'ha', 'ser', 'esta', 'este',
             'sao', 'nao', 'qual', 'quais', 'como', 'quanto', 'quantos',
             'onde', 'quando', 'deve', 'pode', 'tem', 'ter', 'fazer'}

# Arranques que marcan una pregunta de DEFINICIÓN.
DEFINICION = (
    re.compile(r'^(que es|que son|que significa|en que consiste)\b'),
    re.compile(r'^(what is|what are|what does .* mean)\b'),
    # Francés. Ojo: se compara sobre el texto YA normalizado (sin apóstrofos ni
    # guiones), así que «qu'est-ce que», «qu'est-ce qu'» y «c'est quoi» llegan
    # aquí como «qu est ce que», «qu est ce qu» y «c est quoi». El orden importa:
    # la alternativa larga va primero para que no gane el prefijo corto.
    re.compile(r'^(qu est ce que c est que|qu est ce que|qu est ce qu|'
               r'c est quoi|que signifie|que veut dire|a quoi sert)\b'),
    # Alemán. Se compara sobre el texto normalizado (ß→ss, sin diéresis), así
    # que «was heißt» llega como «was heisst». «was versteht man unter» es la
    # fórmula de manual; va primero para que no gane un prefijo corto.
    re.compile(r'^(was versteht man unter|was bedeutet|was heisst|'
               r'was ist|was sind)\b'),
    # Portugués. Se compara sobre el texto normalizado (sin tildes ni cedilla),
    # así que «o que é» llega como «o que e» y «o que são» como «o que sao».
    # La fórmula nominal «haccp o que é» (que en PT gana a la interrogativa,
    # regla 5 del roadmap) la cubre la rama de orden invertido de
    # es_definicion(): acaba en «que e», que se añade allí.
    re.compile(r'^(o que e|o que sao|o que significa|em que consiste|'
               r'para que serve)\b'),
)


def sin_tildes(s):
    # ß→ss ANTES de normalizar: la eszett no se descompone en NFD y el filtro
    # [^a-z0-9ñ ] de tokens() la borraría, partiendo «heißt» en «hei / t».
    s = unicodedata.normalize('NFD', s.lower().replace('ß', 'ss'))
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
    # «¿Chili Crisp qué es?» — el PAA también invierte el orden. La variante
    # portuguesa es «haccp o que é» (normalizada: «haccp o que e»), que además
    # es la forma GANADORA en PT (×6,5 sobre «o que é haccp», regla 5 del
    # roadmap): sin esta rama, la formulación más frecuente del PAA portugués
    # no contaría como definición.
    if re.search(r'\bque es\b\s*$', plano):
        return plano[:plano.rfind('que es')].strip()
    if re.search(r'\bo que e\b\s*$', plano):
        return plano[:plano.rfind('o que e')].strip()
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
    ap.add_argument('--lang', default='es', choices=['es', 'en', 'it', 'fr', 'de', 'pt', 'todos'])
    ap.add_argument('--nivel', default='definicion',
                    choices=['identica', 'definicion', 'parecida'],
                    help='hasta qué nivel reportar (por defecto, sin las PARECIDA)')
    args = ap.parse_args()

    idiomas = ['es', 'en', 'it', 'fr', 'de', 'pt'] if args.lang == 'todos' else [args.lang]
    tope = ORDEN[args.nivel.upper()] if args.nivel.upper() in ORDEN else 1
    total = {'posts': 0, 'frontmatter': 0, 'cuerpo': 0, 'sin_faq': 0}
    hallazgos = []

    for lang in idiomas:
        vacias = {'en': VACIAS_EN, 'it': VACIAS_IT, 'fr': VACIAS_FR, 'de': VACIAS_DE, 'pt': VACIAS_PT}.get(lang, VACIAS_ES)
        carpeta = CONTENT / lang
        if not carpeta.is_dir():
            # Un blog recién abierto puede no tener aún la carpeta (el francés
            # nació el 2026-08-16 con el árbol de rutas y 0 posts). No es un
            # error: es 0 posts que revisar.
            print('· %s: sin carpeta de contenido todavía (0 posts)' % lang)
            continue
        for p in sorted(carpeta.glob('*.md')):
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
