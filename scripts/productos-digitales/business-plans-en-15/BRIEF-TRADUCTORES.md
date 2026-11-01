# Brief para los traductores (subagentes Sonnet) — Burger Restaurant Business Plan Kit (EN)

> Sesión Claude Code, 31-oct-2026 (F2-EN). Fuente de verdad: `../plan-hamburgueseria/F1-camino.md` §6-§7 y
> `F1-research-us-delta.md` (US §n). Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**.
> Carpetas (worktree del Mac, raíz = `/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/6da9d44d-9610-4dc1-9bf3-066bbcb3f10a/scratchpad/wt-burger-en`):
> `scripts/productos-digitales/business-plans-en-15/` (= `BP15/`, datos y salidas de la hamburguesería),
> `scripts/productos-digitales/business-plans-en-14/` (= `BP14/`, el **Sushi Restaurant EN** LIVE: MISMA semilla de libro y
> MISMA rejilla, celda a celda; es la FORMA), `scripts/productos-digitales/business-plans-en-12/` (= `BP12/`, el **Taco Shop
> EN**: el vocabulario de mostrador, take-out y counter) y `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código
> común y el brief de FT/CAF).
>
> **Cuatro tandas, UNA a la vez**: (a) GBUR-plan + revisión de GR → (b) GBUR-check + revisión de GRC → (c) bur_a → (d) bur_b.
> Las entradas de (c) y (d) llevan `cifras_del_caso` (D15 VERDE ya calibrado; no cambian). **No se escriben** GM (359 cadenas:
> motor común con EN limpio) ni GR / GRC (41 + 105: EN reutilizado del Sushi EN que **se revisa** en tu tanda): los escribe
> `bp15.py preparar_tandas`. **El ES ya es FINAL** (F3 ES cerrada, `e883ebaa`).

**Cómo usar este brief**: lee la **sección 0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes: idioma, cero español, moneda,
formato US, marca, cifras, pestañas citadas) + las secciones **0, 1 y 5** de este fichero + la de tu tanda (§2, §3 o §4; las
del Word, además, el bloque «Docx — reglas comunes de las tandas (d)-(g)» de `BP/BRIEF-TRADUCTORES.md`). Lo que aquí choque
con el brief común **manda aquí**. No haces commit, **no corres `preparar_tandas`** y no tocas nada más que tus salidas.
**En el Mac no se ejecuta Python** (regla térmica): la validación corre en el VPS con el comando de §5.

---

## 0. Lo que cambia frente al Sushi EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP15/tandas/<TANDA>.entrada.json`; `BP15/F1-research-us-delta.md` §1, §4, §5, §6, §8
y §9; como FORMA (registro, longitud), el EN del Sushi EN en `BP14/textos_en/{GSUS-plan,GSUS-check}.json` y
`BP14/docx_en_sus_{a,b}.json` — la gemela está en la MISMA hoja y celda de `BP14/textos_es.json` (mismo esqueleto de
párrafos en el Word). **Su vocabulario de sushi NO vale** (sushi, nigiri, roll, platter, sake, raw fish, parasite, servers,
table service, closed Mondays, 310 days, 115 covers, $32.50, 40 seats, 1,800 sq ft…).

**Concepto (US §1): INDEPENDENT SMASH BURGER RESTAURANT** (fast casual, **counter service**), ciudad media de EE. UU. (150-500
mil hab.), ~**1,700 sq ft**, **44 plazas** (mesas y una window counter). Se pide en el **order counter** o en el **self-order
kiosk** y la comida sale en bandeja desde el **expo**: **sin servers** y sin propinas modeladas (las del tip jar o del POS son
del equipo). Pickup propio (take-out) y marketplaces. Carta: **smash burgers** (balls de 3 oz aplastadas en el **flat-top**
para formar la **crust**) single / double / triple, combos con fries, crispy chicken sandwich, veggie burger, fries, loaded
fries, **shakes**, soft drinks y **beer** (licencia como parámetro). Cocina: **dos flat-tops de gas de 48"**, bun toaster,
**tres fryers de gas con filtrado** (la tercera para el pollo rebozado: cross-contact) bajo **Type I hood + UL 300**, make
line, walk-in y reach-ins a 41 °F. **Abre 7 días**, 11:00-22:00 (23:00 viernes y sábado); apertura de cocina a las 8:30
(balls, cortes, salsas); **360 días** (cierra Thanksgiving, Christmas Day, New Year's Day y 2 días de mantenimiento de la
campana y las fryers). **El dueño es el GM.** Variantes (texto, sin Excel): **gourmet burger bar** con servers (propinas
aparte) y **ghost kitchen / delivery-only**; fuera: franquicias y drive-thru (solo comparación de inversión), burger truck
(→ Food Truck Business Plan Kit).

