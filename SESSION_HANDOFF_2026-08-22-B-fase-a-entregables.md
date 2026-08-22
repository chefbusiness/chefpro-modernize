# Handoff — 2026-08-22 (B) · Productos digitales: FASE A del saneamiento de los 630 entregables — HECHA y LIVE

> Sesión en el Mac (Fable, ultracode; CPU 40-56 °C todo el rato, scripts en serie, sin builds
> locales ni Playwright; verificación por `curl` y API de Netlify). Arranca desde
> `SESSION_HANDOFF_2026-08-22-productos-digitales.md` §4.0 y el plan
> `scripts/productos-digitales/PLAN-AUDITORIA-ENTREGABLES-2026-08-23.md`.
> **Repo al cerrar:** `main` = `8a9b8d6`+ (14 commits, pusheados; deploy de código verificado en `ea43a62`). La sesión del VPS (blog PT/NL)
> sigue viva: rebasar antes de pushear; no tocar `astro-site/src/content/blog/**` ni `src/i18n/**`.

## 1. Qué está LIVE

| Qué | Commits | Verificación |
|---|---|---|
| **420 xlsx de 42 productos saneados (v1.1)**: cache de valores (móvil/visores), A4 completo (ajuste al ancho, pie, cabecera repetida, freeze), metadata AI Chef Pro, bio anclada (4 variantes viejas), línea «Versión 1.1 · agosto 2026», casilla unificada por patrón (P1/P2: Nº + «✓ Completada» + desplegable ✓/—/N/A + fila verde + contador con numerador y denominador; P3a: desplegable ✓/☐/N/A sobre la ☐; P3b: desplegable en la columna OK; P4: verde + contador) | `ee415aa` `d42bcf8` `9137c39` `a409a8c` `f62be5c` `3e5920d` `a3e1a77` | `censo-entregables.py --fail` → **0 defectos**; 0 contadores duplicados en 1.204 hojas; gate offline 44/642/0; **gate LIVE 44 productos · 645 entregables · 0 fallos** (2 × 502 transitorios tras el deploy, reintentados → 200); md5 producción = repo en 5 descargas; valores cacheados visibles con `data_only` |
| **30 fórmulas rotas reparadas en ficheros vendidos**: calculadora PVP de escandallos (9 × `=…/=AVERAGE`, abrían con `#¿NOMBRE?`), calculadora de viabilidad dark-kitchen (12 celdas: SUM circular, EBITDA, margen %, food cost sobre comisiones), `cash-flow-break-even` B12 circular en 5 guías, «Progreso (%)» del onboarding con filas literales, 6 etiquetas «= …» guardadas como fórmula → texto | idem | valores cacheados coherentes (p. ej. dark-kitchen pesimista EBITDA −2.785 €; PVP 20,75 €) |
| **38 huérfanos de la raíz de `/dl/` borrados** (17 `ap-*` y 12 `ke-*` duplicados byte a byte; 9 `tr-*` kit base antiguo). `b23-/b1-/pp-7e48…` se quedan: son el eBook por env var | `fa784ff` | `/dl/ke-17b9.xlsx` → 404; gate LIVE del eBook OK |
| **Changelog v1.1 de los 42 productos + badge de versión y bloque «Novedades» en los 43 dashboards + `updateNote` en las 19 landings de kits de tareas** | `b5b30cf` `ea43a62` | cada viñeta contrastada contra los xlsx por un refutador (0 promesas falsas tras corregir 9 hallazgos); deploy `ea43a62` → ver §4 |

Herramientas nuevas (todas en `scripts/productos-digitales/`): `FASE-A-SPEC-postprocess-transversal.md`
(qué se toca y qué no por patrón), `postprocess-transversal.py <pid|all|carpeta> [--dry-run] [--json]
[--nombres-cortos]` (idempotente; `--dry-run` copia a scratchpad), `censo-entregables.py [--only
<pid|carpeta>] [--fail] [--json]` (gate), `auditorias/fase-a-resumen-2026-08-22.json` (qué cambió por
producto). `inject_cache.py` cuenta fórmulas por tipo de celda.

## 2. Lo que cazó el método (para no repetir)

1. **15 hallazgos de 2 refutadores** (5 altas) sobre los scripts antes de tocar `/dl/`: orientación pisada,
   plantillas en blanco con «0 de 3», cabecera falsa en una calculadora, P3b no idempotente, nombres
   cortos que colapsaban 23 productos en «Kit de Tareas Recurrentes», gate que nunca daría verde por
   un falso positivo de bio («un horno bien cuidado dura 15+ anos»), `--skip-cache` roto…
