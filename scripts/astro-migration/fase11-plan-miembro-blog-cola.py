#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 11 (blog, cola larga) — Reescribe con bridge.py la PROSA del blog que
sigue prometiendo el plan gratis de AI Chef Pro (FAQs de frontmatter, párrafos
«empieza sin pagar un euro…», tablas de planes) tras el barrido mecánico de
fase11-plan-miembro-blog.py. Frase a frase: extrae la oración completa
alrededor de cada mención, la reescribe con los datos nuevos y la reemplaza
EXACTA. Resumable por post en .work/fase11-blog-cola/.

    python3 fase11-plan-miembro-blog-cola.py --lang es            # todo lo pendiente
    python3 fase11-plan-miembro-blog-cola.py --lang es --post X.md
    python3 fase11-plan-miembro-blog-cola.py --lang es --workers 3

Datos nuevos: plan Miembro 10 €/mes con 10.000 créditos, sin permanencia; los
Premium siguen igual (25/50/95 €, 950 €/año). No existe «sin tarjeta» ni
«para siempre». Las menciones gratis de Miselup/Timlup/otras marcas NO se tocan.
Al acabar cada post, sube su modDate; después toca purgar .astro, regen-lastmod
y build (gotcha del caché de frontmatter).
"""
import argparse, datetime, json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site/src/content/blog'
WORK = REPO / '.work/fase11-blog-cola'
BRIDGE_PY = '/root/chefbusiness-ai/.venv/bin/python'
BRIDGE = '/root/chefbusiness-ai/bridge.py'
HOY = datetime.date.today().isoformat()

CERCA = 200
MARCA = re.compile(r'AI Chef|aichef\.pro|plan|crédit|credit', re.I)
PALABRA = {'es': re.compile(r'(?:\s|^|>|«|\[|")(?:gratis|gratuit[oa]s?)\b'
                            r'|sin (?:necesidad de )?tarjeta|[Nn]o necesitas tarjeta'
                            r'|sin introducir (?:ningún dato|tarjeta)', re.I),
           'en': re.compile(r'(?:\s|^|>|\[|")free\b'
                            r'|[Nn]o credit card|without (?:a )?card', re.I)}
HERMANOS = re.compile(r'miselup|timlup|gastroseo|gastrolocal|hosply|ingredientsindex|chefbusiness', re.I)
WHITELIST_EN = [r'gluten-free', r'dairy-free', r'sugar-free', r'alcohol-free', r'lactose-free',
                r'allergen-free', r'nut-free', r'free-range', r'risk-free', r'free up', r'frees up',
                r'free items', r'free dessert', r'free delivery', r'free shipping', r'hands-free',
                r'free-form', r'contact-free', r'error-free', r'stress-free', r'waste-free',
                r'free tools?', r'free calculator', r'free version', r'freemium', r'free trial of Chat', r'free pour', r'free-pour', r'free meals']

SYSTEM = {
 'es': """Eres editor del blog de AI Chef Pro (SaaS de hostelería). CAMBIO DE NEGOCIO: el plan
gratuito YA NO EXISTE. El plan de entrada es «AI Chef Miembro»: 10 € al mes con 10.000
créditos, sin permanencia (se cancela o cambia de plan cuando se quiera). Los Premium no
cambian (Pro 25 €/85.000 · Plus 50 €/175.000 · Max 95 €/ilimitados · Anual 950 €). Ya no
existe «sin tarjeta»: todos los planes se pagan con tarjeta desde el alta.
Recibes un JSON {id: fragmento} con fragmentos EXACTOS de posts (HTML, markdown o
frontmatter YAML). Reescribe cada uno eliminando la promesa de gratis y reflejando el plan
nuevo, con el MÍNIMO cambio: conserva etiquetas HTML, enlaces, atributos, comillas del
YAML, longitud similar y el estilo del original. Si el fragmento habla del plan gratis de
OTRO producto (Miselup, Timlup…) o de otra cosa, devuélvelo IDÉNTICO. Devuelve SOLO el
JSON con los mismos ids.""",
 'en': """You are the editor of the AI Chef Pro blog (hospitality SaaS). BUSINESS CHANGE: the free
