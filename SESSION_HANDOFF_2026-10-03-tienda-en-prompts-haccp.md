# Handoff 3-oct-2026 (tarde) — Tienda internacional en inglés: Gastro Pro Prompts eBook + HACCP Food Safety Kit Pro

> Sesión Claude Code. Rotación de 3 sesiones → tocaba producto EN (ola 1). Reglas vigentes: PROPORCIONALIDAD (3-6 h por
> producto, sin supervisión), reparto Mac ↔ VPS, térmica del Mac (istats, cero Playwright/builds locales).

## 🔴 TAREA DE JOHN — cuatro Payment Links de Stripe (USD, Adaptive Pricing activado, como los EN anteriores)

| Producto | Precio | Redirección tras el pago | Env var (la pongo yo en Netlify, scope builds) |
|---|---|---|---|
| **Gastro Pro Prompts eBook** | **$14** | `https://aichef.pro/en/digital-products/ai-prompts-for-restaurants/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_AI_PROMPTS_FOR_RESTAURANTS` |
| **HACCP Food Safety Kit Pro** | **$19** (ancla $39) | `https://aichef.pro/en/digital-products/haccp-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_HACCP_KIT` |
| **Restaurant Staff Scheduling Kit Pro** | **$19** (ancla $59) | `https://aichef.pro/en/digital-products/restaurant-schedule-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT` |
| **Restaurant Financial Plan Kit Pro** | **$49** (ancla $199) | `https://aichef.pro/en/digital-products/restaurant-financial-plan-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT` |

Descripciones para el producto de Stripe (prosa, sin viñetas):

- **Gastro Pro Prompts eBook** — «300 ready-to-use AI prompts for chefs, restaurant managers, pastry chefs, bartenders,
  caterers and owners, organized by topic, role and business type, each with the AI Chef Pro agent it works best with.
  Includes a 73-page PDF, a private prompt library dashboard and two bonuses. One-time payment, lifetime access.»
- **HACCP Food Safety Kit Pro** — «19 ready-to-fill food safety templates in Excel, including a HACCP plan with hazard
  analysis, built on the FDA Food Code 2022 with UK notes: temperatures in °F with automatic alerts, two-stage cooling, receiving,
  cleaning and sanitizing, allergens (US 9 and UK 14), traceability and a health inspection self-checklist. Two bonuses.
  One-time payment, lifetime access.»
- **Restaurant Staff Scheduling Kit Pro** — «Seven Excel templates and two bonuses to schedule your restaurant team and
  control labor cost: weekly and monthly staff schedule with alerts, FLSA overtime by workweek, labor cost by pay period,
  onboarding, PTO, performance reviews and a staff directory. One-time payment, lifetime access.»
- **Restaurant Financial Plan Kit Pro** — «Ten Excel templates to plan and track your restaurant's finances: 3- and
  5-year projections, monthly P&L actual vs budget, break-even, cash-flow forecast, startup costs, a ratios dashboard and
  a lender & investor summary with DSCR and IRR. One-time payment, lifetime access.»

Con el link: env var → `python3 scripts/productos-digitales/sync-payment-links.py` en la rama → merge → gates LIVE.

## 1. Gastro Pro Prompts eBook (ola 1, producto 3) — PR #106, listo a falta del Payment Link

- Rama `feat/pro-prompts-ebook-en`. SPEC y pipeline en `scripts/productos-digitales/pro-prompts-ebook-en/`.
- Entregables en `astro-site/public/dl/ai-prompts-for-restaurants/`: eBook PDF 73 págs (300 prompts), Bonus 1 .docx, Bonus 2+3 .xlsx.
- Gates contra el preview `deploy-preview-106`: `tienda-gate` verde, `gate-flujo-postpago --only ai-prompts-for-restaurants`
  3/3 descargas + cripto (solo falla el Payment Link, esperado), Miselup 102/102 y 0 en EN, DataFast 23/23, `/pro-prompts-ebook`
  solo cambia en hreflang + og:locale.
- Correo EN listo: `scripts/productos-digitales/emails/broadcast-ai-prompts-for-restaurants-lanzamiento-en.html`. Cola EN:
  último envío al segmento EN el 5-oct 14:00Z → **este, el 10-oct 14:00Z** (comprobar que ese día no sale un correo ES).

### Revisión Opus final (1 ronda): 2 bloqueantes + 4 mayores + 11 menores, TODOS arreglados en el EN

