# Recipe Costing Kit — F1 · Research de mercado US/UK

> Sesión Claude Code, **24-sep-2026**. Fase F1 del primer producto de la «Tienda internacional en inglés»
> (`scripts/productos-digitales/TIENDA-INTERNACIONAL.md`). Producto = **copia traducida del Kit de Escandallos Pro
> (12 €)** adaptando variables de mercado. Este documento alimenta la SPEC de diferencias ES→EN; no decide diseño.
>
> **Leyenda de datos:** `[medido DFS 24-sep]` = DataForSEO (US = 2840/en, UK = 2826/en) medido hoy ·
> `[fuente: URL]` = dato leído en esa página · `[fuente secundaria]` = blog de software o resumen de buscador, no
> fuente primaria · `[estimado]` = razonamiento propio · `[no medido]` = no se pudo medir y se dice.
> Los volúmenes del 23-sep (§2 del doc canónico) no se repiten: aquí se amplían.
>
> Restricción de la sesión: Mac con límite térmico → sin navegador, sin builds, sin Playwright. Etsy, Toast,
> RestaurantOwner y DoorDash devuelven 403 a WebFetch; los precios de Etsy se sacaron de los *rich snippets* de la SERP
> vía DataForSEO.

---

## 0. Recomendaciones en una tabla

| Tema | Recomendación | Base |
|---|---|---|
| **Precio** | **$19** (pago único, acceso de por vida). Revisar a **$24** cuando haya reseñas EN reales | §5 |
| **Monedas locales** | Precios manuales en el Price de Stripe (`currency_options`: GBP, CAD, AUD a escalón psicológico) mejor que depender de Adaptive Pricing; **verificar que USD es moneda de liquidación de la cuenta** o Adaptive Pricing no convierte | §5.3 |
| **Slug** | **Se confirma `recipe-costing-kit`**; la keyword «food cost templates» va al `title`/H1/meta, no al slug | §6.4 |
| **Impuesto** | 2 celdas por hoja: «Tax rate (%)» + «Menu prices include tax? (Yes/No)». Por defecto **No / 0 %** (EE. UU.); UK = Yes/20 %, AU = Yes/10 %, CA = No/5-15 % | §3 |
| **Unidades** | Sin interruptor global: la columna «Factor» ya convierte cualquier pareja. Ampliar la hoja *Conversions* con US customary + métrico + imperial UK; ejemplos en lb/oz/fl oz | §4 |
| **Moneda en celdas** | Formato numérico **sin símbolo** (`#,##0.00`) + celda «Currency» en el bloque de ajustes | §3.3 |
| **Terminología UK** | Mostrar **GP %** (= 1 − food cost %) junto al food cost %: es como habla la hostelería británica («gp calculator» = 5.400/mes en UK) | §1, §6 |
| **Google Sheets** | Las 11 funciones del kit existen en Sheets; los riesgos son **protección de hoja, desplegables que leen otra hoja y el texto de Instrucciones** (Excel-only). Gate de conversión real en F2 | §8 |
| **Benchmarks** | Corregir 4 filas de la calculadora al pasar a EN (fine dining, bar, catering, pastelería) | §2.3 |
| **No prometer** | «Menu engineering» NO está en el kit (vive en la Guía Food Cost + Ingeniería de Menú). El doc canónico §2 lo lista como diferencial: no debe ir a la landing EN | §6.5 |

---

## 1. Glosario ES → EN (EE. UU. base; variantes UK/CA/AU)

### 1.1 Conceptos del kit

