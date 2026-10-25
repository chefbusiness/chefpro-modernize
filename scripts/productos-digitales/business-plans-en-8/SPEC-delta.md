# Pizza Shop Business Plan Kit (EN) — SPEC DELTA (F1 · 25-oct-2026 · sesión Claude Code)

> Edición EN (EE. UU.) de `plan-negocio-pizzeria` 1.0 (35 €), **duplicada del ES ya revisado**. **Mandan las SPEC heredadas**
> (`../business-plans-en/SPEC.md` D1-D29, `-2/` D30-D47, `-3/` D48-D65 = **Bar**, `-4/`…`-7/` hasta D132): aquí solo lo que cambia
> frente al Bar EN. Base: `F1-inventario-delta.md` (= **inv. §n**) y `F1-research-us-delta.md` (= **research §n**; manda en caso US,
> jerga y riesgos). Tamaño **S/M**: F2 ≤ 1,2 M · F3 ≤ 0,6 M · ≈ 3 h; +30 % → se para y se reporta. «decisión SPEC» = choque resuelto aquí.

## 0. Jerga (John, 13-oct) — manda sobre todo

Glosario obligatorio = **research §9** entero (26 términos + «(e) no se traducen literalmente»), pegado en `BRIEF-TRADUCTORES.md`: «pizza shop» en nombre, H1 y ficheros, «pizzeria» en prosa;
**«Neapolitan-style»** (nunca «authentic», «verace» ni «VPN-certified» como promesa); «covers» (Bar D55). Unidades D14 + `REGLA_UNIDADES` de PAEL (US, métrico entre paréntesis) salvo la masa en gramos (D145). Sin
tildes.

## 1. Producto (D133-D135)

| D | Tema | Decisión |
|---|---|---|
| D133 | Nombre y URLs | **Pizza Shop Business Plan Kit** · slug/productId `pizza-shop-business-plan` · JWT `pizza-shop-business-plan-jwt` · `/en/digital-products/pizza-shop-business-plan` (+ `/access`, `/library`) · gemelo ES `/plan-negocio-pizzeria`, hreflang recíproco (**el ES tiene hoy `locales={['es']}`**: F3 lo pasa a `alternatesFamilia`, D152) · env `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN`. Sin choque con `pizza-shop-checklist-templates` (otro producto, $19, rutinas) |
| D133b | SEO | Title «Pizza Shop Business Plan Template: Word + Excel Financial Projections + Dough & Food Cost Calculator \| AI Chef Pro» · **H1 Forma B** `Pizza Shop ` + oro `Business Plan` + «Template to Open a Neapolitan-Style Pizzeria: Word Plan + Excel Projections + Dough & Food Cost Calculator + Startup Checklist» · meta, 6 H2, 3 alt y keywords **tal cual research §9** (= docProps) |
| D134 | Precio | **$39** pago único (D49): sin `priceOld`, «-70 %», «Total value», «Save $» ni precio en bonos; sin rating ni review |
| D135 | Ficheros (`dl/pizza-shop-business-plan/`): **4 + guía común** | `pizza-shop-business-plan.docx` «Pizza Shop Business Plan (10 Sections)» · `pizza-shop-financial-projections.xlsx` «Pizza Shop Financial Projections: 3-Year P&L, Cash Flow & Financing» · `pizza-shop-startup-checklist.xlsx` «Pizza Shop Startup Checklist (80 Tasks)» · `pizza-dough-food-cost-calculator.xlsx` «Pizza Dough & Food Cost Calculator (Neapolitan-Style Dough + Food Cost for 8 Pizzas)». **Decisión SPEC** (research proponía un `pizza-shop-equivalents-guide.docx`): la guía ES↔LatAm no cruza; bonus **común** `equivalents-guide` → `/dl/en-shared/hospitality-equivalents-us-uk-canada-australia.docx`, como los 9 planes EN |

## 2. Concepto y caso (D136-D137)

