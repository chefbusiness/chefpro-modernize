# Recipe Costing Kit — F1 · Research de 8 bloques, parte B (bloques 4, 7 y huecos del 8)

> Sesión Claude Code, **24-sep-2026**. Completa `F1-research-us-uk.md` (en adelante *research*) y
> `F1-inventario-es.md` (*inventario*) sin repetirlos, y alimenta `SPEC.md`. Informe para John: en español, con los
> términos ingleses tal cual.
>
> **Leyenda:** `[medido DFS 24-sep]` = DataForSEO de hoy (US = 2840/en, UK = 2826/en) · `[fuente: URL]` = leído en esa
> página · `[fuente: URL · título/snippet SERP]` = el dato está en el título o el resumen del buscador; la página no se
> abrió o dio 403/404 · `[fuente secundaria]` = blog o agregador, no fuente primaria · `[estimado]` = razonamiento
> propio · `[no medido]`.
>
> **Método:** lectura de los 12 xlsx ES publicados con openpyxl (solo lectura; `Conversiones`, rejilla, DV, 04
> `Formatos de Compra`, BONUS, 09, 10, 11); DataForSEO: 2 tandas de volumen (63 keywords US, 45 UK) y 7 SERP; WebSearch
> y WebFetch; 2 PDF (City & Guilds 7133, ProStart Utah) leídos en local con pypdf. CPU entre 42 y 55 °C con `istats`
> antes de cada script. Sin navegador, sin builds.

---

## 0. Lo que cambia en la SPEC (resumen)

| # | Dónde | Cambio | Por qué | Tipo |
|---|---|---|---|---|
| 1 | D7 desplegable | **Quitar `case`** del desplegable y de `Conversions`. Ningún factor único vale para «case» (4 galones, 36 libras, 180 huevos…) y un `case→each = 12` por defecto, como proponía el research §4.3, **costearía mal sin avisar** | §1.6 | contenido |
| 2 | D7 desplegable | Añadir **`imp pt`** y **13 formatos de compra con nombre** (`15 dz case`, `30 dz case`, `50 lb bag`, `40 lb case`, `36x1 lb case`, `16 kg sack`, `40x250 g case`, `4x1 gal case`, `12x750 ml case`, `24x12 fl oz case`, `1/2 bbl keg`, `1/6 bbl keg`, `50 L keg`). La lista literal queda en **33 unidades y 241 caracteres** (el tope de Excel es 255) y **sigue siendo una sola regla de validación**, como en el ES | §1.6 | contenido |
| 3 | D7 `Conversions` | La tabla pasa de 33 a **≈ 224 claves**, generadas por regla: todas las parejas compra→uso **de la misma dimensión** (peso, volumen, recuento), con factores exactos por definición. Sin claves duplicadas y sin parejas peso↔volumen, las dos cosas por construcción. Envases genéricos con tamaño por defecto editable, como en el ES: `bottle` = 750 ml y `can` = 12 fl oz | §1.6 | contenido (la tabla ya podía crecer) |
| 4 | SPEC §2.3 | El rango del `VLOOKUP` va hasta el final de la tabla EN **más ~30 filas vacías**. **Defecto del ES:** las Instrucciones dicen «añade las parejas que te falten», pero el rango acaba en `$A$37`, justo en la última fila, así que una pareja escrita en la fila 38 **nunca se encuentra** | §1.6 | fórmula (rango, ya previsto en §2.3) |
| 5 | 04 `Bottle Sizes` | La columna de tamaño va **en ml** (así lo fija la TTB) y la constante de la fórmula cambia de 100 a 1000 (excepción declarada en el gate de paridad), o bien se deja en cl, que en EE. UU. se lee mal. Precargar dos filas en las 5 vacías: vino de 750 ml y un barril de 1/6 bbl. Añadir en Instrucciones la tabla de medidas legales y estándar y el pour cost por categoría | §1.6, §2.4 | fórmula (1 constante) + contenido |
| 6 | Instrucciones (01-08) | Bloque nuevo **«From invoice to price per unit»**: notación pack/size, catch weight, dividir el precio de la caja, lata #10, aceite de freidora al Q-factor, pesar los secos, subrecetas, escalado y cómo medir tu propio yield | §1.5, §2.6 | solo texto |
| 7 | Ejemplos (D10-D11) | Al menos 2 filas de ejemplo con **formato de caja y el precio tal cual de la factura** (p. ej. harina `50 lb bag` $29.99, huevos `15 dz case`), una en catch weight (`lb`) y el bar a través de `Bottle Sizes` | §1.5 | contenido |
| 8 | 11 Dashboard | Rótulo «Month» → **«Period (month or week)»** e Instrucciones con el método semanal habitual en EE. UU. Las 12 filas se quedan como están | §2.4 | solo texto |
| 9 | Compras sin impuesto | Instrucciones y rótulos: «purchases **net of recoverable tax**». En EE. UU. se compra para reventa con *resale/sales tax license*; en UK casi toda la comida va a tipo cero y el VAT de las bebidas se recupera | §1.3 | solo texto |
| 10 | Landing / FAQ EN | Respuestas honestas: «Does it handle case prices? Yes» · «Par levels / butcher's yield test / menu engineering / ingredient price database? No: …» | §2.5 | copy |
| 11 | Pendiente de John | Dos hojas nuevas **opcionales** que cambian estructura: *Yield Test* y *Ingredient Price List*. **Recomendación: no en la v1 EN**; si se hacen, en una v2.1 **ES y EN a la vez** para no romper la regla de copia | §2.7 | (c) |

**Bloque 8:** los hallazgos no mueven los **$19** (§3).

---

## 1. Bloque 4 · Proveedores y formatos de compra

### 1.1 Distribuidores de EE. UU.

