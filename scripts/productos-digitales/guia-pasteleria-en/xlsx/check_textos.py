#!/usr/bin/env python3
"""Comprueba un textos_en/<libro>.json antes de aplicarlo (ligero, Mac).

    python3 check_textos.py <libro.xlsx> [--avisos]

Errores: falta un índice o sobra uno · residuo de español (gate_md_en.residuo) · «€»/EUR/euros · un nombre de
pestaña que no es el de config_en.LIBROS[libro]['hojas'] · un ítem de lista desplegable con coma o la lista entera
> 255 caracteres · las claves fijas de DECISIONES §5 (tabla de sueldos) o de config (EN_NO, EN_SIN_IVA) traducidas
distinto · una cadena vacía donde el ES tiene texto. Sale con 1 si hay errores.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent))
import config_en as C            # noqa: E402
import gate_md_en as G           # noqa: E402

FIJAS = {
    'Técnicos y titulados superiores': 'Office and administration (degree-level)',
    'Dirección, jefes y encargados': 'Management and supervisors',
    'Personal especialista': 'Skilled specialists',
    'Personal cualificado': 'Qualified staff',
    'Personal de apoyo': 'Support staff',
    'Servicios auxiliares': 'Auxiliary services',
    'Jefe Pastelero': 'Head Pastry Chef',
    'Pastelero': 'Pastry Cook',
    'Ayudante': 'Bakery Assistant',
    'Dependiente Vitrina': 'Counter Associate',
    'No': C.EN_NO,
    'sin IVA': C.EN_SIN_IVA,
    'Sí': 'Yes',
}


def main():
    libro = sys.argv[1]
    ver_avisos = '--avisos' in sys.argv
    es = json.load(open(AQUI / 'textos_es.json'))[libro]
    ruta = AQUI / 'textos_en' / (libro[:-5] + '.json')
    en = json.load(open(ruta))
    cad = list(es.keys())
    E, A = [], []
    want = {str(i) for i in range(1, len(cad) + 1)}
    if set(en) - want:
        E.append('índices que no existen: %s' % sorted(set(en) - want, key=int)[:10])
    if want - set(en):
        E.append('faltan %d índices: %s' % (len(want - set(en)), sorted(want - set(en), key=int)[:15]))
    hojas = C.LIBROS[libro]['hojas']
    for i, s in enumerate(cad, 1):
        t = en.get(str(i))
        if t is None:
            continue
        lugares = es[s]
        if not isinstance(t, str):
            E.append('%d: no es texto' % i)
            continue
        if s.strip() and not t.strip():
            E.append('%d: vacía (ES %r)' % (i, s[:50]))
        if 'sheetname' in lugares and t != hojas.get(s):
            E.append('%d: pestaña %r ≠ %r (config)' % (i, t, hojas.get(s)))
        if any('DVlist' in w for w in lugares) and ',' in t:
            E.append('%d: ítem de lista con coma: %r' % (i, t))
        if s in FIJAS and t != FIJAS[s]:
            E.append('%d: clave fija %r debe ser %r (es %r)' % (i, s, FIJAS[s], t))
        if re.search(r'€|\bEUR\b|\beuros?\b', t, re.I):
            E.append('%d: moneda europea: %r' % (i, t[:80]))
        errs, avs = G.residuo(t, densidad=len(t.split()) >= 8)
        if errs:
            E.append('%d: %s · %r' % (i, errs[0], t[:80]))
        A += ['%d: %s' % (i, a) for a in avs]
        if len(t) > 1.8 * max(len(s), 20) and not any('[comment]' in w for w in lugares):
            A.append('%d: muy larga (%d vs %d)' % (i, len(t), len(s)))
    # listas desplegables completas ≤ 255
    for s, lugares in es.items():
        pass
    print('%s: %d cadenas · %d errores · %d avisos' % (libro, len(cad), len(E), len(A)))
    for e in E[:40]:
        print('  ERROR', e)
    if ver_avisos:
        for a in A[:60]:
            print('  aviso', a)
    sys.exit(1 if E else 0)


if __name__ == '__main__':
    main()
