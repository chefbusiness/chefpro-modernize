# Pizza Shop Business Plan Kit (EN, $39): revisión adversarial final (D150)

> Sesión Claude Code, 25-oct-2026. Una sola pasada, de solo lectura: volcados `dump-en/` (4 entregables), ficha `.ts`, dashboard,
> `verify-purchase.ts`, correo, hub EN, SPEC-delta, F1-research-us-delta, F2-NOTAS y `cifras_caso.json`. No se ha aplicado nada.
> Una sola cita abierta, porque había dudas: **americas.pizzanapoletana.org/en/gas_burning_oven** (leída el 25-oct). La AVPN Americas
> **certifica hornos de cúpula de gas donde la leña está prohibida y se documenta** (ordenanza municipal o norma de edificación).
> Excluye los hornos eléctricos, de carbón y mixtos leña/gas, y cobra $2,500 + $300 + $400 al año.

**Recuento: 4 B · 6 M · 23 m.**

## 0. Lo que se ha recalculado y está bien (no tocar)

| Comprobación | Resultado |
|---|---|
| Ventas | 62 × $36 × 300 = **$669,600**; A2 $709,776 y A3 $738,167 (+6 % / +4 % de covers) ✓ |
| Rampa y estacionalidad (Mes 1 = septiembre) | Pesos sep→ago .084/.088/.084/**.096 dic**/**.068 ene**/.072/.082/.086/.09/.09/.088/.072 = 1.000; rampa .75/.833/.917/1; SUMPRODUCT .9573; mes 1 = 6.58 % del año; el año suma lo mismo que el P&L (O7) ✓ |
| CAPEX y necesidad | 18 partidas **$217,300** + fianza $8,000 + 2 meses de renta previa $8,000 + imprevistos **$9,250** (10 % de B7-B11 = $92,500) = **$242,550**; fondo de maniobra 3 × ($372,829 − $25,932) / 12 = $86,724; necesidad **$329,274**; fuentes $330,000 (+$726) ✓ |
| Préstamo y DSCR | 200,000 × 0.10 / (1 − 1.1^−10) = **$32,549**; DSCR del año 1 = (52,367 − 13,092 + 25,932 + 20,000) / 32,549 = **2.62×**; el cuadro cierra a 0 ✓ |
| Equilibrio y holgura | 372,829 / (36 − 13.14) / 300 = 54.4 → **55**; de caja 359,446 / 22.86 / 300 = 52.4 → **53**; holgura **18.3 %** ✓ |
| Márgenes | Neto **5.9 %** → 9.0 % (año 3); EBITDA $98,299 (14.7 %); prime cost 58.8 %; personal 32.8 % ✓ |
| Personal | $/h: 22.50 · 18 · 19 · 15.50 · 15 · 15.58 (todos ≥ $15); 4.725 FTE; cobertura 99 % ✓ |
| Calculadora | Margherita $2.91 / $18 = **16.2 %**; bola **$0.40** ($24.15 / 60); Bufalina 23.1 %; 8 «On target»; 250 g = 8.82 oz ✓. No hay tiempos de fermentación y la calculadora no los promete (Word [78] lo dice bien) |
| Caja y sales tax | Saldo mínimo **$92,610** en el mes 1; sales tax de $53,568, remitido en los meses 4, 7 y 10 ✓ |
| Coherencia de cifras | Word, landing, correo, emailBody y dashboard = Excel. La landing no lleva DSCR, préstamo ni saldos (solo el objetivo de 1.25×). No aparece «€» ni «authentic», y de las cifras ES solo queda el 10 % de B4 |
| Normativa citada bien | 3-501.19 (4 h / 6 h, 41 °F y 70 °F) · 2-102.12 · 41 °F y 135 °F · 8-201.11 · 9 alérgenos con sésamo desde el 1-ene-2023 · 21 CFR 101.91 < 20 ppm · tip credit de $2.13 / $5.12 y los 7 estados · I-9 en 3 días · FLSA 40 h · HO de amasadoras para menores de 18 · NOL al 80 % · SBA Microloan $50K · tarifas AVPN · Oregon 15-01 con su salvedad · NFPA 96 cap. 14 con salvedad de edición en el Word y la landing ✓ |

