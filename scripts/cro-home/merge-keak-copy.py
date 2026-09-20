#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CRO home (Keak, 20-sep-2026) — funde keak-copy.<lang>.json en src/i18n/locales/<lang>.json
y, con --check, hace de GATE de i18n.

Qué hace al fundir (idempotente):
  1. Deep-merge de las claves v2_* del copy traducido dentro del JSON del idioma.
  2. Para fr/de/it/pt/nl: «75+» → «50+» en las cadenas nuevas (esas plataformas sirven
     53-54 agentes y su hero ya anuncia 50+; ver Hero.astro / CATALOGO_ITALIANO_PENDIENTE.md).
  3. hero.v2_business_types = hero.business_types sin su primer elemento («Gestión»/
     «Management»: encajaba en «Transforma tu Gestión» pero no en «…en tu Gestión»).
     El primero que queda es «Restaurante»: es lo que Google lee en el H1 SSR.
  4. pricing.plans.member.period = pricing.plans.premium_pro.period si falta (la tarjeta
     Member v2 muestra «/mes» como las demás).

Qué comprueba --check (falla con código 1):
  · toda clave v2 del inglés existe en los 7 idiomas y ninguna vale ""
  · los dígitos de cada cadena coinciden con el inglés (salvo el 75+→50+ documentado)
  · cero caracteres de otro alfabeto; «AI Chef Pro» intacto donde el inglés lo lleva
  · hero.v2_business_types tiene 11 elementos en los 7 idiomas
Uso:
    python3 merge-keak-copy.py --lang en          # una
    python3 merge-keak-copy.py --todos            # las 7 que tengan keak-copy.<lang>.json
    python3 merge-keak-copy.py --check            # gate
"""
import argparse, json, re, sys
from pathlib import Path

DIR = Path(__file__).parent
LOCALES = DIR.parent.parent / 'src' / 'i18n' / 'locales'
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
SECUNDARIOS = {'fr', 'de', 'it', 'pt', 'nl'}
SOSPECHOSO = re.compile(
    r'[　-鿿Ѐ-ӿ가-힯؀-ۿ֐-׿฀-๿぀-ヿ]')


def pares(o, path='', acc=None):
    acc = [] if acc is None else acc
    if isinstance(o, dict):
        for k in sorted(o):
            pares(o[k], f'{path}.{k}' if path else k, acc)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            pares(v, f'{path}[{i}]', acc)
    elif isinstance(o, str):
        acc.append((path, o))
    return acc


def resolve(d, path):
    cur = d
    for tok in re.split(r'\.|\[(\d+)\]', path):
        if tok is None or tok == '':
            continue
        if isinstance(cur, list):
            cur = cur[int(tok)] if int(tok) < len(cur) else None
        elif isinstance(cur, dict):
            cur = cur.get(tok)
        else:
            return None
        if cur is None:
            return None
    return cur


def deep_merge(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            deep_merge(dst[k], v)
        else:
            dst[k] = v


def rebaja_agentes(o):
    if isinstance(o, dict):
        return {k: rebaja_agentes(v) for k, v in o.items()}
    if isinstance(o, list):
        return [rebaja_agentes(v) for v in o]
    if isinstance(o, str):
        return o.replace('75+', '50+')
    return o


def cargar(lang):
    p = LOCALES / f'{lang}.json'
    return p, json.loads(p.read_text(encoding='utf-8'))


def guardar(p, d):
    # Mismo formato que el resto del fichero (2 espacios, sin escapar unicode).
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def fundir(lang):
    src = DIR / f'keak-copy.{lang}.json'
    if not src.exists():
        print(f'  – {lang}: no hay keak-copy.{lang}.json (pendiente de traducir)')
        return False
    copy = json.loads(src.read_text(encoding='utf-8'))
    if lang in SECUNDARIOS:
        copy = rebaja_agentes(copy)
    p, d = cargar(lang)
    deep_merge(d, copy)
    bt = d['hero'].get('business_types') or []
    d['hero']['v2_business_types'] = bt[1:] if len(bt) > 1 else bt
    member = d['pricing']['plans']['member']
    if not member.get('period'):
        member['period'] = d['pricing']['plans']['premium_pro'].get('period', '')
    guardar(p, d)
    print(f'  ✓ {lang}: {len(pares(copy))} cadenas fundidas · v2_business_types={len(d["hero"]["v2_business_types"])}')
    return True


def check():
    en_copy = json.loads((DIR / 'keak-copy.en.json').read_text(encoding='utf-8'))
    claves = pares(en_copy)
    errores = []
    for lang in LANGS:
        _, d = cargar(lang)
        for ruta, en in claves:
            v = resolve(d, ruta)
            if not isinstance(v, str) or not v.strip():
                errores.append(f'{lang}: falta o vacía {ruta}')
                continue
            if SOSPECHOSO.search(v):
                errores.append(f'{lang}: alfabeto ajeno en {ruta}: {v[:50]!r}')
            en_dig = re.sub(r'\D', '', en)
            if lang in SECUNDARIOS:
                en_dig = re.sub(r'\D', '', en.replace('75+', '50+'))
            if en_dig != re.sub(r'\D', '', v):
                errores.append(f'{lang}: dígitos distintos en {ruta}: EN {en!r} → {v!r}')
            if 'AI Chef Pro' in en and 'AI Chef Pro' not in v:
                errores.append(f'{lang}: falta «AI Chef Pro» en {ruta}')
        bt = d['hero'].get('v2_business_types')
        if not isinstance(bt, list) or len(bt) != 11:
            errores.append(f'{lang}: hero.v2_business_types tiene {len(bt) if isinstance(bt, list) else "nada"} (esperado 11)')
        if not d['pricing']['plans']['member'].get('period'):
            errores.append(f'{lang}: pricing.plans.member.period vacío')
    if errores:
        print('\n'.join(errores))
        print(f'\n✗ GATE i18n: {len(errores)} errores')
        return 1
    print(f'✓ GATE i18n: {len(claves)} claves × {len(LANGS)} idiomas, todo presente y coherente')
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', choices=LANGS)
    ap.add_argument('--todos', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        return check()
    langs = LANGS if a.todos else ([a.lang] if a.lang else [])
    if not langs:
        sys.exit('indica --lang, --todos o --check')
    for lang in langs:
        fundir(lang)
    return 0


if __name__ == '__main__':
    sys.exit(main())
