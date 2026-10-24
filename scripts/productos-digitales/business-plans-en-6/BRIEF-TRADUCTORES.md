# Brief para los redactores (subagentes Sonnet) — BBQ Catering Business Plan Kit (EN)

> Sesión Claude Code, 24-oct-2026. F2 del producto 26 de la tienda EN (SPEC delta D96-D113 y **§0, regla de jerga**).
> Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-6/` (= `BP6/`, datos y salidas del BBQ), `scripts/productos-digitales/
> business-plans-en-4/` (= `BP4/`, el catering EN publicado: el diccionario) y `scripts/productos-digitales/business-plans-en/`
> (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GBQ-plan + revisión de GRC-plan ‖ (b) GBQ-check** → **tanda 2 = (c) bbq_a ‖ (d) bbq_b**.
> **GM y GRC-plan no se escriben**: sus 312 + 79 cadenas son el EN publicado del Catering en esa misma celda
> (`BP6/textos_en/GM.json` y `GRC-plan.json`, los escribe `bp6.py preparar_tandas`). GRC-plan se **revisa** en (a).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1**
de este fichero (la 1 es el glosario §9 completo, OBLIGATORIO) + la de su tanda. El subagente no hace commit y no toca
nada más que su salida.

---

## 0. Lo que cambia frente a los briefs anteriores (manda sobre ellos en lo que choque)

**REDACTAR, NO TRADUCIR.** El `es` de cada cadena o párrafo puede ser del **FOOD TRUCK** (la ranura del circuito), del
**CATERING** (la `propuesta_en`, EN publicado en esa misma celda) o del **PARRILLERO ES 2.2** (en las notas del docx y en
`BP6/fuente_es_bbq.json`): ninguno de los tres es el contenido. **La pista manda**: dice qué va en esa celda para un
**full-service off-site BBQ caterer**. De la propuesta del catering reutiliza lo que valga (motor, impuestos,
financiación, commissary, buffet, drop-off, ezCater, W-2, service charge, COI) y reescribe lo que hable de la van
frigorífica, el generador, los quemadores o la inducción, las estaciones temáticas, el chef o el emplatado. Contenido BBQ:
`BP6/fuente_es_bbq.json` (checklist ES de 83 tareas con las SOLO_ES marcadas, el docx ES 2.2 por ranura, manual técnico,
carta de cortes, 10 experiencias y contrato del parrillero) + research. **Ninguna cifra del ES** (D110).

**Regla de jerga (§0 de la SPEC, John 13-oct): el producto no se traduce, se adapta** a cómo hablan los BBQ caterers,
planners y clientes de EE. UU. El **glosario de la sección 1 es obligatorio**. Reglas fijas: «BBQ catering» como nombre
(«barbecue» solo como variante); **«pitmaster»** para la persona (nunca «grill master» ni «chef»), «BBQ caterer» para el
negocio, «smoked meats» para el producto; **«commissary»** (nunca «support kitchen»); **«live pit on site»** = el smoker
trailer en el evento, un add-on de pago, NO la base del negocio; **«part-time hourly W-2 staff»**, nunca «freelance»;
**«Cambro» es marca**: di «insulated food carriers» o «hot boxes»; «carving station» sí, las demás «stations» no.

**Medidas US (John, 13-oct)**: principales **lb y oz, °F, miles, gallons / quarts, sq ft**; la métrica entre paréntesis
para UK y Australia: «12 lb (5.4 kg)», «225 °F (107 °C)», «5 gallons (19 liters)», «200 sq ft (19 sq m)» (el gate común
no admite «m²»). Nada de kg, km, litros ni °C como unidad principal (el gate `RX_BBQ_NO` lo rechaza). El ES mide en kg,
°C, km y litros (32 kg por parrilla, 0,8 kg de carbón por kg de carne, 70 °C…): conviértelo siempre.
**Temperaturas**: la de **CALIDAD** (brisket ≈ 203 °F, Kit estimate) y el **MÍNIMO SEGURO del FDA Food Code** (145 °F 15 s
carne intacta · whole roasts 145 °F 4 min · **155 °F 17 s inyectada, ablandada o picada, sausage incluida** · 165 °F aves;
hot holding ≥ 135 °F; enfriado «to 70 °F within 2 hours and to 41 °F within a total of 6 hours»; recalentado a 165 °F)
**nunca en la misma columna ni en la misma frase sin decir cuál es cuál**. Inyectar un brisket o un pork butt lo vuelve
*non-intact* (155 °F). Las AESAN del ES (70 / 74 °C) no se usan.

**Qué lees** (y nada más): tu entrada `BP6/tandas/<TANDA>.entrada.json`; `BP6/SPEC-delta.md` (D96-D113, §0);
`BP6/F1-research-us-delta.md` §1, §4, §5, §6 y §8 (el §9 está en la sección 1 de este brief); `BP6/fuente_es_bbq.json`
(solo la parte de tu tanda); para el docx, el EN del catering de tus ranuras (`BP4/docx_en_cat_a.json` o `_b.json`) como
**modelo de estructura**, no de contenido; de lo heredado, solo lo que tu entrada cite; `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves,
resultado del check y 3-5 decisiones que deban conocer las demás tandas.

