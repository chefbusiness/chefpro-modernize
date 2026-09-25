# Restaurant Inventory Kit Pro — F2 (entregables) · notas de cierre

> Sesión Claude Code, 25-sep-2026. SPEC §7 pasos 4-6 y §8 (G1-G8). Implementador único, sin subagentes (tamaño S).
> Entradas: `textos_en/*.json` (revisados, ver `F2-REVISION.md`), `mercado_en.json` (+ `validar_mercado.py`),
> `mapas.py`, `censo_es.json`, `textos_es.json`. Fuente ES en solo lectura: `astro-site/public/dl/kit-inventario/`
> (sin tocar: `git status` limpio en esa carpeta). Sin commit ni push (lo decide el orquestador).

## 1. Qué se ha construido

| Pieza | Qué es |
|---|---|
| `aplicar_en.py` | Copia adaptada de `recipe-costing-kit/aplicar_en.py`. Maquinaria genérica del piloto (guarda térmica, renombrado de hojas + reescritura de referencias, literales en fórmulas/CF/DV, traducción por celda, «€» fuera y fechas a numFmtId 14, US Letter + pie D19, docProps D21, apóstrofos rectos, huella de idempotencia, `inject_cache` al final) + funciones de mercado PROPIAS: `mercado_libros` (D14/D15, celda a celda), `mercado_fechas_hoy` (D25, 19 `=TODAY()±k`), `mercado_vaciar` + `mercado_03` (D11), `mercado_04` (D12), textos D20 por celda. `--dry-run` escribe en `$CLAUDE_SCRATCHPAD/rik-dryrun` (o `--salida`); sin flag escribe en `astro-site/public/dl/restaurant-inventory-templates/`. `--idempotencia` construye un clon y exige 0 diferencias |
| `gates_en.py` | G1-G8 de SPEC §8 contra `censo_es.json` y los xlsx ES (ningún recuento a mano). Una línea de veredicto por gate, exit 1 si algo falla. `--autotest` inyecta 9 defectos en copias temporales (G1 ×2, G2 ×2, G3, G4, G5, G6, G7) y exige que cada gate caze el suyo |
| `astro-site/public/dl/restaurant-inventory-templates/` | Los 9 xlsx EN (tabla §5) |
| `postprocess-transversal.py` | `restaurant-inventory-templates` añadido a `EXCLUIDOS` (un `all` le forzaría A4 y español) |
| `censo-entregables.py` | `restaurant-inventory-templates` añadido a `PRODUCTOS_LETTER` (exige Letter; «Instructions» es hoja de texto) |
| `textos_en/G02.json`, `textos_en/G03.json` | 3 arreglos de texto pequeños y justificados (§4) |

## 2. Cómo regenerar (en serie, `istats cpu temp | head -1` antes de cada script; esperar si ≥ 63 °C)

```bash
cd /Users/johnguerrero/chefpro-modernize
python3 scripts/productos-digitales/restaurant-inventory-kit/mapas.py              # autotest de mapas: 0 errores
python3 scripts/productos-digitales/restaurant-inventory-kit/validar_mercado.py    # mercado_en.json: 0 fallos
# opcional, ensayo en el scratchpad:
python3 scripts/productos-digitales/restaurant-inventory-kit/aplicar_en.py --dry-run --idempotencia
python3 scripts/productos-digitales/restaurant-inventory-kit/gates_en.py --dir "$CLAUDE_SCRATCHPAD/rik-dryrun"
# construcción real (inject_cache va dentro, AL FINAL; no guardar los xlsx después con openpyxl):
python3 scripts/productos-digitales/restaurant-inventory-kit/aplicar_en.py --idempotencia [--mes October]
python3 scripts/productos-digitales/restaurant-inventory-kit/gates_en.py
python3 scripts/productos-digitales/restaurant-inventory-kit/gates_en.py --autotest
python3 scripts/productos-digitales/censo-entregables.py --only restaurant-inventory-templates --fail
python3 scripts/productos-digitales/gate-no-latinos.py --only restaurant-inventory-templates
```

`--mes`: la línea de versión D21 lleva el mes de la construcción («Version 2.0 · September 2026 · …»). Si F3
publica en octubre, reconstruir con `--mes October` y volver a pasar los gates (`gates_en.py --mes October`).
La construcción tarda ~21 s (con idempotencia); CPU a 41-47 °C durante toda la sesión.

