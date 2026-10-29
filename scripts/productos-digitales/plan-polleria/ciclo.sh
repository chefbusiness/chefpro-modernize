#!/bin/bash
# ciclo.sh — semilla + motor (dry-run) de la Pollería y Asador de Pollos ES 1.0 en el VPS. Uso: bash ciclo.sh [--sin-demos]
# Siempre con --origen (sin él, main.py aborta: la calculadora de dl/ no casa con ninguna firma, F1-camino §1).
# Salida: $SCR/dryrun/plan-negocio-polleria/ (los 2 xlsx) y $SCR/inf.json. Sesión Claude Code, 29-oct-2026 (copia de plan-taqueria/ciclo.sh).
set -u
SCR=${CLAUDE_SCRATCHPAD:-/root/tmp-pol-f2/motor}
AQUI=$(cd "$(dirname "$0")" && pwd)
PY=/root/venv-guias/bin/python
mkdir -p "$SCR"
cd "$AQUI" && $PY semilla_pol.py --salida "$SCR/origen" || exit 2
cd "$AQUI/../planes-v2_0" && CLAUDE_SCRATCHPAD=$SCR timeout 900 $PY "$AQUI/main_pol.py" --producto plan-negocio-polleria \
  --dry-run --origen "$SCR/origen" --solo a --json "$SCR/inf.json" "$@" > "$SCR/run.log" 2>&1
echo "main.py exit $?"