**Concepto (D99): FULL-SERVICE OFF-SITE BBQ CATERER.** El pitmaster **ahúma en el patio de la commissary** (brisket,
pulled pork, ribs, chicken, sausage), **mantiene en caliente** en insulated food carriers / hot boxes y sirve en
**staffed buffet con carving station**. El **smoker trailer** (offset / reverse-flow, clase 500 gal) va al evento solo en
bodas y premium («live pit on site», add-on de pago); lo arrastra la **pickup del dueño** («tow vehicle», $0 en el plan).
Una **cargo van usada** (NO frigorífica) lleva las hot boxes a drop-offs y buffets. Cinco líneas de demanda: drop-off
corporativo (boxed BBQ lunches, ezCater) · fiestas privadas y graduaciones · empresa full-service · bodas · **live-fire
premium** (Argentine asado, Santa Maria tri-tip, whole hog / La Caja China; ≈ 8 eventos, ≈ 11 % de las ventas). Las 10
experiencias del ES → **menu styles** (Texas · Carolina · Kansas City · Memphis · Santa Maria · Argentine asado ·
Brazilian churrasco · pig roast · fire show · corporate boxed lunch). No es nuestro comprador: el BBQ restaurant
(Restaurant Kit), el BBQ food truck (Food Truck Kit), quien vende desde casa (ilegal).

**Motor de eventos (el del catering), solo con rótulos.** `B4` = **events per year** · `B5` = **average price per guest
(excl. sales tax, service included)** — la media de la MEZCLA, no el precio de un paquete · `B6` = **average guests per
event**. Ingresos = eventos × precio × invitados; los años 2-3 crecen en EVENTOS; el break-even sale en **events per
year**. Dos líneas de venta (D103): **BBQ packages** (88 %: smoked meats, sides, bread & sauces, staffing) y **add-ons**
(live pit on site, postres, aperitivos, bebidas sin alcohol, alquileres, travel fees). `B15` = **disposables, wood &
cooking fuel** (variable, 3.5 %: la leña, el carbón, los pellets y el propane backup escalan con las libras). El
combustible del VEHÍCULO es un **fijo** (`3-Year P&L!A27` «Vehicle & trailer fuel, maintenance and registration»); los
**varios** (`B28`, 3 %) son imprevistos de cada evento (carne extra, hielo, parking) **sin combustible**. Alcohol **0 %**.
Personal: `Staffing!B18` = horas por persona y evento, `B19` = personas por evento, `B20` = horas × personas × **eventos**.

**Vocabulario PROHIBIDO (gate D110 = `RX_BBQ_NO`, `check_textos` lo rechaza):** del FT: «per day», «operating days»,
«customers» (di **clients** o **guests**; «corporate customers» sí), «truck» (el vehículo es **tow vehicle** o **pickup**,
nunca «pickup truck»; solo «BBQ food trucks» para el competidor y el nombre «Food Truck Business Plan Kit»), «window»
(ojo: «a 2-hour window» del enfriado también salta: di «within 2 hours»), «festival»; del catering: «plated»,
«chef-attended / themed / action stations», «chef» suelto y «executive / sous chef» (di **pitmaster**, **pit cook**,
**lead cook**; solo la fila OEWS de la D19 dice «chefs and head cooks»), «induction», «taco bar», «pasta», «12 cuisines»,
«refrigerated van»; del bar móvil: «cocktails» (sí «cocktail hour»), «bartender», «dry hire», «mobile bar», «barback»,
«mixers», «specialty / cash bar»; del ES: «Spain», «IVA», «VAT» (salvo la nota UK), «EUR» / «€», «autónomo», «fijo
discontinuo», SL, IAE, AESAN, APPCC, «RD …», «Reglamento (CE)», CCAA, ATP, FACe, Veri*factu, Bodas.net, Zankyou, Hosply,
GGM, «parrillero», «chuletón», «lechazo», «cochinillo», «carné»; de la jerga: «freelance», «grill master», «support
kitchen», «grill / roast catering», «Cambro»; calcos «D-21 / D-14 / D-1»; kg / km / °C / litros fuera de paréntesis.

**Cifras PROHIBIDAS (D110; las rechaza el check):** del ES del parrillero 190.000 · 205.200 · 215.460 · 76.522 · 54.596 ·
21.926 · 87.357 · 65.400 · 15.737 · 160.401 · 151.894 · 182.179 · 192.570 · 109.706 · 80.294 · 92.616 · 57.983 · 14.527 ·
16.887 · 15.403 · 17.090 · 19.867 · 20.538 · 138.000 · 243.100 · 40.588 · 12.934 · 10.835 · 6.145 · 4.912 · 4.251 ·
49.900 · 62.000; 77.000 / 84.000 / 22.000 con € o EUR; «95 events», «80 guests per event», «81 events», «76 events»,
«75-80 events», «6.7 events a month», «25 €», «27.51», «57.7 %», «31.8 %», «30.5 %», «25.1 %», «DSCR 1.51», «83 tasks»,
«93 suppliers», «11 deliverables», «8 regions», «18 cuts», «12-cut menu», «v1.1»; del caso del catering EN («180 events»,
«$60 per guest», sus importes ≥ 10,000), del mobile bar EN (212,800 · 76,972 · 47,530 · 35,772 · 130,032 · 323,400, «160
events», «$14 per guest») y del FT EN. **«$25 per guest» no se veta.** Las notas del libro describen el **método** o usan
`valor_us`; el caso US (research §8, dry-run en `F2-NOTAS.md` §3) es **150 eventos × 75 invitados × $38** = $427,500.

