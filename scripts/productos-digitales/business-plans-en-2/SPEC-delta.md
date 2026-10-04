# Restaurant Business Plan Kit + Bakery Business Plan Kit (EN) — SPEC DELTA (F1 · 4-oct-2026 · sesión Claude Code)

> Productos 9 y 10 de la tienda EN: ediciones de `plan-negocio-bar-restaurante` y `plan-negocio-panaderia` (35 €, v2.2,
> motor `planes-v2_0`). **Manda `../business-plans-en/SPEC.md` (D1-D29, E1-E2, §2-§8)**: aquí solo lo que cambia. Base:
> `F1-inventario-delta.md` (estructura, cadenas, defectos) y `F1-research-us-delta.md` (demanda, cifras, caso US). Lo que
> no está aquí ni en la SPEC heredada no se hace. Tamaño **M** cada uno; F2 + F3 de los dos ≤ 4 M.

## 1. Productos (D30-D32)

| | Restaurant | Bakery |
|---|---|---|
| Nombre (D30) | **Restaurant Business Plan Kit** | **Bakery Business Plan Kit** |
| Slug · productId · JWT | `restaurant-business-plan` · ídem · `restaurant-business-plan-jwt` | `bakery-business-plan` · ídem · `bakery-business-plan-jwt` |
| Gemelo ES (hreflang) | `/plan-negocio-bar-restaurante` | `/plan-negocio-panaderia` |
| Env Stripe | `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN` | `VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN` |
| H1 Forma B | `Restaurant ` + oro `Business Plan` + «Template for a Casual Restaurant & Bar: Word Plan + Excel Financial Projections + Opening Checklist» | `Bakery ` + oro `Business Plan` + «Template for a Retail & Wholesale Bakery: Word Plan + Excel Financial Projections + Opening Checklist» |
| Title | «Restaurant Business Plan Template: Word + Excel Financial Projections + Opening Checklist (Restaurant & Bar) \| AI Chef Pro» | «Bakery Business Plan Template: Word + Excel Financial Projections + Opening Checklist \| AI Chef Pro» |
| Keywords (docProps) | restaurant business plan, restaurant business plan template, bar business plan, restaurant startup costs, how to open a restaurant, AI Chef Pro | bakery business plan, bakery business plan template, how to start a bakery business, bakery startup costs, AI Chef Pro |

- **D30**: la keyword de cabeza entera en slug y H1 (2.400 y 1.900/mes). «bar business plan» (1.900) entra solo como
  «Restaurant & Bar» en subtítulo, title y FAQ: el producto es un restaurante con barra, no un plan de bar de copas. El
  concepto del PAN se describe como «artisan bakery with a storefront, a small café corner and wholesale to cafés».
- **D31 Precio y anclas** (regla de `product-prices.ts`: escalón USD inmediatamente superior): **$39** pago único,
  acceso de por vida. `priceOld` **$129** (120 €); bonos **$29** cada uno (19 €); «Total value: $187 — business plan kit
  ($129) + 2 bonuses ($58)»; ahorro **$90**; «-70%» en hero y buyBox. Idéntico a FT/CAF: los 4 planes EN cuestan lo mismo.
- **D32 Ficheros** (en `dl/<slug>/`; docProps D20; checklist `Instructions!A3` con el nombre comercial):

| ES | EN | Título EN |
|---|---|---|
| `plan-de-negocio-bar-restaurante.docx` | `restaurant-business-plan.docx` | Restaurant Business Plan (10 Sections) |
| `plan-financiero-bar-restaurante.xlsx` | `restaurant-financial-projections.xlsx` | Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing |
| `checklist-apertura-bar-restaurante.xlsx` | `restaurant-opening-checklist.xlsx` | Restaurant Opening Checklist (64 Tasks) |
| `plan-de-negocio-panaderia.docx` | `bakery-business-plan.docx` | Bakery Business Plan (10 Sections) |
| `plan-financiero-panaderia.xlsx` | `bakery-financial-projections.xlsx` | Bakery Financial Projections: 3-Year P&L, Cash Flow & Financing |
| `checklist-apertura-panaderia.xlsx` | `bakery-opening-checklist.xlsx` | Bakery Opening Checklist (66 Tasks) |

