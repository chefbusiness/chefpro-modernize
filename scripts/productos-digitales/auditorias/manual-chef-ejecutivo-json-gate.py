# -*- coding: utf-8 -*-
"""GATE de la fusión D24 — Manual del Chef Ejecutivo."""
import json
import re
import sys
from pathlib import Path
from collections import Counter

JSON_PATH = Path(__file__).parent / "guias-v2-research-sector.json"
BLACKLIST_NOTA = "LISTA NEGRA: no se cita; el lector lo mide con su herramienta."

data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
datos = data["datos"]

fallos = []

# 1) Total de entradas
total = len(datos)
if total != 225:
    fallos.append(f"Total de entradas = {total}, esperado 225")

# 2) Recuento por prefijo
ce = [d for d in datos if re.match(r"^CE-\d+$", d["id"])]
cs = [d for d in datos if re.match(r"^CS-\d+$", d["id"])]
if len(ce) != 40:
    fallos.append(f"CE-* = {len(ce)}, esperado 40")
if len(cs) != 23:
    fallos.append(f"CS-* = {len(cs)}, esperado 23")

# 3) Numeración exacta CE-01..CE-40 y CS-01..CS-23
ce_ids_esperados = {f"CE-{i:02d}" for i in range(1, 41)}
cs_ids_esperados = {f"CS-{i:02d}" for i in range(1, 24)}
ce_ids_reales = {d["id"] for d in ce}
cs_ids_reales = {d["id"] for d in cs}
if ce_ids_reales != ce_ids_esperados:
    fallos.append(f"CE ids no coinciden. Faltan: {sorted(ce_ids_esperados - ce_ids_reales)} "
                  f"Sobran: {sorted(ce_ids_reales - ce_ids_esperados)}")
if cs_ids_reales != cs_ids_esperados:
    fallos.append(f"CS ids no coinciden. Faltan: {sorted(cs_ids_esperados - cs_ids_reales)} "
                  f"Sobran: {sorted(cs_ids_reales - cs_ids_esperados)}")

# 4) Colisiones de id en todo el fichero
ids_todos = [d["id"] for d in datos]
cont = Counter(ids_todos)
colisiones = [i for i, n in cont.items() if n > 1]
if colisiones:
    fallos.append(f"IDs duplicados en TODO el fichero: {colisiones}")

# 5) Todas con url o con la nota de lista negra
sin_url_sin_blacklist = []
for d in ce + cs:
    tiene_url = bool(d.get("url", "").strip())
    tiene_blacklist_nota = BLACKLIST_NOTA in (d.get("nota") or "")
    if not tiene_url and not tiene_blacklist_nota:
        sin_url_sin_blacklist.append(d["id"])
if sin_url_sin_blacklist:
    fallos.append(f"Sin url NI nota de lista negra: {sin_url_sin_blacklist}")

# 6) fiabilidad válida
fiabs_validas = {"alta", "media", "baja"}
malas = [d["id"] for d in ce + cs if d.get("fiabilidad") not in fiabs_validas]
if malas:
    fallos.append(f"fiabilidad inválida en: {malas}")

# 7) Recuento de fiabilidad por bloque (informativo)
def resumen(lista, nombre):
    c = Counter(d["fiabilidad"] for d in lista)
    print(f"{nombre}: alta={c.get('alta',0)} media={c.get('media',0)} baja={c.get('baja',0)} total={len(lista)}")

print("=== GATE manual-chef-ejecutivo-json-fusion-2026-09-06 ===")
print(f"Total entradas en el JSON: {total}")
resumen(ce, "CE-*")
resumen(cs, "CS-*")
print(f"Sin colisión de id en el fichero completo: {'OK' if not colisiones else 'FALLO'}")
print(f"Todas con url o nota de lista negra: {'OK' if not sin_url_sin_blacklist else 'FALLO'}")

if fallos:
    print("\n--- FALLOS ---")
    for f in fallos:
        print(f"- {f}")
    sys.exit(1)
else:
    print("\nGATE VERDE: 225 entradas, 40 CE-*, 23 CS-*, sin colisiones, todas con url o lista negra.")