2. **Mi workflow los perdió como «0 hallazgos»**: `agent()` sin `schema` devuelve texto. Memoria
   `feedback_workflow-agentes-sin-schema-devuelven-string`. Desde entonces, schema siempre.
3. **Dry-run `all` destapó 3 residuos**: referencias circulares preexistentes en 6 guías, IRR sin
   exención en el gate, títulos que caían en un paso numerado.
4. **La ejecución real destapó uno más, antes de commitear**: cafetería/pizzería/hamburguesería/
   dark-kitchen ya tenían contador («Completadas: … de 20») sin desplegable → el script lo clasificó
   P2 y escribió un **segundo contador** encima. Ahora el contador existente se reconoce por su
   fórmula, no por su etiqueta, y `_contador_nuevo` nunca escribe si ya hay uno. Se restauraron los
   4 kits desde git y se reejecutaron.
5. **El refutador del changelog destapó el último**: 147 hojas de 11 kits venían del generador con
   `paperSize=9` a secas y la regla «si ya vale 9 no se toca» las dejó sin ajuste ni pie. Corregido
   en script y gate (`a3e1a77`).
6. El clasificador de permisos bloquea el post-proceso in place masivo en segundo plano: se corre
   por familia en primer plano (que además es lo que pedía el plan).

## 3. Pendiente de JOHN (decisiones, no bloquean)

1. **Marca «ChefBusiness Consultoria Gastronomica»** en A1 y pie de 7 productos vendidos en aichef.pro
   (kits asador, food-truck, marisquería, panadería, sushi-bar, tapas-bar y plan bar-restaurante).
   La Fase A no lo tocó. ¿Rebrand 1:1 a «AI Chef Pro · aichef.pro» o es deliberado?
2. **`updateNote` en guías / kits Excel / planes**: sus 3 plantillas no pintan el campo; los 23
   productos muestran «Versión 1.1» en el dashboard pero la landing pública no dice «actualizado».
   Si interesa: `updateNote?: string` en los 3 types + el bloque condicional de
   `KitTareasLandingPage.astro:234-239` en las 3 plantillas.
3. Siguen de la sesión anterior: armar el **webhook** (`STRIPE_WEBHOOK_SECRET`), `PURCHASE_VALIDATION`
   → strict, quitar `aggregateRating`/`reviews` de las 43 landings, **disputa Stripe 650 € antes del 25-ago**.

## 4. Siguiente trabajo (orden)

0. ~~Confirmar el deploy `ea43a62`~~ — **HECHO**: deploy `ready` 12:08, gate LIVE final
   **44 · 645 · 0 fallos**, `updateNote` visible en `/kit-tareas-asador`, el chunk
   `/_astro/ProductChangelog.*.js` va importado por los islands de los dashboards (el texto del
   changelog viaja en su chunk de datos), `/dl/ke-17b9.xlsx` → 404, md5 de producción = repo.
1. **Fase B — ronda 1 adversarial por representante (opus, 3 lentes)**, empezando por
   `kit-escandallos`: `Workflow({scriptPath: 'scripts/productos-digitales/auditoria-entregables-workflow.js',
   args:{productId:'kit-escandallos', familia:'kit-excel'}})`. ⚠️ Ese workflow usa `agent()` SIN
   schema: añadirlo (o parsear el JSON) antes de lanzarlo. Orden: escandallos → APPCC → kit-tareas →
   inventario / gestión-personal / plan-financiero → guías → planes → hotel y resto → eBook.
   Entradas ya detectadas para la B: **B13 «Break-Even (meses)» VACÍA** en el cash-flow de 5 guías;
   43 hojas P2/P3/P4 sin contador (plantillas en blanco, pies ocupados, P3b sin columnas libres —
   motivos en el resumen JSON); títulos de metadata que caen en rótulos en algún plan financiero;
   `kit-plan-financiero/07` IRR sin cache (pycel, no es defecto).
2. **Homologación AICP↔CB** (regla de John: una sola versión, CB replica): los 42 productos v1.1 +
   pastelería v2.0 deben llegar a CB; y a AICP le falta traer los 6 planes v2.0, la guía casual y el
   catering de CB.
3. SEO de las 44 landings ES + LATAM (memoria `project_seo-landings-productos-hispanoamerica.md`).
