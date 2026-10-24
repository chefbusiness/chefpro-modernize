# Brief para los redactores (subagentes Sonnet) — Paella Catering Business Plan Kit (EN)

> Sesión Claude Code, 24-oct-2026. F2 del producto EN hermano del BBQ (SPEC delta D114-D132 y **§0, regla de jerga**).
> Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-7/` (= `BP7/`, datos y salidas de la paella), `scripts/productos-digitales/
> business-plans-en-6/` (= `BP6/`, el BBQ cerrado: las PROPUESTAS), `scripts/productos-digitales/business-plans-en-4/`
> (= `BP4/`, el catering EN publicado) y `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el
> brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GPA-plan + revisión de GRB-plan ‖ (b) GPA-check** → **tanda 2 = (c) pael_a ‖ (d) pael_b**.
> **No se escriben** GM (312), GRB-plan (98: se **revisa** en (a)) ni GLB-check (202 celdas del checklist cuya propuesta del
> BBQ vale tal cual, con «Pitmaster» → «Paella chef» en la columna C): los escribe `bp7.py preparar_tandas`. **Las entradas
> llevan SOLO lo que cambia.**

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1**
de este fichero (la 1 es el glosario §9 completo, OBLIGATORIO) + la de su tanda. El subagente no hace commit y no toca
nada más que su salida.

---

## 0. Lo que cambia frente al brief del BBQ (manda sobre él en lo que choque)

**REDACTAR, NO TRADUCIR. La propuesta del BBQ da la forma; la pista manda; cero vocabulario BBQ.** Cada cadena de las
tandas xlsx trae `propuesta_en` = el EN del BBQ cerrado en ESA misma celda (o, si el BBQ no tenía, el del catering), y cada
párrafo del docx trae en su `nota` la PROPUESTA EN DEL BBQ de la misma ranura. Reutiliza su estructura, su tono, su
longitud, sus tokens y las fuentes comunes (commissary, W-2, OEWS, Insureon, thefoodcorridor, galleysolutions,
itsacheckmate, sales tax, service charge, SBA 7(a), COI). **Reescribe** todo lo que hable del smoker trailer, el pit, la
carne, la leña, el carving o el caso del BBQ. El `es` es la ranura del FOOD TRUCK ES (solo papel y longitud); el contenido
de paella sale de la pista, de `BP7/fuente_es_pael.json` (checklist ES de 83 tareas con las SOLO_ES marcadas, docx ES 2.2
por ranura, manual técnico, carta de 12 paellas, 10 experiencias, contrato, catálogo de equipo) y de research. **Ninguna
cifra del ES** (D128).

**Concepto (D117): LIVE PAELLA CATERER.** La paella **cocinada en vivo en el evento ES el producto**: paelleras de 26-36 in
sobre quemadores de propano de 3 aros, con ensalada y pan; el paella chef en la estación. **Sofrito, caldo, verdura y marisco
limpio salen de la commissary** la víspera. **Drop-off** (paella cocinada en la commissary y entregada en caliente) = línea
menor; **premium de marisco y tapas** ≈ 7 eventos. Gas = base; **leña solo con permiso** («wood-fire setup»); **inducción
en interiores** (Kit). **8 menu styles**: seafood (paella marinera) · chicken & seafood · chicken & chorizo · Valencian
(rabbit on request) · farm vegetable (vegan) · paella negra · lobster & seafood (premium) · easy-eat peeled seafood;
«fideua (noodle paella)» como nota. Tipos de evento: backyard paella party, boda con tapas hour, live cooking corporativo,
rehearsal dinner, first communion / baptism / quinceañera, cumpleaños, drop-off corporativo, premium, vegano. No es
nuestro comprador: el paella food truck (Food Truck Kit), el restaurante, quien cocina en casa (ilegal), las fiestas
populares (temporary food establishment).

**Motor de eventos (el del catering y el BBQ), solo con rótulos.** `B4` = **events per year** · `B5` = **average price per
guest (excl. sales tax, service included)** — la media de la MEZCLA, con el paella chef y el personal dentro — · `B6` =
**average guests per event**. Dos líneas de venta (D121): **paella packages** (88 %: live-cooked paella, salad & bread,
paella chef & staff) y **add-ons** (tapas, desserts, non-alcoholic sangria & drinks, rentals, extra hours, travel fees).
`B15` = **disposables & cooking fuel** (variable, 3.5 %: el propano; la leña donde haya permiso). El combustible de la VAN
es un **fijo** (`3-Year P&L!A27` «Van fuel, maintenance and registration»); los **varios** (`B28`, 3 %) son imprevistos de
cada evento (marisco extra, hielo, limones, parking) **sin combustible**. Alcohol **0 %**. Personal: `Staffing!B18` = 9 h por
persona y evento, `B19` = 2.5 personas por evento.

