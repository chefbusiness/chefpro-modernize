# Brief para los traductores (subagentes Sonnet) — Ice Cream Shop Business Plan Kit (EN)

> Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a: preparado; **no se ha traducido nada**). SPEC delta D186-D215 y **§0,
> regla de jerga**. Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas
> (worktree del Mac): `scripts/productos-digitales/business-plans-en-10/` (= `BP10/`, datos y salidas de la heladería),
> `scripts/productos-digitales/business-plans-en-8/` (= `BP8/`, la **Pizza Shop EN** cerrada: mismo código y molde, la
> FORMA) y `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GICE-plan + revisión de GR ‖ (b) GICE-check + revisión de GRC** (paso 2, AHORA) →
> **tanda 2 = (c) ice_a ‖ (d) ice_b** (paso 3: las entradas ya existen, pero el orquestador las regenera antes).
> **No se escriben** GM (369 cadenas: motor común con EN limpio de la Pizza EN, el Bar EN o BP) ni GR / GRC (14 + 73:
> EN reutilizado de la Pizza EN, la Bakery EN o REST que **se revisa** en tu tanda): los escribe `bp10.py preparar_tandas`.
> **El ES ya es FINAL y LIVE** (no hay paso 1c): los ids de las entradas son los definitivos.

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0, 1 y 5** de este
fichero (la 1 es el glosario de research §9 completo, OBLIGATORIO; la 5, la validación) + la de su tanda (§2, §3 o §4). Lo
que aquí choque con el brief común **manda aquí** (en particular: el comando de validación es el de §5, con `bp10.py`, no
`check_textos.py` a pelo). El subagente no hace commit, **no corre `preparar_tandas`** y no toca nada más que sus salidas.

---

## 0. Lo que cambia frente al brief de la Pizza EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP10/tandas/<TANDA>.entrada.json`; `BP10/SPEC-delta.md` (D186-D215);
`BP10/F1-research-us-delta.md` §1, §4, §5, §6 y §8 (el §9 ya va pegado abajo); como FORMA (registro, longitud, fuentes
comunes), el EN de la Pizza EN en `BP8/textos_en/{GPIZ-plan,GPIZ-check}.json` (muchas celdas de la heladería son la
misma celda de la pizza con otro negocio: busca la gemela por hoja y celda en `BP8/textos_es.json`). **Su vocabulario
de pizzería NO vale** (pizza, oven, dough, covers, beer & wine, Neapolitan, flue, hood…).

**Concepto (D189): ICE CREAM SHOP de barrio que HACE su helado en el local** (batch freezer a la vista), ciudad media de
EE. UU. (150-300 mil hab.), ~1,000 sq ft (sala de producción ~250 sq ft), dipping cabinets de 18 sabores (10-12 en
invierno), 20 plazas + patio de 5 mesas en temporada; scoops (cup / cone), sundaes, pints y quarts hand-packed, ice cream
cakes por encargo, café y hot chocolate, catering. Abierto todo el año: cierra 3 semanas en enero, Thanksgiving,
Christmas y los lunes de noviembre a febrero. El dueño es el ice cream maker y el GM. **«Ice cream shop»** en nombres y
títulos; «ice cream parlor», «scoop shop» y «creamery» como sinónimos en prosa; **«gelato» solo como estilo, nunca como
nombre del negocio**. Volumen = **customers** (cada persona que compra; nunca «covers» ni «transactions»). Fuera (y así
lo dicen las FAQ): soft serve / frozen yogurt, ice cream truck (→ Food Truck Business Plan Kit), franquicia, quiosco
sin producción, venta desde casa.

