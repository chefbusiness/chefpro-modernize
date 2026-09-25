# Restaurant Inventory Kit Pro — SPEC (F1 · 25-sep-2026 · sesión Claude Code)

> Segundo producto de la **Tienda internacional en inglés**: la edición EN del **Kit de Inventario** (`kit-inventario`,
> 14 €, contenido v2.0). Doc canónico de la tienda: `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`.
> Plantilla de método: el piloto `scripts/productos-digitales/recipe-costing-kit/` (Food Cost Kit Pro, LIVE).
> Base de esta SPEC: `F1-inventario-es.md` (qué entrega el ES, con libro:Hoja!celda), `censo_es.json` y
> `textos_es.json` (de `extraer_textos.py`), `mapas.py` (mapas ES→EN con autotest) y, para convenciones US/UK,
> `recipe-costing-kit/F1-research-us-uk.md` (se reutiliza; no se rehace).
> Esta SPEC **decide**. Lo que no está aquí no se hace. Tamaño **S** (≤ 2,5 M tokens el producto entero).

## 0. Reglas que mandan (John)

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 9 libros, hojas, fórmulas, DV, CF, merges, protección,
  paneles, áreas y títulos de impresión. «Nativo» = traducido con naturalidad, no rediseñado. Toda excepción
  estructural está declarada aquí (D11, D12, D25) y el gate la admite por nombre, no por tolerancia.
- **Nombres por intención de búsqueda**, no traducción literal (D2, D5, D6).
- **Sin fiscalidad añadida:** se vende desde España; nada de registro de sales tax, `currency_options` ni notas
  legales por país. Los campos de impuesto DENTRO de las plantillas son contenido → parámetro neutro (D11).
- Textos de producto con **subagentes Anthropic** (regla 1bis), nunca `bridge.py`.
- Landing EN = la ES replicada, **testimonios traducidos tal cual** con subtítulo de edición española, **sin**
  `aggregateRating` ni `review` en el JSON-LD (TIENDA §3.5).

## 1. Decisiones

