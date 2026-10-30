# Taco Shop Checklists Kit Pro — F2: montaje y gates (31-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-taco`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (32) +
`textos_en/G1.json` (458, un traductor sonnet, `200ba73d`) = las 490 cadenas a traducir; GM 158 por `mapas_taco.py`.
Rama con `origin/main` fusionado (PR #186: `inject_cache` trocea literales > 255). Mes de la línea de versión:
**October** (el de la F2, como los hermanos). Alta en `PRODUCTOS_LETTER` (`censo-entregables.py`) y `EXCLUIDOS`
(`postprocess-transversal.py`).

## Código común tocado (`gates_en.py`, `aa0f6206`) y regresión

- `HOJA_CAJA is None` (`SIN_CAJA`) → G5 da «libro_de_caja = ninguno (D12)»; `F09` / `H_CC` / `F_CAJA0` a `None`; el autotest
  cambia sus mutaciones de caja (G5 y G6 sobre el 09) por una de contador (G6: una tarea marcada ✓ en el 01).
- `FRASES_OK += mapas.FRASES_OK_EXTRA` (taquería: «al pastor», «tinga de pollo», con «al» / «de» funcionales ES).
- G1 compara fórmulas con `parche_xml_xlsx.fundir_literales` en los dos lados: un literal troceado («"a"&"b"») no da
  rojo falso.
- **Regresión** (`gates_en.py --kit <v> --mes October` sobre los `dl/` LIVE del base y los 10 verticales + `--autotest`
  del base y del hotel, antes y después): **13 salidas idénticas byte a byte**. Antes y después igual de verdes: base, bar,
  catering, chocolate, hotel, icecream, pastry; autotest base 16/16 y hotel 19/19. **Rojos previos, sin relación con este
  cambio** (deuda del circuito, idénticos antes y después): pizza 40, burger 36, cafe 43 y ghost 40 fallos = G4 «valor
  fijado» (los mínimos del inventario ES ya son número, `VALORES_EN` espera el texto) + G6, 8-9 en cada uno (caché ES
  vacía en el inventario y la limpieza semanal).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 taco/mapas_taco.py
    python3 aplicar_en.py --kit taco --dry-run --salida /tmp/taco-en --idempotencia --mes October
    python3 gates_en.py --kit taco --dir /tmp/taco-en --mes October [--autotest]
    cp /tmp/taco-en/*.xlsx ../../../astro-site/public/dl/taco-shop-checklist-templates/ && python3 gates_en.py --kit taco --mes October
    python3 ../censo-entregables.py --only taco-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only taco-shop-checklist-templates
    python3 ../parche_xml_xlsx.py --check ../../../astro-site/public/dl/taco-shop-checklist-templates/*.xlsx

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2); idempotencia 0 diferencias; `inject_cache` 46/46 fórmulas con caché, 0 fallos de pycel; 0 desbordes; 0 rellenos |
| Gates | **VERDE 8/0** (dry-run y publicado). G1 36 hojas · 46 fórmulas · 23 DV (428 celdas) · 23 CF · 194 merges · 25 protegidas · 3.265 desbloqueadas · 298 tareas · 36 áreas · 24 paneles · 60 nombres. G3 18 ajustes y 22 altos de fila (las tareas largas por ADAPTAR caben: Letter, sin desbordes). G4 246 horas. G5 sin caja. G6 46 contadores = ES. G7 57 °F, 10 citas normativas, 31 celdas ES con °C |
| Autotest | **16/16 CAZADOS** (los del base sin las 2 de caja + contador G6 + término prohibido) |
| censo-entregables · no-latinos · LIT255 | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos · VERDE (0 literales > 255) |
| Publicado | `astro-site/public/dl/taco-shop-checklist-templates/` (11 xlsx, 150.246 bytes), `12147364` |

## Arreglos de la F2

- G7 (2 fallos en el primer montaje, `mapas_taco.py`, `d789a9b9`): `GRADOS_F_SPEC` + 100 °F (G7 lee las cifras °F de todo
  `mapas`, también la regla base del lavamanos) y 01 «Apertura» B15 en `CELSIUS_SIN_F` (el reorden de la errata sube la
  comprobación del cono, con sus °F, a la B14; en la B15 queda el montaje).
- Ninguna traducción tocada: G1.json salió limpio en G2 (español, términos prohibidos, «[criterio del kit]»), G4 y G7.

Erratas del ES: las de `SPEC.md` §5 (orden cono / montaje del 01, gas mensual del 07 y el B02, horas fuera de orden).
