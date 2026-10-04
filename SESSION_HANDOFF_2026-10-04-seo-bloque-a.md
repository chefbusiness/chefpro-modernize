# Handoff 2026-10-04 — SEO Bloque A + plan de contenidos Q4 (sesión Claude Code, T480 Omarchy)

> Sesión retomada tras un apagón: el T480 se quedó sin batería a media sesión. El primer clon estaba a medias y el scratchpad de `/tmp` se perdió. Lo recuperable del análisis está en `~/recuperacion-chefpro-2026-10-04/` (fuera del repo).

## Decisiones de John (vigentes)

- **Contenido de aichef.pro sin `bridge.py` ni OpenRouter** hasta nuevo aviso. Reparto: Sonnet redacta; Opus se encarga de recetas, técnica, seguridad alimentaria, normativa y la auditoría adversarial; Haiku de lo trivial. Imágenes con Gemini (skill `generate-images`). Prevalece sobre la REGLA CAPITAL del `CLAUDE.md`.
- **Doble CTA en todo post o landing:**
  - Productos digitales del MISMO idioma: ES → `/productos-digitales`; EN → solo los de `/en/digital-products` que estén vivos.
  - Suscripción del workspace del idioma, para subir el MRR en Stripe.
- La tienda EN la lleva **otra sesión de Claude Code**, que reapunta los banners de los posts EN al lanzar cada producto.
- Ritmo del trimestre: ~3 posts/semana. Orden: Bloque A primero.

## Hecho (PR #112, rama `seo/bloque-a-q4`)

| Pieza | Qué |
|---|---|
| A5 | Title y description nuevos en los 16 glosarios ES con más impresiones |
| A2 | `/en/restaurant-marketing-ai`, `/en/kitchen-management-software-ai`, `/fr/calcul-food-cost-restaurant-ia`: title, meta, H1, H2 y FAQ con las queries de GSC (en `src/i18n/locales/{en,fr}.json`) |
| A6 | `astro-site/public/llms.txt` y `llms-full.txt` reescritos y verificados en vivo |
| A1 | `/blog/chef-gpt` pasa de 0 a 4 enlaces internos entrantes. **No se fusiona** con `chef-gpt-espanol` (relevo de URL, no duplicado) |
| Fix | `las-7-mejores-apps…` atribuía nuestro plan Miembro a ChefGPT, Mr. Cook y RecetApp |
| Plan | `PLAN_CONTENIDOS_Q4_2026.md`: 37 piezas en 13 semanas |
| Skill | `.claude/skills/gsc-oportunidades-aichef/` con la línea base para medir hacia el **25-oct** |

Auditoría adversarial Opus: sin bloqueantes; las correcciones menores están aplicadas.

## Siguiente sesión

1. Medir la línea base (skill local) hacia el 25-oct.
2. Semana 1 del plan: EN `kitchen-brigade-system` (2.900/mes, SERP débil), refresh ES de `escandallos-ia-cocina-profesional` y PT `garum`.
3. Técnico, semanas 1-3: abrir `/nl/blog` (bloquea el primer post NL de la semana 4).
4. Pendientes de calidad:
   - H2 «Hidrólisis ácida → ceviche»: en el ceviche hay desnaturalización, no hidrólisis.
   - Cifra sin fuente en la landing FR («5 % et 15 %»).
   - Hub EN dice «55+ apps» frente a «75+».
5. Para John: cutover de `enblog.aichef.pro` (`CUTOVER_ENBLOG_PENDIENTE.md`) y coordinar con la sesión de la tienda EN los ~125 banners de posts EN que aún apuntan a landings españolas.

## Entorno T480

- Clon **parcial** (blobless + sparse). No ejecutar `git fsck` ni `sparse-checkout add` de carpetas de imágenes: dispara la descarga de cientos de MB.
- Claves en `~/.config/chefbusiness/secrets.env` (600). DataForSEO: `DATAFORSEO_ENV=~/.config/chefbusiness/secrets.env`.
