#!/bin/bash
# Gates Fase 3 pSEO ciudades (76 URLs, ES only). Solo curl — red, no CPU.
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin
cd "$(dirname "$0")"
STAGING="https://aichef-astro-staging.netlify.app"
OUT=gates-fase3-results.txt
TSV=gates-fase3-76.tsv
: > "$OUT"; : > "$TSV"

# 1) Esperar deploy: el hub debe responder 200 (max 25 min)
echo "== ESPERA DEPLOY ==" >> "$OUT"
deadline=$((SECONDS + 1500))
while true; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$STAGING/seo-restaurantes-por-ciudad")
  echo "$(date '+%H:%M:%S') hub -> $code" >> "$OUT"
  [ "$code" = "200" ] && break
  [ $SECONDS -ge $deadline ] && { echo "TIMEOUT deploy (último: $code)" >> "$OUT"; echo "GATES: TIMEOUT-DEPLOY"; exit 1; }
  sleep 60
done
sleep 30

# 2) Barrido completo con checks profundos en las 76
check_one() {
  path="$1"
  html=$(curl -s --max-time 30 -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "https://aichef-astro-staging.netlify.app$path")
  tlen=$(echo "$html" | grep -o '<title>[^<]*</title>' | head -1 | wc -c | tr -d ' ')
  desc=$(echo "$html" | grep -o 'name="description" content="[^"]*"' | head -1 | wc -c | tr -d ' ')
  canon="NO"; echo "$html" | grep -q "rel=\"canonical\" href=\"https://aichef.pro$path\"" && canon="SI"
  h1=$(echo "$html" | grep -o '<h1' | wc -l | tr -d ' ')
  faq=$(echo "$html" | grep -o '"FAQPage"' | wc -l | tr -d ' ')
  svc=$(echo "$html" | grep -o '"Service"' | wc -l | tr -d ' ')
  col=$(echo "$html" | grep -o '"CollectionPage"' | wc -l | tr -d ' ')
  bre=$(echo "$html" | grep -o '"BreadcrumbList"' | wc -l | tr -d ' ')
  hre=$(echo "$html" | grep -o 'hreflang="[^"]*"' | wc -l | tr -d ' ')
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$path" "$tlen" "$desc" "$canon" "$h1" "$faq" "$svc" "$col" "$bre" "$hre"
}
export -f check_one
xargs -P4 -I{} bash -c 'check_one "{}"' < expected-city-urls.txt >> "$TSV"

# 3) Resumen. Esperado: hub → FAQ 0, Service 0, CollectionPage ≥1; ciudad → FAQ ≥1, Service ≥1; todas → Breadcrumb ≥1, hreflang=2 (es+x-default), canonical SI, H1=1
{
echo "== RESUMEN =="
echo "filas: $(wc -l < "$TSV" | tr -d ' ')"
echo "sin title: $(awk -F'\t' '$2<20' "$TSV" | wc -l | tr -d ' ')"
echo "sin description: $(awk -F'\t' '$3<30' "$TSV" | wc -l | tr -d ' ')"
echo "canonical mal: $(awk -F'\t' '$4!="SI"' "$TSV" | wc -l | tr -d ' ')"
echo "H1 != 1: $(awk -F'\t' '$5!=1' "$TSV" | wc -l | tr -d ' ')"
echo "ciudad sin FAQPage: $(awk -F'\t' '$1!="/seo-restaurantes-por-ciudad" && $6<1' "$TSV" | wc -l | tr -d ' ')"
echo "ciudad sin Service: $(awk -F'\t' '$1!="/seo-restaurantes-por-ciudad" && $7<1' "$TSV" | wc -l | tr -d ' ')"
echo "hub sin CollectionPage: $(awk -F'\t' '$1=="/seo-restaurantes-por-ciudad" && $8<1' "$TSV" | wc -l | tr -d ' ')"
echo "sin BreadcrumbList: $(awk -F'\t' '$9<1' "$TSV" | wc -l | tr -d ' ')"
echo "hreflang != 2: $(awk -F'\t' '$10!=2' "$TSV" | wc -l | tr -d ' ')"
echo "-- detalle de fallos:"
awk -F'\t' '$2<20 || $3<30 || $4!="SI" || $5!=1 || ($1!="/seo-restaurantes-por-ciudad" && ($6<1 || $7<1)) || ($1=="/seo-restaurantes-por-ciudad" && $8<1) || $9<1 || $10!=2 {print}' "$TSV"
echo "(fin detalle)"
} >> "$OUT"
cat "$OUT" | tail -15
fails=$(awk -F'\t' '$2<20 || $3<30 || $4!="SI" || $5!=1 || ($1!="/seo-restaurantes-por-ciudad" && ($6<1 || $7<1)) || ($1=="/seo-restaurantes-por-ciudad" && $8<1) || $9<1 || $10!=2 {print}' "$TSV" | wc -l | tr -d ' ')
rows=$(wc -l < "$TSV" | tr -d ' ')
if [ "$rows" = "76" ] && [ "$fails" = "0" ]; then echo "GATES FASE 3: TODO VERDE (76/76)"; exit 0; else echo "GATES FASE 3: FALLOS ($fails fallos, $rows filas)"; exit 1; fi