**Caso US (research §8, dry-run del paso 1 en `F2-NOTAS.md` §3; D15 en verde sin calibrar):** 135 eventos × 58 invitados ×
$40 = **$313,200** ($2,320 por evento); CAPEX $49,480 + fondo de maniobra $39,486 = $88,966; propios $25,000 (28 %) +
préstamo $64,000 (SBA 7(a): supera el tope de $50,000 del Microloan); EBITDA 12.5 %; neto $20,319 (6.5 %); equilibrio 116
eventos (117 de caja), holgura 16 % (caída absorbible 14 %); DSCR mín 2.47×; pesimista (101 · $36 · 52) $189,072 y
**caja −$10,040: se agota**. Las notas del libro describen el **método** o usan `valor_us`; el docx cita el caso SOLO con
tokens. **Realismo (D118)**: 135 eventos = dueño-paella chef a tiempo completo con un segundo cocinero los fines de semana,
no la media del primer año (≈ $225K el año 1, Kit estimate); los precios incluyen al paella chef que otros cobran aparte
(cafesevilla.com: $300 por 2 h).

**Vocabulario PROHIBIDO (gate D128 = `RX_PAEL_NO` + `check_textos`; los dos lo rechazan):**
- **BBQ**: «smoke / smoker / smoked / smoking» (solo **«smoked paprika»**), «pitmaster», «pit», «pit cook / crew»,
  «brisket», «pulled pork», «pork butt», «ribs», «bark», «smoke ring», «burnt ends», «live-fire», «live pit», «carving /
  carver» (solo **«Serrano ham carving station»**), «trailer», «tow vehicle», **«pickup»** (también «pickup times»: di
  «drop-off and collection times»), «whole hog», «pig roast», «tri-tip», «picanha», «asado», «churrasco», «Caja China»,
  «Santa Maria», «parrilla», «butcher paper», «rub», «pounds of meat», «meat yield / lines / prices / per guest», «raw /
  cooked / smoked meat», «BBQ», «barbecue», «grill / grilled / grilling» (salvo el nombre propio «Miami Grill Catering»;
  el dominio miamigrillcatering.com vale).
- **Catering y bar móvil heredados**: «plated», «themed / action / food / chef-attended stations» y **«stations» en
  general** salvo «live paella station», «Serrano ham carving station», «cooking station», «handwashing station», «propane
  station»; **«chef» suelto**, «executive / sous chef» (solo **«paella chef»** y «second paella chef»; «chefs and head
  cooks» solo en la fila OEWS de la D19), «taco bar», «pasta», «12 cuisines», «refrigerated van», «cocktails» (sí
  «cocktail hour»), «bartender», «dry hire», «mobile bar», «barback», «mixers», «specialty / cash bar». **«induction» y
  «wood-fire» SÍ valen** (D117).
- **Food truck**: «per day», «operating days», «customers» (di clients / guests; «corporate customers» sí), «truck» (solo
  «paella food truck(s)» y el nombre «Food Truck Business Plan Kit»), «window» (también «a 4-hour window»: di «within 4
  hours»), «festival» (di «public or community event»).
- **ES del paellero**: «paellero», «paellera» (di **paella chef / paella caterer / paella pan**), «garrofó», «ferraura»,
  «bogavante», «senyoret», «finca», «fiesta del pueblo», «Falles», «DO» junto al plato (la DO ampara el arroz: deuda ES),
  Garcima, Vaello, GGM, Arcos, IDAE, ITC-ICG, ADR, «show cooking» (di «live paella», «cooked live in front of your
  guests»), «España», «IVA», «VAT» (salvo la nota UK), «EUR» / «€», «autónomo», «fijo discontinuo», SL, IAE, AESAN, APPCC,
  CCAA, RGSEAA, FACe, Veri*factu, «RD …», «Reglamento (CE)», Bodas.net, Zankyou, Hosply; jerga: «freelance», «support
  kitchen», «Cambro»; calcos «D-21 / D-14 / D-1»; kg / km / °C / litros fuera de paréntesis.
- **`check_textos` (código común) rechaza además «Spain», «Valencia» y «Spanish market»** aunque `RX_PAEL_NO` deje «Spain»
  junto al origen: **no los escribas**; di «Spanish», «imported Spanish saffron», «Spanish bomba rice», «Valencian paella».
