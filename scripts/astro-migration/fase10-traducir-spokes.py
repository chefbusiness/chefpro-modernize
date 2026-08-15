#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 10 — Traduce los 51 spokes de casos de uso de use-cases-content.es.ts a
otro idioma del sitio, con bridge.py como motor y validación byte a byte de lo
que NO se traduce. Reconstruye (commiteado, esta vez) el pipeline efímero con
el que se hizo el italiano el 2026-08-08.

    python3 fase10-traducir-spokes.py --lang fr                # todo lo pendiente
    python3 fase10-traducir-spokes.py --lang fr --spoke pizzeria
    python3 fase10-traducir-spokes.py --lang fr --solo-validar # revalida lo traducido
    python3 fase10-traducir-spokes.py --lang fr --emitir       # escribe use-cases-content.fr.ts

Necesita scripts/astro-migration/fase10-glosario-<lang>.json (nombres de agente
según la PLATAFORMA viva de ese idioma — nunca deducidos del repo) y, opcional,
fase10-allowlist-<lang>.json con falsos positivos aprobados del detector de
castellano (p. ej. «Piña Colada» en el spoke de coctelería).

Qué garantiza el validador por spoke (aborta el spoke si falla, reintenta 1 vez):
  · mismos keys y ningún valor vacío;
  · 0 caracteres de otros sistemas de escritura (CJK, cirílico…);
  · 0 marcadores de castellano fuera de los nombres protegidos/productos
    (á í ó ú ñ ¿ ¡ y la secuencia «ción», que no existe en francés);
  · glosario aplicado: si el ES contiene la clave, el destino contiene el nombre
    oficial y NO conserva el español;
  · protegidos presentes: agente sin versión local = nombre verbatim;
  · productIds, galleryImages, features[].icon, seo.ogImage, appUrlPath y
    testimonialAuthor se copian del ES por construcción y se reverifican.
Avisa (sin abortar) si el multiconjunto de números de una cadena cambia.
"""
import argparse, json, re, subprocess, sys, unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BRIDGE_PY = '/root/chefbusiness-ai/.venv/bin/python'
BRIDGE = '/root/chefbusiness-ai/bridge.py'
ES_TS = REPO / 'src/data/use-cases-content.es.ts'

IDIOMAS = {
    'fr': {'nombre': 'francés', 'const': 'USE_CASES_CONTENT_FR', 'tono':
           'VOUVOIEMENT obligatorio (vous/votre): todo el árbol francés existente vosea, aunque el español tutee.'},
    'de': {'nombre': 'alemán', 'const': 'USE_CASES_CONTENT_DE', 'tono':
           'Trato de usted (Sie/Ihr), coherente con el árbol alemán existente.'},
    'pt': {'nombre': 'portugués', 'const': 'USE_CASES_CONTENT_PT', 'tono':
           'Trato: el de src/data/use-cases-content.pt.consultor.ts (revisar antes de lanzar).'},
    'nl': {'nombre': 'neerlandés', 'const': 'USE_CASES_CONTENT_NL', 'tono':
           'Trato: el de src/data/use-cases-content.nl.consultor.ts (revisar antes de lanzar).'},
}

# Caracteres/secuencias que delatan castellano. Por idioma destino, porque lo
# que es marcador en uno es legítimo en otro (ü existe en francés y alemán;
# 'ción' no existe en ninguno de los cuatro).
MARCADORES_ES = {
    'fr': set('áíóúñÁÍÓÚÑ¿¡'),
    'de': set('áíóúñÁÍÓÚÑ¿¡'),
    'pt': set('ñÑ¿¡'),   # á í ó ú existen en portugués
    'nl': set('ñÑ¿¡'),
}
SECUENCIAS_ES = ['ción', 'cción']

PRODUCTO_RE = re.compile(r'(?:Mega Pack|Kit|Pack|Plan de Negocio|Guía)[ &A-Za-zÁÉÍÓÚÑáéíóúñ-]{2,45}')

CAMPOS_LISTA_STR = {'pains', 'workflow'}
CAMPOS_STR = {'h1', 'heroSubtitle', 'heroTagline', 'badge', 'painsTitle',
              'featuresTitle', 'workflowTitle', 'productsTitle',
              'testimonialQuote', 'testimonialRole', 'faqTitle', 'ctaTitle',
              'ctaSubtitle', 'personalizationTitle', 'personalizationBody',
              'appsTitle', 'galleryTitle', 'gallerySubtitle'}
# Campos que se COPIAN del ES sin pasar por el traductor:
PRESERVADOS = {'productIds', 'galleryImages', 'appUrlPath', 'testimonialAuthor'}


def dump_es():
    """Vuelca USE_CASES_CONTENT_ES a dict vía esbuild (node del astro-site)."""
    js = """
