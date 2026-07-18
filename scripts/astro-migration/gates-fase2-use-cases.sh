#!/bin/bash
# Gates Fase 2 use cases contra staging. Ligero: solo curl (red, no CPU).
cd "$(dirname "$0")"
STAGING="https://aichef-astro-staging.netlify.app"
LIST="expected-use-case-urls.txt"
OUT="gates-fase2-results.txt"

# 1) Esperar deploy: /usos debe pasar de 404 a 200 (max 25 min)
echo "== FASE ESPERA DEPLOY ==" > "$OUT"
deadline=$((SECONDS + 1500))
while true; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$STAGING/usos")
  echo "$(date '+%H:%M:%S') /usos -> $code" >> "$OUT"
  [ "$code" = "200" ] && break
  if [ $SECONDS -ge $deadline ]; then
    echo "TIMEOUT: deploy no publicado en 25 min (último código: $code)" >> "$OUT"
    echo "GATES: TIMEOUT-DEPLOY"; exit 1
  fi
  sleep 60
done
# margen para que el CDN sirva todo el deploy nuevo
sleep 30

# 2) Barrido de las 441 URLs (HEAD, concurrencia 4)
echo "== BARRIDO 441 URLs ==" >> "$OUT"
sed "s|https://aichef.pro|$STAGING|" "$LIST" | \
  xargs -P4 -I{} sh -c 'printf "%s %s\n" "$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "{}")" "{}"' > "$OUT.sweep" 2>/dev/null
total=$(wc -l < "$OUT.sweep" | tr -d ' ')
oks=$(grep -c '^200 ' "$OUT.sweep")
echo "total=$total ok200=$oks" >> "$OUT"
grep -v '^200 ' "$OUT.sweep" >> "$OUT" || echo "(cero no-200)" >> "$OUT"

# 3) Gates profundos en muestra: hub por idioma + consultor hub DE + 1 spoke por idioma
echo "== GATES PROFUNDOS (title/canonical/hreflang) ==" >> "$OUT"
SAMPLE=$(python3 - <<'EOF'
hubs = {'es':'/usos','en':'/en/use-cases','fr':'/fr/cas-d-usage','de':'/de/anwendungsfaelle','it':'/it/casi-uso','pt':'/pt/casos-uso','nl':'/nl/use-cases'}
lines = [l.strip() for l in open('/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/19ce60d0-4f5b-4b86-955f-4286dc1bbdc0/scratchpad/expected-use-case-urls.txt')]
out = []
for lang, hub in hubs.items():
    out.append('https://aichef.pro' + hub)
    spokes = [l for l in lines if l != 'https://aichef.pro'+hub and l.startswith('https://aichef.pro'+hub+'/') and l.count('/') >= 5]
    if spokes: out.append(spokes[len(spokes)//2])
print('\n'.join(dict.fromkeys(out)))
EOF
)
fail=0
while IFS= read -r prod; do
  url=$(echo "$prod" | sed "s|https://aichef.pro|$STAGING|")
  html=$(curl -s --max-time 25 "$url")
  title=$(echo "$html" | grep -o '<title>[^<]*</title>' | head -1)
  canon=$(echo "$html" | grep -o '<link[^>]*canonical[^>]*>' | head -1)
  nhl=$(echo "$html" | grep -c 'hreflang=')
  echo "$prod | $title | $canon | hreflang=$nhl" >> "$OUT"
  [ -z "$title" ] && { echo "  ^ SIN TITLE" >> "$OUT"; fail=1; }
  echo "$canon" | grep -q "\"$prod\"" || { echo "  ^ CANONICAL NO COINCIDE (esperado $prod)" >> "$OUT"; fail=1; }
done <<< "$SAMPLE"

if [ "$oks" = "441" ] && [ "$fail" = "0" ]; then
  echo "GATES: TODO VERDE (441/441 + muestra profunda OK)"; exit 0
else
  echo "GATES: FALLOS — ok200=$oks/441 fail_profundo=$fail (ver $OUT)"; exit 1
fi