- **Tildes**: el detector común de español rechaza jamón, fideuà, pimentón, española, paella «à la»…: escribe **«Serrano
  ham»**, **«fideua (noodle paella)»**, **«smoked paprika»**, **«Spanish tortilla»**; la lista blanca del detector solo
  deja «señor» (Señor Pepe's), jalapeño, café, entrée y pocas más.

**Cifras PROHIBIDAS (D128; las rechaza el check):** del ES del paellero 10.800 · 12.392 · 12.417 · 14.579 · 14.829 · 15.794 ·
16.803 · 18.582 · 19.772 · 20.425 · 41.777 · 42.686 · 51.600 · 55.097 · 57.893 · 63.111 · 71.487 · 85.448 · 100.027 ·
108.375 · 128.987 · 134.903 · 152.768 · 157.920 · 173.712 · 184.135 · 212.500; los pequeños (1.504, 1.750, 2.100, 2.400,
3.354, 3.747, 4.000, 6.130, 8.376) con € o EUR; «105 events», «94 guests», «16 €», «90 / 86 events», «81 / 77 guests»,
«85 events», «22.4 %», «DSCR 1.72», «83 tasks», «88 suppliers», «11 deliverables», «fiestas populares», «contrato
menor», «v1.1»; **del caso del BBQ**: sus importes ≥ 10,000 ($427,500, $101,000, $83,300, $135,671, $29,816…), «150
events», «$38 per guest» y «$38.00», «75 guests per event» / «average of 75 guests», «220 events», «128 events», «$2,850»;
del catering EN («180 events», «$60 per guest», sus importes), del mobile bar EN («160 events», «$14 per guest», sus
importes) y del FT EN. **Ojo, la mezcla de la paella tiene 25 eventos de empresa de 75 invitados a $38**: escríbelo «75
guests at $38» (nunca «75 guests per event» ni «$38 per guest»).

**Rótulos fijados** (`fijos_en` de tu entrada y POR_CELDA, ya los escribe `mapas.py`; si los citas, con esas palabras):
- `0. Assumptions`: «Events per year (year-1 average)», «Average price per guest (excl. sales tax, service included)»,
  «Average guests per event», «PAELLA PACKAGES share of sales (live-cooked paella, salad & bread, paella chef & staff)»,
  «ADD-ONS share of sales (…)», «Cost of goods on PAELLA PACKAGE sales (rice, seafood, meats, saffron, stock, salad,
  bread)», «Disposables & cooking fuel as % of sales», «Corporate catering marketplace share of sales (e.g. ezCater)»,
  «Commissary kitchen rent & equipment storage, per month», «Useful life of the burners, pans, van and fit-outs (years)»,
  «Max events a year your paella crew can handle» (B51, informativo), «Contingency on the burner, pan, van and fit-out
  lines (%)».
- `Startup Costs` filas 7-23 (D120): Paella burners & stands · Paella pans: 2 × 36 in (90 cm), 3 × 32 in (80 cm), 3 × 26 in
  (65 cm) · Propane & fire-safety kit · Commissary prep & storage fit-out · Used cargo van · Van upfit (shelving, upright
  cylinder racks, tie-downs, wrap) · LLC formation, contracts and legal · First-year permits and certifications · Fire /
  event permit & propane setup inspection (only if required) · Catering software, card reader and tablet · Smallwares &
  paella tools · Opening inventory · Website, photos, launch and first bridal show · Event setup & holding · Commissary
  deposit · Commissary rent before opening · Burner, pan, van and fit-out contingency. Base de vida del vehículo = filas 7,
  8, 11, 12, 15 (+ contingencia); de equipo = 9, 10, 16, 17, 20.
- `3-Year P&L`: A2 «Base case — live paella caterer (cooked on site at events)»; A10/A11 paella package / add-on sales;
  A15 «Disposables & cooking fuel»; A16 «Corporate catering marketplace fees»; A22 «Commissary kitchen rent & equipment
  storage»; A24 utilities (sin propano); A25 seguros («general liability with open flame covered…»); A26 permisos; A27
  «Van fuel, maintenance and registration»; A30 software; A31 «Linens, uniforms and cleaning»; A32 «Waste, used oil and
  shell disposal»; A33 «Pan, burner & hose replacement»; A34 «Food safety training (ServSafe Manager, food handler
  cards)»; A35 «Tastings for prospects»; A55 «Commissary & storage / Sales».
- `Staffing`: Owner / Paella Chef & Sales · Lead cook / second paella chef (part-time W-2) · Event staff (servers, buffet
  attendants; hourly W-2) · Prep cook / driver (part-time W-2); A24 = nota W-2 / 1099 + «One paella chef can run about
  three pans at once».
- Checklist: título «PAELLA CATERING STARTUP CHECKLIST — LIVE PAELLA CATERER», «PHASE 2: COMMISSARY, PROPANE STATION, FIRE
  RULES & PERMITS». Pestañas: «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios», «Staffing»,
  «Instructions», «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», **«Phase 2 - Propane &
  Permits»**, «Phase 3 - Equipment», «Phase 4 - Staff», «Phase 5 - Marketing», «Phase 6 - First 90 Days».

**Legal (research §6; lo no verificado va como «check your county / state rules» o «check with your fire marshal», nunca
como cifra nacional):** commissary obligatoria y nada de cocina de casa (Food Code 3-201.11(B)) · cocinar en el evento:
«food establishment» incluye el catering (1-201.10); **limited food preparation** de San Diego County (CalRFC §113818)
**solo como ejemplo** → «ask your county» · **propano y carpas**: estación al aire libre o bajo su toldo, lejos de la carpa
de invitados; Virginia 13VAC5-52-360 (cooking tents a ≥ 20 ft, LP-gas fuera) **solo como ejemplo** → «check with your fire
marshal»; leña solo con permiso y sin burn ban · **arroz cocido = TCS y *B. cereus***: servir a ≥ 135 °F (3-501.16) o time as
a public health control de 4 h con SOP escrito (3-501.19); **sobras a la basura** · MÍNIMOS del Food Code (3-401.11): pollo
165 °F, pescado y marisco 145 °F 15 s, chorizo crudo mexicano 155 °F 17 s (el curado español es listo para comer) ·
marisco de approved source y **shellstock tags 90 días** (3-203.12) · alérgenos: entre los 9 US, *fish* y *crustacean
shellfish*; los moluscos no son alérgeno mayor en EE. UU. (se declaran igual); UK: 14 con moluscos, apio y sulfitos ·
seguros: GL / BOP que **no excluya la llama abierta**, commercial auto, workers' comp, inland marine, COI / additional
insured · W-2, nunca 1099 · sales tax sobre toda la factura de catering · **sangría**: sin licencia no se vende alcohol; sin
alcohol o con el vino que compra el cliente, sin margen; corkage no se modela.

**Medidas US (John, 13-oct)**: lb y oz, °F, miles, gallons / quarts, sq ft; métrica entre paréntesis («3.25 oz (92 g)»,
«135 °F (57 °C)», «2 gallons (7.6 liters)»); **paelleras en pulgadas con los cm entre paréntesis** («36 in (90 cm)»);
**azafrán en gramos**. El **mínimo del Food Code se nombra siempre como tal** (no hay «temperatura de calidad» que lo
sustituya).

**Formato US** (como siempre): punto decimal, coma de miles, «%» pegado, sin símbolo de moneda en el xlsx, «$» solo en el
docx y en rangos de mercado con fuente; pestañas citadas entre comillas dobles rectas con su nombre EN.

**Qué lees** (y nada más): tu entrada `BP7/tandas/<TANDA>.entrada.json`; `BP7/SPEC-delta.md` (D114-D132, §0);
`BP7/F1-research-us-delta.md` §1, §5, §6 y §8 (el §9 está en la sección 1 de este brief); `BP7/fuente_es_pael.json` (solo la
parte de tu tanda); de lo heredado, solo lo que tu entrada cite; `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves,
resultado del check y 3-5 decisiones que deban conocer las demás tandas.

---

## 1. Glosario OBLIGATORIO — research §9 completo (copia literal de `F1-research-us-delta.md`)

> Con la regla de **medidas** de la sección 0. **Cambios de la SPEC sobre el §9 literal**: «paella chef» y «paella
> caterer», nunca «paellero» ni «chef» suelto (el §9 deja «paellero» en prosa: la SPEC §0 lo veta); «Serrano ham carving
> station» y «Spanish tortilla» sin tildes (el detector común las rechaza); «live paella station» solo en prosa; pestaña F2
> **«Phase 2 - Propane & Permits»**; A15 = **«Disposables & cooking fuel»** (D121), no «Disposables & propane».

### 9. Jerga profesional US (glosario OBLIGATORIO de los redactores)

**(a) Nombre.** **«Paella catering»** en nombre, H1 y ficheros (así se anuncian Taste of Paella, Señor Pepe's, Real Paella);
**«Spanish catering»** (2.900) como variante con tapas; **«paella chef»** para la persona; «paellero» solo en prosa (El
Paellero, Seattle, Yelp; resumen); **«paella pan»**, nunca «paellera» en rótulos. «live-action station»: no hallado → **«live
paella station»** solo en prosa.

| # | ES paellero | Término US | Dónde (leída salvo indicación) |
|---|---|---|---|
| 1 | Empresa · show cooking | **paella catering** · **live paella** · «cooked live in front of your guests» · «prepared on site» | tasteofpaella · zola Viton · zola Señor Pepe's |
| 2 | Fiesta de paellas en casa | **backyard paella party** | cafesevilla.com |
| 3 | Paellero · paellera | **paella chef** («Paella chef (required)») · **paella pan** («giant traditional pan») | cafesevilla · zola Viton |
| 4 | Paellero de gas | **paella burner** (3-ring) + legs / tripod + regulator | tienda.com (resumen) |
| 5 | Socarrat · arroz · azafrán | **socarrat** («golden socarrat reveal») · **bomba rice** / «Spanish rice» · **saffron rice** | zola Viton · weddingwire Paella Party CT (resumen) · tasteofpaella · miamigrillcatering |
| 6 | Sofrito · caldo · fumet | **sofrito** · **stock** · fish stock | no hallado en operadores: recetas y prosa |
| 7 | Marinera · mixta · campera | **seafood paella** / paella marinera · **chicken & seafood** / mixta · **chicken & chorizo** | tasteofpaella · zola Viton · miamigrillcatering |
| 8 | Valenciana · huerta · negra · bogavante | **Valencian paella** · **farm vegetable** · **paella negra** · **lobster & seafood** | realpaella.com · tasteofpaella · zola Viton |
| 9 | Entrantes · alioli · jamón | **tapas** (patatas bravas, tortilla española, cheese & cold cuts) · **garlic aioli** · **jamón serrano carving station** | cafesevilla · miamigrillcatering · weddingwire Paella Valenciana (reseña) |
| 10 | Sangría · descorche | **sangria bar** · **non-alcoholic options** · **corkage fee** | weddingwire Paella Time · zola Qué Paella |
| 11 | Animación | **flamenco** · Spanish guitarist | weddingwire Paella Time · Paella Valenciana |
| 12 | Precio y mínimo | **per person** · «a minimum of 20 guests is required for on-site cooking» · «overall minimum must meet $1250» | tasteofpaella · cafesevilla |
| 13 | Temporada alta | **peak season** · holiday season | tasteofpaella · miamigrillcatering |
| 14 | Personal y formato | **buffet attendant** · serving staff · **buffet** · **family-style** · food stations | cafesevilla · zola Viton · zola Qué Paella · zola Señor Pepe's |
| 15 | Para llevar | **delivery orders** · «pick up & delivery» | zola Viton · IG Social Paella (SERP) |
| 16 | Desplazamiento · menaje | **travel fee** («included up to 20 mile radius») · **dishes & flatware** (bamboo / plastic) | cafesevilla · zola Señor Pepe's |
| 17 | Botella · carpa de cocina | **20-lb propane cylinder** / LP-gas container · **cooking tent** | VA 3107.12.5 / 3107.13.2 · Kit |
| 18 | Normas | **limited food preparation** (CA) · **shellstock tags** · **time as a public health control** | San Diego County · Food Code 3-203.12 / 3-501.19 |

**(e) No se traducen literalmente:** «paellero» → **paella chef** / **paella caterer** · «trípode de leña» → **wood-fire setup**
(con permiso) · «ración» → **serving / per person** · «show cooking» → **live paella** · «fiesta popular» → fuera del caso ·
«comunión, bautizo» → **first communion, baptism, quinceañera** (mercado hispano, Kit) · «finca» → **venue / backyard** ·
«garrofó» → **lima beans** · «ferraura» → **flat green beans** · «bogavante» → **lobster** · «regla de los 15 kg» → **no aplica**
(fire code, §6.3) · «época de peligro» → **burn ban** · «APPCC» → **HACCP-based food safety plan + TPHC SOP** · «manipulador» →
**food handler card** · «anticipo» → **deposit** · «IVA» → **sales tax** · «escandallo» → **cost per guest / food cost**.

**Capas (1) y (2):** **Paella Catering Business Plan Kit** · slug `paella-catering-business-plan` · `paella-catering-business-plan.docx`
«Paella Catering Business Plan (10 Sections)» · `paella-catering-financial-projections.xlsx` · `paella-catering-pricing-calculator.xlsx`
«Paella Catering Pricing Calculator (Pans, Rice and Price per Guest to Quote)» · `paella-catering-startup-checklist.xlsx` · pestaña F2
**«Phase 2 - Propane & Permits»** (27 car., ≤ 31) · rótulos con los términos 1-18 y `B11`, `B15`, `B24`, `B51` de §8.

### Términos para la landing (DataForSEO US, 24-oct)

| Keyword | Vol. | Uso |
|---|---|---|
| **paella catering business plan** · paella business plan · how to start a paella catering business | s/d · 10 · s/d | slug, H1, title |
| **paella catering** · paella caterer · **spanish catering** · paella party · tapas catering | 720 · 720 · 2.900 · 320 · 140 | title, H2, cuerpo, alt |
| paella catering prices · cost / menu (relacionadas) · paella pan · paella food truck | 10 · s/d · 12.100 · 90 | H2 precios y raciones, FAQ (→ Food Truck Kit) |

- **Title** (109 car.): «Paella Catering Business Plan Template: Word + Excel Financial Projections + Pricing Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Paella Catering ` + oro `Business Plan` + «Template to Start a Live Paella & Spanish Catering Company: Word
  Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist».
- **Meta** (145 car.): «Paella catering business plan template for a live-cooking Spanish caterer: Word plan, 3-year Excel
  projections, pricing calculator and checklist.»
- **H2 (6)**: What's Inside Your Paella Catering Business Plan Kit · How Much Does It Cost to Start a Paella Catering Business?
  (Pans, Burners, Van, Commissary) · Paella Catering Prices: What to Charge per Person for Paella, Tapas and Seafood · Cooking
  Paella at Events: Commissary, Propane and Food Safety Rules · Is a Paella Catering Business Profitable? Your 3-Year
  Projections · Paella for a Crowd: Pan Sizes, Rice per Guest and Staff for 50, 100 or 200 Guests.
- **FAQ**: How much does it cost to start a paella catering business? · How much should I charge per person for paella
  catering? · How many people does a 36-inch paella pan serve? · How much rice per person for paella for a crowd? · Can I cook
  paella at home and sell it? · Do I need a permit to cook paella at an event? · Can I serve sangria at my paella events? · Is
  a paella catering business profitable? · Is this plan for a paella food truck or restaurant?
- **Alt**: «Paella chef stirring a 36-inch seafood paella over a propane burner at an outdoor wedding» · «Backyard paella party with
  tapas» · «Paella pans and 3-ring burners loaded in a catering van». **No prometer** licencia de alcohol, cocina desde casa ni
  demanda del emprendedor. **Keywords** (schema/docProps): paella catering business plan, paella business plan, how to start a
  paella catering business, spanish catering business plan, paella catering prices, paella party, AI Chef Pro.

---

## (a) Tanda GPA-plan — xlsx del plan financiero (109 cadenas · 2.967 palabras ES · 77 con propuesta del BBQ ≈ 3.300 palabras EN) + revisión de las 98 GRB-plan

Entrada `BP7/tandas/GPA-plan.entrada.json` → **dos** salidas:

1. `BP7/textos_en/GPA-plan.json` (`{"<id>": "<EN>"}` con TODOS los ids y nada más):
   - **Notas del caso (51 forzadas + las que traían vocabulario BBQ)**: col. C de `0. Assumptions` (C4-C8 caso y
     realismo, C11-C15 mezcla paella packages / add-ons y B15 con el propano, C18, C24-C27 commissary que guarde paelleras
     y quemadores, seguros con llama abierta, C44-C62 vidas 7 / 5 con la base de D120, capacidad B51 informativa, rampa,
     contingencia, cobro 7 días con depósito no modelado, alcohol 0 % y la sangría), `Startup Costs` col. D filas 7-20 y 27
     (importes de research §8: quemadores $2,500, paelleras $1,800, kit de propano $900…), P&L F10/F11, F24, F27, F32-F35
     y los umbrales F53-F55 (D122), `Staffing` J5-J8, J18-J19 (personas por evento: drop-off 1 · backyard party 2 · empresa
     3 · boda 4.5 · premium 4 → ≈ 2.5), `Instructions` A5 y `12-Month Cash Flow`. La nota `C5` explica cómo pasar de los
     precios por paquete de la calculadora al precio medio de la mezcla (D123).
   - **Tabla D19, filas 55-68 «US PAELLA CATERING BENCHMARKS (sourced) AND KIT ESTIMATES»**, una celda cada vez
     (`por_celda`): **8 filas nuevas sin propuesta** (55 precio por persona de la paella en vivo · 56 menú español con
     personal · 57 arroz por invitado (Kit) · 59 invitados por paellera (Kit) · 61 paelleras y quemadores (Kit) · **63 paella
     chef y attendant cobrados aparte, cafesevilla.com** · 66 mínimos · 68 propano y desechables (Kit) + 1 persona por 25
     invitados, miamigrillcatering.com) y las celdas sucias de las 6 filas con propuesta (la 64, OEWS, por «chefs and head
     cooks»: es la ÚNICA celda donde vale). `Source` = el dominio de la fuente LEÍDA (tasteofpaella.com, zola.com,
     cafesevilla.com, miamigrillcatering.com, weddingwire.com, bls.gov, galleysolutions.com, itsacheckmate.com,
     thefoodcorridor.com, insureon.com) o «Kit estimate» (lo «(resumen)» de research: tienda.com, EIA, arroz por invitado).
   - **Tabla D18 «WHY THIS MODEL IS BUILT THIS WAY»**: las 14 celdas cuya propuesta del BBQ hablaba del smoker trailer, la
     leña o la carne: describe el MÉTODO con la van de carga, las paelleras y quemadores y el propano. Fila 39 =
     «Commissary kitchen and equipment storage» · fila 41 = dos vidas útiles (quemadores, paelleras, la van y sus upfits
     frente al kit de propano, el montaje y el equipo) · fila 42 = seguros de la van y el inland marine, una sola vez como
     gasto anual · **fila 43 = «Propane (and wood where a permit allows it)»**, dentro de la línea de desechables y
     combustible de cocina · fila 44 = contingencia sobre quemadores, paelleras, la van y sus upfits · **fila 49**: A
     «Miscellaneous event costs» · C «A percentage of sales, treated as a variable cost; van fuel has its own fixed line» ·
     D «Extra seafood, ice, lemons and venue parking rise and fall with the number of events: among the fixed costs they
     would distort the break-even.»
2. `BP7/textos_en/GRB-plan.revision.json`: revisa `revisar_reutilizadas.GRB-plan` (98: el resto de la tabla D18, notas del
   motor y las 21 celdas limpias de las filas D19 con propuesta). Son EN del BBQ que ya no traen vocabulario BBQ; si
   `en_actual` vale para un paella caterer, **no la incluyas**; si no, `{"<id>": "<EN corregido>"}`. **Coherencia por fila**
   (tus celdas de 1. y estas son la misma fila de la tabla): D18 filas 39, 41-44, 49 y 50 («Every sale carries its cost of
   goods: paella packages and add-ons each at their own rate»); **D19 fila 67** (Insureon): la nota añade que la general
   liability no excluya la llama abierta en eventos (Kit); **D19 fila 60** (food cost 28-35 %) y **58** (neto 7-8 %):
   catering en general, valen. Pagos: los particulares pagan depósito y saldo con tarjeta; algunas empresas por ACH. Si
   ninguna cambia: `{}`.

Umbrales del P&L (D122 = BBQ, ya en el libro): margen bruto del motor ≥ **58 %** · coste de mercancía ≤ **35 %** · personal ≤
**38 %** · commissary y almacén ≤ **7 %** · neto ≥ **5 %**, «kit benchmark (editable estimate)».

```bash
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda GPA-plan
python3 scripts/productos-digitales/business-plans-en-7/bp7.py preparar_tandas && \
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda GRB-plan
```

## (b) Tanda GPA-check — checklist (73 celdas que cambian · 455 palabras ES · propuesta del BBQ ≈ 1.850 palabras EN)

Entrada `BP7/tandas/GPA-check.entrada.json` → salida `BP7/textos_en/GPA-check.json` (`{"<id>": "<EN>"}` con TODOS los ids).
**68 tareas en 6 fases (11/13/12/10/12/10), no se añaden ni quitan**; aquí van **solo las 73 celdas que cambian** (las
otras 199 entran directas con la propuesta del BBQ: GLB-check). Cada celda es un id (`por_celda`): col. B = la tarea
(corta, imperativa), C = responsable, D = plazo US, E = nota práctica. **La pista de cada fila dice qué tarea va en esa
ranura y QUÉ columnas cambian**: «[sobrevive con ajuste: E]» = solo la nota; «[… B y E]» = la tarea y la nota; «[nueva]»
(P3 filas 7, 10 y 11: paelleras y quemadores · kit de la estación · arroz bomba, azafrán y despensa) = las 4 columnas.
Dos celdas van solo por una palabra vetada: `Phase 2!E15` («Texas», que se queda) y `Phase 3!E12` («pickup times» →
«drop-off and collection times»). **Coherencia con las celdas que NO ves** (columnas que no cambian de la misma fila: su EN
del BBQ ya vale): no las contradigas. **Columna C ya dice «Paella chef»** en las celdas directas: si escribes una C, usa
«Paella chef», «Owner / Paella chef», «Paella chef / Driver»… **P6 sin calcos «D-21 / D-1»**: «3 weeks out», «2 weeks out»,
«3-5 days out, then the day before», «Day of event», «Within 48 hours», «Weekly», «Day 90». Contenido: `fuente_es_pael.json`
→ `checklist_es` (fuera las SOLO_ES y lo español de las PARCIALES) + research §6. P2 = commissary con sitio para paelleras
y quemadores (¿cilindros?), agreement por escrito, county permit + «limited food preparation» como ejemplo de California
(«ask your county»), fire marshal y la estación de propano lejos de la carpa de invitados (Virginia como ejemplo), la van
(compra, DMV, upfit con racks verticales para los cilindros), GL sin exclusión de llama abierta, liquor liability solo con
el vino del cliente, residuos, aceite usado y conchas.

```bash
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda GPA-check
```

---

## Docx — reglas comunes de las tandas (c)-(d)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»: un párrafo EN por párrafo ES, sin saltos de línea en el
cuerpo, subtítulos de una línea sin punto final, toda cifra del caso con su token `{{…}}`, importes y porcentajes de
mercado solo si están en research/SPEC con fuente), más:

