#!/usr/bin/env python3
"""gate_f1_spec.py — Ronda 2 de la SPEC de la Taquería = GATE DE SCRIPT (política de 3 fases, 20-sep-2026).
Comprueba que las correcciones decididas tras la refutación (auditorias/kit-tareas-taqueria-SPEC-refutacion-2026-09-20.md)
están en la SPEC, sin abrir otra ronda de agente. Uso: python3 gate_f1_spec.py [ruta SPEC]. Exit 0 = PASS."""
import re, sys, unicodedata
p = sys.argv[1] if len(sys.argv) > 1 else 'scripts/productos-digitales/kit-tareas-taqueria/02-SPEC-kit-tareas-taqueria.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
fallos = []
def req(txt, n=1, nombre=None):
    c = s.count(txt)
    if c < n: fallos.append(f"FALTA ({c}<{n}): {nombre or txt}")
def forb(txt, nombre=None):
    c = s.count(txt)
    if c: fallos.append(f"PROHIBIDO ({c}): {nombre or txt}")
# B3 env var · B4 páginas y generador · B1 molde calendario · B8 pie · B7 fila 4 · B2 contrato helpers
req('VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA'); forb('VITE_STRIPE_PAYMENT_LINK_KIT_TAREAS_TAQUERIA')
req('fase5-generate-zona-app.py'); req('kit-tareas-taqueria-access.astro'); req('kit-tareas-taqueria-library.astro')
req('Fecha / Evento'); req('Antelación'); req('Tareas Clave')
req('— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro · aichef.pro')
req('fila 4'); req('freeze_panes'); req('"✓,—,N/A"'); req('astro-site/public/dl/kit-tareas-taqueria')
req('create_task_sheet'); req('create_calendar_sheet'); req('add_instructions_sheet')
# A2 gate de registro horario acotado · D5 redacción
req('registro de jornada (obligatorio; en el soporte que exija la normativa vigente)')
req('control horario digital'); req('fichaje digital')
# A3 tildes: insensible a mayúsculas, controles
req('maría'); req('sésamo'); req('U+00BA')
# 06 pestañas
req('Tortillería'); req('Salsas')
# B5 objetivo 300 / 270-330
req('270-330'); req('300')
# no latinos · espacio fino · guion no separable
malos = [ch for ch in set(s) if unicodedata.category(ch).startswith('L') and
         any(k in unicodedata.name(ch, '') for k in ('CJK', 'CYRILLIC', 'HANGUL', 'ARABIC', 'HEBREW', 'THAI', 'HIRAGANA', 'KATAKANA'))]
if malos: fallos.append(f"NO LATINOS: {malos[:10]}")
if ' ' in s: fallos.append("U+202F presente (las unidades del xlsx van con U+0020)")
if '‑' in s: fallos.append("U+2011 presente")
# 65/75 °C solo en frases de derogación/prohibición/deuda
corte7 = next((i for i, l in enumerate(lines, 1) if re.match(r'#+\s*§7', l)), len(lines) + 1)  # §7 = deuda ajena, exenta
for i, l in enumerate(lines, 1):
    if i >= corte7: break
    if re.search(r'\b6[5]\s*°\s*C|\b75\s*°\s*C', l) and not re.search(r'derog|prohib|NUNCA|nunca|deuda|gate|G2|R1|no debe|no se imprime|no aparece|0 apariciones|cifra vieja|viej', l, re.I):
        fallos.append(f"65/75 °C sin contexto de prohibición en la línea {i}: {l.strip()[:100]}")
# suma de rangos de §3.1
m = re.search(r'#+\s*§?\s*3\.1[^\n]*\n(.*?)(?=\n#{2,3} )', s, re.S)
if not m:
    fallos.append("no encuentro la sección §3.1 para sumar rangos")
else:
    pares = []
    for fila in m.group(1).split('\n'):
        if not re.match(r'\|\s*0\d\s*\|', fila): continue          # solo filas 01-08 de la tabla
        celda = fila.rstrip('|').split('|')[-1]
        rangos = re.findall(r'(\d{1,3})\s*[-–]\s*(\d{1,3})', celda)
        if rangos: a, b = rangos[-1]; pares.append((int(a), int(b)))   # el último rango: en 06 es el total (42-54)
    smin, smax = sum(a for a, _ in pares), sum(b for _, b in pares)
    print(f"§3.1: {len(pares)} rangos, mínimos {smin}, máximos {smax}")
    if (smin, smax) != (270, 330): fallos.append(f"§3.1 suma {smin}-{smax}, esperado 270-330")
print(f"líneas: {len(lines)} · menciones 'Salsero': {s.count('Salsero')} (glosa legítima; pestaña debe ser 'Salsas')")
if fallos:
    print("GATE F1 SPEC: FAIL"); [print(" -", f) for f in fallos]; sys.exit(1)
print("GATE F1 SPEC: PASS")
