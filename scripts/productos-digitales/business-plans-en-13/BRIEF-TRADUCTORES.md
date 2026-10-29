# Brief para los traductores (subagentes Sonnet) — Rotisserie Chicken Restaurant Business Plan Kit (EN)

> Sesión Claude Code, 29-oct-2026 (F2-EN: preparado; **no se ha traducido nada**). Fuente de verdad: `../plan-polleria/
> F1-camino.md` §6-§7 y `F1-research-us-delta.md` (US §n). Regla 1bis: los textos de producto los escriben subagentes
> Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac): `scripts/productos-digitales/business-plans-en-13/` (=
> `BP13/`, datos y salidas de la pollería), `scripts/productos-digitales/business-plans-en-12/` (= `BP12/`, el **Taco Shop
> EN** publicado hoy: MISMA semilla de libro, mismo código y la FORMA) y `scripts/productos-digitales/business-plans-en/`
> (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GPOL-plan + revisión de GR ‖ (b) GPOL-check + revisión de GRC** →
> **tanda 2 = (c) pol_a ‖ (d) pol_b** (las entradas ya existen y llevan `cifras_del_caso`; el orquestador las regenera
> tras la tanda 1 con `preparar_tandas` + `anotar_tandas_docx.py`, sin cambiar ids).
> **No se escriben** GM (357 cadenas: motor común con EN limpio del Taco EN, la Pizza EN, el Bar EN o BP) ni GR / GRC (35 +
> 113: EN reutilizado del Taco EN —18 casadas cambiando «pedido» por «comensal»— que **se revisa** en tu tanda): los
> escribe `bp13.py preparar_tandas`. **El ES ya es FINAL** (F2 ES revisada, `8c34fa09`; sha256 en `mapas_pol.SHA_ES`).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas) + las secciones **0, 1 y 5** de este fichero
(la 1 es el glosario US §9 completo, OBLIGATORIO; la 5, la validación) + la de su tanda (§2, §3 o §4). Lo que aquí choque
con el brief común **manda aquí** (el comando de validación es el de §5, con `bp13.py`). El subagente no hace commit,
**no corre `preparar_tandas`** y no toca nada más que sus salidas.

---

## 0. Lo que cambia frente al brief del Taco EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP13/tandas/<TANDA>.entrada.json`; `BP13/F1-research-us-delta.md` §1, §4, §5, §6
y §8 (el §9 va pegado abajo); como FORMA (registro, longitud), el EN del Taco EN en `BP12/textos_en/{GTAQ-plan,
GTAQ-check}.json` y `BP12/docx_en_taq_{a,b}.json` — el libro de la pollería sale de la MISMA semilla que el de la
taquería: la gemela está en la misma hoja y celda de `BP12/textos_es.json` (salvo `Break-Even` ≥ 25, que sube 2 filas).
**Su vocabulario de taquería NO vale** (taco, trompo, al pastor, tortilla, masa, salsa bar, aguas frescas, patio, «closed
Mondays», 115 covers, 308 days…).

**Concepto (US §1): COUNTER-SERVICE ROTISSERIE CHICKEN RESTAURANT de barrio, estilo peruano (pollo a la brasa)**, en una
ciudad media de EE. UU. (150-300 mil hab.), ~1,600 sq ft, **40 plazas** (sin patio), pedido en mostrador (**sin servicio
de mesa: nunca «servers» ni «waitstaff»**), pickup propio, **family meals, pre-orders y party trays** (cumpleaños,
iglesias, oficinas) y marketplaces. Línea: **dos commercial rotisseries de GAS de 8 espadas** (48 pollos por carga cada
una) a la vista desde la calle, 2 freidoras (yuca fries y fries), fogones (rice & beans, salsas, chicha morada), **heated
display** para los pollos enteros to-go y walk-in para el marinado de 24-48 h. Carta: quarter (dark/white), half y whole
chicken con 2 sides; family meal (whole + 2 large sides + 2 sauces); sandwich/bowl de pollo deshilachado (los pollos que
salen del display por la regla de las 4 h, enfriados con registro); sides yuca fries, fries, rice & beans, maduros, house
salad, salchipapas; salsas aji verde, aji amarillo, huancaina; Inca Kola, chicha morada, sodas y **beer & wine**. **Abre 7
días (360)**: el domingo es el pico. El dueño es el GM y jefe de rotisserie. **Nombre**: «rotisserie chicken restaurant»;
«Peruvian chicken» y «pollo a la brasa» en prosa. Fuera (y así lo dicen las FAQ): food truck (→ Food Truck Business Plan
Kit), franquicias (El Pollo Loco, Pollo Tropical), fried chicken / wings, venta de pollo crudo, kioscos de supermercado.