## 1. B: bloqueantes (antes del LIVE)

| # | Fichero · lugar | Texto actual | Arreglo literal | Dónde se arregla |
|---|---|---|---|---|
| B1 | Hub EN `DigitalProductsHubPage.astro` **l. 626-641** | Sigue la tarjeta vieja `name: 'Business Plan: Neapolitan Pizzeria'` (mismo `slug: '/plan-negocio-pizzeria'`), con «…and the Equivalents Guide for Latin America», junto a la nueva de l. 72-87. `git diff main` = +20/−0: no se borró, aunque el comentario de l. 69 dice «Sustituye a la tarjeta vieja». Las dos se resuelven contra la misma familia: el hub EN enseña **dos tarjetas** del mismo producto y una describe el kit español | Borrar el objeto entero de l. 626-641 (de `{` a `},`) | La ficha del hub (como se hizo con la Paella) |
| B2 | Checklist: no existe **ninguna tarea para pedir la beer & wine license**. Solo aparece como cláusula del contrato (F2 `E8`), en el seguro (F1 `E15`) y en el patio (F2 `E13`). Tampoco hay ninguna lista de los extintores Class K / 2-A (ver M6) | Lo prometen la landing l. 93 («the checklist walks you through the application»), la tarjeta del hub l. 80 («80 tasks: … beer and wine license») y el Word [116] («the beer and wine license application goes in as soon as you do»). SPEC D146 la pedía (3-12 meses: es el camino crítico) | Sin añadir filas, reescribiendo `Phase 2!B11/E11`. **B11**: «Zoning approval, business license and beer and wine license application». **E11**: «A restaurant usually needs a city or county business license, a state sales tax permit and, depending on the zoning, a conditional use approval. File the beer and wine license with your state alcohol beverage control (ABC) board and your city or county as soon as the lease is signed: it often takes 3 to 12 months. In a non-quota state the plan budgets about $3,000 inside the project line; quota states cost far more. Ask in the pre-application meeting which approvals apply to you and in what order.» | `textos_en/GPIZ-check.json` **c0682** (B11) y **c0684** (E11) |
| B3 | Word **[81]** (§6, alternativa eléctrica) | «In exchange you cannot use the protected pizza name, and you may still need a hood and exhaust for the fumes.» Es un resto de la ETG española que contradice [50] y [107] y el argumento de venta de la landing: en EE. UU. el nombre no está protegido | «In exchange you give up the VPN certification (the AVPN does not accept electric ovens), although you can still call your pizza Neapolitan-style, and you may still need a hood and exhaust for the fumes.» | `docx_en_piz_b.json` índice **81** |
| B4 | Checklist `Phase 5!E10` y `Phase 6!E13` | «Set a ceiling: in this plan, 10% of sales.» · «if the marketplace passes 10% of sales». Es la **cifra del caso ES** (plataforma 10 %, prohibida en D149) y contradice el Excel (`B16` 12 %) y el Word [54]/[74]/[89]/[113] (12 %) | «Set a ceiling: in this plan, 12% of sales.» · «if the marketplace passes 12% of sales (the plan's ceiling)» | `GPIZ-check.json` **c0804** y **c0851**. Hueco del gate: añadir `10 ?% of sales` a `FRASES_ES` en `datos_piz.cifras_prohibidas()` (no choca con usos legítimos: renta «≤ 10%», cargas 10 %, interés 10 %) |

## 2. M: mayores

| # | Fichero · lugar | Texto actual | Arreglo literal | Dónde se arregla |
|---|---|---|---|---|
| M1 | **VPN y gas** en 7 sitios: Word [50] y [79], Excel `Startup Costs!D12`, `Instructions!D39` y `D40`, landing l. 73, checklist `Phase 1!E6` | [50] «Gas or electric ovens do not qualify.» · [79] «be aware that gas and electric ovens do not meet the rules for VPN certification» · D12 «A gas or electric oven is a variant and does not qualify for VPN certification» · D39 «gas or electric is a variant and does not qualify for VPN» · D40 «needs an open location and a wood-fired dome oven» · landing «Only a wood-burning dome oven can qualify for the VPN certification» · E6 «Only wood fire can follow the Neapolitan tradition…». Es **falso para el gas** (página AVPN leída hoy; research §6.9) y el Word [107] y la FAQ de l. 77 ya lo dicen bien («gas only where wood is banned»): el producto se contradice | [50] «Electric, coal and wood/gas combination ovens do not qualify; a gas-fired dome oven is accepted only where wood burning is forbidden and you can document it (a city ordinance or a building rule).» · [79] «…but be aware that an electric oven never qualifies for VPN certification, and a gas oven only where wood burning is forbidden and documented.» · D12 «…A gas or electric oven is a variant: an electric oven never qualifies for VPN certification, and a gas oven only where wood burning is forbidden and documented» · D39 «Wood-fired dome oven; gas only where wood is banned (documented); electric does not qualify for VPN» · D40 «…needs an open location and a wood-fired dome oven (gas only where wood is banned)» · landing «For VPN certification, the AVPN wants a wood-burning dome oven (gas only where wood is banned, never electric): see the next question.» · E6 «…For VPN certification the AVPN wants a wood-fired dome oven (gas only where wood is banned and documented; never electric).» | `docx_en_piz_a.json` **50** · `docx_en_piz_b.json` **79** · `GPIZ-plan.json` **c0156**, **c0452**, **c0456** · ficha `.ts` l. 73 · `GPIZ-check.json` **c0628** |
| M2 | Excel `12-Month Cash Flow!O20` | «The model settles quarterly (April, July, October, January)». El libro liquida en los **meses 4, 7 y 10** (diciembre, marzo y junio), como dice `A34` | «The model settles quarterly, in the month after each plan quarter (Months 4, 7 and 10: December, March and June with Month 1 in September; the fourth quarter is remitted in Month 13): if your state requires monthly filing, expect smaller payments every month instead» | `textos_en/GM.json` **c0531** (o POR_CELDA `12-Month Cash Flow!O20` en `datos_piz.py`). Viene de GM: comprobar si el Bar EN arrastra lo mismo |
| M3 | Excel `Staffing!J20` junto a `B20` = **46** | «50 weeks: 52 minus about two weeks of vacation, holidays and average absences…». La nota contradice la celda, que es la que calcula las horas contratadas y la cobertura del 99 % | «46 weeks: 52 minus about six weeks for vacation, holidays, the January closure and average absences. There is no federal vacation requirement in the US: adjust it to your own policy» (el valor no se toca: con 50 la cobertura sube sin cambiar el coste) | `GM.json` **c0387** (o POR_CELDA `Staffing!J20`). Viene de GM: comprobar el Bar EN |
| M4 | Dashboard `PizzaShopBusinessPlanDashboard.tsx` l. 49 (`calculadora-masa`) | «Dough by the batch from your hydration, salt, yeast and **fermentation hours**…». La calculadora no tiene horas de fermentación | «Dough by the batch from the number and weight of your dough balls, per liter of water (traditional Neapolitan ratios) or in baker's percentages, in grams with ounces and pounds beside them, with the dough cost per ball, plus the food cost, margin and menu price of 8 example pizzas. Replace the example ingredient prices with your distributor's.» | Dashboard l. 49 |
| M5 | Landing l. 121 (FAQ UK/CA/AU) | «The calculator works in grams and ounces, degrees Fahrenheit with Celsius, and square feet with square meters.» La calculadora no tiene °F ni sq ft | «The plan and the checklist give US units with metric beside them (°F with °C, sq ft with sq m, lb with kg), and the dough calculator works in grams with ounces and pounds beside them.» | Ficha `.ts` l. 121 |
| M6 | Landing l. 219 (tarjeta «Startup Checklist») | «kitchen, oven and health (grease interceptor, gas contractor, **Class K and 2-A extinguishers**, …)». Ninguna de las 80 tareas lo menciona, y el interceptor y el gas son de la Fase 2 | Mejor ponerlo en el checklist (lo pedía D146), al final de `Phase 3!E7`: «… Keep the extinguishers your fire marshal specifies within reach of the oven (for solid fuel, usually a 2-A water-type or a Class K wet-chemical unit) and a Class K extinguisher by the fryer.» En la landing, mover «grease interceptor, gas contractor» al grupo «site, hood and permits». Si no se toca el checklist: borrar «Class K and 2-A extinguishers» de la landing | `GPIZ-check.json` **c0721** + ficha `.ts` l. 219 |

## 3. m: menores

| # | Lugar | Actual → propuesta | Fuente |
|---|---|---|---|
| m1 | Excel `C6` vs Word [39], [71] y [82] y checklist `Phase 6!B16` | En enero, «a week» en el Excel y «two weeks» en el resto → c0010: «…July 4) and **two weeks** in January for oven maintenance and vacation, rounded to 300» (365 − 52 − 4 − 12 = 297). En [82], «closes on Mondays, on Christmas Day and for two weeks» → «closes on Mondays, on the main holidays (Thanksgiving, Christmas, New Year's Day and July 4) and for two weeks in January» | `GPIZ-plan` c0010 · `piz_b` 82 |
| m2 | Checklist `Phase 3!E7` y Word [79] | Maderas «Oak, beech, ash or olive» y «(oak, ash, maple or olive)» (olivo y haya son de España) → «Oak, ash, maple, hickory or fruitwood» / «(oak, ash, maple or fruitwood)», como `F31` | `GPIZ-check` c0721 · `piz_b` 79 |
| m3 | Word [39] | «on a neighborhood street with foot traffic or next to a plaza» → «on a neighborhood street with foot traffic» | `piz_a` 39 |
| m4 | Checklist `Phase 2!E5` | «kitchen of about 320 sq ft» → «about 325 sq ft» (= `0. Assumptions!C24`) | `GPIZ-check` c0664 |
| m5 | Checklist `Phase 5!E9` y Word [112] | La comisión se suma al food cost y aparece el rango «25-35%»; la calculadora (A49) dice que sale del precio y el Excel da 22-28 %. E9: «…with mozzarella di bufala, burrata or imported cured meats a pizza can run at 22-28% food cost (the Bufalina comes out at about 23% in the calculator), and on marketplace orders the commission comes out of the price on top. Use the kit's dough and food cost calculator.» [112]: «…your best seller can run far above the plan's food cost, and on marketplace orders the commission comes out of the price on top.» | `GPIZ-check` c0802 · `piz_b` 112 |
| m6 | Word [95] | «{{bebida_pct}} beer and wine» → «{{bebida_pct}} beverages (beer, wine, soft drinks and coffee)» (= [49] y `A11`) | `piz_b` 95 |
| m7 | Word [40] | «PMQ's 2026 Pizza Power Report quotes 2-3% for lean independents» → «PMQ's 2026 Pizza Power Report quotes an independent operator at 2-3%» (es la cita de un operador, como en [94]) | `piz_a` 40 |
| m8 | Word [106] | «In a state without a quota, the license is about $3,000» → «In a state without a quota, the case budgets about $3,000 for the license» (estimación del kit, no tarifa leída) | `piz_b` 106 |
| m9 | Word [104] | «Mozzarella, fior di latte, cured meats and cut tomatoes are TCS foods» → «Fior di latte and other fresh mozzarella, cooked ham, raw sausage and cut tomatoes are TCS foods (some dry-cured meats are not: check the label)» | `piz_b` 104 |
| m10 | Checklist `Phase 3!E16` | «…and get health department approval (Food Code 3-501.19)» → «…and keep it on site for the health inspector (Food Code 3-501.19; some jurisdictions also ask you to submit it for approval)» | `GPIZ-check` c0746 |
| m11 | Checklist `Phase 2!E13` | «Using the public sidewalk or right-of-way is always permitted separately.» → «Using the public sidewalk or right-of-way usually needs its own permit.» | `GPIZ-check` c0691 |
| m12 | Excel `0. Assumptions!C4` | «about 10 a day at about $52 … divided by the average check» da 14.4 con $36, no «about 15» → «about $54 excl. sales tax» (10 × 54 / 36 = 15) | `GPIZ-plan` c0006 |
| m13 | Excel `Instructions!B38` | «1 quart (1 liter) of water» (1 qt = 0.95 L) → «1 liter (about 1 quart) of water» | `GPIZ-plan` c0446 |
| m14 | Excel `C20` y `C27` | El workers' comp está a la vez en las cargas del 10 % y en el seguro de $7,500 → C27: «General liability, liquor liability (beer & wine) and property coverage that names the open-flame oven (workers' comp is in the payroll tax rate above)…» | `GPIZ-plan` c0048 |
| m15 | Landing l. 65 | «Less than the SERP suggests.» → «Less than most online articles suggest.» | ficha `.ts` |
| m16 | Landing l. 73 | Frase encadenada «…and some makers publish none, and a gas or electric oven…» → «…and some makers publish none. A gas or electric oven is a legitimate variant…» | ficha `.ts` |
| m17 | Landing l. 81 | «plus 10% for delivery and card processing» → «plus 10% for delivery and a card processing fee (3.05% + $0.30)» (research §5.3) | ficha `.ts` |
| m18 | Landing l. 97 | «…about $0.40 per dough ball, in the example and editable.» → «…about $0.40 per dough ball (editable).» | ficha `.ts` |
| m19 | Word [93] | «how you recover or deduct it depends on your state» choca con «no input credit» del Excel → «Sales tax you pay on purchases is part of the cost (the workbook recovers none); exemptions such as resale certificates depend on your state, so confirm them with your accountant.» | `piz_b` 93 |
| m20 | Word [39], [85] y [94] | Caso «single-owner LLC» con un impuesto del 25 % de C corp. En [94], tras «…effective income tax rate of 25%.», añadir: «The example applies it as if the business paid corporate income tax (an LLC can elect it); as a pass-through, set the rate to 0 on "0. Assumptions" and budget your personal tax.» | `piz_b` 94 |
| m21 | Checklist `Phase 5!B7/E7` | «Offer to-go boxes for what guests do not finish, at no charge, and say so on the menu.» es un resto de la Ley 1/2025 española, sin base en EE. UU. → «If you offer to-go boxes for leftovers, decide whether you charge for them and keep them in stock; check your local packaging rules.» | `GPIZ-check` c0798 |
| m22 | Word [78] | «about 60-65% hydration» frente a 55-62 % tradicional y 60 % de ejemplo en la calculadora → «about 58-65% hydration (the traditional ratios in the calculator sit at 55-62%)» | `piz_b` 78 |
| m23 | Checklist `Phase 1!E6` y `Phase 2!E10` | «NFPA 96 chapter 14» sin la salvedad de edición que sí llevan el Word y la landing → añadir «(chapter 14 in recent editions: ask which edition your fire marshal enforces)» | `GPIZ-check` c0628 · c0681 |