| D | Tema | Decisión | Estado |
|---|---|---|---|
| D1 | Slug | `restaurant-inventory-templates` → `/en/digital-products/restaurant-inventory-templates` (+ `/access`, `/library`). productId = slug; JWT `restaurant-inventory-templates-jwt`; env var `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_INVENTORY_KIT` | DECIDIDA |
| D2 | Nombre | **Restaurant Inventory Kit Pro** (orquestador, datos abajo). Un único nombre en landing, `schema.productName`, dashboard, email, docProps, pies y versión (corrige I8). Title SEO: `Restaurant Inventory Kit Pro: 9 Restaurant Inventory Templates for Excel` | DECIDIDA |
| D3 | Precio | **$19 USD**, pago único, acceso de por vida. Familia `kit-inventario` en `astro-site/src/lib/tienda.ts` (se toca en F3) | DECIDIDA |
| D4 | Anclas comerciales | Regla del piloto (D4): se convierten y suben al escalón $…9 solo los importes base: `priceOld` 49 € → **$59**; cada bono 9 € → **$19**. Derivados: bonos $38; total $97; ahorro $40; descuento −67 % (misma regla de redondeo que el piloto, 1 − 19/59). Nota de lanzamiento igual que el ES | DECIDIDA |
| D5 | Ficheros y títulos | Tabla §2.1 (intención US; UK en nota). El título interior (Instructions!A1 y docProps `title`) = título de la tabla | DECIDIDA |
| D6 | Pestañas | Tabla §2.2. En los textos EN, pestañas y valores se citan entre **comillas dobles rectas** ("Current Order") | DECIDIDA |
| D7 | Glosario | Tabla §3 (US base; UK entre paréntesis y solo en Instrucciones). Ortografía estadounidense | DECIDIDA |
| D8 | Claves-dato | 10 categorías y 9 listas de DV de `mapas.py` (§2.3). Ningún ítem lleva coma (rompería la lista literal). Los **huevos pasan de «Otros» a «Dairy & Eggs»** (agrupación estándar de los distribuidores US) | DECIDIDA |
| D9 | Unidades | DV EN de 16 unidades `lb,oz,kg,gal,qt,L,each,dozen,case,tray,keg,bag,roll,pack,bottle,can` (el métrico se queda en el desplegable, como en el piloto). **Ejemplos en US customary** desde la tabla maestra (D14). Las unidades son solo etiquetas: ninguna fórmula las lee, así que no hay tabla de conversiones | DECIDIDA |
| D10 | Literales y CF | `mapas.LITERALES` (45) y `mapas.TOKENS_CF`, iguales en fórmulas, CF, DV y comodines de COUNTIF. Regla: en cada rango, **cada token de CF casa con un solo estado** (SEARCH no distingue mayúsculas): autotest de `mapas.py` y gate G5 | DECIDIDA |
| D11 | Impuesto (03) | Parámetro neutro: DV `Pedido Actual!H9:H38` pasa de lista `"4,10,21"` a **decimal 0-100** (mismo sqref, mensajes EN); `Tax Rates` (ex `Listas`) con **0 % por defecto** en las 10 categorías; tabla de excepciones E2:F20 **vacía** con su cabecera y una nota; desglose `A46:A48` = **0 / 5 / 20 editables** (verdes, desbloqueadas: corrige I7) con nota «type the rates you actually pay». Rótulos: «Net amount (pre-tax)», «Tax amount», «Order total». Instrucciones: US, la comida comprada para reventa suele ir exenta con resale certificate (0 %) y los suministros llevan el sales tax local; UK, 0 / 5 / 20 % VAT; «check with your accountant». Historial recalculado con esas tasas | DECIDIDA |
| D12 | Temperaturas (04, 06) | **°F** en todas las celdas numéricas comparables (O, P, Q de `Receiving Log`; C:D de `Receiving Temps`); en texto «41 °F (5 °C)». Tabla de 15 familias por fila en `mapas.FAMILIAS` (§4), valores del FDA Food Code 2022 [fuente] y práctica del sector [estimado]. Frío TCS ≤ 41 °F / 5 °C; caliente ≥ 135 °F / 57 °C; congelado «received frozen»; leche, huevos y shellstock ≤ 45 °F. **Huevos refrigerados** (21 CFR 118.4(e)): la zona «Huevera» ambiente pasa a «Dairy & egg cooler» (I9) | DECIDIDA |
| D13 | Moneda | Cero `€` en formatos y textos: `#,##0.00 €` → `#,##0.00`; rótulos sin «(€)»; «amounts are in your currency». `$` solo en texto de ejemplo US | DECIDIDA |
| D14 | Tabla maestra de productos | Los 50 productos + la merluza de 04-06 (§5), con nombre, categoría, unidad US, precio y par levels EN, **una sola vez** en `mercado_en.json` y de ahí a los 9 libros. Precios: los del catálogo del piloto (`recipe-costing-kit/mercado_en.json`, 24-sep, con fuente) por `id` cuando existe; el resto con fuente o `[estimado]`; nunca € convertidos. Identidades (gate G7): mismo precio del mismo producto en todos los libros; BONUS-09 `consumo × (lead + cobertura)` = par level del 01 y stock máx. = par max; importes de ejemplo = cantidad × precio | DECIDIDA |
| D15 | Proveedores de ejemplo | 6 fichas genéricas «(sample)» (§5.2): nombres inventados, direcciones «Anytown», teléfonos **555-01xx** (reservados para ficción), correos en dominio **`.example`** (RFC 2606), Tax ID `00-000000n`. Condiciones «Net 30», «Net 15», «COD» | DECIDIDA |
| D16 | Campos de proveedor (02, 03) | CIF/NIF → «Tax ID (EIN / VAT no.)»; Nº RGSEAA → «Food license / FDA reg. no.»; Homologado (S/N) → «Approved (Y/N)» (approved source, Food Code §3-201.11); APPCC → «HACCP / food safety plan» | DECIDIDA |
| D17 | Normativa citada | Reg. (CE) 853/2004, 852/2004, 589/2008 y RD 3484/2000 → Food Code 2022 (§ por familia en §4); Reg. (UE) 1169/2011 art. 24 → D18. UK: una nota en Instrucciones del 04 («UK: follow your Safer Food Better Business limits; chilled food legally ≤ 8 °C, 5 °C recommended») | DECIDIDA |
| D18 | Fechas de consumo (06) | «Caducidad» → **Use-by** (se tira); «Consumo preferente» → **Best-by** (se revisa); fecha de entrada → «Received date»; apertura → «Opened on». Instrucciones: UK, use-by = seguridad por ley; US, las etiquetas son sobre todo de calidad, pero el **date marking de 7 días** del Food Code (§3-501.17) para RTE TCS abierto o elaborado en casa funciona como use-by | DECIDIDA |
| D19 | Formato | Toda fecha → `numFmtId 14` (fecha corta del sistema; mm/dd/yyyy en US); `Date: ___/___/______` se mantiene; **US Letter** (`paperSize 1`) con el mismo ajuste; pie «AI Chef Pro · aichef.pro · Page &P of &N»; meses en inglés (`Jan…Dec`, `January…`) | DECIDIDA |
| D20 | Textos con cifra derivada | Se **reescriben** con la cifra EN recalculada, no se traducen: 01 A20 (filas 44/34), 03 A10 (filas 40-48), 04 A7-A8 y `Receiving Temps!G15` (límites), 05 A8/A10/A13 (3 % y «500 € de merma»), 07 A7 («4-21 %» → «net of recoverable tax»), 07 `KPI Dashboard!A19` (compras/ventas/cubiertos/food cost), BONUS-08 A14 (fila 84), BONUS-09 A19 (ejemplo de la leche en gal) y A21 (parámetros). Lista cerrada en `mercado_en.json.textos_cifra_derivada` | DECIDIDA |
| D21 | Versión | «Version 2.0 · <mes de publicación> 2026 · aichef.pro/en/digital-products/restaurant-inventory-templates · info@aichef.pro»; `subject` «Restaurant Inventory Kit Pro · v2.0»; `description` = URL; `keywords` «restaurant inventory template, par sheet, AI Chef Pro»; `category` «AI Chef Pro · Digital products». Changelog EN: «first English edition of content 2.0» | DECIDIDA |
| D22 | Landing | §6 (todas las secciones del ES) | DECIDIDA |
| D23 | Defectos heredados | EN nace corregido de I1 (sin «RT-08:»), I2 («7 templates» con unidades), I7 (D11) e I10 (D25); I3/I4 por D22. En el ES se corrigen I1, I2 e I10 en su próxima sesión v2.x | PROPUESTA (ES) |
| D24 | Parámetros de BONUS-09 y objetivos | Se mantienen los valores del ES (coste de pedido 3, almacenamiento 25 %, factor 0,7; objetivo de merma 3 % de las compras [estimado, heredado del ES]; food cost 32 % de techo, dentro del 28-32 % del piloto D12) con «in your currency» | DECIDIDA |
| D25 | Fechas de ejemplo vivas (06, 02) | I10: los estados del 06 y del 02 dependen de `TODAY()` y los ejemplos llevan fechas fijas de agosto de 2026, así que «los cinco estados desde el primer minuto» deja de ser verdad a los pocos días. En EN esas celdas pasan a `=TODAY()+k` con el mismo desfase que el ES respecto al 23-ago-2026: 06 `FIFO Tracker!E5:E10`, `G5:G10`, `H9` (13 celdas) y 02 `Price Comparison!N4,O4,N7,O7,N8,O8` (6). Excepción declarada al gate G1 (+19 fórmulas) | DECIDIDA |
| D26 | Propuesta de nombre | Los datos del orquestador dicen que «kitchen inventory template» (480) y «restaurant inventory sheet» (320) superan a «restaurant inventory template» (210): por eso el 01 se titula «Kitchen & Bar Inventory Sheet with Par Levels». Se propone además probar en el H1 de la landing «Restaurant Inventory Templates» (plural, = slug) en lugar de repetir el nombre del producto **Resuelta por el orquestador (25-sep):** el H1 sigue el patrón del piloto y repite el title de D2, «Restaurant Inventory Kit Pro: 9 Restaurant Inventory Templates for Excel» (nombre + keyword en plural = slug); sin test A/B hasta que haya tráfico | DECIDIDA |