## 2. Decisiones nuevas

| D | Tema | Decisión |
|---|---|---|
| D33 | Pestañas | RESTP **conserva la numeración** del ES: `0. Assumptions` · `1. Startup Costs` · `2. 3-Year P&L` · `3. Break-Even` · `4. Scenarios` · `5. Staffing` · `6. 12-Month Cash Flow` · `7. Financing` · `Instructions`. RESTC: `Checklist Apertura` → `Opening Checklist`. PANP = mapa de FT/CAF. PANC `F1`…`F6` → `Phase 1 - Business Setup` · `Phase 2 - Location & Permits` · `Phase 3 - Equipment` · `Phase 4 - Staff` · `Phase 5 - Marketing` · `Phase 6 - First 90 Days`. Referencias de fórmulas, DV y CF reescritas en el mismo paso (D6) |
| D34 | Marca en el xlsx REST | Las celdas «ChefBusiness Consultoría Gastronómica» (A1 de 5 hojas, RESTC A1) → «AI Chef Pro»; «ChefBusiness.co — Plan de Negocio: Bar-Restaurante» (pie en celda de 5 hojas, RESTC A76) → «AI Chef Pro · aichef.pro/en/digital-products/restaurant-business-plan»; A2/A3 de cada hoja → títulos EN sin «España 2026». `Inversión!A57` → «NOTE: all amounts are US kit-example estimates (2026); replace them with your own quotes.» Van en `FIJOS` (mismas celdas y merges; no es excepción estructural). Misma razón que D23 |
| D35 | Molde de RESTC | Se duplica tal cual: una hoja, 7 fases como filas-cabecera fusionadas (10/8/8/7/8/15/8 = 64), categoría en la col. A, OK en la col. E. **La DV `✓,—,N/A` se conserva**; el EN de `Instructions!A5` describe lo que hay («✓ done, — pending, N/A not applicable»): se corrige I8 en el texto, no en la estructura. Categorías: Legal · Tax · Payroll · Premises · Permits · Build-out · Equipment · Food safety · HR · Brand · Digital · Launch · Insurance · Privacy · Operations · Finance · Marketing. G1 cuenta tareas por fila-cabecera |
| D36 | PAN: pan exento (E3) | La col. H del P&L pasa de «pan común al 4 %» a la parte **exenta** del sales tax: `H4` «Tax-exempt share of the line (%)» (bakery goods to go + wholesale for resale); **`G10`: literal `0.04` → `0`**, resto idéntico; `H10` = **0.80** [kit example]; nota en F10: CA exime la bollería para llevar y grava el consumo en el local (regla 80/80); la venta a un café que revende va con resale certificate; UK: zero-rated para llevar, 20 % en el local. `G13` (soportado de compras) entra en E2 → `$B$41`. Solo afecta a la tesorería (P&L excl. tax) |
| D37 | Alcohol (REST) | Alcohol sobre bebida **0.70**; `B63` (en sala) y `B40` (para llevar) **8 %** como D9, con nota: algunos estados y ciudades añaden un impuesto por consumición al sales tax → teclear el tipo combinado en B63. Fila de inversión «Liquor license + permits (non-quota state example)» $15,000, con la nota «from $50 to $300,000+; in quota states you buy an existing license» [fuente research §3]. Seguro con liquor liability (en «Insurance»). PAN: alcohol 0 % y la fila B63 «…served at the counter» se traduce sin más |
| D38 | Propinas (REST) | El libro no modela propinas ni tip credit: servers y bartenders a **≥ $15/h** de salario base. Nota en `Staffing`: federal $2.13/h + tip credit hasta $5.12 donde el estado lo permite; CA, OR, WA, AK, MN, MT y NV no lo permiten (DOL). Así ningún sueldo sale bajo el suelo (D15) y el coste es prudente |
| D39 | Cottage food (PAN) | El kit es para obrador **comercial** con tienda y mayorista. «cottage food law» (8.100/mes) es otro comprador: el docx §9, una FAQ y la nota de `Phase 1` explican la diferencia y remiten a la licencia de cocina comercial (health department o departamento de agricultura según el estado; FDA registration solo si lo mayorista domina). Post EN «cottage food law» con bridge.py: propuesta aparte, fuera de este presupuesto |
| D40 | Préstamo y vidas | Plazo **10 años** en los dos (SBA 7(a) para equipo y obra; precedente CAF), interest-only 0 (D17), tipo 10 %; vidas obra 10 / equipo 7 (D12). DSCR 1.15 / 1.25 (D13) en `B65:B66` |
| D41 | Umbrales del P&L (D16) | REST `E53,E55:E58`: margen bruto ≥ 65 %, mercancía ≤ 32 %, personal ≤ 35 %, alquiler ≤ 10 %, neto ≥ 5 %. PAN `E51,E53:E56`: ≥ 60 %, ≤ 33 %, ≤ 38 %, ≤ 10 %, ≥ 5 %. Origen «kit benchmark (editable estimate)» con prime cost 60-65 % y bakery 28-35 % / 24-40 % (research §4) |
| D42 | Caso de ejemplo | `F1-research-us-delta.md` §7 (REST 125 cubiertos × $28 × 310 ≈ $1,085,000; PAN 210 × $10 × 310 ≈ $651,000), con la regla de calibración de ese apartado y las exigencias D15. Préstamo `CALIBRAR` como en FT/CAF |
| D43 | Tokens del docx | `TOKENS_DOCX` gana claves `rest`/`pan` en los rótulos por plan (`clientes_*` → «Cubiertos…» / «Transacciones…», PE, Escenarios, `marketing_anual` PAN = «Marketing», `ocupacion_*` como CAF); `aforo`/`rotaciones_dia` solo REST; `inv_*` propios (REST: obra, cocina, campana, barra, sala, licencias; PAN: horno, amasadora, fermentación, vitrina, obra, electricidad). En el docx EN se habla de «covers» (REST) y «transactions» (PAN) |
| D44 | Docx | D22/D23 tal cual. REST 148 párrafos, PAN 131; encabezados en los índices del inventario §0; sin movimientos (no hay I7). Cierre: REST tiene 4 líneas de producto (143-146) → los 4 productos de D23, uno por línea; PAN 2 (128-129) → dos por línea. §9 REST: marco federal/estatal/ciudad · health plan review + permit · building permits + certificate of occupancy · hood/UL 300/NFPA 96 + grease interceptor + fire marshal · **liquor license** (estatal + local, cupo, liquor liability, servicio responsable) · empleo (propinas D38) · alérgenos, consumer advisory y seguros · último párrafo UK (premises + personal licence, FHRS). §9 PAN: cottage food vs comercial · health dept / agricultura · plan review, ventilación y gas · sales tax exento para llevar y resale certificate · FDA registration y etiquetado mayorista · seguros · UK (zero-rated, registro 28 días) |
| D45 | Landing (§3) | Plantilla `PlanNegocioLandingPage.astro` con `lang`, como FT/CAF. REST: tarjeta DOCX la primera del grid (hoy la landing ES no vende el Word: igual que A7). Bonos: **1 «Restaurant Permits & Licenses Guide (US + UK notes, liquor license included)»** = §9 + fases 1, 2 y 6 del checklist; **2 «US Market Data & Industry Benchmarks (sourced)»** = §3 del docx + tabla D19. PAN: bono 1 «Bakery Permits & Licenses Guide (commercial vs cottage food, US + UK notes)», bono 2 «Bakery Industry Benchmarks (sourced)»; la tarjeta «Ratios de Referencia» del grid se funde con «Instructions» (si no, doble cómputo con el bono 2) |
| D46 | Correos EN | REST **9-nov 14:00Z** (programable desde el 10-oct), PAN **14-nov 14:00Z** (desde el 15-oct): cola EN +5 días tras Coffee Shop 4-nov. Los ES de esa semana van el 8-nov y el 13-nov a las 08:00Z (`CALENDARIO-V2-SEMANAL.md` l. 217-243): ningún día compartido. Si la F3 se retrasa, se corre la cola |
| D47 | Interenlazado (D29) | Entrantes: tarjeta viva en el hub EN, `footerLinks` de los otros 3 planes EN y del Financial Plan Kit, catálogo `urlByLang`, banners del blog EN, hreflang recíproco con los 2 gemelos ES. Salientes: Financial Plan Kit, HACCP, Staff Scheduling y los planes hermanos (FT ↔ CAF ↔ REST ↔ PAN). Posts EN propuestos aparte: «cottage food law» (8.100) y «liquor license cost» (880) |

