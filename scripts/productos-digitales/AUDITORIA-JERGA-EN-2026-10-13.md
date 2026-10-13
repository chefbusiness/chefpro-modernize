# Auditoría de jerga US — tienda EN de aichef.pro (13-oct-2026, solo lectura)

Fuentes: HTML servido (curl, 13-oct), fichas `astro-site/src/data/productos-en/**`, GSC `sc-domain:aichef.pro`
15-jul→12-oct (90 d; ojo: los productos nacieron entre el 25-sep y el 11-oct, así que la ventana real es de 1-3 semanas
y casi todas las queries vienen anonimizadas), DataForSEO US (3 llamadas `vol` + 1 `serp`). Rutas abreviadas:
`F/` = `astro-site/src/data/productos-en/`, `HUB` = `astro-site/src/components/pages/DigitalProductsHubPage.astro`.

## 1. Resumen por landing

| Landing | Impr. / clics GSC | Top queries GSC (impr.) | ¿Title/H1/meta con el término US? | Prioridad |
|---|---|---|---|---|
| Hub `/en/digital-products` | 40 / 0 | «artificial intelligence equipment for chefs» (1) | **No**: meta obsoleta, H1 sin keyword y nombres calcados (Dark Kitchen, Recurring Tasks…) | **ALTA** |
| food-cost-templates | 64 / 1 | «food gp calculator excel» (1) · «free recipe costing calculator for new zealand hospitality» (1) | Parcial: «food cost templates» sí; «calculator» no aparece en title/H1 | **ALTA** |
| restaurant-schedule-templates | 30 / 0 | «restaurant staff rota template» (1, pos 16) · «free online rota generator excel» (1) · «digital staff roster…» (1) · «staff scheduling tool for qsr» (1) | **No**: «Staff Rota» es británico; falta «employee schedule» | **ALTA** |
| restaurant-inventory-templates | 98 / 0 | «restaurants inventory sheets» (6) · «bar inventory templates» (5) · «restaurant inventory management excel free download» (3) · «restaurant inventory templates» (2) · «inventory sheets for restaurants» (1) | Parcial: «templates» sí; «inventory sheet/spreadsheet» y «par sheet» no van en title/H1 | MEDIA |
| haccp-templates | 101 / 1 | «haccp plan template» (3) · «haccp cleaning schedule template» (2) · «haccp spreadsheet» (2) · «haccp inspection form» (1) · «haccp plan template uk» (1) | Parcial: «HACCP plan template» sí; «temperature log» solo en la meta | MEDIA |
| ai-prompts-for-restaurants | 71 / 2 | «chef prompt» (12) · «chef ai prompt» (3) · «ai prompts for restaurants» (3) · prompt literal de marisquería (3) · «restaurant ai prompt» (1) | Parcial: la marca «Gastro Pro Prompts» va delante; no salen ni «ChatGPT» ni «chefs» en title/H1 | MEDIA |
| restaurant-financial-plan-templates | 32 / 0 | «restaurant p&l template» (13, pos 14,6) · «restaurant p&l format» (1) · «…p&l template excel» (1) · «restaurant loan editor» (1) | Sí («Restaurant P&L Template»), pero detrás del nombre del kit | MEDIA |
| coffee-shop-business-plan | 21 / 0 | «coffee shop business plan template excel» (1) · «coffee shop financial plan excel» (1) | Sí; le falta la intención «how to open a coffee shop» | MEDIA |
| food-truck-business-plan | 30 / 0 | «food truck business plan excel» (1, pos 2) · «los archivos» (1) | Sí | BAJA |
| restaurant-business-plan | 18 / 1 | (anonimizadas) | Sí | BAJA |
| bakery-business-plan | 2 / 0 | — | Sí (con «pastry business plan» a propósito) | BAJA |
| bar-business-plan | 0 / 0 (sin filas) | — | Sí | BAJA |
| catering-business-plan | 0 / 0 (sin filas) | — | Sí | BAJA |

