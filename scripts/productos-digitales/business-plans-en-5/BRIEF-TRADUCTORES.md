# Brief para los redactores (subagentes Sonnet) — Mobile Bar Business Plan Kit (EN)

> Sesión Claude Code, 13-oct-2026. F2 del producto 13 de la tienda EN (SPEC delta D86, D91, D92, D93 y **§0, regla
> de jerga**). Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas
> (worktree del Mac): `scripts/productos-digitales/business-plans-en-5/` (= `BP5/`, datos y salidas del bar móvil),
> `scripts/productos-digitales/business-plans-en-4/` (= `BP4/`, el catering EN publicado: el diccionario) y
> `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GMB-plan + revisión de GRC-plan ‖ (b) GMB-check** → **tanda 2 = (c) mbar_a ‖ (d) mbar_b**.
> **GM y GRC-plan no se escriben**: sus 313 + 77 cadenas son el EN publicado del Catering en esa misma celda
> (`BP5/textos_en/GM.json` y `GRC-plan.json`, los escribe `bp5.py preparar_tandas`). GRC-plan se **revisa** en (a).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1**
de este fichero (la 1 es el glosario §9 completo, OBLIGATORIO) + la de su tanda. El subagente no hace commit y no toca
nada más que su salida.

---

## 0. Lo que cambia frente a los briefs anteriores (manda sobre ellos en lo que choque)

**REDACTAR, NO TRADUCIR.** El `es` de cada cadena o párrafo es la **ranura del FOOD TRUCK ES** y la `propuesta_en`, el
**EN publicado del CATERING** en esa misma celda: ninguno de los dos es el contenido. **La pista manda**: dice qué va en
esa celda para un **mobile bar en dry hire**. De la propuesta del catering reutiliza lo que valga (motor, impuestos,
financiación, W-2, service charge, COI) y reescribe todo lo que hable de comida, cocina, comisaria, furgoneta,
catering, buffet, servers o estaciones. Contenido: `BP5/fuente_es_mbar.json` (checklist, plan, carta de 15 cócteles,
10 experiencias y contrato de la coctelería ES de línea B) + research. **Ninguna cifra del ES** (D93).

**Regla de jerga (§0 de la SPEC, John 13-oct): el producto no se traduce, se adapta** a cómo hablan operadores, venues y
planners de EE. UU. El **glosario de la sección 1 es obligatorio**. Reglas fijas: «mobile bar» (el negocio) ≠ «portable
bar» (el mueble); **«dry hire» + la glosa «(you supply the alcohol; we bring the bar, the bartenders and everything
else)» en la PRIMERA mención de cada entregable** (libro: la nota `0. Assumptions!C5`; checklist: la tarea P1 fila 14;
docx: §1 párrafo 40; la calculadora ya la trae); «signature cocktails», nunca «author cocktails»; «W-2 event
bartenders», nunca «freelance»; «cash bar» solo para decir que está prohibida en dry hire; «BYOB» solo como aclaración.

**Medidas US (John, 13-oct): TODAS en el sistema anglosajón**, con la métrica entre paréntesis para UK y Australia
(allí los bartenders miden en ml, con jiggers de 25/50 ml). Principales: **oz / fl oz, lb, quarts / gallons, °F, miles,
sq ft**. Ejemplos: «2 oz (59 ml)», «1.5 lb (0.68 kg) of ice per guest», «41°F (5°C)», «a 200 sq ft (19 m²) storage
unit», «a 6 x 12 ft trailer». Botellas: **750 ml («a fifth»)** y **1.75 L («a handle»)**. Coolers e ice bins en
**quarts, gallons o lb**, nunca en litros. Distancias en **miles**. El ES de coctelería mide en ml, kg, m² y litros
(«almacén de 15-25 m²», «nevera de 200 L», «hielo 50 kg»): conviértelo siempre (≈ 160-270 sq ft, ≈ 210 quarts, ≈ 110 lb).
Nada de m², kg, km, litros ni °C como unidad principal.

**Qué lees** (y nada más): tu entrada `BP5/tandas/<TANDA>.entrada.json`; `BP5/SPEC-delta.md` (D81-D95, §0);
`BP5/F1-research-us-delta.md` §1, §4, §5, §6 y §8 (el §9 está en la sección 1 de este brief); `BP5/fuente_es_mbar.json`
(solo la parte de tu tanda); para el docx, el EN del catering de tus ranuras (`BP4/docx_en_cat_a.json` o `_b.json`)
como **modelo de estructura**, no de contenido; de lo heredado, solo lo que tu entrada cite; `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves,
resultado del check y 3-5 decisiones que deban conocer las demás tandas.