### 2.1 Excepciones estructurales (amplían §1.1 de la SPEC heredada; el gate admite solo estas)

- **E1** · la celda del aviso D21 bajo la versión en los 4 libros (RESTP `Instructions!A64`, PANP `A73`, RESTC y PANC `A12`).
- **E2** · REST `2. 3-Year P&L!G14,G15`; PAN `3-Year P&L!G13,G14` → `'0. Assumptions'!$B$41`.
- **E3** · PAN `3-Year P&L!G10`: `0.04` → `0` (D36). Total: 2 fórmulas en REST y 3 en PAN; el resto, idénticas al ES.

## 3. Checklists: equivalencias propias (se suman a la tabla §4.2 heredada, que manda)

| ES (REST / PAN) | US |
|---|---|
| SL con capital de 1 € (Ley 18/2022); certificación negativa de denominación | LLC; business name availability search + DBA if trading under another name |
| Escritura ante notario; inscripción en el Registro Mercantil; alta de autónomos de los socios | Articles of organization (Secretary of State); operating agreement; owners' draws and self-employment tax (accountant) |
| Proyecto técnico de actividad; licencia de obras; boletines eléctrico y de gas | Architect + MEP drawings; building, electrical, plumbing and gas permits with final inspections |
| Declaración responsable / licencia de actividad (PAN: «clasificada», horno) | Zoning check (retail bakery / light food manufacturing use) → certificate of occupancy |
| Instalación de cocina: extracción, gas (REST) · salida de humos y potencia 30-40 kW (PAN) | Type I hood + UL 300 suppression (NFPA 96) · oven ventilation permit · utility service upgrade (3-phase) with the utility |
| Registro Sanitario autonómico (RGSEAA no aplica al minorista) | Health department plan review → food establishment permit (PAN: or state agriculture license if wholesale; FDA facility registration only if mostly wholesale) |
| Licencia de terraza (REST) | Sidewalk café / outdoor dining permit |
| Cartel de prohibición de venta de alcohol a menores (REST) | **Liquor license** (state ABC + local approval; quota states: license transfer) + responsible beverage service training + age signage |
| Hojas de reclamaciones | REST: consumer advisory and allergen notice on the menu · PAN: ingredient and allergen labels for packaged and wholesale products |
| Plan de prevención del desperdicio alimentario (Ley 1/2025, REST) | Food donation program (Bill Emerson Good Samaritan Act protects donors) + local organics recycling rules where they exist [estimado] |
| Comunicación de apertura del centro de trabajo | State new-employer registration + required federal and state labor law posters |
| Marca OEPM (PAN, opcional) | USPTO trademark (optional) |
| InfoJobs, Indeed (REST) | Indeed, Culinary Agents, Poached |