Volúmenes US medidos hoy (DataForSEO, búsquedas al mes): employee schedule template **5.400** · work schedule template 5.400 ·
restaurant schedule template 170 · restaurant scheduling template 170 · restaurant employee schedule template 20 · **staff rota template 10** ·
food cost calculator **1.900** · recipe cost calculator **880** · food cost template 170 · menu costing template 170 · recipe costing template 140 ·
food cost spreadsheet 110 · plate cost calculator 50 · recipe cost card 30 · restaurant inventory spreadsheet **320** · restaurant inventory sheet **320** ·
par sheet **260** · restaurant inventory template 210 · bar inventory template 140 · bar inventory spreadsheet 90 · haccp plan template **390** ·
food temperature log **320** · temperature log sheet 210 · food safety checklist 210 · kitchen temperature log 140 · cooling log 110 · haccp template 110 ·
food safety logs **50** · restaurant cleaning checklist 320 · restaurant p&l template 140 = restaurant profit and loss template 140 · restaurant budget template 70 ·
restaurant pro forma 20 · restaurant financial plan 20 · restaurant financial projections 10 · ai for restaurants 720 (intención sin verificar) ·
«ai prompts for restaurants», «chatgpt prompts for restaurants», «chatgpt prompts for chefs», «chef prompts», «ai for chefs»: **sin volumen en DataForSEO** ·
**ghost kitchen 33.100 frente a dark kitchen 1.900** · **bbq catering 9.900 frente a grill catering 1.000** · restaurant templates 480 ·
restaurant business plan example 390 · restaurant opening and closing checklist 50 · restaurant side work checklist 30 · catering business plan template 90 ·
coffee shop business plan pdf 40 · restaurant business plan pdf 30 · food truck business plan pdf 20.
SERP «food cost calculator» (US): AI Overview con calculadoras online (Supy, StockTake, Rinvy), pero en el puesto 3 está «Free Food Cost Calculator
for Excel» (eatapp) y entre las búsquedas relacionadas salen «food cost calculator excel» y «free food cost calculator excel»: hay hueco para la intención Excel.

## 2. Cambios propuestos (ALTA y MEDIA)

### Hub — ALTA
- Meta `astro-site/src/pages/en/digital-products.astro:20`: «…recipe costing spreadsheets… **English editions coming soon**» está obsoleta (hay 12 vivos y el
  «recipe costing» se cambió por «food cost» el 24-sep) → «Restaurant templates for Excel and business plan kits: food cost calculator, inventory sheets,
  HACCP temperature logs, employee schedules, P&L and business plans for restaurants, bars, bakeries, food trucks and caterers. From $14.» (restaurant templates: 480).
- H1 `HUB:1095` «The Digital Products Store for Today's Hospitality» no lleva keyword → «Restaurant Templates & Business Plans for Hospitality Pros» (se mantienen los spans).
- Calcos del ES en los nombres de las tarjetas (el H2 de cada producto):
  - «Dark Kitchen» `HUB:45`, `:508`, `:653` → **«Ghost Kitchen»** (33.100 frente a 1.900).
  - «Business Plan: Grill Catering for Events» `HUB:540` → **«BBQ Catering Business Plan for Events»** (9.900 frente a 1.000; comprobar que la parrilla del Parrillero encaja con lo que en EE. UU. se entiende por BBQ, porque allí BBQ suele ser ahumador).
  - «Recurring Tasks: …» ×20 (`HUB:300`, `:588`–`:894`, `:917`–`:923`), calco de «Tareas recurrentes» → «Opening & Closing Checklists: …» (restaurant cleaning checklist 320; opening and closing 50; side work 30; «recurring tasks» sin medir. La memoria del 11-oct da un clúster de unas 1.800 búsquedas).
  - «Private Chef / At-Home Showcooking» `HUB:572` → «Private Chef / In-Home Dining» («showcooking» es un término europeo; sin medir).
  - «Grill House / Josper Grill» `HUB:814` → «Steakhouse / Wood-Fired Grill» (Josper es una marca española; sin medir).
  - «Tapas Bar / Gastrobar» `HUB:846` → «Tapas Bar / Gastropub»; «Full Hotel» `HUB:718` → «Full-Service Hotel».
  - «Production Kitchen» `HUB:428`, `:878` y «Workshop» `HUB:318`, `:321`, `:334`, `:337`, `:750`, calcos de «obrador» → «Wholesale Bakery / Commissary Kitchen» y «Chocolatier / Chocolate Kitchen» (sin medir).
  - «Take Your Plan to the City Where You Will Open» `HUB:1559` (calco) → «Opening in a Specific City?».

