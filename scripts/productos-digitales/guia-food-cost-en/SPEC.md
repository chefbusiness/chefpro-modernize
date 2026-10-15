# SPEC — Food Cost + Menu Engineering Guide (EN) · producto 14 de la tienda EN

> Sesión Claude Code, 15-oct-2026. Duplicado de la **Guía Food Cost + Ingeniería de Menú** (ES, 55 €, v1.0 sep-2026,
> `guia-food-cost-ingenieria-menu`) para la tienda EN. Tamaño **L** (≤ 10 M tokens, objetivo ≈ 5 M). Primera guía que
> pasa a inglés: además del producto, `GuiaLandingPage` gana `lang` (como `PlanNegocioLandingPage`).
> Inventario de F1 (anatomía ES + mecánica de los 13 EN): `F1-census.md` en esta carpeta.
> Reglas heredadas que no se repiten aquí: `TIENDA-INTERNACIONAL.md` §1 y §6, `recipe-costing-kit/SPEC.md` D5-D8,
> `business-plans-en/BRIEF-TRADUCTORES.md` §0, `GLOSARIO-JERGA-ES-EN.md`.

## 1. Decisiones

| # | Tema | Decisión |
|---|---|---|
| D1 | Nombre y URL | **«Food Cost + Menu Engineering Guide»** (ya publicado como «Coming soon» en el hub: no se cambia). Slug y productId EN `food-cost-menu-engineering-guide` → `/en/digital-products/food-cost-menu-engineering-guide` (+ `/access`, `/library`). Familia en `tienda.ts`: `guia-food-cost-ingenieria-menu` (es + en) |
| D2 | Precio | Propuesta **$59** (ES 55 €; planes 35-45 € → $39). Lo confirma John al crear el Payment Link (única decisión no delegada) |
| D3 | SEO (DataForSEO US, 15-oct) | Intención informativa «how-to» del dueño, con AI Overview en las tres SERP → cada sección abre con respuesta citable. Keywords: menu pricing 12.100 (picos) · how to calculate food cost 880 · food cost percentage 590 · menu engineering 480 · restaurant menu pricing 480 · plate cost 320 · prime cost restaurant 260 · menu engineering matrix 110. PAA para la FAQ: «What are the 7 menu pricing methods?», «How do I price out a menu?», «What is the 30/30/30 rule for restaurants?». **Sin canibalizar** el Food Cost Kit Pro EN (`food-cost-templates`, intención transaccional «calculator / templates»): enlaces recíprocos guía ↔ kit |
| D4 | Documentos | Se traducen los **dos `.md` ensamblados** del ES (no los `txt/`): `build/docs/guia-food-cost-ingenieria-menu/guia-food-cost-ingenieria-menu.md` (50.408 palabras, 20 capítulos) y `BONUS-ejercicios-resueltos.md` (13.293, 12 ejercicios). Render con `render_en.py` sobre `documentos.maquetar()` (mismo maquetado, A4 como los otros 13 EN y UK/AU). Único cambio en `documentos.py`: la etiqueta del pie «Página» pasa a constante de módulo (ES byte a byte igual). Salidas: `food-cost-menu-engineering-guide.docx/.pdf` y `BONUS-solved-exercises.docx/.pdf` en `astro-site/public/dl/food-cost-menu-engineering-guide/` |
| D5 | Portada | «**Recipe costing, menu pricing and menu profitability · US edition 2026**» (con notas UK, Canada y Australia). Línea de versión: «**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide**». Bonus: «**12 Solved Food Cost and Menu Engineering Exercises**» |
| D6 | Moneda y formato | **€ → $ 1:1, cifra intacta** (18,50 € → $18.50). Formato US: 1,234.56 · 30% · October 15, 2026. En los xlsx, sin símbolo (piloto D5) y fechas `mm/dd/yyyy`. Nunca «€», «EUR», «euros» |
| D7 | Impuestos (piloto D6 + hechos de la Equivalents Guide EN, `dl/en-shared/`, verificados oct-2026) | **US por defecto**: la carta va **sin impuestos** y el sales tax se suma al cobrar; el sales tax cobrado **no es venta**; el TPV da ventas brutas con impuesto y propinas → se quitan las dos antes de calcular cualquier %; el sales tax que pagas en suministros **es coste**. **UK**: IVA 20 % incluido en el precio impreso (neto = precio ÷ 1,20); la mayoría de la comida fría para llevar va al 0 % (no refrescos, dulces ni patatas fritas de bolsa); el IVA soportado se recupera si estás «VAT-registered». **Australia**: GST 10 % incluido (1/11 del precio). **Canadá**: GST 5 % o HST provincial, encima del precio, como en EE. UU.; «input tax credits» si estás registrado. Los tipos españoles **4/10/21 % desaparecen**. **No se añade ningún dato legal que no esté en la Equivalents Guide**. Capítulos que se **readaptan** (no solo se traducen): 3, 4, 15 y la parte fiscal del 16; bonus ejercicio 5. En los xlsx: mismas celdas y fórmulas, rótulo `Tax rate (%)` y **0 % por defecto** |
| D8 | Unidades (piloto D7) | Ejemplos en **US customary** con conversión **exacta** que deja intactas todas las cifras de dinero y %: g → oz (÷ 28.3495), kg → lb (× 2.20462), €/kg → $/lb (× 0.453592), ml → fl oz (÷ 29.5735) en raciones y copas; °C → °F. Dos decimales. **Se quedan en métrico**: botellas de vino y destilado (750 ml: el formato legal US es métrico) y las fórmulas de obrador/pastelería del cap. 17 en gramos (los pasteleros pesan en gramos; la compra, en lb: «50 lb bag»). Mismo criterio en texto y xlsx |
| D9 | Terminología (piloto D8 + glosario) | escandallo → recipe costing / **recipe cost card** · coste por ración → **plate cost** · merma → **trim loss** (yield % = 100% − trim loss %) · bruto/neto → **AP/EP** (as purchased / edible portion) · Q-factor · food cost % (UK: **GP %**) · prime cost · pour cost · menu mix · contribution margin · Kasavana & Smith, Miller, Pavesic, Goal Value (Hayes & Huffman) sin traducir · carta → **menu** · plato principal → **main / main course** (nunca «entrée» en el texto) · sala → **dine-in** · take away → **takeout** (UK takeaway) · delivery → **third-party delivery** (DoorDash, Uber Eats, Grubhub; UK Deliveroo, Just Eat) · albarán → **delivery invoice** · obrador → **bakery / commissary kitchen** · menú del día → **prix fixe lunch** (UK set menu) · cargas sociales → **employer payroll taxes and benefits** · TPV → **POS** · ticket medio → **average check** · cubierto → **cover** |
| D10 | Referencias españolas | Leyes, BOE, organismos, convenios y estadísticas de España (INE, Hostelería de España…) **no se traducen**: se generalizan («industry benchmarks put…») o se quitan. **Nunca se inventa una fuente US.** Lo que el traductor no sepa resolver lo marca `⟦ADAPT: motivo⟧` y lo resuelve la pasada Opus; el gate falla si queda una marca |
| D11 | Ficheros y pestañas | Mapa cerrado §2. En el texto EN, ficheros con su nombre EN (`recipe-cost-card.xlsx`) y pestañas entre **comillas dobles rectas** («the "Cost Card" sheet»). El fichero huérfano `plan-financiero-3-anos.xlsx` (1 cita) se cita como «the Restaurant Financial Plan Kit Pro» o se quita |
| D12 | xlsx | Traducción por celda sobre el xlsx ES generado (patrón `aplicar_en.py`), sin tocar fórmulas salvo referencias a pestañas renombradas; formatos D6; impuesto D7; unidades D8 en `recipe-cost-card`, `yield-and-trim-loss` y `beverage-cost-menu`. Gates: nº de fórmulas = ES, cero español, cero «€», valores derivados = ES (recalculo LibreOffice en el VPS) |
| D13 | Bonus comunes | La guía ES de equivalencias **no** se traduce: el EN lleva el bonus común `equivalents-guide` (`dl/en-shared/hospitality-equivalents-us-uk-canada-australia.docx`) como los otros 13 |
| D14 | Landing y app | `GuiaLandingPage.astro` gana `lang` (ES **byte a byte** igual: `tienda-gate.py --es-identico`); ficha EN en `productos-en/guias/food-cost-menu-engineering-guide.ts`; páginas landing/access/library bajo `pages/en/digital-products/`; dashboard EN gemelo; registro en las 5 fuentes + `admin-generate-access` con `lang:'en'`; `product-prices` en `usd`; `omitGlobalApp`; sin reseñas ni rating; `CryptoPayButton lang="en"` en las 3 puertas; FAQ con las PAA de D3 + «Does it work in the UK, Canada or Australia?». La tarjeta «Coming soon» del hub EN pasa a viva |
| D15 | Correo EN | Hueco EN **29-nov 14:00Z** (handoff 13-oct); borrador + routine como el Mobile Bar |

