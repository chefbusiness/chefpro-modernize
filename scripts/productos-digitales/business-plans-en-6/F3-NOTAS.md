# BBQ Catering Business Plan Kit (EN, $39) — F3-NOTAS (24-oct-2026 · sesión Claude Code)

> F3 = producto y lanzamiento (SPEC-delta §8, D112), duplicado del Mobile Bar (PR #128, `541eb6f3` + `49dc3d4a` +
> `ab277f04`). Rama `feat/bbq-catering-business-plan-en-f3` (sale de `8306a165`); la F2 va en paralelo en
> `feat/bbq-catering-business-plan-en`. Sin builds ni navegador (Mac, regla térmica): verificado con esbuild, grep y
> gates estáticos.

## 1. Puntos y estado

| Punto | Estado | Dónde |
|---|---|---|
| Ficha EN (PlanNegocioLandingPage, carrusel y 3 puertas cripto heredados, $39 sin anclas, sin rating) | ✅ | `astro-site/src/data/productos-en/planes/bbq-catering-business-plan.ts` |
| Landing + `/access` + `/library`, island y dashboard (claves = ES y mobile bar + `equivalents-guide`) | ✅ | `pages/en/digital-products/bbq-catering-business-plan{.astro,/access.astro,/library.astro}` · `islands/library/BbqCateringBusinessPlanLibraryIsland.tsx` · `src/pages/BbqCateringBusinessPlanDashboard.tsx` |
| `tienda.ts` FAMILIAS (`vivo: true`) · `zona-app.ts` · linkify (Astro y SPA) · `sitemap-lastmod.json` | ✅ | — |
| `get-download-urls` (4 + guía de equivalencias) · `verify-purchase` · `resend-access` · `admin-generate-access` (+ SPA) | ✅ | los 4 ficheros de `dl/` los trae la F2 |
| SPA: `productos-digitales-config.ts`, changelog 2.2, catálogo (`name.en`, `urlByLang`, `priceByLang`) | ✅ | — |
| `product-prices.ts` ($39) con `sync-product-prices.py` | ✅ `--check` verde (77 productos, 26 EN) | — |
| `payment-links.ts` | ⏳ John crea el Payment Link → env `VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN` → `sync-payment-links.py` | — |
| Hub EN: tarjeta viva en la 1 (Pastry, Chocolate e Ice Cream bajan a 2-4); fuera la vieja «Business Plan: Grill Catering for Events» (kit español) | ✅ | `DigitalProductsHubPage.astro` |
| `footerLinks` hacia el BBQ: 7 planes EN + Food Cost + HACCP + Catering Checklists | ✅ | — |
| FAQ cruzada «Is there a plan for a BBQ caterer?» en Catering y Food Truck EN (entra también en su FAQPage) | ✅ | — |
| hreflang recíproco en `/plan-negocio-parrillero-asador-eventos` (solo el `<head>`; mismo patrón que coctelería) | ✅ | — |
| `llms.txt` / `llms-full.txt` (25 → 26 productos EN + entrada) | ✅ | — |
| `tienda-gate.py`: EXENTOS (6 nombres con tilde + «Costa del Sol») y comentario de `--esperadas` | ✅ | — |
| OG `og-bbq-catering-business-plan.jpg` | ⚠️ provisional (recorte de `plan-parrillero-asador-eventos-2`) | §4 |
| 3 imágenes nuevas | ❌ las genera el orquestador **antes del merge** | §4 |
| Correo EN de lanzamiento (`.html` + `.subject.txt`), sin programar | ✅ | `emails/broadcast-bbq-catering-business-plan-lanzamiento-en.*` |
| `CALENDARIO-V2-SEMANAL.md` (hueco 29-ene 14:00Z, borrador + routine el 30-dic) | ⏳ orquestador | — |

## 2. Decisiones de contenido

- **SEO (D96b, research §9):** title `BBQ Catering Business Plan Kit: Word Template + Excel Financial Projections + Pricing
  Calculator | AI Chef Pro` (110 car., nombre del producto primero, patrón mobile bar) · H1 Forma B `BBQ Catering ` + oro
  `Business Plan` + «Template for an Off-Site Barbecue Caterer with a Smoker Trailer: Word Plan + Excel Financial
  Projections + Pricing Calculator + Startup Checklist» · meta (151 car.) «BBQ business plan template for a smoked-meat
  catering company: Word plan, 3-year Excel projections, per-guest pricing calculator and startup checklist.» · keywords
  tal cual research §9. Los 6 H2 de research no caben como H2 (constantes de `UI_PLAN`, igual que en el mobile bar): van
  en el subtítulo del grid («What's inside your BBQ Business Plan Kit for catering»), tarjetas 2/4/5 («Is a BBQ business
  profitable?», «Your BBQ catering menu in pounds», «How much does it cost to start a BBQ catering business?»), razones
  2/3 («Can You Start a BBQ Business From Home?», «BBQ Catering Prices per Guest and per Pound») y FAQ.
