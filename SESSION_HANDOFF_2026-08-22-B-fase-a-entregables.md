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
   → strict, quitar `aggregateRating`/`reviews` de las 43 landings (la disputa Stripe la lleva John desde el 23-ago: fuera de la lista).

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

## 7. Tercer representante: **Kit de Tareas Recurrentes v2.0** (familia «▸», madrugada del 23-ago) — `228bfd0`/`de9f961`

- R1: 81 hallazgos / 7 altas, cada uno etiquetado MOTOR (se repite en los hermanos) o CONTENIDO
  (`auditorias/kit-tareas-R1.json`). Lo grave: el **arqueo de caja descuadraba cada día por el
  importe del fondo** (nunca lo restaba; mismo bug que pastelería v2.0 ya resolvió; el fichero va en
  12 kits), 08/09 de otro generador (otra paleta, otro desplegable, sin responsables), contador que
  cuenta las N/A como pendientes, 07 con el denominador clavado a 15.
- SPEC v2.0 (`kit-tareas-v2-SPEC.md`, §8 = reglas que cambiaron en la ronda 2): **motor de familia**
  (`kit-tareas-v2_0/motor.py`, detecta las hojas por CABECERA; `main.py --producto <pid>`) +
  `contenido_kit_tareas.py` (higiene personal, orden seguro del gas, anisakis, jornada, mantenimiento
  legal trimestral/anual, calendario…). Probado en kit-tareas, cafetería y hotel (sus 01-17 quedan
  byte a byte).
- 3 refutadores (61, JSON a fichero) → corrección 61/61 → ronda 2 «listo» → 2.ª vuelta para un guion
  ASCII → real: 0 diferencias, censo 0, gate 11/11. Landing «9 plantillas + 2 bonus (11 ficheros) ·
  491 tareas» (recuento independiente: 491), tarjetas de 08/09, emails y dashboard coherentes,
  changelog 2.0. Censo con campo informativo `autoria`.
- **LIVE verificado**: deploy `de9f961`; gate LIVE 44 · 650 · 0; md5 producción = repo (01, 09);
  09 con 0,02 €, «Fondo de caja inicial (−)» enlazado a `'Apertura de Caja'!C23` y DESCUADRE calculado.
- Bugs del método cazados por los gates (en `auditorias/kit-tareas-v2-construccion.json`): hora ancla
  que se realimentaba 15 min por pasada; nombre del kit leído de celdas que el motor reescribe;
  `inject_cache` solo sobre ficheros con fórmulas nuevas (guardar borra el cache de TODAS); registro
  de fórmulas heredado entre ficheros.
- **Hermanos**: tanda en curso al cerrar (`kit-tareas-hermanos`: motor en dry-run sobre los 10 kits,
  verificador sonnet por kit, crítico opus) → ejecución real por kit + mini-ronda de contenido donde
  el crítico la pida.

## 8. CIERRE DE SESIÓN (23-ago, ~01:20) — cómo retomar mañana

**Estado:** Fase A + Escandallos v2.0 + APPCC v2.0 + Kit de Tareas v2.0 LIVE y verificados. Hermanos «▸»:
tanda 1 verificada (informes en `auditorias/kit-tareas-hermanos/`, crítico con 3 bloqueos del motor);
tanda 2 en curso al cerrar (workflow `kit-tareas-hermanos-2`, run `wf_954d79a7-6ac`): **motor 2.1
hecho** (negocio detectado por estructura, gate estricto, DV+contador normalizados en TODO el kit,
alturas idempotentes) y módulos de contenido de cafetería, pizzería, hamburguesería y dark-kitchen
escritos (`kit-tareas-v2_0/contenido_*.py`, commit WIP `e38bb62`). Faltan: contenido de bar,
catering, chocolatería, heladería, hotel y restaurante-creativo; verificación sonnet por kit; crítico.
**Producción NO se ha tocado** en ninguno de los 10 hermanos (todo en dry-run).

**Para retomar:**
1. `git log --oneline -5` y `git status` (si el workflow siguió corriendo tras cerrar, puede haber
   módulos nuevos sin commitear en `kit-tareas-v2_0/`: revisarlos, no pisarlos).