**Datos de D1-D2** (DataForSEO, orquestador, 25-sep-2026, mensual):

| Keyword | US | UK | Lectura |
|---|---|---|---|
| inventory templates | 1.300 | 210 | genérica (todas las industrias) |
| restaurant inventory management | 720 | 170 | intención software |
| food inventory template / kitchen inventory template | 480 / 480 | ≤ 20 | mismo clúster; la SERP mezcla despensa doméstica |
| restaurant inventory spreadsheet / sheet | 320 / 320 | ≤ 20 | → título del 01 |
| restaurant inventory template | 210 | ≤ 20 | SERP 100 % profesional (Smartsheet, Square, Rezku, RestaurantOwner): plantillas sueltas gratis → el kit se vende como conjunto de 9 |
| bar inventory template | 140 | ≤ 20 | → «Kitchen & Bar» en el 01 |
| stock take template | — | 140 | UK: «stocktake» en el BONUS-08 (nota) |
| food waste log template | 90 | ≤ 20 | → 05 |
| par sheet restaurant | 50 | ≤ 20 | → 01 |
| restaurant order guide template / receiving log template / fifo labels | 40 / 40 / 40 | ≤ 20 | → 03 (nota), 04, 06 |

## 2. Mapas

### 2.1 Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN (landing, dashboard, A1, docProps) | Intención |
|---|---|---|---|---|
| 01 | `01-inventario-stock-diario.xlsx` | `01-kitchen-bar-inventory-par-sheet.xlsx` | Kitchen & Bar Inventory Sheet with Par Levels | kitchen inventory template 480 · restaurant inventory sheet 320 · bar inventory template 140 · par sheet 50 |
| 02 | `02-fichas-proveedores.xlsx` | `02-vendor-list-price-comparison.xlsx` | Vendor List, Price Comparison & Scorecard | «vendor» es como habla el manager US [estimado, sin volumen]; UK «supplier» en nota |
| 03 | `03-pedidos-compra.xlsx` | `03-purchase-order-template.xlsx` | Purchase Order Template & Order Log | restaurant order guide template 40 (el libro es un PO, no una order guide) |
| 04 | `04-recepcion-mercancias.xlsx` | `04-receiving-log.xlsx` | Receiving Log (Temperatures & Credit Requests) | receiving log template 40 |
| 05 | `05-control-mermas.xlsx` | `05-food-waste-log.xlsx` | Food Waste Log & Action Plan | food waste log template 90 |
| 06 | `06-fifo-caducidades.xlsx` | `06-fifo-expiration-date-tracker.xlsx` | FIFO & Expiration Date Tracker | fifo labels 40; «expiration date» = US |
| 07 | `07-analisis-costes-compras.xlsx` | `07-purchasing-cost-analysis.xlsx` | Purchasing Cost Analysis & Food Cost KPIs | sin volumen: prima la claridad |
| B08 | `BONUS-08-inventario-rapido-mensual.xlsx` | `BONUS-08-month-end-inventory-count.xlsx` | BONUS: Month-End Inventory Count | stock take template 140 (UK, nota «stocktake») |
| B09 | `BONUS-09-calculadora-punto-pedido.xlsx` | `BONUS-09-reorder-point-calculator.xlsx` | BONUS: Reorder Point & Order Quantity Calculator | «reorder point» = término US/UK |

