#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8C — Inserta banners de productos digitales en las librerías de prompts ya publicadas.

POLÍTICA (John, 2026-07-31): todo contenido lleva MÍNIMO 3 banners de productos
digitales a tres alturas. El generador ya lo hace con los posts nuevos; este
script cubre los que se publicaron antes de existir la política.

Los productos digitales son **pago único con acceso vitalicio**, no la
suscripción recurrente del SaaS. Es la línea de negocio más desatendida y estos
posts los lee justo quien ya usa la plataforma: el encaje es natural.

CRITERIO DE ELECCIÓN: relevancia temática con el agente, nunca relleno. Un
pizzero no ve el kit de heladería. Cuando no hay un kit específico del oficio se
cae a los transversales (escandallos, tareas, prompts).

El maquetado del banner NO se duplica: se importa de `fase8c-libreria-assemble.py`,
que es donde vive. Si cambia allí, cambia aquí.

Es idempotente: un post que ya tiene banners se salta.

Uso:
    python3 scripts/astro-migration/fase8c-banners-retrofit.py --dry-run
    python3 scripts/astro-migration/fase8c-banners-retrofit.py
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
GEN = Path(__file__).parent / 'fase8c-libreria-assemble.py'

# agente (por slug del post) → 3 productos, del más específico al más transversal
PRODUCTOS = {
    # ── Creatividad culinaria ────────────────────────────────────────────────
    'recetario-cocina-creativa-ai': ['kit-tareas-restaurante-creativo', 'pro-prompts-ebook', 'kit-escandallos'],
    'pasteleria-creativa-ai':       ['kit-tareas-pasteleria', 'kit-escandallos', 'pro-prompts-ebook'],
    'chocolateria-creativa-ai':     ['kit-tareas-chocolateria', 'kit-escandallos', 'pro-prompts-ebook'],
    'heladeria-creativa-ai':        ['kit-tareas-heladeria', 'kit-escandallos', 'pro-prompts-ebook'],
    'panaderia-creativa-ai':        ['kit-tareas-pasteleria', 'kit-escandallos', 'pro-prompts-ebook'],
    'fermentus-ai':                 ['kit-tareas-pasteleria', 'pro-prompts-ebook', 'kit-escandallos'],
    'vegchef-plant-based-ai':       ['pro-prompts-ebook', 'kit-escandallos', 'kit-tareas'],
    'food-pairing-ai':              ['pro-prompts-ebook', 'kit-escandallos', 'kit-tareas-restaurante-creativo'],
    # ── Consultoría Gastro Pro ───────────────────────────────────────────────
    'consultor-gastronomico-ai':    ['kit-plan-financiero', 'guia-restaurante-gastronomico', 'kit-escandallos'],
    'chef-consultor-pro-ai':        ['guia-restaurante-gastronomico', 'kit-escandallos', 'kit-plan-financiero'],
    'heladero-consultor-pro-ai':    ['kit-tareas-heladeria', 'kit-plan-financiero', 'kit-escandallos'],
    'chocolatero-consultor-pro-ai': ['kit-tareas-chocolateria', 'kit-plan-financiero', 'kit-escandallos'],
    'pastelero-consultor-pro-ai':   ['kit-tareas-pasteleria', 'kit-plan-financiero', 'kit-escandallos'],
    'pizzero-consultor-pro-ai':     ['kit-tareas-pizzeria', 'guia-restaurante-casual', 'kit-escandallos'],
    'barista-consultor-pro-ai':     ['kit-tareas-cafeteria', 'kit-plan-financiero', 'kit-escandallos'],
    'sommelier-consultor-pro-ai':   ['kit-tareas-bar', 'guia-restaurante-gastronomico', 'kit-escandallos'],
    'bartender-consultor-pro-ai':   ['kit-tareas-bar', 'kit-plan-financiero', 'kit-escandallos'],
    'panadero-consultor-pro-ai':    ['kit-tareas-pasteleria', 'kit-plan-financiero', 'kit-escandallos'],
    # ── Gastro Profile ───────────────────────────────────────────────────────
    'chef-privado-pro-ai':          ['kit-tareas-chef-privado', 'kit-escandallos', 'pro-prompts-ebook'],
    'chef-ejecutivo-pro-ai':        ['kit-escandallos', 'kit-gestion-personal', 'kit-inventario'],
    'gerente-de-restaurante-pro-ai': ['kit-plan-financiero', 'kit-gestion-personal', 'kit-inventario'],
    # ── Conocimientos · Herramientas · Conceptos de negocio ──────────────────
    'gastro-lexicum-ai':            ['pro-prompts-ebook', 'kit-escandallos', 'kit-tareas'],
    'mermas-gencal':                ['kit-inventario', 'kit-escandallos', 'pack-appcc'],
    'id-alergenos':                 ['pack-appcc', 'kit-tareas', 'pro-prompts-ebook'],
    'catering-ai':                  ['kit-tareas-catering', 'kit-plan-financiero', 'kit-escandallos'],
    'burger-pro-ai':                ['kit-tareas-hamburgueseria', 'guia-restaurante-casual', 'kit-escandallos'],
    'comida-de-personal':           ['kit-gestion-personal', 'kit-escandallos', 'kit-tareas'],
}