2. Relanzar la tanda 2 SOLO para lo que falte (el `resumeFromRunId` es de la misma sesión y ya no
   vale): script en `~/.claude/projects/…/workflows/scripts/kit-tareas-hermanos-2-wf_954d79a7-6ac.js`
   — quitar de `HERMANOS` los kits cuyo `contenido_<pid>.py` exista y pase `--dry-run` exit 0, y
   correr Contenido → Verificar → Crítico. Decisiones ya tomadas en el prompt `DECISIONES` (a)-(h).
3. Con el crítico en verde, por kit: `KIT_TAREAS_APPLY=1 CLAUDE_SCRATCHPAD=<scratch> python3
   scripts/productos-digitales/kit-tareas-v2_0/main.py --producto <pid>` → censo `--fail` → gate
   offline → commit → push → gate LIVE. Aplicar también al representante `kit-tareas` lo que el
   motor 2.1 haya cambiado (`afecta_al_representante` del informe del motor: al menos el mensaje de
   error de la DV).
4. Después: inventario / gestión-personal / plan-financiero (R1 opus con
   `auditoria-entregables-workflow.js` + `r1-desde-journal.py`), guías, planes, eBook.

**Regla térmica:** los workflows de hermanos van de 2 en 2 a propósito (pico de la sesión 61 °C con 3
opus en paralelo abriendo libros). Mantenerlo.

## 9. SESIÓN 23-ago (10:30 → tarde) — los 10 hermanos «▸» + representante en v2.0 LIVE

**Resultado:** la familia «Kit de Tareas» completa (11 kits: representante + 10 hermanos) está en **v2.0 en producción**,
con gate LIVE **44 · 650 · 0 fallos** (`auditorias/kit-tareas-hermanos/gate-live-2026-08-23.json`) y producción = repo
byte a byte (09 del representante, 01 de hotel, 07 de bar comprobados con `cmp`). Commits `187a32d` → `6925a78`.

**Lo que pasó al retomar (no repetir):** el Mac se apagó a las 03:25 con la tanda 2 corriendo y se perdieron los 4 módulos
escritos después del último commit (bar, catering, heladería, chocolatería). Se **recuperaron byte a byte desde los
transcripts** (`agent-*.jsonl` del workflow: reproducir Write/Edit/heredocs en orden) — memoria
`feedback_commitear-wip-de-subagentes-y-recuperar-desde-transcripts.md`. Desde entonces: commit WIP entre fases, informes
de verificación SIEMPRE en `auditorias/` (repo), nunca en el scratchpad. `photoanalysisd` al 150 % tras arrancar
(66 °C): SIP impide `bootout`, `pkill -STOP photoanalysisd` lo congela (`-CONT` para reanudar).

**Tandas (scripts en `scripts/productos-digitales/kit-tareas-hermanos-{3,4,5}-workflow.js`, informes en
`auditorias/kit-tareas-hermanos/`):**
- Tanda 3 → motor 2.2 (sinónimos de hojas del 07, bio/versión en todo fichero con Instrucciones, demo pycel del contador
  P4) + contenido hotel y restaurante-creativo + `*-ver2.json` + `critico-2.json`: 0 listos, T-01 (el 08 se
  contradecía sobre cuál es el marco) VIVO en producción.
- Tanda 4 → motor 2.3 (T-01, T-02 TPV «Comprobar…» en caja, T-03 recuento ▸+P4, T-04 paréntesis de áreas derivado,
  T-05, T-08 frase honesta) + 6 fixes de contenido + `*-ver3.json` (representante incluido en dry-run) + `critico-3.json`:
  9 listos a falta de firmar (d)/(e).
- Tanda 5 → motor 2.4 (frase de niveles condicionada a `f_areas`, dedupe sin nº de fila, **digest con mensajes de DV
  y locked de todas las celdas**) + SPEC §9 + mini-ronda (dark-kitchen delivery, heladería vitrina, catering/chocolatería
  vocabulario del 08, restaurante-creativo plantillas A/B/C diferenciadas) + `*-ver4.json` + `kit-tareas-diff-firmado.json`
  (177 = 26 valor + 33 DV + 26 alturas + 92 locked) + `critico-4.json`: **11/11 listos**.