**Caso US** (`BP13/F2-NOTAS.md` §3; D15 VERDE en la vuelta 0, sin palancas): 130 covers × **$17.50** × 360 días =
**$819,000** · CAPEX $237,832 (18 partidas $211,300 + fianza de 2 meses + 2 meses de renta previa + imprevistos por
fórmula $11,600) + fondo de maniobra $97,876 = **$335,708** · propios $120,000 + préstamo **$216,000** (SBA 7(a), 10 %,
10 años, sin interest-only) · margen tras variables 60.2 % · COGS 28.0 % · personal 33.1 % (10 personas = 6.60 FTE) ·
alquiler 5.5 % · EBITDA $123,379 · **neto 7.1 %** el año 1 y 10.0 % el año 3 · equilibrio 110 / 107 covers al día · holgura
de caja 22 % · DSCR mín 2.96× · saldo mínimo $103,822 (Mes 1). **Mes 1 = ENERO** (orden del calendario; curva plana:
enero-febrero flojos; mayo, julio y diciembre los picos). **Una family meal cuenta como 3.5 covers**: el ES dice
«pedido»; el EN dice **covers** (y «orders» solo para pre-orders y pickup orders). Las notas del libro describen el
**método** o usan `valor_us` de tu entrada; **ninguna cifra del ES** (el gate las caza, en € y en $: 77 pedidos, 15,80,
364.980, 161.601, 300 días, 14 pagas, 33 %, 17.094, 1.221, 11-12 % de plataforma, 63 °C, 75 °C…).

**Lo que el check rechaza** (`datos_pol.RX_POL_NO` + `cifras_prohibidas`): taco / taqueria, trompo / al pastor, tortilla /
masa harina, salsa bar, mezcal / tequila; pizza, Neapolitan, dough, VPN, Margherita / mozzarella / San Marzano; tapas,
small plates, cocktails, happy hour, spirits (salvo «full liquor license»); IVA, convenio, SMI, autónomo, Veri\*factu, SGAE,
IAE, terraza, **comensal / pedido**, croquetas / ensaladilla / alioli / «al ast», **España / Spain / Spanish**, VAT fuera de
la nota UK; RD 1021/2022, RD 1086/2020, RD 126/2015, RD 919/2006, «art. 4.1 / 9 / 30», Leyes 1/2025 y 7/2022, ACSA, AESAN;
**«pollo asado»** salvo para decir que en EE. UU. es el pollo MEXICANO a la parrilla (El Pollo Loco) o negado;
**«poultry shop/store»** salvo «raw» o negado; **«roaster»** salvo «roaster chickens / larger birds»; **«yucca»** (es
«yuca»); **«PERi-PERi»**; **«Broaster»** salvo «(a brand)»; **«chicken shop»** fuera de la nota UK; **Australia** (va solo
en la FAQ de la landing); **authentic**; «gluten-free» salvo negado o con 21 CFR; servers / waitstaff / waiters salvo «no
table service / counter service»; kg, g, km, liters, °C o m² fuera de paréntesis; y los casos EN del Taco (115 covers,
308 days), la Pizza (62 covers, $36…), la Ice Cream, la Bakery, el Bar ($27, 95 covers), FT y el Restaurant.

**Jerga peruana que el inglés US usa tal cual** (el detector de restos no la cuenta: `mapas_pol.TERMINOS_PE`): «pollo a la
brasa», «Día del Pollo a la Brasa» (mejor «Pollo a la Brasa Day»), «El Pollo Loco», «papa a la huancaina». **Sin tildes en
EN**: aji, huancaina, huacatay, yuca (no «ají», «huancaína»). Cualquier otra construcción española con «de», «del», «con»…
**la marca el check**.

**Unidades** (`datos_pol.REGLA_UNIDADES`): lb y oz, °F, gallons / quarts y sq ft como unidad principal; la métrica entre
paréntesis: «3.0 lb (1.4 kg)», «165 °F (74 °C)», «135 °F (57 °C)», «1,600 sq ft (149 sq m)», «50 lb (23 kg)».

**Lo legal y operativo que SUSTITUYE al ES** (US §6; nunca se traduce el trámite español):
- FDA Food Code 2022 (cada estado adopta su edición): **aves a 165 °F** (3-401.11) · **hot holding ≥ 135 °F** (3-501.16) ·
  **cooling 135 → 70 °F en 2 h y → 41 °F en 6 h en total** (3-501.14) · **reheating para hot holding a 165 °F**
  (3-403.11) · cold holding ≤ 41 °F · pollo con inspección USDA (approved source) · pollo crudo abajo en el walk-in, tablas
  por color, **no lavar el pollo crudo**.
- **SOP del heated display**: TPHC (3-501.19) hasta **4 h** con la hora marcada y **procedimiento escrito**; a las 4 h o si
  baja de 135 °F, se enfría con registro para el sandwich/bowl del día siguiente o se tira; nunca vuelve al display sin
  pasar por 165 °F. Pollos envasados en autoservicio: etiqueta (3-602.11). Rice & beans = TCS (*B. cereus*).
