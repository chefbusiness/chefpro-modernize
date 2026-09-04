# Handoff — Guía Food Cost + Ingeniería de Menú (producto nuevo) · sesión Claude Code 2026-09-03 → 04 (Mac)

> Primer producto NUEVO del ciclo de sesiones alternadas (decisión de John del 31-ago). John dio luz verde
> total («directamente a producción») y delegó las decisiones del research; después: «lanza a producción tú
> mismo cuando estés ok con todo» + programar el mailing de lanzamiento en Resend (segmento «AI Chef Pro ES»,
> 10:00 Madrid). Todo lo de abajo está commiteado en `main` local; el push se hace con los documentos.

## 1. Estado al cierre (02:20 del 4-sep) — pusheado a `main` (`562b9af`), build en Netlify en curso

| Pieza | Estado |
|---|---|
| Research (5 lentes + síntesis + refutación) | ✅ `scripts/productos-digitales/auditorias/guia-food-cost-*` · refutación «CORREGIR ANTES» resuelta en la SPEC §1 |
| SPEC v1.0 | ✅ `scripts/productos-digitales/guia-food-cost-SPEC.md` (20 decisiones D1-D20) |
| Juego de datos único | ✅ `scripts/productos-digitales/guia-food-cost/datos_ejemplo.py` (carta de 20 platos, ficha, bodega, año mensual; el fixer reescaló cuadro y techos de delivery, documentado en el propio fichero) |
| 8 xlsx | ✅ en `astro-site/public/dl/guia-food-cost-ingenieria-menu/` (4.358 fórmulas, cache 100 %, censo 0 defectos, refutación 16 hallazgos → 15 fixes; Goal Value como índice sin €) · generadores `guia-food-cost/gen_*.py` |
| Guion | ✅ `guias-v2_0/guion_guia_food_cost_ingenieria_menu.py` (20 caps + bonus de 12 ejercicios; 461 referencias a celda verificadas, 0 rotas; 35 ids `FC-*` del research JSON, que pasó de 67 a 103 entradas) |
| Documentos (guía + bonus, PDF + DOCX) | ✅ guía **95 páginas** (50.265 palabras, 42 tablas) · bonus **32 páginas** (12 ejercicios); todos los gates en verde. Texto: caps 1-7 con bridge (Sonnet 4.6 vía OpenRouter) y **caps 8-20 + 12 ejercicios con 44 subagentes Sonnet en paralelo** (orden de John a la 01:40: «pasa del bridge»; ver §5) |
| Capa de producto | ✅ landing `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts` + wrapper, zona app (registro + generador, 135/135 byte a byte), SPA gate/dashboard/rutas, 4 functions + config, catálogo (45), hub (tarjeta «Nuevo», «próximamente» retirado), changelog 1.0, linkify, footerLinks cruzados |
| Stripe | ✅ Payment Link creado por John: `https://buy.stripe.com/bJe3codkMgISajl6Rf6oo1o` (55 € exclusive, redirección a `-access`, IVA automático, factura) · env `VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST` en el site de prod (todos los contextos, scope builds) · `netlify/shared/payment-links.ts` regenerado (45) |
| Imágenes | ✅ 6 galería + OG en `astro-site/public/` (Nano Banana 2, revisadas a ojo) |
| Blog | ✅ 6 posts con banner sustituido + enlace contextual (`fase8f-guia-food-cost-blog.py`, gate de reversibilidad) + `blog-lastmod.json` |
| Email de lanzamiento | ✅ `scripts/productos-digitales/emails/broadcast-guia-food-cost-lanzamiento-es.html` + `resend-broadcast.py` (guardas) · skill local `.claude/skills/resend-aichef/SKILL.md` |
| Hotfixes colaterales | ✅ 6 imágenes de la galería de la guía gastronómica daban 404 (ya en prod) · bono del Kit de Escandallos con el IVA del alcohol corregido + cross-sell (PDF regenerado) |

## 2. Cómo cerrar el lanzamiento (orden exacto)

1. Esperar a `documentos.py` (log `scratchpad/docs/documentos.log`; salida en `scratchpad/docs/guia-food-cost-ingenieria-menu/`; espejo del caché `txt/` cada 2 min en `scripts/productos-digitales/guia-food-cost/build/docs/`). Debe terminar con todos los `ok` en verde en `informe.json`.
2. Copiar a `astro-site/public/dl/guia-food-cost-ingenieria-menu/`: `guia-food-cost-ingenieria-menu.pdf/.docx` y `BONUS-ejercicios-resueltos.pdf/.docx`.
3. Sustituir `__PAGINAS__` y `__PAGINAS_BONUS__` (landing `.ts` y el HTML del broadcast) por las páginas MEDIDAS (`informe.json` → `paginas_pdf`). Comprobar con `grep -rn "__PAGINAS"` que no queda ninguno.
4. Gates: script del Bug #2 (`MISSING: 0`), `censo-entregables.py --only guia-food-cost-ingenieria-menu --fail`, `gate-no-latinos.py --only …`, `gate-flujo-postpago.py --offline --only guia-food-cost-ingenieria-menu`.
5. `git add -A && git commit && git push` → build en la nube (site `ee5802cf…`, `netlify api listSiteDeploys`) → **ready**.
6. LIVE: `gate-flujo-postpago.py --only guia-food-cost-ingenieria-menu` (landing con `buy.stripe.com`, access/library 200, 12 descargas binarias con el tamaño de disco), hub con la tarjeta, robots-gate por inspección (prefijo `guia-` cubierto).
7. Email: `python3 scripts/productos-digitales/emails/resend-broadcast.py --html … --subject "Nuevo: Guía Food Cost + Ingeniería de Menú (con el IVA bien puesto)" --name "Lanzamiento Guía Food Cost (ES)" --test john@chefbusiness.co` → revisar → mismo comando con `--scheduled-at 2026-09-04T08:00:00Z` (10:00 Madrid).
8. Handoff final + memoria + CALENDARIO §0-ter.