**Concepto (D84): MOBILE BAR & BARTENDING SERVICE EN DRY HIRE.** Un **bar trailer** usado y convertido (el icono que vende
las bodas) + una **portable bar** para el segundo equipo y los salones donde no entra el remolque. El **tow vehicle** es
el del dueño. Se vende **servicio**: bartenders W-2 certificados, barra, **signature cocktails**, **mixers, garnishes,
hielo y vasos incluidos**, **setup & breakdown** y una **shopping list** para que el anfitrión compre el alcohol. Tres
motores: **bodas** (fin de semana; peak wedding season mayo-junio y septiembre-octubre), **eventos de empresa** (entre
semana y holiday parties en diciembre) y **fiestas privadas**. Diferencial: **specialty bars** (las 10 experiencias del ES
→ mimosa bar, espresso martini bar, tiki, speakeasy, gin) con recargo. **Full-service con licencia = opción del docx §9**,
no el caso. No es nuestro comprador: el bar con local (Bar Business Plan Kit), el catering, el food truck.

**Motor de eventos (el del catering), solo con rótulos.** `B4` = **events per year** · `B5` = **average price per guest
(excl. sales tax and alcohol; bar package + add-ons)** · `B6` = **average guests per event**. Ingresos = eventos ×
precio × invitados; los años 2-3 crecen en EVENTOS; el break-even sale en **events per year**. Dos líneas de venta:
**bar packages** (85 %: bartending, barra, mixers, garnish, hielo, vasos) y **add-ons** (travel fees, horas extra,
cristalería, champagne service, specialty bars). Alcohol **0 %**. Personal: `Staffing!B18` = horas por persona y evento,
`B19` = personas por evento (bartenders y barbacks), `B20` = horas × personas × **eventos**.

**Vocabulario PROHIBIDO (gate D93 = `RX_BAR_NO`, `check_textos` lo rechaza):** del FT: «per day», «operating days»,
«customers» (di **clients**, **guests** o **hosts**), «truck» / «food truck» (el vehículo es **tow vehicle** o
**pickup**, nunca «pickup truck»), «window», «festival»; del catering de comida: «food» (salvo «food handler card»,
«FDA Food Code», «mobile food vendors»), «kitchen», «commissary» (salvo hablando del condado / health department),
«chef», «prep cook», «plated», «buffet», «drop-off», «family-style», «themed stations», «chafing», «hotel / sheet
pans», «recipe costing», «boxed lunch», «ezCater», «broadline», «HACCP», «ServSafe Manager», «servers» (di
**bartenders** / **barbacks**; «alcohol server certification» sí), «grease», «pest control», «per plate»; del ES:
«Spain», «IVA», «VAT» (salvo la nota UK), «EUR» / «€», Bodas.net, Zankyou, CateringClick, GGM, Makro; de la jerga:
«author cocktails», «freelance», «cocktail catering», «itinerant bar», «alcohol handler card». Evita también «menu» a
secas (di **drink menu**, **cocktail menu** o **menu sign**), «van» (es un **trailer**), «catering» (salvo «Caterer's
Permit» y la opción licenciada).

**Cifras PROHIBIDAS (D93; las rechaza el check):** del ES de coctelería 40.030 · 25.580 · 18.000 / 35.000 · 70.000 ·
112.500 · 157.500 · 65.000 / 90.000 · 29.400 · 40.600 · 18.220 · 11.180 · 46.410 · 4.635 · 17.220 · 31.058 · 52.500 ·
127.500 · 2.880 · 2.420, «31 events», «50 events a year», «2.6 events a month», «42% margin», «58% variable», «38%
safety margin», «1,400 per event», «$169 per hour», «12-18 per person», «4-7x», «4,500 million», «170,000 weddings»,
«96 suppliers», «71 tasks», «10 real examples», «18-35K»; del caso del catering EN ($648,000, $745,200, $185,453…,
«180 events», «$60 per guest») y del FT EN. Las notas del libro describen el **método** o usan `valor_us`; el caso US
(research §8; calibración D15 en `F2-NOTAS.md` §3) es **160 eventos × 95 invitados × $14** = $212,800.