## 3. Resultados de los gates (construcción real, 25-sep)

```
$ python3 scripts/productos-digitales/restaurant-inventory-kit/gates_en.py
G1 paridad estructural   OK  areas_impresion=29 · autofiltros=1 · cf=31 · columnas_ocultas=6 · desbloqueadas=5982 · dv=35 · dv_celdas=1332 · dv_cita_hoja=2
G2 restos                OK  cabecera-pie=38 · docprops=63 · dv=172 · formato=3238 · hoja=38 · importes_usd_en_texto=11 · literal=7116 · styles.xml=21
G3 formato               OK  fechas_censo=522 · fechas_d25=19 · hojas=38 · pies=38 · versiones=9
G4 claves                OK  celdas_categoria=200 · dv_categorias=12 · familias=15 · hojas_dv_unidades=9 · valores_con_dv=319 · zonas=11
G5 CF y literales        OK  comodines=17 · literales_cf_expresion=1 · literales_con_dv=3 · tokens_cf=28
G6 cálculo               OK  food_cost_07=0.3101 · con_valor=449 · formulas=1945 · historia_04=4 · vacias_legitimas=1496
G7 identidades           OK  validar_mercado: 9 comprobaciones en verde · b09=8 · celdas_mercado=1149 · d20=13 · maestra_01=50
G8 censo-entregables     OK  censo-entregables.py --only restaurant-inventory-templates --fail
VERDE: 8 gates, 0 fallos

$ python3 …/gates_en.py --autotest          → 9/9 CAZADO · AUTOTEST: OK
$ python3 …/aplicar_en.py --idempotencia    → diferencias 1.ª vs 2.ª construcción: 0 · inject_cache fallos_pycel=0 en los 9
$ python3 scripts/productos-digitales/censo-entregables.py --only restaurant-inventory-templates --fail
  TOTAL: n=9 form=1945 f_sinCache=0 box=0 bio=0 noA4=0 creator≠AICP=0 nonlat=0 emptyStr=0 err=0 → OK: 0 defectos (--fail)
$ python3 scripts/productos-digitales/gate-no-latinos.py --only restaurant-inventory-templates
  9 ficheros escaneados · 0 con no-latinos · 0 caracteres (exit 0)
```

Lectura de G1: 1.926 fórmulas del ES idénticas tras los mapas + 19 de D25 = 1.945; 365 fórmulas con referencia a
hoja; 35 DV (33 literales, 2 que citan hoja; la de D11 cambia de lista a decimal 0-100); 31 CF; 60 merges; 29 hojas
protegidas sin contraseña; 29 áreas y 28 títulos de impresión; 1 autofiltro; 6 columnas ocultas; 5.979 + 3 (D11)
celdas desbloqueadas, todas verdes. Caché con valor: EN = ES en 7 libros y +6 (02) / +13 (06) = las 19 de D25.

G6 al día de la construcción: 04 ACCEPT / REJECT (too warm) / ACCEPT / N/A; 07 food cost 31,0 % (objetivo 32 %,
🟢 OK); 06 los cinco estados (EXPIRED, CHECK, URGENT, USE SOON ×2, OK). La caché de `TODAY()` es la del día de
`inject_cache`; Excel recalcula al abrir y, como las fechas son relativas, los cinco estados se mantienen cualquier día.

## 4. Desviaciones de la SPEC (y por qué)

1. **IDs internos en los títulos de mensaje de DV.** El ES publicado trae prefijos de auditoría en `promptTitle`
   («grupo_b · …», «kitinv-v2 · …», «kitinv-a/-c · …») y `textos_en` los conservaba. `aplicar_en.py` los quita
   (`RX_ID_DV`) y G2 los busca: mismo criterio que I1 («RT-08:», D23). **Propuesta para el ES v2.x: quitarlos también.**
2. **8 cadenas sin letras** (el extractor las excluye, así que no estaban en `textos_es.json`) llevaban convención
   española: `2-5 €` y `0,7 (70 %)` (B09 `Parameters!B4/B12`) y las 6 ventanas de reparto de 24 h de 02
   `Vendor Terms!G4:G9`. Se fijan en `aplicar_en.SIN_LETRAS` («2-5 (in your currency)», «0.7 (70%)», «7:00-9:00 a.m.»…).
   G2 detecta ahora coma decimal y horas de 24 h.
