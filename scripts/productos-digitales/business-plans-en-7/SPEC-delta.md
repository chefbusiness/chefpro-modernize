# Paella Catering Business Plan Kit (EN) — SPEC DELTA (F1 · 24-oct-2026 · sesión Claude Code)

> Producto nuevo de la tienda EN, **hermano del BBQ Catering Business Plan Kit** (rama apilada sobre la suya). **Mandan las
> SPEC heredadas** (`../business-plans-en/SPEC.md` D1-D29, `-2/` D30-D47, `-3/` D48-D65, `-4/` D66-D80, `-5/` D81-D95,
> `-6/` D96-D113): aquí solo lo que cambia frente al BBQ. Base: `F1-inventario-delta.md` (= **inv. §n**: diccionario en
> cadena BBQ → catering, código = clon del `bbq`, contenido ES = `plan-negocio-paellero-eventos` 2.2, cuyas cifras NO se
> reutilizan) y `F1-research-us-delta.md` (= **research §n**). Tamaño **S**: F1 ≈ 0,5 M (research 0,25 + inventario y SPEC)
> · F2 ≤ 1,0 M · F3 ≤ 0,5 M. Lo que no está aquí ni en las SPEC heredadas no se hace. «decisión SPEC» = choque entre
> research, BBQ e inventario resuelto aquí.

## 0. Regla de jerga (John, 13-oct) — manda sobre todo lo demás

Tres capas (producto, contenido de los 4 entregables, SEO), **glosario obligatorio = research §9** (18 términos + «(e) no se
traducen literalmente»), entero en `BRIEF-TRADUCTORES.md`. Fijas: **«paella catering»** en nombre, H1 y ficheros; «Spanish
catering» como variante con tapas; **«paella chef»** para la persona y «paella caterer» para el negocio (nunca «paellero» ni
«chef» suelto); **«paella pan»** (nunca «paellera»), «paella burner (3-ring) with legs / stand»; «live paella», «cooked live
in front of your guests»; «live paella station» solo en prosa; «backyard paella party»; «commissary»; «part-time hourly W-2
staff»; «insulated food carriers» (no «Cambro»). Unidades US: lb, oz, °F, galones y cuartos para el caldo, **pulgadas para
las paelleras con cm entre paréntesis** («36 in (90 cm)»); **azafrán en gramos** (decisión SPEC: así se vende en EE. UU.; el
gate no veta «g»). El **mínimo del Food Code** se nombra siempre como tal. **Decisión SPEC (detector común de español,
`mapas.py:935`)**: sin tildes → «Serrano ham» (no jamón), «fideua (noodle paella)», «smoked paprika», «Spanish tortilla».

## 1. Producto (D114-D116)

| D | Tema | Decisión |
|---|---|---|
| D114 | Nombre y URLs | **Paella Catering Business Plan Kit** · slug/productId `paella-catering-business-plan` · JWT `paella-catering-business-plan-jwt` · `/en/digital-products/paella-catering-business-plan` (+ `/access`, `/library`) · gemelo ES (hreflang recíproco) `/plan-negocio-paellero-eventos` · env `VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN` |
| D114b | SEO de la landing | Title, H1 Forma B (`Paella Catering ` + oro `Business Plan` + «Template to Start a Live Paella & Spanish Catering Company: …»), meta, 6 H2, 9 FAQ, 3 alt y keywords **tal cual research §9 «Términos para la landing»** (captan «paella catering», «paella caterer», «spanish catering», «paella party»). Cifras de la FAQ desde `cifras_caso.json`. **Canibalización** con Catering y BBQ: la landing diferencia por paella cocinada en vivo, paelleras y quemadores, arroz por invitado |
| D115 | Precio, SIN anclas | **$39** pago único (D49) |
| D116 | Ficheros (`dl/paella-catering-business-plan/`), **4** | `paella-catering-business-plan.docx` «Paella Catering Business Plan (10 Sections)» · `paella-catering-financial-projections.xlsx` «Paella Catering Financial Projections: 3-Year P&L, Cash Flow & Financing» · `paella-catering-pricing-calculator.xlsx` «Paella Catering Pricing Calculator (Pans, Rice and Price per Guest to Quote)» · `paella-catering-startup-checklist.xlsx` «Paella Catering Startup Checklist (68 Tasks)». docProps D20 con las keywords de research §9. Sin 5.º fichero (inv. §2) |

