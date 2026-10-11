# Bar Business Plan Kit (EN) — SPEC DELTA (F1 · 11-oct-2026 · sesión Claude Code)

> Producto 11 de la tienda EN: edición de `plan-negocio-tapas-bar` (35 €, v2.2). **Mandan `../business-plans-en/SPEC.md`
> (D1-D29, E1-E2, §2-§8) y `../business-plans-en-2/SPEC-delta.md` (D30-D47, E1-E4)**: aquí solo lo que cambia. Base:
> `F1-inventario-delta.md` (el Bar es gemelo estructural de la CAF, contenido cercano al REST) y `F1-research-us-delta.md`.
> Tamaño **M**; presupuesto F2 ≤ 1,5 M y F3 ≤ 1 M tokens; objetivo de calendario: producto listo para el Payment Link en
> 2 sesiones. Lo que no está aquí ni en las SPEC heredadas no se hace.

## 1. Producto (D48-D50)

| D | Tema | Decisión |
|---|---|---|
| D48 | Nombre y URLs | **Bar Business Plan Kit** · slug/productId `bar-business-plan` · JWT `bar-business-plan-jwt` · `/en/digital-products/bar-business-plan` (+ `/access`, `/library`) · gemelo ES (hreflang recíproco) `/plan-negocio-tapas-bar` · env `VITE_STRIPE_PAYMENT_LINK_BAR_BUSINESS_PLAN` |
| D48b | H1 · title · keywords | H1 Forma B: `Bar ` + oro `Business Plan` + «Template for a Neighborhood Bar with Small Plates: Word Plan + Excel Financial Projections + Opening Checklist». Title: «Bar Business Plan Template: Word + Excel Financial Projections + Opening Checklist \| AI Chef Pro». docProps keywords: bar business plan, bar business plan template, how to open a bar, bar startup costs, liquor license, AI Chef Pro |
| D49 | Precio, SIN anclas | **$39** pago único, acceso de por vida (regla de escalón: 35 € → $39). **Sin `priceOld`, sin «-70%», sin «Total value», sin «Save $», sin precio en los bonos** (John, 11-oct, FTC, toda la tienda EN). F3 aplica el MISMO patrón que deje el cambio de la tienda en `main`; si al llegar F3 la plantilla aún exige esos campos, se para y se pregunta al orquestador (no se inventa otro) |
| D50 | Ficheros (`dl/bar-business-plan/`) | `bar-business-plan.docx` «Bar Business Plan (10 Sections)» · `bar-financial-projections.xlsx` «Bar Financial Projections: 3-Year P&L, Cash Flow & Financing» · `bar-opening-checklist.xlsx` «Bar Opening Checklist (73 Tasks)». docProps D20; checklist `Instructions!A3` con el nombre comercial (I5) |

## 2. Concepto y caso (D51-D52)

| D | Tema | Decisión |
|---|---|---|
| D51 | Concepto | **Neighborhood bar with small plates**: bebida 65 / comida 35, 60 plazas (14 en barra) + patio, 7 días de tarde-noche; «small plates (tapas-style)» en docx y landing. Justificación: research §1 (demanda «bar», libro ES sin tocar, no canibaliza a Restaurant 70/30) |
| D52 | Caso US | Celdas de `F1-research-us-delta.md` §8 tal cual (95 guests × $27 × 360 ≈ $923K; alcohol 90 % de la bebida; préstamo CALIBRAR; 10 % a 10 años, interest-only 0). Regla D15 de BP y palanca de research §8. Cifras ES prohibidas en el EN (gate de cifras): 302.400, 153.327, 109.450, 174.317, 129.000, 50.000, 17.094, 115.000, 270.000, «34 clientes», «14 pagas», «33 %» de SS |

## 3. Libros (D53-D59)

