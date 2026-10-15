# Decisiones fijadas por las tandas ya traducidas (léelas antes de traducir la tuya)

> Cada tanda que cierra añade aquí lo que las demás deben respetar. Manda sobre el brief en lo que concrete.

## T02 (cap. 3-4, opus, 15-oct)

- **Títulos**: cap. 3 «Sales Tax, VAT and the Error That Breaks Your Food Cost %» · cap. 4 «The Real Purchase Cost:
  What Actually Belongs on the Invoice Line». Cítalos así si los referencias.
- **Ejemplo conductor**: plate cost **$5.67**, precio de carta **$17.30 pre-tax**, food cost **32.8%**, margen **$11.63**.
  Sales tax ilustrativo redondo de **10%** (marcado como ilustrativo): el cliente paga $19.03 y el food cost mal
  calculado sale 29.8%. UK imprime 20.76 (÷ 1.20); Australia 19.03 (GST 1/11 = 1.73). **UK y AU sin símbolo de moneda.**
- **Matriz de impuesto del simulador multicanal** (pestaña "Inputs"): 9 celdas a **0.0%** por defecto. Filas
  Dine-in / Takeout / Third-party delivery; columnas Food / Soft drink or sweetened drink / Alcoholic drink. US y Canadá
  la dejan a 0% y teclean precios pre-tax; UK 20% (0% en comida fría para llevar zero-rated); AU 10%.
  **Nunca decir a un usuario US que teclee su sales tax ahí**: las fórmulas tratan el precio como impuesto incluido.
- **TPV**: no afirmar que las «gross sales» del POS incluyen impuesto (en Toast/Square no). Decir que el total más
  grande del POS lleva impuesto y propinas → usar **net sales** (tras descuentos, antes de impuesto y propinas). Las
  propinas nunca son venta; un service charge obligatorio en EE. UU. es ingreso que se paga como salario, en su línea.
- **Factura** (hoja "Invoice & Tax Check"): cabecera de 9 columnas `# · Item · Quantity · Unit · Unit price pre-tax ($) ·
  Line amount pre-tax ($) · Tax rate (%) · Tax ($) · Line total ($)`; 0% en todas las líneas (768.40 / 0.00 / 768.40).
  kg → lb exacto (26.46 lb a $7.17…); **el aceite de oliva sigue en L** y el vino en 750 ml.
- **Términos fijados**: "Cost Card", "Inputs", "Invoice & Tax Check"; «input VAT on your VAT return» / «input tax
  credits» / «GST credits»; «registered for VAT or GST/HST»; «Iberico pork tenderloin» (sin tilde); «operating supplies»
  (limpieza y menaje).
- **Para el xlsx**: guardar cantidades y precios **sin redondear** (conversión exacta) para que los importes de línea
  sean idénticos a los del ES; el texto avisa de que multiplicar a mano las cifras redondeadas puede variar céntimos.

## T08 (cap. 15-16, opus, 15-oct)

