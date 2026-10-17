#!/usr/bin/env python3
"""
heredar.py — memoria de traducción de un vertical del circuito de checklists (kit.py) sobre el kit base.
Sesión Claude Code, 18-oct-2026 (Bar Checklists Kit Pro).

    python3 heredar.py --kit bar

Lee `<v>/textos_es.json` (extraer_textos.py --kit <v>) y el kit base ya traducido (`textos_es.json` +
`textos_en/G*.json`, revisado en su F2) y escribe en `<v>/textos_en/`:

  · heredado.json   {id: {"en", "origen" (id del base), "via", "ajustes"}} — cadena ES IDÉNTICA a una del base
                    (via «exacta») o idéntica salvo el sufijo de variante (via «sufijo», mapas.SUFIJO_A_BASE: el EN
                    del base ya no lo lleva, D2). Ajustes deterministas: los nombres de fichero EN del base → los
                    del vertical y las pestañas citadas cuyo EN cambia (entre comillas dobles rectas).
  · pendientes.json lo nuevo o distinto, para UN traductor: id, es, contexto, pistas, adaptar, citas y, si viene
                    del base pero no vale tal cual, `base_en` como referencia y el `motivo`.

Una cadena idéntica NO se hereda (va a pendientes) si: lleva un ADAPTAR del vertical distinto del base
(«adaptar»); su EN nombra lo que el vertical no tiene (mapas.RX_CONTEXTO_PENDIENTE: «contexto»); o, tras los
ajustes, le falta el EN exacto de una pestaña o fichero citado («cita»). No traduce nada (regla 1bis).
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import kit                                                       # noqa: E402
from kit import mapas                                            # noqa: E402

RX_CONTEXTO = re.compile(getattr(mapas, 'RX_CONTEXTO_PENDIENTE', r'(?!x)x'))


def cargar_base():
    te = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
    en = {}
    for p in sorted(glob.glob(os.path.join(AQUI, 'textos_en', 'G[0-9].json'))):
        en.update(json.load(open(p, encoding='utf-8')))
    por_es = {}
    for c in te['cadenas']:
        if c['grupo'] != 'GM' and c['id'] in en:
            por_es[c['es']] = (c, en[c['id']])
    return por_es


def ajustar(en, cb, cv):
    """EN del base → EN del vertical: ficheros y pestañas citados. Devuelve (en, ajustes, problemas)."""
    ajustes, problemas = [], []
    for c in cv.get('cita_ficheros', []):
        viejo = kit.mapas_base.FICHEROS.get(c['es'])
        if viejo and viejo != c['en'] and viejo in en:
            en = en.replace(viejo, c['en'])
            ajustes.append('fichero %s → %s' % (viejo, c['en']))
    rot_b = {c['es']: c['en'] for c in cb.get('cita_rotulos', [])}
    for c in cv.get('cita_rotulos', []):
        viejo = rot_b.get(c['es'])
        if c['en'] and viejo and viejo != c['en']:
            if ('"%s"' % viejo) in en:
                en = en.replace('"%s"' % viejo, '"%s"' % c['en'])
                ajustes.append('pestaña "%s" → "%s"' % (viejo, c['en']))
            else:
                problemas.append('cita «%s»: el EN del base no trae "%s"' % (c['es'], viejo))
    for c in cv.get('cita_rotulos', []):
        if c['en'] and c['en'] not in en:
            problemas.append('falta el EN exacto "%s"' % c['en'])
    for c in cv.get('cita_ficheros', []):
        if c['en'] not in en:
            problemas.append('falta el fichero %s' % c['en'])
    return en, ajustes, problemas


def main():
    ap = argparse.ArgumentParser(description='memoria de traducción de un vertical sobre el kit base')
    kit.argumento(ap)
    args = ap.parse_args()
    if kit.BASE:
        raise SystemExit('heredar.py es para un vertical: --kit <v>')
    base = cargar_base()
    tv = json.load(open(os.path.join(kit.DATOS, 'textos_es.json'), encoding='utf-8'))
    sufijos = list(getattr(mapas, 'SUFIJO_A_BASE', []))
    heredado, pendientes = OrderedDict(), []
    motivos, vias = Counter(), Counter()
    for c in tv['cadenas']:
        if c['grupo'] == 'GM':
            continue
        via, hit = 'exacta', base.get(c['es'])
        if hit is None:
            es2 = c['es']
            for a, b in sufijos:
                es2 = es2.replace(a, b)
            if es2 != c['es']:
                via, hit = 'sufijo', base.get(es2)
        motivo, base_en, extra = 'nueva', None, None
        if hit is not None:
            cb, en_b = hit
            base_en = en_b
            en, ajustes, problemas = ajustar(en_b, cb, c)
            if c.get('adaptar') and c.get('adaptar') != cb.get('adaptar'):
                motivo = 'adaptar'
            elif RX_CONTEXTO.search(en):
                motivo, extra = 'contexto', RX_CONTEXTO.search(en).group(0)
            elif problemas:
                motivo, extra = 'cita', '; '.join(problemas)
            else:
                heredado[c['id']] = OrderedDict([('en', en), ('origen', cb['id']), ('via', via)]
                                                + ([('ajustes', ajustes)] if ajustes else []))
                vias[via] += 1
                continue
        motivos[motivo] += 1
        p = OrderedDict([('id', c['id']), ('es', c['es']), ('grupo', c['grupo']), ('palabras', c['palabras']),
                         ('donde', ['%s · %s · %s' % (d['f'], d['h'], d.get('c')) for d in c['donde'][:3]]
                          + (['… +%d' % (len(c['donde']) - 3)] if len(c['donde']) > 3 else []))])
        for k in ('pistas', 'adaptar', 'cita_rotulos', 'cita_ficheros', 'comun'):
            if c.get(k):
                p[k] = c[k]
        p['motivo'] = motivo + (': ' + extra if extra else '')
        if base_en:
            p['base_en'] = base_en
        pendientes.append(p)
    salida = os.path.join(kit.DATOS, 'textos_en')
    os.makedirs(salida, exist_ok=True)
    with open(os.path.join(salida, 'heredado.json'), 'w', encoding='utf-8') as fh:
        json.dump(heredado, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    pal = sum(p['palabras'] for p in pendientes)
    meta = OrderedDict([
        ('kit', kit.NOMBRE), ('producto', mapas.PRODUCTO),
        ('n_pendientes', len(pendientes)), ('n_palabras', pal), ('motivos', dict(motivos)),
        ('n_heredadas', len(heredado)), ('heredadas_por_via', dict(vias)),
        ('salida_traductor', 'textos_en/G1.json = {id: en} con TODOS los ids de esta lista (ni uno más)'),
        ('referencias', ['bar/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la prosa '
                         'del kit base)', 'bar/textos_en/heredado.json (cómo se dijo ya cada cosa)',
                         'bar/mapas_bar.py: GLOSARIO, HOJAS, FICHEROS, TITULOS', '../GLOSARIO-JERGA-ES-EN.md']),
        ('base_en', 'traducción del kit base de una cadena igual o casi: referencia de estilo; NO vale tal cual '
                    '(ver motivo)'),
    ])
    with open(os.path.join(salida, 'pendientes.json'), 'w', encoding='utf-8') as fh:
        json.dump(OrderedDict([('meta', meta), ('cadenas', pendientes)]), fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    pal_h = sum(c['palabras'] for c in tv['cadenas'] if c['id'] in heredado)
    print('heredado.json: %d cadenas (%s) · %d palabras' % (len(heredado), dict(vias), pal_h))
    print('pendientes.json: %d cadenas (%s) · %d palabras' % (len(pendientes), dict(motivos), pal))


if __name__ == '__main__':
    main()
