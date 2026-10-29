# Brief para los traductores (subagentes Sonnet) — Taco Shop Business Plan Kit (EN)

> Sesión Claude Code, 29-oct-2026 (F2-EN: preparado; **no se ha traducido nada**). Fuente de verdad: `../plan-taqueria/
> F1-camino.md` §6-§7 y `F1-research-us-delta.md` (US §n). Regla 1bis: los textos de producto los escriben subagentes
> Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac): `scripts/productos-digitales/business-plans-en-12/` (=
> `BP12/`, datos y salidas de la taquería), `scripts/productos-digitales/business-plans-en-8/` (= `BP8/`, la **Pizza Shop
> EN** publicada: MISMA rejilla de libro, mismo código y la FORMA) y `scripts/productos-digitales/business-plans-en/` (=
> `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GTAQ-plan + revisión de GR ‖ (b) GTAQ-check + revisión de GRC** →
> **tanda 2 = (c) taq_a ‖ (d) taq_b** (las entradas ya existen y llevan `cifras_del_caso`; el orquestador las regenera
> tras la tanda 1 con `preparar_tandas` + `anotar_tandas_docx.py`, sin cambiar ids).
> **No se escriben** GM (361 cadenas: motor común con EN limpio de la Pizza EN, el Bar EN o BP) ni GR / GRC (34 + 102: EN
> reutilizado de la Pizza EN o del Bar que **se revisa** en tu tanda): los escribe `bp12.py preparar_tandas`.
> **El ES ya es FINAL** (F2 ES revisada, `f5c5b269`; sha256 en `mapas_taq.SHA_ES`): los ids son los definitivos.

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas) + las secciones **0, 1 y 5** de este fichero
(la 1 es el glosario US §9 completo, OBLIGATORIO; la 5, la validación) + la de su tanda (§2, §3 o §4). Lo que aquí choque
con el brief común **manda aquí** (el comando de validación es el de §5, con `bp12.py`). El subagente no hace commit,
**no corre `preparar_tandas`** y no toca nada más que sus salidas.

---

## 0. Lo que cambia frente al brief de la Pizza EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP12/tandas/<TANDA>.entrada.json`; `BP12/F1-research-us-delta.md` §1, §4, §5, §6
y §8 (el §9 va pegado abajo); como FORMA (registro, longitud), el EN de la Pizza EN en `BP8/textos_en/{GPIZ-plan,
GPIZ-check}.json` — el libro de la taquería es la MISMA rejilla que el de la pizzería: la gemela está en la misma hoja y
celda de `BP8/textos_es.json` (en el checklist, la misma posición de pestaña). **Su vocabulario de pizzería NO vale**
(pizza, oven, dough, Neapolitan, wood-fired, firewood, flue, peel, servers…).

**Concepto (US §1): COUNTER-SERVICE TACO SHOP de barrio** en una ciudad media de EE. UU. (150-300 mil hab.), ~1,200 sq ft,
30 plazas + patio de 12 (abril-octubre), pedido en mostrador (**sin servicio de mesa: nunca «servers» ni «waitstaff»**),
take-out/pickup propio y marketplaces. Línea: **dos trompos de gas** (vertical broilers) para el al pastor, flat-top
griddle y comal, freidora para chips, fogón para carnitas y guisados, steam table, **salsa bar** refrigerada. Carta: 8-10
street tacos en doble tortilla de maíz de 6 in, quesadillas y gringas, plates (3 tacos + rice & beans), chips & guac,
aguas frescas, refrescos y **beer & wine** (Mexican beer; **sin full liquor: nada de mezcal ni tequila en el caso**).
Cierra los lunes; el dueño es el head taquero y el GM. **«Taco shop»** en nombres y títulos; **«taqueria»** (sin tilde) en
prosa; **nunca «Tex-Mex» como sinónimo ni «authentic» como promesa**. Volumen = **covers**. Fuera (y así lo dicen las
FAQ): taco truck (→ Food Truck Business Plan Kit), franquicia, restaurante mexicano de mesa con bar completo, venta desde
casa.

**Caso US** (`BP12/F2-NOTAS.md` §3; D15 VERDE en la vuelta 0, sin palancas): 115 covers × **$17.50** × 308 días =
**$619,850** · CAPEX $197,600 (18 partidas $176,800 + fianza de 2 meses + 2 meses de renta previa + imprevistos por
fórmula $9,600) + fondo de maniobra $78,012 = **$275,612** · propios $100,000 + préstamo **$176,000** (SBA 7(a), 10 %, 10
años, sin interest-only) · margen tras variables 62.0 % · COGS 26.2 % · personal 34.6 % (8 personas = 5.02 FTE) ·
alquiler 5.4 % · EBITDA $89,858 · **neto 6.3 %** el año 1 y 9.2 % el año 3 · equilibrio 100 / 97 covers al día · holgura
de caja 19 % · DSCR mín 2.68× · saldo mínimo $79,892. **Mes 1 = ENERO** (orden del calendario: enero-febrero flojos, mayo
el pico con Cinco de Mayo y el patio). Las notas del libro describen el **método** o usan `valor_us` de tu entrada;
**ninguna cifra del ES** (el gate las caza, en € y en $: 77 comensales, 15,50, 358.050, 300 días, 14 pagas, 33 %, 17.094,
1.221, 12 % de plataforma, 9,1 % de neto…).

**Lo que el check rechaza** (`datos_taq.RX_TAQ_NO` + `cifras_prohibidas`): pizza, Neapolitan, dough (di «masa»),
wood-fired / firewood, VPN, Margherita / mozzarella / San Marzano; tapas, small plates, cocktails, happy hour, spirits y
mezcal / tequila (salvo para decir que hacen falta otra licencia: «full liquor license»); IVA, convenio, SMI, autónomo,
Veri\*factu, SGAE, IAE, terraza, comensal, España / Spain, VAT fuera de la nota UK; RD 1021/2022, RD 1086/2020, «art. 4.1»,
«art. 30», Ley 1/2025, Ley 7/2022, ACSA, AESAN; **authentic**; Tex-Mex salvo negado; «gluten-free» salvo «naturally
gluten-free» o negado; servers / waitstaff / waiters salvo «no table service / counter service»; kg, g, km, liters, °C o
m² fuera de paréntesis; y los casos EN de la Pizza (62 covers, $36…), la Ice Cream (165 customers), la Bakery, el Bar, FT
y el Restaurant.

**Jerga mexicana que el inglés US usa tal cual** (el detector de restos de español no la cuenta: `mapas_taq.TERMINOS_MX`):
«al pastor», «pico de gallo», «Cinco de Mayo», «chile de árbol», «tacos de lengua / cabeza / canasta», «carne asada»,
«consomé». Cualquier otra construcción española con «de», «con», «al», «la»… **la marca el check** («con todo» →
«with everything»; «agua de jamaica» → «jamaica (hibiscus) agua fresca»).

**Unidades** (`datos_taq.REGLA_UNIDADES`): lb y oz, °F, gallons / quarts y sq ft como unidad principal; la métrica entre
paréntesis: «1.5 oz (43 g)», «41 °F (5 °C)», «1,200 sq ft (111 sq m)», «30 lb (13.6 kg)»; tortillas «6 in (15 cm)».

**Lo legal y operativo que SUSTITUYE al ES** (US §6; nunca se traduce el trámite español):
- **Temperatura del al pastor: la pone el CONDADO** (145 °F en unas guías, 155 °F en otras; pollo 165 °F; cortar solo lo
  que ha llegado a temperatura): **NUNCA una cifra única como regla**; «get your health department's vertical broiler
  rules in writing (cook temp, max time on the broiler, leftover cone)».
- FDA Food Code 2022 (cada estado adopta su edición): frío ≤ 41 °F, caliente ≥ 135 °F, recalentado a 165 °F en 2 h; TPHC
  (3-501.19: 4 h / 6 h) **con procedimiento escrito** para la salsa bar; tomate cortado = TCS (pico de gallo, salsas
  frescas); guacamole «treat it as TCS; ask your regulator».
- Type I hood + fire suppression (UL 300) + makeup air sobre griddle, freidora y vertical broilers de gas; trompo de
  carbón = combustible sólido (NFPA 96: escape separado, arrestachispas, ceniza diaria) → variante; «ask the fire marshal
  in writing».
- Plan review (8-201.11) + health permit + pre-opening inspection · building permit + certificate of occupancy · business
  license + sales tax permit · CFPM (2-102.12) + food handler cards según estado.
- 9 alérgenos mayores con sésamo (UK 14): **salsa macha = peanuts + sesame**; flour tortillas = wheat; queso y crema =
  milk; cerveza = wheat/barley. **«Gluten-free» no se promete** (comal y freidora compartidos): «corn tortillas are
  naturally gluten-free; ask about our fryer and griddle».
- **Beer & wine license**: estado + aprobación local, coste y plazos muy distintos: «apply early», **nunca prometerla**;
  liquor liability en el seguro.
- Personal W-2 por horas (nada de 1099 para taqueros o cajeros), ≥ $15/h, propinas del mostrador para el equipo (nunca
  para el dueño o los managers), sin tip credit modelado; SBA 7(a); sales tax 8 % de ejemplo, un solo tipo («some states
  tax to-go food differently», sin cifra).
- Tortilla: **comprada al abrir** (6 in, 360 por caja); la propia con masa harina y prensa se paga a ≈ 660 al día y el caso
  gasta ≈ 650; nixtamal desde el grano = variante sin Excel.

---

## 1. Glosario OBLIGATORIO (US §9, pegado entero)

## 9. Jerga profesional US (glosario OBLIGATORIO de los traductores)

(a) **Nombre**: **«Taco Shop Business Plan Kit»** en landing/H1/ficheros (`taco-shop-business-plan`), «taqueria» como sinónimo en subtítulo y prosa
(«taco shop» 60.500 y «taqueria» 201.000 son ruido de «near me»; las dos colas de plan miden 10). Nunca «Tex-Mex» como sinónimo ni «authentic» como
promesa del producto.

| # | ES taquería | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Taquería | **taco shop** (nombre) · **taqueria** (sin tilde en inglés; prosa y subtítulo) | DFS 60.500 / 201.000; SERP |
| 2 | Trompo / asador vertical | **trompo** (27.100) en carta y prosa · **vertical broiler** (480) en equipo y catálogo · **vertical spit** / «cone» o «stack» para la carne | DFS; webstaurantstore [leída]; guías de condado (resumen) |
| 3 | Taco al pastor | **al pastor** (tacos al pastor; «pastor» solo en jerga de cocina) | DFS 880 «al pastor trompo» |
| 4 | Taquero/a | **taquero** (head taquero); en la plantilla «line cook (trompo & griddle)» | uso del sector (por verificar) |
| 5 | Taco de calle, doble tortilla | **street tacos** (74.000): small corn tortillas, onion & cilantro | DFS |
| 6 | «Con todo» | «**with everything**» / «onion and cilantro» | uso (por verificar) |
| 7 | Orden de 3 | **order of 3 tacos** · **plate** / **combo plate** (with rice & beans) | menú Tucson (resumen) |
| 8 | Gringa · quesadilla | **gringa** (flour tortilla, al pastor & cheese) · **quesadilla** | menús (resumen) |
| 9 | Carnitas · suadero · campechano · cochinita · barbacoa · birria | **carnitas** · **suadero** · **campechano** · **cochinita pibil** · **barbacoa** · **birria** (550.000), **quesabirria**, **consomé** | DFS; uso del sector |
| 10 | Barra de salsas | **salsa bar** (2.400) | DFS |
| 11 | Agua fresca · horchata · jamaica | **aguas frescas** · **horchata** (301.000) · **jamaica (hibiscus)** · tamarindo | DFS; menús |
| 12 | Salsa macha | **salsa macha** (chile oil with peanuts/sesame) — siempre con el alérgeno | KT §5.5 |
| 13 | Nixtamal · masa · harina de maíz nixtamalizado | **nixtamal / nixtamalization** · **masa** · **masa harina** (Maseca) | lector US (resumen) |
| 14 | Comal · plancha | **comal** · **flat-top griddle** («plancha» no) | webstaurantstore [leída] |
| 15 | Tortilladora · prensa | **tortilla machine** (2.400) · **tortilla press** (manual/electric) | DFS; webstaurantstore [leída] |
| 16 | Tortillería | **tortilleria** (sin tilde) | uso |
| 17 | Totopos | **tortilla chips** · **chips & guac** · **chips & salsa** | uso (por verificar) |
| 18 | Mostrador / sin servicio de mesa | **counter service** · **fast casual** · **QSR** | ✅ hermanos |
| 19 | Cubierto equivalente · ticket | **covers** · **average check** (excl. sales tax y tip) | ✅ hermanos |
| 20 | Escandallo por taco · rendimiento | **taco costing** / **food cost per taco** · **yield** (trompo yield, tacos per pound) | ✅ hermanos (recipe costing); «yield» uso |
| 21 | Plataforma · para llevar | **third-party delivery marketplace** · **take-out / to-go / pickup** | ✅ PIZ-US §9 |
| 22 | Manipulador | **food handler card** · **Certified Food Protection Manager (CFPM)** | ✅ PIZ-US §9 |
| 23 | Campana · supresión | **Type I hood** · **fire suppression system (UL 300)** | ✅ REST §5 |
| 24 | Control por tiempo | **time as a public health control (TPHC)** | ✅ PIZ-US §9 |
| 25 | «86» | **86'd** | ✅ PIZ-US §9 |
| 26 | Cerveza mexicana, michelada | **Mexican beer** · **michelada** (solo con beer & wine license) | uso |

(e) **No se traducen literalmente**: «taquería» → **taco shop / taqueria** · «trompo (asador vertical)» → **trompo** (+ «vertical broiler» en equipo) ·
«orden» → **order of 3 / plate** · «barra de salsas» → **salsa bar** · «preparado de carne ≤ 4 °C» → **cold holding ≤ 41 °F** · «63 °C» → **135 °F** ·
«74 °C» → **165 °F** · «ordenanza de humos» → **Type I hood + local fire/mechanical code** · «registro sanitario» → **health permit + plan review** ·
«licencia de apertura» → **business license + certificate of occupancy** · «convenio» → **state/local minimum wage** · «IVA» → **sales tax** ·
«autónomo/SL» → **LLC** · «terraza» → **patio** · «plataforma» → **delivery marketplace** · «guía de equivalencias ES↔LatAm» → según el ES.

**Capas (1) y (2)**: **Taco Shop Business Plan Kit** · slug `taco-shop-business-plan` · `taco-shop-business-plan.docx` «Taco Shop Business Plan (10 Sections)» ·
`taco-shop-financial-projections.xlsx` · `taco-shop-startup-checklist.xlsx` · `taco-cost-trompo-yield-calculator.xlsx` (pestañas `Trompo Yield` / `Proteins` /
`Tortillas` / `Salsa Bar` / `Taco Costing` / `Orders & Channels`; oz↔g, lb↔kg, °F↔°C) · `taco-shop-equivalents-guide.docx` (según ES) · pestaña F2
**«Phase 2 - Hood, Gas & Permits»** (29 car., ≤ 31).

### Términos para la landing (DataForSEO US, 28-oct)

| Keyword | Vol. | Uso |
|---|---|---|
| **taco shop business plan** · taqueria business plan · taco restaurant business plan | 10 · 10 · 10 | slug, H1, title, schema |
| how to open a taco shop · how to start a taco business · how much does it cost to open a taco shop | 10 · 10 · 10 | H2, FAQ |
| mexican restaurant business plan | 20 | cuerpo («not a full-service Mexican restaurant») |
| trompo · vertical broiler · tortilla machine · tortilla press commercial · salsa bar | 27.100 · 480 · 2.400 · 260 · 2.400 | H2 equipo, alt |
| street tacos · birria tacos · horchata | 74.000 · 550.000 · 301.000 | cuerpo, alt (consumidor: no title) |

- **Title** (≈ 108 car.): «Taco Shop Business Plan Template: Word + Excel Projections + Taco Cost & Trompo Yield Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Taco Shop ` + oro `Business Plan` + «Template to Open a Taqueria: Word Plan + Excel Projections + Taco Cost & Trompo Yield Calculator + Startup Checklist».
- **Meta** (≈ 155 car.): «Taco shop business plan template for a counter-service taqueria: Word plan, 3-year Excel projections, taco cost and trompo yield calculator, permit checklist.»
- **H2 (6)**: What's Inside Your Taco Shop Business Plan Kit · How Much Does It Cost to Open a Taco Shop? (Hood, Trompo, Build-Out) · Is a Taco Shop Profitable?
  Real Margins per Taco · Al Pastor on the Trompo: Yield, Food Safety and Your Health Department · DoorDash, Uber Eats and Grubhub: What Delivery Really Costs
  a Taqueria · Corn Tortillas: Buy Them or Make Your Own?
- **Alt**: «Taquero slicing al pastor from the trompo onto corn tortillas» · «Salsa bar with labeled salsas and allergen signs» · «Street tacos with onion, cilantro
  and pineapple». **No prometer** licencia de alcohol, «gluten-free», venta desde casa, una temperatura única para el trompo ni «15-25 %».
  **Keywords** (schema/docProps): taco shop business plan, taqueria business plan, how to open a taco shop, taco shop startup costs, trompo yield, AI Chef Pro.


---

## 2. Tanda (a) — GTAQ-plan + revisión de GR

Entrada `BP12/tandas/GTAQ-plan.entrada.json`: **119 cadenas, ≈ 3,5 K palabras** (72 de texto libre + **47 celdas D19**: 12
filas × 4 salvo A39, que está fijada; sin propuesta) + `revisar_reutilizadas.GR` (**34** cadenas). Salidas:
`BP12/textos_en/GTAQ-plan.json` (TODOS los ids) y `BP12/textos_en/GR.revision.json` (solo las de GR que cambian; `{}` si
ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista o el método; sin el 10/21 % del IVA español: un solo sales
  tax de ejemplo (8 %, B39 = B40 = B63), sin crédito por compras (B41 = 0). **C34**: B34 = 0 (sin carencia). **C60/C61**:
  con 12 pagas no hay pagas extra. **C62/C63** y **A62** están fijadas (POR_CELDA): si las citas, con esas palabras.
- **Notas de `Startup Costs` (col. D, filas 7-24)**: las partidas de US §8 en las filas ES (rótulos ya fijados en
  `fijos_en`: lee el rótulo EN de la fila antes de escribir su nota). **OJO D15 y D19**: la nota ES habla de la campana y
  de la barra de cerveza/café; en el EN esas filas son el **walk-in cooler** y la **beverage station** (beer cooler,
  dispensadores de aguas frescas): escribe la nota del rótulo EN. Rangos solo con fuente de US §4 o ninguno.
- **`3-Year P&L` col. F**: F10 = reparto de la comida de su pista; F11 está fijada; los umbrales del semáforo con los del
  libro EN (margen tras variables ≥ 60 %, mercancía ≤ 30 %, personal ≤ 36 %, alquiler ≤ 10 %, neto ≥ 5 %).
- **`Staffing` col. J**: los puestos de US §8 (rótulos fijados: Owner / head taquero & GM · Taquero / line cook · Prep
  cook · Counter lead / cashier · Counter & expo (part-time W-2) · Dish & prep · Relief cover), con su $/h (19 / 18 / 16 /
  15 / 15); el dueño cobra por debajo de un manager: «owner's draw in addition from net profit». A29 está fijada.
- **`Break-Even` E25**: el techo de rotaciones es **5** (B25): incluye take-out y delivery, que no ocupan plaza (pista).
- **Tabla D19 (`Instructions` 35-46, una cadena por celda, SIN propuesta)**: cada fila la dicta su pista: Benchmark |
  Value | Source | Note, en el orden de las filas del ES. **A39 está fijada** («Vertical broiler (trompo)»): escribe B39-D39
  para ella. Solo lo «[leída]» con fuente; lo «(resumen)» como «Kit estimate» o con «check».
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21 (divide by 1 + your sales tax rate); A10 con el **Mes 1 =
  JANUARY**; A12: el Word usa las cifras de este Excel y la calculadora del kit (Taco Cost & Trompo Yield Calculator)
  escandalla cada taco: su food cost NO se copia en «0. Assumptions».
- **`12-Month Cash Flow`**: O5 está fijada (POR_CELDA, Mes 1 = enero con los pesos US); A34 viene del Bar EN (GM).
- **Revisión de GR** (lista `revisar_reutilizadas.GR`): EN de la Pizza EN o del Bar: confirma que vale para una taquería
  de mostrador y corrige solo lo que no case (nada de pizza, horno, masa de pizza, servers ni «dining room service»).

## 3. Tanda (b) — GTAQ-check + revisión de GRC (las 80 tareas)

Entrada `BP12/tandas/GTAQ-check.entrada.json`: **124 cadenas, ≈ 2,7 K palabras** + `revisar_reutilizadas.GRC` (**102**:
plazos, responsables, cabeceras y tareas que la Pizza EN ya tenía). Salidas: `BP12/textos_en/GTAQ-check.json` (TODOS
los ids) y `BP12/textos_en/GRC.revision.json` (solo las de GRC que cambian; `{}` si ninguna). Molde C2 (OK | TASK |
OWNER | TIMING | NOTES); pestañas fijadas («Phase 1 - Business Setup» · «Phase 2 - Hood, Gas & Permits» · «Phase 3 -
Kitchen & Health» · «Phase 4 - Staff & Allergens» · «Phase 5 - Menu, Brand, Delivery» · «Phase 6 - Opening & 90 Days»);
A1 = «TACO SHOP STARTUP CHECKLIST» y la cabecera de la fase 2 fijadas. Las demás cabeceras de fase (A2) siguen el nombre
de su pestaña con sus semanas.

- **DV**: la lista EN es «✓,☐,N/A»: el texto dice **☐ = pending**, nunca «—».
- **Dos tareas propias obligatorias** (F1-camino §6; regla B2 de la pizza: toda licencia que prometan landing, hub o
  Word tiene su tarea): **beer & wine license** y **las reglas del trompo de tu condado por escrito**. No hay filas
  nuevas: se reescribe una tarea existente. Encaje propuesto (las tareas sin equivalente US se SUSTITUYEN, no se
  traducen):

| Celda | ES | Tarea US propuesta |
|---|---|---|
| F1!B5 | Consulta urbanística previa | Zoning check before signing: restaurant use, hood, seats and patio |
| F1!B6 | Trompo de gas o de carbón ANTES de firmar | Decide gas or charcoal trompo before signing (charcoal = solid fuel: separate exhaust, NFPA 96) |
| F1!B8-B9 | SL o autónomo · constituir | LLC vs S corp with your CPA · form the LLC and get the EIN |
| F1!B10 | Alta censal 036 (IAE 671/673, 677.9) | Business license + **sales tax permit** (state and city) |
| F1!B11 | Alta en la Seguridad Social | State payroll and unemployment registration |
| F1!B12 | Certificado digital | **Apply for the beer & wine license** (state + local) as soon as you sign: it can take months; never open counting on it |
| F1!B14 | Gestoría + Veri\*factu | CPA / bookkeeper + POS that reports sales tax |
| F1!B15 | Plan al banco, dos ofertas | Take the plan to two SBA 7(a) lenders |
| F1!B16 | RC y multirriesgo | General liability + liquor liability + property + workers' comp |
| F2!B5-B7 | Local de 70-90 m² · potencia y gas · conducto | Second-generation space of about 1,200 sq ft (111 sq m) · electrical service and gas capacity · hood and duct route with the mechanical contractor |
| F2!B9 | Contrato con uso de restaurante | Lease with restaurant use, hood rights and a beer & wine license contingency |
| F2!B10-B12 | Proyecto técnico · licencia de actividad · licencia de obra | Architect / MEP drawings with the hood · zoning + certificate of occupancy · building permit |
| F2!B13 | Autorización de la terraza | Patio / sidewalk café permit from the city |
| F2!B14-B15 | Gas por instaladora · conducto y filtro si carbón | Licensed gas contractor + permit and inspection · Type I hood, UL 300 suppression and makeup air (charcoal: solid-fuel rules) |
| F2!B18-B19 | Campana · boletín y certificado final | Fire marshal sign-off of hood and suppression + Class K extinguisher · final inspections and certificate of occupancy |
| F3!B7 | Registro sanitario autonómico | **Plan review** (8-201.11) + health permit application and pre-opening inspection |
| F3!B8 | Cono en cámara a 4 °C | Marinated cones held at 41 °F or below, date-marked |
| F3!B9 | Sonda y hora límite del cono | **Get your county's vertical broiler rules in writing** (cook temp, max time on the broiler, leftover cone) and write your trompo SOP |
| F3!B10-B12 | Salsas crudas ≤ 4 °C · carnitas · barra de salsas | Cut tomatoes and salsas ≤ 41 °F (guacamole: treat as TCS) · hot holding ≥ 135 °F, cooling and reheating to 165 °F · salsa bar: cold holding or TPHC with a written procedure, labels and utensils |
| F3!B13 | Pescado crudo: congelación previa | If you serve ceviche or aguachile: parasite destruction by freezing or a supplier letter (Food Code 3-402.11) |
| F4!B5-B6 | Tabla del convenio · contratos | State and local minimum wage + labor law posters · offer letters, I-9, W-4 and new-hire reporting |
| F4!B8 | Registro de jornada | Time clock in the POS (FLSA records), without «digital obligatorio» |
| F4!B10-B11 | Reparto propio · manipuladores | Own drivers: W-2 + hired & non-owned auto insurance · CFPM + food handler cards |
| F4!B13-B14 | PRL · vigilancia de la salud | OSHA basics (burns, cuts, slips; the trompo knife) · workers' comp and injury log |
| F4!B15-B17 | Alérgenos · cartel · «sin gluten» | 9 major allergens incl. sesame (macha) · allergen signs at the salsa bar · never promise «gluten-free» |
| F5!B7 | IVA de la carta | Sales tax on the menu: one rate in the example; check your state's to-go rules |
| F5!B8-B9 | Llevarse lo que no consume · cobro del envase de plástico | Utensils and napkins on request for to-go orders · your city's packaging ordinance (foam bans, bag fees) |
| F5!B10 | Importador de chiles | Mexican specialty distributor (dried chiles, masa harina) + a backup |
| F5!B14 · B17 | OEPM · SGAE | USPTO trademark search · music licensing (ASCAP/BMI/SESAC) |
| F6!B6 · B10 | DDD · inspección sanitaria | Pest control contract · health inspection: food safety plan and logs at hand |
| F6!B11-B12 | Limpieza de la campana · gas cada 5 años | Hood cleaning schedule (NFPA 96) · fire suppression inspection every 6 months and gas appliance service |

- **Revisión de GRC** (lista `revisar_reutilizadas.GRC`): casi todo plazos («Weeks 3-6»), responsables y tareas comunes
  de la Pizza EN: confirma que valen para una taquería y corrige solo lo que no case (horno, masa de pizza, «flue»,
  servers…).

## 4. Tandas (c) taq_a (§1-5) ‖ (d) taq_b (§6-10)

Lo que se pega a cada subagente: sección 0 de `BP/BRIEF-TRADUCTORES.md` + su bloque «Docx — reglas comunes de las tandas
(d)-(g)» + las secciones **0, 1, 4 y 5** de este fichero. Cada uno lee su entrada y, como FORMA, la misma sección de la
Pizza EN (`BP8/docx_en_piz_a.json` o `docx_en_piz_b.json`); NO toca nada más que su salida y no corre `preparar_tandas`.

| Tanda | Entrada | Párrafos · palabras ES | Salida |
|---|---|---|---|
| (c) taq_a | `BP12/tandas/taq_a.entrada.json` | 29 · 3,295 (§1 Executive Summary · §2 Concept · §3 Market · §4 Competition · §5 Marketing) | `BP12/docx_en_taq_a.json` |
| (d) taq_b | `BP12/tandas/taq_b.entrada.json` | 32 · 4,012 (§6 Operations · §7 Staffing · §8 Financial Plan · §9 Legal · §10 Conclusions) | `BP12/docx_en_taq_b.json` |

- Formato de salida: `{"<i>": "<párrafo EN>", …}` con TODOS los «i» de `parrafos` y nada más; un párrafo por clave, sin
  saltos de línea nuevos; los subtítulos (una línea sin punto final) siguen siendo una línea sin punto final.
- Cada párrafo trae su `nota` (`datos_taq.DOCX_NOTAS`): la sección + la FORMA de la Pizza EN; las 7 de §9 (102-108) fijan
  el tema de cada párrafo (102 marco y permisos · 103 hood y fuego · 104 health permit y Food Code · 105 **al pastor: la
  temperatura la pone el condado** · 106 alérgenos y «gluten-free» · 107 beer & wine license, seguro y personal · 108
  venta desde casa y **la nota UK al final**, que el check exige).
- **Lo que no cruza del Word ES** (IVA partido, art. 4.1 y art. 30, ordenanza de humos de Madrid, ACSA/AESAN, convenio,
  Leyes 1/2025 y 7/2022, Veri\*factu, IAE, tortilla sencilla de 12 cm, 3,00 € el taco) se **sustituye** por el bloque legal
  de §0 y el caso US: street taco de **doble tortilla de 6 in**, $4.00 en carta (Kit estimate); tortilla comprada al
  abrir, la propia a partir de ≈ 660 al día; food cost y su sensibilidad sin inventar cifras.
- **Cifras**: las del plan, SOLO como tokens `{{…}}` de `tokens`. La entrada trae además `cifras_del_caso` (el valor
  final de cada token, leído del Excel EN calibrado) SOLO para que entiendas el caso: **en el texto va el token, nunca la
  cifra** (una pérdida: «a pre-tax loss of {{pesimista_perdida}}»). Importes «$» fuera de tokens solo los de la research
  con su fuente (US §4 y §5: trompos $999-$2,844, Type I hood $5,000-$25,000, Mission 360 por caja $58.99…).
- **Terminología** (manda): covers · counter service · trompo (carta y prosa) / vertical broiler (equipo) · al pastor ·
  street tacos · salsa bar · aguas frescas · taquero · beer & wine · Type I hood · TPHC · CFPM · Month 1 = January ·
  ☐ = pending (checklist). Rótulos que cites (partidas, puestos, pestañas) con las palabras de `fijos_en` /
  `pestanas_es_en` de las entradas de la tanda 1; el Word no promete nada que el Excel no haga.

## 5. Validación (Mac, solo JSON) — el comando EXACTO de cada tanda

Desde la raíz del worktree del Mac. Itera hasta `OK (0 errores, …)` en los comandos de tu tanda y revisa los AVISOS
reales. **No corras `preparar_tandas`** (reescribe ficheros compartidos con la otra tanda): `check_revision.py` valida tu
revisión en un temporal propio.

```bash
istats cpu temp | head -1
# tanda (a)
python3 scripts/productos-digitales/business-plans-en-12/bp12.py check_textos --tanda GTAQ-plan
python3 scripts/productos-digitales/business-plans-en-12/check_revision.py GR
# tanda (b)
python3 scripts/productos-digitales/business-plans-en-12/bp12.py check_textos --tanda GTAQ-check
python3 scripts/productos-digitales/business-plans-en-12/check_revision.py GRC
# tanda (c) — Word §1-5
python3 scripts/productos-digitales/business-plans-en-12/bp12.py check_textos --tanda taq_a
# tanda (d) — Word §6-10
python3 scripts/productos-digitales/business-plans-en-12/bp12.py check_textos --tanda taq_b
```

Responde solo con: ficheros escritos, nº de claves (y de correcciones de la revisión), resultado de los checks y 3-5
decisiones de traducción que deban conocer la otra tanda y las del Word.

**Después (orquestador)**: ver `F2-NOTAS.md` §6 (comandos de la cadena completa).
