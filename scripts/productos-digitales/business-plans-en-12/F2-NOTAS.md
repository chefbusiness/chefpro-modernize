# Taco Shop Business Plan Kit (EN) — F2 (entregables) · notas
> Sesión Claude Code, 29-oct-2026, implementador único (opus). Fuente: `../plan-taqueria/F1-camino.md` §6-§7 + US §n.
> Rama `feat/taco-shop-business-plan-en` (sobre `f5c5b269`); xlsx/docx en el VPS (`/root/wt-taco-en`, `/root/tmp-taco-en/`).
## 1. Conjunto «taq» (libro ES = MISMA rejilla que la pizzería → código de la Pizza EN con el circuito de la heladería)
Cambio común: `elif CONJUNTO == 'taq'` en `business-plans-en/mapas.py` + alta G9 (`censo-entregables.py`
`PRODUCTOS_LETTER`, `postprocess-transversal.py` `EXCLUIDOS`). Medido: ES taquería = rejilla de la ES pizzería salvo 4
fórmulas de texto (C50, D27, D37, F13). FUENTE ES fija (`SHA_ES` `5778011f…` · `27b6962c…` · `c028c2bb…`), sin paso 1c.

| Fichero | Qué lleva |
|---|---|
| `mapas_taq.py` | Producto §6, `TAQP`/`TAQC`, pestañas (F2 «Phase 2 - Hood, Gas & Permits»), 80 tareas 12/15/14/13/13/13, parches **E2 (G14), E4 (Staffing!C12), E5 (G11)**, versión A51/A11, D19, docx 131 (tandas `taq_a`/`taq_b`), diccionario en cadena Pizza EN por celda → por texto → Bakery → Bar → BP (`SHA_PIZ`, 10 OK), GR/GRC, G4 (`—` → ☐), `TERMINOS_MX` |
| `datos_taq.py` | FIJOS (inversión, P&L, puestos, títulos), 9 POR_CELDA, caso US (126 valores, Mes 1 = enero con los pesos de US §8), 109 tokens, notas del docx (61; §9 = 102-108, UK en 108), pistas, glosario US §9, `cifras_prohibidas()` + `RX_TAQ_NO` |
| `bp12.py` · `derivar_formulas_taq.py` · `formulas_taq_manual.py` | Lanzador (+ `calculadora` → `calculadora_taq.py`) · 17 fórmulas EN: 13 derivadas de la Pizza EN + 4 manuales (≤ 255 car.), 0 pendientes |
| `calibracion_taq` · `barrido_taq` · `resumen_entregables` · `volcar_en` · `anotar_tandas_docx` · `check_revision` · `canon` · `regresion_taq.sh` | Clones de la heladería (palancas de US §8; regresión de los 11 conjuntos publicados) |
| `BRIEF-TRADUCTORES.md` | 4 tandas, glosario US §9 entero, bloque legal US, encaje de las 80 tareas, validación (§5) |

Sin `inventario_delta.py`: no hay paso 1c y la rejilla se midió celda a celda.
## 2. Decisiones que se apartan de §6 o lo concretan
1. **Fijos 10 → 9**: el ES trae fila propia de DDD (la pizza no): pest control en ESA fila ($900) y las permit renewals
   ($1,100) con «Waste, grease & used-oil hauling» ($3,500, fila ES de terraza y residuos). Total $25,000.
2. **Inversión 19 → 18 en la fila ES más parecida**: signage dentro de la obra (8 = $42,000); «electrical… & grease» partido
   en 10 ($9,000) y 11 ($11,000); freidora + fogón + steam table + warmers = fila 14 ES ($6,500); prensas con el utillaje
   (18, $6,500); beer cooler sacado de la línea de la salsa bar a la barra ES (19, $2,000; 16 = $6,500). Solo la 15 (campana
   ES) cambia de objeto: walk-in $12,800 (pista «OJO» al traductor). Imprevistos por fórmula $9,600 (no $8,000: la base 7-11
   incluye arquitecto y rótulo, como Pizza).
3. **`Break-Even!B25` = 5** (US §8 decía 3): el caso vende 3.8 covers por plaza (casi la mitad, take-out/delivery) y el
   equilibrio de caja pide 3.2 → con 3 el libro diría que el equilibrio no cabe en el local. Pista en E25.