**Modelo de producción (D190, decidido por el orquestador: NO se discute)**: el caso **COMPRA una base pasteurizada**
(ice cream base / mix, 12-14 % butterfat) a una central láctea con licencia y la manteca en el local: recibir la base a
41 °F o menos → aromatizar e incluir mix-ins → batch-freeze (draw a 16-19 °F) → endurecer a 0 °F o menos → dipping
cabinet a 6-10 °F. Regla de seguridad del caso: **«after the dairy's pasteurization you add only flavorings and mix-ins:
no raw eggs, no raw milk or cream; custard flavors need a custard base»**. **Pasteurizar tu propia mezcla es la
VARIANTE** (sin Excel): batch pasteurizer ≈ $25,000-45,000 («get quotes») + licencia estatal de dairy plant / frozen
dessert manufacturer + equipo 3-A + inspecciones; en la variante, grasas, yemas y emulsionantes ANTES de pasteurizar
(155 °F 30 min / 175 °F 25 s, Ohio 901:11-3-05). Todo lo que el ES dice de «pasteurizar a 85 °C», «madurar la mezcla a
4 °C», «huevo a 70 °C» o «el pasteurizador de 30 litros» **se reescribe al modelo de base comprada** (o, si la cadena
compara modelos, a la variante). La licencia **siempre** «depends on your state: ask your state department of
agriculture» (Vermont y Georgia leídas; Arizona, Massachusetts y Pennsylvania en resumen); **nunca «no license needed»
ni una tarifa**.

**Caso US** (`BP10/F2-NOTAS.md` §3; D191, D15 VERDE en la vuelta 0, sin palancas): 165 customers × **$7.50** × 310
días = **$383,625** · CAPEX $204,100 (las 19 partidas de D193 = $186,000 + fianza de 2 meses + 2 meses de renta previa +
imprevistos por fórmula $8,100) + fondo de maniobra $52,771 = **$256,871** · propios $95,000 (37 %) + préstamo
**$162,000** (SBA 7(a), 10 %, 10 años, sin interest-only) · margen tras variables 68.2 % · COGS 22.3 % · personal 33.4 %
(6 personas = 3.05 FTE) · prime cost 55.7 % · alquiler 7.8 % · EBITDA 17.4 % · **neto 5.6 %** el año 1 y 8.6 % el año 3
(y no el «10-25 %» de la SERP: IBISWorld ≈ 5.5 %) · equilibrio 147 / 140 customers al día · holgura de caja 18 % · DSCR
mín 2.26× · saldo mínimo $46,060 (Mes 1). **Mes 1 = MARZO** (pico en julio = Mes 5; valle en enero = Mes 11). Las notas
del libro describen el **método** o usan `valor_us` de tu entrada; **ninguna cifra del ES** (el gate las caza, en € y en
$: 143 clientes, 4,90, 217.217, 14 pagas, 33 %, 17.094, 644.4, 676, 430 g, −18 °C como regla, 3 % de delivery…).

**Lo que el check rechaza** (`datos_ice.RX_ICE_NO` + `cifras_prohibidas`): pizza, dough (salvo «cookie dough»), oven,
Neapolitan, VPN, firewood / wood-fired, beer & wine, «covers per day», flue; bread, bakery, baker, loaf, «transactions
per day»; tapas, cocktails, happy hour; IVA, IAE, autónomo, convenio, SMI, Veri\*factu, RGSEAA, SGAE, terraza, helader-,
mantecad-, carné, RD 618/1998, 1021/2022, crepes, turrón, comunión, España / Spain, VAT fuera de la nota UK; «pasteuriz-»
fuera de la base comprada o la variante (pasa con «dairy», «licensed», «your own mix», «variant», «license»,
«pasteurized base / mix», «155 °F»…); «85 °C» / «185 °F»; «gelato shop / gelateria / artisan gelato»; «no license
needed»; «allergen-free» salvo negado («never promise allergen-free»); kg, km, liters, °C, m² o g/l fuera de
paréntesis; y los casos EN de la Pizza (62 covers, $36…), la Bakery (210 transactions…), el Bar, FT y el Restaurant.

**Unidades** (`datos_ice.REGLA_UNIDADES`, D14): °F, sq ft, gallons / quarts / pints y lb como unidad principal; la
métrica entre paréntesis: «0 °F (−18 °C)», «41 °F (5 °C)», «1,000 sq ft (93 sq m)», «3 gallons (11 liters)»; la densidad
legal del helado en **lb per gallon** («4.5 lb per gallon»), nunca «430 g/l».

