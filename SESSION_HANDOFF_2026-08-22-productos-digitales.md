# Handoff — 2026-08-22 · Productos digitales: Kit Pastelería v2.0 LIVE + capa de pagos (validación + webhook) + bio anclada

> Sesión larga en el Mac (Fable, ultracode, regla térmica: CPU 40-55 °C todo el rato, nada de
> builds locales ni Playwright). Objetivo de John: «dejar todo 100 % funcional» en productos
> digitales, partiendo de `SESSION_HANDOFF_2026-08-20-productos-digitales.md` §4.
> **Estado del repo al cerrar:** `main` = `ed379f3` (3 commits míos rebasados sobre los 2 del VPS
> de esa noche, pusheado, deploy `ready` 01:33, verificado LIVE). La sesión del VPS (blog PT/NL)
> sigue viva: **rebasar antes de pushear** y no tocar `astro-site/src/content/blog/**` ni `src/i18n/**`.

## 1. LIVE y verificado

| Qué | Commit | Verificación |
|---|---|---|
| **Kit de Tareas Pastelería v2.0** — 13 plantillas + 2 bonus (4 nuevas: 10 producción/mermas, 11 encargos, 12 alérgenos BORRADOR, 13 temperaturas/recepción/etiquetas) | `ed379f3` | Gate LIVE **44 productos · 645 entregables · 0 fallos**; los 15 xlsx de producción = md5 del repo y abren `data_only` con valores; landing sin `aggregateRating`/`review`, FAQPage = 7 FAQ visibles, sin «€39/−69 %», «Versión 2.0»; dashboard island hidrata; Mega Pack a 15 |
| **Capa de pagos**: validación producto↔sesión (`PURCHASE_VALIDATION` soft por defecto), `stripe-webhook` (inerte, 501), mapa de 44 Payment Links en `netlify/shared/`, gate sección D, `audit-payment-links.py` | `4a7b44f` | 14 asserts con Stripe simulado; bundle esbuild de las 3 functions; LIVE: webhook responde 501 al UA de Stripe (llega), verify/resend siguen respondiendo sus errores controlados |
| **Bio anclada** en 130 ficheros («en cocina desde los 17 años · consultor desde 2010», nunca sumar) + `priceOld`/`discountBadge`/`bonusSaveLine`/`aggregateRating`/`reviews` **opcionales** en los 4 types + 4 templates | `dfd391d` | grep 0 restos fuera del blog; esbuild OK |

**Método de la v2.0:** workflow `scripts/productos-digitales/kit-tareas-pasteleria-v2-workflow.js`
(3 opus construyen → sonnet finaliza → 3 opus refutan): **60 hallazgos** en la ronda 1 (descuadre de
caja que ignoraba el fondo, cláusula RGPD sin categorías especiales, CF que pintaba en rojo las
celdas vacías del registro de temperaturas, alturas que cortaban textos legales, referencias a una
hoja «Mermas» inexistente…) → 2 agentes de fix → ronda 2 (sonnet, opus daba 529): todos
resueltos o descartados con motivo; 3 menores cerrados a mano (sobrante en el cierre del 01,
caja 20:10, «Control de Alérgenos de Vitrina»). Hallazgos y resultado: en el scratchpad de la
sesión (muere al reiniciar); lo que importa vive en los scripts del repo.

## 2. Gotchas nuevos (ya en memoria y/o en el código)

- **`inject_cache.py` NO era idempotente**: la 2.ª pasada sobre un fichero con fórmulas de texto
  duplicaba `t="str"` → XML inválido → openpyxl revienta. Arreglado (limpia el `t=` previo) y
  convierte escalares de numpy. Cazado en el 10 y el 12.
- **pycel:** `SUMPRODUCT(--(rango<>""))` devuelve numpy y no se cacheaba; `COUNTIF` solo sobre
  rangos 1-D; `COUNTA` no existe; `COUNT` sí acepta 2-D. Las 458 fórmulas «sin cache» del 12 son
  `IF(...="","",...)` que devuelven cadena vacía por diseño: el verificador las cuenta aparte.
- **`git mv -k` sobre un directorio sin trackear no mueve nada y no avisa.**
- **El edge de Netlify devuelve 403 HTML a `curl` SIN User-Agent** (las functions no llegan a
  ejecutarse). Con el UA real de Stripe (`Stripe/1.0 (+https://stripe.com/docs/webhooks)`) sí
  llega. El gate siempre manda UA.
- **Opus dio 529 (overloaded) 6 veces seguidas** a las 01:00 (hora Madrid): la ronda 2 se hizo
  con sonnet + verificación determinista mía. Tener el plan B a mano.

## 3. Pendiente de JOHN (un paso de 5 minutos + dos decisiones) — **John (02:40 del 22-ago): «déjalo para mañana o pasado»** (23-24 ago): el webhook (punto 1) y la decisión soft→strict (punto 3)

1. **Armar el webhook** (mata la clase entera de «pagué y no tengo enlace»):
   Stripe → Developers → Webhooks → *Add endpoint* `https://aichef.pro/.netlify/functions/stripe-webhook`,
   eventos `checkout.session.completed` y `checkout.session.async_payment_succeeded`; copiar el
   `whsec_…` a Netlify (site `ee5802cf-…`) como env var **`STRIPE_WEBHOOK_SECRET`** (secreta,
   scope *functions*). Sin redeploy. Comprobar: `python3 scripts/productos-digitales/gate-flujo-postpago.py`
   → «stripe-webhook LIVE: 400 sin firma (desplegado y armado)».
