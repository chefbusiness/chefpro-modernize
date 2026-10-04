#!/usr/bin/env python3
"""Reapunta a la tienda INGLESA los banners de producto del blog EN.

Por qué (John, 2026-10-04): un post en inglés no puede vender una landing española
(`/kit-tareas`, `/plan-negocio-…`): el lector acaba en un checkout en español. Los posts
EN solo promocionan productos de `/en/digital-products/*` que estén VIVOS.

Cómo:
- Plantillas = los banners EN que YA existen en el corpus (los escribió la sesión de la
  tienda EN con su nombre, descripción y precio en USD). Se copian tal cual y solo se
  cambia `utm_content` por el slug del post. Nada de copy nuevo ni precios a mano.
- Cada banner que no apunte a `/en/digital-products/` se sustituye por el producto EN más
  RELEVANTE para el post (palabras clave en título + cuerpo) que no esté ya en ese post;
  empate → el menos usado en esta pasada (reparto) → orden alfabético (determinista).
- `--rebalanceo` (para cuando nazcan productos EN nuevos): además reasigna banners EN cuyo
  producto esté sobrerrepresentado, para dar entrada a los nuevos. Sin él, solo toca los
  banners que apuntan a landings españolas.
- Gate: el fichero resultante, quitando los bloques <aside> de banner, es idéntico byte a
  byte al original; mismo número de banners por post; ningún producto repetido en un post.

Uso:  python3 scripts/astro-migration/fase8e-banners-en-reapuntar.py            # dry-run
      python3 scripts/astro-migration/fase8e-banners-en-reapuntar.py --aplicar
"""
import argparse, collections, glob, re, sys, urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BLOG_EN = RAIZ / 'astro-site/src/content/blog/en'
HUB = 'https://aichef.pro/en/digital-products'
ASIDE = re.compile(r'<aside class="not-prose my-10 rounded-xl border border-accent/30[^>]*>.*?</aside>', re.S)
HREF_EN = re.compile(r'href="/en/digital-products/([a-z0-9-]+)\?')

# Relevancia temática por producto (slug EN → términos). Un producto EN nuevo sin entrada
# aquí entra igualmente por reparto, solo que sin preferencia temática.
TEMAS = {
    'food-cost-templates': ['food cost', 'costing', 'recipe cost', 'cost per', 'margin', 'pricing', 'price', 'profit', 'menu engineering', 'plate cost'],
    'ai-prompts-for-restaurants': ['prompt', 'chatgpt', 'gpt', 'ai tool', 'artificial intelligence', 'content', 'marketing', 'social media'],
    'restaurant-financial-plan-templates': ['business plan', 'financial', 'open a', 'opening', 'startup', 'cash flow', 'investment', 'break-even', 'dark kitchen', 'ghost kitchen', 'revenue'],
    'haccp-templates': ['haccp', 'food safety', 'allergen', 'hygiene', 'temperature', 'contamination', 'inspection'],
    'restaurant-schedule-templates': ['staff', 'schedule', 'shift', 'team', 'labor', 'labour', 'hiring', 'employee', 'brigade', 'payroll'],
    'restaurant-inventory-templates': ['inventory', 'stock', 'waste', 'purchas', 'supplier', 'ordering', 'storage'],
}