3. **«Nota» con dos sentidos**: en 02 es la nota A/B/C/D del proveedor («Grade») y en 03 `Tax Rates!C1` una columna
   de notas. `aplicar_en.POR_CELDA` fija «Note» en esa celda (comprueba el ES antes de escribir).
4. **Arreglos de texto en `textos_en`** (3, pequeños): G02 `c0535` (04 `Receiving Temps!A20` citaba «Min temp.» /
   «Max temp.»; ahora cita las cabeceras reales «Min. acceptable temp. (°F)» / «Max. acceptable temp. (°F)»); G02 `c0320`
   (03 Instructions: faltaba la guía D11 US/UK — «resale certificate (0 %)… UK VAT 0/5/20 %… Check with your
   accountant»); G03 `c0645` (06 Instructions decía «the 8 product templates»: es I2 → «the 7 templates that list products»).
5. **D11, mensajes de la DV `H9:H38`**: el mensaje de error heredado («Choose a value from the list») no vale para una
   DV decimal; se sustituye por uno propio (0-100, sin %). La nota «type the rates you actually pay» se escribe en
   `Current Order!A49` (nota del desglose), que es donde el usuario ve las tres celdas 0/5/20.
6. **`Receiving Temps!E4:E18`**: sale de `mapas.FAMILIAS[...][4]`, que lleva etiquetas de trazabilidad
   (`[fuente]`, `[estimado]`) y fragmentos en español («límite físico», «»»). `limpiar_etiquetas()` deja solo la cita
   en inglés (p. ej. «FDA Food Code 2022 §3-202.11(D); max = physical limit»). `mapas.py` no se ha tocado.
7. **G6 «pycel sin errores»**: se mide sobre la caché que escribe `inject_cache.py` (que es pycel) y el XML (`<v>` en
   toda `<f>`), no con una segunda evaluación pycel; 0 errores en las 1.945.
8. **G7 «mismo precio en los 9 libros»**: transitivo y completo — `validar_mercado.py` (C) lo exige en las celdas de
   `mercado_en.json` y G7 exige que cada una de las 1.149 celdas esté escrita tal cual en su xlsx; además 01 = tabla
   maestra fila a fila, BONUS-09 ROP = par del 01 y máx. = par max desde la caché, importes = cantidad × precio.
9. D25: desfases contra el 24-ago-2026 (no el 23), decisión ya registrada en `mercado_en.json.decisiones`.

**Abierto (heredado de `F2-REVISION.md`, no tocado):** el literal fijo de 04 es «⚠ NO LIMIT FOR THIS GROUP» y la
columna se llama «Family». Cambiarlo a «FAMILY» exige tocar `mapas.LITERALES` + `TOKENS_CF`/autotest (D10); el token
de CF «NO LIMIT» seguiría casando. Decisión de 1 línea para el orquestador; si se cambia, basta reconstruir y regatear.

## 5. Lo que necesita F3

**Ficheros** (`astro-site/public/dl/restaurant-inventory-templates/`, para `get-download-urls` y el dashboard):

| # | Fichero | Título (landing, dashboard, A1, docProps) | Pestañas | Bytes |
|---|---|---|---|---|
| 01 | `01-kitchen-bar-inventory-par-sheet.xlsx` | Kitchen & Bar Inventory Sheet with Par Levels | Instructions · Kitchen · Bar · Storeroom · Summary Dashboard | 25.781 |
| 02 | `02-vendor-list-price-comparison.xlsx` | Vendor List, Price Comparison & Scorecard | Instructions · Vendor Directory · Price Comparison · Vendor Scorecard · Vendor Terms | 20.678 |
| 03 | `03-purchase-order-template.xlsx` | Purchase Order Template & Order Log | Instructions · Current Order · Vendors · Order Log · Tax Rates | 20.782 |
| 04 | `04-receiving-log.xlsx` | Receiving Log (Temperatures & Credit Requests) | Instructions · Receiving Log · Discrepancy Log · Receiving Temps | 22.276 |
| 05 | `05-food-waste-log.xlsx` | Food Waste Log & Action Plan | Instructions · Daily Waste Log · Waste by Category · Waste Dashboard · Action Plan | 20.521 |
| 06 | `06-fifo-expiration-date-tracker.xlsx` | FIFO & Expiration Date Tracker | Instructions · FIFO Tracker · Expiration Alerts · Storage Map | 22.392 |
| 07 | `07-purchasing-cost-analysis.xlsx` | Purchasing Cost Analysis & Food Cost KPIs | Instructions · Spend by Category · Monthly Trend · Top 20 Items · KPI Dashboard | 18.975 |
| B08 | `BONUS-08-month-end-inventory-count.xlsx` | BONUS: Month-End Inventory Count | Instructions · Quick Count | 17.201 |
| B09 | `BONUS-09-reorder-point-calculator.xlsx` | BONUS: Reorder Point & Order Quantity Calculator | Instructions · Reorder Calculator · Parameters | 15.831 |

