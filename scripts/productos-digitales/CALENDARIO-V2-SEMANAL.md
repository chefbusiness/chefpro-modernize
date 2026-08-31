# Calendario semanal — v2.0 de los productos digitales + productos nuevos (aichef.pro)

> Creado el 2026-08-29 por orden de John: la sesión del 28-29 de agosto consumió ~40 % de la cuota semanal de la
> suscripción máxima en un día. **A partir de aquí: 1 producto por semana (máximo 2), en una sesión corta, y nunca
> más de una familia en paralelo.** Este fichero es la fuente de verdad del ritmo; la SPEC de cada familia es la
> fuente de verdad del contenido. Estado y bitácora detallada: `SESSION_HANDOFF_2026-08-22-B-fase-a-entregables.md` §13-§17.

## 0-bis. ⚠️ DECISIONES DE JOHN DEL 2026-08-31 — mandan sobre todo lo de abajo

Tres decisiones que reorientan la línea. **La tabla de 17 semanas del §2 deja de ser un calendario y pasa a ser la COLA
de prioridad de la línea v2.0**; lo que fija el ritmo es la alternancia.

### 1. Sesiones ALTERNADAS (no semanas)

| Sesión | Qué se hace |
|---|---|
| impar | Actualizar a v2.0 un producto pendiente (siguiente de la cola del §2) |
| **par** | **LANZAR un producto NUEVO** |

Razón de John: «llevamos mucho tiempo sin lanzar un producto nuevo y, además, tenemos muchos productos que lanzar».
La línea v2.0 mejora lo que ya se vende pero no abre mercado. El techo de presupuesto del §0 **no cambia**.

**Primer producto nuevo, elegido por John: «Guía Food Cost + Ingeniería de Menú»** (§3, nº1). Reutiliza
`escandallo-maestro` y `menu-engineering-matrix` v2.0 y el bono de food cost del kit de escandallos; keywords ya medidas
en 8D. Ojo a la alerta de coordinación del catálogo: estaba anunciada en AICP para julio y en CB para septiembre — la
duplicidad **se disuelve sola** con la decisión 2.

### 2. TIENDA OFICIAL ÚNICA: `aichef.pro/productos-digitales` — se acabó replicar en ChefBusiness

**Revoca la regla del 2026-08-18** («AICP y CB = una sola versión; si AICP actualiza, CB replica»).

- Landing, Payment Link, entregables (`dl/`), dashboard y functions de cada producto viven **solo aquí**.
- ChefBusiness y el resto de marcas del grupo ponen una **tarjeta que enlaza a la landing de aichef.pro**; la compra se
  cierra aquí. Palabras de John: «nos ahorramos duplicar infraestructura y vamos más rápido».
- **La homologación AICP↔CB queda CANCELADA.** `homologacion-aicp-cb-censo-2026-08-18.json` pasa a histórico.
  ⚠️ **Antes de darla por muerta**: ese censo decía que **CB iba por delante en 6 planes de negocio v2.0 + guía casual +
  catering**. Si eso sigue siendo cierto, hay que traer ese material a aichef.pro, que ahora es la única tienda — o se
  pierde. **Comprobarlo antes de archivar nada.**
- Nota de dictado: «Hspro» = AI Chef Pro. **No** es el site `hosply` (repo `chefbusiness/hosply` → www.hosply.pro), que
  existe de verdad y es otra cosa.

### 3. Después del español: los mismos productos NATIVOS en inglés

Cerrado el catálogo ES, se rehacen todos en **inglés nativo** (no traducción: normativa, fiscalidad y benchmarks son del
mercado), en la misma tienda, bajo `/en/`. Después, otros idiomas. Clientes ya los están pidiendo. **No se arranca hasta
cerrar el ES.**

---

## 0. Reglas de presupuesto (no negociables)

1. **Techo por semana: ~15 % de la cuota** (≈ 1 producto hermano completo o 1 producto nuevo por fases). Antes de empezar,
   mirar el consumo de la semana en la app; si ya va por el 60 %, esa semana no se toca esta tarea.
2. **Reparto de modelos:** Fable orquesta y verifica lo crítico (APPLY, gates, LIVE); **sonnet** construye contenido de
   hermanos y hace fixes mecánicos; **opus** SOLO para una refutación por producto y para el crítico. Nada de 3 lentes
   opus por hermano (eso es lo que disparó el gasto): un refutador con dos lentes en el mismo prompt.
3. **No se repite ninguna R1** (las 4 familias ya están auditadas y mapeadas id→sección en sus SPEC). No se reescriben
   motores: están construidos y en producción. Sólo `contenido_<pid>` + fixes + APPLY.
