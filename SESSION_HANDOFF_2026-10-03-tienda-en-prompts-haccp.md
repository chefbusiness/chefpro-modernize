# Handoff 3-oct-2026 (tarde) — Tienda internacional en inglés: Gastro Pro Prompts eBook + HACCP Food Safety Kit Pro

> Sesión Claude Code. Rotación de 3 sesiones → tocaba producto EN (ola 1). Reglas vigentes: PROPORCIONALIDAD (3-6 h por
> producto, sin supervisión), reparto Mac ↔ VPS, térmica del Mac (istats, cero Playwright/builds locales).

## 🔴 TAREA DE JOHN — dos Payment Links de Stripe (USD, Adaptive Pricing activado, como los EN anteriores)

| Producto | Precio | Redirección tras el pago | Env var (la pongo yo en Netlify, scope builds) |
|---|---|---|---|
| **Gastro Pro Prompts eBook** | **$14** | `https://aichef.pro/en/digital-products/ai-prompts-for-restaurants/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_AI_PROMPTS_FOR_RESTAURANTS` |
| **HACCP Food Safety Kit Pro** | **$19** (ancla $39) | `https://aichef.pro/en/digital-products/haccp-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_HACCP_KIT` |

Descripciones para el producto de Stripe (prosa, sin viñetas):

- **Gastro Pro Prompts eBook** — «300 ready-to-use AI prompts for chefs, restaurant managers, pastry chefs, bartenders,
  caterers and owners, organized by topic, role and business type, each with the AI Chef Pro agent it works best with.
  Includes a 73-page PDF, a private prompt library dashboard and two bonuses. One-time payment, lifetime access.»
- **HACCP Food Safety Kit Pro** — borrador, se confirma al cerrar su F2: «A complete set of ready-to-fill food safety logs
  and a HACCP hazard analysis in Excel, adapted to the FDA Food Code with UK notes: temperatures, receiving, cleaning,
  cooling, allergens, pest control, traceability and corrective actions. Bonuses included. One-time payment, lifetime access.»

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

## 2. HACCP Food Safety Kit Pro (ola 1, producto 4) — en curso

- Worktree `<scratchpad>/wt-haccp`, rama `feat/haccp-templates-en`. Duplicado del Pack APPCC (19 xlsx + 2 bonus), slug
  `haccp-templates`, $19. Demanda US: «haccp plan template» 390 · «food safety plan template» 170 · «food temperature log
  template» 140 · «haccp template» 110; UK «haccp template» 140.
- F1 (un Opus, ≤ 0,5 M) → F2 (textos por Sonnet + `aplicar_en.py` calcado del Restaurant Inventory Kit, en el VPS) → F3.

Sesión Claude Code · `Via: Claude Code`.
