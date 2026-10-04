#!/usr/bin/env python3
"""
preparar_tandas.py — entradas COMPACTAS para los traductores (BRIEF-TRADUCTORES.md). Solo JSON (corre en el Mac).

Lee textos_es.json, censo_es.json, docx_es_*.json, mapas.py y los glosarios del financial-kit, y escribe en
`tandas/`:
  · GM.entrada.json, GFT.entrada.json, GCAF.entrada.json   (xlsx)
      {"tanda", "salida", "reglas", "glosario", "pestanas", "claves", "fijos_en", "pistas": {"P01": texto…},
       "cadenas": [{"id", "es", "donde": ["FTP · 0. Supuestos!C4", …], "fila": rótulo ES de la col. A,
                    "valor_us": valor del caso US de esa fila (VALORES_EN), "max_len", "cita_hojas", "por_celda",
                    "pistas": ["P03", …]}]}
  · ft_a.entrada.json, ft_b.entrada.json, caf_a.entrada.json, caf_b.entrada.json   (docx)
      {"tanda", "plan", "salida", "secciones", "tokens": {nombre: descripción}, "fijos_que_no_escribes": {...},
       "parrafos": [{"i", "seccion", "rol", "palabras", "es", "nota"?}], "contexto_secciones": {...}}

    python3 preparar_tandas.py
"""
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas                                                     # noqa: E402

FIN = os.path.join(os.path.dirname(AQUI), 'financial-kit', 'textos_en')
SALIDA = os.path.join(AQUI, 'tandas')


def glosario():
    g = OrderedDict()
    for f in ('glosario.json', 'glosario-G2.json'):
        p = os.path.join(FIN, f)
        if os.path.exists(p):
            g.update(json.load(open(p, encoding='utf-8')))
    for k, v in mapas.GLOSARIO.items():
        g.setdefault(k, v)                                     # el del financial-kit manda (SPEC §2.3)
    return g


def main():
    os.makedirs(SALIDA, exist_ok=True)
    te = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
    censo = json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))
    por_corto = {i['corto']: i for i in censo['libros'].values()}
    glo = glosario()
    pestanas = OrderedDict((c, d) for c, d in mapas.HOJAS_POR_LIBRO.items())
    fijos = OrderedDict((k, v) for k, v in mapas.FIJOS.items())
    for g in ('GM', 'GFT', 'GCAF'):
        cad = [e for e in te['cadenas'] if e['grupo'] == g]
        cat = OrderedDict()
        out = []
        for e in cad:
            x = OrderedDict([('id', e['id']), ('es', e['es'])])
            dd = []
            fila_et, valores = None, OrderedDict()
            for o in e['donde'][:6]:
                dd.append('%s · %s!%s%s' % (o['f'], o.get('h', ''), o.get('c', ''),
                                            '' if o['t'] == 'celda' else ' (%s)' % o['t']))
            for o in e['donde']:
                m = re.fullmatch(r'([A-Z]+)(\d+)', o.get('c') or '')
                if o['t'] != 'celda' or not m or m.group(1) == 'A':
                    continue                                   # rótulos de fila: el valor no hace falta
                hd = por_corto[o['f']]['hojas_detalle'][o['h']]
                if fila_et is None:
                    fila_et = hd['etiquetas'].get(m.group(2))
                vals = OrderedDict((col, mapas.VALORES_EN[(o['f'], o['h'], col + m.group(2))][0])
                                   for col in 'BCDE' if (o['f'], o['h'], col + m.group(2)) in mapas.VALORES_EN)
                if vals and m.group(1) not in vals:
                    valores[o['f']] = vals if len(vals) > 1 else list(vals.values())[0]
            if len(e['donde']) > 6:
                dd.append('… y %d apariciones más' % (len(e['donde']) - 6))
            x['donde'] = dd
            if fila_et:
                x['fila'] = fila_et
            if valores:
                x['valor_us'] = valores if len(valores) > 1 else list(valores.values())[0]
            for k in ('max_len', 'cita_hojas', 'por_celda'):
                if k in e:
                    x[k] = e[k]
            refs = []
            for p in e.get('pistas', []):
                if p not in cat:
                    cat[p] = 'P%02d' % (len(cat) + 1)
                refs.append(cat[p])
            if refs:
                x['pistas'] = refs
            out.append(x)
        obj = OrderedDict([
            ('tanda', g), ('salida', 'scripts/productos-digitales/business-plans-en/textos_en/%s.json' % g),
            ('formato_salida', '{"<id>": "<texto EN>", …} con TODOS los ids de "cadenas" y nada más'),
            ('n_cadenas', len(out)), ('n_palabras', sum(len(e['es'].split()) for e in cad)),
            ('pistas', OrderedDict((v, k) for k, v in cat.items())),
            ('glosario', glo), ('pestanas_es_en', pestanas), ('claves_es_en', mapas.CLAVES),
            ('fijos_en (ya escritos por mapas.py: úsalos con esas mismas palabras cuando los cites)', fijos),
            ('cadenas', out),
        ])
        with open(os.path.join(SALIDA, '%s.entrada.json' % g), 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('tandas/%s.entrada.json: %d cadenas, %d palabras, %d pistas' % (g, len(out), obj['n_palabras'], len(cat)))
    for tanda, (plan, secs) in mapas.DOCX_TANDAS.items():
        de = json.load(open(os.path.join(AQUI, 'docx_es_%s.json' % plan), encoding='utf-8'))
        pars = []
        for k, e in de['parrafos'].items():
            if e.get('tanda') == tanda:
                x = OrderedDict([('i', int(k)), ('seccion', e['seccion']), ('rol', e['rol']),
                                 ('palabras', e['palabras']), ('es', e['texto'])])
                if 'nota' in e:
                    x['nota'] = e['nota']
                pars.append(x)
        fij = OrderedDict((str(i), t) for i, t in mapas.textos_fijos_docx(plan).items())
        obj = OrderedDict([
            ('tanda', tanda), ('plan', plan), ('producto', mapas.PLANES[plan]['producto']),
            ('salida', 'scripts/productos-digitales/business-plans-en/docx_en_%s.json' % tanda),
            ('formato_salida', '{"<i>": "<párrafo EN>", …} con TODOS los "i" de "parrafos" y nada más'),
            ('secciones', ['%d. %s' % (s, mapas.ENCABEZADOS_EN[s - 1]) for s in secs]),
            ('n_parrafos', len(pars)), ('n_palabras', sum(p['palabras'] for p in pars)),
            ('tokens', OrderedDict((t, '%s [%s]' % (desc, fmt)) for t, (fmt, src, desc) in mapas.tokens_de(plan).items())),
            ('movimiento_caf', mapas.DOCX_MOVER.get(plan)),
            ('fijos_que_no_escribes (portada, aviso, índice, encabezados, cierre: los pone ensamblar_docx.py)', fij),
            ('parrafos', pars),
        ])
        with open(os.path.join(SALIDA, '%s.entrada.json' % tanda), 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('tandas/%s.entrada.json: %d párrafos, %d palabras' % (tanda, len(pars), obj['n_palabras']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