Aviso de solape: el piloto ya vende un «Food Waste Log» (su 09). No canibaliza (son productos, no URLs por plantilla),
pero la landing del 05 lo describe como «with action plan and category analysis» para distinguirlo.

### 2.2 Pestañas (D6) — 38 hojas, 30 nombres

| Libro | Pestaña ES | Pestaña EN | Por qué |
|---|---|---|---|
| todos | `Instrucciones` | `Instructions` | igual que el piloto |
| 01 | `Cocina` | `Kitchen` | zona de conteo |
| 01 | `Barra` | `Bar` | zona de conteo |
| 01 | `Almacén` | `Storeroom` | almacén general (limpieza, desechables, secos); «Dry Storage» es la zona del 06 |
| 01 | `Resumen Dashboard` | `Summary Dashboard` | |
| 02 | `Directorio Proveedores` | `Vendor Directory` | |
| 02 | `Comparativa Precios` | `Price Comparison` | |
| 02 | `Evaluación Proveedores` | `Vendor Scorecard` | «scorecard» es el término de compras US |
| 02 | `Condiciones Comerciales` | `Vendor Terms` | |
| 03 | `Pedido Actual` | `Current Order` | |
| 03 | `Proveedores` | `Vendors` | |
| 03 | `Historial Pedidos` | `Order Log` | |
| 03 | `Listas` | `Tax Rates` | la hoja solo guarda impuestos (D11): se nombra por lo que es |
| 04 | `Control Recepción` | `Receiving Log` | |
| 04 | `Registro Incidencias` | `Discrepancy Log` | faltas, rechazos y credit memos |
| 04 | `Verificación Temperaturas` | `Receiving Temps` | |
| 05 | `Registro Diario Mermas` | `Daily Waste Log` | |
| 05 | `Análisis por Categoría` | `Waste by Category` | |
| 05 | `Dashboard Mermas` | `Waste Dashboard` | |
| 05 | `Plan de Acción` | `Action Plan` | |
| 06 | `Control FIFO` | `FIFO Tracker` | |
| 06 | `Alertas Caducidad` | `Expiration Alerts` | |
| 06 | `Mapa Almacén` | `Storage Map` | |
| 07 | `Coste por Categoría` | `Spend by Category` | |
| 07 | `Evolución Mensual` | `Monthly Trend` | |
| 07 | `Top 20 Productos` | `Top 20 Items` | |
| 07 | `Dashboard KPIs` | `KPI Dashboard` | |
| B08 | `Conteo Rápido` | `Quick Count` | |
| B09 | `Calculadora` | `Reorder Calculator` | |
| B09 | `Parámetros` | `Parameters` | |