### food-cost-templates — ALTA
- Title `F/kits/food-cost-templates.ts:23` «Food Cost Kit Pro: 13 Food Cost Templates for Excel» → **«Food Cost Calculator & Recipe Costing Templates for Excel | AI Chef Pro»** (calculator 1.900 + recipe cost calculator 880 frente a template 170; la SERP admite la intención Excel).
- H1 `:133` titlePost «: 13 Excel Templates to Control Your Food Cost» → «: Food Cost Calculator & 13 Recipe Costing Templates for Excel».
- H2 `:155` « Professional Food Cost Templates» → « Food Cost & Recipe Costing Templates».
- FAQ `:72` y `:278` «How do I calculate GP %?» (GP es británico: GSC trae «food gp calculator excel») → «How do I calculate gross profit (GP %) on a dish?», para cubrir los dos mercados.
- Tarjeta `:162` «starter, main, dessert» (británico) → «appetizer, entrée, dessert».
- «supplier» en `:77`, `:171`, `:172`, `:283` → «vendor» (es lo que dice la cocina US y ya lo usa la landing de inventario).

### restaurant-schedule-templates — ALTA
- Title `F/kits/restaurant-schedule-templates.ts:40` «…Restaurant Schedule Template & **Staff Rota** for Excel» → **«Restaurant Employee Schedule Template for Excel + Overtime & Labor Cost»** (5.400 frente a 10). «Rota» se queda solo en la FAQ UK `:255`, que ya lo explica y recoge las queries UK que llegan hoy.
- H1 `:115` → «Employee Schedule Template, Overtime Tracker & Labor Cost for Excel».
- Tarjeta `:141` «Restaurant Schedule Template: Weekly & Monthly Staff Rota» → «Employee Schedule Template: Weekly & Monthly Shift Schedule».
- Keywords `:44`: quitar «staff rota template, rota template» de cabeza y meter «employee schedule template, work schedule template».
- Testimonios que **contradicen el kit FLSA** `:299` («collective agreement», «social security»), `:300` («Spain's legal limit») y `:302` («follow current Spanish labor rules», «Spain's Labor Inspectorate»): cambiar solo esa frase (regla de John del 11-oct).

### restaurant-inventory-templates — MEDIA
- Title `F/kits/restaurant-inventory-templates.ts:27` → «Restaurant Inventory Kit Pro: Inventory Spreadsheet & Par Sheet Templates for Excel» (spreadsheet/sheet 320 + par sheet 260 frente a template 210; GSC: «restaurants inventory sheets»).
- H1 `:133` «9 Restaurant Inventory Templates for Excel» → «9 Restaurant & Bar Inventory Sheets for Excel» (bar inventory template 140; GSC «bar inventory templates», pos 10,4).
- H2 `:154` « Restaurant Inventory Templates» → « Restaurant & Bar Inventory Sheets». Keywords `:31` «stock take template» (británico) → «inventory count sheet» (sin medir).

### haccp-templates — MEDIA
- Title `F/kits/haccp-templates.ts:35` y H1 `:128` «…HACCP Plan Template, **Food Safety Logs** & Checklists for Excel» → «…HACCP Plan Template, **Temperature Logs** & Food Safety Checklists for Excel» (food safety logs 50 frente a food temperature log 320 + temperature log sheet 210 + kitchen temperature log 140).
- Tarjeta `:169` «Health Inspection Self-Checklist» → «Health Inspection Self-Inspection Checklist» (es como lo llama el xlsx 15; sin medir).