**Rótulos fijados** (`fijos_en` de tu entrada y POR_CELDA, ya los escribe `mapas.py`; si los citas, con esas palabras):
- `0. Assumptions`: «Events per year (year-1 average)», «Average price per guest (excl. sales tax and alcohol; bar package
  + add-ons)», «Average guests per event», «BAR PACKAGES share of sales (bartending service, bar, mixers, garnishes,
  ice)», «ADD-ONS share of sales (…)», «Share of sales booked through gig marketplaces (GigSalad, The Bash,
  Thumbtack)», «Marketplace fee on those bookings», «Storage unit & trailer parking, per month», «Storage unit deposit
  (months)», «Useful life of the bar trailer and its conversion (years)», «Max events a year your bars and crews can
  handle» (B51, informativo), «Months of storage rent BEFORE opening», «ALCOHOL as a share of add-on sales (0% in dry
  hire: the host buys it)».
- `Startup Costs` filas 7-23 (D87): Bar trailer, used · Trailer conversion · Wrap, signage and bar facade · Portable bar
  for the second crew and indoor venues · Inverter generator and power · Storage unit fit-out · LLC formation, contracts
  and legal · First-year permits and certifications · Health permit / unit inspection (only if your county requires it)
  · Booking software, card reader and tablet · Bar tools and smallwares (4 stations) · Opening inventory · Website,
  photos, launch and first bridal show · Glassware (300 pieces + racks), coolers, ice bins and dispensers · Storage unit
  deposit · Storage rent before opening · Trailer and fit-out contingency.
- `3-Year P&L`: A2 «Base case — mobile bar (dry hire)»; A10/A11 bar package / add-on sales; A16 «Gig marketplace fees»;
  A22 «Storage unit & trailer parking»; A25 seguros; A26 «Permits and certifications renewal»; A27 «Vehicle and trailer
  fuel, maintenance and registration»; A30-A35 software, glass washing, phone and internet, repair and breakage,
  server certifications, tastings; A55 «Storage & parking / Sales».
- `Staffing`: Owner & Lead Bartender (sales and operations) · Second-crew lead bartender (part-time W-2) · Event
  bartenders (hourly W-2) · Barbacks / setup crew (hourly W-2); A24 = nota W-2 / 1099 + propinas (FLSA, AB5).
- Checklist: título «MOBILE BAR STARTUP CHECKLIST — DRY-HIRE MOBILE BARTENDING COMPANY», «PHASE 2: TRAILER, LIQUOR RULES,
  PERMITS & INSURANCE». Pestañas: «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios»,
  «Staffing», «Instructions», «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», **«Phase 2 -
  Trailer & Permits»**, «Phase 3 - Equipment», «Phase 4 - Staff», «Phase 5 - Marketing», «Phase 6 - First 90 Days».

**Formato US** (como siempre): punto decimal, coma de miles, «%» pegado, sin símbolo de moneda en el xlsx, «$» solo en el
docx y en rangos de mercado con fuente; pestañas citadas entre comillas dobles rectas con su nombre EN.

---

## 1. Glosario OBLIGATORIO — research §9 completo (copia literal de `F1-research-us-delta.md`)

> Con la regla de **medidas US** de la sección 0 (oz / fl oz, lb, quarts / gallons, °F, miles, sq ft; la métrica entre
> paréntesis): p. ej. el término 24 se escribe «1.5 lbs per guest (0.68 kg)».

### §9. Jerga profesional US (glosario OBLIGATORIO de los redactores; instrucción de John, 13-oct)

> El producto **no se traduce: se adapta** a cómo hablan operadores, salas y organizadores en EE. UU. Manda en **tres
> capas**: (1) producto (nombre, slug, ficheros, pestañas), (2) contenido de los 4 entregables, (3) SEO de la landing.
> «leída» = la palabra aparece literalmente en la página abierta el 13-oct; «(resumen)» = snippet de búsqueda.

**(a) Nombre del negocio.** **«mobile bar»** (12.100/mes; «mobile bar business» 480) es el nombre que usa todo el sector
(Check Cherry, Montana DOR, Zola «Drink types: Mobile bar»). Los operadores alternan, como sinónimos, **«mobile bartending
service»** (R&R: «a dry hire mobile bartending service») y **«bar service(s)»** (Crystal Beach: «dry hire bar service»;
categoría de Zola «Bar services and beverages»; búsqueda «mobile bartending services» y «bartending services» 1.300/mes
cada una, intención de contratar). «Beverage catering» lo usa algún operador (Crystal Beach) pero tiene 0 búsquedas como
negocio: solo en prosa. **Regla**: «mobile bar» en nombre, H1 y ficheros; «mobile bartending» como variante en subtítulo,
FAQ y keywords; «bar service» en el cuerpo. Nunca «cocktail catering» ni «itinerant bar».

