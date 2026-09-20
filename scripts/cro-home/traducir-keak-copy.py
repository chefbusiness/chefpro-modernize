#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CRO home (Keak, 20-sep-2026) — traduce keak-copy.en.json a los otros 6 idiomas.

POR QUÉ ASÍ: el copy fuente es el INGLÉS (las recomendaciones de Keak llegaron en
inglés y se aplican tal cual). La REGLA CAPITAL manda que el copy web salga de
`bridge.py`; estas cadenas llevan PRECIOS y CRÉDITOS, donde un carácter cambia el
significado, así que el motor es `anthropic/claude-sonnet-4.6` primero (criterio de
CLAUDE.md: «contenido donde un carácter suelto cambia el significado → modelo bueno
+ gate automático») y DeepSeek flash como segundo intento.

GATES (mismos que fase12-traducir-copy.py, más dos propios):
  · estructura idéntica al inglés (claves y longitudes de lista)
  · cero caracteres de otros alfabetos
  · tratamiento del sitio: es tú · fr vous · de Sie · it tu · pt você · nl u
  · LOS DÍGITOS de cada cadena son los mismos que en inglés (10,000 → 10.000 vale;
    10,000 → 1.000 no)
  · «AI Chef Pro» y los nombres de plan (Premium Pro/Plus/Max) se conservan
Los nombres de plan localizados («AI Chef Miembro»…) NO van en este JSON: los
componentes los leen de las claves ya existentes de cada idioma.

Se ejecuta en el VPS (bridge actualizado). Uso:
    /root/chefbusiness-ai/.venv/bin/python traducir-keak-copy.py --todos
    … --lang fr
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

DIR = Path(__file__).parent
BRIDGE = '/root/chefbusiness-ai/bridge.py'
PYBIN = '/root/chefbusiness-ai/.venv/bin/python'

IDIOMAS = {
    'es': 'Español de España',
    'fr': 'Français',
    'de': 'Deutsch',
    'it': 'Italiano',
    'pt': 'Português de Portugal',
    'nl': 'Nederlands',
}
TRATAMIENTO = {
    'es': 'Trata al lector de TÚ (tuteo), como el resto de aichef.pro.',
    'fr': 'Trata al lector de VOUS (vouvoiement). Nunca de «tu».',
    'de': 'Trata al lector de SIE (Siezen). Nunca de «du».',
    'it': 'Trata al lector de TU.',
    'pt': 'Trata al lector de VOCÊ. Nunca de «tu».',
    'nl': 'Trata al lector de U (formal). Nunca de «je» o «jij».',
}
FORMATO_NUM = {
    'es': 'miles con punto (10.000) y el euro DETRÁS con espacio: 10 €/mes',
    'fr': 'miles con espacio fino o espacio (10 000) y el euro DETRÁS: 10 €/mois',
    'de': 'miles con punto (10.000) y el euro DETRÁS: 10 €/Monat',
    'it': 'miles con punto (10.000) y el euro DETRÁS: 10 €/mese',
    'pt': 'miles con punto (10.000) y el euro DETRÁS: 10 €/mês',
    'nl': 'miles con punto (10.000) y el euro DELANTE: €10/maand',
}
MARCAS = ['AI Chef Pro', 'Premium Pro', 'Premium Plus', 'Premium Max', 'Max']

SOSPECHOSO = re.compile(
    r'[\u3000-\u9fff\u0400-\u04ff\uac00-\ud7af\u0600-\u06ff\u0590-\u05ff\u0e00-\u0e7f\u3040-\u30ff]')