| Distribuidor | Tipo | Tamaño | Cómo compra un restaurante | Fuente |
|---|---|---|---|---|
| **Sysco** | Broadline (el mayor) | Ventas FY2026 **$84.600 M**; ~**670.000** puntos de cliente; Internacional $16.000 M (ahí entra Brakes, en UK [estimado: el comunicado no lo nombra]). Mide su volumen **en cajas** («case volume») | Pedido con reparto propio. Mínimos de pedido: [fuente secundaria, blogs de comparativa: $300-500 por entrega; no verificado] | [fuente: https://investors.sysco.com/annual-reports-and-sec-filings/news-releases/2026/08-04-2026-130610546] |
| **US Foods** | Broadline | Ventas FY2025 **$39.424 M**; volumen de cajas +1,0 % | Ídem | [fuente: https://ir.usfoods.com/newsroom/news/news-details/2026/US-Foods-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Earnings/default.aspx · snippet SERP] |
| **Performance Food Group (PFG)** | Broadline + conveniencia | Ventas FY2026 **$67.800 M**; cajas de independientes +10,2 % | Ídem | [fuente: https://investors.pfgc.com/press-releases/press-release-details/2026/Performance-Food-Group-Company-Reports-Fourth-Quarter-and-Full-Year-Fiscal-2026-Results/default.aspx · snippet SERP] |
| **Gordon Food Service (GFS)** | Broadline familiar; también tiendas GFS Store | ~$24.000 M (2024) | Reparto y tiendas de autoservicio: `gfsstore.com` publica el formato («1 Gal, 4/Case») | [fuente secundaria: resumen de buscador sobre zoominfo/oysterlink] · [fuente: https://gfsstore.com/en-us/products/711191 · título SERP] |
| **Restaurant Depot** | *Cash & carry* (autoservicio mayorista) | ~130 almacenes según el desplegable del formulario de alta (el total no se dice) | **Alta gratuita**, solo para negocios: licencia de actividad o carta del IRS, o *sales tax license* si revendes; licencia de alcohol para comprar alcohol; FEIN en CT, IN, MA y PA. Primero se compra en tienda y después se abre el pedido online | [fuente: https://www.restaurantdepot.com/membership] |
| **The Chefs' Warehouse** | Especialista (alta cocina) | Ventas FY2025 ≈ **$4.150 M**; 44 centros de distribución; > 90.000 SKU; > 55.000 clientes | Reparto; producto de especialidad | [fuente: https://www.sec.gov/Archives/edgar/data/1517175/000151717526000005/chef-20251226.htm · snippet SERP] |
| **Costco Business Center** | Club mayorista con socios | 27 locales en EE. UU. | En tienda o con reparto (`costcobusinessdelivery.com`) | [fuente secundaria: https://www.sltcreative.com/costco-business-centers] · [fuente: https://www.costcobusinessdelivery.com/w/-/locations · título SERP] |
| **WebstaurantStore** | Venta online de suministros y alimentación seca | [no medido] | Online; muestra el **precio por bolsa y el precio por libra** a la vez, con descuentos por cantidad | [fuente: https://www.webstaurantstore.com/all-purpose-flour-50-lb/104HR.html] |

### 1.2 Distribuidores de Reino Unido (y nota de Canadá y Australia)

| Distribuidor | Tipo | Tamaño o dato | Cómo compra | Fuente |
|---|---|---|---|---|
| **Brakes** | Broadline (de Sysco, «Sysco GB») | Facturación > £3.500 M | Reparto. Precio por formato y por kg o litro («£33,99 (£1,70/litre)» en el aceite de 20 L) | [fuente secundaria: https://www.gourmetpro.co/blog/uk-top-food-beverage-distributors/] · [fuente: https://www.brake.co.uk/dry-store/oil/vegetable-oil/vegetable-oil/sysco-classic-extended-life-rapeseed-oil/p/9802 · snippet SERP] |
| **Bidfood** (BFS Group, de Bidcorp) | Broadline | £2.300 M (2024) | Reparto | [fuente secundaria: https://en.wikipedia.org/wiki/Bidfood] |
| **Booker** | *Cash & carry* + reparto | 170-200 almacenes | Autoservicio y reparto; también tiene oferta de barriles (su página da 403) | [fuente secundaria: resumen de buscador] · Propiedad de Tesco: [estimado, conocido; no verificado hoy] |
| **JJ Foodservice** | Reparto y recogida | > 30.000 productos | **Dos precios por producto: recogida y reparto**, más escalones por cantidad: harina de 16 kg a £12,49 recogida y £14,49 reparto; £11,49/£13,49 desde 10 unidades; £9,49/£10,49 desde 20. Muestra también el precio **por kg** | [fuente: https://www.jjfoodservice.com/product/england/FLO016] |
| **Costco UK** | Club con reparto a empresas | [no medido] | Formatos de hostelería: harina de 16 kg, tomate troceado 6 × 2,5 kg | [fuente: https://www.costco.co.uk/Business-Delivery/Business-Delivery/Valfrutta-Chopped-Italian-Tomatoes-6-x-25kg/p/34265_BD · título SERP] |
| **Fresh Direct** | Fruta, verdura y frescos (de Sysco desde 2016) | 4 centros (Bicester, Corby, Dagenham y Wigan) y 1.100 empleados | Reparto diario de frescos | [fuente secundaria: resumen de buscador sobre https://www.freshdirect.co.uk/ y Fruitnet] |
| **Philip Dennis Foodservice** | Mayorista regional familiar (suroeste, Oxfordshire y Midlands), con carnicería y pescadería propias | Uno de los **8 mayoristas del grupo de compras Caterforce** | Reparto | [fuente: https://www.philipdennis.co.uk/ · https://www.caterforce.co.uk/our-members/philip-dennis/ · snippets SERP] |
| *Canadá* — Findlay Foods (Kingston, Ontario) | Broadline regional | — | **Catch weight con precio por kilogramo**: se pesa la caja y se refactura al peso exacto | [fuente: https://findlayfoods.com/what-is-catch-weight] |
| *Australia* | — | [no medido] | — | — |

**Para el kit:** EE. UU. compra **por caja**; UK y Canadá, en métrico y con precio por kg/L visible. El kit ya trae las
parejas métricas del ES; lo que falta son **las cajas de EE. UU.** (§1.6).

### 1.3 Cómo se compra y qué pone la factura

1. **Notación pack/size.** El formato se escribe «número de envases / tamaño de cada envase»: `4/10 lb` (4 bolsas
   de 10 lb = caja de 40 lb) [fuente: https://kochfoods.com/products/raw-boneless-skinless-chicken-breast-portions-pieces-trim-blast-blast-frozen-random-size-packed-4-10-lb-poly-bags-in-a-net-40-pound-case/ · título SERP; hoy da 404] ·
   `6/105 oz` (6 latas #10) [fuente: https://www.kraftheinzawayfromhome.com/products/10013000015469-crushed-tomatoes-in-puree-6-105-oz-case-can · título SERP] ·
   `4/1 gal` [fuente: https://darlingtonpackingcompany.com/products/4-1-gal-milk-whole-white · título SERP] ·
   `36/Case` de mantequilla en pastillas de 1 lb [fuente: https://www.webstaurantstore.com/1-lb-unsalted-grade-aa-butter-solid-36-case/874RE3100.html · título SERP].
   En UK: `1x16kg`, `40x250g`, `1x20L`, `6x2.55kg` (títulos de producto de JJ Foodservice, §1.4).
2. **Peso fijo o catch weight.** Carne, pescado, queso y parte del fresco se entregan en caja pero **se facturan
   por el peso real**, a precio por lb o kg: la línea dice «1 case — 50,2 lb × $/lb» [fuente secundaria:
   https://www.inecta.com/blog/calculate-food-catch-weight] · [fuente: https://findlayfoods.com/what-is-catch-weight]
   (precio por kg). **En el kit, un producto en catch weight se compra en `lb` o `kg`, al precio por libra o por kilo
   de la factura. La caja no pinta nada.** («catch weight» = 1.900 búsquedas/mes en EE. UU. y 390 en UK [medido DFS
   24-sep]: es un término que el comprador conoce).
3. **Precio por caja y precio por unidad a la vez.** Las webs de distribuidor imprimen los dos: WebstaurantStore,
   «$29.99/Bag» y «$0.60/Pound» (harina de 50 lb) [fuente: https://www.webstaurantstore.com/all-purpose-flour-50-lb/104HR.html];
   JJ Foodservice, el precio por kg [fuente: https://www.jjfoodservice.com/product/england/FLO016]. Que la **factura**
   del broadline traiga solo el precio de la caja en los productos de peso fijo es **[estimado]**: no he visto una
   factura real de Sysco ni de US Foods. Por eso el kit tiene que admitir las dos entradas (§1.6).
4. **El precio depende de cómo compras.** Recogida o reparto, y escalones por cantidad (JJ, arriba). En el alcohol
   existe además el ***split case fee*** (recargo por romper una caja): Nueva York lo limitó a **$7,39 por caja**
   [fuente: https://www.nfib.com/news/news/new-york-state-liquor-authority-issues-new-rule-to-cap-split-case-fees-on-small-restaurants-taverns-and-liquor-stores/ · snippet SERP]
   · [fuente: https://www.tabc.texas.gov/static/sites/default/files/2020-06/mpb-047.pdf · título SERP]. Regla para
   las Instrucciones: «type the price you actually pay per purchase unit, fees included» [estimado].
5. **Impuesto en las compras.**
   - EE. UU.: Restaurant Depot pide la *sales tax license* a quien revende [fuente: restaurantdepot.com/membership].
     Comprar para revender con *resale certificate* suele ir sin *sales tax*, con reglas que cambian por estado
     [estimado; no verificado estado por estado].
   - UK: «Most food of a kind used for human consumption… is zero-rated». Van siempre a tipo general (20 %) la
     confitería, las bebidas con y sin alcohol, los *crisps* y frutos secos salados y los helados [fuente:
     https://www.gov.uk/guidance/food-products-and-vat-notice-70114]. Un negocio dado de alta en VAT recupera el de
     sus compras, así que en el kit los precios van **sin VAT** [estimado, aplicación de la norma; confirmar con el
     asesor].
   - Consecuencia: los rótulos «Compras netas sin IVA» del 11 y del BONUS pasan a **«Net purchases (excl.
     recoverable tax)»**, no a «ex VAT» a secas.

### 1.4 Tamaños de envase típicos (con fuente por tamaño)

**EE. UU.**

| Producto | Formato habitual | Contenido exacto | Fuente |
|---|---|---|---|
| Pechuga de pollo deshuesada | Caja de **40 lb** (4 bolsas × 10 lb) | 40 lb | [fuente: kochfoods.com (URL en §1.3) · título SERP] · [fuente: https://www.samsclub.com/p/frozen-boneless-skinless-chicken-breast-40lbs-usa/prod9630023 · título SERP] |
| Huevos | Caja de **30 docenas** (la unidad «case» de USDA) o media caja de **15 docenas** | 360 / 180 huevos | «Eggs are generally packed and purchased in 30-dozen cases or half cases of 15 dozen» [fuente: https://www.incredibleegg.org/professionals/foodservice/eggs-egg-products/shell-egg-sizes-grades/] · «case» = 30 docenas en la norma de USDA [fuente: https://www.ams.usda.gov/sites/default/files/media/Shell_Egg_Standard%5B1%5D.pdf · snippet SERP] |
| Harina | Saco de **50 lb** | 50 lb | ADM All Purpose Flour 50 lb, **$29,99/saco = $0,60/lb** (24-sep) [fuente: https://www.webstaurantstore.com/all-purpose-flour-50-lb/104HR.html] |
| Aceite de freír | *Jug-in-box* de **35 lb** | 35 lb **en peso**; «approx 4.5 gallons» | [fuente: https://www.webstaurantstore.com/aak-oasis-peanut-oil-blend-35-lb/101PNUTOIL1.html · título SERP] ⚠️ Se vende al peso y se usa por volumen: es la trampa peso↔volumen |
| Conservas | Lata **#10** (caja de 6) | Neto de **96 oz (6 lb) a 117 oz (7 lb 5 oz)**, de 12 a 13⅔ tazas: **depende del producto** | [fuente: https://foodbuyingguide.fns.usda.gov/FoodComponents/ResourceVegetables] · caja `6/105 oz` [fuente: kraftheinzawayfromhome.com (§1.3) · título SERP] |
| Mantequilla | Caja **36 × 1 lb** | 36 lb / 36 pastillas | [fuente: webstaurantstore.com (§1.3) · títulos SERP de 6 marcas] |
| Leche | Caja **4 × 1 gal** | 4 gal = 512 fl oz | [fuente: https://gfsstore.com/en-us/products/711191 · título SERP] · [fuente: darlingtonpackingcompany.com (§1.3) · título SERP] |
| Destilados | Botella de **750 ml**, 1 L o 1,75 L; caja de **12 × 750 ml = 9 L** | — | Tamaños autorizados (*standards of fill*), entre ellos 1,75 L, 1 L, 750 ml y 700 ml [fuente: https://www.ecfr.gov/current/title-27/chapter-I/subchapter-A/part-5/subpart-K/section-5.203 · snippet SERP] · «A case is 12 750 ml bottles (9 liters)» [fuente: https://americancraftspirits.org/wp-content/uploads/2017/02/Proof-Gallons-Sheet1-2.pdf · snippet SERP] |
| Cerveza envasada | Caja **24 × 12 fl oz** | 288 fl oz (la *case equivalent* del sector) | [fuente secundaria: https://sbstandard.com/case-equivalents/] |
| Cerveza de barril | **1/2 bbl** (15,5 gal) · **1/6 bbl** (5,17 gal) | 1 barril = **31 US gal** | [fuente: https://www.ecfr.gov/current/title-27/chapter-I/subchapter-A/part-25/subpart-B/section-25.11 · snippet SERP; la página redirige a un captcha] |

**Reino Unido**

| Producto | Formato habitual | Fuente |
|---|---|---|
| Harina | Saco de **16 kg** | JJ Plain Flour 1x16kg [fuente: https://www.jjfoodservice.com/product/england/FLO016] · Brakes y Costco UK, 16 kg [títulos SERP] |
| Mantequilla | Caja **40 × 250 g** (10 kg); también 20 × 250 g | [fuente: https://www.jjfoodservice.com/product/england/DAI128/lakeland-unsalted-butter-40x250g/ · título SERP] |
| Aceite | Bidón de **20 L** | [fuente: https://www.jjfoodservice.com/product/england/OIL115 · título SERP] |
| Huevos | Caja de **15 docenas** (180) | [fuente: https://www.brake.co.uk/dairy/eggs/shell/free-range/brakes-15-dozen-fresh-free-range-medium-eggs/p/70327 · título SERP] |
| Tomate en conserva | Lata «A10» de **2,5-2,55 kg**, caja de 6 | [fuente: https://www.jjfoodservice.com/product/WB-MW/VEG597/ · título SERP] · «a10 tin» = 20 búsquedas/mes en UK [medido DFS 24-sep] |
| Destilados | Botella de **70 cl**. Tamaños envasados permitidos: 100, 200, 350, 500, **700**, 1.000, 1.500, 1.750 y 2.000 ml | [fuente secundaria: https://www.theukrules.co.uk/rules/business/sale-of-goods-and-services/weights-and-measures/specified-quantities/, que resume la Weights and Measures (Intoxicating Liquor) Order 1988: https://www.legislation.gov.uk/uksi/1988/2039] |
| Cerveza de barril | Barril de **11 galones imperiales = 50,007 L = 88 pintas**; también de 30 L | Por definición: 1 imp gal = 4,54609 L (NIST HB44 App. C, citado en research §4.3) · [fuente secundaria: https://pinter.co.uk/blogs/news/how-many-pints-in-a-keg] |
| Medidas de servicio | Destilados en 25 ml o 35 ml (y múltiplos); vino en 125 ml, 175 ml y múltiplos; cerveza en **⅓, ½ y ⅔ de pinta** y múltiplos de ½ | [fuente: https://www.legislation.gov.uk/uksi/1988/2039] · ⅔ de pinta desde el 1-oct-2011 [fuente: https://www.legislation.gov.uk/ukdsi/2011/9780111513156] · resumen: [fuente secundaria: theukrules, arriba] |

### 1.5 Del precio por caja al precio por unidad: lo que ya hace la columna «Factor»

La rejilla del ES (01 `Escandallo`, fila 5, leída hoy):
`G (Factor) = VLOOKUP(C&"→"&F, Conversiones!$A$5:$B$37, 2, FALSE)` · `I (Cant. bruta) = E/(1−H)` ·
`J (Coste) = I × D ÷ G`.

El *Factor* es **cuántas unidades de uso caben en una unidad de compra**. Si la unidad de compra es la caja, el kit
divide el precio de la caja sin que el usuario haga nada: es el paso de *culinary math* «cost per unit = AP cost ÷
number of units». La hoja de costes del libro abierto *Culinary Math* (Open Washington) escribe el precio tal cual
viene («APC/Unit: **$23.99/15 pounds**», «**$1.49/10.75-ounce can**») y lo convierte a la unidad de la receta
[fuente: https://openwa.pressbooks.pub/culinarymath/chapter/costing-sheets/, leído con curl porque WebFetch da 403].

Cuentas con la fórmula del kit (J = I × D ÷ G):

| Caso | Unidad de compra | Precio/Ud | Uso | Factor | Coste | Comprobación |
|---|---|---|---|---|---|---|
| Harina de 50 lb, 10 oz en la receta | `50 lb bag` | $29,99 (Webstaurant, 24-sep) | 10 `oz` | 800 | **$0,375** | $0,5998/lb × 0,625 lb = $0,375 ✓ |
| Harina UK de 16 kg, 250 g | `16 kg sack` | £12,49 (JJ, recogida) | 250 `g` | 16.000 | **£0,195** | £0,781/kg × 0,25 = £0,195 ✓ |
| Barril de 1/6 bbl, pinta US de 16 oz | `1/6 bbl keg` | K | 16 `fl oz` | 661,33 | 0,0242 × K | (merma de espuma en *Waste %*) |
| Botella de 750 ml, 1,5 oz | `bottle` | B | 1,5 `fl oz` | 25,36 | 0,0591 × B | — |
| Salmón en catch weight | `lb` | $/lb de la factura | 6 `oz` | 16 | — | La caja no interviene |

**Lo que no se puede meter como clave**, porque el contenido depende del producto:
- **Lata #10:** su peso neto va de 96 a 117 oz según el producto (USDA). Se compra como `can` (precio de la caja ÷ 6)
  y se usa en `can`. Si la receta pide onzas: unidad de compra `oz` y precio = precio de la lata ÷ peso neto de la
  etiqueta.
- **Aceite de 35 lb:** se vende al peso y se usa por volumen. Lo normal es meter el aceite de freidora en el
  **Q-factor** [estimado]. Si se quiere línea a línea, la unidad es `lb`/`oz` pesados.
- **Bunch (manojo):** el ES trae `manojo→g = 30`, que es una estimación. En EN, `bunch` se usa como unidad y no se le
  da peso por defecto.
- **Lata A10 de UK:** el mismo caso que la #10, en kg.

### 1.6 Propuesta: unidades y claves de `Conversions` para la versión inglesa

**Cinco problemas del diseño actual (ES + SPEC D7):**

1. **`case` sin factor posible.** Una caja puede ser 4 galones, 36 libras o 180 huevos. Con `case→each = 12` por
   defecto (research §4.3), una caja de 24 latas o de 180 huevos saldría mal costeada **sin que el kit avise**. Lo
   mismo le pasa al ES en pequeño: «botella→cl = 70» deja un vino de 75 cl un 7 % por debajo, aunque lo avise en
   Instrucciones.
2. **El desplegable no deja crear unidades.** La validación de unidades es una lista literal con estilo de error
   «stop» por defecto (`errorStyle` None, `showErrorMessage` True, leído en 01): el usuario no puede escribir «2/5 lb
   case», así que **toda unidad de caja tiene que venir ya en la lista**.
3. **El rango del VLOOKUP no deja sitio.** `Conversiones!$A$5:$B$37` termina en la última fila de la tabla y las
   Instrucciones ES prometen «añade las parejas que te falten» (01 `Instrucciones`). Una pareja nueva escrita debajo
   no se encuentra. **Es un defecto del ES**, que no se toca en esta tarea; en EN se corrige dejando filas vacías
   dentro del rango.
4. **Parejas imposibles de alcanzar.** El research §4.3 propone `UK fl oz→ml`, `imperial gallon→L`, `bottle (1 L)` y
   `bottle (1.75 L)`, pero el desplegable de D7 no tiene esas unidades. Son filas que ningún usuario puede usar.
5. **04 `Formatos de Compra` trabaja en cl.** `D = ROUND(C×100/B, 4)` convierte el precio de la botella a €/L con el
   tamaño en cl. En EE. UU. el tamaño es legalmente en ml (27 CFR 5.203) y un «75» se lee mal.

**Unidades propuestas (33), todas en una sola lista literal de 241 caracteres:**

```
lb,oz,kg,g,gal,qt,pt,imp pt,cup,fl oz,tbsp,tsp,L,ml,cl,each,dozen,bunch,can,bottle,15 dz case,30 dz case,50 lb bag,40 lb case,36x1 lb case,16 kg sack,40x250 g case,4x1 gal case,12x750 ml case,24x12 fl oz case,1/2 bbl keg,1/6 bbl keg,50 L keg
```

| Unidad | Dimensión | Tamaño base (exacto) | Fuente del tamaño / de que el formato es habitual |
|---|---|---|---|
| lb · oz · kg · g | peso | 1 lb = 453,59237 g; 1 oz = lb/16 | NIST HB44 App. C (research §4.3) |
| gal · qt · pt · cup · fl oz · tbsp · tsp | volumen US | 1 fl oz = 29,5735295625 ml; gal 128, qt 32, pt 16, cup 8 fl oz; tbsp = ½ fl oz; tsp = ⅙ fl oz | NIST (ídem) |
| L · ml · cl | volumen métrico | definición | — |
| **imp pt** | volumen UK | 568,26125 ml | NIST/UK (research §4.3). Hace falta para el *pour cost* de la cerveza de barril en UK (medidas en pintas, §1.4) |
| each · dozen | recuento | dozen = 12 each | definición |
| bunch | aparte | solo `bunch→bunch` y `bunch→each` = 1 | sin peso por defecto (§1.5) |
| can | volumen (por defecto) | **12 fl oz** (355 ml); nota «UK: 330 ml → edit» | igual que la `lata = 33 cl` del ES |
| bottle | volumen (por defecto) | **750 ml** (25,3605 fl oz); nota «UK spirits: 70 cl → edit» | 27 CFR 5.203 · UK: 700 ml (§1.4) |
| 15 dz case · 30 dz case | recuento | 180 · 360 each | American Egg Board / USDA (§1.4) |
| 50 lb bag · 40 lb case · 36x1 lb case | peso | 50 · 40 · 36 lb (+ `36x1 lb case→each` = 36) | Webstaurant, Koch, Sam's (§1.4) |
| 16 kg sack · 40x250 g case | peso | 16.000 g · 10.000 g (+ `→each` = 40) | JJ, Brakes, Costco UK (§1.4) |
| 4x1 gal case | volumen | 512 fl oz (+ `→each` = 4) | GFS, Darlington (§1.4) |
| 12x750 ml case | volumen | 9.000 ml (+ `→bottle` / `→each` = 12) | ACSA (§1.4) |
| 24x12 fl oz case | volumen | 288 fl oz (+ `→can` / `→each` = 24) | *case equivalent* (§1.4) |
| 1/2 bbl keg · 1/6 bbl keg | volumen | 15,5 gal = 1.984 fl oz · 31/6 gal = 661,33 fl oz | 27 CFR 25.11 (§1.4) |
| 50 L keg | volumen | **11 imp gal = 50,00699 L → 88 imp pt exactas**; nota «UK 11-gallon keg» | §1.4 |

**Regla de generación de claves** (la aplica `mapas.py`; nada a mano):
- Clave `compra→uso` para **cada pareja de la misma dimensión**. Factor = tamaño(compra) ÷ tamaño(uso).
- Los formatos (packs) solo aparecen como unidad de compra, más su identidad `pack→pack` = 1 y sus subunidades
  (`→each`, `→bottle`, `→can`).
- `tbsp`, `tsp` y `cup` no se ofrecen como destino de barriles ni de cajas de bebida.
- `can` y `bottle` solo se convierten a unidades de volumen, a `each` y a sí mismas.

Resultado, simulado en el scratchpad: **224 claves únicas**. La regla hace imposibles el duplicado y la pareja
peso↔volumen. Algunos factores: `50 lb bag→oz` 800 · `40 lb case→oz` 640 · `15 dz case→each` 180 ·
`4x1 gal case→fl oz` 512 · `12x750 ml case→fl oz` 304,326 · `1/2 bbl keg→fl oz` 1.984 ·
`1/6 bbl keg→fl oz` 661,333 · `bottle→fl oz` 25,3605 · `gal→L` 3,78541 · `imp pt→ml` 568,261.
Columna C («What it means») generada: «1 × 50 lb bag = 800 oz».

**Qué implica para la F2:**
- El rango `Conversions!$A$5:$B$<n>` pasa a **fila 228 + ~30 vacías** (p. ej. `$A$5:$B$260`), reescrito en las 453
  fórmulas G de 01-08 con el mismo mapa (SPEC §2.3).
- **La DV sigue siendo UNA regla literal por hoja** (p. ej. `C5:C24 F5:F24` en 01; 29 reglas en total): cambia su
  lista, no su estructura. Sheets: sin riesgo
  nuevo (research §8.2).
- Gate §2.3 ampliado: cada clave de la tabla usa unidades que están en la lista; la lista cabe en 255 caracteres; no
  hay claves repetidas; ninguna pareja cruza de dimensión.
- 04 `Bottle Sizes`: **columna en ml y constante 1000** (`=IFERROR(ROUND(C×1000/B,4),"")`), declarada como excepción
  de fórmula en el gate de paridad. **Alternativa sin excepción:** dejar cl y rotular «Bottle size (cl) — 750 ml =
  75 cl». Recomiendo ml: la TTB y cualquier factura estadounidense lo escriben en ml. Las pestañas de cóctel siguen
  con compra en `L` (precio por litro de `Bottle Sizes`) y uso en `fl oz` (EE. UU.) o `ml` (UK), por el factor.
- **Opción no recomendada ahora:** que la DV de unidades lea una columna de `Conversions` para que el usuario pueda
  añadir sus propias cajas. Serían 29 reglas que dejan de ser literales (el mismo patrón que la DV de categorías, que
  lee `Mermas!`) y el ES no lo tiene. La alternativa documentada es suficiente: si tu caja no está en la lista, compra
  en `lb`/`each` y divide el precio de la caja.

**Texto «From invoice to price per unit»** para las Instrucciones (contenido, redacción EN en la F2):
① catch weight → compra en `lb`/`kg` al precio por libra o kilo de la factura; ② caja de peso fijo que esté en la
lista → elige el formato y escribe el precio de la caja tal cual; ③ caja que no esté → compra en `lb`/`each`/`gal` y
escribe precio de la caja ÷ contenido (el *pack/size* de la factura: `4/10 lb` = 40 lb); ④ lata #10 → peso neto de
la etiqueta; ⑤ aceite de freidora → Q-factor; ⑥ precios sin el impuesto recuperable; ⑦ muchas webs de distribuidor
ya imprimen el precio por lb o por kg: si lo tienes, úsalo.

### 1.7 Ejemplos precargados (D10-D11)

Para que la adaptación se vea, las filas de ejemplo tienen que mostrar los tres casos: **catch weight** (01, solomillo
en `lb`), **caja** (05 Croissants: harina `50 lb bag` $29,99 [fuente: Webstaurant 24-sep], mantequilla `36x1 lb case`,
leche `4x1 gal case`, huevos `15 dz case`; los precios que falten, con fuente en `mercado_en.json` o `[estimado]`) y
**botella** (04, a través de `Bottle Sizes`). Hoy el 05 ES compra harina y mantequilla por `kg` y huevos por `docena`
(leído en `Croissants!C5:C11`).

---

## 2. Bloque 7 · Documentación propia del mercado EN

### 2.1 Qué enseñan los temarios

| Temario | Qué pide, relevante para un kit de costes | Fuente |
|---|---|---|
| **ProStart 2** (NRAEF; estándares de Utah revisados en **junio de 2025**) | «Develop a recipe cost card for a standardized recipe» · «Analyze plate cost and drink cost» · «Formulate a new yield for an existing recipe using a **conversion factor**» · «Calculate the price of a menu item using the food cost percentage method» · «Define the **Q factor**» · «Explain the purposes of a **menu sales mix analysis**» y «the four classifications of menu items» · «Recognize the importance of inventory value» · «perpetual inventory and physical inventory systems» · «Understand how **prime cost** affects labor costing» · «make-or-buy analysis» | [fuente: https://www.schools.utah.gov/cte/_cte/strands/ProStart2.pdf, texto extraído del PDF] |
| **Culinary Math** (Open Washington, libro abierto) | Capítulos: 4 *Conversion Factors for Changing Recipe Yields* · 8 *Common Measurements* · 9 *The Metric System* · 11 *Conversions Between the Metric and Common Systems* · **12 *Conversions for Volume and Weight*** · 13 *Yield Percents* · 14 *Edible Portion Cost* · 15 *Costing Sheets* | [fuente: openwa.pressbooks.pub (§1.5)] |
| **Culinary Math**, CIA (Blocker y Hill, 4.ª ed., Wiley, 2016) | Yield percent, edible portion cost, recipe size conversion (según el buscador; el índice en PDF no se pudo leer) | [fuente secundaria: https://www.wiley.com/en-us/Culinary+Math,+4th+Edition-p-9781119195580R150 · resumen de buscador] |
| The Culinary Pro | *AP/EP*, *Trim & Waste*, **«Butcher's Yield Test»** («used to determine portion cost, edible trim, and yield percentage»), *Recipe Conversion Factor (RCF)* | [fuente: https://www.theculinarypro.com/culinary-math] |
| **City & Guilds 7133**, Level 3 Diploma in Professional Cookery (UK) | «**K14. Explain how to cost proposed recipes and work out gross profit**» (p. 45) · «State the **approximate yields** of prepared fish / shellfish / poultry / game» · «approximate yields of prepared meat and how to make use of **by-products**» (pp. 53-65) · «computerised stock control systems» (p. 38) | [fuente: https://www.cityandguilds.com/-/media/productdocuments/hospitality_and_catering/hospitality_and_catering/7133/7133_level_3/centre_documents/7133_l3_qualification_handbook_v2-7-pdf.pdf, extraído con pypdf] |

### 2.2 Qué traen los competidores

| Oferta | Lo que trae y el kit ES no | Fuente |
|---|---|---|
| **Someka** Food Cost ($29,95) | Hoja **Raw Materials** (base de ingredientes: el precio se escribe una vez y las recetas lo leen), hasta 400 recetas, *yield %*, **Sales Summary** y *dashboard* | [fuente: https://www.someka.net/products/food-cost-google-sheets-template/] |
| foodcostchef (gratis) | Tablas de ingredientes por categoría de las que tiran las recetas; al cambiar un precio se actualizan todas; subrecetas (salsas costeadas por ración) | [fuente: https://foodcostchef.com/free-recipe-costing-template/] |
| spreadsheet123 (gratis) | Conmutador imperial/métrico; filas de **mano de obra y suministros** por ración; espacio para foto, **alérgenos**, notas de elaboración y firmas | [fuente: https://www.spreadsheet123.com/calculators/recipe-cost-calculator.html] |
| chefs-resources ($6,75/mes) | **Beef Butchering Yield Form**, **Fish Filleting Log**, Food Cost Calculation Form, **Declining Balance Sheet**, Inventory Turns Calculator, Order Guide, Baker's Recipe Template, Labor Cost | [fuente: https://www.chefs-resources.com/kitchen-forms/] |
| excel.tv (gratis) | *Inventory* con **par level y aviso de reposición**, *Usage & COGS*, P&L con **prime cost** y *dashboard* | [fuente: https://excel.tv/restaurant-inventory-spreadsheet/] |
| Toast (gratis) | Plantillas de inventario de cocina y de bar | [fuente: https://pos.toasttab.com/resources/food-inventory-template · título SERP] |
| Etsy (paquetes) | «Recipe Costing & Menu Pricing Spreadsheet» a **$7,99**; otro a **$12,30 (antes $20,50)** | [fuente: https://www.etsy.com/market/restaurant_food_cost_spreadsheet y https://www.etsy.com/market/restaurant_food_cost_template · snippets SERP 24-sep] |
| Excel Highway ($39) | Base de ingredientes y subrecetas (ya en research §5.1) | research §5.1 |

### 2.3 Demanda medida [medido DFS 24-sep], con la intención comprobada donde el número engaña

| Tema | EE. UU. | UK | Intención |
|---|---|---|---|
| Yield test | butcher's yield test 20 · yield test 70 · meat yield test 10 · **yield percentage 320** · cooking loss test 20 · yield test template / cooked yield test / raw yield test: sin dato | butchers yield test 10 · yield test 10 · yield percentage 20 · cooking loss 10 | Oficio; casi sin demanda de plantilla |
| Escalado | recipe scaling calculator 390 · how to scale a recipe 320 · recipe conversion factor 140 · recipe conversion calculator **1.300** | 30 · — · 10 · 30 | «recipe conversion calculator» = **cocina doméstica** (SERP: conversores de tazas a gramos, apps de recetas) |
| Plate cost / Q-factor | plate cost 320 · plate cost calculator 50 · q factor food cost 20 | plate cost 30 | Oficio |
| Precios / facturas | invoice tracker 720 (genérica, sin verificar) · food price tracker 40 · ingredient price tracker: sin dato | invoice tracker 260 · food price tracker 10 | No hay demanda de «price tracker» de cocina |
| Inventario / par | **par level 1.600** (SERP mezclada: restaurante, sanidad, *vending*) · par sheet 260 · restaurant par sheet 50 · par level template 10 · inventory count sheet 210 · kitchen inventory template 480 · restaurant inventory template 210 · bar inventory template 140 | stock take template 140 · par levels 140 · stock take sheet 70 · par sheet 30 | Real, pero es de **inventario** |
| COGS semanal | weekly food cost 10 · restaurant cogs 110 · cost of goods sold restaurant 40 | — | Poca |
| Prime cost | prime cost 4.400 → **SERP = coste de Amazon Prime** · **prime cost restaurant 260** · prime cost calculator 30 | prime cost 1.000 (intención sin verificar) · labour cost percentage 10 | Solo cuenta el de 260 |
| Bar | pour cost calculator 260 (research) · liquor cost calculator 140 · pour cost 110 · standard pour **14.800 → SERP = un bar de Dallas** («The Standard Pour») | **spirit measures uk 1.000** · **wine measures uk 390** · pour cost 10 | UK busca las medidas legales |
| Menu engineering | 480 (research) · worksheet 30 · template 10 · menu mix 70 | 140 · template 10 | Informativa |
| Batch / prep | batch recipe cost 0 · prep sheet template 50 | — | — |
| Subrecetas | «sub recipe» 720 → **SERP = bocadillo *sub*** | 50 | Sin demanda del oficio medible |
| Receta estandarizada | standardized recipe template 110 · standardized recipe card 30 | — | Pequeña |
| Mermas | food waste log 170 · kitchen waste log 170 · food waste tracking sheet 10 | wastage sheet 90 · wastage log 20 · kitchen wastage sheet 20 | Cubierto por el 09 |
| Compras | catch weight 1.900 · number 10 can 880 · #10 can size 320 · case of chicken 480 | 390 · a10 tin 20 · 10 | El comprador busca tamaños de envase: refuerza §1.6 |

### 2.4 Candidatos: evidencia, qué cubre el ES y recomendación

(a) = ya cubierto · (b) = adaptación pequeña de un fichero existente · (c) = fichero u hoja NUEVO (lo aprueba John)

| Candidato | Evidencia | ¿Lo cubre el ES? | Recomendación |
|---|---|---|---|
| **Butcher's / raw yield test** | Temarios: The Culinary Pro, Culinary Math cap. 13, C&G 7133 («approximate yields… by-products»). Competencia: chefs-resources (formularios de despiece de vacuno y de fileteado de pescado). Demanda de plantilla: casi nula (≤ 70) | **En parte.** Columna *Waste %* por ingrediente y hoja *Waste Factors* con 21 categorías (típica, mínima y máxima) en 01-08. Da un porcentaje de partida; no enseña a medir el tuyo ni el valor del recorte | **(b)** Texto en Instrucciones y en *Waste Factors*: «Measure your own yield: weigh AP, weigh usable trim, waste % = 1 − usable ÷ AP; type it in the Waste % column». Más una referencia pública de rendimientos: USDA Food Buying Guide (https://foodbuyingguide.fns.usda.gov/FoodComponents/ResourceVegetables; sus rendimientos son de preparación en el centro). **(c) opcional:** hoja *Yield Test* (AP weight, by-products y su valor, usable weight, yield %, cost per usable lb, cost factor). Es la hoja nueva con más respaldo académico. No es imprescindible |
| **Cooking loss test** | Mismo temario; demanda 10-20 | **En parte.** El 05 ya mete la pérdida de horneado como merma (8 % en harinas) | **(b)** Una línea: «If you portion by COOKED weight (e.g. a 6 oz cooked burger), add the cooking loss to the Waste %» |
| **Recipe scaling (conversion factor)** | ProStart 2 lo pide literalmente; Culinary Math cap. 4; 390 búsquedas en EE. UU. (el 1.300 es doméstico) | **No.** «Number of portions» reparte el coste, pero no escala cantidades | **(b)** Texto: «New qty = recipe qty × (new yield ÷ old yield)», y aclarar que el coste por ración no cambia al escalar. **(c)** Columna «scaled qty»: cambiaría la rejilla de 71 hojas. No lo recomiendo |
| **Plate cost con Q-factor** | ProStart («Define the Q factor»); plate cost 320 | **Sí.** «Coste elaboración (%)» al 10 % | **(a)**, con el rótulo *Q-factor* de D8 |
| **Invoice price tracker / ingredient master list** | La tiene toda la competencia de pago (Someka *Raw Materials*, Excel Highway, foodcostchef). Demanda como «price tracker»: ~0 | **No.** El precio va en cada fila de cada escandallo; solo el 04 enlaza precios desde `Formatos de Compra`. El Kit de Inventario ES tiene «variación de precios entre proveedores» (`astro-site/src/data/productos/kits/kit-inventario.ts:141,155`) | **(c)** Es la carencia más visible frente a Someka, pero obliga a cambiar la fórmula del precio en 8 ficheros. **No en la v1 EN.** La landing no lo promete; la FAQ dice «each cost card is self-contained» |
| **Inventory count sheet con par levels** | Toast, excel.tv; par sheet 260, stock take template 140 (UK) | **En parte.** BONUS *Inventory* (existencias iniciales, compras, finales y consumo teórico), sin par | **(a) fuera de alcance:** par levels y punto de pedido son del **Kit de Inventario** ES (`kit-inventario.ts:112,135,143`), que tendrá su versión EN propia. Meterlo aquí le quitaría ventas a ese producto |
| **Weekly COGS / food cost** | R365 enseña el método semana a semana (inventario al inicio y al final de la semana) [fuente secundaria: https://www.restaurant365.com/blog/calculating-food-costs-how-to-nail-down-this-ops-cost-enigma/]; demanda mínima | **En parte.** El 11 es mensual (12 filas); el BONUS deja el periodo libre | **(b)** Solo texto: cabecera «Period (month or week)» en el 11, e Instrucciones con el método semanal usando el BONUS. Las 12 filas y el gráfico no cambian. Un calendario de 13 periodos de 4 semanas necesitaría una fila más (c): no |
| **Prime cost tracker** | ProStart; «prime cost restaurant» 260 | **No.** Lo trae el Kit Plan Financiero ES (`kit-plan-financiero.ts:170-171`) | **(a) fuera de alcance.** Como mucho, un párrafo en el PDF bonus con el umbral < 60-65 % (research §2.1). Sin hoja |
| **Pour cost por categoría y pours estándar** | UK: spirit measures uk 1.000, wine measures uk 390; EE. UU.: pour cost/liquor cost 110-260. Benchmarks por categoría en research §2.1 (Backbar) | **En parte.** El 04 calcula 4 cócteles con `Formatos de Compra`; un único rango de bar | **(b)** ① Tabla de medidas en Instrucciones del 04: US 1,5 fl oz de destilado, 5 fl oz de vino y 12 fl oz de cerveza (NIAAA, research §4.1); UK 25/35 ml, 125/175 ml y ⅓, ½ y ⅔ de pinta (§1.4). ② Pour cost por categoría: destilados 18-20 %, cerveza de barril ≈ 20 %, botella ≈ 25 %, vino más alto (research §2.1). ③ En `Bottle Sizes`, precargar en 2 de las 5 filas vacías (`A12:C16`) un vino de 750 ml y un barril de 1/6 bbl. Las 4 pestañas de cóctel no cambian |
| **Menu engineering** | ProStart (sales mix, 4 clasificaciones); 480 US / 140 UK | **No.** Vive en la Guía Food Cost + Ingeniería de Menú (ES) | **(a) fuera de alcance, y no se promete** (D15). Candidato a producto EN propio más adelante |
| **Batch / prep costing** | Culinary Math cap. 15 | **Sí.** El 05 trabaja por tanda completa con rendimiento en unidades, y cualquier ficha se puede costear por tanda con «Number of portions» | **(a)** |
| **Subrecetas** | Competencia (foodcostchef, Excel Highway, meez); sin demanda medible (el 720 de «sub recipe» son bocadillos) | **En parte.** El 01 ya usa una subreceta como ingrediente con precio («fondo oscuro 12 €/L»), sin enlace | **(b)** Texto: «Cost the stock/sauce/dough on a spare card with portions = batch yield in qt/L/lb; use its cost per portion as the ingredient price» |
| *Extra:* **volumen↔peso de los secos** (tazas y cucharadas) | Culinary Math cap. 12 (tabla de volumen a peso) y la hoja de costes del mismo libro pasan de «¼ teaspoon» de sal a un precio por libra | **No, a propósito** (D7: nunca peso↔volumen) | **(b)** Aviso claro. Un estadounidense que escriba «2 cups flour» contra una compra en `lb` verá «?» y «check units». Instrucciones: «Pro kitchens weigh: enter dry goods in oz/g; if your recipe is in cups, weigh one cup once». **No** meter densidades en `Conversions` |
| *Extra:* **receta estandarizada** (elaboración y alérgenos) | ProStart («recipe cost card for a standardized recipe»); spreadsheet123 trae campos de alérgenos y notas; «standardized recipe template» 110 | **En parte.** Foto del plato sí; campos de elaboración y alérgenos no | **(c)** No ahora. Research §7: un kit de costes no es un plan de alérgenos |

### 2.5 Veredicto honesto

**Nada de esta lista es imprescindible para lanzar.** El kit ES ya cubre el núcleo de lo que enseñan ProStart y
Culinary Math:
- *recipe cost card* con *AP/EP* (Waste % → AP qty);
- *Q-factor*;
- *plate cost* y *drink cost*;
- precio de carta por el método del food cost %;
- food cost por inventario;
- consumo teórico frente a real (BONUS);
- control de desperdicio (09).

Para UK, el *GP %* de C&G K14 ya está decidido en D8. Lo que el mercado EN espera y hoy falta es barato de cubrir:
**comprar por caja** (§1.6, sin cambiar estructura) y **explicar** yield test, escalado, subrecetas y pesaje (texto).

Las dos piezas de la competencia que el kit no tiene, **la base de precios de ingredientes y la hoja de yield test**,
son hojas nuevas (c). La primera choca además con el Kit de Inventario. Si John las quiere, mejor en una versión
posterior del ES y del EN a la vez, para no romper la paridad que exige la regla de copia.

### 2.6 Lo que supone la opción (b), fichero por fichero

| Fichero EN | Cambio (contenido, salvo lo marcado) |
|---|---|
| 01-08 `Conversions` | Tabla de §1.6 (≈ 224 claves + ~30 filas vacías); rango del VLOOKUP reescrito |
| 01-08 lista de unidades (DV) | Lista de 33 unidades y 241 caracteres (§1.6) |
| 01-08 `Instructions` | Bloques: «From invoice to price per unit» (§1.6), «Measure your own yield», «Cooking loss», «Scaling a recipe», «Sub-recipes», «Weigh dry goods» |
| 01-08 `Waste Factors` | Nota A2: «Typical % is a starting point — measure yours (see Instructions) or check USDA Food Buying Guide yields» |
| 04 `Bottle Sizes` | Columna en ml y constante 1000 (**excepción de fórmula declarada**), 2 filas precargadas (vino 750 ml, 1/6 bbl) |
| 04 `Instructions` | Tabla de medidas US/UK y *pour cost* por categoría |
| 05 · 07 ejemplos | Filas con formatos de caja (§1.7) |
| 11 `Dashboard` | Cabecera «Period (month or week)» + texto del método semanal |
| 11 · BONUS | «Net purchases (excl. recoverable tax)» |
| PDF bonus | Párrafo de *prime cost* (< 60-65 %) en la semana 4; cómo leer una factura de caja y de catch weight en la semana 1 |

### 2.7 Opciones (c) para John (cambian la estructura, no están en la SPEC)

1. **Hoja *Yield Test*** en 01-03 y 05-08 (o un fichero 12 aparte). A favor: temario US y UK, formularios de
   chefs-resources. En contra: demanda de plantilla casi nula y rompe la paridad con el ES. **Recomendación: no en la v1
   EN.**
2. **Hoja *Ingredient Price List*** que alimente el precio de las fichas. A favor: es la ventaja que venden Someka y
   Excel Highway. En contra: reescribir la columna de precio en 8 ficheros; se solapa con el Kit de Inventario.
   **Recomendación: no.**

---

## 3. Bloque 8 (solo huecos): ¿aguantan los $19?

**Sí, y nada de los bloques 4 y 7 lo cambia.**
- Las adaptaciones (b) son contenido: no añaden piezas que justifiquen subir el precio de salida.
- Lo que tienen Someka ($29,95) y Excel Highway ($39) y el kit no (base de ingredientes) confirma que el kit tiene
  que salir **por debajo** de ellos, como ya decía el research §5.2.
- La SERP de hoy añade dos paquetes de Etsy a **$7,99** y **$12,30** (antes $20,50) (§2.2): el techo de la gama baja
  está por debajo de $19. Los 11 formatos de negocio y los 2 bonus son lo que justifica la diferencia.
- Si algún día se aprueban las hojas (c), serían el argumento para pasar a **$24**, junto con las reseñas EN reales
  que ya pedía el research.

---

## 4. Cambios para pegar en la SPEC

1. **D7:** desplegable EN = la lista de §1.6 (33 unidades, 241 caracteres; **sin `case`**, con `imp pt` y 13
   formatos). `Conversions` generada por la regla de §1.6 (≈ 224 claves), con `bottle` = 750 ml y `can` = 12 fl oz
   editables y avisos UK de 70 cl y 330 ml. Sin peso por defecto para `bunch`. Fuera las filas UK fl oz / imperial
   gallon / 1 L / 1,75 L de research §4.3.
2. **§2.3:** rango `Conversions!$A$5:$B$260` (tabla + ~30 filas vacías). Gates: lista ≤ 255 caracteres; claves
   únicas; ninguna pareja cruza de dimensión; todas las unidades de la tabla están en la lista.
3. **§2.4 / gate 1:** excepción declarada para la constante 100→1000 de 04 `Bottle Sizes!D5:D16` (si se elige ml).
4. **§2.5:** 01-08 con el bloque de Instrucciones de §2.6; 04 con medidas y pour cost por categoría y 2 filas
   precargadas; 05/07 con ejemplos en formato de caja; 11 «Period (month or week)»; 11 y BONUS «Net purchases (excl.
   recoverable tax)».
5. **§2.6 (PDF):** prime cost en la semana 4 y lectura de factura (caja, catch weight, pack/size) en la semana 1.
6. **§3 (landing):** FAQ «Does it handle case prices and catch weight?» (sí) y «Does it include par levels / menu
   engineering / an ingredient price database / a butcher's yield test?» (no, con el porqué). Lista de columnas: añadir
   «Purchase unit (case, bag, keg…)».
7. **§5 (John):** decidir si quiere las opciones (c) de §2.7; la recomendación es no en la v1.

### Log

- **2026-09-24 (sesión Claude Code):** bloques 4 y 7 y huecos del 8. DataForSEO: 63 keywords US y 45 UK; SERP de
  «standard pour», «prime cost», «par level», «recipe conversion calculator», «sub recipe» (US), «costing sheet» (UK)
  y paquetes de Etsy (US). Lectura con openpyxl de `Conversiones`, DV, 04, 05, 09, 10, 11 y BONUS del ES, en serie
  (CPU 42-55 °C). PDF de City & Guilds 7133 y ProStart de Utah extraídos con pypdf en el scratchpad. Simulación de
  claves en `scratchpad/keys_en.py` (no va al repo). No se ha tocado ningún fichero del kit.