**Caso US** (`BP15/cifras_caso.json`; D15 VERDE en la vuelta 0, sin palancas): **195 covers × $16.50 × 360 días =
$1,158,300** · inversión total $382,704 (18 partidas $228,300 + imprevistos por fórmula $11,150 + fianza 2 meses + 2 de renta
previa + fondo de maniobra $125,254) · propios $130,000 + préstamo **$253,000** (SBA 7(a), 10 %, 10 años, sin
interest-only) · margen tras variables 55.5 % · COGS 31.2 % · personal 31.5 % (12 personas = 9.05 FTE) · alquiler 4.7 % ·
EBITDA $167,720 · **neto 7.6 %** el año 1 y 10.3 % el año 3 · equilibrio 160 / 157 covers al día · holgura de caja 24 % ·
DSCR mín 3.37× · saldo mínimo $136,539 (Mes 1) · payback 2.4 años · **pesimista $990,450 CON BENEFICIO de $23,372** (no es
pérdida: no uses `{{pesimista_perdida}}`) · optimista $1,362,025 con $229,781. **Check de $16.50 por cover equivalente**
(US §8): sala **107** covers × **$15.00** (comida $12.00 + bebida $3.00) · take-out **36 pedidos × $28.00** (≈ 58 covers) ·
marketplace **19 pedidos × $32.00** (carta un 15 % más cara; ≈ 30 covers) → $16.52; **1 order = 1.6 covers**. **Mes 1 =
ENERO** (orden del calendario: febrero el más flojo, enero y noviembre detrás; mayo —National Burger Month y graduaciones—,
junio, julio y agosto, los picos). El ES dice «comensal»; el EN dice **covers** («orders» para take-out y marketplace). Las
notas del libro describen el **método** o usan `valor_us` de tu entrada; **ninguna cifra del ES** (el gate las caza: 95
comensales, 16,00 €, 456.000, 104.350, 300 días, 36 plazas, 1,7 comensales por pedido, 14 pagas, 33 %, 17.094, 1.221, 24 % de
plataforma…).

