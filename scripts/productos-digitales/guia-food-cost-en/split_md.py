#!/usr/bin/env python3
"""Trocea los dos .md ensamblados de la guía ES en las tandas de traducción (SPEC §4).

Corta por encabezados `## ` y comprueba la ida y vuelta: concatenar las tandas de cada documento
devuelve el .md original byte a byte. Uso: python3 split_md.py
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ES = AQUI.parent / 'guia-food-cost' / 'build' / 'docs' / 'guia-food-cost-ingenieria-menu'
SALIDA = AQUI / 'tandas' / 'es'

# documento → [(tanda, nº de secciones)]; la sección 0 es la portada (antes del primer `## `).
# Guía: 0 portada · 1 Índice · 2-21 caps. 1-20 · 22 cierre. Bonus: 0 portada · 1 Índice · 2-13 ej. 1-12 · 14 cierre.
TANDAS = {
    'guia-food-cost-ingenieria-menu.md': [
        ('T01', 4), ('T02', 2), ('T03', 2), ('T04', 2), ('T05', 2), ('T06', 2),
        ('T07', 2), ('T08', 2), ('T09', 2), ('T10', 1), ('T11', 2)],
    'BONUS-ejercicios-resueltos.md': [('B01', 6), ('B02', 3), ('B03', 6)],
}


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