### ai-prompts-for-restaurants — MEDIA
- Title `F/ebooks/ai-prompts-for-restaurants.ts:27` «Gastro Pro Prompts eBook: 300 AI Prompts…» → «300+ AI & ChatGPT Prompts for Chefs and Restaurants (eBook) | AI Chef Pro» (GSC: «chef prompt» 12, «chef ai prompt» 3; DataForSEO no da volumen para las variantes).
- H1 `astro-site/src/components/pages/ProPromptsEbookPageEn.astro:246` «The Only AI Prompts eBook for Restaurants & Hospitality You'll Ever Need» → «300+ AI Prompts for Chefs & Restaurants: The ChatGPT Prompts eBook».
- Nombre del producto (capa 1, **decide John**): «Gastro» es un apócope europeo de gastronomía; en EE. UU. suena a gastroenterología o a gastropub. Propuesta: «AI Prompts for Chefs & Restaurants eBook» (`:24`, `:36`, `:41`, `:53`, y los enlaces cruzados `F/kits/*:325/:308/:360/:362`).
- Las 6 FAQ hablan de acceso y formato; ninguna está escrita como lo busca el comprador. Reescribir 2 como «How can chefs use ChatGPT in the kitchen?» y «What are the best ChatGPT prompts for restaurants?» (sin medir; PAA no consultado).

### restaurant-financial-plan-templates — MEDIA
- Title `F/kits/restaurant-financial-plan-templates.ts:106`: es la query con más impresiones de toda la tienda («restaurant p&l template», 13, pos 14,6), pero va detrás del nombre del kit → «Restaurant P&L Template & Budget for Excel + Financial Projections | AI Chef Pro» (p&l 140 = profit and loss 140; budget 70; financial projections 10).
- Testimonios con «EUR» y «Spanish banks» `:280`, `:284`, `:287`: se presentan como de la edición española (`:278`), así que no hay contradicción. Baja prioridad.

### coffee-shop-business-plan — MEDIA
- «how to open a coffee shop» tiene 1.300 búsquedas/mes (medido el 13-oct, memoria `project_english_expansion`). Las landings Restaurant y Bar tienen la FAQ «…step by step?» y la del Coffee Shop no: añadirla en `F/planes/coffee-shop-business-plan.ts` (bloque FAQ, ~`:90`) y meter «how to open a coffee shop» en la meta.

### Transversal (BAJA)
- H1 de los 6 planes: el HTML pega «Business Plan» con «Template» (`<span>Business Plan</span><span class="block">Template…`), así que el texto del H1 queda «Business PlanTemplate». Arreglo: un espacio al principio de titleSubtitle (`F/planes/food-truck…:162`, `coffee-shop…:152`, `restaurant…:170`, `bakery…:166`, `bar…:164`, `catering…:181`).
- Alt de imagen: todas las fotos del hero y la galería llevan `alt=""` (decorativas, con ficheros en español: `croqueta-jamon.jpeg`, `tareas-bar-*.jpg`). El único alt descriptivo es el del eBook. El schema `Product` no tiene `keywords`.
- Restaurant BP: «restaurant business plan example» (390) apenas aparece. Añadir «& Example» al title (`F/planes/restaurant-business-plan.ts`).
- Testimonios de España con «tapas bar/gastrobar» en el Bar `F/planes/bar-business-plan.ts:202`–`:209` y con EUR en Inventory `:333`–`:334`, FT `:201`, Bakery `:209` y Restaurant `:213`: van etiquetados como de la edición española y es decisión de John. Solo señalo que «gastrobar» no es jerga US.

## 3. Capa 2 (muestra: pestañas y rótulos de 8 xlsx; openpyxl no está en /usr/bin/python3, así que he leído el XML con zipfile)
- **Muy nativo** (bien): par sheet (Par Level, On Hand, Beef tenderloin PSMO, Shrimp 16/20), Bar startup costs (second-generation space, Type I hood,
  grease interceptor, high-tops), catering (drop-off, guest minimum, service charge taxable by state), HACCP (Priority / Priority foundation / Core,
  walk-in 32-41 °F), schedule (AM/PM, DBL, Vacation/PTO, clopening).
