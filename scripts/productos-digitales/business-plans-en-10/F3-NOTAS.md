# Ice Cream Shop Business Plan Kit (EN, $39) — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 27-oct-2026. Implementador único de la F3 en `feat/ice-cream-shop-business-plan-en`, apilada sobre
> `feat/hotel-checklists-en` (PR #170: hub, `llms`, `tienda.ts`, `footerLinks` del hotel ya dentro; esta rama construye
> encima). Molde: la F3 del Pizza Shop Business Plan Kit (`git show 64ace831`) replicada punto por punto con
> `ice-cream-shop-business-plan`; contrato = `SPEC-delta.md` §7 (D204-D206) y `REVISION-FINAL.md` §4. Sin build,
> Playwright ni navegador (regla térmica; CPU 42-47 °C toda la sesión). Payment Link: NO (John).

## 1. Puntos de registro

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Ficha EN (D204): $39 sin `priceOld`/`discountBadge`/`value`/`aggregateRating`/`review`/testimonios; SEO, H1, meta y keywords de research §9; 20 FAQ (las 8 de research §3 + teen scoopers, «ice cream» y «homemade», Checklists Kit Pro, Restaurant/Bakery, lender, Excel, UK/CA/AU, moneda, suscripción, clientes, garantía) | `astro-site/src/data/productos-en/planes/ice-cream-shop-business-plan.ts` | ✅ |
| 2 | Landing, `omitGlobalApp`, `miselup={false}`, env `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN` → `#comprar` sin link | `pages/en/digital-products/ice-cream-shop-business-plan.astro` | ✅ |
| 3 | Gate `/access` y `/library` + island | `…/ice-cream-shop-business-plan/{access,library}.astro`, `islands/library/IceCreamShopBusinessPlanLibraryIsland.tsx` | ✅ |
| 4 | Dashboard: claves `plan-negocio`, `plan-financiero`, `checklist-apertura`, `equivalents-guide` (4 tarjetas, sin calculadora) | `src/pages/IceCreamShopBusinessPlanDashboard.tsx` | ✅ |
| 5 | Familia `plan-negocio-heladeria` → es + en vivos | `lib/tienda.ts` | ✅ |
| 6 | Gemelo ES con hreflang recíproco (`alternatesFamilia`) | `pages/plan-negocio-heladeria.astro` | ✅ (solo el `<head>`: va en `--esperadas /plan-negocio-heladeria`) |
| 7 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 8 | PRODUCTS `lang: 'en'` + email | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 9 | Descargas: 3 ficheros + `equivalents-guide` | `get-download-urls.ts` | ✅ cruzado por script contra `dl/`, dashboard y config: 0 de más, 0 de menos |
| 10 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 11 | Precio `{ usd: 39 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (84 productos; catálogo coincide en las 54 entradas) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Catálogo (`name.en`, `description.en`, `urlByLang.en`, `priceByLang.en`) + `digital-products-catalogue.json` (entrada EN) | `src/data/products-catalog.ts`, `astro-site/src/data/digital-products-catalogue.json` | ✅ |
| 14 | Config SPA y changelog (versión **2.2**, la de los docProps de los 3 ficheros; SPEC decía «1.0») | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ |
| 15 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ «Ice Cream Shop Business Plan Kit» |
| 16 | Hub EN: tarjeta «Business Plan: Artisan Gelato Shop» (→ ES) **sustituida** por «Ice Cream Shop Business Plan Kit» en la 1, «New» (el hotel baja a la 2) | `DigitalProductsHubPage.astro` | ✅ una sola tarjeta; imagen = hero ES (sin texto) |
| 17 | `footerLinks`: +1 línea en 13 fichas EN (11 planes y kits que enlazaban a la pizza + Pizza Shop Checklists + Catering Checklists, incl. Food Cost y HACCP) y en Pizza Shop Business Plan; el Ice Cream Shop Checklists Kit Pro enlaza al plan | 15 fichas EN | ✅ |
| 18 | GEO: `llms.txt` y `llms-full.txt` (30 productos) | `astro-site/public/` | ✅ +1 fila cada uno |
| 19 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ 2026-10-27 |
| 20 | FAQ «Is there a business plan for an ice cream shop?» | `ice-cream-shop-checklist-templates.ts` (on-page), `food-truck-business-plan.ts` (ice cream truck → ese kit) | ✅ |
| 21 | OG | `astro-site/public/og-ice-cream-shop-business-plan.jpg` | ✅ 1200×630, recorte del hero ES (`sips -z`, misma proporción) |
| 22 | `tienda-gate.py`: comentario de `--esperadas` + `/plan-negocio-heladeria` (ya estaba en `PLANES_ES`); sin exentos (la ficha no lleva testimonios) | `tienda-gate.py` | ✅ |
| 23 | Correo EN | `emails/broadcast-ice-cream-shop-business-plan-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR (va el 28-feb-2027 14:00Z; lo programa el orquestador); «Hi everyone,», negro #111 + dorado #FFD700, sin precio tachado |
| 24 | G9 (`PRODUCTOS_LETTER`, `EXCLUIDOS`) | `censo-entregables.py`, `postprocess-transversal.py` | ✅ ya estaban desde la F2 |
| 25 | Blog, `robots.txt`, TEMAS, `PAYMENT_LINKS_PENDIENTES_JOHN.md` | — | ❌ NO (carril de otra sesión / lo toca el merge del link) |

