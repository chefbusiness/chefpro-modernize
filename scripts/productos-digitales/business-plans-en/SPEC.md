# Food Truck Business Plan Kit + Coffee Shop Business Plan Kit (EN) — SPEC (F1 · 4-oct-2026 · sesión Claude Code)

> Productos 7 y 8 de la **Tienda internacional en inglés**: ediciones EN de `plan-negocio-food-truck` y
> `plan-negocio-cafeteria` (29 €, v2.2, motor común `planes-v2_0`). Doc canónico: `TIENDA-INTERNACIONAL.md`. Base:
> `F1-inventario-es.md` (estructura y lo español) y `F1-research-us.md` (demanda, SERP, cifras con fuente, caso de
> ejemplo US). Método calcado del `financial-kit/` (F2 por capa sobre los ficheros publicados) y de sus decisiones, que
> se **reutilizan** donde aplican (D8, D11-D13, D17-D18, D26, D35-D36 de `financial-kit/SPEC.md`; glosario
> `financial-kit/textos_en/glosario*.json`; `FOOTER_EN`/`MARCA_EN`/`FORMULAS_EN`/`CLAVES` de `financial-kit/mapas.py`).
> Esta SPEC **decide**; lo que no está aquí no se hace. Tamaño **M** cada uno ($39): techo 5 M; los dos juntos ≤ 4,5 M.

## 0. Reglas que mandan

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 6 ficheros, mismas hojas, filas, fórmulas, DV, CF, merges,
  protección sin contraseña, paneles y verdes; mismo docx de 10 secciones párrafo a párrafo. Lo que el mercado US
  exige dentro de un entregable se declara aquí como excepción (§1.1) y el gate la admite por nombre.
- **Mercado: base US con notas UK** (TIENDA §1). Impuestos = parámetros editables; moneda sin símbolo; US Letter; fecha
  US; sq ft; galones donde haya litros. Un SKU para US/UK/CA/AU.
- Textos con **subagentes Anthropic** (regla 1bis); nada de bridge.py. Landing = la ES replicada con la plantilla que ya
  acepta `lang` (`PlanNegocioLandingPage.astro`, commit `b734fe33`): no se toca su HTML ES.
- **Al duplicar se duplican los errores del ES** (lección del 3-oct): §6 lista las afirmaciones que no cruzan el EN.
- Proporcionalidad: research en una pasada (hecho), un implementador por fase, gates de script, una revisión final.

## 1. Decisiones