**Rótulos fijados** (`fijos_en` de tu entrada y POR_CELDA, ya los escribe `mapas.py`; si los citas, con esas palabras):
- `0. Assumptions`: «Events per year (year-1 average)», «Average price per guest (excl. sales tax, service included)»,
  «Average guests per event», «BBQ PACKAGES share of sales (smoked meats, sides, bread & sauces, staffing)», «ADD-ONS
  share of sales (…)», «Cost of goods on BBQ PACKAGE sales (raw meat, sides, bread, sauces)», «Disposables, wood &
  cooking fuel as % of sales», «Corporate catering marketplace share of sales (e.g. ezCater)», «Commissary kitchen rent &
  smoker trailer parking, per month», «Useful life of the smoker trailer, van and fit-outs (years)», «Max events a year
  your pit and crew can handle» (B51, informativo), «Contingency on the trailer, van and fit-out lines (%)».
- `Startup Costs` filas 7-23 (D102, orden del inventario §3): Smoker trailer (offset / reverse-flow, 500-gal class, new) ·
  Smoker trailer upfit · Live-fire rig · Commissary storage fit-out · Used cargo van · Van upfit · LLC formation, contracts
  and legal · First-year permits and certifications · Plan review / trailer inspection (only if your county requires it)
  · Catering software, card reader and tablet · Smallwares & pit tools · Opening inventory · Website, photos, launch and
  first bridal show · Holding & service equipment · Commissary deposit · Commissary rent before opening · Smoker trailer,
  van and fit-out contingency. Base de vida del vehículo = filas 7, 8, 11, 12, 15 (+ contingencia); de equipo = 9, 10,
  16, 17, 20.
- `3-Year P&L`: A2 «Base case — BBQ caterer (smoked meats, off-site)»; A10/A11 BBQ package / add-on sales; A15
  «Disposables, wood & cooking fuel»; A16 «Corporate catering marketplace fees»; A22 «Commissary kitchen rent & smoker
  trailer parking»; A24 utilities (sin propano); A25 seguros; A26 permisos; A27 «Vehicle & trailer fuel, maintenance and
  registration»; A30 software; A31 «Linens, uniforms and cleaning»; A32 «Waste, grease and ash disposal»; A33 «Smoker &
  equipment repair»; A34 «Food safety training (ServSafe Manager, food handler cards)»; A35 «Tastings for prospects»; A55
  «Commissary & parking / Sales».
- `Staffing`: Owner / Pitmaster & Sales · Pit cook / lead cook (W-2) · Event staff (servers, buffet attendants, carvers;
  hourly W-2) · Prep cook / driver (part-time W-2); A24 = nota W-2 / 1099 + «One pit cook can watch several cooks at once».
- Checklist: título «BBQ CATERING STARTUP CHECKLIST — OFF-SITE BBQ CATERER», «PHASE 2: COMMISSARY, SMOKER TRAILER, FIRE
  RULES & PERMITS». Pestañas: «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios», «Staffing»,
  «Instructions», «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», **«Phase 2 - Pits, Fire &
  Permits»**, «Phase 3 - Equipment», «Phase 4 - Staff», «Phase 5 - Marketing», «Phase 6 - First 90 Days».

**Legal (research §6; lo no verificado va como «check your county / state rules» o «check with your fire marshal», nunca
como cifra):** commissary obligatoria, nada de cocina de casa (Food Code 3-201.11(B); el cottage food excluye la carne en
Texas) · ahumar o servir desde el trailer en el evento puede convertirlo en **mobile food unit** (Texas 25 TAC §228.221;
Florida y North Carolina, parecido; California sin verificar): «ask your county»; si no hay permiso, se ahúma en la
commissary · fuego: Class K + 2A:10BC, 10 ft, propano ≤ 200 lb (IFC según lo adopte la ciudad); burn bans y carpas sin
verificar · approved source (USDA o inspección estatal; whole hog nunca custom exempt) · seguros: GL / BOP, commercial
auto que cubra el remolque, workers' comp, inland marine, COI / additional insured · W-2, nunca 1099 · sales tax sobre
toda la factura de catering · alcohol: el BBQ caterer no lo vende; si lo pone el cliente, un servicio con licencia.

**Formato US** (como siempre): punto decimal, coma de miles, «%» pegado, sin símbolo de moneda en el xlsx, «$» solo en el
docx y en rangos de mercado con fuente; pestañas citadas entre comillas dobles rectas con su nombre EN.

---

## 1. Glosario OBLIGATORIO — research §9 completo (copia literal de `F1-research-us-delta.md`)

> Con la regla de **medidas y temperaturas** de la sección 0: p. ej. el término 16 se escribe «cooling to 70 °F (21 °C)
> within 2 hours and to 41 °F (5 °C) within a total of 6 hours». **Dos cambios de la SPEC sobre el §9 literal**: la
> pestaña F2 es **«Phase 2 - Pits, Fire & Permits»** (D107; no «Smoker & Permits») y la calculadora se titula «BBQ Catering
> Pricing Calculator (Pounds of Meat per Guest to Quote + Smoke Schedule & Shopping List)» (D98).

