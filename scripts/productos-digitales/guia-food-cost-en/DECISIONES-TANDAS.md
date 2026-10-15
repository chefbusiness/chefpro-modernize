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
