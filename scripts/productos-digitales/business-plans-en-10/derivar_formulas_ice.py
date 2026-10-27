#!/usr/bin/env python3
"""
derivar_formulas_ice.py — Ice Cream Shop Business Plan Kit (EN) · FORMULAS_EN de HELP derivadas de sus gemelas ya
traducidas (SPEC D197; sesión Claude Code, 27-oct-2026, F2-EN paso 1a). Solo JSON (Mac o VPS, sin openpyxl).

Clon de `../business-plans-en-8/derivar_formulas_piz.py` con CUATRO fuentes de gemelas, en este orden: la PIZZA EN (la
celda de la pizzería ES ↔ su EN publicado: `../business-plans-en-8/censo_es.json` + `formulas_piz.json`), REST/PAN
(la panadería ES 2.2 es la semilla del libro: `../business-plans-en-2/censo_es.json` + `formulas_rp.json`), el BAR EN y
FT/CAF. Mismo ESQUELETO (literales idénticos, referencias como marcador, pestañas canónicas) → EN de la gemela con las
referencias reescritas. Las que no tienen gemela (C9, D28, D38 y F13: inv. §2.1) van a mano en
`formulas_ice_manual.py`. Escribe `formulas_ice.json` y falla si queda alguna sin EN o con español en un literal.

    python3 derivar_formulas_ice.py         (o: python3 bp10.py derivar_formulas)
"""
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
BP = os.path.join(PD, 'business-plans-en')
BP2 = os.path.join(PD, 'business-plans-en-2')
BAR = os.path.join(PD, 'business-plans-en-3')
PIZ = os.path.join(PD, 'business-plans-en-8')
sys.path.insert(0, BP)
sys.path.insert(0, BP2)
sys.path.insert(0, PIZ)
sys.path.insert(0, AQUI)
os.environ.pop('BP_CONJUNTO', None)
import mapas as M                                                # noqa: E402  (ftcaf: FORMULAS_EN de FT/CAF)
import mapas_rp as RP                                            # noqa: E402
import mapas_piz as PZ                                           # noqa: E402
import mapas_ice as B                                            # noqa: E402

RX_STR = re.compile(r'"(?:[^"]|"")*"')
RX_REF = re.compile(r"(?<![\w$.'!])(?:(?:'((?:[^']|'')+)'|([A-Za-z_][\w.]*))!)?(\$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?)"
                    r"(?![\w(])")
HOJAS = OrderedDict()
HOJAS.update(M.HOJAS_POR_LIBRO)
HOJAS.update(RP.HOJAS_POR_LIBRO)
HOJAS.update(PZ.HOJAS_POR_LIBRO)
HOJAS['BARP'] = PZ.HOJAS_POR_LIBRO['PIZP']                    # el libro del Bar = mismas pestañas
HOJAS.update(B.HOJAS_POR_LIBRO)


def trozos(f):
    out, pos = [], 0
    for m in RX_STR.finditer(f):
        out += _refs(f[pos:m.start()])
        out.append(('lit', m.group(0)))
        pos = m.end()
    return out + _refs(f[pos:])


def _refs(s):
    out, pos = [], 0
    for m in RX_REF.finditer(s):
        if m.start() > pos:
            out.append(('txt', s[pos:m.start()]))
        hoja = m.group(1) if m.group(1) is not None else m.group(2)
        out.append(('ref', ((hoja.replace("''", "'") if hoja else None), m.group(3))))
        pos = m.end()
    if pos < len(s):
        out.append(('txt', s[pos:]))
    return out


def esqueleto(f):
    return tuple((t, v if t != 'ref' else (None if v[0] is None else M.norm_hoja(v[0]))) for t, v in trozos(f))


def ref_hoja(nombre):
    if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', nombre):
        return nombre
    return "'" + nombre.replace("'", "''") + "'"


