# CRO de las portadas — recomendaciones de Keak aplicadas a mano (20-sep-2026)

John probó **keak.com** (SaaS de CRO con tests A/B continuos) sobre `aichef.pro`. No lo contrata
—quiere vivir conectado a la web— pero sus tres recomendaciones le parecen buenas y **se aplican
exactamente como las propone**, en los 7 idiomas y en todas las páginas con tabla de precios.
Capturas originales: `~/Downloads/Mejoras CRO Conversión Web/` (12 PNG + captura de página completa).
Las recomendaciones se dieron sobre la home EN («built for more pricing page visits»).

Sesión Claude Code · rama `feat/cro-home-keak` · sin builds locales (regla térmica): traducciones y
build en el VPS, verificación en el deploy preview.

## 1. Los tres cambios de Keak (copy EN literal)

### Cambio 1 — Hero «reframed for head chefs» (`components/Hero.astro`)
Orden de arriba abajo:
1. Prueba social (ya existía; cambia el texto): 8 avatares · 4,5 estrellas ·
   «Trusted by **764+** chefs · **64,216** recipes & solutions generated» (764+ = `stats.chefs`;
   el contador es el dinámico de siempre, `getDynamicCount()`).
2. H1: «Cut ingredient costs in your **{Pizzeria}** with AI Chef Pro». La palabra rotatoria ya
   existía (`hero.business_types`, 12 por idioma) y conserva su estilo dorado con subrayado
   (`.dynamic-hero-text`). Novedades: la lista v2 quita «Gestión/Management» (no encaja en «en tu
   Gestión») → `hero.v2_business_types` (11, empieza por «Restaurante», que es lo que lee Google en
   el SSR). La marca «AI Chef Pro» va en negro plano (Keak), no con `gradient-text`.
3. Subtítulo dorado: «Automate food cost, waste, portions and menus with 75+ AI agents built for
   professional kitchens.»
4. Línea gris: «Trained on the daily workflows of head chefs, pastry chefs, bakers and hospitality
   operators, not generic restaurant marketing.»
5. Caja de 4 cifras, **número y etiqueta en línea** (no apilados), número en negro, sin gradiente:
   `75+ AI agents · 10+ business & cost tools · 25+ regional cookbooks · 6 chef roles covered`
   (orden nuevo: agentes, herramientas, recetarios, roles). fr/de/it/pt/nl siguen anunciando 50+.
6. CTA doble: enlace de texto en mayúsculas «SEE PLANS & PRICING →» (a la página de precios del
   idioma) + botón dorado «TRY NOW» (plataforma). En móvil el botón dorado va PRIMERO.
7. Microcopy: «Plans from €10/month · new AI agent added every week».
Desaparece el botón «SEE RESOURCES» (blog).

### Cambio 2 — «Waste GenCal leads, CTA routes to pricing» (`components/BusinessToolsShowcase.astro`)
NO es una sección nueva: es el rediseño de la de Herramientas Business, que ya iba justo después de
las tarjetas de cocinas del mundo (`WorldCookbooks`). Misma posición.
- Eyebrow (versalitas): «BUSINESS TOOLS · 6 KITCHEN-NATIVE AGENTS»
- H2: «Cut ingredient costs up to **30%** with tools built for the pass.» (30% dorado)
- Sub: «Waste, portioning, allergens, conversions: the daily math of a professional kitchen, automated.»
- Dos columnas. IZQUIERDA, tarjeta oscura (Waste GenCal como protagonista): píldora «✓ PROOF POINT»,
  «30%» enorme dorado, «average ingredient-cost reduction with precise waste calculations»,
  nombre «Waste GenCal», blurb, y caja «USE CASE» con la cita «Save up to 30% in ingredient costs
  with precise calculations» (= el `preview` existente del agente).
- DERECHA, rejilla 2×3 con los otros 5 (icono dorado + nombre + blurb): Allergen ID, Portion
  Calculator, Unit Converter, Mental Coach, ChatGPT 5.5. Nombres = claves `apps.business.*.name`
  existentes (así salen bien en cada idioma: ID Alérgenos, Mermas GenCal, Calcula Pax…).
- Pie: «Every tool included from the **AI Chef Member** plan upward.» + enlace
  «See plans that unlock all 6 tools →» a la página de precios del idioma.
- Sin botones «Usar herramienta» por tarjeta (Keak concentra el CTA en precios).
- La flecha negra gigante de las capturas es un SVG sin tamaño en el preview de Keak: no existe.

### Cambio 3 — «Pricing cards reordered around role» (`components/Pricing.astro` + 7 páginas de precios + islands)
- H2 «Find your plan in 10 seconds» + sub «Match your role to a tier. Credits scale with how much
  of your kitchen and business you automate — from single-station recipe help to a full
  multi-restaurant operation.»
- 4 chips de rol → plan: «Cook or assistant → Member €10», «Head chef → Premium Pro €25»,
  «Owner or group → Premium Plus €50», «Power user → Max €95». Enlazan a la tarjeta (`#plan-…`) y
  la resaltan 2 s.
