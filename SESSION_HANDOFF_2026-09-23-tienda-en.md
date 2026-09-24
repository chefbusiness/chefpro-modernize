# Handoff 23→24 sep 2026 — Tienda internacional de productos digitales (sesiones Claude Code)

**Doc canónico (leer ENTERO antes de seguir):** `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`

## Qué se decidió (John, 23-sep)
- El frente EN arranca YA; va en **rotación de 3 sesiones**: v2.0 ES → producto nuevo ES → producto EN.
- Mercado: inglés US como base internacional, con parámetros de impuesto, moneda y unidades en los Excel, y anexos US (FDA) y UK (FSA).
- Precios en USD con precio psicológico, más Adaptive Pricing de Stripe.
- Piloto: **Recipe Costing Kit** (= kit-escandallos).
- URLs anidadas: `/en/digital-products/<slug>` (+ `/access`, `/library`).
- Plantillas parametrizadas con `lang`, no copias por idioma.
- En EN no se muestran reseñas ni ratings hasta que haya compradores reales.

## Qué quedó hecho
| Fase | Estado | Commit |
|---|---|---|
| 0.A research US/UK + doc canónico + calendario | ✅ | `954366e` |
| 0.B infraestructura (registro `tienda.ts`, robots/sitemap anidados, `KitExcelLandingPage` con `lang`, backend con idioma y USD, `tienda-gate.py`) | ✅ LIVE, sin cambios visibles | PR #93 → `42a6878` |
| Log con lecciones | ✅ | `30a1175` |

Verificación de la 0.B:
- 5/5 landings KitExcel ES salen byte a byte idénticas (`tienda-gate.py --es-identico`).
- `robots-gate` en verde.
- Emails, facturas cripto y gate ES idénticos para los 50 productos (render antes y después).

## Pendiente
1. **Repetir `gate-flujo-postpago.py` LIVE** desde otra red o espaciado. El 23-sep dio 186 «fallos» que eran 500 de Netlify contra la IP del Mac: el Chrome de Windows dio 40/40 en 200 y el deploy anterior fallaba igual.
2. ~~**0.C Hub EN**~~ ✅ LIVE el 24-sep (PR #94) y **REHECHO** el mismo día como copia del hub ES (PR #95) — ver bloque del 24-sep abajo. Era:
   - `TiendaHubPage.astro` + `pages/en/digital-products.astro`.
   - Copy con bridge.py; imágenes con `generate-images`.
   - Activar `TIENDAS.en.activa`.
   - Enlaces en los 4 ficheros de navegación y CTA en la portada EN.
   - `alternates` recíprocos en el hub ES.
   - Gates.
3. **Piloto Recipe Costing Kit** (SIGUIENTE sesión EN; al publicarlo: `vivo: true` en FAMILIAS + precio `usd` + `omitGlobalApp` en sus páginas) (F1/F2/F3), con el checklist §6 del doc. Riesgos que ya conocemos:
   - falta la página `/en/crypto-payment`;
   - `CryptoPayButton.astro` todavía no tiene `lang`;
   - un precio `usd` exige `lang: 'en'` en PRODUCTS;
   - falta la entrada en `admin-generate-access.ts`;
   - `miselup-gate` necesita ajuste;
   - **John: el aviso de desistimiento de 14 días del correo cripto EN es de la norma UE; decidir qué va para EE. UU.**
   - **John crea el Payment Link USD** (lo único no delegable).


## 🔴 Sesión Claude Code del 24-sep (tras el apagón térmico de la madrugada)

**Recuperación:** la sesión anterior murió con el PR #94 fusionado y su deploy de producción FALLIDO (exit 4, transitorio:
mismo árbol que el preview verde). Se relanzó el build y se commitearon los docs que quedaron sin commitear.

**Regla nueva de John (permanente, todos los idiomas):** el español lleva siempre la delantera. Otro idioma = **DUPLICAR** lo
español (landing, dashboard, ficheros xlsx/pdf/docx/md, hubs) y **traducirlo**, adaptando las variables del mercado. Nunca
componentes, plantillas ni diseños nuevos. «Nativo» = traducido al idioma de destino, no rehecho. Está en `CLAUDE.md`, §1 del
doc canónico y la memoria `feedback_version-idioma-duplicar-no-reconstruir`. Nomenclatura: «Tienda internacional en <idioma>»
(§0 del doc). El hub EN de la PR #94 se construyó desde cero y John lo rechazó: se tiró.

| Hecho | PR / commit |
|---|---|
| Hub EN = copia traducida de `ProductosDigitalesHubPage.astro` (`DigitalProductsHubPage.astro`); 50 tarjetas «Coming soon in English» sin precio ni enlace; sin estrellas ni 4,9/5; `TiendaHubPage.astro` borrado | PR #95 → `b181f1d` |
| Hubs FR/DE/IT/PT/NL = copias traducidas del EN (bridge.py + Sonnet de respaldo); tiendas activadas; `hubLocales()`/`hubAlternates()` → hreflang recíproco de los 7; enlace en menú/menú móvil/pie de cada portada; robots.txt y `tienda-gate.py` para todas | PR #96 → `4c66731` |
| Verificado LIVE: 7 hubs 200; cada portada enlaza a su hub y a ningún otro; menú en una fila a 1.362 px en los 7 idiomas (Chrome de Windows); 0 desbordes a 360 px; 50/50 imágenes | — |

**Decisiones tomadas por Claude (delegadas):** sin rating en los hubs no-ES; ciudades como texto sin enlace fuera del ES;
`TiendaStrip` (franja de tienda de la portada EN, invento de la PR #94 que la portada ES no tiene) NO se replicó a otros
idiomas — **pregunta abierta para John: ¿se quita también de la portada EN?**

## ▶️ Mañana: primer producto en inglés — Recipe Costing Kit (= `kit-escandallos`)
Cómo, según la regla nueva:
1. **Duplicar**, no construir: landing (`KitExcelLandingPage` ya acepta `lang` desde la 0.B → misma plantilla, texto EN),
   dashboard `-library` y **los ficheros** del kit ES → traducir y adaptar variables (moneda/impuesto/unidades como
   parámetros, anexos FDA/FSA). Mismo diseño y componentes.
2. Rutas: `/en/digital-products/recipe-costing-kit` (+ `/access`, `/library`). Al publicar: `vivo: true` en `FAMILIAS.en`,
   precio `usd` en `product-prices.ts`, `omitGlobalApp`. La tarjeta del hub EN pasa sola a enlace con precio.
3. Riesgos conocidos del punto 3 de «Pendiente» (arriba): `/en/crypto-payment`, `lang` en `CryptoPayButton`,
   `admin-generate-access.ts`, `miselup-gate`, desistimiento para EE. UU. **John crea el Payment Link USD.**
4. Política de 3 fases (F1/F2/F3) con gate + commit en cada una; tamaño M (≤ 5 M tokens de subagentes).

## Lecciones (detalle en el log del doc)
- Compilar con `@astrojs/compiler` + esbuild en el scratchpad cualquier `.astro` tocado **antes** de subir. Así se evita el build roto por template literals o backslashes dentro de las expresiones.
- Los 500 «Error - Request ID» de 46 bytes tras ráfagas de gates vienen de la IP, no del sitio. Contrastar con el Chrome de Windows antes de alarmarse.
