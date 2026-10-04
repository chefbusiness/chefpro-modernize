# Brief para los traductores (subagentes Sonnet) — Restaurant + Bakery Business Plan Kit (EN)

> Sesión Claude Code, 4-oct-2026. F2 de los productos 9 y 10 de la tienda EN (SPEC delta §5 paso 2). Regla 1bis: los
> textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-2/` (= `BP2/`, datos y salidas de estos dos productos) y
> `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Seis tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **(a) GN + GREST** ‖ **(b) GPAN** → después **(c) rest_a** ‖ **(d) rest_b** → **(e) pan_a** ‖ **(f) pan_b**.
> Los docx usan tokens: pueden ir en paralelo con (a)-(b) si hay hueco térmico; no necesitan las cifras.
> **GM no se traduce**: sus 391 cadenas son idénticas a las comunes de FT/CAF y su EN ya está en
> `BP2/textos_en/GM.json` (lo escribe `bp2.py preparar_tandas`).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + la sección **0** de
este fichero + la de su tanda. El subagente no hace commit y no toca nada más que su salida.

---

## 0. Lo que cambia frente al brief de FT/CAF (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP2/tandas/<TANDA>.entrada.json`; `BP2/SPEC-delta.md` (§1-§4, D30-D47);
`BP/SPEC.md` §1 (D1-D29), §2.3, §3, §4 y §6; `BP2/F1-research-us-delta.md` §3, §4, §5 y §7 y `BP/F1-research-us.md`
§3-§5 (cifras US con fuente, marco legal, caso de ejemplo); `BP/textos_en/glosario-GM.json` (glosario fijado por FT/CAF).

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-2/bp2.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves,
resultado del check y 3-5 decisiones que deban conocer las demás tandas.

**Conceptos** (D30): el **restaurante** es un *casual restaurant with a bar* (unas 60 plazas, comida y cena, barra con
cerveza, vino y cócteles; no es un bar de copas). Su volumen diario son **covers** (cubiertos) y la rotación **seat
turns**. La **panadería** es una *artisan bakery with a storefront, a small café corner and wholesale to cafés*; su
volumen son **transactions**. Lo mayorista va **dentro de la línea de pan** (no es un canal modelado aparte) y los
escenarios mueven transacciones, ticket y días, no el mix (R8). Cottage food (venta desde casa con topes) es **otro
comprador** (D39): este kit es una panadería comercial.

**Cadenas con `propuesta_en`** (62, la mayoría notas del motor y trámites comunes): son idénticas a una cadena YA
traducida para el food truck o la cafetería (`propuesta_de` dice cuál y dónde estaba). Úsala tal cual si vale para
este negocio; **adáptala** si el contexto cambia (un restaurante no tiene commissary ni camión; una panadería no tiene
brunch). Nunca la dejes en español.

**Rótulos fijados** (`fijos_en` de tu entrada, ya los escribe `mapas.py`): los títulos y pies de marca del libro del
restaurante (D34, «AI Chef Pro»), «Liquor license + permits (non-quota state example)» (fila 42 de la inversión del
restaurante, D37), «Tax-exempt share of the line (%)» (col. H del P&L de la panadería, D36), las filas de sales tax,
financiación y tesorería de FT/CAF. Si los citas, con esas mismas palabras.

**Cifras del caso ES prohibidas** (80 cubiertos, 18,20 €, 180 transacciones, 5,50 €, 3.000 €/mes, 1,8 covers por
mesa, 17.094 €, 33 %, 14 pagas, 133.000 €, 105.000 €, 350.000 €, 200.000 €…). Usa `valor_us` (el caso US de
`mapas.VALORES_EN`, research delta §7: REST 125 covers × $28 × 310 días, PAN 210 transactions × $10 × 310) o redacta
sin cifra: el caso se recalibra en la tanda de `aplicar_en.py` y una nota con cifra puede quedarse vieja.

---

## (a) Tanda GN + GREST — xlsx del restaurante (24 + 384 cadenas · ≈ 290 + 3.400 palabras; 83 celdas de tabla)

