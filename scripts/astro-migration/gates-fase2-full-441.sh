#!/bin/bash
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin
cd "$(dirname "$0")"
STAGING="https://aichef-astro-staging.netlify.app"
OUT=full-gates-441.tsv
: > "$OUT"

check_one() {
  path="$1"
  html=$(curl -s --max-time 30 -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "https://aichef-astro-staging.netlify.app$path")
  tlen=$(echo "$html" | grep -o '<title>[^<]*</title>' | head -1 | wc -c | tr -d ' ')
  desc=$(echo "$html" | grep -o 'name="description" content="[^"]*"' | head -1 | wc -c | tr -d ' ')
  canon="NO"; echo "$html" | grep -q "rel=\"canonical\" href=\"https://aichef.pro$path\"" && canon="SI"
  h1=$(echo "$html" | grep -o '<h1' | wc -l | tr -d ' ')
  faq=$(echo "$html" | grep -o '"FAQPage"' | wc -l | tr -d ' ')
  hre=$(echo "$html" | grep -o 'hreflang="[^"]*"' | wc -l | tr -d ' ')
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$path" "$tlen" "$desc" "$canon" "$h1" "$faq" "$hre"
}
export -f check_one

xargs -P4 -I{} bash -c 'check_one "{}"' < expected-use-case-urls.txt >> "$OUT"

echo "== RESUMEN =="
echo "filas: $(wc -l < "$OUT" | tr -d ' ')"
echo "sin title (tlen<20): $(awk -F'\t' '$2<20' "$OUT" | wc -l | tr -d ' ')"
echo "sin meta description (desc<30): $(awk -F'\t' '$3<30' "$OUT" | wc -l | tr -d ' ')"
echo "canonical mal: $(awk -F'\t' '$4!="SI"' "$OUT" | wc -l | tr -d ' ')"
echo "sin H1: $(awk -F'\t' '$5<1' "$OUT" | wc -l | tr -d ' ')"
echo "sin FAQPage: $(awk -F'\t' '$6<1' "$OUT" | wc -l | tr -d ' ')"
echo "hreflang != 8: $(awk -F'\t' '$7!=8' "$OUT" | wc -l | tr -d ' ')"
echo "-- detalle de fallos (si hay):"
awk -F'\t' '$2<20 || $3<30 || $4!="SI" || $5<1 || $6<1 || $7!=8 {print}' "$OUT" | head -30