| D | Tema | Decisión |
|---|---|---|
| D1 | Slugs | `food-truck-business-plan` y `coffee-shop-business-plan` → `/en/digital-products/<slug>` (+ `/access`, `/library`). productId = slug; JWT `<slug>-jwt`; env `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_BUSINESS_PLAN` y `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_BUSINESS_PLAN`; ficheros en `dl/<slug>/`. La keyword de cabeza va entera en el slug (12.100 y 3.600/mes US) |
| D2 | Nombres | **Food Truck Business Plan Kit** y **Coffee Shop Business Plan Kit** (landing, schema, dashboard, email, docProps, marca). Sin «Pro»: los planes ES tampoco lo llevan y la keyword va primero. H1 Forma B: `Food Truck ` + oro `Business Plan` + subtítulo «Template: Word Plan + Excel Financial Projections + Startup Checklist» (CAF: «… + Opening Checklist»). Title: «Food Truck Business Plan Template: Word + Excel Financial Projections + Startup Checklist \| AI Chef Pro» y el gemelo «Coffee Shop…». El concepto del CAF se describe como «coffee shop with brunch» (es el modelo del ES) |
| D3 | Precio | **$39** cada uno, pago único, acceso de por vida (29 € → escalón USD superior; competencia en `F1-research-us.md` §6: gratis / $45 / $79 + $119) |
| D4 | Anclas | Como el ES (99 € y bonos de 19 €) al escalón USD superior: `priceOld` **$129**; bonos **$29** cada uno; «Total value: $187 — business plan kit ($129) + 2 bonuses ($58)»; ahorro **$90** (= 129 − 39, convención del ES); «-70%» (1 − 39/129) en hero Y buyBox |
| D5 | Ficheros | Tabla §2.1. docProps `title` = título EN · «Food Truck Business Plan Kit»; checklist `Instructions!A3` = nombre comercial, no el id |
| D6 | Pestañas | Tabla §2.2; el renombrado reescribe en el mismo paso las referencias de fórmulas (419 / 423), DV y CF. En texto, pestañas entre comillas dobles rectas |
| D7 | Claves | `mapas.CLAVES` común: «Sí/No» → «Yes/No» (DV de Inversión col. E, SUMIF, «Break-even reached»), «CUMPLE/REVISAR» → «OK/REVIEW», «Más de 3 años» → «Over 3 years»; literales de fórmula (41-44) en `FORMULAS_EN` en un solo paso; ✓ ☐ N/A se quedan. Tokens de CF 1:1 y ningún mensaje cambia de color (gate G5) |
| D8 | Moneda y formato | Cero `€`: `#,##0 €` → `#,##0`, `#,##0.00 €` → `#,##0.00`; «Month n (€)» → «Month n»; `Supuestos!A2` dice una vez «amounts in your currency». Punto decimal en textos y DV («0.35 = 35%»). **US Letter** (`paperSize 1`) en las 32 hojas; pie `mapas.FOOTER_EN` |
| D9 | Sales tax (reutiliza financial-kit D8) | `Supuestos!B39` «Sales tax rate on sales» **8 %** [ejemplo: state + local; UK 20 % VAT]; B40 y B63 tipo del alcohol para llevar / en el local (8 %, nota de impuestos especiales de licor); **B41 «Recoverable input tax on purchases and capex» = 0** (US: el sales tax pagado es coste; UK: 20 %). Ingresos y costes del P&L **excl. sales tax**; tesorería **incl.** lo cobrado; liquidación trimestral (abril, julio, octubre, enero) con la misma fórmula, rótulo «Sales tax remitted (quarterly filer)»; mensual → nota. Excepción E2 abajo |
| D10 | Impuesto sobre beneficios | B37 y B38 «Effective income tax rate (years 1-2 / from year 3)» = **25 %** las dos (21 % federal C corp + estatal; pass-through: 0 % y el dueño tributa fuera). Bases negativas → «Net operating losses carried forward» con nota (federal: hasta el 80 % de la base; el modelo compensa el 100 %, simplificación declarada) |
| D11 | Personal (financial-kit D11) | B20 «Employer payroll taxes» **10 %** (FICA + FUTA/SUTA + workers' comp); B21 **12** pay periods (las extras de B60/B61 salen 0 solas: verificado en `Tesorería!B13`; rótulo «only if pay periods > 12»); B22 «Federal minimum wage, annual full-time» **$15,080** ($7.25 × 2,080); B68 «State / local minimum wage, annual full-time» (vacío; manda el mayor, misma lógica SMI/convenio); jornada 40 h (umbral FLSA de horas extra); 50 semanas; propinas no modeladas (nota). `Personal!A2` (fórmula) → «Payroll — N pay periods + employer taxes X%» |
| D12 | Amortización | Lineal de libros; vidas FT 7/7, CAF 10/7 (financial-kit D10: obra = menor de alquiler y vida). MACRS / Section 179 solo en nota. Sin cambio de fórmula |
| D13 | Financiación (financial-kit D12-D13, D26) | Filas `Financiación!8-11`: «SBA-guaranteed loan (7(a), through your bank)» · «SBA Microloan (nonprofit intermediaries, up to $50,000)» · «Investors / partners (equity: dilutes, not repaid)» · «Local grants (usually paid after you spend)». Tipo **10 %** nominal «not APR»; plazo FT 7, CAF 10; **interest-only 0** por defecto. DSCR límite **1.15×** y objetivo **1.25×**, sin «SBA minimum» (texto D26). Aportación propia: «lenders usually expect an owner equity injection (often around 10% for SBA start-ups; many want 20-30%)» |
| D14 | Unidades | m² → sq ft; litros → galones (conversión exacta y «check your county»: depósito residual mayor que el limpio, regla local habitual); 3.500 kg → regla CDL (GVWR ≥ 26,001 lb) |
| D15 | Caso de ejemplo US | Celdas verdes = `F1-research-us.md` §7 (todas [kit example]). F2 recalcula; si un semáforo del caso base sale rojo ajusta SOLO esas celdas y lo anota en `F2-NOTAS.md`. Exigido en el caso base: DSCR mínimo ≥ 1.25, saldo mínimo de caja > 0, cobertura de horas ≥ 98 %, ningún sueldo bajo el suelo, holgura sobre el equilibrio de caja ≥ 15 %. Los ratios del P&L pueden quedar ámbar solo con nota que lo explique (como hace el ES con el EBITDA) |
| D16 | Umbrales del P&L | `PyG!E51:E56` = research §7 («kit benchmark (editable estimate)», financial-kit D35); los textos de comentario se reescriben con ese origen |
| D17 | DSCR del año 1 (I4) | Con interest-only 0 el DSCR del año 1 ya mide la cuota completa: se corrige el defecto heredado sin tocar fórmulas. La nota C51 se conserva traducida (avisa si el usuario pone interest-only) |
| D18 | Bloque «QUÉ HA CAMBIADO RESPECTO DE LA VERSIÓN 1.1» | Mismas filas y columnas → «WHY THIS MODEL IS BUILT THIS WAY», cabeceras «Common shortcut \| This workbook \| Why»: cada fila explica el atajo de las plantillas típicas y lo que hace este libro, sin historia de versiones (la EN nace en 2.2) |
| D19 | Tabla de referencias | «Fuente» → «Source» con las fuentes de research §3-§4 o «Kit estimate»; **nunca «Fichero v1.1»** (I3). Filas de convenio / SMI → suelo de salario mínimo federal + estatal (DOL) |
| D20 | Versión y marca | «Version 2.2 · October 2026 · aichef.pro/en/digital-products/<slug> · info@aichef.pro»; firma de John traducida; «Más plantillas…» → `aichef.pro/en/digital-products`; docProps `subject` «<Nombre> · v2.2», `keywords` (keywords de research §1), `description` = URL, `category` «AI Chef Pro · Digital products» |
| D21 | Aviso legal (financial-kit D36) | En `Instructions` de los 4 xlsx, bajo la versión: «Planning tool, not financial, tax or legal advice. Requirements vary by state, county and city — check with your accountant and local authorities.»; checklists además «This checklist is a starting point, not an exhaustive list.» (excepción E1) |
| D22 | Docx | Traducción-adaptación **párrafo a párrafo** (131 / 167 párrafos, mismos estilos; un run por párrafo → se sustituye el texto del run). **Todas las cifras del plan salen del xlsx EN** (`cifras_caso.json` que extrae F2 tras recalcular): se acaba la contradicción docx v1.1 ↔ Excel (I1). Datos de mercado: solo los de `F1-research-us.md` con su fuente en el texto, o redacción cualitativa; nada inventado. Encabezados: 1 Executive Summary · 2 Concept & Value Proposition · 3 Market Analysis · 4 Competitive Analysis · 5 Marketing Plan · 6 Operations Plan · 7 Management & Staffing · 8 Financial Plan · 9 Legal Requirements, Permits & Licenses · 10 Conclusions & Action Plan. §9 = párrafo a párrafo §5 de research (orden: marco federal/estatal/ciudad · vending license · health permit + commissary + plan review · higiene y alérgenos · seguros · vehículo/DMV/CDL/fire · varias ciudades y eventos + **último párrafo con la nota UK**). En la CAF §9: certificate of occupancy, building permits, health, sign permit, liquor (si aplica) + nota UK. Core props EN |
| D23 | Marca del docx | Portada, aviso y cierre bajo **AI Chef Pro · aichef.pro** (autor John Guerrero), como los xlsx del mismo producto y la tienda EN. El ES conserva ChefBusiness (decisión de John del 22-ago, no se toca). Motivo: la venta cruzada ES apunta en EUR a `chefbusiness.co/productos-digitales/`, que no tiene edición inglesa. Cierre EN: Food Cost Kit Pro, HACCP Food Safety Kit Pro, Restaurant Staff Scheduling Kit Pro y AI Prompts eBook → `aichef.pro/en/digital-products`, **sin precios** (cambian) |
| D24 | Checklists | Fila a fila: mismas tareas por fase (FT 11/13/12/10/12/10, CAF 11/13/15/12/14/10). Cada trámite español pasa a su equivalente US de la tabla §4.2; responsable y plazo adaptados; notas UK en la columna E de la fila equivalente (sin filas nuevas) |
| D25 | Landing | §6; sin `aggregateRating` ni `review` (TIENDA §3.5); Google Sheets / Docs / LibreOffice / Numbers en `compatPills` **solo** tras un test real en F3 |
| D26 | Testimonios | Los 8 del ES traducidos tal cual (TIENDA §3.5, decisión de John), subtítulo «…with the Spanish edition of this plan». Riesgo anotado en §6: tres por plan citan cifras que ya no son las del producto |
| D27 | Máquina | Reparto Mac ↔ VPS (CLAUDE.md): textos y docx con Sonnet desde el Mac (2 a la vez, `istats` < 62 °C); `aplicar_en.py`, `inject_cache`, gates y `ensamblar_docx.py` en el VPS (`/root/chefpro-modernize`, venv `/root/venv-guias`, `git worktree` de la rama, `/dev/null` roto → ficheros de `/tmp`); `scp` y commit desde el Mac |
| D28 | Correos EN | Propuesta: Food Truck **30-oct 14:00Z**, Coffee Shop **4-nov 14:00Z** (cola EN +5 días sobre el 25-oct; ningún correo ES esos días: los ES van el 29-oct y el 3-nov; 4-nov programable desde el 5-oct por el tope de 30 días de Resend). Si la F3 se retrasa, se corre la cola, nunca se juntan |
| D29 | Interenlazado | Entrantes: tarjeta viva en el hub EN, `footerLinks` de los 6 productos EN, catálogo `urlByLang`, banners del blog EN, hreflang recíproco con `/plan-negocio-food-truck` y `/plan-negocio-cafeteria`. Salientes: Financial Plan Kit, HACCP y Staff Scheduling. Propuesta aparte (no en este presupuesto): post EN «food truck permits» (9.900/mes) con bridge.py, que enlace al kit |

### 1.1 Excepciones estructurales (las únicas que admite el gate)

- **E1** · Una celda de texto nueva por libro (`Instructions`, fila bajo la versión) con el aviso D21: 4 celdas.
- **E2** · `PyG!G13` y `G14` (soportado de las compras de comida y bebida) pasan de `$B$39`/mezcla con `$B$40` a
  `'0. Supuestos'!$B$41`: con el tipo de venta como soportado, el sales tax del 8 % se convertiría en un crédito por
  compras que no existe en EE. UU. 2 fórmulas por plan; el resto, idénticas al ES.
- No son estructurales: valores de celdas verdes (D15), umbrales E51:E56 (D16), textos de D18-D19.

## 2. Mapas

### 2.1 Ficheros (D5)

| Plan | Fichero ES | Fichero EN | Título EN |
|---|---|---|---|
| FT | `plan-de-negocio-food-truck.docx` | `food-truck-business-plan.docx` | Food Truck Business Plan (10 Sections) |
| FT | `plan-financiero-food-truck.xlsx` | `food-truck-financial-projections.xlsx` | Food Truck Financial Projections: 3-Year P&L, Cash Flow & Financing |
| FT | `checklist-apertura-food-truck.xlsx` | `food-truck-startup-checklist.xlsx` | Food Truck Startup Checklist (68 Tasks) |
| CAF | `plan-de-negocio-cafeteria-brunch.docx` | `coffee-shop-business-plan.docx` | Coffee Shop Business Plan (10 Sections) |
| CAF | `plan-financiero-cafeteria-brunch.xlsx` | `coffee-shop-financial-projections.xlsx` | Coffee Shop Financial Projections: 3-Year P&L, Cash Flow & Financing |
| CAF | `checklist-apertura-cafeteria-brunch.xlsx` | `coffee-shop-opening-checklist.xlsx` | Coffee Shop Opening Checklist (75 Tasks) |

### 2.2 Pestañas (D6)

| ES | EN | ES | EN |
|---|---|---|---|
| `0. Supuestos` | `0. Assumptions` | `F1 - Constitución` | `Phase 1 - Business Setup` |
| `Inversión Inicial` | `Startup Costs` | `F2 - Vehículo` (FT) | `Phase 2 - Truck & Permits` |
| `PyG 3 Años` | `3-Year P&L` | `F2 - Local` (CAF) | `Phase 2 - Location & Permits` |
| `Punto Equilibrio` | `Break-Even` | `F3 - Equipamiento` | `Phase 3 - Equipment` (CAF `Phase 3 - Build-Out & Equipment`) |
| `Escenarios` | `Scenarios` | `F4 - Personal` | `Phase 4 - Staff` |
| `Personal` | `Staffing` | `F5 - Marketing` | `Phase 5 - Marketing` |
| `Tesorería 12 meses` | `12-Month Cash Flow` | `F6 - 90 Días` | `Phase 6 - First 90 Days` |
| `Financiación` | `Financing` | `Instrucciones` | `Instructions` |

### 2.3 Glosario (añade al del financial-kit, que manda)

plan de negocio → business plan · cliente/día → customers per day · ticket medio sin IVA → average check (excl. sales
tax) · PVP con IVA → menu price incl. sales tax · aparcamiento y base del vehículo → commissary & truck parking ·
venta ambulante → mobile vending · gestor/gestoría → accountant / bookkeeper · autónomo → sole proprietor · SL → LLC ·
alta en Hacienda → state tax registration / seller's permit · Seguridad Social (empresa) → employer payroll taxes ·
SMI → minimum wage · convenio → state / local minimum wage · carencia → interest-only period · fondo de maniobra →
working capital · DDD → pest control · gestor de residuos → licensed waste / grease hauler · carnet de manipulador →
food handler card · APPCC → HACCP-based food safety plan · registro sanitario → health permit.

## 3. Reglas US/UK (cifras únicas; `mapas.REGLAS_US` y `VALORES_EN`)

Las de `F1-research-us.md` §3-§5 y §7, con su etiqueta. Resumen de lo normativo: sales tax 8 % ejemplo, sin crédito
por compras; cargas ≈ × 1.10; mínimo federal $7.25/h; FLSA 40 h; impuesto efectivo 25 %; préstamo 10 % / 7-10 años /
sin interest-only; DSCR 1.15 / 1.25; vidas 7/7 y 10/7; 9 alérgenos US (UK 14); CDL desde 26,001 lb; UK: registro 28
días antes, street trading licence, FHRS 1-5, VAT 20 % en caliente y en local.

## 4. Qué cambia en cada entregable además de la traducción

### 4.1 Plan financiero (una capa para los dos)

| Hoja | Cambio |
|---|---|
| `0. Assumptions` | D8-D15 (filas 4-68: rótulos, notas y valores de §7 de research) |
| `Startup Costs` | Partidas US (research §7) en las mismas filas; col. E «Taxable / recoverable tax?» Yes/No (sin efecto con B41 = 0, se conserva para UK); notas US; B28/B37 «Recoverable input tax on capex» |
| `3-Year P&L` | E2; fijos con rótulo US (permisos anuales, inspecciones, contabilidad, plagas, grasa, formación, música ASCAP/BMI); notas LIVA/LIS → sales tax / income tax; E51:E56 (D16) |
| `Break-Even`, `Scenarios` | Traducción; «sin IVA» → «excl. sales tax»; interpretación (fórmula de texto) en `FORMULAS_EN` |
| `Staffing` | D11; puestos US (research §7); notas ET → FLSA/DOL |
| `12-Month Cash Flow` | D9: filas 16-20 («Sales tax collected», «Recoverable input tax», «Carried forward», «Quarterly sales tax return», «Sales tax remitted»); estacionalidad «your area» |
| `Financing` | D13 |
| `Instructions` | D18, D19, D20, D21; línea 4 sin divisores 1,10/1,21 («divide a menu price by 1 + your sales tax rate»); línea 8: el docx usa las mismas cifras de ejemplo que el libro |

### 4.2 Checklists — equivalencias (D24; los traductores completan responsable, plazo y nota)

| ES | US |
|---|---|
| Forma jurídica SL / autónomo; constitución, notaría, Registro Mercantil | Choose structure (LLC vs sole proprietorship); file articles of organization (Secretary of State); registered agent; operating agreement |
| Alta en Hacienda 036/037 + IAE; certificado digital FNMT | EIN (IRS, free); state sales tax registration / seller's permit; city or county business license |
| Alta en Seguridad Social; contratos, convenio | Register as employer (state withholding + unemployment insurance); workers' comp; I-9, W-4, new-hire reporting; W-2 vs 1099 |
| Registro sanitario autonómico; autorización sanitaria del vehículo; proyecto técnico sanitario | Health department plan review → mobile food unit permit + inspection (CAF: food establishment permit) |
| Venta ambulante municipal; ocupación de vía pública; ferias | City mobile vending license (per city); parking / vending-zone rules and written permission on private property; temporary food event permits |
| Hojas de reclamaciones (FT) | **Commissary agreement** (la mayoría de health departments lo exigen) |
| ITV de reforma; carnet B/C | DMV registration and title; CDL only above 26,001 lb GVWR; fire marshal inspection (propane, suppression, NFPA 96 donde aplique) |
| Licencia de actividad inocua / declaración responsable; informe urbanístico; licencia de obras; terraza (CAF) | Zoning check before signing; building permits; certificate of occupancy; sidewalk café permit |
| LAU, fianza (CAF) | Commercial lease review (NNN/CAM, personal guarantee) |
| Seguro RC 300.000 € + multirriesgo / vehículo | General liability (often $1M per occurrence required by events and landlords) + commercial auto (FT) / BOP or property (CAF) |
| RGPD, LOPDGDD, cláusulas, videovigilancia | Privacy notice for loyalty and email data; TCPA consent for SMS; camera signage per state law |
| Veri*factu / factura electrónica | POS set up to collect and report sales tax by location |
| Carnet de manipulador (RD 109/2010); APPCC; 14 alérgenos | Certified Food Protection Manager + food handler cards; HACCP-based food safety plan; 9 major US allergens (UK 14) |
| PRL; registro horario (art. 34.9 ET) | OSHA basics + workers' comp; FLSA time and payroll records |
| DDD (ROESB); gestor de residuos y aceite | Licensed pest control; licensed grease / waste hauler (FT: at the commissary) |
| SGAE / AGEDI-AIE | ASCAP / BMI / SESAC licenses if you play music |
| Glovo / Uber Eats, TheFork, Google My Business, TripAdvisor | DoorDash / Uber Eats, Resy / OpenTable, Google Business Profile, Yelp; food truck apps (Roaming Hunger, StreetFoodFinder) |
| Primer cierre trimestral (gestor) | First quarter close + first sales tax return (accountant) |

### 4.3 Docx: D22-D23.

## 5. Datos para los traductores

Glosario §2.3 + financial-kit; `cifras_caso.json` (salidas del xlsx EN recalculado: ventas años 1-3, CAPEX, fondo de
maniobra, necesidad de caja, equilibrio contable y de caja, ratios, DSCR mínimo, saldo mínimo, plantilla y coste);
research §3-§5 con fuentes. Cifras en formato US («$254,800», «29.9%»); en el docx con símbolo $ (texto de un plan
para un lector de EE. UU.), en los xlsx sin símbolo (D8).

## 6. Afirmaciones de las fichas ES que NO pasan al EN (revisadas contra los ficheros)

| # | Ficha | Afirmación ES | Realidad | EN |
|---|---|---|---|---|
| A1 | FT | «Ratios… **cada dato con su fuente**» (bono 2) | Toda la columna «Fuente» dice «Fichero v1.1» (el propio producto) | Fuentes reales de research o «kit estimate» (D19), y solo entonces «sourced» |
| A2 | FT | «41 clientes/día… y **38 para cubrir además la cuota del préstamo**» | El equilibrio de caja sale MÁS BAJO en el año 1 porque es año de carencia y no lleva amortización: «además» engaña | Con interest-only 0 se recalcula; redactar «cash break-even (loan payments in, depreciation out)» con la cifra EN |
| A3 | FT/CAF | Checklist «**verificado** contra la normativa vigente» | Afirmación que el EN no puede sostener en 50 estados | «A starting point; requirements vary by state, county and city» (D21) |
| A4 | FT | «Inversión **45-85K EUR** (vs 100-150K de un restaurante)» | Rango del docx v1.1; el Excel dice 81.997 € | Cifra del xlsx EN + rango US con fuente (research §3) |
| A5 | FT | Bono 1 «Guía Permisos por **CCAA**» | Es la §9 del docx + fase 2 del checklist, no un fichero | «Food Truck Permits & Licenses Guide (US + UK notes) — section 9 of the plan + Phase 2 of the checklist; no state forms» |
| A6 | FT/CAF | Docx con cifras de la v1.1 (73 K / 27 clientes; 94 K / 53 clientes) | Contradice al Excel (I1) | D22: el docx EN usa las cifras del xlsx EN |
| A7 | CAF | La landing **no menciona el DOCX** (6.508 palabras) | Se entrega y no se vende | Tarjeta DOCX la primera del grid; la tarjeta «Equipamiento» se funde con «Startup Costs» (son filas de esa hoja) para seguir en 9 |
| A8 | CAF | «Equipamiento… **con marcas de referencia** y precios» | Ninguna marca en el xlsx; una mención «tipo La Marzocco o similar» en el docx | «with reference prices» |
| A9 | CAF | «Ratios… **rotación por franja horaria** (mañana / mediodía / tarde)» | El libro tiene rotaciones/día implícitas y ocupación entre semana / fin de semana; no hay franjas | Quitar; decir lo que hay |
| A10 | CAF | «Plan de Financiación… con **orden recomendado de gestión**» | No existe en el libro | Quitar |
| A11 | CAF | Bono 1 «Cuadro de Personal con Seg. Social» | Es la hoja `Personal`, ya vendida como tarjeta del grid (doble cómputo) | Bono 1 = «Coffee Shop Permits & Licenses Guide (US + UK notes)» (§9 + fases 1-2), simétrico al FT |
| A12 | FT/CAF | `aggregateRating` 4,9 / 8 reseñas y 3 `reviews` en el schema | Capa comercial ES | Fuera (TIENDA §3.5) |
| A13 | FT/CAF | «El plan de negocio **más completo**…» (badge) | Superlativo sin medida | «Lender-ready food truck business plan: Word + Excel + checklist» |
| A14 | FT/CAF | «Listo para Microcrédito + **ICO / ENISA**», «Datos reales del mercado español», «licencia inocua», «SS 33 %, 14 pagas, SMI» | Mercado ES | SBA 7(a) / Microloan («lender-ready format; approval not guaranteed»), cifras de ejemplo US etiquetadas, permisos US, payroll taxes y minimum wage |
| A15 | FT/CAF | Compatibilidad Google Sheets / Docs / LibreOffice / Numbers | Sin test en EN | Solo tras test (D25) |
| A16 | FT/CAF | Testimonios con «59 trámites», «27 clientes/día a 12 €», «retorno 12-24 meses», «guía por CCAA» (FT) y «53 clientes/día a 9,50 €» (CAF) | Cifras de la v1.1: hoy ni el ES dice eso (68 trámites, 41 y 84 clientes, payback FT «más de 3 años») | Se traducen tal cual por la regla de John (D26); **riesgo**: si John lo pide, se sustituyen esas cifras por las del producto o se eligen otros textos |

Lo que sí se mantiene (comprobado): 10 secciones del docx, 9 hojas del Excel, P&L 3 años, tesorería 12 meses, plan de
financiación con cuadro y DSCR, 3 escenarios, 68 / 75 tareas en 6 fases, 722 / 742 fórmulas (las cifras EN se
recuentan en F2), celdas verdes y protección sin contraseña.

## 7. Plan de F2 y F3

1. **Extracción** (`extraer_textos.py`, calcado del financial-kit, para los 4 xlsx): grupos **GM** (414 cadenas comunes
   del motor + 61 del checklist), **GFT** (≈190 propias del plan + ≈145 del checklist FT) y **GCAF** (≈215 + ≈165).
2. **Textos xlsx**: 3 subagentes **sonnet**: GM primero (fija glosario y la línea de firma), luego GFT y GCAF en paralelo.
   Reciben cadenas con `donde`/`pistas`, §1-§5, research §5 y §7, `CLAVES`, `FORMULAS_EN`. DV ≤ 255, títulos ≤ 32.
3. **`aplicar_en.py` + `gates_en.py`** (un **opus** en el VPS, copia adaptada de `financial-kit/`): copiar los 4 ES →
   pestañas y referencias → `FORMULAS_EN`/`CLAVES` → E2 → textos → `VALORES_EN` (D15-D16) → formatos (D8) → Letter →
   E1 → protección idéntica → nombre EN → `inject_cache.py` → calibración D15 → `cifras_caso.json`. `--dry-run`,
   `--idempotencia`, `--autotest` con defectos inyectados.
4. **Docx**: 4 subagentes **sonnet** (FT §1-5 · FT portada, §6-10 y cierre · CAF ídem) con `cifras_caso.json`; salida
   `{índice de párrafo: texto}`; `ensamblar_docx.py` (python-docx) sustituye el run de cada párrafo y fija core props.
5. **UNA revisión adversarial** (opus): lente prestamista/CPA US que **recalcula** cifras (sales tax, DSCR, nóminas,
   equilibrio) + lente técnica de ficheros. Tope 2 rondas. `F2-NOTAS.md` con todo lo calibrado.
6. Los 2 slugs en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de `censo-entregables.py`.

**F3** (un opus en worktree, réplica del Financial Plan Kit): `data/productos-en/planes/<slug>.ts` (mismo tipo
`PlanNegocioData`, §6), 3 páginas anidadas, dashboard copiado y traducido (3 descargas), familias
`plan-negocio-food-truck` / `plan-negocio-cafeteria` con `en.vivo` en `tienda.ts`, `zona-app.ts`, las 5 fuentes del
backend con `lang: 'en'`, `product-prices.ts` USD 39, tres puertas cripto, hreflang en las 2 landings ES
(`tienda-gate --es-identico --esperadas`), tarjeta del hub, catálogo, `footerLinks` hermanos, correo EN.

**Presupuesto**: F1 ≈ 0,45 M (esta) · F2 ≤ 2,5 M (los dos) · F3 ≤ 1,5 M (los dos). Si el total pasa de 5,9 M (+30 %),
se para y se reporta.

## 8. Gates

- **G1 Paridad** (contra censo ES): pestañas §2.2; fórmulas idénticas tras pestañas + claves salvo E2; DV (tipo, sqref,
  rango), CF (sqref, tipo, prioridad, relleno), merges, paneles, protección sin contraseña con los mismos flags, verdes
  y desbloqueadas; tareas por fase y contadores; celdas nuevas = solo E1.
- **G2 Restos**: cero español, `€`, «m²», no latinos, coma decimal, normativa ES (LIVA, LIS, IAE, SMI, ICO, ENISA,
  CCAA, RGSEAA, ITV, SL, autónomo, convenio, Veri*factu…), «v1.1», «Fichero», ids internos en celdas, literales, DV, CF,
  pies y docProps; DV con título ≤ 32 y mensaje ≤ 255.
- **G3 Formato**: Letter en las 32 hojas, pie, versión, marca, docProps (D20), aviso D21.
- **G4/G5 Claves y CF**: listas de DV ⊂ `CLAVES`; tokens de CF inyectivos y mismo color por mensaje.
- **G6 Cálculo**: caché sin errores; E2 aplicado → IVA soportado de compras = 0 y liquidación trimestral = sales tax
  cobrado; caso base cumple D15; con 12 pagas la fila de nóminas es constante; `cifras_caso.json` = caché.
- **G7 Reglas**: cada valor de `VALORES_EN` = research §7 o declarado en `F2-NOTAS.md`; ningún texto con «SBA
  minimum».
- **G8 Docx**: mismo nº de párrafos y estilos que el ES; cero español, «EUR», «€», «ChefBusiness», «chefbusiness.co»;
  encabezados D22; toda cifra del plan presente en `cifras_caso.json`; Letter.
- **G9** `censo-entregables.py --only <slug> --fail` y `gate-no-latinos.py` en 0 para los dos slugs.
- **F3**: `tienda-gate.py --base`, `robots-gate.py`, `gate-flujo-postpago.py --only` ×2, `whatsapp-gate.py`,
  `datafast-gate.py`, `miselup-gate.py` (0 en `/en/`), `--es-identico` de las 2 landings ES.

## 9. Lo que decide John

Solo los dos **Payment Links USD $39** (pago único, impuesto automático, Adaptive Pricing) con redirección a
`/en/digital-products/<slug>/access?session_id={CHECKOUT_SESSION_ID}`. Todo lo demás está decidido aquí.
