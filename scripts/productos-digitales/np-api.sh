#!/usr/bin/env bash
# np-api.sh — llamadas a la API de NOWPayments leyendo la clave de un fichero 600.
# La clave NUNCA se imprime ni pasa por argumentos: va a curl por un fichero de
# configuración temporal (-K) que se borra al salir. Uso:
#   scripts/productos-digitales/np-api.sh GET 'estimate?amount=12&currency_from=eur&currency_to=usdttrc20'
#   scripts/productos-digitales/np-api.sh POST invoice '{"price_amount":12,...}'
# Ficheros: ~/.config/nowpayments/api-key (producción) o NP_KEY_FILE=... (p. ej. sandbox).
# Base: NP_API_BASE (default https://api.nowpayments.io/v1).
set -euo pipefail
KEYFILE="${NP_KEY_FILE:-$HOME/.config/nowpayments/api-key}"
BASE="${NP_API_BASE:-https://api.nowpayments.io/v1}"
METHOD="${1:?GET|POST}"; PATH_="${2:?ruta}"; BODY="${3:-}"
[ -s "$KEYFILE" ] || { echo "np-api: no existe $KEYFILE" >&2; exit 2; }
CFG="$(mktemp)"; trap 'rm -f "$CFG"' EXIT; chmod 600 "$CFG"
printf 'header = "x-api-key: %s"\n' "$(tr -d '\r\n ' < "$KEYFILE")" > "$CFG"
if [ "$METHOD" = POST ]; then
  curl -sS -m 30 -K "$CFG" -H 'Content-Type: application/json' -X POST --data "$BODY" -w '\n[http %{http_code}]\n' "$BASE/$PATH_"
else
  curl -sS -m 30 -K "$CFG" -w '\n[http %{http_code}]\n' "$BASE/$PATH_"
fi
