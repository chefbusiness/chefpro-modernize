#!/usr/bin/env python3
"""Alinea las capacidades de las 3 paelleras Garcima del catálogo con la tabla del Manual Técnico.
Edición quirúrgica a nivel de run; idempotente (si ya está aplicado, no cambia nada)."""
import docx, sys
F = '/root/wt-manual/astro-site/public/dl/plan-negocio-paellero-eventos/catalogo-equipamiento-utensilios-menaje-paellero.docx'
REF = '(ver la tabla de escalado del Manual Técnico)'
CAMBIOS = [  # (texto exacto actual, texto nuevo)
 ('Función: Paella eventos pequeños 15-25 pax', f'Función: Paella eventos pequeños ≈ 11-15 raciones {REF}'),
 ('Paellera de acero pulido de 60 cm de diámetro, capacidad 25-30 raciones tipo cumpleaños familiar.',
  f'Paellera de acero pulido de 60 cm de diámetro, capacidad ≈ 11-15 raciones {REF}, tipo cumpleaños familiar.'),
 ('Función: Paella eventos medianos 40-60 pax', f'Función: Paella eventos medianos ≈ 30-40 raciones {REF}'),
 ('Función: Paella eventos grandes 80-150 pax', f'Función: Paella eventos grandes ≈ 60-80 raciones {REF}'),
]
# descripciones sin cifra: se añade la capacidad al final del texto
AÑADIR = [('Paellera de 90 cm, ideal para bodas íntimas', 'capacidad ≈ 30-40 raciones'),
          ('Paellera grande para bodas y eventos corporate', 'capacidad ≈ 60-80 raciones')]
d = docx.Document(F)
n = 0
for p in d.paragraphs:
    for r in p.runs:
        for a, b in CAMBIOS:
            if r.text == a:
                print('ANTES:', a); print('DESPUÉS:', b); r.text = b; n += 1
        for pref, cap in AÑADIR:
            if r.text.startswith(pref) and 'raciones' not in r.text:
                a = r.text
                b = a.rstrip()
                b = (b[:-1] if b.endswith('.') else b) + f', {cap} {REF}.'
                print('ANTES:', a); print('DESPUÉS:', b); r.text = b; n += 1
if n: d.save(F)
print('cambios:', n)
