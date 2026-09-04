#!/usr/bin/env python3
"""Comprueba un bloque escrito por un agente con los MISMOS detectores que usa
documentos.py antes de aceptar una salida de bridge.
Uso: python3 check_bloque.py <ruta_txt> <palabras_min> [<epígrafe1> <epígrafe2> …]
Exit 0 = limpio y con extensión suficiente; 1 = defectos (los imprime)."""
import importlib.util, re, sys
sp = importlib.util.spec_from_file_location('d', '/Users/johnguerrero/chefpro-modernize/scripts/productos-digitales/guias-v2_0/documentos.py')
d = importlib.util.module_from_spec(sp); sp.loader.exec_module(d)
ruta, minimo = sys.argv[1], int(sys.argv[2]); epis = sys.argv[3:]
t = open(ruta, encoding='utf-8').read().strip()
fallos = []
n = len(t.split())
if n < minimo:
    fallos.append(f'corto: {n} palabras (mínimo {minimo})')
for m in d.defectos_de_bloque(t):
    fallos.append(f"{m['tipo']}: {m['muestra'][:100]!r}")
if not t.startswith('### '):
    fallos.append('no empieza por «### »')
if re.search(r'^#{1,2} ', t, re.M):
    fallos.append('lleva encabezados de nivel 1 o 2')
if '|' in t and re.search(r'^\|.*\|$', t, re.M):
    fallos.append('lleva una tabla Markdown (prohibido: las pone el maquetador)')
if re.search(r'[一-鿿Ѐ-ӿ가-힯؀-ۿ֐-׿฀-๿]', t):
    fallos.append('caracteres no latinos')
if re.search(r'\.xlsx!|![A-Z]{1,3}\d+\b', t):
    fallos.append('cita de celda en sintaxis de prompt (fichero!Hoja!Celda)')
for e in epis:
    if f'### {e}' not in t:
        fallos.append(f'falta el epígrafe literal: ### {e}')
if fallos:
    print('DEFECTOS:'); [print(' -', f) for f in fallos]; sys.exit(1)
print(f'OK {n} palabras')
