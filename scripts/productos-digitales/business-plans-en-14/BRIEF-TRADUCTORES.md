# Brief para los traductores (subagentes Sonnet) — Sushi Restaurant Business Plan Kit (EN)

> Sesión Claude Code, 31-oct-2026 (F2-EN). Fuente de verdad: `../plan-sushi/F1-camino.md` §6-§7 y `F1-research-us-delta.md`
> (US §n). Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del
> Mac, raíz = `/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/6da9d44d-9610-4dc1-9bf3-066bbcb3f10a/scratchpad/wt-sushi-en`):
> `scripts/productos-digitales/business-plans-en-14/` (= `BP14/`, datos y salidas del sushi), `scripts/productos-digitales/
> business-plans-en-12/` (= `BP12/`, el **Taco Shop EN** LIVE: MISMA semilla de libro y MISMA rejilla, celda a celda; es la
> FORMA) y `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas, UNA a la vez** (el Mac se apaga con calor: `istats cpu temp` antes de empezar; si ≥ 62 °C, espera):
> (a) GSUS-plan + revisión de GR → (b) GSUS-check + revisión de GRC → (c) sus_a → (d) sus_b. Las entradas de (c) y (d)
> llevan `cifras_del_caso` (D15 VERDE ya calibrado; no cambian). **No se escriben** GM (360 cadenas: motor común con EN
> limpio del Taco EN, el Rotisserie EN, la Pizza EN, el Bar EN o BP) ni GR / GRC (39 + 97: EN reutilizado del Taco EN que
> **se revisa** en tu tanda): los escribe `bp14.py preparar_tandas`. **El ES ya es FINAL** (F2 ES revisada, `51060183`).

**Cómo usar este brief**: lee la **sección 0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes: idioma, cero español, moneda,
formato US, marca, cifras, pestañas citadas) + las secciones **0, 1 y 5** de este fichero + la de tu tanda (§2, §3 o §4; las
del Word, además, el bloque «Docx — reglas comunes de las tandas (d)-(g)» de `BP/BRIEF-TRADUCTORES.md`). Lo que aquí choque
con el brief común **manda aquí**. No haces commit, **no corres `preparar_tandas`** y no tocas nada más que tus salidas.
**En el Mac no se ejecuta Python** (regla térmica): la validación corre en el VPS con el comando de §5.

---

## 0. Lo que cambia frente al Taco EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP14/tandas/<TANDA>.entrada.json`; `BP14/F1-research-us-delta.md` §1, §4, §5, §6, §8
y §9; como FORMA (registro, longitud), el EN del Taco EN en `BP12/textos_en/{GTAQ-plan,GTAQ-check}.json` y
`BP12/docx_en_taq_{a,b}.json` — la gemela está en la MISMA hoja y celda de `BP12/textos_es.json`. **Su vocabulario de
taquería NO vale** (taco, trompo, al pastor, tortilla, masa, salsa bar, aguas frescas, patio, counter service, 308 days,
$17.50, 1,200 sq ft…).