## 2. Concepto y caso (D117-D118)

| D | Tema | Decisión |
|---|---|---|
| D117 | Concepto | Research §1 tal cual: **live paella caterer**: la paella cocinada en vivo en el evento **es el producto base** (paelleras de 26-36 in sobre quemadores de propano de 3 aros, con ensalada y pan); sofrito, caldo, verdura y marisco limpio salen de la **commissary**; **drop-off** = línea menor; **premium de marisco y tapas** ≈ 7 eventos. **8 menu styles** (inv. §2) y tipos de evento de las experiencias ES. Gas = base; leña solo con permiso; inducción en interiores (Kit). No es nuestro comprador: paella food truck (Food Truck Kit), restaurante, quien cocina en casa, fiestas populares |
| D118 | Caso US | Celdas de research §8 sobre el libro del catering: **B4 135 · B5 $40 · B6 58** (≈ $313,200; $2,320 por evento), crecimiento 10/6 %, mezcla 88/12, coste 28/35 %, `B15` 3,5 %, marketplaces 5 % × 15 %, tarjeta 3 %, commissary $1,100/mes, suministros $150, seguros $5,500, varios 3 %, propios $25,000, préstamo **CALIBRAR** con la regla D85 (≈ $62,400 al 10 % a 7 años: **SBA 7(a)**, no cabe en el Microloan de $50K), vidas 7/5, `B51` 200, rampa 0,50/8, 1 mes previo, imprevistos 10 %, cobro y pago 7 días, alcohol 0 %, `B39` 8 %, estacionalidad con Month 1 = marzo, escenarios **101 · $36.00 · 52 / 169 · $44.00 · 64**, personal y fijos de §8. **Derivadas por D120 (decisión SPEC)**: contingencia **$2,580** (no $2,620) → CAPEX ≈ **$49,480**; D&A ≈ **$5,700** (no $5,200). **D15** (regla de research): holgura ≥ 15 %; si no, `B4` de 5 en 5 hasta 150; si la caja mínima ≤ 0, `B35` 3 → 4 antes de tocar el precio; todo en `CALIBRACION_D15` y `F2-NOTAS`. **El docx dice la verdad**: 135 eventos = dueño-chef a tiempo completo con segundo cocinero los fines de semana, no el primer año medio (≈ $225K); los precios incluyen el paella chef que otros cobran aparte; **el pesimista agota la caja (EBITDA ≈ −$36K) y lo dice** |

## 3. Libro financiero (D119-D122) — conjunto nuevo `pael`