2. ~~Auditar los 44 Payment Links~~ — **HECHO el 2026-08-22**: CLI emparejado con «AI Chef Pro
   ES/EN» (`acct_1PsZO84CcdRGidmE`, clave hasta el 2026-11-20) y `audit-payment-links.py` (modo
   `--live`) → **44/44 activos con redirect correcto a `-access?session_id={CHECKOUT_SESSION_ID}`,
   0 fallos**. La cuenta tiene otros 39 links activos ajenos al catálogo (el webhook los ignora).
3. **Decisión:** pasar `PURCHASE_VALIDATION` a `strict` tras unos días mirando los logs
   `[purchase-validation]` en Netlify (ojo: si rotas un Payment Link, las sesiones antiguas
   llevan el plink viejo → en strict `resend-access` les daría 404; fallback `/admin/generar-acceso`).
4. **Decisión:** extender a las otras 43 landings lo que ya hizo pastelería (quitar
   `aggregateRating`/`reviews` sin sistema real de reseñas y el ancla de precio permanente). Ya es
   solo borrar campos en cada data file: tipos y templates lo admiten. **Ojo:** el JSON-LD del
   layout (`BaseLayout.astro:173`) lleva otro `aggregateRating` site-wide del SaaS — misma
   conversación.
5. ~~Email al cliente del Kit Pastelería~~ — **CERRADO por John el 2026-08-22**: el cliente del
   16-ago ya tiene todo y está avisado por WhatsApp. El borrador
   `scripts/productos-digitales/kit-tareas-pasteleria-v2-EMAIL-CLIENTE.md` queda como plantilla
   para futuras actualizaciones de producto.
6. **Disputa Stripe 650 €: responder ANTES del 25-ago** (memoria `project_disputa-stripe-650…`).

## 4. Siguiente trabajo de productos digitales (orden propuesto)

0. **AUDITORÍA DE CONTENIDO DE LOS 630 ENTREGABLES RESTANTES** (pregunta de John a las 02:30:
   «¿están auditados, sin defectos?» — respuesta honesta: NO, solo Pastelería). Censo determinista
   del 2026-08-22 sobre los 645 (`scripts/productos-digitales/censo-entregables-2026-08-22.json`):
   458 xlsx + 61 docx + 9 pdf; **179 xlsx con fórmulas sin valor cacheado** (7.684 fórmulas: en
   móvil/visores se ven en blanco — bug B de CB), **79 con la casilla ☐ en la columna A que no
   cuenta** (bug L1-02, el mismo que tenía pastelería: 7 kits de tareas + asador/sushi/panadería-obrador),
   **25 con la bio caducada dentro del Excel**, **401 sin impresión A4 configurada**, 443 con
   `creator = openpyxl`; 0 caracteres no latinos. Los 39 xlsx sueltos en la raíz de `/dl/` (fuera de
   carpeta de producto) son los peores (25 sin cache) — identificar a qué productos sirven.
   Plan: (a) post-proceso determinista transversal (generalizar
   `kit-pasteleria-v1_1-postprocess.py`: metadata, A4, cache con `inject_cache.py` ya idempotente,
   bio anclada, casilla unificada «✓ Completada» donde aplique) sobre los 458 xlsx, por línea de
   producto y con gate antes/después; (b) auditoría ADVERSARIAL de contenido por línea (kits de
   tareas 12 → lente chef/obrador por sector; guías 8 + planes 9 → lente consultor; escandallos /
   APPCC / inventario / RRHH / financiero → lente técnica Excel + experto), con Workflow, 3 lentes,
   fixes y ronda 2 como en pastelería; (c) docx/pdf: revisión de texto (bio, tildes, promesas).
   Es trabajo de varias sesiones: empezar por los que más se venden (kits de tareas, escandallos,
   APPCC) y por los 7 kits con el bug de la casilla.

1. **SEO de las 44 landings para España + Hispanoamérica** (encargo de John de hoy, memoria
   `project_seo-landings-productos-hispanoamerica.md`): baseline GSC 90 d = las landings casi no
   tienen impresiones en NINGÚN país (mejor caso `/kit-escandallos` 253 imp., 2 clics, pos. 27;
   LATAM: MX 3, CO 1). Plan: GSC por país + Stripe por país → research por país con DataForSEO
   (+ Apify para SERP/PAA y competidores) → glosario ES↔LATAM por producto → enriquecer cada
   landing con `bridge.py` (sin páginas por país) → auditoría adversarial → medir.
2. **Homologación AICP↔CB** (regla de John: una sola versión, CB replica): CB debe recibir el
   Kit Pastelería v2.0 (15 ficheros + código) y los 08/09 de 12 kits; AICP debe traer de CB los
   6 planes v2.0, la guía casual y el catering. Censo md5:
   `scripts/productos-digitales/homologacion-aicp-cb-censo-2026-08-18.json`.
3. Restos de la bio vieja que NO se tocaron por territorio: `astro-site/src/layouts/BlogPost.astro:151,164`
   (JSON-LD del autor de los posts, ES y PT) → para la sesión del blog.
4. Las 4 landings «sin tildes» (dark-kitchen, restaurante-creativo, inventario, gestión-personal)
   siguen sin tildes en TODO su copy (solo se corrigió la bio): candidatas a barrido ortográfico.
