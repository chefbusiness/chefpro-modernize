# Rotisserie Chicken Restaurant Business Plan Kit (EN) — F2 (entregables) · notas
> Sesión Claude Code, 29-oct-2026, implementador único (opus). Fuente: `../plan-polleria/F1-camino.md` §6-§7 + US §n.
> Rama `feat/rotisserie-chicken-business-plan-en` (sobre `8c34fa09`); xlsx/docx en el VPS (`/root/wt-rotisserie-en`, `/root/tmp-rot-en/`).
## 1. Conjunto «pol» (libro ES = semilla de la taquería LIVE con la rotación apagada → código y diccionario del Taco EN)
Cambio común: `elif CONJUNTO == 'pol'` en `business-plans-en/mapas.py` + alta G9 (`censo-entregables.py` `PRODUCTOS_LETTER`, `postprocess-transversal.py` `EXCLUIDOS`). FUENTE ES fija (`SHA_ES` `c8d54739…` · `c2db78d3…` · `cd12837f…` = `plan-polleria/REVISION-FINAL.md`), sin paso 1c.

| Fichero | Qué lleva |
|---|---|
| `mapas_pol.py` | Producto §6, `POLP`/`POLC`, pestañas (F3 «Phase 3 - Rotisserie & Health», F5 «Phase 5 - Menu & Pre-Orders»), 80 tareas 12/15/14/13/13/13, parches E2 (G14) / E4 (Staffing!C12) / E5 (G11), versión A51/A11, D19 de 12 filas, docx 131 (`pol_a`/`pol_b`), diccionario en cadena (§2.1), `SHA_TAQ` + `SHA_PIZ` (22 OK), G4 (`—` → ☐), `TERMINOS_PE` |
| `datos_pol.py` | FIJOS (inversión, P&L, puestos, títulos, fases 2/3/5), 7 POR_CELDA, caso US (126 valores), 110 tokens, notas del docx (61; §9 = 102-108, UK en 108), pistas, glosario US §9, `cifras_prohibidas()` + `RX_POL_NO` |
| `bp13.py` · `derivar_formulas_pol.py` · `formulas_pol_manual.py` | Lanzador · 16 fórmulas EN: 11 derivadas del Taco EN (gemela 1.ª) + 5 manuales (C9, D27, D37, F13, Break-Even A26; ≤ 255 car.) |
| `calibracion_pol` · `barrido_pol` · `resumen_entregables` · `volcar_en` · `anotar_tandas_docx` · `check_revision` · `canon` · `regresion_pol.sh` | Clones del Taco EN (palancas de US §8; regresión de los 12 conjuntos publicados) |
| `BRIEF-TRADUCTORES.md` | 4 tandas, glosario US §9 entero, bloque legal US, cinco corrientes US, encaje de las tareas, validación (§5) |
## 2. Decisiones que se apartan de §6 o lo concretan
1. **Diccionario: el Taco EN va PRIMERO** (por celda → por texto → por texto con «pedido» → «comensal») y luego la cadena de
   la Pizza EN (celda, texto) → Bakery → Bar → BP. El camino solo nombraba la Pizza EN; la pollería ES sale de la
   taquería, así que el Taco EN (revisado hoy) cubre 334 GM + 130 GR/GRC. Lo casado por alias (18 rótulos «Pedidos…» →
   «Covers…») va SIEMPRE a revisión (GR). `RX_REESCRIBIR` + vocabulario y cifras del taco.
2. **Nombres de fichero**: `rotisserie-chicken-restaurant-{financial-projections,startup-checklist}.xlsx` (el «…» de §6 =
   la raíz del slug, = Taco); US §9 decía `rotisserie-chicken-…`. **Calculadora**: `rotisserie-chicken-yield-costing-calculator.xlsx` (§6).
3. **Inversión 19 → 18** con la clase de la fila ES: signage en la obra (8 = $53,000); «electrical, HVAC, plumbing, gas
   & grease» partido en 10 ($11,000) y 11 ($13,000); freidoras + fogones = 14 ($7,000); estación de salsas y tinas con el
   utillaje (18, $7,500); nevera de bebida + hielo sacados de la línea de frío a la 19 (botellero ES, $3,000; 16 = $6,500);
   la 15 (campana ES) = walk-in $12,800 (pista «OJO»). Imprevistos por fórmula **$11,600** (no $9,800: la base 7-11 incluye
   arquitecto y rótulo, = Taco).
4. **Fijos 10 → 9** ($26,000): pest control en DDD ($900); permit renewals ($1,100) con «waste, grease & used-oil» ($2,400,
   fila 31 ES). **Plantilla** en la fila ES de su función: camarero ES → counter, packing & expo (4 × 0.4); refuerzo de
   fin de semana → fry & line (0.5); suplencias → prep & relief rotisserie cook (1.0, cubre los descansos con 7 días) =
   10 personas, 6.60 FTE, $20,531/mes; cobertura 10.5 h × 2.75 + 3 h × 1.5 → **101.1 %**; B14/B15 $5,000 (= Taco).
