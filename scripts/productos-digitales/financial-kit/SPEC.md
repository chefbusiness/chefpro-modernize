# Restaurant Financial Plan Kit Pro — SPEC (F1 · 3-oct-2026 · sesión Claude Code)

> Sexto producto de la **Tienda internacional en inglés**: la edición EN del **Kit Plan Financiero para Restaurantes**
> (`kit-plan-financiero`, 39 €, v2.0, 8 plantillas + 2 bonus; decisiones ES en `kit-plan-financiero-v2-SPEC.md`). Doc
> canónico: `TIENDA-INTERNACIONAL.md`. Método calcado de `staff-kit/` (F1 → F2 por capa sobre los xlsx publicados) y,
> para los gráficos, de `recipe-costing-kit/`. Base: `F1-inventario-es.md`, `censo_es.json`, `textos_es.json`
> (`extraer_textos.py`) y `mapas.py` (autotest + cruce con el censo, 0 errores). Esta SPEC **decide**; lo que no está
> aquí no se hace. Tamaño **M** ($49): techo 5 M tokens; esta F1 ≈ 0,3 M.

## 0. Reglas que mandan (John)

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 10 libros, 56 hojas, rangos, merges, gráficos, paneles,
  protección (sin contraseña) y semáforos. Lo que el mercado US exige DENTRO de un entregable (un parámetro, una
  columna, un rótulo) se aplica, se declara aquí (D8-D16) y el gate lo admite por nombre.
- **Mercado: base US con notas UK** (TIENDA §1). Fiscalidad = **parámetros editables**, nunca ley clavada en una
  fórmula. Moneda sin símbolo («in your currency»), US Letter, fecha US, sq ft.
- Textos de producto con **subagentes Anthropic** (regla 1bis), nunca bridge.py. Landing = la ES replicada, sin
  `aggregateRating` ni `review` (TIENDA §3.5), testimonios traducidos con subtítulo de edición española.
- Proporcionalidad: una pasada de research (DataForSEO US + PAA + una búsqueda SBA), un implementador por fase, gates
  de script, una revisión final. Cada cifra normativa o de benchmark lleva su fuente una vez (§3).

## 1. Decisiones