El renombrado reescribe en el mismo paso: 365 fórmulas con referencia a hoja, las 2 DV que citan hoja (03 C3,
04 G4:G43), 29 áreas y 28 títulos de impresión, y todo texto que cite una pestaña.

### 2.3 Claves-dato (D8, D9)

- **Categorías:** Cárnicos → Meat & Poultry · Pescados → Seafood · Lácteos → Dairy & Eggs · Verduras/Frutas →
  Produce · Secos/Granos → Dry Goods · Congelados → Frozen · Bebidas Alcohólicas → Alcoholic Beverages · Bebidas No
  Alcohólicas → Non-Alcoholic Beverages · Limpieza → Paper & Cleaning · Otros → Other.
- **Listas de DV** (`mapas.DV_LISTAS`): S/N/Pendiente → Y/N/Pending; estados de pedido (Draft… Invoiced); 7 tipos de
  incidencia; 5 estados de incidencia (Open, Claimed, Credit received, Closed without credit, Closed); 10 motivos de
  merma (Past use-by date… Unexplained variance); prioridad High/Medium/Low; 5 estados del plan; Use-by/Best-by;
  11 zonas (`mapas.ZONAS`); periodo `Full year,Jan…Dec`; ✓/✗/— sin cambio.
- Cada clave se sustituye **a la vez** en la DV, en las etiquetas de agregación y en las celdas de ejemplo.

## 3. Glosario ES → EN (D7)

| ES | EN (US) | UK (solo notas) |
|---|---|---|
| stock / existencias | inventory, on hand | stock |
| Stock Real | On Hand | |
| existencias iniciales / finales | beginning / ending inventory | opening / closing stock |
| inventario mensual | month-end inventory count | stocktake |
| par level / par max | par level / par max | |
| A Pedir | Order Qty | |
| punto de pedido · stock de seguridad | reorder point · safety stock | |
| proveedor | vendor | supplier |
| homologado | approved (vendor) | |
| albarán | invoice / packing slip | delivery note |
| abono | credit memo | credit note |
| rappel · portes · pedido mínimo | volume rebate · delivery fee · order minimum | |
| merma | waste (merma de despiece: butchery trim loss) | |
| cámara · congelador · economato | walk-in cooler · walk-in freezer · dry storage | |
| cubiertos · ticket medio | covers · average check | covers · average spend |
| base imponible · cuota de IVA | net amount (pre-tax) · tax amount | net · VAT |
| lote · caducidad · consumo preferente | lot no. · use-by · best-by | lot · use by · best before |
| APPCC | HACCP / food safety plan | |
| 5.ª gama | fresh-cut, ready-to-eat produce | |
| Revisar → Desproteger hoja | Review → Unprotect Sheet | |

## 4. Temperaturas de recepción (D12) — `Receiving Temps!A4:E18`, en °F

| Fila | Familia EN | Mín | Máx | Base | Etiqueta |
|---|---|---|---|---|---|
| 4 | Raw beef, pork & lamb | 30 | 41 | Food Code §3-202.11(A) | [fuente]; mín [estimado] |
| 5 | Ground & variety meats | 30 | 41 | §3-202.11(A) | [fuente] |
| 6 | Raw poultry | 30 | 41 | §3-202.11(A) | [fuente] |
| 7 | Marinated & processed raw meat | 30 | 41 | §3-202.11(A) | [fuente] |
| 8 | Live shellfish (shellstock) | 32 | 45 | §3-202.11(B); NSSP | [fuente] |
| 9 | Fresh fish & shucked shellfish | 30 | 41 | §3-202.11(A) | [fuente] |
| 10 | Frozen food | −40 | 0 | §3-202.11(E) «received frozen» | [fuente]; 0 °F [estimado] |
| 11 | Cold ready-to-eat TCS food | 30 | 41 | §3-202.11(A) | [fuente] |
| 12 | Hot TCS food (received hot) | 135 | 212 | §3-202.11(D) | [fuente]; máx = límite físico |
| 13 | Dairy & other refrigerated TCS | 30 | 41 | §3-202.11(A)-(B) (leche ≤ 45 °F en texto) | [fuente] |
| 14 | Whole produce | 32 | 54 | sin límite legal | [estimado] |
| 15 | Shell eggs | 30 | 45 | §3-202.11(C); 21 CFR 118.4(e) | [fuente] |
| 16 | Dry & canned goods (ambient) | N/A | N/A | §3-202.15 (envase íntegro) | [fuente] |
| 17 | Beverages (ambient) | N/A | N/A | fabricante | [estimado] |
| 18 | Non-food (cleaning & disposables) | N/A | N/A | §7-201.11 (químicos separados) | [fuente] |