Lo grave venía **heredado del ES** (la traducción fiel lo arrastró). **Pendiente en el producto ES `pro-prompts-ebook`**
(no se ha tocado; para una v1.0.1 cuando John diga):
- Landing (`ProPromptsEbookPage.astro`): promete el «framework CRAFT» y «respuestas 10x» (:165) que no existen en el
  producto (el Bonus 1 enseña 5 elementos: Rol, Contexto, Tarea, Parámetros, Formato); «Dashboard exclusivo con todos los
  prompts» (:124, :553) cuando el dashboard tiene 76 prompts distintos de los 300; «300 prompts en 12 categorías» (:420)
  frente a 3 bloques/33 secciones; «El recurso #1» (:329) y «Únete a miles» (:709) sin respaldo.
- Bonus 1 (.docx): «los 80 prompts del eBook» (son 300) y «el 80 % de los profesionales…» sin fuente.
- Bonus 3 (.xlsx): A2 manda buscar en el eBook unos números que son del dashboard (#27 del eBook es APPCC, no un post de
  Instagram) y la fila «Generador maestro de prompts» no existe en ningún sitio; «hasta un 40 %» sin fuente.

## 2. HACCP Food Safety Kit Pro (ola 1, producto 4) — PR #107, listo a falta del Payment Link

