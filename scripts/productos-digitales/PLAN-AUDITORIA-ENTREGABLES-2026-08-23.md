# Plan — Auditoría y saneamiento de los 630 entregables restantes (arranque 2026-08-23)

> Pregunta de John (2026-08-22, 02:30): «¿los ficheros de cada dashboard están disponibles y
> auditados, sin defectos?». Disponibles sí (645/645 LIVE); auditados **solo el Kit Pastelería**
> (15 ficheros, 2 rondas adversariales). Este plan cubre los otros 43 productos.
> Método de referencia: lo que funcionó en pastelería el 2026-08-21/22 (workflow 3 lentes → fixes
> → ronda 2), con el reparto de modelos acordado con John (memoria
> `feedback_auditorias-que-modelo-para-que`): **scripts para lo medible · opus descubre (ronda 1,
> 1-2 representantes por familia) · sonnet verifica (ronda 2) y ejecuta fixes mecánicos · opus para
> generadores/post-procesos con criterio · haiku no audita · Fable orquesta y firma.**
> Regla térmica: scripts python EN SERIE, `istats cpu temp` entre pasos, nada de builds locales.

## 0. Punto de partida (censo 2026-08-22, `censo-entregables-2026-08-22.json`)

645 entregables servidos = 458 xlsx + 61 docx + 9 pdf (+ 39 xlsx HUÉRFANOS en la raíz de
`astro-site/public/dl/` que **ningún producto sirve** — fuera del alcance; candidatos a borrar
tras confirmar con `grep -r` que nada los enlaza).

| Defecto medible | xlsx afectados | Efecto para el cliente |
|---|---|---|
| Fórmulas sin valor cacheado (7.684) | **179** | Totales en blanco en móvil / Numbers / visores |
| ☐ en columna A que NO cuenta (COUNTIF mira otra columna) | **79** | Marca tareas y el contador sigue en 0 |
| Bio caducada dentro del xlsx («29 años…») | 25 | Dato falso firmado |
| Sin impresión A4 (paperSize ≠ 9) | 401 | Hojas cortadas al imprimir |
| `creator = openpyxl` / sin título | 443 | Cosmético |
| Caracteres no latinos | 0 | — |

## 1. Familias, generadores y REPRESENTANTES (auditoría opus a fondo)

| Familia | Productos (ficheros) | Generador común | Representantes ronda 1 (opus) | Hermanos (sonnet verifica contra los hallazgos del representante) |
|---|---|---|---|---|
| **Kits de tareas** | kit-tareas 11 · cafeteria 11 · pizzeria 11 · hamburgueseria 11 · dark-kitchen 11 · bar 11 · catering 11 · hotel 19 · heladeria 11 · chocolateria 11 · restaurante-creativo 13 · chef-privado 9 · sushi-bar 11 · asador 11 · marisqueria 11 · panaderia 11 · food-truck 11 · tapas-bar 11 · **mega-pack-tareas** (agrega todos) | `scripts/generate-tareas-*.py` + `generate-checklists-negocio.py` (08/09 de 12 kits) | **kit-tareas** (base restaurante) y **kit-tareas-hotel** (19, estructura distinta) | los otros 16 |
| **Guías «Cómo montar»** | gastronomico 18 · casual 15 · panaderia-obrador 15 · mexicano 15 · peruano 15 · japones 15 · nikkei 15 · dark-kitchen 3 (+3 docx +1 pdf cada una) | `scripts/generate-guia-*.py` | **guia-restaurante-gastronomico** | los otros 7 |
| **Planes de negocio** | línea A (2 ficheros): bar-restaurante, cafeteria, food-truck, panaderia, tapas-bar · línea B (4 xlsx + 5-7 docx): cocteleria, paellero, parrillero, catering-tematico, chef-privado-showcooking | `scripts/generate-plan-*.py` | **plan-negocio-bar-restaurante** (A) y **plan-negocio-cocteleria-eventos** (B) | los otros 8 |
| **Kits Excel únicos** (los que más se venden) | kit-escandallos 12 · pack-appcc 17 · kit-inventario 9 · kit-gestion-personal 9 · kit-plan-financiero 10 | uno por producto | **los 5, a fondo** (no tienen hermanos) | — |
| **eBook Pro Prompts** | 1 pdf + 1 docx + 1 xlsx (env vars) | — | revisión de texto (sonnet) | — |

Orden de ejecución (por dinero y por riesgo): **1) kit-escandallos · 2) pack-appcc · 3) kit-tareas
(representante) → 7 kits con el bug de la casilla · 4) kit-inventario / gestion-personal /
plan-financiero · 5) guías · 6) planes · 7) hotel y resto de kits · 8) eBook.**

## 2. Fases