### §9. Jerga profesional US (glosario OBLIGATORIO de los redactores)

> **No se traduce: se adapta** en tres capas: (1) producto (nombre, slug, ficheros, pestañas, rótulos), (2) contenido de
> los 4 entregables, (3) SEO de la landing. «leída» = el término aparece en la página abierta el 24-oct; «(resumen)» =
> snippet; «no hallado» = término común que no apareció en lo leído.

**(a) Nombre.** **«BBQ catering»** (9.900/mes, igual que «barbecue catering») es como lo llaman Q39, Hutchins y Owen's.
**Regla**: «BBQ catering» en nombre, H1 y ficheros; «barbecue» como variante; **«pitmaster»** para la persona (no «grill
master»); «smoked meats» para el producto. Nunca «grill catering», «roast catering» ni «parrilla service» como nombre.

| # | Concepto (ES parrillero) | Término US | Dónde aparece | Nota |
|---|---|---|---|---|
| 1 | Empresa de parrilla para eventos | **BBQ catering** company / BBQ caterer | q39kc.com · hutchinsbbq.com (leídas) | nombre |
| 2 | Maestro parrillero (dueño) | **pitmaster** | Owen's («a dedicated pitmaster, crew, and smoker») · hutchins (leídas) | «Owner / Pitmaster & Sales» |
| 3 | BBQ pit con hogar lateral | **offset smoker** («offset firebox») · reverse-flow · **stick burner** | yodersmokers.com (leída) · stick burner: no hallado | stick burner solo en prosa |
| 4 | Remolque-parrilla | **smoker trailer** («Barbecue Smoker with Trailer») | webstaurantstore TS500 (leída) | 2.900/mes |
| 5 | Combustible | **solid fuel** (wood, charcoal, pellets) · **pellet smoker** | webstaurant · Corpus Christi FD (leídas) | `B15` y fire code |
| 6 | Leña de roble | **post oak** (TX) · hickory · **red oak** (Santa Maria) | zola Heim («Our post oak wood», leída) · El Vaquero (resumen) | |
| 7 | Cocción lenta | **low and slow** | zola Heim (leída) | |
| 8 | Pecho entero · punta · parte magra | **packer brisket** · **point** · **flat** | fieryfoodscentral («whole packer briskets») · destination-bbq («brisket point») (leídas) | flat: no hallado |
| 9 | Puntas caramelizadas | **burnt ends** | destination-bbq.com/glossary (leída) | Kansas City |
| 10 | Paleta de cerdo desmigada | **pulled pork** (pork butt / shoulder) | Owen's · fieryfoods (leídas) | |
| 11 | Costillar | **spare ribs** · **St. Louis style** · **baby backs** | destination-bbq (leída) | |
| 12 | Adobo seco · corteza · anillo de humo | **(dry) rub** · **bark** · **smoke ring** | destination-bbq (leída) | |
| 13 | Meseta · envolver | **the stall** · **the wrap / Texas crutch** (foil o **butcher paper**) | destination-bbq (leída) · bradleysmoker (stall, resumen) | |
| 14 | Reposo y mantenimiento | **resting** · **holding** en **insulated food carriers / hot box** («faux Cambro») | girlscangrill (resumen) | «Cambro» es marca: no en rótulos |
| 15 | Mantener caliente (norma) | **hot holding at 135 °F** | Food Code 3-501.16 (leída) | |
| 16 | Enfriar · recalentar | **cooling** (135→70 °F 2 h; 41 °F 6 h) · **reheating for hot holding** (165 °F) | Food Code 3-501.14 / 3-403.11 (leídas) | |
| 17 | Merma / rendimiento | **yield** («about 50% of the fresh weight») · shrink | fieryfoodscentral (leída) | calculadora |
| 18 | Gramos por invitado | **pounds of meat per guest** («about ½ lb», «one-third to one-half pound») | Owen's · hutchins (leídas) | lb crudas en la calculadora |
| 19 | Precio por invitado · mínimo | **per person / per guest** · **guest minimum** («30-guest minimum», «75 Person minimum») | Owen's · hutchins · Heim (leídas) | `B5` = per guest |
| 20 | Entrega sin servicio | **drop-off** · **Drop & Set** · «delivered ready to serve» | q39 · Owen's · hutchins (leídas) | línea corporativa |
| 21 | Servicio completo | **full-service** («setup, service, cleanup») | q39 · sonnybryans (leídas) | |
| 22 | Buffet con personal | **(staffed) buffet** · «tend the buffet» | q39 (leída) | |
| 23 | Corte al momento | **carving station** · «carving to order» · food stations | Owen's · zola Heim (leídas) | |
| 24 | Parrilla en el evento | **live pit on site** · «on-site pit» | Owen's · hutchins (leídas) | add-on premium |
| 25 | Guarniciones | **sides** (mac n cheese, potato salad, coleslaw, collard greens, baked beans) | Owen's · q39 (leídas) | |
| 26 | Bandejas | **chafing dishes** · buffet trays · **boxed BBQ lunches** | hutchins (leída) | |
| 27 | Señal · cargo del evento | **deposit** («50% nonrefundable») · **event fee** / **service fee** | Owen's · hutchins (leídas) · Southside (resumen) | service fee ≠ gratuity |
| 28 | Cocina de apoyo | **commissary** / **central preparation facility** | 25 TAC §228.221 (leída) · bbq-brethren (SERP) | nunca «support kitchen» |
| 29 | Remolque que cocina en el evento | **mobile food unit** (TX) · mobile food dispensing vehicle (FL) · mobile food facility (CA) | §228.221 (leída) · FL (resumen) | según estado |
| 30 | Autorización puntual | **temporary food establishment permit** (CA: TFF) | NC (resumen) · BP4 §6.1 | |
| 31 | Origen autorizado | **approved source** · USDA-inspected · «custom exempt… not for sale» | Food Code 3-201.11 · nichemeat (leídas) | whole hog |
| 32 | Extintor | **Class K** extinguisher (2.5 gal para solid fuel) | Corpus Christi FD (leída) | |
| 33 | Asado argentino | **Argentine asado** · **parrilla** · **chimichurri** | Asado Life / Gaucho Parrilla en The Knot (resumen) | chimichurri se usa igual |
| 34 | Parrilla de altura regulable | **Santa Maria grill** · **tri-tip** over red oak | El Vaquero / Kullman (resumen) | California |
| 35 | Cochinillo / caja china | **pig roast** · **whole hog** · **La Caja China** · lechón | Meadow Creek PR72 (resumen) · caja china: no hallado | |
| 36 | Estilos regionales | **Texas · Kansas City · Memphis · Carolina** («four types of BBQ», PAA) | SERP §3 | menú del docx |

