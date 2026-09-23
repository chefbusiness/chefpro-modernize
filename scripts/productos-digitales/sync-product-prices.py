#!/usr/bin/env python3
"""
Mapa productId → precio anunciado en la landing, generado desde el campo
`schema.price` de cada ficha de producto (astro-site/src/data/productos/**/*.ts)
más los 2 productos sin ficha (mega-pack-tareas, pro-prompts-ebook), que se
mapean a mano en SPECIAL_PRICES.

`schema.price` es el precio que ya se declara en el JSON-LD Product de cada
landing (el que ve Google): tomarlo de ahí, en vez de escribirlo de nuevo,
evita que este fichero se desincronice si sube el precio de un producto.
Lo va a consumer la function de crypto-checkout (NOWPayments, pendiente) para
crear la invoice: el precio es el mismo en EUR para todos los países
(decisión de John 2026-09-05) — no hay que geolocalizar ni convertir moneda.

Uso:
  python3 scripts/productos-digitales/sync-product-prices.py          # regenera el .ts
  python3 scripts/productos-digitales/sync-product-prices.py --check  # exit 1 si el .ts difiere de las fichas

Fuente del mapa productId → precio: el campo numérico `schema.price` (p.ej. `price: '55.00'`
dentro del bloque `schema: { ... }`) de cada `astro-site/src/data/productos/{guias,kits,planes,manuales,tareas}/*.ts`
(excluyendo types.ts) + SPECIAL_PRICES para los 2 productos sin ficha tipada. Se cruza con
PRODUCTS de verify-purchase.ts: deben ser los mismos 46. El parser acota el bloque `schema: { ... }`
por su indentación (no por el primer `price:` del fichero, que también aparece en el bloque
`pricing: { ... }` con el descuento tipo '24 EUR') y por su llave de cierre, así nunca cruza
al bloque del siguiente producto ni confunde el precio de partida con el de oferta.

TIENDA INTERNACIONAL (2026-09-23, fase 0.B): el mapa pasa a `{ eur?: number; usd?: number }`
y lee además las fichas de las otras tiendas, `astro-site/src/data/productos-<lang>/**/*.ts`
(hoy solo `productos-en`; mismo tipo que las ES; si el directorio no existe, no hace nada). El
precio sigue siendo `schema.price`; la MONEDA es la de la tienda a la que pertenece la ficha,
`TIENDAS[lang].moneda` de `astro-site/src/lib/tienda.ts` — la misma fuente de la que la plantilla
saca el `priceCurrency` del JSON-LD, así que landing y factura no pueden discrepar. Las fichas ES
son EUR sin depender de ese fichero. Cada producto lleva UNA sola moneda: `crypto-checkout.ts`
factura en USD si el producto tiene `usd`, y en EUR si no.

`--check` cruza ADEMÁS contra `src/data/products-catalog.ts` (46 entradas, el catálogo que
usa `fase8c-libreria-assemble.py` para los banners del blog): su campo `price: '€12'` (a
veces con coma decimal, p.ej. `'€18,50'` → 18.5) es una copia de precio independiente y
puede desincronizarse del `schema.price` real de la ficha — igual que el precio y el nombre
del propio catálogo ya se desincronizaron una vez en silencio (2026-08-30, ver CLAUDE.md).
Un banner con el precio equivocado vende mal. El parser acota cada bloque `'id': { ... }`
por su indentación de 2 espacios y su llave de cierre, con el mismo criterio que
`ficha_prices()`, para no cruzar al `price:` de la siguiente entrada del catálogo.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'netlify', 'shared', 'product-prices.ts')
CATALOG = os.path.join(ROOT, 'src', 'data', 'products-catalog.ts')
TIENDA_TS = os.path.join(ROOT, 'astro-site', 'src', 'lib', 'tienda.ts')

# Los únicos 2 productos sin ficha tipada en astro-site/src/data/productos/: viven como
# JSON-LD a mano dentro de la página/componente. Precio leído de su bloque `offers.price`.
SPECIAL_PRICES = {
    'mega-pack-tareas': ('EUR', 89.00),   # astro-site/src/pages/mega-pack-tareas.astro (offers.price)
    'pro-prompts-ebook': ('EUR', 9.00),   # astro-site/src/components/pages/ProPromptsEbookPage.astro (offers.price)
}

# Moneda de la ficha → clave del mapa generado (y `price_currency` de NOWPayments).
MONEDAS = {'EUR': 'eur', 'USD': 'usd'}
SIMBOLOS = {'€': 'EUR', '$': 'USD'}


def monedas_tiendas():
    """lang → moneda ('EUR'|'USD') del registro `TIENDAS` de astro-site/src/lib/tienda.ts.
    {} si el fichero no existe (entonces solo hay tienda española)."""
    if not os.path.exists(TIENDA_TS):
        return {}
    t = open(TIENDA_TS, encoding='utf-8').read()
    return {lang: mon for lang, mon in re.findall(r"^\s*([a-z]{2}):\s*\{[^}\n]*\bmoneda:\s*'([A-Z]{3})'", t, re.M)}


def fichas():
    """(fichero, moneda) de todas las fichas tipadas: las ES (EUR, sin depender de tienda.ts)
    y las de cada otra tienda en productos-<lang>/** con la moneda de TIENDAS[lang]
    (None si tienda.ts no la declara: se aborta antes que adivinar la moneda de un cobro)."""
    out = [(f, 'EUR') for f in sorted(glob.glob(os.path.join(ROOT, 'astro-site/src/data/productos/*/*.ts')))]
    monedas = monedas_tiendas()
    for d in sorted(glob.glob(os.path.join(ROOT, 'astro-site/src/data/productos-*'))):
        lang = os.path.basename(d)[len('productos-'):]
        for f in sorted(glob.glob(os.path.join(d, '**', '*.ts'), recursive=True)):
            out.append((f, monedas.get(lang)))
    return out