MARCADORES = {
    'fr': (r"\b(vous|votre|vos)\b", r"\b(tu|ton|ta|tes|toi)\b"),
    'de': (r"\b(Sie|Ihre|Ihrem|Ihren|Ihr)\b", r"\b(du|dein|deine|deinem|dich|dir)\b"),
    'pt': (r"\b(você|vocês|o seu|a sua|seus|suas)\b", r"\b(tu|teu|tua|teus|tuas)\b"),
    'nl': (r"\b(u|uw)\b", r"\b(je|jij|jouw|jullie)\b"),
    'it': (r"\b(Lei|La Sua|Il Suo)\b", r"\b(tu|tuo|tua|tuoi|tue)\b"),
    'es': (r"\b(usted|ustedes|su|sus)\b", r"\b(tu|tus|tú|te)\b"),
}
ESPERADO = {'fr': 'formal', 'de': 'formal', 'pt': 'formal', 'nl': 'formal',
            'it': 'informal', 'es': 'informal'}


def forma(o):
    if isinstance(o, dict):
        return {k: forma(v) for k, v in sorted(o.items())}
    if isinstance(o, list):
        return [forma(x) for x in o]
    return type(o).__name__


def pares(o, path='', acc=None):
    """[(ruta, texto)] en orden estable."""
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


def digitos(s):
    return re.sub(r'\D', '', s)


def revisar_tratamiento(lang, data):
    formal_re, informal_re = (re.compile(p, re.I) for p in MARCADORES[lang])
    blob = ' '.join(t for _, t in pares(data))
    nf, ni = len(formal_re.findall(blob)), len(informal_re.findall(blob))
    # Copy muy corto: puede no haber ni un marcador. Solo se falla si el contrario GANA.
    if nf == ni == 0:
        return None
    gana = 'formal' if nf > ni else 'informal'
    if gana != ESPERADO[lang]:
        return f'tratamiento {gana} (formal={nf}, informal={ni}) pero el sitio usa {ESPERADO[lang]}'
    return None


_LINEA_VALOR = re.compile(r'^(\s*"[A-Za-z_][\w]*"\s*:\s*")(.*)("\s*,?)$')
_LINEA_ITEM = re.compile(r'^(\s*")(.*)("\s*,?)$')


def repara_comillas(raw):
    fuera = []
    for linea in raw.split('\n'):
        m = _LINEA_VALOR.match(linea) or _LINEA_ITEM.match(linea)
        if m:
            dentro = m.group(2).replace('\\"', '\x00').replace('"', '\\"').replace('\x00', '\\"')
            linea = m.group(1) + dentro + m.group(3)
        fuera.append(linea)
    return '\n'.join(fuera)


def validar(lang, data, base):
    if forma(data) != forma(base):
        return 'la ESTRUCTURA no coincide con el inglés'
    pb, pd = pares(base), pares(data)
    for (ruta, en), (_, tr) in zip(pb, pd):
        if SOSPECHOSO.search(tr):
            return f'caracteres de otro alfabeto en {ruta}: {tr[:60]!r}'
        if digitos(en) != digitos(tr):
            return f'DÍGITOS distintos en {ruta}: EN {en!r} → {tr!r}'
        for marca in MARCAS:
            if re.search(r'\b' + re.escape(marca) + r'\b', en) and marca not in tr:
                return f'falta la marca «{marca}» en {ruta}: {tr!r}'
        if '"' in tr:
            return f'comilla recta dentro del valor en {ruta}'
    return revisar_tratamiento(lang, data)