**(b) «Dry hire» SÍ se dice en EE. UU.** Aparece en operadores de TX (R&R, Crystal Beach, Sip Sip Hooray) y CO («Colorado
is a dry hire state», resumen), en Check Cherry («Nearly all mobile bars use dry hire») y tiene búsqueda propia: **«dry
hire mobile bar» 390/mes**; «byob bartending» = **0**. Los operadores lo **explican** siempre en la frase siguiente: «we
provide everything you'll need for your event except the alcohol» (R&R) · «you, the client, supply the alcohol… akin to a
BYOB setup» (Crystal Beach) · «Client must provide all consumables» (Perfect Pour DMV). **Regla**: «dry hire» + glosa
«(you supply the alcohol; we bring the bar, the bartenders and everything else)» en la primera mención de cada
entregable; «BYOB» solo como aclaración; nunca «liquor not included» como nombre del modelo (no hallado como tal).

| # | Concepto (ES de coctelería para eventos) | Término US | Dónde aparece | Nota para el redactor |
|---|---|---|---|---|
| 1 | Empresa de coctelería para eventos | **mobile bar** company / business | checkcherry.com/articles/104-… (leída) | nombre del producto |
| 2 | Servicio de barra (sinónimo) | **mobile bartending service** · **bar service** | zola.com/…/r-r-mobile-bar · zola.com/…/crystal-beach-mobile-bars (leídas) | alternar en el cuerpo |
| 3 | El cliente compra el alcohol | **dry hire** («except the alcohol») | ídem (leídas) | glosar en 1.ª mención (b) |
| 4 | Con alcohol incluido y licencia | **full-service** / licensed bar (wet hire es raro en US) | brewerslaw (FL, leída) · AI Overview SERP | solo en la opción del docx |
| 5 | Lista de la compra para el cliente | **shopping list** («budget friendly shopping list») | thumbtack.com/-Houston-TX/service/3496355 (resumen) | entregable de la calculadora |
| 6 | Barra móvil (mueble) | **portable bar** | fwe.com/files/pdf/specs/s12-01500-cb-hs.pdf (leída) | ≠ «mobile bar» (el negocio) |
| 7 | Remolque-barra | **bar trailer** · **converted trailer** · horse trailer bar | checkcherry 104 («converted trailer build», leída) | «mobile bar trailer» 2.400/mes |
| 8 | Vehículo que lo arrastra | **tow vehicle** | checkcherry 104 (leída) | fila de inversión |
| 9 | Raíl de botellas · cubeta de hielo · lavamanos · depósitos | **speed rail** · **ice bin** (60 lb) · **hand sink** · fresh / **gray water tank** | fwe.com spec (leída) | inventario de equipo |
| 10 | Montaje y desmontaje | **setup & breakdown** | zola.com/…/the-perfect-pour-dmv-llc (leída) | incluido, no «assembly» |
| 11 | Hora extra | **extra hour of service** | r-r-mobile-bar (leída) | tarifa en la calculadora |
| 12 | Paquete por invitado | **per person** / **per guest** pricing · «$1,500 plus $15 per guest» | crystal-beach («$10 per person») · perfect-pour (leídas) | `B5` = per guest |
| 13 | Paquetes cerrados | **bar packages** («Price Per Person… Flat Rate») | herecomestheguide.com/…/how-to-budget-for-your-wedding-bar (leída) | nombres de paquete propios |
| 14 | Solo bartender | **bartender-only** service | checkcherry 106 (leída) | ≈ $75-120/h |
| 15 | Barra libre pagada por el anfitrión | **open bar** / **hosted bar** | herecomestheguide (leída) | en dry hire el alcohol lo pone el host |
| 16 | Barra de pago | **cash bar** («a no-host bar») | ídem | **prohibida en dry hire** (§6.1) |
| 17 | Por consumo | **consumption bar** («priced by consumption») | ídem | solo full-service |
| 18 | Solo cerveza y vino (+1 cóctel) | **limited bar** · beer & wine bar | ídem | paquete de entrada |
| 19 | Cóctel de autor / carta de la casa | **signature cocktails** · **custom cocktail menu** | r-r · perfect-pour (leídas) | NO «author cocktails» |
| 20 | Carta impresa en la barra | **personalized menu** / menu sign | crystal-beach (leída) | |
| 21 | Bebidas sin alcohol | **mocktails** · N/A drinks | r-r · perfect-pour (leídas) | «zero-proof» como variante |
| 22 | Brindis con espumoso | **champagne service** / champagne toast | perfect-pour (leída) | add-on |
| 23 | Mezcladores, garnish, hielo, vasos | **mixers · garnishes · ice & coolers · plastic cups, napkins & straws** | r-r (leída) | líneas del coste por invitado |
| 24 | Hielo por invitado | **1.5 lbs per guest** (ice per guest) | The Easy Pour, Zola (resumen) | regla de la calculadora |
| 25 | Desplazamiento | **travel fee** · «$2/mile» | checkcherry 106 · r-r (leídas) | add-on |
| 26 | Mínimo de contratación | **minimum** («$400 total») · bar minimum | r-r · herecomestheguide (leídas) | |
| 27 | Señal / anticipo | **deposit** («to secure the date») | r-r · checkcherry 173 (leídas) | «retainer» (no reembolsable) no hallado en lo leído |
| 28 | Propina | **gratuity** · tip jar | herecomestheguide («service charge, tax, and gratuity», leída) · MO 24-01 (leída) | tip jar: riesgo de «venta» en MO |
| 29 | Recargo de servicio | **service charge** (≠ gratuity) | herecomestheguide (leída) · BP4 §6.3 | salario, no propina |
| 30 | Jefe de barra | **lead bartender** · «Owner & Lead Bartender» | perfect-pour · r-r (leídas) | puesto 1 del Staffing |
| 31 | Ayudante de barra | **barback** | perfect-pour («1 professional barback», leída) | puesto 4 |
| 32 | Certificado de servicio responsable | **TABC-certified** (TX) · RBS (CA) · TIPS / ServSafe Alcohol | r-r, crystal-beach (leídas) · BP4 | nunca «alcohol handler card» |
| 33 | Seguro de RC por alcohol | **liquor liability insurance** · general liability | r-r, perfect-pour «(COI)» (leídas) | |
| 34 | Certificado del seguro · asegurado adicional | **COI** · **additional insured** | ravenswoodmansion.com/coi (sala, leída) · insurancecanopy (leída) | requisito de sala |
| 35 | Requisitos de la sala | **venue requirements** | insurancecanopy («Meet Venue Requirements», leída) | |
| 36 | Seguro del anfitrión | **host liquor liability** | ravenswoodmansion.com/coi (leída) | lo contrata el cliente, no nosotros |
| 37 | Coste por copa / escandallo | **cost per guest** (dry hire) · **pour cost** (solo full-service) | (no hallado en webs de operador leídas) | NO «escandallo» ni «recipe costing» |
| 38 | Última ronda | **last call** | (no hallado en lo leído) | término común; usar sin explicarlo |

