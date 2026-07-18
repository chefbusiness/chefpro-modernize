#!/bin/bash
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin
F="https://aichef.pro/.netlify/functions/verify-purchase"
R="https://aichef.pro/.netlify/functions/resend-access"

# 1) Esperar a que el deploy publique el código nuevo: producto desconocido debe devolver unknown_product
deadline=$((SECONDS + 1500))
while true; do
  body=$(curl -s --max-time 20 -X POST -H 'Content-Type: application/json' -d '{"product":"producto-inexistente-smoke-test"}' "$F")
  echo "$(date '+%H:%M:%S') verify(desconocido) -> $body"
  echo "$body" | grep -q "unknown_product" && break
  [ $SECONDS -ge $deadline ] && { echo "TIMEOUT: el deploy no publica el codigo nuevo en 25 min"; exit 1; }
  sleep 60
done

echo "--- codigo nuevo LIVE. Checks de mapa: ---"
fail=0
# 2) Producto de los 17 ahora conocido: NO debe ser unknown_product
for p in kit-tareas-asador guia-panaderia-obrador plan-negocio-bar-restaurante plan-catering-tematico-eventos; do
  body=$(curl -s --max-time 20 -X POST -H 'Content-Type: application/json' -d "{\"product\":\"$p\"}" "$F")
  if echo "$body" | grep -q "unknown_product"; then echo "FAIL verify($p): $body"; fail=1; else echo "OK verify($p): $body"; fi
done
# 3) Producto ya existente (regresión): igual que antes, no unknown
body=$(curl -s --max-time 20 -X POST -H 'Content-Type: application/json' -d '{"product":"kit-escandallos"}' "$F")
if echo "$body" | grep -q "unknown_product"; then echo "FAIL regresion kit-escandallos: $body"; fail=1; else echo "OK regresion verify(kit-escandallos): $body"; fi
# 4) resend-access endurecido: desconocido -> unknown_product; conocido de los 40 nuevos -> otro error (falta email => 400 distinto)
body=$(curl -s --max-time 20 -X POST -H 'Content-Type: application/json' -d '{"product":"producto-inexistente-smoke-test","email":"smoke@test.invalid"}' "$R")
if echo "$body" | grep -q "unknown_product"; then echo "OK resend(desconocido): $body"; else echo "FAIL resend(desconocido): $body"; fail=1; fi
body=$(curl -s --max-time 20 -X POST -H 'Content-Type: application/json' -d '{"product":"kit-tareas-asador","email":"smoke@test.invalid"}' "$R")
if echo "$body" | grep -q "unknown_product"; then echo "FAIL resend(kit-tareas-asador): $body"; fail=1; else echo "OK resend(kit-tareas-asador): $body"; fi

[ "$fail" = "0" ] && echo "SMOKE HOTFIX: TODO VERDE" || { echo "SMOKE HOTFIX: FALLOS"; exit 1; }
