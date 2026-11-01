# SPEC — `business-plans-en-15/calculadora_bur.py` (Smash Burger Patty, Fries & Costing Calculator, EN/US)

> Sesión Claude Code, 31-oct-2026 (F2-EN, lead opus). Implementa un subagente sonnet. Fuente de datos US:
> `business-plans-en-15/F1-research-us-delta.md` §4-§8 (**US §n**) y `../plan-hamburgueseria/F1-camino.md` §6.

Write `scripts/productos-digitales/business-plans-en-15/calculadora_bur.py` = the ES calculator
`scripts/productos-digitales/plan-hamburgueseria/calculadora_ham_es.py` (same 4-sheet structure, same rows/blocks/formula
logic, same `calcular()` mirror, `EXPUESTOS`, `valores_expuestos`, protection without password, green inputs unlocked,
inject_cache, autotest with pycel + cache = `calcular()` with 3 input sets, beef and fries selectors, the informative
dropdown with INDEX/MATCH) TRANSLATED with the code pattern of the EN twin
`scripts/productos-digitales/business-plans-en-14/calculadora_sus.py` (imports of `mapas as M` with
`os.environ.setdefault('BP_CONJUNTO', 'bur')`, `_PL = M.PLANES['bur']`, VERSION/MES from mapas, VERSION_LINEA, FOOTER_EN,
FIRMA_EN, AVISO_EN, URL_TIENDA, US Letter, number formats without currency symbol and labels with «($)», docProps in
English, `--salida` generates + inject_cache + autotest, `--autotest` only tests an existing file, PROHIBIDOS list +
`datos_bur.RX_BUR_NO` + `M.no_latinos` + `M.restos_espanol` checks on every text cell, `motor.gate_formatos`).

- File: `smash-burger-patty-costing-calculator.xlsx`. Visible name: **«Smash Burger Patty, Fries & Costing Calculator»**;
  docProps title «Smash Burger Patty, Fries & Costing Calculator (Beef & Patty, Fries & Oil and Cost per Burger)».
- Sheets: **`Beef & Patty` · `Fries & Oil` · `Costing` · `Instructions`**.
- Units: beef, fries and oil in **$/lb**; portions in **oz** with the grey constant «16 oz per lb» (no typed numbers in
  formulas except 0/1); oil by weight (lb: US fryers are rated in lb of oil); «60 minutes per hour» constant. °F only in
  instruction text. No kg, g, ml, liters, °C, € anywhere (metric only in parentheses in instruction text, if at all).
- Every default is «Kit estimate, editable» unless a source is given. Vocabulary (US §9): smash burger (never «smashed
  burger»), ball (raw) / patty (cooked), flat-top (never «fry-top»), smash press, crust, potato bun, American cheese, combo
  (never «value meal»), shake, fries, make line, cook loss, covers, take-out / pickup, delivery marketplace. No «rare»,
  «medium» or «pink» as an option; no «gourmet», «authentic», «gluten-free» promises.

## Beef & Patty (= ES `Carne`): 3 beef options + 1 free column, B..E
| # | Name | $/lb | usable share | minutes to trim and grind per lb | fat % (informative) |
|---|---|---|---|---|---|
| 0 | 80/20 ground chuck blend (bought ground) | 5.25 | 1.00 | 0.0 | 0.20 |
| 1 | Whole chuck for house grinding | 4.50 | 0.90 | 3.0 | 0.20 |
| 2 | Pre-portioned balls (bought, 3 oz) | 6.25 | 1.00 | 0.0 | 0.20 |
| 3 | Other beef (type yours) | 5.75 | 1.00 | 0.0 | 0.20 |
Price note: «No wholesale price for 80/20 was read in Oct 2026: BLS/FRED ground beef (100% beef, retail) was $6.79/lb in
Sep 2026 and retail 80/20 runs about $5.69-6.93/lb. The kit puts 5.25 $/lb for 80/20 chuck from a distributor, 4.50 for whole
chuck and 6.25 for pre-portioned balls (no source: ask your supplier). Kit estimate (Oct 2026): replace with your
distributor's price.» Usable note: 100% if you buy it ground; 90% for whole chuck (no source: weigh before and after).
Common inputs (block B): end-of-day shrink (balls, buns and sauces thrown out) **3%** · **oz per ball 3.0** («2-4 oz; 3 oz
is the case of the plan: weigh 10 balls and use the average») · cook loss on the flat-top **25%** («no primary source:
weigh 10 balls before and after the flat-top; it only changes the ounces served») · cook cost per hour **$18.70** («a grill
cook at about $17/h + 10% employer payroll taxes ≈ $18.70/h») · balls per cover **1.6** («plan criterion: measure it») ·
covers per day **195** («the case of the business plan») · dropdown «Do you buy ground beef or grind in-house?» (informative,
changes no figure) · constants «16 oz per lb» and «60 minutes per hour» (grey, locked). Dropdown options and reminders:
1. «I buy ground beef» → «Keep raw ground beef at 41 °F or below and store it below ready-to-eat food (FDA Food Code 2022,
   3-501.16 and 3-302.11). File the supplier's establishment number, lot and pack date of every delivery.»