**(e) Términos ES que NO se traducen literalmente:** «experiencias temáticas» → **specialty bars / themed bars** (mimosa
bar, espresso martini bar, dirty soda bar, lemonade bar: Whiskey & Copper, GigSalad, resumen) · «coctelería de autor» →
**signature / craft cocktails** · «barra móvil» → **portable bar** (mueble) o **mobile bar** (negocio) · «escandallo» →
**cost per guest / drink costing** · «autónomo» → **sole proprietor** o **single-member LLC** (el caso: LLC) · «bartender
freelance» → **W-2 event bartender** (1099 = riesgo, BP4 §6.5) · «licencia de actividad» → **business license** (ciudad o
condado) + **sales tax permit** · «autorización puntual» → **temporary / special event permit** (solo full-service) ·
«IVA» → **sales tax** · «fianza/señal» → **deposit** · «wedding planner» → **wedding planner / coordinator** · «contrato» →
**service agreement / event contract** · «hostelero / sala» → **venue** · «evento de empresa» → **corporate event /
holiday party** · «temporada alta» → **peak wedding season** (May-June, Sept-Oct).

**Capas (1) y (2), propuesta:** nombre **Mobile Bar Business Plan Kit** · slug `mobile-bar-business-plan` · ficheros
`mobile-bar-business-plan.docx` «Mobile Bar Business Plan (10 Sections)» · `mobile-bar-financial-projections.xlsx` ·
`mobile-bar-pricing-calculator.xlsx` «Mobile Bar Pricing Calculator (Cost per Guest to Quote)» ·
`mobile-bar-startup-checklist.xlsx` · pestaña F2 **«Phase 2 - Trailer & Permits»** (27 car., ≤ 31) · rótulos del libro
con los términos 1-38 (p. ej. `B11` «Bar packages (service, mixers, garnishes, ice)», `B24` «Storage unit & trailer
parking», staffing «Owner & Lead Bartender», «Barback / setup crew»).

#### Términos para la landing (DataForSEO US, 13-oct; las 6 primeras, del orquestador)

