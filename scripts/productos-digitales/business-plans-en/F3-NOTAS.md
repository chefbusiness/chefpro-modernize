# Food Truck y Coffee Shop Business Plan Kit (EN) — notas de F3 (4-oct-2026 · sesión Claude Code)

## F3

Implementador único (Opus) en el worktree de la rama `feat/business-plans-en` (PR #110), en paralelo con la F2, que
trabaja solo en esta carpeta. Réplica del Restaurant Financial Plan Kit Pro EN pieza a pieza, con la plantilla de la
línea Planes (`PlanNegocioLandingPage.astro`, que ya aceptaba `lang` desde `b734fe33`).

### Qué se hizo

| Pieza | Ficheros |
|---|---|
| Fichas EN | `astro-site/src/data/productos-en/planes/food-truck-business-plan.ts`, `coffee-shop-business-plan.ts` |
| Landing + gate + dashboard | `astro-site/src/pages/en/digital-products/<slug>.astro`, `<slug>/access.astro`, `<slug>/library.astro` |
| Dashboards + islands | `src/pages/FoodTruckBusinessPlanDashboard.tsx`, `CoffeeShopBusinessPlanDashboard.tsx`; `astro-site/src/islands/library/*BusinessPlanLibraryIsland.tsx` |
| Registros | `tienda.ts` (FAMILIAS), `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`, `get-download-urls.ts`, `product-prices.ts` (regenerado con `sync-product-prices.py`), `src/data/productos-digitales-config.ts`, `productos-changelog.ts` (2.2 «First English edition»), `AdminGenerateAccess.tsx` |
| hreflang ES | `plan-negocio-food-truck.astro` y `plan-negocio-cafeteria.astro`: `locales={['es']}` → `alternatesFamilia(...)` (único cambio permitido en el ES) |
| Interenlazado (D29) | hub EN (las 2 tarjetas vivas arriba: Food Truck 1, Coffee Shop 2), catálogo `urlByLang`/`priceByLang` + `name.en`/`description.en`, alias de linkify (SPA y Astro), mención de `/en/usos/` (consultor: «Coffee Shop Business Plan Kit ($39)»), pies de los 6 productos EN, 2 banners del blog EN (`fase8x-banners-tienda-idioma.py --con-descripcion`, idempotente), `sitemap-lastmod.json` |
| Entregables (lado web) | `EXCLUIDOS` de `postprocess-transversal.py` y `PRODUCTOS_LETTER` de `censo-entregables.py` (SPEC §7.6) |
| Imágenes | 10 fotos propias sin texto (`ftbp-en-*` ×5, `csbp-en-*` ×5, Nano Banana 2, ≈ $0,67) + `og-food-truck-business-plan.jpg` y `og-coffee-shop-business-plan.jpg` (recorte 1200×630 del hero). Reutilizadas: `use-case-food-truck-grill.jpg` y `use-case-cafeteria-brunch.jpg` (sin rótulos) |
| Correos | `scripts/productos-digitales/emails/broadcast-<slug>-lanzamiento-en.html` (sin programar; propuesta D28: FT 30-oct, CAF 4-nov, 14:00Z) |

### Decisiones tomadas en F3

- **Testimonios** (orquestador sobre D26): los 8 del ES traducidos con el subtítulo «…with the Spanish edition of this
  plan». Reformuladas sin número las frases con cifras de la v1.1: FT «59 trámites», «27 clientes/día a 12 €»,
  «food cost 30 %, margen 65 %, retorno 12-24 meses», «guía de licencias por CCAA» (→ «the licensing section of the
  plan»); CAF «53 clientes/día a 9,50 €», «food cost 25-30 %», «licencia inocua» (→ «the right activity license in
  Spain»). Se conservan las cifras personales de cada testimonio (su inversión de 62.000 EUR, «18 meses», «5 aperturas»,
  «3 meses») y se marca España donde el texto habla de bancos o licencias españolas.
- **Compatibilidad** (orquestador sobre D25): pastillas «Microsoft Excel (.xlsx)», «Microsoft Word (.docx)», «US Letter
  size» y `compatSubtitle` «Microsoft Excel and Word files, set up to print on US Letter paper». Lo mismo en el aviso del
  dashboard. ⚠️ Residuo de plantilla: el marquee de logos (constante de línea en `PlanNegocioLandingPage.astro`) sigue
  mostrando el logo de Google Sheets entre los 9 de IA/ofimática; no se toca para no romper la identidad byte a byte de
  las 10 landings ES. Si John lo quiere fuera en EN, hay que condicionar el array `apps` por `lang`.
- **Grid CAF**: DOCX primera tarjeta (A7); «Equipamiento» fundida con «Startup Costs & Equipment» (sigue en 9).
- **Bonos**: FT y CAF = «Permits & Licenses Guide (US + UK Notes)» ($29, §9 del plan + fases del checklist, sin
  formularios estatales) + «Benchmarks (Reference Table)» ($29).
- **FAQ** (16 cada una): PAA de research §2 + las del ES adaptadas + UK + moneda + suscripción + licencia (un negocio con
  todos sus camiones/locales) + garantía. No se cita ninguna «tasa de fracaso» (no hay fuente) ni rangos de coste de
  terceros marcados «(resumen)» en el research: se describe la estructura de costes y se remite al caso del kit.
- **Fórmulas**: «more than 700 linked formulas» (722 / 742 en el ES; G1 exige las mismas fórmulas salvo E2, así que el
  recuento no baja). Si la F2 cambia el recuento, revisar esa frase (FT: FAQ «free template»; CAF: tarjeta del Excel y
  FAQ «Can I change the numbers»).
- **Changelog 2.2**: afirma lo que la SPEC decide para los ficheros (sales tax sin crédito, 12 pagas, suelo federal +
  estatal, SBA 7(a)/Microloan sin interest-only, DSCR 1.25×, sin símbolo de moneda, sq ft/galones, Letter). Si la F2
  se aparta de algo, corregir `src/data/productos-changelog.ts`.
- **Hub**: tarjetas viejas «Business Plan: Food Truck» y «Business Plan: Coffee Shop / Brunch» (59 procedimientos, ITV,
  RGSEAA, «53 customers/day») sustituidas por las EN vivas, con badge «New» en verde, como el Financial Plan.

### TODO_CIFRA (las rellena el orquestador con `cifras_caso.json` de la F2)

| Fichero | Dónde | Qué cifra |
|---|---|---|
| `food-truck-business-plan.ts` | FAQ «How much money is needed to start a food truck?» | caja total necesaria del camión de ejemplo |
| `food-truck-business-plan.ts` | `why.reasons[1]` «Numbers Calculated, Not Copied» | ticket medio (excl. sales tax), coste de mercancía %, margen bruto %, equilibrio en clientes/día y clientes/día previstos |
| `coffee-shop-business-plan.ts` | FAQ «How much does it cost to open a coffee shop?» | caja total necesaria del coffee shop de ejemplo |
| `coffee-shop-business-plan.ts` | `why.reasons[1]` «Numbers Calculated, Not Copied» | ticket medio (excl. sales tax), margen bruto % y equilibrio en clientes/día |

Cada uno lleva un comentario `// TODO_CIFRA:` encima. Las FAQ son el mismo array que el FAQPage: el JSON-LD también los
lleva hasta que se rellenen. Correos: sin cifras del caso.

### Lo que falta para publicar

1. **F2**: los 6 ficheros en `astro-site/public/dl/<slug>/` con los nombres D5 (el gate B los exige en disco, trackeados y
   servidos con content-type binario) + `cifras_caso.json` → rellenar los TODO_CIFRA.
2. **John**: los 2 Payment Links USD $39 → env `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_BUSINESS_PLAN` y
   `..._COFFEE_SHOP_BUSINESS_PLAN` (scope builds) → `sync-payment-links.py` → redeploy.
3. Gates LIVE tras el merge (`gate-flujo-postpago --only` ×2, `tienda-gate --base https://aichef.pro`, `robots-gate
   --live`, `miselup-gate`, `datafast-gate`) y programar los 2 correos EN (cola D28).

### Gates contra el preview (deploy preview del PR #110, commit `66a89da1`)

| Gate | Veredicto |
|---|---|
| `tienda-gate.py` (estático) | ✅ 8 productos vivos fuera de ES con data, páginas y zona-app |
| `tienda-gate.py --base <preview>` | ✅ tras añadir a `EXENTOS` los 5 nombres con tilde de los testimonios (María López, Carlos Méndez, Laura Fernández, Ana García, Pedro Gutiérrez; mismo patrón que los kits anteriores). Hreflang recíproco en↔es, /access y /library 200 + noindex, 0 €, 0 no latinos, sin EUR en el JSON-LD ni aggregateRating |
| `tienda-gate.py --es-identico --esperadas /plan-negocio-food-truck,/plan-negocio-cafeteria` | ✅ 13/15 idénticas byte a byte; las 2 esperadas con texto visible idéntico. Diff normalizado propio: solo `<link rel="alternate" hreflang="en">` + `og:locale:alternate en_US` (y la inyección de Netlify del preview) |
| `robots-gate.py --live` (censo = sitemap de producción + páginas del repo + zona-app) | ✅ las 2 landings nuevas en el censo público, sus /access y /library en el privado; ninguna pública bloqueada, toda la zona app bloqueada |
| `gate-flujo-postpago.py --base <preview> --crypto-products all --crypto-exclude pro-prompts-ebook --only <slug>` ×2 | ❌ esperado, 10 fallos cada uno y todos de los dos pendientes: 3 ficheros sin disco + 3 LIVE 404 (los entrega la F2), landing con `#comprar`, sin entrada en `payment-links.ts` y env `VITE_STRIPE_PAYMENT_LINK_*` inexistentes (Payment Links de John). Verde lo demás: claves dashboard ↔ get-download-urls, landing/access/library 200 con island, `product-prices.ts` al día, puertas cripto en el HTML (1 landing con botón, 0 sin él) |
| `whatsapp-gate.py` | necesita `dist` (prohibido el build local): réplica por red con su mismo regex sobre las 6 páginas nuevas + hub + 2 landings ES → 1 botón en landings, access y hub, 0 en los dashboards; aria-label EN |
| `miselup-gate.py --base <preview>` | ✅ 102/102 páginas ES correctas; 16 páginas de 8 productos de otras tiendas (incluidas las 4 nuevas de landing+library) sin tarjeta |
| `datafast-gate.py --base <preview>` | ✅ 23/23 (muestra fija); las 2 landings nuevas, comprobadas aparte: cargador exactamente 1 vez |
| `fase8c-libreria-en-gate.py --todos` | ✅ banners ↔ tienda EN en 68 posts, ya con `plan-negocio-food-truck` y `plan-negocio-cafeteria` con landing EN |
| curl propio sobre las 2 landings | title D2, canonical propio, H1 Forma B, JSON-LD Product (USD 39.00) + FAQPage + BreadcrumbList sin rating ni review, 0 €, 0 no latinos, tildes solo en los nombres de los testimonios y en la píldora «Español», 6 imágenes y la OG con 200 image/*, sitemap con las 2 landings y sin sus dashboards, hub EN con las 2 tarjetas enlazadas en las posiciones 1 y 2 |
