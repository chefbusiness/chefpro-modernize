#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 11 (spokes) — Quita el plan gratis de use-cases-content.*.ts: reemplazos
por PLANTILLA EXACTA por idioma (nunca word-strip: «gluten-free», «risk-free» y
compañía son legítimos), sufijo de las seo.description, y verificador
fail-closed que lista todo lo que quede sin clasificar.

    python3 fase11-plan-miembro-spokes.py            # dry-run + informe
    python3 fase11-plan-miembro-spokes.py --aplicar

El copy nuevo sale de .work/fase11-copy-<lang>[.limpio].json (mismo juego de
claves que el barrido de locales). El fr.ts NO se toca aquí: sus .ok.json de
.work/fase10-fr se corrigen ANTES de emitir (véase fase10-traducir-spokes.py).
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / 'src/data'
COPY = REPO / '.work'

# Palabra gratis por idioma (con espacio-o-inicio delante: no caza «gluten-free»).
PALABRAS = {
    'es': r'gratis|gratuit[oa]s?', 'en': r'free', 'fr': r'gratuit\w*',
    'de': r'kostenlos\w*', 'it': r'gratis|gratuit\w*', 'pt': r'grátis|gratuit\w*|de graça',
    'nl': r'gratis',
}
# Contextos ingleses legítimos que el verificador ignora.
WHITELIST = [r'risk-free', r'free-form', r'free up', r'frees up', r'gluten-free',
             r'dairy-free', r'lactose-free', r'nut-free', r'allergen-free',
             r'alcohol-free', r'sugar-free', r'hands-free', r'free-range']


def copy_de(lang):
    f = COPY / f'fase11-copy-{lang}.limpio.json'
    if not f.exists():
        f = COPY / f'fase11-copy-{lang}.json'
    d = json.loads(f.read_text())
    d.pop('_doc', None)
    return d


def plantillas(lang, c):
    """[(exacta_o_regex, reemplazo)] — el orden importa (largas primero).
    Los patrones con apóstrofe usan APO para casar tanto l'onboarding (ficheros
    con comillas dobles, it.ts) como l\\'onboarding (los de comilla simple)."""
    APO = r"(?:\\)?'"
    if lang == 'es':
        return [
            ('Empieza gratis con el onboarding de 2 minutos. 3.000 créditos al mes para probar todos los agentes. Sin tarjeta.', c['cta_a']),
            ('Empieza gratis con el onboarding de 2 minutos. 3.000 créditos al mes. Sin tarjeta.', c['cta_b']),
            ('Habla con nosotros para un onboarding personalizado a tu grupo o empieza gratis con 3.000 créditos al mes.', c['cta_grupo']),
            ('Habla con nosotros para un onboarding personalizado o empieza gratis con 3.000 créditos al mes.', c['cta_solo']),
            ('Puedes empezar gratis con 3.000 créditos al mes para tus propias listas y propuestas.', c['souschef_frag']),
            ('Empieza gratis.', c['seo_sufijo']),
            ('Prueba gratis.', c['seo_sufijo']),
        ]
    if lang == 'en':
        return [
            (re.compile(r'Start free with (?:the|a) 2-minute onboarding\. 3,000 credits per month to (?:try|test) every agent\. No (?:credit )?card(?: required)?\.'), c['cta_a']),
            (re.compile(r'Start free with (?:the|a) 2-minute onboarding\. (?:3,000 credits|5 monthly uses)[^.]*\. No (?:credit )?card(?: required)?\.'), c['cta_b']),
            (re.compile(r'Book a tailored onboarding for your group,? or start free with 3,000 credits per month\.'), c['cta_grupo']),
            (re.compile(r'(?:Book a tailored onboarding|Talk to us for a personalized onboarding),? or start free with 3,000 credits per month\.'), c['cta_solo']),
            (re.compile(r'You can start free with 3,000 credits per month for your own (?:lists|checklists) and proposals\.'), c['souschef_frag']),
            ('Start free.', c['seo_sufijo']),
        ]
    if lang == 'it':
        return [
            (re.compile(r"Inizia gratis con l" + APO + r"onboarding di 2 minuti\. 3\.000 crediti al mese per provare tutti gli agenti\. Senza carta( di credito)?\."), c['cta_a']),
            (re.compile(r"Inizia gratis con l" + APO + r"onboarding di 2 minuti\. 3\.000 crediti al mese\. Senza carta( di credito)?\."), c['cta_b']),
            (re.compile(r'Parla con noi per un onboarding personalizzato (?:(?:per il|al) tuo gruppo )?o inizia gratis con 3\.000 crediti al mese\.'),
             c['cta_grupo']),
            (re.compile(r'Puoi iniziare gratis con 3\.000 crediti al mese[^.]*\.'), c['souschef_frag']),
            ('Inizia gratis.', c['seo_sufijo']),
            ('Prova gratis.', c['seo_sufijo']),
        ]
    if lang == 'fr':
        return [
            (re.compile(r"Commencez gratuitement avec l" + APO + r"onboarding de 2 minutes\. 3 000 crédits par mois pour tester tous les agents\.( Sans carte( bancaire| de crédit)?\.)?"), c['cta_a']),
            ('Essai gratuit.', c['seo_sufijo']),
        ]
    if lang == 'de':
        return [
            ('Starten Sie kostenlos mit dem 2-Minuten-Onboarding. 3.000 Credits pro Monat, um alle Agenten zu testen. Ohne Kreditkarte.', c['cta_a']),
            ('Kostenlos starten.', c['seo_sufijo']),
        ]
    if lang == 'pt':
        return [
            ('Comece grátis com o onboarding de 2 minutos. 3.000 créditos por mês para experimentar todos os agentes. Sem cartão.', c['cta_a']),
            ('Comece grátis.', c['seo_sufijo']),
        ]
    if lang == 'nl':
        return [
            ('Begin gratis met de onboarding van 2 minuten. 3.000 credits per maand om alle agents te proberen. Zonder kaart.', c['cta_a']),
            ('Gratis starten.', c['seo_sufijo']),
        ]
    return []


