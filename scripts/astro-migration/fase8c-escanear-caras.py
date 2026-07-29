#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8C — Escaneo de riesgo de imagen en el blog (caras y parecidos reales).

POR QUÉ. El 2026-07-28 se detectó `mermas-dashboard.jpg`: una imagen generada
por IA con el parecido inequívoco de Gordon Ramsay, con marca de un tercero
("CHEF'S TABLE"), dentro de un post comercial. Llevaba live desde febrero.
Riesgo de derechos de imagen y de endorsement implícito no autorizado. Además
la regla de marca del propio pipeline (skill generate-images) dice: "NO faces
shown directly, NO posed portraits".

CÓMO. Dos fases, para no gastar de más:
  FASE 1 (barata): por cada imagen, una pregunta binaria — ¿hay una cara humana
    reconocible y enfocada? Descarta de golpe las fotos de producto/plato.
  FASE 2 (solo sobre las que dieron SÍ): ¿se parece a alguna persona pública
    real? ¿hay marcas de terceros? ¿hay texto ilegible generado por IA?

Se ejecuta contra la API de Gemini, NO con agentes: son céntimos y cero tokens
del asistente. La salida es un JSON que un humano revisa.

FASE 3 (`--informe`): no llama a la API. Lee el JSON, ordena por gravedad y dice
en qué POST vive cada imagen, que es lo que hace falta para actuar:
  · CRÍTICO — parecido con persona pública real (confianza alta o media).
  · ALTO    — marca o logotipo de un tercero visible.
  · MEDIO   — retrato posado mirando a cámara (viola la regla de marca del
              pipeline de imágenes: "NO faces shown directly, NO posed portraits").
  · BAJO    — texto ilegible generado por IA.

Uso:
  python3 scripts/astro-migration/fase8c-escanear-caras.py --fase 1 [--limite N]
  python3 scripts/astro-migration/fase8c-escanear-caras.py --fase 2
  python3 scripts/astro-migration/fase8c-escanear-caras.py --informe
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
# TODA la colección, no sólo el español: desde 8B.6 hay 93 imágenes inglesas que
# vienen de otro WordPress y no las había visto nadie con este filtro.
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'
ASSETS = REPO / 'astro-site' / 'public' / 'blog-assets'
OUT = REPO / 'scripts' / 'astro-migration' / 'fase8c-escaneo-imagenes.json'
API = ('https://generativelanguage.googleapis.com/v1beta/models/'
       'gemini-2.5-flash:generateContent')

P1 = ("¿Hay en esta imagen al menos una CARA humana claramente visible y enfocada "
      "(no de espaldas, no borrosa al fondo, no recortada fuera de plano)? "
      "Responde EXACTAMENTE una palabra: SI o NO.")

P2 = ("Analiza esta imagen y responde en JSON compacto, sin markdown, con estas claves:\n"
      '{"parecido": "<nombre de la persona pública real a la que se parece, o NINGUNO>",\n'
      ' "confianza": "<alta|media|baja>",\n'
      ' "marcas_terceros": "<marcas o logotipos ajenos visibles, o NINGUNA>",\n'
      ' "texto_ilegible": "<SI si hay texto generado por IA sin sentido, si no NO>",\n'
      ' "retrato_posado": "<SI si es un retrato posado mirando a cámara, si no NO>"}\n'
      "Sé conservador: si no reconoces a nadie concreto, di NINGUNO.")


def key():
    k = os.environ.get('GEMINI_API_KEY', '')
    if k:
        return k
    sec = Path.home() / '.claude/skills/generate-images/secrets.env'
    if sec.exists():
        m = re.search(r'^export GEMINI_API_KEY="([^"]+)"', sec.read_text(), re.M)
        if m:
            return m.group(1)
    sys.exit('sin GEMINI_API_KEY')


