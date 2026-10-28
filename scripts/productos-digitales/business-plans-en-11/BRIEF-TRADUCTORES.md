# Brief para los redactores (subagentes Sonnet) — Coffee Cart Business Plan Kit (EN)

> Sesión Claude Code, 28-oct-2026. F2 del gemelo EN de la cafetería móvil (SPEC delta D216-D235 y **§0, regla de jerga**).
> Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-11/` (= `BP11/`, datos y salidas del café), `business-plans-en-7/` (= `BP7/`, la
> Paella LIVE: las PROPUESTAS), `business-plans-en-4/` (= `BP4/`, el catering EN publicado) y `business-plans-en/` (= `BP/`, el
> código común y el brief de FT/CAF).
>
> **Cinco tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac), **reanudados con SendMessage** para
> mantener la terminología: **tanda 1 = (a) GCF-plan + revisión de GRP-plan ‖ (b) GCF-check + (e) contrato** → **tanda 2 =
> (c) cof_a ‖ (d) cof_b**. **No se escriben** GM (310), GRP-plan (59: se **revisa** en (a)) ni GLP-check (186 celdas del
> checklist cuya propuesta de la paella vale tal cual, con «Paella chef» → «Lead barista» en la columna C): los escribe
> `bp11.py preparar_tandas`. **Las entradas llevan SOLO lo que cambia.** Paso 1c hecho (28-oct): cada nota de (c)-(d)
> lleva el párrafo ES 1.0 FINAL de su ranura (`1b43d5fb`) y las cifras vetadas son las del ES final.

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1** de este fichero
(la 1 es el glosario §9 completo, OBLIGATORIO) + la de su tanda. El subagente no hace commit y no toca nada más que su salida.

---

## 0. Lo que cambia frente al brief de la Paella (manda sobre él en lo que choque)

**REDACTAR, NO TRADUCIR. La propuesta de la paella da la forma; la pista manda; cero vocabulario de paella.** Cada cadena de
las tandas xlsx trae `propuesta_en` = el EN de la Paella LIVE en ESA celda (o, si no había, el del catering), y cada párrafo
del docx trae en su `nota` la PROPUESTA EN DE LA PAELLA de la misma ranura. Reutiliza su estructura, su tono, su longitud, sus
tokens y las fuentes comunes (commissary, W-2, Insureon, thefoodcorridor, sales tax, service charge, SBA 7(a), COI).
**Reescribe** todo lo que hable de paella, paelleras, quemadores, propano, marisco, arroz, la van o el caso de la paella. El
`es` es la ranura del FOOD TRUCK ES (solo papel y longitud); el contenido de café sale de la pista, de `BP11/fuente_es_cof.json`
(checklist ES de 80 tareas, Word ES final por ranura, tabla de escalado, calculadora ES, contrato ES) y de
research. **Ninguna cifra del ES** (D231).

**Concepto (D219): COFFEE CATERING COMPANY con DOS estaciones.** Un **espresso cart** (NSF, lavamanos, depósitos de agua
potable y grises, nevera bajo barra) + un **portable espresso bar** para la segunda estación y los salones interiores; los dos
viajan en un **remolque cerrado** que arrastra el vehículo del dueño. Servicio **hosted** (paga el anfitrión): baristas W-2,
espresso, batch brew, cold brew, leches (la de avena incluida), siropes, vasos compostables, montaje y recogida; add-ons: horas
extra, branded cups y latte printing, bollería de un obrador con licencia, travel fee. **Tres motores**: **empresa entre
semana** (oficinas, conferencias, trade shows, brand activations: el VOLUMEN; 69.3 % de las reservas reales, Flashquotes),
**bodas** (el TICKET) y **fiestas privadas**; **festivales y farmers markets guest-pay** con minimum sales guarantee como
complemento. Base en una **commissary**. Fuera: coffee shop con local (Coffee Shop Kit), food truck de ruta diaria (Food Truck
Kit), espresso martinis («partner with a licensed mobile bar»: Mobile Bar Kit), drive-thru.

**Motor de eventos (el de la paella), solo con rótulos.** `B4` = **events per year** · `B5` = **average price per guest (excl.
sales tax, baristas included)** — la media de la MEZCLA — · `B6` = **average guests per event** (en un festival, cada bebida
vendida cuenta como un invitado). Dos líneas (D223): **coffee bar packages** (85 %) y **add-ons** (15 %). `B15` =
**compostable cups, lids, sleeves & napkins** (4 %). **Canal `B16`/`B17` = festivales y farmers markets guest-pay** (5 %) con
**cuota del organizador** (15 %) (D224: NO marketplaces; GigSalad / Thumbtack / The Bash / Zola van al marketing fijo). El
combustible del vehículo y del remolque es un **fijo** (`3-Year P&L!A27`); el del **generador** va en **suministros** (`B26`);
los **varios** (`B28`, 3 %) son imprevistos de cada evento (leche extra, hielo, cables, parking). Alcohol **0 %**. Personal:
`Staffing!B18` = 7 h por persona y evento, `B19` = 1.6 baristas por evento.

**Caso US (research §8; dry-run del paso 1a en `F2-NOTAS.md` §3; D15 VERDE sin calibrar):** 170 eventos × 95 invitados ×
$12.60 = **$203,490** ($1,197 por evento); CAPEX $71,290 + fondo de maniobra $29,000 = $100,290; propios $30,000 (30 %) +
préstamo **$71,000** (SBA 7(a): supera el tope de $50,000 del Microloan); EBITDA 21.8 %; neto $20,162 (9.9 %); equilibrio 141
eventos (138 de caja), holgura 24 % (caída absorbible 19 %); DSCR mín 2.58×; saldo mínimo en el **mes 7 (septiembre)**;
pesimista (128 · $11.34 · 86) $124,831 y **caja −$487: se agota, por poco** (decirlo sin dramatizar). Las notas del libro
describen el **método** o usan `valor_us`; el docx cita el caso SOLO con tokens. **Realismo**: 170 eventos = operador a tiempo
completo con venta corporativa activa y dos estaciones, no la media del primer año; Flashquotes da ≈ 15 reservas por operador
y año **solo en su plataforma** (nunca como «eventos esperados»); julio vende un tercio de diciembre.

**Vocabulario PROHIBIDO (gate D231 = `RX_COF_NO` + `check_textos`; los dos lo rechazan):**
- **Falsos amigos y nombre**: «cafeteria» (≠ cafetería), «mobile café»; «coffee truck» SOLO como formato (nunca como el
  negocio); «truck» suelto (valen «coffee truck», «food truck», «pickup truck» y el nombre «Food Truck Business Plan Kit»).
- **Paella** (las propuestas): paella, paella chef, paella pan, 3-ring burner, propane cylinder, wind guard, socarrat, sofrito,
  saffron, bomba, seafood, shellfish, mussels, clams, lobster, chorizo, aioli, fideua, tapas, sangria, shellstock, TPHC,
  «cargo van», «van upfit», «refrigerated van», «chef» suelto (aquí: barista, lead barista; «AI Chef Pro» y la firma valen).
- **Catering / BBQ / bar móvil**: plated, family-style, chef-attended, «themed / action / food / carving stations» (las
  **estaciones de café SÍ valen**: espresso station, second station, self-serve coffee station, handwashing station), taco bar,
  pasta, buffet, chafing, ezCater, smoker, pit, brisket, BBQ, grill, carving, meat; «cocktails» (valen «cocktail hour» y
  «espresso martini»), «bartender», «barback», «dry hire», «mixers», «cash bar», «mobile bar» (solo «licensed mobile bar» y
  «Mobile Bar Business Plan Kit»).
- **Food truck**: «per day», «operating days», «customers» (di clients, hosts, guests; «corporate customers» sí), «window»
  (solo **«service window»**). **«festival» y «farmers market» SÍ valen** (D224).
- **ES**: «España», «Spain», «Spanish», «IVA», «VAT» (salvo la nota UK), «EUR» / «€», «autónomo», «fijo discontinuo»,
  «convenio», «SMI», SL, IAE, AESAN, APPCC, CCAA, RGSEAA, FACe, Veri*factu, ITV, RGV, «RD …», «Ley …», «Reglamento (CE)»,
  Piaggio / Ape 50, «furgoneta», «bollería», «comida testigo» («cortado» SÍ vale: es carta US), Bizum, Bodas.net, Zankyou, «feria»; jerga:
  «freelance», «support kitchen», «Cambro», «recipe costing» / «escandallo» (di **cost per drink**); calcos «D-21 / D-14 /
  D-1»; «growing demand» (la demanda es estacional, research §0); kg / km / °C / litros / ml fuera de paréntesis.

**Cifras PROHIBIDAS (D231; las rechaza el check):** del **ES de la cafetería** (borrador del 28-oct; se refresca en 1c): sus
importes ≥ 10.000 € (108.810, 119.691, 129.266, 44.416, 60.061, 44.500, 43.216, 96.841…), «130 events», «135 guests», «6,10 /
6,20 €»; del **caso de la Paella** ($313,200, $344,520, $49,480, $64,000…, «135 events», «$40 per guest», «58 guests», «116
events», «$2,320»); del BBQ («150 events», «$38 per guest», «220 events», «$2,850» — **«128 events» SÍ vale**: es nuestro
pesimista), del catering («180 events», «$60 per guest»), del bar móvil («160 events», «$14 per guest») y del FT.

**Rótulos fijados** (`fijos_en` de tu entrada y POR_CELDA, ya los escribe `mapas.py`; si los citas, con esas palabras):
- `0. Assumptions`: «Events per year (year-1 average)», «Average price per guest (excl. sales tax, baristas included)»,
  «Average guests per event», «COFFEE BAR PACKAGES share of sales (baristas, espresso drinks, batch & cold brew, milks, syrups,
  cups)», «ADD-ONS share of sales (…)», «Compostable cups, lids, sleeves & napkins as % of sales», «FESTIVALS & FARMERS MARKETS
  share of sales (guest-pay pop-ups)», «Organizer / vendor fee on those sales (booth fees converted to %)», «Commissary, cart
  storage & trailer parking, per month», «Max events a year your stations and baristas can handle» (B51, informativo),
  «Contingency on the cart, portable bar, trailer, wrap and plan review lines (%)».
- `Startup Costs` 7-23 (D222): Espresso cart (…) · Portable espresso bar for the second station · Espresso machines: 2-group
  volumetric (220V) + compact 2-group · Espresso grinders ×4 · Enclosed cargo trailer (6×12 ft, ramp door) · Trailer wrap,
  hitch, tie-downs & cart loading ramps · LLC formation, contracts and legal · First-year permits and certifications · Mobile
  food unit plan review & cart inspection · POS, card readers & booking software · Batch brewer, airpots, cold brew system,
  smallwares & commissary storage racks · Opening inventory · Website, photos, tastings & launch · Power: inverter generator
  (5,500 W), cords & power distribution · Commissary deposit · Commissary rent before opening · Cart, bar, trailer and plan
  review contingency. Base de vida del vehículo = filas 7, 8, 11, 12, 15 (+ contingencia); de equipo = 9, 10, 16, 17, 20.
- `3-Year P&L`: A2 «Base case — coffee catering company with two espresso stations»; A10/A11 coffee bar package / add-on
  sales; A16 «Festival & market organizer fees»; A22 «Commissary, cart storage & trailer parking»; A24 utilities (generator
  fuel, water and ice); A27 «Tow vehicle & trailer fuel, maintenance and registration»; A32 «Phone, internet & card-reader
  data plans»; A33 «Espresso machine service, water filters & grinder burrs»; A34 «Food safety & barista training (CFPM,
  food handler cards)»; A35 «Tastings for prospects (corporate open house, couples)».
- `Staffing`: Owner / Lead Barista & Sales · Lead barista (part-time W-2) · Event baristas (hourly W-2) · On-call barista /
  driver (hourly W-2, peak months); A24 = W-2 frente a 1099 + «One barista serves about 50-65 drinks an hour».
- Checklist: «COFFEE CART STARTUP CHECKLIST — MOBILE ESPRESSO BAR & COFFEE CATERING», «PHASE 2: COMMISSARY, CART & TRAILER,
  HEALTH PERMIT & INSURANCE». Pestañas del plan: «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios»,
  «Staffing», «Instructions», «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», **«Phase 2 - Permits &
  Commissary»**, «Phase 3 - Equipment», «Phase 4 - Staff», «Phase 5 - Marketing», «Phase 6 - First 90 Days».

**Legal (research §6; lo no verificado va como «check with your county / state» o «ask your fire marshal», nunca como cifra
nacional):** un carro es *mobile food unit* (WA, IN) o *mobile food facility* (CA): permiso + **plan review ANTES de comprar el
carro** (Snohomish County como EJEMPLO leído: plan review $1,100, permiso anual $500 / $745 / $1,025) · **commissary**: «usually
yes; some counties exempt self-contained units: ask yours in writing» (CA HSC §114295, resumen; WA salvo RCW 43.20.148) · la
**leche es TCS**: cold holding a 41 °F (5 °C) o menos (mínimo del FDA Food Code, nombrado como tal) · **electricidad**: 2 grupos a
220V / 3,400 W = circuito dedicado (NEMA 6-20); si no, generador · **bomberos**: sin campana tipo I (no hay vapores grasos), pero
el **generador** sí tiene reglas (NFPA 96 «≥ 12 ft» solo como ejemplo, resumen) → «ask your fire marshal», nunca «no fire permit
needed» · **bollería** solo de obrador con licencia (nada de «cottage food pastries are fine») · **vasos compostables**: regla
LOCAL (Seattle como ejemplo) · **sales tax**: hosted = catering (toda la factura en muchos estados); guest-pay = bebida a bebida
· W-2, nunca 1099; service charge ≠ gratuity (IRS Rev. Rul. 2012-18); tip jar solo si el anfitrión lo acepta · seguros: GL
$1M/$2M con additional insureds ilimitados, commercial auto con el remolque, workers' comp, COI · sin alcohol · BLS OEWS no tiene
ocupación «barista» propia: 35-3023 (nunca «BLS barista wage»).

**Formato US**: punto decimal, coma de miles, «%» pegado, sin símbolo de moneda en el xlsx, «$» solo en el docx y en rangos de
mercado con fuente; pestañas citadas entre comillas dobles rectas con su nombre EN.

**Qué lees** (y nada más): tu entrada `BP11/tandas/<TANDA>.entrada.json`; `BP11/SPEC-delta.md` (D216-D235, §0);
`BP11/F1-research-us-delta.md` §1, §4-§8 (el §9 está en la sección 1 de este brief); `BP11/fuente_es_cof.json` (solo la parte de
tu tanda); de lo heredado, solo lo que tu entrada cite; `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-11/bp11.py check_textos --tanda <TANDA>     # (e): check_contrato --todas
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves, resultado del
check y 3-5 decisiones que deban conocer las demás tandas.