## 4. Afirmaciones de las fichas ES que NO pasan al EN (revisadas contra los ficheros)

| # | Ficha | Afirmación ES | Realidad | EN |
|---|---|---|---|---|
| R1 | REST | «~80K-150K EUR», «~133K EUR de referencia» (hero, grid, buyBox) | Excel: 179.015 € de inversión; 133 K es la cifra del docx v1.1 | Cifra del xlsx EN + rango US con fuente |
| R2 | REST | Bono 1 «Cuadro de Personal con Seg. Social» | Es la hoja `Personal`, ya en el grid (doble cómputo, como A11) | Bono 1 = Permits & Licenses Guide (D45) |
| R3 | REST | Bono 2 / grid «Análisis de Mercado España 2026: 81K+ restaurantes, ticket por comunidad, tasa de cierre en 3 años» | No es un fichero; la tabla D19 da cierre 25 %/50 % con fuente «Fichero v1.1» | Bono 2 = §3 + D19 con fuentes; sin tasa de cierre salvo con fuente |
| R4 | REST | «Plan de Financiación: ICO, ENISA… con orden recomendado de gestión» | El orden no existe (A10); ICO/ENISA = ES | SBA 7(a) / Microloan, «lender-ready, approval not guaranteed» |
| R5 | REST | «Cuadro… jefe de sala, cocineros» | Los 7 puestos del libro no incluyen jefe de sala | Puestos reales del libro EN |
| R6 | REST/PAN | «SS 33 %, 14 pagas», «Datos reales España 2026», «licencia clasificada», «RGSEAA», «Registro Sanitario + 66 trámites» | Mercado ES | D11, research §4-§5, permisos US |
| R7 | PAN | «Plan de financiación con ICO, ENISA, **leasing de horno** y subvenciones» | El libro no tiene leasing | Sin leasing; SBA y equipment financing solo como mención en el docx |
| R8 | PAN | «Canal mayorista» como si fuera un canal modelado; escenarios «con mix barra/bollería/cafetería» | El mayorista va dentro de la línea de pan (fila 10); los escenarios mueven volumen, ticket y días, no el mix | «retail + wholesale in one bakery line with a tax-exempt share»; escenarios: transactions, ticket, days |
| R9 | PAN | Bono 2 «Ratios de Referencia» + tarjeta «Ratios de Referencia Panadería» | La misma tabla dos veces; fuente «Versión anterior de este kit» | D45 |
| R10 | REST/PAN | `aggregateRating` 4,9; badge «El plan de negocio más completo…»; «737 fórmulas» | Capa ES; superlativo; recuento ES | Fuera (A12-A13); recuento EN en F2 |
| R11 | REST/PAN | Docx v1.1 (§4 del inventario: 133 K/350 K/40 cubiertos; 105 K/200 K/114 transacciones) | Contradice al Excel | D22: cifras del xlsx EN |
| R12 | REST/PAN | Testimonios: «financiación en 10 días», «Seg. Social al 33,4 % y 14 pagas» (REST); «65K EUR con leasing del horno», «RGSEAA», «break-even por kilos de pan», «plus nocturnidad», «merma 3-5 %, materia prima 22-28 %» (PAN) | Nada de eso está en el producto | D26 (se traducen tal cual por decisión de John) — **riesgo** anotado; si John lo pide, se eligen otros |