| D | Tema | Decisión |
|---|---|---|
| D136 | Concepto | Research §1: **Neapolitan-style pizza shop** de barrio (ciudad de 150-300 mil hab.), ~1,500 sq ft, 50 plazas + patio de 24 (abr-oct), mesa + take-out/delivery, horno de leña 47-51 in UL 2162 (gas/eléctrico = variante en el Word), **beer & wine**, cierra lunes, dueño = pizzaiolo y GM. Fuera (FAQ): slice shop NY, franquicia, food truck (→ Food Truck Kit), ghost kitchen, venta desde casa |
| D137 | Caso US | `VALORES_EN` = research §8 sobre las celdas de inv. §2.3: **B4 62 · B5 $35 · B6 300** · 6/4 % · 82/18 · 26/26 % · B15 3.5 % · **B16 12 % · B17 25 %** · B18 3 % · B20 10 % · B21 12 · B22 15,080 · B24 $4,000 · B25 2 · B26 $1,800 · B27 $7,500 · B28 1 % · **B30 $130,000 · B31 CALIBRAR** (semilla $192,400; SBA 7(a) 10 % a 10 años, interest-only 0) · B35 3 · B37/B38 25 % · B39/B40/B63 8 % · B41 0 · B44/B45 10/7 · B51 50 · B52/B53 0.75/4 · B54 2 · B55 10 % · B58/B59 2/14 · B62 0.50 · B65-B67 1.15/1.25/15 % · B68 vacío; escenarios 54·$32.50·295 / 70·$37.50·305. **D15**: holgura año 1 ≥ 15 %, DSCR mín ≥ 1.25, saldo mín > 0, cobertura ≥ 98 %, neto a régimen ≤ 12 %, D142 verde; palancas en su orden (research §8): holgura → B30 +$10,000 o B5 $36 · neto > 12 % → B4 58 · DSCR → B30. Máx. 3 vueltas, todo en `CALIBRACION_D15` y `F2-NOTAS`. El Word dice la verdad: neto ≈ 5 % frente al «15-25 %» de la SERP |

## 3. Libro financiero (D138-D144) — conjunto nuevo `piz` (clon del `bar`)