def ficha_prices():
    """productId → (moneda, precio float), leído del schema.price de cada ficha (la moneda,
    de su tienda). Aborta con error claro (fichero:motivo) si alguna ficha no tiene un
    schema.price numérico, o si su tienda no tiene moneda declarada."""
    prices = {}
    errors = []
    for f, moneda_ficha in fichas():
        if f.endswith('types.ts'):
            continue
        rel = os.path.relpath(f, ROOT)
        t = open(f, encoding='utf-8').read()
        slug_m = re.search(r"^\s*slug:\s*'([^']+)'", t, re.M)
        if not slug_m:
            errors.append(f'{rel}: sin `slug:` — no se puede mapear a un productId')
            continue
        slug = slug_m.group(1)
        schema_m = re.search(r'^([ \t]*)schema:\s*\{', t, re.M)
        if not schema_m:
            errors.append(f'{rel} ({slug}): sin bloque `schema: {{ ... }}`')
            continue
        indent = schema_m.group(1)
        start = schema_m.end()
        # Cierre del bloque schema: la primera línea con la MISMA indentación que "schema:"
        # que sea solo "}," — así nunca sigue de largo hasta el bloque del siguiente producto
        # (aquí no aplica, un producto por fichero, pero es el mismo criterio que en el catálogo).
        close_m = re.search(r'\n' + re.escape(indent) + r'\},?[ \t]*\n', t[start:])
        if not close_m:
            errors.append(f'{rel} ({slug}): no se encuentra el cierre del bloque `schema: {{ ... }}`')
            continue
        block = t[start:start + close_m.start()]
        price_m = re.search(r"price:\s*'([\d.]+)'", block)
        if not price_m:
            errors.append(f'{rel} ({slug}): schema.price ausente o no numérico dentro del bloque schema')
            continue
        moneda = moneda_ficha
        if moneda is None:
            errors.append(f'{rel} ({slug}): su tienda no declara `moneda` en {os.path.relpath(TIENDA_TS, ROOT)}')
            continue
        if moneda not in MONEDAS:
            errors.append(f'{rel} ({slug}): moneda {moneda!r} no soportada (solo {sorted(MONEDAS)})')
            continue
        if slug in prices:
            errors.append(f'{rel}: slug {slug!r} duplicado (ya lo declaraba otra ficha)')
            continue
        prices[slug] = (moneda, float(price_m.group(1)))
    return prices, errors


def catalog_prices():
    """productId → (moneda, precio float) anunciado en src/data/products-catalog.ts (46 entradas,
    campo `price: '€12'`, a veces con coma decimal: '€18,50' → 18.5). Devuelve (prices, errors);
    errors nunca aborta el script (el catálogo no es la fuente de verdad, solo se contrasta)."""
    prices, errors = {}, []
    if not os.path.exists(CATALOG):
        return prices, [f'{os.path.relpath(CATALOG, ROOT)}: no existe']
    t = open(CATALOG, encoding='utf-8').read()
    rel = os.path.relpath(CATALOG, ROOT)
    for m in re.finditer(r'^( {2})\'([a-z0-9-]+)\':\s*\{[ \t]*\n', t, re.M):
        indent, pid = m.group(1), m.group(2)
        start = m.end()
        close_m = re.search(r'\n' + re.escape(indent) + r'\},?[ \t]*\n', t[start:])
        if not close_m:
            errors.append(f'{rel} ({pid}): no se encuentra el cierre del bloque')
            continue
        block = t[start:start + close_m.start()]
        price_m = re.search(r"price:\s*'([€$])\s*([\d.,]+)'", block)
        if not price_m:
            errors.append(f'{rel} ({pid}): sin `price: \'€…\'` (o `\'$…\'`) reconocible')
            continue
        if pid in prices:
            errors.append(f'{rel}: id {pid!r} duplicado')
            continue
        prices[pid] = (SIMBOLOS[price_m.group(1)], float(price_m.group(2).replace(',', '.')))
    return prices, errors