## 2. Verificación (ligera, sin build)

- `sync-product-prices.py --check` verde; `tienda-gate.py` (estático, python 3.11) verde: «30 producto(s) vivos fuera de ES
  con data, páginas y zona-app».
- `gate-flujo-postpago.py --offline --only ice-cream-shop-business-plan`: 4 ficheros = 4 tarjetas, 0 issues de ficheros;
  falla SOLO «SIN Payment Link» (esperado; lo comparte el hotel).
- esbuild (stdin) sobre los 31 `.ts`/`.tsx` tocados y el frontmatter de los 5 `.astro` tocados: 0 errores; los 2 JSON válidos.
- Barrido de la ficha, el dashboard y el correo: 0 «€», 0 español, 0 no latinos, 0 `aggregateRating`/`review`/`priceOld`/
  «% off»/«worth»/testimonios, 0 pizza/panadería/España. «no license needed» solo aparece negado («the plan never says…»).
- Cifras de la landing contra `REVISION-FINAL.md` §0 y `cifras_caso.json`: ventas $383,625, CAPEX $204,100 (19 partidas
  $186,000), caja $256,871, fondo $52,771, préstamo $162,000 + $95,000 propios, neto 5.6 % → 8.6 %, equilibrio 147 (140 de caja),
  holgura 18.3 %, DSCR 2.26×, saldo mínimo $46,060, pesimista $294,000. «More than 700 formulas» (hay 736).
- **No hecho (necesita build/preview):** `es-identico-local/comparar.mjs`, render EN, `tienda-gate --base` y `--es-identico`,
  `robots`/`whatsapp`/`miselup`/`hub`/`carrusel-apps`, `gate-flujo-postpago --crypto-products` (preview y LIVE), `fase6-gate`.

## 3. Decisiones de contenido

- **Lo que la ficha NO dice** (REVISION-FINAL §4): «retail food establishment in most states», «no hood / no smoke exhaust
  needed» (la FAQ de equipamiento remite al plan reviewer), «at least one CFPM» (no se menciona el CFPM como cifra) ni
  «no license needed». Licencias: «ask your state department of agriculture and your local health department»; Vermont y
  Georgia con su condición («eaten on the premises»). Modelo D190: base pasteurizada comprada; pasteurizar = variante
  ($25,000-45,000, licencia de dairy plant o frozen dessert manufacturer habitualmente).
- **Sin testimonios** (los 8 del ES son clientes de España; FTC). La diferenciación con el Ice Cream Shop Checklists Kit Pro
  ($19, `/en/digital-products/ice-cream-shop-checklist-templates`): una FAQ, una de las 8 razones del bloque «why», el
  primer enlace del pie y el enlace de vuelta desde la ficha del Checklists Kit (pie + FAQ).
- **Los 6 H2 de research §9** no caben como H2 (constantes de la plantilla): van como títulos de las razones y de las tarjetas.
- **Imágenes** (abiertas una a una): descartada `plan-heladeria-vitrina.jpg` (tarjetas del mostrador con texto borroso tipo
  «LIMÓN / CHOCOLAT»); `-obrador` se queda (muestra la batch freezer y una cuba tapada al lado; el caso no tiene pasteurizador,
  por eso la ficha no la describe como tal) y `-invierno` también (tarta helada y chocolate caliente; sale además un crêpe).
  El resto, sin texto ni marcas. Hero y cono con calle de aire europeo: sin texto, se dejan.
- **Versión 2.2** en changelog y `updateNote` (docProps de los 3 ficheros: «v2.2 · October 2026»); el SPEC decía «1.0».
- **Pendientes**: Payment Link (USD 39, éxito → `/en/digital-products/ice-cream-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}`),
  luego `payment-links.ts`, env de Netlify, programar el correo (28-feb-2027 14:00Z), gates con build y alta en
  `PAYMENT_LINKS_PENDIENTES_JOHN.md`. Posible conflicto de merge con el hotel (PR #170) en hub, `llms`, `tienda.ts` y
  `footerLinks`: ya está apilada, no debería haberlo.