| D | Tema | Decisión |
|---|---|---|
| D119 | Código y diccionario | Código común **solo** con la rama `elif CONJUNTO == 'pael'` de `business-plans-en/mapas.py` (copia de `:1225-1231` + mensaje de `:1233`). En `business-plans-en-7/`, clonados del `bbq`: `mapas_pael.py`, `datos_pael.py`, `bp7.py`, `fuente_pael.py`, `barrido_pael.py`, `calculadora_pael.py`, `BRIEF-TRADUCTORES.md`. **Diccionario en cadena, POR CELDA**: propuesta = EN del BBQ en esa celda (`A_BBQ = {'PAEP': 'BBQP', 'PAEC': 'BBQC'}`; `textos_en/{GM,GRC-plan,GBQ-plan,GBQ-check}.json` + `GRC-plan.revision.json`; por ranura, `docx_en_bbq_{a,b}.json`); si no hay, el EN publicado del catering (los mismos 8 sha256). `SHA_BBQ` fija los 8 ficheros del BBQ: **16 sha256** en `verificar`. Grupos `GM` (≈ 312 tal cual) · `GRB-plan` (≈ 77, revisión) · `GPA-plan` (≈ 130: 51 forzadas + 23 con vocabulario BBQ + 56 D19) · `GPA-check` (275); `REVISAR_EN_TANDA = {'GPA-plan': ('GRB-plan',)}`. `RX_REESCRIBIR` = vocabulario y caso del BBQ + lo que sigue vetado del catering (inv. §1). `PARCHES_FORMULA` = los del BBQ sin cambios (Break-Even ±$3 / +$6). Regresión: FT/CAF, REST/PAN, BAR, CAT, MBAR **y BBQ** en verde |
| D120 | Inversión (filas 7-20) | **Huecos del BBQ (decisión SPEC: la numeración de research §8 metería la van en la base de equipo)**, solo se mueven filas: 7 paella burners & stands $2,500 · 8 paella pans (2 × 36 in, 3 × 32, 3 × 26) $1,800 · 9 propane & fire-safety kit $900 · 10 commissary prep & storage fit-out $1,500 · 11 used cargo van $18,000 · 12 van upfit (shelving, upright cylinder racks, tie-downs, wrap) $3,000 · 13 LLC $1,500 · 14 permits & certifications $2,000 · 15 fire/event permit & propane setup inspection (if required) $500 · 16 software $1,200 · 17 smallwares & paella tools $1,800 · 18 opening inventory $2,500 · 19 website, launch & bridal show $4,500 · 20 event setup & holding (canopy for the cooking station, tables, handwashing station, coolers, chafing dishes, insulated carriers) $3,000 = **$44,700**. Rótulos A23 / A31 / A44 / A55 de inv. §3 |
| D121 | Ventas, variables, fijos, personal | A11 «Paella packages (live-cooked paella, salad & bread, paella chef & staff)» 88 % · A12 «Add-ons (tapas, desserts, non-alcoholic sangria & drinks, rentals, extra hours, travel fees)» (`_F13/_F14` del BBQ con el nombre nuevo). **A15 «Disposables & cooking fuel» 3,5 %** (decisión SPEC: research decía «Disposables & propane»; la nota C15 dice que es el propano, y cubre la leña donde haya permiso). A24 utilities sin propano (= BBQ) · A22 «Commissary kitchen rent & equipment storage» (nota: ¿admite cilindros? pregúntalo) · A25 seguros: GL/BOP $1,700 que **no excluya la llama abierta** · auto $2,200 · workers' comp $1,100 · inland marine $500 · A27 «Van fuel, maintenance and registration» $5,000 (combustible del vehículo = fijo, como el BBQ) · A33 «Pan, burner & hose replacement» $1,000 · resto de fijos de research §8 ($25,100). **Personal** (4 puestos W-2): Owner / Paella Chef & Sales 1 × 1.0 $26 · Lead cook / second paella chef (part-time W-2) 1 × 0.4 $20 · Event staff (servers, buffet attendants; hourly W-2) 4 × 0.10 $18 · Prep cook / driver (part-time W-2) 1 × 0.3 $17 → 2.1 FTE, $8,026/mes; `Staffing!B18` 9 h · `B19` 2,5. Nota `Cash Flow`: el depósito no se modela y mejora la caja real |
| D122 | Umbrales y D19 | `E51:E56` = BBQ (58 / 35 / 38 / 7 / 5 %). Tabla D19 «US PAELLA CATERING BENCHMARKS (sourced) AND KIT ESTIMATES», 14 filas: **6 con propuesta del BBQ** (58 neto, 60 food cost, 62 marketplace Kit, 64 OEWS, 65 shared kitchen, 67 Insureon) + **8 nuevas** de research §5 (55 precio por persona en vivo $12-31 y langosta $45 · 56 menú español con personal $44-65 · 57 arroz por invitado · 59 invitados por paellera · 61 paelleras y quemadores · **63 paella chef y attendant cobrados aparte, cafesevilla** (decisión SPEC: la fila 63 del BBQ citaba operadores BBQ) · 66 mínimos 20-30 invitados y $500-1,600 · 68 propano y desechables por evento). **Solo lo «leída» se cita con fuente**; lo «(resumen)» (arroz, invitados por paellera, precios de tienda.com, propano EIA) va como «Kit estimate» |

## 4. Calculadora (D123-D124) — `calculadora_pael.py` sobre `calculadora_bbq.py` (VPS)

