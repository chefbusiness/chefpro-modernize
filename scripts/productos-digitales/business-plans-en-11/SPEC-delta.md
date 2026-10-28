# Coffee Cart Business Plan Kit (EN) — SPEC DELTA (F1 · 28-oct-2026 · sesión Claude Code)

> Edición EN (EE. UU.) del «Plan de Negocio: Cafetería Móvil para Eventos» 1.0 (45 €, en F2), **duplicada del ES**. **Mandan las
> SPEC heredadas** (`../business-plans-en/SPEC.md` D1-D29 … `-7/` D114-D132 = **Paella**, cuyo código se clona; `-9/` D171 =
> contrato; `-8/` = Escandallo): aquí solo lo que cambia frente a la Paella EN. Base: `F1-inventario-delta.md` (= **inv. §n**) y
> `F1-research-us-delta.md` (= **research §n**; manda en caso, jerga y riesgos). Numeración **D216-D235** (D215 = última de
> `-10/`). Tamaño **M** (5 entregables): F2 restante ≤ 0,9 M · F3 ≤ 0,5 M · ≈ 3 h + el link; +30 % → se para y se reporta.

## 0. Jerga (John, 13-oct) — manda sobre todo

Glosario = **research §9** entero (22 términos + «(e)»), pegado en `BRIEF-TRADUCTORES.md` §1 y en `GLOSARIO-JERGA-ES-EN.md`.
**«coffee cart»** en nombre, slug, H1 y ficheros; **«coffee catering»** y **«mobile espresso bar»** en subtítulo y cuerpo;
«coffee truck» / «coffee trailer» **solo como formatos** (H2 y FAQ); **nunca «mobile cafeteria»** ni «mobile café» (falso amigo).
espresso cart · portable espresso bar · full-service espresso bar · self-serve coffee station · hosted / guest-pay · minimum
sales guarantee · service window · base fee + hourly rate · retainer · final guest count · travel fee · drinks per hour · cost
per drink (nunca «recipe costing» ni «escandallo») · alt / oat milk · batch & cold brew · branded cups · latte printing ·
commissary · mobile food unit permit · plan review · COI. Unidades D14: lb / oz, °F, gal, miles, ft; **dosis en g con su oz**
(«18 g (0.63 oz)»); electricidad en V / A / W; métrica entre paréntesis. Sin tildes.

## 1. Producto (D216-D218)

| D | Tema | Decisión |
|---|---|---|
| D216 | Nombre y URLs | **Coffee Cart Business Plan Kit** · slug/productId `coffee-cart-business-plan` · JWT `coffee-cart-business-plan-jwt` · `/en/digital-products/coffee-cart-business-plan` (+ `/access`, `/library`) · gemelo ES `/plan-negocio-cafeteria-movil-eventos` (hreflang recíproco: el ES nace con `locales={['es']}` y la F3 EN lo pasa a `alternatesFamilia`) · env `VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN` · Stripe «Coffee Cart Business Plan Kit» (USD 39, prosa sin viñetas) |
| D216b | SEO | Title, H1 Forma B (`Coffee Cart ` + oro `Business Plan` + «Template for a Mobile Espresso Bar & Coffee Catering Company: …»), meta, 6 H2, 8 FAQ, 3 alt y keywords **tal cual research §9 «Términos para la landing»**; cifras de la FAQ desde `cifras_caso.json`; FAQ «Can I use this as a coffee truck business plan?» deriva la ruta diaria al Food Truck Kit |
| D217 | Precio | **$39** pago único: sin tachado, «worth $X», ratings ni reviews |
| D218 | Ficheros (`dl/coffee-cart-business-plan/`): **5 + guía común** | `coffee-cart-business-plan.docx` «Coffee Cart Business Plan (10 Sections)» · `coffee-cart-financial-projections.xlsx` «… 3-Year P&L, Cash Flow & Financing» · `coffee-cart-pricing-calculator.xlsx` «Coffee Cart Pricing Calculator (Cost per Drink to Quote per Guest)» · `coffee-cart-startup-checklist.xlsx` «Coffee Cart Startup Checklist (68 Tasks)» · `coffee-catering-service-agreement-template.docx` «Coffee Catering Service Agreement Template» + `equivalents-guide` común en descargas. La guía ES ↔ LatAm no cruza. **Versión 2.2 · October 2026** (la familia EN; el ES es 1.0: «v1.0» vetado). Si la F2 pasa de 2 h, se cae el contrato (como el ES) |

