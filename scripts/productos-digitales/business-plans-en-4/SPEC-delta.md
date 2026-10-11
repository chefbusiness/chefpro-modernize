# Catering Business Plan Kit (EN) — SPEC DELTA (F1 · 11-oct-2026 · sesión Claude Code)

> Producto 12 de la tienda EN. **Mandan `../business-plans-en/SPEC.md` (D1-D29), `../business-plans-en-2/SPEC-delta.md`
> (D30-D47) y `../business-plans-en-3/SPEC-delta.md` (D48-D65)**: aquí solo lo que cambia. Base: `F1-inventario-delta.md`
> (gemelo = **Food Truck**; fuente ES de contenido = `plan-catering-tematico-eventos`, línea B, cuyas cifras y fórmulas NO
> se reutilizan) y `F1-research-us-delta.md`. Tamaño **M**: F2 ≤ 1,8 M, F3 ≤ 0,8 M tokens (F1 gastó 0,59 M). Lo que no
> está aquí ni en las SPEC heredadas no se hace. Decisión de alcance aprobada por John el 11-oct: los mismos ficheros que
> los otros planes EN **+ la calculadora de precios**; fuera contratos, menús, manual multicocina, catálogo y proveedores.

## 1. Producto (D66-D68)

| D | Tema | Decisión |
|---|---|---|
| D66 | Nombre y URLs | **Catering Business Plan Kit** · slug/productId `catering-business-plan` · JWT `catering-business-plan-jwt` · `/en/digital-products/catering-business-plan` (+ `/access`, `/library`) · gemelo ES (hreflang recíproco) `/plan-catering-tematico-eventos` · env `VITE_STRIPE_PAYMENT_LINK_CATERING_BUSINESS_PLAN` |
| D66b | H1 · title · keywords | H1 Forma B: `Catering ` + oro `Business Plan` + «Template for an Event Catering Company: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist». Title: «Catering Business Plan Template: Word + Excel Financial Projections + Pricing Calculator \| AI Chef Pro». docProps keywords: catering business plan, catering business plan template, how to start a catering business, catering startup costs, catering pricing per person, AI Chef Pro |
| D67 | Precio, SIN anclas | **$39** pago único (D49 tal cual: sin `priceOld`, «-x %», «Total value», «Save $» ni precio en los bonos). Comparables: Growthink $97, eFinancialModels $95-99 (research §7) |
| D68 | Ficheros (`dl/catering-business-plan/`), **4** | `catering-business-plan.docx` «Catering Business Plan (10 Sections)» · `catering-financial-projections.xlsx` «Catering Financial Projections: 3-Year P&L, Cash Flow & Financing» · `catering-pricing-calculator.xlsx` «Catering Pricing Calculator (Cost per Guest to Quote)» · `catering-startup-checklist.xlsx` «Catering Startup Checklist (68 Tasks)». docProps D20; checklist `Instructions!A3` con el nombre comercial (I5) |

## 2. Concepto y caso (D69-D70)

| D | Tema | Decisión |
|---|---|---|
| D69 | Concepto | **Full-service off-site event caterer** desde cocina comisaria compartida con permiso + furgoneta refrigerada: empresas entre semana (drop-off, buffets, recepciones, diciembre) y particulares el fin de semana (bodas, fiestas privadas); estilos drop-off · buffet · family-style · plated · stations. Lo temático del ES queda como diferencial de carta: **chef-attended themed stations** (research §1). Sin 12 cocinas ni su equipo. Sin alcohol propio: el cliente lo compra y lo sirven bartenders certificados (research §6) |
| D70 | Caso US | Celdas de research §8 tal cual sobre el libro FT EN: **B4 170 eventos/año · B5 $60/invitado (sin sales tax, servicio incluido) · B6 60 invitados/evento** (≈ $612K), comida 88 %, coste 30/25 %, desechables 3 %, marketplaces 10/15 %, tarjeta 2,5 %, comisaria $2,500/mes, seguros $6,000, fondos propios $40K, préstamo **CALIBRAR** (≈ $140K, 10 %, 7 años), vidas 5/7, rampa 0,50/8, **cobro 14 días**, **alcohol 0 %**, estacionalidad 7·8·9,5·10·7·7·10·11·8,5·11,5·5·5,5 % con Month 1 = marzo. Regla D15: holgura del break-even ≥ 15 %; si no, subir B4 de 10 en 10 hasta 190 y, si aún no, reportar. `B51` = el límite con el que el libro compare (medirlo en F2): si es el techo del break-even, «Max events a year your kitchen and crew can handle» = 250 [estimado]. Cifras ES prohibidas en el EN (gate): 603.700 · 303.364 · 8.520 · 21.410 · 54.440 · 10.560 · 2.200 · 4.500 · 846.720 · «14 eventos/mes» · 5.500 · 11.500 · 55 % de margen |