Es una **reescritura por fila** (las familias UE se funden en el Food Code); el rango de la DV y del VLOOKUP no
cambia. Categoría → familia por defecto (`G4:H13`): `mapas.FAMILIA_POR_CATEGORIA`. Ejemplo del 04 (misma historia
de 4 líneas): solomillo a 37 °F (accept, entrega corta), bacalao fresco a **46 °F** con límite 41 °F (reject too warm),
tomate a 48 °F (accept; rechazo por moho), y la 4.ª línea pasa de huevos a **harina 50 lb** (familia sin control de
temperatura, «N/A»), porque en EE. UU. el huevo sí se controla. Zonas del 06 en °F: coolers ≤ 41 °F, freezer ≤ 0 °F,
dry storage 50-70 °F [estimado], wine & liquor 55-60 °F [estimado]. Fuente: FDA Food Code 2022 (fda.gov/food/fda-food-code).

## 5. Datos de ejemplo (D14, D15)

### 5.1 Tabla maestra (50 + 1) — unidad US; `id` del catálogo del piloto cuando existe

| ES | EN · unidad | ES | EN · unidad |
|---|---|---|---|
| Pechuga de pollo | Boneless chicken breast · lb | Solomillo de ternera | Beef tenderloin (PSMO) · lb `beef_tenderloin` |
| Salmón fresco | Fresh salmon fillet · lb | Gambas | Shrimp 16/20 · lb `shrimp` |
| Tomate | Tomatoes · lb `tomato` | Cebolla | Yellow onions · lb `yellow_onion` |
| Lechuga | Romaine lettuce · each | Patata | Russet potatoes · lb `potato` |
| Aceite de oliva virgen extra | Extra virgin olive oil · gal `evoo` | Sal marina | Kosher salt · lb `kosher_salt` |
| Pimienta negra molida | Ground black pepper · lb `black_pepper` | Arroz redondo | Arborio rice · lb |
| Pasta seca | Dry pasta · lb | Harina de trigo | All-purpose flour · lb `ap_flour` |
| Huevos M | Large eggs · dozen `eggs` | Nata 35 % M.G. | Heavy cream · qt `heavy_cream` |
| Mantequilla | Unsalted butter · lb `butter` | Queso parmesano | Parmesan · lb |
| Limón | Lemons · each `lemon` | Ajo | Peeled garlic · lb `garlic` |
| Café en grano | Whole bean coffee · lb `coffee` | Leche entera | Whole milk · gal `whole_milk` |
| Bebida de avena | Oat milk (barista) · qt `oat_milk` | Zumo de naranja | Orange juice · gal |
| Refresco de cola | Cola (12 fl oz) · can | Cerveza de grifo (barril 30 L) | Draft beer (1/2 bbl) · keg |
| Agua mineral | Bottled water · bottle | Tónica | Premium tonic water · bottle `tonic` |
| Vino tinto (botella 75 cl) | House red wine (750 ml) · bottle `red_wine` | Vino blanco (botella 75 cl) | House white wine (750 ml) · bottle `white_wine` |
| Hielo en cubitos | Bagged ice (20 lb) · bag `ice` | Azúcar blanquilla | Granulated sugar · lb `sugar` |
| Servilletas de papel (barra) | Beverage napkins (bar) · case | Pajitas de papel | Paper straws · case |
| Vasos desechables | Disposable cups · pack | Papel de cocina | Paper towels · roll |
| Film transparente | Plastic wrap · roll | Papel de aluminio | Aluminum foil · roll |
| Bolsas de basura | Trash bags · pack | Guantes de nitrilo | Nitrile gloves · case |
| Detergente de lavavajillas | Dish machine detergent · gal | Desengrasante de cocina | Kitchen degreaser · gal |
| Lejía alimentaria | Sanitizer (quat) · gal | Cubetas GN 1/1 | Full-size hotel pans · each |
| Etiquetas FIFO | Day dot date labels · roll | Rollos de ticket | POS receipt paper rolls · pack |
| Servilletas de papel (reserva de almacén) | Beverage napkins (storeroom backup) · case | Aceite de girasol (garrafa 5 L) | Canola fryer oil (35 lb jug) · lb `fryer_oil` |
| Vinagre de vino | Red wine vinegar · gal | Legumbres secas | Dried beans · lb |
| Merluza fresca (04-06) | Fresh cod fillet · lb | | |