## 2. Concepto y caso (D219-D220)

| D | Tema | Decisión |
|---|---|---|
| D219 | Concepto | Research §1: **coffee catering company con dos estaciones** (espresso cart + portable espresso bar) en un **remolque cerrado** que arrastra el vehículo del dueño; servicio **hosted** con baristas W-2; **empresa entre semana = volumen** (69.3 % de las reservas, Flashquotes), **bodas = ticket**, fiestas privadas; **festivales y farmers markets guest-pay** con minimum sales guarantee como complemento; base en una **commissary**. Fuera (FAQ): coffee shop con local, food truck de ruta diaria, espresso martinis (licencia: «partner with a licensed mobile bar»), drive-thru |
| D220 | Caso US | `VALORES_EN` = research §8 con las filas de D222: **B4 170 · B5 $12.60 · B6 95** · 10/6 % · 85/15 · 12/25 % · B15 4 % · **B16 5 % · B17 15 %** (D224) · B18 3 % · B20 10 % · B21 12 · B22 15,080 · **B24 $700** · B25 1 · B26 $100 · **B27 $3,800** · B28 3 % · **B30 $30,000 · B31 CALIBRAR** (punto fijo **$71,000**: SBA 7(a), 10 %, 7 años) · B35 3 · B39/B40/B63 8 % · B41 0 · B44/B45 7/5 · B51 350 · B52/B53 0.45/9 · B54 1 · B55 10 % · B58/B59 14/7 · **B62 0**; escenarios **128 · $11.34 · 86 / 212 · $13.86 · 105**; Break-Even a **±$1 / +$2**. **D15**: holgura ≥ 15 %, DSCR ≥ 1.25, saldo mín > 0, cobertura ≥ 98 %, neto A1 ≥ 5 % (A3 ≤ 16 %), exceso 0-5 %, umbrales D225; palancas en orden: holgura → B4 +10 (≤ 190) · saldo ≤ 0 → B35 3 → 4 · DSCR → B30. **Medido (paso 1a): VERDE sin calibrar** — ventas $203,490 · EBITDA 21.8 % · neto 9.9 % · CAPEX $71,290 · total $100,290 · equilibrio 141 / 138 eventos · holgura 24 % · DSCR 2.58 · saldo mín $17,705 (mes 7) · **pesimista: caja −$487 (se agota)**. El Word dice la verdad: operador a tiempo completo con venta corporativa activa; el primer año es más lento; julio vende un tercio de diciembre |

## 3. Libro financiero (D221-D226) — conjunto `cof` (clon de `pael`)