---

## 1. Glosario OBLIGATORIO — research §9 completo (copia literal de `F1-research-us-delta.md`)

### 9. Jerga profesional US (glosario OBLIGATORIO de los redactores; se añade a `../GLOSARIO-JERGA-ES-EN.md`)

**(a) Nombre del negocio.** El operador se llama a sí mismo **coffee catering** + **mobile espresso bar / mobile coffee cart** (Icon:
«Mobile Espresso Bar», «mobile coffee cart»; Big Dipper: «coffee cart and coffee truck services»; Houston: «coffee catering»
[leídas]); DFS: coffee catering 2,900 · coffee cart business 880 · mobile coffee bar 880 · mobile espresso bar 260. **Regla**: «coffee
cart» en nombre, slug, H1 y ficheros; «coffee catering» y «mobile espresso bar» en subtítulo y cuerpo; «coffee truck» y «coffee trailer»
como **formatos** (H2 y FAQ), nunca como nombre. **Falso amigo**: «cafetería» ≠ *cafeteria* (en US = comedor de colegio/empresa): nunca
«mobile cafeteria»; «café» solo en *café* = local.

| # | ES (cafetería móvil para eventos) | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Servicio de café para eventos | **coffee catering** · **coffee cart catering** | Houston, CCB [leídas]; DFS 2,900 / 590 |
| 2 | Barra con baristas · estación sin barista | **full-service espresso bar** · **self-serve coffee station** / **drop-off** (cold brew) | Sweet Carolinas, Flashquotes [leídas] |
| 3 | Carro · remolque · camión · bici · furgoneta | **espresso cart / coffee cart** · **coffee trailer** (Airstream) · **coffee truck** · coffee bike · coffee van | DFS 480 · 4,400 · 8,100 · 590 · 590; Big Dipper [leída] |
| 4 | Barra portátil · barista jefe · de evento | **portable espresso bar** · **lead barista** · **event barista** | por verificar (MBAR «portable bar») |
| 5 | Bebidas sin límite durante el servicio | «**unlimited made-to-order espresso drinks during your booked service window**» | Icon [leída] |
| 6 | Horas de servicio · hora extra · tarifa base | **service hours / service window** · **additional hour / extra time** ($75) · **base fee + hourly rate** | Icon, Flashquotes, Sweet Carolinas, GrindKit [leídas] |
| 7 | Precio por invitado · paquete | **per person (pp) / per guest** («$5/pp after 75 guests») · **package** («100 Guest Package») | Sweet Carolinas, Houston [leídas] |
| 8 | Paga el anfitrión · pagan los invitados · mínimo | **hosted** («host-paid, all-inclusive») · **guest-pay / pop-up** · **minimum sales guarantee** | GrindKit, Big Dipper [leídas] |
| 9 | Leche vegetal (suplemento) | **alt milk / plant-based milk** · **oat milk** («additional alternative milk $50», o incluida) | Sweet Carolinas, Houston [leídas] |
| 10 | Filtro por lotes · frío · nitro | **batch brew** · **drip coffee** («drip only») · **cold brew** ($100 add-on) · **nitro cold brew** | cart-king, Sweet Carolinas, Prima [leídas]; batch brew (resumen) |
| 11 | Bebida de autor · temporada · siropes caseros | **signature drinks** · **seasonal drinks** · **house-made syrups** | Icon, Sweet Carolinas [leídas] |
| 12 | Vasos personalizados · activación de marca | **branded cups** · **custom cup sleeves** · **latte logo printing** · **brand activation** · **trade show** | Icon, Big Dipper, Flashquotes [leídas] |
| 13 | Montaje, servicio y desmontaje | **setup, service & breakdown** · **load-in** | Icon [leída] |
| 14 | Enchufe · circuito propio · sin toma de agua | **standard 110V outlet** · **dedicated circuit** · «**No plumbing connection is required**» (self-contained) | Icon, Prima [leídas] |
| 15 | Ajustar molienda · sacar un café · doble | **dial in** · **pull a shot** · **double shot** (18 g in / 36 g out) | resumen · por verificar · resumen |
| 16 | Capacidad · consumo | **drinks per hour** (50-65 por barista; «50 cups per hour») · **drinks per guest** | Flashquotes, CCB, GrindKit [leídas] |
| 17 | Escandallo de bebida | **cost per drink** («all-in cost per drink») · **COGS %** | GrindKit [leída] (NO «escandallo» ni «recipe costing») |
| 18 | Señal · saldo · recuento final · desplazamiento | **retainer** (30-50 %, non-refundable) · balance due 14 days before · **final guest count** · **travel fee** ($/mile, free radius) | GrindKit, Flashquotes [leídas] |
| 19 | Tasa de cierre | **booking rate** (quotes → bookings) | Flashquotes [leída] |
| 20 | Cocina base · permiso · revisión de planos | **commissary** (+ agreement, log) · **mobile food unit / facility permit** · **plan review** | Snohomish [leída]; CA §114295 (resumen) |
| 21 | Manipulador · seguro y certificado | **food handler card** · CFPM · **general liability $1M/$2M** · **COI** · **additional insured** | resumen · ✅ BP, MBAR |
| 22 | Vasos compostables | **compostable cups** (single-use, onsite) | seattle.gov (resumen) |

