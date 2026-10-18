# Catering Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en la rama `feat/catering-checklists-en` (worktree,
> apilada sobre la del Coffee Shop, que va sobre la del bar). Molde: la F3 del Coffee Shop (`../cafe/F3-NOTAS.md`,
> commit `44456cab`) replicada punto por punto. Contrato: `SPEC.md` (delta) + la SPEC base. Sin build, sin Playwright,
> sin navegador (regla térmica): verificación = lectura + scripts ligeros (CPU 46-49 °C toda la sesión).

## 1. Puntos de registro (los 25 de la cafetería, para `catering-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas-catering.ts`) | `astro-site/src/data/productos-en/tareas/catering-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/catering-checklist-templates` | `…/catering-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/catering-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/CateringChecklistsKitLibraryIsland.tsx`, `src/pages/CateringChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide); claves del ES (02 = `partidas`; 09 = cobros por evento con la clave `apertura-caja`); cruza a Restaurant, Bar Checklists y Food Cost Kit Pro (el ES: Kit Tareas, Kit Tareas Bar, Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas-catering.astro` → `alternatesFamilia('kit-tareas-catering')` | ✅ (cambia solo el `<head>`) |
| 7 | Familia `kit-tareas-catering` → `en: catering-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves de `kit-tareas-catering` → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres de `SPEC.md` §2 |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (70 productos) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog EN | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo `kit-tareas-catering`: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ |
| 16 | Alias de enlace | `linkify-use-case.ts` (astro) y `.tsx` (SPA) | ✅ |
| 17 | Hub EN: «Recurring Tasks: Catering / Events» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «9 pre-filled checklists», «dining room manager»; imagen = la misma, sin texto ES) |
| 18 | `footerLinks`: 5 kits + Restaurant, Bar y Coffee Shop Checklists + Catering Business Plan Kit | `kits/*-templates.ts` ×5, `tareas/{restaurant,bar,coffee-shop}-checklist-templates.ts`, `planes/catering-business-plan.ts` | ✅ |
| 19 | GEO: `llms.txt` y `llms-full.txt` («currently 19 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap: lastmod de la landing | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 2 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-catering-en.json` + `--aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×2; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos | `fase8e-banners-en-reapuntar.py` (`TEMAS`, en minúsculas: el script compara con `.lower()`) | ✅ |
| 23 | `tienda-gate.py`: testimonios exentos + `/kit-tareas-catering` en `--esperadas` (comentario) | `tienda-gate.py` | ✅ estático verde (19 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `emails/broadcast-catering-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla | ✅ |

Blog EN: `prompt-library-catering` (128 menciones; víctima Restaurant Financial Plan 29 → 28; párrafo antes de «Tips for
getting more out of Catering AI+», ancla 10) y `cloud-kitchen-business-models` (25, su «Model 7: Catering Cloud
Kitchen»; víctima el eBook de prompts 28 → 27; párrafo al final del Model 7, antes de la tabla comparativa, ancla 10).
El siguiente (Allergen ID, 8) solo nombra el catering en prompts sueltos: fuera.

## 2. Las 20 landings ES siguen byte a byte iguales

Comparador sin build (`es-identico-local/comparar.mjs`, `ASTRO_NM` = `johnguerrero-es-astro/node_modules`,
`--ref main`): **ES idénticas 40 · distintas 0**. Render EN (245.102 bytes): `revisar_texto` de `tienda-gate` sin
fallos en las 4 fichas EN, 0 `ratingValue`, `priceCurrency` USD; «€» y «Google Sheets» solo en las constantes de la
plantilla (las mismas 9 / 8 apariciones que el bar y la cafetería). Bar y cafetería: +1 línea cada una (su pie).

## 3. Decisiones de contenido

- Traducción propia desde el ES (regla 1bis, sin bridge); cifras comprobadas contra los xlsx EN (las 02:50, ya con la
  ronda 1 de la revisión F2): **347 tareas** = los contadores del kit (327 en las 9 plantillas + 20 del briefing, como
  el ES), 38 en el 01, 24 en el 02, 33 + 20 en el 03, 16 por perfil, 27 + 17 en el 05, 33 en el 08 con responsable y
  hora, 12 + 12 en el 09, registro de 25 eventos, 22 fechas; 41 / 135 °F, lectura cada 30 min, 3 h antes en el venue,
  12–15 piezas por persona, 1 camarero por 20, 68–72 °F, depósito 30–50 %, 5 filas libres solo en el 08 y el 09.
- **Lo que el ES afirma y el kit no trae, fuera:** «cumple normativa APPCC de transporte», «certificado ATP», «IVA
  10/21 %», «Verifactu», las «secciones ya puestas» de la plantilla en blanco, «sin internet» y «€60-75/mes» de Trail,
  los «€31» de los bonos; las «20 fechas» del dashboard ES (son 22).
- **Alineada con la ronda 1 de la revisión** (leída en `revision/REVISION-F2.md`): TPHC = servir dentro de las 4 h y
  descartar lo que quede (B1), sobrantes calientes a enfriar y fríos de vuelta a 41 °F (M2), el service charge es
  ingreso y lo que se paga de él al equipo es salario (m3), el tipo de sales tax empieza en 0 (M9).
- FAQ obligatorias: UK/CA/AU (8 °C / 63 °C, «event catering», 14 alérgenos ya anotados en carteles y tarjetas de
  bandeja, nota UK del calendario, tipo de VAT/GST/HST en la celda del tipo, tabla de efectivo editable sin
  contraseña, edad del alcohol como los hermanos) e impuestos (sales tax = tipo que introduce el comprador sobre el
  subtotal gravable; service charge ≠ propina, Rev. Rul. 2012-18; certificado de exención; «not tax advice: your CPA»).
- Testimonios: los 10 traducidos tal cual con el subtítulo de la edición española; UNA frase cambiada (Roberto Ibáñez:
  «el timing sheet del event manager» → «the event manager's checklist»: el kit trae la run sheet como tarea).
  «APPCC» → HACCP. Sin anclas (FTC), fórmula «One-time payment · lifetime access · updates included», sin rating.
- **Imágenes:** las 6 fotos del ES no llevan texto en español (furgoneta «FRESH EVENT CATERING», cajas «CRYSTAL»,
  «LOADING BAY») y ya las publica el Catering Business Plan Kit EN: se quedan. Fuera solo la OG ES («Kit de Tareas
  Recurrentes», «€12», «Imprimible A4») → OG = `tareas-catering-hero.jpg`. Falta una OG EN propia si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/catering-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py`.
   Hoy `gate-flujo-postpago --offline --only catering-checklist-templates`: 12 entregables, **1 fallo esperado**
   («SIN Payment Link», que lista también el bar y la cafetería porque la rama está apilada).
2. `vivo: true` ya está en la rama: fusionar SOLO con el link creado (o `vivo: false` si hubiera que fusionar antes).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-catering` (+ `/kit-tareas-bar` y
   `/kit-tareas-cafeteria` si van en el mismo PR), `whatsapp-gate`, `robots-gate`; render visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only catering-checklist-templates`; sitemap en GSC; correo a la
   cola de 5 días (`CALENDARIO-V2-SEMANAL.md`, siguiente hueco EN) y programarlo con su routine.
5. Si la revisión F2 cambia cifras después de las 02:50 (tareas, filas, fechas), repasar ficha, hub, catálogo, llms,
   changelog y correo (grep «347»).
6. Test real en Google Sheets (común a la línea) → pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