| D | Tema | Decisión |
|---|---|---|
| D221 | Código y diccionario | Común: **solo** `elif CONJUNTO == 'cof'` en `business-plans-en/mapas.py`. En `business-plans-en-11/`: `mapas_cof`, `datos_cof`, `bp11`, `fuente_cof`, `barrido_cof`, `calibracion_cof`, `check_contrato`, `contrato_cof`, `regresion_cof.sh`, `canon`, `BRIEF-TRADUCTORES.md`. Diccionario en cadena POR CELDA: **Paella LIVE → Catering** (`SHA_PAEL` 10 + 8 = 18 sha256 en `verificar`). Grupos `GM` 310 · `GRP-plan` 59 (revisión) · `GLP-check` 186 · **`GCF-plan` 148** · **`GCF-check` 89** · GX 167; `REVISAR_EN_TANDA = {'GCF-plan': ('GRP-plan',)}`; 87 forzadas (inv. §1). Regresión de los 10 conjuntos (39/39) |
| D222 | Inversión 7-20 | Las bases de las fórmulas mandan (inv. §3): 7 espresso cart $13,400 · 8 portable espresso bar $5,400 · 9 espresso machines $15,700 · 10 grinders ×4 $4,800 · 11 enclosed cargo trailer $6,500 · 12 trailer wrap, hitch, tie-downs & ramps $1,500 · 13 LLC $1,500 · 14 permits & certifications $1,400 · 15 MFU plan review & cart inspection $1,100 · 16 POS & booking $1,000 · 17 batch brewer, cold brew, smallwares & racks $3,300 · 18 opening inventory $1,500 · 19 website, tastings & launch $5,000 · 20 inverter generator 5,500 W + cords $5,000 = **$67,100**; contingencia por fórmula **$2,790**. Vehículo de arrastre = el del dueño ($0; nota: furgoneta usada ≈ $18,000 si no) |
| D223 | Ventas, variables, fijos, personal | A10/A11 «Coffee bar package sales (…)» / «Add-on sales (extra hours, branded cups & latte printing, pastries, travel fees)» · coste 12 % (con merma) / 25 % · `B15` compostable cups 4 % · fijos 26-35 $21,000 (inv. §3) · `B26` combustible del generador, agua y hielo (= FT) · **Staffing** 4 puestos W-2 (Owner / Lead Barista & Sales $22/h · Lead barista part-time $20 · Event baristas $19 · On-call barista / driver $19) = 1.54 FTE, $5,644/mes; `B18` 7 h, `B19` 1.6; nota A24: «One barista serves about 50-65 drinks an hour» |
| D224 | Canal (decisión SPEC) | B16/B17 = **festivales y farmers markets guest-pay** 5 % × **cuota del organizador 15 %** (Kit estimate; booth fee convertida), duplicando el canal de ferias del ES (D5 ES); research §8 proponía marketplaces 20 % × 5 %: GigSalad / Thumbtack / The Bash / Zola van al marketing fijo. Rótulo «Festival & market organizer fees» |
| D225 | Umbrales y D19 | `E51` 72 % · `E53` 20 % · `E54` 40 % · `E55` 6 % · `E56` 5 % (verdes los 3 años). **D19** «US COFFEE CART & COFFEE CATERING BENCHMARKS (sourced) AND KIT ESTIMATES», 14 filas: 55 precio por reserva (Flashquotes) · 56 precio por invitado por tamaño · 57 bebidas por invitado (GrindKit) · 58 permiso MFU + plan review (Snohomish) · 59 bebidas por hora · 60 coste por bebida · 61 arranque (cart-king; «$5-25K» como Kit) · 62 café y leche (BLS) · 63 base + hora, travel fee, retainer · 64 BLS 35-3023 · **65 shared kitchen** (propuesta) · 66 estacionalidad · **67 Insureon** (propuesta) · 68 tasa de cierre y antelación. Solo lo «[leída]» con fuente; lo «(resumen)» como Kit estimate |
| D226 | Sales tax y Tesorería | `B39`/`B40`/`B63` 8 % sobre toda la factura; `B41` 0; nota C39: hosted = catering, guest-pay = bebida a bebida, «rate and taxability depend on your state and on who pays» · **Month 1 = marzo** (Flashquotes) · POR_CELDA **O5, O20 y A34** con marzo (liquidaciones en junio, septiembre y diciembre; el 4.º trimestre en el mes 13) · C67/E24 con la holgura definida como plan ÷ equilibrio − 1 y la caída absorbible 1 − equilibrio ÷ plan |

## 4. Calculadora (D227) — **paso 1b**: duplicar las 4 hojas de la calculadora ES cuando pase su revisión

