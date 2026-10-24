# BBQ Catering Business Plan Kit (EN) — SPEC DELTA (F1 · 24-oct-2026 · sesión Claude Code)

> Producto nuevo de la tienda EN (hoy 25 en `main`). **Mandan las SPEC heredadas** (`../business-plans-en/SPEC.md` D1-D29,
> `-2/` D30-D47, `-3/` D48-D65, `-4/` D66-D80, `-5/` D81-D95): aquí solo lo que cambia. Base: `F1-inventario-delta.md`
> (diccionario por celda = **Catering EN**; código = clon del **Mobile Bar**; fuente del circuito = FT ES; contenido ES =
> `plan-negocio-parrillero-asador-eventos` 2.2, cuyas cifras NO se reutilizan) y `F1-research-us-delta.md` (§1 concepto,
> §5 benchmarks, §6 legal, §8 caso, §9 jerga). Tamaño **M**: F1 ≈ 0,66 M (hecha) · F2 ≤ 1,5 M · F3 ≤ 0,6 M tokens. Lo que
> no está aquí ni en las SPEC heredadas no se hace. «decisión SPEC» = choque entre research e inventario resuelto aquí.

## 0. Regla de jerga (John, 13-oct) — manda sobre todo lo demás

El producto **no se traduce: se adapta** a cómo hablan los BBQ caterers, planners y clientes de EE. UU., en **tres capas**:
(1) producto (nombre, slug, ficheros, pestañas, rótulos), (2) contenido de los 4 entregables, (3) SEO de la landing. **Glosario
obligatorio = research §9** (36 términos + «(e) no se traducen literalmente»), entero en `BRIEF-TRADUCTORES.md`; la revisión
final comprueba las 3 capas contra él. Reglas fijas: «BBQ catering» en nombre, H1 y ficheros, «barbecue» solo como variante;
**«pitmaster»** para la persona (nunca «grill master»), «BBQ caterer» para el negocio, «smoked meats» para el producto;
**«commissary»** (nunca «support kitchen»); «live pit on site» = extra de pago, no la base; «part-time hourly W-2 staff»,
nunca «freelance»; «Cambro» es marca: fuera de rótulos («insulated food carriers / hot boxes»). Unidades US: lb, oz, °F,
millas y galones; kg, °C y litros solo entre paréntesis (`REGLA_UNIDADES`). Temperatura **de calidad** (brisket ≈ 203 °F) y
**mínimo seguro del Food Code** nunca en la misma columna ni en la misma frase sin decir cuál es cuál.

## 1. Producto (D96-D98)

| D | Tema | Decisión |
|---|---|---|
| D96 | Nombre y URLs | **BBQ Catering Business Plan Kit** · slug/productId `bbq-catering-business-plan` · JWT `bbq-catering-business-plan-jwt` · `/en/digital-products/bbq-catering-business-plan` (+ `/access`, `/library`) · gemelo ES (hreflang recíproco) `/plan-negocio-parrillero-asador-eventos` · env `VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN` |
| D96b | SEO de la landing | Title, H1 (Forma B: `BBQ Catering ` + oro `Business Plan` + «Template for an Off-Site Barbecue Caterer with a Smoker Trailer: …»), meta que **abre con «BBQ business plan»**, 6 H2, 9 FAQ del PAA en la redacción del comprador, 3 alt y keywords **tal cual research §9 «Términos para la landing»**. Un H2 solo se ajusta si choca con `PlanNegocioLandingPage` y conserva sus keywords. Las cifras de la FAQ («¿cuánto cuesta?», «¿es rentable?») salen de `cifras_caso.json`, no de esta SPEC |
| D97 | Precio, SIN anclas | **$39** pago único (D49: sin `priceOld`, «-x %», «Total value», «Save $» ni precio en bonos). Comparables: research §7 (FinancialModelsLab $109, Growthink $97) |
| D98 | Ficheros (`dl/bbq-catering-business-plan/`), **4** | `bbq-catering-business-plan.docx` «BBQ Catering Business Plan (10 Sections)» · `bbq-catering-financial-projections.xlsx` «BBQ Catering Financial Projections: 3-Year P&L, Cash Flow & Financing» · `bbq-catering-pricing-calculator.xlsx` «BBQ Catering Pricing Calculator (Pounds of Meat per Guest to Quote + Smoke Schedule & Shopping List)» · `bbq-catering-startup-checklist.xlsx` «BBQ Catering Startup Checklist (68 Tasks)». docProps D20 con las keywords del schema de research §9. **Sin 5.º fichero**: manual y carta ES entran en la calculadora (D106), las 10 experiencias en el docx §2 |

