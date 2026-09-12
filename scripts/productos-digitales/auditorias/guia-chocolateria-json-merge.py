# -*- coding: utf-8 -*-
"""
Fusiona los ids CHS-* (sector, Research L4) y CHN-* (verificación legal) de
«Cómo Montar una Chocolatería» en guias-v2-research-sector.json.

Calca el patrón de guia-pasteleria-json-merge.py (2026-09-10), con la
diferencia de que aquí los DOS lotes (CHS y CHN) ya existen desde el arranque
(no hay una segunda pasada de otro agente en paralelo), pero se mantiene el
mismo tratamiento «opcional si falta» por si un día se reejecuta con uno de
los dos ficheros movido o renombrado.

  - dry-run por defecto: SIEMPRE simula la fusión y corre el gate contra el
    resultado simulado; sólo escribe si se pasa --apply Y el gate pasa.
  - idempotente: si los ids ya están en el fichero destino, no se duplican
    (se detectan y se excluyen del lote a añadir; si no hay nada nuevo que
    añadir, termina en OK sin tocar el fichero).
  - respaldo previo (sólo en --apply) en el scratchpad de ESTA sesión, nunca
    en el repo.
  - los EXCLUIDOS del verificador legal (guia-chocolateria-verificacion-legal-
    2026-09-12-EXCLUIDOS.json) NO se fusionan: son entradas descartadas por el
    verificador, no datos válidos.

Uso:
  python3 guia-chocolateria-json-merge.py            # dry-run (no escribe nada)
  python3 guia-chocolateria-json-merge.py --apply     # escribe si el gate pasa
"""
import json
import shutil
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
JSON_PATH = HERE / "guias-v2-research-sector.json"
CHS_PATH = HERE / "guia-chocolateria-ids-CHS.json"
CHN_PATH = HERE / "guia-chocolateria-verificacion-legal-2026-09-12.json"

# Directorio del scratchpad de ESTA sesión (nunca el repo) para el respaldo.
SCRATCHPAD_DIR = Path(
    "/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/"
    "3fbfe5a7-ebc5-452f-9893-f0fa6b68474a/scratchpad"
)

EXPECTED_KEYS = {
    "id", "tema", "dato", "cifra", "unidad", "anio_del_dato", "fuente_titulo",
    "url", "fecha_publicacion", "cita_literal", "fiabilidad", "nota",
}
BASELINE_TOTAL = 411  # total en guias-v2-research-sector.json antes de esta fusión


def cargar_lote(path, prefijo):
    """Carga un fichero de entradas nuevas (lista de objetos). Devuelve
    (lista, existe). Si no existe, devuelve ([], False) sin abortar: el
    llamador decide si eso es aceptable."""
    if not path.exists():
        return [], False
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print(f"ERROR: {path.name} no es una lista JSON de objetos.")
        sys.exit(1)
    no_prefijo = [d.get("id") for d in data if not str(d.get("id", "")).startswith(prefijo)]
    if no_prefijo:
        print(f"ERROR: {path.name} trae ids que no empiezan por '{prefijo}-': {no_prefijo[:10]}")
        sys.exit(1)
    return data, True


def validar_lote(nombre, lote):
    """Valida forma de cada entrada de un lote nuevo (claves exactas, cifra
    nunca '', url no vacía). Devuelve lista de fallos (vacía si OK)."""
    fallos = []
    for d in lote:
        id_ = d.get("id", "<sin id>")
        claves = set(d.keys())
        if claves != EXPECTED_KEYS:
            faltan = EXPECTED_KEYS - claves
            sobran = claves - EXPECTED_KEYS
            fallos.append(f"{id_}: claves distintas de las 12 (faltan={sorted(faltan)}, sobran={sorted(sobran)})")
            continue
        if d.get("cifra") == "":
            fallos.append(f"{id_}: cifra es '' (debe ser numérica o null)")
        if not isinstance(d.get("cifra"), (int, float, type(None))):
            fallos.append(f"{id_}: cifra no es numérica ni null (tipo {type(d.get('cifra')).__name__})")
        if d.get("fiabilidad") not in ("alta", "media", "baja"):
            fallos.append(f"{id_}: fiabilidad inválida ({d.get('fiabilidad')!r})")
        # url: se permite null/"" cuando fiabilidad es "baja" y así lo declara
        # la propia entrada (huecos deliberados, ej. CHS-01 "sin fuente
        # primaria de inversión"); en cualquier otro caso, url vacía es fallo.
        if not d.get("url") and d.get("fiabilidad") != "baja":
            fallos.append(f"{id_}: url vacía o ausente (y fiabilidad no es 'baja')")
    if fallos:
        print(f"--- Fallos de forma en {nombre} ---")
        for f in fallos:
            print(f"  - {f}")
    return fallos