**(e) Términos ES que NO se traducen literalmente:** «parrillero» → **pitmaster** (persona) o **BBQ caterer** (negocio) ·
«asador» → **asado cross** o **spit roast**, nunca «roaster» como negocio · «brasa» → **live fire / coals** · «cocina de
apoyo» → **commissary** · «autónomo» → **single-member LLC** · «fijo discontinuo» / «freelance» → **part-time hourly W-2
staff** · «carnet de manipulador» → **food handler card** · «APPCC» → **HACCP-based food safety plan** · «plan B de gas» →
**propane backup** · «época de peligro» → **county burn ban** · «chuletón» → **bone-in ribeye / tomahawk** · «picaña» →
**picanha** · «entraña» → **skirt steak** · «vacío» → **flank / bavette** · «provoleta» → **grilled provolone** · «finca» →
**venue** (ranch, barn venue) · «IVA» → **sales tax** · «señal» → **deposit** · «escandallo» → **cost per guest / food cost**.

**Capas (1) y (2):** **BBQ Catering Business Plan Kit** · slug `bbq-catering-business-plan` · `bbq-catering-business-plan.docx`
«BBQ Catering Business Plan (10 Sections)» · `bbq-catering-financial-projections.xlsx` · `bbq-catering-pricing-calculator.xlsx`
«BBQ Catering Pricing Calculator (Pounds of Meat per Guest to Quote)» · `bbq-catering-startup-checklist.xlsx` · pestaña F2
**«Phase 2 - Smoker & Permits»** (26 car., ≤ 31) · rótulos con los términos 1-36 (`B11`, `B15`, `B24` y Staffing como en §8).

### Términos para la landing (DataForSEO US, 24-oct)

| Keyword | Vol. | Comp. | Uso |
|---|---|---|---|
| **bbq business plan** | **70** (10 → 90) | LOW | title, meta, H2 1 |
| **bbq catering business plan** · barbecue catering business plan | 10 · s/d | LOW | slug, H1 |
| how to start a bbq business · how to start a bbq catering business · bbq catering business | 70 · 10 · 40 | LOW | H2 + FAQ · subtítulo |
| bbq catering · barbecue catering | 9.900 · 9.900 | LOW | cuerpo, alt |
| bbq catering prices · … cost per person · bbq catering menu | 170 · 20 · 320 | LOW | H2 precios y menú + FAQ |
| smoker trailer · bbq smoker trailer · pitmaster | 2.900 · 590 · 8.100 | HIGH · HIGH · LOW | H2 de costes, alt, rótulos |
| bbq business plan template · bbq food truck business plan · how to start a bbq business from home | 10 · 20 · 10 | LOW | keywords / FAQ |
| bbq catering near me | 18.100 | LOW | local: no se ataca |

- **Title** (≈ 105 car., patrón catering): «BBQ Catering Business Plan Template: Word + Excel Financial Projections + Pricing
  Calculator | AI Chef Pro».
- **H1 (Forma B)**: `BBQ Catering ` + oro `Business Plan` + «Template for an Off-Site Barbecue Caterer with a Smoker
  Trailer: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist».
- **Meta description** (≈ 151 car.): «BBQ business plan template for a smoked-meat catering company: Word plan, 3-year Excel
  projections, per-guest pricing calculator and startup checklist.»