2. «I grind in-house» → «Keep a house-grind log as good practice and for recalls: supplier establishment numbers and lots,
   the date and time of every grind and of every cleaning and sanitizing of the grinder. The FSIS rule (9 CFR 320.1(b)(4))
   covers retail stores and official establishments that grind raw beef: ask your health department whether it applies to
   you.»
3. «I buy pre-portioned balls» → «Keep the spec sheet and the label with the lot and date of every case, and hold the balls
   at 41 °F or below until they go on the flat-top.»
Outputs: **COST PER USABLE LB** = price ÷ usable ÷ (1 − shrink) [defaults ≈ 5.41 · 5.15 · 6.44 · 5.93] · cost per usable lb
with the labor of trimming and grinding = (price + minutes ÷ 60 × $/h) ÷ usable ÷ (1 − shrink) · cost of the beef of one ball
= cost with labor × oz ÷ 16 · double (2 balls) · triple (3 balls) · **BALLS PER LB, RAW** = 16 ÷ oz [≈ 5.3] · balls per lb
counting the end-of-day shrink · oz served after the flat-top · balls sold per day = covers × balls per cover · **LB OF BEEF
PER DAY** = balls × oz ÷ 16 [≈ 58.5] · labor per usable lb of whole chuck · **«GRINDING IN-HOUSE PAYS OFF AS LONG AS TRIMMING
AND GRINDING COST LESS THAN ($ per usable lb)»** = blend cost with labor − whole-chuck cost without labor · verdict
«Grinding in-house pays off» / «Buy the blend ground» · reminder of the dropdown case. Fixed note under the outputs: «Cook
every smash burger to 155 °F (68 °C) for 17 seconds (FDA Food Code 2022, 3-401.11(A)(2)) and probe one burger per batch: the
crust is not a thermometer.»

## Fries & Oil (= ES `Patatas`)
Inputs: frozen fries **$1.16/lb** («Saint-Arneault 1/2" crinkle, 6 × 5 lb $34.68; 3/8" crinkle $1.11/lb; webstaurantstore.com,
Oct 2026») · **oz of frozen fries per portion 5.0** · oil absorbed by a frozen portion **5%** of its weight · fresh potatoes
(russet) **$0.55/lb** («no price read: ask your produce supplier») · oz of fresh-cut fries per portion 5.0 · usable share
after peeling and cutting **75%** («no source: weigh 10 lb before and after») · oil absorbed by a fresh portion **10%** ·
minutes to peel, cut and soak 1 lb of fresh potatoes **3.0** · cook cost per hour **$18.70** («same as Beef & Patty») · **lb
of oil per fryer 40** («a 40-50 lb fryer») · **fryers for fries 2** («the third fryer is for the breaded chicken:
cross-contact») · frying oil **$1.40/lb** («a 35 lb jug or JIB runs about $1.20-1.60/lb; no price read») · **portions
between oil changes 1,500** («set it by your TPM readings: there is no federal limit; filter nightly») · portions of fries per
cover **0.8** · **days open per month 30** («the plan opens 360 days a year») · constants «16 oz per lb», «60 minutes per hour».
Outputs (same formulas as ES with oz/lb): covers per day (from Beef & Patty) · oil cost of one full change = lb per fryer ×
fryers × $/lb · **OIL PER FROZEN PORTION** = change ÷ portions + oz × absorbed ÷ 16 × $/lb · fries of a frozen portion =
oz × $/lb ÷ 16 · **COST PER FROZEN PORTION** [≈ 0.46] · lb unpeeled per fresh portion = oz ÷ usable ÷ 16 · fresh potatoes of a
portion · oil per fresh portion · **COST PER FRESH PORTION, WITHOUT LABOR** · labor of a fresh portion · cost with labor
(feeds Costing if selected) · labor per lb unpeeled · **«FRESH-CUT PAYS OFF AS LONG AS PEELING AND CUTTING COST LESS THAN ($ per
lb unpeeled)»** = (frozen − fresh without labor) ÷ lb unpeeled per portion · verdict «Fresh-cut pays off» / «Frozen pays
off» · **PORTIONS OF FRIES PER DAY** · lb of frozen fries per day · lb of fresh potatoes per day · **LB OF OIL PER MONTH
(frozen)** = portions/day × days × (lb of one change ÷ portions + oz × absorbed ÷ 16). Fixed note: «Fry at 350-355 °F; filter
the oil every night and change it by your TPM reading or the manufacturer's guidance; used oil goes to a licensed renderer.
Acrylamide has no federal limit for restaurants; in California, ask your attorney about the Prop 65 warning for fried
potatoes.»