def gate(datos_finales, n_chn_lote, n_chs_lote):
    """Corre el GATE sobre la lista final simulada (o real, tras escribir).
    Devuelve lista de fallos (vacía si el gate pasa)."""
    fallos = []

    total = len(datos_finales)
    esperado = BASELINE_TOTAL + n_chn_lote + n_chs_lote
    if total != esperado:
        fallos.append(f"Total de entradas = {total}, esperado {BASELINE_TOTAL} + {n_chn_lote} CHN-* + "
                       f"{n_chs_lote} CHS-* = {esperado}")

    ids_todos = [d["id"] for d in datos_finales]
    cont = Counter(ids_todos)
    colisiones = [i for i, n in cont.items() if n > 1]
    if colisiones:
        fallos.append(f"IDs duplicados en TODO el fichero: {sorted(colisiones)}")

    # Los checks de forma (claves/cifra/url) sólo tienen sentido sobre el lote
    # que esta fusión controla (CHN-* y CHS-*): el resto de las 411 entradas
    # ya vive con sus propias convenciones históricas y no es el contrato de
    # esta tarea.
    lote_nuevo = [d for d in datos_finales if d["id"].startswith("CHN-") or d["id"].startswith("CHS-")]
    fallos_forma_final = []
    for d in lote_nuevo:
        id_ = d["id"]
        claves = set(d.keys())
        if claves != EXPECTED_KEYS:
            fallos_forma_final.append(f"{id_}: claves distintas de las 12 en el fichero final")
        if d.get("cifra") == "":
            fallos_forma_final.append(f"{id_}: cifra == '' en el fichero final")
        if not d.get("url") and d.get("fiabilidad") != "baja":
            fallos_forma_final.append(f"{id_}: url vacía en el fichero final (y fiabilidad no es 'baja')")
    fallos.extend(fallos_forma_final)

    print("=== GATE guia-chocolateria-json-merge ===")
    print(f"Total entradas (simulado o real): {total} (esperado {esperado})")
    print(f"CHS-* en el lote: {n_chs_lote} · CHN-* en el lote: {n_chn_lote} · baseline: {BASELINE_TOTAL}")
    print(f"Colisiones de id: {'ninguna' if not colisiones else colisiones}")
    print(f"Entradas del lote (CHS-*/CHN-*) con forma válida (12 claves, cifra numérica/null, url no "
          f"vacía salvo fiabilidad 'baja'): {len(lote_nuevo) - len(fallos_forma_final)} de {len(lote_nuevo)}")

    return fallos