## 3. Libro financiero (D71-D75) — molde FT, conjunto nuevo `cat`

| D | Tema | Decisión |
|---|---|---|
| D71 | Código | Conjunto `cat`: `mapas.py` gana `elif CONJUNTO == 'cat'` → `business-plans-en-4/mapas_cat.py` (`instalar(M)` como `mapas_bar.py`), `datos_cat.py` y lanzador `bp4.py` (copia de `bp3.py`), fuente ES del circuito = **FT ES** (`plan-negocio-food-truck`). Reutilizar el EN del FT por diccionario; a los traductores, solo las cadenas nuevas de catering (≈ 258) + las 32 del motor que hablan de clientes/día. Regresión: autotests y gates de FT/CAF, REST/PAN y BAR en verde |
| D72 | Motor permutado | Solo rótulos: `B4` = **events per year**, `B5` = **average price per guest (excl. sales tax, service included)**, `B6` = **average guests per event**. Fórmulas que cambian: **`Staffing!B20`** → `…!$B$4` (horas × personas × **eventos**) y **`Staffing!C9`** → `SUMPRODUCT(B5:B8,C5:C8)` (E4); **`Break-Even!B31,D31,E31`** escalones de precio ±$10/+$20. Break-even en **eventos/año** (`B15`) con su rótulo. Gate de vocabulario FT = 0 en el libro EN: per day, operating days, customers (salvo «corporate customers»), truck, window, festival, service window |
| D73 | Personal (opción A) | 4 puestos (research §8): Owner / executive chef · Sous chef · **Event staff (servers, bartenders, attendants; hourly W-2)** 8 personas × 0,22 FTE · Prep cook / driver. Fijo + cobertura por evento (B18 horas/evento 12 × B19 personas 4,3). Nota en `Staffing`: personal de eventos en nómina (W-2), con cargas y workers' comp; contratarlo como 1099 es riesgo de mala clasificación (FLSA; California AB5). Nota en Escenarios: en el pesimista el coste real del personal de eventos baja con los eventos |
| D74 | Inversión, fijos, variables | Filas 7-20 = rótulos de `F1-inventario-delta.md` §3 (furgoneta refrigerada usada, adaptación, equipo propio, cocina portátil y energía, unidad de frío, almacenaje en la comisaria, LLC, permisos del año 1, plan review solo si alquilas cocina propia, software de catering + datáfono, menaje GN, inventario inicial, web/fotos/lanzamiento, chafing dishes + cajas isotermas + menaje de servicio) con los importes de research §8 (≈ $97,500 + fianza, meses previos e imprevistos ≈ $106,100). Fijos `A22` «Commissary kitchen rent & van parking», `A27` «Van fuel, maintenance and inspections», `A35` «Tastings for prospects». `B16/B17` = **corporate catering marketplaces (e.g. ezCater)**: cuota × comisión. Nota `Cash Flow!A5`: Month 1 = mes de apertura; los anticipos (25-50 %) no se modelan y mejoran la caja real |
| D75 | Umbrales y tabla D19 | Umbrales `3-Year P&L` (research §5): margen bruto ≥ 62 % · mercancía + desechables ≤ 35 % · personal ≤ 38 % · comisaria ≤ 8 % · neto ≥ 5 %, «kit benchmark (editable estimate)». Tabla D19 «US CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» con las filas de research §5 (food cost 28-35 %, personal 25-35 %, neto 7-8 %, $/invitado por estilo, bodas $80/plato, ezCater 15 %/7 %, anticipos, sueldos) — **solo fuentes leídas**; las marcadas «(resumen)» se citan como «Kit estimate» o se abren en F2 antes de citarlas |

## 4. Calculadora de precios (D76) — código nuevo `calculadora_cat.py` (openpyxl, en el VPS)

