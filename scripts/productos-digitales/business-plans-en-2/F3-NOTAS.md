# Restaurant y Bakery Business Plan Kit (EN) — notas de F3 (4-oct-2026 · sesión Claude Code)

## F3

Implementador único (Opus) en el worktree de la rama `feat/business-plans-en-2` (PR #111, en borrador, base
`feat/business-plans-en` = PR #110), rebasada sobre lo último del #110 antes de empezar (el F1 de esta rama quedó como
`0057b098`, mismo contenido que `b0f41656`; push con `--force-with-lease` contra ese sha). Réplica pieza a pieza de la F3
de Food Truck / Coffee Shop (`../business-plans-en/F3-NOTAS.md`), con la SPEC delta D30-D47 y R1-R12.

### Qué se hizo

| Pieza | Ficheros |
|---|---|
| Fichas EN | `astro-site/src/data/productos-en/planes/restaurant-business-plan.ts`, `bakery-business-plan.ts` |
| Landing + gate + dashboard | `astro-site/src/pages/en/digital-products/<slug>.astro`, `<slug>/access.astro`, `<slug>/library.astro` (copias de las de Coffee Shop) |
| Dashboards + islands | `src/pages/RestaurantBusinessPlanDashboard.tsx`, `BakeryBusinessPlanDashboard.tsx`; `astro-site/src/islands/library/*BusinessPlanLibraryIsland.tsx` |
| Registros | `tienda.ts` (FAMILIAS), `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`, `get-download-urls.ts` (ficheros D32 en `dl/<slug>/`), `product-prices.ts` (regenerado con `sync-product-prices.py`, `--check` verde), `src/data/productos-digitales-config.ts`, `productos-changelog.ts` (2.2 «First English edition»), `AdminGenerateAccess.tsx` |
| hreflang ES | `plan-negocio-bar-restaurante.astro` y `plan-negocio-panaderia.astro`: `locales={['es']}` → `alternatesFamilia(...)` (único cambio en el ES) |
| Interenlazado (D47) | hub EN (Restaurant 1, Bakery 2; FT y CAF pasan a 3 y 4, el Financial Plan a 5), catálogo `urlByLang`/`priceByLang` + `name.en`/`description.en`, alias de linkify (SPA y Astro), pies de los 8 productos EN (6 kits/eBook + FT + CAF), las 2 fichas nuevas enlazan a Financial Plan, HACCP, Staff Scheduling y los 3 planes hermanos, 5 banners del blog EN re-apuntados (`fase8x-banners-tienda-idioma.py --con-descripcion`: 3 de REST, 2 de PAN), `sitemap-lastmod.json` |
| Entregables (lado web) | `EXCLUIDOS` de `postprocess-transversal.py` y `PRODUCTOS_LETTER` de `censo-entregables.py` |
| tienda-gate | `EXENTOS` sin cambios: los testimonios de REST y PAN usan los MISMOS 5 nombres con tilde que FT/CAF (solo comentario) |
| Imágenes | 10 fotos propias sin texto (`rbp-en-*` ×5: hero, bar, dining, owner-plan, storefront; `bbp-en-*` ×5: hero, oven, bench, owner-plan, wholesale; Nano Banana 2, 11 llamadas ≈ $0,74, un reintento del horno) + `og-restaurant-business-plan.jpg` y `og-bakery-business-plan.jpg` (recorte 1200×630 del hero). Reutilizadas: `use-case-casual-kitchen.jpg` y `use-case-panadero-panes.jpg` (sin rótulos; `use-case-casual-bar` NO: pizarras «TAPAS»/«VINOS»). Hoja de contacto revisada a ojo: ninguna letra legible |
| Correos | `scripts/productos-digitales/emails/broadcast-<slug>-lanzamiento-en.html` (sin programar; D46: REST 9-nov y PAN 14-nov 14:00Z, programables desde el 10-oct y el 15-oct) |

### Decisiones tomadas en F3