4. **Un solo workflow por sesión, con `par: 1`**, y siempre `schema` + `model` explícito (memoria
   `feedback_workflow-agentes-sin-schema-devuelven-string`). Térmica: `istats cpu temp` antes de cada python.
5. **Texto largo (guías PDF, planes docx) SIEMPRE con bridge.py** (`--model ~deepseek/deepseek-v4-flash-latest --max-tokens 8192`):
   es barato; lo caro es el agente que lo orquesta, así que se le da el guion ya hecho y se le pide una pasada.
6. **Cada semana termina con push y gate LIVE del producto tocado** (nunca dejar un producto a medias en `dl/`).

**Coste medido el 29-ago (tokens de subagentes):** hermano construido + refutado ≈ 0,6-0,9 M · fixer de un crítico ≈ 0,3 M ·
representante entero (motor + grupos + 3 refutadores + corrección + ronda 2 + crítico) ≈ 3-4 M · documentos de una guía
(pipeline + generación + 2 refutadores + corrección + crítico) ≈ 2-3 M. **Una semana «normal» debe quedarse por debajo de 1,5 M.**

## 0-ter. ESTADO AL CERRAR EL 1-SEP (manda sobre el §1, que es del 29-ago)

### guia-restaurante-gastronomico — a MEDIO CAMINO, no publicada

**LIVE y correcto:** los 18 xlsx con el **IVA de la bebida en sala al 10 %** (decisión de John, RD-17) y sin
instrucciones duplicadas. Commits `379fe79` y `72668fc`.

**NO publicado:** los tres documentos, sus dos PDF nuevos y el cableado que apunta a ellos (dashboard, landing y los
**dos** mapas de descarga — están duplicados). Todo revertido a la versión publicada **a propósito**: el crítico final
devolvió **120 hallazgos, 58 bloqueantes** (`auditorias/guias-v2-critico-final-2026-09-01.json`).

**Lo hecho y que NO hay que repetir:** 59 correcciones de coherencia aplicadas y refutadas · las 3 páginas de basura del
cap. 15 · los 4 truncamientos · dos focos de la «t» caída (caps. 5 y 21) · las tablas con el «0,06» bajo un encabezado
«(%)» · los tres documentos llegaron a estar con **todos los gates en VERDE**.

**Lo que falta:** segunda tanda sobre los 58 bloqueantes → gates → crítico → copiar a `dl/` + restaurar el cableado →
LIVE. Receta y detalle completo en el handoff **§20**.

### ⚠️ Deuda nueva detectada, para meter en la cola

1. **El error del 21 % de IVA está VIVO en la familia de PLANES** (`planes-v2_0/grupo_a.py`), y afecta a los **10 planes
   publicados**. En un bar o una coctelería la bebida es el negocio, así que pesa más que en la guía. El arreglo ya está
   diseñado y probado en las guías: subir el tipo a `motor.PARAMETROS`, celda verde con nota, regenerar. **Candidato a
   ser lo primero de la siguiente sesión impar.**
2. **`_instr` acumulaba la instrucción vieja al editar el texto** (arreglado en guías). Revisar si el mismo helper se
   usa igual en las otras familias.
3. **Pasarela CRYPTO** (`PAGOS_CRYPTO_PENDIENTE.md`): infraestructura, no producto. Decidir si desplaza una sesión.

---

## 1. Estado al cerrar el 29-ago

### LIVE en v2.0 (no se tocan salvo hotfix)
- 11 kits de tareas «▸» (kit-tareas + cafetería, pizzería, hamburguesería, dark-kitchen, bar, catering, chocolatería, heladería, hotel,
  restaurante-creativo) · kit-tareas-pasteleria · kit-escandallos · pack-appcc (cita anisakis RD 1021/2022 ✅) · kit-inventario ·
  kit-gestion-personal · kit-plan-financiero · **plan-negocio-bar-restaurante** (xlsx; docx v1.1) · **guia-restaurante-gastronomico** (18 xlsx;
  docx/PDF: ver §2 semana 1).