**Concepto (US §1): INDEPENDENT SUSHI RESTAURANT con SUSHI BAR**, ciudad media de EE. UU. (150-500 mil hab.), ~1,800 sq ft,
**40 plazas (10 en el sushi bar frente al sushi case, 30 en mesas)**, **servicio en mesa con servers W-2 y propinas
aparte**, pickup propio (take-out) y marketplaces. El **head sushi chef (itamae)** a la vista en la barra; cocina caliente
pequeña (tempura, gyoza, miso, teriyaki) bajo **Type I hood**; **arroceras de gas**; walk-in; **freezer de −4 °F con
registrador** para el stock de pescado YA tratado. Carta: nigiri y sashimi, classic rolls (California, spicy tuna),
specialty rolls, hand rolls, poke bowls, appetizers (edamame, gyoza, tempura), **beer, sake & wine**. **Abre 6 días**
(cierra el lunes; 310 días: además Thanksgiving, Christmas Day y New Year's Day). Horario 11:30-14:30 y 17:00-21:30 (22:00
viernes y sábado); el sushi chef entra a las 9:30 (arroz, corte del saku). **En EE. UU. el dueño es el GM y el head sushi
chef es un puesto contratado** (el ES pone al titular de itamae). Variantes (texto de guía, sin Excel): **omakase**
(chef's counter de 10 plazas, 2 turnos, precio fijo y reserva) y **poke / hand roll bar** (counter service). Fuera: grocery
store sushi y quioscos franquiciados (otro negocio), kaiten / conveyor (variante sin Excel), food truck.

**Caso US** (`BP14/cifras_caso.json`; D15 VERDE en la vuelta 0, sin palancas): **115 covers × $32.50 × 310 días =
$1,158,625** · inversión total $385,156 (18 partidas $223,800 + imprevistos por fórmula $13,300 + fianza 2 meses + 2 de
renta previa + fondo de maniobra $130,056) · propios $130,000 + préstamo **$256,000** (SBA 7(a), 10 %, 10 años, sin
interest-only) · margen tras variables 58.5 % · COGS 30.8 % · personal 33.2 % (10 personas = 8.6 FTE) · alquiler 4.7 % ·
EBITDA $182,591 · **neto 8.5 %** el año 1 y 11.4 % el año 3 · equilibrio 93 / 92 covers al día · holgura de caja 26 % · DSCR
mín 3.59× · saldo mínimo $140,937 (Mes 1) · payback 2.3 años · pesimista $883,738 con pérdida de $29,140 · optimista
$1,453,140. **Check de $32.50 por cover equivalente** (US §8): sala **70** covers × **$36.00** (comida $28.50 + bebida
$7.50) · take-out **15.6 pedidos × $41.00** (≈ 25 covers) · marketplace **12.5 pedidos × $46.00** (carta un 15 % más cara y
pedido algo mayor; ≈ 20 covers) → $32.48; **1 order = 1.6 covers**. **Mes 1 = ENERO** (orden del calendario: enero el más
flojo; febrero —Valentine's Day—, mayo —Mother's Day y graduaciones— y diciembre —holiday parties y New Year's Eve
platters— los picos). El ES dice «comensal»; el EN dice **covers** («orders» para take-out y marketplace). Las notas del
libro describen el **método** o usan `valor_us` de tu entrada; **ninguna cifra del ES** (el gate las caza: 79 comensales,
20,00 €, 474.000, 103.350, 300 días, 36 plazas, 14 pagas, 33 %, 17.094, 1.221, 24 % de plataforma, 63 °C…).

**Lo que el check rechaza** (`datos_sus.RX_SUS_NO` + `cifras_prohibidas`): taco / taqueria, trompo / al pastor, tortilla,
salsa bar, mezcal / tequila; **rotisserie, spit(s), family meal, heated display, yuca, huancaina**; pizza, Neapolitan,
dough, VPN, mozzarella; tapas, small plates, **cocktails**, happy hour, **spirits** (salvo «full liquor license» o negado);
IVA, convenio, SMI, autónomo, Veri\*factu, SGAE, IAE, terraza, **comensal / pedido / combinado / vitrina / sushiman /
sushiwoman**, **España / Spain / Spanish** (salvo «Spanish mackerel»), VAT fuera de la nota UK; RD 1021/2022, RD
1086/2020, RD 126/2015, RD 1420/2006, «art. 4.1 / 8.1 / 8.2 / 30 / 30.5», Leyes 1/2025 y 7/2022, AESAN; **«−20 °C … 24 h»
fuera de la nota UK** (la regla US es −4 °F durante 7 días o las de −31 °F); **«sushi-grade» / «sashimi-grade»** salvo para
decir que no tiene definición legal; **authentic**; «gluten-free» salvo negado o con 21 CFR; **«surimi»** (es «imitation
crab»); **«counter service»** salvo en la variante poke / hand roll; «open 7 days / 7 days a week»; kg, g, km, liters, ml,
°C o m² fuera de paréntesis; y los casos EN del Taco (308 days, $17.50), el Rotisserie (130 covers, 360 days), la Pizza (62
covers), la Ice Cream, la Bakery, el Bar ($27), FT y el Restaurant. **Sí valen** (son del caso sushi): 115 covers, 40
seats, $36.00, 95 covers (pesimista), servers, seat turns, closed Mondays, griddle.

**Jerga japonesa** (US §9): el inglés US la usa tal cual y en minúscula: nigiri, sashimi, maki, temaki → **hand roll**,
uramaki → **inside-out roll**, futomaki, neta (topping), shari → **sushi rice (shari)**, sushi-zu → **sushi vinegar**,
saku block, hangiri, omakase, edamame, gyoza, tempura, miso, wasabi, nori, sake. **«itamae» se glosa UNA vez** («the head
sushi chef (itamae)») y luego «head sushi chef»; **«sushiman» nunca** (→ sushi chef); «combinado» → **platter / combo**
(«party platter» si es por encargo); «surimi» → **imitation crab** («kani» o «krab» en carta); «vitrina» → **sushi case**.

**Unidades** (`datos_sus.REGLA_UNIDADES`): lb, oz, fl oz, gallons, °F y sq ft como unidad principal; la métrica entre
paréntesis: «0.5 oz (14 g)», «−4 °F (−20 °C)», «41 °F (5 °C)», «1,800 sq ft (167 sq m)», «50 lb (23 kg)».

**Lo legal y operativo que SUSTITUYE al ES** (US §6; nunca se traduce el trámite español):
- **Parasite destruction** (FDA Food Code 2022 **3-402.11**; cada estado adopta su edición): antes de servir pescado crudo,
  **−4 °F o menos durante 168 h (7 días)**, o **−31 °F hasta sólido + 15 h**, o **−31 °F hasta sólido + −4 °F durante 24 h**.
  **Exentos**: el atún de las especies *Thunnus* (yellowfin, bigeye, bluefin, albacore…) y el **pescado de acuicultura
  alimentado con pienso** (como el salmón) **con declaración escrita** del proveedor o del acuicultor; bivalvos. **Registros
  3-402.12**: tiempo y temperatura de congelación **90 días** después de servir; si congela el proveedor, **supplier letter**
  (acuerdo o declaración escrita). **SOP del kit**: comprar el pescado YA tratado o exento con su carta archivada; el
  freezer de −4 °F con registrador guarda el stock (congelar tú −4 °F × 7 días ocupa mucho freezer). Hamachi de granja,
  caballa (saba), calamar y salvajes: carta del proveedor o congelación propia con registro.
- **Sushi rice** (TCS, *B. cereus*): **(a) TPHC 3-501.19**: hasta **4 h** con la **hora marcada** en cada tanda y
  **procedimiento escrito** para el inspector; a las 4 h **se tira** (no vuelve al frío ni se recalienta) = **el caso por
  defecto**; **(b) variance + HACCP plan** para el arroz acidificado (**3-502.11(C)**; el anexo pone de ejemplo un límite
  crítico de **pH < 4.2**; cada condado fija el suyo, de 4.0 a 4.6, con pH-metro calibrado y registro por tanda; Snohomish
  WA cobra $2,100 de plan review). El kit **NO fija un pH «legal»**: «decide TPHC or variance with your health department
  in writing, before opening».
- **Consumer advisory 3-603.11**: *disclosure* (asterisco o descripción en cada plato crudo) + *reminder* («Consuming raw or
  undercooked … seafood … may increase your risk of foodborne illness»), en la carta, en la web y **en los listados de
  marketplace**.
- **Scombrotoxin (histamina)**: atún, yellowtail/hamachi y caballa: **recepción a ≤ 40 °F** o se rechaza (FDA Fish and
  Fishery Products Hazards and Controls Guidance, cap. 7). Cold holding ≤ 41 °F; pescado del servicio en reach-in a 32-34 °F.
- **«Sushi-grade» / «sashimi-grade» no tienen definición legal**: no se prometen; se habla de «fish handled for raw service
  (frozen per 3-402.11 or exempt, with records)».
- **9 alérgenos mayores** con sésamo (FASTER Act, desde 2023): fish, crustacean shellfish (shrimp, crab), **soy y wheat**
  (soy sauce; tamari solo si la etiqueta lo dice), **sesame** (semillas, aceite), egg (spicy mayo, tamago, rebozado de
  tempura), milk (cream cheese), wheat (tempura, panko; el imitation crab suele llevar almidón de trigo y clara de huevo:
  según etiqueta). **Moluscos y mostaza NO son major en EE. UU.** (sí en UK: nota UK). **«Gluten-free» no se promete** (21
  CFR 101.91).
- **Type I hood** + supresión **UL 300** + makeup air sobre la freidora de tempura, el range y el griddle; limpieza de
  campana **semestral** (NFPA 96, Tabla 11.4); grease interceptor; «ask the mechanical inspector whether the gas rice
  cookers go under the hood». Plan review (**8-201.11**) + health permit + inspección previa · building permit +
  certificate of occupancy · business license + sales tax permit · **CFPM (2-102.12)** + food handler cards según estado.
- **Beer & wine license** (estado + aprobación local; **el sake suele ir con la licencia de vino: «ask your state ABC»**;
  «apply early», **nunca prometerla**); liquor liability y product liability en el seguro.
- Personal **W-2 por horas** (nada de 1099), ≥ $15/h, **propinas de los servers aparte y para el equipo** (nunca para el
  dueño o los managers), sin tip credit modelado; SBA 7(a); **sales tax 8 %** de ejemplo, un solo tipo («some states tax
  to-go food differently», sin cifra).
- **«Every slice counts»** (US §8): el margen está en los rolls y el precio en el pescado; regla del sushi case: cortar por
  servicio, nunca llenarlo «por si acaso»; merma objetivo ≤ 5 % del pescado comprado (Kit estimate). Las cifras por pieza
  las da la **Sushi Fish, Rice & Costing Calculator** del kit (pestañas `Fish Yield` · `Sushi Rice` · `Costing` ·
  `Instructions`): **no inventes porcentajes por pieza**; si hace falta uno, di «the calculator shows…» sin cifra.
- **Ningún producto citado** salvo los del cierre del Word (Food Cost Kit Pro · HACCP Food Safety Kit Pro · Restaurant
  Checklists Kit Pro · Food Cost + Menu Engineering Guide): no hay guía de restaurante japonés ni checklists de sushi en EN.

---

## 1. Glosario OBLIGATORIO

El **§9 de `BP14/F1-research-us-delta.md`** entero (tabla de 16 filas + «(e) No se traducen literalmente» + capas (1) y
(2)): léelo y aplícalo. Además, `glosario` de tu entrada (incluye `datos_sus.GLOSARIO_SUS`). Rótulos que cites (partidas,
puestos, pestañas) con las palabras de `fijos_en` / `pestanas_es_en` de las entradas de la tanda (a)/(b).

---

## 2. Tanda (a) — GSUS-plan + revisión de GR

Entrada `BP14/tandas/GSUS-plan.entrada.json`: **117 cadenas, ≈ 3,7 K palabras** (69 de texto libre + **48 celdas D19**: 12
filas × 4; sin propuesta) + `revisar_reutilizadas.GR` (**39** cadenas del Taco EN). Salidas: `BP14/textos_en/GSUS-plan.json`
(TODOS los ids, `{"<id>": "<EN>"}`) y `BP14/textos_en/GR.revision.json` (solo las de GR que cambian; `{}` si ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista o el método; el ES explica el comensal equivalente (sala
  + pedidos × 1,6) con cifras ES: **en EN, covers** con las cifras US de la pista (C4, C5, C6), **ninguna cifra ES**. Sin el
  10/21 % del IVA español: un solo sales tax de ejemplo (8 %, B39 = B40 = B63), sin crédito por compras (B41 = 0). **C13**: el
  puente del food cost (32 % = consumo real de toda la carta con la merma; el teórico por pieza de la calculadora sale más
  bajo, **sin cifra**). **C34**: B34 = 0 (sin carencia). **C60/C61**: con 12 pagas no hay pagas extra. **C62/C63** y **A62**
  están fijadas (POR_CELDA): si las citas, con esas palabras. **C68** (convenio ES): «state/local minimum wage; this plan
  budgets ≥ $15/h».
- **Notas de `Startup Costs` (col. D, filas 7-24)**: las partidas de US §8 en las filas ES (rótulos ya fijados en
  `fijos_en`: **lee el rótulo EN de la fila antes de escribir su nota**). **OJO D16**: la nota ES habla de la campana; en el
  EN esa fila es el **walk-in cooler (6×8)** (la campana va en la 9 con el Type I hood): escribe la nota del rótulo EN.
  **D14**: el freezer de −4 °F **guarda** el stock tratado (la regla de parásitos es −4 °F 7 días o las de −31 °F; nada de
  «−20 °C 24 h»). Rangos solo con fuente de US §4 o ninguno; nada de precios en € ni de Madrid.
- **`3-Year P&L` col. F**: F10 = reparto de la comida de su pista; F11 está fijada; F13 es fórmula (ya EN); umbrales del
  semáforo del libro EN (margen tras variables ≥ 55 %, mercancía ≤ 33 %, personal ≤ 36 %, alquiler ≤ 10 %, neto ≥ 5 %).
  Notas de los fijos 26-34 con los rótulos fijados (hood cleaning **semestral**; las renovaciones de permisos —CFPM, HACCP
  plan o variance— van con la formación, fila 34).
- **`Staffing` col. J**: los puestos de US §8 en la fila ES de su jornada (rótulos fijados: Owner / GM · Head sushi chef
  (itamae) · Kitchen line cook · Sushi chef · Servers, host & to-go packing (4 × 0.75) · Sushi chef (part-time W-2,
  weekends & dinner peaks) · Dish & prep); cada J lleva su pista con el $/h. A29 está fijada. J21-J24: la cobertura de US §8
  (servicio 7.5 h × 4.5 + producción 3 h × 2).
- **`Break-Even`**: rotación ENCENDIDA (= Taco): techo **3** seat turns (E25: comida, cena y segundo turno de cena el viernes
  y el sábado, estancias de 45-60 min); A28 es fórmula (ya EN).
- **Tabla D19 (`Instructions` 35-46, una cadena por celda, SIN propuesta)**: cada fila la dicta su pista: Benchmark |
  Value | Source | Note, en el orden de las filas (Month 1 · consumer demand · menu prices · cost per piece · salmon yield
  · sushi rice · marketplace commission · sales tax · parasite destruction · sushi rice TPHC/variance · minimum wage · labor
  cost). Solo lo «[leída]» con fuente; lo «(resumen)» como «Kit estimate» o «secondary sources». **Fila 38** (cost per
  piece): «Value» = «theoretical cost of each nigiri, roll and platter by channel» (sin porcentaje).
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21 («divide a menu price by 1 + your sales tax rate»); A10 con el
  **Mes 1 = JANUARY** (sin el agosto español); A12: el Word usa las cifras de este Excel y la calculadora del kit (**Sushi
  Fish, Rice & Costing Calculator**) calcula el coste de cada pieza por canal: su food cost NO se copia en «0. Assumptions».
- **`12-Month Cash Flow`**: O5 está fijada (POR_CELDA); O16 (IVA por línea): «each sales line at ITS rate, read from the
  tax column of the P&L (one 8% rate in the example)», sin artículos de la ley española.
- **Revisión de GR**: EN del Taco EN en la misma celda: confirma que vale para un sushi restaurant con servicio en mesa y
  corrige solo lo que no case (nada de tacos, trompo, patio, counter service).

## 3. Tanda (b) — GSUS-check + revisión de GRC (las 80 tareas)

Entrada `BP14/tandas/GSUS-check.entrada.json`: **123 cadenas, ≈ 3,2 K palabras** + `revisar_reutilizadas.GRC` (**97**:
plazos, responsables, cabeceras y tareas que el Taco EN ya tenía en la misma celda). Salidas:
`BP14/textos_en/GSUS-check.json` (TODOS los ids) y `BP14/textos_en/GRC.revision.json` (solo las de GRC que cambian; `{}`
si ninguna). Molde C2 (OK | TASK | OWNER | TIMING | NOTES); pestañas fijadas («Phase 1 - Business Setup» · «Phase 2 - Hood
& Permits» · «Phase 3 - Raw Fish & Health» · «Phase 4 - Staff & Allergens» · «Phase 5 - Menu, Brand, Delivery» · «Phase 6
- Opening & 90 Days»); A1 = «SUSHI RESTAURANT STARTUP CHECKLIST»; cabeceras de las fases 2 y 3 fijadas; las demás (A2)
siguen el nombre de su pestaña con sus semanas. **DV**: «✓,☐,N/A» (☐ = pending). Responsables US: Owner, Head sushi chef,
Sushi chef, Kitchen line cook, Contractor, Architect / engineer, CPA, Insurance broker… (nunca «Itamae» ni «Sushiman» como
responsable: «Head sushi chef»; «Gestoría» → «CPA / bookkeeper»).

**Tareas propias obligatorias** (F1-camino §6; regla B2: toda regla que prometan landing, hub o Word tiene su tarea): **decide
TPHC or variance for sushi rice with your health department** (F3!B13), **file supplier parasite letters and aquaculture
statements (keep 90 days)** (F3!B9), **consumer advisory on the menu and marketplace listings** (F3!B10), **receiving log:
reject tuna above 40 °F** (F3!B12) y la **beer & wine license** (F1, ya en GRC: confírmala; el sake con la de vino). No hay
filas nuevas: se reescribe la tarea existente. Encaje propuesto (las que no tienen equivalente US se SUSTITUYEN):

| Celda | ES | Tarea US propuesta |
|---|---|---|
| F1!B5 | Consulta urbanística: extracción, potencia y aforo | Zoning check before signing: restaurant use, Type I hood route, electrical service and seats |
| F1!B6 | Decidir el formato antes de firmar | Decide your format before signing the lease: sushi bar + tables with take-out, or omakase counter |
| F1!B7 | Cómo cumplirás el anisakis | Decide how you will meet the parasite rule: buy fish already frozen or exempt (supplier letters) or freeze it yourself (−4 °F for 7 days, logged) |
| F1!B10 | Alta censal 036 (IAE) | Business license + **sales tax permit** (state and city) |
| F1!B16 | RC y multirriesgo con avería del frío | General, product and liquor liability + property with refrigeration breakdown (spoilage) cover |
| F2!B5 | Local de 90-100 m² | Second-generation restaurant space of about 1,800 sq ft (167 sq m) with a route for the Type I hood |
| F2!B6 | Potencia para cocina eléctrica | Check the electrical service and the gas line for rice cookers, fryer, walk-in and sushi case |
| F2!B9 | Contrato con uso y humos | Lease with restaurant use, hood rights and a beer & wine license contingency |
| F2!B10 · B13 | Proyecto técnico · conducto a cubierta | Architect / MEP drawings and plan review submittal · Type I hood, UL 300 fire suppression and makeup air (permit and fire marshal sign-off) |
| F2!B14-B15 | Obra lavable · cuarto frío y zona de pescado | Build-out with smooth, cleanable surfaces (sushi bar, kitchen, dining room) · walk-in and a fish prep area separate from the cutting station |
| F2!B17-B18 | Campana · zona de empaquetado | Hood over the fryer, range and griddle (ask whether the gas rice cookers go under it) · to-go packing station by the door |
| F3!B5 | Comprar congelador, vitrina, arroceras | Buy NSF-listed equipment: freezer (−4 °F or colder) with temperature logger, refrigerated sushi case and gas rice cookers |
| F3!B6 · B7 | Registro sanitario · APPCC del anisakis | Plan review approval, health permit and pre-opening inspection · written food safety plan with raw-fish (parasite) and sushi-rice controls |
| F3!B8 · B9 | Registro por lote · documento del proveedor | Freezing log by lot, kept 90 days, if you freeze in-house · **file supplier parasite letters and aquaculture statements (keep 90 days)** |
| F3!B10 | Cartel o carta del anisakis | **Consumer advisory (disclosure + reminder) on the menu, website and marketplace listings** |
| F3!B11 · B12 | Pescado 0-4 °C · recepción y atún | Fish held at 41 °F or below (32-34 °F in the reach-in); thaw under refrigeration · **receiving log: reject tuna, yellowtail and mackerel above 40 °F** |
| F3!B13 · B14 | Shari validado o refrigerado · pH por tanda | **Decide TPHC or variance for sushi rice with your health department, in writing** · if variance: pH of every batch with a calibrated pH meter, logged (TPHC: time-stamp every batch, discard at 4 h) |
| F3!B15 | Cocina caliente a 63 °C | Hot kitchen: gyoza, tempura and miso held at 135 °F or above; cool and reheat per Food Code |
| F3!B17 · B18 | Fichas con alérgenos · etiqueta de bandejas | Recipe cards per piece with the 9 major allergens (sesame, soy, wheat, egg, milk, fish, shellfish) · label prepackaged to-go platters (3-602.11) |
| F4!B6 | Contratar itamae y sushiman antes de la obra | Hire the head sushi chef and the sushi chef BEFORE the build-out |
| F4!B11-B12 | Manipuladores con pescado crudo · formación de barra | CFPM + food handler cards, with raw-fish handling · sushi bar training: cutting, ounces of neta and sushi rice per piece |
| F4!B16-B17 | Matriz de 14 alérgenos · «sin gluten» | Allergen matrix (9 major in the US) with fish, shellfish, sesame and the soy sauce wheat · never promise «gluten-free» (21 CFR 101.91) |
| F5!B5-B7 | Carta corta y menú del día · escandallo · IVA | Short menu (about 35 items) and lunch specials · cost per piece and per platter by channel (calculator) · sales tax on the menu: one rate; check your state's to-go rules |
| F5!B8 | Envases (Ley 1/2025) | To-go packaging that meets your local ordinances (some cities ban polystyrene) |
| F5!B9-B11 | Dos proveedores de pescado · arroz y nori · temporadas | Two fish suppliers with their parasite letters · sushi rice, nori and sauces supplier with spec sheets · fish seasonality and price alerts from your suppliers |
| F5!B12 · B14 | Plataformas con techo · alérgenos y frío del pedido | Marketplace contracts with a share cap · allergens before ordering and cold chain for to-go (consumer advisory in the listing) |
| F5!B15-B16 | Marca OEPM, web · Google y fechas | Trademark search (USPTO), brand, photos and website with menu and allergens · Google Business Profile, Yelp, Instagram and peak dates (Valentine's Day, Mother's Day, New Year's Eve platters) |
| F6!B11-B13 | Mantenimiento · calibración del pH-metro · rendimiento | Refrigeration, freezer and semiannual hood cleaning · calibrate the pH meter (variance only) · measure salmon yield and real ounces per piece, and recalculate (calculator) |
| F6!B14 | Fechas fuertes y agosto | Schedule and stock for peak dates (Valentine's Day, Mother's Day, graduations, New Year's Eve platter pre-orders) |

- **Revisión de GRC**: casi todo plazos («Weeks 3-6»), responsables y tareas comunes del Taco EN: confirma que valen y
  corrige solo lo que no case (trompo, tortilla, salsa bar, patio, «taquero», counter service…).

## 4. Tandas (c) sus_a (§1-5) y (d) sus_b (§6-10)

Lee además el bloque «Docx — reglas comunes de las tandas (d)-(g)» de `BP/BRIEF-TRADUCTORES.md` y, como FORMA, la misma
sección del Taco EN (`BP12/docx_en_taq_a.json` o `docx_en_taq_b.json`).

| Tanda | Entrada | Párrafos · palabras ES | Salida |
|---|---|---|---|
| (c) sus_a | `BP14/tandas/sus_a.entrada.json` | 29 · 3,207 (§1 Executive Summary · §2 Concept · §3 Market · §4 Customer · §5 Marketing) | `BP14/docx_en_sus_a.json` |
| (d) sus_b | `BP14/tandas/sus_b.entrada.json` | 32 · 4,197 (§6 Operations · §7 Staffing · §8 Financial Plan · §9 Legal · §10 Roadmap) | `BP14/docx_en_sus_b.json` |

- Formato de salida: `{"<i>": "<párrafo EN>", …}` con TODOS los «i» de `parrafos` y nada más; un párrafo por clave, sin
  saltos de línea nuevos; los subtítulos (una línea sin punto final) siguen siendo una línea sin punto final.
- Cada párrafo trae su `nota` (`datos_sus.DOCX_NOTAS`): la sección + la FORMA del Taco EN; las 7 de §9 (102-108) fijan el
  tema de cada párrafo (102 marco y permisos · 103 hood, fuego, health permit y CFPM · 104 **pescado crudo: parasite
  destruction, supplier letters, histamina** · 105 **sushi rice (TPHC o variance) y consumer advisory** · 106 alérgenos y
  «gluten-free» · 107 beer & wine license (sake), seguro, personal y propinas · 108 venta desde casa y **la nota UK al
  final**, que el check exige).
- **Lo que no cruza del Word ES** (IVA partido, RD 1021/2022 y su −20 °C 24 h, RD 1086/2020 art. 30.5, RD 126/2015, la
  ordenanza de Madrid, IAE, convenio, SMI, 14 pagas, Leyes 1/2025 y 7/2022, Veri\*factu, el menú del día español, agosto como
  mes flojo, las franquicias españolas, el local de 95 m² y las 36 plazas, la Guía Restaurante Japonés y el Kit de Tareas
  Sushi Bar) se **sustituye** por el bloque legal de §0 y el caso US.
- **Cifras**: las del plan, SOLO como tokens `{{…}}` de `tokens` (usa **`{{cogs_pct_xl}}`** y **`{{plantilla_jornadas_xl}}`**,
  que redondean como Excel). La entrada trae `cifras_del_caso` SOLO para que entiendas el caso: **en el texto va el token,
  nunca la cifra** (una pérdida: «a pre-tax loss of {{pesimista_perdida}}»). Importes «$» fuera de tokens solo los de la
  research con su fuente (US §4 y §5: sushi case Hoshizaki $4,045, walk-in $12,808, Calrose $1.04/lb, nori $0.31 la hoja,
  imitation crab $1.80/lb, carta nigiri $5-7 el par, classic $7-9, specialty $13-18, sashimi $28-65; IBISWorld 17,301
  negocios; Indeed sushi chef $20.72/h; FinModelsLab $99…). **Ningún porcentaje por pieza** (los da la calculadora).
- **Terminología** (manda): covers · sushi restaurant · sushi bar · head sushi chef (itamae, una vez) · sushi chef · sushi
  case · neta · sushi rice (shari) · saku block · nigiri · sashimi · maki · inside-out roll · hand roll · classic / specialty
  roll · platter · imitation crab · take-out · pickup · delivery marketplace · beer, sake & wine · Type I hood · parasite
  destruction · supplier letter · TPHC · variance · HACCP plan · consumer advisory · CFPM · Month 1 = January.

## 5. Validación — en el VPS, el comando EXACTO de cada tanda

Escribe tus salidas en el Mac (rutas de §2-§4), cópialas al VPS y valida allí (el Mac no ejecuta Python). Itera hasta
`OK (0 errores, …)` y revisa los AVISOS reales. **No corras `preparar_tandas`**.

```bash
W=/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/6da9d44d-9610-4dc1-9bf3-066bbcb3f10a/scratchpad/wt-sushi-en
B=scripts/productos-digitales/business-plans-en-14; R=/root/wt-sushi-en; PY=/root/venv-guias/bin/python
# tanda (a)
scp -q $W/$B/textos_en/GSUS-plan.json $W/$B/textos_en/GR.revision.json vps:$R/$B/textos_en/ && \
  ssh vps "cd $R/$B && $PY bp14.py check_textos --tanda GSUS-plan; $PY check_revision.py GR"
# tanda (b)
scp -q $W/$B/textos_en/GSUS-check.json $W/$B/textos_en/GRC.revision.json vps:$R/$B/textos_en/ && \
  ssh vps "cd $R/$B && $PY bp14.py check_textos --tanda GSUS-check; $PY check_revision.py GRC"
# tanda (c)
scp -q $W/$B/docx_en_sus_a.json vps:$R/$B/ && ssh vps "cd $R/$B && $PY bp14.py check_textos --tanda sus_a"
# tanda (d)
scp -q $W/$B/docx_en_sus_b.json vps:$R/$B/ && ssh vps "cd $R/$B && $PY bp14.py check_textos --tanda sus_b"
```

Responde solo con: ficheros escritos, nº de claves (y de correcciones de la revisión), resultado de los checks y 3-5
decisiones de traducción que deban conocer las otras tandas.

**Después (orquestador)**: ver `F2-NOTAS.md` §6 (comandos de la cadena completa).
