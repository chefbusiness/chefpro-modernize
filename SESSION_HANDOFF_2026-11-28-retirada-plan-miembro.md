# Handoff 28-nov-2026 — Retirada del plan AI Chef Miembro (10 €) — sesión Claude Code (Mac)

## Qué se hizo
Decisión de John (27-nov): el plan **AI Chef Miembro (10 €/mes, 10.000 créditos)** deja de venderse; no convertía y
nadie subía desde él a los planes superiores. Entrada nueva: **Premium Pro, 25 €/mes, 85.000 créditos**, para
«Cocineros, jefes de cocina y responsables». La parte de Pickaxe la lleva Codex; aquí solo la web pública.

**PR #288** (squash `69490765`), 380 ficheros:
- Tabla de precios: 3 tarjetas mensuales (25 / 50 / 95, «más popular» en el centro) + el anual (950 €) como banda a
  todo el ancho. `Pricing.astro` y su gemelo `PricingV2.tsx` en paridad. Oferta de 10 € fuera del JSON-LD.
- Copy en los 7 idiomas: locales, 7 páginas de precios, FAQ, sobre nosotros, contacto, landings, casos de uso
  (`src/data/use-cases-content.*`), pSEO, productos digitales (menciones cruzadas), CTA del blog, `llms*.txt`,
  `og-meta.ts` (vistas previas de redes sociales).
- Blog: 349 entradas candidatas revisadas (269 ES, 51 EN, 29 FR/DE/IT/PT/NL). Corregidos además datos de planes
  erróneos anteriores (plan «gratis», anual a 500 €, plan «Business», Plus «ilimitado», «1 crédito = 1 uso») y celdas
  de competidores dañadas por un reemplazo masivo antiguo (7shifts, DishGen, ChatGPT).
- `de-gratis-a-pro-5-senales-de-que-necesitas-upgrade` reescrito en su misma URL: «de Premium Pro a Plus o Max».
- `keak-dist-gate.py` endurecido; `merge-keak-copy.py` bloqueado; `keak-copy.*.json` alineados con los locales.

## Método (para repetirlo)
Ficha de hechos única → censo por patrón → lotes sin solape → subagentes `opus` para el texto, DeepSeek (Ori) para el
código con barrido `opus` → comprobación global por patrón → dos auditorías adversariales → preview de Netlify →
gate y `curl` contra la preview → fusionar → `curl` contra producción.

## Gotchas cazados
- **El censo inicial solo miró `astro-site/`**: los casos de uso viven en `src/data/` de la raíz (≈430 líneas) y
  `og-meta.ts` en `netlify/`. La comprobación global sobre TODO el repo es obligatoria.
- **`og-meta.ts` NO está muerta** (lo decía el CLAUDE.md): sirve a los robots de redes sociales.
- **En el Mac, 10 subagentes en paralelo llevaron la CPU a 64,4 °C.** Máximo 2 a la vez; `istats` entre tandas.
- El botón «Empieza desde 10 €/mes» más repetido del blog es de la tarjeta de **Miselup**, no de AI Chef Pro.
- Claude Code del VPS tenía la sesión caducada; y el VPS estaba ocupado por el T480: no se usó.

## Pendiente de John
1. Mirar la tabla de precios en el MÓVIL (no se pudo verificar visualmente; escritorio sí).
2. Tarjeta de Miselup en el blog: ¿«desde 10 €/mes» o «desde 19 €/mes por local»? Hoy dice las dos cosas (75 tarjetas).
3. «Planes empresa», descuentos «a partir de 5 unidades» y «mentoría 500 € inicial» en FAQ de casos de uso y algún
   post: ¿existen o se reformulan hacia Plus/Max?
4. Post EN `mental-health-support-chefs-ai`: habla de «Mental Chef» y «Stress Manager» (no existen; el agente es
   «Mental Coach») con funciones de salud y cifras sin fuente. Necesita revisión entera.
5. Portugués: «escandallos» (≈470 veces) y «escandalhos» (137, no existe) en los datos PT, incluida la URL.
6. Cifra de agentes sin unificar en posts antiguos: «más de 80», «más de 55», «59» frente a 75+.
7. Pickaxe (Codex): un comentario de `src/lib/app-urls.ts` indica que `ptapp`/`nlapp` muestran «Experimente grátis» /
   «Probeer het gratis».
8. `priceValidUntil: '2026-12-31'` del JSON-LD caduca en un mes.
9. Gate `keak-dist-gate.py`: sus avisos «75+ vs 50+» (95) y «111 vs 113 islands» ya fallaban en producción antes.
10. Worktree huérfano en el VPS: `/root/chefpro-plan10` (`git worktree remove`), creado antes de saber que el VPS
    estaba ocupado.
11. No se cambió `modDate` de los ~290 posts editados (solo el reescrito): Google los revisitará a su ritmo.