- **FAQ (21):** las 9 de research §9 en la redacción del comprador + qué incluye, ¿genérico?, seguridad alimentaria de
  carnes ahumadas (mínimos del Food Code separados de la temperatura de calidad ≈ 203 °F), seguros, **«Should I buy this
  or the Catering Business Plan Kit?»** (canibalización, D112), lender, Excel, **UK/Canada/Australia** (estilo mobile
  bar), moneda, suscripción, clientes, garantía. `schema.faqs` = el mismo array.
- **Legal sin inventar (research §6):** sin cocina de casa (Food Code 3-201.11; cottage food de TX excluye carne),
  commissary con acuerdo escrito, trailer que cocina en el evento = mobile food unit según el condado («Texas rules say
  so» → «ask your county»), fuego → fire marshal en genérico (Class K, distancias, propano, burn bans): **las cifras del
  boletín de Corpus Christi (10 ft, 200 lb) no salen en la landing** porque son de una ciudad.
- **Jerga:** pitmaster, BBQ caterer, smoked meats, commissary, live pit on site (extra de pago), insulated food carriers /
  hot boxes, W-2. Fuera de la landing «La Caja China» (marca) y «lechón» (tilde; tienda-gate): «whole hog / pig roast».
  Precios de smoker trailers de fabricantes citados sin marca («US makers list at roughly $8,500 to $20,400»).
- **Testimonios:** los 8 del ES traducidos con «…with the Spanish edition of this plan»; cambiada solo la frase que no es
  verdad en el EN (18 cortes → smoke schedule; CCAA y modelo de contrato → legal section + permits checklist; roadmap de
  food truck y 30.000 EUR → startup costs; 93 proveedores y «Tienda Biomasa» → checklist; 100.000 EUR → sin cifra;
  contratos B2C/B2B → calculadora; «freelance» y «Don» fuera).
- **Imagen del hub:** `plan-parrillero-asador-eventos-2` (offset smoker en un evento), no el hero ES (parrilla argentina).

## 3. Cifras «a confirmar con F2-NOTAS»

Todas viven en **un solo bloque `CASO`** al principio de la ficha (comentario `// a confirmar con F2-NOTAS` en cada
línea); la ficha las interpola en FAQ, razones y tarjetas. Hub, `llms*`, changelog, dashboard y correo **no** llevan
cifras del caso.

| Clave `CASO` | Valor puesto (research §8 / SPEC) | Fuente F2 esperada |
|---|---|---|
| `eventos` · `invitados` · `precio` | 150 · 75 · $38.00 | `B4` · `B6` · `B5` (D15 puede subir B4 hasta 170) |
| `ventas` | $427,500 | `ventas_a1` |
| `inversion` · `circulante` · `necesidad` | $83,300 · $49,800 · $133,100 | Startup Costs total, circulante, total cash needed |
| `propios` · `prestamo` · `dscr` | $35,000 · $98,000 · 3.0× | `B30` · `B31` calibrado · DSCR mínimo |
| `neto` · `netoPct` · `equilibrio` | $30,700 · 7.2% · 126 | neto año 1 · % · eventos de equilibrio |
| `marketing` · `seguros` | $10,000 · $6,000 | fijo de marketing · `B27` |
| `pesEventos` · `pesPrecio` · `pesInvitados` | 113 · $34.20 · 68 | Scenarios pesimista (y que la caja se agote de verdad) |
| `ejDropoff` · `ejGraduacion` · `ejBoda` | $22 · $35 · $52 | «3 Example Quotes» (precio por invitado de cada uno) |
| `livePit` · `cortes` · `menuStyles` · `formulas` | $650 · 13 · 10 · 700 | calculadora D105/D106 · docx §2 · fórmulas del libro |

**Frases a cotejar con los ficheros F2** (si alguna no es verdad, se cambia esa frase): calculadora con lb (kg) y °F (°C)
(FAQ UK); nota UK del docx §9 (council 28 días antes, food hygiene rating, 14 alérgenos, VAT 20 %, plan de fuego con
council y recinto); oz por invitado 6/8/8 editables; precios de carne en blanco; depósito 50 % nonrefundable y tramos de
cancelación; salida «price per pound of cooked meat»; referencias 40/80/150/300 en la lista de la compra; «start the pit
by»; fase 2 «Pits, Fire & Permits» con commissary agreement, condado, fire marshal, DMV, commercial auto e inland marine;
ServSafe Manager, Thumbtack, Google Business Profile y launch tasting en el checklist; camioneta de arrastre del dueño
($0) con la nota de la pickup (≥ 3,000 lb, $25-40K); líneas $20,000 / $3,500 / $4,500 / $18,000 de Startup Costs; `B5`
«excl. sales tax; staffing and service charge included»; el docx dice que el pesimista agota la caja.

## 4. Imágenes

Del ES del parrillero valen **-2** (offset smoker en un evento: hero, buyBox, CTA, hub), **-6** (evento al aire libre:
whyBg, bonus 1) y **-hero** (parrilla argentina: solo como línea live-fire, nunca hero; bonus 2). Fuera -1 («ASADOR»),
-3 (restaurante, texto en la camisa), -4 («PREMIUM QUEBRACHO CHARCOAL MADRID 2026») y -5 («ASADO MADRID», food truck).