`calculadora_cof.py` sobre `calculadora_pael.py` (esqueleto, cobro, cancelación, sales tax, autotest) + `hoja_escandallo` de
`calculadora_piz.py`. Hojas = ES traducidas (inv. §4): **«Cost per Drink»** · **«Pricing Calculator»** · **«3 Example Quotes»**
· **«Instructions»**. Entradas US: $/lb, $/gal, oz, 18 g por doble; canal Private / Corporate / Festival or market; bebidas
por invitado de GrindKit (≤ 2 h 1.0 … 6+ h 2.0-2.5; +25 % por la mañana); 50-65 bebidas por barista y hora; **aviso eléctrico**
(110V / 220V, amperios, generador); retainer 30-50 % + saldo 14 días; tramos «from X to less than Y»; festival: precio por
bebida, cuota y **minimum sales guarantee**. Ejemplos a ±10 % de $15 (boda) / $12 (empresa) / $6.50 (festival). Autotest
pycel multipestaña; 0 precios tecleados en fórmulas; mínimo del Food Code (leche 41 °F) nombrado como tal. La nota `C5` del
libro explica cómo pasar del precio de la calculadora al B5 de la mezcla.

## 5. Checklist (D228) · Docx (D229) · Contrato (D230)

- **D228**: 68 tareas 11/13/12/10/12/10 sobre las filas FINALES de la paella: **22 L · 42 A · 4 N** (inv. §5); pestaña F2
  **«Phase 2 - Permits & Commissary»**; título «COFFEE CART STARTUP CHECKLIST — MOBILE ESPRESSO BAR & COFFEE CATERING»;
  columna C mecánica. **Regla B2 de la pizza**: todo permiso que prometan la landing, la tarjeta o el Word tiene su tarea
  (MFU permit + plan review, temporary event permit, sales tax permit, business license, fire marshal / generador).
- **D229**: 131 ranuras del FT; 61 a redactar (21 L · 28 A · 12 N), un run por párrafo, cifras SOLO con tokens
  (`cifras_caso.json`, 118); nota = nivel + pista + propuesta EN de la paella + ES 1.0 de la ranura (paso 1c). §9 (102-108)
  = commissary · MFU permit + plan review · electricidad, generador y bomberos «as an example» · bollería, vasos, alcohol ·
  sales tax hosted vs guest-pay · W-2 y seguros · remolque en el DMV + nota UK. Cierre: Coffee Shop BP Kit · Mobile Bar BP
  Kit · Coffee Shop Checklists Kit Pro · HACCP Food Safety Kit Pro.
- **D230**: `contrato_cof.py` (molde = docx ES del contrato, Letter) + `textos_en/contrato_en.json` (1 sonnet; reglas y
  decisiones en `check_contrato.py`): cabecera legal literal; corchetes para todo lo editable; **circuito dedicado
  ([110V or 220V], [20] amps, ≤ [50] ft) por escrito o generator fee**; retainer aplicado al precio (nunca «non-refundable»
  solo); tramos sin huecos + «not a penalty» + crédito por recolocar; lluvia ≠ fuerza mayor; Cooling-Off solo como nota
  «ask your attorney whether»; governing law «[State]»; mutual responsibility; anexo corporativo y de festivales (W-9, PO,
  exención, net terms, **minimum sales guarantee**, vendor fee). Cero derecho español.

## 6. Gates (D231), cifras y vocabulario, revisión (D232)