**(e) No se traducen literalmente**: «cafetería móvil» → **coffee cart / mobile espresso bar** (nunca *mobile cafeteria*) · «café de
especialidad» → **specialty coffee** · «barra de café» → **espresso bar / coffee bar** · «carrito» → **cart** · «tueste / tostador» →
**roast / roaster** · «leche de avena» → **oat milk** · «feria» → **festival / farmers market / fair** · «evento de empresa» → **corporate
event** · «barista autónomo» → **W-2 event barista** · «IVA» → **sales tax** · «licencia de actividad» → **business license** · «registro
sanitario» → **health permit + plan review** · «señal» → **retainer / deposit** · «manipulador» → **food handler**.

**Capas (1) y (2), propuesta:** **Coffee Cart Business Plan Kit** · slug `coffee-cart-business-plan` (`/en/digital-products/coffee-cart-business-plan`)
· `coffee-cart-business-plan.docx` · `coffee-cart-financial-projections.xlsx` · `coffee-cart-pricing-calculator.xlsx` «Coffee Cart Pricing
Calculator (Cost per Guest to Quote)» · `coffee-cart-startup-checklist.xlsx` · pestaña F2 **«Phase 2 - Cart, Permits & Commissary»** (≤ 31 car.).

#### Términos para la landing

- **Por qué «cart» y no «truck»**: «truck» tiene más volumen (720 frente a 320), pero en eventos «cart» gana ×3-4 (§2), el AI Overview
  de «coffee truck business plan» separa street vending de catering (la ruta diaria es del Food Truck kit) y el caso **no tiene camión**.
  **Cobertura de «coffee truck»**: H2 de formatos con la tabla cart / trailer / truck (§4.1), FAQ «Can I use this as a coffee truck
  business plan?» («yes for events and catering; for daily street routes, see the Food Truck kit»), meta y keywords del schema.