## 2. Concepto y caso (D99-D100)

| D | Tema | Decisión |
|---|---|---|
| D99 | Concepto | Research §1 tal cual: **full-service off-site BBQ caterer** que ahúma en el patio de la **commissary** (brisket, pulled pork, ribs, chicken, sausage), mantiene en caliente en insulated carriers / hot boxes y sirve en staffed buffet con carving station. **Smoker trailer al evento solo en bodas y premium** («live pit on site», extra de pago). Drop-off corporativo = segunda línea. **Live-fire premium** (Argentine asado, Santa Maria tri-tip, whole hog / La Caja China) ≈ 8 eventos, ≈ 11 % de ventas. 10 experiencias ES → **menu styles** (Texas · Carolina · Kansas City · Memphis · Santa Maria · Argentine asado · Brazilian churrasco · pig roast · fire show · corporate boxed lunch); 8 sistemas ES → equipo US de research §1. No es nuestro comprador: BBQ restaurant (Restaurant Kit), BBQ food truck (Food Truck Kit), quien vende desde casa (ilegal) |
| D100 | Caso US | Celdas de research §8 tal cual sobre el libro del catering: **B4 150 · B5 $38 · B6 75** (≈ $427,500), crecimiento 12/8 %, mezcla 88/12 (D103), coste 28/35 %, `B15` 3,5 %, marketplaces 6 % × 15 %, tarjeta 3 %, commissary y parking $1,800/mes, suministros $150, seguros $6,000, varios 3 %, propios $35,000, préstamo **CALIBRAR** con la regla D85 (≈ $98K, 10 %, 7 años: **SBA 7(a)**, no cabe en el Microloan de $50K), vidas 7/5, `B51` 220, rampa 0,50/8, 1 mes previo, imprevistos 10 %, cobro 7 días, alcohol 0 %, `B39` 8 % sobre toda la factura, estacionalidad con Month 1 = marzo, escenarios 113·$34.20·68 / 188·$41.80·83, personal y fijos de §8. **Cifras derivadas por el orden de D102 (decisión SPEC)**: contingencia = 10 % × (7+8+11+12+15) = **$4,500** (no $4,900) → CAPEX ≈ **$83,300**; D&A ≈ $10,500 (el rig deprecia a 5 años) → holgura ≈ 15 %, justa. **D15**: holgura ≥ 15 %; si no, `B4` de 10 en 10 hasta 170; si la caja mínima ≤ 0 por la rampa, `B35` 3 → 4 antes de tocar el precio; todo en `CALIBRACION_D15` y `F2-NOTAS`. **El docx dice la verdad**: 150 eventos = operador a tiempo completo con pit cook y $10K de marketing, no la media del primer año (≈ $300K el año 1); **el pesimista agota la caja (EBITDA ≈ −$40K) y lo dice** |

## 3. Libro financiero (D101-D104) — conjunto nuevo `bbq` sobre el catering

