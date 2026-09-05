#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 12 — traduce el post de la actualización de agentes a los 5 idiomas.

DOS LLAMADAS POR IDIOMA, a propósito:
  1. El CUERPO, que es Markdown y viaja como texto plano. Meterlo dentro de un
     JSON obliga a escapar comillas y saltos de línea, y ahí es donde se rompen
     los modelos (el alemán ya rompió un JSON con su comilla de cierre „…").
  2. Los METADATOS (título, descripción, alt de imágenes y FAQ), que sí son un
     JSON pequeño y se validan por estructura.

GATES sobre lo traducido, los mismos que en el resto de la fase más dos propios
del blog:
  · Nada de H1 en el cuerpo: el layout ya pinta uno (fase8c-h1-unico.py).
  · La TABLA de las 16 plataformas tiene que seguir ahí y con sus 16 filas: es el
     bloque con más valor del post y es justo lo que un modelo tiende a resumir.
  · Tratamiento (vous/Sie/você/u) según la convención medida del sitio.
  · Barrido de alfabetos ajenos.

Uso:
    python3 fase12-post-traducir.py --lang fr
    python3 fase12-post-traducir.py --todos
"""
import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

DIR = Path(__file__).parent
COPY = DIR / 'fase12-post-copy'
CUERPOS = DIR / 'fase12-post-cuerpo'

_spec = importlib.util.spec_from_file_location(
    'tr', DIR / 'fase12-traducir-copy.py')
_tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tr)

IDIOMAS = {
    'en': ('English', 'ai-agents-connect-gmail-sheets-instagram'),
    'fr': ('Français', 'agents-ia-connectes-gmail-sheets-instagram'),
    'de': ('Deutsch', 'ki-agenten-gmail-sheets-instagram'),
    'it': ('Italiano', 'agenti-ia-collegati-gmail-sheets-instagram'),
    'pt': ('Português de Portugal', 'agentes-ia-ligados-gmail-sheets-instagram'),
}

# (modelo, max_tokens, timeout). El timeout del PRIMERO es corto a propósito:
# medido el 2026-09-05 sobre este mismo contenido, DeepSeek se quedó 40 minutos
# sin devolver nada mientras Sonnet resolvía el artículo entero en cinco. Se le
# da su oportunidad porque es mucho más barato, pero no se le espera media hora.
MOTORES = [('~deepseek/deepseek-v4-flash-latest', '16000', 420),
           ('anthropic/claude-sonnet-4.6', '8192', 900)]


def bridge(lang, prompt, tarea):
    ultimo = 'sin intentos'
    for modelo, tokens, tope in MOTORES:
        try:
            r = subprocess.run(
                [_tr.PYBIN, _tr.BRIDGE, '--task', tarea, '--domain', 'aichef',
                 '--lang', lang, '--model', modelo, '--max-tokens', tokens,
                 '--temperature', '0.3', '--strict-lang', '--prompt', prompt],
                capture_output=True, text=True, timeout=tope)
        except subprocess.TimeoutExpired:
            ultimo = '%s agoto los %ds' % (modelo, tope)
            continue
        out = (r.stdout or '').strip()
        if r.returncode == 0 and out:
            return out, modelo
        ultimo = 'codigo %d, salida %s' % (r.returncode, 'vacia' if not out else 'ok')
    return None, ultimo


def recorta_json(txt):
    """Devuelve el primer objeto JSON completo del texto.

    Buscar sólo el primer `{` no basta: el modelo a veces añade una frase
    DESPUÉS del JSON («Extra data: line 35») y a veces antes. Se cuentan llaves
    ignorando las que van dentro de cadenas, y se corta en la que cierra.
    """
    i = txt.find('{')
    if i < 0:
        return txt
    prof, en_cadena, escapa = 0, False, False
    for j in range(i, len(txt)):
        c = txt[j]
        if escapa:
            escapa = False
            continue
        if c == '\\':
            escapa = True
            continue
        if c == '"':
            en_cadena = not en_cadena
            continue
        if en_cadena:
            continue
        if c == '{':
            prof += 1
        elif c == '}':
            prof -= 1
            if prof == 0:
                return txt[i:j + 1]
    return txt[i:]


def filas_tabla(md):
    """Cuenta las filas de datos de la tabla más larga del Markdown."""
    mejor = 0
    actual = 0
    for l in md.split('\n'):
        if l.strip().startswith('|') and l.strip().endswith('|'):
            if not re.match(r'^\s*\|[\s:|-]+\|\s*$', l):
                actual += 1
        else:
            mejor = max(mejor, actual)
            actual = 0
    return max(mejor, actual)


def trocea(md):
    """Parte el artículo en intro + una pieza por cada `## `.

    Cada pieza lleva 0 o 1 encabezados, así que traducirlas por separado hace
    IMPOSIBLE que el modelo funda dos secciones o se invente una tercera.
    """
    piezas, actual = [], []
    for linea in md.split('\n'):
        if linea.startswith('## ') and actual:
            piezas.append('\n'.join(actual).strip())
            actual = [linea]
        else:
            actual.append(linea)
    if actual:
        piezas.append('\n'.join(actual).strip())
    return [p for p in piezas if p]


def traduce_cuerpo(lang, es_md):
    """Traduce POR SECCIONES.

    La primera versión mandaba el artículo entero y confiaba en que el modelo
    conservara los 5 encabezados. No lo hace: el alemán volvió con 6 y luego con
    4, y el portugués con 6, oscilando entre reintentos. Trocear por `## ` y
    traducir cada pieza suelta convierte el problema en imposible por
    construcción: si una pieza tenía un encabezado, la traducida tiene ese.
    """
    nombre, _ = IDIOMAS[lang]
    trato = _tr.TRATAMIENTO.get(lang)
    piezas_es = trocea(es_md)
    fuera = []

    for n, pieza in enumerate(piezas_es):
        tiene_h2 = pieza.startswith('## ')
        filas = filas_tabla(pieza)
        reglas = [
            'Devuelve UNICAMENTE el Markdown traducido, sin ``` ni comentarios.',
            ('Empieza por el encabezado de nivel ## y no anadas NINGUN otro '
             'encabezado.' if tiene_h2
             else 'NO anadas ningun encabezado: este fragmento no lleva.'),
            ('Conserva la tabla con sus %d filas de datos, sin resumirla.' % filas)
            if filas else None,
            ('NO traduzcas marcas: AI Chef Pro, Gmail, Outlook, Google Sheets, '
             'Google Docs, Google Drive, Google Calendar, Google Super, Notion, '
             'Canva, LinkedIn, Facebook, Instagram, X (Twitter), TikTok, '
             'WordPress, Reddit, Composio.'),
            'Tono cercano y natural, para chefs y hosteleros profesionales.',
            'Escribe SOLO en %s, sin caracteres de otro alfabeto.' % nombre,
            ('TRATAMIENTO AL LECTOR: %s' % trato) if trato else None,
        ]
        prompt = ('Traduce al %s este fragmento de un articulo de blog.\n\nREGLAS:\n%s'
                  '\n\nFRAGMENTO:\n%s'
                  % (nombre,
                     '\n'.join('%d. %s' % (k + 1, r)
                                for k, r in enumerate([x for x in reglas if x])),
                     pieza))

        out, motor = bridge(lang, prompt, 'translation')
        if not out:
            return None, 'seccion %d/%d: bridge no devolvio nada (%s)' % (n + 1, len(piezas_es), motor)
        m = re.search(r'```(?:markdown)?\s*(.*?)```', out, re.S)
        if m and m.group(1).strip():
            out = m.group(1).strip()

        n_h2 = len(re.findall(r'^## ', out, re.M))
        if n_h2 != (1 if tiene_h2 else 0):
            return None, 'seccion %d/%d: %d encabezados donde tocaba %d' % (
                n + 1, len(piezas_es), n_h2, 1 if tiene_h2 else 0)
        if re.search(r'^# ', out, re.M):
            return None, 'seccion %d/%d: trae un H1' % (n + 1, len(piezas_es))
        if filas and filas_tabla(out) != filas:
            return None, 'seccion %d/%d: la tabla tiene %d filas y deberia tener %d' % (
                n + 1, len(piezas_es), filas_tabla(out), filas)
        raro = _tr.SOSPECHOSO.search(out)
        if raro:
            return None, 'seccion %d/%d: caracter de otro alfabeto %r' % (n + 1, len(piezas_es), raro.group(0))
        fuera.append(out.strip())

    completo = '\n\n'.join(fuera)

    # Controles sobre el conjunto ya montado
    h2, h2_es = (len(re.findall(r'^## ', x, re.M)) for x in (completo, es_md))
    if h2 != h2_es:
        return None, 'el montaje tiene %d H2 y el espanol %d' % (h2, h2_es)
    pal, pal_es = len(completo.split()), len(es_md.split())
    if not (pal_es * 0.6 <= pal <= pal_es * 1.5):
        return None, 'longitud fuera de rango: %d palabras frente a %d' % (pal, pal_es)
    parrafos = [b.strip() for b in completo.split('\n\n') if len(b.split()) > 25]
    if len(parrafos) != len(set(parrafos)):
        return None, 'hay parrafos repetidos literalmente'

    return completo, None


def traduce_meta(lang, es_meta):
    nombre, slug = IDIOMAS[lang]
    trato = _tr.TRATAMIENTO.get(lang)
    base = {k: v for k, v in es_meta.items() if k != 'slug'}
    prompt = (
        'Traduce al %s este JSON de metadatos de un articulo de blog.\n\n'
        'REGLAS:\n'
        '1. Devuelve UNICAMENTE el JSON. Sin ```, sin explicaciones.\n'
        '2. Misma estructura exacta: mismas claves, misma cantidad de elementos.\n'
        '3. "description" debe quedar por debajo de 160 caracteres.\n'
        '4. NO traduzcas marcas: AI Chef Pro, Gmail, Google Sheets, Instagram,\n'
        '   Notion, Composio, Google Docs, Google Drive, Google Calendar,\n'
        '   Outlook, Canva, WordPress, LinkedIn, Facebook, TikTok, Reddit.\n'
        '5. NUNCA uses la comilla doble recta (") dentro de los valores: rompe\n'
        '   el JSON. Usa comillas tipograficas del idioma.\n'
        '6. Escribe SOLO en %s, sin caracteres de otro alfabeto.\n'
        '%s\n'
        'JSON:\n%s'
        % (nombre, nombre, ('7. TRATAMIENTO AL LECTOR: %s\n' % trato) if trato else '',
           json.dumps(base, ensure_ascii=False, indent=2)))

    out, motor = bridge(lang, prompt, 'translation')
    if not out:
        return None, 'bridge no devolvio nada (%s)' % motor
    m = re.search(r'```(?:json)?\s*(.*?)```', out, re.S)
    if m:
        out = m.group(1).strip()
    out = recorta_json(out)
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        # El aleman cierra comillas con „ … " y emite el cierre como comilla
        # RECTA, que termina la cadena JSON. Mismo reparador que fase12-traducir-copy.
        try:
            data = json.loads(_tr.repara_comillas(out))
            print('    (JSON reparado: comillas rectas dentro de los valores)')
        except json.JSONDecodeError as e:
            return None, 'JSON invalido aun tras reparar: %s' % e
    if _tr.forma(data) != _tr.forma(base):
        return None, 'la estructura del JSON no coincide con el espanol'
    malos = [t for t in _tr.textos(data) if _tr.SOSPECHOSO.search(t)]
    if malos:
        return None, 'caracteres de otro alfabeto: %r' % malos[0][:60]
    if len(data.get('description', '')) > 160:
        return None, 'description de %d caracteres (max 160)' % len(data['description'])
    data['slug'] = slug
    return data, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', choices=sorted(IDIOMAS))
    ap.add_argument('--todos', action='store_true')
    ap.add_argument('--solo-meta', action='store_true',
                    help='rehace solo los metadatos reutilizando el cuerpo ya traducido')
    args = ap.parse_args()

    langs = sorted(IDIOMAS) if args.todos else ([args.lang] if args.lang else [])
    if not langs:
        sys.exit('indica --lang <xx> o --todos')

    es_md = (CUERPOS / 'es.md').read_text(encoding='utf-8')
    es_meta = json.loads((COPY / 'es.json').read_text(encoding='utf-8'))

    fallos = 0
    for lang in langs:
        destino_cuerpo = CUERPOS / ('%s.md' % lang)
        if args.solo_meta and destino_cuerpo.exists():
            cuerpo = destino_cuerpo.read_text(encoding='utf-8')
            print('· %s — cuerpo reutilizado' % lang, flush=True)
        else:
            print('· %s — cuerpo…' % lang, flush=True)
            cuerpo, err = traduce_cuerpo(lang, es_md)
            if err:
                print('  ✗ cuerpo: %s' % err); fallos += 1; continue
            # Se persiste ya: si fallan los metadatos, no se tira el cuerpo bueno.
            destino_cuerpo.write_text(cuerpo + '\n', encoding='utf-8')

        print('· %s — metadatos…' % lang, flush=True)
        meta, err = traduce_meta(lang, es_meta)
        if err:
            print('  ✗ meta: %s' % err); fallos += 1; continue

        err = _tr.revisar_tratamiento(lang, {'a': cuerpo})
        if err:
            print('  ✗ %s' % err); fallos += 1; continue

        (CUERPOS / ('%s.md' % lang)).write_text(cuerpo + '\n', encoding='utf-8')
        (COPY / ('%s.json' % lang)).write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('  ✓ %s — %d palabras, tabla de %d filas'
              % (lang, len(cuerpo.split()), filas_tabla(cuerpo)))

    print('\n%d ok / %d fallos' % (len(langs) - fallos, fallos))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