**Claims que no se hacen** (D203): «homemade» / «house-made» / «small-batch» solo si se hace en el local («made here in
small batches from a local dairy's base»); «ice cream» y «frozen custard» solo si la receta cumple 21 CFR 135.110
(«ice cream» ≥ 10 % milkfat y ≥ 4.5 lb/gal; frozen custard 1.4 % egg yolk solids); de «gelato» no afirmes que no hay
estándar federal («if you call it ice cream, the federal standard applies»); nunca «allergen-free» (scoops y dipper
wells compartidos); sales tax: «the scoop is taxed as prepared food; packaged pints and whole cakes may be taxed as
groceries in some states (Texas, for example): check your state»; jóvenes de 14-15 años solo con horario FLSA (29 CFR
570.35); nunca prometer márgenes de la SERP.

---

## 1. Glosario OBLIGATORIO (research §9, pegado entero)

## 9. Jerga profesional US (glosario OBLIGATORIO de los traductores)

(a) **Nombre**: **«Ice Cream Shop Business Plan Kit»** en landing/H1/ficheros (`ice-cream-shop-business-plan`); «ice cream
parlor» y «scoop shop» como sinónimos en prosa; **«gelato» solo como estilo** (menos grasa y overrun, se sirve más caliente),
nunca en el nombre (10/mes). «Homemade ice cream shop» en el subtítulo (2.400/mes), sin prometer «homemade» si no se fabrica.

| # | ES heladería | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Heladería artesanal | **ice cream shop** · ice cream parlor · **scoop shop** (4.400, oficio) · **creamery** (40.500; nombre común de tiendas que fabrican) | DFS 24/27-oct; ✅ glosario |
| 2 | Mantecadora · mantecar | **batch freezer** (590) · **batch-freeze / churn**; extracción = **draw** (16-19 °F) | DFS; ✅ glosario |
| 3 | Mezcla base | **ice cream base / mix** (base 2.400 · mix 3.600) · **butterfat** · «14 % base» | DFS; Upstate Farms (resumen) |
| 4 | Pasteurizador (variante) | **batch pasteurizer** · «vat pasteurization» (155 °F 30 min) · **HTST** | Ohio 901:11-3-05 [leída] |
| 5 | Maduración | **aging the mix** (36-39 °F) | ✅ glosario |
| 6 | Abatidor · abatir | **hardening cabinet** / **blast freezer** · **harden** | ✅ glosario |
| 7 | Vitrina de cubetas · cubeta | **dipping cabinet** (gelato: **gelato case**) · **tub** (3 gal) / **pan** (gelato) | DFS 320; KaTom/Ojeda «3-gallon tubs» (resumen) |
| 8 | Lavaporcionador | **dipper well** (agua corriente, 3-304.12(D)) | DFS 1.000; ✅ ICK |
| 9 | Porcionador · espátula | **scoop** (dipper) · **spade** | ✅ glosario |
| 10 | Rendimiento de aire | **overrun** (210) | ✅ glosario (21 CFR 135.110: ≥ 4.5 lb/gal) |
| 11 | Tarrina para llevar | **pint** · **quart** · **hand-packed** · envasar = **pack-out** | DFS «ice cream pints» 4.400; ✅ glosario |
| 12 | Cucurucho · barquillo | **cone** (**waffle cone**, sugar cone, cake cone) · **waffle cone iron/maker** (9.900) | DFS |
| 13 | Copa | **sundae** (40.500) · **cup** | DFS |
| 14 | Inclusiones · variegato · virutas | **mix-ins** · **swirl / ripple** · **sprinkles** | ✅ glosario |
| 15 | Mantecado (≥ 4 % yema) | **frozen custard** (33.100; 1.4 % egg yolk solids) | 21 CFR 135.110 [leída] |
| 16 | Tarta helada | **ice cream cake** (135.000) | ✅ glosario |
| 17 | Sabor de prueba | **sample** con **tasting spoon** | ✅ glosario |
| 18 | Dependiente/a | **scooper** / counter staff · **shift lead** | ✅ glosario |
| 19 | Maestro heladero | **ice cream maker** (owner/operator) | ✅ glosario |
| 20 | Fijo discontinuo de temporada | **seasonal part-time (W-2)** | §6.5 |
| 21 | Temporada alta · reapertura | **peak season** (Memorial Day → Labor Day) · **Opening Day** · **off-season** | ✅ glosario |
| 22 | Licencia de obrador | **frozen dessert license** / **dairy plant / milk handler license** (estatal) + **health permit** local | §6.1 |
| 23 | Elaboración propia / artesano | **made here in small batches** · **homemade** / **house-made** (solo si es verdad) | §6.2 |
| 24 | Seguro de mercancía por avería | **equipment breakdown** con **food spoilage** | ✅ glosario |
| 25 | Ticket medio | **average check per person** (excl. sales tax) | ✅ hermanos |
| 26 | IVA · terraza | **sales tax** · **patio / sidewalk café** | ✅ hermanos |

(e) **No se traducen literalmente**: «helado crema/mantecado/sorbete» (RD 618) → los nombres US de 21 CFR 135 (ice cream, frozen
custard, sherbet ❌ no abierto, sorbet sin estándar leído) · «644.4/676, declaración responsable» → business license + zoning +
building permit/CO · «registro sanitario autonómico / RGSEAA» → health permit + plan review / licencia estatal de frozen dessert ·
«fijo discontinuo, convenio, SMI» → seasonal W-2, state/local minimum wage · «−18 °C» → **0 °F** · «430 g/l» → **4.5 lb/gal** ·
«IVA 10 %» → sales tax · «autónomo/SL» → LLC · «manipulador» → food handler card + CFPM · «crepera/gofrera con salida de humos» →
**waffle cone irons** (sin humos; las crepes no cruzan: en invierno, cakes, pints y chocolate caliente) · «turrón helado de
Navidad» → **holiday pies and cakes** · «comuniones» → **birthdays and graduations**.

**Capas (1) y (2)**: **Ice Cream Shop Business Plan Kit** · slug `ice-cream-shop-business-plan` · `ice-cream-shop-business-plan.docx`
«Ice Cream Shop Business Plan (10 Sections)» · `ice-cream-shop-financial-projections.xlsx` · `ice-cream-shop-startup-checklist.xlsx`
+ bonus común `hospitality-equivalents-us-uk-canada-australia.docx`.

### Términos para la landing (DataForSEO US, 24/27-oct)

| Keyword | Vol. | Uso |
|---|---|---|
| **ice cream shop business plan** · ice cream parlor business plan · ice cream business plan · template | 320 · 320 · 170 · 20 | slug, H1, title, keywords |
| opening an ice cream shop · how to open an ice cream shop · how to start an ice cream business | 320 · 170 · 140 | H2, FAQ |
| cost to open an ice cream shop · ice cream shop profit margin · is an ice cream shop profitable | 50 · 50 · 40 | H2, FAQ |
| ice cream shop equipment · batch freezer · dipping cabinet · blast freezer · dipper well | 1.000 · 590 · 320 · 1.900 · 1.000 | H2 equipo, alt |
| homemade ice cream · frozen custard · ice cream cake · ice cream pints · creamery | 40.500 · 33.100 · 135.000 · 4.400 · 40.500 | cuerpo, glosario |

- **Title** (≈ 95 car.): «Ice Cream Shop Business Plan Template: Word + Excel Financial Projections + Startup Checklist | AI Chef Pro».
- **H1 (Forma B)**: `Ice Cream Shop ` + oro `Business Plan` + «Template to Open a Homemade Ice Cream Shop: Word Plan + Excel
  Projections with Seasonality + 80-Task Startup Checklist».
- **Meta** (≈ 155 car.): «Ice cream shop business plan template: Word plan, 3-year Excel projections with summer seasonality, dairy
  license guide and an 80-task opening checklist. $39, instant download.»
- **H2 (6)**: What's Inside Your Ice Cream Shop Business Plan Kit · How Much Does It Cost to Open an Ice Cream Shop? (Batch Freezer,
  Cabinets, Build-Out) · Is an Ice Cream Shop Profitable? Real Margins vs the 10-25% Claims · Buy a Base or Make Your Own Mix?
  Dairy Licenses by State · Seasonality: Open in March and Get Through the Winter · Sales Tax, Teen Scoopers and Permits.