- **Británico**: pestañas «Starter» y «Main» en `public/dl/food-cost-templates/03-prix-fixe-set-menu-costing.xlsx` y «2. Starter» en `02-tasting-menu-costing.xlsx`
  (en EE. UU. se dice «Appetizer» y «Entrée»); «GP %» repetido en 02, 03, 04, 05, 07 y 08 (→ «Gross margin % (GP)»); el rótulo interno de
  `restaurant-schedule-templates/01-…xlsx` también pone «Weekly & Monthly Staff Rota»; «Staff changing rooms» en HACCP 15 (→ «Employee dressing/locker area»).
- **Calcos del ES**: «Traffic Light» (de «semáforo») ×12 en `restaurant-financial-plan-templates/05-…`, también en 03 y 06, en `03-labor-cost-calculator` y en los
  6 `*-financial-projections.xlsx` de los planes (→ «Status» o «Flag»); «Food cost (raw materials)» (de «materias primas») en financial 01, 01b y 05 (→ «Food cost (COGS)»).
- «supplier» aparece mucho en todos los libros. «vendor» es lo más US en restaurantes, pero «supplier» se entiende: baja prioridad.

## 4. Top-10 arreglos (impacto/esfuerzo; todos de texto, sin tocar diseño ni estructura)
1. **Schedule**: «Staff Rota» → «Employee Schedule Template» en title, H1 y tarjeta (`restaurant-schedule-templates.ts:40`, `:115`, `:141`, `:44`). 5.400 frente a 10.
2. **Food Cost**: «Food Cost Calculator & Recipe Costing Templates» en title, H1 y H2 (`food-cost-templates.ts:23`, `:133`, `:155`). 1.900 + 880 frente a 170.
3. **Hub**: meta obsoleta («coming soon», «recipe costing») y H1 sin keyword (`digital-products.astro:20`, `HUB:1095`).
4. **Hub**: «Dark Kitchen» → «Ghost Kitchen» (`HUB:45`, `:508`, `:653`) y «Grill Catering» → «BBQ Catering» (`HUB:540`). 33.100 frente a 1.900 y 9.900 frente a 1.000.
5. **Schedule**: los 3 testimonios que contradicen el kit FLSA (`:299`, `:300`, `:302`). Se cambia solo la frase.
6. **Inventory**: «Inventory Spreadsheet / Sheets & Par Sheet» en title, H1 y H2 (`restaurant-inventory-templates.ts:27`, `:133`, `:154`). 320/320/260 frente a 210, y GSC lo confirma.
7. **HACCP**: «Food Safety Logs» → «Temperature Logs» en title y H1 (`haccp-templates.ts:35`, `:128`). 50 frente a 320 + 210 + 140.
8. **eBook**: keyword delante de la marca, con «ChatGPT» y «Chefs», en title y H1 (`ai-prompts-for-restaurants.ts:27`, `ProPromptsEbookPageEn.astro:246`). Que John decida si se cambia el nombre «Gastro».
9. **Hub**: «Recurring Tasks» ×20 → «Opening & Closing Checklists», más Showcooking, Josper, Workshop, Production Kitchen, Gastrobar y Full Hotel (`HUB`, líneas en §2).
10. **Financial**: «Restaurant P&L Template» al principio del title (`restaurant-financial-plan-templates.ts:106`). Es la query con más impresiones de la tienda y está en la posición 14,6.
Después: FAQ «how to open a coffee shop» (1.300), el espacio del H1 en los 6 planes, «starter/main/GP %» en la ficha del Food Cost (`:72`, `:162`, `:278`) y la capa 2
(Starter/Main, Traffic Light, raw materials, Staff Rota). La capa 2 obliga a regenerar los xlsx en el VPS y pasar los gates, así que va en otra tanda.
