#!/usr/bin/env python3
"""
Rename "apps" / "aplicaciones" -> "agentes IA" / "AI agents" / etc. across:
- 7 i18n locale JSONs (only VALUES, never KEYS).
- og-meta.ts (47 routes x 7 langs, title/description strings).

Run with --apply to write changes; without it, prints diff.

Brand "ChatGPT" never touched. Component/file names never touched.
"""
import json
import os
import re
import sys
from copy import deepcopy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALES_DIR = os.path.join(ROOT, 'src/i18n/locales')

# Rules per language. Order matters: more specific (multi-word) first.
RULES = {
    'es': [
        # Avoid "Agentes IA de Inteligencia Artificial" (redundant): keep "Inteligencia Artificial" untouched
        (r'\bAplicaciones de Inteligencia Artificial\b', 'Agentes de Inteligencia Artificial'),
        (r'\baplicaciones de Inteligencia Artificial\b', 'agentes de Inteligencia Artificial'),
        (r'\bAplicaciones de IA\b', 'Agentes IA'),
        (r'\baplicaciones de IA\b', 'agentes IA'),
        (r'\bApps Especializadas\b', 'Agentes IA Especializados'),
        (r'\bapps especializadas\b', 'agentes IA especializados'),
        (r'\baplicaciones especializadas\b', 'agentes IA especializados'),
        (r'\bAplicaciones Especializadas\b', 'Agentes IA Especializados'),
        (r'\bCategorías de Apps\b', 'Categorías de Agentes IA'),
        (r'\bCategorías de Aplicaciones\b', 'Categorías de Agentes IA'),
        (r'\bTodas las Apps\b', 'Todos los Agentes IA'),
        (r'\bTodas las Aplicaciones\b', 'Todos los Agentes IA'),
        (r'\bNuestras Apps\b', 'Nuestros Agentes IA'),
        (r'\bnuestras apps\b', 'nuestros agentes IA'),
        (r'\bnuestras aplicaciones\b', 'nuestros agentes IA'),
        (r'\bApp Perfecta\b', 'Agente IA Perfecto'),
        (r'\bExplorar App\b', 'Explorar Agente'),
        (r'\bExplora App\b', 'Explora Agente'),
        (r'\bNueva App\b', 'Nuevo Agente IA'),
        (r'\bAplicación\b', 'Agente IA'),
        (r'\baplicación\b', 'agente IA'),
        (r'\bAplicaciones\b', 'Agentes IA'),
        (r'\baplicaciones\b', 'agentes IA'),
        (r'\bApps\b', 'Agentes IA'),
        (r'\bapps\b', 'agentes IA'),
        (r'\bApp\b', 'Agente IA'),
        (r'\bapp\b', 'agente IA'),
    ],
    'en': [
        (r'\bSpecialized Apps\b', 'Specialized AI Agents'),
        (r'\bspecialized apps\b', 'specialized AI agents'),
        (r'\bSpecialist apps\b', 'Specialist AI agents'),
        (r'\bspecialist apps\b', 'specialist AI agents'),
        (r'\bSpecialized Applications\b', 'Specialized AI Agents'),
        (r'\bspecialized applications\b', 'specialized AI agents'),
        (r'\bApp Categories\b', 'AI Agent Categories'),
        (r'\bExplore All Apps\b', 'Explore All AI Agents'),
        (r'\ball Apps\b', 'all AI Agents'),
        (r'\ball apps\b', 'all AI agents'),
        (r'\bPerfect App\b', 'Perfect AI Agent'),
        (r'\bExplore App\b', 'Explore Agent'),
        (r'\bNew App\b', 'New AI Agent'),
        (r'\bApplications\b', 'AI Agents'),
        (r'\bapplications\b', 'AI agents'),
        (r'\bApps\b', 'AI Agents'),
        (r'\bapps\b', 'AI agents'),
        (r'\bApp\b', 'AI Agent'),
        (r'\bapp\b', 'AI agent'),
    ],
    'fr': [
        (r'\bApps Spécialisées\b', 'Agents IA Spécialisés'),
        (r'\bapps spécialisées\b', 'agents IA spécialisés'),
        (r'\bApplications Spécialisées\b', 'Agents IA Spécialisés'),
        (r'\bapplications spécialisées\b', 'agents IA spécialisés'),
        (r"\bCatégories d'Apps\b", "Catégories d'Agents IA"),
        (r"\bCatégories d'Applications\b", "Catégories d'Agents IA"),
        (r'\bToutes les Apps\b', 'Tous les Agents IA'),
        (r'\bNouvelle App\b', 'Nouvel Agent IA'),
        (r"\bExplorer l'App\b", "Explorer l'Agent"),
        (r"\bApp Parfaite\b", 'Agent IA Parfait'),
        (r'\bApplications\b', 'Agents IA'),
        (r'\bapplications\b', 'agents IA'),
        (r'\bApps\b', 'Agents IA'),
        (r'\bapps\b', 'agents IA'),
        (r'\bApp\b', 'Agent IA'),
        (r'\bapp\b', 'agent IA'),
    ],
    'de': [
        (r'\bSpezialisierte Apps\b', 'Spezialisierte KI-Agenten'),
        (r'\bspezialisierte Apps\b', 'spezialisierte KI-Agenten'),
        (r'\bSpezialisierte Anwendungen\b', 'Spezialisierte KI-Agenten'),
        (r'\bApp-Kategorien\b', 'KI-Agenten-Kategorien'),
        (r'\bApp Erkunden\b', 'Agent Erkunden'),
        (r'\bNeue App\b', 'Neuer KI-Agent'),
        (r'\bAnwendungen\b', 'KI-Agenten'),
        (r'\bAnwendung\b', 'KI-Agent'),
        (r'\bApps\b', 'KI-Agenten'),
        (r'\bapps\b', 'KI-agenten'),
        (r'\bApp\b', 'KI-Agent'),
        (r'\bapp\b', 'KI-agent'),
    ],
    'it': [
        (r'\bApp Specializzate\b', 'Agenti IA Specializzati'),
        (r'\bapp specializzate\b', 'agenti IA specializzati'),
        (r'\bApplicazioni Specializzate\b', 'Agenti IA Specializzati'),
        (r'\bapplicazioni specializzate\b', 'agenti IA specializzati'),
        (r"\bCategorie di App\b", 'Categorie di Agenti IA'),
        (r"\bCategorie di Applicazioni\b", 'Categorie di Agenti IA'),
        (r'\bTutte le App\b', 'Tutti gli Agenti IA'),
        (r'\bEsplora App\b', 'Esplora Agente'),
        (r'\bNuova App\b', 'Nuovo Agente IA'),
        (r'\bApp Perfetta\b', 'Agente IA Perfetto'),
        # Italian: "app" is invariant. Plural when preceded by a number > 1.
        (r'\b(\d+) app\b', r'\1 agenti IA'),
        (r'\b(\d+) App\b', r'\1 Agenti IA'),
        (r'\bApplicazioni\b', 'Agenti IA'),
        (r'\bapplicazioni\b', 'agenti IA'),
        (r'\bApps\b', 'Agenti IA'),
        (r'\bapps\b', 'agenti IA'),
        (r'\bApp\b', 'Agente IA'),
        (r'\bapp\b', 'agente IA'),
    ],
    'pt': [
        (r'\bApps Especializadas\b', 'Agentes IA Especializados'),
        (r'\bapps especializadas\b', 'agentes IA especializados'),
        (r'\bAplicações Especializadas\b', 'Agentes IA Especializados'),
        (r'\baplicações especializadas\b', 'agentes IA especializados'),
        (r"\bCategorias de Apps\b", 'Categorias de Agentes IA'),
        (r"\bCategorias de Aplicações\b", 'Categorias de Agentes IA'),
        (r'\bTodas as Apps\b', 'Todos os Agentes IA'),
        (r'\bExplorar App\b', 'Explorar Agente'),
        (r'\bNova App\b', 'Novo Agente IA'),
        (r'\bApp Perfeita\b', 'Agente IA Perfeito'),
        (r'\bAplicações\b', 'Agentes IA'),
        (r'\baplicações\b', 'agentes IA'),
        (r'\bAplicação\b', 'Agente IA'),
        (r'\baplicação\b', 'agente IA'),
        (r'\bApps\b', 'Agentes IA'),
        (r'\bapps\b', 'agentes IA'),
        (r'\bApp\b', 'Agente IA'),
        (r'\bapp\b', 'agente IA'),
    ],
    'nl': [
        (r'\bGespecialiseerde Apps\b', 'Gespecialiseerde AI-agents'),
        (r'\bgespecialiseerde apps\b', 'gespecialiseerde AI-agents'),
        (r'\bGespecialiseerde Applicaties\b', 'Gespecialiseerde AI-agents'),
        (r'\bgespecialiseerde applicaties\b', 'gespecialiseerde AI-agents'),
        (r'\bApp-Categorieën\b', 'AI-agent-categorieën'),
        (r'\bVerken App\b', 'Verken Agent'),
        (r'\bNieuwe App\b', 'Nieuwe AI-agent'),
        (r'\bApplicaties\b', 'AI-agents'),
        (r'\bapplicaties\b', 'AI-agents'),
        (r'\bApps\b', 'AI-agents'),
        (r'\bapps\b', 'AI-agents'),
        (r'\bApp\b', 'AI-agent'),
        (r'\bapp\b', 'AI-agent'),
    ],
}