- **D231**: G1-G9 · `RX_COF_NO` = 0 en los 5 (falsos amigos «cafeteria», «mobile café»; FT «per day», «customers», «truck»
  salvo coffee / food / pickup truck, «window» salvo «service window»; paella, BBQ, bar móvil; ES: IVA, autónomo, convenio,
  RD / Ley, Piaggio, furgoneta, bollería, Bizum, «feria»; «recipe costing»; «growing demand»; métrica fuera de paréntesis) ·
  cifras prohibidas: **ES de la cafetería** desde su `cifras_caso_es.json` (`COF_CIFRAS_ES` hasta que esté en git; sin los
  importes que cita la research ni los redondos ≤ $50,000) + «130 events», «135 guests», «6,10-6,20 €» · caso **Paella** + BBQ
  (sin «128 events», que aquí es el pesimista), catering (sin «180 events» si B4 = 180), bar móvil y FT · `check_textos` ·
  `check_contrato` · autotests · no latinos · `censo-entregables --fail --letter --only coffee-cart-business-plan` (alta en
  `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9) · `verificar` (18 sha256) · regresión 10 conjuntos · 2.ª pasada sha canónico.
- **D232 Una revisión opus** (tope 2 rondas, arreglos por texto): recalcular ventas, CAPEX con la contingencia de fórmula,
  equilibrio, holgura, DSCR y el pesimista · jerga de las 3 capas · claims (commissary «usually yes», plan review como
  ejemplo, generador «ask your fire marshal», cottage food fuera, compostable como regla local, Flashquotes ≠ ingresos
  esperados, ≈ 15 reservas/año solo en su plataforma, BLS 35-3023 ≠ «barista wage») · abrir Snohomish y Flashquotes ·
  coherencia del aviso eléctrico en Word, checklist, calculadora y contrato · **cero rastro de paella, BBQ y España** ·
  checklist entero · que el Word no prometa lo que el Excel no hace.

## 7. Capa de producto (D233, F3) — duplicar la F3 de la Finca EN (`ae531f6b`, 5 entregables) con el hub de la Heladería

Ficha `coffee-cart-business-plan.ts` = `cp` de `wedding-venue-business-plan.ts` (SEO D216b; cifras MEDIDAS: ventas, CAPEX, neto %
del año 1, equilibrio; nada de neto del año 3; sin testimonios: los del ES son de España, FTC) · páginas, isla, dashboard (5
tarjetas), functions ×4, registros, changelog '2.2', `tienda.ts` + hreflang del ES, `footerLinks` (Coffee Shop, Mobile Bar, Food
Truck, Catering, Coffee Shop Checklists) + FAQ cruzada, `llms`, `sitemap-lastmod`, gates (inv. §7). **Hub EN: sustituir la
tarjeta ES** que meta la F3 del ES (B1 de PIZ), no añadir otra. Imágenes: las 7 del ES (`plan-cafe-movil-*`) sin texto en
español + `og-coffee-cart-business-plan.jpg`; alt de research §9. **Payment Link: John.** Correo EN en el siguiente hueco libre
de la cola EN (CALENDARIO l. 790: **10-mar-2027 14:00Z** si sigue libre) con routine ≥ 30 días antes. El ES se mergea primero.

## 8. Plan, presupuesto y riesgos (D234-D235)

| Paso (D234) | Quién | Tokens · reloj |
|---|---|---|
| 1a ✅ conjunto, caso, D15, extracción, tandas, brief, regresión | opus | ≈ 0,45 M (con F1) |
| 1b calculadora ‖ 1c re-extracción (tras la revisión del ES) | 1 opus/sonnet · VPS | 0,23 M · 40 min |
| Tanda 1: (a) GCF-plan + GRP ‖ (b) GCF-check + contrato · Tanda 2: cof_a ‖ cof_b (sonnet reanudados con SendMessage) | 2 sonnet | 0,42 M · 45 min |
| Paso 3 + gates + revisión D232 + 1 ronda; F2-NOTAS | VPS + opus | 0,25 M · 35 min |
| F3 + PR + gates contra preview + link + LIVE | 2 sonnet + orquestador | 0,5 M · 60 min |

**D235 Riesgos**: (1) **el ES cambia** tras su revisión → 1c (solo notas y cifras vetadas; ids estables mientras no cambien
FIJOS / POR_CELDA / pistas / grupos); (2) **calculadora** sin ES cerrado: no se empieza antes; (3) legal por condado
(commissary, plan review, generador): solo ejemplos con fuente; (4) fuga de la paella en propuestas (pans, burners, van, socarrat)
→ `RX_COF_NO` + revisión; (5) pesimista que agota la caja por $487: decirlo sin dramatizar; (6) canibalización con Coffee Shop y
Food Truck EN (la landing deriva); (7) conflictos de merge con el ES en hub, `tienda.ts`, CALENDARIO y glosario. **NO se hace**:
testimonios, anclas, ratings, tabla de 50 estados, espresso martinis, research nueva, posts, compra de prueba.