- **Redactas cada párrafo** (D126): `notas_del_plan` y la `nota` de CADA párrafo dicen el **nivel** («CASI LITERAL» 22 ·
  «ADAPTAR» 27 · «NUEVA» 12, F1-inventario §6), la **pista** de lo que va en esa ranura, la **PROPUESTA EN DEL BBQ** de la
  misma ranura (la forma) y, en «adaptar» y «nueva», el **párrafo ES 2.2 del paellero** (contenido de referencia: sus
  cifras, sus `{TOKENS}` en mayúsculas y todo lo español NO se usan). El `es` (food truck) solo da el papel y la longitud
  (±30 %). En las «casi literales», cambia SOLO lo que dice la pista (vocabulario BBQ, tokens, fuentes de la paella) y deja
  el resto de la propuesta.
- **Tokens de la paella** (usa estos, no los alias heredados ni los del BBQ): `eventos_a1/_a2/_a3`, `precio_invitado`,
  `precio_invitado_con_tax`, `invitados_evento`, `invitados_a1`, `ventas_evento`, `capacidad_eventos`,
  `cuota_paquetes_pct`, `coste_paquetes_pct`, `coste_extras_pct`, `equilibrio_eventos`, `equilibrio_caja_eventos`,
  `caida_absorbible_pct`, `pesimista_/optimista_eventos`, `_precio`, `_invitados`, `pesimista_caja`, `marketplace_pct`,
  `marketplace_comision`, **`cobro_dias` (días de COBRO) y `pago_dias` (días de PAGO a proveedores: cada token a su
  celda)**, `horas_evento`, `personas_evento`, **`inv_quemadores`** (quemadores y soportes, fila 7), **`inv_paelleras`**
  (fila 8), **`inv_propano`** (kit de propano y seguridad, fila 9), `inv_almacen`, `inv_furgoneta`, `inv_furgoneta_upfit`,
  `inv_llc`, `inv_permisos`, `inv_inspeccion`, `inv_software`, `inv_herramientas`, `inv_stock`, `inv_lanzamiento`,
  **`inv_montaje`** (montaje y holding, fila 20), `consumibles_pct` (sale «3.5%»), y los del motor (ventas, márgenes,
  inversión, préstamo, DSCR, caja, payback, plantilla). **No existen** `inv_vehiculo`, `inv_adaptacion`, `inv_rig` ni
  `inv_holding` (los del BBQ): la propuesta del BBQ los trae, cámbialos.
