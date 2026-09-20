#!/usr/bin/env python3
"""hub-gate.py — Los DOS ficheros gemelos del hub de productos digitales (Astro + SPA) deben ser iguales en ORDEN de
`products`, en la lista `comingSoon`, y cumplir la política del 20-sep-2026 (novedad en la posición 1, Mega Pack el último,
«✨ Nuevo» solo en los 5 primeros). Uso: python3 scripts/astro-migration/hub-gate.py [--first <slug>] [--n <productos>]
[--coming <n>]. Exit 0 = PASS."""
import re, sys
A = 'astro-site/src/components/pages/ProductosDigitalesHubPage.astro'
T = 'src/pages/ProductosDigitales.tsx'
args = sys.argv[1:]
def opt(k, default=None):
    return args[args.index(k) + 1] if k in args else default
def bloques(path):
    s = open(path, encoding='utf-8').read()
    i = s.index('const products = ['); j = s.index('\n];', i); k = s.index('[', i) + 1
    d = 0; start = None; out = []
    for idx in range(k, j + 1):
        ch = s[idx]
        if ch == '{':
            if d == 0: start = idx
            d += 1
        elif ch == '}':
            d -= 1
            if d == 0: out.append(s[start:idx + 1])
    slugs = [re.search(r"slug: '([^']+)'", b).group(1) for b in out]
    badges = [(re.search(r"badge: '([^']*)'", b) or [None, ''])[1] for b in out]
    cs = re.search(r'comingSoon[^=]*=\s*\[(.*?)\n\];', s, re.S)
    coming = re.findall(r"name: '([^']+)'", cs.group(1)) if cs else []
    return slugs, badges, coming
fallos = []
sa, ba, ca = bloques(A); st, bt, ct = bloques(T)
if sa != st: fallos.append(f'orden distinto entre los dos hubs (astro {len(sa)} / tsx {len(st)})')
if ca != ct: fallos.append(f'comingSoon distinto entre los dos hubs (astro {len(ca)} / tsx {len(ct)})')
n = opt('--n'); first = opt('--first'); coming = opt('--coming')
if n and len(sa) != int(n): fallos.append(f'{len(sa)} productos, esperados {n}')
if first and sa[0] != first: fallos.append(f'primero {sa[0]}, esperado {first}')
if coming and len(ca) != int(coming): fallos.append(f'{len(ca)} en comingSoon, esperados {coming}')
if sa[-1] != '/mega-pack-tareas': fallos.append(f'el último es {sa[-1]}, debe ser /mega-pack-tareas')
nuevos = [i for i, b in enumerate(ba) if '✨' in b]
if any(i >= 5 for i in nuevos): fallos.append(f'«✨ Nuevo» fuera del top-5: posiciones {nuevos}')
for nombre in ca:
    if any(nombre.split(':')[-1].strip().lower() in sl for sl in []): pass
print(f'productos {len(sa)} · primero {sa[0]} · último {sa[-1]} · ✨ en {nuevos} · comingSoon {len(ca)}')
if fallos:
    print('HUB GATE: FAIL'); [print(' -', f) for f in fallos]; sys.exit(1)
print('HUB GATE: PASS')
