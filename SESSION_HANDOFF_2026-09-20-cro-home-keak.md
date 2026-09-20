# Handoff 2026-09-20 — CRO de las portadas (recomendaciones de Keak) · sesión Claude Code

Producción = `main` = `e86b2ff` (árbol limpio, empujado). La sesión original se cerró a la fuerza (Claude dejó de
responder) y este handoff se escribió en una sesión de cierre posterior, tras verificar producción con curl en los 7 idiomas
(«profesionales», «de más de 32 países» y «recetas, procesos y soluciones generadas» de cada JSON + `data-social-chefs`).

## Qué hay en producción (7 idiomas, 127 páginas)
- **Hero** (`astro-site/src/components/Hero.astro`): H1 «Crea, gestiona y haz crecer tu {Restaurante…} con AI Chef Pro»
  (solo rota la palabra de negocio; DE/IT/PT llevan el artículo con género dentro de la palabra), subtítulo «…para
  restaurantes y negocios de hostelería», prueba social **dinámica** «Con la confianza de 764+ profesionales de más de
  32 países · N recetas, procesos y soluciones generadas», badge de cifras apilado, CTA doble y microcopy «Planes desde
  10 €/mes · 16 herramientas conectables (Gmail, Sheets, Outlook…)».
- **Business Tools** (`BusinessToolsShowcase.astro`) bajo las cocinas del mundo: Waste GenCal protagonista, 5 agentes, CTA a precios.
- **Pricing v2** (`Pricing.astro` + gemelo React `src/components/PricingV2.tsx` para las 113 páginas con island): chips de
  rol, Premium Plus «más popular», Max/anual aparte, hint del Miembro cualitativo (decisión delegada), primera
  característica «75+ agentes y herramientas incluidos». UTM: `utm_medium` = home-pricing/pricing/landing-<slug>/tool-<slug>.
- **Franja de cifras** (`SocialProofStrip.astro`): el 764+ dinámico y «15+ herramientas para conectar» en vez de «1 agente/semana».

## Cómo se retoca el copy (NO editar los `v2_*` a mano en los JSON)
1. Editar `DECISIONES_JOHN` u `OVERRIDES` en `scripts/cro-home/merge-keak-copy.py`.
2. `python3 scripts/cro-home/merge-keak-copy.py --todos && python3 scripts/cro-home/merge-keak-copy.py --check`.
3. PR → gate `python3 scripts/cro-home/keak-dist-gate.py --base https://deploy-preview-N--aichefpro.netlify.app` (127/127).
4. Merge → `keak-dist-gate.py --base https://aichef.pro`. Sin build local ni Playwright (regla térmica).

## Contador dinámico de chefs (John preguntó dos veces si era fijo: NO lo es)
`astro-site/src/lib/social-counts.ts`: `dynamicChefs()` parte de 764 el 20-sep-2026 y suma 2-3 al día de forma
determinista por fecha; `dynamicSolutions()` es el antiguo `getDynamicCount()`. `SocialCountLive.astro` lo recalcula en
cliente (`[data-social-chefs]`) si el build es de otro día, así que no depende de redesplegar. Revisar la base contra
la plataforma cada pocos meses para que no se vuelva falsa.

## Pendientes (no bloquean)
- 3 copias de `getDynamicCount()` sin migrar: `UseCasePageContent`, `UseCasesHubPage`, `ConsultoriaGastroProHubPage`.
- Clave `stats.chefs` huérfana en los 7 JSON de `src/i18n/locales/`.
- Revisión de fondo de los copies «hostelería en general, no solo cocina» (John, sesión propia; memoria
  `feedback_copies-hosteleria-no-solo-cocina`).
- Vigilar en GSC las consultas genéricas de la portada y en Ads/GA las series nuevas de `utm_medium`/`utm_content`.

## Referencias
`CRO_HOME_KEAK_2026-09-20.md` (spec + decisiones + retoques) · PR #86 (`d693c11`) · commits posteriores `548a1d5`,
`1f32f2d`, `d58f176`, `f29a0e8`, `39ce6ec`, `e86b2ff` · `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8 (entrada 2026-09-20 tarde/noche).

---

# Handoff 2026-09-20/21 (noche) — DataFast: analítica + atribución de ingresos · sesión Claude Code

Producción = `main` (ver último commit). Doc operativa en `CLAUDE.md` («Analítica: DataFast en todo el sitio»).

## Hecho y verificado
- **DataFast en aichef.pro** (PR #87 `fe8adfd` + PR #88 `bed88fb`): `components/DataFast.astro` montado en `BaseLayout`
  tras `<GoogleTag />`, modo híbrido según la cookie `aichef_consent` (cookieless sin «Aceptar», script estándar con él),
  solo bajo `aichef.pro`, **inyectado de inmediato desde el head** (no en `DOMContentLoaded`) para ganar la carrera con
  `ProductAccessGate`, que hace `window.location.replace` al dashboard nada más verificar. Gate
  `scripts/astro-migration/datafast-gate.py` 17/17 en preview y producción.
- **Pickaxe, los 7 workspaces** (ES `aaee43ff`, EN `d09bd252`, FR `2721aa1c`, DE `639b9cfd`, PT `b7f121de`, IT `51799471`,
  NL `e16796af`): snippet híbrido autocontenido en `Settings → Deploy → Workspace Level Custom code → Header`, verificado
  recargando cada editor y por el HTML servido de los 7 subdominios (`app`, `enapp`, `frapp`, `deapp`, `itapp`, `ptapp`, `nlapp`).
- **Atribución de ingresos (Payment Links)**: Stripe conectado por John; los links ya devuelven a `-access?session_id=`;
  cableado verificado en el Chrome de Windows (se carga el script, se llama a `verify-purchase` y sale el XHR a
  `datafa.st/api/events`). El punto «Attribute payments» del widget se marca solo con el primer pago real atribuido.

## Cómo retomar / pendientes
- **Primera venta real** → comprobar en el panel que aparece atribuida (referrer, país). Si no: `CLAUDE.md` § DataFast.
- **Suscripciones de Pickaxe** (no atribuibles por visitante: vuelven a `?success=login` sin `session_id`): vía candidata =
  método por email `window.datafast("payment",{email})` en «Confirmation Page Header/Footer» del workspace
  (https://datafa.st/docs/stripe-other-methods.md); el snippet B de Google Ads ya captura el email del alta en una cookie
  de 900 s. Necesita una suscripción real de prueba.
- **Proxy anti-bloqueadores** (`/js/script.js`, `/api/events`): solo tras demostrar que Netlify reenvía la IP real
  (en cookieless la IP es el identificador).
- Limpieza de agosto aún pendiente en Pickaxe ES: `confirmationHeadCodeLegacy` lleva el tag de Google pelado.
- Trampas de automatización en Pickaxe: editor CodeMirror 6 sin `cmView` visible desde la extensión → `paste` sintético
  sobre `.cm-content` enfocado; **clic en «Save Settings» unos segundos DESPUÉS del pegado y verificar recargando**;
  tandas de `browser_batch` de más de ~40 s agotan el tiempo del tool; `ctrl+End` no mueve el cursor en ese editor.
- Docs de DataFast en Markdown puro: `https://datafa.st/docs/<slug>.md` (WebFetch del HTML solo devuelve la navegación).