- **Títulos**: cap. 15 «Multichannel: Dine-In, Takeout and Third-Party Delivery» · cap. 16 «Beverage Cost: The Bar as a P&L of Its Own». Canales: Dine-in / Takeout / Third-party delivery. «Parámetros» → "Inputs", «Resumen» → "Summary", «Resumen Bodega» → "Beverage Summary".
- **Croquetas**: «the croquettes» (coste $2.10, carta $8.60): 24.4% dine-in, 46.5% delivery, precio necesario **$10.00 pre-tax**, techo **$11.60**. Packaging $1.75/pedido ÷ 2.5 = $0.70; comisión 30%; objetivos 30/30/40%. Carta de **20 platos**: 16 viables en sala, 12 en delivery, 8 fuera (el ES decía «de los 16… los otros 8»: corregido).
- **Comisiones de plataforma**: sin Glovo/Uber/Just Eat/Deliveroo ni fuente qamarero ni «+ IVA». La tabla de 4 filas pasa a **tipos de contrato** como «working examples» del guide: Zone-priced plan (15-35%, ~$39/mes) · Tiered plan (30/25/15-20%) · Marketplace listing (13% / 25-35% / $0.30 por pedido) · Volume plan (30%, 25% desde 500 pedidos/mes, $50/mes). **El xlsx EN ("Inputs") debe llevar esas mismas 4 filas**. Apps citadas: US DoorDash, Uber Eats, Grubhub; UK Deliveroo, Just Eat.
- **Bebidas**: «bodega» → «the bar». Estudio CaixaBankLab/elBulli → «a 2026 European industry study» (28% / 34.5%, mix 70/30); qamarero → «another industry source»; getbackbar.com y purimax.com se mantienen. «Combinados» → **spirits and highballs (21.6%)**, cócteles 19.7% (el ES decía que 21.6% estaba bajo el 20%: corregido).
- **Unidades (D8)**: barril «30 L keg» (7.93 gal; 120 pours de 8.45 fl oz / 60 de 16.91 fl oz); tercio y lata «330 ml, 11.16 fl oz»; agua «500 ml, 16.91 fl oz»; zumo de naranja **$0.64 por lb, 1.81 servings por lb**, $0.35 por servicio. Copa: 750 ml ÷ 5 = 150 ml = 5.07 fl oz; pour US 1.5 fl oz; UK 25/35 ml destilado, 125/175 ml vino.
- **Vinos**: House red (young Tempranillo) · Rioja Crianza · Ribera del Duero Roble · Rueda Verdejo · Rias Baixas Albariño (sin tilde en Rias) · Cava Brut Nature · Navarra Rosé · Pedro Ximénez dessert wine.

## T01 (portada, índice y cap. 1-2, sonnet, 15-oct)

- **Títulos EN de los 20 capítulos** (tal cual en el índice): 1 Who This Guide Is For (and What You Will Not Find Here) · 2 The Four Numbers That Run Your Menu · 3-4 y 15-16 como T02/T08 · 5 From AP to EP: Trim Loss, Yield and the Test That Replaces the Chart · 6 The Recipe Cost Card That Survives an Audit · 7 Theoretical vs. Actual Food Cost: Where the Money Leaks · 8 Prime Cost: The Metric That Measures the Health of the Business · 9 Four Ways to Price a Dish · 10 Pricing Psychology: What Is Proven and What Is Myth · 11 Menu Engineering I: Kasavana & Smith Done Right · 12 Menu Engineering II: What the Classic Matrix Can't See · 13 When the Methods Disagree: The Decision Protocol · 14 Short Menus, Prix Fixe, Buffets and Banquets · 17 Batch Costing for Commissary Kitchens and Pastry · 18 When Your Supplier Raises Prices: The Re-Costing Protocol · 19 The Full Case: One Entire Menu, Start to Finish · 20 When Your Spreadsheet Falls Short
- «Índice» → «Table of Contents». Kit de Escandallos → **Food Cost Kit Pro**; plan-financiero → «Restaurant Financial Plan Kit Pro».
- Hojas citadas: "Data" (menu-engineering-matrix), "Cost Card" (recipe-cost-card), "Inputs" y "Monthly" (prime-cost-dashboard), "Tracking KPIs" (90-day-action-plan). Familias: Starters / Mains / Desserts. Meses y lecturas: «Above target» / «On target».
- Informes españoles (CaixaBankLab, qamarero) quitados: rangos de food cost (25-35%, por formato) y estructura de costes (labor 30-35, rent 5-10, overhead 13-20, EBITDA 10-13) quedan como «commonly cited» / «reference ranges the pack works with», sin fuente. Un ⟦ADAPT⟧ en cap. 1 sobre la banda EBITDA 10-13% para la pasada Opus.
- Gate: T01 sale ERROR [j-cifras] por el «21» del título ES del cap. 4 (tipo español eliminado, D7): correr con `--fiscal` (OK) o ignorar.

## T03 (cap. 5-6, sonnet, 15-oct)

