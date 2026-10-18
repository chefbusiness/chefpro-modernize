# Ghost Kitchen Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en `feat/ghost-kitchen-checklists-en` (worktree apilado
> sobre burger → pizza → catering → cafetería → bar). Molde: la F3 de la hamburguesería (`../burger/F3-NOTAS.md`,
> commits `41b0b0c4` y `a345762f`) replicada punto por punto. Sin build, Playwright ni navegador (regla térmica;
> CPU 45-51 °C toda la sesión). Sin commit: lo cierra el orquestador.

## 1. Puntos de registro (los 25 de la hamburguesería, para `ghost-kitchen-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-dark-kitchen.ts`) | `astro-site/src/data/productos-en/tareas/ghost-kitchen-checklist-templates.ts` | ✅ |
| 3 | Landing | `pages/en/digital-products/ghost-kitchen-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/ghost-kitchen-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/GhostKitchenChecklistsKitLibraryIsland.tsx`, `src/pages/GhostKitchenChecklistsKitDashboard.tsx` | ✅ 12 tarjetas, claves del ES (02 = `partidas`); cruza a Restaurant, Burger Joint Checklists y Food Cost Kit Pro (el ES: Kit Tareas, Kit Tareas Hamburguesería, Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-dark-kitchen.astro` → `alternatesFamilia('kit-tareas-dark-kitchen')` | ✅ (solo el `<head>`) |
| 7 | Familia `kit-tareas-dark-kitchen` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres de `SPEC.md` §2 = los de `dl/` (F2 `a713d4a9`) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (73 productos, 22 priceByLang) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ (y el caso de uso EN `/en/use-cases/concept/dark-kitchen`, que lista el kit, ya apunta a la landing EN) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ |
| 17 | Hub EN: «Recurring Tasks: Dark Kitchen» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «293 pre-filled tasks», Glovo/Just Eat, «riders and dispatch») |
| 18 | `footerLinks`: 5 kits + Restaurant, Bar, Coffee Shop, Catering, Pizza Shop y Burger Joint | 11 fichas EN | ✅ +1 línea cada una |
| 19 | GEO: `llms.txt` y `llms-full.txt` («22 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 2 banners + párrafo | `fase8x-config/kit-tareas-dark-kitchen-en.json` + `--aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×2; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | TEMAS para rebalanceos | `fase8e-banners-en-reapuntar.py` | ✅ |
| 23 | `tienda-gate.py`: exento «Adrián Soto» + `/kit-tareas-dark-kitchen` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ estático verde (22 vivos fuera de ES) |
| 24 | Correo EN | `emails/broadcast-ghost-kitchen-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Cripto + devoluciones | plantilla | ✅ |

Blog EN: `ghost-kitchen-complete-guide` (párrafo al cierre de «Running Multiple Brands from One Kitchen», ancla 6; víctima
Staff Scheduling Kit) y `cloud-kitchen-business-models` (cierre de «Model 2: Multi-Brand Cloud Kitchen», ancla 5; víctima
Staff Scheduling Kit; convive con el Catering Checklists por su «Model 7», ver `_doc` del JSON). Saliente extra en el pie
de la landing: el caso de uso EN de ghost kitchens (no hay guía EN de dark kitchen).

## 2. ES byte a byte

`es-identico-local/comparar.mjs --ref main`: **ES idénticas 40 · distintas 0**. Render EN (244.949 bytes):
`revisar_texto` 0 fallos, 0 `aggregateRating`/`review`, USD, H1 = title SEO (75 car.; description 160), 6 `Question`;
«€» 9 y «Google Sheets» 8 = las constantes de la plantilla (igual que los hermanos). «Dark Kitchen» solo en el nombre de
la edición española y en un negocio de testimonio. esbuild: 32 TS/TSX/.astro tocados sin errores.

## 3. Decisiones de contenido

- Cifras comprobadas contra los 11 xlsx EN (F2 `a713d4a9`): **331 tareas** (31 + 24 = 55 en el 01; 18 + 15 = 33 en el
  08), inventario de 32 artículos con Par y «⚠️ REORDER» (lb, qt, ea, sets), 22 fechas + 5 huecos + nota UK; marcas a las
  10:30 AM tras tablets (10:00), impresoras, timbre y tiempos; al cierre, marcas fuera antes de la alarma; 135 / 41 °F y
  bolsas separadas; 165 / 155 °F 17 s / 145 °F 15 s; pescado crudo −4 °F 7 días o −31 °F + 15 h, 90 días, aviso al
  consumidor; arroz de sushi (varianza + HACCP, 41 °F o TPHC 4 h); 8–12 min, < 10 min, < 12 min, < 30 s, > 15 min;
  food cost 25–30 %; comisiones ≈ 15–30 % con topes NYC/SF; NFPA 96 trimestral si alto volumen, semestral si moderado.
- Fuera lo que el ES afirma y el kit no trae: Trail €60-75/mes y «sin internet», Glovo/Just Eat, coordinación de
  riders y «tiempos de espera por plataforma», «foco por día» del semanal (todo el lunes), «calibración de balanzas»,
  «pre-evento 48 h» y «festivos con menú limitado», DDD/BIE/Verifactu; dashboard ES «6 checklists» (son 2) y «17 fechas»
  (son 22). Precio de lanzamiento / -69 % → fórmula EN.
- **Testimonios: 7 de 10 tal cual; retirados SOLO en EN** (comentario en la ficha): Daniel Ortiz «CloudEats» (operador
  real de cloud kitchens, Filipinas), Hugo Martinez «GhostBurger + GhostPoke + GhostWok» (Ghostburger, ghost kitchen
  real de Washington DC, RAMMY 2021) y Laura Serrano (cita Glovo, Uber Eats y Just Eat; rescatable cambiando solo esa
  frase por «three delivery apps»). Ninguna frase cambiada.
- Imágenes: ninguna lleva texto en español; fuera `tareas-dk-tablets` (Glovo, Deliveroo, Just Eat a toda pantalla) →
  `tareas-ghost-tablets-en.jpg`, JPG (306 KB, 1376×768) de la foto ya publicada en el blog EN
  (`post9-order-tablets.png`). OG = `tareas-dk-hero.jpg` (la OG ES lleva «Kit de Tareas» y «€12»).

## 4. Pendiente

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/ghost-kitchen-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`. Hoy
   `gate-flujo-postpago --offline --only ghost-kitchen-checklist-templates`: 12/12, 0 issues; único fallo «SIN Payment
   Link» (lista también los 5 hermanos de la rama apilada).
2. `vivo: true` ya en la rama: fusionar SOLO con el link (o `vivo: false`).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-dark-kitchen` (+ hermanos del PR),
   `whatsapp-gate`, `robots-gate`; render visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago --only …`; sitemap en GSC; correo a la cola (siguiente hueco EN) con su
   routine.
5. John decide los 3 testimonios retirados y si quiere una OG EN propia.