- **D123 «Pricing Calculator»**: esqueleto, cobro, cancelación (60 / 30 / 14 días; 50 / 75 / 90 / 100 %), service charge,
  sales tax + «¿grava el service charge?», margen calculado y autotest del BBQ. **Paquete** (3): «Drop-off paella (cooked at
  the commissary, delivered hot)» · «Live paella party (cooked on site, salad & bread)» · «Full-service live paella (paella
  chef & staff; weddings & corporate)». **Estilo** (lista de los 8 de la hoja 2) · interruptor **«Tapas hour?»** con coste
  por invitado (Kit $3-6; sustituye al «live pit on site», decisión SPEC) · invitados y guest minimum · **oz de arroz crudo
  por invitado 3,25** (Kit 3-3,5) · tamaño de paellera · salad & bread y desechables por invitado · propano (lb por
  paellera × $/lb) · paella chefs = paelleras ÷ 3 y ayudante desde 4 paelleras u 80 invitados (manual ES, Kit) · servers 1
  por 25 invitados en full-service (miamigrillcatering, leída) · depósito 50 % por defecto como «Kit estimate (US caterers
  ask 25-50 %)». **Ingredientes con $/lb en blanco** (el usuario los teclea); mientras falte alguno, coste por invitado del
  estilo = Kit de research §5 ($5 chicken & chorizo · $8.50 seafood · $16.50 lobster; los demás, Kit interpolado) con fila
  de estado, como el BBQ (F2-NOTAS §4.5). Salidas: paelleras por tamaño, personas, arroz (lb), caldo (gal), propano y
  cilindros de 20 lb, costes, precio por invitado, subtotal, service charge, impuesto, total, depósito, saldo, retenciones y
  margen calculado. Gratuity voluntaria fuera.
- **D124 pestañas nuevas**: **«Paella Yield & Pan Sizing»** (tamaños 18-40 in; invitados por paellera: 36 in = 40 · 32 = 30 ·
  26 = 18 de research y el resto de la tabla ES convertida, todo «Kit estimate»; arroz, caldo y aros por paellera; 8 estilos
  con oz por invitado de cada ingrediente; **mínimo del Food Code en su columna** (165 °F aves · 145 °F 15 s pescado y
  marisco · 155 °F 17 s chorizo crudo mexicano; el curado español es listo para comer); hot holding ≥ 135 °F o TPHC 4 h;
  alérgenos típicos con «verify with your recipe and suppliers»; notas de *B. cereus*, sobras a la basura, shellstock tags) ·
  **«Shopping List by Guest Count»** (tu evento + 40 / 80 / 150 / 300 editables, por fórmula: inv. §4) · **«3 Example
  Quotes»** (drop-off corporativo 30 inv. · backyard paella party 45 · **boda 110 con tapas hour y personal**; cada uno a
  **±10 %** de su línea de research §8: $22 / $34 / $52) · «Instructions». **Autotest**: pycel = caché en las 4 pestañas de
  cálculo + estilo, tapas y precios tecleados probados con `set_value`; ningún $/lb tecleado; ejemplos dentro de banda.

## 5. Checklist (D125)

68 tareas **11/13/12/10/12/10** sobre las ranuras del BBQ, propuesta = su EN en esa celda: **42 L · 23 A · 3 N** (inv. §5).
Pestaña F2 **«Phase 2 - Propane & Permits»** (27 car.; decisión SPEC: research frente a «Pits, Fire & Permits» del BBQ);
títulos de inv. §5; columna C «Pitmaster» → «Paella chef». Contenido US (research §6): commissary agreement por escrito ·
«ask your county» si cocinar el arroz en el evento cabe en su límite (limited food preparation, CA) · fire marshal:
estación de propano fuera de la carpa de invitados, cooking tents y cilindros según el fire code local («check with your fire
marshal»; los 20 ft de Virginia solo como ejemplo) · cilindros en la van, verticales y sujetos · plan HACCP con arroz TCS,
SOP escrito de TPHC 4 h, 165 / 145 / 155 °F y sobras a la basura · marisco de approved source y **shellstock tag log de 90
días** (3-203.12) · ServSafe Manager y food handler cards · W-2 · sales tax permit · contrato con deposit, tramos, plan B de
viento y lluvia y «fuego no autorizado» · sangría sin alcohol o con el vino del cliente, sin venderla; liquor liability solo
con alcohol del cliente. Marketing = BBQ (The Knot, WeddingWire, Zola, ezCater, Thumbtack, Google Business Profile, bridal
shows, tasting de lanzamiento) con fotos y vídeo de la paella en vivo.

## 6. Docx (D126)