## 2. Mapa de ficheros y pestañas (cerrado)

| ES | EN | Pestañas EN (en orden) |
|---|---|---|
| ficha-escandallo-base.xlsx | **recipe-cost-card.xlsx** | Instructions · Cost Card · Invoice & Tax Check |
| rendimiento-mermas-producto.xlsx | **yield-and-trim-loss.xlsx** | Instructions · Yield Test · Cooking Loss Test · My Trim Loss Table |
| precio-objetivo-multi-metodo.xlsx | **menu-pricing-calculator.xlsx** | Instructions · By Dish |
| matriz-multimetodo-carta.xlsx | **menu-engineering-matrix.xlsx** | Instructions · Data · Kasavana-Smith · Miller · Pavesic · Goal Value · Comparison · Prix Fixe Menu |
| cuadro-de-mando-prime-cost.xlsx | **prime-cost-dashboard.xlsx** | Instructions · Inputs · Monthly |
| carta-de-bebidas-beverage-cost.xlsx | **beverage-cost-menu.xlsx** | Instructions · Inputs · Wines · Beer & Soft Drinks · Spirits & Cocktails · Beverage Summary |
| simulador-repricing-multicanal.xlsx | **multichannel-repricing-simulator.xlsx** | Instructions · Inputs · Menu · Summary |
| plan-accion-90-dias.xlsx | **90-day-action-plan.xlsx** | Instructions · Decisions · 90-Day Calendar · Tracking KPIs |
| guia-food-cost-ingenieria-menu.docx/.pdf | **food-cost-menu-engineering-guide.docx/.pdf** | — |
| BONUS-ejercicios-resueltos.docx/.pdf | **BONUS-solved-exercises.docx/.pdf** | — |