- Type I hood + supresión UL 300 + makeup air sobre rotisseries y freidoras; limpieza de campana trimestral (NFPA 96, Tabla
  11.4); dos rotisseries de ≈ 177,500 BTU + freidoras → acometida y regulador de gas dimensionados, con permiso. **Carbón**
  = combustible sólido (NFPA 96 cap. 14: escape propio, arrestachispas, ceniza diaria) → **variante**, no el caso;
  aparato listado (UL/ETL) + NSF/ANSI 4; los asadores importados de Perú pueden no tener listing; aire: «ask your air
  district». Ventless solo con equipo listado con su campana (las freidoras siguen bajo Type I).
- Plan review (8-201.11) + health permit + pre-opening inspection · building permit + certificate of occupancy · business
  license + sales tax permit · CFPM (2-102.12) + food handler cards según estado.
- 9 alérgenos mayores con sésamo (UK 14): **marinado = soy sauce (soy + wheat) + cerveza (wheat/barley)**; aji verde a
  menudo con mayonesa (egg) y queso fresco / cotija (milk), según receta; huancaina = milk + galletas (wheat); pan del
  sandwich = wheat (sesame si lleva semillas); freidora compartida con empanados → contacto cruzado. **«Gluten-free» no se
  promete**, ni del pollo ni de las yuca fries.
- **Beer & wine license**: estado + aprobación local, coste y plazos muy distintos: «apply early», **nunca prometerla**;
  liquor liability en el seguro.
- Personal W-2 por horas (nada de 1099 para cocineros o cajeros), ≥ $15/h, propinas del mostrador para el equipo (nunca
  para el dueño o los managers), sin tip credit modelado; SBA 7(a); sales tax 8 % de ejemplo, un solo tipo («some states
  tax to-go food differently», sin cifra).
- **Nombres**: «peri-peri» genérico en minúscula (nunca «PERi-PERi»); «pressure-fried chicken» («Broaster» es marca);
  **«pollo asado» NO es sinónimo** (en EE. UU. = pollo mexicano a la parrilla, El Pollo Loco): el producto es
  **«rotisserie chicken»**; nunca «poultry shop» (es pollo crudo) ni «roaster» (es un pollo grande).
- **Las cinco corrientes** (Word §2, ES ¶47; contenido de guía, sin Excel propio), adaptadas al comprador US: (1)
  **Peruvian pollo a la brasa** = el caso; (2) **peri-peri** (chile africano a la portuguesa); (3) **charcoal chicken**
  (el mismo pollo sobre carbón: la identidad del asador limeño, aquí variante NFPA 96); (4) la **rotisserie francesa**
  (poulet rôti en espadas horizontales); (5) el **pollo en brasa venezolano** con guasacaca. La corriente española (y el
  pollo al ast catalán) **no cruza**. **Ningún producto citado** salvo los del cierre (no hay guía de restaurante peruano
  en la tienda EN: lección M2 del Taco EN).

---

## 1. Glosario OBLIGATORIO (US §9, pegado entero)

## 9. Jerga profesional US (glosario OBLIGATORIO de los traductores)

(a) **Nombre**: **«Rotisserie Chicken Restaurant Business Plan Kit»** en landing/H1/ficheros (`rotisserie-chicken-restaurant-business-plan`). «Peruvian chicken» / «pollo a la brasa» en subtítulo, descriptor y prosa;
«chicken shop» solo en las notas UK; «charcoal chicken» en descriptor y notas AU. **Nunca** «poultry shop/store», «roaster», «roast chicken shop», «Tex-Mex», «authentic» como promesa ni «PERi-PERi».