- **Grid (D45)**: DOCX la primera tarjeta en los dos. REST: fuera «Análisis de Mercado España 2026» (R3) y la tarjeta de
  ratios queda como «Instructions & Ratio Checks» (el semáforo OK/REVIEW), para no contar dos veces la tabla de
  referencias, que es el bono 2. PAN: «Equipamiento» fundida con «Startup Costs & Equipment» y «Ratios de Referencia»
  fundida con «Instructions» (lo que D45 pide). Siguen 9 tarjetas.
- **Bonos (D45)**: REST 1 «Restaurant Permits & Licenses Guide (US + UK Notes, Liquor License Included)» = §9 + fases 1,
  2 y 6; 2 «US Market Data & Industry Benchmarks (Sourced)» = §3 + tabla D19 (prime cost, food cost, personal, gastos
  generales y alquiler; sin «margen», que el research REST no trae). PAN 1 «Bakery Permits & Licenses Guide (Commercial
  vs Cottage Food, US + UK Notes)» = §9 + fases 1-2; 2 «Bakery Industry Benchmarks (Sourced)».
- **Testimonios**: los 8 de cada ES traducidos con el subtítulo «…with the Spanish edition of this plan». Reformuladas
  sin número las frases con cifras del producto ES que el EN no tiene: REST «50+ trámites», «Seg. Social al 33,4 % y 14
  pagas», ratios «28-32 % / <35 % / <10 %», «las 6 fases» (son 7) y el superlativo de David Torres; PAN «60+ trámites»,
  «leasing del horno» (R7), «break-even por kilos de pan» y «mix bollería» (R8), «plus nocturnidad», «margen real
  superior al 25 %», «materia prima 22-28 %, merma 3-5 %, margen bollería >75 %», «mix de producción», RGSEAA (→ «Spain's
  food registry»). Se conservan las cifras personales (135.000 / 65.000 EUR, «10 días», «300 / 800 EUR al mes», «4
  meses», «3 aperturas») y las «6 fases» del PAN (el checklist EN también tiene 6).
- **Cifras con fuente en la ficha REST**: «A survey of independent owners by RestaurantOwner.com put the median opening
  cost at around $375,000» (research delta §3, fuente DoorDash Merchants que cita la encuesta). Licencia de alcohol en
  rango cualitativo («from a few hundred dollars … to well over $100,000 in states that cap the number of licenses»),
  dentro del dato del research ($50 a $300,000+). La revisión adversarial final puede abrir la fuente; si no se confirma,
  quitar la frase del $375,000 (la FAQ se sostiene sin ella).
- **FAQ** (17 cada una). REST: PAA de research §2 (qué incluye, 30/30/30/10 —descrita como «informal rule of thumb» y
  contestada con los umbrales D41 y el prime cost 60-65 % con fuente—, ¿es rentable?, causas de cierre sin tasa) +
  «startup costs», «liquor license cost», «how to open a restaurant», permisos, «bar business plan» (restaurante con
  barra; para un bar sin cocina sirve el Excel, el Word hay que reescribirlo más), prestamista, cambiar cifras (sin
  propinas ni tip credit, D38), UK (premises + personal licence), moneda, suscripción, licencia de uso y garantía. PAN:
  PAA (qué incluye, ¿es rentable? con umbrales D41, cuánto gana el dueño, cómo empezar, sin dinero) + coste, cottage food
  vs comercial (D39), permisos (FDA registration solo si domina el mayorista), sales tax del pan (D36, sin cifra de la
  parte exenta), prestamista, cifras, UK (zero-rated para llevar, 20 % en local), moneda, suscripción, licencia, garantía.
- **Puestos**: los nombres EN de los 7 (REST) y 6 (PAN) puestos los fija la ficha con los rótulos ES («general
  manager-owner, head chef, line cook, server-bartender, part-time server, weekend extra and relief cover»; «head
  baker-owner, baker, bakery assistant, counter staff, weekend extra and relief cover»). Si la F2 los traduce distinto,
  igualar la ficha (grid «Staffing», FAQ «Is it a generic plan…») y el dashboard no los nombra.