- **H2 (6)**: What's Inside Your BBQ Business Plan Kit for Catering · How Much Does It Cost to Start a BBQ Catering
  Business? (Smoker Trailer, Commissary, Permits) · BBQ Catering Prices: What to Charge per Person, Drop-Off vs.
  Full-Service · Can You Start a BBQ Business From Home? Licenses, Commissary and Fire Rules · Is a BBQ Business
  Profitable? Your 3-Year Projections · BBQ Catering Menu: Pounds of Meat per Guest, Smoker Yield and Live-Fire Asado.
- **FAQ (redacción del comprador)**: «How much does it cost to start a BBQ catering business?» · «How profitable is a BBQ
  business?» · «How to charge for catering BBQ?» · «How much barbecue per person for catering?» · «Can I sell BBQ from my
  home without a license?» · «Do I need a commissary kitchen for BBQ catering?» · «What smoker do I need to start a BBQ
  catering business?» · «What are the four types of BBQ?» · «Is this plan for a BBQ food truck or restaurant?».
- **Alt**: «Pitmaster slicing brisket at a carving station during an outdoor wedding» · «Offset smoker trailer at a BBQ
  catering event» · «Drop-off BBQ catering trays with pulled pork, ribs and sides for a corporate lunch».
- **Keywords del schema / docProps**: bbq catering business plan, bbq business plan, bbq business plan template, barbecue
  catering business plan, how to start a bbq catering business, bbq catering prices, smoker trailer, AI Chef Pro.

---

## (a) Tanda GBQ-plan — xlsx del plan financiero (128 cadenas · ≈ 3.000 palabras ES) + revisión de las 79 GRC-plan

Entrada `BP6/tandas/GBQ-plan.entrada.json` → **dos** salidas:

1. `BP6/textos_en/GBQ-plan.json` (`{"<id>": "<EN>"}` con TODOS los ids y nada más):
   - **Texto libre** (≈ 60): notas de la col. C de `0. Assumptions` (pistas por celda C4-C62: caso, mezcla BBQ packages /
     add-ons, B15 con leña y combustible de cocina, marketplaces, commissary donde se pueda ahumar, seguros con el
     remolque, varios SIN combustible, préstamo SBA 7(a), vidas 7 / 5, capacidad B51 informativa, rampa, cobro 7 días con
     depósito del 50 % sin anticipos en el modelo, alcohol 0 %), notas de `Startup Costs` (col. D, filas 7-20 y 27, con
     los importes de research §8 y el tow vehicle propio), del P&L (F10/F11, F22, F24, F32-F35 y los umbrales F51-F55 de
     D104), de `Staffing` (J5-J8, J18-J19), de `Instructions` (A5) y de `12-Month Cash Flow` (D32). La nota `C5` explica
     cómo pasar de los precios por paquete de la calculadora al precio medio de la mezcla (D105).
   - **Tabla D19, filas 55-68 «US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES»**, una celda cada vez
     (`por_celda`). **Las filas 58, 62, 63, 65 y 67 traen la propuesta del catering** (neto 7-8 %, marketplace ~15 %,
     depósito —cámbialo a 50 % nonrefundable—, shared kitchen $15-45/h, seguros Insureon); las otras 9 son nuevas, sin
     propuesta (precio por servicio, operador de Los Angeles, carne por invitado, rendimiento ≈ 50 %, food cost, smoker
     trailer, sueldos OEWS, mínimos de invitados, leña y personal). `Source` = el dominio de la fuente LEÍDA (q39kc.com,
     eventective.com, hutchinsbbq.com, zola.com, fieryfoodscentral.com, sonnybryans.com, yodersmokers.com,
     webstaurantstore.com, bls.gov, galleysolutions.com, itsacheckmate.com, thefoodcorridor.com, insureon.com) o «Kit
     estimate». «chefs and head cooks» SOLO en la fila 64.
   - **Tabla D18 «WHY THIS MODEL IS BUILT THIS WAY»**: las 11 celdas que hablaban de la van, el generador o el
     combustible (A39, C39, C41, D41, A42, A43, C44, D44, A49, B49, D49): describe el MÉTODO del libro con el smoker
     trailer + la furgoneta. Fila 39 = «Commissary kitchen and smoker trailer parking» · fila 41 = dos vidas útiles: el
     smoker trailer, la van y sus upfits frente al live-fire rig y el equipo · fila 42 = seguros del trailer y la van,
     una sola vez como gasto anual · **fila 43 = «Wood, charcoal and propane backup»** (C: dentro de la línea de
     desechables, leña y combustible de cocina, % de ventas) · fila 44 = contingencia sobre el trailer, la van y sus
     upfits · **fila 49 (M6 del bar móvil)**: A «Miscellaneous event costs» · B «A miscellaneous line typed in among the
     fixed costs» · D «Extra meat, ice and venue parking rise and fall with the number of events: among the fixed costs
     they would distort the break-even.»