Las 131 ranuras del FT ES; **61 a redactar** (inv. §6: 22 casi literales · 27 adaptadas · 12 nuevas), un run por párrafo,
cifras desde `cifras_caso.json`, escritas por redactores Sonnet sobre la **propuesta EN del BBQ de esa ranura** + el párrafo
ES 2.2 del paellero (`pae_es_{a,b}.json`) + research §1, §5, §6. [98]: `{{cobro_dias}}` y `{{pago_dias}}` (D113). §2 = los 8
menu styles y los tipos de evento; §6 = orden de compra (paelleras por tamaño, quemadores, kit de propano, carpa de la
estación, van, carriers); §7 = fases (la víspera en la commissary; el día, llegada 2-3 h antes, montaje, ≈ 1 h de cocción,
servicio y recogida; 1 persona por 25 invitados); §8 = realismo (D118). **§9 legal = el núcleo**: 102 commissary y nada de
casa (= BBQ) · 103 permisos, CFPM, food handlers, plan HACCP (arroz TCS y *B. cereus*, ≥ 135 °F o TPHC 4 h con SOP escrito,
165 / 145 / 155 °F, sobras fuera, approved source y shellstock tags) · 104 cocinar en el evento: *food establishment* incluye el
catering (1-201.10); limited food preparation de San Diego (CalRFC §113818) como ejemplo → «ask your county»; un festival
público es *temporary food establishment*, no el caso · 105 propano y carpas (Virginia 3107.12.5 / 3107.13.2 como ejemplo;
burn bans) → «check with your fire marshal» · 106 sales tax + service charge + sangría (sin licencia no se vende alcohol;
corkage no se modela) · 107 W-2 y seguros (GL sin exclusión de llama abierta) · 108 van en el DMV + nota UK (14 alérgenos con
moluscos, apio y sulfitos; council y recinto para el gas; registro 28 días antes; FHRS; VAT 20 %). Lo no verificado, como
«check your county/state rules». Fijos: portada «Paella Catering», línea 9 «…to launch a live paella catering company in the
United States», `PRODUCTOS_CIERRE` = los del BBQ. Fuera todo lo de España (anexo CCAA sin ranura) y la deuda ES (D131).

## 7. Gates (D127), cifras y vocabulario prohibidos (D128) y revisión (D129)

- **D127 Gates F2**: G1-G9 · `RX_PAEL_NO` = 0 en los 4 ficheros · cifras prohibidas · autotest `Break-Even!B15` · autotest de
  la calculadora · no latinos · `censo-entregables --letter --only paella-catering-business-plan` (alta en `PRODUCTOS_LETTER`
  y `EXCLUIDOS` antes de G9) · `verificar`: 272 celdas en GPA-check y 16 sha256 · regresión de los 6 conjuntos.
- **D128 Cifras**: importes ES ≥ 10.000 del paellero (27, inv. §7; 18.000 y 20.000 al filtro `propios`), los pequeños **solo con
  €**, frases ES (inv. §7 + research §8) · **caso BBQ** (`_cifras_caso('../business-plans-en-6/cifras_caso.json', 'bbq')` +
  «150 events», «$38 per guest», «75 guests», «220 events», «128 events») · catering, mobile bar y FT heredados.
  **Vocabulario** = `RX_BBQ_NO` heredado con tres cambios (**decisión SPEC**): «chef» permitido solo como «paella chef» /
  «second paella chef» (se vetan executive, sous y chef suelto; «chefs and head cooks» solo en la fila OEWS) · «Spain»
  permitido solo junto a origen (Valencia, bomba, saffron, imported) · «stations» solo «live paella station» y «Serrano ham
  carving station»; **más** el vocabulario BBQ y el ES paellero de inv. §7. Lista blanca: socarrat, sofrito, bomba rice,
  chorizo, aioli, tapas, patatas bravas, sangria, «paella food truck(s)» (no es nuestro comprador), commissary, food handler,
  «cocktail hour», «burn ban», AI Chef Pro y la firma. VAT solo en la nota UK.
- **D129 Una revisión opus final**: (1) las 3 capas de jerga contra research §9; (2) checklist entero (272 celdas sobre
  ranuras del BBQ); (3) recalcular a mano ventas (135 × 58 × $40), CAPEX con la contingencia de la fórmula, equilibrio,
  holgura y DSCR; (4) abrir 3 fuentes legales (Food Code 2022 3-501.19 y 3-203.12, PDF del caterer de San Diego County,
  13VAC5-52-360 de Virginia); (5) calculadora: mínimo del Food Code en su columna, ejemplos a ±10 %, ningún $/lb tecleado,
  alérgenos con el aviso; (6) **cero rastro BBQ** (smoker, pitmaster, meat, carving, pounds of meat) en los 4 ficheros; (7) que
  el docx no prometa nada que el Excel no haga. Tope de 2 rondas; los arreglos, por la vía de texto.

