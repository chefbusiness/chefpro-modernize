#!/bin/bash
# ciclo.sh — semilla + motor (dry-run) del Parrillero / Asador ES 2.2 en el VPS. Uso: bash ciclo.sh [--sin-demos]
# Salida: $SCR/dryrun/plan-negocio-parrillero-asador-eventos/ (los 2 xlsx) y $SCR/inf.json. Sesión Claude Code, 12-oct-2026 (copia de paellero-2_2/ciclo.sh).
set -u
SCR=${CLAUDE_SCRATCHPAD:-/root/tmp-par-f2/motor}
AQUI=$(cd "$(dirname "$0")" && pwd)
PY=/root/venv-guias/bin/python
cd "$AQUI" && $PY semilla_par.py --salida "$SCR/origen" || exit 2
cd "$AQUI/../planes-v2_0" && CLAUDE_SCRATCHPAD=$SCR timeout 900 $PY main.py --producto plan-negocio-parrillero-asador-eventos \
  --dry-run --origen "$SCR/origen" --solo a --json "$SCR/inf.json" "$@" > "$SCR/run.log" 2>&1
echo "main.py exit $?"