2. `BP6/textos_en/GRC-plan.revision.json`: revisa `revisar_reutilizadas.GRC-plan` (79: el resto de la tabla D18 y notas
   del motor). Son el EN del catering, que ya habla de eventos y de comida; si `en_actual` vale para un BBQ caterer, **no
   la incluyas**; si no, `{"<id>": "<EN corregido>"}`. **Coherencia por fila de la D18** (tus celdas de 1. y estas son la
   misma fila): B39 / D39 (commissary y aparcamiento del smoker trailer; «Catering has to be cooked» → «Smoked meat has
   to be cooked in a permitted kitchen»), B42-D42 (seguros del trailer y la van), **C43 «Included in the disposables,
   wood and cooking fuel line»** y D43 (escala con las libras y los eventos), **C49 «A percentage of sales, treated as a
   variable cost; vehicle and trailer fuel has its own fixed line»**, **C50** («Every sale carries its cost of goods: BBQ
   packages and add-ons each at their own rate») y A44 / B44 si chocan. Pagos: los particulares pagan depósito y saldo
   con tarjeta; algunas empresas por ACH. Si ninguna cambia: `{}`.

Umbrales del P&L (D104, ya en el libro): margen bruto del motor ≥ **58 %** · coste de mercancía ≤ **35 %** · personal ≤
**38 %** · commissary y parking ≤ **7 %** · neto ≥ **5 %**, «kit benchmark (editable estimate)».

```bash
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda GBQ-plan
python3 scripts/productos-digitales/business-plans-en-6/bp6.py preparar_tandas && \
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda GRC-plan
```

## (b) Tanda GBQ-check — checklist (275 cadenas: 68 tareas × 4 columnas + 3 textos)

Entrada `BP6/tandas/GBQ-check.entrada.json` → salida `BP6/textos_en/GBQ-check.json` (`{"<id>": "<EN>"}` con TODOS los
ids): **68 tareas en 6 fases (11/13/12/10/12/10), no se añaden ni quitan**; cada celda es un id (`por_celda`): col. B =
la tarea (corta, imperativa), C = responsable, D = plazo US, E = nota práctica. **La pista de cada fila dice qué tarea va
en esa ranura** (D107): «[sobrevive]» = la tarea del catering vale casi literal (su `propuesta_en` es la base);
«[sobrevive con ajuste]» = la misma tarea con otras palabras; «[nueva]» = tarea distinta, la `propuesta_en` solo sirve
para el tono y la longitud. **Columna C: «Executive chef» → «Pitmaster»** (y «Bartenders» desaparece con la tarea P4 fila
11). **P6 sin el calco «D-21 / D-14 / D-7 / D-1»** del catering publicado: «3 weeks out», «2 weeks out», «5-7 days
out», «1-2 days out», «Day of event», «Within 48 hours», «Weekly», «Day 90». Contenido: `fuente_es_bbq.json` →
`checklist_es` (fuera las SOLO_ES y lo español de las PARCIALES) + research §6. P2 = commissary donde se pueda ahumar,
agreement por escrito, county permit + «ask your county» por la mobile food unit, temporary event permits, fire marshal,
smoker trailer + van (compra, DMV, upfit), seguros, residuos y ceniza. P5 = The Knot, WeddingWire, Zola, ezCater,
Thumbtack, Google Business Profile, tasting de lanzamiento y bridal show. Los 3 textos que no son tareas (títulos de las
fases 1 y 3 y la nota del contador) vienen con la propuesta del catering: cámbialos solo si no valen.

```bash
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda GBQ-check
```

---

## Docx — reglas comunes de las tandas (c)-(d)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»: un párrafo EN por párrafo ES, sin saltos de línea en el
cuerpo, subtítulos de una línea sin punto final, toda cifra del caso con su token `{{…}}`, importes y porcentajes de
mercado solo si están en research/SPEC con fuente), más:

- **Escribes cada párrafo** (D108): `notas_del_plan` y la `nota` de CADA párrafo (todos la tienen) dicen qué va en esa
  ranura; **al final de cada nota va el párrafo ES 2.2 del parrillero de la MISMA ranura** (contenido de referencia: sus
  cifras, sus `{TOKENS}` en mayúsculas y todo lo español NO se usan); el `es` (food truck) solo da el papel y la longitud
  (±30 %); el EN del catering de la misma ranura (`BP4/docx_en_cat_a.json` / `_b.json`, clave = mismo `i`) es el modelo
  de estructura. Más contenido en `fuente_es_bbq.json` (manual, carta, experiencias, contrato) + research §1, §5, §6, §8.
- **Tokens del BBQ** (usa estos, no los alias heredados): `eventos_a1/_a2/_a3`, `precio_invitado`,
  `precio_invitado_con_tax`, `invitados_evento`, `invitados_a1`, `ventas_evento`, `capacidad_eventos`,
  `cuota_paquetes_pct`, `coste_paquetes_pct`, `coste_extras_pct`, `equilibrio_eventos`, `equilibrio_caja_eventos`,
  `caida_absorbible_pct`, `pesimista_/optimista_eventos`, `_precio`, `_invitados`, `pesimista_caja`, `marketplace_pct`,
  `marketplace_comision`, **`cobro_dias` (días de COBRO) y `pago_dias` (días de PAGO a proveedores: cada token a su
  celda; el ES [98] los confunde)**, `horas_evento`, `personas_evento`, `inv_vehiculo` (smoker trailer),
  `inv_adaptacion` (su upfit), `inv_rig`, `inv_almacen`, `inv_furgoneta`, `inv_furgoneta_upfit`, `inv_llc`,
  `inv_permisos`, `inv_inspeccion`, `inv_software`, `inv_herramientas`, `inv_stock`, `inv_lanzamiento`, `inv_holding`, y
  los del motor (ventas, márgenes, inversión, préstamo, DSCR, caja, payback, plantilla). `clientes_dia`, `ticket`,
  `dias`… son alias heredados: no los uses.