| D | Tema | Decisión |
|---|---|---|
| D138 | Código y diccionario | Código común **solo** `elif CONJUNTO == 'piz'` en `business-plans-en/mapas.py` (copia de `:1205-1210`). Clones de inv. §7 en esta carpeta (`mapas_piz`, `datos_piz`, `bp8`, `derivar_formulas_piz`, `formulas_piz_manual`, `inventario_delta`, `resumen_entregables`, `calculadora_piz`, `barrido_piz`, `BRIEF-TRADUCTORES.md`). Molde del Bar (plan `_HOJAS_PLAN`, checklist `hojas`, `COL_OK 1`); **docx = config de PAEL** (131). **Reuso exacto con el Bar EN primero** (GM, GR, GBAR-plan, GBAR-check y POR_CELDA de `-3/`), luego BP/BP2, **normalizando antes «comensal(es)» → «cubierto(s)»**; lo reutilizado de otra celda va a `GR` con revisión en la tanda. Grupos `GM · GR · GPIZ-plan · GPIZ-check · GX`. `verificar`: sha256 del ES final + los 3 del Bar EN. Regresión: ftcaf, restpan, bar, cat, mbar, bbq, pael |
| D139 | Inversión 7-24 (solo rótulo e importe: **ninguna fila se mueve**; la clase de amortización la fija la fila) | 7 Architect, MEP, hood & flue drawings, plan review & permit fees (incl. **beer & wine license, non-quota state ≈ $3,000**; quota states: far more, ask your state ABC) $14,000 · 8 Build-out (second-generation space), signage & facade $46,500 · 9 Flue/chimney, spark arrestor & insulated hearth pad $12,000 · 10 Electrical service & panel $8,000 · 11 Plumbing, grease interceptor, HVAC & makeup air $12,000 · 12 Neapolitan wood-fired dome oven (47-51 in, UL 2162-listed) $22,000 · 13 Spiral mixer (60 qt) $8,000 · 14 Pizza prep table (67-71 in) $6,500 · 15 Walk-in (6×8), reach-ins, dough-ball cabinets & freezer $19,800 · 16 Type I hood & support line (fryer, range) $9,000 · 17 3-comp sink, dish machine, hand sinks & stainless $12,000 · 18 Peels, dough boxes, scales & smallwares $5,500 · 19 Beer & wine bar (taps, back bar, espresso) $7,000 · 20 Furniture (50 seats) & patio $16,000 · 21 POS, online ordering & delivery tablets $4,500 · 22 LLC, legal & food safety plan $2,500 · 23 Branding, website, training & launch $6,500 · 24 Opening inventory $5,500 = **$217,300**. Imprevistos **por fórmula** (10 % de B7-B11 = $9,250, no $8,300: decisión SPEC como PAEL D118). A1-A3 «US kit example (2026) — replace with your own quotes». Si el ES arregla «Campaña»/B16 (inv. §8), la 16 entra en equipo; si no, deuda anotada |
| D140 | P&L, fijos, personal | A2 «Base case — Neapolitan-style pizza shop, 50 seats + patio» · A10 «Food sales (pizza, starters & desserts: dine-in, take-out & delivery)» · A11 «Beverage sales (beer, wine, soft drinks & coffee)» · fijos 26-34 (**$30,400**): accounting 4,200 · maintenance (oven, hood & flue cleaning, refrigeration) 3,600 · marketing 6,000 · software, POS & online ordering 3,600 · cleaning, linens, uniforms & pest control 3,300 · **firewood** 5,500 · waste, grease & ash 2,400 · music licensing (ASCAP/BMI/SESAC) 1,000 · food safety & staff training (CFPM, allergens, OSHA) 800. **Staffing** 7 filas (personas·FTE·bruto mes de la fila; ≥ $15/h, 12 pagas, sin propinas D38): Owner / head pizzaiolo & GM 1·1.0·$4,500 · Pizzaiolo (stretching & oven) 1·1.0·$3,900 · Prep & dough cook 1·0.75·$2,340 · FOH lead / bar 1·1.0·$3,293 · Servers (dinner & weekends, part-time W-2) 2·0.25·$1,343 · Weekend runner / counter & pickup 1·0.375·$975 · Relief cover 1·0.1·$270; B14/B15 $5,000; cobertura = ES. Nota: el dueño cobra por debajo del OEWS ($33.36/h) |
| D141 | Sales tax (inv. §3) | **E5** `3-Year P&L!G11`: `H11*0.21` → `H11*'0. Supuestos'!$B$40` (mecanismo E3 de la Bakery EN); `H4` «Beverage share taxed at the alcohol rate in B40 (%)», **`H11` 0.50**, nota F11 = la de Texas del Bar D57 (efecto nulo con B40 = B39). **`G13` (valor en el ES) → 0**, «no input credit». `G14` → E2 del Bar. `B62` «reference only», `B63` «no effect». Tesorería 16-20 = Bar EN; `A34` «plan quarters, not calendar quarters» |
| D142 | Umbrales y D19 | `E50` 62 % · `E52` 28 % · `E53` 36 % · `E54` 10 % · `E55` 5 %. **D19** (`Instructions` 34-47; sin D18), «US PIZZA SHOP BENCHMARKS (sourced) AND KIT ESTIMATES», 13 filas: Month 1 = September · Margherita food cost (calculadora, Kit) · Margherita **$18** (Bufalina, Antico, via Marina) · Neapolitan dough ratios (EU TSG/AVPN reference, not a US rule) · bake 60-90 s ≈ 900 °F (Kit) · «Neapolitan-style» vs «VPN-certified» (AVPN $2,500 + $300 + $400/yr) · DoorDash 15/25/30 % + 6 % pickup, Uber Eats 15-30 % · sales tax (8 % example) · minimum wage federal $7.25 + state (DOL) · labor 25-35 % (UpMenu) · rent ≤ 10 % (Kit) · firewood ≈ $5,500/yr (Kit) · prime cost ≤ 60 % (Restaurant365). Solo lo «leída» con fuente; lo «(resumen)» = Kit estimate |
| D143 | Fórmulas y excepciones | Con texto: las derivables de su gemela (celda tapas ↔ Bar EN) + manuales C9, C50, D27, D37, F13 (+ A28 si hace falta). **E1** aviso D21 (PIZP `A53`, PIZC `A12`) · **E2** solo `G14` · **E4** `Staffing!C12` → `SUMPRODUCT(B5:B11,C5:C11)` · **E5** (D141). Sin E3. G1 = **741** fórmulas y 80 tareas |
| D144 | Mes 1 y pagas | **Mes 1 = septiembre** (pesos del ES sin tocar); `O5` «Month 1 = SEPTEMBER… replace the weights with your area's pattern»; `B60`/`B61`/`O13`: con 12 pagas no hay extras (EN del Bar) |

## 4. Calculadora (D145) — `calculadora_piz.py` = `../plan-pizzeria/calculadora_piz_es.py` traducida y adaptada (VPS)

