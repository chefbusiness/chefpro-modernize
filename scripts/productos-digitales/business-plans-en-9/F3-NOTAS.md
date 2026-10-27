# Wedding Venue Business Plan Kit (EN, $49) — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 27-oct-2026. Implementador único de la F3 en `feat/wedding-venue-business-plan-en`, apilada sobre
> `feat/ice-cream-shop-business-plan-en` (PR #171) y esta sobre `feat/hotel-checklists-en` (PR #170): el hub, `llms`, `tienda.ts`,
> `footerLinks` del hotel y de la heladería ya están dentro; esta rama construye encima. Molde: la F3 del Ice Cream Shop Business
> Plan Kit (`business-plans-en-10/F3-NOTAS.md`) y la del Pizza Shop (`git show 64ace831`), esta última para el dashboard con
> calculadora. Contrato = `SPEC-delta.md` §9 (D175-D177) y §11 (O1-O4) + `REVISION-FINAL.md` §0/§5. Sin build, Playwright ni
> navegador (regla térmica; CPU 44-49 °C toda la sesión). Payment Link: NO (John).

## 1. Puntos de registro

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Ficha EN (D175): $49 sin `priceOld`/`discountBadge`/`value`/`aggregateRating`/`review`/testimonios; SEO, H1, meta y keywords de research §9; 23 FAQ (las 8 de research §3 + LLC, alquilar o comprar, calculadora, contrato, ¿granero/venue existente/banquet hall?, Catering/BBQ/Paella/Mobile Bar, lender, Excel, UK/CA/AU, moneda, suscripción, clientes, garantía) | `astro-site/src/data/productos-en/planes/wedding-venue-business-plan.ts` | ✅ |
| 2 | Landing, `omitGlobalApp`, `miselup={false}`, env `VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN` → `#comprar` sin link | `pages/en/digital-products/wedding-venue-business-plan.astro` | ✅ |
| 3 | Gate `/access` y `/library` + island (`wedding-venue-business-plan-jwt`) | `…/wedding-venue-business-plan/{access,library}.astro`, `islands/library/WeddingVenueBusinessPlanLibraryIsland.tsx` | ✅ |
| 4 | Dashboard: claves `plan-negocio`, `plan-financiero`, `checklist-apertura`, `calculadora-pricing`, `modelos-contrato`, `equivalents-guide` (6 tarjetas) | `src/pages/WeddingVenueBusinessPlanDashboard.tsx` | ✅ |
| 5 | Familia `plan-negocio-finca-eventos-bodas` → es + en vivos | `lib/tienda.ts` | ✅ |
| 6 | Gemelo ES con hreflang recíproco (`alternatesFamilia`) | `pages/plan-negocio-finca-eventos-bodas.astro` | ✅ (solo el `<head>`: va en `--esperadas /plan-negocio-finca-eventos-bodas`) |
| 7 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 8 | PRODUCTS `lang: 'en'` + email | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 9 | Descargas: 5 ficheros + `equivalents-guide` | `get-download-urls.ts` | ✅ cruzado por script contra `dl/`, dashboard y config: 0 de más, 0 de menos |
| 10 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 11 | Precio `{ usd: 49 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (85 productos; catálogo coincide en las 54 entradas) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Catálogo (`name.en`, `description.en`, `urlByLang.en`, `priceByLang.en`) + `digital-products-catalogue.json` (entrada EN) | `src/data/products-catalog.ts`, `astro-site/src/data/digital-products-catalogue.json` | ✅ (`name.en` decía «… (Spain)») |
| 14 | Config SPA y changelog (versión **2.2**, la de los docProps de los 5 ficheros; SPEC decía «1.0») | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ |
| 15 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ «Wedding Venue Business Plan Kit» |
| 16 | Hub EN: tarjeta «Business Plan: Event & Wedding Venue» (→ ES) **sustituida** por «Wedding Venue Business Plan Kit» en la 1, «New» (la heladería baja a la 2) | `DigitalProductsHubPage.astro` | ✅ una sola tarjeta; imagen = hero ES (sin texto) |
| 17 | `footerLinks`: +1 línea tras la heladería en 8 fichas EN (Catering, Mobile Bar, BBQ, Paella, Catering Checklists, Restaurant, Bar, Food Truck); la ficha nueva enlaza a Catering, BBQ, Paella, Mobile Bar, Catering Checklists, Restaurant, Hotel y resto | 8 fichas + la nueva | ✅ |
| 18 | GEO: `llms.txt` y `llms-full.txt` (31 productos) | `astro-site/public/` | ✅ +1 fila cada uno |
| 19 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ 2026-10-27 |
| 20 | FAQ «Is there a business plan for a wedding venue?» | `catering-business-plan.ts`, `mobile-bar-business-plan.ts` | ✅ |
| 21 | OG | `astro-site/public/og-wedding-venue-business-plan.jpg` | ✅ 1200×630, recorte centrado del hero ES (`sips -c` + `-z`) |
| 22 | `tienda-gate.py`: comentario de `--esperadas` + `/plan-negocio-finca-eventos-bodas` (ya estaba en `PLANES_ES`); sin exentos (la ficha no lleva testimonios) | `tienda-gate.py` | ✅ |
| 23 | Correo EN | `emails/broadcast-wedding-venue-business-plan-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR (va el 23-feb-2027 14:00Z; lo programa el orquestador); «Hi everyone,», negro #111 + dorado #FFD700, sin precio tachado |
| 24 | G9 (`PRODUCTOS_LETTER`, `EXCLUIDOS`) | `censo-entregables.py`, `postprocess-transversal.py` | ✅ ya estaban desde la F2 |
| 25 | Blog, `robots.txt`, `PAYMENT_LINKS_PENDIENTES_JOHN.md` | — | ❌ NO (carril de otra sesión / lo toca el merge del link) |

## 2. Verificación (ligera, sin build)

- `sync-product-prices.py --check` verde; `tienda-gate.py` (estático, python 3.11) verde: «31 producto(s) vivos fuera de ES con data,
  páginas y zona-app».
- `gate-flujo-postpago.py --offline --only wedding-venue-business-plan`: 6 ficheros = 6 tarjetas, 0 issues de ficheros; falla SOLO
  «SIN Payment Link» (esperado; lo comparten el hotel y la heladería).
- Cruce por script: las 5 claves de `get-download-urls.ts` + la guía = las 6 del dashboard; la config SPA lista los 5 ficheros (como la
  heladería, sin la guía); los 5 existen en `dl/wedding-venue-business-plan/` y la guía en `dl/en-shared/`; 0 de más, 0 de menos.
- esbuild (stdin) sobre los `.ts`/`.tsx` tocados y el frontmatter de los `.astro` tocados: 0 errores; los 2 JSON válidos.
- Barrido de la ficha, el dashboard y el correo: 0 «€», 0 español visible, 0 no latinos visibles, 0 `aggregateRating`/`review`/`priceOld`/
  «% off»/«worth»/testimonios, 0 «covers» como unidad, 0 volúmenes de búsqueda, 0 «Cooling-Off» afirmada (solo «ask your attorney
  whether…»), «non-refundable» solo entrecomillado como lo que NO hay que escribir sin matiz.
- Cifras de la landing contra `REVISION-FINAL.md` §0/§5 y `cifras_caso.json`: 100 eventos × 90 guests × $68 = ventas $612,000, CAPEX
  $570,500 (19 partidas $503,500), caja $669,716, préstamo $470,000 (SBA 7(a), 10 años), DSCR mín. 1.86×, neto 8.9 % → 14.2 %,
  equilibrio 86 eventos (84 de caja), holgura ≈ 20 % (19.8 %), calculadora: boda de sábado de temporada alta, 130 guests, $12,690 con
  sales tax; «more than 700 formulas» (hay 734).
- **No hecho (necesita build/preview):** `es-identico-local/comparar.mjs`, render EN, `tienda-gate --base` y `--es-identico`,
  `robots`/`whatsapp`/`miselup`/`hub`/`carrusel-apps`, `gate-flujo-postpago --crypto-products` (preview y LIVE), `fase6-gate`.

## 3. Decisiones de contenido

- **Reglas de la revisión respetadas** (REVISION-FINAL): finca ARRENDADA → lease con prórrogas que solo ejerce el inquilino ≥ plazo del
  préstamo («SBA lenders typically require this; confirm with your lender»), opción de compra o ROFR, consentimiento del propietario,
  TI allowance y lease contingente al permiso; comprar = variante SBA 504 sin Excel. El venue no sirve alcohol (el exclusive caterer
  con licencia; BYOB solo con bartender licenciado y host liquor liability, «ask your state's alcohol board»). Cooling-Off: solo
  «ask your attorney whether…». Contrato: «template, not legal advice; state law varies; have a local attorney review it». Permisos:
  siempre «ask your county». Comisión del caterer 10 % del F&B (≈ 12 % de las ventas del venue). Sin The Knot, sin cifras de sprinklers,
  sin volúmenes de búsqueda (M4). «wedding venue» en nombre/H1, «event venue» como descriptor.
- **Sin testimonios** (los del ES son clientes de España; FTC). Diferenciación con Catering, BBQ Catering, Paella Catering y Mobile Bar:
  una FAQ, una de las razones del bloque «why», los primeros enlaces del pie, y el enlace de vuelta desde Catering y Mobile Bar (FAQ + pie).
- **Los 6 H2 de research §9** no caben como H2 (constantes de la plantilla): van como títulos de las razones y de las tarjetas.
- **Imágenes** (abiertas una a una las 7 `plan-finca-*`): ninguna descartada, todas sin texto ni marcas ni logos. Aviso: el escenario es
  mediterráneo (olivos, teja, piedra), no un granero estadounidense; se dejan como en la heladería (calle de aire europeo) y ninguna
  descripción de la ficha afirma un granero. `-barra` muestra a un barman sirviendo: la ficha no dice que sea el venue quien sirve.
  `-cocina` = el caterer cocinando; se usa como fondo de «why» (el exclusive caterer). Los `alt` los pinta la plantilla vacíos.
- **Versión 2.2** en changelog y `updateNote` (docProps de los 5 ficheros: «v2.2 · October 2026»); el SPEC decía «1.0».
- **Pendientes**: Payment Link (USD 49, prosa sin viñetas, éxito → `/en/digital-products/wedding-venue-business-plan/access?session_id={CHECKOUT_SESSION_ID}`),
  luego `payment-links.ts`, env de Netlify, programar el correo (23-feb-2027 14:00Z), gates con build y alta en
  `PAYMENT_LINKS_PENDIENTES_JOHN.md`. Posible conflicto de merge en hub, `llms`, `tienda.ts` y `footerLinks` con #170/#171: la rama
  ya está apilada, no debería haberlo.