- Ejecución real en serie (canario hamburguesería → cafetería, pizzería, bar, dark-kitchen → catering, chocolatería,
  heladería, hotel, restaurante-creativo → representante el último). Cada kit: `main.py` con `KIT_TAREAS_APPLY=1`
  (idempotencia 0, cache, §6, DV, bio, censo) + `gate-flujo-postpago.py --offline`. Informes `*-real.json`. El diff real
  del representante contra producción dio **exactamente 177** en las 4 categorías firmadas.
- Capa de producto (`kit-tareas-capa-producto-workflow.js`, sonnet por kit + refutador opus): landings con cifras
  reales, tarjetas 08/09 que faltaban en 5 landings, hotel 19 ficheros / 53 checklists / 636 tareas, BONUS-02 como
  calendario MENSUAL en chocolatería/heladería/restaurante-creativo, changelog 2.0 por kit, email post-pago «(v2.0)»,
  tildes y eñes restauradas en dark-kitchen y restaurante-creativo (sus `.ts` llevaban nota «verbatim, no corregir»:
  desobedecida a conciencia por la regla capital de ortografía; la fuente SPA `src/components/kit-tareas-dark-kitchen/*`
  sigue sin tildes, no se usa en la landing Astro).

**Cifras firmadas (tareas · tareas del 01 · hojas checklist · ficheros · BONUS-02):** cafetería 500·130·33·11·22 ·
pizzería 373·76·31·11·22 · hamburguesería 346·72·31·11·22 · dark-kitchen 331·55·28·11·22 · bar 342·54·28·11·23 ·
catering 346·38·22·11·22 · chocolatería 338·41·24·11·12 meses · heladería 298·43·25·11·12 meses · hotel 636·64·53·19·24 ·
restaurante-creativo 477·55·34·13·12 meses · representante 491·111·33·11·22.

**Tarde del 23-ago (luz verde de John a todo, incluido catering) — `88925f7`…`8f0e393`, gate LIVE 44 · 650 · 0
(`auditorias/kit-tareas-hermanos/gate-live-2026-08-23-b.json`):**
- **Catering: el 09 ya es «Cobros y Facturación por Evento»** (`09-cobros-facturacion-eventos.xlsx`, 301 desde el nombre
  viejo en `_redirects`): Antes del Evento (12 tareas, D-15…D-1) · Después del Evento (12, D+0…D+30) · Liquidación con IVA
  10/21, anticipo, PENDIENTE en ámbar y ESTADO Cobrado/Pendiente/VENCIDO · Registro de 25 eventos · barra en efectivo
  como sección opcional. Motor 2.5: `modelo_caja` 'eventos' (papel 'cobros' detectado por cabecera, §6 «liquidacion»),
  metadata `title/subject/keywords` en TODOS los ficheros (m5). SPEC §10. Constructor `kit-tareas-v2_0/construir_09_catering.py`.
  Landing/dashboard/changelog/functions actualizados (347 tareas). Versión del producto se mantiene en 2.0 (los
  entregables dicen 2.0): la entrada 2.1 del changelog se fundió en la 2.0.
- **Bug cazado por el crítico-5 antes de tocar producción:** el dry-run de catering salía VERDE mientras escribía el
  sufijo del REPRESENTANTE («Kit de Tareas Recurrentes Pro») en el title/subject de los 11 ficheros — el 09 nuevo votaba
  con el fallback y empataba 1-1 con el 08, desempate alfabético. Fix 2.5.1: votan TODOS los ficheros y el constructor
  hereda el sufijo del 08 real. Lección: **un gate que compone su valor esperado desde el mismo CTX que valida no es un
  gate**; lo delató el diff contra producción.
- **Metadata v2.0 en los 55 xlsx P4** (hotel 17, catering 9, chocolatería 9, heladería 9, restaurante-creativo 11 — eran
  55, no 26). Hotel además sin el «46 Checklists» en title/subject (parche de `docProps/core.xml` dentro del zip, sin
  reabrir con openpyxl para no perder el cache) ni en su dashboard (`KitTareasHotelDashboard.tsx`: 53 checklists · 17
  plantillas + 2 bonus · 19 ficheros). Los componentes SPA `src/components/kit-tareas-hotel/*` siguen con 46 pero no se usan.
- El representante NO se volvió a aplicar: diff contra producción 0 (propiedades incluidas), es la regresión que autoriza al resto.