**BLOQUEANTE antes del merge**: la ficha ya referencia estas 3 rutas (galería posiciones 2-4 y strip del grid); hay
que crearlas con `generate-images` en `astro-site/public/lovable-uploads/ai-gallery/` (JPG 1600 px, 200-450 KB). Ningún
gate comprueba que existan: `ls` de las tres antes de fusionar.

| Fichero | Alt (research §9) | Prompt (una línea) |
|---|---|---|
| `bbq-catering-smoker-trailer-wedding.jpg` | Offset smoker trailer at a BBQ catering event | Photorealistic golden-hour photo of a black 500-gallon offset smoker on a trailer at an outdoor rustic barn wedding in Texas, a pitmaster in a dark apron opening the firebox, light smoke, guests and string lights softly blurred behind, no text, no logos, 16:9 |
| `bbq-catering-brisket-carving-station.jpg` | Pitmaster slicing brisket at a carving station during an outdoor wedding | Photorealistic medium close-up of a pitmaster slicing a smoked packer brisket with a pink smoke ring and dark bark on butcher paper at a carving station of an outdoor wedding buffet, chafing dishes with sides behind, warm evening light, no text, no logos, 16:9 |
| `bbq-catering-drop-off-corporate.jpg` | Drop-off BBQ catering trays with pulled pork, ribs and sides for a corporate lunch | Photorealistic high-angle photo of disposable aluminum half pans with pulled pork, St. Louis ribs, sliced brisket, mac and cheese, coleslaw, baked beans, rolls and sauce cups set on a conference room table for a corporate lunch, daylight, no text, no logos, no brand names, 16:9 |

**OG**: `og-bbq-catering-business-plan.jpg` (1200×630) es hoy un recorte de -2; rehacerlo desde
`bbq-catering-smoker-trailer-wedding.jpg` (como el mobile bar en `49dc3d4a`) y, si se rehace, cambiar el alt del correo
por «Offset smoker trailer at a BBQ catering event» (nota en la cabecera del `.html`).

## 5. Posts EN candidatos para banners (blog EN = otra sesión, Cursor; no tocados)

`/en/blog/how-to-start-a-food-truck-business` (lectores que dudan entre truck y catering; ya enlaza al Food Truck Kit) ·
`/en/blog/prompt-library-catering` · `/en/blog/restaurant-profit-margins-explained-benchmarks` (margen neto 7-8 % del
catering) · `/en/blog/ai-recipe-scaling-guide` (escalar por invitados ≈ Shopping List by Guest Count) ·
`/en/blog/ai-food-cost-calculator-reduce-costs`. No hay post EN de BBQ: hueco SEO para «how to start a bbq catering
business» (research §2-§3) cuando la sesión del blog lo coja.

## 6. Gates (24-oct, sin build)

- `tienda-gate.py` (estático): ✅ 26 productos vivos fuera de ES con data, páginas y zona-app.
- `sync-product-prices.py --check`: ✅ 77 productos (51 ES + 26 EN); catálogo coincide (26 `priceByLang`).
- `gate-flujo-postpago.py --offline --only bbq-catering-business-plan`: 5 ficheros = 5 tarjetas; ❌ esperados: los 4
  ficheros de `dl/bbq-catering-business-plan/` (F2) y el Payment Link (John; avisa también de los 3 checklists de
  postre, que lo esperan igual).
- `robots-gate.py`: ✅ (zona app bloqueada, landing rastreable).
- esbuild: ✅ los 26 TS/TSX tocados o nuevos + los frontmatter de los 5 `.astro` (3 páginas BBQ, ES parrillero, hub EN).
- Texto de la ficha evaluado con node: sin `€`, sin restos de español (fuera los EXENTOS), sin no latinos, sin
  «grill master / support kitchen / freelance / Cambro / Caja China».
- **No ejecutados (necesitan preview o red contra la página nueva):** `tienda-gate.py --base` y `--es-identico --base
  <preview> --esperadas /plan-negocio-parrillero-asador-eventos` (la ES solo cambia en el `<head>`: el wrapper queda
  idéntico línea a línea al de coctelería y la plantilla no se toca), `carrusel-apps-gate.py --base`, `whatsapp-gate.py`,
  `gate-flujo-postpago.py` LIVE. `nombre-gate.py` no aplica (solo fichas ES).

## 7. Pendientes

1. Orquestador: confirmar el bloque `CASO` con `F2-NOTAS` / `cifras_caso.json` y cotejar las frases de §3.
2. Orquestador: generar las 3 imágenes de §4 y rehacer la OG.
3. John: Payment Link USD → env en Netlify → `sync-payment-links.py` → `gate-flujo-postpago.py --only
   bbq-catering-business-plan` LIVE (sin compra de prueba: acceso por admin).
4. Tras el deploy: gates con `--base`, sitemap reenviado en GSC (`sc-domain:aichef.pro`), correo (borrador + routine el
   30-dic para el 29-ene 14:00Z) y entrada en `CALENDARIO-V2-SEMANAL.md`.
5. Blog EN (Cursor): banners de §5.