Coste → precio, entradas verdes con DV de lista: invitados · estilo de servicio (5) · coste de comida por invitado
(escandallo) · paquete de bebida sin alcohol · personal de evento (personas × horas × $/h + cargas %) · alquileres repercutidos ·
millas × $/milla · margen objetivo % · **service charge %** · **sales tax %** + interruptor «¿grava el service charge en tu
estado?» (Sí/No, con nota CA sí · NY salvo gratuity íntegra al personal · TX exento ≤ 20 % separado y repartido) · propina
voluntaria **fuera** del precio · anticipo % (35 %) · mínimo de invitados. Salidas: precio por invitado, subtotal, service charge,
impuesto, total, anticipo, saldo y **margen bruto calculado** (no tecleado). Nota IRS Rev. Rul. 2012-18: el service charge es
salario, no propina. Hoja 2 «3 Example Quotes» (corporate drop-off lunch · wedding buffet · plated dinner) calculados por la
propia fórmula; **sin** «10 ejemplos validados». Hoja «Instructions». Autotest: recalcular los 3 ejemplos con pycel = salida.

## 5. Checklist (D77)

Molde FT (circuito de texto sobre el FT ES): **68 tareas 11/13/12/10/12/10**, DV `✓,☐,N/A`, contadores y CF intactos.
Pestaña F2 **«Phase 2 - Kitchen, Van & Permits»**; título «CATERING STARTUP CHECKLIST — FULL-SERVICE EVENT CATERER».
Contenido: las 99 tareas válidas del ES condensadas (inventario §5) + trámites US de research §6: commissary agreement
por escrito, catering / health permit, temporary food event permits, fire marshal, registro y commercial auto de la
furgoneta, liquor liability si se sirve alcohol del cliente; P4 Staff desde el EN del FT/REST (I-9, W-4, new-hire
reporting, workers' comp, food handler cards, OSHA, alcohol server certification); marketing US (The Knot, WeddingWire,
ezCater, Google). Fuera las 9 «solo España» y las 12 de equipo multicocina.

## 6. Docx (D78)

Las 131 ranuras fijas del FT ES (D22/D23; H1 en 37·44·51·59·67·76·83·91·100·109), un run por párrafo, **todas las cifras
desde `cifras_caso.json`**, escrito (no traducido) por redactores Sonnet con el contenido del ES (concepto, mezcla
particulares/empresas, política comercial —anticipo, cancelación—, operativa de un evento en 6 fases, riesgos) y research
§6 (legal). Fuera L14 (portada «España 2026», «ChefBusiness Consultoría», «96 proveedores validados», porcentajes sin fuente).
§9 legal: comisaria obligatoria y catering desde casa no legal (FDA Food Code; cottage food), permisos por evento, alcohol
(sin licencia propia por defecto), sales tax sobre toda la factura y el service charge por estado, W-2 vs 1099, seguros.

## 7. Gates (D79) y F3 (D80)

- **Gates F2:** G1-G9 de BP + vocabulario FT = 0 (D72) + autotest `Break-Even!B15` (eventos/año del caso) + cifras ES
  prohibidas (D70) + autotest de la calculadora (D76) + no latinos + `censo-entregables` de los 4 ficheros. **Una**
  revisión opus final (recalcular cifras a mano, abrir 3 fuentes legales).
- **F3:** ficha `productos-en/planes/catering-business-plan.ts` duplicando la del FT EN (misma plantilla
  `PlanNegocioLandingPage`, carrusel completo de 9 logos, sin anclas), FAQ desde PAA de research §3 (incluida «¿desde
  casa?» → no), `/access` y `/library` con su island, dashboard, registros (`tienda.ts`, `zona-app.ts`,
  `get-download-urls.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`, `product-prices.ts` $39),
  `llms.txt`/`llms-full.txt` («12 products»), hub EN, `footerLinks` de las 11 fichas EN, hreflang en
  `plan-catering-tematico-eventos.astro`, FAQ cruzadas desde Food Truck y Restaurant. Correo EN de lanzamiento: hueco
  **24-nov 14:00Z** (programable desde el 25-oct). Gates F3: `gate-flujo-postpago --only catering-business-plan`,
  `tienda-gate`, `robots-gate`, `carrusel-apps-gate`.
- **Deuda ES anotada (no se toca aquí):** la ficha ES dice «break-even 14 eventos/mes», «60+ pp.» y «10 ejemplos
  validados» (L1, L12, L15): al calendario como deuda de la línea B.
