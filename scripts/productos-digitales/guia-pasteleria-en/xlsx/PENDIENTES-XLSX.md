# Pendientes de los xlsx EN que salen de las tandas de texto

- T01: «Variante del Formato» (→ "Format Variant") K15:L24 lleva los rangos publicados ESPAÑOLES por formato. En EN: rangos
  US de Zenind 2026 (research §12.1) en las 3 filas que los tienen en el texto (home $15K–$25K, small retail $50K–$100K+,
  production $75K–$150K+; online $20K–$40K si hay fila) y vacías las demás; nombres EN de las 10 filas como en T01.
- T02: «Peso sobre el Año» (→ "Share of the Year"): picos por mes = Jan «Día de Reyes (Three Kings Day)» · Feb «Valentine's
  Day» · Apr «Easter (Holy Week)» · May «Mother's Day, First Communions and graduations» · Nov «All Saints' Day and Día de
  los Muertos» · resto «-». Las notas «por qué este coeficiente» de marzo y mayo asumen el Día del Padre en marzo:
  reescribirlas (marzo sin pico; mayo con Mother's Day + comuniones + graduaciones).
- T02: «Decisión de Surtido» (→ "Menu Decision"): veredictos Keep / Review price / Drop; «semáforo de carta» → "menu
  traffic light"; «margen ponderado» → "weighted margin".
- T03: «CAPEX por Bloque» (→ "Startup Costs by Block"): nombres de bloque, partidas y valores de la columna «Procedencia»
  (→ "Source": Build-out scenario · Example price · Assumption · Food Code + assumption; fuera PS-*/PA-*) exactamente como
  en la tabla de T03 y DECISIONES §9 T03 (Docriluc, Sammic, Selmi y Salva en genérico; fregaderos → «Three-compartment sink,
  hand sink and mop sink»; TPV sin Verifactu; tasas → «City and county permit fees…» y «Health department plan review and
  food permit application»). Reescribir las notas N/O que citan €, PS-xx o Barcelona. «Parámetros» B13 (→ "Settings"):
  rótulo «Sales tax rate on purchases» (0 % por defecto; nota: «e.g. 8.25%, the Texas maximum combined rate»), porque el
  texto dice que tecleando 8.25 % ahí salen las columnas de impuesto de sus tablas; B14-B15 coherentes con eso.
- T03: «Zonas y m2» (→ "Zones and Square Feet"): columna «Qué tiene que cumplir» como la tabla de T03 (Food Code 3-501.16 y
  5-203.11, ADA 904.4.1; fuera RD 1021/2022, PA-03b, PA-12) y su comentario de celda «Verificado… BOE» → «Checked October
  2026 · FDA Food Code 2022…». Bloques: Production kitchen · Front counter · Cold and dry storage · Restrooms and lockers.
- T03: altura en pies: capacidad «Parámetros»!B22 (3 m) y «Ficha de Visita a Local»!F12 (3.2 m) → ×3.2808399 (9.84 · 10.50
  ft) con unidad «ft», para que cuadre con «9.8 feet» del texto (op opcional de CONFIG-NOTAS §3). Caudal en CFM (ya en
  config: 1,360 m³/h → 800 CFM).
- T03: «Ficha de Visita a Local» (→ "Site Visit Checklist") ítems 1-2 («salida de humos propia» / «no comparte conducto»)
  → preguntas US de T03: «The hood type the space has (or can take) matches your ovens: Type I + fire suppression for deck
  ovens, Type II for enclosed electric convection, written answer from the building/mechanical department» y «There's a
  route for the duct to the roof»; ítem 12 «liso, lavable e impermeable» → «smooth, durable, easily cleanable; coved
  floor-wall junctions»; ítem 13 sin «separados de los de clientes» (lo fija el plumbing code local).
- T04: «Ficha de Visita a Local» (→ "Site Visit Checklist") B6:D23: qué se comprueba y cómo, como la tabla del cap. 6 de T04
  (ítem 1 ruta del ducto propio a cubierta, sin enlazar con aseos/sala; ítem 2 tipo de campana Type I/II por escrito; 4
  service size amps/voltage/phase; 5 planning/zoning en escrito; 6 landlord + CC&Rs/center rules/association; 17 gas
  service and piping; 18 use clause, permit contingency, CAM/NNN, personal guarantee, TI). Fuera RITE, CTE, RD 193/2023,
  RD 919/2006, RD 1021/2022, «Nota simple» y sus comentarios BOE (J6, J7, J14, J21, J22). Veredictos (CF y fórmulas)
  DESCARTAR / Punto débil / Pendiente / OK → «RULE OUT» / «Weak point» / «Pending» / «OK»; E32 → «RULE OUT THIS SPACE» /
  «DON'T DECIDE YET» / «GO AHEAD WITH CAUTION» / «GO AHEAD»; respuestas «Sí/No/Por comprobar» → «Yes/No/To check».
- T04: «Traspaso vs Obra Nueva» (→ "Takeover vs New Build"): A26:A40 con nombres sin tildes del texto (Barcelona, Gracia ·
  Seville · Almeria · Barcelona, Passeig Maragall…), B26:B40 tipos de negocio EN del texto, H26:H40 «Milanuncios, 2026» /
  «negociosenventa.es, 2026» (fuera PS-69/PS-70), C25 «Square feet» y F25 «Dollars per square foot» (C26:C30 ya en config
  ×10.7639). Notas J6 (85 m², 43.000 €, Gràcia) y J8 → sin €/m²: «seeded with the closest listing in size (915 sq ft,
  43,000)». A47 debe decir que son anuncios ESPAÑOLES llevados 1:1 a dólares y no precios US; A49 (modelos 303/390,
  Seguridad Social) → «ask for three years of tax returns, P&Ls, sales tax returns and payroll reports». Literales de C22 →
  «The TAKEOVER comes out ahead» / «The NEW BUILD comes out ahead». Pendiente de la marca ⟦ADAPT⟧ de T04 (¿se quedan?).
- T04: «Capacidad por Equipo» (→ "Capacity by Equipment"): nombres de equipo y categorías como la tabla del cap. 7
  (Mixing · Sheeting · Heat · Refrigeration · Freezing · Storefront and display; «Walk-in cooler, 8 m³ (about 283 cu ft)»,
  «Spiral mixer, 25 kg (55 lb) of dough», «Planetary mixer, 20 qt», «Automatic dough sheeter, up to 16 in wide»).
- (orquestador, T04) «Traspaso vs Obra Nueva»: filas 27-40 VACIADAS (config `_traspasos`); fila 26 = «The space you're
  looking at (the modeled case)» · «Pastry and cake shop» · fuente «The seller's listing». A24 → «Your local takeover
  listings: the case plus fourteen rows for your area». A47/A49 → asking prices, not prices paid; where to find listings
  (BizBuySell, BizQuest or a local business broker, with the date read); valora por lo que gana el negocio: pide 3 años de
  tax returns y P&L, el payroll y el contrato de alquiler (sin modelos 303/390 ni Seguridad Social). J6/J8 sin Gràcia ni
  Barcelona: «Seeded with the case's own takeover (915 sq ft), an ASKING price».
- T05: «Equipamiento» (→ "Equipment") del libro de equipo: nombres de línea IGUAL que la tabla del cap. 8 (= T03); Marca y
  Modelo: UNOX, SMEG, Docriluc (×2), Sammic DF-40 y BE-20, Selmi → **«Not named»** + ficha en Modelo (textos en la tabla de
  T05); Salva → marca y modelo vacíos (es «Assumption», como en T03); Irinox / «MultiFresh line» se queda. Columna
  «¿Lleva IVA?» → **«Price basis»** con lista «pre-tax · incl. sales tax · not stated»; **J22** («no declarada», batidora)
  → «pre-tax» como J16/J17. Prioridad Crítico/Opcional → Critical/Optional. NOTAS_LIBRO: la nota «LA COLUMNA QUE MÁS
  DINERO MUEVE ES ¿Lleva IVA?… 21 %… 14.000 €» → la trampa US (list price sin sales tax, freight/liftgate, instalación,
  voltaje y fase; el sales tax del equipo es coste); «Nueve líneas traen precio publicado… trece un supuesto» → **«Eight
  lines carry an example price and fourteen an assumption»** (el horno de pisos es Assumption, T03); fuera «libro 2/5/6/7»
  → nombres EN de fichero. **T03 + «CAPEX por Bloque»**: quitar «UNOX XB693 Bakerlux» y «SMEG ALFA420E1HDS» de los nombres
  de partida → «Convection oven, 6 trays» / «Convection oven, 4 trays».
- T05: «Variante del Formato» del libro de equipo (→ "Format Variant"): las 7 descripciones citan PS-xx, € publicados y el
  RD 1021/2022. EN: nombres de T01 (Home-based bakery under cottage food · Closed-door production kitchen · Mid-size pastry
  shop (the case) · Bakery-café · Small bake-off shop · Wholesale production kitchen for restaurants and cafés · Ventless
  pastry shop (no Type I hood)) y descripciones sin cifras ES; la ventless: «All-electric ovens under a Type II hood, or
  listed to UL 710B; saves the exhaust duct and rules out frying». Su total tiene que seguir dando **$60,480** (base − ducto).
- T05: «Ruta Doméstica» (→ "Cottage Food Route") **B15 y B16**: con los formatos del ES (entero y 0.0), 0.743 y 0.4645 se ven
  como «1» y «0.5»; formato **0.00** (el texto dice 0.74 y 0.46 kg per usable sq ft a week). B6 = 129.17 → formato entero (129).
- T05: «Suministro a Otros Minoristas» (→ "Selling Wholesale"): el radio (verde 50) y las distancias de las cuentas son
  **km del ES bajo un rótulo en millas**: convertir (× 0.621371 → 31 mi) o reescribir el semilla; el texto no da cifra.
- T08: «plantilla-turnos-y-coste-personal» (→ staff-schedule-and-labor-cost.xlsx): áreas **OBRADOR → «PRODUCTION KITCHEN»**,
  **COMERCIO → «FRONT COUNTER»**, ADMINISTRACIÓN → «ADMINISTRATION» en los valores (Turnos Semanales C11:C15, Parámetros E8:E13)
  **y** en los literales de fórmula E17:K18 (SUMIF), o la cobertura se rompe; A17/A18 → «PRODUCTION KITCHEN hours per day» /
  «FRONT COUNTER hours per day»; A19 «Counter coverage» con «Covered» / «Closed» / «NOBODY»; turnos D11:D15 «Early bake
  (04:30-12:30)» · «Early bake (05:00-13:00)» · «Morning (07:00-11:00)» · «Morning (08:00-12:00)» · «Afternoon (16:30-20:30)»;
  días L M X J V S D → Mon…Sun. "Hours and Cost": D6 «Pay grade», L6 **«Employer cost per hour worked»**, N6 «Minimum wage check»
  con N7:N11 «Below the annual minimum wage»; A3/A32 (33 % = «payroll taxes, workers' comp and benefits», no «quince pagas y
  Seguridad Social»); Parámetros A6 y comentarios C8:C13 (convenio de Madrid/BOCM) → «The modeled case's wage table: an example,
  not a legal schedule. Replace it with what you'll pay; check federal, state and city minimum wage» ; G8:G13 (plus de
  nocturnidad) → «Base pay, before overtime. Federal law has no night or weekend premium; check your state.»; F8:F13 puestos como la
  tabla 2 de T08. Plan de Contratación K7:K11 (alta en la Seguridad Social) → «Before the first shift: Form I-9, payroll
  setup and workers' comp (optional in Texas)» (§8-bis P6; nada más sin research). Turnos Semanales A35 (Kit de Tareas, 12 €) → «your daily task checklists».
