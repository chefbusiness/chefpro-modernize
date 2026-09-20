# Handoff 2026-09-20 — Política de 3 fases + «Tareas Recurrentes: Taquería Mexicana» (sesión Claude Code)

Producción = `main`. Política nueva de John (decisiones delegadas a Claude): `CALENDARIO-V2-SEMANAL.md` §3 y `CLAUDE.md`.

## F1 Fundamentos — CERRADA (gate de script en verde)
- Research `kit-tareas-taqueria/01-research-taqueria-mexicana.md` (601 líneas) · SPEC `02-SPEC-kit-tareas-taqueria.md`
  (862 líneas; refutada en ronda única → 24 correcciones aplicadas → `gate_f1_spec.py` PASS) · contrato del molde v2.0
  `03-contrato-molde-v2.md` + volcados `molde-referencia*.json` (`extraer_molde.py`).
- Decisiones: 14 € / `priceOld '€69'`; BONUS-02 en molde calendario NO-CB; 300 tareas (270-330) en 22 hojas; molde
  canónico = kit base v2.0 (sushi-bar y 5 más siguen en v1.1 CB); Mega Pack fuera; env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA`.
- Consumo F1: research 0,24 M · SPEC 0,21 M · refutación 0,28 M · fixer 0,28 M = **1,0 M** de los 2,5 M del producto.

## F2 Entregables — CERRADA (gates de script en verde)
- `scripts/generate-tareas-taqueria.py` (helpers del molde v2.0 + loader de `contenido/contenido_a.py` (01-04, 173 tareas) y
  `contenido_b.py` (05-08 + 09 + bonus, 125 tareas)) → `astro-site/public/dl/kit-tareas-taqueria/` (11 xlsx, caché inyectada).
- Verificado: generador == post-motor celda a celda (0 diferencias) · `main.py --dry-run --origen` TODO VERDE (11/11 en
  alcance, idempotencia 0) · `comparar_molde.py` 9/9 · `gate_f2_contenido.py` PASS (298 tareas, rango 270-330) ·
  `censo-entregables --only --fail` 0 · `gate-no-latinos` 0. **`postprocess-transversal` NO se corre** (v1.1: degradaría el kit).
- Trampas cazadas: `main.py` tiene el scratchpad de OTRA sesión hardcodeado (`CLAUDE_SCRATCHPAD=$SP` al invocarlo);
  `motor.cadencia` retitula la columna de tiempo por CONTENIDO (07 mensual solo `1º de mes/Quincenal/Mensual/Fin de mes`,
  08 con «antes/víspera/día siguiente/al confirmar»); las colas de «Se conecta con» de 07/08/bonus las escribe el motor
  (`COLA_MOTOR` en el generador, pegadas del dry-run); `texto_appcc` añade la coletilla del Pack a toda celda con APPCC.
- Consumo F2: helpers 0,31 M · redactores 0,24 + 0,22 M = **0,77 M**. Acumulado producto: **1,77 M** de 2,5 M.

## F3 Producto y lanzamiento — HECHA salvo el Payment Link (PR #85, rama `feat/kit-tareas-taqueria`, commit `87a6edc`)
- Capa de producto completa (1 Sonnet + revisión de Fable): ficha, landing Astro, gate/dashboard SPA + island, zona app
  generada (`fase5-generate-zona-app.py` 49→50), App.tsx, catálogo (sin comentarios en `description`), config, changelog
  **v2.0** (nace en el molde 2.0 de la familia, como dicen sus Excel), 4 functions, `product-prices.ts` (50),
  `payment-links.ts` con placeholder `''` + comentario PENDIENTE, hub ×2 (posición 1, 21 en «Próximos», ItemList JSON-LD =
  orden real, sin Mega Pack), cesta del use-case `restaurante-mexicano`, `footerLinks` de la guía mexicana → kit,
  7 imágenes Gemini (OG 1200×630 + galería 1600×893, 0,60 $). **No se creó landing SPA** (ningún producto post-cutover
  la tiene; la landing Astro es data-driven desde la ficha). ºC→°C en 16 sitios.
- **Preview verificado** (`https://deploy-preview-85--aichefpro.netlify.app`): landing 200 sin noindex, 3 puertas cripto,
  `-access`/`-library` con noindex, hub con la Taquería 1.ª y el Mega Pack último, OG/galería/xlsx 200, `miselup-gate`
  100/100, `gate-flujo-postpago --base … --crypto-products all --crypto-exclude pro-prompts-ebook`: 50 productos, la
  taquería 11/11/11, 7 fallos TODOS esperados (4 del eBook por `--base`, 2 del Payment Link ausente, 1 botón `#comprar`).
