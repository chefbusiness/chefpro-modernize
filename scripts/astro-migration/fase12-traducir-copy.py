#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 12 — traduce el copy de la landing de INTEGRACIONES a los 6 idiomas.

POR QUÉ ASÍ: la REGLA CAPITAL manda que la prosa larga salga de `bridge.py`, no
de tokens de Claude. El español lo escribe una persona (son afirmaciones de
producto: qué hace la conexión, qué pasa con las credenciales) y de ahí salen las
seis traducciones.

GATES, porque este copy va a producción en 7 idiomas:
  · La estructura del JSON traducido debe ser IDÉNTICA a la del español —mismas
    claves, mismas longitudes de lista—. Si el modelo se inventa o se come una
    clave, la plantilla reventaría en el build (o peor: pintaría `undefined`).
  · Barrido de caracteres no latinos. Ver CLAUDE.md: `deepseek-v4-pro` llegó a
    inyectar chino en mitad de una frase y tres de esos textos salieron vivos a
    producción. Se pasa `--strict-lang` al bridge Y se revisa aquí.
  · Las MARCAS no se traducen. «Google Sheets» es «Google Sheets» en neerlandés.

Uso:
    python3 fase12-traducir-copy.py --lang fr           # una
    python3 fase12-traducir-copy.py --todos             # las seis