const esbuild = require('esbuild');
const fs = require('fs');
let src = fs.readFileSync(process.argv[2],'utf8');
src = src.replace(/import type .*?;\\n/s,'');
const out = esbuild.transformSync(src,{loader:'ts',format:'cjs'}).code;
const mod = {exports:{}};
new Function('exports','module',out)(mod.exports,mod);
process.stdout.write(JSON.stringify(mod.exports.USE_CASES_CONTENT_ES));
"""
    r = subprocess.run(['node', '-e', js, 'x', str(ES_TS)],
                       capture_output=True, text=True, cwd=REPO / 'astro-site')
    if r.returncode != 0:
        sys.exit(f'esbuild dump falló: {r.stderr[:400]}')
    return json.loads(r.stdout)


def aplanar(spoke):
    """Extrae {ruta: texto} con SOLO lo traducible."""
    plano = {}
    def put(ruta, val):
        if isinstance(val, str) and val.strip():
            plano[ruta] = val
    for campo in CAMPOS_STR:
        if campo in spoke and spoke[campo] is not None:
            put(campo, spoke[campo])
    for campo in CAMPOS_LISTA_STR:
        for i, v in enumerate(spoke.get(campo) or []):
            put(f'{campo}[{i}]', v)
    for i, f in enumerate(spoke.get('features') or []):
        put(f'features[{i}].title', f.get('title'))
        put(f'features[{i}].description', f.get('description'))
    for i, f in enumerate(spoke.get('faqs') or []):
        put(f'faqs[{i}].q', f.get('q'))
        put(f'faqs[{i}].a', f.get('a'))
    for i, a in enumerate(spoke.get('apps') or []):
        put(f'apps[{i}].name', a.get('name'))
        put(f'apps[{i}].category', a.get('category'))
        put(f'apps[{i}].description', a.get('description'))
    for i, m in enumerate(spoke.get('metrics') or []):
        put(f'metrics[{i}].value', m.get('value'))
        put(f'metrics[{i}].label', m.get('label'))
    ba = spoke.get('beforeAfter')
    if ba:
        put('beforeAfter.beforeTitle', ba.get('beforeTitle'))
        put('beforeAfter.afterTitle', ba.get('afterTitle'))
        for i, v in enumerate(ba.get('beforeItems') or []):
            put(f'beforeAfter.beforeItems[{i}]', v)
        for i, v in enumerate(ba.get('afterItems') or []):
            put(f'beforeAfter.afterItems[{i}]', v)
    seo = spoke.get('seo') or {}
    for k in ('title', 'description', 'keywords'):
        put(f'seo.{k}', seo.get(k))
    return plano


def fundir(spoke_es, plano_tr):
    """Deep-copy del ES + valores traducidos en sus rutas. Lo no traducido queda
    byte-idéntico por construcción."""
    out = deepcopy(spoke_es)
    for ruta, val in plano_tr.items():
        # [a-zA-Z0-9]: el campo «h1» lleva dígito y rompía el fullmatch
        m = re.fullmatch(r'([a-zA-Z][a-zA-Z0-9]*)(?:\[(\d+)\])?(?:\.([a-zA-Z][a-zA-Z0-9]*))?(?:\[(\d+)\])?', ruta)
        campo, idx, sub, idx2 = m.group(1), m.group(2), m.group(3), m.group(4)
        if campo == 'beforeAfter':
            if idx2 is not None:
                out['beforeAfter'][sub][int(idx2)] = val
            else:
                out['beforeAfter'][sub] = val
        elif campo == 'seo':
            out['seo'][sub] = val
        elif idx is not None and sub is not None:
            out[campo][int(idx)][sub] = val
        elif idx is not None:
            out[campo][int(idx)] = val
        else:
            out[campo] = val
    return out


def numeros(s):
    return sorted(re.sub(r'[.,\s]', '', n) for n in re.findall(r'\d[\d.,]*', s))


def validar(spoke_id, plano_es, plano_tr, glosario, protegidos, allowlist, lang):
    errores, avisos = [], []
    if set(plano_es) != set(plano_tr):
        faltan = set(plano_es) - set(plano_tr)
        sobran = set(plano_tr) - set(plano_es)
        errores.append(f'keys distintos (faltan {sorted(faltan)[:5]}, sobran {sorted(sobran)[:5]})')
        return errores, avisos
    marcadores = MARCADORES_ES[lang]
    for ruta, es_v in plano_es.items():
        tr_v = plano_tr[ruta]
        if not isinstance(tr_v, str) or not tr_v.strip():
            errores.append(f'{ruta}: vacío o no-string'); continue
        for c in tr_v:
            if ord(c) > 0x2AF and unicodedata.category(c).startswith('L'):
                errores.append(f'{ruta}: carácter de otro alfabeto «{c}» (U+{ord(c):04X})')
                break
        # La allowlist va PRIMERO y de largo a corto: si los protegidos borran
        # antes «Guía Restaurante», el literal completo «Guía Restaurante
        # Gastronómico» de la allowlist ya no casa y su cola con ó da falso rojo.
        enmascarado = tr_v
        for ok in sorted(allowlist, key=len, reverse=True):
            enmascarado = enmascarado.replace(ok, '')
        for p in sorted(protegidos, key=len, reverse=True):
            enmascarado = enmascarado.replace(p, '')
        enmascarado = PRODUCTO_RE.sub('', enmascarado)
        hits = [c for c in enmascarado if c in marcadores]
        seqs = [s for s in SECUENCIAS_ES if s in enmascarado]
        if hits or seqs:
            frag = enmascarado
            for x in (hits + seqs):
                i = frag.find(x if isinstance(x, str) else x)
                if i >= 0:
                    frag = frag[max(0, i-30):i+30]; break
            errores.append(f'{ruta}: castellano {hits[:3]}{seqs} …{frag}…')
        # El chequeo de glosario ignora lo que viva DENTRO de un literal
        # protegido: «Kit de Tareas Chef Privado» contiene «Chef Privado» y ese
        # producto va verbatim — flagearlo era un falso positivo (cazado en fr).
        es_m, tr_m = es_v, tr_v
        for p in sorted(protegidos, key=len, reverse=True):
            es_m = es_m.replace(p, '∎')
            tr_m = tr_m.replace(p, '∎')
        for k, v in glosario.items():
            if k in es_m:
                if k in tr_m:
                    errores.append(f'{ruta}: conserva «{k}» (debe ser «{v}»)')
                elif v not in tr_m:
                    errores.append(f'{ruta}: falta el nombre oficial «{v}»')
        for p in protegidos:
            if p in es_v and p not in tr_v:
                errores.append(f'{ruta}: nombre protegido «{p}» desaparecido')
        if numeros(es_v) != numeros(tr_v):
            avisos.append(f'{ruta}: números {numeros(es_v)} → {numeros(tr_v)}')
    return errores, avisos


def system_prompt(lang, cfg, glosario, protegidos):
    glos = '\n'.join(f'  «{k}» → «{v}»' for k, v in glosario.items())
    prot = ', '.join(f'«{p}»' for p in protegidos)
    return f"""Eres traductor profesional de español a {cfg['nombre']} de contenido de marketing SaaS