- T08: «plan-financiero-3-anos-pasteleria» "Staff": nombres de puesto de la tabla de 6 grupos (F15:F20) iguales que la tabla 2 de
  T08; áreas en el mismo vocabulario (PRODUCTION KITCHEN / FRONT COUNTER / ADMINISTRATION).
- T06: «Proveedores» (→ "Suppliers") de equipment-and-suppliers-checklist.xlsx TIENE QUE CUADRAR con la tabla del cap. 11
  (DECISIONES §9 T06): B7:B15 empresa, C7:C15 «What it sells you», D7:D15 URL, en este orden: AUI Fine Foods · Puratos ·
  BakeMark · Barry Callebaut (Callebaut) · Valrhona · Plugrà (Dairy Farmers of America) · King Arthur Baking · Sysco ·
  WebstaurantStore; H (pedido mínimo 300) e I (plazo 7) intactos. E7:E15 (PS-87…PS-95) → «Official website, Oct 2026» (fuera
  ids PS-*); L7:L15 («por qué está en la lista») con los hechos de research §16 [T06] (p. ej. «Headquartered in Gaithersburg,
  Maryland»; «Chocolate Academy courses in Chicago»; «82% butterfat; find-a-distributor link»; «Tax ID or EIN to open an
  account»). A3, G16, A26, Instrucciones A10 y Contador C43: «checked October 2026» y SIN «los 22 sin verificar del
  research»; A27 (Hosply) → «Need more names? Start with each brand's distributor locator (Plugrà, Callebaut, AUI Fine Foods)
  and ask your broadline sales rep»; A28 = supuestos (pedido mínimo, plazo, condiciones), no condiciones de estas empresas.
  Contador A47 (comunicación al registro sanitario, licencia, APPCC, formación) → «the food permit, the food safety plan with
  a CFPM as person in charge, and the training log are counted in permits-and-licenses-checklist.xlsx».