def _de_censo(carpeta, fichero_en, ref):
    cen = json.load(open(os.path.join(carpeta, 'censo_es.json'), encoding='utf-8'))
    fen = json.load(open(os.path.join(carpeta, fichero_en), encoding='utf-8'))
    for info in cen['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for x, f in hd['formulas_texto'].items():
                k = '%s|%s|%s' % (info['corto'], h, x)
                if k in fen:
                    ref.append(((info['corto'], h, x), f, fen[k]['en']))


def gemelas():
    """[(corto, hoja ES, celda), fórmula ES, fórmula EN] de la PIZZA EN (primero), REST/PAN, BAR y FT/CAF."""
    ref = []
    _de_censo(PIZ, 'formulas_piz.json', ref)
    _de_censo(BP2, 'formulas_rp.json', ref)
    _de_censo(BAR, 'formulas_bar.json', ref)
    cen = json.load(open(os.path.join(BP, 'censo_es.json'), encoding='utf-8'))
    for info in cen['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for x, f in hd['formulas_texto'].items():
                k = (info['corto'], h, x)
                if k in M.FORMULAS_EN:
                    ref.append((k, f, M.FORMULAS_EN[k]))
    return ref


def main():
    cen = json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))
    try:
        from formulas_ice_manual import MANUAL
    except ImportError:
        MANUAL = {}
    ref = gemelas()
    inv_en = {c: {en: es for es, en in d.items()} for c, d in HOJAS.items()}
    out, pend = OrderedDict(), []
    for info in cen['libros'].values():
        c = info['corto']
        for h, hd in info['hojas_detalle'].items():
            for x, f in hd['formulas_texto'].items():
                clave = '%s|%s|%s' % (c, h, x)
                if clave in MANUAL:
                    out[clave] = OrderedDict([('en', MANUAL[clave]), ('de', None), ('metodo', 'manual')])
                    continue
                esq = esqueleto(f)
                cands = [(k, fes, fen) for k, fes, fen in ref
                         if M.norm_hoja(k[1]) == M.norm_hoja(h) and esqueleto(fes) == esq]
                hecho = None
                for k, fes, fen in cands:
                    a, b = [v for t, v in trozos(fes) if t == 'ref'], [v for t, v in trozos(f) if t == 'ref']
                    mapa, ok = {}, True
                    for (ha, ca), (hb, cb) in zip(a, b):
                        ka = (M.norm_hoja(ha) if ha else M.norm_hoja(k[1]), ca)
                        kb = (M.norm_hoja(hb) if hb else M.norm_hoja(h), cb)
                        if mapa.setdefault(ka, kb) != kb:
                            ok = False
                    if not ok:
                        continue
                    partes = []
                    for t, v in trozos(fen):
                        if t != 'ref':
                            partes.append(v)
                            continue
                        hen, cel = v
                        hes = inv_en[k[0]].get(hen) if hen else k[1]
                        if hes is None or (M.norm_hoja(hes), cel) not in mapa:
                            ok = False
                            break
                        h2, c2 = mapa[(M.norm_hoja(hes), cel)]
                        h2_real = next(r for r in B.HOJAS_POR_LIBRO[c] if M.norm_hoja(r) == h2)
                        partes.append((ref_hoja(B.HOJAS_POR_LIBRO[c][h2_real]) + '!' if hen else '') + c2)
                    if ok:
                        hecho = (k, ''.join(partes))
                        break
                if hecho:
                    out[clave] = OrderedDict([('en', hecho[1]), ('de', '%s|%s|%s' % hecho[0]), ('metodo', 'auto')])
                else:
                    cerca = [('%s|%s|%s' % k, fen) for k, fes, fen in ref if M.norm_hoja(k[1]) == M.norm_hoja(h)]
                    pend.append(OrderedDict([('clave', clave), ('es', f), ('gemelas_misma_hoja', cerca[:3])]))
    err, avi = [], []
    hojas_es = {h for d in B.HOJAS_POR_LIBRO.values() for h in d}
    hojas_en = {e for d in B.HOJAS_POR_LIBRO.values() for e in d.values()}
    rx_no = re.compile(r'(?i)\bpizz|(?<!cookie )\bdough\b|\bovens?\b|\bcovers?\b|\bbread\b|\bbakery\b|\bbeer\b')
    for k, d in out.items():
        for t, v in trozos(d['en']):
            if t == 'ref' and v[0] and v[0] in hojas_es and v[0] not in hojas_en:
                err.append('%s cita la pestaña ES %r' % (k, v[0]))
            if t == 'lit':
                lit = v[1:-1]
                r = [x for x in M.restos_espanol(lit) if not x[0].startswith('oficio')]
                if r or '€' in lit:
                    err.append('%s con español en un literal: %r %s' % (k, lit[:50], r[:1]))
                if rx_no.search(lit):
                    err.append('%s con vocabulario de otro negocio en un literal: %r' % (k, rx_no.search(lit).group(0)))
                if len(lit.replace('""', '"')) > 255:
                    # Excel limita a 255 caracteres cada literal de texto de una fórmula: en las manuales es error
                    # (se trocean con «"…"&"…"»); en las derivadas, aviso (las gemelas publicadas ya lo superan)
                    (err if d['metodo'] == 'manual' else avi).append(
                        '%s: literal de %d caracteres (> 255, Excel)' % (k, len(lit)))
    json.dump(out, open(os.path.join(AQUI, 'formulas_ice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(pend, open(os.path.join(AQUI, 'formulas_ice_pendientes.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    n_auto = sum(1 for d in out.values() if d['metodo'] == 'auto')
    print('formulas_ice.json: %d (auto %d, manual %d) · pendientes %d → formulas_ice_pendientes.json' % (
        len(out), n_auto, len(out) - n_auto, len(pend)))
    for p in pend:
        print('  PENDIENTE', p['clave'])
    for e in avi:
        print('AVISO', e)
    for e in err:
        print('ERROR', e)
    return 1 if (pend or err) else 0


if __name__ == '__main__':
    sys.exit(main())