Mismas hojas (`Dough` · `Food Cost` · `Instructions`), filas, helpers, `inject_cache` y autotest (pycel + caché = `calcular()`, 3 juegos). Cambios: (1) **masa en gramos** (decisión SPEC, como el azafrán de PAEL:
el oficio US trabaja en gramos y % panadero) con eco gris en oz (bola) y lb (masa y harina); (2) precios **$/lb** con constante gris «453.6 g per lb» y porciones de `Food Cost` en **oz** con «16 oz per lb» (el
gate prohíbe números tecleados en fórmulas); (3) `B5` «Sales tax included in your menu prices (%)» = **0 %** (menú US sin impuesto; misma fórmula); (4) bloque A «traditional Neapolitan ratios (EU TSG spec, also
used by the AVPN)», semáforo «Within / Outside…» y aviso fijo: en EE. UU. no hay norma sobre «Neapolitan-style» y cumplir las proporciones **no** da el «VPN-certified»; (5) 8 pizzas: Margherita $18 · Marinara $15
· Diavola $20 · Capricciosa $21 · Quattro Formaggi $21 · Ham & Mushroom $20 · Bufalina $23 · Sausage & Broccoli Rabe $22; ingredientes y caja ($0.75) = «Kit estimate (Oct 2026): replace with your distributor's
price»; (6) Letter, formatos sin «€», docProps D20. Gates: autotest VERDE · Margherita food cost 15-30 % · 0 español / no latinos / cifras ES / `RX_PIZ_NO`.

## 5. Checklist (D146) — las 80 tareas 12/15/14/13/13/13 del ES, mismas filas

Pestañas: «Phase 1 - Business Setup» · **«Phase 2 - Site, Hood & Permits»** (decisión SPEC frente a research: la instalación del horno es la F3 del ES) · «Phase 3 - Kitchen, Oven, Health» · «Phase 4 - Staff &
Safety» · «Phase 5 - Menu, Brand, Delivery» · «Phase 6 - Opening & 90 Days» (≤ 31). A1 «PIZZA SHOP STARTUP CHECKLIST»; `Instructions!A3` = nombre comercial. Equivalencias (se suman a BP §4.2, BP2 §3, Bar D60):

| ES | US |
|---|---|
| SL, SS/autónomo, IAE, Veri\*factu · urbanismo, licencia, terraza | LLC vs S corp with your CPA · EIN + state payroll/unemployment · business license + sales tax permit · POS that reports sales tax · zoning check before signing · building permit + CO · patio permit · **beer & wine license** (state ABC + local, often 3-12 months: lease contingency, M4 del Bar) |
| Salida de humos y ordenanza de leña · registro sanitario, gas, extintores, grasas | **NFPA 96 ch. 14** (dedicated exhaust, spark arrestor, UL 2162-listed oven, ash out daily, fuel away from the oven) + «ask the fire marshal in writing: hood? suppression? UL 2162 file number?» · plan review (8-201.11) + health permit + inspection · licensed gas contractor · Class K + 2-A · grease interceptor |
| Aceite irrellenable, Ley 1/2025, reclamaciones · convenio, PRL, manipuladores, alérgenos | TPHC written procedure (3-501.19) · cold holding ≤ 41 °F · required public notices · offer letters, I-9, W-4, state minimum wage · OSHA basics · CFPM (2-102.12) + food handler cards · **9 allergens incl. sesame** · no «gluten-free» promise |
| Riders, plataformas, envases, SGAE · nombre «napolitana» (ETG) | Own drivers = W-2 + hired & non-owned auto (check your state) · DoorDash/Uber Eats/Grubhub tiers · local packaging ordinances · ASCAP/BMI/SESAC · «Neapolitan-style» allowed; «VPN-certified» only after AVPN certification |

## 6. Docx (D147)

Las **131 ranuras del FT ES** (inv. §5); 61 traducidas-adaptadas desde el **Word ES de la pizzería** (`piz_a` §1-5 ‖ `piz_b` §6-10), un run por párrafo, **todas las cifras desde `cifras_caso.json`** (tokens D43 +
`inv_horno`, `inv_chimenea`, `inv_campana`, `inv_amasadora`, `inv_mesa_fria`, `lena_ano`, `plataforma_pct`, `comision_pct`, `bebida_pct`, `prime_cost_pct`; los de la calculadora solo si el ES los cita). Nota por
ranura = pista de research + la sección del Bar EN como forma cuando coincide. **El bloque D11 del ES (ETG y sus 3 reglamentos) no cruza**: «Neapolitan-style vs VPN-certified: what you can put on your menu»
(research §6.9). §9: permisos, plan review, NFPA 96, CFPM, TPHC, alérgenos, gluten-free, beer & wine + liquor liability, W-2 drivers, sales tax; **nota UK** en 108. FIJOS 35 «Appendices: … + Equivalents Guide»;
cierre = Pizza Shop Checklists Kit Pro · Food Cost Kit Pro · HACCP Food Safety Kit Pro · Restaurant Business Plan Kit.