- **Títulos**: cap. 5 «From AP to EP: Trim Loss, Yield and the Test That Replaces the Chart» · cap. 6 «The Recipe Cost Card That Holds Up to an Audit». Hojas: "Yield Test", "Cooking Loss Test", "My Trim Loss Table", "Cost Card"; Q-factor, trim loss / cooking loss / waste, AP weight / EP weight, "Food Cost Kit Pro".
- **Conversiones**: 31.50 kg = 69.45 lb · 19.07 kg = 42.04 lb · lubina 1.2 kg = 2.65 lb ($6.76/lb; $13.08/lb limpio sin aprovechar = $28.84/kg; $12.53/lb aprovechando = $27.63/kg) · sobrecoste $12.73/kg = $5.77/lb · 180 g = 6.35 oz · ración de solomillo 0.22 kg = 0.49 lb = 7.76 oz → bruto 0.25 kg = 0.55 lb = 8.82 oz (mal calculado 8.69 oz). Precios/lb: 15.80→$7.17, 11.50→$5.22, 8.90→$4.04, 1.60→$0.73, 0.95→$0.43, 12.00→$5.44, 6.00→$2.72. Líquidos de la ficha (nata, PX, caldo, aceite) se quedan en L.
- **Ficha**: dinero de línea idéntico al ES; fila «IVA» = "Tax rate (%)" con 10% ilustrativo (el xlsx arranca en 0%, las filas "WITH tax" igualan al pre-tax); se dejan los precios/kg en una frase para lectores UK/AU (el gate exige las cifras).
- **Corregido**: el ES decía que el boniato tenía merma nula con bruto 0.22 kg; la tabla dice 18% (neto 0.18 → bruto 0.22): el EN lo explica como pelado en cocina.

## T04 (cap. 7-8, sonnet, 15-oct)

- **Títulos**: cap. 7 «Theoretical vs. Actual Food Cost: Where the Money Leaks» · cap. 8 «Prime Cost: The Metric That Measures the Health of the Business». Libro prime-cost-dashboard.xlsx: "Inputs" (antes «Parámetros», objetivos Full service 65.0% / Counter / self-service 55.0%) y "Monthly"; "Data", "Cost Card". Kit de personal → «Restaurant Staff Scheduling Kit Pro».
- **Cifras fijas**: año $1,232,200 ventas, compras $396,100, consumo $395,400 (food cost 32.1%, labor 31.3%, prime 63.4%, margen $451,142); labor con payroll taxes and benefits $385,658 = $277,600 brutos + $16,450 otros + 33% (parámetro del modelo, «replace it with your own»). Abril 62.7% mejor, agosto 69.9% «Above target». 180 g = 6.35 oz; 5 g = 0.18 oz.
- **Referencias**: CaixaBankLab/INE/Ministerio quitados («commonly cited»); única fuente nombrada: Toast, How to Calculate Prime Cost, 2026 (60% máx.; 60-65% full service, 55-60% QSR), que ya venía en el ES. Estructura 5-10% alquiler, 13-20% overhead, 10-13% resultado: «commonly cited», sin fuente.

## T05 (cap. 9-10, sonnet, 15-oct)

- **Títulos**: cap. 9 «Four Ways to Price a Dish» · cap. 10 «Pricing Psychology: What Is Proven and What Is Myth». Métodos: A · Cost Factor (food cost % markup / factor pricing) · B · Target Margin (contribution margin in dollars) · C · Market Price · D · Perceived Value. Columna Q de "By Dish"; semáforo «On target» / «Above target».
- **Cifras fijas**: chuletón = «dry-aged bone-in ribeye (17.64 oz)»: factor $49.33, margen $25.30, food cost 58.5%, carta actual $32.70; croquetas «Iberico ham croquettes (6 pcs)» $7.00 vs $8.60 actual; carta de 20 platos: 5 A / 6 B / 4 C / 5 D, 11 en objetivo y 9 por encima, 36.7%, margen medio $8.01; valor percibido total $307.04 vs elegido $266.90.
- **Impuesto**: última columna de la tabla 2 = «Chosen Menu Price With 10% Illustrative Sales Tax ($)» (cifras ES intactas, 10% ilustrativo como T02); US/CA el precio impreso es el pre-tax; UK/AU el incluido. Estudios citados (Wansink 2001, Yang-Kimes-Sessarego 2009, IHR/Emerald) intactos; CaixaBankLab/elBulli quitado («commonly cited» 30%, 25-35%).