| # | ES pollería | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Pollería / asador de pollos (negocio) | **rotisserie chicken restaurant** · **Peruvian chicken place/restaurant** · *chicken shop* (UK) | DFS 1.600 / 2.900; SERP |
| 2 | Pollo a la brasa | **pollo a la brasa** (sin traducir) · **Peruvian rotisserie chicken** · «Peruvian chicken» | DFS 40.500 · 3.600 · 40.500 |
| 3 | Asador / horno de pollos (equipo) | **commercial rotisserie (oven)** · **chicken rotisserie machine**; pollero peruano = **charcoal rotisserie** | DFS 590 · 2.400; webstaurantstore [leída] |
| 4 | Espetón · cesta | **spit** (8-spit rotisserie) · **basket** (basket rotisserie) · «load» = carga | webstaurantstore [leída] |
| 5 | Pollo asado (España) | **rotisserie chicken**; **«pollo asado» en EE. UU. = mexicano a la parrilla** (El Pollo Loco): no usar como sinónimo | DFS 135.000; SERP |
| 6 | Brasa / carbón vegetal | **charcoal** (lump/hardwood charcoal) · **charcoal-fired** | uso |
| 7 | Pollo entero · medio · cuarto (muslo / pechuga) | **whole · half · quarter chicken (dark = leg & thigh / white = breast & wing)** | menús [leída] |
| 8 | Menú familiar | **family meal** (whole chicken + 2 large sides) | menús (resumen) |
| 9 | Guarniciones | **sides** (regular / large): **yuca fries** (no «yucca»), fries, **rice & beans**, **maduros** (sweet plantains), house salad, coleslaw, **salchipapas** | DFS 40.500 / 49.500; menús |
| 10 | Salsas | **aji verde** (Peruvian green sauce), **aji amarillo**, **rocoto**, **huancaína**, **huacatay** (sin tildes en inglés) | DFS 14.800 · 9.900 · 6.600 |
| 11 | Bebidas | **Inca Kola** · **chicha morada** (purple corn drink) | DFS 22.200 |
| 12 | Adobo / maceración | **marinade** · «marinated 24-48 hours» | SERP (Braza, Mister Pio) |
| 13 | Rendimiento · merma | **cooked yield** · **shrink** / holding waste | uso; Kit |
| 14 | Vitrina caliente | **heated display (merchandiser)** · **hot holding** | webstaurantstore [leída] |
| 15 | Pollo de 1,2-1,4 kg | **broiler/fryer** (2.5-4.5 lb) · **WOG** (without giblets); «roaster» = pollo grande, **no el asador** | USDA AMS (resumen) |
| 16 | Encargos para fiestas | **pre-orders** · **party trays** · **catering orders** | DFS 70 |
| 17 | Para llevar · plataforma | **take-out / to-go / pickup** · **third-party delivery marketplace** | ✅ PIZ-US §9 |
| 18 | Mostrador | **counter service** · **fast casual** · **QSR** | ✅ hermanos |
| 19 | Cubierto equivalente · ticket | **covers** · **average check** (excl. sales tax y tip) | ✅ hermanos |
| 20 | Escandallo | **food cost per bird / per plate** · **recipe costing** | ✅ hermanos |
| 21 | Campana · carbón | **Type I hood** · **fire suppression (UL 300)** · **solid-fuel cooking (NFPA 96)** · **spark arrester** | ✅ REST §5 · PIZ-US §6.2 |
| 22 | Enfriar · recalentar · control por tiempo | **cooling** · **reheating for hot holding** · **TPHC** | ✅ BBQ §9 · PIZ-US §9 |
| 23 | Manipulador | **food handler card** · **CFPM** | ✅ PIZ-US §9 |
| 24 | Pollo broaster | **pressure-fried chicken** («Broaster» es marca) | 🟡 |
| 25 | Piri-piri portugués | **peri-peri** (minúscula, genérico) | DFS 40.500 |
| 26 | «86» | **86'd** | ✅ PIZ-US §9 |

(e) **No se traducen literalmente**: «pollería» → **rotisserie chicken restaurant** (nunca «poultry shop»: es venta de pollo crudo) · «asador» (equipo) → **rotisserie**, (negocio) → **rotisserie chicken restaurant**
(nunca «roaster») · «pollo asado» → **rotisserie chicken** · «brasa» → **charcoal** · «vitrina» → **heated display** · «menú familiar» → **family meal** · «63 °C» → **135 °F** · «75 °C» → **165 °F** · «ordenanza de
humos» → **Type I hood + local fire/mechanical code (+ air district)** · «registro sanitario» → **health permit + plan review** · «licencia de apertura» → **business license + certificate of occupancy** · «convenio»
→ **state/local minimum wage** · «IVA» → **sales tax** · «autónomo/SL» → **LLC** · «plataforma» → **delivery marketplace**.

**Capas (1) y (2)**: **Rotisserie Chicken Restaurant Business Plan Kit** · slug `rotisserie-chicken-restaurant-business-plan` · `rotisserie-chicken-restaurant-business-plan.docx` «Rotisserie Chicken Restaurant
Business Plan (10 Sections)» · `rotisserie-chicken-financial-projections.xlsx` · `rotisserie-chicken-startup-checklist.xlsx` · calculadora **según el ES** (propuesta `chicken-cost-rotisserie-yield-calculator.xlsx`,
pestañas `Bird Cost` / `Plates & Family Meals` / `Rotisserie Loads` / `Sauces` / `Holding Waste`; lb↔kg, °F↔°C) · guía de equivalencias según el ES · pestaña F2 **«Phase 2 - Hood, Gas & Permits»** (29 car., ≤ 31).

### Términos para la landing (DataForSEO US, 29-oct)

| Keyword | Vol. | Uso |
|---|---|---|
| **rotisserie chicken restaurant business plan** · chicken restaurant business plan · chicken shop business plan | 10 · 10 · 10 | slug, H1, title, schema |
| how to open a chicken restaurant · how to start a chicken business · rotisserie chicken business | 10 · 20 · 20 | H2, FAQ |
| peruvian chicken restaurant · rotisserie chicken restaurant · peruvian rotisserie chicken | 2.900 · 1.600 · 3.600 | cuerpo, H2 |
| chicken rotisserie machine · rotisserie chicken oven · commercial rotisserie oven | 2.400 · 4.400 · 590 | H2 equipo, alt |
| pollo a la brasa · peruvian chicken · charcoal chicken · peri peri chicken · aji verde · yuca fries | 40.500 · 40.500 · 18.100 · 40.500 · 14.800 · 40.500 | cuerpo, alt (consumidor: no title) |
| rotisserie chicken temperature | 590 | FAQ (hot holding) |