5. **Sin `Break-Even!B25` ni nota E25** (rotación apagada = ES); `B62` = `H11` = **17 %** (US §8). POR_CELDA (7): H4, F11, A62, C62, C63, O5 (enero con los pesos US), Staffing A29.
6. Gate: `HECHOS_US = {50000}` (el tope de los SBA Microloans coincide con los 50.000 € de propios ES: GM c0552, GR c0055);
   FRASES_OTROS SIN «360 days» del Bar (aquí se abre 360). Vetados además «pollo asado» (salvo mexicano/negado), «poultry
   shop», «roaster», «yucca», «PERi-PERi», «Broaster», «chicken shop» fuera de UK, Australia, «Spanish», 63/75 °C.
7. Cierre del Word: Food Cost · HACCP · Restaurant Checklists Kit Pro · Food Truck Business Plan Kit (no hay guía de
   restaurante peruano ni checklists de pollería en la tienda EN). Australia fuera del Word (solo la FAQ de la landing).
## 3. Caso US y D15 (dry-run `/root/tmp-rot-en/dry`, `cifras_caso.json` 110 tokens) — **VERDE en la vuelta 0, sin palancas**
Préstamo de punto fijo **$216,000** (semilla 208,500 → 216,000 → 216,000) · ventas **$819,000** / $868,140 / $902,866 (130 ×
$17.50 × 360) · CAPEX $237,832 + fondo $97,876 = **$335,708** · propios $120,000 · cuota $35,153 · margen tras variables
60.2 % · COGS 28.0 % · personal 33.1 % (6.60 FTE) · alquiler 5.5 % · EBITDA $123,379 · **neto 7.1 % / 8.9 % / 10.0 %**
($57,946 → $90,465) · equilibrio 110 / 107 covers · **holgura 21.8 %** · **DSCR mín 2.96×** · saldo mín $103,822 (Mes 1) ·
payback 2.8 · pesimista $644,325, −$27,945 · optimista $1,004,550, +$189,018 · 5 umbrales en verde los 3 años. `CALIBRACION_D15` vacía.
## 4. Gates (VPS, sobre el dry-run con GM/GR/GRC aplicadas)
| Comprobación | Resultado |
|---|---|
| `bp13.py mapas` + `verificar` (Mac y VPS) | 0 errores (97 fijos, 16 fórmulas EN, 126 valores, 110 tokens); 22 sha256 Taco/Pizza OK; 8 avisos (pistas de 3 celdas GM/GR, 5 FIJOS comunes sin uso) |
| `extraer_textos` · `extraer_docx` | 855 cadenas: GM 357 · GR 35 · GRC 113 · GPOL-plan 118 · GPOL-check 109 · GX 123 · 80 tareas · docx 131 (61 ranuras: 29 + 32); único ERROR = A4 del Word ES (sale Letter, = Taco) |
| `aplicar_en --dry-run --parcial --idempotencia` | 0 diferencias · inject_cache 701 + 12, 0 fallos de pycel |
| `gates_en --parcial --solo G1,G3,G4,G5,G6` | **TODO VERDE** (736 fórmulas · 80 tareas · 16 hojas Letter · 234 bajo DV · 0 dif. de caché) |
| `barrido --parcial` | 1,259 piezas, 0 fallos (pendientes en ES = las de las tandas) |
| Inyección en `check_textos` (16 defectos) | caza los 16 (pollo asado, yucca, 63 °C, taco, PERi-PERi, Broaster, roaster, poultry shop, Australia, 77 covers, 15.80, 115 covers, chicken shop, gluten-free, pedido, kg) |
| `regresion_pol.sh` (12 conjuntos) | **48/48 IGUAL** (sha256 canónico), todos rc 0 |
## 5. Calculadora EN (`calculadora_pol.py`): ESPECIFICADA, no hecha (presupuesto) → un sonnet aparte
= `../plan-polleria/calculadora_pol_es.py` traducida con el patrón de `../business-plans-en-12/calculadora_taq.py` (mismas
filas, helpers, `inject_cache`, autotest con `calcular()`; versión de `mapas`; Letter; `--salida` + autotest). Hojas
`Chicken Yield` · `Rotisserie` · `Costing` · `Instructions`; lb y oz (constante gris «16 oz per lb»), $/lb, °F, «your
county's rules» en el hot holding. Por defecto (US §4/§8, Kit estimate): pollo 3.0 lb WOG a $1.75/lb + marinado $0.45 + 5 %
de merma de display = **$5.99**; cooked yield 0.72 (70-75 %); 2 rotisseries × 8 spits × 6 = 96 por carga (48 cada una),
75-90 min por carga + carga/descarga, primera carga 9:00; domingo 65-70 y días punta 120-150 frente a la capacidad; gas
177,500 BTU/h por rotisserie × $/therm verde (Kit, «check your gas bill»). Costing: whole $19.00 · half + 2 sides $17.50 ·
quarter + 2 sides $13.00 · family meal $34.00 (≈ 29.6 %) · sandwich/bowl $13.50 · sides (yuca fries 0.9 lb × $2.75, rice &
beans $0.90, salad $0.60, maduros, salchipapas), aji verde 2 oz $0.25, Inca Kola/soda $3.25; sales tax en carta 0 %,
comisión 25 %, margen por canal (dine-in · pickup & pre-orders · marketplace). EXPUESTOS EN: BIRDS_PER_LOAD,
SUNDAY_CAPACITY, COOKED_YIELD, COST_PER_BIRD, FAMILY_MEAL_FC. Autotest = el ES + `RX_POL_NO`, cifras prohibidas y no
latinos. **Tras generarla**: cruzar Instructions D19 filas 38-39 y el Word ($5.99, 70-75 %, ≈ 30 %) con su caché (lección m1).
## 6. Tandas de traducción y lo que va después (comandos de cada traductor: `BRIEF-TRADUCTORES.md` §5)
- **Tanda 1** (a) `GPOL-plan` (118 · 3,859 palabras + 35 GR) → `textos_en/GPOL-plan.json` + `GR.revision.json` ‖ (b)
  `GPOL-check` (109 · 2,879 + 113 GRC) → `textos_en/GPOL-check.json` + `GRC.revision.json`.