## 3. Si el Mac se apagó a mitad

- Relanzar la generación con el mismo comando (reutiliza el caché `txt/` de bloques; si el scratchpad murió, copiar antes `scripts/productos-digitales/guia-food-cost/build/docs/guia-food-cost-ingenieria-menu/txt/` a la salida):
  `GUIAS_SCRATCH=<scratch> python3 scripts/productos-digitales/guias-v2_0/documentos.py --producto guia-food-cost-ingenieria-menu --modelo anthropic/claude-sonnet-4.6 --salida <scratch>/guia-food-cost-ingenieria-menu --json <scratch>/informe.json`
- Nada de lo commiteado depende del scratchpad.

## 4. Decisiones tomadas por Claude con la delegación de John (todas en la SPEC §1)

55 € sin precio tachado · sin ratings ni testimonios inventados (sección oculta si `items` vacío) · IVA verificado contra el BOE (aceite 4 % por RDL 4/2024 — letra **g**; matriz 3×3 sala/take away/delivery; DGT V2254-22) · prime cost con umbral español 65 %/55 % · matriz multi-método honesta (Pavesic ponderado, Goal Value con hoja propia, K&S reconstruida) · bonus de 12 ejercicios · sin cifras de inflación · distribución quirúrgica en 6 posts · euros + vocabulario neutro · FAQ de compra · bono del Kit corregido.

## 5. Trampas nuevas de esta sesión (para la memoria)

- **`fase8e` no reinserta**: un producto nuevo no entra en el blog reejecutando la rotación (salta los posts con banners). Hace falta inserción quirúrgica (`fase8f`).
- **Las imágenes de galería viven en `astro-site/public/`**, no en `public/` de la SPA: las 6 de la guía gastronómica llevaban desde la migración dando 404.
- **DeepSeek flash devuelve vacío en bloques con muchas cifras/tablas**; `documentos.py` ahora cae a Sonnet 4.6 al 3.er intento y admite `--modelo`.
- **Bash en background del tool tiene tope de 10 min**: los procesos largos van con `nohup … &` y se vigilan con Monitor sobre el log.
- **`documentos.py` tenía «Versión 2.0 · agosto 2026» a fuego** en portada/pie/subject: ahora sale de `GUIA['version']` y `GUIA['fecha']` (defaults intactos para las 8 guías).
- **Stripe CLI**: la clave restringida no tiene `product_write`/`payment_link_write`; el flujo manual de John (crear producto + link en el panel → URL → env var en Netlify + `sync-payment-links.py`) funciona en 5 minutos.
- **Resend**: la key YA está en local (`~/michelin-leads/.env`); `POST /broadcasts` admite `segment_id` + `send: true` + `scheduled_at`; el `python3` del Mac no valida TLS → curl.
- **Presupuesto**: research 1,47 M + construcción 2,76 M tokens de subagentes (ultracode, luz verde de John para hacerlo todo en una sesión).

Via: Claude Code

## 6. Cierre (02:20 → 03:00)

- ✅ **LIVE 02:30** — https://aichef.pro/guia-food-cost-ingenieria-menu · `gate-flujo-postpago.py --only guia-food-cost-ingenieria-menu`: 12/12 descargas binarias con su tamaño, landing/access/library 200, webhook armado, 0 fallos. Hub: «45 productos disponibles · 4 próximamente». Sitemap con la URL; `sitemap-index.xml` reenviado a GSC (URL aún «desconocida para Google»: pedir indexación a mano en GSC si se quiere acelerar). Auditoría SEO en vivo: canonical, hreflang es/x-default, OG + Twitter, robots index, JSON-LD Organization/WebSite + Product (55 € InStock, sin rating) + FAQPage (6) + BreadcrumbList; alts descriptivos en galería y bonus (fix del template para las 9 guías, `66fb6f5`).
- ✅ Mailing programado por API: broadcast `c6d68465-b229-4973-b9d2-b5a349775650`, segmento «AI Chef Pro ES», `scheduled` para 2026-09-04 08:00 UTC (10:00 Madrid); prueba enviada a john@chefbusiness.co (email `98076cfc…`). Se cancela desde el panel de Resend si hace falta.
- Regla nueva de John (01:40): **bridge.py NO para productos digitales** (solo SEO/web). Registrada en `~/.claude/CLAUDE.md` (1bis), `CLAUDE.md` del proyecto y memoria `feedback_bridge-no-para-productos-digitales`. Patrón guardado en el repo: `guias-v2_0/dump_prompts.py` + `check_bloque.py`.
- Gates de la familia corregidos por el camino: paréntesis con enumeradores legales, `«€.» → «. €»` (RX_EURO_*), versión/fecha desde el guion, léxico (lista blanca por producto en `_ERRATAS_OK`), `mortalidad_permitida` para «cierra el mes con…».
- Presupuesto real de la sesión (tokens de subagentes): research 1,47 M + construcción 2,76 M + redacción 5,48 M ≈ **9,7 M**. Muy por encima del techo semanal del calendario; hecho con luz verde expresa de John («directamente a producción»).
