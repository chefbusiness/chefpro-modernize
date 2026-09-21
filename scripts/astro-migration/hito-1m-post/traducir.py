#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Traduce el post del hito 1M (cuerpo/es.md + copy/es.json) a en/fr/de/it/pt, ADAPTÁNDOLO a
cada plataforma: los nombres de agente son los del workspace de ese idioma (agentes-map.json,
extraído del HTML de cada app el 21-sep), las filas de agentes que NO existen en ese workspace
se eliminan, el modelo de OpenAI se llama ChatGPT 5.5 (EN) / ChatGPT 5 (resto), el recuento de
agentes es el del workspace (80 EN, 59 FR/DE/IT/PT) y la sección de los 35 afinados —sólo
verificada en ES— queda sin cifra ni lista. Enlaces internos: sólo los que existen en ese idioma
(los demás pierden el enlace y conservan el texto); gate: todos responden 200.

Reutiliza trocea()/filas_tabla()/recorta_json() de fase12-post-traducir.py y los gates de
fase12-traducir-copy.py (estructura, alfabetos, tratamiento, comillas alemanas). Motor: Sonnet
vía bridge.py (el del Mac no admite --strict-lang), DeepSeek flash de reserva.

    python3 traducir.py --lang en | --todos
"""
import argparse, importlib.util, json, re, subprocess, sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
PADRE = DIR.parent
BRIDGE = '/Users/johnguerrero/chefbusiness-ai/bridge.py'
if not Path(BRIDGE).exists():
    BRIDGE = '/root/chefbusiness-ai/bridge.py'
PYBIN = sys.executable


def _carga(nombre, fichero):
    spec = importlib.util.spec_from_file_location(nombre, PADRE / fichero)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_tr = _carga('tr', 'fase12-traducir-copy.py')
_p = _carga('p12', 'fase12-post-traducir.py')

MAPA = json.loads((DIR / 'agentes-map.json').read_text(encoding='utf-8'))

CFG = {
    'en': dict(nombre='English', slug='ai-chef-pro-one-million-queries', n=80, openai='ChatGPT 5.5', app='https://enapp.aichef.pro/',
               links={'https://aichef.pro/blog/modelos-open-source-ai-chef-pro': 'https://aichef.pro/en/blog/open-source-models-ai-chef-pro',
                      'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram': 'https://aichef.pro/en/blog/ai-agents-connect-gmail-sheets-instagram',
                      'https://aichef.pro/integraciones': 'https://aichef.pro/en/integrations',
                      'https://aichef.pro/libreria-de-prompts': 'https://aichef.pro/en/prompt-libraries',
                      'https://aichef.pro/blog/chatgpt-restaurantes-vs-ai-chef-pro-comparativa': 'https://aichef.pro/en/chatgpt-for-restaurants',
                      'https://aichef.pro/precios': 'https://aichef.pro/en/pricing'}),
    'fr': dict(nombre='Français', slug='ai-chef-pro-un-million-de-requetes', n=59, openai='ChatGPT 5', app='https://frapp.aichef.pro/',
               links={'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram': 'https://aichef.pro/fr/blog/agents-ia-connectes-gmail-sheets-instagram',
                      'https://aichef.pro/integraciones': 'https://aichef.pro/fr/integrations',
                      'https://aichef.pro/precios': 'https://aichef.pro/fr/tarifs'}),
    'de': dict(nombre='Deutsch', slug='ai-chef-pro-eine-million-anfragen', n=59, openai='ChatGPT 5', app='https://deapp.aichef.pro/',
               links={'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram': 'https://aichef.pro/de/blog/ki-agenten-gmail-sheets-instagram',
                      'https://aichef.pro/integraciones': 'https://aichef.pro/de/integrationen',
                      'https://aichef.pro/precios': 'https://aichef.pro/de/preise'}),
    'it': dict(nombre='Italiano', slug='ai-chef-pro-un-milione-di-richieste', n=59, openai='ChatGPT 5', app='https://itapp.aichef.pro/',
               links={'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram': 'https://aichef.pro/it/blog/agenti-ia-collegati-gmail-sheets-instagram',
                      'https://aichef.pro/integraciones': 'https://aichef.pro/it/integrazioni',
                      'https://aichef.pro/precios': 'https://aichef.pro/it/prezzi'}),
    'pt': dict(nombre='Português de Portugal', slug='ai-chef-pro-um-milhao-de-consultas', n=59, openai='ChatGPT 5', app='https://ptapp.aichef.pro/',
               links={'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram': 'https://aichef.pro/pt/blog/agentes-ia-ligados-gmail-sheets-instagram',
                      'https://aichef.pro/integraciones': 'https://aichef.pro/pt/integracoes',
                      'https://aichef.pro/precios': 'https://aichef.pro/pt/precos'}),
}
LINKS_ES = ['https://aichef.pro/blog/modelos-open-source-ai-chef-pro', 'https://aichef.pro/blog/agentes-ia-conectados-gmail-sheets-instagram',
            'https://aichef.pro/integraciones', 'https://aichef.pro/libreria-de-prompts',
            'https://aichef.pro/blog/chatgpt-restaurantes-vs-ai-chef-pro-comparativa', 'https://aichef.pro/precios', 'https://app.aichef.pro/']
MODELOS = ['Gemini 3.7 Flash', 'Grok 4.6', 'DeepSeek V4 Flash', 'Kimi K2.5', 'GLM-5.2', 'Sonar Deep Research']
MOTORES = [('anthropic/claude-sonnet-4.6', '8192', 420), ('~deepseek/deepseek-v4-flash-latest', '16000', 600)]


def bridge(lang, prompt):
    ultimo = 'sin intentos'
    for modelo, tokens, tope in MOTORES:
        try:
            r = subprocess.run([PYBIN, BRIDGE, '--task', 'translation', '--domain', 'aichef', '--lang', lang,
                                '--model', modelo, '--max-tokens', tokens, '--temperature', '0.3', '--prompt', prompt],
                               capture_output=True, text=True, timeout=tope)
        except subprocess.TimeoutExpired:
            ultimo = '%s agoto los %ds' % (modelo, tope); continue
        out = (r.stdout or '').strip()
        if r.returncode == 0 and out:
            return out, modelo
        ultimo = 'codigo %d, salida %s' % (r.returncode, 'vacia' if not out else 'ok')
    return None, ultimo


def prepara_es(lang, md):
    """Sustituye en el ORIGEN lo que no debe traducirse a ciegas: enlaces por idioma (los que no
    existen se dejan como texto plano) y la app del idioma."""
    c = CFG[lang]
    for es_url in LINKS_ES:
        if es_url == 'https://app.aichef.pro/':
            md = md.replace('[app.aichef.pro](https://app.aichef.pro/)', '[%s](%s)' % (c['app'].replace('https://', '').rstrip('/'), c['app']))
        elif es_url in c['links']:
            md = md.replace('(%s)' % es_url, '(%s)' % c['links'][es_url])
        else:
            md = re.sub(r'\[([^\]]+)\]\(%s\)' % re.escape(es_url), r'\1', md)
    # Filas de la tabla de agentes que NO existen en ese workspace: fuera ANTES de traducir.
    # Pedírselo al modelo no funcionó (DE dejó 11 filas, IT 10 en dos intentos cada uno).
    for es, t in MAPA[lang].items():
        if not isinstance(t, str):
            md = re.sub(r'^\| %s \|[^\n]*\n' % re.escape(es), '', md, flags=re.M)
    # Geografía: el original dice «tanto en España como en toda Hispanoamérica»; el modelo
    # inventaba «across the UK» / «en France»: se neutraliza en origen.
    md = md.replace('tanto en España como en toda Hispanoamérica', 'en todo el mundo')
    return md


def reglas_adaptacion(lang, pieza):
    c = CFG[lang]; mapa = MAPA[lang]
    r = []
    existentes = {es: t for es, t in mapa.items() if isinstance(t, str)}
    faltan = [es for es, t in mapa.items() if not isinstance(t, str)]
    citados = [es for es in mapa if es in pieza]
    if citados:
        r.append('NOMBRES DE AGENTE: usa EXACTAMENTE estos nombres, que son los de la plataforma en %s: %s.'
                 % (c['nombre'], '; '.join('«%s» → «%s»' % (es, existentes[es]) for es in citados if es in existentes)))
    borrar = [es for es in citados if es in faltan]
    if borrar:
        r.append('Estos agentes NO existen en la plataforma en %s: %s. Ya no están en la tabla; '
                 'reescribe las frases que los citan para que no aparezcan (sin inventar cifras). Si el texto '
                 'contrapone «creatividad» y «consultoría» y los agentes consultores no existen, di que lideran la '
                 'creatividad y los recetarios profesionales. Si hay un párrafo dedicado a «Calcula Pax», cámbialo por '
                 'uno equivalente sobre «%s» (planifica la comida del equipo): un agente sencillo que resuelve un dolor '
                 'cotidiano de cualquier cocina.' % (c['nombre'], ', '.join(borrar), existentes.get('Comida del Personal', 'Staff Meal')))
    if 'GPT-5.6 Luna' in pieza or 'GPT-5.5' in pieza:
        r.append('El modelo de OpenAI se llama «%s» en esta plataforma: sustituye «GPT-5.6 Luna» por «%s», elimina cualquier '
                 'mención a GPT-5.5 y a que se haya actualizado (en la columna Novedad pon «—»), y elimina las fechas «26 de agosto» '
                 'y «30 de agosto»: di que Gemini 3.7 Flash y Grok 4.6 son las incorporaciones más recientes.' % (c['openai'], c['openai']))
    if '91 agentes' in pieza or '91 ' in pieza:
        r.append('Donde diga «91 agentes especializados en español» pon «%d agentes especializados en %s»; conserva los siete idiomas.' % (c['n'], c['nombre']))
    if '35 ' in pieza and 'afinado' in pieza.lower():
        r.append('Esta sección habla de 35 agentes afinados esta semana en la plataforma en español. Para %s NO cites la cifra 35 '
                 '(tampoco en el encabezado) ni la lista de agentes: di que el equipo está revisando los agentes uno a uno tras la '
                 'migración y conserva lo demás (qué es afinar, qué nota el usuario, nada que activar).' % c['nombre'])
    if 'Perplexity' in pieza:
        r.append('NO traduzcas los nombres de modelos: %s, %s.' % (', '.join(MODELOS), c['openai']))
    return r


def traduce_cuerpo(lang, es_md):
    c = CFG[lang]; trato = _tr.TRATAMIENTO.get(lang)
    es_md = prepara_es(lang, es_md)
    piezas = _p.trocea(es_md)
    fuera = []
    for n, pieza in enumerate(piezas):
        tiene_h2 = pieza.startswith('## ')
        filas = _p.filas_tabla(pieza)
        borradas = sum(1 for es, t in MAPA[lang].items() if not isinstance(t, str) and re.search(r'^\| %s \|' % re.escape(es), pieza, re.M))
        esperadas = filas - borradas if filas else 0
        reglas = ['Devuelve UNICAMENTE el Markdown traducido, sin ``` ni comentarios.',
                  ('Empieza por el encabezado de nivel ## y no anadas NINGUN otro encabezado.' if tiene_h2 else 'NO anadas ningun encabezado: este fragmento no lleva.'),
                  ('La tabla debe quedar con %d filas de datos (tenia %d; se eliminan %d).' % (esperadas, filas, borradas)) if filas else None,
                  'Conserva los enlaces Markdown tal cual (misma URL); el texto del enlace sí se traduce. No anadas enlaces.',
                  'NO traduzcas la marca AI Chef Pro ni los nombres de modelos de IA.',
                  'Tono cercano y natural, de un fundador que escribe a profesionales de la hosteleria.',
                  'Escribe SOLO en %s, sin caracteres de otro alfabeto. Cifras en el formato de ese idioma.' % c['nombre'],
                  ('TRATAMIENTO AL LECTOR: %s' % trato) if trato else None] + reglas_adaptacion(lang, pieza)
        prompt = ('Traduce al %s este fragmento de un articulo del blog de AI Chef Pro, ADAPTANDOLO a la plataforma en ese idioma segun las reglas.\n\nREGLAS:\n%s\n\nFRAGMENTO:\n%s'
                  % (c['nombre'], '\n'.join('%d. %s' % (k + 1, r) for k, r in enumerate([x for x in reglas if x])), pieza))
        out, motor = bridge(lang, prompt)
        if not out:
            return None, 'seccion %d/%d: bridge no devolvio nada (%s)' % (n + 1, len(piezas), motor)
        m = re.search(r'```(?:markdown)?\s*(.*?)```', out, re.S)
        if m and m.group(1).strip():
            out = m.group(1).strip()
        n_h2 = len(re.findall(r'^## ', out, re.M))
        if n_h2 != (1 if tiene_h2 else 0):
            return None, 'seccion %d/%d: %d encabezados donde tocaba %d' % (n + 1, len(piezas), n_h2, 1 if tiene_h2 else 0)
        if re.search(r'^# ', out, re.M):
            return None, 'seccion %d/%d: trae un H1' % (n + 1, len(piezas))
        if filas and _p.filas_tabla(out) != esperadas:
            return None, 'seccion %d/%d: la tabla tiene %d filas y deberia tener %d' % (n + 1, len(piezas), _p.filas_tabla(out), esperadas)
        raro = _tr.SOSPECHOSO.search(out)
        if raro:
            return None, 'seccion %d/%d: caracter de otro alfabeto %r' % (n + 1, len(piezas), raro.group(0))
        fuera.append(out.strip())
    completo = '\n\n'.join(fuera)
    if len(re.findall(r'^## ', completo, re.M)) != len(re.findall(r'^## ', es_md, re.M)):
        return None, 'el montaje no tiene los mismos H2 que el espanol'
    pal, pal_es = len(completo.split()), len(es_md.split())
    if not (pal_es * 0.6 <= pal <= pal_es * 1.5):
        return None, 'longitud fuera de rango: %d palabras frente a %d' % (pal, pal_es)
    parrafos = [b.strip() for b in completo.split('\n\n') if len(b.split()) > 25]
    if len(parrafos) != len(set(parrafos)):
        return None, 'hay parrafos repetidos literalmente'
    # gates de adaptación
    for es, t in MAPA[lang].items():
        if not isinstance(t, str) and re.search(r'\b%s\b' % re.escape(es), completo):
            return None, 'cita al agente inexistente «%s»' % es
    for es in ['Cocina Creativa', 'Pastelería Creativa', 'Cocina Española', 'Comida del Personal']:
        t = MAPA[lang][es]
        if isinstance(t, str) and t not in completo:
            return None, 'falta el agente «%s» (%s)' % (t, es)
    if 'GPT-5.6' in completo or 'GPT-5.5' in completo or c['openai'] not in completo:
        return None, 'modelo de OpenAI mal adaptado'
    if re.search(r'\b35\b', completo):
        return None, 'sigue citando los 35 agentes afinados'
    permitidas = set(c['links'].values()) | {c['app']}
    # Un enlace que el modelo se inventa (PT añadió https://aichef.pro a secas) se convierte en
    # texto plano en vez de tumbar el idioma: el texto del enlace es válido, la URL no.
    def _sin_enlace(m):
        return m.group(1) if m.group(2) not in permitidas else m.group(0)
    completo = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', _sin_enlace, completo)
    urls = set(re.findall(r'\]\((https?://[^)\s]+)\)', completo))
    if not urls <= permitidas:
        return None, 'enlaces fuera del mapa: %s' % sorted(urls - permitidas)
    for u in sorted(urls):
        st = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '-L', '--max-time', '30', u], capture_output=True, text=True).stdout
        if st != '200':
            return None, 'enlace %s responde %s' % (u, st)
    err = _tr.revisar_tratamiento(lang, {'t': completo})
    if err:
        return None, err
    return completo, None


def traduce_meta(lang, es_meta):
    c = CFG[lang]; trato = _tr.TRATAMIENTO.get(lang)
    base = {k: v for k, v in es_meta.items() if k != 'slug'}
    prompt = ('Traduce al %s este JSON de metadatos de un articulo del blog de AI Chef Pro.\n\nREGLAS:\n'
              '1. Devuelve UNICAMENTE el JSON. Sin ```, sin explicaciones.\n'
              '2. Misma estructura exacta: mismas claves, misma cantidad de elementos.\n'
              '3. "description" por debajo de 160 caracteres. El "title" en el estilo de titulo del idioma.\n'
              '4. NO traduzcas AI Chef Pro ni los nombres de modelos (%s, %s).\n'
              '5. Donde diga «91 agentes» pon «%d agentes» (plataforma en %s). Donde cite «GPT-5.6 Luna en español» conserva ese dato '
              'tal cual (habla del espanol) y donde cite «Modelos IA + LLM» deja el nombre de la seccion en %s como en la plataforma.\n'
              '6. NO cites la cifra 35: donde diga «35 agentes afinados» di «los agentes afinados tras la migración».\n'
              '7. NUNCA uses la comilla doble recta (") dentro de los valores. Usa comillas tipograficas.\n'
              '8. Escribe SOLO en %s, sin caracteres de otro alfabeto.\n%s\nJSON:\n%s'
              % (c['nombre'], ', '.join(MODELOS), c['openai'], c['n'], c['nombre'], c['nombre'], c['nombre'],
                 ('9. TRATAMIENTO AL LECTOR: %s\n' % trato) if trato else '', json.dumps(base, ensure_ascii=False, indent=2)))
    out, motor = bridge(lang, prompt)
    if not out:
        return None, 'meta: bridge no devolvio nada (%s)' % motor
    m = re.search(r'```(?:json)?\s*(.*?)```', out, re.S)
    if m:
        out = m.group(1).strip()
    out = _p.recorta_json(out)
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        try:
            data = json.loads(_tr.repara_comillas(out)); print('    (JSON reparado)')
        except json.JSONDecodeError as e:
            return None, 'meta: JSON invalido: %s' % e
    if _tr.forma(data) != _tr.forma(base):
        return None, 'meta: estructura distinta'
    malos = [t for t in _tr.textos(data) if _tr.SOSPECHOSO.search(t)]
    if malos:
        return None, 'meta: alfabeto ajeno %r' % malos[0][:60]
    if len(data['description']) > 160:
        return None, 'meta: description de %d caracteres' % len(data['description'])
    if re.search(r'\b35\b', ' '.join(_tr.textos(data))):
        return None, 'meta: sigue citando la cifra 35'
    err = _tr.revisar_tratamiento(lang, data)
    if err:
        return None, 'meta: ' + err
    data['slug'] = c['slug']
    return data, None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--lang'); ap.add_argument('--todos', action='store_true'); ap.add_argument('--intentos', type=int, default=2)
    a = ap.parse_args()
    langs = list(CFG) if a.todos else [a.lang]
    es_md = (DIR / 'cuerpo' / 'es.md').read_text(encoding='utf-8').strip()
    es_meta = json.loads((DIR / 'copy' / 'es.json').read_text(encoding='utf-8'))
    fallos = []
    for lang in langs:
        print('== %s' % lang, flush=True)
        ok = False
        for intento in range(a.intentos):
            cuerpo, err = traduce_cuerpo(lang, es_md)
            if err:
                print('    cuerpo intento %d: %s' % (intento + 1, err), flush=True); continue
            meta, err = traduce_meta(lang, es_meta)
            if err:
                print('    meta intento %d: %s' % (intento + 1, err), flush=True); continue
            (DIR / 'cuerpo' / ('%s.md' % lang)).write_text(cuerpo + '\n', encoding='utf-8')
            (DIR / 'copy' / ('%s.json' % lang)).write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print('    OK: %d palabras · %s' % (len(cuerpo.split()), meta['title']), flush=True)
            ok = True; break
        if not ok:
            fallos.append(lang)
    if fallos:
        sys.exit('idiomas fallidos: %s' % fallos)


if __name__ == '__main__':
    main()