## 4. Notas

- B2, M6 y m1-m23 se arreglan solo por texto: ni filas, ni DV, ni fórmulas. Tras aplicarlos hay que volver a pasar
  `check_textos --todas` → `aplicar_en` → `ensamblar_docx` → gates G1-G9 + barrido + 2.ª pasada canónica (F2-NOTAS §7).
  `cifras_caso.json` no cambia, porque ningún arreglo toca un valor.
- c0531 y c0387 vienen de **GM** (texto del Bar EN en la misma celda): conviene comprobar si el Bar EN publicado tiene el mismo
  desajuste de meses y semanas. Queda fuera de este producto.
- El correo, el `emailBody` y los nombres de venta cruzada (Pizza Shop Checklists Kit Pro, Food Cost Kit Pro, HACCP Food Safety
  Kit Pro, Restaurant Business Plan Kit, más los 11 `footerLinks`) están bien: todas las rutas `/en/digital-products/*` existen.

## 5. Aplicado (ronda única de arreglos, sesión Claude Code, 25-oct-2026)

Todo en la fuente: `textos_en/GPIZ-{plan,check}.json` por id, `docx_en_piz_{a,b}.json` por índice, `textos_en/GM.revision.json`
(nuevo), `datos_piz.py`, la ficha `.ts`, el dashboard y el hub. Ni filas, ni DV, ni fórmulas, ni valores: `cifras_caso.json`
igual salvo `generado`. La calculadora no se toca (sha256 igual).

