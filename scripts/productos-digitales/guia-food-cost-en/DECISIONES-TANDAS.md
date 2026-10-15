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
