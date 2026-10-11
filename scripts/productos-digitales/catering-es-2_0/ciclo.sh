#!/bin/bash
# ciclo.sh — semilla + motor (dry-run) del Catering ES 2.0 en el VPS. Uso: bash ciclo.sh [--sin-demos]
# Salida: $SCR/dryrun/plan-catering-tematico-eventos/ (los 2 xlsx) y $SCR/inf.json. Sesión Claude Code, 11-oct-2026.
set -u
SCR=${CLAUDE_SCRATCHPAD:-/root/tmp-cates-f2}
AQUI=$(cd "$(dirname "$0")" && pwd)
PY=/root/venv-guias/bin/python
cd "$AQUI" && $PY semilla_cat.py --salida "$SCR/origen" || exit 2
cd "$AQUI/../planes-v2_0" && CLAUDE_SCRATCHPAD=$SCR timeout 900 $PY main.py --producto plan-catering-tematico-eventos \
  --dry-run --origen "$SCR/origen" --solo a --json "$SCR/inf.json" "$@" > "$SCR/run.log" 2>&1
echo "main.py exit $?"