def transform(s: str, rules) -> str:
    for pattern, repl in rules:
        s = re.sub(pattern, repl, s)
    return s


def walk_and_transform(obj, rules):
    if isinstance(obj, dict):
        return {k: walk_and_transform(v, rules) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_and_transform(v, rules) for v in obj]
    if isinstance(obj, str):
        return transform(obj, rules)
    return obj


def diff_strings(before, after, path=''):
    """Yield (path, old, new) for every changed string."""
    if isinstance(before, dict):
        for k in before:
            yield from diff_strings(before[k], after[k], f'{path}.{k}' if path else k)
    elif isinstance(before, list):
        for i in range(len(before)):
            yield from diff_strings(before[i], after[i], f'{path}[{i}]')
    elif isinstance(before, str) and before != after:
        yield (path, before, after)


def process_locale(lang: str, apply: bool):
    fname = os.path.join(LOCALES_DIR, f'{lang}.json')
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    rules = RULES[lang]
    new_data = walk_and_transform(deepcopy(data), rules)
    changes = list(diff_strings(data, new_data))
    print(f'\n=== {lang} ===  changes: {len(changes)}')
    for path, old, new in changes[:8]:
        print(f'  {path}')
        print(f'    -  {old[:120]}')
        print(f'    +  {new[:120]}')
    if len(changes) > 8:
        print(f'  ... and {len(changes) - 8} more')
    if apply:
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'  ✓ wrote {fname}')
    return len(changes)


def main():
    apply = '--apply' in sys.argv
    only = None
    for arg in sys.argv[1:]:
        if arg.startswith('--lang='):
            only = arg.split('=', 1)[1]
    total = 0
    for lang in sorted(RULES.keys()):
        if only and lang != only:
            continue
        total += process_locale(lang, apply)
    print(f'\nTOTAL changes: {total}')
    if not apply:
        print('(dry-run; pass --apply to write)')


if __name__ == '__main__':
    main()
