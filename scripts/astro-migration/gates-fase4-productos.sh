#!/bin/bash
# GATE DE ACEPTACIÓN FASE 4 — 44 landings + hub. Criterio del plan: checkouts con los MISMOS payment links + QA enlaces 44/44.
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin
cd "$(dirname "$0")"
STAGING="https://aichef-astro-staging.netlify.app"
OUT=gates-f4-final-results.txt
: > "$OUT"

# 0) mapa slug -> env var -> link para los 44 (data dirs + one-offs)
python3 - <<'EOF' > f4-expected.tsv
import json, re, glob, os
env = json.load(open('stripe-env-vars.json'))
rows = {}
for d in ['tareas','kits','guias','planes']:
    for f in glob.glob(f'/Users/johnguerrero/chefpro-modernize/astro-site/src/data/productos/{d}/*.ts'):
        if f.endswith('types.ts'): continue
        slug = os.path.basename(f)[:-3]
        m = re.search(r'(VITE_STRIPE_PAYMENT_LINK[A-Z_0-9]*)', open(f).read())
        rows[slug] = m.group(1) if m else 'NO-VAR'
for slug, paths in [('pro-prompts-ebook', ['/Users/johnguerrero/chefpro-modernize/astro-site/src/pages/pro-prompts-ebook.astro','/Users/johnguerrero/chefpro-modernize/astro-site/src/components/pages/ProPromptsEbookPage.astro']),
                    ('mega-pack-tareas', ['/Users/johnguerrero/chefpro-modernize/astro-site/src/pages/mega-pack-tareas.astro','/Users/johnguerrero/chefpro-modernize/astro-site/src/components/pages/MegaPackTareasPage.astro'])]:
    key='NO-VAR'
    for p in paths:
        if os.path.exists(p):
            m = re.search(r'(VITE_STRIPE_PAYMENT_LINK[A-Z_0-9]*)', open(p).read())
            if m: key=m.group(1); break
    rows[slug]=key
for slug in sorted(rows):
    key = rows[slug]
    link = env.get(key, {}).get('value', 'NO-LINK')
    print(f"{slug}\t{key}\t{link}")
EOF
n=$(wc -l < f4-expected.tsv | tr -d ' ')
echo "mapa: $n productos (esperado 44)" >> "$OUT"

# 1) esperar deploy (hub nuevo)
deadline=$((SECONDS + 1500))
while true; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$STAGING/productos-digitales")
  echo "$(date '+%H:%M:%S') /productos-digitales -> $code" >> "$OUT"
  [ "$code" = "200" ] && break
  [ $SECONDS -ge $deadline ] && { echo "GATE FASE 4: TIMEOUT-DEPLOY"; exit 1; }
  sleep 60
done
sleep 30

# 2) las 44 landings: 200 + CTA con link exacto
fail=0
while IFS=$'\t' read -r slug key link; do
  html=$(curl -s --max-time 30 -A "Mozilla/5.0 (compatible; Googlebot/2.1)" "$STAGING/$slug")
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$STAGING/$slug")
  ctas=$(echo "$html" | grep -o "href=\"$link\"" | wc -l | tr -d ' ')
  tlen=$(echo "$html" | grep -o '<title>[^<]*</title>' | head -1 | wc -c | tr -d ' ')
  st="OK"
  [ "$code" != "200" ] && st="FAIL-HTTP($code)"
  [ "$tlen" -lt 20 ] && st="$st SIN-TITLE"
  if [ "$link" = "NO-LINK" ] || [ "$ctas" -lt 1 ]; then st="$st CTA($key=$ctas)"; fi
  [ "$st" != "OK" ] && fail=$((fail+1))
  echo "[$st] /$slug ctas=$ctas" >> "$OUT"
done < f4-expected.tsv

# 3) hub: 200 + los 44 href presentes + title/canonical
hub=$(curl -s --max-time 30 -A "Mozilla/5.0 (compatible; Googlebot/2.1)" "$STAGING/productos-digitales")
misslinks=0
while IFS=$'\t' read -r slug key link; do
  echo "$hub" | grep -q "href=\"/$slug\"" || { echo "HUB SIN LINK a /$slug" >> "$OUT"; misslinks=$((misslinks+1)); }
done < f4-expected.tsv
hubtitle=$(echo "$hub" | grep -o '<title>[^<]*</title>' | head -1)
hubcanon="NO"; echo "$hub" | grep -q 'rel="canonical" href="https://aichef.pro/productos-digitales"' && hubcanon="SI"
echo "HUB: links faltantes=$misslinks title='$hubtitle' canonical=$hubcanon" >> "$OUT"
[ "$misslinks" != "0" ] && fail=$((fail+1))
[ "$hubcanon" != "SI" ] && fail=$((fail+1))

grep -c '^\[OK\]' "$OUT" >> "$OUT"
tail -8 "$OUT"
oks=$(grep -c '^\[OK\]' "$OUT")
if [ "$n" = "44" ] && [ "$fail" = "0" ]; then echo "GATE ACEPTACIÓN FASE 4: TODO VERDE (44/44 + hub 44 links)"; else echo "GATE FASE 4: $fail FALLOS (oks=$oks/$n)"; exit 1; fi