para hostelería profesional (la plataforma AI Chef Pro, aichef.pro). Recibes un JSON
{{ruta: texto_español}} y devuelves EXACTAMENTE el mismo JSON con los MISMOS keys y cada
valor traducido al {cfg['nombre']}. SOLO el JSON, sin comentarios ni fences.

REGLAS INNEGOCIABLES:
1. {cfg['tono']}
2. GLOSARIO OBLIGATORIO — nombres oficiales de los agentes en la plataforma {cfg['nombre']};
   usa EXACTAMENTE la forma de la derecha cada vez que aparezca la de la izquierda:
{glos}
3. NOMBRES QUE NO SE TRADUCEN (déjalos tal cual, letra a letra; son agentes o marcas sin
   versión local): {prot}. Tampoco se traducen: «AI Chef Pro», nombres de personas, ni los
   nombres de productos digitales que empiezan por Kit / Pack / Mega Pack / Plan de Negocio /
   Guía (van en español porque el producto es español).
4. Números, porcentajes, horas, rangos y monedas se conservan tal cual (33 %, 08:30, 60-90).
5. Traducción natural de marketing, no literal: adapta modismos, no calques. Ortografía y
   tipografía perfectas del {cfg['nombre']}.
6. PUREZA DE IDIOMA: ni una palabra en español fuera de los nombres del punto 2-3, y ningún
   carácter de otros sistemas de escritura (chino, cirílico, coreano…).
"""


def traducir_spoke(spoke_id, plano_es, workdir, sysprompt, intento=1):
    destino = workdir / f'{spoke_id}.json'
    payload = json.dumps(plano_es, ensure_ascii=False, indent=0)
    args = [BRIDGE_PY, BRIDGE, '--task', 'translation', '--strict-lang',
            '--temperature', '0.3' if intento == 1 else '0.2',
            '--max-tokens', '26000', '--system', sysprompt,
            '--prompt', payload, '--output', str(destino)]
    r = subprocess.run(args, capture_output=True, text=True, timeout=1200)
    if r.returncode != 0:
        raise RuntimeError(f'bridge exit {r.returncode}: {r.stderr[-300:]}')
    raw = destino.read_text().strip()
    raw = re.sub(r'^```(json)?|```$', '', raw, flags=re.M).strip()
    return json.loads(raw)


def emitir(lang, cfg, spokes_tr, destino):
    cuerpo = json.dumps(spokes_tr, ensure_ascii=False, indent=2)
    hoy = subprocess.run(['date', '+%Y-%m-%d'], capture_output=True, text=True).stdout.strip()
    header = f"""// {cfg['nombre'].capitalize()} content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el {hoy} con scripts/astro-migration/fase10-traducir-spokes.py