| ES (kit) | EN · EE. UU. (usar) | UK / CA / AU | Nota |
|---|---|---|---|
| Escandallo | **Recipe cost card** · plate cost sheet | UK: *dish costing sheet* / *recipe costing sheet* | «Recipe costing» es el término del oficio (escuelas, CIA); «plate cost» es jerga de cocina US |
| Ficha técnica | **Standardized recipe** · recipe spec | UK: *recipe spec sheet* | |
| Coste por ración | **Cost per portion** · plate cost · cost per serving | UK: *cost per portion* | |
| Nº de raciones | **Number of portions** (yield in portions) | igual | «Yield» también = rendimiento en piezas (05 pastelería: «Yield (units)») |
| Merma (%) | **Waste % (trim loss)** | UK: *wastage* | Nota en cabecera: «Yield % = 100 % − waste %». La fórmula ES `E/(1−H)` ES la de culinary math `APQ = EPQ ÷ yield %` [fuente: https://nicoletcollege.pressbooks.pub/culinarymath/chapter/2-3-calculating-as-purchased-edible-portion-quantities/] |
| Cantidad (en ud. de uso) | **Recipe qty (EP)** — edible portion | igual | |
| Cant. bruta | **AP qty** (as purchased) | igual | |
| Ud. compra / Ud. uso | **Purchase unit** / **Recipe unit** | igual | |
| Precio/Ud (€) | **Price per purchase unit** | igual | Sin símbolo de moneda (§3.3) |
| Factor | **Conversion factor** | igual | |
| Coste elaboración (%) | **Q-factor (%)** — seasonings, oil, garnish, packaging | UK: *hidden costs (%)* | El Q-factor US cubre condimentos, aceite, guarniciones, envases y sobreproducción; típico 5-10 % [fuente secundaria: https://www.theculinarypro.com/calculating-food-cost · https://www.restaurantbusinessonline.com/advice-guy/costing-recipes]. El ES lo define como energía + envasado + pérdidas de preparación: encaja; mantener 10 % por defecto |
| Food cost objetivo (%) | **Target food cost %** | UK: añadir **Target GP %** calculado | |
| Food cost real (%) | **Actual food cost %** | UK: *actual GP %* | |
| Beverage/pour cost | **Pour cost %** (bar) · beverage cost % | UK: *drinks GP %* / *wet GP* | |
| PVP (sin IVA) | **Menu price (pre-tax)** · selling price | UK: *menu price ex VAT* | |
| PVP con IVA | **Menu price incl. tax** | UK: *menu price inc VAT* (= el que se imprime) · AU: *inc GST* | Ver §3 |
| Margen bruto (€) | **Gross profit per portion** · contribution margin | UK: **cash GP** | En menu engineering US: *contribution margin* = precio − coste |
| Margen bruto (%) | **Gross profit %** | UK: **GP %** | |
| Multiplicador | **Markup factor** (price = cost × factor) | igual | |
| IVA | **Sales tax** (US) | UK: **VAT** · CA: **GST/HST (+PST/QST)** · AU: **GST** | Rótulo neutro: «Tax rate (sales tax / VAT / GST)» |
| Menú del día | **Prix fixe lunch** · lunch special | UK: **set lunch menu** / set menu | No existe el concepto español. «prix fixe menu» 5.400/mes US; «set menu» 880 y «set lunch menu» 480 UK [medido DFS 24-sep]. «lunch special» (33.100 US) es búsqueda de comensal local, no de oficio |
| Primer plato / segundo / postre | **Starter / Main / Dessert** | igual | ⚠️ **No usar «entrée»**: en EE. UU. es el principal y en UK/AU el entrante |
| Aperitivo (menú degustación) | **Amuse-bouche** | igual | |
| Menú degustación | **Tasting menu** | igual | 8.100 US / 1.600 UK [medido DFS 24-sep] |
| Pase | **Course** | igual | |
| Pastelería | **Pastry & bakery** | UK: *patisserie* | |
| Catering | **Catering & events** | igual | |
| Pax / comensales | **Guests** | UK: **covers** | |
| Menaje | **Rentals** (tableware & equipment) | UK: *equipment hire* | |
| Camareros / jefe de sala | **Servers / floor manager** | UK: *waiting staff / restaurant manager* | |
| Presupuesto cliente | **Client proposal** · catering quote | UK: *client quote* | |
| Cafetería-brunch | **Café & brunch** | UK: *café & brunch* | |
| Food truck | **Food truck** | UK: *street food van* (nota, no renombrar) | |
| Punto de equilibrio | **Break-even** | igual | |
| Inventario / stock inicial y final | **Inventory** · beginning / ending inventory | UK: **stock** · opening / closing stock · **stocktake** | «stock take template» 140/mes UK [medido DFS 24-sep] |
| Consumo teórico / diferencia | **Theoretical usage** / **variance** (actual vs. theoretical) | igual | |
| Compras / ventas | **Purchases** / **food sales (net of tax)** | UK: *net sales ex VAT* | |
| Comisión plataforma | **Third-party delivery commission** | igual | |
| Escalado de recetas | **Recipe scaling** | igual | «recipe scaling calculator» 390 US / 30 UK [medido DFS 24-sep] |
| Formato de compra (cl) | **Bottle size** (fl oz / ml) | UK/AU: ml / cl | |
| Merma y hielo (%) | **Spillage & ice allowance (%)** | igual | |
| Celdas verdes editables | **Green cells = inputs** | igual | |

**Vocabulario de ingredientes que cambia** (usar la columna US en el kit base y dejar la UK en las Instrucciones):
zucchini/courgette · eggplant/aubergine · cilantro/coriander · scallion/spring onion · arugula/rocket · shrimp/prawns ·
ground beef/beef mince · heavy cream/double cream · all-purpose flour/plain flour · superfine sugar/caster sugar ·
powdered sugar/icing sugar · fries/chips · cookie/biscuit · takeout/takeaway · check/bill · server/waiter ·
inventory/stock. Ortografía: estadounidense (color, flavor) como base [estimado: el mercado base es US].

### 1.2 Nombres de los 13 ficheros

| ES | EN propuesto | Título dentro del fichero |
|---|---|---|
| 01-escandallo-estandar.xlsx | `01-standard-recipe-cost-card.xlsx` | Standard Recipe Cost Card — À la Carte Dish |
| 02-menu-degustacion.xlsx | `02-tasting-menu.xlsx` | Tasting Menu Costing (up to 9 courses) |
| 03-menu-del-dia.xlsx | `03-prix-fixe-lunch-menu.xlsx` | Prix Fixe / Set Lunch Menu |
| 04-cocktails-bebidas.xlsx | `04-cocktails-and-drinks.xlsx` | Cocktail & Drink Costing (Pour Cost) |
| 05-pasteleria.xlsx | `05-pastry-and-bakery.xlsx` | Pastry & Bakery Costing |
| 06-catering.xlsx | `06-catering-and-events.xlsx` | Catering & Event Costing |
| 07-cafeteria-brunch.xlsx | `07-cafe-and-brunch.xlsx` | Café & Brunch Costing |
| 08-food-truck.xlsx | `08-food-truck.xlsx` | Food Truck Costing & Break-Even |
| 09-control-mermas.xlsx | `09-food-waste-tracker.xlsx` | Weekly Food Waste Tracker (UK: wastage log) |
| 10-calculadora-pvp.xlsx | `10-menu-price-calculator.xlsx` | Menu Price Calculator |
| 11-dashboard-food-cost-mensual.xlsx | `11-monthly-food-cost-dashboard.xlsx` | Monthly Food Cost Dashboard |
| BONUS-mermas-inventario.xlsx | `BONUS-inventory-and-waste-control.xlsx` | Inventory & Waste Control (theoretical vs. actual usage) |
| BONUS-guia-food-cost-30-dias.pdf | `BONUS-30-day-food-cost-guide.pdf` | Control Your Food Cost in 30 Days |

### 1.3 Pestañas (≤ 31 caracteres, límite de Excel)

- Comunes: `Instructions` · `Conversions` · `Waste Factors`.
- 01: `Recipe Cost Card`. 02: `1. Amuse-Bouche`, `2. Starter`, `3. Fish`, `4. Meat`, `5. Dessert`, `6. Course`…`9. Course`, `Summary`.
- 03: `Starter`, `Main`, `Dessert`, `Menu Summary`, `Weekly Rotation`. 04: `Bottle Sizes`, `Gin & Tonic`, `Mojito`, `Margarita`, `Aperol Spritz`.
- 05: `Chocolate Cake`, `Croissants`, `Macarons`. 06: `Reception (per guest)`, `Event Quote`, `Event Checklist`, `Client Proposal`.
- 07: `Avocado Toast`, `Açaí Bowl`, `Eggs Benedict`, `Carrot Cake`.
- 08: `Smash Burger`, `Loaded Fries`, `Pulled Pork Sandwich`, `Break-Even`. 09: `Weekly Waste Log`, `Trend`.
- 10: `Menu Price Calculator`. 11: `Dashboard`. BONUS: `Inventory`, `Sales for the Period`, `Waste Checklist`.
- ⚠️ Las fórmulas citan nombres de hoja (`'Resumen'!$C$12`, `Mermas!$A$5:$A$25`, `Conversiones!…`): el renombrado tiene que hacerse **en el motor**, no con buscar y reemplazar sobre el xlsx.

### 1.4 Las 21 categorías de la hoja «Mermas» → «Waste Factors»

Beef & red meat · Poultry · Fish · Shellfish · Leafy greens · Root vegetables · Fruiting vegetables · Fruit · Dairy ·
Dry goods & grains · Frozen · Bread & pastry · Eggs · Oils & fats · Herbs & spices · Chocolate & cocoa ·
Beverages & spirits · Mushrooms · Canned & pickled · Sauces & condiments · Pasta & rice.

---

## 2. Benchmarks de food cost

> No hay fuente primaria pública y gratuita: el *Restaurant Operations Report* de la National Restaurant Association es de
> pago. Lo publicado son blogs de proveedores de software (R365, Backbar, Jelly…), útiles como consenso pero
> **secundarios**. El único dato primario encontrado es el de una cadena cotizada (Chipotle, SEC/IR).

### 2.1 EE. UU.

| Tipo de negocio | Rango | Fuente |
|---|---|---|
| General (restaurante) | 28-35 % | [fuente secundaria: https://www.restaurant365.com/blog/cooking-up-success-understanding-what-is-a-good-food-cost-percentage/] |
| Fast casual (dato real) | **29,6 %** de los ingresos en 2025 (food, beverage **and packaging**); 29,8 % en 2024 | [fuente: https://ir.chipotle.com/2026-02-03-CHIPOTLE-ANNOUNCES-FOURTH-QUARTER-AND-FULL-YEAR-2025-RESULTS] |
| QSR / fast casual | 25-30 % | [fuente secundaria, resumen de buscador sobre https://www.xenia.team/articles/average-restaurant-food-cost] |
| Full-service / casual | 28-32 % | ídem |
| Fine dining | 30-35 % (hasta 34-40 %) | ídem |
| Por formato (tabla completa) | QSR 25-30 · fast casual 27-32 · casual 28-35 · fine dining 30-38 · pizzería 22-28 · café/bakery 25-35 · bar food 28-38 · catering 28-35 · delivery/ghost 28-32 | [fuente secundaria: https://cucinovo.com/blog/food-cost-percentage-by-restaurant-type] ⚠️ elaborada con informes de **Austria y Alemania** (WKO, DEHOGA), no de EE. UU. |
| Bar — pour cost global | **18-24 %**, media 20 % | [fuente: https://www.restaurant365.com/blog/metric-monday-how-to-calculate-liquor-cost-in-a-restaurant/] · [fuente: https://www.getbackbar.com/liquor-cost-bars-restaurants] |
| Bar — por categoría | destilados 18-20 %; cerveza de barril ≈ 20 %; botella ≈ 25 %; vino más alto | [fuente: https://www.getbackbar.com/liquor-cost-bars-restaurants] |
| Café / coffee shop (COGS) | 25-35 % | [fuente secundaria, resumen de buscador: https://freshcup.com/understanding-key-coffee-shop-metrics/ y otras] |
| Bakery & café | 25-35 %; pan 15-22 %, bollería/croissant 12-20 %, bebidas de café 8-15 % | [fuente secundaria: https://vellinapp.com/blog/bakery-food-cost-percentage] |
| Catering | 28-35 % (alta gama ~25 %, volumen hasta 40 %) | [fuente secundaria, resumen de buscador: https://www.galleysolutions.com/blog/how-to-price-a-catering-menu-for-profitability y otras] |
| Food truck | 25-35 %; objetivo ajustado 25-30 % | [fuente secundaria, resumen de buscador: https://mobilefoodmath.com/guides/food-truck-menu-pricing y otras] |
| Prime cost (food + labor) | < 65 % de ventas | [fuente secundaria, resumen de buscador: https://www.xenia.team/articles/average-restaurant-food-cost] |

### 2.2 Reino Unido (la hostelería británica habla en **GP %**)

| Métrica | Rango | Fuente |
|---|---|---|
| GP % comida | 65-70 % (= food cost 30-35 %) | [fuente secundaria: https://blog.getjelly.co.uk/restaurant-gross-profit-margin-benchmarks/] |
| GP % bebidas | 65-80 %; destilados 75-82 % (= coste 18-25 %) | ídem |
| GP % mezcla restaurante | mediana 63-68 %; los mejores 65-70 % | ídem |
| Pubs y bares | 70-80 % | ídem |
| Alarma | GP < 60 % · food cost > 35 % · prime cost > 70 % | ídem |
| Base de cálculo | GP sobre ventas **netas de VAT** (usar el precio con VAT infla el resultado ~17 %) | [fuente: snippet SERP de https://blog.getjelly.co.uk/gp-margin-calculator-food-beverage/] |

### 2.3 Qué cambia en `10-menu-price-calculator` (filas del ES frente a las fuentes)

| Fila ES | Rango ES | Fuentes US/UK | Propuesta EN |
|---|---|---|---|
| Fine Dining | 25-28 % | 30-35 % (hasta 38-40 %) | **30-35 %** ⚠️ el ES está por debajo de toda fuente encontrada |
| Casual Dining | 28-32 % | 28-32 / 28-35 % | 28-32 % (igual) |
| Fast Casual | 30-35 % | 27-32 %; Chipotle 29,6 % | **27-32 %** |
| Cafetería | 25-30 % | 25-35 % | 25-30 % (igual; bebidas de café bajan la media) |
| Catering | 30-40 % | 28-35 % | **28-35 %** |
| Food Truck | 28-35 % | 25-35 % | 28-35 % (igual) |
| Hotel F&B | 30-35 % | [no medido] | 30-35 % (igual, marcado sin fuente) |
| Pastelería | 20-30 % | 25-35 % (producto 12-22 %) | **25-35 %** |
| Bar/Cócteles | 20-25 % | pour cost 18-24 % | **18-24 %** (y en el 04 y la landing, un único rango) |
| Delivery | 28-32 % s/neto + 30 % comisión | DoorDash 15/25/30 % (Basic/Plus/Premier); Uber Eats UK 30 % con reparto propio de la plataforma | FC s/neto igual; **comisión por defecto 25 %** (US base), nota «UK ≈ 30 %» |

Comisiones: [fuente secundaria, resumen de buscador sobre https://merchants.doordash.com/en-us/pricing (403 a WebFetch) y https://shopops.co.uk/blog/deliveroo-uber-eats-just-eat-commission-uk-2026].

---

## 3. Impuestos y precio de carta

### 3.1 Cómo funciona en cada mercado

| Mercado | ¿La carta lleva el impuesto? | Tipos | Fuente |
|---|---|---|---|
| **EE. UU.** | **No.** La carta es antes de impuestos; el *sales tax* se suma en la cuenta. La propina va aparte y no toca el food cost | Estatal + local. Media nacional ponderada **7,53 %**; más altos: Louisiana 10,13 %, Tennessee 9,61 %, Washington 9,57 %, Arkansas 9,48 %, Alabama 9,46 %. Sin impuesto estatal: AK, DE, MT, NH, OR. NY 8,54 · CA 9,03 · TX 8,20 · FL 6,98 · IL 8,98 % | [fuente: https://taxfoundation.org/data/all/state/2026-sales-tax-rates-midyear/ (6-jul-2026)]. Que la carta sea antes de impuestos: práctica generalizada [estimado; no se buscó norma federal porque no existe una única] |
| **Reino Unido** | **Sí.** Los precios al consumidor incluyen VAT y se exhiben (con los cargos de servicio) a la entrada | **20 %** en consumo en local y comida caliente para llevar; comida fría para llevar, tipo cero (salvo excepciones) | [fuente: https://www.gov.uk/guidance/catering-takeaway-food-and-vat-notice-7091 §1.3 y §4.1] · [fuente: https://www.legislation.gov.uk/uksi/2003/2253/made — Price Marking (Food and Drink Services) Order 2003] |
| **Canadá** | **No.** Carta sin impuestos; se suman en la cuenta | GST 5 % (AB, BC, MB, QC, SK, territorios) · HST 13 % ON · **14 % NS (desde 1-abr-2025)** · 15 % NB, NL, PE. Además PST/QST en algunas provincias (QC 9,975 %) | [fuente: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html]. Qué PST se aplica a comidas de restaurante en cada provincia: **[no medido]** |
| **Australia** | **Sí.** Precio total único con GST; recargos de fin de semana/festivo pueden ir aparte **si** la carta dice «A surcharge of [x] % applies on [días]» con la misma visibilidad que el precio | **10 %** GST | [fuente: https://www.accc.gov.au/business/pricing/price-displays] |

### 3.2 Parametrización propuesta (dentro del mandato de §1 del doc canónico: «impuesto… son parámetros del Excel»)

Hoy cada escandallo ES tiene «Tipo de IVA (%)» (10 %) y la fila «PVP CON IVA»; la calculadora 10 tiene uno global.
Propuesta EN, **una sola celda nueva** junto a la del tipo:

| Celda | Valor por defecto (US) | Uso |
|---|---|---|
| `Tax rate (%)` (sales tax / VAT / GST) | **0 %** | UK 20 % · AU 10 % · CA 5-15 % · US: opcional, su tipo local |
| `Menu prices include tax?` (desplegable Yes/No) | **No** | UK y AU = Yes |

Fórmulas (mismo patrón IFERROR del kit):
- `Suggested menu price (pre-tax)` = coste por ración ÷ target food cost (igual que el ES).
- `Menu price to print` = `IF(toggle="Yes", pretax*(1+rate), pretax)` → en UK/AU es el precio con VAT/GST; en US/CA, el de la carta.
- `Current menu price` (entrada, **tal como está impreso en la carta**) → `Net price = IF(toggle="Yes", price/(1+rate), price)`, y el **Actual food cost %** se calcula siempre sobre el **neto**.
- Rótulo UK adicional: `GP % = 1 − food cost %` (ver §2.2).

Por qué el toggle y no solo renombrar filas: un británico teclea el precio de su carta (con VAT); sin el toggle el kit le
calcularía el food cost sobre un precio inflado un 20 % [estimado]. Es la única variación de estructura y va solo en EN:
el gate de F2 (ES regenerado idéntico celda a celda) no se ve afectado si el motor ramifica por `mercado`.

Instrucciones EN: tabla de valores por mercado (la de §3.1) + «US: leave 0 % — menu prices are pre-tax; tips are not
part of food cost».

### 3.3 Moneda

- Los formatos numéricos del ES llevan «€»/rótulos «(€)». En EN: **formato sin símbolo (`#,##0.00`)** y una celda
  `Currency` (por defecto `USD`) en el bloque de ajustes. Un formato con «$» se vería raro en UK/AU y el formato de celda
  no se puede hacer dinámico de forma fiable en Excel y Sheets a la vez [estimado].
- Cero «€» en los entregables EN (ya es un check del §6 del doc canónico).

### 3.4 Aviso fiscal sobre la VENTA del kit (no sobre el Excel)

Un vendedor **no establecido** en el Reino Unido que vende servicios digitales a consumidores británicos debe registrarse
en VAT desde la **primera venta, sin umbral** [fuente secundaria, resumen de buscador; guía oficial:
https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers]. Canadá y Australia
tienen regímenes propios para no residentes y EE. UU. el *economic nexus* estatal **[no medido]**. No cambia el
research del producto, pero sí el precio neto: **decisión de John con su asesor** antes de la F3.

---

## 4. Unidades

### 4.1 Qué usa cada mercado

| Mercado | Cocina | Bar |
|---|---|---|
| EE. UU. | US customary: **lb, oz (peso), fl oz, gal, qt, pt, cup, tbsp, tsp, each, dozen, case** | Chupito estándar **1,5 fl oz** (1 bebida estándar = 12 oz de cerveza al 5 %, 5 oz de vino al 12 %, 1,5 oz de destilado al 40 %) [fuente: https://www.niaaa.nih.gov/alcohols-effects-health/what-standard-drink]. Botella **750 ml = 25,4 fl oz**; pinta de cerveza 16 oz [fuente: https://www.getbackbar.com/liquor-cost-bars-restaurants] |
| Reino Unido | **Métrico** (g, kg, ml, L) | Ginebra, ron, vodka y whisky solo en **25 ml o 35 ml** (o múltiplos) [fuente: https://www.legislation.gov.uk/uksi/1988/2039]; vino en 125/175 ml y múltiplos [fuente secundaria, resumen de buscador sobre la misma Order]; botella de destilado **70 cl**; pinta imperial **568 ml** |
| Canadá | Métrico oficial; en cocina conviven lb/oz | Chupito 1-1,5 oz según provincia y local [fuente secundaria, resumen de buscador; **no verificado por provincia**] |
| Australia | Métrico; **cucharada AU = 20 ml**, taza = 250 ml [estimado, conocido; no verificado en esta sesión] | Medida estándar de destilado **30 ml** [fuente secundaria, resumen de buscador] |

### 4.2 Propuesta

- **Sin interruptor «unit system».** La columna *Factor* ya busca la pareja «compra→uso» en la hoja *Conversions*: basta
  con que la tabla tenga las parejas US, métricas e imperiales. Un interruptor duplicaría fórmulas sin aportar nada.
- **Desplegable de unidades EN** (lista literal, 80 caracteres, bajo el tope de 255 de Excel):
  `lb,oz,kg,g,gal,qt,pt,cup,fl oz,tbsp,tsp,L,ml,cl,each,dozen,bunch,case,can,bottle`.
- **Ejemplos precargados en unidades US** (lb/oz/fl oz/each); las Instrucciones explican que un kit métrico funciona igual.
- **Trampas que el kit debe avisar:** «oz» (peso) ≠ «fl oz» (volumen); la pinta y el galón **US ≠ imperiales**
  (473 ml vs 568 ml; 3,785 L vs 4,546 L); **no** incluir conversiones peso↔volumen (1 cup de harina ≈ 120-125 g,
  depende del ingrediente) [estimado].

### 4.3 Tabla *Conversions* que debería llevar el kit (factores exactos por definición)

| Pareja | Factor | Pareja | Factor |
|---|---|---|---|
| lb→oz | 16 | gal→fl oz | 128 |
| lb→g | 453,59237 | gal→qt / pt / cup | 4 / 8 / 16 |
| lb→kg | 0,45359237 | gal→L | 3,785411784 |
| oz→g | 28,349523125 | qt→fl oz | 32 |
| oz→lb | 0,0625 | pt→fl oz | 16 |
| kg→lb | 2,20462262 | cup→fl oz / tbsp | 8 / 16 |
| kg→oz | 35,2739619 | cup→ml | 236,5882365 |
| g→oz | 0,0352739619 | fl oz→tbsp / tsp | 2 / 6 |
| fl oz→ml | 29,5735295625 | tbsp→tsp | 3 |
| L→fl oz | 33,8140227 | tbsp→ml / tsp→ml | 14,78676 / 4,92892 |
| bottle (750 ml)→fl oz | 25,3605 | bottle (1 L)→fl oz | 33,814 |
| bottle (1.75 L)→fl oz | 59,1745 | bottle (70 cl)→ml | 700 |
| can (12 fl oz)→fl oz | 12 | dozen→each | 12 |
| case→each | 12 (editable: 24…) | imperial pint→ml | 568,26125 |
| UK fl oz→ml | 28,4130625 | imperial gallon→L | 4,54609 |

\+ todas las parejas métricas que ya tiene el ES (kg→g, L→ml, L→cl, cl→ml…). Fuente de los factores US e imperiales:
NIST Handbook 44, Appendix C [fuente: https://www.nist.gov/document/2026-nist-handbook-44-appendix-c] (definiciones
exactas: 1 lb = 0,45359237 kg; 1 US fl oz = 29,5735295625 ml).

---

## 5. Competencia y precio

### 5.1 Qué hay en el mercado

| Oferta | Precio | Qué incluye | Sheets | Reseñas | Fuente |
|---|---|---|---|---|---|
| Airtable «Food Costing Calculator» | Gratis | Food cost % por plato + informes | No (Airtable) | — | [fuente: https://www.airtable.com/templates/food-costing-calculator/exp81QzrI66zOZzkM] |
| spreadsheet123 Recipe Cost Calculator | Gratis (licencia de uso interno) | Ingredientes, mano de obra, suministros por ración, **interruptor imperial/métrico** | **Sí** (y xls/xlsx) | — | [fuente: https://www.spreadsheet123.com/calculators/recipe-cost-calculator.html] |
| chefs-resources Recipe/Plate Cost | **$6,75/mes** (membresía) | AP/EP, yield %, coste por ración, precio por food cost objetivo | No (Excel) | — | [fuente: https://www.chefs-resources.com/kitchen-forms/recipe-template/plate-cost-how-to-calculate-recipe-cost/] |
| RestaurantOwner Menu & Recipe Cost | [no medido] (403) | Libro Excel de coste de recetas | Excel | — | SERP [medido DFS 24-sep] |
| foodcostchef, sheetrix, Apicbase, Eat App, FoodDocs, R365, Galley, aimenupricer | Gratis (captación de SaaS) | Plantilla simple | Varias | — | SERP [medido DFS 24-sep] |
| Etsy — listados individuales | **$1,99-$7** | Una calculadora de receta | Casi todos Excel + Sheets | $5,48 → 4,9★/**121**; $5,82 → 4,9★/6; $7 → 3,9★/2; $1,99 → 1,4★/2 | *rich snippets* SERP [medido DFS 24-sep] |
| Etsy — páginas de categoría | «desde» $1-$3 | — | — | — | ídem |
| Etsy — «Food Cost Management Software in Excel» | $59,16 | Gestión para delis | Excel | — | ídem |
| palmandgracedesigns | $4,90 | Recipe cost (Sheets) | Sí | — | ídem |
| Gumroad (loomiqstudio / foodcosting) | $3,99 / $19 | Excel simple / base Airtable | Excel / Airtable | [no medido] | [fuente secundaria, resumen de buscador; las páginas no dieron precio a WebFetch] |
| **Someka** Food Cost (Sheets) | **$29,95** (1 usuario) · $59,95 (multi) | Hasta 400 recetas, unidades y moneda configurables, sin macros | Sí | 4,58★/12 | [fuente: https://www.someka.net/products/food-cost-google-sheets-template/] |
| Excel Highway Food Cost Calculator | **$39** | Base de ingredientes, subrecetas | **No** (VBA, solo Windows) | 0 | [fuente: https://excelhighway.com/product/food-cost-calculator-excel/] |
| meez (SaaS) | Starter **$19/mes** (anual; $24 mensual) · Pro $89 · Premium $179 | Recetas + costes | — | — | [fuente: https://www.getmeez.com/pricing] |
| MarginEdge (SaaS) | **$350/mes por local** | Facturas, inventario, costes | — | — | [fuente: https://www.marginedge.com/pricing/] |
| Creative Market | [no medido] | No aparece ninguna oferta indexada para estas búsquedas | — | — | búsqueda web 24-sep |

### 5.2 Precio recomendado: **$19**

- El comprador compara con **plantillas sueltas de $2-7** (Etsy) y con **una sola plantilla premium a $30-39**
  (Someka, Excel Highway). El kit son **11 plantillas + 2 bonus**, incluidos formatos que nadie cubre en un paquete
  (bar/pour cost, pastelería, catering con presupuesto, food truck con punto de equilibrio, dashboard mensual).
- **$19 = un mes de meez Starter, para siempre**: argumento de landing honesto y verificable.
- En EN **no hay prueba social** (capa comercial honesta: sin testimonios ni ratings hasta que haya compradores EN):
  un precio por debajo de Someka reduce la fricción [estimado].
- Revisión a **$24** cuando haya reseñas EN reales; **no** subir a $29 de salida: se cruzaría con Someka (4,58★) sin reseñas.
- Coherente con la regla del doc canónico (12 € → escalón USD por encima → $19).

### 5.3 Monedas locales y Adaptive Pricing

- Adaptive Pricing **siempre está activo en Payment Links**, el comprador paga un **2-4 %** de conversión y **no
  convierte a una moneda que ya esté fijada en `currency_options`** del Price [fuente:
  https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md?payment-ui=stripe-hosted].
- ⚠️ **Requisito:** Adaptive Pricing exige que la moneda del precio (USD) sea **una de las monedas de liquidación de
  la cuenta** (misma fuente). Si la cuenta de John solo liquida en EUR, un Payment Link en USD **no se convertirá** y el
  británico verá dólares. **Comprobarlo en el Dashboard antes de crear el link.**
- Recomendación: Price en USD **$19** + `currency_options` manuales a escalón psicológico igual o superior a la
  conversión del día para **GBP, CAD y AUD** [estimado; el tipo de cambio no se midió]. Así UK/CA/AU ven un precio
  redondo y sin el 2-4 %; el resto del mundo queda en Adaptive Pricing.

---

## 6. SERP y keywords

### 6.1 Volúmenes nuevos, EE. UU. [medido DFS 24-sep, 2840/en]

| Keyword | Vol. | Lectura |
|---|---|---|
| menu pricing calculator / menu cost calculator | 1.900 / 1.900 | Mismo grupo que «food cost calculator» (1.900): intención herramienta → la calculadora gratuita del sitio |
| food cost formula | 1.300 | Informativa → FAQ y blog |
| recipe cost calculator | 880 | Herramienta |
| how to calculate food cost | 880 | Informativa → FAQ |
| food cost percentage | 590 | Informativa |
| menu engineering | 480 | Informativa (el kit NO la cubre; §6.5) |
| recipe scaling calculator | 390 | Herramienta |
| yield percentage · plate costing · plate cost | 320 · 320 · 320 | Oficio: usar «plate cost» y «yield» en la landing |
| recipe costing software | 320 | Comparativa SaaS |
| pour cost calculator · pour cost | 260 · 110 | Bar |
| food cost percentage calculator | 260 | Herramienta |
| catering pricing calculator | 210 | Catering |
| restaurant inventory template | 210 | Fuera del kit (ola 1: Inventory Kit) |
| **food cost templates** (= food costing template = menu costing template, mismo grupo de Google Ads) | **170** | Principal |
| **recipe costing templates** (plural) | **140** | Secundaria. El singular «recipe costing template» da **30**: el 140 del doc del 23-sep era el plural |
| bakery pricing calculator · liquor cost calculator | 170 · 140 | Verticales |
| food cost spreadsheet · menu costing spreadsheet · cost per serving calculator | 110 · 110 · 110 | Secundarias |
| food cost calculator excel · food cost excel template | 90 · 70 | «excel» |
| cocktail cost calculator | 70 | Bar |
| food cost sheet · recipe costing sheet · how to cost a recipe · bakery costing spreadsheet · restaurant profit margin calculator | 50 c/u | Cola larga |
| recipe cost card · prime cost calculator · food cost worksheet · recipe cost template | 30 c/u | Cola larga |
| food cost template google sheets · food cost calculator spreadsheet · food cost template free | 20 c/u | «google sheets» existe pero es pequeño |
| menu engineering template · recipe cost card template · recipe costing spreadsheet · restaurant food cost template · recipe costing template google sheets · catering costing template · beverage cost template · restaurant costing templates · recipe costing card · recipe costing excel · coffee shop cost calculator | ≤ 10 | Sin demanda |
| plate cost template · **recipe costing kit** · bar pour cost template · yield test template · liquor cost template · food waste tracking template · food cost kit · food cost template kit | sin dato | Sin demanda medible |
| recipe card template · food truck costing | 4.400 · 2.900 | ⚠️ Intención ajena [estimado, SERP no medida]: fichas de receta de cocina doméstica y «cuánto cuesta un food truck» |

### 6.2 Volúmenes nuevos, Reino Unido [medido DFS 24-sep, 2826/en]

| Keyword | Vol. | Lectura |
|---|---|---|
| **gp calculator** · gross profit calculator | **5.400** · 5.400 | SERP de hostelería: Total Foodservice, Brakes, Bidfood, Crown Cellars, Lynx Purchasing, Jelly → el británico calcula **GP %**, no food cost % |
| food cost calculator · menu pricing calculator | 260 · 260 | Herramienta |
| recipe card template | 210 | Ajena |
| gp percentage | 170 | Informativa |
| menu engineering · stock take template | 140 · 140 | Informativa / inventario |
| how to calculate food cost | 110 | Informativa |
| recipe cost calculator | 70 | Herramienta |
| food cost template = menu costing template | 30 | Principal (pequeña) |
| recipe scaling calculator · plate costing · food gp | 30 c/u | |
| food cost spreadsheet · cocktail cost calculator · food cost percentage · yield percentage | 20 c/u | |
| recipe costing template · recipe costing · dish costing (template) · pour cost calculator · cocktail costing · how to cost a recipe | ≤ 10 | Sin demanda |
| set menu · set lunch menu · prix fixe menu · lunch special · tasting menu | 880 · 480 · 480 · 260 · 1.600 | Nombres de menú (§1) |

### 6.3 SERP [medido DFS 24-sep]

**Quién aparece** (US «food cost template», «recipe costing template», «menu costing template», «food cost spreadsheet»;
UK «food cost template»): Airtable (1.º en tres de las seis SERP), chefs-resources, RestaurantOwner, spreadsheet123, Etsy,
Pinterest, YouTube (varios tutoriales de Sheets), Facebook (grupo con plantilla gratuita de Sheets), Reddit
r/restaurantowners, foodcostchef, sheetrix, jotform, Apicbase, R365, Galley, aimenupricer, Florosa (microbakeries),
Unilever Food Solutions UK (calculadora gratuita). Plantilla de colegios de Victoria (Australia) presente en US y UK.

**Intención y formatos:** comercial-informativa con sesgo **gratuito**. Las relacionadas son «free», «pdf», «google
sheets», «excel». Dominan landings de plantilla descargable y tutoriales en vídeo. **AI Overview** en «recipe costing
template» y «food cost spreadsheet»: enumera las columnas esenciales (ingredient, purchase unit, purchase cost, recipe
unit, amount used, yield per batch, servings, overhead & labor) → la landing debe **listar las columnas del kit
literalmente** y enseñar capturas. Bloques de vídeo e imágenes en todas → demo corta (Loom) y capturas con `alt`.

**People Also Ask (guion de la FAQ)** — US «food cost template»: *Is there a free template for calculating food costs? ·
How do I calculate my food cost? · How to make food costing in Excel? · What is the best app for calculating food costs? ·
Is there a free way to calculate the cost of a recipe? · How to calculate food cost for a recipe formula? · Is 30% a
typical food cost? · How to calculate the cost of a food product?* — «menu costing template»: *How do I calculate the cost
of a menu? · How to calculate what to charge for a menu item? · What are the 7 menu pricing methods? · What is the
30/30/30 rule for restaurants? · What is the normal markup on restaurant food? · What is the food cost equation?* —
«recipe costing template»: *How to calculate recipe cost? · Can you provide a free spreadsheet for baking costing?* —
UK «food cost template»: *Is the 32.8% food cost acceptable? · What is the 30/30/30/10 rule in restaurants? · What is a
30% food cost?* — UK «gp calculator»: *How do you calculate GP%? · How to calculate 60% GP? · What is a good GP ratio? ·
How do I calculate gross profit percentage in Excel?*

**FAQ propuesta para la landing EN (8):** Does it work in Google Sheets? · Is 30 % a typical food cost? · How do I
calculate food cost for a recipe (formula)? · What's the difference between AP and EP (yield)? · Can I use ounces and
pounds — or grams? · How does it handle sales tax and VAT? · How do I calculate GP % (UK)? · Why pay when there are free
templates? · Is it a subscription? (no: pago único, acceso de por vida).

### 6.4 Slug: se confirma `recipe-costing-kit`

- Plantilla: «food cost templates» 170 frente a «recipe costing templates» 140 (US); en UK 30 frente a 10. Calculadora:
  «food cost calculator» 1.900 frente a «recipe cost calculator» 880. La redacción «food cost» gana, pero **no por un
  orden de magnitud** en la intención de plantilla.
- «recipe costing» es el término del oficio y cubre también bebidas (pour cost), que «food cost» no nombra.
- El slug pesa poco frente a `title`/H1/contenido; ya figura en `FAMILIAS` de `tienda.ts` y en la tarjeta del hub.
- Propuesta de `title`: **«Recipe Costing Kit: 11 Food Cost Templates for Excel & Google Sheets»**; H1 «Recipe Costing
  Kit»; en el cuerpo: food cost template, recipe costing templates, menu costing template, food cost spreadsheet, plate
  cost, pour cost, yield %; «GP %» en la FAQ para UK.
- Única alternativa defendible: `food-cost-templates`. No la recomiendo por lo anterior.

### 6.5 Dos avisos para la landing

1. **«Menu engineering» no está en el kit** (ni matriz estrella/caballo/puzzle/perro): vive en la Guía Food Cost +
   Ingeniería de Menú (ES). El doc canónico §2 la cita como diferencial del piloto → **quitarla** de cualquier copy EN.
2. La landing ES afirma «Puedes importar los .xlsx a Google Sheets y **todas las fórmulas se mantienen**» sin gate que
   lo haya comprobado (`astro-site/src/data/productos/kits/kit-escandallos.ts:59-60`). En EN la frase solo sale tras el
   gate de §8.3.

---

## 7. Normativa (solo lo pertinente para un kit de costes)

| Tema | EE. UU. | Reino Unido | Uso en el kit |
|---|---|---|---|
| Alérgenos | **9 principales**: leche, huevo, pescado, crustáceos, frutos de cáscara, cacahuete, trigo, soja y **sésamo** (FASTER Act, vigente desde 1-ene-2023) [fuente: https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies] | **14**: apio, cereales con gluten, crustáceos, huevo, pescado, altramuz, leche, moluscos, mostaza, frutos de cáscara, cacahuete, sésamo, soja, sulfitos > 10 ppm. **Natasha's Law**: etiquetado completo de ingredientes en PPDS desde **1-oct-2021** [fuente: https://www.food.gov.uk/business-guidance/allergen-guidance-for-food-businesses (resumen de buscador; la página redirige a gov.uk)] | Solo una línea en el «Event Checklist» de catering: «Allergen matrix (US: 9 major · UK/EU: 14)». Un kit de costes no es un plan de alérgenos |
| Calorías en carta | Cadenas con **20 o más locales**: calorías en carta + frase de 2.000 kcal; en vigor desde el 7-may-2018 [fuente: https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/menu-labeling-requirements] | Inglaterra: empresas con **250 o más empleados**, desde el **6-abr-2022** [fuente: https://www.legislation.gov.uk/ukdsi/2021/9780348223538] | No aplica al coste; como mucho una nota en Instrucciones. **No** añadir columna de calorías (sería producto nuevo) |
| Medidas de bar | — | Destilados en 25/35 ml [fuente: https://www.legislation.gov.uk/uksi/1988/2039] | Nota en el 04 |
| Precio en carta | Práctica: antes de impuestos | VAT incluido y cargos de servicio visibles [fuente: https://www.legislation.gov.uk/uksi/2003/2253/made] | §3 |
| Australia | — | — | Precio total con GST y aviso de recargo [fuente: https://www.accc.gov.au/business/pricing/price-displays] |
| Canadá (alérgenos) · Australia (PEAL) | — | — | **[no medido]**: fuera del alcance de un kit de costes |

El anexo FDA Food Code / FSA de la arquitectura (§1 del doc canónico) es para el HACCP Pack, no para este kit.

---

## 8. Compatibilidad con Google Sheets

### 8.1 Qué usa hoy el kit ES (censo de los 12 xlsx con openpyxl, 24-sep)

| Rasgo | Dónde | Recuento |
|---|---|---|
| Funciones | todos | IF, IFERROR, VLOOKUP, SUM, COUNTIF, ROUND, ROUNDUP, MAX, AVERAGE, SUMPRODUCT, NA → **las 11 existen en Sheets** [fuente: https://support.google.com/docs/table/25273] |
| Validación de datos (desplegables) | 01-08, BONUS | 58 en total; **28 leen un rango de OTRA hoja** (`Mermas!$A$5:$A$25`) |
| Formato condicional | 01-09, 11 | 66 reglas (`cellIs = "?"` y expresiones sobre la misma hoja) |
| Hojas protegidas sin contraseña | todos | 43 hojas |
| Gráficos | 09 y 11 | 2 LineChart, con `NA()` para los huecos |
| Celdas combinadas | todos | hasta 164 en el 02 |
| Tablas estructuradas · nombres definidos · macros · imágenes | — | **0** (bien) |
| Claves con «→» en VLOOKUP y emojis en rótulos (📋 📷) | 01-08 | texto Unicode normal [estimado: sin riesgo] |

### 8.2 Riesgos y reglas

| # | Riesgo | Qué hacer | Fuente |
|---|---|---|---|
| 1 | **Protección de hoja**: en el modo de edición de Office de Sheets no existe «Protected sheets and ranges»; hay que convertir el archivo. Si la protección de Excel sobrevive a la conversión: **[no medido]** | Mantenerla (sirve en Excel) y dar en Instrucciones la ruta de Sheets: *Data → Protect sheets and ranges*. Las instrucciones actuales («Revisar → Desproteger hoja») son solo de Excel | [fuente: https://support.google.com/docs/answer/1218656] |
| 2 | **Desplegables que leen otra hoja** (28): la ayuda oficial no documenta su conversión; en el foro de Google hay casos de validaciones de Excel que al convertir dan «violates the data validation rules» o desaparecen | Probar en F2 (§8.3). Plan B si fallan: copiar la lista de categorías a una columna auxiliar oculta de la MISMA hoja. La lista literal no cabe: las 21 categorías EN suman 270 caracteres y el tope de Excel es 255 | [fuente: https://support.google.com/docs/thread/5819132] (hilo; contenido no legible por WebFetch) |
| 3 | **Formato condicional con fórmula**: en Sheets **solo puede referenciar la misma hoja**; para otra hay que usar INDIRECT | Gate: ninguna fórmula de formato condicional con «!». Hoy se cumple | [fuente: https://support.google.com/docs/answer/78413] |
| 4 | **Gráficos**: los de línea/barra simples suelen convertirse; el formato personalizado puede volver al de por defecto | Aceptable (2 gráficos de línea). Comprobar en F2 | [fuente secundaria: resumen de buscador] |
| 5 | **Funciones modernas**: XLOOKUP, LET, LAMBDA y FILTER existen en Sheets pero no en Excel 2016/2019 | Mantener el juego clásico del ES; nada de matrices dinámicas ni macros | [fuente: https://support.google.com/docs/table/25273] |
| 6 | **Tablas de Excel**: desde el 11-ago-2026 Sheets las importa como tablas de Sheets | El kit no usa tablas: no hace falta cambiar | [fuente: https://workspaceupdates.googleblog.com/2026/08/improved-file-import-google-sheets-tables.html] |
| 7 | **Foto del plato**: la instrucción «Desproteger → Insertar → Imagen» es de Excel | Añadir «Google Sheets: Insert → Image → Image over cells» | [estimado] |
| 8 | `showDropDown=True` en openpyxl **oculta** la flecha (semántica invertida) | Gate: `showDropDown` falso en todas las validaciones | [fuente: https://openpyxl.readthedocs.io/en/stable/validation.html] |
| 9 | Valores cacheados: Sheets recalcula al importar | Seguir con `inject_cache.py` por Excel y visores; no afecta a Sheets | [estimado] |

### 8.3 Gate propuesto para F2 (sin navegador)

Subir cada xlsx EN a una carpeta de prueba de Google Drive **convirtiéndolo a Google Sheets** (conector de Google
Drive), volver a leerlo o exportarlo a xlsx y comparar: (a) valores calculados frente a los de pycel/caché; (b) que
existen las validaciones, el formato condicional y los dos gráficos; (c) qué pasa con la protección. Necesita el visto
bueno de John para escribir en su Drive (y borrar después). **Que el conector convierta formatos no está verificado.**
Hasta entonces, la landing EN no afirma «all formulas work in Google Sheets».

---

## 9. Datos de ejemplo realistas (EE. UU.)

### 9.1 Precios de referencia

**Minoristas, media urbana de EE. UU., agosto de 2026** — BLS Average Price Data. Son precios de supermercado: sirven de
techo razonable, **no** son precios de distribuidor (Sysco, US Foods, cash & carry) [estimado].

| Ingrediente | Precio ago-2026 | ago-2025 | Fuente |
|---|---|---|---|
| Flour, white, all-purpose | $0,548/lb | $0,557 | [fuente: https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandmidwest_table.htm] |
| Sugar, white | $1,024/lb | $1,040 | ídem |
| Rice, white | $1,111/lb | $1,059 | ídem |
| Spaghetti & macaroni | $1,374/lb | $1,294 | ídem |
| Bread, white pan | $1,823/lb | $1,841 | ídem |
| Ground beef, 100 % beef | $6,923/lb | $6,318 | ídem |
| Chuck roast, USDA Choice | $9,448/lb | $8,845 | ídem |
| Sirloin steak, USDA Choice | $14,357/lb | $14,319 | ídem |
| Bacon, sliced | $6,605/lb | $7,208 | ídem |
| Chicken, whole fresh | $2,012/lb | $2,076 | ídem |
| Chicken breast, boneless | $4,173/lb | — | [fuente: https://fred.stlouisfed.org/data/APU0000FF1101] (serie BLS) |
| Eggs, grade A large | $2,272/dozen | $3,587 | [fuente: tabla BLS citada] |
| Milk, whole | $4,229/gal | $4,171 | ídem |
| Butter, stick | $4,021/lb | — | [fuente: https://fred.stlouisfed.org/data/apu0000fs1101] (serie BLS) |
| Cheddar cheese | $5,983/lb | $6,123 | [fuente: tabla BLS citada] |
| Potatoes, white | $0,976/lb | $1,001 | ídem |
| Tomatoes, field grown | $1,977/lb | $1,925 | ídem |
| Lettuce, iceberg | $1,471/lb | $1,673 | ídem |
| Lemons | $2,114/lb | — | [fuente: https://fred.stlouisfed.org/data/APU0000711412] (serie BLS) |
| Bananas | $0,652/lb | $0,666 | [fuente: tabla BLS citada] |
| Strawberries | $2,578/dry pint | $2,408 | ídem |
| Coffee, ground roast | $9,299/lb | $8,872 | ídem |

**Mayorista — carne de vacuno (USDA AMS, LM_XB459, *negotiated sales*, semana al 18-sep-2026, FOB planta, Choice):**
tenderloin 189A heavy **$1.720,88/cwt ≈ $17,21/lb** (rango $16,60-$19,74); ribeye 112A heavy $1.533,40/cwt ≈
$15,33/lb; *cutout* Choice 371,94 [fuente: https://www.ams.usda.gov/mnreports/ams_2461.pdf, texto extraído del PDF en
local]. ⚠️ El resumen automático de WebFetch de ese PDF dio cifras falsas (tenderloin «$245,30»): **verificar siempre los
PDF del USDA extrayendo el texto**, no fiarse del resumen.

**[no medido]:** aguacate, espárrago, lima, açaí, microgreens, cobertura de chocolate, nata para montar (heavy cream),
destilados (el precio de botella depende de si el estado es *control state*) y **todo el Reino Unido** (la herramienta
de precios de la ONS es interactiva y no se dejó leer).

### 9.2 Cómo usarlos en los ejemplos

- Mantener las recetas del ES (lo pide la regla de «copia»), la mayoría ya son internacionales (smash burger, eggs
  benedict, avocado toast, margarita, carrot cake). El 01 pasa a **«Beef Tenderloin, Sherry Reduction & Asparagus»**
  (el Pedro Ximénez se entiende en EE. UU. como *PX sherry*).
- Precios en **USD y unidades US**; rótulo fijo en Instrucciones: *«Sample prices: U.S. city-average retail (BLS,
  Aug 2026) and USDA wholesale beef (Sep 2026). Replace them with your supplier invoices.»* Nada de convertir los euros
  del ES por tipo de cambio.
- El caso práctico del bonus PDF (food cost 32 % → 27 %) se mantiene: el porcentaje no depende del mercado.

---

## 10. Qué queda para la SPEC F1 (lista de diferencias ES → EN)

1. Textos: glosario §1, nombres de ficheros y pestañas §1.2-1.3 (renombrado de hojas **en el motor**).
2. Impuesto: celda `Tax rate` + toggle `Menu prices include tax?`, precio a imprimir y food cost real sobre neto (§3.2).
3. Moneda: formato sin símbolo + celda `Currency` (§3.3).
4. Unidades: desplegable EN y hoja *Conversions* ampliada (§4.2-4.3).
5. Benchmarks: 5 filas de la calculadora 10 + comisión de delivery 25 % (§2.3); fila GP % para UK.
6. Q-factor como rótulo del «coste de elaboración» (§1.1).
7. Ejemplos con precios BLS/USDA etiquetados (§9).
8. Instrucciones con rutas de Google Sheets además de Excel (§8.2) y gate de conversión (§8.3).
9. Landing: sin «menu engineering», sin la frase de Sheets hasta el gate, FAQ de §6.3, `title` de §6.4.
10. Decisiones de John: settlement currency USD en Stripe y precios manuales GBP/CAD/AUD (§5.3); fiscalidad de la venta
    digital en UK/CA/AU/US (§3.4).

### Log

- **2026-09-24 (sesión Claude Code):** research F1 escrito. DataForSEO: 5 consultas de volumen (US ×2, UK ×1, y slugs +
  nombres de menú en US y en UK), 6 SERP (4 US + 2 UK) y 2 SERP para precios de Etsy. Censo de rasgos Sheets sobre los 12 xlsx ES con
  openpyxl, en serie y vigilando `istats` (máximo 56 °C).
