# Taco Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 31-oct-2026. Implementador único de la F3 en `feat/taco-shop-checklists-en` (worktree compartido con
> la F2, que publicó los 11 xlsx EN en `astro-site/public/dl/taco-shop-checklist-templates/`, `12147364`). Molde: la F3 del
> Hotel Checklists Kit Pro (`../hotel/F3-NOTAS.md`) replicada punto por punto, con la del Pizza Shop (`../pizza/F3-NOTAS.md`)
> como segunda referencia. Commits `9fc50978` (registro) y `78e99f93` (ficha, páginas y lanzamiento). Sin build, Playwright
> ni navegador (regla térmica; CPU 43-47 °C toda la sesión).

## 1. Puntos de registro (los 25 del hotel, para `taco-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-taqueria.ts`) | `astro-site/src/data/productos-en/tareas/taco-shop-checklist-templates.ts` | ✅ $19, sin `priceOld`/`discountBadge`/`value`/`aggregateRating`/`review`; 9 plantillas + 3 bonus, 21 FAQ on-page + 6 en el JSON-LD, 8 testimonios sin marcas |
| 3 | Landing | `pages/en/digital-products/taco-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/taco-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/TacoShopChecklistsKitLibraryIsland.tsx`, `src/pages/TacoShopChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + `equivalents-guide`), claves e iconos del ES (02 = `trompo-plancha-comal`); cruza a Taco Shop Business Plan Kit, Restaurant Checklists y HACCP Food Safety Kit Pro (el ES: Guía Restaurante Mexicano, Kit Tareas y Pack APPCC) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-taqueria.astro` → `alternatesFamilia('kit-tareas-taqueria')` | ✅ (solo el `<head>`: va en `--esperadas /kit-tareas-taqueria`) |
| 7 | Familia `kit-tareas-taqueria` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` (+ `productos-digitales-config.ts`) | ✅ nombres = `SPEC.md` §2 = `dl/` en disco; `gate-flujo-postpago --offline`: 12 ficheros = 12 tarjetas |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (92 productos) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» (la versión de los xlsx es 2.0 · October 2026) |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ `$19`; + `digital-products-catalogue.json` (entrada EN, como las hermanas) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ «Taco Shop Checklists Kit Pro» (el nombre viejo «Tasks: Mexican Taquería» no sale en ningún uso EN: sin alias viejo) |
| 17 | Hub EN: «Recurring Tasks: Mexican Taqueria» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ una sola tarjeta (la vieja decía «EU allergen rules», «14 mandatory allergens», «Spanish campaigns»); imagen = hero EN; el Mega Pack sigue el último |
| 18 | `footerLinks`: 11 fichas de checklists y 5 kits + el plan hermano | 17 fichas EN | ✅ +1 línea cada una (tras Hotel; en el hotel, tras Pastry Shop; en el Taco Shop Business Plan Kit, tras Digital Products) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («34 products») | `astro-site/public/` | ✅ + fila del kit y mención en la tabla de checklists (19 USD) |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ 2026-10-31 |
| 21 | Blog EN: banners + párrafo | — | ❌ otra sesión |
| 22 | TEMAS para rebalanceos | — | ❌ otra sesión |
| 23 | `tienda-gate.py`: exentos (3 nombres con tilde + el subtítulo de la edición ES) y `/kit-tareas-taqueria` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ estático verde: «35 producto(s) vivos fuera de ES con data, páginas y zona-app» |
| 24 | Correo EN | `emails/broadcast-taco-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR (entra en la cola EN después); «Hi everyone,», negro #111 + dorado #FFD700, sin precio tachado |
| 25 | Cripto + devoluciones | plantilla | ✅ (render: las mismas 13 apariciones de la pasarela y la nota de reembolso que pizza y hotel) |

## 2. Verificación (ligera, sin build)

- Cifras contra los 11 xlsx EN (openpyxl, script en el scratchpad): **36 hojas, 298 tareas** (50 = 28 + 22 · 36 = 18 + 18 ·
  48 = 18 + 15 + 15 · 39 = 15 + 11 + 13 · 25 = 15 + 10 · 48 = 6 × 8 · 26 = 14 + 12 · 26 = 12 + 14), 5 filas verdes libres
  al pie de cada checklist, 09 con 3 secciones y 15 filas numeradas + 5 libres, B02 con 27 filas + 5 libres y nota UK
  (Mothering Sunday, bank holidays, Boxing Day), columnas E = Due by / Day / Frequency / Lead time, versión «2.0 · October
  2026». °F en los xlsx: −31, −4, 0, 32, 41, 70, 135, 145, 165; la ficha usa 0, 32, 41, 70, 135, 145, 155 y 165 (155 solo
  como cifra de algunos condados, dentro de `GRADOS_F_SPEC`); °C solo en la FAQ UK (8 / 63 °C). Las ≈ 90 frases clave de la
  ficha, el changelog y el correo, buscadas en el texto de los xlsx: todas están (solo faltan las 2 de control que no se
  afirman: sneeze guard, gluten). Ajustado tras el contraste: el enfriado en dos fases va en los checklists de cierre y
  guisados (no en «Temp Logs»), el 09 trae 3 secciones y 15 filas, y los puestos del changelog = los de la columna D.
