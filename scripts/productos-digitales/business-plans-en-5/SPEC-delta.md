# Mobile Bar Business Plan Kit (EN) — SPEC DELTA (F1 · 13-oct-2026 · sesión Claude Code)

> Producto 13 de la tienda EN. **Mandan las SPEC heredadas** (`../business-plans-en/SPEC.md` D1-D29, `-2/` D30-D47,
> `-3/` D48-D65, `-4/` D66-D80): aquí solo lo que cambia. Base: `F1-inventario-delta.md` (gemelo y diccionario = **Catering
> EN**; fuente del circuito = FT ES; fuente de contenido = `plan-negocio-cocteleria-eventos`, cuyas cifras y fórmulas NO se
> reutilizan) y `F1-research-us-delta.md` (§8 caso, §9 jerga). Tamaño **M**: F2 ≤ 1,8 M, F3 ≤ 0,8 M tokens (F1 ≈ 0,6 M).
> Lo que no está aquí ni en las SPEC heredadas no se hace. Elegido por demanda US el 13-oct (clúster ≈ 1.400/mes, LOW).

## 0. Regla de jerga (John, 13-oct) — manda sobre todo lo demás

El producto **no se traduce: se adapta** a cómo hablan operadores, salas y planners de EE. UU., en **tres capas**: (1)
producto (nombre, slug, ficheros, pestañas, rótulos), (2) contenido de los 4 entregables, (3) SEO de la landing (title,
H1, meta, H2, FAQ en la redacción del comprador, alt, keywords). **Glosario obligatorio = research §9** (38 términos +
«(e) no se traducen literalmente»). Va entero en `BRIEF-TRADUCTORES.md`, y la revisión final comprueba las 3 capas contra él.
Reglas fijas: «mobile bar» (negocio) ≠ «portable bar» (mueble); «dry hire» + glosa «(you supply the alcohol; we bring the
bar, the bartenders and everything else)» en la primera mención de cada entregable; «signature cocktails», nunca
«author cocktails»; «W-2 event bartenders», nunca «freelance»; «cash bar» solo para decir que está prohibida en dry hire.

## 1. Producto (D81-D83)

| D | Tema | Decisión |
|---|---|---|
| D81 | Nombre y URLs | **Mobile Bar Business Plan Kit** · slug/productId `mobile-bar-business-plan` · JWT `mobile-bar-business-plan-jwt` · `/en/digital-products/mobile-bar-business-plan` (+ `/access`, `/library`) · gemelo ES (hreflang recíproco) `/plan-negocio-cocteleria-eventos` · env `VITE_STRIPE_PAYMENT_LINK_MOBILE_BAR_BUSINESS_PLAN` |
| D81b | SEO de la landing | Title, H1 (Forma B), meta, 6 H2, 8 FAQ, alt y keywords **tal cual research §9 «Términos para la landing»**. Se ajusta un H2 solo si choca con el diseño de `PlanNegocioLandingPage` (el H2 conserva sus keywords) |
| D82 | Precio, SIN anclas | **$39** pago único (D49: sin `priceOld`, «-x %», «Total value», «Save $» ni precio en bonos). Comparables: research §7 |
| D83 | Ficheros (`dl/mobile-bar-business-plan/`), **4** | `mobile-bar-business-plan.docx` «Mobile Bar Business Plan (10 Sections)» · `mobile-bar-financial-projections.xlsx` «Mobile Bar Financial Projections: 3-Year P&L, Cash Flow & Financing» · `mobile-bar-pricing-calculator.xlsx` «Mobile Bar Pricing Calculator (Cost per Guest to Quote + Shopping List)» · `mobile-bar-startup-checklist.xlsx` «Mobile Bar Startup Checklist (68 Tasks)». docProps D20 con las keywords de research §9. Sin 5.º fichero: la carta de cócteles y el equipamiento del ES entran en la calculadora (D90) |

## 2. Concepto y caso (D84-D85)