Par levels y consumo diario se convierten a la unidad US y se redondean a cantidades de compra reales, cumpliendo las
identidades de D14. Precios del piloto derivados a la unidad EN con su factor (p. ej. 50 lb bag → lb) y la nota
`[derivado]`. «Sample prices are illustrative U.S. references — replace them with your own vendor invoices».

### 5.2 Proveedores «(sample)» (D15)

Cárnicas del Norte → Prime Cut Meats · Pescados Ría Fresca → Harbor Fresh Seafood · Frutas y Verduras La Huerta →
Green Valley Produce · Distribuciones Economato Sur → Pantry Foodservice Supply · Bebidas y Distribución Levante →
Metro Beverage Distributors · Higiene Profesional HORECA → ProClean Janitorial Supply (sigue siendo la nota D
«Pending»). Notas de ficha localizadas: «reject seafood above 41 °F», «rebate 2 % over 2,000 a month», «keg deposit».

## 6. Landing EN (D22) — réplica de `kit-inventario.ts` en `data/productos-en/kits/restaurant-inventory-templates.ts`

| Sección ES | Tratamiento EN |
|---|---|
| `seo` | title D2; description «9 Excel templates… $19»; keywords del set de D1; `ogImage` propio |
| `schema` | productName = D2; price `19.00` USD; **sin `aggregateRating` ni `reviews`**; `schema.faqs` = FAQ EN |
| `images.gallery` | las mismas imágenes con `alt` en inglés |
| `hero` | badge «Uncounted waste eats 3-5 % of purchases…» (mismo dato del ES, marcado como observación de consultoría); título `Restaurant Inventory ` + gold `Kit Pro`; 5 checkItems traducidos («7 templates with the same units», I2); CTA «BUY NOW — $19» |
| `compatApps` | «Print, Delegate and Control»; «optimized for US Letter» |
| `grid` | **9** tarjetas (7 + 2 bonus) con los títulos de §2.1; «9 Restaurant Inventory Templates» |
| `why` | 4 razones traducidas; «HACCP records» en lugar de APPCC; «Inventory software is a monthly subscription; this kit is $19, once» (sin cifra de software: solo se pone una si F3 la cita de la página de precios pública de un competidor); pastillas = las del piloto + «Printable (US Letter)» (I3) |
| `authorBio` / `authorBadges` | los del piloto EN |
| `bonus` | «Besides the 7 core templates…», 2 bonos a $19 (D4) |
| `buyBox`, `guarantee`, `cta` (9 ítems), `pricing`, `stickyLabel` | traducidos con D3-D4 |
| `faqs` | las 6 del ES traducidas (licencia = D18 del piloto, I4) + semillas PAA: «Is there a free Excel template for restaurant inventory?» · «How do I make an inventory list for a restaurant?» · «What is the best inventory system for restaurants?» (Excel vs software) · «Does Excel have an inventory template?» · «Does it work in Google Sheets?» · «How do I set par levels?» · «How does it handle sales tax and VAT?» (D11) · «Which temperatures does the receiving log use?» (D12) · «What currency will I pay in?» |
| `testimonials` | los **8 del ES traducidos tal cual** (nombres, negocios, ciudades, cifras «EUR 400»), subtítulo «…with Kit de Inventario, the Spanish edition of this kit» |
| `footerLinks`, `updateNote`, `alreadyBought` | a páginas EN (`/en/digital-products`, Food Cost Kit Pro, contacto); «Version 2.0 · <mes> 2026» |

**Dashboard (F3):** `…/library` con la isla `KitInventarioLibraryIsland` copiada y traducida (9 descargas con los títulos
de §2.1); `…/access` con `ProductAccessGate`; email de acceso EN; ficheros en `astro-site/public/dl/restaurant-inventory-templates/`.

## 7. Plan de F2 (entregables)

1. `extraer_textos.py` ✅ (F1) → `textos_es.json` + `censo_es.json`. `mapas.py` ✅ (autotest 0 errores contra el censo).
2. **Traducción** (sonnet, subagentes Anthropic): G0-comun (28 cadenas) PRIMERO, fija glosario; después G01-G05 (61-126
   cadenas cada uno), de 2 en 2. Cada agente recibe: sus cadenas con `donde`, `pistas`, `cita_hojas`,
   `categorias_citadas` y `con_cifra`; el glosario §3; los mapas (§2); D11-D13, D16-D20. Salida `textos_en/<grupo>.json`.