- **Realismo (D118), obligatorio en §1, §3 y §8**: {{eventos_a1}} eventos es el caso de un dueño-paella chef a tiempo
  completo con segundo cocinero los fines de semana, no la media del primer año (≈ $225K de ventas el año 1, Kit
  estimate); la holgura sobre el equilibrio es real pero justa; `{{pesimista_caja}}` es negativo: el docx dice que **la
  caja se agota** («the cash runs out»). [56]: la mezcla suma {{eventos_a1}} eventos (25 + 60 + 25 + 18 + 7 = 135; si el
  libro final cambia B4, el orquestador ajusta la mezcla).
- Fuentes citables (research §1, §5, §6, solo las leídas): tasteofpaella.com, zola.com (Viton Paella, Señor Pepe's, Qué
  Paella), cafesevilla.com, miamigrillcatering.com, weddingwire.com (Paella Time, Paella Valenciana), airbnb.com (Don
  Paella), fda.gov (Food Code 2022: 1-201.10, 3-201.11, 3-401.11, 3-501.16, 3-501.19, 3-203.12, Anexo 3),
  sandiegocounty.gov (caterer, CalRFC §113818), law.lis.virginia.gov (13VAC5-52-360), gov.uk; heredadas: bls.gov (OEWS mayo
  2025), thefoodcorridor.com, insureon.com, galleysolutions.com, itsacheckmate.com, cdtfa.ca.gov, IRS Rev. Rul. 2012-18. Lo
  marcado «(resumen)» en research (tienda.com, EIA, SBS Food, missvickie.com, Idaho, Boulder) → sin cifra o «Kit
  estimate».