## 8. Landing y F3 (D130)

**Duplicar la F3 del BBQ** (commit `527c35eb`, 39 ficheros: `cp` y adaptar, sin plantilla nueva): ficha
`astro-site/src/data/productos-en/planes/paella-catering-business-plan.ts` desde la del BBQ, `/access` y `/library` con su
island, dashboard, registros (`tienda.ts`, `zona-app.ts`, `linkify-use-case.ts/.tsx`, `sitemap-lastmod.json`,
`get-download-urls.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`, `product-prices.ts` $39,
`products-catalog.ts`, `productos-digitales-config.ts`, changelog, `tienda-gate.py`, `footerLinks`), tres puertas cripto, `llms.txt`
/ `llms-full.txt` (+1), hub EN, hreflang en `plan-negocio-paellero-eventos.astro`, FAQ cruzadas desde Catering, BBQ y Food
Truck EN («Is there a plan for a paella caterer?»). **Imágenes**: las del ES paellero sin texto; si quedan menos de 4 útiles,
2 con `generate-images` (paella chef con una paella de marisco de 36 in en una boda al aire libre · paelleras y quemadores en
la van) + `og-paella-catering-business-plan.jpg`; alt de research §9. Gates F3: `gate-flujo-postpago --only
paella-catering-business-plan`, `tienda-gate`, `robots-gate`, `carrusel-apps-gate`. Cierre: sitemap + GSC. **Payment Link:
lo crea John.** Correo EN: hueco **3-feb 14:00Z** (29-ene = BBQ); borrador + routine el 4-ene (confirmar con `GET /broadcasts`).

## 9. Esfuerzo, riesgos, orden con el BBQ y deuda (D131-D132)

| Paso (D131) | Quién | Tokens |
|---|---|---|
| Paso 1: rama `pael`, 6 ficheros clonados, diccionario en cadena, ≈ 44 GX, caso, 68 pistas, 14 D19, 61 notas, calculadora (2 pestañas nuevas), dry-run y D15 | 1 implementador **opus** (Mac + VPS) | ≈ 0,35 M |
| Tanda 1: GPA-plan 130 + revisión GRB-plan 77 ‖ GPA-check (26 tareas + columna C) | 2 **sonnet** en paralelo | ≈ 0,2 M |
| Tanda 2: docx `pael_a` ‖ `pael_b` (61 ranuras, ≈ 7.500 pal., ≈ 1.800 nuevas) | 2 **sonnet** en paralelo | ≈ 0,2 M |
| Gates + revisión D129 (una ronda; tope 2) | VPS + 1 **opus** | ≈ 0,25 M |
| **F2** | Mac redacta y orquesta; VPS genera, ensambla y pasa gates | **≤ 1,0 M** (F3 ≤ 0,5 M) |

**D132 Orden con el BBQ**: PR apilado; el paso 1 empieza cuando la F2 del BBQ esté cerrada (D111 aplicada, gates verdes y
`docx_en_bbq_{a,b}.json` en git) y entonces se fija `SHA_BBQ`. Si el BBQ cambia después, `bp7.py verificar` avisa y se rehace
`preparar_tandas` antes de los redactores. El BBQ se mergea primero.
**Riesgos**: (1) **legal del evento**: arroz TCS, TPHC, limited food preparation (solo CA leída), propano y carpas (solo VA
leída), shellstock tags, alérgenos US frente a UK, GL y llama abierta → «check with your county / fire marshal», nunca cifra
nacional. (2) **Fuga BBQ y de caso**: las propuestas son texto BBQ con cifras suyas en las notas → `RX_PAEL_NO`, cifras BBQ,
D129 (6). (3) **Calculadora**: rendimientos todos «Kit estimate», ingredientes en blanco, estilo y paquete casan con el B5 de
mezcla por la nota C5. (4) **Holgura** (≈ 17 % en research, menos con D&A ≈ $5,700): D15 sin discutir. (5) Altas G9.
**Deuda ES anotada (no se toca aquí)**: «Paella valenciana DO» y «Paella vegetal DO» en carta, manual, calculadora y landing
(la DO ampara el arroz, no el plato). **Deuda BBQ heredable**: ninguna nueva; la fila 63 de su D19 no se reutiliza (D122).
