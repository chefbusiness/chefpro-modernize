#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Traduce copy/es.json a los otros 6 idiomas del mailing del hito 1M.

Reutiliza los gates del traductor de la Fase 12 (fase12-traducir-copy.py): misma
estructura que el español, ningún alfabeto ajeno, tratamiento del sitio (fr vous ·
de Sie · it tu · pt você · nl u) y reparación de las comillas alemanas.

Motor: anthropic/claude-sonnet-4.6 vía bridge.py (el mailing lo lee toda la lista y
DeepSeek ya inyectó CJK en contenido ES: CLAUDE.md 2026-08-08); DeepSeek flash de reserva.
El bridge.py del Mac no admite --strict-lang: el barrido lo hace SOSPECHOSO aquí.

    python3 traducir.py --todos | --lang fr
"""
import argparse, importlib.util, json, re, subprocess, sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
RAIZ = DIR.parents[3]
BRIDGE = '/Users/johnguerrero/chefbusiness-ai/bridge.py'
if not Path(BRIDGE).exists():
    BRIDGE = '/root/chefbusiness-ai/bridge.py'
PYBIN = sys.executable

_spec = importlib.util.spec_from_file_location(
    'tr', RAIZ / 'scripts' / 'astro-migration' / 'fase12-traducir-copy.py')
_tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tr)

IDIOMAS = {'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'it': 'Italiano',
           'pt': 'Português de Portugal', 'nl': 'Nederlands'}
SOLO_ES = ('h_afinados', 'p_afinados')   # bloque que sólo se monta en ES
MARCAS = ['AI Chef Pro', 'Modelos IA + LLM', 'Grok', 'Sonar', 'John Guerrero']
FORMATO_NUM = {
    'en': '1,000,000 · €10 a month · 10,000 credits · food cost of 30%',
    'fr': '1 000 000 · 10 € par mois · 10 000 crédits · food cost de 30 %',
    'de': '1.000.000 · 10 € im Monat · 10.000 Credits · Wareneinsatz von 30 %',
    'it': '1.000.000 · 10 € al mese · 10.000 crediti · food cost del 30%',
    'pt': '1 000 000 · 10 € por mês · 10 000 créditos · food cost de 30%',
    'nl': '1.000.000 · € 10 per maand · 10.000 credits · food cost van 30%',
}


def traducir(lang, base):
    src = {k: v for k, v in base.items() if k not in SOLO_ES}
    es_raw = json.dumps(src, ensure_ascii=False, indent=2)
    trat = _tr.TRATAMIENTO.get(lang)
    prompt = (
        'Traduce al %s el siguiente JSON: es el copy de un correo a los usuarios de AI Chef Pro '
        '(agentes de IA para chefs y hosteleros) que celebra el millón de consultas resueltas.\n\n'
        'REGLAS ESTRICTAS:\n'
        '1. Devuelve UNICAMENTE el JSON traducido. Sin explicaciones, sin ```.\n'
        '2. Mismas claves, mismo numero de elementos. No anadas ni quites nada.\n'
        '3. NO traduzcas las marcas ni los nombres propios: %s. El nombre de la seccion '
        '«Modelos IA + LLM» se deja tal cual.\n'
        '4. Conserva las etiquetas HTML (<strong>, &amp;, &nbsp;) donde esten.\n'
        '5. Es un correo de marketing para profesionales: tono cercano y humano, no corporativo. '
        'Adapta la expresion al idioma en vez de calcar la sintaxis del espanol. El asunto '
        '("subject") tiene que sonar natural y atractivo en %s.\n'
        '6. Escribe SOLO en %s. Ni una palabra en espanol ni en ningun otro idioma, y ningun '
        'caracter de otro alfabeto.\n'
        '7. NUNCA uses la comilla doble recta (") dentro de los VALORES. Usa las comillas '
        'tipograficas del idioma.\n'
        '8. Cifras y precios en el formato de ese idioma: %s.\n'
        '9. La clave "conj" es la conjuncion que une el ultimo elemento de una lista de nombres '
        '(en espanol «y»): pon la de %s.\n'
        '%s\n'
        'JSON:\n%s' % (IDIOMAS[lang], ', '.join(MARCAS), IDIOMAS[lang], IDIOMAS[lang],
                       FORMATO_NUM[lang], IDIOMAS[lang],
                       ('10. TRATAMIENTO AL LECTOR: %s\n' % trat) if trat else '', es_raw))
    intentos = [('anthropic/claude-sonnet-4.6', '8192'),
                ('~deepseek/deepseek-v4-flash-latest', '16000')]
    err = 'sin intentos'
    for modelo, tokens in intentos:
        cmd = [PYBIN, BRIDGE, '--task', 'translation', '--domain', 'aichef', '--lang', lang,
               '--model', modelo, '--max-tokens', tokens, '--temperature', '0.3', '--prompt', prompt]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        out = (r.stdout or '').strip()
        if r.returncode != 0 or not out:
            err = 'bridge codigo %d / salida %s' % (r.returncode, 'vacia' if not out else 'ok')
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
                data = json.loads(_tr.repara_comillas(out))
                print('    (JSON reparado)')
            except json.JSONDecodeError as e:
                err = 'JSON invalido: %s' % e
                continue
        if _tr.forma(data) != _tr.forma(src):
            err = 'la ESTRUCTURA no coincide con el espanol'
            continue
        malos = [t for t in _tr.textos(data) if _tr.SOSPECHOSO.search(t)]
        if malos:
            err = 'caracteres de otro alfabeto: %r' % malos[0][:80]
            continue
        e2 = _tr.revisar_tratamiento(lang, data)
        if e2:
            err = e2
            continue
        faltan = [m_ for m_ in ('AI Chef Pro',) if m_ not in ' '.join(_tr.textos(data))]
        if faltan:
            err = 'falta la marca %s' % faltan
            continue
        if '{{{' in ' '.join(_tr.textos(data)):
            err = 'token de baja dentro del copy'
            continue
        for k in SOLO_ES:
            data[k] = ''
        print('    ok con %s' % modelo)
        return data, None
    return None, err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang')
    ap.add_argument('--todos', action='store_true')
    a = ap.parse_args()
    langs = list(IDIOMAS) if a.todos else [a.lang]
    base = json.loads((DIR / 'copy' / 'es.json').read_text(encoding='utf-8'))
    fallos = []
    for lang in langs:
        print('== %s' % lang, flush=True)
        data, err = traducir(lang, base)
        if err:
            print('    FALLO: %s' % err, flush=True)
            fallos.append(lang)
            continue
        (DIR / 'copy' / ('%s.json' % lang)).write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('    asunto: %s' % data['subject'], flush=True)
    if fallos:
        sys.exit('idiomas fallidos: %s' % fallos)


if __name__ == '__main__':
    main()
