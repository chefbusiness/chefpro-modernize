# Ice Cream Shop Business Plan Kit (EN) — SPEC DELTA (F1 · 27-oct-2026 · sesión Claude Code)

> Edición EN (EE. UU.) de `plan-negocio-heladeria` 1.0 (35 €, LIVE desde el 25-oct), **duplicada del ES ya revisado**. **Mandan
> las SPEC heredadas** (`../business-plans-en/SPEC.md` D1-D29, `-2/` D30-D47 = **Bakery**, `-3/` D48-D65 = Bar, `-4/`…`-8/` hasta
> D155 = **Pizza Shop**): aquí solo lo que cambia frente a la Pizza Shop EN, cuyo código se clona. Base: `F1-inventario-delta.md`
> (= **inv. §n**) y `F1-research-us-delta.md` (= **research §n**; manda en caso US, jerga y riesgos). Numeración **D186-D215**
> (D156-D185 = la otra F1 paralela). Tamaño **S**: F2 ≤ 1,0 M · F3 ≤ 0,55 M · ≈ 2,5-3 h; +30 % → se para y se reporta.
> «decisión SPEC» = choque resuelto aquí.

## 0. Jerga (John, 13-oct) — manda sobre todo

Glosario obligatorio = **research §9** entero (26 términos + «(e) no se traducen literalmente»), pegado en `BRIEF-TRADUCTORES.md`
(F2, paso 1a): «ice cream shop» en nombre, H1 y ficheros; «ice cream parlor», «scoop shop» y «creamery» en prosa; **«gelato» solo
como estilo**, nunca como nombre; **batch freezer · hardening cabinet · dipping cabinet · dipper well · base/mix · butterfat ·
overrun · pint/quart (hand-packed) · scooper · shift lead · frozen custard · ice cream cake · peak season / off-season**.
Unidades D14 + `REGLA_UNIDADES` de PAEL/PIZ (US con métrico entre paréntesis): **°F (°C)**, **sq ft (m²)**, **gal/qt/pint (l)**,
**lb (kg)**; la densidad legal en **lb/gal** (4.5), nunca «430 g/l». Sin tildes.

## 1. Producto (D186-D188)

| D | Tema | Decisión |
|---|---|---|
| D186 | Nombre y URLs | **Ice Cream Shop Business Plan Kit** · slug/productId `ice-cream-shop-business-plan` · JWT `ice-cream-shop-business-plan-jwt` · `/en/digital-products/ice-cream-shop-business-plan` (+ `/access`, `/library`) · gemelo ES `/plan-negocio-heladeria`, hreflang recíproco (**el ES tiene hoy `locales={['es']}`**, `plan-negocio-heladeria.astro:28`: F3 lo pasa a `alternatesFamilia`, D205) · env `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN`. Sin choque con `ice-cream-shop-checklist-templates` (Ice Cream Shop Checklists Kit Pro, $19, rutinas) |
| D186b | SEO | Title «Ice Cream Shop Business Plan Template: Word + Excel Financial Projections + Startup Checklist \| AI Chef Pro» · **H1 Forma B** `Ice Cream Shop ` + oro `Business Plan` + «Template to Open a Homemade Ice Cream Shop: Word Plan + Excel Projections with Seasonality + 80-Task Startup Checklist» · meta, 6 H2, 3 alt y keywords **tal cual research §9** (= docProps) |
| D187 | Precio | **$39** pago único (D49): sin `priceOld`, «-70 %», «Total value», «Save $» ni precio en bonos; sin rating ni review |
| D188 | Ficheros (`dl/ice-cream-shop-business-plan/`): **3 + guía común** | `ice-cream-shop-business-plan.docx` «Ice Cream Shop Business Plan (10 Sections)» · `ice-cream-shop-financial-projections.xlsx` «Ice Cream Shop Financial Projections: 3-Year P&L, Cash Flow & Financing» · `ice-cream-shop-startup-checklist.xlsx` «Ice Cream Shop Startup Checklist (80 Tasks)». La guía ES↔LatAm no cruza: bonus **común** `equivalents-guide` → `/dl/en-shared/hospitality-equivalents-us-uk-canada-australia.docx` (PIZ D135). **Sin calculadora** (el ES no la tiene; no se inventa una pieza) |

