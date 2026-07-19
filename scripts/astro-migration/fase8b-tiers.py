#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Clasificador de tiers de migración (slug → A/B/C/D).

Cruza:
  - La auditoría de clusters 2026-06-15 (~/aichef-blog/.work/audit-2026-06-15/catalogo.json,
    327 posts con cluster C1..C5 / RECETAS_TECNICA / GLOSARIO / SIN_CLASIFICAR)
  - El censo live del export (posts-publish.jsonl, 408 posts) para los posteriores a la auditoría.

Reglas (del análisis FASE8B_ANALISIS_CONTENIDO_BLOG.md):
  A = money clusters C1-C5 + librerías de prompts (cat 15) + verticales "ia-para-X"
  B = glosario (cats 24/21) + técnica profesional
  C = recetas/consumo (RECETAS_TECNICA, tutoriales, recetario) + futurismo + resto
  D = NO migrar: pSEO guias-ia-locales (cat 264) + escuelas US + duplicados conocidos

Salida: scripts/astro-migration/fase8b-tiers.json  {slug: {tier, why, wpId}}
"""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT = Path.home() / 'aichef-blog' / 'export-2026-07-19'
CATALOGO = Path.home() / 'aichef-blog' / '.work' / 'audit-2026-06-15' / 'catalogo.json'
OUT = REPO / 'scripts' / 'astro-migration' / 'fase8b-tiers.json'

# Duplicados exactos detectados en el censo 2026-07-19: se migra el superviviente,
# el otro entra como D con 301 al superviviente.
DUP_LOSERS = {
    'desbloquea-las-funciones-de-ai-chef-pro-para-una-planificacion-de-comidas-sin-esfuerzo-2': 'desbloquea-las-funciones-de-ai-chef-pro-para-una-planificacion-de-comidas-sin-esfuerzo',
    'ia-alimentaria-revolucion-tecnologica-en-la-industria-de-alimentos-2025': 'ia-alimentaria-revolucion-tecnologica-en-la-industria-de-alimentos',
}

CLUSTER_TO_TIER = {
    'C1_Costes_Rentabilidad': 'A', 'C2_IA_Restaurantes': 'A',
    'C3_Operaciones_Cumplimiento': 'A', 'C4_Marketing_Ventas': 'A',
    'C5_Modelos_Negocio': 'A',
    'GLOSARIO': 'B',
    'RECETAS_TECNICA': 'C',
    'SIN_CLASIFICAR': None,  # se decide por reglas de slug/categoría
}

# Verticales comerciales del hallazgo 3 de la auditoría (SIN_CLASIFICAR → A)
VERTICAL_RE = re.compile(
    r'^(ia-para-|como-crear-restaurante|optimizacion-de-delivery|chef-gpt|'
    r'las-\d+-mejores|(\d+)-(herramientas|prompts|hacks|recursos))'
)
ESCUELAS_RE = re.compile(r'^top-10-escuelas-')


def load_jsonl(path):
    with open(str(path), encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    catalogo = {p['slug']: p for p in json.load(open(str(CATALOGO), encoding='utf-8'))}
    posts = load_jsonl(EXPORT / 'posts-publish.jsonl')

    tiers = {}
    for p in posts:
        slug, cats = p['slug'], p.get('categories', [])
        why = None

        if 264 in cats:
            tier, why = 'D', 'pSEO guias-ia-locales (canibaliza pSEO aichef.pro)'
        elif slug in DUP_LOSERS:
            tier, why = 'D', 'duplicado exacto → 301 a ' + DUP_LOSERS[slug]
        elif ESCUELAS_RE.match(slug):
            tier, why = 'D', 'listicle escuelas US fuera de estrategia (decisión análisis §3)'
        elif 15 in cats:
            tier, why = 'A', 'librería de prompts (destino final: página de agente 8C)'
        elif slug in catalogo and CLUSTER_TO_TIER.get(catalogo[slug]['cluster']):
            tier = CLUSTER_TO_TIER[catalogo[slug]['cluster']]
            why = 'auditoría 06-15: ' + catalogo[slug]['cluster']
        elif VERTICAL_RE.match(slug):
            tier, why = 'A', 'vertical/listicle comercial (hallazgo 3 auditoría)'
        elif 24 in cats or 21 in cats:
            tier, why = 'B', 'glosario'
        elif 44 in cats or 1 in cats:
            tier, why = 'C', 'recetario/tutoriales (consumo)'
        else:
            tier, why = 'C', 'resto (ia-en-gastronomia/ai-chef-pro sin cluster ni patrón money)'

        tiers[slug] = {'tier': tier, 'why': why, 'wpId': p['id']}

    counts = {}
    for v in tiers.values():
        counts[v['tier']] = counts.get(v['tier'], 0) + 1
    OUT.write_text(json.dumps(tiers, ensure_ascii=False, indent=1, sort_keys=True),
                   encoding='utf-8')
    print('Total %d posts → %s' % (len(tiers), json.dumps(counts, sort_keys=True)))
    print('Escrito: %s' % OUT)
    print('\nMuestra Tier A:')
    for s, v in sorted(tiers.items()):
        if v['tier'] == 'A':
            print('  A', s)


if __name__ == '__main__':
    main()