- **Fases del checklist**: REST «business setup · location and permits · build-out and equipment · staff · marketing and
  launch · what must be in place before you open (final inspections, liquor license, insurance, pest control, music
  licenses) · first 90 days» (filas-cabecera A4…A66 del ES); PAN las 6 de D33. El certificate of occupancy se nombra sin
  asignarle fase.
- **Changelog 2.2**: afirma lo que la SPEC decide para los ficheros (sales tax sin crédito y con tipo propio del alcohol
  en sala, D37; parte exenta del pan, D36; sin propinas, D38; campana, separador de grasas y fila de licencia de alcohol;
  12 pagas; SBA sin interest-only; DSCR 1.25×; sin símbolo de moneda; sq ft/galones; Letter). Si la F2 se aparta de algo,
  corregir `src/data/productos-changelog.ts`.
- **Fórmulas**: «more than 700 linked formulas» (772 REST / 737 PAN en el ES; G1 exige las mismas salvo E2/E3).
- **Hub**: tarjetas viejas «Business Plan: Bar-Restaurant» (50+ trámites, «Spanish reference budget») y «Business Plan:
  Bakery / Bakehouse» (RGSEAA, kilos de pan) sustituidas por las EN vivas, badge «New» en verde.
- **Usos EN (`/en/usos/`)**: ninguna página de usos menciona estos dos productos (el #110 sí retocó una FAQ del consultor
  barista para el Coffee Shop); no se añade mención nueva: D47 no la pide.

### TODO_CIFRA (las rellena el orquestador con `cifras_caso.json` de la F2)

| Fichero | Dónde | Qué cifra |
|---|---|---|
| `restaurant-business-plan.ts` | FAQ «How much does it cost to open a restaurant?» | caja total necesaria del restaurante de ejemplo |
| `restaurant-business-plan.ts` | FAQ «How much does a liquor license cost?» | importe de la fila de licencia de alcohol (D37 fija $15,000; confirmar) |
| `restaurant-business-plan.ts` | `why.reasons[1]` «Numbers Calculated, Not Copied» | ticket medio (excl. sales tax), margen bruto % y equilibrio en cubiertos/día |
| `bakery-business-plan.ts` | FAQ «How much does it cost to open a bakery?» | caja total necesaria de la bakery de ejemplo |
| `bakery-business-plan.ts` | `why.reasons[1]` «Numbers Calculated, Not Copied» | ticket medio (excl. sales tax), margen bruto % y equilibrio en transacciones/día |

Cada uno lleva un comentario `// TODO_CIFRA:` encima. Las FAQ son el mismo array que el FAQPage: el JSON-LD también los
lleva hasta que se rellenen (REST 7 apariciones en el JSON de la ficha, PAN 5). Correos y dashboards: sin cifras del caso.

### Lo que falta para publicar

1. **F2**: los 6 ficheros en `astro-site/public/dl/<slug>/` con los nombres D32 + `cifras_caso.json` → rellenar los
   TODO_CIFRA y revisar puestos, fases y changelog contra los ficheros reales.
2. **John**: los 2 Payment Links USD $39 → env `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN` y
   `VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN` (scope builds) → `sync-payment-links.py` → redeploy.
3. Merge del #110 primero y después este (el #111 está apilado); gates LIVE tras el merge (`gate-flujo-postpago --only`
   ×2, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, `miselup-gate`, `datafast-gate`) y programar los 2
   correos EN (cola D46).

### Gates

| Gate | Veredicto |
|---|---|
| `tienda-gate.py` (estático) | ✅ 10 productos vivos fuera de ES con data, páginas y zona-app |
| `sync-product-prices.py --check` | ✅ 61 productos; catálogo coincide (10 `priceByLang`) |
| `fase8c-libreria-en-gate.py --todos` | ✅ banners ↔ tienda EN en 68 posts, ya con `plan-negocio-bar-restaurante` y `plan-negocio-panaderia` con landing EN; 26 posts, 0 errores |
| esbuild (transform) sobre los 30 TS/TSX tocados + `node --experimental-strip-types` sobre las 3 fichas | ✅ sintaxis; fichas: 17 FAQ, 9 tarjetas, 8 testimonios, 9 enlaces de pie |
| Gates contra el preview | ver §«Preview» abajo |