H2_BLOQUE = re.compile(r'<h2 class="wp-block-heading">Prompts para ')
MARCA = 'Producto digital · pago único'


def cargar_generador():
    spec = importlib.util.spec_from_file_location('gen', GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.argv = ['gen']          # el módulo no debe parsear nuestros argumentos
    spec.loader.exec_module(mod)
    return mod


def alturas(n_bloques):
    """3 posiciones repartidas por el artículo (índice del bloque ANTES del cual
    se inserta). Nunca antes del primero: el lector tiene que entrar en materia
    antes de ver la primera oferta."""
    return {7: [2, 4, 6],      # 29 % · 57 % · 86 %
            6: [1, 3, 5],      # 17 % · 50 % · 83 %
            5: [1, 2, 4]       # 20 % · 40 % · 80 %
            }.get(n_bloques, sorted({max(1, round(n_bloques * f))
                                     for f in (0.25, 0.5, 0.75)}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    gen = cargar_generador()
    prods = gen.catalogo_productos()

    tocados = insertados = saltados = 0
    sin_mapa = []
    for md in sorted(CONTENT.glob('libreria-de-prompts-para-*.md')):
        clave = md.stem.replace('libreria-de-prompts-para-', '')
        txt = md.read_text(encoding='utf-8')
        if MARCA in txt:
            saltados += 1
            continue
        if clave not in PRODUCTOS:
            sin_mapa.append(clave)
            continue
        pos = [m.start() for m in H2_BLOQUE.finditer(txt)]
        if len(pos) < 3:
            sin_mapa.append('%s (solo %d bloques)' % (clave, len(pos)))
            continue
        idx = [i for i in alturas(len(pos)) if i < len(pos)]
        nuevo, desplaz = txt, 0
        for n, i in enumerate(idx[:3]):
            b = gen.banner(PRODUCTOS[clave][n], prods, md.stem)
            p = pos[i] + desplaz
            nuevo = nuevo[:p] + b + nuevo[p:]
            desplaz += len(b)
        if not args.dry_run:
            md.write_text(nuevo, encoding='utf-8')
        tocados += 1
        insertados += len(idx[:3])
        print('  %-46s %d bloques → banners tras %s' % (clave[:46], len(pos), idx[:3]))

    print('\n%s%d posts · %d banners · %d ya tenían · %d sin mapa'
          % ('[dry-run] ' if args.dry_run else '', tocados, insertados, saltados, len(sin_mapa)))
    for s in sin_mapa:
        print('   ⚠️  sin productos asignados:', s)
    return 1 if sin_mapa else 0


if __name__ == '__main__':
    sys.exit(main())
