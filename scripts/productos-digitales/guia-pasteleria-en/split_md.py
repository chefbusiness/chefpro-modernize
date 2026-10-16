#!/usr/bin/env python3
"""Trocea los tres .md ensamblados de la guía «Cómo Montar una Pastelería» en las tandas de traducción (SPEC §4).

Corta por encabezados `## ` y comprueba la ida y vuelta: concatenar las tandas de cada documento
devuelve el .md original byte a byte. Uso: python3 split_md.py
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ES = AQUI.parent / 'guia-pasteleria' / 'build' / 'docs'
SALIDA = AQUI / 'tandas' / 'es'

# documento → [(tanda, nº de secciones)]; la sección 0 es la portada (antes del primer `## `).
# Guía: 0 portada · 1 Índice · 2-21 caps. 1-20 · 22 anexo · 23 autor. Bonus: 0 · Índice · dec. 1-12 · autor.
# Plan: 0 · Índice · §1-6 · autor.
TANDAS = {
    'guia-pasteleria-obrador.md': [
        ('T01', 3), ('T02', 2), ('T03', 2), ('T04', 2), ('T05', 2), ('T06', 2),
        ('T07', 1), ('T08', 2), ('T09', 2), ('T10', 2), ('T11', 1), ('T12', 3)],
    'BONUS-12-decisiones-de-apertura.md': [('B01', 6), ('B02', 4), ('B03', 5)],
    'business-plan-modelo-pasteleria.md': [('P01', 6), ('P02', 3)],
}
# Tandas que se readaptan a EE. UU. (todas salvo T07): una cifra del ES ausente en el EN es aviso, no error
ADAPT = {t for plan in TANDAS.values() for t, _ in plan} - {'T07'}
# Ficheros ES citados que no tienen EN (SPEC §2): el texto EN no puede citarlos
ORFANOS = {'05-pasteleria', 'BONUS-02-calendario-anual-tareas', '04-tareas-perfiles',
           '10-plan-produccion-semanal', '12-control-alergenos-vitrina'}


def secciones(texto):
    return re.split(r'(?m)^(?=## )', texto)


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for doc, plan in TANDAS.items():
        original = (ES / doc).read_text(encoding='utf-8')
        partes = secciones(original)
        if sum(n for _, n in plan) != len(partes):
            sys.exit(f'{doc}: {len(partes)} secciones y el plan reparte {sum(n for _, n in plan)}')
        i, trozos = 0, []
        for tanda, n in plan:
            trozo = ''.join(partes[i:i + n])
            i += n
            (SALIDA / f'{tanda}.md').write_text(trozo, encoding='utf-8')
            trozos.append(trozo)
            print(f'{tanda}: {len(trozo.split()):6d} palabras · {partes[i - n].splitlines()[0][:60]}')
        if ''.join(trozos) != original:
            sys.exit(f'{doc}: la ida y vuelta NO es byte a byte')
        print(f'{doc}: ida y vuelta OK ({len(partes)} secciones)')


if __name__ == '__main__':
    main()