- Mac: `B=scripts/productos-digitales/business-plans-en-13; python3 $B/bp13.py preparar_tandas && python3
  $B/anotar_tandas_docx.py && python3 $B/bp13.py check_textos --todas` (los ids de pol_a/pol_b no cambian).
- **Tanda 2** (c) `pol_a` (29 · 3,319) → `docx_en_pol_a.json` ‖ (d) `pol_b` (32 · 4,564) → `docx_en_pol_b.json`.
- VPS (tras `scp` de `textos_en/*.json` y `docx_en_pol_{a,b}.json`; `PY=/root/venv-guias/bin/python`,
  `D=/root/wt-rotisserie-en/astro-site/public/dl/rotisserie-chicken-restaurant-business-plan`, en `business-plans-en-13/`):
  `bp13.py mapas` → `aplicar_en --idempotencia --json /tmp/pol-real.json` → `calibracion /tmp/pol-real.json` →
  `ensamblar_docx --plan pol` → `calculadora --salida $D` (genera + autotest) → `gates_en` (+ `--autotest`) →
  `ensamblar_docx --autotest --dir /tmp/pol-docx-at` → `barrido` → `resumen_entregables.py` → `../censo-entregables.py --fail
  --letter --only rotisserie-chicken-restaurant-business-plan` + `../gate-no-latinos.py --only …` → `bash regresion_pol.sh`
  → `volcar_en.py` → revisión opus + 1 ronda (`<g>.revision.json`, tokens `_xl`) → 2.ª pasada `canon.py` → `scp` de vuelta.
**Estado** (cierre F2): tandas 1-2 hechas, calculadora generada, paso real §6 y revisión cerrados (§7). Pendiente: F3 (web).
## 7. Paso real y revisión final (VPS, 29-oct; detalle en `REVISION-FINAL.md`)
- **Primer paso real**: todo verde salvo **G8/barrido ROJOS** por falsos positivos del gate: `\$27\b` (Bar EN) casaba con
  «$27,945» y había empujado a escribir «27,500 to 35,950 US dollars»; «1 therm = 100,000 BTU» casaba con los $100,000 del
  Taco EN. Arreglo en `datos_pol.py` (solo este conjunto): `(?![.,]\d)` en `$27`/`$36` y `EXCEPCION_CIFRA` (BTU/therm).
- **Revisión (una ronda)**: 0 B · 3 M · 6 m, todos arreglados en fuente: pestañas inexistentes en el Word/checklist
  («Bird Cost», «Rotisserie Loads» → `Chicken Yield`, `Rotisserie`); TPHC (a las 4 h se tira, nunca se enfría; el SOP del
  plan es hot holding ≥ 135 °F con límite propio de 4 h); «Inca Kola» → genérico (vetada en `RX_POL_NO`); 42.5 + 42.5 + 15;
  dos puestos en ¶43; 22 % del sandwich/bowl; «Sunday lunch peak»; cantidad neta en la etiqueta. Cifras del caso intactas.
- **Gates finales**: G1-G9 TODO VERDE · D15 VERDE · autotests 20/20 y 8/8 · calculadora VERDE · barrido 1,708 piezas 0
  fallos · censo `--letter` 0 · no latinos 0 · regresión 48/48 IGUAL · 2.ª pasada `canon.py` 4/4 IGUAL · sha256 Mac = VPS.
- **Para la landing (nombres exactos)**: `rotisserie-chicken-restaurant-business-plan.docx` ·
  `rotisserie-chicken-restaurant-financial-projections.xlsx` · `rotisserie-chicken-restaurant-startup-checklist.xlsx` ·
  `rotisserie-chicken-yield-costing-calculator.xlsx` (pestañas `Chicken Yield` · `Rotisserie` · `Costing` · `Instructions`;
  nombre visible «Rotisserie Chicken Yield & Costing Calculator»).
- Lección: ante un falso positivo de un gate se arregla el regex, no el texto (el traductor cambia el formato para esquivarlo).