Dos ficheros: entrada `BP2/tandas/GN.entrada.json` → salida `BP2/textos_en/GN.json` (check `--tanda GN`; comunes a
restaurante y panadería: no escribas «restaurant» ni «bakery» en ellas) y `BP2/tandas/GREST.entrada.json` →
`BP2/textos_en/GREST.json` (check `--tanda GREST`).

- **Pestañas numeradas** (D33): «0. Assumptions», «1. Startup Costs», «2. 3-Year P&L», «3. Break-Even», «4. Scenarios»,
  «5. Staffing», «6. 12-Month Cash Flow», «7. Financing», «Instructions»: cítalas así, con su número.
- **`1. Startup Costs`** (rótulo US en la MISMA fila; el importe lo pone `aplicar_en.py`): 7 broker and lease review ·
  8 build-out (second-generation restaurant space) · 9 architect, MEP drawings and permits (building + health plan
  review) · 10 interior design · 15 cooking line (range + griddle) · 16 convection oven · 17 fryers · 18 refrigerated
  prep tables · 19 walk-in cooler · 20 Type I hood + UL 300 fire suppression · 21 commercial dishwasher · 22
  smallwares · 23 sinks + grease interceptor · 24 NSF shelving · 26 bar (build and install) · 27 dining tables and
  chairs · 28 bar stools · 29 espresso machine · 30 coffee grinder · 31 beer taps · 32 wine fridge · 33 glassware,
  plates and flatware · 34 POS + reservations · 35 patio furniture · 37 brand and menu design · 38 website + Google
  Business Profile · 39 grand opening campaign · 41 LLC formation and legal · 42 (fijo: liquor license) · 44 opening
  food inventory · 45 opening bar inventory. Bloques (filas 6, 14, 25, 36, 40, 43) en mayúsculas como el ES. Notas de
  la col. D sin cifras ES.
- **`2. 3-Year P&L`** fijos 27-37: accounting / bookkeeping · marketing · maintenance and repairs · software (POS,
  reservations, social) · cleaning, laundry and linens · waste and grease hauling · pest control · music licensing
  (ASCAP, BMI, SESAC) · workplace safety and training · online reservation fees · smallwares and glassware
  replacement. Comentarios de umbral: «kit benchmark (editable estimate)» (D41: margen bruto ≥ 65 %, mercancía ≤ 32 %,
  personal ≤ 35 %, alquiler ≤ 10 %, neto ≥ 5 %).
- **`5. Staffing`** filas 6-12: general manager / owner · head chef · line cooks · servers / bartenders · part-time
  servers · weekend dishwasher / extra · vacation and day-off relief. **D38**: el libro no modela propinas ni tip credit
  (servers a ≥ $15/h de base); la nota del suelo (A29) lo dice con la regla federal ($2.13/h + tip credit donde el
  estado lo permite; CA, OR, WA, AK, MN, MT y NV no lo permiten, DOL).
- **`0. Assumptions`**: B62 alcohol = share of beverage sales (70 % en el ejemplo); C63 (si tiene nota): algunos estados
  y ciudades suman un impuesto por consumición al sales tax → tipo COMBINADO (D37). B51 seats; «rotaciones» = seat
  turns.
- **Tablas de Instructions celda a celda**: D18 filas 34-45 y D19 49-58 (pistas P de cada celda, como FT/CAF). En D19:
  fila 56 → «Liquor license (state + local)» · «from $50 to $300,000+» · webstaurantstore.com · nota de estado sin
  cupo / con cupo; fila 57 → «Prime cost (food + labor)» · «60-65% of sales» · restaurant365.com (I10: las tasas de
  cierre del ES no tienen fuente); fila 58 → salario mínimo federal + estatal (DOL). El resto con research delta §4
  (food cost 25-35 %, labor 25-33 %, inversión $175,000-$400,000 o mediana $375,000 con su fuente).