| D | Tema | Decisión |
|---|---|---|
| D84 | Concepto | Research §1 tal cual: **mobile bar & bartending service en DRY HIRE**. Remolque-barra convertido + barra portátil para el 2.º equipo; bartenders W-2 certificados, signature cocktails, mixers/garnish/hielo/vasos incluidos, setup & breakdown y **shopping list** para el anfitrión. Bodas, eventos de empresa y fiestas privadas. Las 10 experiencias del ES → **specialty bars** (mimosa, espresso martini…) como diferencial y recargo. **Full-service con licencia = opción explicada en el docx §9**, no el caso. No es nuestro comprador: bar con local (Bar Business Plan Kit), catering, food truck |
| D85 | Caso US | Celdas de research §8 tal cual sobre el libro del catering: **B4 160 · B5 $14 · B6 95** (≈ $212,800), mezcla 85/15 (bar packages / add-ons), coste 19/20 %, desechables 4 %, marketplaces 20 % × 5 %, tarjeta 3 %, trastero y parking $600/mes, seguros $4,000, propios $26,000, préstamo **CALIBRAR** (≈ $50K, 10 %, 7 años; SBA Microloan), vidas 7/5, rampa 0,45/9, 2 meses previos, cobro 1 día, **alcohol 0 %**, `B39` 8 % sobre toda la factura, `B51` 260, estacionalidad con Month 1 = marzo (§8), escenarios 120·$12.60·86 / 200·$15.40·105, personal de 4 puestos (§8), inversión fila a fila (§8, ≈ $47,500), fijos (§8). **D15**: holgura ≥ 15 %; si no, `B4` de 10 en 10 hasta 180; si la caja mínima ≤ 0 por la rampa, `B35` 3 → 4 antes de tocar el precio; todo en `CALIBRACION_D15` y `F2-NOTAS`. **El docx dice la verdad del caso**: cuartil alto de Check Cherry, la mediana del primer año es de 3 eventos, operador a tiempo completo con 2 equipos; si el pesimista agota la caja, lo dice |

## 3. Libro financiero (D86-D88) — conjunto nuevo `mbar` sobre el catering

| D | Tema | Decisión |
|---|---|---|
| D86 | Código | Inventario §1 tal cual: código común **solo** con la rama `elif CONJUNTO == 'mbar'` de `business-plans-en/mapas.py`. Lo demás va en `business-plans-en-5/` (`mapas_mbar.py` con `_cargar_cat` = **diccionario por celda = EN publicado del catering**, sha256 del diccionario fijados en el código · `datos_mbar.py` · `bp5.py` · `fuente_mbar.py` · `barrido_mbar.py` · `calculadora_mbar.py` · `BRIEF-TRADUCTORES.md`). Grupos `GM` (322 tal cual) · `GRC-plan` (94, revisión) · `GMB-plan` (128) · `GMB-check` (272). Regresión: FT/CAF, REST/PAN, BAR **y CAT** en verde |
| D87 | Rótulos y filas | Inventario §3 para la estructura, **con los rótulos y los importes de research §8** (manda el research donde difieren): filas 7-20 = remolque usado, conversión, wrap y fachada, barra portátil, generador, trastero, LLC, permisos y certificaciones, health permit (si el condado lo exige), software, herramientas, inventario inicial, web y lanzamiento, cristalería y coolers. **Vehículo de arrastre = el del dueño, $0**, con nota. `B16/B17` = **gig marketplaces (GigSalad, The Bash, Thumbtack)**. `B24` «Storage unit & trailer parking». Puestos: Owner & Lead Bartender · Second-crew lead bartender (part-time W-2) · Event bartenders (hourly W-2) · Barbacks / setup crew (hourly W-2). Nota `Staffing`: W-2, no 1099 (FLSA, CA AB5); el empleador no se queda las propinas. Nota `Cash Flow`: el depósito del 30 % no se modela y mejora la caja real |
| D88 | Umbrales, break-even y D19 | Umbrales `E51:E56` de research §5: margen bruto del motor ≥ 65 % · mercancía + desechables ≤ 26 % · personal ≤ 40 % · trastero y parking ≤ 6 % · neto ≥ 5 % («kit benchmark (editable estimate)»). `Break-Even!B31/D31/E31` = **±$1 / +$2** por invitado. Tabla D19 «US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES», 14 filas de research §5: **solo lo «leída» se cita con fuente**; lo «(resumen)» va como «Kit estimate» |