## Costing (= ES `Escandallo`, 14 products)
General inputs: **sales tax included in menu prices 0%** («US menus usually exclude sales tax: leave 0%. Type your rate only
if your prices include it; UK: VAT is 20% dine-in and on hot take-out food») · **target food cost 30%** («a common target
for a burger menu; the plan's 34% is the real usage of the whole food menu») · watch band **3 points** · **beef selector 1-4**
(column of Beef & Patty; default 1 = bought ground) · **fries selector 1 frozen / 2 fresh with labor** (default 1) · **potato
bun $0.55** («Martin's Sandwich Potato Rolls 2.1 oz, 60 for $33.02 = $0.55, webstaurantstore.com, Oct 2026») · **American
cheese, $ per slice 0.14** («Kraft 640 ct $87.22 ≈ $0.14; Schreiber 480 ct $58.90 ≈ $0.12; webstaurantstore.com») — this
ONE input replaces the ES pair €/kg + g per slice (cost of cheese = slices × $ per slice) · to-go packaging per order
**$0.55** (wrapper, fry cup, bag, napkins) · marketplace packaging per order **$0.75** (vented fry box, tamper-evident
seal) · marketplace price markup **15%** · marketplace commission **25%** («on the price before tax; check your
contract»). Links to Beef & Patty (cost of one ball, selected column) and Fries & Oil (cost of one portion, selected type).
Products (name, balls, cheese slices, buns, other ingredients $, fries portions, menu price $, units per week):
| Product | balls | slices | buns | other $ | fries | price $ | units/wk |
|---|---|---|---|---|---|---|---|
| Single smash burger (1 ball) | 1 | 1 | 1 | 0.30 | 0 | 8.49 | 230 |
| Double smash burger (2 balls) | 2 | 2 | 1 | 0.35 | 0 | 10.99 | 390 |
| Triple smash burger (3 balls) | 3 | 3 | 1 | 0.40 | 0 | 13.49 | 65 |
| Double bacon smash burger | 2 | 2 | 1 | 0.80 | 0 | 12.49 | 150 |
| Oklahoma onion smash burger (2 balls) | 2 | 2 | 1 | 0.45 | 0 | 11.99 | 80 |
| House smash burger (2 balls) | 2 | 2 | 1 | 0.85 | 0 | 12.99 | 115 |
| Crispy chicken sandwich | 0 | 1 | 1 | 2.10 | 0 | 10.49 | 100 |
| Veggie burger | 0 | 1 | 1 | 1.90 | 0 | 9.99 | 35 |
| Fries | 0 | 0 | 0 | 0.00 | 1 | 3.99 | 280 |
| Loaded fries (cheese sauce and bacon) | 0 | 0 | 0 | 0.85 | 1 | 6.49 | 150 |
| Shake | 0 | 0 | 0 | 1.45 | 0 | 6.49 | 100 |
| Dessert (cookie or sundae) | 0 | 0 | 0 | 1.10 | 0 | 4.49 | 90 |
| Combo: double + fries + soft drink | 2 | 2 | 1 | 0.60 | 1 | 15.99 | 380 |
| Meal for two: 2 doubles + 2 fries | 4 | 4 | 2 | 0.70 | 2 | 28.99 | 55 |
Other-ingredients note: «toppings and sauce (pickles, onion, lettuce, special sauce) about $0.35 on a double; bacon, the
breaded chicken breast, the veggie patty, the shake base and the soft drink (syrup and cup) at Kit estimate prices».
Outputs per product (same columns as ES): cost · price before tax · food cost % with traffic light («On target» / «Watch
the cost» / «Above target») · suggested price · **margin $ by channel** (dine-in = price − cost; take-out/pickup = dine-in −
to-go packaging; marketplace = price × (1 + markup) × (1 − commission) − cost − marketplace packaging) · rank by dine-in
margin. Totals: weekly sales before tax, weekly food cost, **WEIGHTED FOOD COST** + traffic light. Fixed warning (instead of
the ES one): «A smash burger travels worse than other food: the crust softens in about 15 minutes. Use vented boxes for the
fries and price the marketplace menu about 15% higher.» Bridge note (replaces the ES 28 % note; NO invented points): «The
plan's 34% food cost ("0. Assumptions" B13 of the Burger Restaurant Financial Projections) is the real usage of the whole
food menu, with the balls, buns and sauces thrown out, staff meals, comps, mistakes and marketplace refunds and promotions:
this weighted theoretical cost comes out lower. Do not copy it into the plan.»

## Instructions (= ES `Instrucciones`, US content)
Steps: weigh 10 balls and type the average oz; weigh 10 balls before and after the flat-top (cook loss); weigh 10 portions of
fries; time 3 lb of whole chuck (if you grind) and 3 lb of fresh potatoes; **cooking rule**: 155 °F (68 °C) for 17 seconds
for ground beef, or 145 °F 3 min · 150 °F 1 min · 158 °F instantaneous (Food Code 2022, 3-401.11(A)(2)); probe one burger
per batch; **consumer advisory** (3-603.11: disclosure + reminder on the menu, the website and the marketplace listings)
only if you offer burgers cooked to order at the guest's request (3-401.11(D)); never on the children's menu; the example
serves every burger cooked through; **house-grind log** (practice, not claimed as mandatory); 41 °F cold holding; **9 major
allergens** in a burger: the bun (wheat; milk, egg, soy and sesame depending on the recipe), American cheese (milk), mayo
(egg), shakes (milk), the breaded chicken (wheat, egg, milk) and the shared fryer oil; mustard is not a major allergen in
the US; never promise «gluten-free»; **frying oil**: TPM, no federal limit; **acrylamide**: no federal limit, Prop 65 in
California; sales tax (menu prices before tax); the cost per burger of this calculator is NOT copied into the plan;
«Kit estimate, editable»; the version line; the AI Chef Pro signature (FIRMA_EN), the store URL and AVISO_EN as in
`calculadora_sus.py`. Name the other files of the kit exactly: «Burger Restaurant Financial Projections», «Burger Restaurant
Startup Checklist», «Burger Restaurant Business Plan». No Spanish norms, no «Kit de Tareas», no Spanish franchises.

## EXPUESTOS (names exactly)
COST_LB_USABLE_BLEND (Beef & Patty B cost per usable lb) · COST_LB_USABLE_CHUCK (C) · GRIND_PAYS_OFF_BELOW (X) ·
BALLS_PER_LB · BALLS_PER_LB_NET · BEEF_PER_DAY_LB · COST_SINGLE · COST_DOUBLE · FC_SINGLE · FC_DOUBLE · FC_COMBO ·
FC_WEIGHTED · COST_FROZEN_FRIES_PORTION · COST_FRESH_FRIES_PORTION · OIL_PER_PORTION · OIL_LB_MONTH ·
MARGIN_DINEIN_COMBO · MARGIN_TAKEOUT_COMBO · MARGIN_MARKETPLACE_COMBO.

## Autotest (= ES 644 checks + EN twin)
pycel and cache ± 0.01 against `calcular()` with 3 input sets (defaults, selectors 2/2, and a third set with other oz,
prices and commission) · cost per usable lb = price ÷ usable ÷ (1 − shrink) · balls per lb = 16 ÷ oz · marketplace margin <
take-out < dine-in for the combo and the meal for two · double default FC in 24-32% · weighted FC below the plan's 34% ·
Letter paper, protection, 0 formulas without cache, 0 typed numbers in formulas (except 0/1) · `motor.gate_formatos` 0 · DV ·
docProps · PROHIBIDOS (the sushi/taco/rotisserie/pizza list of `calculadora_sus.py` + «hamburguesería», «bola», «plancha»,
«patata», «fry-top», «value meal», «smashed burger», «rare», «medium-rare», «gluten-free» without negation, «IVA», «RD 1021»,
«Inf26008», «853/2004», «Orden», «AESAN», «polares», «175 °C», «70 °C», «75 °C», «2 °C», «−18 °C», kg, g, ml, liters, €) +
`datos_bur.RX_BUR_NO` + no latinos 0 · then `python3 scripts/productos-digitales/parche_xml_xlsx.py --check <file>` must be
clean (every formula literal ≤ 255 characters).