| # | Estado | Cómo |
|---|---|---|
| B1 | ✅ | Hub EN: borrada la tarjeta vieja «Business Plan: Neapolitan Pizzeria» (16 líneas). Queda 1 sola (la EN, posición 1, «New»). `grep "slug: '/plan-negocio-pizzeria'"`: 1 por hub en ES/DE/FR/IT/NL/PT/EN |
| B2 | ✅ | c0682 / c0684 con el texto literal. 80 tareas y reparto 12/15/14/13/13/13 sin cambios (G1) |
| B3 | ✅ | `piz_b` 81 literal |
| B4 | ✅ | c0804 y c0851 literales + regla `(?i)\b10 ?% of sales\b` en `datos_piz._frases_es()` (probada: caza «10% of sales», no la renta «≤ 10%» ni las cargas «of 10%: 32.8% of sales») |
| M1 | ✅ | Los 7 sitios con el texto literal: `piz_a` 50, `piz_b` 79, c0156, c0452, c0456, c0628 y la landing l. 73. Barrido de coherencia: el resto de menciones (c0046, c0249, c0480, c0656, c0795/796, c0859-861, Word [57], [107], FAQ l. 77) ya casaban |
| M2 | ✅ | c0531 en `textos_en/GM.revision.json` (mecanismo de las reutilizadas: `preparar_tandas` lo aplica encima en cada pasada y `check_textos` comprueba que está aplicado). No se edita GM.json a mano ni se usa POR_CELDA (obligaría a re-extraer `textos_es.json`) |
| M3 | ✅ | c0387 en `GM.revision.json`, texto literal (B20 = 46 no se toca) |
| M4 | ✅ | Dashboard l. 49 literal |
| M5 | ✅ | Ficha l. 121 literal |
| M6 | ✅ | Extintores al final de c0721 (Phase 3!E7) con el texto literal. Landing l. 219: «grease interceptor, gas contractor» pasa a «site, hood and permits» y en «kitchen, oven and health» entra «dry firewood storage» (tarea Phase 3 B7). El checklist no nombraba el interceptor en ninguna tarea: se añade «plumbing with the grease interceptor» al plan review (c0681, Phase 2!E10) para que la landing diga verdad |
| m1 | ✅ | c0010 y `piz_b` 82 (el Word [39] ya decía «two weeks») |
| m2 | ✅ | c0721 y `piz_b` 79 |
| m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m15, m16, m17, m18, m19, m20, m21, m22 | ✅ | Literales (m5: c0802 y `piz_b` 112; m20: solo `piz_b` 94) |
| m13 | ✅ con variante | «1.06 quarts (1 liter) of water…» en vez de «1 liter (about 1 quart)»: `REGLA_UNIDADES`/`RX_PIZ_NO` solo admite la métrica entre paréntesis y lo habría dado rojo; 1 L = 1.06 qt, el ratio sigue siendo por litro |
| m14 | ✅ ampliado | c0048 literal + `piz_b` 106, que repetía el workers' comp dentro del seguro: «…liquor liability and property coverage that accounts for open flame; workers' compensation is budgeted in the payroll taxes» |
| m23 | ✅ | c0628 «NFPA 96 (chapter 14 in recent editions: ask which edition your fire marshal enforces)» y c0681 «(NFPA 96; chapter 14 in recent editions: …)» |