## 4. Calculadora (D89-D90) — `calculadora_mbar.py` sobre `calculadora_cat.py` (VPS)

- **D89 «Pricing Calculator»** (inventario §4): entradas verdes con DV. **Paquete** de una lista de 3: «Full bar – dry hire» ·
  «Limited bar (beer, wine + 1 signature) – dry hire» · «Full bar – licensed (alcohol included)», el último con nota «only
  if you hold the license, see the plan §9». Más: invitados, horas, copas (2 la 1.ª hora + 1/h, eventplanning.com), bartenders
  sugeridos por paquete (1:50 completa, 1:75 limitada, Kit estimate), barbacks, horas de montaje/viaje/desmontaje, $/h y cargas,
  mixers/garnish/NA por copa, alcohol por copa (solo con licencia), vasos por invitado, hielo 1,5 lb/invitado (Kit
  estimate) × $/lb, bar fee fijo, millas × $/milla, recargo de specialty bar %, comisión de marketplace %, margen objetivo,
  service charge %, sales tax % + interruptor de si se grava el service charge, depósito 30 %, mínimo y precio de la hora extra.
  Salidas: copas, lb de hielo, coste directo, **precio por invitado y su equivalente por hora**, subtotal, service charge,
  impuesto, total, depósito, saldo y **margen calculado**. La gratuity voluntaria queda fuera. Notas: Rev. Rul. 2012-18;
  en dry hire, nada de cobrar copas, entrada con bebida ni recargos sobre el alcohol (MO 24-01).
- **D90 pestañas nuevas**: «Drinks & Shopping List» (copas por categoría según la mezcla, botellas de 750 ml ≈ 16 copas de
  1.5 oz, vino 5 copas por botella, cerveza, bolsas de hielo; **la lista que el bar entrega al anfitrión**) · «Signature
  Cocktail Specs» (**10 recetas** de la carta ES pasadas a oz con 0.25 oz de paso; escalado a 50/100/200 copas **por
  fórmula**, no tecleado, porque el ES lo tiene a la mitad; coste por copa a partir del precio de botella que teclea el
  usuario; alérgenos: orgeat, coco) · «3 Example Quotes» (wedding 120 inv. 5 h full bar · corporate holiday party 100
  inv. 4 h · private birthday 60 inv. 4 h limited bar: los 3 en dry hire y con las mismas fórmulas) · «Instructions».
  **Autotest**: pycel = caché en las 4 pestañas de cálculo, más el paquete con licencia probado en la hoja principal.

## 5. Checklist (D91)

68 tareas **11/13/12/10/12/10** sobre la rejilla del FT, reuso por celda del catering **respetando las ranuras que
sobreviven** (inventario §5). Pestaña F2 **«Phase 2 - Trailer & Permits»**; título «PHASE 2: TRAILER, LIQUOR RULES,
PERMITS & INSURANCE»; título del libro «MOBILE BAR STARTUP CHECKLIST — DRY-HIRE MOBILE BARTENDING COMPANY». Contenido: las
64 tareas válidas del ES (inventario §5) + trámites US de research §6: reglas de alcohol de TU estado para bartending-only
(tabla MO/MT/TX/CA/FL/NY + «varies by state»), edad mínima para servir, certificación (TABC/RBS/TIPS), liquor liability +
COI + additional insured, preguntar al condado por hielo y garnish, hielo comercial embolsado, lavamanos en el remolque,
remolque en el DMV + commercial auto, sales tax permit, contrato con cláusulas de dry hire (el anfitrión compra y es dueño del
alcohol, lo que sobra es suyo, sin cash bar, gratuity pactada), shopping list en D-14, mixers y garnish en D-1. Marketing: The
Knot, WeddingWire, Zola, GigSalad, The Bash, Google Business Profile, bridal shows.