| D | Tema | Decisión |
|---|---|---|
| D101 | Código | Inventario §1 tal cual: código común **solo** con la rama `elif CONJUNTO == 'bbq'` de `business-plans-en/mapas.py` (copia de `:1218-1224` + mensaje de `:1226`). Lo demás en `business-plans-en-6/`, **clonado del mobile bar**: `mapas_bbq.py` (`_cargar_cat` = **diccionario por celda = EN publicado del catering**, los mismos 8 sha256 de `mapas_mbar.py:164-173`; `RX_REESCRIBIR` invertido de inventario §1; 41 `FORZAR_TRADUCTORES`; `reuso_de` deja pasar las 5 filas D19 útiles; 7 PARCHES del motor; `PRESTAMO_SEMILLA` = punto fijo del dry-run) · `datos_bbq.py` (estructura de `datos_mbar.py`, contenido de comida de `datos_cat.py`; `REGLA_UNIDADES` entera; fuera `GLOSA_DRY_HIRE`) · `bp6.py` · `fuente_bbq.py` (checklist ES importado de `parrillero-2_2/datos_checklist.py`; docx de `par_es_{a,b}.json`) · `barrido_bbq.py` · `calculadora_bbq.py` · `BRIEF-TRADUCTORES.md`. Grupos `GM` (331 tal cual) · `GRC-plan` (92, revisión) · `GBQ-plan` (121) · `GBQ-check` (272). Regresión: FT/CAF, REST/PAN, BAR, CAT **y MBAR** en verde |
| D102 | Inversión (filas 7-20) | **Orden del inventario §3** (solo se mueven filas; ninguna fórmula): 7 smoker trailer (offset / reverse-flow, 500-gal class, new) $20,000 · 8 su upfit (warming cabinet, hand sink + water tanks if your county requires, storage boxes, lights) $3,500 · 9 **live-fire rig** (Santa Maria grill, Argentine parrilla, asado crosses, La Caja China) $4,500 · 10 commissary storage fit-out (racks, meat lugs, vacuum sealer) $1,500 · 11 used cargo van $18,000 · 12 van upfit (shelving, racks, tie-downs, wrap) $3,000 · 13-20 = research §8 (LLC $1,500 · permits $2,500 · plan review / trailer inspection $500 · software $1,200 · smallwares & pit tools $3,500 · opening inventory $4,000 · launch & first bridal show $5,000 · holding & service equipment $6,500). Así `B31`/`B32`/`B23` casan con sus notas. Rótulos de base: A23 «Smoker trailer, van and fit-out contingency» · A31 «Smoker trailer, van and fit-outs (depreciated over the vehicle life)» · A44 «Useful life of the smoker trailer, van and fit-outs» · A55 «Contingency on the trailer, van and fit-out lines (%)». **Vehículo de arrastre = el del dueño, $0**, con nota (si no: pickup usada que remolque ≥ 3,000 lb, Kit estimate $25-40K) |
| D103 | Ventas, variables, fijos, personal | **Líneas de venta adoptadas**: A11 «BBQ packages (smoked meats, sides, bread & sauces, staffing)» 88 % · A12 «Add-ons (live pit on site, desserts, appetizers, non-alcoholic drinks, rentals, travel fees)» 12 % (decisión SPEC: el live pit va en add-ons), con `_F13/_F14_BBQ` (mecanismo `datos_mbar.py:1085-1087`). **Combustible de cocina = variable**: A15 «**Disposables, wood & cooking fuel**» 3,5 % (wood, charcoal, pellets y propane backup; escala con las libras y los eventos). **Combustible del vehículo = fijo** en A27 «Vehicle & trailer fuel, maintenance and registration» $6,000, como el mobile bar y research §8 (decisión SPEC; el catering lo tenía en varios): F18, C28, D18 e `Instructions!A49` se reescriben en coherencia (varios = imprevistos de cada evento: carne extra, hielo, parking en el venue; **sin combustible**). A24 «Utilities (water, power and phone not covered by the commissary)», **sin propano** (decisión SPEC). B16/B17 «Corporate catering marketplaces (e.g. ezCater)». A22 «Commissary kitchen rent & smoker trailer parking» (nota: ahumar en el patio de la commissary). Resto de fijos (A25, A26, A32-A35) e importes: inventario §3 + research §8 (= $30,300). **Personal** (4 puestos W-2, research §8): Owner / Pitmaster & Sales $26 · Pit cook / lead cook (W-2) $21 · Event staff (servers, buffet attendants, carvers; hourly W-2) 6 × 0.10 $18 · Prep cook / driver (part-time W-2) $17 → 2.85 FTE, $10,582/mes; `Staffing!B18` 10 h · `B19` 3,4 personas. Nota `Staffing`: W-2, no 1099; el pit cook vigila varias piezas a la vez. Nota `Cash Flow`: el depósito del 50 % no se modela y mejora la caja real |
| D104 | Umbrales, break-even y D19 | Umbrales `E51:E56` de research §5: margen bruto del motor ≥ 58 % · mercancía + desechables ≤ 35 % · personal ≤ 38 % · commissary ≤ 7 % · neto ≥ 5 % («kit benchmark (editable estimate)»). `Break-Even!B31/D31/E31` = **±$3 / +$6** por invitado. Tabla D19 «US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES», 14 filas: 5 del catering con propuesta (marketplace 15 %, depósito → 50 % nonrefundable, shared kitchen $15-45/h, seguros Insureon, neto 7-8 %) + 9 nuevas de research §5 (precio por paquete, carne por invitado, rendimiento ≈ 50 %, food cost, OEWS mayo 2025, smoker trailer $8,495-20,395, mínimos de invitados, leña por cocción). **Solo lo «leída» se cita con fuente**; lo «(resumen)» va como «Kit estimate» |

