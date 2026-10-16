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