## 2. Concepto y caso (D189-D191)

| D | Tema | Decisión |
|---|---|---|
| D189 | Concepto | Research §1: **ice cream shop de barrio que hace su helado en el local**, ciudad de 150-300 mil hab., ~1,000 sq ft (sala de producción ~250), dipping cabinets de 18 sabores (10-12 en invierno), 20 plazas + patio de 5 mesas en temporada, scoops, sundaes, pints/quarts, ice cream cakes, café y chocolate caliente, catering. Abierto todo el año: cierra 3 semanas en enero, Thanksgiving, Christmas y los lunes de noviembre a febrero. Dueño = ice cream maker y GM. Fuera (FAQ): soft serve/froyo, ice cream truck (→ Food Truck Kit), franquicia, quiosco sin producción, casa |
| D190 | **Modelo de producción** (decisión SPEC, la adaptación grande) | **Base pasteurizada comprada a una central con licencia + batch freezer en el local**; pasteurizar la propia mezcla = **VARIANTE** sin Excel (pasteurizador de lotes ≈ $25,000-45,000 «pide presupuesto» + licencia estatal de dairy plant / frozen dessert manufacturer + equipo 3-A; research §6.1). Regla de seguridad que sustituye al D11 ES en el caso: **«after the dairy's pasteurization you add only flavorings and mix-ins: no raw eggs, no raw milk or cream; custard flavors need a custard base»**; en la variante, D11 ES tal cual (grasas, yemas y emulsionantes ANTES de pasteurizar; mínimos estatales 155 °F 30 min / 175 °F 25 s, Ohio 901:11-3-05). Consecuencias: fila 12 del Excel (D193), Word §2/§6/§8/§9 (D200), checklist F3 (D199), producción 2,0 h/día (D194). La licencia **siempre** «depends on your state: ask your state department of agriculture» con los ejemplos leídos (Vermont, Georgia) y en resumen (Arizona, Massachusetts, Pennsylvania); nunca «no license needed» ni tarifas |
| D191 | Caso US | `VALORES_EN` = research §8 sobre las celdas de inv. §2.3: **B4 165 · B5 $7.50 · B6 310** · 8/5 % · 90/10 · **22/25 %** · B15 4.5 % · **B16 4 % · B17 25 %** · B18 3 % · B20 10 % · B21 12 · B22 15,080 · **B24 $2,500** · B25 2 · **B26 $1,300** · **B27 $4,500** · B28 1 % · **B30 $95,000 · B31 CALIBRAR** (semilla $162,000; SBA 7(a) 10 % a 10 años, sin interest-only) · B35 3 · B37/B38 25 % · B39/B40/B63 8 % · B41 0 · B42 0 · B44/B45 10/7 · B48 0 · B51 20 · B52/B53 0.70/4 · B54 2 · B55 10 % · B58/B59 2/14 · **B62 0** · B65-B67 1.15/1.25/15 % · B68 vacío · `PyG!G13` 0; escenarios **140·$7.00·300 / 190·$8.00·320**. **D15**: holgura año 1 ≥ 15 %, DSCR mín ≥ 1.25, saldo mín > 0, cobertura ≥ 98 %, neto año 3 ≤ 12 %, umbrales D196 verdes; palancas en orden: holgura → **B5 $7.75** (o B30 +$10,000) · neto > 12 % → B4 155 · DSCR → B30. Máx. 3 vueltas, en `CALIBRACION_D15` y `F2-NOTAS`. **La estacionalidad no es palanca.** El Word dice la verdad: neto ≈ 5-6 % el año 1 frente al «10-25 %» de la SERP |

## 3. Libro financiero (D192-D198) — conjunto nuevo `ice` (clon del `piz`)