**Lo que el check rechaza** (`datos_bur.RX_BUR_NO` + `cifras_prohibidas`): **sushi, nigiri, sashimi, maki, itamae, sake,
raw fish, parasite, omakase, nori, wasabi, imitation crab, poke, tempura, gyoza, teriyaki, rice cooker; «roll(s)»** (salvo
«potato roll» / «Martin's»: di **bun**); **«platter(s)»**; taco / taqueria, trompo / al pastor, tortilla, salsa bar, mezcal /
tequila; rotisserie, spit(s), family meal, heated display, yuca; pizza, Neapolitan, dough, VPN, mozzarella; tapas, small
plates, cocktails, happy hour, spirits (salvo «full liquor license» o negado); IVA, convenio, SMI, autónomo, Veri\*factu,
SGAE, IAE, terraza, **comensal / pedido / hamburguesería / bola / batido / menú del día**, **«fry-top»** (→ flat-top),
**«value meal»** (→ combo), **«smashed burger»** (→ smash burger; «smashed on the flat-top» sí), España / Spain / Spanish,
VAT fuera de la nota UK; RD 1021/2022, RD 1086/2020, RD 919/2006, «art. 4.1 / 7.2 / 7.3 / 30», Leyes 1/2025, 7/2022 y
37/1992, AESAN, Inf26008, la Orden de 1989, el Rgto. 2017/2158, ROESB, RGSEAA; las temperaturas españolas **«75 °C»,
«−18 °C», «70 °C»** (salvo «158 °F (70 °C)»), **«175 °C»**, **«63 °C»** (salvo «145 °F (63 °C)») y **«2 °C»**; el **«25 %»
de polares**; **«authentic»**, **«gourmet»** (salvo «gourmet burger bar», la variante), «gluten-free» salvo negado o con 21
CFR; **«rare», «medium-rare», «pink in the middle»** salvo con consumer advisory, 3-603.11 o negado; **afirmar que los
grinding logs son obligatorios**; **«servers» / «table service»** salvo en la variante burger bar o negado («no servers»);
**«closed Mondays», «six days a week»**; kg, g, km, liters, ml o °C fuera de paréntesis; y los casos EN del Sushi (115
covers, 310 days, $32.50, 40 seats, 1,800 sq ft), el Taco (308 days), el Rotisserie (130 covers), la Pizza (62 covers), la
Ice Cream, la Bakery, el Bar ($27), FT y el Restaurant. **Sí valen** (son del caso burger): 195 covers, 44 seats, 1,700 sq ft,
360 days, $16.50, $17.50 (optimista), 180 covers (pesimista), counter service, kiosk, seat turns, open 7 days, griddle.

**Jerga burger** (US §9, ya decidida en el Burger Joint Checklists Kit Pro, `../checklists-kit/burger/`, y en
`../GLOSARIO-JERGA-ES-EN.md`): smash burger · ball (cruda, 3 oz) · puck · patty (el disco cocinado) · **flat-top** (o
griddle) · smash press / smasher · burger scraper · crust · lacy edges · **potato bun** · single / double / triple · **combo**
· **shake** · make line · expo · grill cook · fry cook · shift lead · counter crew · cook loss · ground beef (80/20) · ground
chuck · blend (chuck, brisket, short rib) · American cheese · fries (frozen 3/8" crinkle o fresh-cut) · cross-contact
(alérgenos) · cross-contamination (patógenos) · take-out / to-go / pickup · third-party delivery marketplace · recipe
costing · cost per burger · plate cost. «Hamburguesería» → **burger restaurant** (títulos) · **burger joint / burger shop**
(prosa coloquial); «hamburguesa» → **burger**.

**Unidades** (`datos_bur.REGLA_UNIDADES`): lb, oz, fl oz, gallons, °F y sq ft como unidad principal; la métrica entre
paréntesis: «3 oz (85 g)», «155 °F (68 °C)», «41 °F (5 °C)», «1,700 sq ft (158 sq m)».

**Lo legal y operativo que SUSTITUYE al ES** (US §6; nunca se traduce el trámite español):
- **Cocción de la carne picada** (FDA Food Code 2022 **3-401.11(A)(2)**; cada estado adopta su edición): **155 °F (68 °C)
  durante 17 segundos**, o 145 °F 3 min · 150 °F 1 min · 158 °F instantáneo. **SOP del kit**: TODAS las smash a ≥ 155 °F 17 s,
  sonda de punta fina en una por tanda (el color y la crust no certifican la temperatura). Poultry 165 °F. Hot holding ≥ 135
  °F; cold holding ≤ 41 °F.
- **Consumer advisory 3-603.11** solo si el dueño ofrece la burger **cooked to order** (poco hecha a petición del cliente,
  3-401.11(D)): disclosure («hamburgers (can be cooked to order)» o asterisco) + reminder («Consuming raw or undercooked meats,
  poultry, seafood, shellfish, or eggs may increase your risk of foodborne illness»), en la carta, la web y **los listados de
  marketplace**; nunca en el menú infantil ni para highly susceptible populations (3-801.11). **El caso sirve todo cocido y
  no necesita advisory.**
- **Carne**: comprada ya picada o en balls con el **establishment number** del proveedor, lotes y fechas; cruda ≤ 41 °F,
  **separada** por debajo de lo listo para comer y por especie (3-501.16, 3-302.11). **Grinding logs**: la regla de FSIS (9
  CFR 320.1(b)(4)) es para «retail stores and official establishments that grind raw beef»; **el kit NO afirma que sea
  obligatoria para un restaurante**: si picas en casa, **house-grind log** como buena práctica (lotes, establishment numbers,
  fecha y hora de cada picada y de cada limpieza) y «ask your health department». La regla española de la carne madurada **no
  cruza** (el caso no ofrece dry-aged).
- **Aceite**: filtrado cada noche y cambio por **TPM** (total polar materials) o por el fabricante, **sin límite federal**;
  freír a 350-355 °F; el usado a un **renderer** autorizado. **Acrilamida**: sin límite federal para restaurantes; **California
  Prop 65** («ask your attorney about the Prop 65 warning for fried potatoes»).
- **9 alérgenos mayores** con sésamo (FASTER Act, desde 2023): el **bun** (wheat; milk, egg y soy según la receta; sesame en
  las semillas y a veces en el aceite), el **American cheese** (milk), las salsas (mayo = egg), los **shakes** (milk; mix-ins
  con peanuts o tree nuts), el pollo rebozado (wheat, egg, milk) y **el aceite compartido** (cross-contact); el flat-top
  compartido pasa wheat y sesame si se tuesta el bun en él. **La mostaza NO es major en EE. UU.** (sí en UK). **«Gluten-free»
  no se promete** (21 CFR 101.91). Allergen matrix.
- **Type I hood** + supresión **UL 300** + makeup air sobre los flat-tops y las fryers; limpieza de campana y conductos según
  **NFPA 96** (trimestral con mucha grasa, semestral si moderada: «ask the fire marshal»); **Class K** + extintores; **grease
  interceptor** (lo dimensiona el condado en el plan review). Plan review (**8-201.11**) + health permit + inspección previa ·
  building permit + certificate of occupancy · business license + sales tax permit · **CFPM (2-102.12)** + food handler
  cards según estado · gas lines por un plumber o gas fitter licenciado con su permiso.
- **Beer license o beer & wine license** (estado + aprobación local; «apply early», **nunca prometerla**); liquor liability en
  el seguro. Personal **W-2 por horas** (nada de 1099), ≥ $15/h, **sin servers y sin tip credit**; SBA 7(a); **sales tax 8 %** de
  ejemplo, un solo tipo («some states tax to-go food differently», sin cifra).
- **«The ball is the business»** (US §8): cada onza cuenta; pesar las balls con báscula (nunca a ojo), no mezclar lotes en el
  flat-top, merma objetivo ≤ 4 % de la carne comprada; **revisar el precio de la carne cada 4 semanas**. Las cifras por burger
  las da la **Smash Burger Patty, Fries & Costing Calculator** del kit (pestañas `Beef & Patty` · `Fries & Oil` · `Costing` ·
  `Instructions`): solo las de `BP15/cifras_calculadora.md` (caché de la calculadora); **no inventes porcentajes por burger**.
- **Ningún producto citado** salvo los del cierre del Word (Burger Joint Checklists Kit Pro · Food Cost Kit Pro · HACCP Food
  Safety Kit Pro · Food Cost + Menu Engineering Guide) y, como variante, el Food Truck Business Plan Kit.

---

## 1. Glosario OBLIGATORIO

El **§9 de `BP15/F1-research-us-delta.md`** entero (tabla de 19 filas + «(e) No se traducen literalmente» + capas (1) y
(2)): léelo y aplícalo. Además, `glosario` de tu entrada (incluye `datos_bur.GLOSARIO_BUR`). Rótulos que cites (partidas,
puestos, pestañas) con las palabras de `fijos_en` / `pestanas_es_en` de las entradas de la tanda (a)/(b).

---

## 2. Tanda (a) — GBUR-plan + revisión de GR

Entrada `BP15/tandas/GBUR-plan.entrada.json`: **115 cadenas, ≈ 3,7 K palabras** (67 de texto libre + **48 celdas D19**: 12
filas × 4; sin propuesta) + `revisar_reutilizadas.GR` (**41** cadenas del Sushi EN). Salidas: `BP15/textos_en/GBUR-plan.json`
(TODOS los ids, `{"<id>": "<EN>"}`) y `BP15/textos_en/GR.revision.json` (solo las de GR que cambian; `{}` si ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista o el método; el ES explica el comensal equivalente (sala +
  pedidos × 1,7) con cifras ES: **en EN, covers** con las cifras US de la pista (C4, C5, C6), **1 order = 1.6 covers**,
  **ninguna cifra ES**. Sin el 10/21 % del IVA español: un solo sales tax de ejemplo (8 %, B39 = B40 = B63), sin crédito por
  compras (B41 = 0). **C13**: el puente del food cost (34 % = consumo real de toda la carta con la merma; el teórico por burger
  de la calculadora sale más bajo, **sin cifra inventada**). **C34**: B34 = 0 (sin carencia). **C35**: el colchón de 3 meses
  para la rampa de enero a abril (sin el agosto español). **C60/C61**: con 12 pagas no hay pagas extra. **C62/C63** y **A62**
  están fijadas (POR_CELDA). **C68** (convenio ES): «state/local minimum wage; this plan budgets ≥ $15/h». **A51**: «Seating
  capacity (seats, window counter included)».
- **Notas de `Startup Costs` (col. D, filas 7-24)**: las partidas de F1-camino §6 en las filas ES (rótulos ya fijados en
  `fijos_en`: **lee el rótulo EN de la fila antes de escribir su nota**). La campana va partida como en el ES: **D9** = el duct
  hasta la cubierta con el makeup air; **D14** = la campana Type I con la supresión UL 300. Rangos solo con fuente de US §4 o
  ninguno; nada de precios en € ni de Madrid.
- **`3-Year P&L` col. F**: F10 = reparto de la comida de su pista; F11 está fijada; F13 es fórmula (ya EN); umbrales del
  semáforo del libro EN (**margen tras variables ≥ 52 %**, mercancía ≤ 33 %, personal ≤ 36 %, alquiler ≤ 10 %, neto ≥ 5 %:
  F50, F52, F53, F55 con su pista). Notas de los fijos 26-34 con los rótulos fijados (hood cleaning **trimestral**; las
  renovaciones de permisos —CFPM, food handler cards— van con la formación, fila 34).
- **`Staffing` col. J**: los puestos de US §8 en la fila ES de su jornada (rótulos fijados: Owner / GM · Grill cooks (smash
  station) · Fry & prep cook · Shift lead · Counter crew (cashier, expo, to-go packing) · Weekend crew (part-time W-2) · Dish &
  prep); cada J lleva su pista con el $/h. A29 está fijada. J21-J24: la cobertura de US §8 (servicio 11 h × 3.5 + producción
  2.5 h × 2).
- **`Break-Even`**: rotación ENCENDIDA (= Sushi): techo **5** seat turns (E25: 11 h abiertas, pedido en el counter, estancias
  de 20-30 min; solo la sala da ≈ 2.4); A28 es fórmula (ya EN).
- **Tabla D19 (`Instructions` 35-46, una cadena por celda, SIN propuesta)**: cada fila la dicta su pista: Benchmark | Value |
  Source | Note, en el orden de las filas (Month 1 · consumer demand · menu prices · ball size · burgers per lb · marketplace
  commission · sales tax · ground beef cooking · ground beef cold holding · frying oil · minimum wage · labor cost). Solo lo
  «[leída]» con fuente; lo «(resumen)» como «Kit estimate» o «secondary sources».
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21 («divide a menu price by 1 + your sales tax rate»); A10 con el
  **Mes 1 = JANUARY** (sin el cierre de enero ni el agosto español); A12: el Word usa las cifras de este Excel y la calculadora
  del kit (**Smash Burger Patty, Fries & Costing Calculator**) calcula el coste de cada burger por canal: su food cost NO se
  copia en «0. Assumptions».
- **`12-Month Cash Flow`**: O5 está fijada (POR_CELDA); O16 (IVA por línea): «each sales line at ITS rate, read from the tax
  column of the P&L (one 8% rate in the example)», sin artículos de la ley española.
- **Revisión de GR** (EN del Sushi EN en la misma celda): confirma que vale para un smash burger restaurant con counter service
  y corrige solo lo que no case. **Dos ya sabidas, corrígelas**: **c0099** (`0. Assumptions!C58`) dice «(15% of sales)»: el caso
  burger es el **19 %**; **c0375** (`Staffing!J11`) dice «Dishwashing, rice washing and prep: about $16 per hour»: es **dish &
  prep** de la hamburguesería (friegue, limpieza del flat-top y de la línea, reposición; **about $15.50 per hour**, 1 × 0.6).

## 3. Tanda (b) — GBUR-check + revisión de GRC (las 80 tareas)

Entrada `BP15/tandas/GBUR-check.entrada.json`: **116 cadenas, ≈ 3,5 K palabras** + `revisar_reutilizadas.GRC` (**105**:
plazos, responsables, cabeceras y tareas que el Sushi EN ya tenía en la misma celda). Salidas:
`BP15/textos_en/GBUR-check.json` (TODOS los ids) y `BP15/textos_en/GRC.revision.json` (solo las de GRC que cambian; `{}` si
ninguna). Molde C2 (OK | TASK | OWNER | TIMING | NOTES); pestañas fijadas («Phase 1 - Business Setup» · «Phase 2 - Hood &
Permits» · «Phase 3 - Beef & Health» · «Phase 4 - Staff & Allergens» · «Phase 5 - Menu, Brand, Delivery» · «Phase 6 - Opening
& 90 Days»); A1 = «BURGER RESTAURANT STARTUP CHECKLIST»; cabeceras de las fases 2 y 3 fijadas; las demás (A2) siguen el
nombre de su pestaña con sus semanas. **DV**: «✓,☐,N/A» (☐ = pending). Responsables US: Owner, Shift lead, Grill cook, Fry &
prep cook, Contractor, Architect / engineer, Plumber / gas fitter, CPA, Insurance broker, Attorney… («Gestoría» → «CPA /
bookkeeper»).

**Tareas propias obligatorias** (F1-camino §6; regla B2: toda regla que prometan landing, hub o Word tiene su tarea):
**cook every smash to 155 °F for 17 seconds; probe one per batch** (F3!B10) · **consumer advisory on the menu, website and
marketplace listings if you offer cooked-to-order** (F3!B12, sustituye la congelación de bolas propias) · **keep supplier
establishment numbers and lot dates; house-grind log if you grind** (F3!B7-B8) · **filter fryers nightly and change oil by
TPM** (F3!B14) · **hood cleaning schedule per NFPA 96** (F6!B13) · **California: ask your attorney about the Prop 65 warning
for fries** (F3!B13) · y la **beer license** (F1, ya en GRC: confírmala). No hay filas nuevas: se reescribe la tarea
existente. Encaje propuesto (las que no tienen equivalente US se SUSTITUYEN; las NOTES de cada fila, a juego):

| Celda | ES | Tarea US propuesta |
|---|---|---|
| F1!B5 | Consulta urbanística: extracción, potencia y aforo | Zoning check before signing: restaurant use, Type I hood route, electrical service and seats |
| F1!B6 | Formato antes de firmar | Decide your format before signing the lease: counter service with take-out and delivery, delivery-only, or a burger bar with servers |
| F1!B7 | Carne comprada picada o picada en el local | Decide before signing: buy ground beef (or pre-portioned balls) or grind in-house |
| F1!B8 | Patata congelada o fresca | Decide before signing: frozen fries or fresh-cut |
| F1!B9 | SL o autónomo | Choose your entity (LLC or S corp with your CPA) and get your EIN |
| F1!B10 | Alta censal 036 (IAE) | Business license + **sales tax permit** (state and city) |
| F2!B5 | Local de unos 90 m² | Second-generation restaurant space of about 1,700 sq ft (158 sq m) with a route for the Type I hood |
| F2!B14 | Campana sobre plancha y freidoras | Type I hood with UL 300 fire suppression over the flat-tops and fryers (permit and fire marshal sign-off) |
| F2!B15 | Gas por empresa habilitada | Gas lines by a licensed plumber or gas fitter, with permit and inspection |
| F2!B16 | Obra lisa y lavable | Build-out of kitchen, order counter and dining room with smooth, cleanable surfaces |
| F2!B18 | Zona de empaquetado y repartidores | To-go packing and driver pickup area by the door |
| F2!B19 | Boletín, gas y final de obra | Final electrical, gas and building inspections → certificate of occupancy |
| F3!B6 | APPCC: picada a 2 °C | Written food safety plan: raw ground beef at 41 °F or below, stored below ready-to-eat food |
| F3!B7 | Si picas: solo lo del día | If you grind: keep a house-grind log (lots, establishment numbers, time of each grind and each cleaning) |
| F3!B8 | Si picas: músculo, frío, plazo | Keep supplier establishment numbers, lots and pack dates for every beef delivery |
| F3!B9 | Nada de madurada para picar | Ground beef only from approved suppliers with spec sheets (no dry-aged program in this plan) |
| F3!B10 | Control de la cocción con sonda | **Cook every smash to 155 °F for 17 seconds; probe one per batch** |
| F3!B11 | Recepción y utensilios de crudo | Receiving log (beef at 41 °F or below) and separate raw-meat tools and trays |
| F3!B12 | Congelar bolas propias | **Consumer advisory on the menu, website and marketplace listings if you offer cooked-to-order** |
| F3!B13 | Acrilamida | Fries: fry at 350-355 °F to a golden color; **California: ask your attorney about the Prop 65 warning** |
| F3!B14 | Polares < 25 % | **Filter fryers nightly and change the oil by TPM** (no federal limit); used oil to a licensed renderer |
| F3!B15 | Salsas a 63 °C | Hot holding at 135 °F or above (cheese sauce, chili); cool and reheat per Food Code |
| F3!B16 | Verdura a 4 °C en la línea | Cut produce and sauces on the make line at 41 °F or below, date-marked (7 days) |
| F3!B17 | Trazabilidad y registros | Traceability and logs: lots, dates and temperatures |
| F3!B18 | Fichas de cada hamburguesa | Recipe cards for every burger with its major allergens |
| F4!B6 | Cocinero de plancha antes de la obra | Hire the lead grill cook BEFORE the build-out |
| F4!B11 | Manipuladores con carne y freidora | CFPM + food handler cards, with ground beef and fryer safety |
| F4!B12 | Formación de la línea | Line training: ounces per ball, the smash and the build |
| F4!B16 | Matriz de 14 alérgenos | Allergen matrix (9 major in the US) with the bun, sauces, cheese, shakes and breaded items |
| F4!B17 | No prometer «sin gluten» | Never promise «gluten-free» with a wheat bun, a shared fryer and a shared flat-top (21 CFR 101.91) |
| F5!B5 | Carta de 14 referencias y menú | Short menu of about 14 items and the combo |
| F5!B6 | Escandallo por canal | Cost per burger and per combo by channel (calculator) |
| F5!B7 · B8 | IVA para llevar · batido y menú | Sales tax on the menu: one rate in the plan · check your state's rules for to-go food and combos |
| F5!B9 | Envases (Ley 1/2025) | To-go packaging that meets your local ordinances (some cities ban polystyrene) |
| F5!B10 · B11 | Proveedores de carne · pan y patata | Two beef suppliers with spec sheets and establishment numbers · bun and fries suppliers with spec sheets and allergens |
| F5!B14 | Alérgenos y temperatura del pedido | Allergens before ordering and hot food out fast (consumer advisory in the listing if you offer cooked-to-order) |
| F5!B16 | Google Business, vídeo y fechas | Google Business Profile, Yelp, Instagram and TikTok and peak dates (National Burger Month, Super Bowl Sunday, March Madness) |
| F6!B7 | Limpieza de plancha y freidoras | Cleaning schedule for the flat-tops, fryers and make line |
| F6!B11 | Pesar 10 bolas | Weigh 10 balls, measure cook loss and fries portions, and recalculate (calculator) |
| F6!B12 | Polares y cambios de aceite | Log TPM readings and every oil change |
| F6!B13 | Mantenimiento | **Hood and duct cleaning schedule per NFPA 96**, flat-tops, gas and refrigeration |
| F6!B14 | Calibrar la sonda | Calibrate the probe thermometers (ice-point check) |

- **Revisión de GRC**: casi todo plazos («Weeks 3-6»), responsables y tareas comunes del Sushi EN: confirma que valen y corrige
  solo lo que no case (sushi, fish, rice, servers, sake…).

## 4. Tandas (c) bur_a (§1-5) y (d) bur_b (§6-10)

Lee además el bloque «Docx — reglas comunes de las tandas (d)-(g)» de `BP/BRIEF-TRADUCTORES.md` y, como FORMA, la misma
sección del Sushi EN (`BP14/docx_en_sus_a.json` o `docx_en_sus_b.json`, mismo esqueleto de párrafos).

| Tanda | Entrada | Párrafos · palabras ES | Salida |
|---|---|---|---|
| (c) bur_a | `BP15/tandas/bur_a.entrada.json` | 29 · 3,371 (§1 Executive Summary · §2 Concept · §3 Market · §4 Customer · §5 Marketing) | `BP15/docx_en_bur_a.json` |
| (d) bur_b | `BP15/tandas/bur_b.entrada.json` | 32 · 4,563 (§6 Operations · §7 Staffing · §8 Financial Plan · §9 Legal · §10 Roadmap) | `BP15/docx_en_bur_b.json` |

- Formato de salida: `{"<i>": "<párrafo EN>", …}` con TODOS los «i» de `parrafos` y nada más; un párrafo por clave, sin
  saltos de línea nuevos; los subtítulos (una línea sin punto final) siguen siendo una línea sin punto final.
- Cada párrafo trae su `nota` (`datos_bur.DOCX_NOTAS`): la sección + la FORMA del Sushi EN; las 7 de §9 (102-108) fijan el
  tema de cada párrafo (102 marco y permisos · 103 hood, fuego, aceite, health permit y CFPM · 104 **carne picada: 155 °F 17 s,
  41 °F, establishment numbers, grinding logs sin afirmar obligación** · 105 **consumer advisory solo si cooked to order y
  acrilamida / Prop 65** · 106 alérgenos y «gluten-free» · 107 beer license, seguro, personal y propinas · 108 venta desde casa
  y **las notas UK y Australia al final, sin cifras de cocción**, que el check exige).
- **Lo que no cruza del Word ES** (IVA partido, RD 1021/2022 y sus 2 °C, la picada del día, la carne madurada y los plazos del
  853/2004, AESAN y sus 70 °C, el Rgto. 2017/2158 y sus 175 °C, los polares < 25 % de la Orden de 1989, RD 919/2006, la ordenanza
  de Madrid, IAE, convenio, SMI, 14 pagas, Leyes 1/2025, 7/2022 y 37/1992, Veri\*factu, el menú del día español, el cierre de
  enero, agosto, las franquicias españolas, Goiko, Smash Hiro, Street Smash, el local de 90 m² y las 36 plazas, el Kit de Tareas
  Hamburguesería) se **sustituye** por el bloque legal de §0 y el caso US.
- **Cifras**: las del plan, SOLO como tokens `{{…}}` de `tokens` (usa **`{{cogs_pct_xl}}`** y **`{{plantilla_jornadas_xl}}`**,
  que redondean como Excel). La entrada trae `cifras_del_caso` SOLO para que entiendas el caso: **en el texto va el token,
  nunca la cifra**. **El pesimista da BENEFICIO** ({{pesimista_resultado}}): no uses `{{pesimista_perdida}}` ni digas
  «loss». Importes «$» fuera de tokens solo los de la research con su fuente (US §4 y §5: flat-top de 36" $589-$4,858,
  smash presses $10.49-25.99, Martin's potato rolls $0.55, American cheese ≈ $0.14 la loncha, fries $1.11-1.16/lb, ground beef
  retail $6.79/lb (BLS/FRED, sep-2026), carne del kit $5.25/lb, walk-in $12,800; Smashburger $1,239,500-$2,255,500 y Freddy's
  $785,936-$2,753,566 de Item 7 «reported by third-party franchise directories; check the FDD»; el AI Overview «$30,000 to
  $130,000» de un pop-up; FinModelsLab $79-119) y las de la calculadora en `BP15/cifras_calculadora.md`. **Ningún porcentaje
  por burger inventado.**
- **Terminología** (manda): covers · burger restaurant · smash burger · burger joint (coloquial) · ball · patty · flat-top ·
  smash press · crust · potato bun · American cheese · single / double / triple · combo · shake · fries · make line · expo ·
  grill cook · shift lead · counter crew · counter service · self-order kiosk · take-out · pickup · delivery marketplace ·
  beer license · Type I hood · NFPA 96 · TPM · consumer advisory · cooked to order · establishment number · house-grind log ·
  CFPM · Month 1 = January.

## 5. Validación — en el VPS, el comando EXACTO de cada tanda

Escribe tus salidas en el Mac (rutas de §2-§4), cópialas al VPS y valida allí (el Mac no ejecuta Python). Itera hasta
`OK (0 errores, …)` y revisa los AVISOS reales. **No corras `preparar_tandas`**.

```bash
W=/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/6da9d44d-9610-4dc1-9bf3-066bbcb3f10a/scratchpad/wt-burger-en
B=scripts/productos-digitales/business-plans-en-15; R=/root/wt-burger-en; PY=/root/venv-guias/bin/python
# tanda (a)
scp -q $W/$B/textos_en/GBUR-plan.json $W/$B/textos_en/GR.revision.json vps:$R/$B/textos_en/ && \
  ssh vps "cd $R/$B && $PY bp15.py check_textos --tanda GBUR-plan; $PY check_revision.py GR"
# tanda (b)
scp -q $W/$B/textos_en/GBUR-check.json $W/$B/textos_en/GRC.revision.json vps:$R/$B/textos_en/ && \
  ssh vps "cd $R/$B && $PY bp15.py check_textos --tanda GBUR-check; $PY check_revision.py GRC"
# tanda (c)
scp -q $W/$B/docx_en_bur_a.json vps:$R/$B/ && ssh vps "cd $R/$B && $PY bp15.py check_textos --tanda bur_a"
# tanda (d)
scp -q $W/$B/docx_en_bur_b.json vps:$R/$B/ && ssh vps "cd $R/$B && $PY bp15.py check_textos --tanda bur_b"
```

Responde solo con: ficheros escritos, nº de claves (y de correcciones de la revisión), resultado de los checks y 3-5
decisiones de traducción que deban conocer las otras tandas.

**Después (orquestador)**: ver `F2-NOTAS.md` (comandos de la cadena completa).
