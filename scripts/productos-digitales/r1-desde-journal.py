#!/usr/bin/env python3
"""Reconstruye auditorias/<pid>-R1.json desde el journal.jsonl de un Workflow de ronda 1.

Por qué: el paso «Persistir» con un agente (haiku) reescribía el JSON y lo truncaba (pasó
con kit-escandallos y pack-appcc el 2026-08-22). El journal guarda el resultado íntegro de
cada agent() con schema; esto lo vuelca tal cual, sin modelo de por medio.

Uso: python3 scripts/productos-digitales/r1-desde-journal.py <journal.jsonl> <productId> [familia]
"""
import json, os, sys

def main():
    journal, pid = sys.argv[1], sys.argv[2]
    familia = sys.argv[3] if len(sys.argv) > 3 else None
    inv = None; R = {}
    for line in open(journal):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get('type') != 'result' or not isinstance(e.get('result'), dict):
            continue
        r = e['result']
        if 'ficheros' in r:
            inv = r
        elif 'lente' in r and 'hallazgos' in r:
            # Clave por PREFIJO mayoritario de los ids (DOM/TEC/COM), no por el texto de la
            # lente: el 29-ago la lente de dominio de planes decía «coherencia de inversión…»
            # y pisó a la de coherencia (se perdieron 30 hallazgos COM-*).
            from collections import Counter
            pref = Counter(str(h.get('id', ''))[:3].upper() for h in r['hallazgos'])
            top = pref.most_common(1)[0][0] if pref else ''
            k = {'DOM': 'dominio', 'TEC': 'excel', 'COM': 'coherencia'}.get(top)
            if k is None:
                L = r['lente'].upper()
                k = 'excel' if ('TÉCNICA EXCEL' in L or 'TECNICA EXCEL' in L) else ('coherencia' if 'COHERENCIA' in L else 'dominio')
            if k in R:
                raise SystemExit(f'dos lentes clasificadas como {k!r}: revisar el journal a mano')
            R[k] = r
    out = {'productId': pid, 'familia': familia, 'inventario': inv, 'rondas': {'R1': R}}
    root = os.path.dirname(os.path.abspath(__file__))
    dst = os.path.join(root, 'auditorias', f'{pid}-R1.json')
    json.dump(out, open(dst, 'w'), ensure_ascii=False, indent=1)
    n = {k: len(v['hallazgos']) for k, v in R.items()}
    print(f'{dst}: lentes {n} · inventario {"ok" if inv else "FALTA"}')
    return 0 if len(R) == 3 and inv else 1

if __name__ == '__main__':
    sys.exit(main())