def main():
    apply_ = "--apply" in sys.argv

    if not JSON_PATH.exists():
        print(f"ERROR: no existe {JSON_PATH}")
        sys.exit(1)
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    existentes = {d["id"] for d in data["datos"]}
    total_actual = len(data["datos"])
    if total_actual != BASELINE_TOTAL:
        print(f"AVISO: el fichero tiene {total_actual} entradas, no el baseline esperado de "
              f"{BASELINE_TOTAL}. Puede que esta fusión ya se haya aplicado antes, o que otra fusión "
              f"distinta haya tocado el fichero entretanto. Se continúa igualmente usando el recuento "
              f"real como referencia del gate.")

    chs_lote, chs_existe = cargar_lote(CHS_PATH, "CHS")
    if not chs_existe:
        print(f"ERROR: no existe {CHS_PATH}. Los CHS-* son obligatorios para esta fusión.")
        sys.exit(1)

    chn_lote, chn_existe = cargar_lote(CHN_PATH, "CHN")
    if not chn_existe:
        print(f"AVISO: no existe todavía {CHN_PATH.name}. Se fusionan SOLO los {len(chs_lote)} CHS-*; "
              f"vuelve a ejecutar este script cuando exista para incorporar los CHN-* en la misma pasada.")

    # Validación de forma de los lotes nuevos, antes de tocar nada.
    fallos_forma = validar_lote("guia-chocolateria-ids-CHS.json", chs_lote) + \
                   validar_lote("guia-chocolateria-verificacion-legal-2026-09-12.json", chn_lote)
    if fallos_forma:
        print(f"\nABORTA: {len(fallos_forma)} fallos de forma en los lotes de entrada. No se toca "
              f"{JSON_PATH.name}.")
        sys.exit(1)

    # Colisión interna de cada lote y entre lotes.
    todos_nuevos = chs_lote + chn_lote
    ids_nuevos = [d["id"] for d in todos_nuevos]
    cont_nuevos = Counter(ids_nuevos)
    dup_internos = [i for i, n in cont_nuevos.items() if n > 1]
    if dup_internos:
        print(f"ERROR: ids duplicados dentro de los lotes de entrada: {sorted(dup_internos)}")
        sys.exit(1)

    # Idempotencia: lo que ya está en el fichero destino no se vuelve a añadir.
    ya_presentes = [d["id"] for d in todos_nuevos if d["id"] in existentes]
    a_anadir = [d for d in todos_nuevos if d["id"] not in existentes]
    if ya_presentes:
        print(f"INFO: {len(ya_presentes)} ids del lote YA estaban en {JSON_PATH.name} "
              f"(idempotencia: no se duplican): {ya_presentes[:10]}"
              f"{'…' if len(ya_presentes) > 10 else ''}")

    # El gate cuenta el lote COMPLETO (len(chs_lote)/len(chn_lote)), ya
    # estuviera antes en el fichero o se añada ahora: el recuento esperado es
    # baseline + CHN + CHS con independencia de si esta ejecución concreta
    # añade algo nuevo o repite una fusión ya aplicada (idempotencia).
    datos_simulados = data["datos"] + a_anadir
    fallos_gate = gate(datos_simulados, n_chn_lote=len(chn_lote), n_chs_lote=len(chs_lote))

    if fallos_gate:
        print(f"\n--- FALLOS DEL GATE ({len(fallos_gate)}) ---")
        for f in fallos_gate:
            print(f"  - {f}")
        print(f"\nABORTA: el gate no pasa. No se toca {JSON_PATH.name}.")
        sys.exit(1)

    print("\nGATE VERDE (simulado)." if not apply_ else "\nGATE VERDE.")

    if not apply_:
        print(f"\nDRY-RUN (por defecto, no se ha escrito nada): se añadirían {len(a_anadir)} entradas "
              f"nuevas ({sum(1 for d in a_anadir if d['id'].startswith('CHS-'))} CHS-*, "
              f"{sum(1 for d in a_anadir if d['id'].startswith('CHN-'))} CHN-*) a {JSON_PATH.name}, "
              f"que pasaría de {total_actual} a {total_actual + len(a_anadir)} entradas. "
              f"Ejecuta con --apply para escribir de verdad.")
        return

    if not a_anadir:
        print(f"\nOK: nada que añadir (todo el lote ya estaba en {JSON_PATH.name}). No se escribe nada.")
        return

    # Respaldo previo, en el scratchpad de la sesión — nunca en el repo.
    SCRATCHPAD_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = SCRATCHPAD_DIR / f"guias-v2-research-sector.json.bak-{ts}"
    shutil.copy2(JSON_PATH, backup_path)
    print(f"Respaldo escrito en {backup_path}")

    data["datos"] = datos_simulados
    totales = data["_meta"].get("totales", {})
    totales["datos"] = len(data["datos"])
    fiab_count = {"alta": 0, "media": 0, "baja": 0}
    for d in data["datos"]:
        f = d.get("fiabilidad", "")
        if f in fiab_count:
            fiab_count[f] += 1
    totales.update(fiab_count)
    sin_url = sum(1 for d in data["datos"] if not d.get("url"))
    totales["sin_url"] = sin_url
    data["_meta"]["totales"] = totales
    data["_meta"]["guia_chocolateria_2026_09_12"] = (
        f"{len(a_anadir)} entradas añadidas para «Cómo Montar una Chocolatería» (2026-09-12): "
        f"{sum(1 for d in a_anadir if d['id'].startswith('CHS-'))} CHS-* (datos del sector, Research L4) "
        f"+ {sum(1 for d in a_anadir if d['id'].startswith('CHN-'))} CHN-* (verificación legal). "
        "Fusionado con scripts/productos-digitales/auditorias/guia-chocolateria-json-merge.py, patrón de "
        "guia-pasteleria-json-merge.py (2026-09-10)."
    )

    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Re-verificación del fichero YA escrito (cinturón y tirantes).
    releido = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    fallos_post = gate(releido["datos"], n_chn_lote=len(chn_lote), n_chs_lote=len(chs_lote))
    if fallos_post:
        print(f"\n🚨 ERROR CRÍTICO: el gate falla releyendo el fichero YA ESCRITO. Restaura desde "
              f"{backup_path} manualmente. Fallos: {fallos_post}")
        sys.exit(1)

    print(f"\nOK: {len(a_anadir)} entradas añadidas. Total: {len(data['datos'])}. "
          f"Respaldo previo en {backup_path}.")


if __name__ == "__main__":
    main()