plan NO LONGER EXISTS. The entry plan is "AI Chef Member": €10/month with 10,000 credits,
no commitment (cancel or switch anytime). Premium plans unchanged (Pro €25/85,000 · Plus
€50/175,000 · Max €95/unlimited · Annual €950). "No credit card" claims are gone: every
plan is paid by card from signup.
You receive a JSON {id: fragment} with EXACT fragments from posts (HTML, markdown or YAML
frontmatter). Rewrite each one removing the free promise and reflecting the new plan, with
MINIMAL edits: keep HTML tags, links, attributes, YAML quoting, similar length and the
original tone. If a fragment is about a DIFFERENT product's free offer (Miselup, Timlup…)
or something unrelated (free tools, gluten-free…), return it UNCHANGED. Return ONLY the
JSON with the same ids."""}


def frases_flageadas(t, lang):
    """Fragmentos únicos (expandidos a frontera de oración/línea) con la promesa."""
    frags = []
    for m in PALABRA[lang].finditer(t):
        ctx = t[max(0, m.start() - CERCA):m.end() + CERCA]
        if not MARCA.search(ctx):
            continue
        if HERMANOS.search(ctx):
            continue
        if lang == 'en' and any(re.search(w, ctx, re.I) for w in WHITELIST_EN):
            continue
        # frontera de oración: el punto ENTRE DÍGITOS (3.000, 10.000) no corta —
        # cortar ahí dejó «…10 € al mes.000 créditos…» en el piloto.
        def es_punto_numerico(i):
            return (t[i] == '.' and 0 < i < len(t) - 1
                    and t[i - 1].isdigit() and t[i + 1].isdigit())
        ini = m.start()
        while ini > 0 and (t[ini - 1] not in '.!?\n>' or es_punto_numerico(ini - 1)):
            ini -= 1
        fin = m.end()
        while fin < len(t) and (t[fin] not in '.!?\n<' or es_punto_numerico(fin)):
            fin += 1
        if fin < len(t) and t[fin] in '.!?':
            fin += 1
        frag = t[ini:fin].strip()
        if 8 < len(frag) < 900 and frag not in frags:
            frags.append(frag)
    return frags


def procesa(f, lang, aplicar=True, intento=1):
    hecho = WORK / f'{f.name}.done'
    if hecho.exists():
        return f.name, 'ya hecho', 0
    t = f.read_text(encoding='utf-8')
    frags = frases_flageadas(t, lang)
    if not frags:
        hecho.write_text('sin fragmentos')
        return f.name, 'limpio', 0
    payload = {str(i): s for i, s in enumerate(frags)}
    out = WORK / f'{f.name}.out.json'
    r = subprocess.run([BRIDGE_PY, BRIDGE, '--task', 'content', '--strict-lang',
                        '--temperature', '0.3' if intento == 1 else '0.2',
                        '--max-tokens', '24000', '--system', SYSTEM[lang],
                        '--prompt', json.dumps(payload, ensure_ascii=False),
                        '--output', str(out)], capture_output=True, text=True, timeout=1200)
    if r.returncode != 0:
        raise RuntimeError(f'bridge {r.returncode}: {r.stderr[-200:]}')
    raw = out.read_text()
    fin_i = raw.rfind('}')
    prof = 0
    for i in range(fin_i, -1, -1):
        prof += raw[i] == '}'
        prof -= raw[i] == '{'
        if prof == 0:
            nuevo = json.loads(raw[i:fin_i + 1])
            break
    if set(nuevo) != set(payload):
        raise RuntimeError('keys distintos')
    cambiados = 0
    for k, viejo in payload.items():
        rep = nuevo[k]
        if rep == viejo:
            continue
        if PALABRA[lang].search(f' {rep} ') and MARCA.search(rep) and not HERMANOS.search(rep):
            # negar el gratis es copy legítimo («ya no hay plan gratuito…»)
            niega = re.search(r'ya no (?:hay|existe|es)|dejó de ser|no hay plan gratuito'
                              r'|no longer (?:free|offers a free)|no free plan|is no longer',
                              rep, re.I)
            if not niega and (lang != 'en' or not any(re.search(w, rep, re.I) for w in WHITELIST_EN)):
                raise RuntimeError(f'frag {k} sigue con gratis: {rep[:80]}')
        idx = t.find(viejo)
        if idx < 0:
            continue
        # guarda anti-corte: si justo después del fragmento hay un dígito, el
        # fragmento se cortó en mitad de un número — no reemplazar, reportar.
        despues = t[idx + len(viejo):idx + len(viejo) + 1]
        if despues.isdigit():
            raise RuntimeError(f'frag {k} corta un número: …{viejo[-40:]}|{despues}')
        t = t.replace(viejo, rep)
        cambiados += 1
    if cambiados and aplicar:
        t = re.sub(r'^modDate: \d{4}-\d{2}-\d{2}$', f'modDate: {HOY}', t, count=1, flags=re.M)
        f.write_text(t, encoding='utf-8')
    restantes = frases_flageadas(t, lang)
    if restantes and intento == 1:
        return procesa(f, lang, aplicar, intento=2)
    if restantes:
        return f.name, f'QUEDAN {len(restantes)}: {restantes[0][:70]}', cambiados
    hecho.write_text(f'{cambiados} fragmentos')
    return f.name, 'OK', cambiados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', required=True, choices=['es', 'en'])
    ap.add_argument('--post', action='append')
    ap.add_argument('--workers', type=int, default=3)
    args = ap.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    ficheros = [BLOG / args.lang / p for p in args.post] if args.post else \
        sorted((BLOG / args.lang).glob('*.md'))
    pendientes = [f for f in ficheros if not (WORK / f'{f.name}.done').exists()]
    print(f'{len(pendientes)} posts pendientes de {len(ficheros)}')
    resumen = {'OK': 0, 'limpio': 0, 'quedan': 0, 'error': 0}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(procesa, f, args.lang): f for f in pendientes}
        for fut in as_completed(futs):
            try:
                nombre, estado, n = fut.result()
            except Exception as e:                              # noqa: BLE001
                nombre, estado, n = futs[fut].name, f'ERROR {e}', 0
            clave = estado.split(' ')[0].split(':')[0]
            resumen['OK' if clave == 'OK' else 'limpio' if clave in ('limpio', 'ya') else
                    'quedan' if clave == 'QUEDAN' else 'error'] += 1
            marca = '✓' if clave in ('OK', 'limpio', 'ya') else '✗'
            print(f'{marca} {nombre}: {estado[:110]} ({n} frags)')
    print(f'\nresumen: {resumen}')


if __name__ == '__main__':
    main()
