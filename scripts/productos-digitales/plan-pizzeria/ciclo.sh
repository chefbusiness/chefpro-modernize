#!/bin/bash
# ciclo.sh — semilla + motor (dry-run) de la Pizzería Napolitana ES 1.0 en el VPS. Uso: bash ciclo.sh [--sin-demos]
# Salida: $SCR/dryrun/plan-negocio-pizzeria/ (los 2 xlsx) y $SCR/inf.json. Sesión Claude Code, 25-oct-2026 (copia de plan-heladeria/ciclo.sh).
set -u
SCR=${CLAUDE_SCRATCHPAD:-/root/tmp-piz-f2/motor}
AQUI=$(cd "$(dirname "$0")" && pwd)
PY=/root/venv-guias/bin/python
mkdir -p "$SCR"
cd "$AQUI" && $PY semilla_piz.py --salida "$SCR/origen" || exit 2
cd "$AQUI/../planes-v2_0" && CLAUDE_SCRATCHPAD=$SCR timeout 900 $PY "$AQUI/main_piz.py" --producto plan-negocio-pizzeria \
  --dry-run --origen "$SCR/origen" --solo a --json "$SCR/inf.json" "$@" > "$SCR/run.log" 2>&1
echo "main.py exit $?"
