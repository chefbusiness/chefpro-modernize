# Bar Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en la rama `feat/bar-checklists-en` (worktree). Molde:
> el PR #133 (Restaurant Checklists Kit Pro, `../F3-NOTAS.md`), replicado punto por punto. Contrato: `SPEC.md` (delta)
> + la SPEC base. Sin build, sin Playwright, sin navegador (regla térmica): verificación = lectura + scripts ligeros
> (CPU 47-49 °C toda la sesión).

## 1. Puntos de registro (los 25 del hermano, replicados para `bar-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios (ya la tiene desde el #133) |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas-bar.ts`) | `astro-site/src/data/productos-en/tareas/bar-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/bar-checklist-templates` | `astro-site/src/pages/en/digital-products/bar-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/bar-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/bar-checklist-templates/library.astro`, `islands/library/BarChecklistsKitLibraryIsland.tsx`, `src/pages/BarChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide); cruza a Restaurant Checklists y Food Cost Kit Pro (el ES cruza a Kit Tareas y Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas-bar.astro` → `alternatesFamilia('kit-tareas-bar')` | ✅ (cambia solo el `<head>` de `/kit-tareas-bar`) |
| 7 | Familia `kit-tareas-bar` → `en: bar-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (ver §4: fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `netlify/functions/verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: mismas claves que `kit-tareas-bar` → 11 xlsx EN + `equivalents-guide` | `netlify/functions/get-download-urls.ts` | ✅ nombres de `SPEC.md` §2, ya en `public/dl/` (commit F2) |
| 11 | Precio `{ usd: 19 }` | `netlify/shared/product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (68 productos) |
| 12 | Payment Link | `netlify/shared/payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `admin-generate-access.ts`, `src/pages/AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog EN | `src/data/productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` (`kit-tareas-bar`) | ✅ (los casos de uso EN que citan `kit-tareas-bar` ya enlazan la landing EN a $19) |
| 16 | Alias de enlace | `astro-site/src/lib/linkify-use-case.ts`, `src/lib/linkify-use-case.tsx` | ✅ |
| 17 | Hub EN: «Recurring Tasks: Bar / Cocktails» sube a la 1 con copy EN | `components/pages/DigitalProductsHubPage.astro` | ✅ |
| 18 | `footerLinks` de los 6 kits EN + cruzados con los planes de bar | `kits/{food-cost,haccp,restaurant-inventory,restaurant-schedule,restaurant-financial-plan}-templates.ts`, `tareas/restaurant-checklist-templates.ts`, `planes/{bar,mobile-bar}-business-plan.ts` | ✅ (los cruzados entre hermanos van por `footerLinks`) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («currently 17 products») | `astro-site/public/` | ✅ |
| 20 | Sitemap: lastmod de la landing | `astro-site/src/lib/sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 3 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-bar-en.json` + `fase8x-sustituir-banner.py --aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×3; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos | `fase8e-banners-en-reapuntar.py` (`TEMAS`) | ✅ |
| 23 | `tienda-gate.py`: testimonios exentos + `/kit-tareas-bar` en `--esperadas` (comentario) | `scripts/productos-digitales/tienda-gate.py` | ✅ estático verde (17 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `emails/broadcast-bar-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla | ✅ |

Blog EN (víctima → Bar Checklists Kit Pro): `prompt-library-bartender-consulting` (HACCP; se quedan Food Cost y
Restaurant Checklists), `bar-profit-margins-beverage-costing` (Financial Plan; párrafo antes de «How to Calculate Pour
Cost», lejos del de la guía de Food Cost) y `prompt-library-sommelier-consulting` (Financial Plan; párrafo tras «Cellar
Management»). Las víctimas son los productos más repetidos del corpus EN (Financial Plan 32 → 30, HACCP 30 → 29).

## 2. Las 20 landings ES siguen byte a byte iguales

La plantilla no se toca en este PR. Comparador sin build (`es-identico-local/comparar.mjs`, `ASTRO_NM` =
`johnguerrero-es-astro/node_modules`, `--ref main`): **ES idénticas 40 · distintas 0**. El mismo pase renderiza la EN
(241.843 bytes): 0 restos de español con la heurística de `tienda-gate`, 0 «€», 0 no latinos, 0 `ratingValue`,
`priceCurrency` USD; «Google Sheets» solo en el carrusel de apps (constante de la tienda, igual que el hermano).
`/kit-tareas-bar` cambia solo en el `<head>` (hreflang) → `--esperadas /kit-tareas-bar` en el preview (`/kit-tareas` ya sale así en producción desde el PR 133).

## 3. Decisiones de contenido

- Traducción propia desde el ES (regla 1bis, sin bridge); **cada cifra se comprobó contra los xlsx EN del commit F2**
  (342 tareas, 54 en el 01, 33 en el 08, 23 fechas, 65–110 lb de hielo, 38 °F, PSI del técnico, líneas cada 2 semanas
  y ácido cada 3 meses, 46–50 °F, «3 days», Challenge 25 en 03 Daily, «Report #», rollos de 25¢/10¢, propinas fuera,
  ASCAP/BMI/SESAC/GMR, licencia de alcohol, 6:00–8:00 PM, «86'd», 5 filas verdes libres).
- **Lo que el ES afirma y el kit EN no trae, fuera:** Halloween y St. Patrick como hojas del 06 (están en el
  calendario), «2,5-3 bar», «cóctel gratis», las «17 fechas» del dashboard ES, el «briefing» del manager como plantilla
  (es una tarea) y las **filas libres del calendario** (no las hay: celdas editables + «Add your local dates»).
- Sin anclas (FTC); fórmula «One-time payment · lifetime access · updates included»; sin rating ni reviews; los 10
  testimonios traducidos tal cual con el subtítulo de la edición española. Alcohol siempre «check your state's
  ABC/liquor authority». FAQ UK/CA/AU: Challenge 25, personal licence, licensing hours, TEN (nota del B02), 8 °C y 14
  alérgenos; Canadá 19 (18 en AB, MB, QC) con Smart Serve / Serving It Right; Australia 18 + RSA; caja editable sin
  contraseña; Equivalents Guide.
- **Imágenes:** las 7 del ES no llevan texto en español (rótulos en inglés: «PREMIUM SPIRITS», «THE BOTANICAL 2026»)
  → se quedan todas. Fuera solo `og-kit-tareas-bar.jpg` («Kit de Tareas Recurrentes», «€12», «Imprimible A4»):
  **OG provisional = `tareas-bar-hero.jpg`**; bonus 3 = `en-equivalents-guide.jpg`. Falta una OG EN propia si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/bar-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py`. Hoy
   `gate-flujo-postpago --offline --only bar-checklist-templates`: 12 entregables encontrados, **1 fallo esperado**
   («SIN Payment Link»).
2. `vivo: true` ya está en la rama: fusionar SOLO con el link creado (o `vivo: false` si hubiera que fusionar antes).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-bar`, `whatsapp-gate`,
   `robots-gate`; render visual de landing y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only bar-checklist-templates`; sitemap en GSC; correo a la cola
   de 5 días (`CALENDARIO-V2-SEMANAL.md`, siguiente hueco EN) y programarlo con su routine.
5. Test real en Google Sheets (común a la línea) → pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
