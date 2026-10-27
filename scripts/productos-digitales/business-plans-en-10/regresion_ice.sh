#!/bin/bash
# Regresión de los 8 conjuntos EN publicados con la rama `ice` en mapas.py (paso 1a de la heladería, 27-oct-2026,
# sesión Claude Code). Clon de /tmp/regresion-piz.sh (pizza, 25-oct) + el conjunto `piz` (bp8, con su calculadora).
# Por conjunto: `mapas` (0 errores) + `aplicar_en --dry-run` + `ensamblar_docx --salida` en $OUT y sha256 CANÓNICO
# (canon.py: miembros del zip sin las fechas de core.xml) frente a astro-site/public/dl/. Corre en el VPS:
#     bash scripts/productos-digitales/business-plans-en-10/regresion_ice.sh [/root/wt-icecream]
PY=/root/venv-guias/bin/python
R=${1:-/root/wt-icecream}
P=$R/scripts/productos-digitales
DL=$R/astro-site/public/dl
OUT=/root/tmp-icen/regresion
CANON=$P/business-plans-en-10/canon.py
rm -rf $OUT; mkdir -p $OUT
unset PIZ_FUENTE_ES ICE_FUENTE_ES
N_IGUAL=0; N_DIST=0
res() { echo "  $1 → rc=$2 · $(grep -v -i "deprecat\|utcnow\|^\s*$" $3 | tail -1 | cut -c1-150)"; }
run() { local n=$1; shift; "$@" > $OUT/$n.txt 2>&1; res "$n" $? $OUT/$n.txt; }
cmp_dir() {  # $1 = carpeta dry-run (con subcarpetas <slug>/)
  for d in $1/*/; do s=$(basename $d); for f in $d*.xlsx $d*.docx; do [ -f "$f" ] || continue
    if $PY $CANON "$f" "$DL/$s/$(basename $f)" | sed 's/^/    /'; [ ${PIPESTATUS[0]} -eq 0 ]; then N_IGUAL=$((N_IGUAL+1)); else N_DIST=$((N_DIST+1)); fi
  done; done; }
for par in "ftcaf mapas.py business-plans-en ft,caf" "bp2 bp2.py business-plans-en-2 rest,pan" "bp3 bp3.py business-plans-en-3 bar" "bp4 bp4.py business-plans-en-4 cat" "bp5 bp5.py business-plans-en-5 mbar" "bp6 bp6.py business-plans-en-6 bbq" "bp7 bp7.py business-plans-en-7 pael" "bp8 bp8.py business-plans-en-8 piz"; do
  set -- $par; b=$1; dir=$3; planes=$4
  cd $P/$dir; echo "== $b"
  if [ "$b" = "ftcaf" ]; then
    run $b-mapas $PY mapas.py
    run $b-aplicar $PY aplicar_en.py --dry-run --salida $OUT/$b
  else
    run $b-mapas $PY $b.py mapas
    run $b-aplicar $PY $b.py aplicar_en --dry-run --salida $OUT/$b
  fi
  if [ "$b" = "ftcaf" ]; then CJ=ftcaf; else CJ=$(grep -o "BP_CONJUNTO'\] = '[a-z]*'" $b.py | grep -o "'[a-z]*'$" | tr -d "'"); fi
  for pl in ${planes//,/ }; do
    rel=$(cd $P/business-plans-en && BP_CONJUNTO=$CJ $PY -c "import mapas; print(mapas.PLANES['$pl']['slug'] + '/' + mapas.DOCX['$pl'][1])")
    if [ "$b" = "ftcaf" ]; then run $b-docx-$pl $PY ensamblar_docx.py --plan $pl --salida $OUT/$b/$rel
    else run $b-docx-$pl $PY $b.py ensamblar_docx --plan $pl --salida $OUT/$b/$rel; fi
  done
  if [ "$b" = "bp8" ]; then run bp8-calculadora $PY bp8.py calculadora --salida $OUT/bp8/pizza-shop-business-plan; fi
  cmp_dir $OUT/$b
done
echo "== regresión: $N_IGUAL IGUAL · $N_DIST DISTINTO"
cd $R && echo "== git status (VPS)" && git status --short | head -20
[ $N_DIST -eq 0 ]