- **Checklist de una hoja** (`Opening Checklist`, D35): 7 fases como filas-cabecera (A4, A15, A24, A33, A41, A50, A66:
  «PHASE 1: …» con el título US de la fase) y 64 tareas; **col. A = categoría** (Legal, Tax, Payroll, Premises,
  Permits, Build-out, Equipment, Food safety, HR, Brand, Digital, Launch, Insurance, Privacy, Operations, Finance,
  Marketing); B trámite, C responsable, D plazo US, F notas. Equivalencias de SPEC delta §3 + §4.2 heredada (pistas P):
  LLC y articles of organization; architect + MEP drawings y permisos con inspecciones; zoning → certificate of
  occupancy; Type I hood + UL 300 + grease interceptor + fire marshal; health plan review → food establishment permit;
  sidewalk café permit; **liquor license** (state ABC + local, cupo, responsible beverage service, age signage); food
  donation (Bill Emerson); new-employer registration y carteles; Indeed, Culinary Agents, Poached. La fila B52 (hojas
  de reclamaciones) ya está fijada («Consumer advisory and allergen notice on the menu»): traduce su nota de la col.
  F a juego. La col. OK usa **✓, —, N/A** (D35): el mensaje de la DV y las instrucciones lo dicen así.

## (b) Tanda GPAN — xlsx de la panadería (385 cadenas · ≈ 5.100 palabras; 120 celdas de tabla)

Entrada `BP2/tandas/GPAN.entrada.json` → salida `BP2/textos_en/GPAN.json` (check `--tanda GPAN`). Lee antes
`BP2/textos_en/GN.json` si ya existe.

- **`Startup Costs`** filas 7-25: 7 LLC formation and legal · 8 licenses and health plan review · 9 architect and
  permit drawings · 10 build-out · 11 electrical service upgrade for the ovens (sin «kW» españoles: «three-phase
  service, check with your utility») · 12 oven ventilation and exhaust · 13 deck / rack oven · 14 spiral mixer · 15
  divider-rounder · 16 proofer / retarder · 17 walk-in cooler and freezer · 18 stainless tables and shelving · 19 dough
  sheeter (for pastries) · 20 display case and counter · 21 retail store fixtures · 22 POS + scale · 23 signage · 24
  launch marketing · 25 opening ingredients inventory.
- **`3-Year P&L`**: fila 10 = «Bakery sales: bread, pastries and wholesale to cafés» (retail + wholesale en una línea);
  **col. H** (fijo «Tax-exempt share of the line (%)», D36): la nota F10 explica la parte exenta (bollería para llevar +
  reventa con resale certificate; ejemplo 0.80; «check your state»; UK zero-rated para llevar). Fijos 26-35:
  accounting · oven and equipment maintenance · marketing · software · cleaning · miscellaneous · waste hauling
  (organic and cardboard) · pest control · music licensing · training. Umbrales D41: margen bruto ≥ 60 %, mercancía ≤
  33 %, personal ≤ 38 %, alquiler ≤ 10 %, neto ≥ 5 %.
- **`Staffing`** filas 5-10: head baker / owner · baker · bakery assistant · counter staff / baristas · weekend extra ·
  vacation and day-off relief; filas 22-23 = **production shift before opening** (horas y personas), con el
  turno de madrugada sin «plus de nocturnidad» (no existe en EE. UU.).
- **D19** (filas 55-67): food cost 28-35 % y labor 24-40 % (Toast), margen 3-5 % del sector alimentario con la
  artesana más alto (Toast); merma, producción en kg → lb y hora de inicio como «Kit estimate»; fila 67 (convenio) →
  salario mínimo federal + estatal (DOL). Nunca «Versión anterior de este kit».
- **Checklist F1-F6** (pestañas «Phase 1 - Business Setup»… «Phase 6 - First 90 Days»; 11/12/12/10/11/10 tareas, molde
  de FT/CAF con OK en la col. A ☐/✓/N/A): equivalencias de SPEC delta §3 (cottage food frente a cocina comercial, D39,
  en la nota de Phase 1; health department o departamento de agricultura; FDA registration solo si lo mayorista
  domina; resale certificate; etiquetas de producto envasado con 9 alérgenos; USPTO opcional). F2!B13 ya está fijada
  («Ingredient and allergen labels for packaged and wholesale products»): su nota a juego.

