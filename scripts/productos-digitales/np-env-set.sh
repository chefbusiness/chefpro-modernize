#!/usr/bin/env bash
# np-env-set.sh — sube una clave de NOWPayments a Netlify como variable SECRETA
# leyéndola de un fichero 600, sin que pase por el chat ni por los logs.
#   scripts/productos-digitales/np-env-set.sh NOWPAYMENTS_API_KEY ~/.config/nowpayments/api-key deploy-preview
#   scripts/productos-digitales/np-env-set.sh NOWPAYMENTS_IPN_SECRET ~/.config/nowpayments/ipn-secret production
# Recuerda: tras cambiar una env var el REDEPLOY es obligatorio (build en la nube).
set -euo pipefail
VAR="${1:?nombre de la variable}"; FILE="${2:?fichero 600 con la clave}"; CTX="${3:?contexto: production|deploy-preview|branch-deploy}"
SITE="${AICP_SITE_ID:-ee5802cf-34bb-4354-90d9-aa9f628b4038}"
export PATH="$HOME/Library/pnpm:$PATH"
[ -s "$FILE" ] || { echo "np-env-set: no existe $FILE" >&2; exit 2; }
VAL="$(tr -d '\r\n ' < "$FILE")"
[ ${#VAL} -ge 10 ] || { echo "np-env-set: valor sospechosamente corto (${#VAL})" >&2; exit 2; }
# Netlify no permite fijar contexto y scope a la vez sobre una variable que YA
# existe («Setting the context and scope at the same time on an existing env
# var is not allowed»): si existe, se conserva su scope y solo se pone el valor
# del contexto; si es nueva, se declara con scope functions.
if netlify env:list --json --site "$SITE" 2>/dev/null | grep -q "\"$VAR\""; then
  netlify env:set "$VAR" "$VAL" --secret --context "$CTX" --site "$SITE" >/dev/null
  echo "✓ $VAR (existente) actualizada como secreta en contexto $CTX (site $SITE), ${#VAL} caracteres. Redeploy pendiente."
else
  netlify env:set "$VAR" "$VAL" --secret --context "$CTX" --scope functions --site "$SITE" >/dev/null
  echo "✓ $VAR creada como secreta en contexto $CTX (site $SITE, scope functions), ${#VAL} caracteres. Redeploy pendiente."
fi