- Fuera: portada «España 2026», «ChefBusiness», proveedores y marcas españolas, normativa autonómica, el anexo CCAA,
  «freelance», porcentajes sin fuente, la deuda ES («Paella valenciana DO»). Financiación: préstamo bancario o **SBA 7(a)**
  (el del ejemplo supera el tope de $50,000 del Microloan), «lender-ready, approval not guaranteed». Sin superlativos.
- El cierre (productos de la tienda) lo escribe el ensamblador (123-130): Catering Business Plan Kit · Food Truck Business
  Plan Kit · Food Cost Kit Pro · HACCP Food Safety Kit Pro; el 35 (anexos) nombra los 3 Excel.

## (c) Tanda pael_a — docx §1-§5 (29 párrafos · 2.954 palabras de ranura · propuesta del BBQ 3.334 palabras EN)

Entrada `BP7/tandas/pael_a.entrada.json` → salida `BP7/docx_en_pael_a.json` (`{"<i>": "<párrafo EN>"}`). §1 resumen con
tokens y la frase honesta del caso; §2 concepto (**[40] nueva**: cocinar en vivo ES el producto), qué vende y a quién (**[46]
nueva**), propuesta de valor (**[47] nueva**: socarrat, el paella chef incluido en el precio), modelo económico (depósito:
los caterers US piden 25-50 %), posicionamiento y **los 8 menu styles y los tipos de evento ([50] nueva)**; §3 mercado
desde el lado del cliente (búsquedas de research §2, bodas, empresas, **la mezcla de research §8 en [56]**, realismo); §4
competencia (Porter, barreras con paelleras y quemadores, DAFO); §5 marketing (The Knot, WeddingWire, Zola, ezCater,
Thumbtack, Google Business Profile, venues, planners, comunidad hispana, bridal shows, degustaciones).

