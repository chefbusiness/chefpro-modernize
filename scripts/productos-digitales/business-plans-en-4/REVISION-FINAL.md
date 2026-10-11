# Catering Business Plan Kit (EN) — revisión adversarial final (1 ronda) · sesión Claude Code 2026-10-11

Rama `feat/catering-business-plan-en` @ `87737408` (sha256 Mac = VPS). Revisor: 1 Opus, solo lectura (xlsx/docx abiertos en el VPS).
**Veredicto: listo tras arreglar los 5 MAYOR; 0 BLOQUEANTES.** Todo se arregla por la **vía de TEXTO**: ninguna cifra ni fórmula está mal
y `cifras_caso.json` no se mueve.

**Cifras recalculadas a mano** (cuadran al dólar con el xlsx, `cifras_caso.json` y el docx): ventas 180 × 60 × $60 = **$648,000** /
$745,200 / $819,720 · variables 39.4 % ($255,312) → margen bruto 60.6 % · personal (5,000 + 3,640 + 6,060 + 2,210) × 12 × 1.10 =
**$223,212** (34.4 %) · fijos $328,066 · EBT $64,622 · **EBITDA $94,276 (14.5 %)** · neto $48,466 (7.5 %) · año 2 $87,798 · año 3
$116,937 · CAPEX $97,500 + 2,500 + 2,500 + 4,700 = **$107,200** · FM 3 × (328,066 − 15,054) / 12 = $78,253 · **cuota** 146,000 × 0.1 /
(1 − 1.1⁻⁷) = **$29,989** · **DSCR** 78,121 / 29,989 = **2.60×** · **equilibrio** 328,066 / (36.36 × 60) = 150.4 → **151 eventos**; caja
150.5 → 151 · holgura 180/150.5 − 1 = 19.6 % · **payback** 1 + (185,453 − 78,121)/115,913 = **1.9** (CAPEX 1.3) · cobertura 9,180/9,288 =
98.8 % · pesimista 135 × 54 × 55 = $400,950 → −$85,091, caja 78,253 − 85,091 + 15,054 − 15,389 = **−$7,173** · optimista $256,875.
**Calculadora** (pycel, 2 casos propios = mano): 100 invitados / mínimo 120 / plated / margen 45 % / SC 22 % / tax 9.5 % → precio
$80.00, subtotal $9,600, SC $2,112, tax $1,112.64 (SC gravado) o $912.00 (no gravado), total $12,824.64 / $12,624.00, margen 45.2 %,
propina 10 % = $960 fuera del total, 9 servers. DV correctas en las 19 entradas. **Integridad**: 4 ZIP sanos, abren en openpyxl /
python-docx, docProps D20, US Letter en todas las hojas y en el docx (8.5 × 11"). Vocabulario food truck: 0 restos reales
(«generator» = energía portátil de estaciones, correcto). «guests» (asistentes) vs «clients» (compradores): coherente, no se toca.

**Fuentes abiertas:** (1) eldoradocounty.ca.gov/…/Caterers — el caterer opera desde «an approved, permitted food facility» con
«written agreement», el permiso no vale en community events (TFF), y **«the caterer is required to submit the catering operations
standard operating procedures for review… There is an annual health permit fee and plan review fee»**; **no dice** nada de «home».
(2) tax.ny.gov TB-ST-320 — 3 condiciones (aparte, «identified as a gratuity», íntegra al personal); ejemplo 8 % service charge gravado /
15 % gratuity no: conforme. (3) IRS IRB 2012-26, Rev. Rul. 2012-18 — 4 factores de propina; «to the extent any portion of a service
charge… is distributed to an employee it is wages»: conforme, con el matiz de M3. (4) TX 34 TAC §3.293/§3.337 (búsqueda) — ≤ 20 %,
aparte, **identificado como gratuity**, repartido a qualified employees (no chefs). (5) ezCater selling fees (búsqueda) — 15 % + 2.99 %;
7 % ezOrdering: conforme. Alcohol: el kit nunca dice que el caterer pueda vender sin licencia (OK).

## MAYOR

- **M1 · plan review** (docx [103]; `Startup Costs!A15/D15`; checklist `Phase 2!E7`). Dicen «solo si alquilas cocina propia… pon 0», y la
  propia fuente citada cobra plan review a todo caterer y revisa sus SOP; además el ejemplo presupuesta $500 que su nota manda poner a 0.
  - A15 → «Health permit plan / SOP review» · D15 → «Many counties review a caterer's written operating procedures before issuing the
    permit and charge a plan review fee (El Dorado County, CA, does). If you lease your own kitchen, expect a full plan review with layout
    drawings, which costs more.»
  - [103] «A plan review is only needed if you lease your own kitchen.» → «Many counties also review your written operating procedures
    and charge a plan review fee; a full plan review with layout drawings applies if you lease your own kitchen.»
  - `Phase 2!E7` → «Many counties review your catering SOPs and charge a plan review fee before issuing the permit; a full plan review
    applies if you lease your own kitchen. Expect an application, a fee, a menu review and an inspection of the kitchen and the van.»
- **M2 · combustible contado tres veces y contra el propio libro.** `3-Year P&L!A27` «Van fuel, maintenance and inspections» ($6,000 FIJO)
  + `Assumptions!C28`/`P&L F51`/`Instructions D56` (combustible en el 3 % variable) + utilities. `Instructions!D49` dice que meter el
  combustible en fijos «distorts the break-even» y `D43` que escribirlo dos veces lo cuenta doble.
  - `P&L!A27` → «Van maintenance, repairs and inspections» · `P&L!F27` (vacía) → «Oil, tires, brakes, refrigeration-unit service and
    inspections: they follow the calendar, not the events. Fuel for trips to venues is in "Miscellaneous and contingency", a % of sales.»
  - docx [82] «…and a fuel and maintenance line in the P&L.» → «…and a maintenance line in the P&L; fuel for each trip sits in the
    variable costs, so it moves with the number of events.» · `Instructions!A43` → «Generator and burner fuel».
- **M3 · «price per guest» con dos definiciones + service charge sin destino.** El libro: `B5` «service included»; la calculadora:
  `B32` «Excl. service charge», y `Assumptions!C5` remite a la calculadora para ese precio (si te quedas el 20 %, ventas −17 %).
  Rev. Rul. 2012-18 solo hace salario la parte que se reparte al personal.
  - `Assumptions!C5`: «…the Pricing Calculator in this kit builds the price per guest for each service style.» → «…the Pricing Calculator
    builds a quote per service style; to bring it here, divide its subtotal plus the service charge you keep by the billable guests (its
    own price per guest excludes the service charge).»
  - Calculadora `C19` → «Added on top of the price per guest. The part you pay out to staff is wages, not tips (IRS Rev. Rul. 2012-18),
    with payroll taxes; the part you keep is revenue. Kit estimate.» · `C32` → «Excl. service charge and sales tax; staff wages are
    already inside it.»
  - docx [106] «…a mandatory service charge is wages, not a tip.» → «…a mandatory service charge is not a tip: whatever part of it you
    pay out to staff is wages.» · checklist `Phase 4!E14` → «A mandatory service charge is not a tip: the part paid out to staff is
    wages (IRS Rev. Rul. 2012-18). A gratuity is voluntary and goes to staff. Keep them on separate invoice lines and check your
    state's sales tax rule.»
- **M4 · atribución legal que la fuente no hace** (docx [64], [102]): El Dorado no dice «prohibits preparing the food at home».
  - [64] → «…one California county health department requires catering operations to work from an approved, permitted food facility
    under a written agreement for its use, which a home kitchen is not.»
  - [102] → «…and in California, according to the environmental health guidance of one county (eldoradocounty.ca.gov), a catering
    operation must work from an approved, permitted food facility, with a written agreement for that kitchen, and have its operating
    procedures reviewed before the permit is issued.»
- **M5 · el pesimista del docx contradice al libro** (docx [99] vs `Scenarios!E23` «The SAME staffing in all three scenarios»). «In the
  pessimistic case, labor cost also falls as events fall… which softens the result…» → «The workbook keeps labor at the base-case level
  in all three scenarios, so this is a cautious figure: in a real slow year you would schedule fewer event-staff hours, which softens
  the loss but does not remove the risk.»
## MENOR

| # | Dónde | Arreglo (texto) |
|---|---|---|
| m1 | `P&L!F53` | «plus disposables» es falso (B53 = comida + bebida): «Ceiling for food + beverage cost of goods (disposables have their own line): kit benchmark (editable estimate), based on the 28-35% food cost range…» |
| m2 | docx [97]; `Break-Even!E24`; `Assumptions!C67` | 20 % = plan ÷ equilibrio − 1; lo que se puede caer es 16 %. [97] → «…compared with 180 events in the plan: the plan sits 20% above the cash break-even, so events could fall by about 16% before cash stops covering costs.» E24 → «How far the plan sits above the cash break-even (plan ÷ break-even − 1); the drop you can absorb is 1 − break-even ÷ plan.» (deuda común de la familia) |
| m3 | docx [43], [87] | Libro = nómina mensual constante. [43] «so labor cost rises and falls…» → «so in practice their hours rise and fall with the number of events»; [87] añadir «The workbook spreads this pool evenly over the year, which keeps the plan cautious in quiet months.»; [86] «The fixed crew costs» → «Labor costs» y «the owner's draw» → «the owner's salary» (el modelo le aplica cargas de nómina) |
| m4 | `Assumptions!C20` | 10 % vs «15-30%» de `Instructions!D64`: «…+ workers' comp. The example uses a lean 10% with no benefits; the benchmarks table on "Instructions" gives 15-30% with benefits. Ask your payroll provider and carrier for your rate.» |
| m5 | checklist `Phase 1` filas 6-7 | El EIN va después de la LLC (la IRS pide la entidad formada): intercambiar el texto de las filas 6 y 7 (B-E); D «Weeks 1-2» la LLC y «Weeks 2-3» el EIN; E del EIN empieza «Apply once the state approves your LLC.» |
| m6 | checklist `Phase 6!B11/E11`; docx [98] | B11 → «Send the final invoice within 48 hours; track deposits and balances»; E11 → «Private clients usually pay the balance 5-7 days before the event; invoice overages within 48 hours and follow corporate invoices on their 30-day terms.» [98] «Corporate clients often pay after 14 days on average» → «The workbook assumes clients pay 14 days after the event on average (weddings prepaid, companies often at 30 days)» |
| m7 | calculadora `C21`, `Instructions!A13`; docx [106] | NY/TX: «…separately stated, **identified as a gratuity** and paid to qualified employees (servers and bartenders, not chefs); over 20% all of it is taxable in TX» |
| m8 | `Instructions!D66` | Añadir: «The example ($107,200 before working capital) sits above this range because it buys a refrigerated van ($41,000 with its unit) and its own serving equipment.» |
| m9 | `Staffing!A24` | 488 car. en col. A (34) a 194.5 pt: la última línea puede cortarse. → «Columns D-G are TOTALS for the row: the event staff row covers all its people. Event staff (servers, bartenders, attendants) are hourly W-2 employees with payroll taxes and workers' comp; paying them as 1099 contractors is a misclassification risk (FLSA; California AB5). Tax rate and pay periods: "0. Assumptions".» |
| m10 | `12-Month Cash Flow!O5` | Sin wrap en la última columna (patrón de la familia): 363 car. se cortan al imprimir. → «Share of the year's events per month (100% in total). Month 1 = opening month (March in the example): rotate the row.» |
| m11 | `Assumptions!C39`; `Startup Costs!D21` | C39 «UK: 20% VAT on hot food and dine-in» → «UK: 20% VAT applies to catering for events and functions (VAT Notice 709/1)»; D21 (cadena de la fórmula) «when the lease ends» → «when the commissary agreement ends» |
| m12 | docx [114] | Los seguros están en Phase 2, no en la 1: «…you form the LLC, get your EIN, open the bank account and register for the seller's permit. "Phase 2 - Kitchen, Van, Permits" covers the commissary agreement, the health permit, the van and your insurance.» |
| m13 | docx [40], [105] | «The usual model is simpler:» → «Where your state and the venue allow it, the usual model is simpler:»; [40] «the client buys the alcohol» → «the client buys the alcohol where the venue and state rules allow it» |
| m14 | checklist `Phase 2!E6`, `B13`; `Phase 3!B10` | E6 «The health department requires it.» → «Most health departments ask for it with the permit application.»; B13 → «general liability (or a business owner's policy)»; B10 → «…a broadline distributor (US Foods, Sysco) and a cash-and-carry such as Restaurant Depot» |

Aceptadas las desviaciones de F2-NOTAS §4 (pestaña de 31 car., umbral 60 % explicado en F51, B4 = 180 y pool 0.23 FTE —D15 cumple
aun con la holgura estricta, 16.4 %—, B51 informativo); D19: 8 filas con fuente leída en F1 y 6 «Kit estimate» declaradas.