- **Correo de lanzamiento redactado** (`emails/broadcast-kit-tareas-taqueria-lanzamiento-es.html`, negro/dorado, asunto
  «Nuevo: Kit de Tareas Taquería Mexicana — 298 tareas, 14€»). **NO programado ni probado todavía**: (a) la prueba exige
  las imágenes vivas en producción (solo tras el merge); (b) la cola de Resend acaba el 19-oct (Kit Pastelería 2.1), el
  hueco del 24-oct es de la Chocolatería (programable desde el 24-sep) → **la Taquería va el 29-oct 08:00 UTC, programable
  desde el 29-sep** (tope de 30 días de Resend). Si la Chocolatería pasa al 29-oct (D53), la Taquería al 3-nov.
- Consumo F3: capa 0,34 M · imágenes 0,14 M · correo 0,14 M = **0,62 M**. **Producto entero: 2,39 M de 2,5 M** (F1 1,0 ·
  F2 0,77 · F3 0,62). Reloj: F1+F2+F3 en una sola sesión con tres cortes, sin panics.

### Cómo cerrar (orden exacto)
1. **John**: producto + Payment Link en Stripe (paquete abajo) y env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA` en Netlify (scope builds).
2. Claude: URL en `netlify/shared/payment-links.ts` (sustituir el `''`), commit en la rama, merge de la PR #85, esperar deploy.
3. Gates LIVE: `python3 scripts/productos-digitales/gate-flujo-postpago.py` sin flags (esperado 50 / 722 / 0) ·
   `miselup-gate.py` · `python3 scripts/astro-migration/hub-gate.py --first /kit-tareas-taqueria --n 50 --coming 21` ·
   curl del checkout cripto con email `qa-…@aichef.pro` (crea pedido: purgar después) · reenviar sitemap a GSC.
4. Correo: `resend-broadcast.py --test john@chefbusiness.co` (ya con imágenes vivas) y el **29-sep** `--scheduled-at
   2026-10-29T08:00:00Z` (leer antes la cola: regla `feedback_resend-reprogramar-sin-borrar-a-ciegas`).
5. Memoria/calendario: marcar LIVE, quitar la Taquería de la cola de «Próximos» del calendario §3, siguiente producto del
   top-20 = **Kit Cuadro de Mando Operativo** (M, 19 €, 2 sesiones) o **Plan de Negocio Hamburguesería Smash** (M, 35 €).

### Paquete Stripe para John (único paso no delegable)
- **Nombre del producto:** Tareas Recurrentes: Taquería Mexicana
- **Precio:** 14,00 € (pago único) · **moneda:** EUR
- **Descripción (259 caracteres, prosa, sin bullets):** Kit de Tareas de taquería mexicana: 11 Excel con 298 tareas en 22 checklists de apertura, cierre, trompo, tortillería, salsas y alérgenos, manager y perfiles, más briefing pre-servicio y calendario anual. Pago único, acceso vitalicio. Excel, Sheets o Numbers.
- **Confirmation URL (tras el pago):** `https://aichef.pro/kit-tareas-taqueria-access?session_id={CHECKOUT_SESSION_ID}`
- **Env var en Netlify (scope builds):** `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA` = URL del Payment Link
- Cripto: nace con NOWPayments (`CRYPTO_PRODUCTS=all`); el importe sale de `product-prices.ts` (regenerado en F3).