def productos_vivos():
    html = urllib.request.urlopen(urllib.request.Request(HUB, headers={'User-Agent': 'Mozilla/5.0'}), timeout=40).read().decode()
    return sorted(set(re.findall(r'href="/en/digital-products/([a-z0-9-]+)"', html)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--rebalanceo', action='store_true')
    a = ap.parse_args()

    vivos = productos_vivos()
    ficheros = sorted(BLOG_EN.glob('*.md'))
    corpus = {f: f.read_text(encoding='utf-8') for f in ficheros}

    # Plantillas desde el corpus
    plantilla = {}
    for b in corpus.values():
        for blk in ASIDE.findall(b):
            m = HREF_EN.search(blk)
            if m and m.group(1) in vivos:
                plantilla.setdefault(m.group(1), blk)
    sin_plantilla = [p for p in vivos if p not in plantilla]
    if sin_plantilla:
        sys.exit(f'productos EN vivos sin banner modelo en el corpus: {sin_plantilla} (créalo primero)')
    prods = sorted(plantilla)
    print(f'productos EN vivos con plantilla: {len(prods)} → {prods}')

    uso = collections.Counter()
    for b in corpus.values():
        for blk in ASIDE.findall(b):
            m = HREF_EN.search(blk)
            if m and not a.rebalanceo:
                uso[m.group(1)] += 1
    cuota = None
    if a.rebalanceo:
        total = sum(len(ASIDE.findall(b)) for b in corpus.values())
        cuota = -(-total // len(prods))  # techo

    cambios, informe = {}, []
    for f, b in corpus.items():
        slug = f.stem
        bloques = list(ASIDE.finditer(b))
        if not bloques:
            continue
        texto = re.sub(r'<[^>]+>', ' ', ASIDE.sub(' ', b)).lower()
        def score(p):
            return sum(texto.count(t) for t in TEMAS.get(p, []))
        actuales = []
        for m in bloques:
            h = HREF_EN.search(m.group(0))
            actuales.append(h.group(1) if h and h.group(1) in prods else None)
        if a.rebalanceo:
            # libera los banners de productos que ya pasan su cuota (conserva los más relevantes)
            for i, p in sorted(enumerate(actuales), key=lambda ip: (ip[1] is None, -score(ip[1]) if ip[1] else 0)):
                if p is None:
                    continue
                if uso[p] >= cuota:
                    actuales[i] = None
                else:
                    uso[p] += 1
        nuevos = list(actuales)
        for i, p in enumerate(actuales):
            if p is not None:
                continue
            libres = [q for q in prods if q not in nuevos]
            # Relevancia por NIVELES (muy/algo/nada) y, dentro del nivel, el menos usado: con la
            # puntuación bruta, «price/profit» casan en casi todo y food-cost se llevaba el 30 %.
            nivel = lambda q: 2 if score(q) >= 6 else (1 if score(q) >= 2 else 0)
            q = sorted(libres, key=lambda q: (-nivel(q), uso[q], q))[0]
            nuevos[i] = q
            uso[q] += 1
        if nuevos == actuales and all(actuales):
            continue
        out, pos = [], 0
        for m, p_old, p_new in zip(bloques, actuales, nuevos):
            out.append(b[pos:m.start()])
            if p_old == p_new:
                out.append(m.group(0))
            else:
                blk = re.sub(r'utm_content=[a-z0-9-]+', f'utm_content={slug}', plantilla[p_new])
                out.append(blk)
                antes = re.search(r'href="([^"?]+)', m.group(0)).group(1)
                informe.append(f'{slug}: {antes} → /en/digital-products/{p_new}')
            pos = m.end()
        out.append(b[pos:])
        nb = ''.join(out)
        # Gates
        assert ASIDE.sub('', nb) == ASIDE.sub('', b), f'{slug}: cambió algo fuera de los banners'
        assert len(ASIDE.findall(nb)) == len(bloques), f'{slug}: nº de banners distinto'
        hs = [HREF_EN.search(x).group(1) for x in ASIDE.findall(nb)]
        assert len(hs) == len(set(hs)), f'{slug}: producto repetido {hs}'
        assert f'utm_content={slug}' in nb
        cambios[f] = nb

    for l in informe:
        print(' ', l)
    fin = collections.Counter()
    for f in ficheros:
        for blk in ASIDE.findall(cambios.get(f, corpus[f])):
            h = HREF_EN.search(blk)
            fin[h.group(1) if h else 'NO-EN:' + re.search(r'href="([^"?]+)', blk).group(1)] += 1
    print(f'\n{len(informe)} banners reapuntados en {len(cambios)} posts. Reparto final:')
    for k, v in fin.most_common():
        print(f'  {v:4} {k}')
    restos = [k for k in fin if k.startswith('NO-EN:')]
    if restos:
        sys.exit(f'quedan banners no EN: {restos}')
    if a.aplicar:
        for f, nb in cambios.items():
            f.write_text(nb, encoding='utf-8')
        print('APLICADO')
    else:
        print('(dry-run: --aplicar para escribir)')


if __name__ == '__main__':
    main()