| D | Tema | Decisión |
|---|---|---|
| D53 | Código | **Molde FT/CAF**: conjunto nuevo `bar` (`mapas.py` gana `elif CONJUNTO == 'bar'` → `business-plans-en-3/mapas_bar.py`, `instalar(M)` como `mapas_rp.py`) y lanzador `bp3.py` (copia de `bp2.py`). Pestañas plan = `_HOJAS_PLAN`; checklist = mapa CAFC salvo `F2 - Local` → **`Phase 2 - Location & Licenses`**. `MOLDE_CHECK 'hojas'`, `COL_OK 1`, `TAREAS_POR_FASE` 11/13/13/12/14/10, `FILA_VERSION` BARP 74 · BARC 11, `ZONAS_CELDA` BARP D18 34-50 · D19 53-69. Reutilización: GM de BP + las 136 de REST/CAF/PAN/FT por diccionario (`inventario_delta.json` → `reuso`) con marca «revisar contexto»; a traductores solo **GBAR** (263) y las 25 de D18/D19. Regresión: autotests y gates de FT/CAF **y** REST/PAN en verde |
| D54 | Inversión (filas 7-24, rótulos fijados) | 7 LLC formation + legal · **8 Liquor license + local permits (non-quota state example)** · 9 Architect, MEP drawings + permit fees · 10 Build-out (second-generation space) · 11 Electrical + HVAC · 12 Plumbing, grease interceptor + Type I hood · 13 Kitchen equipment (griddle, fryer, oven) · 14 Refrigeration (walk-in + back-bar coolers) · 15 Bar build (bar top + underbar stations) · 16 Draft beer system + installation · 17 Furniture (tables, high-tops + bar stools) · 18 Patio (furniture + awning) · 19 Glassware, smallwares + tableware · 20 Decor, lighting + sound · 21 Exterior signage · 22 Launch marketing · 23 Opening inventory (liquor, beer, wine + food) · 24 POS + handhelds + software. Nota fila 8: rango y cupo de research §4; licencia comprada = intangible, «ask your CPA». A2/A3 sin «España 2026»: «US kit example (2026) — replace with your own quotes» |
| D55 | P&L y Personal | A2 «Base case — neighborhood bar with small plates, 60 seats»; A10 «Food sales (small plates)»; A11 «Beverage sales (cocktails, beer, wine + non-alcoholic)»; fijos A22-A34 = los de research §8 (A33 «Music licensing (ASCAP/BMI/SESAC)», A34 «Safety + responsible-service training»). Puestos B5:B11: Owner / general manager · Kitchen lead · Bartenders (peak shifts) · Servers (floor & patio) · Line / prep cook · Barback / weekend extra · Relief cover (vacations + days off). `Personal!A2` = fórmula EN de FT/CAF (D11). Nota de propinas D38 en `Staffing`. Terminología: el libro dice **«covers»** como el REST (24 cadenas reutilizadas sin retocar); el docx y la landing, «guests (covers)» la primera vez |
| D56 | Umbrales (`PyG!E50, E52:E55`) | margen bruto ≥ 68 % · mercancía ≤ 28 % · personal ≤ 35 % · alquiler ≤ 10 % · neto ≥ 5 % (research §5), «kit benchmark (editable estimate)» |
| D57 | Impuestos del alcohol | `B62` 90 % · `B63`/`B40` 8 % con nota: «some states add a tax on drinks served on premises; e.g. Texas: 8.25% mixed beverage sales tax (customer) + 6.7% gross receipts tax (paid by the bar): put the first here and add the second to your beverage cost %» (research §6) |
| D58 | Tablas de `Instructions` | D18 (34-50) como BP D18: «WHY THIS MODEL IS BUILT THIS WAY», «Common shortcut \| This workbook \| Why», sin «v1.1». D19 (53-69) «US INDUSTRY BENCHMARKS», `Source` real o «Kit estimate» (nunca «Fichero v1.1», I3): pour cost total 18-24 % · beer 24 % · spirits 15 % · wine 28 % (BevSpot) · food cost 25-35 % · personal ≤ 35 % (kit) · alquiler ≤ 10 % (kit) · startup $110K-$550K leased / media $425,500 (RestaurantOwner vía Poster) · liquor license beer & wine ~$3,000 / full $12K-$400K · liquor liability ~$2,039/año small bars (Insureon) · ticket y rotaciones = kit estimate · fila 69 «Minimum wage floor: federal $7.25 + your state (DOL)». Ocupación, merma, «consumiciones de barra 35-45 %» y «retorno 18-30 meses» salen (sin fuente) → filas sustituidas por las de arriba |
| D59 | Fórmulas y excepciones | 17 fórmulas con texto: 14 derivadas de su gemela (`derivar_formulas.py` de BP2), **3 manuales** (`0. Supuestos!C50` sin «1,8 servicios del documento»: compara con el techo de `"Break-Even"`; `Inversión!D27` y `D37` con las listas de D54 en minúscula). Excepciones que admite el gate: **E1** aviso D21 (BARP `Instructions!A75`, BARC `A12`) · **E2** `3-Year P&L!G13,G14` → `$B$41` · **E4** `Staffing!C12` → `SUMPRODUCT(B5:B11,C5:C11)`. Sin E3 |

## 4. Checklist (D60) — mismas 73 tareas y fases; equivalencias propias (se suman a BP §4.2 y BP2 §3, que mandan)