| D | Tema | Decisión |
|---|---|---|
| D192 | Código y diccionario | Código común **solo** `elif CONJUNTO == 'ice'` en `business-plans-en/mapas.py` (copia de `:1240-1247`; choque de merge trivial con la F1 paralela). Clones de inv. §7 (`mapas_ice`, `datos_ice`, `bp10`, `derivar_formulas_ice`, `formulas_ice_manual`, `calibracion_ice`, `barrido_ice`, `resumen_entregables`, `inventario_delta` ✅ ya escrito, `BRIEF-TRADUCTORES.md`). Molde de PIZ (plan `_HOJAS_PLAN`, checklist `hojas`, `COL_OK 1`, G4 de la DV). **Diccionario en cadena, sin normalizar** (inv. §6): EN de la **Pizza EN en la misma celda** (`../business-plans-en-8/textos_es.json` + `textos_en/{GM,GR,GPIZ-plan,GPIZ-check}` + `*.revision.json` + `datos_piz.POR_CELDA`) → Pizza EN por texto → **Bakery** (GPAN/GN + `overrides_`) → Bar → BP. Lo reutilizado de otra celda o de GPIZ-* va a **GR** con revisión en la tanda (84 + 18 cadenas, inv. §6). Grupos `GM · GR · GICE-plan · GICE-check · GX`. `verificar`: sha256 del ES final (inv. cabecera) + el diccionario de `-8/` (`SHA_PIZ`). Regresión: ftcaf, restpan, bar, cat, mbar, bbq, pael, piz |
| D193 | Inversión 7-25 (solo rótulo, importe y nota: **ninguna fila se mueve**; la clase de amortización la fija la fila) | 7 Architect, MEP drawings, plan review & permit fees $9,000 · 8 Build-out of production room & shop (second-generation retail, ~1,000 sq ft) $48,000 · 9 Electrical service & panel (about 30 kW) $9,000 · 10 Plumbing, floor sinks, hand sinks, HVAC & condenser ventilation $10,000 · 11 Signage & storefront $5,000 · **12 Base refrigerator & flavor prep (≤ 41 °F, stick blender, scales) $4,500** — nota D12: «Base case: you buy pasteurized base from a licensed dairy. Making your own mix adds a batch pasteurizer (about $25,000-45,000: get quotes) and, in many states, a dairy or frozen dessert manufacturer license» · 13 Batch freezer (20 qt, horizontal) $30,000 (nota: «a 20-qt Carpigiani lists at about $40,800; get two quotes; reconditioned units cost less») · 14 Hardening cabinet / blast freezer $9,000 · 15 Storage freezers (0 °F or colder) $7,000 · 16 Prep tables, 3-compartment sink, hand sinks, scales, pans & smallwares $8,500 · 17 Dipping cabinets (18 flavors) $11,000 · 18 Front counter, dipper wells, espresso, waffle cone irons & hot fudge warmers $9,000 · 19 Furniture (20 seats) & patio $7,000 · 20 POS, card terminal & online ordering $2,500 · 21 Scoops, spades, cups, uniforms & allergen signage $1,500 · 22 Ice cream training course $2,500 · 23 Branding, website, photos & launch $5,000 · 24 LLC, legal, permits & food safety plan $2,500 (E = «No») · 25 Opening inventory (base, flavorings, cones, cups, pint containers) $5,000 = **$186,000**. **B12 nunca vacía** (`B37 = IF(B12="","",…)`). Imprevistos **por fórmula** (10 % de B7-B11 = $8,100). A1 «ICE CREAM SHOP BUSINESS PLAN», A2 «Startup costs — ice cream shop with on-site production», A3 «US kit example (2026) — replace with your own quotes». Precios = research §4 («Kit estimate» salvo cita) |
| D194 | P&L, fijos, personal | A2 «Base case — ice cream shop with on-site production» · A10 «Ice cream sales (scoops, sundaes, pints & quarts to go, ice cream cakes, catering)» · A11 «Coffee & beverages (espresso, hot chocolate, sodas, water)» · F10 reparto de la venta (Kit) · fijos 26-35 (**$16,600**): accounting & bookkeeping 3,000 · refrigeration service contract (EPA 608-certified tech) 2,400 · seasonal marketing 4,500 · software, POS & phone 1,800 · cleaning supplies, uniforms & laundry 1,500 · **sidewalk café / patio permit (your city's fee)** 500 · waste & recycling 1,200 · pest control 600 · music licensing (ASCAP/BMI/SESAC) 600 · food safety & OSHA training (CFPM, food handler cards, allergens) 500. **Staffing** 6 filas, **1 persona por fila** (≥ $15/h, 12 pagas, sin propinas D38): Owner / ice cream maker & GM 1.0 $4,000 · Shift lead / counter (year-round) 1.0 $2,946 · Seasonal scooper (part-time, April-September) 0.5 $1,300 · Summer scooper (part-time, June-August) 0.25 $650 · Production assistant (part-time, May-September) 0.2 $555 · Relief cover (vacations and days off) 0.1 $260 (= 3.05 FTE); `B13`/`B14` $8,000; cobertura = ES salvo **`B22` 2.0 h** (sin pasteurizar). Nota J de los seasonal: «seasonal part-time W-2, rehired each spring; scoopers aged 14-15 only within FLSA hours (29 CFR 570.35)». Nota de Tesorería (como ES D13): el personal se reparte en 12 meses → invierno más caro que la realidad (prudente). El dueño cobra por debajo de un gerente: «draw in addition from net profit» |
| D195 | Sales tax y Tesorería (inv. §3) | `B39`/`B40`/`B63` 8 %, `B41` 0, `B62` 0 (`G11` = `B39`); **`G13` (valor) → 0** «no input credit»; `G14` → E2. **Sin E3 ni E5** (no hay línea partida). `B39` nota: «Scoops served to eat are taxed as prepared food in most states; packaged pints and whole cakes may be taxed as groceries in some (Texas example): use your blended rate». `B63` «no effect». Tesorería 16-20 = Bar/PIZ EN; **POR_CELDA**: `O5` «Month 1 = MARCH: open in season so the first winter is paid by the first summer… replace the weights with your area's pattern (colder states: more weight June-August; Sun Belt: flatter)», **`A34`** «plan quarters (March-May, June-August, September-November, December-February), not calendar quarters» y **`O20`** «…settles in the month after each plan quarter (Months 4, 7 and 10: June, September and December with Month 1 in March; the fourth quarter is remitted in Month 13)…» (**no** el c0531 de la pizza, inv. §6). `Personal!J19` = c0387 de la pizza (vale: cierre en enero) |
| D196 | Umbrales y D19 | `E51` 65 % · `E53` 25 % · `E54` 35 % · `E55` 10 % · `E56` 5 %. **D19** (`Instructions` 34-47; sin D18), «US ICE CREAM SHOP BENCHMARKS (sourced) AND KIT ESTIMATES», 13 filas (sin propuesta: van a GICE-plan): Month 1 = March (plan decision) · peak season Memorial Day → Labor Day; July = National Ice Cream Month (Proclamation 5219; IDFA) · ice cream cost per serving (Kit) · menu prices (Kit menu, research §5.1) · «ice cream» ≥ 10 % milkfat and ≥ 4.5 lb/gal; frozen custard 1.4 % egg yolk solids (21 CFR 135.110) · storage 0 °F or colder, dipping cabinet 6-10 °F (Food Code + manufacturer) · buy base vs make your own mix: license by state (Vermont/Georgia, research §6.1) · labor 28-35 % (Kit) · rent ≤ 10 % (Kit) · waste 5-8 % (Kit) · electrical ≈ 30 kW (Kit) · sales tax: scoop vs packaged pint (Texas Comptroller) · minimum wage federal $7.25 + state; teens 14-15 hours (29 CFR 570.35). Solo lo «[leída]» con fuente; lo «(resumen)» con «check» o como Kit estimate |
| D197 | Fórmulas y excepciones | Con texto: las derivables de su gemela (inv. §2.1; PIZP primero, PANP para las de la fila 28/38) + **manuales C9** (ticket + sales tax medio de las líneas), **D28** (lista EN de las 5 partidas de obra), **D38** (lista EN de lo que no se amortiza, ≤ 255 caracteres por literal) y **F13** (food cost sobre ventas de helado: base, inclusiones, conos, catas y merma; **sin** afirmaciones de impuestos de compra). **E1** aviso D21 (HELP `A53`, HELC `A12`) · **E2** solo `G14`. **Sin E3, E4 ni E5** (inv. §2.6: `PARCHES_FORMULA` de PIZ apunta a `C12`, que aquí es una cabecera). G1 = **736** fórmulas y 80 tareas |
| D198 | Mes 1 y pagas | **Mes 1 = marzo** (pesos del ES sin tocar, inv. §2.8); `B60`/`B61`/`O13`: con 12 pagas no hay extras (EN del Bar/PIZ) |

## 4. Checklist (D199) — las 80 tareas 12/15/15/12/13/13 del ES, mismas filas

Pestañas: «Phase 1 - Business Setup» · «Phase 2 - Site & Permits» · «Phase 3 - Production & Health» · «Phase 4 - Staff & Food
Safety» · «Phase 5 - Brand & Menu» · «Phase 6 - Opening & Season» (todas ≤ 31). A1 «ICE CREAM SHOP STARTUP CHECKLIST»;
`Instructions!A3` = nombre comercial; DV `"✓,☐,N/A"` (G4 de PIZ) y **su texto de error/ayuda con ☐**, no «—». Equivalencias (se
suman a BP §4.2, BP2 §3, Bar D60, PIZ D146):

| ES | US |
|---|---|
| SL/autónomo, IAE 644.4/676, Veri\*factu · consulta urbanística, potencia | LLC vs S corp with your CPA · EIN + state payroll/unemployment · business license + **sales tax permit** · POS that reports sales tax · zoning check before signing (retail food with on-site production) · **ask the utility about 3-phase service and amps before signing** |
| Declaración responsable, obra, terraza, boletín | building permit + CO · **plan review (8-201.11) with the equipment layout** · sidewalk café/patio permit · signage permit · electrical inspection |
| Registro sanitario autonómico, RGSEAA, APPCC, huevo/ovoproducto, RD 618 | health permit + inspection · **license decision: buy base from a licensed dairy or make your own mix (state dairy / frozen dessert license, 3-A equipment)** — una tarea propia, con «ask your state department of agriculture in writing» · base supplier agreement (delivery ≤ 41 °F, lot codes) · **dipper well with running water (3-304.12)** · cold holding ≤ 41 °F, frozen storage 0 °F, date marking · labels on packaged pints (3-602.11, allergens) · «ice cream» / «frozen custard» only if the recipe meets 21 CFR 135.110 |
| Fijos discontinuos, convenio, PRL, manipuladores, alérgenos | offer letters, I-9, W-4, state new-hire reporting, minimum wage posters · **seasonal hiring each spring** · **teen scoopers: FLSA hours and state work permits** · OSHA basics (cold, slips, cuts) · CFPM (2-102.12) + food handler cards · **9 allergens incl. sesame** · no «allergen-free» promise (shared scoops and dipper wells) |
| «Artesano»/«elaboración propia», Google, encargos (comuniones, turrón), delivery | honest claims («made here in small batches»; «homemade» only if true) · Google Business Profile · cake pre-orders (birthdays, graduations, holidays) · **National Ice Cream Day (3rd Sunday of July)** · DoorDash/Uber Eats for pints · ASCAP/BMI/SESAC |
| Apertura, temporada, invierno | soft opening + Opening Day · peak-season staffing (Memorial Day → Labor Day) · winter plan (cakes, holiday pies and pints, hot chocolate, catering; or close November-February: Word alternative) · insurance with **equipment breakdown + food spoilage** · refrigeration service contract before summer (EPA 608 tech; staff never top up refrigerant) |

**Regla B2 de la pizza**: toda licencia o permiso que prometan la landing, la tarjeta del hub o el Word tiene **su tarea** en el
checklist (license decision, health permit, sales tax permit, patio permit, building permit/CO). Si no cabe sin añadir filas, se
reescribe una tarea existente (como PIZ B2).

## 5. Docx (D200)

Las **131 ranuras del FT ES** (inv. §5) con la config de PIZ; 61 traducidas-adaptadas desde el **Word ES de la heladería**
(`ice_a` §1-5 = 29 ‖ `ice_b` §6-10 = 32), un run por párrafo, **todas las cifras desde `cifras_caso.json`** (tokens D43 + los 19
`inv_*` de D193, `delivery_pct`, `comision_pct`, `produccion_horas`, `sabores`, `prime_cost_pct`, `fijos_anual`). Nota por ranura =
pista de research + la sección de la Pizza EN como forma. **No cruzan** (inv. §5): IAE/Ley 12/2012, RGSEAA/registro autonómico,
RD 618 y RD 1021/2022, convenio y fijos discontinuos, Veri\*factu, MAPA y DataForSEO España, crepes con salida de humos. **Se
sustituyen**: [53]-[56] demanda US (IDFA julio, National Ice Cream Month, DataForSEO US de research §2) · [47]/[78]-[80] proceso
con **base comprada** (recibir ≤ 41 °F → aromatizar → batch-freeze → endurecer a 0 °F o menos → dipping cabinet 6-10 °F; las cifras
de producción de [80] se recalculan en F2 a partir del caso o la frase va sin cifra) · [79] equipo con precios de D193 · [99] dos
alternativas: **variante «make your own mix»** (pasteurizador + licencia, sin Excel) y cierre de noviembre a febrero · [50]/[113]
invierno sin crepes (no cruzan: cakes, holiday pies, pints, hot chocolate y catering; nada que pida campana o salida de humos) ·
[73] encargos: birthdays, graduations, Fourth of July, holiday pies. **§9 (102-108)**: [102] LLC, EIN, business
license, sales tax permit · [103] zoning, building permit/CO, plan review, patio y signage · [104] health permit + **la decisión de
licencia de D190** con Vermont/Georgia · [105] Food Code (CFPM, food handler cards, dipper well, ≤ 41 °F, 0 °F, date marking; sin
huevo crudo) · [106] 21 CFR 135.110 y reclamos honestos · [107] alérgenos (9 con sésamo) y sales tax del scoop frente al pint ·
[108] FLSA y jóvenes, W-2 de temporada, salario mínimo estatal, seguro con equipment breakdown + spoilage, ASCAP/BMI/SESAC y
**nota UK**. FIJOS 35 «Appendices: … + Equivalents Guide»; cierre 127-130 = Ice Cream Shop Checklists Kit Pro · Food Cost Kit Pro ·
HACCP Food Safety Kit Pro · aichef.pro/en/digital-products.

## 6. Gates (D201), cifras y vocabulario (D202), revisión (D203)

- **D201**: G1-G9 (E1, E2 por nombre) · `RX_ICE_NO` y cifras prohibidas 0 en los 3 · barrido · no latinos · `censo-entregables
  --fail --letter --only ice-cream-shop-business-plan` (alta en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9) · `verificar` ·
  regresión de los 8 conjuntos · 2.ª pasada con sha256 canónico igual.
- **D202**: `cifras_prohibidas()` de `datos_piz.py`: `CIFRAS_ES` = importes ≥ 10.000 € de `../plan-heladeria/cifras_caso_es.json`
  (los pequeños, solo con «€»), fuera los que coinciden con el caso US · `FRASES_ES` («143 customers», «4[.,]90», «14 pay», «33 %»,
  «17[.,]094», «644\.4», «\b676\b», «430 g», «−18 °C» como regla, «fijo discontinuo», «3 ?% of sales» del delivery ES con la regla
  de contexto de PIZ B4) · caso de la **Pizza EN** (`_cifras_caso('../business-plans-en-8/cifras_caso.json', 'piz')` + «62
  covers», «$36», «300 days») y BAKERY. `RX_ICE_NO` = restos de la pizza (`pizza|pizzaiolo|(?<!cookie )dough|\boven\b|Neapolitan|VPN|firewood|
  beer (?:&|and) wine|equivalent covers|covers per day|\bflue\b|spark arrestor`) + de la Bakery (`\bbread\b|bakery|\bbaker\b|
  loa(?:f|ves)|transactions per day`) + del ES (`\bIVA\b|\bIAE\b|aut[oó]nomo|convenio|\bSMI\b|Veri\*?factu|RGSEAA|SGAE|terraza|
  helader|mantecad|fijo discontinuo|carn[eé]|618/1998|1021/2022|crepe|turr[oó]n|comuni[oó]n`). «pasteuriz» solo en la nota de
  `D12`, en D19, en el Word §2/§6/§8/§9 de la variante y en la tarea de licencia.
- **D203 Una revisión opus** (tope 2 rondas, arreglos por texto): recalcular ventas, CAPEX con imprevistos de fórmula, equilibrio,
  holgura y DSCR · jerga · **claims** (licencia láctea por estado, «homemade», «frozen custard», «gelato», «allergen-free», sales tax,
  jóvenes, «10-25 %») · abrir 21 CFR 135.110, Food Code 3-304.12 y 2-102.12, Vermont y Georgia · **que el modelo de base comprada sea
  coherente en los 3 ficheros y la landing** (ningún resto de «pasteurize at 85 °C» en el caso) · **cero rastro de pizzería, de
  panadería ni de España** · que el Word no prometa lo que el Excel no hace · O20/A34 con los meses de marzo.

## 7. Capa de producto (D204-D206, F3) — duplicar la F3 de la Pizza (`git show 64ace831 --stat`)

- **D204 Landing** `astro-site/src/data/productos-en/planes/ice-cream-shop-business-plan.ts` = `cp` de `pizza-shop-business-plan.ts`,
  SEO D186b, FAQ = las 8 de research §3 + UK/CA/AU; cifras MEDIDAS (ventas, CAPEX, caja, neto %, equilibrio; nada movible);
  **sin testimonios** (los 8 del ES son clientes de España: no se trasladan ni se inventan, FTC); `omitGlobalApp`; imágenes
  `plan-heladeria-*.jpg` del ES (7; F3 comprueba que no lleven texto en español) + `og-ice-cream-shop-business-plan.jpg` (recorte
  del hero). La FAQ 8 y un bloque de la landing **diferencian y enlazan** el Ice Cream Shop Checklists Kit Pro.
- **D205 Registros**: páginas `en/digital-products/ice-cream-shop-business-plan{.astro,/access.astro,/library.astro}`, island
  `IceCreamShopBusinessPlanLibraryIsland.tsx`, `src/pages/IceCreamShopBusinessPlanDashboard.tsx` (claves `plan-negocio`,
  `plan-financiero`, `checklist-apertura`, `equivalents-guide`) · `tienda.ts` (FAMILIAS `plan-negocio-heladeria`, es + en vivos) y
  **`plan-negocio-heladeria.astro`** → `alternatesFamilia('plan-negocio-heladeria')` (diff de PIZ) · `zona-app.ts` ·
  `get-download-urls.ts` (3 + guía) · `verify-purchase.ts` · `resend-access.ts` · `admin-generate-access.ts` + `AdminGenerateAccess.tsx`
  · `product-prices.ts` (`sync-product-prices.py`) · `payment-links.ts` (tras el link) · `products-catalog.ts` (entrada ES: `name.en`,
  `urlByLang`, `priceByLang`) · config · changelog '1.0' · `linkify-use-case.{ts,tsx}` · **hub EN**: la tarjeta «Business Plan:
  Artisan Gelato Shop» (→ ES, `DigitalProductsHubPage.astro:643-656`) **se sustituye** por la del EN (posición 1, «New»; no dos
  tarjetas, B1 de PIZ) · `llms.txt`/`llms-full.txt` (+1 sobre lo que haya al merge) · `sitemap-lastmod.json` · `footerLinks` de los
  planes EN + Ice Cream Shop Checklists + Food Cost + HACCP · FAQ «Is there a business plan for an ice cream shop?» en Ice Cream Shop
  Checklists EN y Food Truck EN (ice cream truck) · `tienda-gate.py` · correo `broadcast-ice-cream-shop-business-plan-lanzamiento-en`.
- **D206** Gates F3: `sync-product-prices --check` · `tienda-gate` (+ `--es-identico`) · `robots`/`whatsapp`/`miselup`/`hub`/
  `carrusel-apps` · `gate-flujo-postpago --crypto-products all --crypto-exclude pro-prompts-ebook --only ice-cream-shop-business-plan`
  (preview y LIVE) · `fase6-gate.py <URL EN>`. **Payment Link: John** (USD 39, prosa sin viñetas, éxito →
  `/en/digital-products/ice-cream-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}`). **Correo EN** en el siguiente hueco
  libre de la cola EN (CALENDARIO l. 774: **23-feb-2027 14:00Z** si la F1 paralela no lo ha tomado; si no, 28-feb): borrador + prueba +
  routine ≥ 30 días antes. El ES ya está LIVE: el merge no espera a nadie. No se tocan `robots.txt` ni el blog (carril Cursor).

## 8. Plan, presupuesto y riesgos (D207-D208; D209-D215 libres)

| Paso (D207) | Quién | Tokens · reloj |
|---|---|---|
| 1a · rama `ice`, clones de PIZ, caso D191, tokens, POR_CELDA, `RX_ICE_NO`, `extraer_textos`/`extraer_docx` sobre el ES final, `preparar_tandas`, dry-run + D15 (VPS) | 1 opus | 0,35 M · 40 min |
| 2 · Tanda 1: GICE-plan (155 cad., ≈ 3,5 K pal. + 13 filas D19 + revisión de GR ≈ 100) ‖ GICE-check (156, ≈ 2,4 K) | 2 sonnet | 0,20 M · 20 min |
| 3 · `aplicar_en` + D15 → `cifras_caso.json`; Tanda 2 `ice_a` ‖ `ice_b` (61 ranuras, ≈ 6,7 K pal.); `ensamblar_docx` | VPS + 2 sonnet | 0,22 M · 25 min |
| 4 · Gates D201 + revisión D203 + 1 ronda; `F2-NOTAS`; commit + push | VPS + 1 opus | 0,20 M · 30 min |
| 5-6 · F3: sonnet A (ficha, páginas, isla, dashboard) ‖ sonnet B (registros, hub, hreflang ES, enlaces, correo); OG, PR, preview, gates, link, LIVE | 2 sonnet + orquestador | 0,55 M · 60 min |
| **Total F2 (≈ 0,97 M) + F3 (≈ 0,55 M)** | | **≈ 1,5 M · ≈ 2,5-3 h** + el link |

Más barato que la pizza (≈ 1,8 M): sin calculadora y con el ES ya cerrado (sin paso 1c de re-medición).
**D208 Riesgos**: (1) **modelo de base comprada** (D190): es la decisión de adaptación más grande; si el orquestador quiere el
pasteurizador en el caso, cambian D193 fila 12, D191 `B13` (≈ 18 %) y la tarea de licencia: decidirlo antes del paso 1a; (2)
**holgura justa** (≈ 15,4 % con la semilla) → D15 con las palancas de D191; (3) licencias por estado: solo ejemplos con fuente, nunca
«no license needed»; (4) **fuga de la pizza** por el diccionario (PIZ-GM, PIZ y GR: «covers», «oven», «dough», «beer & wine») →
D202 y revisión de GR; los dos `GM.revision` de la pizza: **c0531 (O20) no vale** y c0387 (J19) sí (D195); (5) el texto de la DV
dice «—» en el EN de PIZ (D199: ☐); (6) canibalización con el Ice Cream Shop Checklists Kit Pro y con la tarjeta ES del hub EN
(D204-D205); (7) conflicto de merge con la F1 paralela en `mapas.py`, `llms`, `footerLinks`, hub y CALENDARIO: el segundo en
mergear rebasa. **NO se hace**: testimonios, anclas, ratings, tabla de licencias de los 50 estados, calculadora nueva, pasteurizador
en el Excel, tip credit, cambiar filas/hojas/DV, research nueva, posts del blog, compra de prueba.