Total 184.437 bytes (≈ 180 KB). Los tamaños cambian unos bytes en cada reconstrucción (fechas de guardado).

**Datos para la landing (todos verificables en los xlsx):**
- **9 plantillas Excel** (7 + 2 bonus), **38 pestañas** (9 de instrucciones + 29 de trabajo), 1.945 fórmulas con valor
  cacheado (se ven también en visores que no recalculan), 35 desplegables, 31 formatos condicionales (semáforos).
- **Verde = lo que escribes**: 5.982 celdas editables, el resto protegido **sin contraseña** (Review → Unprotect Sheet).
- **Una sola taxonomía**: las mismas 10 categorías en las 9 plantillas y la misma lista de 16 unidades
  (lb, oz, kg, gal, qt, L, each, dozen, case, tray, keg, bag, roll, pack, bottle, can) en las **7** que llevan producto
  (I2: nunca «8»). Los análisis del 01, 05 y 07 agregan por ese texto.
- **Datos de ejemplo US**: 50 productos (cocina 20, barra 15, almacén 15) con unidad US, precio de referencia y par
  levels; BONUS-09 calibrado para que el punto de pedido = par level del 01 y el stock máx. = par max. 6 proveedores
  «(sample)» (teléfonos 555-01xx, correos `.example`). «Sample prices are illustrative U.S. references».
- **Impuesto neutro (D11)**: tasas por categoría al 0 % editables, desglose 0/5/20 editable; sirve para sales tax US y
  VAT UK; «amounts are in your currency» (sin símbolo de moneda en las celdas).
- **Recepción en °F (D12)**: 15 familias con límites del FDA Food Code 2022 (frío TCS ≤ 41 °F, caliente ≥ 135 °F,
  shellstock y huevos ≤ 45 °F, congelado «received frozen»), veredicto automático ACCEPT / REJECT (too warm/too cold) /
  N/A, registro de incidencias con credit memo.
- **FIFO/FEFO (06)**: use-by vs best-by, fecha efectiva tras apertura, 5 estados (EXPIRED — DISCARD, CHECK, URGENT,
  USE SOON, OK) con fechas de ejemplo vivas (siempre enseña los cinco), 11 zonas de almacén con temperatura en °F.
- **KPIs (07)**: food cost por consumo (inicial + compras − final), coste por cubierto, variación, Top 20 con alerta de
  subida > 5 % y Top 5 que se ordena solo. Ejemplo coherente: 31,0 % de food cost.
- **Impresión**: US Letter en las 38 hojas, pie «AI Chef Pro · aichef.pro · Page &P of &N».
- Línea de versión en las 9 Instructions: «Version 2.0 · September 2026 · aichef.pro/en/digital-products/restaurant-inventory-templates · info@aichef.pro».

**Recordatorios F3** (SPEC §6 y §9): registrar la familia `kit-inventario` con `en.slug = restaurant-inventory-templates`
en `tienda.ts`; las 5 fuentes del backend con `lang: 'en'` y estos 9 nombres de fichero; alta en `zona-app.ts`,
`product-prices.ts` (19 USD) y las tres puertas cripto; Payment Link USD de John con redirección a
`/en/digital-products/restaurant-inventory-templates/access?session_id={CHECKOUT_SESSION_ID}`; gates LIVE.

**Resuelto por el orquestador (25-sep, noche):** el literal de estado del 04 pasa a «⚠ NO LIMIT FOR THIS FAMILY», coherente con las columnas «Family» / «Suggested Family». Cambiado en `mapas.LITERALES` y en su lista de estados, `generar_mercado.py`, `validar_mercado.py`, `textos_en/G02.json` (c0403) y `mercado_en.json` (D20 04!A8). El token de CF «NO LIMIT» no cambia. Rebuild + gates en verde.