## 5. Plan de F2 y F3 (reutiliza `../business-plans-en/`; un implementador opus por fase, Sonnet para textos)

**Requisito previo**: `feat/business-plans-en` cerrada (FT/CAF con `aplicar_en.py` y gates en verde) y esta rama
rebasada sobre ella. No se toca su código mientras otro agente lo termina.

1. **Generalizar a 4 planes** (opus, VPS): `mapas.py` → `PLANES` + `rest`/`pan`; `LIBROS` + RESTP/RESTC/PANP/PANC;
   `HOJAS_POR_LIBRO` por libro (D33) y un `norm_hoja()` en todo lo que hoy usa `_P/_I/_E/_T/_F/_R/_ES`; `TAREAS_POR_FASE`
   por fila-cabecera para RESTC; `PARCHES_FORMULA` (E2 en sus celdas + E3); `FORMULAS_EN` +32 celdas (copiando la
   redacción de `formulas_en.py`); `VALORES_EN` (D42); `FIJOS` (D34, D35 A5); `FILA_VERSION` (63/72/11/11);
   `ZONAS_CELDA` por cabecera (REST D18 34-45, D19 49-58; PAN 35-51, 55-67); `TOKENS_DOCX` (D43); `DOCX_ENCABEZADOS` /
   `DOCX_INDICE` / `DOCX_FIJOS` / `DOCX_TANDAS` por plan. `extraer_textos.py`: las cadenas ya traducidas (GM y las 85
   reutilizables de GFT/GCAF) no van a los traductores; entran del diccionario con marca «revisar contexto».
   `aplicar_en.py`, `gates_en.py`, `ensamblar_docx.py`, `check_textos.py` y `preparar_tandas.py`: parametrizados por
   plan, con los autotests de FT/CAF en verde además de los nuevos (RESTC de una hoja, E3).