| D | Tema | Decisión | Estado |
|---|---|---|---|
| D1 | Slug | `restaurant-financial-plan-templates` → `/en/digital-products/restaurant-financial-plan-templates` (+ `/access`, `/library`). productId = slug; JWT `restaurant-financial-plan-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT`; ficheros en `dl/restaurant-financial-plan-templates/` | DECIDIDA |
| D2 | Nombre | **Restaurant Financial Plan Kit Pro** en landing, schema, dashboard, email, docProps, marca y versión. Title SEO = H1 (Forma B): «Restaurant Financial Plan Kit Pro: Restaurant P&L Template & Financial Projections for Excel» (US: «restaurant p&l template» 140/mes, «restaurant profit and loss template» 140, «restaurant budget template» 70, «restaurant startup costs spreadsheet» 20, «restaurant pro forma template» 20) | DECIDIDA |
| D3 | Precio | **$49 USD**, pago único, acceso de por vida. Familia `kit-plan-financiero` en `tienda.ts` (F3) | DECIDIDA |
| D4 | Anclas | Como el ES (190 € y bonos de 14 €) al escalón psicológico USD superior: `priceOld` **$199**; bonos **$19** cada uno ($38; valor total $237); ahorro $150; descuento 1 − 49/199 → «-75%» en hero Y buyBox (el «72 %» del ES no se copia) | DECIDIDA |
| D5 | Ficheros y títulos | Tabla §2.1. `Instructions!B2` = `mapas.titulo_interior` («NN · título», «BONUS 08 · …»); docProps `title` = «NN · título · Restaurant Financial Plan Kit Pro». Cita de otro fichero en texto: `file NN "nombre corto"` (`mapas.NOMBRES_CITA`, un solo nivel) | DECIDIDA |
| D6 | Pestañas | Tabla §2.2 (41 nombres, meses incluidos). El renombrado reescribe en el mismo paso las 577 con referencia a hoja, las referencias de los 9 gráficos y los títulos de impresión; en texto, pestañas entre comillas dobles rectas ("Monthly Cash Flow") | DECIDIDA |
| D7 | Claves | Un solo diccionario `mapas.CLAVES` (36): literales de fórmula y de CF e ítems de la DV del BONUS-09, en **un solo paso**. Tokens de CF 1:1; **ningún mensaje EN cambia de color** (SEARCH casa subcadenas); lo prueba `mapas.cruzar_censo` | DECIDIDA |
| D8 | Sales tax / VAT | Ingresos **excl. sales tax** en 01, 01b, 02, 05, 06, 07, B08 (glosario); el 03 es caja **incl.** el impuesto cobrado. 03 `Assumptions`: C7 impuesto sobre ventas **8 %** [ejemplo; cada usuario pone su state + local; UK 20 %], C8 y C9 «recoverable tax» **0** (el sales tax no tiene crédito por compras; UK 20 % / alimentos 0 %). Fila 25: misma fórmula, **declarante trimestral** (abril, julio, octubre; enero = input del Q4 anterior); declarante mensual → desproteger y teclear; UK: 1 mes + 7 días. Textos en `FIJOS` | DECIDIDA |
| D9 | Nóminas en el 03 | Fila 18 «Employer payroll taxes deposited (last month's)» ← fila 34 «accrued this month» (depositante mensual, IRS Pub. 15: el 15 del mes siguiente); fila 24 «Employee taxes withheld, deposited (income tax + FICA)»; fila 17 «Payroll (net pay)». Mismas fórmulas; UK PAYE el 22 | DECIDIDA |
| D10 | CAPEX (04) | C = **Recoverable tax %**: US **0** (el sales tax va dentro del coste: forma parte de la base del activo), UK 20 %. H = **Useful life (years)**, lineal, libro: obra 10 (el menor de plazo del alquiler y vida útil), cocina 7, mobiliario 7, tecnología 5 [kit estimate], licencias y tasas vacío (gasto; licencia de obras y proyecto técnico = 10, D33). **Único patrón que cambia**: `=$B{r}*$H{r}` → `=IFERROR($B{r}/$H{r},0)` (48 celdas). La DV 0-1 que cubría C y H se parte en 2 (**5 DV partidas**: H decimal 0-50, título «Invalid useful life»). MACRS/Section 179 y capital allowances UK solo en nota | DECIDIDA |
| D11 | Coste de personal | 02 `Inputs!B7` «gross wages + employer payroll taxes», nota «≈ gross wages × 1.10 (more with benefits)» [kit estimate: FICA 7,65 % + FUTA/SUTA + workers' comp]. «Gestoría» → «accounting / bookkeeping» | DECIDIDA |
| D12 | Informe para el banco (07) | → **Lender & Investor Summary** («Referencia Bancaria» → «Typical lender guideline (indicative)», D35). Impuesto: «Effective income tax rate» C29 = **25 %** (21 % federal C corp + estatal; pass-through = 0; UK 19-25 %), fórmulas iguales. Préstamo de ejemplo tipo **SBA 7(a)**: C5 **10 %** nominal («not APR»), C6 **10 años**, carencia → **interest-only period** (vacío). TIR/VAN/payback sin cambios (DSCR: D25); la caché de la TIR se recalcula (Newton, `cachear_irr` del ES) | DECIDIDA |
| D13 | Ratios y garantías (07) | DSCR: objetivo **1.25×** (objetivo habitual del prestamista, orientativo) y límite **1.15×** («Limit» editable del kit, **sin etiqueta SBA**: el suelo SBA depende de la operación y del SOP vigente), valores ya del ES. Fondos propios / inversión: límite G9 0.20 → **0.10** (aportación propia habitual en start-ups, orientativa; la deciden el prestamista y el SOP vigente); el resto, kit benchmark sin cambio. *Enmendada en la revisión final.* `Collateral`: personal guarantee (SBA: socios ≥ 20 %), mortgage, pledged deposits, blanket lien (UCC-1), assignment of life insurance, additional deposit (`FIJOS`) | DECIDIDA |
| D14 | Unidades | m² → **sq ft**: 06 `Ratios!C11` 80 → **860**; «Sales per sq ft»; 07 «Total area (sq ft)»; aviso «Enter the dining room sq ft» | DECIDIDA |
| D15 | Benchmarks (06) | Reglas US full-service [kit estimate]: **labor 30 % / 35 %** (ES 25/30) y **ocupación 6 % / 10 %** (ES 8/12) en F:G y en sus textos (`POR_CELDA`); food 28/32, prime 60/65, GOP, EBITDA 15/10, bebida 18/24, margen bruto, coste/ticket sin cambio; RevPASH «per seat-hour» sin moneda (6/3). `Benchmarks!B17` reescrita (I3) | DECIDIDA |
| D16 | Checklist (B09) | 54 tareas en 7 fases; **35 tareas** con trámite español pasan a su equivalente US por `FIJOS` (entidad LLC/S/C corp, articles, DBA, EIN, seller's permit, USPTO, SBA 7(a), business license y certificate of occupancy, health permit, fire inspection, liquor license, workers' comp, liquor liability, employer registration, posters, I-9/W-4, new-hire reporting, Form 941); el resto se traduce. Contador y CF sin cambio | DECIDIDA |
| D17 | Moneda | Cero `€`: las 3.273 celdas con formato € → `#,##0.00`; rótulos sin «(€)»; «€/mes» → «per month»; título de eje «€» → «Amount» | DECIDIDA |
| D18 | Formato | `dd/mm/yyyy` → `numFmtId 14`; `0.0" p.p."` → `0.0%` (I1: 64 celdas); `" años"` → `" years"`; «p.p.» en texto → «pts»; **US Letter** (`paperSize 1`) en las 56 con la misma orientación y ajuste; pie `mapas.FOOTER_EN` | DECIDIDA |
| D19 | Gráficos | 9 gráficos y 20 series con el mismo tipo, ancla y rangos; títulos traducidos (traductores), eje por D17, referencias con pestaña EN; los nombres de serie salen de cabeceras ya traducidas | DECIDIDA |
| D20 | Versión y marca | «Version 2.0 · <mes> 2026 · aichef.pro/en/digital-products/restaurant-financial-plan-templates · info@aichef.pro»; marca `mapas.MARCA_EN`; docProps: `subject` «Restaurant Financial Plan Kit Pro · v2.0», `keywords` «restaurant p&l template, restaurant financial projections, restaurant budget template, break-even, cash flow, AI Chef Pro», `description` = URL, `category` «AI Chef Pro · Digital products». La EN nace en 2.0: los textos que cuentan historia («antes este informe pedía…», «hasta hoy…») explican el porqué sin ella | DECIDIDA |
| D21 | Datos de ejemplo | §5: mismos números (moneda neutra), salvo D8, D10 y D12-D15 | DECIDIDA |
| D22 | Landing | §6 (todas las secciones del ES) | DECIDIDA |
| D23 | Defectos heredados | EN nace corregido de I1-I3 (`F1-inventario-es.md` §3). En el ES se proponen para su próxima v2.x | PROPUESTA (ES) |
| D25 | DSCR a cuota completa (07) · rev. final | `Ratios!C5` = flujo libre año 1 / **cuota anual completa** (`'Loan Schedule'!$C$8`), rótulo «DSCR at full payment»; con interest-only el año 1 solo paga intereses y el DSCR salía inflado. `Ratios!B21`, `Instructions!B15:B16`, `Loan Schedule!B18` coherentes (la cuota se COPIA a mano al 03) | DECIDIDA |
| D26 | SBA en textos · rev. final | Ningún texto (xlsx, landing, changelog) dice «1.15× SBA minimum» ni «10 % SBA minimum»: «1.25× is the usual lender target; the SBA floor depends on the transaction and the current SOP» y «SBA lenders usually expect an owner equity injection (often around 10 % for start-ups)…». G7 lo vigila | DECIDIDA |
| D27 | Plazo de proveedores (03) · rev. final | DV de `Assumptions!C6` 0-30 días (la DV «≥ 0» de C5 C6 C26 se parte: **6 DV partidas** en total) y `MIN(C6,30)` en `Monthly Cash Flow!B16:M16`: el flujo paga cada compra este mes o el siguiente; con > 30 días salían pagos negativos. **El ES tiene el mismo defecto** | DECIDIDA |
| D28 | Base del sales tax (03) · rev. final | `B36:M36` = impuesto sobre filas 7 + 8 + 10 (sala, barra, eventos): fuera el delivery de marketplaces (el marketplace cobra e ingresa el impuesto en la mayoría de estados) y «Other receipts» (capital, préstamos, devoluciones). Nota en `Assumptions!D7`, rótulo A36 | DECIDIDA |
| D29 | Tipo 0 % (07) · rev. final | `Loan Schedule!C8` = `IF(C5=0, C4/(C6-C7), anualidad)` | DECIDIDA |
| D30 | Ventas por sq ft (06) · rev. final | `Ratios!C30` anual (× 12, convención US), rótulo «Annual sales per sq ft»; sin umbrales | DECIDIDA |
| D31 | Balance del 07 · rev. final | `Ratios!C15` = `'Executive Summary'!C14`, `C16` = `'Loan Schedule'!C4` (fórmulas con el estilo de C17; dejan de ser input verde) | DECIDIDA |
| D32 | Ocupación evaluada (06) · rev. final | Fila nueva `Ratios!26` «Occupancy (rent) / Sales» = C38 / C6 con semáforo contra `Benchmarks!F8:G8` (CF E17:E26). Marketing / Sales queda «reference only» (no hay dato de marketing) | DECIDIDA |
| D33 | Licencias capitalizadas (04) · rev. final | `Licenses & Permits!H6:H7` (licencia de obras, proyecto técnico) = 10 años (vida de la obra, US GAAP); el resto de licencias y tasas, vacío (gasto). Nota en J6:J7 | DECIDIDA |
| D34 | GOP (06) · rev. final | Umbrales **21 % / 16 %** = EBITDA 15 / 10 + 6 puntos de ocupación (antes 20/15, incoherentes); textos C7:E7, Instrucciones y nota B19 | DECIDIDA |
| D35 | Benchmarks como estimación · rev. final | «Kit benchmark (editable estimate)», «Kit Benchmarks (editable estimates)», gráfico «Your value vs kit target», 07 «Typical lender guideline (indicative)»; RevPASH 6 / 3 «set for your market» (B13 y nota B18) | DECIDIDA |
| D36 | Aviso legal · rev. final | En las 10 Instrucciones, bajo la versión: «Planning tool, not financial, tax or legal advice. Requirements vary by state and city — check with your accountant and local authorities.»; B09 además «This checklist is a starting point, not an exhaustive list.» | DECIDIDA |
| D37 | Rótulos cortados · rev. final | Ajuste + alto de fila: 01/01b `Year n!A27`, 04 `Kitchen Equipment!A15`, B09 `Checklist!B53:B58` y C5:C58, 06 D16/B30 y `Benchmarks!B17:B19`, 07 `Ratios!D3` | DECIDIDA |
| D24 | Máquina | F2 en el **VPS** (`ssh vps`, `/root/chefpro-modernize`, venv `/root/venv-guias`, `git worktree` de la rama; su `/dev/null` está roto → redirigir a ficheros de `/tmp`); `scp` de vuelta y commit desde el Mac. Si el VPS no responde: Mac en serie con `istats` < 62 °C | DECIDIDA |

## 2. Mapas

### 2.1 Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN (landing, dashboard, B2, docProps) |
|---|---|---|---|
| 01 | `01-plan-financiero-previsional.xlsx` | `01-restaurant-financial-projections-3-year.xlsx` | Restaurant Financial Projections: 3-Year Pro Forma P&L |
| 01b | `01b-plan-financiero-previsional-5-anos.xlsx` | `01b-restaurant-financial-projections-5-year.xlsx` | Restaurant Financial Projections: 5-Year Pro Forma P&L |
| 02 | `02-calculadora-punto-equilibrio.xlsx` | `02-restaurant-break-even-calculator.xlsx` | Restaurant Break-Even Calculator |
| 03 | `03-cash-flow-forecast.xlsx` | `03-restaurant-cash-flow-forecast.xlsx` | Restaurant Cash Flow Forecast (12 Months) |
| 04 | `04-presupuesto-inversion-capex.xlsx` | `04-restaurant-startup-costs-budget.xlsx` | Restaurant Startup Costs & Capex Budget |
| 05 | `05-pyl-mensual-real-vs-presupuesto.xlsx` | `05-restaurant-pl-template-budget-vs-actual.xlsx` | Restaurant P&L Template: Monthly Budget vs Actual |
| 06 | `06-dashboard-ratios-financieros.xlsx` | `06-restaurant-kpi-ratios-dashboard.xlsx` | Restaurant Financial Ratios & KPI Dashboard |
| 07 | `07-informe-viabilidad-bancos.xlsx` | `07-restaurant-loan-proposal-lender-summary.xlsx` | Restaurant Loan Proposal: Lender & Investor Summary |
| B08 | `BONUS-08-simulador-escenarios.xlsx` | `BONUS-08-what-if-scenario-simulator.xlsx` | BONUS: What-If Scenario Simulator |
| B09 | `BONUS-09-checklist-pre-apertura.xlsx` | `BONUS-09-pre-opening-financial-checklist.xlsx` | BONUS: Pre-Opening Financial Checklist (54 Tasks) |

### 2.2 Pestañas (D6) — 56 hojas, 41 nombres

| Libro | Pestaña ES | Pestaña EN | Libro | Pestaña ES | Pestaña EN | Libro | Pestaña ES | Pestaña EN |
|---|---|---|---|---|---|---|---|---|
| todos | `Instrucciones` | `Instructions` | todos | `Año 1` | `Year 1` | todos | `Año 2` | `Year 2` |
| todos | `Año 3` | `Year 3` | 01b | `Año 4` | `Year 4` | 01b | `Año 5` | `Year 5` |
| todos | `Resumen` | `Summary` | 02 | `Datos` | `Inputs` | 02 | `Break-Even` | `Break-Even` |
| 02 | `Escenarios` | `Scenarios` | 03 | `Parámetros` | `Assumptions` | 03 | `Flujo Mensual` | `Monthly Cash Flow` |
| 03 | `Alertas` | `Cash Alerts` | 04 | `Obra` | `Build-Out` | 04 | `Equipamiento Cocina` | `Kitchen Equipment` |
| 04 | `Mobiliario Sala` | `Dining Room FF&E` | 04 | `Tecnología` | `Technology` | 04 | `Licencias` | `Licenses & Permits` |
| 04 | `Otros conceptos de apertura` | `Other Opening Costs` | 05 | `Ene` | `Jan` | 05 | `Feb` | `Feb` |
| 05 | `Mar` | `Mar` | 05 | `Abr` | `Apr` | 05 | `May` | `May` |
| 05 | `Jun` | `Jun` | 05 | `Jul` | `Jul` | 05 | `Ago` | `Aug` |
| 05 | `Sep` | `Sep` | 05 | `Oct` | `Oct` | 05 | `Nov` | `Nov` |
| 05 | `Dic` | `Dec` | 05 | `Resumen Anual` | `Annual Summary` | todos | `Ratios` | `Ratios` |
| 06 | `Benchmarks` | `Benchmarks` | 07 | `Resumen Ejecutivo` | `Executive Summary` | 07 | `Proyecciones` | `Projections` |
| 07 | `Financiación` | `Loan Schedule` | 07 | `Garantías` | `Collateral` | B08 | `Simulador` | `Simulator` |
| B08 | `Comparativa` | `Comparison` | B09 | `Checklist` | `Checklist` | | | |

Los meses en celdas (cabeceras de 01, 01b, 03 y 05) usan el mismo mapa (`mapas.MESES`).

## 3. Reglas US/UK (fuente única de las cifras; `mapas.REGLAS_US`, `VALORES_EN`)

| Concepto | ES (publicado) | EN | Fuente |
|---|---|---|---|
| Impuesto sobre ventas | IVA 10 % repercutido; soportado 10/21 % deducible | sales tax de un solo escalón, sin crédito; 8 % = ejemplo; reventa con resale certificate | Tax Foundation «State and Local Sales Tax Rates» [8 % = kit estimate] |
| VAT UK | — | 20 % al comer en el local y comida caliente; casi todo alimento 0 % | HMRC VAT Notice 709/1 |
| Plazo del impuesto | modelo 303: abril, julio, octubre, enero | trimestral (por defecto); UK 1 mes + 7 días | estado de cada usuario; gov.uk/vat-returns/deadlines |
| Cargas de empresa | SS ≈ bruto × 1,32, pago al mes siguiente | ≈ × 1.10; depósito mensual el 15 del mes siguiente | IRS Publication 15 §11; IRS Topic 759 (FUTA 0,6 % sobre $7.000) |
| Retenciones | IRPF mod. 111 | income tax + FICA retenidos (Form 941); UK PAYE el 22 | IRS Publication 15; gov.uk/pay-paye-tax |
| Impuesto sobre beneficios | IS 25 % (15 % nueva creación, art. 29.1 LIS) | 25 % efectivo = 21 % federal + estatal; pass-through 0; UK 19-25 % | IRC §11(b); IRS «Business structures»; gov.uk/corporation-tax-rates |
| Amortización | coeficientes 3/12/10/25 % | lineal, vida útil 10/7/7/5 años [kit estimate]; leasehold improvements: menor de alquiler y vida | ASC 842-20-35-12; nota fiscal: IRS Pub. 946, IRC §168(e)(6); UK AIA gov.uk |
| Préstamo | TIN 6 %, 8 años, carencia | 10 % nominal, 10 años, interest-only [ejemplo] | SBA 7(a): 13 CFR 120.212-120.214 |
| DSCR | > 1,25× | objetivo 1.25× (habitual del prestamista); límite 1.15× del kit, sin etiqueta SBA (D26) | [kit estimate] práctica de banca; SBA SOP 50 10 vigente |
| Aportación propia | > 30 % / límite 20 % | > 30 % [kit]; límite 10 % (habitual en start-ups, orientativo) | SBA SOP 50 10 vigente [orientativo] |
| Aval | aval del promotor, SGR | personal guarantee de socios ≥ 20 % | 13 CFR 120.160(a) |
| Benchmarks | labor 25/30, alquiler 8/12, GOP 20/15 | labor 30/35, ocupación 6/10, GOP 21/16 (D34); RevPASH 6/3 en USD; resto igual | [kit estimate] reglas full-service US |
| Superficie | 80 m² | 860 sq ft (1 m² = 10,764 sq ft) | NIST SP 811, Appendix B |
| Cobro con tarjeta | 65 % | 80 % | [kit estimate] |

## 4. Qué cambia en cada libro además de la traducción

| # | Cambio |
|---|---|
| 01 / 01b | D8 (glosario «excl. sales tax»); comisión de delivery 30 % se queda (15-30 % en apps US; regla del sector) |
| 02 | D11 (`Inputs!B7`, D7); «€/mes» → «per month» |
| 03 | D8, D9 (`Assumptions` C4, C7:C9 y textos D7:D9, B28; `Monthly Cash Flow` A17, A18, A24, A25, A34, A36, A37) |
| 04 | D10 (cabeceras de las 7 hojas, columna H, patrón de I, 5 DV partidas, licencias A5:A12, otros conceptos, `Summary!A12`, `A16`) |
| 05 | D18 (formato p.p.); pestañas de mes |
| 06 | D14, D15 (C11, F5:G5, F8:G8, textos de `Benchmarks`, B17); «Labor Cost %» de Instrucciones |
| 07 | D12, D13 (A15, A29:A30, A28 sin «referencia habitual», `Loan Schedule` C5:C6 y notas, `Ratios!G9`, `Collateral`), D14 |
| B08 | traducción; mismos escenarios |
| B09 | D16; docProps con 54 tareas (I2) |

## 5. Datos de ejemplo (D21) — los traductores los usan tal cual

- Restaurante casual pequeño de 60 plazas: ticket 22, 55 covers/día, 26 días, ventas 31,460 al mes, EBITDA ≈ 17.3 %
  (02, 06, B08), saldo inicial 15,000 y umbral 5,000 (03), descuento 8 %, impuesto 25 % (07). Cifras en formato US
  («31,460», «17.3%») y sin símbolo de moneda.
- Glosario: comedor → dine-in; barra → bar; cubiertos → covers; ticket medio → average check; facturación → revenue;
  personal → labor; gestoría → accounting / bookkeeping; TPV → POS; datáfono → card terminal; amortización (activo) →
  depreciation; amortización (préstamo) → principal repaid; cuadro → amortization schedule; carencia →
  interest-only period; TIR/VAN → IRR/NPV; BAI → EBT; fondos propios → owner's equity; banco → lender.

## 6. Landing EN — réplica de `kit-plan-financiero.ts` en `data/productos-en/kits/restaurant-financial-plan-templates.ts`

| Sección ES | Tratamiento EN |
|---|---|
| `seo` / `schema` | title = H1 de D2; description «10 Excel templates for restaurant financial planning: P&L template budget vs actual, 3- and 5-year projections, break-even, cash flow, startup costs, KPIs and a lender summary with IRR, NPV and DSCR. $49»; `49.00` USD; **sin rating ni reviews**; `schema.faqs` = FAQ EN |
| `hero` | badge sin cifra sin fuente: «Lender-ready: IRR, NPV, payback and DSCR calculated for you»; `Restaurant ` + gold `Financial Plan` + ` Kit Pro`; subtítulo «Plan, Track and Present Your Numbers»; 5 checks del ES; CTA «BUY NOW — $49» |
| `grid` | 8 + 2 tarjetas con los títulos de §2.1; descripciones con lo que hacen de verdad (excl. sales tax, quarterly sales tax in the cash flow, useful lives, DSCR) |
| `why` | «Built for restaurants» · «Templates that agree with each other» (mismas líneas y base; sin enlaces entre libros) · «Lender-ready format» (sin garantizar aprobación) · «An advisor bills by the hour; this is $49, once» (sin cifra) |
| `bonus`, `buyBox`, `cta`, `pricing`, `stickyLabel` | D3-D4; anclas e ids de sección iguales al ES; tres puertas cripto |
| `faqs` | PAA de «restaurant p&l template»: «How to do a P&L for a restaurant?» · «Can I create my own P&L statement?» · «How to calculate profit and loss for a restaurant?» · «What is the 30/30/30 rule for restaurants?» (regla orientativa; el kit mide food, labor y prime contra `Benchmarks`) · «What is a reasonable profit margin for a restaurant?» (solo con el benchmark del kit, EBITDA 10-15 % [kit estimate], o con fuente citada en F3) + las 6 del ES adaptadas («Will a lender accept it?» = estructura, no aprobación; SBA) + «Does it work in the UK?» (VAT, corporation tax: parámetros) + Google Sheets **solo si el test de F3 lo confirma** |
| `testimonials` | los del ES traducidos tal cual, subtítulo «…with the Kit Plan Financiero, the Spanish edition of this kit» |

Dashboard (F3): `…/library` con la isla del ES copiada y traducida (10 descargas, títulos §2.1); `…/access` con
`ProductAccessGate`; email EN; ficheros en `astro-site/public/dl/restaurant-financial-plan-templates/`.

## 7. Plan de F2 (entregables, en el VPS — D24)

1. `extraer_textos.py` ✅ → 719 cadenas: **G1** 299 (comunes + 01-05, 1.664 palabras) · **G2** 239 (06-B09, 1.524
   palabras) · GM 181 sin traducir (pestañas, meses, claves, 103 fijos, `POR_CELDA`, versión, marca, pie, docProps).
2. **Traducción**: 2 subagentes sonnet. G1 PRIMERO (fija glosario §5 y la línea de firma/desprotección); G2 después
   con el glosario de G1. Cada uno recibe sus cadenas (`donde`, `pistas`, `cita_hojas`, `en_mapa`), §1-§5,
   `mapas.CLAVES`, `FIJOS`, `NOMBRES_CITA` y `TITULOS`. Salida `textos_en/G<n>.json` = `{id: en}`. Mensajes de DV
   ≤ 255 y títulos ≤ 32; nada de IDs internos. Barrido de no latinos y de español al recibirlos.
3. **`aplicar_en.py`** (copia adaptada del staff-kit + `restaurar_graficos` del recipe-costing-kit): copiar los 10 ES →
   hojas y referencias (fórmulas, DV, CF, gráficos, títulos de impresión) → `FORMULAS_EN` → `CLAVES` en fórmulas, CF
   (fórmula **y** atributo `text`) y DV → `DV_PARTIDAS` → textos por aparición → `FIJOS`, `POR_CELDA` y regenerados
   (título interior, versión, marca, pie, docProps) → `VALORES_EN` → `FORMATOS_EN` → Letter → protección idéntica →
   guardar con nombre EN → `inject_cache.py` → **caché de la TIR** (`cachear_irr`, pycel no evalúa `IRR`). Ajuste de
   texto y alto de fila donde el EN sea más largo (`AJUSTE_TEXTO`, a medir en el dry-run). `--dry-run`, `--idempotencia`.
4. **`gates_en.py`** (§8) + `--autotest` con defectos inyectados → UNA revisión adversarial (sonnet: lente de un
   lender/CPA US + lente técnica). Tope 2 rondas.
5. `restaurant-financial-plan-templates` en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de
   `censo-entregables.py`.

Presupuesto: F1 ≈ 0,3 M · F2 ≤ 2,5 M · F3 ≤ 1,5 M. Si el total pasa de 6,5 M (techo + 30 %), se para y se reporta.

## 8. Gates de F2 (contra `censo_es.json`, nunca cifras fijas)

- **G1 Paridad**: 56 hojas vía §2.2; 2.437 fórmulas idénticas tras HOJAS + CLAVES salvo el patrón D10 (celda a
  celda); 60 DV + 6 DV partidas (5 de vida útil + 1 de plazo de proveedores, D27; mismo tipo salvo la parte nueva; unión de sqref = la del ES); 59 CF (sqref, tipo, prioridad,
  relleno); 9 gráficos y 20 series (tipo, ancla, rangos con pestaña EN); 83 merges; 41 títulos de impresión;
  42 paneles; 56 hojas protegidas sin contraseña con los mismos flags; 2.082 celdas verdes y 2.187 desbloqueadas.
- **G2 Restos**: cero español, `€`, «m²», caracteres no latinos, coma decimal, normativa ES (`RX_NORMA`) e IDs
  internos en valores, literales, DV, CF, gráficos, pies y docProps; las 3.273 celdas con formato € reescritas; citas
  a otro fichero con un solo nivel; DV con título ≤ 32 y mensaje ≤ 255.
- **G3 Formato**: `paperSize 1` en 56; fechas 14; `0.0%` en las 64 de I1; pie, marca, versión, docProps D20;
  `Instructions!B2` = título interior; ajuste de texto donde se declare.
- **G4 Claves**: cada ítem de la DV del B09 ∈ `CLAVES`; cada celda de estado igual a un ítem.
- **G5 CF**: tokens EN inyectivos por rango y cada mensaje EN con el mismo color que su ES (`mapas.cruzar_censo`).
- **G6 Cálculo**: caché sin errores; caché EN = caché ES salvo lo que mueven D8, D10, D12-D15 (lo recalcula pycel);
  TIR cacheada (caso del ES: −150,000 / 30,000 / 45,000 / 60,000 / 70,000 → 11.9592 %); un caso D10 (coste 7,000,
  vida 7 → 1,000; vida vacía → 0); 06 C30 = ventas × 12 / 860. Revisión final: préstamo 100,000 al 10 % / 10 años
  con 1 año interest-only → cuota 17,364.05 y DSCR 30,000 / 17,364.05 = 1.73× (antes 3.00×); tipo 0 % → cuota 10,000;
  03 con ventas de ejemplo → pago de abril 3,120 (base 7 + 8 + 10; antes 4,951.11) y plazo 45 días → B16 = 0.
- **G7 Reglas**: cada cifra de `VALORES_EN` coincide con §3 (`mapas.REGLAS_US`); `TEXTOS_NUEVOS`, `POR_CELDA` y
  `UMBRALES_TEXTO_EN` escritos; ningún texto con «SBA minimum» ni «1.15»; tope de 30 días en las 12 celdas (D27).
- **Fórmulas declaradas** (rev. final): `mapas.PARCHES_FORMULA` (D25, D27-D30, en espacio ES), `FORMULAS_NUEVAS` (D31-D32),
  `CF_SQREF_EN` (D32); G1 las exige tal cual y el resto idéntico al ES; G6 las aplica a la referencia.
- **G8** `censo-entregables.py --only restaurant-financial-plan-templates --fail` y `gate-no-latinos.py` en 0.

## 9. F3 y lo que decide John

Checklist de `TIENDA-INTERNACIONAL.md` §6 (familia `kit-plan-financiero` con `en: {slug:
'restaurant-financial-plan-templates', vivo: true}`, 5 fuentes del backend con `lang: 'en'`, `product-prices.ts` en
USD, `zona-app.ts`, gates LIVE, broadcast EN en la cola de 5 días; enlaces entrantes desde el hub EN, el catálogo, los
banners del blog EN y los kits EN hermanos; anclas de D4). Test real en Google Sheets (IRR, gráficos, protección) antes
de afirmarlo en la FAQ. **John**: el Payment Link USD $49 con redirección a
`/en/digital-products/restaurant-financial-plan-templates/access?session_id={CHECKOUT_SESSION_ID}`.
