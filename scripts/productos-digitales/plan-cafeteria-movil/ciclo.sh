#!/bin/bash
# ciclo.sh — semilla + motor (dry-run) de la Cafetería Móvil para Eventos ES 1.0 en el VPS. Uso: bash ciclo.sh [--sin-demos]
# Salida: $SCR/dryrun/plan-negocio-cafeteria-movil-eventos/ (los 2 xlsx) y $SCR/inf.json. Sesión Claude Code, 28-oct-2026
# (copia de plan-pizzeria/ciclo.sh). La tabla de escalado de Instrucciones sale de datos_escalado.py (fuente única, la
# escribe el agente de la calculadora): sin ella el libro saldría sin la tabla, así que se para.
set -u
SCR=${CLAUDE_SCRATCHPAD:-/root/tmp-caf-f2/motor}
AQUI=$(cd "$(dirname "$0")" && pwd)
PY=/root/venv-guias/bin/python
mkdir -p "$SCR"
[ -f "$AQUI/datos_escalado.py" ] || { echo "falta datos_escalado.py (tabla de escalado, SPEC D13)"; exit 3; }
cd "$AQUI" && $PY semilla_caf.py --salida "$SCR/origen" || exit 2
cd "$AQUI/../planes-v2_0" && CLAUDE_SCRATCHPAD=$SCR timeout 900 $PY "$AQUI/main_caf.py" --producto plan-negocio-cafeteria-movil-eventos \
  --dry-run --origen "$SCR/origen" --solo a --json "$SCR/inf.json" "$@" > "$SCR/run.log" 2>&1
echo "main.py exit $?"
