#!/usr/bin/env python3
"""
anotar_tandas_docx.py — añade a `tandas/taq_a.entrada.json` e `taq_b.entrada.json` (las que escribe `bp12.py
preparar_tandas`) las CIFRAS FINALES del caso US, leídas de `cifras_caso.json` (la caché del libro EN calibrado que deja
`aplicar_en`), para que los traductores del Word entiendan el caso (signo del pesimista, qué cifra es grande o pequeña,
mes del saldo mínimo). En el texto siguen yendo SOLO los tokens `{{…}}` (`check_textos` rechaza importes «$»
fuera de tokens que no estén en research/SPEC). Solo JSON (Mac). Sesión Claude Code, 29-oct-2026 (F2-EN, paso 3).

    python3 scripts/productos-digitales/business-plans-en-12/bp12.py preparar_tandas
    python3 scripts/productos-digitales/business-plans-en-12/anotar_tandas_docx.py
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
CLAVE = 'cifras_del_caso (SOLO para entender el caso: en el texto escribe SIEMPRE el token {{…}}, nunca la cifra)'


def main():
    cif = json.load(open(os.path.join(AQUI, 'cifras_caso.json'), encoding='utf-8'))
    caso = cif['taq']
    for tanda in ('taq_a', 'taq_b'):
        p = os.path.join(AQUI, 'tandas', '%s.entrada.json' % tanda)
        d = json.load(open(p, encoding='utf-8'), object_pairs_hook=OrderedDict)
        faltan = [t for t in d['tokens'] if t not in caso]
        if faltan:
            print('ERROR %s: tokens sin cifra en cifras_caso.json: %s' % (tanda, faltan))
            return 1
        valores = OrderedDict((t, caso[t]['texto']) for t in d['tokens'])
        out = OrderedDict()
        for k, v in d.items():
            if k == CLAVE:
                continue
            out[k] = v
            if k == 'tokens':
                out[CLAVE] = valores
        out['generado_cifras'] = cif['meta'].get('generado')
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('tandas/%s.entrada.json: %d párrafos · %d palabras · %d tokens con su cifra final' % (
            tanda, d['n_parrafos'], d['n_palabras'], len(valores)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