## T06 (cap. 11-12, sonnet, 15-oct)

- **Títulos**: cap. 11 «Menu Engineering I: Kasavana & Smith Done Right» · cap. 12 «Menu Engineering II: What the Classic Matrix Can't See». Categorías EN: K&S **Star / Plowhorse / Puzzle / Dog** · Miller **Winner / Marginal / Loser** · Pavesic **Prime / Standard / Sleeper / Problem** · Goal Value **Above target / Below target** (hojas "Kasavana-Smith", "Miller", "Pavesic", "Goal Value", "Data"). Popularidad High/Low; familias Starters / Mains / Desserts; columna «Menu Mix in Category (MM%)».
- **Cifras fijas**: 4,870 uds/mes, CM medio ponderado $8.16 (Starters $7.46, Mains $10.80, Desserts $4.48); 6 Star 1,950 uds 40.0% $14,865 · 6 Plowhorse $16,198 · 5 Puzzle $6,357 · 3 Dog 350 uds $2,318; Winner 8 / 2,940 / 60.4% / 26.9% · Loser 5 / 40.7%; Prime 7 $21,408 · Problem 6 $7,830; Goal Value labor 32% + otros 10%, 9 por encima / 11 por debajo, food cost de carta 32.7%.
- **Platos** (reutilizar tal cual): Heirloom tomato salad with tuna belly and scallions · Garlic shrimp · Broken eggs with potatoes and chistorra sausage · Iberico pork tenderloin with sweet potato purée · Confit cod in pil-pil sauce · Dry-aged beef burger with fries · Creamy rice with Iberico pork secreto and mushrooms · Salt-baked sea bass · Seared bluefin tuna tataki with sesame · Creamy cheesecake · Caramelized torrija with ice cream · Chocolate lava cake · Prepared seasonal fruit (+ croquetas y chuletón de T05).

## T07 (cap. 13-14, sonnet, 15-oct)

- **Títulos**: cap. 13 «When the Methods Disagree: The Decision Protocol» · cap. 14 «Short Menus, Prix Fixe, Buffets and Banquets». Las 4 erres: **Reformulate / Reprice / Redesign / Remove** (+ Keep / Review en "Comparison"); hojas "Comparison" y "Prix Fixe Menu".
- **Prix fixe**: $13.18 pre-tax = $14.50 con 10% ilustrativo; coste medio $5.63 / A $5.93 / B $5.35; food cost 42.7 / 45.0 / 40.6%; margen $7.55 / $7.25 / $7.83 → $754.93 / $725.18 / $782.93 por 100 menús; fijo $0.55 (table bread, coffee, included drink); objetivo 30%. Cursos: First courses / Main courses / Desserts.
- **Discrepancia** (20 platos): 0 fuera = 3 (15.0%), 1 = 4, 2 = 1 (5.0%), 3 = 4, 4 = 8 (40.0%). Chuletón = «Dry-aged bone-in ribeye (17.64 oz)»; CM ponderado $8.16. El ES decía «3 + otros 3» con cero lecturas fuera: la tabla solo da 3, corregido.
- Fuentes: qamarero → «commonly cited 28-32%»; Cucinovo (28-40% hotel/buffet) se mantiene; LeBruto/Quain/Ashley 1995 intacto («Operators bank dollars, not percentages»).

## T09 (cap. 17-18, sonnet, 15-oct)

- **Títulos**: cap. 17 «Batch Costing for Commissary Kitchens and Pastry» · cap. 18 «When Your Supplier Raises Prices: The Re-Costing Protocol». Tabla de cocción (hoja "Cooking Loss Test") en lb: 0.55/0.44 · 3.31/2.38 · 0.44/0.40 · 0.66/0.49 · 2.20/1.52 lb; $/lb crudo→cocinado 8.14→10.44 · 2.45→3.40 (pollo) · 6.76→7.68 · 7.48→10.12 · 1.00→1.45. Técnicas: Flat-top / Oven / Confit / Charcoal. Fórmulas de obrador en gramos (2,000 g vs 1,000 g).
- **Decisiones del plan** ("Decisions"): Reformulate 1/$900 · Reprice 1/$210 · Redesign 2/$400 · Remove 3/$290 · Review 2/$300 · Negotiate 1/$260; total $2,360. Los «2 de negociación/$300» del ES se dicen «2 supplier review decisions, $300» (la hoja los pone en Review).
- Platos de "By Dish" nuevos: Local cheese board · Confit artichokes with ham · Roasted tomato soup with basil · Free-range roast chicken with potatoes · Seasonal vegetable lasagna. Columnas: Plate Cost ($) · Current/Chosen Menu Price Pre-Tax ($) · Status vs. Target (On target / Above target).
- Fuentes: CaixaBankLab → «a 2026 European industry study» (30-35% / 15-25%); INE y MAPA/Mercasa (y su cifra «34 productos») generalizados a «published price indexes» y «wholesale market quotes», sin nombrar fuente.