```bash
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda pael_a
```

## (d) Tanda pael_b — docx §6-§10 (32 párrafos · 3.765 palabras de ranura · propuesta del BBQ 4.596 palabras EN)

Entrada `BP7/tandas/pael_b.entrada.json` → salida `BP7/docx_en_pael_b.json`. §6 operaciones (**[78]-[81] nuevas**:
commissary con sitio para paelleras y quemadores, el equipo y su orden de compra, las fases del evento con la víspera en la
commissary y la llegada 2-3 h antes, seguridad del arroz y del marisco con el mínimo del Food Code nombrado como tal;
[82] proveedores con approved source); §7 equipo (puestos de `Staffing`, W-2, OEWS, 1 persona por 25 invitados, un paella
chef por ≈ 3 paelleras, formación, service charge ≠ gratuity); §8 plan financiero SOLO con tokens (break-even en eventos
al año; [98] con `{{cobro_dias}}` y `{{pago_dias}}` cada uno en su sitio; realismo; pesimista que agota la caja); **§9 legal
= el núcleo** con las 7 notas (**102-105 nuevas**: 102 commissary y nada de casa; 103 permisos, CFPM, food handlers, plan
HACCP con arroz TCS, *B. cereus*, ≥ 135 °F o TPHC 4 h con SOP escrito, 165 / 145 / 155 °F, sobras fuera, approved source y
shellstock tags; 104 cocinar en el evento con San Diego como ejemplo, «ask your county»; 105 propano y carpas con Virginia
como ejemplo, «check with your fire marshal»; 106 sales tax, service charge y sangría sin vender alcohol; 107 empleo y
seguros con la llama abierta cubierta; **el 108 cierra con la nota UK**: registro 28 días antes, FHRS, 14 alérgenos con
moluscos, apio y sulfitos, VAT 20 %, gas con el council y el venue); §10 conclusiones y hoja de ruta en el orden del
checklist (Business Setup → Propane & Permits → Equipment → Staff → Marketing → First 90 Days).

```bash
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --tanda pael_b
```

## Después de las 4 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-7/bp7.py preparar_tandas      # aplica GRB-plan.revision.json
python3 scripts/productos-digitales/business-plans-en-7/bp7.py check_textos --todas  # GM, GRB-plan, GLB-check, GPA-plan, GPA-check + 2 docx
```

Luego el paso 3 en el VPS: ver `F2-NOTAS.md` §6.