- T09: «estacionalidad-y-picos» (→ seasonal-peaks-planner.xlsx): nombres de campaña en "6-Peak Calendar" B6:B11, "Share of
  the Year" A24:A29 y E, "Peak Capacity vs Demand" A6:A11 y "Extra Staff and Cash" A6:A11 IGUALES que el cap. 15 (Día de
  Reyes (Three Kings Day) · Valentine's Day · Mother's Day · Easter (Holy Week) · First Communions and graduations · All
  Saints' Day and Día de los Muertos). "6-Peak Calendar": C8 «19 de marzo y primer domingo de mayo» → «Día de las Madres
  (May 10) and US Mother's Day (2nd Sunday in May)», D8 = 5; C6 «January 2-6», C11 «October 30 – November 1»; F6:F11
  productos estrella con los nombres de DECISIONES §4. Notas R6 (PS-35, 30 millones de roscones en España) → king cake
  season + búsquedas US 90,500/110,000 (sin PS-*); R8 («Dos fechas… el kit las separa») → una sola fecha operativa (Día de las
  Madres + US Mother's Day, tarta con dedicatoria por encargo), sin «kit»; R10 y las notas gemelas «MESETA… 11-control-
  encargos.xlsx del kit (R2)» (también kitchen-capacity-and-site "Bottleneck" J22 y staff-schedule "Hiring Plan" K20) →
  «deposit, delivery calendar and cancellation risk (chapter 16)», sin fichero del kit. "Extra Staff and Cash" R6 («almendra,
  naranja confitada y agua de azahar en noviembre; roscón relleno 4 °C y 24 h») → °F (39 °F) y sin regla española; A18
  (Kit de Tareas 12 €, BONUS-02, 06-eventos-festivos, 10-plan-produccion-semanal) → «your annual task calendar and daily
  task checklists»; E5 «Coste hora de empresa» = employer cost per hour (payroll taxes, workers' comp and benefits).
  Instrucciones A10 («bruto de convenio más Seguridad Social») → «base pay plus payroll taxes, workers' comp and benefits»;
  A16 y Calendario A3 (Kit de Tareas) → sin kit; A23 «en enero… para Reyes, seis semanas antes, a finales de noviembre»
  se puede quedar (late November).
- T09: «plan-financiero-3-anos-pasteleria» "Channels and Break-Even": A6:A9 = Counter · Custom orders · Wholesale (local
  cafés and restaurants) · Online and shipping (como la tabla del cap. 16). **J7** («Anticipo del 30 % al reservar
  (supuesto)…») → «30% deposit at booking (assumption): it turns a cancellation into a nuisance instead of a loss. Many US
  bakeries ask 50%, often non-refundable: common practice, not law. Better margin because it's made to order with zero
  display waste.» El texto del cap. 16 cita esa nota (no hay celda editable de la señal). A31 (95/5 de una pastelería
  española, TPV) → «a published Spanish case… your POS data».
- T10: «plan-financiero-3-anos-pasteleria» "3-Year P&L": rótulos A11:A43 como la tabla del cap. 18 (DECISIONES §9 T10):
  A19 «Staff (wages plus payroll taxes, workers' comp and benefits)», A20 «Owner's pay (before your own self-employment and
  income tax)», A36 «PRE-TAX PROFIT», A43 «NET PROFIT», A11 «TOTAL REVENUE (before sales tax)». Filas 34-35 (IVA soportado,
  ya a 0) → «Input VAT/GST on variable costs (UK, Canada, Australia; $0 in the US)» y «… on fixed costs …»; G35 sin modelo
  303. Bloque de impuesto A37:A42 → «Net operating losses at the start of the year» · «Taxable income (after losses)» ·
  «Years with a profit (running count)» · «Income tax rate (illustrative)» · «Income tax» · «Net operating losses at year
  end»; G37 (art. 26 LIS) → NOL en genérico; G40 (15 % de nueva creación, IRPF) → «Illustrative: 15% for the first two
  years with a profit, 25% after. By default a single-member LLC is reported on its owner's return and a multi-member LLC
  is classified as a partnership (IRS): ask your CPA». Notas a reescribir sin España: G13 (modelo 303), G21/G22/G24/G25
  (IVA, Verifactu), G23 (Ley 37/1992, CCAA → «Assumption. Ask your insurance agent what your landlord and lender require»),
  G28 (inspección de gas cada 5 años → «Assumption»), A54 («SIN IVA» → before sales tax).
- T10: "Scenarios": A15 «Income tax (the workbook's illustrative rate)» y su nota E15 sin «entidad de nueva creación».
  "Break-Even" A13 «Loan principal repaid this year (cash out)» (el texto cita sus valores 3,808 · 7,979 · 8,488).
- T10: "Channels and Break-Even" A24:A28 (aviso del art. 3 del RD 1021/2022) → bloque de la línea FDA: título «THE FDA LINE:
  WHEN WHOLESALE CHANGES YOUR REGISTRATION»; A25 «Wholesale share of food sales, by value (%)»; A26/B26 «Our cautious
  working line (the legal line is 50%: 21 CFR 1.227)» = 25 %; B27 literal «Retail: below the working line; run the three
  checks in permits-and-licenses-checklist.xlsx»; J26 y A28 sin 500 kg, «marginal, localizado y restringido» ni declaración
  responsable → «only sales to businesses you don't own count; measured by value over the year»; A31 → 95/5 = ejemplo español
  declarado (lo dice también T09). Rótulos de columna como la tabla del cap. 17 (Days to collect, Cost to serve…).
- T10: «carta-de-apertura-y-escandallo» "Egg & TCS Decision": columnas y valores como la tabla 2 del cap. 17 (Egg route:
  Cooked through · Pasteurized egg product · No egg · Shelf-stable; «Shelf-stable at room temperature?» Yes/No; «Holding
  temperature (°F)» = 41; el 24 h → «Date-mark if held over (hours)» con «N/A»; «Refrigerated case» / «Room-temperature
  case»). Las cabeceras «Techo del art. 4.1 fila 9» y «Techo del art. 9.3» (G, H) → «Food Code cold-holding limit (°F),
  3-501.16»; las dos salen 41.