"""
import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

DIR = Path(__file__).parent / 'fase12-copy'
BRIDGE = '/root/chefbusiness-ai/bridge.py'
PYBIN = '/root/chefbusiness-ai/.venv/bin/python'

IDIOMAS = {
    'en': ('English', '/en/integrations', 'Integrations'),
    'fr': ('Français', '/fr/integrations', 'Intégrations'),
    'de': ('Deutsch', '/de/integrationen', 'Integrationen'),
    'it': ('Italiano', '/it/integrazioni', 'Integrazioni'),
    'pt': ('Português de Portugal', '/pt/integracoes', 'Integrações'),
    'nl': ('Nederlands', '/nl/integraties', 'Integraties'),
}

# TRATAMIENTO — no es cosmético: si la landing tutea y el resto del sitio trata
# de usted, el visitante nota el remiendo. Medido sobre src/i18n/locales/*.json
# el 2026-09-05 (ocurrencias formal vs informal en el sitio ya publicado):
#   es 306 informal · fr 405 formal · de 1009 formal · it 307 informal ·
#   pt 233 formal · nl 452 formal
# El español original tutea, así que TODO idioma formal necesita que se le diga
# expresamente: la primera pasada del francés vino con «tu/tes» y había que
# tirarla. El inglés no distingue.
TRATAMIENTO = {
    'en': None,
    'fr': 'Trata al lector de VOUS (vouvoiement). Nunca de «tu».',
    'de': 'Trata al lector de SIE (Siezen). Nunca de «du».',
    'it': 'Trata al lector de TU, como en el original.',
    'pt': 'Trata al lector de VOCE. Nunca de «tu».',
    'nl': 'Trata al lector de U (formal). Nunca de «je» o «jij».',
}

# Marcas que NO se traducen jamás.
MARCAS = ['AI Chef Pro', 'Gmail', 'Outlook', 'Google Sheets', 'Google Docs',
          'Google Drive', 'Google Calendar', 'Google Super', 'Notion', 'Canva',
          'LinkedIn', 'Facebook', 'Instagram', 'X (Twitter)', 'TikTok',
          'WordPress', 'Reddit', 'Composio']

# Rangos que delatan una inyección de otro alfabeto (CLAUDE.md, 2026-08-08).
SOSPECHOSO = re.compile(
    r'[　-鿿一-鿿Ѐ-ӿ가-힯'
    r'؀-ۿ֐-׿฀-๿぀-ヿ]')


def forma(o):
    """Firma estructural del JSON: claves y longitudes, sin los textos."""
    if isinstance(o, dict):
        return {k: forma(v) for k, v in sorted(o.items())}
    if isinstance(o, list):
        return [forma(x) for x in o]
    return type(o).__name__


def textos(o, acc=None):
    acc = [] if acc is None else acc
    if isinstance(o, dict):
        for v in o.values():
            textos(v, acc)
    elif isinstance(o, list):
        for v in o:
            textos(v, acc)
    elif isinstance(o, str):
        acc.append(o)
    return acc


# Marcadores para COMPROBAR el tratamiento en el texto devuelto. Un modelo puede
# ignorar la instrucción, así que se mide sobre el resultado.
MARCADORES = {
    'fr': (r"\b(vous|votre|vos)\b", r"\b(tu|ton|ta|tes|toi)\b"),
    'de': (r"\b(Sie|Ihre|Ihrem|Ihren|Ihr)\b", r"\b(du|dein|deine|deinem|dich|dir)\b"),
    'pt': (r"\b(você|vocês|o seu|a sua|seus|suas)\b", r"\b(tu|teu|tua|teus|tuas)\b"),
    'nl': (r"\b(u|uw)\b", r"\b(je|jij|jouw|jullie)\b"),
    'it': (r"\b(Lei|La Sua|Il Suo)\b", r"\b(tu|tuo|tua|tuoi|tue)\b"),
}
# Cuál de los dos DEBE ganar en cada idioma.
ESPERADO = {'fr': 'formal', 'de': 'formal', 'pt': 'formal', 'nl': 'formal',
            'it': 'informal'}


def revisar_tratamiento(lang, data):
    """Devuelve un error si el texto usa el tratamiento contrario al del sitio."""
    if lang not in MARCADORES:
        return None
    formal_re, informal_re = (re.compile(p, re.I) for p in MARCADORES[lang])
    blob = ' '.join(textos(data))
    nf = len(formal_re.findall(blob))
    ni = len(informal_re.findall(blob))
    gana = 'formal' if nf > ni else 'informal'
    if gana != ESPERADO[lang]:
        return ('tratamiento %s (formal=%d, informal=%d) pero el sitio usa %s '
                '— retraducir' % (gana, nf, ni, ESPERADO[lang]))
    return None


# El aleman cierra las comillas con „ … " y el modelo emite ese cierre como
# comilla RECTA (U+0022), que termina la cadena JSON. Paso con los dos motores y
# aun despues de pedirle expresamente que no lo hiciera, asi que se deja de
# confiar en la instruccion y se repara.
#
# Es seguro porque el JSON viene impreso con una clave por linea: se toma lo que
# hay ENTRE la primera y la ultima comilla de la linea y se escapa cualquier
# comilla suelta de dentro. No toca las comillas estructurales.
_LINEA_VALOR = re.compile(r'^(\s*"[A-Za-z_][\w]*"\s*:\s*")(.*)("\s*,?)$')
_LINEA_ITEM = re.compile(r'^(\s*")(.*)("\s*,?)$')


def repara_comillas(raw):
    """Escapa comillas rectas sueltas dentro de los valores de un JSON impreso."""
    fuera = []
    for linea in raw.split('\n'):
        m = _LINEA_VALOR.match(linea) or _LINEA_ITEM.match(linea)
        if m:
            dentro = m.group(2)
            # \" ya escapada -> se protege; el resto de " se escapa
            dentro = dentro.replace('\\"', '\x00').replace('"', '\\"').replace('\x00', '\\"')
            linea = m.group(1) + dentro + m.group(3)
        fuera.append(linea)
    return '\n'.join(fuera)


def traducir(lang, es_raw, base):
    nombre, path, breadcrumb = IDIOMAS[lang]
    prompt = (
        'Traduce al %s el siguiente JSON de copy de una landing comercial.\n\n'
        'REGLAS ESTRICTAS:\n'
        '1. Devuelve UNICAMENTE el JSON traducido. Sin explicaciones, sin ```.\n'
        '2. La estructura debe ser EXACTAMENTE la misma: mismas claves, mismo\n'
        '   numero de elementos en cada lista. No anadas ni quites nada.\n'
        '3. NO traduzcas los nombres de marca: %s.\n'
        '4. Los campos "lang", "path" y "breadcrumb" NO se traducen: ponlos con\n'
        '   estos valores exactos -> "lang": "%s", "path": "%s", '
        '"breadcrumb": "%s".\n'
        '5. Es copy de marketing para chefs y hosteleros profesionales: tono\n'
        '   cercano y humano, no corporativo. Adapta la expresion al idioma en\n'
        '   vez de calcar la sintaxis del espanol.\n'
        '6. Escribe SOLO en %s. Ni una palabra en espanol ni en ningun otro\n'
        '   idioma, y ningun caracter de otro alfabeto.\n'
        '7. NUNCA uses el caracter de comilla doble recta (") dentro de los\n'
        '   VALORES del JSON: rompe la cadena. Para entrecomillar dentro de una\n'
        '   frase usa comillas tipograficas del idioma (por ejemplo « » en\n'
        '   frances, „ “ en aleman, “ ” en ingles). El original ya usa « ».\n'
        '%s\n'
        'JSON:\n%s' % (nombre, ', '.join(MARCAS), lang, path, breadcrumb,
                       nombre,
                       ('8. TRATAMIENTO AL LECTOR: %s\n' % TRATAMIENTO[lang])
                       if TRATAMIENTO.get(lang) else '',
                       es_raw))

    # CLAUDE.md: DeepSeek se atasca en algunos prompts y devuelve VACÍO, y subir
    # el presupuesto de tokens NO lo arregla (la FAQ del garum volvió vacía con
    # 24.000 y otra vez con 48.000; salió a la primera con otro motor y 8.192).
    # Así que el reintento NO duplica tokens: cambia de motor.
    #
    # Y el reintento cubre CUALQUIER fallo de validación, no sólo la respuesta
    # vacía: el italiano de la primera tanda volvió con el JSON cortado a medias
    # («Unterminated string»), que es el mismo problema —presupuesto agotado—
    # disfrazado de error de sintaxis. Si sólo se reintenta al ver un vacío, ese
    # caso se pierde.
    intentos = [
        ('~deepseek/deepseek-v4-flash-latest', '16000'),
        ('anthropic/claude-sonnet-4.6', '8192'),
    ]

    ultimo_err = 'sin intentos'
    for n, (modelo, tokens) in enumerate(intentos):
        cmd = [PYBIN, BRIDGE, '--task', 'translation', '--domain', 'aichef',
               '--lang', lang, '--model', modelo, '--max-tokens', tokens,
               '--temperature', '0.3', '--strict-lang', '--prompt', prompt]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        out = (r.stdout or '').strip()

        if r.returncode != 0 or not out:
            ultimo_err = 'bridge codigo %d / salida %s' % (
                r.returncode, 'vacia' if not out else 'ok')
            continue

        # A veces envuelve en ``` pese a pedirle que no, o antepone prosa.
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
                print('    (JSON reparado: comillas rectas dentro de los valores)')
            except json.JSONDecodeError as e:
                ultimo_err = 'JSON invalido aun tras reparar: %s' % e
                continue

        if forma(data) != forma(base):
            ultimo_err = 'la ESTRUCTURA no coincide con el espanol'
            continue

        malos = [t for t in textos(data) if SOSPECHOSO.search(t)]
        if malos:
            ultimo_err = 'caracteres de otro alfabeto: %r' % malos[0][:80]
            continue

        err = revisar_tratamiento(lang, data)
        if err:
            ultimo_err = err
            continue

        for campo, val in (('lang', lang), ('path', path), ('breadcrumb', breadcrumb)):
            data[campo] = val

        if n:
            print('    (resuelto con %s; el primer motor fallo por: %s)'
                  % (modelo, ultimo_err))
        return data, None

    return None, ultimo_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', choices=sorted(IDIOMAS))
    ap.add_argument('--todos', action='store_true')
    args = ap.parse_args()

    langs = sorted(IDIOMAS) if args.todos else ([args.lang] if args.lang else [])
    if not langs:
        sys.exit('indica --lang <xx> o --todos')

    es_path = DIR / 'es.json'
    es_raw = es_path.read_text(encoding='utf-8')
    base = json.loads(es_raw)

    fallos = 0
    for lang in langs:
        destino = DIR / ('%s.json' % lang)
        print('· %s …' % lang, flush=True)
        data, err = traducir(lang, es_raw, base)
        if err:
            print('  ✗ %s' % err)
            fallos += 1
            continue
        destino.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('  ✓ %s (%d cadenas)' % (destino.name, len(textos(data))))

    print('\n%d ok / %d fallos' % (len(langs) - fallos, fallos))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