def preguntar(path, prompt, api_key):
    mime = mimetypes.guess_type(str(path))[0] or 'image/jpeg'
    payload = {'contents': [{'parts': [
        {'inline_data': {'mime_type': mime,
                         'data': base64.b64encode(path.read_bytes()).decode()}},
        {'text': prompt}]}]}
    tmp = Path('/tmp/_escaneo_payload.json')
    tmp.write_text(json.dumps(payload))
    r = subprocess.run(['curl', '-s', '--max-time', '90', '-X', 'POST',
                        '%s?key=%s' % (API, api_key),
                        '-H', 'Content-Type: application/json',
                        '-d', '@' + str(tmp)], capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        if 'error' in d:
            return 'ERROR:' + str(d['error'].get('message', ''))[:90]
        return d['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        return 'ERROR:%s' % e


def referenciadas():
    """Sólo imágenes que un post publica: lo que no se sirve no es riesgo."""
    refs = set()
    for p in CONTENT.glob('*/*.md'):
        t = p.read_text(encoding='utf-8')
        for m in re.finditer(r'/blog-assets/([^"\'\s\)]+\.(?:jpg|jpeg|png|webp))', t):
            refs.add(m.group(1))
    return sorted(refs)


def posts_por_imagen():
    """{ruta relativa de la imagen: [posts que la publican]} — para poder actuar."""
    uso = {}
    for p in sorted(CONTENT.glob('*/*.md')):
        t = p.read_text(encoding='utf-8')
        for m in re.finditer(r'/blog-assets/([^"\'\s\)]+\.(?:jpg|jpeg|png|webp))', t):
            # Una misma imagen puede aparecer varias veces en el mismo post
            # (img + srcset + enlace): el post interesa UNA vez.
            quien = '%s/%s' % (p.parent.name, p.stem)
            if quien not in uso.setdefault(m.group(1), []):
                uso[m.group(1)].append(quien)
    return uso


def informe(datos):
    """Ordena los hallazgos de la fase 2 por gravedad. No llama a la API."""
    uso = posts_por_imagen()
    cubos = {'CRÍTICO': [], 'ALTO': [], 'MEDIO': [], 'BAJO': []}
    conteo = {}      # banderas secundarias, para no perderlas en el recuento
    sin_parsear = []
    for rel, v in sorted(datos.items()):
        crudo = v.get('riesgo')
        if not crudo:
            continue
        try:
            r = json.loads(re.sub(r'^```(?:json)?|```$', '', crudo.strip(), flags=re.M).strip())
        except Exception:
            sin_parsear.append(rel)
            continue
        parecido = str(r.get('parecido', 'NINGUNO')).strip()
        conf = str(r.get('confianza', '')).lower()
        marcas = str(r.get('marcas_terceros', 'NINGUNA')).strip()
        posado = str(r.get('retrato_posado', 'NO')).upper().startswith('SI')
        ilegible = str(r.get('texto_ilegible', 'NO')).upper().startswith('SI')
        nada = {'ninguno', 'ninguna', 'no', 'n/a', ''}
        # Una imagen puede disparar varias banderas: se clasifica por la más
        # grave, pero se enseñan TODAS o el informe engaña (un retrato posado
        # con un logo al fondo no puede desaparecer del recuento de posados).
        banderas = []
        if parecido.lower() not in nada and conf in ('alta', 'media'):
            banderas.append(('CRÍTICO', 'parecido a %s (confianza %s)' % (parecido, conf)))
        if marcas.lower() not in nada:
            banderas.append(('ALTO', 'marca de tercero: %s' % marcas))
        if posado:
            banderas.append(('MEDIO', 'retrato posado a cámara'))
        if ilegible:
            banderas.append(('BAJO', 'texto generado ilegible'))
        if banderas:
            nivel = banderas[0][0]
            cubos[nivel].append((rel, ' · '.join(m for _, m in banderas)))
            for n, _ in banderas[1:]:
                conteo[n] = conteo.get(n, 0) + 1

    total = sum(1 for v in datos.values() if v.get('riesgo'))
    print('Analizadas en fase 2: %d imágenes\n' % total)
    for nivel in ('CRÍTICO', 'ALTO', 'MEDIO', 'BAJO'):
        items = cubos[nivel]
        extra = conteo.get(nivel, 0)
        print('%s — %d%s' % (nivel, len(items),
                             ' (+%d como bandera secundaria)' % extra if extra else ''))
        for rel, motivo in items:
            posts = uso.get(rel, ['(sin post: revisar)'])
            print('   %-58s %s' % (rel, motivo))
            print('   %-58s ↳ %s' % ('', ', '.join(posts[:3]) + ('…' if len(posts) > 3 else '')))
        print()
    if sin_parsear:
        print('Sin parsear (respuesta no-JSON): %d — %s' % (len(sin_parsear), sin_parsear[:5]))
    limpias = total - sum(len(v) for v in cubos.values())
    print('Sin hallazgos: %d' % limpias)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fase', type=int, choices=(1, 2))
    ap.add_argument('--informe', action='store_true', help='lee el JSON y ordena por gravedad')
    ap.add_argument('--limite', type=int, default=0)
    args = ap.parse_args()
    if args.informe:
        informe(json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {})
        return
    if not args.fase:
        sys.exit('indica --fase 1|2 o --informe')
    api_key = key()
    datos = json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}

    if args.fase == 1:
        # Los ERROR se reintentan: una imagen sin escanear no es una imagen limpia.
        objetivo = [r for r in referenciadas()
                    if r not in datos or datos[r].get('cara', '').startswith('ERROR')]
        if args.limite:
            objetivo = objetivo[:args.limite]
        print('fase 1 — %d imágenes por escanear' % len(objetivo), flush=True)
        for i, rel in enumerate(objetivo, 1):
            p = ASSETS / rel
            if not p.exists():
                continue
            datos[rel] = {'cara': preguntar(p, P1, api_key)}
            if i % 25 == 0:
                OUT.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding='utf-8')
                con = sum(1 for v in datos.values() if v.get('cara', '').upper().startswith('SI'))
                print('  %d/%d · con cara: %d' % (i, len(objetivo), con), flush=True)
            time.sleep(0.2)
        OUT.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding='utf-8')
        con = [k for k, v in datos.items() if v.get('cara', '').upper().startswith('SI')]
        print('\nFASE 1 COMPLETA: %d escaneadas, %d con cara visible' % (len(datos), len(con)))

    else:
        pend = [k for k, v in datos.items()
                if v.get('cara', '').upper().startswith('SI') and 'riesgo' not in v]
        print('fase 2 — %d imágenes con cara por analizar' % len(pend), flush=True)
        for i, rel in enumerate(pend, 1):
            datos[rel]['riesgo'] = preguntar(ASSETS / rel, P2, api_key)
            if i % 10 == 0:
                OUT.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding='utf-8')
                print('  %d/%d' % (i, len(pend)), flush=True)
            time.sleep(0.2)
        OUT.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding='utf-8')
        print('\nFASE 2 COMPLETA. Revisa %s' % OUT.name)


if __name__ == '__main__':
    main()
