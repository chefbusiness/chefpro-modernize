#!/usr/bin/env python3
"""
Replace competitor-context "apps" mentions in Kit Tareas / kit-inventario / ebook
components. These refer to competing SaaS (Trail, generic management apps) — using
"agentes IA" here would be wrong, so we use "software" / "sistemas" instead.

Run with --apply to write changes.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (regex, replacement) — applied in order.
RULES = [
    # Hero comparison: "Lo que apps de gestión cobran €40/mes..."
    (r'\bLo que apps de gestión cobran\b', 'Lo que el software de gestión cobra'),
    # FAQ Q comparing with Trail
    (r'¿En qué se diferencia de Trail u otras apps\?', '¿En qué se diferencia de Trail u otros sistemas?'),
    (r'¿En que se diferencia de Trail u otras apps\?', '¿En que se diferencia de Trail u otros sistemas?'),
    # FAQ Q comparing with management apps
    (r'¿En qué se diferencia de apps de gestión\?', '¿En qué se diferencia del software de gestión?'),
    # FAQ A starting with "Las apps de gestión cobran..."
    (r'\bLas apps de gestión cobran\b', 'El software de gestión cobra'),
    # WhySection desc tail: "Las tareas que apps genéricas no cubren..."
    (r'\bLas tareas que apps genéricas no cubren\b', 'Las tareas que los sistemas genéricos no cubren'),
    (r'\bLas tareas que apps genericas no cubren\b', 'Las tareas que los sistemas genericos no cubren'),
    (r'\bLa operativa completa que apps genéricas no cubren\b',
     'La operativa completa que los sistemas genéricos no cubren'),
    # WhySection card title: "Apps Cobran €XX/mes. Esto es €XX"
    (r"'Apps Cobran (\d+ ?(?:EUR|€)/mes)\. Esto es ([\d,]+ ?(?:EUR|€))'",
     r"'Software de Gestión Cobra \1. Esto es \2'"),
    # eBook FAQ: "lance nuevas apps" — this IS AICP product, so use agentes IA
    (r'\blance nuevas apps\b', 'lance nuevos agentes IA'),
    # Testimonial: "apps genericas no cubren ni el 20%"
    (r'\bLas apps genericas no cubren\b', 'Los sistemas genericos no cubren'),
    (r'\bapps genéricas no cubren\b', 'sistemas genéricos no cubren'),
    (r'\bapps genericas no cubren\b', 'sistemas genericos no cubren'),
]

# Files to scan — restrict to components/data to avoid touching anything outside.
INCLUDE_DIRS = [
    'src/components',
    'src/data',
]
EXCLUDE_NAMES = {'AppsCategories.tsx', 'AppsFinder.tsx', 'FeaturedApps.tsx', 'CompatibleAppsMarquee.tsx'}


def iter_files():
    for d in INCLUDE_DIRS:
        for root, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                if not (f.endswith('.tsx') or f.endswith('.ts')):
                    continue
                # Don't touch the apps component itself — those are React component files
                # that already reference the AICP product apps; we already handled their
                # i18n keys in the locale step.
                if f in EXCLUDE_NAMES:
                    continue
                yield os.path.join(root, f)


def main():
    apply = '--apply' in sys.argv
    total_changes = 0
    files_touched = 0
    for path in iter_files():
        with open(path, 'r', encoding='utf-8') as fp:
            text = fp.read()
        new_text = text
        for pat, repl in RULES:
            new_text = re.sub(pat, repl, new_text)
        if new_text != text:
            files_touched += 1
            # Count lines changed (rough).
            old_lines = text.splitlines()
            new_lines = new_text.splitlines()
            file_changes = sum(1 for a, b in zip(old_lines, new_lines) if a != b)
            total_changes += file_changes
            print(f'{os.path.relpath(path, ROOT)}: {file_changes} line(s)')
            if apply:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(new_text)
    print(f'\n{files_touched} files, {total_changes} line(s) changed')
    if not apply:
        print('(dry-run; pass --apply to write)')


if __name__ == '__main__':
    main()