| Fila ES | US |
|---|---|
| F1-5 «Elegir forma jurídica (SL recomendada)» · F1-9 «Alta SS (autónomo + empresa)» | LLC vs S corp with your accountant · EIN + state payroll / unemployment registration |
| F1-15 «Veri*factu» (reuso REST) | POS that reports sales tax correctly (reuso) |
| **F2-8 «Licencia de actividad CLASIFICADA» (2-4 meses)** | **Liquor license: apply right after signing the lease** (state alcohol agency + local approval; quota states: buy/transfer an existing license); «often 3-12 months»; responsable Owner + attorney (lección M1 de BP2) |
| F2-7 «Verificar uso urbanístico» · F3-5 «Proyecto técnico actividad clasificada» | Zoning check before signing · architect + MEP drawings → building permits + health department plan review |
| F2-9 Terraza · F2-10 Música ambiente · F2-13 Medición acústica | Sidewalk café / patio permit · entertainment permit if live music or DJ · noise ordinance check (residential neighbors) |
| F2-11 Seguro RC · F2-12 Multirriesgo | General liability **+ liquor liability (dram shop)** · property / BOP |
| F3-8 Salida de humos · F3-9 Trampa de grasas · F3-11 Grifos | Type I hood + UL 300 suppression (NFPA 96) · grease interceptor (plumbing review) · draft system: distributor install (lines, glycol); tied-house rules limit what a brewer can give you free [estimado] |
| F4-8 Contratos (convenio provincial) · F4-9 Alta SS · F4-11 PRL | Offer letters, I-9, W-4; state minimum wage · new-hire reporting · OSHA basics |
| F4-13 Formación servicio y barra · F4-14 Alérgenos + APPCC | Bar service **+ responsible beverage service certification (TIPS / ServSafe Alcohol)** · allergen + food safety (Food Code); age-ID checks |
| F5-13 Acuerdos proveedores (exclusividad por grifos gratis) | Distributor accounts (beer, wine, spirits) — three-tier system: you buy from licensed distributors |
| F5-14 TripAdvisor, TheFork · F6-12 Glovo, Uber Eats | Google, Yelp, OpenTable/Resy · DoorDash / Uber Eats only for food (alcohol delivery depends on state law) |

## 5. Docx (D61)

D22/D23 tal cual: 133 párrafos, 10 Heading 1 en 37 · 45 · 52 · 60 · 69 · 79 · 86 · 96 · 104 · 111, un run por párrafo,
**todas las cifras desde `cifras_caso.json`** (tokens D43 + los del Bar: `clientes_*` con rótulo «Cubiertos…», `inv_licencia`,
`inv_grifos`, `inv_cocina`, `inv_frio`, `bebida_pct`, `prime_cost_pct`). Fuera los defectos I1-BAR del inventario §5.
§2 concepto small plates + barra; §3 mercado con las fuentes de research §4-§5 (sin cifras de mercado sin fuente);
§6 operaciones con pour cost y control de inventario de barra; §7 personal (bartenders, barback, sin tip credit); §9:
liquor license (estatal + local, cupo, plazos), dram shop / liquor liability, servicio responsable, health permit + plan
review, building permits + CO, hood / grease, música (ASCAP/BMI/SESAC + permiso de entretenimiento), horario y last call
según ley local, párrafo UK (premises + personal licence, FHRS). Cierre: los 4 productos EN de D23. Tandas: **bar_a** §1-5
(≈ 3,56 K palabras) y **bar_b** §6-10 (≈ 3,15 K).

## 6. Capa de producto (D62-D65, F3)

| D | Tema | Decisión |
|---|---|---|
| D62 | Landing | `data/productos-en/planes/bar-business-plan.ts` = duplicado de `restaurant-business-plan.ts` (misma plantilla `PlanNegocioLandingPage.astro` con `lang`), copy del Bar; imágenes del ES (`plan-tapas-bar-*`). Tarjeta DOCX la primera del grid. Bonos (sin precio): 1 «Bar Licensing & Liquor License Guide (US + UK notes)» = §9 + fases 1, 2 y 6; 2 «US Bar Industry Benchmarks (sourced)» = §3 + D19; la tarjeta «Ratios de Referencia» se funde con «Instructions» (sin doble cómputo). FAQ = research §3 (8). Sin `aggregateRating` ni `review`; `omitGlobalApp`. Testimonios D26 tal cual («…Spanish edition») — riesgo §8 |
| D63 | Registros | Las fuentes donde vive Restaurant EN (lista de `git grep restaurant-business-plan`): `tienda.ts` (familia planes, `en.vivo`), `zona-app.ts`, `product-prices.ts` (USD 39), `payment-links.ts`, `get-download-urls.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts` + `AdminGenerateAccess.tsx`, dashboard (`*LibraryIsland.tsx` + página SPA), `products-catalog.ts` (`urlByLang`), `productos-digitales-config.ts`, changelog, `linkify-use-case`, `llms.txt` + `llms-full.txt` (y el recuento del hub), `sitemap-lastmod.json`, `censo-entregables.py` (`PRODUCTOS_LETTER`), `postprocess-transversal.py` (`EXCLUIDOS`). Tres puertas cripto (`/en/crypto-payment` ya existe). hreflang en la página ES `plan-negocio-tapas-bar.astro` (`tienda-gate --es-identico`) |
| D64 | Interenlazado | Entrantes: tarjeta en el hub EN, `footerLinks` de los 4 planes EN y del Financial Plan Kit, FAQ «bar» de la landing Restaurant → Bar (sin tocar sus ficheros), catálogo, banners del blog EN, hreflang. Salientes: Restaurant (hermano), Financial Plan Kit, Inventory Kit (stock de barra), Staff Scheduling, Food Cost. Posts EN propuestos aparte (bridge.py, fuera de presupuesto): «liquor liability insurance» (1.900), «how much does it cost to open a bar» (720) |
| D65 | Correo EN | **19-nov 14:00Z** (siguiente hueco EN de `CALENDARIO-V2-SEMANAL.md` l. 277; programable desde el 20-oct por el tope de 30 días de Resend); ningún ES ese día (ES siguiente 23-nov) |

