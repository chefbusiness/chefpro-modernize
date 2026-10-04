#!/usr/bin/env python3
"""
derivar_formulas.py — Restaurant + Bakery Business Plan Kit (EN) · FORMULAS_EN de RESTP/PANP derivadas de las de
FT/CAF (sesión Claude Code, 4-oct-2026, F2 tanda 1). Solo JSON (Mac o VPS, sin openpyxl).

Las 32 fórmulas con literales de texto de RESTP y PANP son, casi todas, las MISMAS 33 de FT/CAF con otras
referencias (F1-inventario-delta §2.8). Para cada una se busca en FT/CAF una fórmula ES con el mismo ESQUELETO
(literales idénticos y la misma forma, con las referencias sustituidas por un marcador y las pestañas por su nombre
canónico); si la hay, se toma su EN de `formulas_en.py` y se le reescriben las referencias con el mapa posición a
posición FT→REST (debe ser una función y cubrir todas las referencias de la EN). Las que no tienen gemela exacta van a
`MANUAL` en `formulas_rp_manual.py` (EN escrita a mano con la misma redacción). Escribe `formulas_rp.json`:

    {"RESTP|0. Supuestos|C9": {"en": "=…", "de": "FTP|0. Supuestos|C9", "metodo": "auto" | "manual"}, …}

y falla si alguna fórmula de texto del censo queda sin EN o si una EN cita una pestaña o un literal en español.

    python3 derivar_formulas.py
"""
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
sys.path.insert(0, BASE)
sys.path.insert(0, AQUI)
os.environ.pop('BP_CONJUNTO', None)
import mapas as M                                                # noqa: E402  (conjunto ftcaf: FORMULAS_EN de FT/CAF)
import mapas_rp as RP                                            # noqa: E402

RX_STR = re.compile(r'"(?:[^"]|"")*"')
RX_REF = re.compile(r"(?<![\w$.'!])(?:(?:'((?:[^']|'')+)'|([A-Za-z_][\w.]*))!)?(\$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?)"
                    r"(?![\w(])")


def trozos(f):
    """[(tipo, valor)]: 'lit' (literal con comillas), 'ref' ((hoja o None, celda)), 'txt'."""
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


def canon_es(corto, hoja):
    return None if hoja is None else M.norm_hoja(hoja)


def esqueleto(corto, f, canon):
    return tuple((t, v if t != 'ref' else canon(corto, v[0])) for t, v in trozos(f))


def ref_hoja(nombre):
    if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', nombre):
        return nombre
    return "'" + nombre.replace("'", "''") + "'"


def main():
    cen_ref = json.load(open(os.path.join(BASE, 'censo_es.json'), encoding='utf-8'))
    cen = json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))
    try:
        from formulas_rp_manual import MANUAL
    except ImportError:
        MANUAL = {}
    # gemelas FT/CAF: (corto, hoja ES, celda) → (fórmula ES, fórmula EN)
    ref = []
    for info in cen_ref['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for x, f in hd['formulas_texto'].items():
                k = (info['corto'], h, x)
                if k in M.FORMULAS_EN:
                    ref.append((k, f, M.FORMULAS_EN[k]))
    inv_en = {c: {en: es for es, en in M.HOJAS_POR_LIBRO[c].items()} for c in M.HOJAS_POR_LIBRO}
    out, pend = OrderedDict(), []
    for info in cen['libros'].values():
        c = info['corto']
        for h, hd in info['hojas_detalle'].items():
            for x, f in hd['formulas_texto'].items():
                clave = '%s|%s|%s' % (c, h, x)
                if clave in MANUAL:
                    out[clave] = OrderedDict([('en', MANUAL[clave]), ('de', None), ('metodo', 'manual')])
                    continue
                esq = esqueleto(c, f, canon_es)
                cands = [(k, fes, fen) for k, fes, fen in ref if M.norm_hoja(k[1]) == M.norm_hoja(h) and
                         esqueleto(k[0], fes, canon_es) == esq]
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
                    partes, ok = [], True
                    for t, v in trozos(fen):
                        if t != 'ref':
                            partes.append(v)
                            continue
                        hen, cel = v
                        hes = inv_en[k[0]].get(hen) if hen else k[1]
                        if hes is None:
                            ok = False
                            break
                        kk = (M.norm_hoja(hes), cel)
                        if kk not in mapa:
                            ok = False
                            break
                        h2, c2 = mapa[kk]
                        h2_real = next(r for r in RP.HOJAS_POR_LIBRO[c] if M.norm_hoja(r) == h2)
                        h2_en = RP.HOJAS_POR_LIBRO[c][h2_real]
                        partes.append((ref_hoja(h2_en) + '!' if hen else '') + c2)
                    if ok:
                        hecho = (k, ''.join(partes))
                        break
                if hecho:
                    out[clave] = OrderedDict([('en', hecho[1]), ('de', '%s|%s|%s' % hecho[0]), ('metodo', 'auto')])
                else:
                    cerca = [('%s|%s|%s' % k, fen) for k, fes, fen in ref if M.norm_hoja(k[1]) == M.norm_hoja(h)]
                    pend.append(OrderedDict([('clave', clave), ('es', f), ('gemelas_misma_hoja', cerca[:3])]))
    # comprobaciones
    err = []
    hojas_es = {h for d in RP.HOJAS_POR_LIBRO.values() for h in d}
    for k, d in out.items():
        en = d['en']
        for t, v in trozos(en):
            if t == 'ref' and v[0] and v[0] in hojas_es and v[0] not in {e for dd in RP.HOJAS_POR_LIBRO.values()
                                                                       for e in dd.values()}:
                err.append('%s cita la pestaña ES %r' % (k, v[0]))
            if t == 'lit':
                lit = v[1:-1]
                r = [x for x in M.restos_espanol(lit) if not x[0].startswith('oficio')]
                if r or '€' in lit:
                    err.append('%s con español en un literal: %r %s' % (k, lit[:50], r[:1]))
    json.dump(out, open(os.path.join(AQUI, 'formulas_rp.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(pend, open(os.path.join(AQUI, 'formulas_rp_pendientes.json'), 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    n_auto = sum(1 for d in out.values() if d['metodo'] == 'auto')
    print('formulas_rp.json: %d (auto %d, manual %d) · pendientes %d → formulas_rp_pendientes.json' % (
        len(out), n_auto, len(out) - n_auto, len(pend)))
    for p in pend:
        print('  PENDIENTE', p['clave'])
    for e in err:
        print('ERROR', e)
    return 1 if (pend or err) else 0


if __name__ == '__main__':
    sys.exit(main())