- **Realismo (D100), obligatorio en §1, §3 y §8**: {{eventos_a1}} eventos es el caso de un operador **a tiempo completo
  con pit cook y $10K de marketing**, no la media del primer año (orden de magnitud: ≈ $300K de ventas el año 1, Kit
  estimate); la holgura sobre el equilibrio es real pero no amplia; si `{{pesimista_caja}}` es negativo, el docx dice
  que **la caja se agota** («the cash runs out»).
- Fuentes citables (research §4-§6, solo las leídas): q39kc.com, eventective.com (Owen's BBQ), hutchinsbbq.com,
  zola.com (Heim BBQ), fieryfoodscentral.com (Dr. BBQ), sonnybryans.com, yodersmokers.com, webstaurantstore.com (Meadow
  Creek TS500), bls.gov (OEWS mayo 2025), fda.gov (Food Code 2022), dshs.texas.gov (cottage food), law.cornell.edu (25 TAC
  §228.221), corpuschristitx.gov (boletín del fire department), nichemeatprocessing.org, gov.uk (food business
  registration), financialmodelslab.com; heredadas del catering (BP4): thefoodcorridor.com, insureon.com,
  galleysolutions.com, itsacheckmate.com, cdtfa.ca.gov, IRS Rev. Rul. 2012-18. Lo marcado «(resumen)» en research → sin
  cifra o «Kit estimate».
- Fuera: portada «España 2026», «ChefBusiness», proveedores españoles, normativa autonómica, el anexo CCAA, «freelance»,
  porcentajes sin fuente, «60+ páginas», las erratas del ES (merma del brisket 35-40 %, «18 cortes», «carta 12 cortes»).
  Financiación: préstamo bancario o **SBA 7(a)** (el préstamo del ejemplo supera el tope de $50,000 del Microloan),
  «lender-ready, approval not guaranteed». Sin superlativos.
- El cierre (productos de la tienda) lo escribe el ensamblador (123-130): Catering Business Plan Kit · Food Truck Business
  Plan Kit · Food Cost Kit Pro · HACCP Food Safety Kit Pro; el 35 (anexos) nombra los 3 Excel.

## (c) Tanda bbq_a — docx §1-§5 (29 párrafos · ≈ 2.950 palabras de ranura)

Entrada `BP6/tandas/bbq_a.entrada.json` → salida `BP6/docx_en_bbq_a.json` (`{"<i>": "<párrafo EN>"}`). §1 resumen con
tokens y la frase honesta del caso; §2 concepto (smoke en la commissary + live pit on site como premium), propuesta de
valor, modelo económico (depósito 50 % nonrefundable), posicionamiento y **los 10 menu styles** (párrafo 50); §3 mercado
desde el lado del cliente (búsquedas de research §2, bodas, empresas, la mezcla de research §8, realismo); §4 competencia
(Porter y DAFO); §5 marketing (The Knot, WeddingWire, Zola, ezCater, Thumbtack, Google Business Profile, venues,
planners, bridal shows, degustaciones).

```bash
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda bbq_a
```

## (d) Tanda bbq_b — docx §6-§10 (32 párrafos · ≈ 3.770 palabras de ranura)

Entrada `BP6/tandas/bbq_b.entrada.json` → salida `BP6/docx_en_bbq_b.json`. §6 operaciones (commissary, equipo con su
orden de compra, **las 6 fases del evento con cocción nocturna y sonda**, seguridad de las carnes ahumadas con calidad y
mínimo seguro distinguidos, proveedores con approved source); §7 equipo (puestos de `Staffing`, W-2, OEWS, formación,
service charge ≠ gratuity); §8 plan financiero SOLO con tokens (break-even en eventos al año; [98] con `{{cobro_dias}}` y
`{{pago_dias}}` cada uno en su sitio; realismo; pesimista que agota la caja); **§9 legal = el núcleo** con las 7 notas
(102 commissary y nada de casa; 103 permisos, CFPM, food handlers, plan HACCP con 145 / 155 / 165 °F, 135 °F, enfriado y
recalentado, approved source; 104 el trailer en el evento como mobile food unit, «ask your county»; 105 fuego y burn
bans, «check with your fire marshal»; 106 sales tax, service charge y alcohol solo del cliente; 107 empleo y seguros; **el
108 cierra con la nota UK**: registro 28 días antes, FHRS, 14 alérgenos, VAT 20 %, council y plan de fuego); §10
conclusiones y hoja de ruta en el orden del checklist (Business Setup → Pits, Fire & Permits → Equipment → Staff →
Marketing → First 90 Days).

```bash
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --tanda bbq_b
```

## Después de las 4 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-6/bp6.py preparar_tandas      # aplica GRC-plan.revision.json
python3 scripts/productos-digitales/business-plans-en-6/bp6.py check_textos --todas  # GM, GRC-plan, GBQ-plan, GBQ-check + 2 docx
```

Luego el paso 3 en el VPS: ver `F2-NOTAS.md` §6.