### Construido en disco y SIN aplicar (lo que quedó al parar)
| Producto | Familia | Qué hay | Qué falta |
|---|---|---|---|
| guia-restaurante-gastronomico (documentos) | guías | `documentos.py` + `guion_…py` + **PDF 119 págs / 62.904 palabras / 32 tablas + 2 bonus docx** generados en `guias-v2_0/build/guia-restaurante-gastronomico/` (fuera de `dl/`); 2 refutadores «no listo» (`auditorias/guias-v2-doc-ref-{dominio,tecnico}.json`) | corrector (opus, 1 pasada sobre los hallazgos) → crítico → copiar 4 ficheros a `dl/` con los mismos nombres → censo/gate/no-latinos → LIVE → landing con «119 páginas» medidas |
| plan-negocio-cafeteria | planes A | `contenido_plan_negocio_cafeteria/a.py` + refutación (24 hallazgos / 8 altas) | fixes sonnet → dry-run 13/13 → APPLY |
| plan-negocio-tapas-bar | planes A | contenido + refutación (25 / 9 altas) | idem |
| plan-negocio-panaderia | planes A | contenido + refutación (18 / 6 altas) | idem |
| plan-negocio-food-truck | planes A | `contenido_plan_negocio_food_truck/` PARCIAL (el agente se paró a medias) | revisar/completar contenido → refutar (1 opus) → fixes → APPLY |
| kit-tareas-sushi-bar | kits CB | motor extendido (CB-E1..E9, `regresion.py`), `contenido_kit_tareas_sushi_bar.py`, 3 refutaciones y corrección | ronda 2 (sonnet) → crítico (opus) → canario **chef-privado** → APPLY sushi-bar |
| guia-restaurante-casual | guías | contenido a/b/c + refutación (25 / 10 altas) | fixes → APPLY → documentos |
| guia-restaurante-mexicano | guías | contenido + refutación (25 / 8 altas) | idem |
| guia-restaurante-peruano | guías | contenido + refutación (25 / 12 altas) | idem |
| guia-restaurante-japones | guías | `contenido_guia_restaurante_japones/` PARCIAL | completar → refutar → fixes → APPLY → documentos |

### Sin empezar
- Planes línea B: coctelería (representante B: `grupo_b.py` + contenido; SPEC §3), parrillero, paellero, catering, chef-privado-showcooking.
- Planes docx (10): regeneración con bridge.py (SPEC planes §4) — se hace con el producto de su semana.
- Guías: nikkei, panadería-obrador, dark-kitchen (+ documentos de los 7 hermanos: el pipeline `documentos.py` es de familia).
- Kits CB: asador, marisquería, panadería, food-truck, tapas-bar, chef-privado (canario), mega-pack (decisión de John si se amplía).
- eBook Pro Prompts: revisión de texto (sonnet, 1 sesión corta).
- Homologación AICP↔CB (otra terminal, chefbusiness-astro).

## 2. Calendario (semana = lunes a domingo; 1 producto, máx. 2)

| Semana | Producto(s) | Trabajo | Presupuesto |
|---|---|---|---|
| **S1 · 31 ago – 6 sep** | guia-restaurante-gastronomico (documentos) · plan-negocio-cafeteria | si el workflow de documentos terminó: crítico → copiar → LIVE; si no, relanzar SOLO el paso que falte. Cafetería: fixes de sus 8 altas (sonnet) → APPLY | 1,2 M |
| S2 · 7 – 13 sep | plan-negocio-tapas-bar · plan-negocio-panaderia | fixes → APPLY cada uno (ya refutados) | 0,8 M |
| S3 · 14 – 20 sep | plan-negocio-food-truck · kit-tareas-sushi-bar | completar contenido food-truck + 1 refutación; sushi-bar: ronda 2 + crítico + canario chef-privado + APPLY | 1,5 M |
| S4 · 21 – 27 sep | guia-restaurante-casual (+ sus documentos) | fixes → APPLY → `documentos.py` con guion casual (bridge) + 1 refutador | 1,5 M |
| S5 · 28 sep – 4 oct | guia-restaurante-mexicano (+ documentos) | idem | 1,5 M |
| S6 · 5 – 11 oct | guia-restaurante-peruano (+ documentos) | idem | 1,5 M |
| S7 · 12 – 18 oct | guia-restaurante-japones (+ documentos) | completar contenido → refutar → fixes → APPLY → documentos | 1,8 M |
| S8 · 19 – 25 oct | guia-restaurante-nikkei (+ documentos) | contenido (sonnet) → 1 refutación → fixes → APPLY → documentos | 1,8 M |
| S9 · 26 oct – 1 nov | guia-panaderia-obrador (+ documentos) | idem (molde B: sin columna de coste, decisión 17) | 1,8 M |
| S10 · 2 – 8 nov | guia-dark-kitchen (+ documentos +40 págs) | idem (moldes C/D, 3 xlsx) | 1,2 M |
| S11 · 9 – 15 nov | plan-negocio-cocteleria-eventos (representante B) | `grupo_b.py` + contenido (opus, 1 agente) → 1 refutación → fixes → APPLY + docx | 2,5 M |
| S12 · 16 – 22 nov | plan parrillero · plan paellero | contenido B (sonnet) → refutar → APPLY + docx | 1,5 M |
| S13 · 23 – 29 nov | plan catering-tematico · plan chef-privado-showcooking | idem | 1,5 M |
| S14 · 30 nov – 6 dic | kit-tareas-asador · kit-tareas-marisqueria (anisakis pendiente aquí) | contenido (sonnet) → refutar → APPLY | 1,2 M |
| S15 · 7 – 13 dic | kit-tareas-panaderia · kit-tareas-food-truck (molde PLANO) | idem | 1,2 M |
| S16 · 14 – 20 dic | kit-tareas-tapas-bar · kit-tareas-chef-privado (+ mega-pack) | idem; chef-privado ya lo arregla el motor (contadores «5 de 41») | 1,0 M |
| S17 · 21 – 27 dic | 10 planes: docx restantes + eBook Pro Prompts | regeneración bridge de los docx que falten + revisión sonnet del eBook | 1,0 M |

