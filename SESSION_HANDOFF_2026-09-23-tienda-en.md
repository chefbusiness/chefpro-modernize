# Handoff 23→24 sep 2026 — Tienda internacional de productos digitales, frente EN (sesión Claude Code)

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
2. **0.C Hub EN** (siguiente sesión EN):
   - `TiendaHubPage.astro` + `pages/en/digital-products.astro`.
   - Copy con bridge.py; imágenes con `generate-images`.
   - Activar `TIENDAS.en.activa`.
   - Enlaces en los 4 ficheros de navegación y CTA en la portada EN.
   - `alternates` recíprocos en el hub ES.
   - Gates.
3. **Piloto Recipe Costing Kit** (F1/F2/F3), con el checklist §6 del doc. Riesgos que ya conocemos:
   - falta la página `/en/crypto-payment`;
   - `CryptoPayButton.astro` todavía no tiene `lang`;
   - un precio `usd` exige `lang: 'en'` en PRODUCTS;
   - falta la entrada en `admin-generate-access.ts`;
   - `miselup-gate` necesita ajuste;
   - **John: el aviso de desistimiento de 14 días del correo cripto EN es de la norma UE; decidir qué va para EE. UU.**
   - **John crea el Payment Link USD** (lo único no delegable).

## Lecciones (detalle en el log del doc)
- Compilar con `@astrojs/compiler` + esbuild en el scratchpad cualquier `.astro` tocado **antes** de subir. Así se evita el build roto por template literals o backslashes dentro de las expresiones.
- Los 500 «Error - Request ID» de 46 bytes tras ráfagas de gates vienen de la IP, no del sitio. Contrastar con el Chrome de Windows antes de alarmarse.