- **Alt**: «Scooper serving a double scoop from an 18-flavor dipping cabinet» · «Batch freezer extruding fresh ice cream into a
  tub» · «Hand-packed pints and an ice cream cake for the holidays». **Keywords** (schema/docProps): ice cream shop business plan,
  ice cream parlor business plan, how to open an ice cream shop, ice cream shop startup costs, batch freezer, AI Chef Pro.
  **No prometer**: «no license needed», «homemade» con base sin aromatizar en el local, «10-25 % net», «gelato» como nombre,
  «organic/all-natural», precios de bola como benchmark US.

---

## 2. Tanda (a) — GICE-plan + revisión de GR

Entrada `BP10/tandas/GICE-plan.entrada.json`: **131 cadenas, ≈ 3,1 K palabras** (79 de texto libre + **52 celdas D19**: 13
filas × 4, sin propuesta) + `revisar_reutilizadas.GR` (**14** cadenas). Salidas: `BP10/textos_en/GICE-plan.json`
(TODOS los ids) y `BP10/textos_en/GR.revision.json` (solo las de GR que cambian; `{}` si ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista (D191) o el método; sin el 10/21 % del IVA español: un
  solo sales tax de ejemplo (8 %, B39 = B40 = B63), sin crédito por compras (B41 = 0). **C34**: B34 = 0 (sin carencia).
  **C60/C61**: con 12 pagas no hay extras (July = Month 5, December = Month 10). Las notas `C62`/`C63` ya están fijadas
  (POR_CELDA): si las citas, con esas palabras.
- **Notas de `Startup Costs` (col. D, filas 7-25 salvo la 12)**: las partidas de D193 (rótulos ya fijados en `fijos_en`);
  rangos solo con fuente de research §4 o ninguno. **La D12 está fijada** (POR_CELDA: base comprada; el pasteurizador
  es la variante). D13: «a 20-qt Carpigiani lists at about $40,800; get two quotes; reconditioned units cost less». D14:
  endurecer a 0 °F o menos. D15: storage freezers a 0 °F o menos (sin armario de maduración: la base llega madura). D17:
  6-10 °F según el fabricante. D18: dipper wells de agua corriente y waffle cone irons (sin crepera ni salida de humos).
  D20: POS que reporta el sales tax. D24: LLC, legal, permits y food safety plan (sin registro autonómico).
- **`3-Year P&L` col. F**: F10 = el reparto del helado de su pista (scoops / pints / cakes / catering / delivery); los
  umbrales F51-F56 con D196 (65 / 25 / 35 / 10 / 5 %).
- **`Staffing` col. J**: los puestos de D194 (rótulos fijados); seasonal part-time W-2 (nunca «fijo discontinuo» ni art.
  16 ET); la J22 son **2.0 h sin pasteurizar ni madurar**.
- **Tabla D19 (`Instructions` 35-47, 52 celdas, una por celda, SIN propuesta)**: cada fila la dicta su pista (D196):
  Benchmark | Value | Source | Note, en el orden de las filas del ES. Solo lo «[leída]» con fuente; lo «(resumen)» con
  «check» o como «Kit estimate». La fila 41 es la ÚNICA de la tabla donde cabe «pasteurized base / your own mix» con
  Vermont y Georgia.
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21 (divide by 1 + your sales tax rate); A10 con el **Mes 1 = MARCH**;
  A12: el Word usa las cifras de este Excel.
- **`12-Month Cash Flow`**: O5, A34 y O20 están fijadas (POR_CELDA, Mes 1 = marzo); O13 = 12 pagas y el aviso de que los
  seasonal solo cobran en temporada (el invierno sale más caro que la realidad: prudente).
- **Revisión de GR** (lista `revisar_reutilizadas.GR`): EN de la Pizza EN (C18, C30, C31, A51, F33, F34, J10…) o de la
  Bakery: confirma que vale para una heladería y corrige solo lo que no case (p. ej. A51 «dining room seats» → «indoor
  seats»; F33 «HACCP-based» puede quedarse; nada de pizza ni de pan).

## 3. Tanda (b) — GICE-check + revisión de GRC (las 80 tareas, D199)

Entrada `BP10/tandas/GICE-check.entrada.json`: **157 cadenas, ≈ 2,4 K palabras** + `revisar_reutilizadas.GRC` (**73**:
plazos, responsables, cabeceras y tareas que la Pizza EN ya tenía). Salidas: `BP10/textos_en/GICE-check.json` (TODOS los
ids) y `BP10/textos_en/GRC.revision.json` (solo las de GRC que cambian; `{}` si ninguna). Molde C2 (OK | TASK | OWNER |
TIMING | NOTES); pestañas ya fijadas («Phase 1 - Business Setup» · «Phase 2 - Site & Permits» · «Phase 3 - Production &
Health» · «Phase 4 - Staff & Food Safety» · «Phase 5 - Brand & Menu» · «Phase 6 - Opening & Season»); A1 =
«ICE CREAM SHOP STARTUP CHECKLIST» (fijado). Las cabeceras de fase (A2) siguen el nombre de su pestaña con sus semanas
(«PHASE 2: SITE & PERMITS (weeks 3-12)»).

- **DV (c0654)**: la lista EN es «✓,☐,N/A»: el texto dice **☐ = pending**, nunca «—» (la propuesta de la Pizza EN dice
  «— = pending»: está mal también allí, D199).
- **Equivalencias US de D199** (las pistas de cada cadena las recuerdan; cada trámite español se SUSTITUYE, nunca se
  traduce): LLC vs S corp with your CPA · EIN + state payroll / unemployment · business license + **sales tax permit** ·
  POS that reports sales tax · zoning check before signing (retail food with on-site production) · ask the utility about
  3-phase service and amps before signing · building permit + CO · **plan review (8-201.11) with the equipment layout** ·
  sidewalk café / patio permit · signage permit · electrical inspection · health permit + inspection · **license
  decision: buy base from a licensed dairy or make your own mix (state dairy / frozen dessert license, 3-A equipment) —
  ask your state department of agriculture in writing** · base supplier agreement (delivery ≤ 41 °F, lot codes) ·
  dipper well with running water (3-304.12) · cold holding ≤ 41 °F, frozen storage 0 °F, date marking · labels on
  packaged pints (3-602.11, allergens) · «ice cream» / «frozen custard» only if the recipe meets 21 CFR 135.110 · offer
  letters, I-9, W-4, state new-hire reporting, minimum wage posters · seasonal hiring each spring · teen scoopers: FLSA
  hours and state work permits · OSHA basics (cold, slips, cuts) · CFPM (2-102.12) + food handler cards · 9 allergens
  incl. sesame · no «allergen-free» promise · honest claims («made here in small batches») · Google Business Profile ·
  cake pre-orders (birthdays, graduations, holidays) · National Ice Cream Day (3rd Sunday of July) · DoorDash / Uber Eats
  for pints · soft opening + Opening Day · peak-season staffing (Memorial Day → Labor Day) · winter plan (cakes, holiday
  pies and pints, hot chocolate, catering; or close November-February) · insurance with equipment breakdown + food
  spoilage · refrigeration service contract before summer (EPA 608 tech; staff never top up refrigerant).
- **Regla B2 de la pizza**: toda licencia o permiso que prometan la landing, el hub o el Word tiene **su tarea**: license
  decision, health permit, sales tax permit, patio permit, building permit / CO. No hay filas nuevas: se reescribe una
  tarea existente. Propuesta de encaje (las tareas sin equivalente US se sustituyen, no se traducen):

| Celda | ES | Tarea US propuesta |
|---|---|---|
| F1!B5 | Consulta urbanística previa | Zoning check before signing (retail food with on-site production) |
| F1!B8 | Alta censal 036 (644.4 y 676 del IAE) | Business license + **sales tax permit** (state and city) |
| F1!B9 | Valorar el 414.4 si fabricas para otros | **License decision**: buy pasteurized base or make your own mix — ask your state department of agriculture in writing |
| F1!B15 | Seguro RC y multirriesgo | General liability, property and equipment breakdown + food spoilage |
| F2!B6-B7 | Potencia 30 kW · desagües y salida de humos | 3-phase service and amps (about 30 kW) · floor sinks, drains and condenser ventilation (sin humos) |
| F2!B11 | Licencia de obra (propuesta con «flue») | Building permit for the build-out (sin «flue») |
| F2!B12 | Declaración responsable (644.4) | **Plan review** (Food Code 8-201.11) with the equipment layout |
| F2!B13 | Licencia de hostelería (676) | Seating and restrooms: confirm with the building and health departments what your seat count requires |
| F2!B17 · F3!B5 | Frío y pasteurizador · comprar pasteurizador, mantecadora, abatidor | Batch freezer, hardening cabinet and base refrigerator (sin pasteurizador) |
| F3!B8 | Declaración de inicio de actividad alimentaria | **Health permit** application and pre-opening inspection |
| F3!B9 | Art. 3 RD 1021/2022 (vender a restaurantes) | Before selling to restaurants or cafés, ask your state: it may require a manufacturer license |
| F3!B10-B12 | APPCC con PCC de pasteurización · maduración… · huevo | Written food safety plan (receiving ≤ 41 °F, lot codes, date marking) · batch freezing, hardening ≤ 0 °F, dipping cabinet 6-10 °F · custard flavors from a custard base, no raw eggs |
| F3!B17 | Denominaciones del RD 618/1998 | Menu names that meet 21 CFR 135.110 («ice cream», «frozen custard») |
| F4!B6 · B8 · B10 | Fijos discontinuos · llamamientos · menores | Seasonal part-time W-2 hires · seasonal hiring calendar (rehire each spring) · teen scoopers (14-15): FLSA hours and state work permits |
| F5!B6 · B9 · B14 | «Artesano» · carta de invierno con crepes · restaurantes (art. 3) | Honest claims · winter menu: cakes, holiday pies and pints, hot chocolate · catering and events |

- **Revisión de GRC** (lista `revisar_reutilizadas.GRC`): casi todo plazos («Weeks 3-6»), responsables y tareas comunes
  de la Pizza EN: confirma que valen para una heladería y corrige solo lo que no case (p. ej. «Owner / Code consultant»,
  algo de pizza, de humos o de horno; la cabecera de la fase 1 «PHASE 1: BUSINESS SETUP & TAXES (weeks 1-4)» vale).

## 4. Tandas (c) ice_a (§1-5) ‖ (d) ice_b (§6-10) — paso 3: LISTAS (27-oct, tras la tanda 1)

Lo que se pega a cada subagente: sección 0 de `BP/BRIEF-TRADUCTORES.md` + su bloque «Docx — reglas comunes de las tandas
(d)-(g)» + las secciones **0, 1, 4 y 5** de este fichero. Cada uno lee su entrada y, como FORMA, la misma sección de la
Pizza EN (`BP8/docx_en_piz_a.json` o `docx_en_piz_b.json`); NO toca nada más que su salida y no corre `preparar_tandas`.

| Tanda | Entrada | Párrafos · palabras ES | Salida |
|---|---|---|---|
| (c) ice_a | `BP10/tandas/ice_a.entrada.json` | 29 · 3,039 (§1 Executive Summary · §2 Concept · §3 Market · §4 Competition · §5 Marketing) | `BP10/docx_en_ice_a.json` |
| (d) ice_b | `BP10/tandas/ice_b.entrada.json` | 32 · 3,780 (§6 Operations · §7 Staffing · §8 Financial Plan · §9 Legal · §10 Conclusions) | `BP10/docx_en_ice_b.json` |

- Formato de salida: `{"<i>": "<párrafo EN>", …}` con TODOS los «i» de `parrafos` y nada más; un párrafo por clave, sin
  saltos de línea nuevos; los subtítulos (una línea sin punto final) siguen siendo una línea sin punto final.
- Cada párrafo trae su `nota` (`datos_ice.DOCX_NOTAS`): la sección + la FORMA de la Pizza EN; las de [47], [50],
  [53]-[56], [64], [73], [78]-[80], [82], [87]-[88], [99], [113], [115] SUSTITUYEN el bloque ES que no cruza (D200) y las
  7 de §9 (102-108) fijan el tema de cada párrafo; **la 108 cierra con la nota UK** (el check la exige).
- **Cifras**: las del plan, SOLO como tokens `{{…}}` de `tokens` (112). La entrada trae además `cifras_del_caso` (el valor
  final de cada token, leído del Excel EN calibrado: ventas $383,625, neto 5.6 %, pesimista −$32,344…) SOLO para que
  entiendas el caso: **en el texto va el token, nunca la cifra** (p. ej. una pérdida se escribe «a pre-tax loss of
  {{pesimista_perdida}}», no «{{pesimista_resultado}}», que lleva el signo menos). Importes «$» fuera de tokens solo los de
  research/SPEC con su fuente (carta de ejemplo research §5.1, batch freezer de 20 qt ≈ $40,800, pasteurizador de la
  variante $25,000-45,000…).
- **Terminología fijada por la tanda 1** (manda): «customers» (nunca covers / transactions) · «pasteurized base» de un
  «licensed dairy»; «pasteurize your own mix» = la variante · licencias: «ask your state department of agriculture» (y el
  local health department para el health permit), sin tarifas ni «no license needed» · «seasonal part-time W-2» ·
  «scooper» / «shift lead» · jóvenes de 14-15 años solo con horario FLSA (29 CFR 570.35) · «waffle cone irons» · «dipper
  wells» con agua corriente · °F con °C entre paréntesis · Month 1 = March · ☐ = pending (checklist).
- Coherencia con el Excel y el checklist EN: los rótulos que cites (partidas, puestos, pestañas) con las palabras de
  `fijos_en` / `pestanas_es_en` de las entradas de la tanda 1; el Word dice lo mismo que el libro sobre el modelo de base
  comprada (§2, §6, §8 [99] y §9 [104]) y no promete nada que el Excel no haga.

## 5. Validación (Mac, solo JSON) — el comando EXACTO de cada tanda

Desde la raíz del worktree del Mac. Itera hasta `OK (0 errores, …)` en los DOS comandos de tu tanda y revisa los AVISOS
reales. **No corras `preparar_tandas`** (reescribe ficheros compartidos con la otra tanda): `check_revision.py` valida tu
revisión en un temporal propio.

```bash
istats cpu temp | head -1
# tanda (a)
python3 scripts/productos-digitales/business-plans-en-10/bp10.py check_textos --tanda GICE-plan
python3 scripts/productos-digitales/business-plans-en-10/check_revision.py GR
# tanda (b)
python3 scripts/productos-digitales/business-plans-en-10/bp10.py check_textos --tanda GICE-check
python3 scripts/productos-digitales/business-plans-en-10/check_revision.py GRC
```

Responde solo con: ficheros escritos, nº de claves (y de correcciones de la revisión), resultado de los dos checks y 3-5
decisiones de traducción que deban conocer la otra tanda y las del Word.

```bash
# tanda (c) — Word §1-5
python3 scripts/productos-digitales/business-plans-en-10/bp10.py check_textos --tanda ice_a
# tanda (d) — Word §6-10
python3 scripts/productos-digitales/business-plans-en-10/bp10.py check_textos --tanda ice_b
```

En la tanda 2, un solo comando por traductor (no hay revisión de reutilizadas); misma respuesta: fichero, nº de claves,
resultado del check y 3-5 decisiones.

**Después (orquestador)**: tanda 1 → `bp10.py preparar_tandas` (aplica GR/GRC.revision) → `bp10.py check_textos --todas`
→ paso 3 (VPS: `aplicar_en` real + D15 → `cifras_caso.json`; `preparar_tandas` + `anotar_tandas_docx.py` en el Mac) →
tanda 2 ice_a ‖ ice_b → `bp10.py check_textos --todas` → paso 4 (VPS: `ensamblar_docx --plan ice`, G1-G9, barrido,
regresión; F2-NOTAS §8).