3. **Mercado** (1 agente opus): `mercado_en.json` = tabla maestra §5 con fuentes (reutiliza el catálogo del piloto),
   proveedores §5.2, familias §4, GL-mercado (246 cadenas), `textos_cifra_derivada` (D20). `validar_mercado.py`
   comprueba las identidades de D14.
4. **`aplicar_en.py`** (copia adaptada del piloto): copiar los 9 ES → renombrar hojas y referencias → claves-dato →
   literales y CF → textos → mercado → D11 → D12 → D25 → formatos (€, fechas 14) → Letter y pie → docProps →
   `inject_cache.py` al final. Idempotente, `--dry-run` al scratchpad; salida `astro-site/public/dl/restaurant-inventory-templates/`.
5. **`gates_en.py`** (§8) → 1 ronda de revisión adversarial (sonnet, lente manager US + lente técnica; tope 2 rondas).
6. `restaurant-inventory-templates` en `EXCLUIDOS` de `postprocess-transversal.py` y Letter admitido en
   `censo-entregables.py` para `productos-en/**` (como el piloto). Mac, en serie, con vigilante térmico.

Presupuesto: F1 ≈ 0,6 M · F2 ≤ 1,2 M · F3 ≤ 0,7 M. Si el total pasa de 3,25 M (techo + 30 %), se para y se reporta.

## 8. Gates de F2 (contra `censo_es.json`, nunca cifras fijas)

- **G1 Paridad estructural:** por libro, mismas hojas vía §2.2; mismo número de fórmulas y misma fórmula celda a celda
  tras aplicar los mapas de hoja y de literales (+19 de D25, declaradas); mismas referencias a hoja (365); mismas DV
  (35, mismos sqref y `n_celdas`; tipo igual salvo D11) y CF (31, mismos sqref, tipos, prioridades); 60 merges;
  29 hojas protegidas sin contraseña; paneles; 29 áreas y 28 títulos de impresión; 1 autofiltro; columnas ocultas;
  verdes = desbloqueadas (5.979 + 3 de D11). 0 gráficos, 0 imágenes.
- **G2 Restos:** cero español (lista de palabras y acentos ES), cero `€`/`EUR`, cero caracteres no latinos, en valores,
  formatos, pestañas, DV, CF, cabeceras/pies y docProps. Lista blanca: Parmesan, Arborio, ✓ ✗ ⚠ ⛔ 🔴 🟡 🟢.
- **G3 Formato:** `paperSize 1` en las 38 hojas; 522 fechas (+ las de D25) con `numFmtId 14`; cero `dd/mm`; pie D19;
  versión D21 en las 9 Instrucciones; docProps D21.
- **G4 Claves:** las 10 categorías idénticas en las 7 DV literales, en las etiquetas de agregación y en los ejemplos;
  lista de unidades D9 en las 9 hojas que la llevan; familias y zonas = `mapas.py`.
- **G5 CF y literales:** cada token de CF casa con un solo estado de su rango; `"Y"`, `"Best-by"`, `"Full year"` y
  `Jan…Dec` coinciden con sus DV.
- **G6 Cálculo:** caché con `data_only`; pycel sin `#REF!`/`#VALUE!`/`#N/A` en las filas de ejemplo; la historia del 04
  da ACCEPT / REJECT (too warm) / ACCEPT / N/A; 07 food cost dentro del objetivo; el 06 muestra los 5 estados hoy.
- **G7 Identidades de D14:** mismo precio por producto en los 9 libros; BONUS-09 ROP = par del 01 y máx. = par max;
  importes = cantidad × precio; cifras derivadas de D20 recalculadas sobre la hoja EN final.
- **G8** `censo-entregables.py --only restaurant-inventory-templates --fail` en 0 con Letter admitido.

## 9. F3

Checklist de cierre de `TIENDA-INTERNACIONAL.md` §6 completo (registro `tienda.ts` familia `kit-inventario` con
`en: {slug: 'restaurant-inventory-templates', vivo: true}`, 5 fuentes del backend con `lang: 'en'`, gates LIVE,
Payment Link USD de John con redirección a `/en/digital-products/restaurant-inventory-templates/access?session_id={CHECKOUT_SESSION_ID}`,
compra de prueba con 9 descargas, tarjeta viva en el hub EN, enlaces entrantes, broadcast EN en la cola de 5 días).