| Keyword | Vol. | Comp. | Uso |
|---|---|---|---|
| **mobile bar business plan** | **210** (90 → 210) | LOW | cabeza: slug, title, H1 |
| mobile bar business · mobile bartending business | 480 · 260 | LOW | subtítulo, intro, schema |
| how to start a mobile bar business · … mobile bartending business | 210 · 210 | LOW | H2 + FAQ |
| mobile bartending business plan · … template · … pdf | 70 · 30 · 20 | LOW | title / keywords |
| **dry hire mobile bar** | **390** | LOW | H2 legal + FAQ |
| **mobile bar license** · mobile bartending license | **320** · 320 | LOW | FAQ (licencia) |
| mobile bar insurance · mobile bartender insurance | 260 · 260 | HIGH | H2/FAQ de seguros |
| mobile bar pricing · mobile bartending prices | 140 · 140 | LOW | H2 calculadora |
| mobile bar packages | 50 | LOW | calculadora |
| mobile bar trailer | 2.400 | HIGH | intención de compra del remolque: alt/H2, no cabeza |
| mobile bartending services · bartending services · mobile bar for events | 1.300 · 1.300 · 720 | MED/LOW/HIGH | intención de contratar: no se atacan |
| mobile bar startup costs · is a mobile bar business profitable · how much do mobile bars make | 10 · 10 · 10 | LOW | FAQ |
| cost to start a mobile bar · byob bartending · mobile bar financial projections | 0 | — | no usar como objetivo |