## 3. Plan por fases (gate + commit + push al cerrar cada una)

- **F1 (Mac)** — esta SPEC + `F1-census.md` + utillaje: `split_md.py` (trocea los dos `.md` en las tandas §4),
  `gate_md_en.py` (por tanda), `ensamblar_md.py` y `render_en.py`. Cierra con el gate corrido sobre una tanda de prueba.
- **F2** — (a) traducción de las tandas §4: Sonnet de 2 en 2, Opus en las tandas fiscales; (b) xlsx EN (Opus, VPS);
  (c) ensamblado + render + gates de documento (VPS); (d) revisión Opus única sobre los `.md` EN.
- **F3** — landing con `lang`, páginas, dashboard, registro, precio, gates LIVE, Payment Link de John, correo, llms.txt,
  sitemap, GSC, handoff.

## 4. Tandas de traducción (entrada `tandas/es/<T>.md` → salida `tandas/en/<T>.md`)

| Tanda | Contenido | Palabras | Modelo |
|---|---|---|---|
| T01 | portada + índice + cap. 1-2 | ≈ 5.200 | sonnet |
| T02 | cap. 3-4 (IVA → impuestos, D7) | ≈ 4.900 | **opus** |
| T03 | cap. 5-6 (unidades D8, filas de impuesto D7) | ≈ 5.600 | sonnet |
| T04 | cap. 7-8 | ≈ 4.600 | sonnet |
| T05 | cap. 9-10 | ≈ 4.650 | sonnet |
| T06 | cap. 11-12 | ≈ 5.300 | sonnet |
| T07 | cap. 13-14 | ≈ 4.800 | sonnet |
| T08 | cap. 15-16 (multicanal y bebidas, D7) | ≈ 5.550 | **opus** |
| T09 | cap. 17-18 | ≈ 4.700 | sonnet |
| T10 | cap. 19 | ≈ 4.300 | sonnet |
| T11 | cap. 20 + cierre de la guía | ≈ 2.100 | sonnet |
| B01 | bonus: portada + índice + ej. 1-4 | ≈ 4.650 | sonnet |
| B02 | bonus: ej. 5 (IVA de una bebida → impuestos, D7) + ej. 6-7 | ≈ 3.500 | **opus** |
| B03 | bonus: ej. 8-12 + cierre | ≈ 5.800 | sonnet |

## 5. Brief para cada traductor (el orquestador lo pega con la sección de su tanda)

**Lees** (y nada más): tu entrada `tandas/es/<T>.md`; esta SPEC (§1, §2 y §5); `business-plans-en/BRIEF-TRADUCTORES.md`
§0 («Idioma y tono», «Reglas duras», «Glosario»: lo que choque con esta SPEC, manda la SPEC); y, **solo en las tandas
fiscales**, el texto de la Equivalents Guide (`dl/en-shared/…docx`, se lee con `unzip -p … word/document.xml`).

**Escribes** `tandas/en/<T>.md`: el mismo Markdown, **estructura idéntica** (mismo nº y nivel de encabezados, mismas
tablas con las mismas filas y columnas, mismas listas, negritas y cursivas en su sitio). Encabezados en Title Case
inglés. Tú a tú («you»), inglés de EE. UU. natural de alguien que ha llevado cocinas, no traducción literal.

**Cifras**: todo importe y todo % se conserva (D6); solo cambian las magnitudes con unidad, por la regla exacta de D8,
y siempre igual en todo el capítulo. Si una tabla trae una columna en g o kg, conviértela entera.

**Fiscalidad** (tandas sonnet): «sin IVA» → «pre-tax» / «excl. tax»; una fila «IVA» de una ficha → «Tax rate (%)»
con la explicación de D7 en una frase. Si el párrafo depende del sistema español (tipos 4/10/21, recargo, modelo 303),
`⟦ADAPT: …⟧`. Tandas opus: readaptáis el contenido fiscal entero con D7 y solo con los hechos de la Equivalents Guide;
la lección de fondo se mantiene (el % siempre sobre el precio neto de impuesto; el impuesto recuperable fuera del coste).

**Validación** (Mac, ligera): `istats cpu temp | head -1` y
`python3 scripts/productos-digitales/guia-food-cost-en/gate_md_en.py --tanda <T>` hasta `OK` (las marcas `⟦ADAPT⟧`
son aviso en tu pasada y error en la final, `--final`). Responde solo con:
fichero escrito, resultado del gate, nº de marcas `⟦ADAPT⟧` y 3-5 decisiones que las demás tandas deban conocer.
Sin commits; no toques nada fuera de tu salida.