def verify_purchase_products():
    t = open(os.path.join(ROOT, 'netlify/functions/verify-purchase.ts'), encoding='utf-8').read()
    block = t.split('const PRODUCTS', 1)[1].split('\n};', 1)[0]
    return set(re.findall(r"^\s{2}'([a-z0-9-]+)':\s*\{", block, re.M))


def fmt_price(value):
    """12.0 → '12' · 18.5 → '18.5' · 55.0 → '55' (sin decimales innecesarios)."""
    s = f'{value:.2f}'.rstrip('0').rstrip('.')
    return s or '0'


def render(prices):
    lines = [
        '// GENERADO por scripts/productos-digitales/sync-product-prices.py — NO editar a mano.',
        '// productId → precio anunciado en la landing (schema.price de la ficha), en SU moneda: `eur` en la tienda',
        '// española, `usd` en la internacional (una sola por producto). Es el importe con el que crypto-checkout crea',
        '// la invoice de NOWPayments: el precio es el mismo para todos los países (decisión de John 2026-09-05).',
        'export const PRODUCT_PRICES: Record<string, { eur?: number; usd?: number }> = {',
    ]
    for pid in sorted(prices):
        moneda, valor = prices[pid]
        lines.append(f"  '{pid}': {{ {MONEDAS[moneda]}: {fmt_price(valor)} }},")
    lines.append('};')
    lines.append('')
    return '\n'.join(lines)


def parse_existing(content):
    """productId → 'moneda precio' (tal cual escrito) del .ts ya publicado, para el diff de --check."""
    return {
        pid: f'{cur} {val}'
        for pid, cur, val in re.findall(r"^\s*'([a-z0-9-]+)':\s*\{\s*(eur|usd):\s*([\d.]+)\s*\},?\s*$", content, re.M)
    }


def diff_lines(old, new_content):
    new = parse_existing(new_content)
    lines = []
    for pid in sorted(set(old) | set(new)):
        if pid not in old:
            lines.append(f"  + {pid}: {new[pid]}")
        elif pid not in new:
            lines.append(f"  - {pid}: {old[pid]}")
        elif old[pid] != new[pid]:
            lines.append(f"  ~ {pid}: {old[pid]} → {new[pid]}")
    return lines


def main():
    check = '--check' in sys.argv
    prices, errors = ficha_prices()
    dup_special = set(prices) & set(SPECIAL_PRICES)
    if dup_special:
        errors.append(f'SPECIAL_PRICES pisa fichas ya tipadas: {sorted(dup_special)}')
    prices.update(SPECIAL_PRICES)
    vp = verify_purchase_products()
    if set(prices) != vp:
        errors.append(
            f'productIds con precio ≠ PRODUCTS de verify-purchase: '
            f'solo_precios={sorted(set(prices) - vp)} solo_vp={sorted(vp - set(prices))}'
        )
    if errors:
        for e in errors:
            print('✗', e)
        sys.exit(1)
    content = render(prices)
    if check:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        if cur != content:
            print(f'✗ {os.path.relpath(OUT, ROOT)} difiere de las fichas: regenerar con sync-product-prices.py y commitear')
            for d in diff_lines(parse_existing(cur), content):
                print(' ', d)
            sys.exit(1)
        # Cruce adicional: el catálogo de banners del blog (products-catalog.ts) debe
        # anunciar el MISMO precio que la ficha (fuente de verdad = schema.price).
        cat_prices, cat_errors = catalog_prices()
        problems = list(cat_errors)
        txt = lambda mv: f'{fmt_price(mv[1])} {mv[0]}'
        for pid in sorted(set(prices) | set(cat_prices)):
            if pid not in cat_prices:
                # Los productos de la tienda internacional pueden no tener banner en el
                # catálogo del blog: solo se exige presencia a los de la tienda española.
                if prices[pid][0] == 'EUR':
                    problems.append(f'{pid}: precio real {txt(prices[pid])} pero AUSENTE en products-catalog.ts')
            elif pid not in prices:
                problems.append(f'{pid}: products-catalog.ts trae {txt(cat_prices[pid])} pero no existe como producto real (ni ficha ni SPECIAL_PRICES)')
            elif prices[pid][0] != cat_prices[pid][0] or abs(prices[pid][1] - cat_prices[pid][1]) > 0.005:
                problems.append(f'{pid}: ficha {txt(prices[pid])} ≠ products-catalog.ts {txt(cat_prices[pid])}')
        if problems:
            print(f'✗ {os.path.relpath(CATALOG, ROOT)} difiere del precio real ({len(problems)} discrepancia(s)):')
            for p in problems:
                print(' ', p)
            sys.exit(1)
        print(f'✓ product-prices.ts al día ({len(prices)} productos) · products-catalog.ts coincide en precio con las {len(cat_prices)} entradas')
        return
    open(OUT, 'w', encoding='utf-8').write(content)
    print(f'✓ escrito {os.path.relpath(OUT, ROOT)} con {len(prices)} productos')


if __name__ == '__main__':
    main()