- `es-identico-local/comparar.mjs` (una vez, CPU 47 °C): **ES idénticas 40 · distintas 0**; render EN 252.834 bytes:
  `revisar_texto` de `tienda-gate` sin fallos, 0 «€», 0 `aggregateRating`, `priceCurrency` USD; «Google Sheets» solo en las
  constantes de la plantilla (8, como pizza y hotel); «Taquería» solo en el subtítulo exento.
- `tienda-gate.py` estático (python 3.11) verde; `sync-product-prices.py --check` verde; `gate-flujo-postpago.py --offline
  --only taco-shop-checklist-templates`: 12 = 12, falla SOLO «SIN Payment Link» (esperado).
- esbuild (stdin) sobre los TS/TSX tocados y el frontmatter de los 4 `.astro` tocados: 0 errores (cazó una comilla sin
  escapar en un testimonio, corregida).
- **No hecho (necesita preview):** `tienda-gate --base`, `--es-identico --esperadas /kit-tareas-taqueria`, `whatsapp-gate`,
  `robots-gate`, render visual de landing, hub y dashboard.

## 3. Decisiones de contenido

- **Fuera lo que el ES afirma y el kit EN no trae:** «el software de gestión cobra €40/mes» (→ la fórmula de los hermanos),
  -80 %, «ahorra €55», «valorados en €49», rating 4,9 de 8 reseñas, RD 1021/2022 y sus 63 / 74 / 4 / −18 °C y «los 65 °C que
  ya no aplican» (→ FDA Food Code en °F: 145 °F en el trompo o la cifra del condado, 135 / 165 / 41 / 0 °F), los 14
  alérgenos de la UE (→ 9; UK 14), «estándar Sanidad», «Imprimible A4», «campañas españolas de terraza y Navidad» (→ Super
  Bowl, Cinco de Mayo, Memorial Day, Thanksgiving), «importador» (→ Mexican food distributor), «formación del equipo» del
  calendario anual (el B02 no la trae), «stock de tortilla» del briefing (el B01 trae 86s y la tortilla de harina sí/no), la
  Guía de Equivalencias ES↔LatAm (→ Equivalents Guide) y la FAQ de Google Sheets (sin test real). La caja: no hay libro de
  caja (D12); la FAQ lo dice y manda al Restaurant Checklists Kit Pro si se quiere la hoja por billete.
- **Testimonios (los 8, sin marcas):** traducidos tal cual con su rol y ciudad española y el subtítulo «…with Kit de Tareas
  Recurrentes: Taquería Mexicana, the Spanish edition of this kit». **Una frase cambiada** (regla de John, 11-oct): Carmen
  Ibáñez («las campañas españolas» y «chiles en nogada en otoño» → «the busy days» y «chiles en nogada season»: el
  calendario EN es de fechas US y la temporada va del 15-jul a finales de septiembre). En Sofía Ramírez «el producto del día»
  → «the day's trompo, guisados and salsas» (lo que trae el B01). **Avatares** reasignados para que género y oficio cuadren
  (en el ES, Guadalupe lleva un avatar de hombre): taquero → avatar-7, director → 1, consultor → 5, chef → 8, dueña → 2,
  encargada → 4, jefa de mostrador → 6 y, como solo hay 3 avatares de mujer, uno nuevo de tortillera (Nano Banana 2,
  `lovable-uploads/avatars-nicho/avatar-tortillera.jpg`, 66 KB, ≈ $0,07).
- **Imágenes:** abiertas las 6 del ES (`tareas-taqueria-hero`, `-trompo`, `-tortilleria`, `-salsas`, `-equipo`, `-tacos`):
  sin texto legible (la carta de la pared de `-salsas` y el portapapeles de `-equipo`, ilegibles al 100 %), sin logos → se
  quedan, con el reparto del ES. Descartada la OG del ES → `ogImage` = el hero.
- **FAQ:** 21 on-page (apertura y cierre con la intención «restaurant opening / closing checklist», temperaturas, al pastor
  145 °F, sin trompo, tacos por trompo —remite a la calculadora del plan hermano—, salsa bar y alérgenos, nixtamal,
  cómo se lleva una taquería, limpieza, plantilla gratis, ya rellenas, firma, fechas fuertes, apps tipo Trail, varios
  locales, caja, UK/CA/AU, moneda, suscripción, garantía) y 6 en el JSON-LD.
- **Pie y cruces:** los 11 hermanos EN de checklists, el Taco Shop Business Plan Kit, los 5 kits y el eBook; recíproco en
  el pie del plan. La FAQ del plan «Should I buy this or the Restaurant Checklists Kit Pro?» se deja como está (decisión de
  la familia de planes; cuando se toque, el par natural es este kit, como el plan de pizzería).

## 4. Pendiente

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/taco-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`.
2. `vivo: true` ya en la rama: fusionar SOLO con el link (los 11 xlsx ya están en `dl/`).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-taqueria`, `whatsapp-gate`, `robots-gate`, render
   visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago --only taco-shop-checklist-templates`; sitemap en GSC; correo a la cola EN
   con su routine.
5. Blog EN (puntos 21-22, otra sesión): posts EN de comida mexicana / tacos para banners. Aviso: el catálogo JSON EN de los
   banners no tiene el Taco Shop Business Plan Kit ni el Rotisserie Chicken (sí este kit desde hoy).