## 7. Plan de F2 y F3 (máx. 2 Sonnet a la vez; Mac redacta, VPS genera y pasa gates)

1. **Implementador opus (VPS)**: `mapas_bar.py` + `bp3.py` + rama `bar` en `mapas.py`; `datos_bar.py` (VALORES_EN de
   research §8, FIJOS D34-like, POR_CELDA de D18/D19, FORMULAS_EN 14 + 3, PARCHES E2/E4); `extraer_textos` /
   `extraer_docx` / `preparar_tandas` con el diccionario de reutilización. ≈ 0,5 M.
2. **Tanda 1 (Sonnet ‖ Sonnet)**: `GBAR-plan` (153 cadenas, 2,8 K palabras + 25 de D18/D19) ‖ `GBAR-check` (109, 0,65 K
   + revisión de las 136 reutilizadas). `BRIEF-TRADUCTORES.md` de BP2 + este delta. ≈ 0,25 M.
3. `aplicar_en.py` + calibración D15 → `cifras_caso.json` (VPS). **Tanda 2 (Sonnet ‖ Sonnet)**: docx `bar_a` ‖ `bar_b`
   (≈ 3,5 K + 3,2 K). ≈ 0,3 M. `ensamblar_docx.py` (VPS).
4. Gates G1-G9 (E1, E2, E4 por nombre) + barrido de no latinos + gate de cifras ES prohibidas (D52) + `censo-entregables`.
   **Una** revisión adversarial opus (prestamista/CPA que recalcula + técnica de ficheros), tope 2 rondas. ≈ 0,3 M.
5. **F3** (opus, worktree): D62-D65 + gates F3 de BP §8 (`tienda-gate`, `robots-gate`, `whatsapp-gate`, `miselup-gate`,
   `gate-flujo-postpago --only bar-business-plan` LIVE tras el Payment Link). ≈ 0,8 M.

Total estimado F2 + F3 ≈ **2,1 M** (techo M: 5 M; +30 % sobre 2,5 M → se para y se reporta).

## 8. Riesgos y lo que NO se hace

1. **Licencia de alcohol**: $15,000 es un ejemplo de estado sin cupo; con cupo el CAPEX cambia un orden de magnitud
   (Boston > $450,000). Va en la nota de la fila 8, en §9 y en una FAQ, nunca como coste típico nacional.
2. **Caso optimista si se lee mal**: EBITDA ≈ 18-19 % con bebida al 22 %. Si la calibración lo sube de ~20 %, F2 baja
   antes volumen que ticket y lo anota; el docx explica que el pour cost manda.
3. **Testimonios ES** (D26) con «63 trámites», «break-even de 34 clientes», «préstamo ICO»: contradicen el kit EN
   (73 tareas; equilibrio del caso US). Riesgo heredado y aceptado por John en D26; se anota en F3.
4. **Regresión**: tocar `mapas.py` para un tercer conjunto no puede romper FT/CAF ni REST/PAN (correr sus autotests y G1-G9).
5. Fuentes leídas como resumen (NAICS 722410, campana/grasas de BP2): la revisión final las abre antes de que una cifra
   suya llegue al docx; si no se confirman, redacción cualitativa.

**NO se hace**: precios tachados ni anclas (D49); reseñas o ratings; cifras de licencia por estado; modelar tip credit,
propinas o el gross receipts tax como fórmula; cambiar la estructura del libro (filas, hojas, DV); tocar los ficheros
del Restaurant EN; nightclub / brewery; posts del blog dentro de este presupuesto; compra de prueba (verificación por
acceso admin + gates LIVE).
