# Revisión final adversarial — Food Cost + Menu Engineering Guide (EN)

> Sesión Claude Code, 15-oct-2026. Revisor único final (opus). Alcance: las 14 tandas `tandas/en/*.md`, los 8 xlsx EN
> (solo lectura, valores cacheados), la base fiscal (`dl/en-shared/…equivalents…docx`), SPEC, DECISIONES y ERRATAS-ES.
> Todas las líneas citadas son de `tandas/en/<T>.md` **después** de los arreglos. Gate `--todas --final`: 14/14 OK,
> 0 errores. `ensamblar_md.py` corrido al final (guía 45.036 palabras · 121 títulos · 42 tablas; bonus 11.978 · 51 · 12).
> Copia de las tandas antes de tocar nada: `scratchpad/rev/en.bak/`.

## Resumen

| Severidad | Nº | Arreglados en las tandas | Pendientes |
|---|---|---|---|
| Blocker | 0 | — | — |
| Important | 17 | 17 | 0 |
| Minor | 22 | 18 | 4 (sin acción o fuera de mi alcance, ver M19-M22) |

Comprobaciones de integridad (lente 6): los 8 xlsx abren con openpyxl; 4.358 fórmulas, **0 errores cacheados**
(#REF!/#VALUE!/#DIV/0!), **0 «€»/EUR** (los 3 avisos son la palabra «European»); toda celda de fórmula sin caché está en
una fila vacía de plantilla o devuelve `""` por diseño (Cost Card E45 a 0 %, My Trim Loss Table I con medida vacía,
líneas 4 de cóctel vacías, Data!43 «Prix fixe» sin platos). docx/pdf presentes y no triviales (66-295 KB); se re-maquetan
después. Muestreo texto ↔ xlsx: **>80 cifras** cotejadas en los 8 libros (ver §3).

## 1. Hallazgos

| id | sev. | fichero:línea | problema | arreglo |
|---|---|---|---|---|
| I1 | important | T02:27 | «a US mandatory service charge is revenue that you then pay out as wages»: sobregeneraliza (el dueño puede quedarse parte) | Reescrito con la base: no es propina; es ingreso del negocio y lo que se paga al personal se trata como salario; UK: se traslada íntegro como las propinas. Aplicado |
| I2 | important | T08:58, B02:11 | Razón falsa: «the simulator reads every price as including the rate in its cell». Las fórmulas del simulador (Menu!J/Q/X = precio × (1+tipo)) tratan TODO precio como **sin** impuesto; el tipo solo alimenta las columnas «Price incl. tax for the guest» | Regla 0 % mantenida con la razón verdadera: costes y márgenes van siempre sin impuesto; a 0 % esas columnas muestran el precio impreso US; teclear el sales tax las convierte en total de caja. Aplicado |
| I3 | important | T02:42, T02:62, T02:74 | «every price and margin … reads its rate» / «at 0% the simulator works on pre-tax prices»: el margen no lee el tipo | «every tax-inclusive price … (food cost and margins always run on pre-tax prices)»; notas de 0 % reescritas. Aplicado |
| I4 | important | B01:46 | Manda teclear el impuesto de COMPRA en la celda «Tax rate (%)», que es el impuesto del PRECIO DE CARTA (Cost Card E35); el de compra es la columna «Purchase tax rate (%)» (G) | Referencia corregida + aclaración de las dos celdas. Aplicado |
| I5 | important | T07:93 | UK/AU: «a tax-inclusive price of $14.50 … strip the tax out to get back to $13.18»: falso para UK (14.50 ÷ 1.20 = 12.08) y con «$» | AU 14.50 → 13.18 (GST 1/11); UK ÷ 1.20; sin símbolo. Aplicado |
| I6 | important | T07:103 | US: «a flat rate on everything served at the table, alcohol included»: afirmación fiscal no respaldada (calco del IVA español) | «applied, for the example, to the whole check». Aplicado |
| I7 | important | T08:100 | «alcohol can carry taxes of its own depending on your state»: fuera de la base | Suavizado a sales tax + meals tax + licencia (lo que dice la base). Aplicado |
| I8 | important | T05:83, T05:103 | **Errata heredada del ES**: $266.90 llamado «the prices you have actually chosen»; el xlsx (By Dish E49) lo rotula «Revenue at current menu prices». Los elegidos suman $253.36 (= 266.90 − 13.54, coherente con cap. 18-19; 36.7 % y $8.01 salen de 253.36) | «at today's menu prices $266.90 … chosen $253.36, $13.54 less». Aplicado |
| I9 | important | T09:17, T09:35 | **Heredada**: $8.01 y 36.7 % atribuidos a «the 6 dishes that use target margin»; son de los 20 platos a precio elegido (los 6 de método B dan $9.83 y 47.7 %) | Atribución corregida. Aplicado |
| I10 | important | T09:96, T09:123 | «2 supplier review decisions, $300»: en "Decisions" las 2 «Review» son platos (S3 gambas, M8 lasaña) de la matriz; la de proveedor es 1 «Negotiate» (pescado entero → filetes, $260) | «1 supplier negotiation decision … $260». Aplicado |
| I11 | important | T09:123, T01:46 | Dice que el Food Cost Kit Pro (y su bonus) «comes in the same pack» / «The pack comes in two pieces»: el Kit es otro producto (la ficha ES lo confirma); el comprador esperaría recibirlo | «sister product … sold separately». Aplicado |
| I12 | important | T03:173-178, B01:59-66 | Tabla de la ficha no cuadra con "Cost Card": mantequilla 0.0331 lb → 0.03 (texto 0.02), cebolla bruta 0.1002 → 0.10 (0.11), boniato bruto 0.4839 → 0.48 (0.49), AOVE 0.015 L → 0.02 (0.01) | Cifras corregidas en las dos tablas y en T03:130, B01:44, B01:50. Aplicado |
| I13 | important | T09:43-46 | Tabla "Cooking Loss Test": lomo cocinado 0.4299 → 0.43 (texto 0.44), bacalao 0.388 → 0.39 (0.40), secreto $10.1139 → $10.11 ($10.12) | Corregido. Aplicado |
| I14 | important | T03:35, T03:53 | Ahorro de las cabezas de gamba «$1.43» = cifra por **kg**; el xlsx (Yield Test O15) da $0.65 por lb | «$0.65 per clean pound ($1.43 per kg)», como B01. Aplicado |
| I15 | important | T03:65 | **Heredada**: «"My Trim Loss Table" has a last-measured date column»: esa columna no existe (ni en ES ni en EN) | Usar la columna "Note" para la fecha. Aplicado |
| I16 | important | B03:5-15 | Ej. 8 «Goal Value for Two Dishes» no resolvía nada y describía mal el objetivo (lo llamaba «food cost medio ponderado»); un comprador no podía reproducir 503.30/916.77/301.50 | Reescritos los 3 pasos con la fórmula real de la hoja (categoría: unidades medias 247.14, precio medio $10.77, FC 30.71 %) y dos entrantes resueltos (croquetas 916.77 arriba, gambas 301.50 abajo). Aplicado |
| I17 | important | T06:42, T06:57-159, T10:70-137, B03:11-88 | 19 comillas invertidas `` `fichero.xlsx` `` salían **literales** en el docx/pdf renderizado (el ES tiene 0) | Quitadas en las 14 tandas. Aplicado |
| M1 | minor | T01:22 | Índice: «the 55% one for the bar» (calco de «barra») — es el objetivo de mostrador/autoservicio | «for counter service». Aplicado |
| M2 | minor | T01:86 | «The terms we keep in English…»: calco evidente de traducción | Reescrito para un lector US. Aplicado |
| M3 | minor | T01:72, T01:138, T09:13, T09:23, T10:43, T10:64, B03:158 | «integrated service» (calco de «servicio integrado») | «full-service / full table service». Aplicado |
| M4 | minor | T01:58, T01:7 | «two and seven tenths of a point», «not an opening guide» | «2.7 points», «not a guide to opening a restaurant». Aplicado |
| M5 | minor | T01:70, T03:142, T04:26, T04:59, T09:37 | Contenido del Food Cost Kit Pro descrito con la lista ES (colectividades, delivery, tapas, «real time», ficha de obrador con «timing»): no cuadra con el Kit EN (13 plantillas + bonus; la de pastelería no tiene mano de obra) | Listas ajustadas al Kit EN real. Aplicado |
| M6 | minor | T01:48 | Platos españoles (torrija, chistorra…) sin contexto para el lector US | Una frase: menú de acento español, torrija = French toast española; la matemática vale igual. Aplicado |
| M7 | minor | T03:110 | «your P&L, which always works with amounts before tax»: contradice el cap. 3-4 (en US el sales tax de compras es coste) | Reescrito sin la afirmación. Aplicado |
| M8 | minor | T03:128, B01:42 | Precios por kg para UK/AU con «$» (decisión: UK/AU sin símbolo) y sin Canadá | Sin símbolo, + Canadá. Aplicado |
| M9 | minor | T04:36 | «A quarter of an ounce too much (about 0.18 oz)»: ¼ oz ≠ 0.18 oz | «An extra 0.18 oz (5 g)». Aplicado |
| M10 | minor | T04:51 | Manda sacar los 10 artículos de la hoja "Monthly", que solo tiene totales | Facturas de compra; "Monthly" da el total. Aplicado |
| M11 | minor | T04:96 | El 33 % de cargas sin pista para el comprador US | Añadidos los componentes de la base (Social Security, Medicare, FUTA/SUTA, workers' comp, benefits). Aplicado |
| M12 | minor | T04:127, T06:122, T06:128, T06:128/136, B02:92/94, B01:117, T05:91 | Calcos sueltos: «December's figure», «a stew against a fish dish», «push a dish from the floor», «till» (UK), «in qualitative terms», «net sales invoiced», «confirmed by the Cornell Chronicle» | Corregidos. Aplicado |
| M13 | minor | T05:38-128 | Nombres de plato distintos del xlsx en las dos tablas citadas de "By Dish" (Broken eggs with fries, Confit cod with pil-pil, Bluefin tuna tataki, torrija con glosa) | Nombres del xlsx. Aplicado |
| M14 | minor | T07:7 | Goal Value «boils those same two variables»: usa 4 (food cost, precio, popularidad, costes variables) | Corregido. Aplicado |
| M15 | minor | T08:104 | UK: «set that cell to 6 or 4.29»: "Glasses per bottle" es fórmula; lo editable es "Glass pour (ml)" | «set the "Glass pour (ml)" cell to 125 or 175». Aplicado |
| M16 | minor | T08:91 | Takeout deja más margen ($49,597) que sala ($43,635) sin explicación: parece un error del simulador | Nota bajo la tabla: cada canal cobra su precio necesario (tope techo); el de takeout incorpora el envase al 30 %. Aplicado |
| M17 | minor | T09:115, T09:152, T10:17, T10:33, T10:39, T10:53 | Contradicciones heredadas: «not the whole menu» y lista los 20; pie «empieza por la corrección mayor en $» contra el texto «empieza por las pequeñas»; 60.5 % atribuido a la ficha; cocción metida en el rendimiento | Reconciliados. Aplicado |
| M18 | minor | T10:103-120, T11:59, B01:19, B03:122, T11:77, B03:232, T11:13 | Etiquetas: «No: exclude or reformulate» (xlsx: «rework»), «Target Price» (xlsx: «Menu pricing calculator»); índice del bonus ej. 5 hablaba de «two tax treatments» (en US es el mismo); «no breakdown by type» y «inside that same band» (26 % está por encima de 18-24 %); aviso legal con «restaurant service versus a sale of goods» (concepto IVA España); «table above» | Corregidos. Aplicado |
| M19 | minor | T07:152/160, B03:212, T08:158, B03:131, T03:35/47, B01:94 | Redondeo de visualización: Excel enseña 3.40/3.07 (Prix Fixe E28/G28 = 3.395/3.065), 26.3 % (Wines P8 = 0.2625) y 5.16 (Yield Test E29 = 5.155); el texto (y el ES) dicen 3.39/3.06/26.2 %/5.15 | **Sin cambiar**: el gate exige las cifras del ES (j-cifras → ERROR). Propuesta: corregir ES y EN a la vez en la próxima mejora puntual, o envolver esas celdas en `ROUND(…,2)` en los dos xlsx |
| M20 | minor | B02:106-127 | Diagnósticos de la tabla Miller/Pavesic con redacción algo distinta de "Comparison" (p. ej. «cut the cost» vs «lower the cost») | Sin cambiar: la tabla no cita la hoja; no confunde |
| M21 | minor | recipe-cost-card.xlsx "Cost Card"!E45 | «Tax on this card's ingredients» sale en blanco a 0 % (`=IF(COUNTIF(J10:J29,">0")=0,"",SUM(…))`) | xlsx no tocado. Propuesta: `=SUM($J$10:$J$29)` para que muestre 0.00 |
| M22 | minor | ERRATAS-ES.md | Erratas heredadas del ES halladas ahora (no está en mi alcance editar ese fichero) | Añadir: cap. 10 «266,90 € = precios elegidos» (son los actuales; elegidos 253,36 €) · cap. 17 «8,01 €/36,7 % de los 6 platos de margen» (son de los 20) · cap. 6 «columna de fecha» en Mi Tabla de Mermas (no existe) · cap. 18 pie de tabla contradice el texto · bonus ej. 8 sin resolver y objetivo mal descrito · cap. 13 Goal Value «dos variables» · cap. 7 manda sacar los 10 artículos de la hoja «Mensual», que solo tiene totales · cap. 19 rendimiento 60,5 % atribuido a la ficha |

## 2. Lente fiscal y legal (la de más peso)

- Todo lo que queda está en la base (Equivalents Guide EN, oct-2026): sales tax estatal + condado + ciudad, meals tax
  «check»; UK 20 %/5 %/0 %, comida fría para llevar a tipo cero salvo refrescos, dulces y crisps, VAT Notices 709/1 y
  701/14; Canadá GST 5 %/HST/PST/QST, ITCs; Australia GST 10 % incluido, 1/11, GST credits; propinas fuera de ventas;
  service charge (I1); sales tax en compras = coste en US, «resale rules vary by state»; alcohol = licencia local;
  US standard drink 5 fl oz vino / 1.5 fl oz destilado; UK 25/35 ml y 125/175 ml.
- Ejemplo de 10 % ilustrativo coherente en cap. 3, 4, 6, 10, 14, 19 y bonus 1, 5, 12 (siempre «illustrative»; los xlsx a
  0 %). Regla 0 % del simulador coherente en cap. 3, 15 y bonus 5 con la razón real de las fórmulas (I2-I3). Bonus 9 no
  toca impuestos.
- Comisiones de plataforma: solo como «working examples», sin nombre de app asociado a una tarifa; la tabla del texto
  coincide con "Inputs" A24:B27 del simulador.
- Nóminas: 33 % presentado como parámetro del modelo (ahora con los componentes US de la base, M11).

## 3. Cifras re-derivadas y cotejo texto ↔ xlsx (muestra)

Recalculadas a mano y contra caché: ejemplo conductor 5.6704/17.30 → 32.78 %, 11.63, 18.90, 9.26 %, 19.03, 29.8 %,
20.76 → 27.3 % / GP 72.7 %, 0.56 → 6.23 → 36.0 %; factura 768.40 (7 líneas) y el 8 % ilustrativo (6.08 / 82.08 / 774.48);
conversiones D8 (0.22 kg = 0.485 lb = 7.76 oz → 8.82 oz; 8.69 oz mal; lubina 6.7585 $/lb, 13.081, 12.532, 5.77/6.32;
17.64 oz; 30 L = 7.93 gal; 8.45/16.91/11.16 fl oz; zumo 0.64 $/lb y 1.81 raciones/lb); croquetas 24.4 %/46.5 %/$10.00/
$11.60; Summary 31.4/38.2/54.6 %, 16/12/12, 43,635/49,597/30,050/−13,585; bebidas 43,657/11,503.96/26.4 %/32,153.04/
41.6/35.6 %, 646.38 = 28.60 + 525.32 + 92.46, highballs 21.6 %, cócteles 19.7 %, 8 vinos (márgenes y %); prime cost
12 meses (usos, 32.1/31.3/63.4 %, 385,658 = 277,600 × 1.33 + 16,450, 451,142, abril 62.7, agosto 69.9); matriz 4,870/
59,029/32.7 %/8.16, familias 7.46/10.80/4.48, umbrales 10.0/7.8/17.5 %, K&S 1,950/14,865·16,198·6,357·2,318, Miller 8/7/5
y 26.9/32.0/40.7 %, Pavesic 21,408/6,508/3,992/7,830, Goal Value 20 filas y 503.30/543.03/436.37, Comparison 3/4/1/4/8;
precios 5/6/4/5, 11/9, 36.7 %, 8.01, 307.04, 266.90, −13.54, −5.1 %, 49.33/25.30/58.5 %; prix fixe 13.18/14.50, 5.63/
5.93/5.35, 42.7/45.0/40.6 %, 754.93/725.18/782.93; plan 90 días 2,360/28,320, 26 hitos (4/4/8/8/2), 5 decisiones de la
matriz = $760, 2 del simulador = $230, KPIs 33.1→29.8, 66.8→63.8, 27.40→29.10, 18.10→20.20.

## 4. Veredicto

**Listo para la venta tras el re-maquetado** (`render_en.py` sobre los `en/*.md` ya re-ensamblados). No queda ningún
blocker ni important abierto; los 4 minor pendientes (M19-M22) no confunden al comprador y no exigen tocar los xlsx.
