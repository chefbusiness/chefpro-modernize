#!/usr/bin/env python3
"""Gate de la traducción EN del eBook Pro Prompts (SPEC §4.3). Sin dependencias: corre en 1 s.

Uso:
  python3 gate_en.py --parte 2      # comprueba en/parte-2.json contra entrada/es-parte-2.json
  python3 gate_en.py                # todas las partes presentes + exige las 4 y los 300 prompts

Lo que mira, prompt a prompt:
  - número y orden iguales al ES; título, cuerpo y agentes no vacíos;
  - el MISMO número de placeholders [..] que el ES (el lector los rellena: uno de menos es un hueco en el prompt);
  - agentes solo del catálogo EN (`agentes_en.json`), sin repetidos;
  - cero «€»/«euro», cero caracteres fuera del latín (las inyecciones CJK de DeepSeek, CLAUDE.md), cero años que el ES no tenga;
  - palabras-centinela del español y trozos de 5 palabras idénticos al ES (texto sin traducir).
En la parte 1, además, portada/bienvenida/cierre/bloques/secciones con la misma cantidad de piezas que el ES.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
AGENTES = set(json.loads((AQUI / 'agentes_en.json').read_text())['mapa'].values())
PH = re.compile(r'\[[^\]]+\]')
ANIO = re.compile(r'\b(19|20)\d\d\b')
# Palabras que en un texto inglés no aparecen nunca sueltas (las ambiguas —la, con, el, a— fuera).
CENTINELA = re.compile(r'\b(que|los|las|del|una|para|según|también|cómo|qué|receta|recetas|cocina|plato|platos|carta|'
                       r'hostelería|incluye|diseña|crea|actúa|eres|quiero|necesito|tengo|mis|tus|sus|cada|desde|'
                       r'entre|sobre|cliente|clientes|equipo|negocio|precio|coste|costes|mermas|obrador|comensal|'
                       r'comensales|de|en|al)\b', re.I)
# «y/o/e» solo en minúscula: en mayúscula son variables de ejemplo («X vegan, Y celiac»).
CONECTOR = re.compile(r'(?<=\s)(y|o|e)(?=\s)')
# Expresiones culinarias que el inglés usa tal cual y contienen centinelas.
PERMITIDAS = re.compile(r"(à la|a la|chili con carne|pico de gallo|tres leches|dulce de leche|mise en place|"
                        r"de cuisine|crème de|pâte de|fleur de sel|sauce|jus|en papillote|pommes|y\)|\by/n\b|"
                        r"sous vide|al dente|al pastor|al fresco|cuisine|de partie|chef de|garde manger|pan de|tarta de|vin de|eau de|"
                        r"\bo\b(?=\s*/)|/\s*o\b|\be\.g\.|\bi\.e\.)", re.I)


def no_latinos(t):
    malos = []
    for ch in t:
        if ord(ch) < 0x250:                      # ASCII + Latin-1 + Latin Extended-A/B
            continue
        cat = unicodedata.category(ch)
        if ch in '–—‘’“”…•·°×→←≈≤≥±½¼¾€™®©': # tipografía legítima (€ se caza aparte)
            continue
        if cat.startswith('Z'):
            continue
        malos.append(ch)
    return malos


def ventanas(t, n=5):
    w = re.findall(r"[a-záéíóúñü]+", t.lower())
    return {' '.join(w[i:i + n]) for i in range(len(w) - n + 1)}


def revisa_prompt(es, en, errs):
    tag = f"#{es['n']:03d}"
    if en.get('n') != es['n']:
        errs.append(f"{tag}: número {en.get('n')} ≠ {es['n']}")
        return
    for k in ('titulo', 'cuerpo'):
        if not str(en.get(k, '')).strip():
            errs.append(f'{tag}: {k} vacío')
    apps = en.get('apps') or []
    if not apps:
        errs.append(f'{tag}: sin agentes')
    fuera = [a for a in apps if a not in AGENTES]
    if fuera:
        errs.append(f'{tag}: agentes fuera del catálogo EN {fuera}')
    if len(set(apps)) != len(apps):
        errs.append(f'{tag}: agentes repetidos {apps}')
    n_es, n_en = len(PH.findall(es['cuerpo'] + es['titulo'])), len(PH.findall(en['cuerpo'] + en['titulo']))
    if n_es != n_en:
        errs.append(f'{tag}: placeholders {n_en} ≠ ES {n_es}')
    texto = f"{en['titulo']} {en['cuerpo']} {' '.join(apps)}"
    revisa_texto(tag, texto, es['titulo'] + ' ' + es['cuerpo'], errs)


def revisa_texto(tag, texto, es_texto, errs):
    if '€' in texto or re.search(r'\beuros?\b', texto, re.I):
        errs.append(f'{tag}: moneda euro')
    m = no_latinos(texto)
    if m:
        errs.append(f'{tag}: caracteres no latinos {sorted(set(m))}')
    anios = set(ANIO.findall(texto)) - set(ANIO.findall(es_texto))
    if ANIO.search(texto) and anios:
        errs.append(f'{tag}: año que el ES no tiene → {ANIO.findall(texto)}')
    limpio = PERMITIDAS.sub(' ', texto)
    c = sorted(set(x.lower() for x in CENTINELA.findall(limpio)) | set(CONECTOR.findall(limpio)))
    if c:
        errs.append(f'{tag}: palabras en español {c}')
    comunes = ventanas(texto) & ventanas(es_texto)
    if comunes:
        errs.append(f'{tag}: texto idéntico al ES {sorted(comunes)[:2]}')


def revisa_parte(i, errs):
    es = json.loads((AQUI / f'entrada/es-parte-{i}.json').read_text())
    p = AQUI / f'en/parte-{i}.json'
    if not p.exists():
        errs.append(f'parte {i}: falta {p.relative_to(AQUI)}')
        return 0
    try:
        en = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        errs.append(f'parte {i}: JSON inválido ({e})')
        return 0
    if len(en.get('prompts', [])) != len(es['prompts']):
        errs.append(f"parte {i}: {len(en.get('prompts', []))} prompts ≠ {len(es['prompts'])}")
    for a, b in zip(es['prompts'], en.get('prompts', [])):
        revisa_prompt(a, b, errs)
    if i == 1:
        for k in ('portada', 'bienvenida', 'cierre', 'bloques', 'secciones'):
            if len(en.get(k, [])) != len(es[k]):
                errs.append(f'parte 1: {k} {len(en.get(k, []))} piezas ≠ ES {len(es[k])}')
                continue
            for j, (a, b) in enumerate(zip(es[k], en[k])):
                ta = ' '.join(str(v) for kk, v in a.items() if kk != 'estilo')
                tb = ' '.join(str(v) for kk, v in b.items() if kk != 'estilo')
                if not tb.strip():
                    errs.append(f'parte 1: {k}[{j}] vacío')
                revisa_texto(f'{k}[{j}]', tb, ta, errs)
    return len(en.get('prompts', []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parte', type=int)
    a = ap.parse_args()
    errs = []
    partes = [a.parte] if a.parte else [1, 2, 3, 4]
    total = sum(revisa_parte(i, errs) for i in partes)
    for e in errs:
        print('✗', e)
    if not a.parte and total != 300:
        errs.append(f'total {total} ≠ 300')
        print('✗', errs[-1])
    print(f"{'VERDE' if not errs else 'ROJO'} · partes {partes} · {total} prompts · {len(errs)} fallos")
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
