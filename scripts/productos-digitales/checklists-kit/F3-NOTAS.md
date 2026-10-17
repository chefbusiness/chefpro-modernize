# Restaurant Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 17-oct-2026. Implementador único de F3 sobre la rama `feat/restaurant-checklists-en`
> (worktree). Contrato: `SPEC.md` §1, §2.1, §6, §7 punto 6, §9 + `TIENDA-INTERNACIONAL.md` §6. Molde:
> `restaurant-schedule-templates` (kit EN más parecido) y `how-to-open-a-pastry-shop` (último lanzamiento EN).
> Sin build, sin Playwright, sin navegador (regla térmica): verificación = lectura + scripts ligeros.

## 1. Puntos de registro (los del hermano, replicados para `restaurant-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` + `titlePost` + `compatSubtitle` + `value` opcional | `astro-site/src/components/pages/KitTareasLandingPage.astro`, `data/productos/tareas/types.ts` | ✅ ES byte a byte (§2) |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas.ts`) | `astro-site/src/data/productos-en/tareas/restaurant-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/restaurant-checklist-templates` | `astro-site/src/pages/en/digital-products/restaurant-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}` |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/restaurant-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/restaurant-checklist-templates/library.astro`, `islands/library/RestaurantChecklistsKitLibraryIsland.tsx`, `src/pages/RestaurantChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas.astro` → `alternatesFamilia('kit-tareas')` | ✅ (cambia solo el `<head>` de `/kit-tareas`) |
| 7 | Familia `kit-tareas` → `en: restaurant-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (ver §4: fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `netlify/functions/verify-purchase.ts`, `resend-access.ts` | ✅ email EN post-compra y reenvío |
| 10 | Descargas: mismas claves que `kit-tareas` → 11 xlsx EN + `equivalents-guide` (`dl/en-shared/`) | `netlify/functions/get-download-urls.ts` | ✅ nombres SPEC §2.1 (ya en `public/dl/`) |
| 11 | Precio `{ usd: 19 }` | `netlify/shared/product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (67 productos) |
| 12 | Payment Link | `netlify/shared/payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `netlify/functions/admin-generate-access.ts`, `src/pages/AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA (emails + ficheros) y changelog EN | `src/data/productos-digitales-config.ts`, `src/data/productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo del blog: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` (`kit-tareas`) | ✅ |
| 16 | Alias de enlace en casos de uso | `astro-site/src/lib/linkify-use-case.ts`, `src/lib/linkify-use-case.tsx` | ✅ |
| 17 | Hub EN: la tarjeta «Recurring Tasks: Casual Restaurant» sube a la 1 con copy EN | `components/pages/DigitalProductsHubPage.astro` | ✅ (enlace y precio salen solos de `vivo` + `product-prices`) |
| 18 | `footerLinks` de los 5 kits EN hermanos | `data/productos-en/kits/{food-cost,haccp,restaurant-inventory,restaurant-schedule,restaurant-financial-plan}-templates.ts` | ✅ |
| 19 | GEO: `llms.txt` y `llms-full.txt` (y «currently 16 products» en los dos) | `astro-site/public/` | ✅ |
| 20 | Sitemap: lastmod de la landing (gate y dashboard ya salen del filtro anidado) | `astro-site/src/lib/sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 4 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-en.json` + `fase8x-sustituir-banner.py --aplicar` + `fase8b-regen-lastmod.py` | ✅ gate de reversibilidad OK; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos de banners EN | `scripts/astro-migration/fase8e-banners-en-reapuntar.py` (`TEMAS`) | ✅ |
| 23 | `tienda-gate.py`: las 20 landings Tareas en `--es-identico` + nombres de testimonios exentos | `scripts/productos-digitales/tienda-gate.py` | ✅ estático verde (16 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `scripts/productos-digitales/emails/broadcast-restaurant-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla (`CryptoPayButton` con `lang`, `landingPath` anidado) | ✅ renderizadas en EN: hero, buybox, cta + nota EN |

Blog EN: `prompt-library-restaurant-manager` (víctima Financial Plan Kit), `kitchen-brigade-system` (Food Cost Kit),
`prompt-library-executive-chef` (Inventory Kit), `prompt-library-bartender-consulting` (Financial Plan Kit). Ningún
post EN enlazaba a `/kit-tareas`, así que `fase8x-banners-tienda-idioma.py` no tenía nada que re-apuntar.

## 2. Cómo se garantiza que las 20 landings ES salen byte a byte iguales

- Son **20**, no 21: `mega-pack-tareas.astro` no importa la plantilla (copia el carrusel).
- **Método calcado de KitExcel/PlanNegocio/Guías**, ya verificados en producción con `tienda-gate --es-identico`:
  textos a `i18n/tienda/<lang>.json` (el `es.json` es VERBATIM con los literales de esta plantilla: se comprobó cadena a
  cadena), texto multilínea con los helpers `nl()`/`nlSp()`, el `<a>` de «Empieza desde 10 €/mes» literal en la rama ES
  (como atributo de expresión Astro escaparía el `&`), `priceCurrency` y breadcrumb condicionados a `lang`. Lo nuevo
  propio de la línea (título y subtítulo del carrusel de apps) va en `UI_TAREAS` con el ES verbatim.
- `titlePost` va pegado al `</span>` dorado: con `compressHTML` el compilador ya quitaba el blanco entre elementos
  (comprobado en el JS compilado), y `undefined` no emite nada.
- **Prueba sin build** — `scripts/astro-migration/es-identico-local/comparar.mjs` (nuevo, reutilizable): renderiza con
  el Container API de Astro 5.18.2 y `@astrojs/compiler` 2.13.1 (las versiones del lock, tomadas de otro proyecto del
  Mac con `ASTRO_NM`) la plantilla de `git show HEAD` y la de ahora con las 20 fichas ES, con y sin cripto, y compara el
  HTML normalizando solo el id de scope y el nombre del fichero. **Resultado: 40/40 idénticas.** Prueba de mutación: un
  espacio de más en `es.json` → 40/40 distintas.
- Prueba final en el **deploy preview**: `tienda-gate.py --es-identico --base <preview> --esperadas /kit-tareas`
  (49 landings; `/kit-tareas` solo cambia en el `<head>` por el hreflang EN).

## 3. Decisiones de contenido (landing, dashboard, correo)

- Traducción propia desde el ES (regla 1bis, sin bridge), jerga de `GLOSARIO-JERGA-ES-EN.md` y `textos_en/glosario.json`.
- **Sin anclas** (FTC): sin `priceOld`, `discountBadge`, `bonusSaveLine` ni `value` de bonos; «One-time payment ·
  lifetime access · updates included»; `bonusTotalLabel` = «Everything included: 9 templates + 3 bonuses». Sin rating
  ni reviews en el JSON-LD; los 10 testimonios del ES traducidos tal cual con el subtítulo de la edición española.
- **Afirmaciones del ES que el kit no cumple, fuera:** «48 h» del pre-evento (el xlsx dice «from booking to event day»);
  la FAQ «¿Funcionan con Google Sheets?» (SPEC §9: sin test real; pastillas y subtítulo del carrusel sin Sheets, como
  `restaurant-schedule-templates`). El logo de Google Sheets del carrusel de apps es constante en toda la tienda.
- FAQ: las 5 PAA de SPEC §6 + las del ES adaptadas + «Does it work in the UK, Canada or Australia?» (8 °C / 63 °C y 14
  alérgenos en la celda de la tarea, patio = terrace / beer garden, billetes editables desprotegiendo la hoja sin
  contraseña, nota UK del calendario, Equivalents Guide) + moneda, suscripción y garantía (como los hermanos).
- Hechos comprobados contra los xlsx/textos EN: 491 tareas, 111 en el 01, 5 filas verdes libres por tabla, contador que
  excluye N/A, BEFORE/DURING/AFTER SERVICE en el 02, DAYS 1-5 en el 03, «Report #» en «Quarterly & Annual», rollos de
  25¢/10¢ y propinas fuera de ventas en el 09, nota UK del B02.
- **Imágenes con texto en español → fuera de la EN** (no se generó ninguna): `og-kit-tareas.jpg` («Kit de Tareas
  Recurrentes», «€14», «Imprimible A4»), `tareas-restaurante-manager.jpg` (tablón «HORARIOS») y
  `tareas-restaurante-perfiles.jpg` (pizarra «Vinos / Tapas»). Entran `staff-en-preshift.jpg`,
  `staff-en-schedule-board.jpg` y `manual-manager-briefing.jpg` (sin texto, ya en la tienda EN). Se queda
  `tareas-restaurante-limpieza.jpg` (rótulo «EL ABRAZO», nombre de local). **OG provisional = `tareas-restaurante-hero.jpg`**
  (sin texto): falta una OG EN propia (Gemini) si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/restaurant-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py` (hoy
   `gate-flujo-postpago --offline --only` da 1 fallo esperado: «SIN Payment Link»).
2. **`vivo: true` ya está en la rama** (criterio de la guía de pastelería): fusionar SOLO con el link creado; si hubiera
   que fusionar antes, poner `vivo: false` en `tienda.ts` (la tarjeta del hub y el hreflang se apagan solos).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas`, `whatsapp-gate`, `robots-gate`; render
   visual de landing y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only restaurant-checklist-templates`; sitemap reenviado en GSC
   (`sc-domain:aichef.pro`); correo en la cola de 5 días (`CALENDARIO-V2-SEMANAL.md`, routine).
5. Test real en Google Sheets → si pasa: pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
6. El changelog EN describe lo que SPEC D8-D17 exige a F2: si algún gate de F2 lo recorta, ajustar la entrada.