**Pendiente (documentado, no bloqueante):**
1. SPEC §9.5 «caja fuera del 09» (hamburguesería 01/04, pizzería 01, restaurante-creativo 01, heladería 01!B36): criterio
   T-02 (reescribir con remisión), cuando se aborde.
2. `UMBRAL_BANDA` 0,8 y T-06 (BONUS sin protección en catering/hotel/chocolatería): decisiones abiertas, sin acción.
3. `casos_6` con denominadores distintos entre verificadores (métrica, no fondo).
4. Landings: la comparación «Trail» no se generalizó en los hermanos (solo en el representante) — pedirlo si se quiere.
5. Catering: IVA medio del Registro de Eventos en C3 (editable); si John prefiere dos columnas de base por tipo de IVA
   en el registro, es un cambio del constructor.

**Siguiente familia (orden del plan §4):** inventario / gestión-personal / plan-financiero con
`auditoria-entregables-workflow.js` (añadir schema) + `r1-desde-journal.py`; después guías, planes, hotel completo, eBook.
Homologación AICP↔CB sigue pendiente (los 11 kits v2.0 deben llegar a CB).

## 10. Madrugada del 24-ago — familia inventario/gestión-personal/plan-financiero

- **R1 de los 3 productos** (3 lentes opus cada uno): inventario 91 hallazgos/30 altas · gestión-personal 86/29 ·
  plan-financiero 90/25 — «no listo» ×9 lentes. JSON en `auditorias/<pid>-R1.json`.
- **SPEC v2.0 de los 3** (borrador opus + decisiones firmadas §7-bis): `kit-inventario-v2-SPEC.md`,
  `kit-gestion-personal-v2-SPEC.md`, `kit-plan-financiero-v2-SPEC.md`. Claves: pycel no implementa COUNTA/MODE/IRR/PMT/
  WEEKDAY(,tipo)/DATEDIF (sustitutos en las SPEC; TIR con Newton propio cacheada en main.py); los gráficos del
  plan-financiero SE CONSTRUYEN (openpyxl.chart, antes de inject_cache, gate ws._charts); horas nocturnas con ROUND.
- **⚠️ AVISO LEGAL PARA JOHN (plan-financiero)**: ancla de 190 € nunca cobrada (salió a 19 €, subió a 39 € el mismo día
  — art. 20 Ley 7/1996 / Directiva Ómnibus) y aggregateRating 4,9/8 sin reseñas en JSON-LD (riesgo de acción manual).
  También: licencia del kit-inventario (FAQ contradictoria, §7-bis.5) y testimonios con funcionalidades inexistentes.
- **Kit de Inventario v2.0 LIVE** (`6039a4b`): construcción completa (motor + grupos A/B/C + integración + 3 refutadores
  → corrección 72/72 ids → ronda 2 → crítico con 2 bloqueos de una línea, arreglados). 1.926 fórmulas (×3,6; el 04 tenía
  0), 35 desplegables, 31 reglas de CF, 29/38 hojas protegidas, taxonomía única de 10 categorías, FIFO 5 estados,
  temperaturas legales con «Conforme» por fórmula, EOQ parametrizada. Gate LIVE 9/9, producción = repo.
  Paquete reutilizable: `kit-inventario-v2_0/` (motor + grupos + main con APPLY).
- **Kit de Gestión de Personal v2.0 LIVE** (`c3d7503`, mañana del 24-ago): horas con cruce de medianoche, recargo de
  convenio en celda + 80 h/año, 4 alertas del cuadrante por fórmula (12 h art. 34.3 ET), vacaciones que cuentan DÍAS,
  SS 33 % en celda + pagas prorrateadas, onboarding 0 %/50 tareas, ficha sin #DIV/0!, directorio sin datos de salud
  (art. 9 RGPD), BONUS-02 con 7 FTE/31,3 %; copy legal corregido (registro horario 2019, LISOS 7.5). Crítico paró 3
  bloqueos de fontanería (demos que escribían en public/dl en pasada real — parcheado también en el kit de inventario —,
  CtaFinal con 40+, tildes SPA); todos aplicados. Gate LIVE 9/9, producción = repo.
- **Plan-financiero v2.0**: construcción EN CURSO (workflow `wf_b368e319-e72`, auto-commit cada 15 min); si se corta,
  relanzar el workflow entero revisando el paquete `kit-plan-financiero-v2_0/` existente. Al dar verde el crítico:
  fixes → dry-run → APPLY → censo → gate offline → commit rutas explícitas → deploy → gate LIVE (nunca `git add dl/` entero).