## 6. Docx (D92)

Las 131 ranuras del FT ES; **61 a redactar** según inventario §6 (9 casi literales · ~16 adaptadas del catering · ~36
nuevas), un run por párrafo, **todas las cifras desde `cifras_caso.json`**, escritas (no traducidas) por redactores Sonnet con
el contenido ES de coctelería (inventario §2) y research §1, §5 y §6. **§9 legal = el núcleo**: dry hire y sus condiciones
(MO 24-01, MT), full-service por estado (TX, CA, FL, NY), health permit por condado, seguros (liquor liability, COI),
W-2, sales tax del servicio (CA lo grava) y nota UK (personal licence, TEN). §8: realismo del caso (D85). Fuera todo lo de
España (inventario §2) y las erratas del ES.

## 7. Gates (D93), revisión (D94) y F3 (D95)

- **D93 Gates F2**: G1-G9 de BP · `RX_BAR_NO` = 0 en los 4 ficheros (vocabulario de inventario §7, con su lista blanca:
  «Caterer's Permit», «drink/cocktail menu», «bar station», «trailer», «FDA Food Code», «food handler», «alcohol server»,
  «server certification», «mobile food vendor(s)» solo en contexto legal) · cifras prohibidas (ES de coctelería, como
  importe o como frase, + caso del catering EN + FT) · autotest `Break-Even!B15` · autotest de la calculadora (D90) · no
  latinos · `censo-entregables --letter --only mobile-bar-business-plan` (alta en `PRODUCTOS_LETTER` y en `EXCLUIDOS` de
  `postprocess-transversal.py`) · regresión FT/CAF, REST/PAN, BAR, CAT · sha256 del diccionario del catering sin cambios.
- **D94 Una revisión opus final**: (1) **las 3 capas de jerga contra el glosario §9**; (2) leer el checklist entero (272
  celdas escritas sobre ranuras del catering y del FT); (3) recalcular a mano ventas (160 × 95 × 14), equilibrio y DSCR;
  (4) abrir 3 fuentes legales (MO 24-01, MT Mobile Bars, CDTFA); (5) que el docx no prometa nada que el Excel no haga. Tope
  de 2 rondas; los arreglos, por la vía de texto.
- **D95 F3**: ficha `astro-site/src/data/productos-en/planes/mobile-bar-business-plan.ts` duplicando la del catering
  (`PlanNegocioLandingPage`, carrusel completo, sin anclas), SEO de D81b, FAQ en la redacción del comprador (incluida «Do I
  need a liquor license for a dry hire mobile bar?»), `/access` y `/library` con su island, dashboard, registros (`tienda.ts`,
  `zona-app.ts`, `get-download-urls.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`,
  `product-prices.ts` $39), las tres puertas cripto heredadas de la plantilla, `llms.txt`/`llms-full.txt` («13 products»),
  hub EN, `footerLinks` de las 12 fichas EN, hreflang en `plan-negocio-cocteleria-eventos.astro`, FAQ cruzadas desde
  Catering y Bar EN. **Imágenes**: reutilizar las del ES de coctelería que no lleven texto; si quedan menos de 4 útiles o
  ninguna enseña un remolque-barra, se generan 2 con la skill `generate-images` (bar trailer en una boda al aire libre ·
  lead bartender y barback en una portable bar) más la `og-mobile-bar-business-plan.jpg`. Gates F3:
  `gate-flujo-postpago --only mobile-bar-business-plan`, `tienda-gate`, `robots-gate`, `carrusel-apps-gate`. Correo EN
  de lanzamiento: hueco **24-nov 14:00Z** (borrador + routine el 25-oct).
- **Deuda ES anotada (no se toca aquí)**: inventario §8 (plan financiero sin fórmulas, inversión 18-35K frente a 40.030,
  break-even contradictorio, «10 ejemplos» tecleados, escalado de la carta a la mitad, tarifas guardadas como fechas,
  erratas). Pasa al calendario como entrada de la **coctelería ES 2.2** (línea B), que podrá reutilizar este motor.