**No aplicado**: nada; ninguno era opinable hasta el punto de dejarlo fuera.

**Deuda (no se arregla hoy)**: el Bar EN **no** tiene el desajuste de semanas (Staffing!B20 = 50 y la nota dice 50; lo mismo en
FT, cafetería, panadería, restaurante, catering, mobile bar, BBQ y paella). La nota de O20 «settles quarterly (April, July,
October, January)» está en los 8 planes EN anteriores, cuyo Mes 1 es «opening» y no un mes del calendario: solo es exacta si se
abre en enero. Arreglo de una línea por conjunto (`GM.revision.json` o POR_CELDA) cuando toque actualizar cada uno.

`tandas/GPIZ-{plan,check}.entrada.json` cambian solo en la línea de CLAVES `"—": "☐"`: `preparar_tandas` refleja ya el arreglo
de G4 de `mapas_piz.instalar` (las entradas no las lee la construcción).

**Gates (VPS, sin `PIZ_FUENTE_ES`)**: `check_textos --todas` 6/6 OK, 0 errores · `mapas` + `verificar` 0 errores (7 avisos de
siempre) · `aplicar_en --idempotencia` préstamo $200,000 en 1 vuelta, faltan 0, 0 diferencias, 0 fallos de pycel · calibración
D15 VERDE (holgura 18.3 %, DSCR 2.62, saldo $92,610, cobertura 99.1 %, neto 5.9/7.8/9.0 %) · `ensamblar_docx` G8 VERDE (131
párrafos, 7,470 palabras) · `gates_en` G1-G9 **TODO VERDE** (G1 741 fórmulas + 80 tareas, G2 1,304 piezas, G3 16 hojas, G4 235
valores bajo DV, G5 8 rangos, G6 0 diferencias, G7 110 valores) · `gates_en --autotest` 20/20 · `ensamblar_docx --autotest` 8/8
· barrido 1,644 piezas, 0 fallos · `resumen_entregables` 3,385 piezas, 0/0/0 · `censo-entregables --fail --letter --only` 4
ficheros, 0 defectos · `gate-no-latinos --only` 0 · regresión de los 7 conjuntos **27/27 IGUAL**, rc 0 · 2.ª pasada (aplicar +
docx) **IGUAL** en los 4 (canónico) y `cifras_caso.json` igual salvo `generado`. Mac: `esbuild` OK (ficha, dashboard,
frontmatter del hub), `sync-product-prices --check` OK, `tienda-gate` VERDE, HTML del correo bien formado (no se toca).

| Entregable (`astro-site/public/dl/pizza-shop-business-plan/`) | sha256 nuevo (Mac = VPS) |
|---|---|
| `pizza-shop-business-plan.docx` | `6eef3b58667319968236fa317305c1ba81ba64b062eff7c7dc224ec214c21206` |
| `pizza-shop-financial-projections.xlsx` | `d5dd1400badd6975f7a3ec26227af879326d9e6416aa7a1b38e39ee706d256c7` |
| `pizza-shop-startup-checklist.xlsx` | `7a25b1e23bce687b6061e8f53194bd189aca267f7eaeb98efeed676b21914728` |
| `pizza-dough-food-cost-calculator.xlsx` | `435361dcf57a9625625788ec10b236b3b330951b97dd6d4250496412e5ef537f` (sin cambios) |
| `cifras_caso.json` · `entregables_piz.json` | `901173f7…` · `6f1f286e…` |