def traducir(lang, en_raw, base):
    prompt = (
        f'Traduce del inglés al {IDIOMAS[lang]} el siguiente JSON de copy de la portada y '
        'la sección de precios de aichef.pro (SaaS de agentes de IA para chefs y '
        'restaurantes).\n\nREGLAS ESTRICTAS:\n'
        '1. Devuelve ÚNICAMENTE el JSON traducido. Sin explicaciones, sin ```.\n'
        '2. Estructura EXACTAMENTE igual: mismas claves, mismo número de elementos en cada '
        'lista. No añadas ni quites nada. Las CLAVES no se traducen.\n'
        f'3. NO traduzcas: {", ".join(MARCAS)}. «AI Chef Pro» siempre literal.\n'
        '4. Conserva TODOS los números con su valor exacto (10,000 · 85,000 · 175,000 · 200 '
        f'· 100 · 75+ · 25+ · 30% · 10 · 6). Formato del idioma: {FORMATO_NUM[lang]}.\n'
        '5. Conserva los símbolos ≈ · → + % € tal cual, en la misma posición lógica.\n'
        '6. Es copy comercial para chefs y hosteleros PROFESIONALES: preciso, directo, '
        'humano, sin jerga corporativa. «the pass» es el pase de cocina; «cover count» son '
        'los cubiertos/comensales; «food cost» puede quedarse como food cost si es el uso '
        'habitual del sector en ese idioma; «cost calcs» son cálculos de costes/escandallos.\n'
        '7. Las cadenas "v2_title_prefix" y "v2_title_suffix" forman el H1 con una palabra '
        'rotatoria en medio (Pizzería, Panadería, Restaurante…) y después la marca: '
        '«{prefix} {Pizzería} {suffix} AI Chef Pro». Tradúcelas para que la frase completa '
        'sea natural con cualquier tipo de negocio en medio. Los sufijos "v2_included_prefix"/'
        '"v2_included_suffix" rodean el nombre del plan de entrada: «{prefix} AI Chef Member '
        '{suffix}».\n'
        f'8. Escribe SOLO en {IDIOMAS[lang]}. Ningún carácter de otro alfabeto.\n'
        '9. NUNCA uses la comilla doble recta (") dentro de los VALORES.\n'
        f'10. TRATAMIENTO AL LECTOR: {TRATAMIENTO[lang]}\n\n'
        f'JSON:\n{en_raw}'
    )
    intentos = [
        ('anthropic/claude-sonnet-4.6', '8192'),
        ('~deepseek/deepseek-v4-flash-latest', '16000'),
    ]
    ultimo = 'sin intentos'
    for n, (modelo, tokens) in enumerate(intentos):
        cmd = [PYBIN, BRIDGE, '--task', 'translation', '--domain', 'aichef', '--lang', lang,
               '--model', modelo, '--max-tokens', tokens, '--temperature', '0.2',
               '--strict-lang', '--prompt', prompt]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired:
            ultimo = f'{modelo}: timeout 600 s'
            continue
        out = (r.stdout or '').strip()
        if r.returncode != 0 or not out:
            ultimo = f'{modelo}: bridge código {r.returncode} / salida {"vacía" if not out else "ok"} / {(r.stderr or "")[-300:]}'
            continue
        m = re.search(r'```(?:json)?\s*(.*?)```', out, re.S)
        if m:
            out = m.group(1).strip()
        i = out.find('{')
        if i > 0:
            out = out[i:]
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            try:
                data = json.loads(repara_comillas(out))
                print('    (JSON reparado: comillas rectas)')
            except json.JSONDecodeError as e:
                ultimo = f'{modelo}: JSON inválido: {e}'
                continue
        err = validar(lang, data, base)
        if err:
            ultimo = f'{modelo}: {err}'
            continue
        if n:
            print(f'    (resuelto con {modelo}; antes: {ultimo})')
        return data, None
    return None, ultimo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', choices=sorted(IDIOMAS))
    ap.add_argument('--todos', action='store_true')
    a = ap.parse_args()
    langs = sorted(IDIOMAS) if a.todos else ([a.lang] if a.lang else [])
    if not langs:
        sys.exit('indica --lang <xx> o --todos')
    en_raw = (DIR / 'keak-copy.en.json').read_text(encoding='utf-8')
    base = json.loads(en_raw)
    fallos = 0
    for lang in langs:
        print(f'· {lang} …', flush=True)
        data, err = traducir(lang, en_raw, base)
        if err:
            print(f'  ✗ {err}', flush=True)
            fallos += 1
            continue
        (DIR / f'keak-copy.{lang}.json').write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'  ✓ keak-copy.{lang}.json ({len(pares(data))} cadenas)', flush=True)
    print(f'\n{len(langs) - fallos} ok / {fallos} fallos')
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