## 7. Gates (D148), cifras y vocabulario (D149), revisión (D150)

- **D148**: G1-G9 (E1, E2, E4, E5 por nombre) · `RX_PIZ_NO` y cifras prohibidas 0 en los 4 · `bp8.py calculadora --autotest` · barrido · no latinos · `censo-entregables --fail --letter --only
  pizza-shop-business-plan` (alta en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9) · `verificar` · regresión de los 7 conjuntos · 2.ª pasada con sha256 canónico igual.
- **D149**: `cifras_prohibidas()` de `datos_pael.py`: `CIFRAS_ES` = importes ≥ 10.000 € de `../plan-pizzeria/cifras_caso_es.json` (los pequeños, solo con «€»), fuera los que coinciden con el caso US · `FRASES_ES`
  («66 covers», «19[.,]50», «14 pay», «33 %», «1[.,]221», «9[.,]3 %», plataforma 10 %) · caso del **Bar EN** (`_cifras_caso('../business-plans-en-3/cifras_caso.json', 'bar')` + «95 covers», «$27», «360 days») y
  REST/FT. `RX_PIZ_NO` = restos del Bar (`tapas|small plates|cocktails?|spirits|neighborhood bar|barback|last call|happy hour|draft beer system`) + del ES
  (`ETG|pliego|convenio|SMI|aut[oó]nomo|Veri\*?factu|\bIVA\b|SGAE|\bIAE\b|terraza|comensal`); «97/2010», «TSG» y «Napoletana» solo en la fila D19 del nombre, en la ranura de esa sección y en «Verace Pizza
  Napoletana».
- **D150 Una revisión opus** (tope 2 rondas, arreglos por texto): recalcular ventas, CAPEX con imprevistos de fórmula, equilibrio, holgura y DSCR · jerga · claims (VPN, gluten-free, alcohol, casa, «15-25 %») ·
  abrir Food Code 3-501.19 y 2-102.12, Oregon 15-01 y AVPN · unidades de la calculadora · **cero rastro de bar de tapas ni de España** · que el Word no prometa lo que el Excel no hace.

## 8. Capa de producto (D151-D153, F3) — duplicar la F3 de la Paella (`git show a9f3c3cf -- <fichero>`, 40 ficheros)

- **D151 Landing** `astro-site/src/data/productos-en/planes/pizza-shop-business-plan.ts` = `cp` de `bar-business-plan.ts`, SEO D133b, FAQ = las 8 de research §3 + canibalización (Pizza Shop Checklists = rutinas,
  Restaurant Plan, Food Truck) + UK/CA/AU; cifras MEDIDAS (ventas, CAPEX, caja, neto %, equilibrio; nada movible); **sin testimonios** (el ES no tiene); `omitGlobalApp`; imágenes `plan-pizzeria-*.jpg` del ES sin
  texto en español + `og-pizza-shop-business-plan.jpg` (recorte del hero).
- **D152 Registros**: páginas `en/digital-products/pizza-shop-business-plan{.astro,/access.astro,/library.astro}`, island `PizzaShopBusinessPlanLibraryIsland.tsx`, `src/pages/PizzaShopBusinessPlanDashboard.tsx`
  (claves `plan-negocio`, `plan-financiero`, `checklist-apertura`, `calculadora-masa`, `equivalents-guide`) · `tienda.ts` (FAMILIAS `plan-negocio-pizzeria`, es + en vivos) y **`plan-negocio-pizzeria.astro`**:
  `import { alternatesFamilia }`, `const hreflang = alternatesFamilia('plan-negocio-pizzeria')`, `locales={hreflang.locales}` + `alternates={hreflang.alternates}` (diff del paellero) · `zona-app.ts` ·
  `get-download-urls.ts` (4 + guía) · `verify-purchase.ts` · `resend-access.ts` · `admin-generate-access.ts` + `AdminGenerateAccess.tsx` · `product-prices.ts` (`sync-product-prices.py`) · `payment-links.ts` (tras
  el link) · `products-catalog.ts` (entrada ES: `name.en`, `urlByLang`, `priceByLang`) · config · changelog '1.0' · `linkify-use-case.{ts,tsx}` · **hub EN**: la tarjeta «Business Plan: Neapolitan Pizzeria» (→ ES,
  l. 607-621, de `3906cff9`) pasa a ser la del EN; `comingSoon` «Mobile Wood-Fired Pizza» se queda · `llms.txt`/`llms-full.txt` (27 → 28) · `sitemap-lastmod.json` · `footerLinks` de los 9 planes EN + Pizza Shop
  Checklists + Food Cost + HACCP · FAQ «Is there a plan for a pizza shop?» en Restaurant, Food Truck y Pizza Shop Checklists EN · `tienda-gate.py` · correo `broadcast-pizza-shop-business-plan-lanzamiento-en`.