- Rama `feat/haccp-templates-en` (apilada sobre #106: **fusionar #106 primero**). SPEC, pipeline y notas en
  `scripts/productos-digitales/haccp-kit/` (`SPEC.md` D1-D27, `F2-NOTAS.md` con cómo reconstruir en el VPS).
- 21 xlsx EN en `astro-site/public/dl/haccp-templates/` (19 registros + 2 bonus), FDA Food Code 2022 en °F + notas UK,
  Letter. Construidos en el VPS (`aplicar_en.py --idempotencia` + `inject_cache` al final): `gates_en.py` G1-G8 verde,
  autotest 10/10, `censo-entregables` 0, `gate-no-latinos` 0.
- Excepciones estructurales D13 (cocción 5 procesos), D14 (enfriamiento en dos tramos), D15-D16 (fila de horas):
  las exige la norma US. **Se le preguntó a John y no hacía falta** (ya decidido en TIENDA §1): ver CLAUDE.md y la memoria
  `feedback_adaptacion-mercado-en-ya-decidida`.
- Revisión Opus final: 0 bloqueantes, 3 mayores (salud del empleado §2-201, acción correctiva del enfriamiento,
  concentración de desinfectante en ppm) + 12 menores → todos arreglados y reconstruido (`b10eafd9`). Galería con 3
  fotos propias sin texto (`haccp-en-*.jpg`) y OG `og-haccp-kit.jpg` (`f90c71a2`, `d6699981`).
- Preview `deploy-preview-107`: `tienda-gate` verde (`/pack-appcc` solo cambia en hreflang), 21/21 descargas, Miselup
  102/102 y 0 en EN. Solo faltan los Payment Links.
- Correo EN: `scripts/productos-digitales/emails/broadcast-haccp-templates-lanzamiento-en.html` → **15-oct 14:00Z**
  (cola EN: eBook 10-oct; el 14-oct sale un correo ES, el 15 está libre).

## 2b. Restaurant Staff Scheduling Kit Pro (ola 3, producto 5) — PR #108, listo a falta del Payment Link

- Rama `feat/restaurant-schedule-templates-en` (apilada sobre #107 → #106: **fusionar #106 → #107 → #108**). SPEC, pipeline y
  notas en `scripts/productos-digitales/staff-kit/` (`SPEC.md` D1-D24, `F2-NOTAS.md` §6 «Revisión final»).
- 9 xlsx EN en `astro-site/public/dl/restaurant-schedule-templates/` (7 + 2 bonus): FLSA (horas extra > 40 h por semana
  laboral a 1,5×, umbral diario estatal opcional), coste laboral por periodo de pago con % de cargas del empleador editable,
  onboarding (I-9, W-4…), PTO sin mínimo federal, notas UK («rota», WTR 48 h/11 h, 5,6 semanas, NI 15 %). Sin afirmar
  Google Sheets hasta un test real (SPEC). Construidos en el VPS: gates G1-G8 verde, autotest 13/13, idempotencia 0.
- Revisión Opus final: 1 bloqueante (las horas extra de una semana que cruza meses se perdían entre copias mensuales →
  cada copia guarda semanas COMPLETAS), 3 mayores (alertas de menores 14-15 vs 16-17, promedio de horas heredado de
  España, semana del cuadrante lunes vs domingo → B3 por defecto lunes) + 10 menores → todos arreglados (`f9f973cf`).
- Preview `deploy-preview-108`: `tienda-gate --es-identico --esperadas /kit-gestion-personal,/pack-appcc` verde, 9/9
  descargas, Miselup 102/102. Imágenes propias sin texto (`og-staff-scheduling-kit.jpg`, `staff-en-*.jpg`).
- Correo EN: `scripts/productos-digitales/emails/broadcast-restaurant-schedule-templates-lanzamiento-en.html` →
  **20-oct 14:00Z** (cola EN: 10-oct eBook, 15-oct HACCP; los ES del 19 y 24 no chocan).

## 2c. Restaurant Financial Plan Kit Pro (ola 3, producto 6) — PR #109, listo a falta del Payment Link

- Rama `feat/restaurant-financial-plan-templates-en` (apilada: **fusionar #106 → #107 → #108 → #109**). SPEC D1-D37 y notas
  en `scripts/productos-digitales/financial-kit/` (`F2-NOTAS.md` §6 «Revisión final» con los defectos a corregir en el ES).
- 10 xlsx EN (8 + 2 bonus) en `astro-site/public/dl/restaurant-financial-plan-templates/`: sales tax/VAT fuera de ingresos,
  impuestos editables, préstamo tipo SBA 7(a) con periodo de solo intereses, DSCR «at full payment», amortización por vida
  útil, sq ft; 9 gráficos con las pestañas renombradas; TIR en caché. VPS: gates G1-G8 verde, autotest 27/27, idempotencia 0.
- Revisión Opus final: 0 bloqueantes, 6 mayores (DSCR inflado con carencia, «mínimo SBA 1,15×» quitado, plazos de proveedor
  > 30 días rompían la tesorería —también en el ES—, base del sales tax, benchmarks presentados como norma, imagen con rótulo)
  + 15 menores → todos arreglados (`9ae0654e`). Aviso «planning tool, not financial, tax or legal advice» en los 10 libros.
- Preview `deploy-preview-109` en verde (10/10 descargas). Correo EN:
  `scripts/productos-digitales/emails/broadcast-restaurant-financial-plan-templates-lanzamiento-en.html` → **25-oct 14:00Z**.

## 3. Al volver John con los dos Payment Links

1. Env vars en Netlify (scope builds, contexto all): `VITE_STRIPE_PAYMENT_LINK_AI_PROMPTS_FOR_RESTAURANTS`,
   `VITE_STRIPE_PAYMENT_LINK_HACCP_KIT`, `VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT` y `VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT`; comprobar con la CLI de Stripe importe USD y redirección `…/access?session_id=`.
2. En la rama del eBook: `python3 scripts/productos-digitales/sync-payment-links.py` → commit → merge #106 → gates LIVE
   (`gate-flujo-postpago.py --only ai-prompts-for-restaurants`, `tienda-gate.py --base https://aichef.pro`).
3. Rama del HACCP: `git merge origin/main`, `sync-payment-links.py` → merge #107 → gates LIVE con `--only haccp-templates`.
   Igual con #108 (`--only restaurant-schedule-templates`) y #109 (`--only restaurant-financial-plan-templates`).
4. Programar los 4 correos EN (10, 15, 20 y 25-oct, 14:00Z; comprobar antes que el 25 no hay correo ES) con `scripts/productos-digitales/emails/resend-broadcast.py` (prueba a John con `--test`).
5. Limpiar worktrees: `git worktree remove <scratchpad>/wt-haccp`, `wt-staff` y `wt-fin`; las ramas `-f3` ya están fusionadas.

## 4. Pendientes que NO son de estos productos

- Verificación humana antes de vender (recomendación de Claude, 3-oct): abrir 2-3 xlsx de cada kit en Excel/LibreOffice
  (colores, impresión, gráficos del Plan Financiero) y repasar las 4 landings en el Chrome de Windows a escritorio y a 360 px.
- ES `kit-plan-financiero`: defectos heredados listados en `financial-kit/F2-NOTAS.md` §6 (plazos de proveedor > 30 días,
  DSCR con carencia, tipo 0 %, benchmarks de ocupación/GOP sin evaluar) para su próxima v2.x.

- ES `pro-prompts-ebook`: las afirmaciones falsas listadas en §1 (v1.0.1 cuando John diga).
- `use-cases-content.en.ts`: ~40 menciones tipo «Pizzeria HACCP Kit» prometen funciones que el kit no tiene (registro
  móvil, exportar PDF, normativa UE/Latam). Revisarlas en una sesión de contenidos.
- `photoanalysisd` congelado en el Mac (`pkill -STOP`); reanudar con `pkill -CONT photoanalysisd` cuando se quiera.

Sesión Claude Code · `Via: Claude Code`.
