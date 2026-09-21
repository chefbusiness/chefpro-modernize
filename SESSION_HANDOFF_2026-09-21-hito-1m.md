# Handoff — 2026-09-21 · Hito «1.000.000 de consultas» (sesión Claude Code)

**Todo en producción tras la luz verde de John.** Origen: informe semanal de Pickaxe (25-ago → 1-sep) que marcó el millón de usos acumulados como el mejor gancho de captación.

## 1. Qué se ha desplegado

| Pieza | Dónde | Estado |
|---|---|---|
| Contador de prueba social con el millón por delante | `astro-site/src/lib/social-counts.ts` (`SOLUTIONS_BASE_COUNT` 48149 → 1048149) + 5 copias verbatim (`SocialCountLive.astro`, `UseCasesHubPage`, `UseCasePageContent`, `ConsultoriaGastroProHubPage`, SPA `HeroSocialProof.tsx`) | LIVE (PR #89, merge `4fec7ab`): el 21-sep pinta **1.064.282** y sigue sumando ~70/día |
| `components/MilestoneCounter.astro` | Antes de `<Pricing />` en las 7 portadas; copy `milestone.*` en `src/i18n/locales/*.json` | LIVE: 7 portadas con el contador ×2 (hero + componente) y el componente ×1 |
| Post «AI Chef Pro Supera el Millón de Consultas» | `blog/ai-chef-pro-un-millon-de-consultas` + EN `one-million-queries`, FR `un-million-de-requetes`, DE `eine-million-anfragen`, IT `un-milione-di-richieste`, PT `um-milhao-de-consultas` | LIVE: 200 ×6, FAQPage ×7, 3 banners ES/EN, 2 figuras + destacada, en el sitemap, lastmod 2026-09-22 |
| Correo del hito ×7 idiomas | `scripts/productos-digitales/emails/broadcast-hito-1m-<lang>.html` (fuente `emails/hito-1m/`) | **7 broadcasts programados 2026-09-22 08:00Z** (prueba enviada a John antes de cada uno) |
| Piezas sociales | `scripts/astro-migration/hito-1m-post/social.md` (LinkedIn ES/EN, WhatsApp ES) | Para que John las publique |

Broadcasts del hito (Resend): ES `6d52cfaf` · EN `766e2f75` · FR `f70e15af` · DE `ccdb8320` · IT `a688c8b3` · PT `80a0d215` · NL `547073f7`. Remitentes: `hola@` (ES), `hello@` (EN), `bonjour@` (FR), `hallo@` (DE, NL), `ciao@` (IT), `ola@` (PT), todos en `news.aichef.pro`; Reply-To `info@aichef.pro`; bloque de baja `{{{RESEND_UNSUBSCRIBE_URL}}}` en los 7.

## 2. Regla nueva de John: NUNCA «Hola, chef»

La lista es transversal (dueños, managers, panaderos, pasteleros, chocolateros, bartenders, consultores). Saludo abierto en todos los correos e idiomas: «Hola, colegas:» · «Hi everyone,» · «Bonjour à tous,» · «Hallo zusammen,» · «Ciao a tutti,» · «Olá a todos,» · «Hallo allemaal,». Persistido en `CLAUDE.md` (reglas de marca), en la skill local `resend-aichef` y en memoria; los 15 moldes de `scripts/productos-digitales/emails/` ya lo llevan.

**Los 6 broadcasts de producto que ya estaban programados se RECREARON con el saludo nuevo en sus mismos huecos** (Resend no deja editar un broadcast programado: `PATCH` → 403 «Only draft broadcasts can be edited»; se creó el nuevo con el mismo `scheduled_at`, se verificó por GET y sólo entonces se borró el viejo):

| Hueco (UTC) | Correo | Id viejo → nuevo |
|---|---|---|
| 24-sep 08:00 | Actualización Plan de Negocio Cafetería y Brunch 2.2 | `b21b65e5` → `d402afc9` |
| 29-sep 08:00 | Actualización Plan de Negocio Tapas Bar 2.2 | `29700c86` → `6e58e44a` |
| 4-oct 08:00 | Actualización Plan de Negocio Panadería 2.2 | `e01eae4b` → `e5a339a6` |
| 9-oct 08:00 | Actualización Plan de Negocio Food Truck 2.2 | `8332079d` → `2cb1e142` |
| 14-oct 08:00 | Lanzamiento Guía Pastelería | `476bf7fa` → `481e40c4` |
| 19-oct 08:00 | Actualización Kit de Tareas Pastelería 2.1 | `ec87d4a8` → `44192ce9` |

## 3. Decisiones tomadas con la luz verde (las 7 de la página de revisión)

1. Envío el 22-sep 10:00 Madrid, los 7 a la vez, tras el post (cumplido; no choca con Cafetería 2.2 el 24-sep).
2. Imágenes: la API de Gemini seguía en `402 RESOURCE_EXHAUSTED` → **Higgsfield `gpt_image_2_5` esta vez**. **Recargar créditos en AI Studio** antes del próximo contenido (la skill `generate-images` sigue siendo la norma).
3. «35 agentes afinados» sólo en ES (correo y post); en los otros idiomas el post dice «revisando los agentes uno a uno» sin cifra ni lista.
4. La migración de modelo va como «nuevo modelo de razonamiento», sin nombrar Gemini 3.7.
5. NL: correo sin bloque de modelos (su workspace sólo tiene ChatGPT 5) y sin post (no hay blog NL).
6. Remitentes nuevos por idioma en `news.aichef.pro` (dominio verificado; no hace falta crear buzones).
7. Workspace DE: el agente se llama «Deep Sonar Research» (errata frente a «Sonar Deep Research» en los demás); el correo lo cita tal cual. **Pendiente de John: corregir el nombre en Pickaxe.**

## 4. Cómo se adaptó el post a cada plataforma (`hito-1m-post/traducir.py`)

Nombres de agente reales por workspace (`agentes-map.json`, extraído del HTML de cada app), las filas de agentes que no existen en ese idioma se retiran EN ORIGEN antes de traducir (pedírselo al modelo no funcionó: DE dejó 11 filas y IT 10 en dos intentos), ChatGPT 5.5 (EN) / ChatGPT 5 (resto) en lugar de GPT-5.6 Luna, recuento de agentes del workspace (80 EN, 59 FR/DE/IT/PT), enlaces sólo a páginas que existen en ese idioma (los inventados se degradan a texto plano) y geografía neutra («tanto en España como en toda Hispanoamérica» → «en todo el mundo»: el modelo había inventado «across the UK» y «en France»). Gates: H2 = ES, filas de tabla, alfabetos, tratamiento (vous/Sie/você), sin «35», sin «GPT-5.6», todos los enlaces 200. IT: «consulenze» → «richieste» (el modelo traduce «consultas» como consultoría).

## 5. Gotchas de la sesión

- **En zsh, `for path in …` destruye `$PATH`** (`path` es el array ligado a `PATH`): «command not found: curl». Usar otro nombre de variable.
- La API de Gemini con créditos de prepago agotados devuelve `402 RESOURCE_EXHAUSTED`; el script de imágenes no lo distingue de un bloqueo de seguridad si no se mira el JSON.
- `photoanalysisd` al 86 % de CPU subió el Mac a 65,4 °C sin carga nuestra: congelado con `pkill -STOP photoanalysisd` (reanudar `pkill -CONT photoanalysisd`).

## 6. Pendiente

- John: recargar créditos de Gemini (AI Studio) · corregir «Deep Sonar Research» en el workspace DE · publicar las piezas sociales · comprobar el 22-sep en resend.com/emails que los 7 salieron (bounces < 4 %, spam < 0,08 %).
- Si se quiere alinear el ritmo del contador con el real (~1.450/día según el informe, frente a ~70/día del código), es un cambio de una constante en `social-counts.ts` + 5 copias; no se hizo porque el dictado fue sólo «el millón por delante».