- **Title** (≈ 105 car.): «Rotisserie Chicken Restaurant Business Plan: Word + Excel Projections + Chicken Cost Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Rotisserie Chicken Restaurant ` + oro `Business Plan` + «Template for a Peruvian Pollo a la Brasa or Charcoal Chicken Shop: Word Plan + Excel Projections + Chicken Cost & Rotisserie Calculator +
  Startup Checklist».
- **Meta** (≈ 155 car.): «Rotisserie chicken restaurant business plan for a Peruvian pollo a la brasa shop: Word plan, 3-year Excel projections, chicken cost calculator and permit checklist.»
- **H2 (6)**: What's Inside Your Rotisserie Chicken Restaurant Business Plan Kit · How Much Does It Cost to Open a Rotisserie Chicken Restaurant? (Hood, Rotisseries, Build-Out) · Is a Rotisserie Chicken Restaurant
  Profitable? The Cost of Every Bird · Gas, Electric or Charcoal: Choosing Your Rotisserie (and What the Fire Marshal Asks) · Hot Holding, Family Meals and Holiday Pre-Orders · DoorDash, Uber Eats and Grubhub: What
  Delivery Really Costs a Chicken Shop.
- **Alt**: «Peruvian rotisserie chicken turning on spits over charcoal» · «Family meal with whole chicken, yuca fries and aji verde» · «Heated display with whole rotisserie chickens ready for pickup». **Keywords**
  (schema/docProps): rotisserie chicken restaurant business plan, chicken restaurant business plan, how to open a rotisserie chicken restaurant, Peruvian chicken restaurant, pollo a la brasa, AI Chef Pro.

---

## 2. Tanda (a) — GPOL-plan + revisión de GR

Entrada `BP13/tandas/GPOL-plan.entrada.json`: **118 cadenas, ≈ 3,9 K palabras** (70 de texto libre + **48 celdas D19**: 12
filas × 4; sin propuesta) + `revisar_reutilizadas.GR` (**35** cadenas: 18 rótulos «Pedidos…» casados con los «Covers…» del
Taco EN, 16 por celda del Taco EN, 1 de la Bakery). Salidas: `BP13/textos_en/GPOL-plan.json` (TODOS los ids) y
`BP13/textos_en/GR.revision.json` (solo las de GR que cambian; `{}` si ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista o el método; el ES explica «pedido» (mostrador, encargo,
  plataforma o cliente sentado) y el reparto semanal con cifras ES (278, 45, 140, 150, 40…): **en EN, covers** (una family
  meal = 3.5 covers; US §8: ≈ 55 en sala, ≈ 55 pickup y pre-orders, ≈ 20 marketplace; domingo ≈ 1.6-1.8 × un laborable,
  65-70 pollos; Kit estimate), **ninguna cifra ES**. Sin el 10/21 % del IVA español: un solo sales tax de ejemplo (8 %,
  B39 = B40 = B63), sin crédito por compras (B41 = 0). **C34**: B34 = 0 (sin carencia). **C60/C61**: con 12 pagas no hay
  pagas extra. **C62/C63** y **A62** están fijadas (POR_CELDA): si las citas, con esas palabras.
- **Notas de `Startup Costs` (col. D, filas 7-24)**: las partidas de US §8 en las filas ES (rótulos ya fijados en
  `fijos_en`: lee el rótulo EN de la fila antes de escribir su nota). **OJO D15 y D19**: la nota ES habla de la campana y
  del botellero de la cervecera; en el EN esas filas son el **walk-in cooler (6×8)** y el **beverage cooler & ice
  machine**: escribe la nota del rótulo EN. **D12**: dos rotisseries de gas de 8 espadas (Pegasus CR-8G, $6,011 retail,
  48 pollos por carga; el caso $13,000 con flete e instalación); nada de «doce espadas» ni precios en €. Rangos solo con
  fuente de US §4 o ninguno.
- **`3-Year P&L` col. F**: F10 = reparto de la comida de su pista; F11 está fijada; F13 es fórmula (ya EN); los umbrales
  del semáforo con los del libro EN (margen tras variables ≥ 60 %, mercancía ≤ 30 %, personal ≤ 36 %, alquiler ≤ 10 %,
  neto ≥ 5 %). Notas de los fijos 26-34 con los rótulos fijados (hood cleaning **trimestral**; permit renewals con residuos).
- **`Staffing` col. J**: los puestos de US §8 en la fila ES de su función (rótulos fijados: Owner / GM & head of
  rotisserie · Rotisserie cook · Counter lead / cashier · Counter, packing & expo (part-time W-2, 4 personas × 0.4) · Dish
  & prep (part-time W-2) · Fry & line cook (part-time W-2, weekends & peak days) · Prep & relief rotisserie cook), con su
  $/h (owner $4,500/mes · 19 · 16 · 15 · 15 · 17 · 17.50); el dueño cobra por debajo de un manager (OEWS $33.36/h):
  «owner's draw in addition from net profit». A29 está fijada. Cobertura: servicio 10.5 h × 2.75 + producción 3 h × 1.5.
- **`Break-Even`**: SIN rotación (el bloque está apagado en el ES); A26 es fórmula (ya EN). Nada de «seat turns».
- **Tabla D19 (`Instructions` 35-46, una cadena por celda, SIN propuesta)**: cada fila la dicta su pista: Benchmark |
  Value | Source | Note, en el orden de las filas del ES (Month 1 · consumer demand · family meal · cost of a marinated
  bird · cooked yield · 8-spit gas rotisserie · marketplace commission · sales tax · cook/hold/cool/reheat · TPHC of the
  display · minimum wage · labor cost). Solo lo «[leída]» con fuente; lo «(resumen)» como «Kit estimate» o con «check».
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21 (divide by 1 + your sales tax rate); A10 con el **Mes 1 =
  JANUARY**; A12: el Word usa las cifras de este Excel y la calculadora del kit (**Rotisserie Chicken Yield & Costing
  Calculator**) escandalla cada pollo y cada plato: su food cost NO se copia en «0. Assumptions».
- **`12-Month Cash Flow`**: O5 está fijada (POR_CELDA, Mes 1 = enero con los pesos US).
- **Revisión de GR** (lista `revisar_reutilizadas.GR`): EN del Taco EN («covers» por «pedidos»): confirma que vale para una
  rotisserie chicken restaurant de mostrador y corrige solo lo que no case (nada de tacos, trompo, patio ni «seat turns»).

## 3. Tanda (b) — GPOL-check + revisión de GRC (las 80 tareas)

Entrada `BP13/tandas/GPOL-check.entrada.json`: **109 cadenas, ≈ 2,9 K palabras** + `revisar_reutilizadas.GRC` (**113**:
plazos, responsables, cabeceras y tareas que el Taco EN ya tenía en la misma celda). Salidas:
`BP13/textos_en/GPOL-check.json` (TODOS los ids) y `BP13/textos_en/GRC.revision.json` (solo las de GRC que cambian; `{}` si
ninguna). Molde C2 (OK | TASK | OWNER | TIMING | NOTES); pestañas fijadas («Phase 1 - Business Setup» · «Phase 2 - Hood,
Gas & Permits» · «Phase 3 - Rotisserie & Health» · «Phase 4 - Staff & Allergens» · «Phase 5 - Menu & Pre-Orders» ·
«Phase 6 - Opening & 90 Days»); A1 = «ROTISSERIE CHICKEN RESTAURANT STARTUP CHECKLIST» y las cabeceras de las fases 2, 3
y 5 fijadas. Las demás cabeceras de fase (A2) siguen el nombre de su pestaña con sus semanas.

- **DV**: la lista EN es «✓,☐,N/A»: el texto dice **☐ = pending**, nunca «—».
- **Tres tareas propias obligatorias** (F1-camino §6; regla B2: toda licencia o regla que prometan landing, hub o Word
  tiene su tarea): **beer & wine license** (ya en F1!B12, GRC: confírmala), **las reglas de tu condado para el pollo y el
  hot holding por escrito** (F3!B10) y el **holiday pre-order plan** (F6!B14). No hay filas nuevas: se reescribe una
  tarea existente. Encaje propuesto de las tareas de GPOL-check (las que no tienen equivalente US se SUSTITUYEN):

| Celda | ES | Tarea US propuesta |
|---|---|---|
| F1!B5 | Consulta urbanística: humos, trifásica, aforo | Zoning check before signing: restaurant use, Type I hood, gas service and seats |
| F1!B6 | Asador de gas o brasa ANTES de firmar | Decide gas or charcoal rotisseries before signing (charcoal = solid fuel: dedicated exhaust, NFPA 96, listed appliance) |
| F1!B7 | Tamaño del asador con la cuenta del domingo | Size the rotisseries with your Sunday count (48 birds per load, 75-90 min loads) |
| F1!B10 | Alta censal 036 (IAE) | Business license + **sales tax permit** (state and city) |
| F2!B5 | Local de unos 80 m² con salida de humos | Second-generation restaurant space of about 1,600 sq ft (149 sq m) with a route for the Type I hood |
| F2!B9 | Contrato con uso de asador y humos | Lease with restaurant use, hood rights and a beer & wine license contingency |
| F2!B13-B14 | Gas por instaladora · conducto y filtro si brasa | Licensed gas contractor, gas permit and inspection for two rotisseries + fryers · Type I hood, UL 300 suppression and makeup air (charcoal: separate solid-fuel exhaust and spark arrester) |
| F2!B15 | Obra con superficies lavables | Build-out with smooth, cleanable surfaces in the kitchen and prep areas |
| F2!B17-B18 | Campana · trifásica, boletín y certificado | Fire marshal sign-off of hood and suppression + Class K extinguisher · electrical final inspection and certificate of occupancy |
| F2!B19 | Rótulo con el teléfono de encargos | Sign permit; rotisseries visible from the street; pre-order phone and website on the sign |
| F3!B5-B6 | Comprar asador, vitrina, freidora, fogón · frío | Buy listed equipment (UL/ETL, NSF/ANSI 4): two gas rotisseries, heated display, fryers, range · walk-in, prep table and reach-in freezer |
| F3!B8-B9 | Crudo ≤ 4 °C, mollejas ≤ 3 °C · mesa de crudo, sin lavar | Raw and marinated chicken at 41 °F or below, bottom shelf, date-marked (WOG: no giblets) · separate raw-chicken prep sink and table, color-coded boards, never wash raw chicken |
| F3!B10 | Sonda a 74 °C en el muslo | **Get your county's rules for cooking and hot holding chicken in writing** and write your rotisserie SOP: probe the thigh at 165 °F and log it |
| F3!B11-B12 | Vitrina ≥ 63 °C con hora · sobrante enfriado | Heated display at 135 °F or above, time marked on every load (TPHC: 4 h with a written procedure) · leftover chicken cooled 135 → 70 °F in 2 h and → 41 °F within 6 h, logged; reheat to 165 °F |
| F3!B13 | Alioli, mayonesa, ensaladilla, cremas | Aji verde, huancaina and other sauces: TCS, at 41 °F or below and date-marked; mayonnaise base = egg |
| F3!B14 · B16 | Etiqueta de lo envasado · fichas con alérgenos | Label the birds and sides you pack for self-service (3-602.11) · recipe cards with the 9 major allergens (soy and wheat in the marinade; milk and egg in the sauces) |
| F4!B7 · B9 · B12 | Segundo asador · cuadrante del domingo · formación | Hire the second rotisserie cook before opening (7 days) · Sunday and peak-day schedule (2 rotisserie cooks + 3 on the counter) · rotisserie training: spitting, loading, probing at 165 °F, carving |
| F4!B16-B17 | Cartel de alérgenos · «sin gluten» | Allergen notice at the counter and online · never promise «gluten-free» with a shared fryer (21 CFR 101.91) |
| F5!B5-B7 | Tipo de pollería · carta con escandallo · IVA de la carta | Choose your style (Peruvian pollo a la brasa in the case) and your menu · short menu (quarter, half, whole, family meal, sandwich/bowl) costed with the calculator · sales tax on the menu: one rate; check your state's to-go rules |
| F5!B10-B12 | Dos proveedores de pollo · patata, aceite… · aceite y grasa | Two USDA-inspected chicken suppliers (fixed 3.0 lb WOG birds, received at 41 °F or below) · frozen yuca and fries, oil, packaging, Inca Kola and a beer & wine distributor · used cooking oil pickup and drip-tray grease |
| F5!B13 · B16-B17 | Encargos · web · Google, redes y música | Pre-order system: phone, online ordering, pickup slots and deposits for party trays · brand, photos and website with menu, allergens and pre-orders · Google Business Profile, Yelp, Instagram + music licensing (ASCAP/BMI/SESAC) |
| F6!B7-B8 | Limpieza · pruebas de carga | Cleaning plan for kitchen, rotisseries and display · test loads with the full menu (time each load) |
| F6!B12-B13 | Gas cada 5 años · rendimiento | Fire suppression inspection every 6 months and annual rotisserie and gas service · measure cooked yield and load time and recalculate (calculator) |
| F6!B14 | Verano y encargos de Navidad | **Holiday pre-order plan**: Mother's Day, Super Bowl Sunday, Christmas Eve and New Year's Eve (pickup slots, deposits, order cap = rotisserie capacity, whole crew) |

- **Revisión de GRC** (lista `revisar_reutilizadas.GRC`): casi todo plazos («Weeks 3-6»), responsables y tareas comunes
  del Taco EN: confirma que valen para una rotisserie chicken restaurant y corrige solo lo que no case (trompo, tortilla,
  salsa bar, patio, «closed Mondays», «taquero»…). F6!B5 («Open in January, Month 1 of the plan») vale.

## 4. Tandas (c) pol_a (§1-5) ‖ (d) pol_b (§6-10)

Lo que se pega a cada subagente: sección 0 de `BP/BRIEF-TRADUCTORES.md` + su bloque «Docx — reglas comunes de las tandas
(d)-(g)» + las secciones **0, 1, 4 y 5** de este fichero. Cada uno lee su entrada y, como FORMA, la misma sección del Taco
EN (`BP12/docx_en_taq_a.json` o `docx_en_taq_b.json`); NO toca nada más que su salida y no corre `preparar_tandas`.

| Tanda | Entrada | Párrafos · palabras ES | Salida |
|---|---|---|---|
| (c) pol_a | `BP13/tandas/pol_a.entrada.json` | 29 · 3,319 (§1 Executive Summary · §2 Concept · §3 Market · §4 Competition · §5 Marketing) | `BP13/docx_en_pol_a.json` |
| (d) pol_b | `BP13/tandas/pol_b.entrada.json` | 32 · 4,564 (§6 Operations · §7 Staffing · §8 Financial Plan · §9 Legal · §10 Conclusions) | `BP13/docx_en_pol_b.json` |

- Formato de salida: `{"<i>": "<párrafo EN>", …}` con TODOS los «i» de `parrafos` y nada más; un párrafo por clave, sin
  saltos de línea nuevos; los subtítulos (una línea sin punto final) siguen siendo una línea sin punto final.
- Cada párrafo trae su `nota` (`datos_pol.DOCX_NOTAS`): la sección + la FORMA del Taco EN; las 7 de §9 (102-108) fijan el
  tema de cada párrafo (102 marco y permisos · 103 hood, gas y fuego, carbón como variante · 104 health permit y Food Code
  del pollo · 105 **SOP del heated display** · 106 alérgenos y «gluten-free» · 107 beer & wine license, seguro, personal y
  nombres · 108 venta desde casa y **la nota UK al final**, que el check exige).
- **Lo que no cruza del Word ES** (IVA partido, arts. 4.1, 9 y 30, RD 126/2015, ordenanza de humos de Madrid, IAE,
  convenio, Leyes 1/2025 y 7/2022, Veri\*factu, la corriente española y el pollo al ast, croquetas y ensaladilla, «doce
  espadas», el local de 80 m² y las 20 plazas, la Guía Restaurante Peruano) se **sustituye** por el bloque legal de §0 y el
  caso US. **«Every bird counts»** (US §8, en §6): pollo marinado $5.99; uno que pasa su ventana de 4 h y se tira cuesta
  $5.99, uno enfriado con registro para sandwich/bowl ($13.50, 5 oz) vale ≈ $2.70 de producto → carga por franjas con el
  histórico del POS + pre-orders; merma ≤ 5 % de los pollos cargados. ≈ 40 pollos al día de media (Kit estimate).
- **Cifras**: las del plan, SOLO como tokens `{{…}}` de `tokens` (usa **`{{cogs_pct_xl}}`** y **`{{plantilla_jornadas_xl}}`**,
  que redondean como Excel: lección M5 del Taco EN). La entrada trae además `cifras_del_caso` (el valor final de cada
  token, leído del Excel EN calibrado) SOLO para que entiendas el caso: **en el texto va el token, nunca la cifra** (una
  pérdida: «a pre-tax loss of {{pesimista_perdida}}»). Importes «$» fuera de tokens solo los de la research con su fuente
  (US §4 y §5: Pegasus CR-8G $6,011, Type I hood $5,000-28,000, J&R charcoal $27,500-35,950, menús $10-13 / $16-18 /
  $31-34…).
- **Terminología** (manda): covers · counter service · rotisserie chicken restaurant · commercial rotisserie · spit · load
  · heated display · hot holding · family meal · quarter (dark/white) · half · whole · sides · yuca fries · aji verde ·
  pre-orders · party trays · beer & wine · Type I hood · TPHC · CFPM · Month 1 = January · ☐ = pending (checklist).
  Rótulos que cites (partidas, puestos, pestañas) con las palabras de `fijos_en` / `pestanas_es_en` de las entradas de la
  tanda 1; el Word no promete nada que el Excel no haga.

## 5. Validación (Mac, solo JSON) — el comando EXACTO de cada tanda

Desde la raíz del worktree del Mac. Itera hasta `OK (0 errores, …)` en los comandos de tu tanda y revisa los AVISOS
reales. **No corras `preparar_tandas`** (reescribe ficheros compartidos con la otra tanda): `check_revision.py` valida tu
revisión en un temporal propio.

```bash
istats cpu temp | head -1
# tanda (a)
python3 scripts/productos-digitales/business-plans-en-13/bp13.py check_textos --tanda GPOL-plan
python3 scripts/productos-digitales/business-plans-en-13/check_revision.py GR
# tanda (b)
python3 scripts/productos-digitales/business-plans-en-13/bp13.py check_textos --tanda GPOL-check
python3 scripts/productos-digitales/business-plans-en-13/check_revision.py GRC
# tanda (c) — Word §1-5
python3 scripts/productos-digitales/business-plans-en-13/bp13.py check_textos --tanda pol_a
# tanda (d) — Word §6-10
python3 scripts/productos-digitales/business-plans-en-13/bp13.py check_textos --tanda pol_b
```

Responde solo con: ficheros escritos, nº de claves (y de correcciones de la revisión), resultado de los checks y 3-5
decisiones de traducción que deban conocer la otra tanda y las del Word.

**Después (orquestador)**: ver `F2-NOTAS.md` §6 (comandos de la cadena completa).