2. **Textos** (Sonnet, 2 a la vez, `istats` < 62 °C): **GREST** (344 + 6 GN, ≈ 3,0 K palabras) ‖ **GPAN** (340, ≈ 4,8 K)
   con `BRIEF-TRADUCTORES.md` + este delta + research delta §5/§7. Después `aplicar_en.py` + calibración D42 →
   `cifras_caso.json` → docx **rest_a** (§1-5, ≈ 3,2 K) ‖ **rest_b** (§6-10, ≈ 3,5 K) y **pan_a** (≈ 3,3 K) ‖ **pan_b**
   (≈ 3,5 K). Seis tandas en total.
3. **Una revisión adversarial** (opus: prestamista/CPA que recalcula + técnica de ficheros), tope 2 rondas; G1-G9 de la
   SPEC heredada sobre los 4 libros nuevos, con E1-E3 por nombre. Los 2 slugs en `EXCLUIDOS` de
   `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de `censo-entregables.py`.
4. **F3** (opus, worktree, réplica de FT/CAF): `data/productos-en/planes/<slug>.ts` (§4 + D45), 3 páginas anidadas,
   dashboard (3 descargas), familias con `en.vivo` en `tienda.ts`, `zona-app.ts`, las 5 fuentes del backend `lang: 'en'`,
   `product-prices.ts` USD 39, tres puertas cripto, hreflang en las 2 landings ES (`tienda-gate --es-identico`), hub,
   catálogo, `footerLinks`, correos D46. Gates F3 de la SPEC heredada §8.

**Presupuesto**: F1 ≈ 0,35 M (esta) · F2 ≤ 2,5 M · F3 ≤ 1,5 M (los dos productos). +30 % → se para y se reporta.

## 6. Riesgos

1. **Generalizar sin romper FT/CAF**: el molde de pestañas numeradas y el checklist de una hoja tocan funciones comunes;
   los autotests y gates de FT/CAF deben seguir en verde tras el cambio (correr los 4 libros viejos también).
2. **Calibración REST**: con salarios US sin tip credit el margen es estrecho; la holgura de caja del caso estimado
   (~20 %) depende del volumen. Si para cumplir D15 hiciera falta pasar de 130 cubiertos (2,2 rotaciones), revisar
   alquiler y plantilla antes que el ticket, y anotarlo.
3. **E3 es fiscalidad estatal**: «exento para llevar» no vale en todos los estados (algunos gravan la comida a tipo
   reducido). El rótulo y la nota dicen «check your state»; H10 es editable y con 0 el libro grava todo.
4. **Licencia de alcohol**: $15,000 es un ejemplo de estado sin cupo; en estados con cupo cambia el CAPEX en un orden de
   magnitud. Va en la nota de la fila, en §9 y en una FAQ, para que nadie lo lea como coste típico nacional.
5. Testimonios ES con cifras y trámites que el producto no tiene (R12), heredado de D26.
6. Fuentes de §3 leídas como resumen de búsqueda (cloudkitchens, rotorooter, CDTFA, FDA): la revisión final las abre
   antes de que una cifra suya llegue al docx; si no se confirma, redacción cualitativa.