4. Cobertura (10.5 h × 2.5 + 2.5 h × 1.5) y suplencias 0.1 FTE $270 → **100.1 %**; B14/B15 $5,000 (= Pizza); umbrales
   P&L 60 / 30 / 36 / 10 / 5 % (el 60 % es el margen tras TODOS los variables).
5. Tabla D19 de 12 filas (el ES no tiene la 47): versión en A51; **A39 por POR_CELDA** (su ES es el rótulo de la partida
   12, un FIJO); la fila 46 (convenio ES) pasa a «Al pastor cook temperature: set by your county».
6. POR_CELDA (9): H4, F11, A62, C62, C63 (sales tax, = Pizza), O5 (enero con pesos US), Staffing A29 (counter service:
   propinas del equipo), Instructions A39. A34 sale del Bar EN (GM, mismo ES).
7. Detector de español: «al pastor», «pico de gallo», «Cinco de Mayo»… se retiran como los topónimos US (`TERMINOS_MX`,
   solo este conjunto); «consomé» a la lista blanca; «con todo», «de la casa»… siguen cazados.
8. Cierre del Word: Food Cost · HACCP · Restaurant Checklists Kit Pro · Food Truck Business Plan Kit (no hay Taco Checklists EN).
## 3. Caso US y D15 (dry-run `/root/tmp-taco-en/dry`, `cifras_caso.json` 109 tokens) — **VERDE en la vuelta 0, sin palancas**
Préstamo de punto fijo **$176,000** (semilla 170,000 → 176,000 → 176,000) · ventas **$619,850** / $657,041 / $683,323 (115 ×
$17.50 × 308) · CAPEX $197,600 + fondo $78,012 = **$275,612** · propios $100,000 · cuota $28,643 · margen tras variables
62.0 % · COGS 26.2 % · personal 34.6 % (5.02 FTE) · alquiler 5.4 % · EBITDA $89,858 · **neto 6.3 % / 8.1 % / 9.2 %** ($39,009 →
$62,763) · equilibrio 100 / 97 covers · **holgura 18.9 %** · **DSCR mín 2.68×** · saldo mín $79,892 · cobertura 100.1 % ·
pesimista $499,950, −$22,326, caja $64,889 (no se agota) · optimista $750,360, +$132,928 · umbrales en verde los 3 años.
`CALIBRACION_D15` vacía.
## 4. Gates (VPS, sobre el dry-run)
| Comprobación | Resultado |
|---|---|
| `bp12.py mapas` + `verificar` | 0 errores (95 fijos, 17 fórmulas EN, 127 valores, 109 tokens); 10 sha256 Pizza OK; solo avisos |
| `extraer_textos` · `extraer_docx` | 861 cadenas: GM 361 · GR 34 · GRC 102 · GTAQ-plan 119 · GTAQ-check 124 · GX 121 · 80 tareas · docx 131 (61 ranuras: 29 + 32), único ERROR = A4 del Word ES (el ensamblador pasa a Letter, = Pizza) |
| `aplicar_en --dry-run --parcial --idempotencia` | 0 diferencias · inject_cache 741 + 12, 0 fallos de pycel |
| `gates_en --parcial --solo G1,G3,G4,G5,G6,G7` | **TODO VERDE**: G1 (741 fórmulas · 80 tareas) · G3 (16 hojas Letter) · G4 (235 bajo DV) · G5 · G6 (0 dif.) · G7 |
| `barrido --parcial` · `check_textos` GM/GR/GRC · `check_revision` | 1,270 piezas, 0 fallos · OK los 3 · OK |
| Inyección en `check_textos` (12 defectos) | caza los 12 (authentic, 77 covers, 15.50, dough, mezcal, gluten-free, servers, IVA, °C, Tex-Mex, 358,050, «con todo», 12 % of sales); «145 °F» como regla única no es regex: lo vigilan brief y revisión |
| `regresion_taq.sh` (11 conjuntos) | **44/44 ficheros IGUAL** (sha256 canónico), rc 0 |
## 5. Calculadora EN (`calculadora_taq.py`): ESPECIFICADA, no hecha (presupuesto) → un sonnet aparte
= `../plan-taqueria/calculadora_taq_es.py` traducida con el patrón de `../business-plans-en-8/calculadora_piz.py` (mismas
hojas, filas, helpers, `inject_cache`, autotest; versión de `mapas`): `Trompo Yield` · `Tortillas` · `Taco Costing` ·
`Instructions`; cono en lb, porción en oz con constante gris «16 oz per lb», $/lb, Letter. Por defecto (US §4, Kit
estimate): cono 30 lb, adobo 8 %, pork shoulder $3.00/lb, merma 35 % + recortes 5 %, 1.5 oz por taco (≈ 208 tacos); campo
verde «Your county's cook temp (°F)» vacío («145 or 155 °F: ask in writing»); Mission 6 in 360/caja $58.99 frente a masa
harina + prensa + 0.75 FTE $27,450 + máquina $7,808 / 7 años, 308 días, 650 al día (equilibrio ≈ 660); doble tortilla de
6 in, street taco $4.00, gringa $11.50, sales tax en carta 0 %, comisión 25 %, margen por canal. Autotest = el ES +
`RX_TAQ_NO`, cifras prohibidas y no latinos. `bp12.py calculadora --salida $D [--autotest]`.
## 6. Tandas de traducción y lo que va después (comandos de cada traductor: `BRIEF-TRADUCTORES.md` §5)
- **Tanda 1** (a) `GTAQ-plan` (119 · 3,522 palabras + 34 GR) → `textos_en/GTAQ-plan.json` + `GR.revision.json` ‖ (b)
  `GTAQ-check` (124 · 2,703 + 102 GRC) → `textos_en/GTAQ-check.json` + `GRC.revision.json`.