- Fila 1 (3 tarjetas): Member 10 · Premium Pro 25 · **Premium Plus 50 = «🔥 Most Popular»** (borde y
  CTA dorados). Anatomía: píldora de audiencia («COOKS & STATION CHEFS») · nombre · descripción ·
  precio grande + «/month» · caja de créditos con borde dorado izquierdo («10,000 credits/month» +
  «≈ 200 recipes or 100 cost calcs») · CTA negro a ancho completo «Start with Member →» · lista de
  checks dorados.
- Separador «— FOR POWER USERS & ANNUAL COMMITMENT —».
- Fila 2 (2 tarjetas, más estrechas, centradas): Premium Max 95 (badge negro «∞ Unlimited Credits»
  arriba centrado; caja «∞ Unlimited credits / Use every tool as often as service demands») y
  Premium Max Annual 950 (badge verde «Save 2 months» arriba a la derecha; «€1,140» tachado; caja
  «∞ Unlimited credits, all year / + monthly personalized consulting included»; CTA «Start Annual &
  save →»).
- Pie: «Running a group or need custom volume? **Talk to us for an enterprise plan →**».
- Ojo: el CTA de la fila 1 no popular es NEGRO (`bg-primary`), no dorado.


### Ajustes de John sobre el preview (20-sep, tarde)
- **Tarjeta oscura del 30 %**: «se veía robusta y sin mucho que decir» → foto de fondo generada con
  Nano Banana (`public/images/business-waste-gencal-bg.jpg`, pase de cocina, manos pesando en báscula,
  sin rostro) con degradado oscuro encima (`from-zinc-950 via-zinc-950/85 to-zinc-950/35`) para que el
  30 % y el texto sigan siendo legibles. `alt=""`, `loading="lazy"`.
- **Pricing**: «blanco sobre blanco no resalta» → panel pastel de la paleta (dorado al 7 %→3 % con borde
  `accent/15`, `rounded-3xl`) envolviendo chips y tarjetas; la tarjeta popular sube a `bg-accent/10`.
  Aplicado en `Pricing.astro` y en `PricingV2.tsx` (paridad).

## 2. Claves i18n (fuente única: `src/i18n/locales/*.json`, que Astro importa)
Fuente EN = `scripts/cro-home/keak-copy.en.json` (copy de Keak literal). Traducción a los 6 idiomas
con `scripts/cro-home/traducir-keak-copy.py` (en el VPS, bridge → sonnet primero, gates de
estructura/dígitos/alfabeto/tratamiento) y fusión con `merge-keak-copy.py` (que además rebaja 75+→50+
en los 5 secundarios, crea `hero.v2_business_types` y `pricing.plans.member.period`).
**Gate**: `python3 scripts/cro-home/merge-keak-copy.py --check`.

Todas las claves nuevas llevan prefijo `v2_` y viven junto a las viejas, que se conservan porque
otras partes las usan (`SocialProofStrip`, JSON-LD, `sobre-nosotros`, landings):
- `hero.v2_social_prefix / v2_social_chefs / v2_social_count / v2_title_prefix / v2_title_suffix /
  v2_subtitle / v2_description / v2_stat_agents / v2_stat_tools / v2_stat_cookbooks / v2_stat_roles /
  v2_cta_pricing / v2_microcopy / v2_business_types[]`
- `showcase.v2_business_eyebrow / v2_business_title_prefix / v2_business_title_highlight /
  v2_business_title_suffix / v2_business_description / v2_proof_label / v2_proof_value /
  v2_proof_text / v2_use_case_label / v2_included_prefix / v2_included_suffix / v2_business_cta`
- `apps.business.{mermas_gencal,id_alergenos,calcula_pax,conversor_ing,mental_coach,chatgpt_4o}.v2_blurb`
- `pricing.v2_title / v2_description / v2_role_member / v2_role_premium_pro / v2_role_premium_plus /
  v2_role_premium_max / v2_divider / v2_enterprise_question / v2_enterprise_link`
- `pricing.plans.<id>.v2_short / v2_eyebrow / v2_description / v2_credits / v2_hint / v2_cta`
  (+ `member.v2_features[4]`; los otros 4 planes reutilizan sus `features` existentes, que ya
  coinciden con Keak). Nombres, precios, `period`, `original_price` y `discount`: claves existentes.