- **D153** Gates F3: `sync-product-prices --check` · `tienda-gate` (+ `--es-identico`) · `robots`/`whatsapp`/`miselup`/`hub`/`carrusel-apps` · `gate-flujo-postpago --crypto-products all --crypto-exclude
  pro-prompts-ebook --only pizza-shop-business-plan` (preview y LIVE) · `fase6-gate.py <URL EN>`. **Payment Link: John** (USD 39, prosa sin viñetas, éxito →
  `/en/digital-products/pizza-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}`). **Correo EN 18-feb-2027 14:00Z** (CALENDARIO l. 732): borrador + prueba + routine ≥ 19-ene. Merge **después** del ES. No se tocan `robots.txt` ni el blog (carril Cursor).

## 9. Plan, presupuesto y riesgos (D154-D155)

| Paso (D154) | Quién | Tokens · reloj |
|---|---|---|
| 1a · **ya**, sin esperar al ES: rama `piz`, clones, caso, E5, tokens, `RX_PIZ_NO`, dry-run + D15 sobre el dry-run ES (en `/tmp` del VPS) ‖ 1b `calculadora_piz.py` + autotest | 1 opus ‖ 1 sonnet | 0,40 + 0,12 M · 45 min |
| 1c · sobre el ES FINAL: inv. §9 (`inventario_delta`, `extraer_textos/docx`, `mapas`, `preparar_tandas`) | orquestador | incl. · 10 min |
| 2 · Tanda 1: GPIZ-plan (≈ 200 cad., ≈ 3 K pal. + revisión GR) ‖ GPIZ-check (≈ 440, ≈ 3,3 K) | 2 sonnet | 0,20 M · 20 min |
| 3 · `aplicar_en` + D15 → `cifras_caso.json`; Tanda 2 `piz_a` ‖ `piz_b` (61 ranuras, ≈ 6,5 K pal.); `ensamblar_docx` | VPS + 2 sonnet | 0,22 M · 25 min |
| 4 · Gates D148 + revisión D150 + 1 ronda; `F2-NOTAS`; commit + push | VPS + 1 opus | 0,26 M · 30 min |
| 5-6 · F3: sonnet A (ficha, páginas, isla, dashboard) ‖ sonnet B (registros, hub, hreflang ES, enlaces, correo); OG, PR apilado, preview, gates, link, LIVE | 2 sonnet + orquestador | 0,60 M · 70 min |
| **Total F2 (≈ 1,2 M) + F3 (≈ 0,6 M)** | | **≈ 1,8 M · ≈ 3 h** + el link |

**Del ES terminado necesito** (antes de 1c): los 4 ficheros finales en `dl/plan-negocio-pizzeria/` (plan, checklist, **Word**, calculadora) tras su revisión Opus y su ronda,
`../plan-pizzeria/cifras_caso_es.json`, la decisión sobre «Campaña»/B16 (inv. §8) y la rama ES pusheada. Si el ES cambia tras 1c: re-extraer y `preparar_tandas` antes de los traductores. **D155 Riesgos**: (1)
**holgura justa** (≈ 15-16 % año 1 con rampa; imprevistos de fórmula y suplencias la bajan) → D15; (2) NFPA 96/AHJ: nunca prometer que sobra la campana; (3) claims VPN, gluten-free, alcohol, casa; (4) fuga del
Bar EN (propuestas con cifras y vocabulario de bar) → D149-D150; (5) la normalización comensal→cubierto puede casar mal → revisión GR; (6) canibalización con Restaurant Plan y Pizza Shop Checklists (la landing
diferencia). **NO se hace**: testimonios, anclas, ratings, licencias por estado, tip credit, reparto propio, cambiar filas/hojas/DV, research nueva, posts del blog, compra de prueba.
