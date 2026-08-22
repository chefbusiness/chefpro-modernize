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

## 5. Fase B+C ejecutadas en el primer representante: **Kit de Escandallos Pro v2.0** (tarde del 22-ago)

- **Ronda 1** (workflow `auditoria-entregables-workflow.js`, ya con `schema`): 90 hallazgos / 20 altas
  (`auditorias/kit-escandallos-R1.json`). Lo grave: bono «Guía Food Cost 30 días» vendido y NO
  entregado, unidades compra/uso sin factor (costes ×100/×1000), control de mermas que comparaba
  despiece con desperdicio, food cost = compras/ventas, pastelería sin rendimiento, cócteles con cl/L
  cruzados, food truck sin punto de equilibrio.
- **SPEC v2.0** (`kit-escandallos-v2-SPEC.md`, §7 = decisiones: delivery 28-32 % sobre ingreso neto,
  catering por bloques con mínimo de evento, carrot cake realista, marca ChefBusiness deliberada).
- **Construcción** (`kit-escandallos-v2_0/`: motor + grupos A/B/C + `bono_guia.py` + `main.py` con
  `--dry-run`, `--solo`, `KIT_ESCANDALLOS_APPLY=1` y respaldo en scratch; 6 fases, 9 agentes) → 3
  refutadores (55) → corrección → **ronda 2b** sobre los 33 que el corrector no vio (recorte a 40 k:
  lección en memoria) → 33/33 resueltos, «listo». Texto del bono con `bridge.py` (Mac enruta a
  `deepseek-v4-pro`: desactualizado, memoria) y 0 caracteres no latinos; PDF maquetado con reportlab
  y saneado de glifos fuera de WinAnsi (gate propio).
- **Ejecución real** `ed45f35` (+ gemelos SPA `ad1fac6`): 12 xlsx idénticos celda a celda a la copia
  verificada, 13 entregables (PDF `bonus-guia` en `PRODUCT_FILES` y tarjeta), censo 0 defectos,
  gate offline 13/13, changelog 2.0, landing 10 tipos / 21 categorías / 20-25 % barra / valor €95,
  `updateNote` 2.0. Deploy y gate LIVE: ver línea siguiente.
- **LIVE verificado**: deploy `ad1fac6` ready 17:15; gate LIVE 44 productos · **646 entregables** (el PDF nuevo) · 8 × 502 transitorios en kit-tareas/cafetería reintentados → 0 fallos en kit-tareas, cafetería, escandallos y mega pack; md5 de producción = repo (01, 10 y el PDF); `01` con hoja Factor y protegida, Delivery 26,19 €; landing «Versión 2.0 · 10 tipos · €95»; island del dashboard con `bonus-guia`.
- Registro completo: `auditorias/kit-escandallos-v2-construccion.json`.
- **Siguiente representante (orden del plan): `pack-appcc`** → `Workflow({scriptPath:
  'scripts/productos-digitales/auditoria-entregables-workflow.js', args:{productId:'pack-appcc',
  familia:'kit-excel'}})`; después kit-tareas (familia «▸») con hermanos verificados por sonnet.

## 6. Segundo representante: **Pack de Plantillas APPCC v2.0** (noche del 22-ago) — `bf2be96`

- R1: 92 hallazgos / 15 altas (`auditorias/pack-appcc-R1.json`; persistido con `r1-desde-journal.py`,
  porque el agente haiku truncaba el JSON — fase eliminada del workflow). Lo grave: PCC declarados
  sin registro (cocción, enfriamiento), sin anisakis, matriz de alérgenos en blanco, límites de
  recepción que aceptaban pescado a 4 °C y rechazaban vacuno conforme, plan L+D que prescribía
  **desincrustante ácido + lejía**, normas derogadas citadas (RD 2207/1995, RD 140/2003, carné de
  manipulador), «€60.000» inventado, protocolo de alerta que mandaba al 112 en vez de a la autoridad.
- SPEC v2.0 (`pack-appcc-v2-SPEC.md`): 4 registros nuevos (16 cocción/regeneración, 17
  enfriamiento/descongelación, 18 congelación anisakis, 19 verificación de termómetros) → **19
  registros + 2 bonos = 21 ficheros**; hoja «Límites» por familia en 02; semáforo y DV que valida en
  todo el pack; normativa vigente; matriz con los 8 ejemplos declarados; HACCP con preventivas/
  vigilancia/verificación, nivel de riesgo y 7 fases; guía con 25 puntos reales y Ley 17/2011.
- Construcción `pack-appcc-v2_0/` (main.py `--dry-run` / `PACK_APPCC_APPLY=1`, respaldo en scratch) →
  3 refutadores que **escriben su JSON a fichero** (57 hallazgos; el corrector los lee enteros:
  `ids_vistos` = 57) → ronda 2: 57/57 «listo». Ejecución real: 0 diferencias frente a la copia
  verificada, censo 0 defectos, gate offline 21/21. Deploy y LIVE: ver línea siguiente.
- **LIVE verificado**: deploy `bf2be96` ready 21:34; gate LIVE **44 · 650 · 0 fallos** a la primera; md5 producción = repo (02, 16, 18); landing «19 registros · Versión 2.0», 0 ocurrencias de RD 2207/1995, RD 140/2003 o «60.000»; island del dashboard con `coccion/enfriamiento/anisakis/termometros`.
- Para John: COM-15 (la landing promete «30 días de garantía» y `/terminos` no tiene cláusula de
  productos digitales — toca `src/i18n/**`, territorio del VPS) y lo aparcado (reseñas, ancla de
  precio, `priceValidUntil`). La integración retocó también `src/data/use-cases-content.*.ts`
  (17→19 registros y sin «PDF export»).
- Registro: `auditorias/pack-appcc-v2-construccion.json`.
- **Siguiente: `kit-tareas`** (representante «▸») — R1 lanzada al cerrar este bloque.