- **Title** (≈ 95 car., mismo patrón que el catering): «Mobile Bar Business Plan Template: Word + Excel Financial
  Projections + Pricing Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Mobile Bar ` + oro `Business Plan` + «Template for a Dry-Hire Mobile Bartending Company: Word Plan +
  Excel Financial Projections + Pricing Calculator + Startup Checklist».
- **Meta description** (≈ 155 car.): «Mobile bar business plan template for a dry-hire bartending company: Word plan, 3-year
  Excel projections, per-guest pricing calculator and startup checklist.»
- **H2 (6)**: What's Inside Your Mobile Bar Business Plan Kit · How Much Does It Cost to Start a Mobile Bar Business? ·
  Dry Hire vs. Full-Service: Do You Need a Liquor License for a Mobile Bar? · Mobile Bar Pricing: What to Charge per Guest
  and per Bartender Hour · Is a Mobile Bar Business Profitable? Your 3-Year Projections · Mobile Bar Insurance, Permits
  and Venue Requirements.
- **FAQ en la redacción del comprador** (PAA + relacionadas): «How hard is it to get a liquor license for a mobile bar?» ·
  «Do I need a liquor license for a dry hire mobile bar?» · «How much does it cost to start a mobile bartending business?»
  · «How much does a mobile bar make?» (PAA: «How much does a bar owner make per month?») · «What insurance do I need for a
  mobile bar?» · «How much should I charge per guest for a mobile bar?» · «Can an LLC own a mobile bar?» (PAA «Can an LLC
  own a bar?») · «Can I accept tips at a dry hire event?».
- **Alt de imágenes**: «Mobile bar trailer set up at an outdoor wedding» · «Dry hire mobile bar with signature cocktails
  menu sign» · «Lead bartender and barback at a portable bar during a corporate event».
- **Keywords del schema / docProps**: mobile bar business plan, mobile bartending business plan, mobile bar business plan
  template, how to start a mobile bar business, dry hire mobile bar, mobile bar pricing, mobile bar license, AI Chef Pro.

---

## (a) Tanda GMB-plan — xlsx del plan financiero (130 cadenas · ≈ 3.250 palabras ES) + revisión de las 77 GRC-plan

Entrada `BP5/tandas/GMB-plan.entrada.json` → **dos** salidas:

1. `BP5/textos_en/GMB-plan.json` (`{"<id>": "<EN>"}` con TODOS los ids y nada más):
   - **Texto libre** (≈ 74): notas de la col. C de `0. Assumptions` (pistas por celda C4-C63: caso, mezcla bar packages /
     add-ons, marketplaces, storage, seguros, capacidad B51 informativa, rampa lenta, cobro 1 día sin anticipos, alcohol
     0 %), notas de `Startup Costs` (col. D, filas 7-20 con los importes de research §8 y el tow vehicle propio), del P&L
     (F10/F11, F16, F22-F35 y los umbrales F51-F56 de D88), de `Staffing` (J5-J8, J18-J19), de `Scenarios` (E23) y de
     `Instructions` (A5, A12). La nota `0. Assumptions!C5` lleva la **primera mención de «dry hire» con su glosa**.
   - **Tabla D19, filas 55-68 «US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES»**, una celda cada vez (`por_celda`),
     sin propuesta: cada fila trae su pista (precio por evento, por invitados, por duración, bartender-only, depósito y
     travel fee, estacionalidad, el primer año real, copas por invitado, ratio de bartenders (Kit estimate), sueldo BLS,
     comisión de GigSalad, coste de arranque, seguros, hielo y mixers (Kit estimate)). `Source` = el dominio de la fuente
     LEÍDA (checkcherry.com, eventplanning.com, bls.gov, gigsalad.com, insurancecanopy.com) o «Kit estimate».
   - Las celdas de la tabla D18 que hablaban de comida (≈ 11): describe el MÉTODO del libro para un bar móvil.
2. `BP5/textos_en/GRC-plan.revision.json`: revisa `revisar_reutilizadas.GRC-plan` (77: la tabla D18 «WHY THIS MODEL IS
   BUILT THIS WAY» y 20 notas del motor). Son el EN del catering, que ya habla de eventos; si `en_actual` vale para un
   bar móvil, **no la incluyas**; si no, `{"<id>": "<EN corregido>"}` (p. ej. pagos con ACH de empresas → los
   particulares pagan con tarjeta; «events you cater» → «events you work»). Si ninguna cambia: `{}`.

Umbrales del P&L (D88, ya en el libro): margen bruto ≥ **65 %** · coste de mercancía ≤ **26 %** · personal ≤ **40 %** ·
storage y parking ≤ **6 %** · neto ≥ **5 %**, «kit benchmark (editable estimate)».

```bash
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda GMB-plan
python3 scripts/productos-digitales/business-plans-en-5/bp5.py preparar_tandas && \
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda GRC-plan
```

## (b) Tanda GMB-check — checklist (275 cadenas: 68 tareas × 4 columnas + 3 textos)

Entrada `BP5/tandas/GMB-check.entrada.json` → salida `BP5/textos_en/GMB-check.json` (`{"<id>": "<EN>"}` con TODOS los
ids): **68 tareas en 6 fases (11/13/12/10/12/10), no se añaden ni quitan**; cada celda es un id (`por_celda`): col. B =
la tarea (corta, imperativa), C = responsable, D = plazo US, E = nota práctica. **La pista de cada fila dice qué tarea va
en esa ranura** (D91): las marcadas «[sobrevive]» son la tarea del catering con ajustes (su `propuesta_en` vale de
base); el resto son tareas NUEVAS y la `propuesta_en` (catering) solo sirve para el tono y la longitud. Contenido:
`fuente_es_mbar.json` → `checklist_es` (fuera las marcadas SOLO_ES) + research §6. P1 fila 14 = la primera mención de
«dry hire» del checklist, con su glosa. P2 = reglas de alcohol de tu estado (tabla MO / MT / TX / CA / FL / NY +
«varies by state»), storage unit, health permit solo si el condado lo exige, venues (COI, additional insured), remolque
(compra, DMV, conversión), seguros (GL, liquor liability, workers' comp, inland marine), permiso de caterer solo si vas
a full-service. P5 = The Knot, WeddingWire, Zola, GigSalad, The Bash, Thumbtack, Google Business Profile, bridal shows.
P6 fila 7 = shopping list al anfitrión en D-14 + mixers, garnish y hielo en D-1. Los 3 textos que no son tareas (títulos
de las fases 1 y 3 y la nota del contador) vienen con la propuesta del catering: cámbialos solo si no valen.

```bash
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda GMB-check
```

---

## Docx — reglas comunes de las tandas (c)-(d)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»: un párrafo EN por párrafo ES, sin saltos de línea en el
cuerpo, subtítulos de una línea sin punto final, toda cifra del caso con su token `{{…}}`, importes y porcentajes de
mercado solo si están en research/SPEC con fuente), más:

- **Escribes cada párrafo** (D92): `notas_del_plan` y la `nota` de CADA párrafo (todos la tienen) dicen qué va en esa
  ranura; el `es` (food truck) solo da el papel y la longitud (±30 %); el EN del catering de la misma ranura
  (`BP4/docx_en_cat_a.json` / `_b.json`, clave = mismo `i`) es el modelo de estructura. Contenido de
  `fuente_es_mbar.json` (plan ES, carta, experiencias, contrato) + research §1, §5, §6, §8 y el glosario.
- **Tokens del bar móvil** (usa estos, no los alias heredados): `eventos_a1/_a2/_a3`, `precio_invitado`,
  `precio_invitado_con_tax`, `invitados_evento`, `invitados_a1`, `ventas_evento`, `capacidad_eventos`,
  `cuota_paquetes_pct`, `coste_paquetes_pct`, `coste_extras_pct`, `equilibrio_eventos`, `equilibrio_caja_eventos`,
  `caida_absorbible_pct`, `pesimista_/optimista_eventos`, `_precio`, `_invitados`, `pesimista_caja`, `marketplace_pct`,
  `marketplace_comision`, `cobro_dias`, `horas_evento`, `personas_evento`, `inv_vehiculo` (bar trailer),
  `inv_adaptacion` (conversion), `inv_fachada`, `inv_barra_portatil`, `inv_energia`, `inv_almacen`, `inv_llc`,
  `inv_permisos`, `inv_health_permit`, `inv_software`, `inv_herramientas`, `inv_stock`, `inv_lanzamiento`,
  `inv_cristaleria`, y los del motor (ventas, márgenes, inversión, préstamo, DSCR, caja, payback, plantilla).
  `clientes_dia`, `ticket`, `dias`… son alias heredados: no los uses.
- **Realismo (D85), obligatorio en §1, §3 y §8**: el caso es el **cuartil alto** de Check Cherry ({{ventas_evento}} por
  evento frente a la mediana de $750), un operador a tiempo completo con 2 equipos; la mediana de un bar móvil nuevo hace
  **3 eventos** el primer año; si `{{pesimista_caja}}` es negativo, el docx dice que la caja se agota.
- Fuentes citables (research §4-§6, solo las leídas): checkcherry.com (articles 104 y 106), eventplanning.com,
  bls.gov (OES 35-3011, mayo 2025), help.gigsalad.com, insurancecanopy.com, atc.dps.mo.gov (Circular 24-01),
  revenue.mt.gov (Mobile Bars), nyc-business.nyc.gov (Caterer's Alcohol Permit), cdtfa.ca.gov, legalclarity.org (TX,
  secundaria), IRS Rev. Rul. 2012-18, gov.uk (personal licence, TEN), planbuildr.com (plan de ejemplo con alcohol).
  Lo marcado «(resumen)» en research → sin cifra o «Kit estimate».
- Fuera: portada «España 2026», «ChefBusiness», proveedores españoles, normativa autonómica, «freelance», porcentajes sin
  fuente, «60+ páginas». Financiación: préstamo bancario, SBA 7(a) o SBA Microloan (tope $50,000), «lender-ready,
  approval not guaranteed». Sin superlativos.
- El cierre (productos de la tienda) lo escribe el ensamblador (123-130); el 35 (anexos) nombra los 3 Excel.

## (c) Tanda mbar_a — docx §1-§5 (29 párrafos · ≈ 2.950 palabras de ranura)

Entrada `BP5/tandas/mbar_a.entrada.json` → salida `BP5/docx_en_mbar_a.json` (`{"<i>": "<párrafo EN>"}`). §1 resumen con
tokens (el 40 lleva la primera mención de «dry hire» con su glosa) y la frase honesta del caso; §2 concepto, propuesta de
valor, paquetes y specialty bars; §3 mercado desde el lado del cliente (bodas, empresas, fiestas; estacionalidad; el
primer año real); §4 competencia (Porter y DAFO); §5 marketing (The Knot, WeddingWire, Zola, GigSalad, Google Business
Profile, venues, planners, bridal shows, degustaciones).

```bash
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda mbar_a
```

## (d) Tanda mbar_b — docx §6-§10 (32 párrafos · ≈ 3.770 palabras de ranura)

Entrada `BP5/tandas/mbar_b.entrada.json` → salida `BP5/docx_en_mbar_b.json`. §6 operaciones (storage unit, remolque y
equipo, operativa de un evento del ES, hielo, garnish y copas por invitado); §7 equipo (puestos de `Staffing`, W-2,
certificaciones, service charge ≠ propina); §8 plan financiero SOLO con tokens (break-even en eventos al año; realismo;
pesimista); §9 legal con las 7 notas (102-108: dry hire y sus condiciones MO / MT, full-service por estado, health
permit, sales tax, empleo y seguros; **el 108 cierra con la nota UK**: personal licence, TEN); §10 conclusiones y hoja
de ruta en el orden del checklist.

```bash
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --tanda mbar_b
```

## Después de las 4 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-5/bp5.py preparar_tandas      # aplica GRC-plan.revision.json
python3 scripts/productos-digitales/business-plans-en-5/bp5.py check_textos --todas  # GM, GRC-plan, GMB-plan, GMB-check + 2 docx
```

Luego el paso 3 en el VPS: ver `F2-NOTAS.md` §6.