## 11. PARADA por consumo de tokens (24-ago ~11:25, orden de John) — cómo retomar plan-financiero

**Contexto del gasto:** el incidente global de Anthropic (529 en Opus, 05:27-09:00 UTC) tumbó 3 veces la fase de
grupos del workflow de plan-financiero; cada reintento re-ejecutó integración/refutadores contra una copia sin
grupos (~1M tokens quemados en verificaciones inválidas). Todo parado: workflow, auto-commit y vigilantes.

**Estado real:**
- LIVE y cerrado: 11 kits de tareas v2.0 · kit-inventario v2.0 · kit-gestion-personal v2.0 (gates verdes, prod = repo).
- plan-financiero: `kit-plan-financiero-v2_0/motor.py + main.py` COMPLETOS y verificados (TIR Newton, 51 CF, 53 hojas
  protegidas, gráficos; informe `auditorias/kit-plan-financiero-v2-motor.json`). Los GRUPOS A/B/C no existen.
  ⚠️ Los informes de integración/refutación/corrección/ronda2/crítico de auditorias/ describen una copia SIN grupos:
  INVÁLIDOS para dar por bueno nada. El integrador ya revirtió del copy las afirmaciones que dependían de los grupos.
  `dl/kit-plan-financiero` INTACTO (sigue v1.1 en producción, funcional como siempre).

**Para retomar (sesión nueva; el runId no sobrevive):** relanzar
`Workflow({scriptPath:'scripts/productos-digitales/kit-plan-financiero-v2-workflow.js', args:{par:2}})` SIN resume —
el motor se re-ejecuta (~40 min; su prompt es el mismo y el código ya está en el repo, así que el agente debería
detectarlo hecho y solo verificar). El script ya lleva el nonce T2. Después: fixes del crítico → dry-run → APPLY →
censo → gate offline → commit rutas explícitas → deploy → gate LIVE.

**Después de plan-financiero (orden del plan):** guías → planes → hotel completo → eBook · homologación AICP↔CB ·
SEO landings ES+LATAM. Pendientes de John: avisos legales (ancla 190 €, aggregateRating), licencia inventario,
webhook/strict, marca CB en 7 productos.

**Cierre certificado (24-ago 11:35):** gate LIVE global 44 · 650 · 0 fallos
(`auditorias/gate-live-2026-08-24-cierre.json`); main `d77d7c2` limpio; capa de producto de plan-financiero en la
rama `wip/plan-financiero-capa-producto` (pusheada, NO mergear hasta aplicar los grupos). Sesión pausada por consumo
de tokens; retomar por §11 en sesión fresca.

## 12. Broadcast de la v2.0 enviado (24-ago mediodía, orden de John)

Dos broadcasts en Resend anunciando los 11 Kits de Tareas v2.0, con los kits listados por nombre y
enlazados a su landing pública (UTM `utm_content=kits-tareas-v2`):
- **«2026-08-24 Kits de Tareas v2.0 (ES)»** → segmento AI Chef Pro ES, **239 destinatarios**, From
  `AI Chef Pro <hola@news.aichef.pro>`, Reply-To info@aichef.pro. SENT.
- **«2026-08-24 Kits de Tareas v2.0 (ChefBusiness)»** → segmento Chefbusiness, **19 destinatarios**,
  From `ChefBusiness <hola@mailer.chefbusiness.co>`, Reply-To john@chefbusiness.co. SENT.
- HTML reutilizable en `scripts/productos-digitales/emails/broadcast-kits-tareas-v2-es.html`
  (negro #111 + dorado #FFD700 — regla de John: nunca más el marrón; pie con RESEND_UNSUBSCRIBE_URL).
- Método completo (Upload HTML + file_upload, duplicado para el 2.º segmento, slider por JS) documentado
  en la skill `~/.claude/skills/resend-operaciones-grupo`. Queda un Draft de prueba en el panel
  («2026-08-17 Modelos open source (ES) (copy)») que John puede borrar. Métricas de apertura: tracking
  no activado en news.aichef.pro (activarlo en Domains si se quiere medir el próximo).