## 3. Dónde hay tabla de precios (todas pasan a la v2)
| Superficie | Ficheros | Cómo |
|---|---|---|
| 7 portadas | `pages/{,en,fr,de,it,pt,nl}/index.astro` → `Pricing.astro` | reescritura del componente |
| 7 páginas de precios | `precios.astro`, `en/pricing`, `fr/tarifs`, `de/preise`, `it/prezzi`, `pt/precos`, `nl/prijzen` | su rejilla `<section aria-label>` con `plans[]` propios → `<Pricing lang medium="pricing" />`; se quedan comparativa, perfiles y FAQ; la columna destacada de la comparativa pasa a Premium Plus |
| 8 landings de marketing × 7 idiomas (islands `client:load`) | `src/pages/{ReducirCostesRestaurante,ChatGPTRestaurantes,MenuRestaurante,RecetasIARestaurantes,SoftwareGestionCocina,EscandallosRestaurante,HerramientasIARestaurantes,MarketingRestaurante}.tsx` | su `<section>` de precios inline + `const plans` → `<PricingV2 medium="landing-…" />` |
| 6 herramientas gratuitas × 7 idiomas | `src/components/PricingPlans.tsx` (usado por `TestDigitalizacion`, `CalendarioContenidos`, `CalculadoraBrigada`, `GeneradorMenuDegustacion`, `DetectorAlergenos`, `GeneradorTextosCarta`) | pasa a envolver `PricingV2`, traduciendo su `toolKey` camelCase a `utm_medium` kebab |
| 2 herramientas más × 7 idiomas | `src/pages/CalculadoraFoodCost.tsx`, `src/pages/SimuladorRentabilidad.tsx` | **no** usan `PricingPlans`: montan `<PricingV2 medium="tool-food-cost" />` y `medium="tool-rentabilidad"` directamente |
Total de islands: **8 landings + 8 herramientas = 16 × 7 idiomas = 112 páginas** con la tabla v2
servida por React, más las 7 portadas y las 7 páginas de precios que la sirven desde Astro.

`src/components/PricingV2.tsx` es el gemelo React de `Pricing.astro`: mismo copy (react-i18next,
mismas claves), mismas clases, `useLanguage().getAppUrl()` para el CTA.

## 4. Rutas de CTA
- Botones de plan: `appCtaUrl(lang, medium, slug)` con `utm_content` = `member | premium-pro |
  premium-plus | premium-max | premium-max-annual`.
- **`utm_medium` identifica la superficie CONCRETA, no la familia** (si todas las landings
  mandasen `landing-pricing` no se podría saber cuál vende). El esquema real, todo en kebab-case:

  | Superficie | `utm_medium` | Valores |
  |---|---|---|
  | 7 portadas | `home-pricing` | uno solo |
  | 7 páginas de precios | `pricing` | uno solo |
  | 8 landings de marketing | `landing-<slug>` | `landing-reducir-costes`, `landing-chatgpt`, `landing-carta-menu`, `landing-recetas-ia`, `landing-software-gestion`, `landing-escandallos`, `landing-herramientas-ia`, `landing-marketing` |
  | 8 herramientas gratuitas | `tool-<slug>` | `tool-digitalizacion`, `tool-calendario`, `tool-degustacion`, `tool-alergenos`, `tool-brigada`, `tool-textos-carta` (los 6 del mapa de `PricingPlans.tsx`) + `tool-food-cost` y `tool-rentabilidad` (montados a mano) |

  El slug NO se deriva del `toolKey`, que es camelCase (`toolScore`, `toolMenuCopy`): `PricingPlans.tsx`
  lleva un mapa explícito, porque dos de los seis no se deducen de su nombre. Un `toolKey` nuevo cae a
  un kebab automático, pero lo correcto es darlo de alta en el mapa.
- «See plans & pricing» (hero) y «See plans that unlock all 6 tools» (business): página de precios
  del idioma (`lib/pricing-path.ts`, el mapa que tenía `Header.astro`).
- «Talk to us for an enterprise plan»: `/contacto` en ES; `mailto:info@aichef.pro` en el resto
  (no hay página de contacto en otros idiomas).

## 5. Marcadores para el gate del `dist`/preview
`data-keak="hero-v2" | "business-v2" | "pricing-v2"` en la raíz de cada sección; en pricing,
`data-plan="<id>"` por tarjeta, `data-role-chip` por chip y `data-popular` sólo en Premium Plus.
Gate: `scripts/cro-home/keak-dist-gate.py --base <url del preview o dist local>`.

**Token nuevo `text-accent-ink`** (`--accent-ink`, 42 100% 30% en claro y 42 100% 62% en oscuro;
declarado en `astro-site/src/styles/global.css` y en los dos `tailwind.config.ts`). El dorado de
marca es un color de FONDO: `--accent` (42 100% 50%) da ~1,9:1 sobre blanco y `--accent-dark`
(42 100% 40%) ~2,9:1, los dos por debajo del 4,5:1 que pide WCAG AA para texto normal. La v2 de
Keak metió dorado en texto PEQUEÑO —la píldora de audiencia de cada plan (11 px), el enlace
enterprise, el «30 %» del H2 de herramientas y los iconos de las 5 tarjetas claras—, así que esos
usos pasan a `text-accent-ink` (~4,7:1). `accent` y `accent-dark` se quedan para fondos, bordes,
iconos grandes y el dorado sobre la tarjeta oscura, donde el contraste ya es correcto.

## 6. Cifras: cuáles son nuestras y cuál hay que confirmar
- 764+ chefs, contador dinámico, 75+/50+, 10+, 25+, 6, «new AI agent every week», 30 % (preview de
  Waste GenCal), precios y créditos: ya estaban en la web.
- **«≈ 200 recipes or 100 cost calcs»** (10.000 créditos) la inventó Keak. Va tal cual por orden de
  John, en una sola clave (`pricing.plans.member.v2_hint`) para cambiarla en un minuto si la
  plataforma dice otra cosa.