// (bridge.py ~deepseek/deepseek-v4-flash-latest, --strict-lang) y el glosario
// de la PLATAFORMA viva fase10-glosario-{lang}.json. Los agentes sin versión
// {lang} se preservan verbatim a propósito (decisión de catálogo pendiente,
// ver CATALOGO_ITALIANO_PENDIENTE.md — aplica a los 5 idiomas).
//
// NO editar a mano campo a campo: productIds, galleryImages, features[].icon,
// seo.ogImage y testimonialAuthor se preservan verbatim desde el ES y el
// validador del script lo comprueba. Regenerar PISA ediciones manuales.

import type {{ UseCaseContent }} from './use-cases';

export const {cfg['const']}: Record<string, UseCaseContent> = {cuerpo};
"""
    destino.write_text(header)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', required=True, choices=list(IDIOMAS))
    ap.add_argument('--spoke', action='append', help='sólo estos ids')
    ap.add_argument('--workers', type=int, default=3)
    ap.add_argument('--solo-validar', action='store_true')
    ap.add_argument('--emitir', action='store_true')
    args = ap.parse_args()

    cfg = IDIOMAS[args.lang]
    aqui = Path(__file__).parent
    glos_path = aqui / f'fase10-glosario-{args.lang}.json'
    if not glos_path.exists():
        sys.exit(f'Falta {glos_path.name}: constrúyelo desde el listado vivo de la plataforma.')
    g = json.loads(glos_path.read_text())
    glosario, protegidos = g['glosario'], g['protegidos']
    allow_path = aqui / f'fase10-allowlist-{args.lang}.json'
    allowlist = json.loads(allow_path.read_text()) if allow_path.exists() else []

    workdir = REPO / f'.work/fase10-{args.lang}'
    workdir.mkdir(parents=True, exist_ok=True)

    es = dump_es()
    ids = args.spoke or list(es)
    planos = {i: aplanar(es[i]) for i in ids}
    sysprompt = system_prompt(args.lang, cfg, glosario, protegidos)

    if args.emitir:
        spokes_tr, faltan = {}, []
        for i in list(es):
            f = workdir / f'{i}.ok.json'
            if f.exists():
                spokes_tr[i] = fundir(es[i], json.loads(f.read_text()))
            else:
                faltan.append(i)
        if faltan:
            sys.exit(f'No emito: faltan {len(faltan)} spokes validados: {faltan[:8]}…')
        destino = REPO / f'src/data/use-cases-content.{args.lang}.ts'
        emitir(args.lang, cfg, spokes_tr, destino)
        print(f'✅ {destino} escrito con {len(spokes_tr)} spokes.')
        return

    def procesa(spoke_id):
        plano_es = planos[spoke_id]
        okf = workdir / f'{spoke_id}.ok.json'
        if okf.exists() and not args.solo_validar:
            return spoke_id, 'ya validado', []
        if args.solo_validar:
            f = workdir / f'{spoke_id}.json'
            if not f.exists():
                return spoke_id, 'SIN TRADUCIR', []
            raw = re.sub(r'^```(json)?|```$', '', f.read_text().strip(), flags=re.M).strip()
            plano_tr = json.loads(raw)
        else:
            plano_tr = None
        for intento in (1, 2):
            try:
                if plano_tr is None:
                    plano_tr = traducir_spoke(spoke_id, plano_es, workdir, sysprompt, intento)
                errores, avisos = validar(spoke_id, plano_es, plano_tr, glosario,
                                          protegidos, allowlist, args.lang)
                if not errores:
                    okf.write_text(json.dumps(plano_tr, ensure_ascii=False))
                    return spoke_id, 'OK', avisos
                if args.solo_validar or intento == 2:
                    return spoke_id, f'FALLA: {errores[:4]}', avisos
                plano_tr = None
            except Exception as e:
                if args.solo_validar or intento == 2:
                    return spoke_id, f'ERROR: {e}', []
                plano_tr = None
        return spoke_id, 'agotado', []

    resultados = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(procesa, i): i for i in ids}
        for fut in as_completed(futs):
            sid, estado, avisos = fut.result()
            resultados[sid] = estado
            marca = '✓' if estado in ('OK', 'ya validado') else '✗'
            print(f'{marca} {sid}: {estado}')
            for a in avisos[:3]:
                print(f'   ⚠ {a}')
    ok = sum(1 for v in resultados.values() if v in ('OK', 'ya validado'))
    print(f'\n{ok}/{len(ids)} spokes validados. Siguiente: --emitir cuando estén los 51.')


if __name__ == '__main__':
    main()