def procesa(fichero, lang, aplicar):
    t = fichero.read_text(encoding='utf-8')
    original = t
    c = copy_de(lang)
    # Los ficheros emitidos con comilla simple escapan el apóstrofe (l\'onboarding):
    # el reemplazo debe escaparse igual o rompe el TS. it.ts y fr.ts van con dobles.
    estilo_simple = "ctaSubtitle: '" in t
    cambios = []
    for patron, nuevo in plantillas(lang, c):
        if estilo_simple:
            nuevo = nuevo.replace("'", "\\'")
        if isinstance(patron, str):
            n = t.count(patron)
            if n:
                t = t.replace(patron, nuevo)
                cambios.append(f'×{n} {patron[:60]!r}')
        else:
            # lambda: el reemplazo es LITERAL (re.sub interpretaría \' como escape)
            t, n = patron.subn(lambda m, _n=nuevo: _n, t)
            if n:
                cambios.append(f'×{n} regex {patron.pattern[:60]!r}')
    # verificador
    pal = re.compile(r'(?:\s|^|«|")(' + PALABRAS[lang] + r')(?=\s|[.,;:!»"]|$)', re.I)
    restos = []
    for m in pal.finditer(t):
        ctx = t[max(0, m.start() - 70):m.end() + 70].replace('\n', ' ')
        if any(re.search(w, ctx, re.I) for w in WHITELIST):
            continue
        restos.append(ctx)
    if aplicar and t != original:
        fichero.write_text(t, encoding='utf-8')
    return cambios, restos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()
    objetivos = [
        (DATA / 'use-cases-content.es.ts', 'es'),
        (DATA / 'use-cases-content.en.ts', 'en'),
        (DATA / 'use-cases-content.it.ts', 'it'),
        (DATA / 'use-cases-content.es.consultor.ts', 'es'),
        (DATA / 'use-cases-content.en.consultor.ts', 'en'),
        (DATA / 'use-cases-content.fr.consultor.ts', 'fr'),
        (DATA / 'use-cases-content.de.consultor.ts', 'de'),
        (DATA / 'use-cases-content.it.consultor.ts', 'it'),
        (DATA / 'use-cases-content.pt.consultor.ts', 'pt'),
        (DATA / 'use-cases-content.nl.consultor.ts', 'nl'),
    ]
    fr_ts = DATA / 'use-cases-content.fr.ts'
    if fr_ts.exists():
        objetivos.insert(3, (fr_ts, 'fr'))
    fallos = 0
    for f, lang in objetivos:
        cambios, restos = procesa(f, lang, args.aplicar)
        print(f'—— {f.name} [{lang}]: {len(cambios)} plantillas aplicadas')
        for cmb in cambios:
            print(f'   {cmb}')
        if restos:
            fallos += len(restos)
            print(f'   ⛔ {len(restos)} SIN clasificar:')
            for r in restos[:10]:
                print(f'      …{r}…')
    if fallos:
        print(f'\n⛔ {fallos} restos — añadir plantillas o whitelist antes de aplicar')
        sys.exit(1)
    print('\n✅ limpio' + ('' if args.aplicar else ' (dry-run)'))


if __name__ == '__main__':
    main()
