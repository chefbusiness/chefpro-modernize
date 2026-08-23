#!/usr/bin/env bash
# Ejecución REAL del post-proceso v2 de la familia «Kit de Tareas» sobre
# astro-site/public/dl/<pid>/, kit a kit y EN SERIE (regla térmica del Mac).
#
#   scripts/productos-digitales/kit-tareas-aplicar-real.sh <pid> [<pid> ...]
#
# Por cada kit: guardia térmica → main.py con KIT_TAREAS_APPLY=1 (respaldo en el
# scratchpad, informe JSON en auditorias/kit-tareas-hermanos/<pid>-real.json) →
# censo-entregables.py --only <pid> --fail → gate-flujo-postpago.py --offline
# --only <pid>. Para al PRIMER fallo (set -e) y deja el respaldo localizado en
# el informe. NO hace git add/commit: eso lo hace el orquestador tras revisar.
set -euo pipefail
REPO=/Users/johnguerrero/chefpro-modernize
PKG=$REPO/scripts/productos-digitales/kit-tareas-v2_0
VER=$REPO/scripts/productos-digitales/auditorias/kit-tareas-hermanos
SCR=${CLAUDE_SCRATCHPAD:-/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/7340312f-b4fe-4aa1-b254-4b0c17c8375f/scratchpad}
MAX_TEMP=${MAX_TEMP:-58}

esperar_frio() {
  for _ in $(seq 1 40); do
    t=$(istats cpu temp --value-only 2>/dev/null | tr -d ' '); t=${t%%.*}
    if [ "${t:-99}" -lt "$MAX_TEMP" ]; then echo "  · CPU ${t} °C"; return 0; fi
    echo "  · CPU ${t} °C ≥ ${MAX_TEMP}: espero 30 s"; sleep 30
  done
  echo "CPU no baja de ${MAX_TEMP} °C tras 20 min: abortando" >&2; exit 3
}

[ $# -ge 1 ] || { echo "uso: $0 <pid> [<pid> ...]" >&2; exit 2; }
cd "$REPO"
for pid in "$@"; do
  echo "=================== $pid ==================="
  [ -d "astro-site/public/dl/$pid" ] || { echo "no existe dl/$pid" >&2; exit 2; }
  esperar_frio
  KIT_TAREAS_APPLY=1 CLAUDE_SCRATCHPAD="$SCR" python3 "$PKG/main.py" --producto "$pid" --json "$VER/$pid-real.json"
  esperar_frio
  python3 scripts/productos-digitales/censo-entregables.py --only "$pid" --fail --quiet
  esperar_frio
  python3 scripts/productos-digitales/gate-flujo-postpago.py --offline --only "$pid"
  echo "OK $pid · $(git status --porcelain "astro-site/public/dl/$pid" | wc -l | tr -d ' ') ficheros cambiados"
done
echo "TODO OK: $*"