- Mac: `B=scripts/productos-digitales/business-plans-en-12; python3 $B/bp12.py preparar_tandas && python3
  $B/anotar_tandas_docx.py && python3 $B/bp12.py check_textos --todas` (los ids de taq_a/taq_b no cambian).
- **Tanda 2** (c) `taq_a` (29 · 3,295) → `docx_en_taq_a.json` ‖ (d) `taq_b` (32 · 4,012) → `docx_en_taq_b.json`.
- VPS (tras `scp` de los JSON; `PY=/root/venv-guias/bin/python`, `D=…/dl/taco-shop-business-plan`, en `business-plans-en-12/`):
  `bp12.py mapas` → `aplicar_en --idempotencia --json /tmp/taq-real.json` → `calibracion /tmp/taq-real.json` →
  `ensamblar_docx --plan taq` → `calculadora --salida $D` (+ `--autotest`) → `gates_en` (+ `--autotest`) →
  `ensamblar_docx --autotest --dir /tmp/taq-docx-at` → `barrido` → `resumen_entregables.py` → `censo-entregables.py --fail
  --letter --only taco-shop-business-plan` + `gate-no-latinos.py --only …` → `regresion_taq.sh` → `volcar_en.py` → revisión
  opus + 1 ronda → 2.ª pasada con `canon.py` → `scp` de vuelta.
## 7. Estado
Cerrado: clones, caso US, D15 verde, tandas 1 y 2 preparadas (taq_a/taq_b anotadas con las cifras finales), regresión
44/44. G7 rojo en la 1.ª corrida solo por faltar este fichero (= heladería §4.1).
**29-oct (cierre F2, sesión Claude Code):** 4 tandas y calculadora hechas; paso real §6 en el VPS TODO VERDE; revisión
adversarial única (`REVISION-FINAL.md`): 0 B · 5 M · 8 m, los 13 arreglados en una ronda (GM/GRC por `<g>.revision.json`,
tokens `cogs_pct_xl`/`plantilla_jornadas_xl` con el redondeo que muestra Excel, docx a/b, GTAQ-plan/check, calculadora);
gates re-pasados verdes, 2.ª pasada `canon.py` 4/4 IGUAL, regresión 44/44, 4 entregables en `dl/` con sha256 Mac = VPS.
Ojo: `calculadora --salida $D --autotest` SOLO prueba el fichero existente; para regenerarlo, `calculadora --salida $D` (que
ya corre el autotest). Pendiente: F3 (capa EN: landing, catálogo, Stripe, correo).
