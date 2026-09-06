#!/usr/bin/env python3
"""Mide el solape de frases entre los bloques de un mismo capítulo (Jaccard sobre tokens ≥ 0,55)."""
import re, glob, os, sys, unicodedata
S=os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s=unicodedata.normalize('NFKD', s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    return set(t for t in re.findall(r'[a-z0-9]{3,}', s))
def frases(t):
    t=re.sub(r'^###.*$', '', t, flags=re.M)
    return [f.strip() for f in re.split(r'(?<=[.!?])\s+', t) if len(f.split())>=8]
umbral=float(sys.argv[1]) if len(sys.argv)>1 else 0.55
total=0; peores=[]
for cap in range(1,21):
    bl=sorted(glob.glob(f'{S}/txt/cap{cap:02d}_b*.txt'))
    fr=[(os.path.basename(b), f) for b in bl for f in frases(open(b,encoding='utf-8').read())]
    hits=[]
    for i in range(len(fr)):
        for j in range(i+1,len(fr)):
            if fr[i][0]==fr[j][0]: continue
            a,b=norm(fr[i][1]),norm(fr[j][1])
            if not a or not b: continue
            jac=len(a&b)/len(a|b)
            if jac>=umbral: hits.append((jac, fr[i][1][:90], fr[j][1][:90]))
    total+=len(hits)
    if hits: peores.append((cap, len(hits), max(hits)[0]))
    print(f'cap {cap:02d}: {len(hits):2d} pares ≥{umbral} · frases {len(fr)}' + (f' · peor {max(hits)[0]:.2f}: «{max(hits)[1]}»' if hits else ''))
print('TOTAL pares solapados:', total)