Las semanas con **producto nuevo** (§3) van INTERCALADAS: cuando toque una, la v2.0 de esa semana se salta (no se hacen las dos).

## 3. Micro-proyecto «productos nuevos» (Hoja 4 del catálogo `/Users/johnguerrero/productos-digitales/`)

Cola real (la guía de panadería/obrador ya salió el 14-may): **5 productos**. Orden propuesto por demanda y reutilización
de motores ya construidos (John decide):
1. **Guía Food Cost + Ingeniería de Menú** (guía técnica premium) — reutiliza `escandallo-maestro` y `menu-engineering-matrix` v2.0 y el bono de food cost de escandallos; es lo más buscado (keywords ya medidas en 8D).
2. **Manual del Manager de Restaurante** (manual operativo) — reutiliza kit-gestion-personal y kit-tareas.
3. **Manual del Chef Ejecutivo** — reutiliza brigada/turnos y APPCC.
4. **Cómo Montar una Pastelería** (guía premium) — sobre el motor de guías + kit-tareas-pasteleria v2.0.
5. **Cómo Montar una Chocolatería** — idem + kit-tareas-chocolateria.

**Método por producto nuevo, en 3 semanas de 1 sesión cada una** (memoria `feedback_research-previo-producto-nuevo`, `feedback_productos-completos-investigados`,
`feedback_digital-products-non-negotiables`, skill `digital-product-launch`):
- **Semana A — research + SPEC**: keyword research + SERP (`scripts/dataforseo.py`), GSC, competencia, precio; SPEC del producto (opus, 1 agente) con
  lista de entregables, guion de documentos y decisiones firmadas. Presupuesto 0,8 M.
- **Semana B — entregables**: xlsx con los motores de familia existentes + documentos con `documentos.py` + bridge.py; 1 refutador (opus) + fixes
  (sonnet); gates (censo, no-latinos, páginas). Presupuesto 1,5 M.
- **Semana C — capa de producto y lanzamiento**: landing (plantilla existente), dashboard, functions, Payment Link de Stripe (John), changelog, hub,
  banners en el blog; gate offline + LIVE. Presupuesto 0,8 M.

Propuesta de intercalado: **S3, S6, S9, S12, S15…** se dedican al producto nuevo (A, B, C consecutivas para el primero: S3-S5), desplazando la v2.0 de esa
semana una semana. Primer lanzamiento realista: **Guía Food Cost + Ingeniería de Menú a mediados de octubre**.

## 4. Protocolo de cada sesión semanal (copiar y seguir)

1. `git pull --ff-only`, leer este fichero y el §16-17 del handoff; `istats cpu temp`.
2. Mirar el consumo semanal en la app; si > 60 %, no empezar.
3. Un solo producto: (a) si ya tiene contenido + refutación en `auditorias/`, lanzar SOLO el fixer (sonnet) con la lista de hallazgos → dry-run → mi
   verificación de 5-6 celdas → APPLY con respaldo → censo → gate offline → `gate-no-latinos.py --only` → commit rutas explícitas → push → gate LIVE + md5.
   (b) si no tiene contenido: 1 agente sonnet construye `contenido_<pid>` siguiendo el del representante → 1 refutador opus (dos lentes en un prompt) →
   (a).
4. Documentos (guías/planes): `documentos.py` + guion del producto (el del representante como plantilla) → bridge.py → 1 refutador → fixes → copiar a `dl/`.
5. Cerrar: handoff (una línea por producto), `git push`, gate LIVE del producto. Parar aunque sobre presupuesto: el margen es para el resto de frentes.

## 5. Decisiones de John que siguen abiertas (no bloquean el calendario)
- Capa comercial intacta por orden suya (ratings, testimonios con marcas reales en kit-hotel, anclas): inventario en
  `auditorias/capa-comercial-inventario-2026-08-29.json`.
- Mega-pack: ¿se amplía con los 6 kits CB? · Licencia del kit de inventario · Webhook Stripe / `PURCHASE_VALIDATION` strict · Marca CB en 7 productos
  (deliberada) · Nombre del enlace «Kit Gestión Personal» vs página «Kit Gestión de Personal y Turnos».