## 4. Calculadora (D105-D106) — `calculadora_bbq.py` sobre `calculadora_mbar.py` (VPS)

- **D105 «Pricing Calculator»**: esqueleto y autotest de `calculadora_mbar.py`, coste → precio de `calculadora_cat.py:47-108`,
  escalado de `calculadora_par_es.py:55-77, :242-257`. Entradas verdes con DV. **Paquete** de una lista de 3 (decisión SPEC: el
  libro tiene 5 tipos de evento, la calculadora cotiza 3): «Drop-off (delivered & set, disposable pans)» · «Full-service BBQ buffet
  (staffed, carving station)» · «Live-fire premium (Argentine asado / Santa Maria / whole hog)», más el interruptor **«Live pit
  on site (smoker trailer at the event)»** con fee fijo (por defecto $650, Owen's, leída). Más: invitados y guest minimum; **oz de
  carne cocinada por invitado por paquete = 6 / 8 / 8** (decisión SPEC: dentro de «one-third to one-half pound» de Hutchins y
  Owen's y de los 6-8 oz de sonnybryans, leídas; Dr. BBQ ¼-⅓ lb se cita como suelo); mezcla de carnes % (brisket / pulled pork /
  ribs / chicken / sausage, debe sumar 100 %); **$/lb crudo por corte en blanco, lo teclea el usuario** (sin precios 2026
  inventados; aviso si falta); sides, pan y salsas, desechables por invitado; lb de leña o carbón por lb cruda × $/lb; pitmasters
  y servers sugeridos (buffet 1 por 25-30 invitados, Kit estimate), horas de evento y de cocción nocturna, $/h y cargas %;
  alquileres, millas × $/milla, event / travel fee; margen objetivo, service charge %, sales tax % + «¿grava tu estado el service
  charge?» (`calculadora_cat.py:76-81`), depósito 50 % nonrefundable y tramos de cancelación (estructura ES sin huecos, días US).
  Salidas: lb crudas y cocinadas por corte, piezas (packers, butts, racks), leña, coste de carne, sides y personal, coste directo,
  **precio por invitado y su equivalente por lb cocinada**, subtotal, service charge, impuesto, total, depósito, saldo, retención
  por tramo y **margen calculado**. La gratuity voluntaria queda fuera (Rev. Rul. 2012-18). Nota de `C5` del libro: cómo pasar
  de los precios por paquete al B5 de mezcla ($38).
- **D106 pestañas nuevas**: **«Meat Yield & Smoke Schedule»** (13 cortes: packer brisket, pork butt, St. Louis ribs, baby back
  ribs, beef plate ribs, chicken thighs, chicken halves, turkey breast, sausage, tri-tip, picanha, tomahawk / bone-in ribeye,
  whole hog opcional; columnas: peso crudo por pieza, pit temp °F (°C), **temperatura de calidad** (Kit estimate), **mínimo del
  Food Code en columna aparte** (145 °F 15 s intacta · whole roasts 145 °F 4 min · **155 °F 17 s inyectada, ablandada o picada**,
  sausage incluida · 165 °F aves; 3-401.11), horas, reposo y hold, **rendimiento** (brisket y pork butt ≈ 50 %, fieryfoods,
  leída; pollo 65-70 %, sausage 85-90 % y el resto = «Kit estimate»), raciones por lb cruda y **«Start the pit by»** = hora de
  servicio − cocción − reposo − margen, por fórmula; notas de hot holding ≥ 135 °F, enfriado y recalentado 165 °F) ·
  **«Shopping List by Guest Count»** (invitados de la hoja principal + referencia 40/80/150/300 del T4 ES, todo por fórmula: lb
  crudas por corte, piezas, half pans o galones de sides, rolls, salsa, leña o carbón, butcher paper y foil, hotel pans, hot boxes,
  pitmasters y servers) · **«3 Example Quotes»** (corporate drop-off 40 inv. · graduation party staffed buffet 70 inv. · **wedding
  130 inv. full-service + live pit on site**, decisión SPEC: el inventario decía «wedding live-fire»; cada uno con los valores por
  defecto queda a **±10 % del precio de su línea en la mezcla** de research §8: $22 / $35 / $52) · «Instructions».
  **Autotest**: pycel = caché en las 4 pestañas de cálculo, más el paquete live-fire y el interruptor del live pit probados en la
  hoja principal, y la mezcla de carnes = 100 %.

## 5. Checklist (D107)

68 tareas **11/13/12/10/12/10** sobre la rejilla del FT, reuso por celda del catering **respetando las ranuras que
sobreviven** (inventario §5: **39 L · 21 A · 8 N**). Pestaña F2 **«Phase 2 - Pits, Fire & Permits»** (30 car.; decisión
SPEC: la research proponía «Smoker & Permits», pero el fuego es el bloque legal propio del BBQ); título «PHASE 2: COMMISSARY,
SMOKER TRAILER, FIRE RULES & PERMITS»; título del libro «BBQ CATERING STARTUP CHECKLIST — OFF-SITE BBQ CATERER». Columna C:
«Executive chef» → «Pitmaster» (≈ 20 filas). P6 **sin el calco «D-21 / D-14 / D-7 / D-1»** del catering publicado → «3 weeks
out / 2 weeks out / 1 week out / day before». Contenido: las 72 tareas ES adaptables (fuera las 11 solo-España y lo español
de las 5 parciales) + trámites US de research §6: commissary agreement por escrito (Food Code 3-201.11; nada de cocina de casa
ni cottage food para carne) · «ask your county» si ahumar en el evento convierte el trailer en mobile food unit (TX 25 TAC
§228.221; FL, NC) y, si no hay permiso, ahumar en la commissary · fire marshal (Class K + 2A:10BC, 10 ft, propano ≤ 200 lb,
burn bans: «check with your fire marshal») · plan HACCP con 145/155/165 °F, hot holding 135 °F, enfriado y recalentado · approved
source (USDA o inspección estatal; whole hog nunca custom exempt) · trailer en el DMV + commercial auto que lo cubra + inland
marine · COI / additional insured · ServSafe Manager y food handler cards · W-2, nunca 1099 · sales tax permit · contrato con
depósito 50 %, tramos de cancelación y fuerza mayor por burn ban (propane backup o nueva fecha) · pedido de carne 5-7 días y
rubs y porcionado en la commissary · yield real frente a la calculadora. Marketing: The Knot, WeddingWire, Zola, ezCater,
Thumbtack, Google Business Profile, bridal shows y tasting de lanzamiento.

## 6. Docx (D108)

Las 131 ranuras del FT ES; **61 a redactar** según inventario §6 (≈ 23 casi literales · 26 adaptadas · 12 nuevas), un run
por párrafo, **todas las cifras desde `cifras_caso.json`**, escritas (no traducidas) por redactores Sonnet con el párrafo ES
2.2 **de la misma ranura** (`par_es_{a,b}.json`) y research §1, §5, §6. Cada token apunta a su celda (decisión SPEC: en el ES
la ranura [98] usa `{DIAS_COBRO}` para los pagos a proveedores; aquí `B58 = B59 = 7` escondería el mismo error). §2 = los 10
menu styles; §6 = orden de compra del equipo US (T8 ES); §7 = 6 fases del evento con cocción nocturna y sonda; §8 = realismo
(D100). **§9 legal = el núcleo** (ranuras 102-108): sin cocina de casa (3-201.11(B); cottage food excluye carne, TX) ·
commissary agreement por escrito · trailer que cocina en el evento = mobile food unit según el condado («ask your county») ·
fuego (Class K, 10 ft, propano ≤ 200 lb, burn bans → fire marshal) · carne inyectada = non-intact, 155 °F · enfriado «to 70 °F
within 2 hours and to 41 °F within a total of 6 hours» (decisión SPEC de redacción: «4 h más» y «6 h» son la misma regla
3-501.14) · recalentado 165 °F · hot holding 135 °F · approved source USDA · seguros · ServSafe · W-2 vs 1099 · sales tax sobre
el catering · alcohol solo del cliente (liquor liability). Nota UK breve (registro 28 días antes, FHRS, 14 alérgenos, VAT 20 %,
council y plan de fuego). Lo no verificado por la research va como «check your county/state rules», nunca como cifra. Fijos:
portada «BBQ Catering», línea 9 «…to launch an off-site BBQ catering company in the United States», `PRODUCTOS_CIERRE` =
Catering Business Plan Kit · Food Truck Business Plan Kit · Food Cost Kit Pro · HACCP Food Safety Kit Pro. Fuera todo lo de
España (anexo CCAA sin ranura) y las erratas del ES (§9).

## 7. Gates (D109), cifras y vocabulario prohibidos (D110) y revisión (D111)

- **D109 Gates F2**: G1-G9 de BP · `RX_BBQ_NO` = 0 en los 4 ficheros · cifras prohibidas (D110) · autotest `Break-Even!B15` ·
  autotest de la calculadora (D106) · no latinos · `censo-entregables --letter --only bbq-catering-business-plan` (alta en
  `PRODUCTOS_LETTER` y en `EXCLUIDOS` de `postprocess-transversal.py` antes de G9) · `verificar` exige 272 celdas en GBQ-check ·
  regresión FT/CAF, REST/PAN, BAR, CAT, MBAR · sha256 del diccionario del catering sin cambios.
- **D110 Cifras** (`cifras_prohibidas()` como `datos_mbar.py:1126-1140`, con el filtro `propios` y `_importes_research`):
  importes ES de inventario §7 (31 de `cifras_caso_es.json` + 49.900 y 62.000; incluye 190.000, 65.400, 57.983) · **redondos ES
  (77.000, 84.000, 22.000) solo como frase con € o «EUR»**, no como importe (decisión SPEC: la research los veta, el inventario
  avisa de que chocan con importes US plausibles, p. ej. «≈ $84K» de CAPEX) · frases de inventario §7 («95 events», «80 guests»,
  «81 events», «76 events», «25 €», «31.8 %», «DSCR 1.51», «83 tasks»…) + «75-80 events» · casos EN ajenos (catering
  `cifras_caso.json` + `FRASES_CAT`; mobile bar 212,800 · 76,972 · 47,530 · 35,772 · 130,032 · 323,400, «160 events», «$14 per
  guest»; FT `_cifras_ft`). «$25 per guest» no se veta.
  **Vocabulario** = inventario §7: del FT (per day, operating days, customers salvo «corporate customers», **truck**, window,
  festival) · del catering (plated, chef-attended / themed / action stations, executive / sous chef y «chef» suelto, induction,
  taco bar, pasta, «12 cuisines», refrigerated van) · del mobile bar (cocktails, bartender, dry hire, mobile bar, bartending,
  barback, mixers, signature cocktails, specialty bar, cash bar) · del ES (España, IVA, autónomo, SL, IAE, fijo discontinuo, AESAN,
  APPCC, RD, CCAA, Veri*factu, FACe, parrillero, chuletón, lechazo, cochinillo, €, freelance, carné) · calcos «D-21» y similares.
  **Lista blanca**: chimichurri, Argentine asado, picanha, provoleta (en menú), commissary, food handler, smoker trailer, pickup,
  «BBQ food trucks» (no es nuestro comprador), **«carving station»**, **«cocktail hour»** (boda), «AI Chef Pro» y la firma, y
  **«chefs and head cooks»** solo en la fila OEWS de la D19 (decisión SPEC). VAT solo en la nota UK.
- **D111 Una revisión opus final**: (1) **las 3 capas de jerga contra el glosario §9**; (2) leer el checklist entero (272
  celdas escritas sobre ranuras del catering y del FT); (3) recalcular a mano ventas (150 × 75 × $38), CAPEX con la contingencia
  de la fórmula, equilibrio, holgura y DSCR; (4) abrir 3 fuentes legales (Food Code 2022, 25 TAC §228.221, boletín de Corpus
  Christi FD); (5) calculadora: calidad y mínimo seguro en columnas distintas, ejemplos dentro de ±10 %, ningún precio de carne
  tecleado; (6) que el docx no prometa nada que el Excel no haga. Tope de 2 rondas; los arreglos, por la vía de texto.

## 8. Landing y F3 (D112)

Ficha `astro-site/src/data/productos-en/planes/bbq-catering-business-plan.ts` duplicando la del catering
(`PlanNegocioLandingPage`, carrusel completo, sin anclas), SEO de D96b, 9 FAQ en la redacción del comprador (incluidas «Can I
sell BBQ from my home without a license?» y «Is this plan for a BBQ food truck or restaurant?»), `/access` y `/library` con su
island, dashboard y **los mismos registros que hoy citan `mobile-bar-business-plan`** (`grep -rl` en `astro-site/src` y `netlify`:
`tienda.ts`, `zona-app.ts`, `linkify-use-case.ts`, `sitemap-lastmod.json`, `get-download-urls.ts`, `verify-purchase.ts`,
`resend-access.ts`, `admin-generate-access.ts`, `payment-links.ts`, `product-prices.ts` $39, `footerLinks` de las fichas EN que
lo enlazan), las tres puertas cripto heredadas de la plantilla, `llms.txt`/`llms-full.txt` (25 → 26, o 27 si el PR #156 de Ice
Cream Shop entra antes), hub EN, hreflang en `plan-negocio-parrillero-asador-eventos.astro`, FAQ cruzadas desde Catering y Food
Truck EN («Is there a plan for a BBQ caterer?»). **Canibalización con el Catering Kit**: la landing diferencia por smoke,
pitmaster, smoker trailer y libras por invitado. **Imágenes**: reutilizar las del ES parrillero sin texto; si quedan menos de 4
útiles o ninguna enseña un smoker trailer, se generan 2 con `generate-images` (offset smoker trailer en una boda al aire libre ·
pitmaster cortando brisket en una carving station) más `og-bbq-catering-business-plan.jpg`; alt de research §9. Gates F3:
`gate-flujo-postpago --only bbq-catering-business-plan`, `tienda-gate`, `robots-gate`, `carrusel-apps-gate`. Cierre: sitemap +
GSC. **Payment Link: lo crea John.** Correo EN de lanzamiento: hueco **29-ene 14:00Z** (el 24-ene es de Ice Cream Shop;
borrador + routine el 30-dic, Resend no programa a > 30 días).

## 9. Riesgos, esfuerzo y deuda (D113)

| Paso (D113) | Quién | Tokens |
|---|---|---|
| Paso 1: rama `bbq` en `mapas.py`, `mapas_bbq.py`, `datos_bbq.py` (≈ 30 GX, caso, 68 pistas, 14 D19, 61 notas, cifras y vocabulario), `bp6`/`fuente`/`barrido`, **calculadora** (5 pestañas, 2 nuevas), dry-run y calibración D15 | 1 implementador **opus** (Mac + VPS) | ≈ 0,55 M |
| Tanda 1: GBQ-plan 121 + revisión GRC-plan 92 ‖ GBQ-check (≈ 29 filas que cambian + columna C) | 2 **sonnet** en paralelo | ≈ 0,25 M |
| Tanda 2: docx `bbq_a` ‖ `bbq_b` (61 ranuras, ≈ 4.300 palabras, con el ES alineado) | 2 **sonnet** en paralelo | ≈ 0,25 M |
| Gates + revisión D111 (una ronda; tope 2) | VPS + 1 **opus** | ≈ 0,3 M |
| **F2** | Mac redacta y orquesta; VPS genera, ensambla y pasa gates | **≤ 1,5 M** (F3 ≤ 0,6 M) |

**Riesgos**: (1) **legal y fuego**: MFU (TX sí, CA sin verificar), burn bans y carpas sin verificar → «ask your county / fire
marshal», nunca cifra; non-intact 155 °F y enfriado bien redactados (D108). (2) **Fuga de vocabulario y calcos**: chef, stations,
plated y van frigorífica del catering; «truck» del FT; «D-21» del P6; «Executive chef» en la columna C → `RX_BBQ_NO` + lectura
entera del checklist. (3) **Calculadora**: rendimientos sin fuente = «Kit estimate»; precios de carne en blanco; ejemplos dentro
de banda; el B5 de mezcla y los precios por paquete casan por la nota C5. (4) **Holgura justa** (≈ 15 % tras D102): si F2 da
menos, se aplica D15 sin discutir. (5) Altas en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9.
**Deuda ES anotada (no se toca aquí; pasa al calendario como erratas del parrillero ES 2.2)**: merma del brisket 35-40 % (manual
T3, ficha 08) frente a 40-50 % (manual §8, `REGLAS['merma']`) · «18 cortes» son 16 de carne y la «carta 12 cortes» son 10 ·
docx [98] con `{DIAS_COBRO}` en los pagos a proveedores. **Deuda del Catering EN**: su checklist publicado conserva el calco
«D-21 / D-14 / D-7 / D-1» en P6 (corregir en su próxima actualización ligera).