## Docx — reglas comunes de las tandas (c)-(f)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»), más:

- `notas_del_plan` de tu entrada (concepto, «covers»/«transactions», cifras del docx ES que contradicen al Excel y NO
  se traducen) y las `nota` por párrafo (§9, D44) mandan.
- Tokens propios: restaurante `inv_obra`, `inv_cocina`, `inv_campana`, `inv_barra`, `inv_sala`, `inv_licencias`,
  `inv_lanzamiento`, `inv_stock`, `inv_stock_barra`, `aforo`, `rotaciones_dia`; panadería `inv_horno`,
  `inv_amasadora`, `inv_fermentacion`, `inv_vitrina`, `inv_electricidad`, `inv_obra`, `inv_lanzamiento`, `inv_stock`.
  `clientes_dia` / `equilibrio_*_clientes_dia` / `pesimista_clientes` son covers en el restaurante y transactions en la
  panadería: escribe la palabra correcta al lado del token.
- Sin leasing de horno (R7), sin «ICO/ENISA», sin «tasa de cierre» sin fuente, sin superlativos («the most complete»).
  Financiación: préstamo bancario o SBA 7(a) a 10 años (D40), «lender-ready, approval not guaranteed».
- El cierre (productos de la tienda) lo escribe el ensamblador: el restaurante tiene 4 líneas (143-146) y la panadería
  2 (128-129, dos productos por línea).

## (c) Tanda rest_a — docx restaurante §1-§5 (31 párrafos · ≈ 3.150 palabras)

Salida `BP2/docx_en_rest_a.json`. §1 resumen con tokens (inversión, ventas, covers × ticket × días, equilibrio, DSCR,
préstamo); §2 concepto (casual restaurant with a bar; comida, cena y barra); §3 mercado con cifras de research §1-§4
nombrando la fuente (nada de «81K+ restaurantes» ni datos de España); §4 competencia; §5 marketing (Google Business
Profile, Yelp, OpenTable / Resy, Instagram; delivery apps solo como opción).

## (d) Tanda rest_b — docx restaurante §6-§10 (44 párrafos · ≈ 3.500 palabras)

Salida `BP2/docx_en_rest_b.json`. §6 operaciones (la sección larga: cocina, barra, turnos, compras, seguridad
alimentaria); §7 equipo y personal (puestos reales del libro EN, D38 sin tip credit); §8 plan financiero SOLO con
tokens; §9 legal con las 8 notas (115-122; el 122 cierra con la nota UK); §10 conclusiones y plan de acción.

## (e) Tanda pan_a — docx panadería §1-§5 (29 párrafos · ≈ 3.250 palabras)

Salida `BP2/docx_en_pan_a.json`. Igual que (c) para la panadería: transactions, tienda + café + mayorista a cafés;
mercado con research delta §3-§4 (bakery $50,000-$100,000+ retail, food cost y labor de Toast).

## (f) Tanda pan_b — docx panadería §6-§10 (33 párrafos · ≈ 3.500 palabras)

Salida `BP2/docx_en_pan_b.json`. §6 operaciones (producción de madrugada, hornos, fermentación, reparto mayorista); §7
equipo; §8 SOLO tokens (sin «4-5 personas, 75-80 K €», sin «retorno en 24-36 meses»: {{payback}}); §9 legal con las 5
notas (106-110; el 110 cierra con la nota UK); §10.

## Después de las 6 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-2/bp2.py check_textos --todas      # GM, GN, GREST, GPAN + 4 docx
```

Luego la tanda de `aplicar_en.py` (opus, VPS): `bp2.py aplicar_en` consume `textos_en/{GM,GN,GREST,GPAN}.json`,
calibra D42/D15, escribe `cifras_caso.json` y `bp2.py ensamblar_docx --plan rest|pan` monta los Word (F2-NOTAS §5).