## T10 (cap. 19, sonnet, 15-oct)

- **Título**: «The Full Case: One Entire Menu, Start to Finish» (T01). Códigos de plato en "Decisions" pasan de E/P/D a **S/M/D** (S3 garlic shrimp, M5 ribeye, S5 cheese board, M8 lasagna, D4 fruit, M6 sea bass); el xlsx EN debe usarlos. Cabeceras: Dish · Family · Units Sold · Plate Cost ($) · Menu Price Pre-Tax ($) · CM ($) · Food Cost (%) · Menu Price With 10% Illustrative Sales Tax ($); hoja del simulador = "Menu".
- Herramientas de origen en "Decisions": Multi-method matrix · Multichannel simulator · Yield test · Beverage menu · Prime cost dashboard; estado «Pending»; impacto «Estimated Impact ($/Month)». KPI "Average check pre-tax ($)", "Contribution margin per cover ($)".
- El ES contradecía su tabla en la diferencia de -13,54 € ("pide subir más de lo que baja"): EN dice solo que, sumados los 20 platos, los precios elegidos quedan $13.54 por debajo de los actuales. Rangos 25-35% / 30% / estructura de costes / EBITDA 10-13%: «commonly cited», sin fuente.

## T11 (cap. 20 + cierre, sonnet, 15-oct)

- **Cierre**: encabezado «## About the Author and Terms of Use». Línea de versión (negrita): «**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide · info@aichef.pro**». Bio: «CEO of AI Chef Pro» (sin ChefBusiness Group), johnguerrero.es; aviso en cursiva: no tax, legal or accounting advice; tasas ilustrativas en celdas editables; "check with your accountant or tax advisor".
- Cap. 20: software $1,100/año por local «before sales tax»; hojas "90-Day Calendar" y "Decisions"; bloques Measure / Cost and Classify / Apply Decisions / Measure the Effect / Review.

## B01 (bonus: portada, índice y ej. 1-4, sonnet, 15-oct)

- **Títulos EN de los 12 ejercicios** (reutilizar tal cual): 1 Gross Quantity and Cost With Trim Loss · 2 Yield Test With Byproducts · 3 Actual Food Cost for a Month · 4 The Same Dish Through the Four Methods · 5 Tax on a Drink, Channel by Channel · 6 Classifying a Category With Kasavana & Smith · 7 The Same Group Under Miller and Pavesic · 8 Goal Value for Two Dishes · 9 Third-Party Delivery Repricing With Packaging and a Price Ceiling · 10 Glass or Bottle · 11 A Month's Prime Cost and Its Traffic Light · 12 Prix Fixe Menu: The Mix Decides the Margin. Subsecciones: «The Problem and the Data» / «The Solution, Step by Step» / «How to Read the Result»; «Familia» → category.
- Portada: bonus «Bonus of the "Food Cost + Menu Engineering Guide" Pack»; línea de versión D5 sin correo. Tablas del bonus con cabeceras Title Case y unidad en la celda cuando mezclan lb y L.
- Ej. 2 en lb/$ por lb (kg entre paréntesis en texto): sobrecoste $6.32/lb ($13.94/kg) sin aprovechar y $5.77/lb ($12.73/kg) aprovechando (el ES decía 12,73 «sin aprovechar»: erróneo). Compra lubina $17.88; ahorro gamba $0.65/lb ($1.43/kg).