### Fase A — Saneamiento determinista transversal (sonnet escribe, scripts ejecutan, 1 sesión)
1. Generalizar `kit-pasteleria-v1_1-postprocess.py` → **`postprocess-transversal.py <productId|carpeta> [--dry-run]`**, idempotente, que aplique a TODOS los xlsx de la carpeta: metadata (creator/title/subject/keywords «AI Chef Pro»), impresión A4 con `print_title_rows`/freeze/pie en hojas de trabajo, bio anclada (sustituciones 1:1 de `29 años…`), **casilla unificada** donde haya tabla con cabecera «Tarea» + ☐ en col. A (Nº correlativo en A, marca en la columna del COUNTIF renombrada «✓ Completada», DV «✓,—,N/A», CF verde, denominador dinámico), línea de versión en Instrucciones, y al final `inject_cache.py` (ya idempotente) + verificación `data_only` (0 sin cache salvo cadena vacía por diseño), 0 no-latinos, 0 datetime en numéricos. Informe por fichero.
2. `--dry-run` sobre los 458 → leer el informe → ejecutar por familia → `gate-flujo-postpago.py --offline` → commit por familia (`git add astro-site/public/dl/<producto>/`) → push → deploy → gate LIVE → descargar 2-3 de producción y abrir `data_only`.
3. Gate nuevo: **`censo-entregables.py`** (el script del censo del 22-ago, versionado) con `--fail` para que vuelva a 0 en cache/casilla/bio/A4 y no se repita la deriva.

### Fase B — Ronda 1 adversarial por representante (opus, 3 lentes, Workflow)
`Workflow({scriptPath: 'scripts/productos-digitales/auditoria-entregables-workflow.js', args: {productId: 'kit-escandallos', familia: 'kit-excel'}})`
— lentes: **experto de dominio** (prompt por familia: chef/jefe de cocina por sector para kits de tareas; consultor de aperturas para guías y planes; técnico de costes/APPCC/RRHH/finanzas para los kits Excel), **técnica Excel** (pycel en vivo, rangos, DV, CF, formatos, impresión, cache), **coherencia comercial** (landing ↔ dashboard ↔ emails ↔ ficheros ↔ changelog). Salida: `scripts/productos-digitales/auditorias/<productId>-R1.json` (commiteado: sobrevive al reinicio).

### Fase C — Fixes (opus con criterio / sonnet mecánico) + hermanos
- Representante: post-proceso idempotente `<producto>-v1_1-postprocess.py` o generador corregido.
- Hermanos: sonnet aplica el MISMO post-proceso y verifica cada hallazgo del representante en cada hermano (informe por fichero); lo que no encaje → mini-ronda opus solo para ese hermano.
- Dashboard/changelog: entrada v1.1 por producto en `src/data/productos-changelog.ts` + `<ProductVersionBadge/>` + `<ProductChangelog/>` (ya existen; hoy solo los usa pastelería) y `updateNote` en la landing.

### Fase D — Ronda 2 (sonnet) + cierre
Verificación celda a celda de cada id de la R1 (resuelto/parcial/no) + regresiones + gate offline → commit → push → deploy → gate LIVE → descarga de producción `data_only`. Handoff + memoria + **nota para homologación CB** (regla de John: una sola versión; CB replica).

## 3. Criterios de «listo» por producto
- `censo-entregables.py --fail` en verde (0 sin cache / 0 ☐ en A / 0 bio vieja / 0 sin A4 / creator AI Chef Pro).
- R1 y R2 en `auditorias/` con veredicto «listo» o descartes justificados.
- Gate offline y LIVE 0 fallos; ficheros de producción = md5 repo.
- Landing/dashboard/emails coherentes con los ficheros reales (cifras, nombres de hojas, promesas).

## 4. Coste y tiempos estimados
- Fase A: 1 sesión (scripts + 43 carpetas en serie + deploy).
- Fases B-D: ~1 sesión por representante (5 kits Excel + 5 representantes de familia = ~10
  sesiones cortas), hermanos en tandas de 3-4 con sonnet. Opus solo en B y en los fixes con criterio.

## 5. Estado — 2026-08-22: FASE A EJECUTADA Y LIVE

- Herramientas: `FASE-A-SPEC-postprocess-transversal.md` (spec), `postprocess-transversal.py`
  (idempotente; `--dry-run` sobre copias; 8 patrones P1-P5 por cabecera), `censo-entregables.py`
  (gate `--fail`). Resumen por producto: `auditorias/fase-a-resumen-2026-08-22.json`.
- Commits `ee415aa`…`fa784ff` (7), deploy `ready` 11:26, **gate LIVE 44 productos · 645 entregables ·
  0 fallos** (2 × 502 transitorios reintentados), md5 producción = repo, censo `--fail` 0 defectos
  en los 458 xlsx, 0 contadores duplicados en 1.204 hojas. 38 huérfanos de la raíz borrados.
- Reparaciones de fórmulas rotas (vendidas): escandallos `10-calculadora-pvp` (9 × `/=AVERAGE`),
  dark-kitchen `calculadora-viabilidad` (12 celdas circulares + food cost sobre comisiones),
  `cash-flow-break-even` B12 circular en 5 guías, onboarding «Progreso (%)» con filas literales,
  6 etiquetas «= …» que abrían con `#¿NOMBRE?`.
- Método: 2 refutadores (15 hallazgos, 5 altas) + 3 residuos del dry-run `all` + 1 defecto cazado en
  la ejecución real (segundo contador en 4 kits: el existente se reconocía por etiqueta, no por
  fórmula). Lecciones en memoria.
- Para la Fase B: B13 «Break-Even (meses)» vacía en 5 guías; 43 hojas P2/P3/P4 sin contador (motivo
  anotado); marca ChefBusiness en 7 productos de origen CB (decisión de John); el workflow de R1
  usa `agent()` sin `schema` → parsear el JSON o añadir schema antes de usarlo.