- **Title** (≈ 105 car.): «Coffee Cart Business Plan Template for Coffee Catering: Word + Excel Projections + Pricing Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Coffee Cart ` + oro `Business Plan` + «Template for a Mobile Espresso Bar & Coffee Catering Company: Word Plan +
  Excel Projections + Per-Guest Pricing Calculator + Startup Checklist».
- **Meta** (≈ 155 car.): «Coffee cart business plan for coffee catering (cart, trailer or truck): Word plan, 3-year Excel projections,
  per-guest pricing calculator and startup checklist.»
- **H2 (6)**: What's Inside Your Coffee Cart Business Plan Kit · How Much Does It Cost to Start a Coffee Cart Business? (Cart vs. Trailer
  vs. Truck) · Coffee Cart Pricing: What to Charge per Guest and per Service Hour · Is a Coffee Cart Business Profitable? Corporate
  Events, Weddings and the Summer Dip · Coffee Cart Permits: Health Department, Commissary and Fire Marshal · Coffee Truck or Coffee
  Cart: Which Business Plan Do You Need?
- **FAQ (8)**: How much does it cost to start a coffee cart business? ($5-25K un carro; caso ≈ $71.5K) · Is a coffee cart business
  profitable? (EBITDA ≈ 21 %, neto ≈ 10 % a régimen; julio flojo) · How much should I charge for a coffee cart at an event? (mediana
  $1,040; 50 % central $765-1,700) · How many drinks per hour can one barista make? (50-65) · **Do you need a commissary kitchen for a
  coffee cart?** (PAA, §6.2) · What permits do I need? · Can I use this as a coffee truck or trailer business plan? · Can I sell
  pastries or espresso martinis? (§6.6, §6.8).
- **Alt**: «Espresso cart with two baristas serving lattes at a corporate event» · «Mobile espresso bar at an outdoor wedding cocktail
  hour» · «Barista dialing in a two-group espresso machine on a coffee cart». **Keywords**: coffee cart business plan, coffee truck
  business plan, mobile coffee business plan, coffee trailer business plan, how to start a coffee cart business, coffee catering, AI Chef Pro.
- **Interenlazado**: entrantes desde Coffee Shop, Food Truck, Mobile Bar, Catering, Coffee Shop Checklist Templates y el hub EN;
  salientes a Mobile Bar (espresso martinis) y Coffee Shop (siguiente paso: local).

---

## (a) Tanda GCF-plan — xlsx del plan (148 cadenas · 3.557 palabras ES) + revisión de las 59 GRP-plan

Salida `BP11/textos_en/GCF-plan.json` (todos los ids) + `BP11/textos_en/GRP-plan.revision.json` (solo las que cambian; `{}` si
ninguna). Qué llega: (1) **51 notas del caso** (Supuestos C4-C63, Startup D7-D20, P&L F10-F56, Staffing J5-J19): método, sin
cifras del caso salvo `valor_us`; (2) **36 celdas con pista de café** que la paella dejaba «limpias» (canal F16, umbrales F51 /
F56, E23, `Instructions!A12`, filas D18 39 / 41 / 42 / 43 / 44 / 49 / 50); (3) **la tabla D19** (14 filas × 4: Benchmark | Value |
Source | Note; 12 nuevas sin propuesta y 2 con la de la paella): Source = el dominio de una fuente «[leída]» o «Kit estimate»;
(4) las celdas cuya propuesta habla de paella. En la **revisión de GRP-plan** mira sobre todo `0. Assumptions!C35` y
`Instructions!D40` («off-season for weddings» / «slow month between wedding seasons» → el **valle de verano**, julio y agosto),
y que nada hable de cocinar. Cero «July is the slowest month» sin «for coffee carts» (Flashquotes).

## (b) Tanda GCF-check — checklist (89 celdas que cambian · 543 palabras ES)

Salida `BP11/textos_en/GCF-check.json`. Cada celda trae la pista de SU tarea (columnas que cambian). Las otras columnas de la
fila son el EN de la paella que vale (GLP-check): **no las contradigas** (si la B dice «Buy…», la E no puede hablar de alquilar).
Las 4 tareas nuevas (P3 filas 8, 10, 11, 12) se escriben enteras (B · C · D · E). Plazos «Week 1», «Weeks 3-8», «3 weeks out»;
columna C con «Owner», «Lead barista», «Event baristas», «Owner / Accountant», «Owner / Insurance broker». Orden de plazos
creciente dentro de cada fase (lección m13 de la paella). Toda licencia que prometa el Word tiene su tarea (regla B2).

## Docx — reglas comunes de las tandas (c)-(d)

Un párrafo por ranura, un solo run, ±30 % de la longitud de la ranura; cifras del caso **solo** con tokens `{{…}}` de la entrada
(los de partidas: `{{inv_carro}}`, `{{inv_barra}}`, `{{inv_espresso}}`, `{{inv_molinos}}`, `{{inv_remolque}}`,
`{{inv_remolque_wrap}}`, `{{inv_plan_review}}`, `{{inv_brew}}`, `{{inv_energia}}`, `{{inv_permisos}}`, `{{inv_lanzamiento}}`,
`{{inv_stock}}`; canal: `{{festivales_pct}}`, `{{festivales_comision}}`); **los de la paella no existen** (`{{inv_quemadores}}`,
`{{inv_paelleras}}`, `{{inv_propano}}`, `{{inv_furgoneta}}`, `{{inv_montaje}}`, `{{marketplace_pct}}`…). [98]: `{{cobro_dias}}`
para los cobros y `{{pago_dias}}` para los pagos (D113). Números de mercado solo de research «[leída]» con su fuente
(Flashquotes, GrindKit, operadores en zola.com, Icon, Coffee Cart Boys, Big Dipper, cart-king, Prima, BLS, Snohomish). «Kit
estimate» en minúscula en prosa. Validación: `bp11.py check_textos --tanda cof_a` (o `cof_b`).

## (c) Tanda cof_a — docx §1-§5 (29 párrafos · 2.954 palabras de ranura)

§1 resumen (oportunidad sin «growing demand», concepto de dos estaciones, inversión, proyecciones con la frase honesta, equipo) ·
§2 qué vende (formatos hosted / self-serve / guest-pay, carta corta, propuesta de valor, modelo económico por invitado) · §3
mercado (Flashquotes: mediana $1,040, $38 / $18 / $13 por invitado según tamaño, 69.3 % corporativo, estacionalidad con Month 1 =
marzo; mezcla del ejemplo 110 / 30 / 20 / 10) · §4 competencia (Porter; no competir por debajo de $612) · §5 marketing (empresas
+ bodas; The Knot / Zola; GigSalad / Thumbtack / The Bash; open house; catas).

## (d) Tanda cof_b — docx §6-§10 (32 párrafos · 3.765 palabras de ranura)

§6 operaciones (commissary; orden de compra; operativa de un evento de 2 h = 7-9 h de turno; 18 g por doble, 1.0-1.5 bebidas por
invitado; leche a 41 °F) · §7 equipo (4 puestos W-2, 50-65 bebidas por barista y hora, BLS 35-3023) · §8 finanzas con tokens
(equilibrio en eventos, holgura, saldo mínimo en el mes 7, **pesimista que agota la caja por poco**) · §9 legal (102-108 de las
notas; 108 cierra con la nota UK) · §10 conclusión, riesgos (sala sin 220V, julio, avería, cancelación), hoja de ruta, KPIs,
visión, cierre con la calculadora, el contrato y el checklist.

## (e) Tanda contrato — `textos_en/contrato_en.json` (92 párrafos ES · 3.047 palabras)

Entrada `BP11/tandas/contrato.entrada.json` (reglas, decisiones D230 cláusula a cláusula, glosario y el ES). Lista
`[{"estilo", "texto"}]` con los estilos del ES y `**negrita**`; cabecera legal literal tras la portada; corchetes para todo lo
editable; **circuito dedicado por escrito o generator fee**; retainer aplicado al precio; tramos «from X to less than Y» + «not a
penalty» + crédito por recolocar; lluvia ≠ fuerza mayor; Cooling-Off solo como nota «ask your attorney whether»; anexo corporativo
y de festivales con **minimum sales guarantee**. Validación: `bp11.py check_contrato --todas`.

## Después de las tandas (orquestador)

`bp11.py check_textos --todas` y `check_contrato --todas` (Mac) → VPS: `aplicar_en --idempotencia --json`, `calibracion`,
`ensamblar_docx --plan cof`, `contrato --salida dl/… --pdf`, `gates_en`, `barrido`, `regresion_cof.sh` → UNA revisión opus
(D232) → una ronda de arreglos por texto → F2-NOTAS §7-§8 → commit + push (`Via: Claude Code`).
