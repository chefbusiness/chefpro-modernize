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
mercado), en la misma tienda, bajo `/en/`. Después, otros idiomas. Clientes ya los están pidiendo. ~~No se arranca hasta
cerrar el ES.~~ **DEROGADO por John el 2026-09-23: el frente EN arranca ya, en ROTACIÓN DE 3 SESIONES (v2.0 ES → producto
nuevo ES → producto EN).** Doc canónico: `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`.

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

### ✅ 2026-09-04 — «Guía Food Cost + Ingeniería de Menú» LANZADA (producto nuevo nº 1, sesión par)

En producción a 55 € (`/guia-food-cost-ingenieria-menu`): guía de 95 páginas + bonus de 32 + 8 xlsx. Handoff:
`SESSION_HANDOFF_2026-09-03-guia-food-cost.md`. **Siguiente sesión = impar (v2.0 pendiente)**: lo primero de la cola sigue
siendo el IVA del 21 % vivo en la familia de PLANES (§ deuda 1) o rematar los documentos de la guía gastronómica (§20 del
handoff B). **Regla nueva de John: los productos NO se escriben con bridge.py** (subagentes Anthropic; patrón
`guias-v2_0/dump_prompts.py` + `check_bloque.py`): el presupuesto por producto sube (≈ 5,5 M tokens la redacción de una guía de
95 páginas) y hay que contarlo así en las semanas de guías.

### ✅ 2026-09-05 — «Manual del Manager de Restaurante» PUBLICADO (producto nuevo nº 2, por orden expresa de John el 4-sep)

En `main` (`4a649d0`) a 55 € (`/manual-manager-restaurante`): manual de 77 páginas + bonus de 28 + 7 xlsx; gates en verde. **LIVE completo a las 02:10 del 5-sep** (Payment Link de John, env, `sync-payment-links.py`, redeploy, gate LIVE 0 fallos) y mailing
programado para el lunes 7-sep 10:00 Madrid (handoff `SESSION_HANDOFF_2026-09-04-manual-manager.md`). Primer producto de la línea «Manuales operativos»; siguen Chef Ejecutivo,
Pastelería y Chocolatería. Coste ≈ 10,5 M tokens de subagentes (dos productos nuevos en dos días: la alternancia se retoma con una
sesión impar). Hotfix colateral: la landing de la Guía Food Cost servía dos botones de WhatsApp.

### ✅ 2026-09-05 (sesión IMPAR, Claude Code en el Mac) — RD-17 aplicado a la familia de PLANES: bar-restaurante 2.1

El 21 % en la bebida solo vivía en **`plan-negocio-bar-restaurante`** (único con el molde v2.0 en producción): los otros 9
siguen en v1.1 y no lo llevaban. Parámetro `iva_bebida` (B63, 10 %), mezcla de ventas por canal (el alcohol que sale por
delivery sí va al 21 %), compras intactas, DV purgadas por solape (bloqueante cazado por la refutación), changelog 2.0 + 2.1,
landing/dashboard con las cifras reales (9 hojas, 7 fases, 64 trámites), paellero `C23` sin «21%». Detalle en el handoff
`SESSION_HANDOFF_2026-09-05-rd17-planes.md`. **Próxima sesión impar**: documentos de la guía gastronómica (handoff B §20).
**Segunda parte del 5-sep (luz verde de John, presupuesto suspendido): los 4 hermanos de línea A (cafetería, tapas-bar,
panadería, food-truck) pasan de 1.1 a 2.2 y el bar de 2.1 a 2.2 con el motor 2.2/2.2.1** (`f9283b3`; handoff
`SESSION_HANDOFF_2026-09-05-planes-linea-A-2.2.md`). Línea A: HECHA salvo los docx (T9). Queda la línea B (5 planes v1.1) y
el T9 de documentos.
**Correos (regla de John del 5-sep: un broadcast por producto actualizado/nuevo, cola de 5 días):** Manual 7-sep · Bar-Restaurante 2.1
**12-sep** (programado) · hermanos de línea A en los slots 17-sep, 22-sep, 27-sep y 2-oct según se apliquen.
> 🔄 **Cola REPROGRAMADA el 6-sep** (decisión del orquestador con «sobre Resend decide tú» de John): el lanzamiento del **Manual del
> Chef Ejecutivo** ocupa el **lunes 14-sep 10:00 Madrid** y las actualizaciones de línea A se corren un hueco: bar-restaurante
> **19-sep**, cafetería **24-sep**, tapas-bar **29-sep**, panadería **4-oct** (los cuatro recreados por API: Resend no permite editar
> un broadcast programado, sólo borrarlo y crearlo de nuevo) y **food truck 9-oct, que quedó como BORRADOR** «Actualización Plan de
> Negocio Food Truck 2.2 (ES) — PROGRAMAR 9-oct» porque Resend no admite programar a más de 30 días vista: **programarlo a partir
> del 9-sep** (`resend-broadcast.py --scheduled-at 2026-10-09T08:00:00Z` o desde el panel). ✅ **PROGRAMADO el 10-sep** (`POST /broadcasts/{id}/send` con `scheduled_at`, aprobado por John; el nombre conserva el sufijo «— PROGRAMAR 9-oct» porque Resend no renombra un broadcast programado). Trampa cazada: al recrear, leer el
> asunto ANTES de borrar y con `json.loads(strict=False)` (el html trae caracteres de control); un `DELETE` sin el asunto en la mano
> obligó a reconstruir cuatro asuntos por el patrón del quinto.

### ✅ 2026-09-06 (sesión PAR, Claude Code en el Mac) — «Manual del Chef Ejecutivo» PUBLICADO (producto nuevo nº 3, 65 €)

En `main` (`b056abc` → `c2ceccc`) a **65 €** (decisión de John; el Manager sigue a 55 €): manual de 96 páginas + bonus de 34 + 7 xlsx;
gates en verde; Payment Link de John a las 22:30; **nace con la pasarela cripto** (`CRYPTO_PRODUCTS=kit-tareas-cafeteria,manual-chef-ejecutivo`);
mailing programado el **lunes 14-sep 10:00 Madrid** (cola de línea A desplazada un hueco, ver arriba). Handoff
`SESSION_HANDOFF_2026-09-06-manual-chef-ejecutivo.md`. Coste ≈ 17 M tokens de subagentes (sesión dedicada por John). Hallazgo de
método: `documentos.py` reparte epígrafes pero no `puntos` entre los bloques de un capítulo → prosa duplicada; medir en Food Cost y
Manager (sesión impar). **Próxima sesión = impar**: anisakis en producto vendido (punto 0 de la deuda) y luego documentos de la guía
gastronómica (handoff B §20).

### ✅ 2026-09-10 (sesión PAR, Claude Code en el Mac, NOCHE ENTERA por orden de John) — «Cómo Montar una Pastelería» CONSTRUIDA (producto nuevo nº 4, 65 €)

Elegida por John el 9-sep (nº 4 de su cola, anunciada en el hub desde mayo). Research (6 lentes + síntesis + refutación 8/16/8),
SPEC de 36 decisiones, verificación legal contra el BOE (72 fichas, 14 correcciones: IAE 644.1 basta, el DB-HS 3 no aplica al
obrador, pan al 4 % desde feb-2025, art. 3 con vías alternativas…), 8 libros de Excel (4.556 fórmulas, refutados y corregidos),
guion con `puntos_por_epigrafe`, 47 bloques redactados por Sonnet, guía de **103 páginas** + bonus de 37 + business plan de 18 (v1.0.1 del 12-sep),
capa de producto completa (48), imágenes, blog (3 banners + 8 enlaces). **En `main` LOCAL, sin push: falta el Payment Link de
John** (datos en `SESSION_HANDOFF_2026-09-10-guia-pasteleria.md` §0). Decisiones de John (02:30): 65 € · 8 libros · dos sesiones
(fundidas en una por su orden de las 02:35) · arreglar HOY el libro 13 del kit de pastelería (ampliado a 01/02/08 con su OK).
Coste ≈ 14 M tokens de subagentes. **Correos:** lanzamiento de la guía **14-oct** (borrador; programar desde el 14-sep) ·
**Kit de Tareas Pastelería 2.1 el 19-oct** (borrador; programar desde el 19-sep). **Próxima sesión = impar**: anisakis
(punto 0) y documentos de la guía gastronómica (handoff B §20); `nombre-gate.py` en 43 fichas antiguas y «9 checklists» en 5
verticales quedan como deuda menor.

### ✅ 2026-09-12 (sesión PAR, Claude Code en el Mac) — Pastelería **1.0.1 LIVE y verificada** + «Cómo Montar una Chocolatería Boutique & Atelier» (producto nuevo nº 5): research CERRADO, John DELEGÓ («decide tú, adelante!»), D1-D53 firmadas, **fase A2+B1 HECHA** (verificación legal 109 CHN · JSON común 635 · SPEC LISTA tras 5 rondas · datos_ejemplo · 9 xlsx con gate 9/9 · guion en curso al cerrar). Sesión partida por un corte de cuota (15:08) y un kernel panic (16:02); restaurada a las 16:05. Queda la sesión B2+C (redactores → documentos → refutación → capa de producto → Payment Link → LIVE → Resend 24-oct), **a hacer en el VPS por decisión de John** (los productos futuros también)

El fixer del 10-sep estaba al 95 % (no «a mitad»): verificación adversarial (3 lentes + regresiones + 2º voto, opus, 1,55 M) → 7 residuos
arreglados a mano → v1.0.1 en `0ba5158`, gate post-pago LIVE 13/13. Research de Chocolatería con el mismo workflow de 6 lentes + síntesis +
refutación (2,35 M): «CORREGIR ANTES» 8/14/6; propuesta 65 €, slug `guia-chocolateria-obrador`, 20 caps + anexo, 9 xlsx, 2 bonus, alcance
bombonería con obrador (taza/churros como epígrafe, bean-to-bar como variante), presupuesto ≈14,7-14,9 M → DOS sesiones. Decisiones D1-D18 en
`SESSION_HANDOFF_2026-09-12-chocolateria.md` §2.4. **Correo:** slot **24-oct** (programable desde el 24-sep). Hallazgo colateral a corregir con
el 49: seis FAQ de `use-cases-content.*.consultor.ts` (7 idiomas) publican inversiones inventadas, dos contra guías en venta.

### ✅ 2026-09-18→19 (sesión IMPAR de infraestructura, Claude Code en el Mac) — cripto en los 48 · Miselup en los 48 · «Próximos Productos» ×23
Réplica de NOWPayments a todos los productos (PR #81; `CRYPTO_PRODUCTS=all`, eBook excluido; el pago real de prueba de
John sigue pendiente) · tarjeta lateral de Miselup en landing + dashboard (PR #82, decidida por `BaseLayout` con el
registro `zona-app`) · hub con 23 tarjetas en «Próximos Productos» (PR #83): Churrería-Chocolatería, Heladería y el
top-20 del banco de 161 ideas (§3 reescrito con la cola, precios y olas; Excel maestro actualizado con backup) ·
renombre a «Cómo Montar una Chocolatería Boutique & Atelier». Reglas nuevas de John: todo producto nace con Stripe +
NOWPayments; volumen 0 no descalifica un producto. Handoff: `SESSION_HANDOFF_2026-09-18-cripto-replica-48.md`.
**Siguiente sesión PAR:** Chocolatería B2+C (local) y después «Tareas Recurrentes: Taquería Mexicana» (VPS); antes,
programar el broadcast de Pastelería (14-oct) y decidir la política del Mega Pack.

### 🔄 2026-09-19 (sesión PAR, Claude Code en el Mac) — correos de Pastelería PROGRAMADOS · Chocolatería B2+C EN CURSO

- **Resend, dos huecos cerrados por `GET /broadcasts` (el último programado era Food Truck 2.2 el 9-oct):**
  lanzamiento **«Cómo Montar una Pastelería» → 14-oct 08:00 UTC** (`476bf7fa-8cf1-441d-a49a-ce70c4fb080b`) y
  **Kit de Tareas Pastelería 2.1 → 19-oct 08:00 UTC** (`ec87d4a8-5ea6-4fec-a9d1-eb48d64c6c13`); prueba de cada uno
  enviada a John antes de programar. **El siguiente hueco es el 24-oct** (Chocolatería; 29-oct si John aprueba el
  kit de chocolatería 2.1 —D53—, que iría delante). Programable desde el 24-sep.
- **DataForSEO con saldo otra vez** (John, 19-sep): «taquería mexicana» 210/mes ES; sirve para el research de la Taquería.
- ✅ **Chocolatería Boutique & Atelier LIVE a las 16:20 (PR #84 → `7a1a101`; Payment Link de John a las 16:00; gates LIVE 49/711/0, Miselup 98/98, robots OK; sitemap reenviado a GSC). Pendiente: broadcast 24-oct (programar desde el 24-sep; 29-oct si John aprueba D53), compra de prueba de John, pedir indexación en GSC.** Antes de eso, fase B2+C HECHA en LOCAL (15:45): capa de producto 49 + 45 bloques + refutación en 2 rondas + documentos finales (guía 111 págs · BP 19 · bonus 34) en `dl/`, gates offline en verde, PR #84 en borrador con deploy preview. Falta SOLO el Payment Link de John (datos entregados) → `sync-payment-links.py` → merge → gates LIVE → Resend 24-oct (o 29-oct si aprueba D53).** Detalle: `SESSION_HANDOFF_2026-09-19-chocolateria-b2c.md`. Arrancó así: 45 redactores Sonnet por bloque (workflow
  `escribir-bloques-guia-chocolateria`) + capa de producto (workflow `capa-producto-guia-chocolateria`: 3 lotes opus
  con ficheros disjuntos, `fase8x-sustituir-banner.py` genérico, 7 imágenes, revisor + fixer) en la rama
  `feat/guia-chocolateria-obrador`. Desviación de la SPEC ya decidida: `comingSoon` pasa de 23 a 22 (se quita sólo
  su tarjeta), no a cero.

### 🔄 2026-09-20 (sesión PAR, Claude Code en el Mac) — POLÍTICA DE 3 FASES + «Tareas Recurrentes: Taquería Mexicana» F1+F2+F3 en un día
Política escrita en §3 (decisiones delegadas por John). Taquería (producto 50, **14 €**, S): F1 cerrada `d6076de` (research 601 líneas, SPEC
862 refutada en ronda única + `gate_f1_spec.py`), F2 cerrada `96c6b88` (11 xlsx, 298 tareas, generador == post-motor, `gate_f2_contenido.py`),
F3 mergeada (**PR #85 → `4f214a0`, LIVE 15:38 UTC**), gates LIVE 50/722/0 y Miselup 100/100 → correo el 29-oct
(programar el 29-sep, tras el de la Chocolatería del 24-oct). Consumo total 2,39 M / 2,5 M. Hub reordenado y LIVE en `8b3fe17`
(novedades primero, Mega Pack último). Handoff: `SESSION_HANDOFF_2026-09-20-taqueria-3-fases.md`.

### ✅ 2026-09-24 (sesión Claude Code en el Mac) — Kit de Escandallos Pro **v2.1 LIVE** (PR #98 → `dd3c128`) + piloto EN en F2
- Nuevas plantillas **12 Test de Rendimiento** y **13 Lista de Precios**, en ES y EN a la vez (decisión de John del 24-sep). El EN (Recipe Costing Kit Pro) se duplica desde esta v2.1.
- Detalle: `kit-escandallos-v2_1/INFORME-construccion.md` y `recipe-costing-kit/SPEC.md`.
- **Correo ES:** `broadcast-kit-escandallos-v2.1-es.html`, prueba enviada a John el 24-sep; **hueco 3-nov 08:00Z**, programable desde el 4-oct.
- ⚠️ La cola previa sigue pendiente de programar: Chocolatería 24-oct (programable desde hoy; su HTML no está en `emails/`) y Taquería 29-oct (desde el 29-sep).
- Consumo: F1 del piloto EN 2,8 M; ES v2.1 1,7 M (casilla «v2.x ES»).

### ✅ 2026-09-25 (sesión Claude Code en el Mac) — correo EN del Food Cost Kit Pro PROGRAMADO
- **Segmento EN, lunes 28-sep 14:00 UTC** (`4f449fb2-…`): presentación de la tienda EN + primer producto en un solo correo.
- La cola EN es **independiente** de la ES (otro segmento): hueco = último envío al segmento EN + 5 días, sin coincidir con un
  correo de producto ES el mismo día. Detalle: handoff `SESSION_HANDOFF_2026-09-25-food-cost-kit-en.md` (bloque de la tarde).
- **D53 DECIDIDA (John delegó: «decide tú», 25-sep): SÍ al Kit de Tareas Chocolatería 2.1**, con el orden cambiado respecto a la
  SPEC. Motivo: el kit es un producto VENDIDO cuyas tres celdas de declaración funden cacahuetes, frutos de cáscara y sésamo
  en «frutos secos» y omiten los sulfitos (entradas 5, 8, 11 y 12 del Anexo II): es un error de etiquetado de alérgenos, no
  de estilo, y arreglarlo cuesta ≈0,15 M. Alcance exacto en `guia-chocolateria-SPEC.md` §D53 (b) + acotación: solo las tres
  celdas y la humedad 50-60 %; las otras 7 celdas con «frutos secos» NO se tocan.
  - **Correo de la guía: 24-oct 08:00Z, PROGRAMADO** (`ff01873f-2746-4345-b8b4-bfc4685e2800`, prueba a John `01a0d89e-…`). La guía va
    delante del kit (y no detrás, como decía la SPEC): lleva desde el 19-sep sin correo, es la venta grande (65 € frente a 12 €)
    y su nota-puente del cap. 12 vale con el kit 2.0 y con el 2.1.
  - 🔴 **Plazo: el kit 2.1 tiene que estar LIVE antes del 24-oct**, porque el correo de la guía recomienda el kit («lo que vas a
    usar cada mañana»). Se hace en la próxima sesión «v2.x ES» (S, Mac en serie con vigilante), por su generador y con los gates
    de §8.2 de la SPEC (grep de las 3 celdas, censo, descargas LIVE).
  - Correo del kit 2.1: siguiente hueco libre tras Escandallos 2.1 (3-nov) → **8-nov**, programable desde el 9-oct.
  - Guía v1.1: retirar la nota-puente del cap. 12 cuando el kit 2.1 esté LIVE (SPEC §D53 c).
- **Tienda EN, producto 2: Restaurant Inventory Kit Pro ($19, S) — F1 cerrada** (0,37 M de 2,5 M). F2 en la próxima sesión EN.
  Deuda ES que destapó (D23 de su SPEC): el Kit de Inventario ES muestra «RT-08:» en `BONUS-09!Parámetros!C12`, dice «8
  plantillas» donde son 7 y sus estados FIFO/validez usan `TODAY()` contra fechas fijas de agosto → corregir en su próxima v2.x.
- Cola ES: Chocolatería 24-oct ✅ programado · Taquería 29-oct (desde el 29-sep) · Escandallos 2.1 3-nov (desde el 4-oct) · Kit Chocolatería 2.1 8-nov (desde el 9-oct, si está LIVE).

### 🔄 2026-10-03 (sesión PAR, Claude Code en el Mac) — «Cómo Montar una Churrería-Chocolatería» F1 EN CURSO + correo de la Taquería PROGRAMADO
- **Correo de la Taquería programado** (llevaba en ventana desde el 29-sep sin programar): **29-oct 08:00 UTC**,
  `2e4b4d68-30e7-4962-b9d6-6376ca20e4e3`, segmento ES, guardas y enlaces en verde. Cola ES leída por `GET /broadcasts`: Panadería 2.2 4-oct ·
  Food Truck 2.2 9-oct · Pastelería 14-oct · Kit Pastelería 2.1 19-oct · Chocolatería 24-oct · **Taquería 29-oct** · Escandallos 2.1 **3-nov
  (programable desde el 4-oct 08:00Z)** · Kit Chocolatería 2.1 8-nov (desde el 9-oct, y solo si está LIVE) → hueco siguiente **13-nov**.
- **Siguiente producto nuevo (decisión delegada): «Cómo Montar una Churrería-Chocolatería»** (L, 65 € orientativo, producto 51). Primero de la
  cola de construcción del §3, anunciado «Q4 2026» en el hub, temporada alta de churros, y la hermana (Chocolatería Boutique, D1) ya la separó como
  «otro negocio»: reutiliza sus 109 CHN y 115 CHS verificados, sus 9 generadores y su guion. F1 en el Mac (solo API) con 5 lentes de research,
  2 a la vez por la térmica (workflow `research-guia-churreria`, run `wf_ca9bdc63-a48`).
- ✅ **Kit de Tareas Chocolatería 2.1 LIVE el mismo 3-oct** (PR #104 → `1eb58b26`; plazo del 24-oct cumplido): los ocho alérgenos del Anexo II
  en las tres celdas de declaración (01!Apertura B26 · 04!Dependiente B7 · 06!Pascua B17) y la humedad del obrador en 50-60 % (02!Templado,
  02!Instrucciones, BONUS-01!Briefing); versión 2.1 solo en esos 5 ficheros. Por su generador: el motor de familia gana versión por fichero
  (`VERSIONES` / `version_de`), regresión 0 en cafetería, hotel y heladería. Gates: censo 0, no latinos 0, post-pago LIVE 11/0/0. Coste 0,44 M.
  **Correo: HTML `emails/broadcast-kit-tareas-chocolateria-v2.1-es.html`, prueba a John `01a0ffd4-…`; programarlo el 9-oct o después** con
  `resend-broadcast.py --html … --subject "Kit de Tareas Chocolatería 2.1: los ocho alérgenos, uno a uno" --name "Actualización Kit de Tareas
  Chocolatería 2.1 (ES)" --scheduled-at 2026-11-08T08:00:00Z` (Escandallos 2.1 va antes: 3-nov, programable desde el 4-oct).
  Deuda que destapó: el changelog del Mega Pack (`get-download-urls.ts:1403`) sigue en 1.1 del 22-ago y nunca recoge las versiones de sus kits.
- VPS: `/dev/null` sigue siendo un fichero normal (`regular file 644`, comprobado hoy) → la galería de capturas sigue bloqueada (arreglo de John).
- ✅ **Churrería-Chocolatería, F1 CERRADA** (`c4449f1d`, `d419934d`, `079eca66`): research 2,11 M · fichas + SPEC + refutación 1,66 M ·
  `datos_ejemplo.py` «El Molinete» 0,86 M = **4,63 M** (la SPEC lo estimaba en 3,26). Proyección con la F2 tal cual: **14,06 M → por
  encima de la parada de 13 M → F2 PARADA hasta que John elija** entre A (≈ 13,2 M), **B (≈ 12,8 M, recomendada: 7 libros, 16 caps +
  anexo)** y C (aplazar). Handoff: `SESSION_HANDOFF_2026-10-03-churreria-f1.md`.
- John (3-oct): **VPS aparcado** hasta que él lo actualice entero y avise; la galería de capturas, en pausa con él.
- ✅ **Churrería-Chocolatería LIVE (3-oct, tarde, PR #105)** — Stripe `7sY14gdkMeAK3UXejH6oo1A` + NOWPayments verificados en
  producción. **Correo de lanzamiento: hueco 13-nov 08:00Z, PROGRAMAR a partir del 14-oct** (tope de 30 días de Resend), antes
  `GET /broadcasts` para confirmar que Escandallos 2.1 (3-nov) y Kit Chocolatería 2.1 (8-nov) están programados; si no, el hueco es
  el `scheduled_at` más tardío + 5 días. Plantilla de lanzamiento: `emails/broadcast-manual-manager-lanzamiento-es.html`; prueba a
  John con `--test`. Hermana v1.0.1 (D7): aplazada por John; su correo, 5 días después del de la Churrería.
- John (3-oct, tarde): **VPS reactivado** con reparto Mac ↔ VPS para todos los productos (regla en `CLAUDE.md`).

### ✅ 2026-10-11 (Claude Code en el Mac + VPS) — Plan Paellero **1.2 LIVE** (PR #115): revisión rápida por un cliente real

- **Origen:** un cliente compró el 10-oct a las 22:11 por la **réplica de ChefBusiness** (Payment Link `eVqeV60…`, redirige a
  `chefbusiness.co/…/acceso/`, sin webhook y con el correo sin `await`) y **no recibió nada**. Acceso reenviado el 11-oct a las
  10:12 Madrid desde aichef.pro (`resend-access`, entregado). Pendiente a futuro (John): el hub de CB pasa a ser un catálogo de
  tarjetas que abren la landing de aichef.pro, sin Payment Links propios.
- **Regla nueva de John:** actualizar = **mejoras puntuales** con sonnet/haiku y revisión rápida; la SPEC de familia es catálogo, no
  alcance. Hecho con 2 sonnet en paralelo (xlsx y docx, ejecución en el VPS) en ~1 h: pycel 0 errores, anticipo en €, IFERROR,
  desplegables, «88 proveedores», checklist con OK/contador (**104 hitos**, no 110), contrato (IVA 10 %, cancelación B2C escalonada y
  simétrica, fuero del consumidor), manual técnico (tiempos = suma de fases, alioli), anexo legal autonómico verificado, A4 en los 7 docx.
  Scripts: `scripts/productos-digitales/paellero-v1_2/`.
- **Verificado LIVE** (`45a45121`): los 11 ficheros servidos = repo byte a byte (`cmp`), `gate-flujo-postpago.py --only` 11/11, 0 fallos, landing con «Versión 1.2» y «104 hitos».
- **Manual técnico AMPLIADO el mismo día (PR #116, John: «démosle más calidad»):** de ~1.100 a ~4.400 palabras y de 2 a 10
  tablas (escalado por paellera en rangos evento/menú, fuego gas/leña, caldos, cronograma, seguridad alimentaria, alérgenos
  ×12 paellas, problemas y soluciones, checklist); catálogo con las capacidades de las paelleras alineadas (prometía 25-30 /
  40-60 / 80-150; ahora ≈ 11-15 / 30-40 / 60-80 raciones). Verificado LIVE byte a byte y gate 11/11. Borrador del correo del
  18-nov actualizado (ojo: `PATCH` sin `name` lo deja «Untitled»).
- **La v2.0 completa de línea B (motor `grupo_b.py`, SPEC §3) sigue pendiente** y NO se hizo: break-even sin amortización (10,2
  eventos/año frente a «18-22» de la landing), inversión de la landing (3.500-25.000) frente al xlsx (3.790 / 9.670 / 23.110),
  tasas dentro de fórmulas, «Plantillas validadas con asesor legal» sin respaldo.
- **Cola de correos SANEADA el 11-oct** (John: «decide tú y soluciona eso»; había 4 huecos programables sin programar):
  - Programados hoy: **Escandallos 2.1** 3-nov 08:00Z `bd4839ce` · **Kit Chocolatería 2.1** 8-nov 08:00Z `f53775c5` (ES) ·
    **Coffee Shop** 4-nov 14:00Z `c6f59951` · **Restaurant** 9-nov 14:00Z `8789caca` (EN).
  - Más allá del tope de 30 días de Resend → **BORRADORES** + routine en la nube **`trig_01WdpgX2KtUL9PbTyXHC4dVg`** (19-oct 08:23Z,
    conector Resend, probado en lectura con `trig_013WPxwByVLs8GG76vN2djSD`) que los programa: **Churrería** 13-nov 08:00Z `395a7eb1`
    (`emails/broadcast-guia-churreria-lanzamiento-es.html`) · **Bakery EN** 14-nov 14:00Z `68bc8f49` · **Paellero 1.2** 18-nov 08:00Z
    `42ccda21` (`emails/broadcast-plan-negocio-paellero-eventos-v1.2-es.html`). Pruebas de los dos ES enviadas a John.
    Comprobar el resultado: `RemoteTrigger list_runs` del routine o https://claude.ai/code/routines.
  - **Siguiente hueco libre: ES ~~23-nov~~ 28-nov 08:00Z · EN ~~19-nov~~ 24-nov 14:00Z** (el 19-nov lo ocupa el Bar; el 23-nov, el Parrillero 2.2 del 12-oct).

### ✅ 2026-10-11 (Claude Code en el Mac + VPS) — **Bar Business Plan Kit (EN, $39) LIVE** (PR #118, merge `efc7f72b`)

- **Producto 11 de la tienda inglesa** y quinto business plan: duplicado del ES `plan-negocio-tapas-bar` (gemelo estructural de la
  cafetería, así que reutiliza el código de BP FT/CAF con contenido del Restaurant) y adaptado a EE. UU. con notas UK. Entregables:
  plan en Word (10 secciones, ~7.800 palabras), Excel financiero (9 hojas, 742 fórmulas) y checklist de apertura (73 tareas, licencia
  de alcohol como camino crítico). Caso: ventas $923,400 · préstamo $369,000 · DSCR 2,44 · payback 2,5 años · equilibrio 81 cubiertos.
  Código en `scripts/productos-digitales/business-plans-en-3/`; revisión adversarial (1 Opus, 0 bloqueantes, 7 MAYOR + 17 MENOR
  arreglados por la vía de texto) en `REVISION-FINAL.md`. ≈ 2,2 M tokens de subagentes (techo M = 5 M).
- **Stripe:** `plink_1UPLlb4CcdRGidmEYaeOXn3r` = `https://buy.stripe.com/bJe00c3KccsCcrt0sR6oo1J`, $39 USD pago único, impuesto
  automático, redirección a `/en/digital-products/bar-business-plan/access?session_id=…` (verificado con la CLI en live). Env
  `VITE_STRIPE_PAYMENT_LINK_BAR_BUSINESS_PLAN` (builds, all) + `netlify/shared/payment-links.ts` (62 enlaces).
- **Verificado LIVE:** `gate-flujo-postpago.py --only bar-business-plan` 3/3 entregables, 0 fallos, 0 avisos, 3 puertas cripto · gate completo (el PR tocó functions compartidas) **62 productos / 819 entregables / 0 fallos / 0 avisos** ·
  `tienda-gate.py --base https://aichef.pro` verde · `robots-gate.py --live` verde · sitemap + `llms.txt` + `llms-full.txt` con la
  URL · enlazada desde el hub EN, los otros 10 productos EN y el Restaurant Kit (que suelta la keyword «bar business plan») ·
  hreflang recíproco con `plan-negocio-tapas-bar` · sitemap reenviado en GSC.
- **Correo de lanzamiento EN:** borrador `813229ae` (`emails/broadcast-bar-business-plan-lanzamiento-en.html`, prueba enviada a
  John); lo programa para el **19-nov 14:00Z** el routine **`trig_01W3wg4wmuaSrGazNW6mep1u`** (20-oct 15:07Z). Comprobar su `list_runs`.
- **Además hoy (PR #117):** fuera el precio tachado y los «valores» de bonus de toda la tienda EN (FTC 16 CFR 233.1). Los correos EN
  ya programados que dicen «launch/regular price» se quedan así (John: «déjalo así… para no retrasar trabajo»).

### ✅ 2026-10-11 (Claude Code en el Mac + VPS) — **Catering Business Plan Kit (EN, $39) LIVE** (PR #122, merge `2e96d40`)

- John eligió el Catering (880/mes en EE. UU., LOW, subiendo) y el retoque del Bakery para «pastry business plan» (1.900/mes;
  su SERP es de bakery business plans → sin producto nuevo; LIVE en el PR #121).
- **F1 cerrada** en la rama `feat/catering-business-plan-en` (`784b2e0f`): `business-plans-en-4/` con `F1-inventario-delta.md`
  (gemelo = **Food Truck EN**; la línea B del ES no es financiable: margen neto 50 %, break-even de 5,5 eventos/año),
  `F1-research-us-delta.md` y `SPEC-delta.md` (D66-D80). 4 ficheros: plan Word, Excel (motor del FT con eventos/año ×
  $/invitado × invitados/evento), **calculadora de precios** regenerada en EN y checklist de 68 tareas. F1 ≈ 0,59 M tokens.
- **Retomar:** worktrees `scratchpad/wt-cat` (Mac) y `/root/wt-cat` (VPS) en la rama; F2 paso 1 = implementador opus
  según `SPEC-delta.md` §3-§7 y el patrón de `business-plans-en-3/F2-NOTAS.md`. Deuda ES de la línea B (ficha del catering:
  «break-even 14 eventos/mes», «60+ pp.», «10 ejemplos validados»): anotada, no se toca ahora.
- **F2 + F3 cerradas el mismo día** (rama `feat/catering-business-plan-en`, HEAD `261804be`; preview
  `deploy-preview-122--aichefpro.netlify.app`). 4 ficheros en `dl/catering-business-plan/` (docx 6.662 palabras · xlsx 9 hojas
  722 fórmulas · calculadora con autotest · checklist 68 tareas). Caso: 180 eventos × 60 invitados × $60 = $648,000 · préstamo
  $146,000 · DSCR 2.60 · equilibrio 151 eventos · neto 7,5 %. Revisión opus: 0 bloqueantes, 5 MAYOR + 14 MENOR de TEXTO
  aplicados (`e958c641`; ninguna cifra cambió). Gates F2 y regresión FT/CAF/REST/PAN/BAR en verde; contra la preview solo
  fallan los 3 del Payment Link. ≈ 2,6 M tokens en total (techo M = 5 M).
- **Cierre al recibir el link** (como el Bar): CLI de Stripe (USD 39, redirección
  `/en/digital-products/catering-business-plan/access?session_id={CHECKOUT_SESSION_ID}`) → env
  `VITE_STRIPE_PAYMENT_LINK_CATERING_BUSINESS_PLAN` (builds) → `sync-payment-links.py` → PR fuera de draft + merge → gates
  LIVE (`gate-flujo-postpago --only`, completo, `tienda-gate`, `robots-gate --live`, `carrusel-apps-gate`) → GSC → correo EN
  24-nov 14:00Z (borrador + routine el 25-oct; plantilla `broadcast-catering-business-plan-lanzamiento-en.html`) → worktrees fuera.
- **LIVE el 11-oct (17:50 Madrid):** Stripe `plink_1UPOsm4CcdRGidmEPrEMILKX` = `buy.stripe.com/fZuaEQa8AdwGfDF0sR6oo1K` ($39 USD,
  impuesto automático, redirección comprobada con la CLI) + env + mapa de 63 links. Gates LIVE: `--only` 4/4 · completo **63 productos /
  823 entregables / 0 fallos / 0 avisos** · tienda-gate · robots-gate · carrusel 63/63. Sitemap reenviado en GSC. **Tienda EN: 12 productos.**
  Correo EN: **PROGRAMADO el martes 13-oct 14:00Z** (`dc53426b`; John: fuera de la cola, junto con la 2.0 ES); el routine
  `trig_01RQdZrmsAtKFEUCjWykZQyy` queda DESACTIVADO. Siguiente hueco EN: 24-nov 14:00Z (vuelve a estar libre).
- **Correo de la 2.0 ES (John 11-oct): el MARTES 13-oct 08:00Z, fuera de la cola** (el lunes 12 es festivo); programarlo con
  `resend-broadcast.py --scheduled-at 2026-10-13T08:00:00Z` en cuanto la 2.0 esté LIVE. El 14-oct sale la Guía Pastelería.
- ✅ (HECHO el 11-oct, ver entrada «Catering ES 2.2 LIVE») **SIGUIENTE TAREA tras el Catering EN (John, 11-oct: «habrá que solucionar el de español… para que quede conforme a los
  estándares de calidad»): Plan Catering Temático Eventos ES → 2.0.** Reutiliza el motor que sale del EN (molde FT ES con
  eventos/año × €/invitado × invitados/evento, personal fijo + cobertura por evento, calculadora coste → precio con IVA 10 %),
  caso España con cocina comisaria, sueldo del dueño y amortización, docx en las ranuras del FT, checklist 68 tareas desde las
  99 válidas del ES, y la landing/dashboard sin las afirmaciones falsas (L1-L16 de `business-plans-en-4/F1-inventario-delta.md`:
  «60+ pp.» frente a ~2.700 palabras, «break-even 14 eventos/mes», «10 ejemplos validados», «110 hitos» = 108, inversión
  5.500/11.500 en ficha y docx frente a 8.520/21.410/54.440 en el xlsx). Versión 2.0 (cambia el modelo) + correo de
  actualización a la cola ES. Después, proponer a John el mismo motor para el resto de la línea B (paellero, parrillero,
  coctelería, chef privado), uno a uno.

### ✅ 2026-10-11 (Claude Code en el Mac + VPS) — **Plan de Negocio Catering Temático Eventos ES 2.2 LIVE** (PR #123, merge `ea75b3b`)

- Encargo de John: dejar el catering ES «conforme a los estándares de calidad». La 1.x (línea B) no era financiable (margen neto
  50 %, break-even de 5,5 eventos/año sin cocina, sueldo ni amortización) y la landing prometía «60+ pp.», «break-even 14
  eventos/mes», «10 ejemplos validados», «110 hitos» e inversiones que no cuadraban con el xlsx.
- **2.2 sobre el motor ES de línea A** (molde del Food Truck ES v2.2, `planes-v2_0/contenido_plan_catering_tematico_eventos/`;
  carpeta `scripts/productos-digitales/catering-es-2_0/`, con F1, research España con BOE, SPEC, F2-NOTAS y REVISION-FINAL):
  Excel de 9 hojas (130 eventos × 65 invitados × 53 € = 447.850 € · neto 8,8 % · préstamo 111.000 € · equilibrio 55
  invitados/evento ≈ 109 eventos/año · IVA 10 % · cocina central compartida · extras fijos discontinuos), checklist 82 tareas,
  calculadora por invitado regenerada (autotest 168/168), Word reescrito en 10 secciones (7.565 palabras, A4), 34 arreglos de
  texto en los otros 7 ficheros (sin «freelance» ni «validado», contrato con no desistimiento, sin carnet de manipulador, A4).
  Revisión opus: 1 bloqueante (restos del FT) + 6 MAYOR + 15 MENOR, todo aplicado; gate nuevo `gate_restos_ft.py`.
  `compilar_vocabulario` de `grupo_a` con opción opt-in; regresión de los 5 planes de línea A = 0 diferencias.
- Landing, dashboard, changelog (2.2), tarjetas de los hubs ES/DE/FR/IT/NL/PT corregidas; capa comercial intacta salvo la
  frase de Yuki («sushi para amigos y familia», decisión de John). LIVE: 11/11 ficheros = repo byte a byte, gate completo
  63 / 823 / 0, carrusel 63/63, robots verde. ≈ 1,9 M tokens.
- **Correo de la 2.2: PROGRAMADO martes 13-oct 08:00Z** (`2b60e0ca`, fuera de la cola por decisión de John; el 14-oct sale la
  Guía Pastelería). El Catering EN sale ese mismo día a las 14:00Z.
- **Deuda anotada:** (1) las tarjetas de hub de los otros planes de eventos (parrillero, paellero, chef privado) dicen «DOCX 60+
  pp» y «17 CCAA»: verificar al pasarles el motor; (2) la panadería publicada dice «Transacciones/día previstos / necesarios»
  (concordancia); (3) proponer a John el mismo motor para el resto de la línea B, uno a uno.

### ✅ 2026-10-11 (Claude Code en el Mac + VPS) — **Plan de Negocio Paellero para Eventos ES 2.2 LIVE** (PR #124, merge `57a4bc1`)

- John: «dale, arranca con el paellero» (tras el catering). Mismo método: motor ES de línea A sobre el FT ES con el módulo clonado
  del catering (`planes-v2_0/contenido_plan_negocio_paellero_eventos/`, carpeta `scripts/productos-digitales/paellero-2_2/` con F1,
  research delta de gas / fuego / fiestas populares con BOE, SPEC, F2-NOTAS y REVISION-FINAL). Caso: 105 eventos × 94 raciones ×
  16 € de media (bodas 28 · empresas 24 · privadas 18 · populares 5) = 157.920 € · neto 7,8 % · préstamo 51.600 € · DSCR 1,72 ·
  equilibrio 90 eventos/año · holgura de caja 22,4 % (año 2: 13,7 %, explicada con palancas). Checklist 83 tareas, calculadora por
  paelleras (autotest 336/336), docx reescrito 7.990 palabras con anexo autonómico corregido (PATRICOVA era de inundaciones),
  carta re-escandallada, contratos con fuerza mayor (B2C y B2B), no desistimiento y efectivo < 1.000 €; manual técnico de la 1.2
  intacto. Revisión opus: 0 bloqueantes, 6 MAYOR + 16 MENOR aplicados (comida testigo RD 1086/2020 art. 30.8 incluida).
- **El mismo PR corrigió el Catering 2.2 LIVE**: nota del Excel «el Word sigue en la versión 1.1» (texto del motor, falso en las
  2.2), comida testigo que faltaba, comida al 82 % (no el 85,19 % del molde), «pan común» en Tesorería y el email post-compra de
  `verify-purchase.ts` (decía «DOCX 60+ pp… anexo 17 CCAA»). Equilibrio del catering: 108 eventos/año (landing actualizada).
- Testimonios (John): Marc Esteve sin «4.200 EUR / escenario mínimo viable»; Antonio Rivas y Sam Williams «los contratos B2B».
- LIVE: 22/22 ficheros = repo byte a byte; gate completo 63 / 823 / 0 (un fallo pasajero en la 1.ª pasada, 0 al repetir);
  carrusel 63/63; robots verde. ≈ 2,3 M tokens.
- **Correo de la 2.2**: el borrador `42ccda21` lleva ya la 2.2 («Actualización Plan de Negocio Paellero 2.2 (ES)»), mismo hueco
  **18-nov 08:00Z**; el routine `trig_01WdpgX2KtUL9PbTyXHC4dVg` (19-oct) actualizado con el nombre nuevo. Prueba enviada a John.
- **Deuda anotada**: email post-compra y tarjetas de **chef privado**, **parrillero** y **coctelería** con «DOCX 60+ pp» / «17 CCAA»
  (pendientes de su 2.2); la nota «el Word sigue en la 1.1» es cierta en los 5 de línea A mientras su docx siga en 1.1 (T9).

### ✅ 2026-10-12 (Claude Code en el Mac + VPS) — **Plan de Negocio Parrillero-Asador para Eventos ES 2.2 LIVE** (PR #125, merge `ba24758`)

- John: «seguimos con el Plan Parrillero-Asador a la 2.2, con el mismo método que el catering y el paellero». Carpeta
  `scripts/productos-digitales/parrillero-2_2/` (F1-camino, F1-research, SPEC, F2-NOTAS, REVISION-FINAL), módulo
  `planes-v2_0/contenido_plan_negocio_parrillero_asador_eventos/` clonado del paellero. La 1.1 estaba peor que la del paellero:
  P&L con fórmulas desplazadas (margen bruto −4.496 €), 7 docx en Letter, sin tabla de escalado, «retención 7 %/15 %» (falsa:
  RIRPF art. 95.6, el 677.9 es actividad empresarial).
- Caso: 95 eventos × 80 invitados × 25 € (bodas 12×110×42 · empresa 30×70×31 · privados 45×40×25 · fiestas 8×300×10) =
  190.000 € · neto 7,6 % · préstamo 65.400 € · DSCR mín. 1,51 · equilibrio 81 eventos (caja 76) · holguras de caja 25,1 / 12,6 /
  11,9 % (años 2-3 contadas con palancas). Excel de 9 hojas, checklist 83, calculadora con escalado/IVA/cancelación (552/552),
  docx 11 H1 / 8.175 palabras, 126 arreglos de texto en los otros 7 (A4, contrato con fuerza mayor B2C y B2B, manual con
  «8. Escalado por invitados» y temperaturas de la carne, 93 proveedores «Por verificar»). Mes de versión «octubre 2026» con
  `par_version.py`/`main_par.py` (parche en proceso, sin tocar `motor.py`).
- Revisión opus: 0 bloqueantes, 4 MAYOR + 12 MENOR, todos aplicados. **M1: comida testigo en TODOS los eventos** (RD 1086/2020
  art. 30.8.d, verificado en el BOE: «para eventos, cuando esta sea la actividad principal de la empresa»; el «más de 40
  personas» es el 30.8.e). **El checklist del Paellero 2.2 LIVE lo decía como condición doble: corregido en el mismo PR**
  (regenerado; `cifras_caso_es.json` idéntico). El Catering ya estaba bien.
- Landing, dashboard, changelog, hubs ×7, email post-compra (`verify-purchase.ts` + config) y testimonios (solo Federico Aguirre y
  Marcos Pérez; Sandra Vera «freelance» como rol, intacta). LIVE: 11/11 parrillero y 11/11 paellero = repo byte a byte; gate de
  pago 0 fallos en los dos y gate completo LIVE 63 / 823 / 0; carrusel 63/63; Miselup 102/102. ≈ 2,2 M tokens de subagentes.
- **Correo**: borrador `f8257c43` «Actualización Plan de Negocio Parrillero-Asador 2.2 (ES)», hueco **23-nov 08:00Z**; lo programa
  el routine `trig_01WAN2WR9EaRUsi4C2WTqYj9` el **24-oct 08:23Z**. Prueba enviada a John. Siguiente hueco ES: 28-nov.
- **Línea B pendiente**: coctelería y chef privado (mismo método, uno por sesión).

### ▶️ 2026-10-13 (Claude Code en el Mac + VPS) — **Mobile Bar Business Plan Kit (EN, $39)** — F1 CERRADA

- Elegido por demanda US (DataForSEO, 13-oct): mobile bar business 480 · how to start a mobile bar/bartending business
  210+210 · mobile bar business plan 210 (90 → 210) · dry hire mobile bar 390 · mobile bar license 320, todo LOW. Descartados
  hoy: checklists (la SERP de «kitchen cleaning checklist» es de limpieza doméstica) y las guías L (cola en
  `project_english_expansion`). John (13-oct): «al final los traduciremos todos; ahora, los que más tracción tienen».
- **Regla nueva de John (13-oct): jerga profesional US en las 3 capas** (producto, contenido, SEO de la landing). El research
  §9 lleva el glosario (38 términos con fuente) y los términos de la landing con volumen.
- Rama `feat/mobile-bar-business-plan-en` (worktree `scratchpad/wt-mbar`), carpeta `business-plans-en-5/`:
  `F1-inventario-delta.md` (diccionario por celda = EN del CATERING, −37 % de cadenas a redactar), `F1-research-us-delta.md`
  (dry hire, caso 160 × 95 × $14 = $212,800, préstamo ≈ $50K) y `SPEC-delta.md` (D81-D95). F1 ≈ 0,6 M tokens.
- **Retomar F2:** implementador opus según `SPEC-delta.md` §3-§6 y el patrón de `business-plans-en-4/F2-NOTAS.md`.
  Correo EN: 24-nov 14:00Z (borrador + routine el 25-oct).
- **F2 + F3 cerradas el mismo día** (rama `feat/mobile-bar-business-plan-en`, **PR #128 draft**, preview `deploy-preview-128`):
  4 ficheros en `dl/mobile-bar-business-plan/` (docx, financial projections, pricing calculator con shopping list y 10 cócteles en
  oz (ml), checklist de 68 tareas). Caso: 160 × 95 × $14 = $212,800 · préstamo $49,000 (SBA Microloan) · DSCR 2.93 · equilibrio
  134 eventos · pesimista con caja −$2,664. Revisión opus: 1 BLOQUEANTE (cláusula de «agente» sacada de una fuente de FL
  «AI Generated»), 10 MAYOR, 16 MENOR, todos aplicados (`business-plans-en-5/REVISION-FINAL.md`, `F2-NOTAS` §9); ejemplos de la
  calculadora llevados a precio de mercado. 2 imágenes propias (remolque-barra en boda, barra portátil) + og.
  **Cierre al recibir el link** (ficha Stripe dada a John el 13-oct: $39 USD, redirección `/en/digital-products/mobile-bar-business-plan/access?session_id={CHECKOUT_SESSION_ID}`):
  CLI de Stripe → env `VITE_STRIPE_PAYMENT_LINK_MOBILE_BAR_BUSINESS_PLAN` (builds) → `sync-payment-links.py` → PR fuera de draft + merge →
  gates LIVE → GSC → correo EN 24-nov (borrador + routine el 25-oct; plantilla `broadcast-mobile-bar-business-plan-lanzamiento-en.html`).
  Después: añadirle el bonus común «US · UK · Canada · Australia Hospitality Equivalents Guide» (rama `feat/en-equivalents-guide`).
- **LIVE el 13-oct (merge `90f6a351` del #128).** Stripe `plink_1UQ1Ke4CcdRGidmEQZ5Tkw9S` (`buy.stripe.com/cNicMY2G878i4Z17Vj6oo1L`, $39 USD,
  impuesto automático, redirección comprobada con la CLI) + env + mapa de 64 links. Gates LIVE: `--only` 0 fallos · completo **64 productos /
  827 entregables / 0** · tienda · robots · carrusel 64/64. Sitemap reenviado. **Tienda EN: 13 productos.** Correo EN 24-nov 14:00Z: borrador
  `704556eb` + routine `trig_01HXbLtxV9NLEcnZT5tW26hF` (25-oct 15:07Z). **Siguiente hueco EN: 29-nov.** Bonus de equivalencias en los 13 (PR #129).
  Handoff: `SESSION_HANDOFF_2026-10-13-tienda-en.md`.

### ⚠️ Deuda nueva detectada, para meter en la cola

**Del research de la Taquería (20-sep-2026, `kit-tareas-taqueria/01-research-taqueria-mexicana.md`):**
- **Copy vivo que afirma «control horario digital obligatorio en 2026»: 4 apariciones** (`astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:75` y `:105` más los gemelos de la SPA `src/components/guia-panaderia-obrador/ContentGrid.tsx:14` y `src/data/testimonials-guia-panaderia-obrador.ts:58`): el RD no constaba publicado en el BOE a mediados de 2026 (sin verificar el estado a 20-sep). Redacción neutra («en el soporte que exija la normativa vigente») en los 4 sitios; tocar el `.ts` de Astro y su gemelo SPA a la vez.
- **Los xlsx de la familia Kit de Tareas van SIN TILDES** («Camara», «Hora Limite», «PREPARACION»; verificado en sushi-bar y asador vía `sharedStrings.xml`). Ningún gate lo mide. El kit nuevo se escribe con tildes (D6); homologar la familia es una tanda aparte.
- **La cifra derogada «65 °C» sigue viva en 24 celdas de 12 productos LIVE** (medido en la SPEC de la Taquería §7): entre ellos `pack-appcc` (5 celdas, y su fichero 12 dice «recuperar a ≥ 75 °C»), el kit base `kit-tareas` y `guia-restaurante-mexicano/checklist-appcc.xlsx`. El RD 1021/2022 (BOE-A-2022-21681, art. 30.2, verificado literal) fija ≥ 63 °C en caliente y 74 °C/15 s de recalentado. **No es un fallo de seguridad** (65 y 75 son más estrictos que la ley): es una cita derogada que resta credibilidad al producto que vende APPCC. Tanda de sesión IMPAR: sustituir con criterio (solo mantenimiento en caliente / recalentado) y regenerar `inject_cache`.
- **Ningún kit está en las cestas de los casos de uso** (`src/data/use-cases-content.es.ts`, p. ej. `restaurante-mexicano` en la línea 3580): ventas cruzadas perdidas.


0. 🔴 **Seguridad alimentaria en producto VENDIDO (cazado por el research del Manual del Chef Ejecutivo, 6-sep; John: «déjalo
   anotado para la siguiente sesión»)**: `kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx` y
   `kit-tareas-marisqueria/03-trazabilidad-appcc-marisco.xlsx` dicen «congelación anisakis −20 °C durante 7 días» citando el
   **RD 1420/2006, derogado**; lo vigente es **−20 °C ≥ 24 h o −35 °C ≥ 15 h** (RD 1021/2022 art. 8.1). Y
   `kit-inventario/04-recepcion-mercancias.xlsx` cita el **RD 3484/2000 (derogado)** como fuente de los umbrales por fila.
   Corregir con el MOTOR de cada familia (no a mano sobre el xlsx) + `inject_cache.py` + censo + changelog. **Primera tarea
   de la próxima sesión impar.**

1. ~~El error del 21 % de IVA está VIVO en la familia de PLANES y afecta a los 10 planes~~ **RESUELTO el 2026-09-05**
   (y la deuda estaba sobredimensionada: medido con openpyxl sobre `dl/`, solo `plan-negocio-bar-restaurante` llevaba el
   molde v2.0 con el 21 %; los 9 hermanos son v1.1 sin ese parámetro). Lo que queda: los 4 hermanos de línea A con
   contenido construido (cafetería, tapas-bar, panadería, food-truck) heredan el 10 % al aplicarse con el motor 2.1;
   **decidir antes de aplicarlos si nacen como 2.1 o se les estampa primero la 2.0** (su changelog tendría que contar el
   salto 1.1 → 2.1 entero). Seguimientos de la refutación, ninguno bloquea: fila de aire antes de «UMBRALES» en Supuestos
   (mover el bloque son 5 celdas publicadas) · gate ortográfico que no lee literales dentro de fórmulas · nota de inversión
   del sujeto pasivo para plataformas extranjeras (TheFork, delivery) · docx v1 del bar (40 cubiertos / 22 €) contradice al
   xlsx: T9 pendiente · parámetro propio para la bebida no alcohólica de compra (hoy aproximada al 10 %, declarado en B62).
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
- Planes línea B: coctelería (representante B: `grupo_b.py` + contenido; SPEC §3), parrillero, paellero, catering, chef-privado-showcooking. (Paellero: revisión rápida **1.2** LIVE el 11-oct; su v2.0 de motor sigue pendiente.)
- Planes docx (10): regeneración con bridge.py (SPEC planes §4) — se hace con el producto de su semana.
- Guías: nikkei, panadería-obrador, dark-kitchen (+ documentos de los 7 hermanos: el pipeline `documentos.py` es de familia).
- Kits CB: asador, marisquería, panadería, food-truck, tapas-bar, chef-privado (canario), mega-pack (decisión de John si se amplía).
- eBook Pro Prompts: revisión de texto (sonnet, 1 sesión corta).
- Homologación AICP↔CB (otra terminal, chefbusiness-astro).

## 1-bis. Cola de correos EN (segmento EN, 14:00Z) — 4-oct

10-oct eBook (`b2c99916`) · 15-oct HACCP (`9b7f8f57`) · 20-oct Staff (`7b520469`) · 25-oct Financial (`3d49a8d7`) · 30-oct
Food Truck Business Plan (`f52308c0`) · **4-nov Coffee Shop (programar desde el 5-oct) · 9-nov Restaurant (desde el 10-oct) ·
14-nov Bakery (desde el 15-oct)**. Siguiente hueco EN: 19-nov. → **11-oct: Coffee Shop y Restaurant PROGRAMADOS; Bakery en borrador, lo programa el routine del 19-oct; el 19-nov es del Bar (routine del 20-oct); siguiente EN 24-nov (ver entradas 11-oct).**

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

## 3. Micro-proyecto «productos nuevos» — COLA ANUNCIADA en el hub el 19-sep-2026 (John)

De la cola original de la Hoja 4 (5 productos) **4 ya están LIVE** (Food Cost 4-sep, Manual Manager 5-sep, Manual Chef
Ejecutivo 6-sep, Pastelería 12-sep) y queda la **Chocolatería** (A2+B1 hecha; falta B2+C en local). El 19-sep John
ordenó publicar en «Próximos Productos» del hub la Churrería-Chocolatería, el Plan de Negocio Heladería y **las 20
mejores ideas del banco de 161** (Hoja 6 del catálogo maestro), elegidas por un panel de 3 jueces opus (demanda ·
reutilización de motores · negocio y catálogo) + 2 refutadores contra los 48 LIVE. Criterio de John: **volumen de
búsqueda 0 no descalifica** (se descubre en el catálogo y posiciona sin competencia); el veto es canibalizar lo LIVE.
El Excel maestro (`/Users/johnguerrero/productos-digitales/…RoadmapExpansion.xlsx`, Hojas 4, 6 y 7) quedó actualizado
ese día; copia previa en `…BACKUP-2026-09-19.xlsx`.

**Orden de construcción = orden de esta tabla** (sesiones pares; ~1 producto/semana). Las fechas de las tarjetas solo
van en las dos primeras olas; el resto sale como «Próximamente» a propósito (la Chocolatería llegó a decir «Junio 2026»
tres meses tarde). Precios orientativos, coherentes con su familia LIVE.

| Producto (nombre de la tarjeta) | Familia | Precio | Ola |
|---|---|---|---|
| Cómo Montar una Chocolatería Boutique & Atelier | Guías Cómo Montar | 65 € | Octubre 2026 |
| Cómo Montar una Churrería-Chocolatería — ✅ F1 · ✅ 8 Excel · ✅ guion · ✅ capa técnica (rama) · ⏸️ **PARADA por John el 3-oct a las 11:20** (proceso desproporcionado: ≈ 10,5 M); falta redacción + landing + PR en modo mínimo (≈ 2 M) | Guías Cómo Montar | 65 € | Q4 2026 |
| Plan de Negocio: Heladería Artesanal | Planes de negocio | 35 € | Q4 2026 |
| ~~Tareas Recurrentes: Taquería Mexicana~~ **✅ LIVE 20-sep-2026** (producto 50, 14 €, PR #85 → `4f214a0`; correo el 29-oct) | Kits de tareas | 14 € | — |
| Kit Cuadro de Mando Operativo | Kits de gestión | 19 € | Q4 2026 |
| Plan de Negocio: Hamburguesería Smash | Planes de negocio | 35 € | Q4 2026 |
| ~~Plan de Negocio: Finca de Eventos y Bodas~~ **✅ LIVE 25-oct-2026** (producto 53, PR #164 → `769a0e26`) | Planes de negocio | 45 € | — |
| Tareas Recurrentes: Pollería y Pollo a la Brasa | Kits de tareas | 12 € | Q1 2027 |
| Tareas Recurrentes: Arepería | Kits de tareas | 12 € | Q1 2027 |
| ~~Plan de Negocio: Pizzería Napolitana~~ **✅ LIVE 25-oct-2026** (producto 54, PR #165 → `2e7a3af5`; gemelo EN Pizza Shop Business Plan Kit $39, PR #166 → `64ace831`) | Planes de negocio | 35 € | — |
| Plan de Negocio: Steakhouse / Restaurante de Carnes | Planes de negocio | 35 € | Q1 2027 |
| Calculadora de Comisiones de Delivery | Kits de gestión | 9 € | Q1 2027 |
| Tareas Recurrentes: Poke Bowl / Healthy Bowl | Kits de tareas | 12 € | Próximamente |
| Tareas Recurrentes: Restaurante Vegetariano / Plant-Based | Kits de tareas | 12 € | Próximamente |
| Plan de Negocio: Cortador de Jamón para Eventos | Planes de negocio | 45 € | Próximamente |
| Plan de Negocio: Cafetería Móvil para Eventos | Planes de negocio | 45 € | Próximamente |
| Plan de Negocio: Pizzero Móvil con Horno de Leña | Planes de negocio | 45 € | Próximamente |
| Kit de Análisis de Reseñas con IA | Kits de gestión | 19 € | Próximamente |
| Manual del Empleado de Hostelería | Manuales | 55 € | Próximamente |
| Plan de Negocio: Pastelería y Obrador | Planes de negocio | 35 € | Próximamente |
| Cocina al Vacío Profesional eBook | eBooks | 24 € | Próximamente |
| Cómo Montar una Marisquería | Guías Cómo Montar | 65 € | Próximamente |
| Cómo Montar una Carnicería Boutique | Guías Cómo Montar | 65 € | Próximamente |

Notas de la refutación que condicionan el guion de cada uno: el **Cuadro de Mando** es OPERATIVO (ventas por franja,
ticket, rotación, productividad), no financiero — los ratios financieros ya los vende el Kit Plan Financiero ·
**Reseñas con IA** = plantilla + prompts de usuario final, exportación/copia manual (nada de raspar Google) ·
**Manual del Empleado**: modelos ORIENTATIVOS adaptables al convenio provincial, con descargo legal; nunca «listos
para firmar» · **Comisiones de Delivery**: tarifas en hoja de parámetros editable y fechada · **Carnicería boutique**
(retail, no hostelería): research normativo ANTES de comprometer el guion; si no reutiliza el APPCC hostelero,
sustituir por la Quesería boutique · **Marisquería**: esfuerzo L (vivero, lonja, depuración, moluscos vivos) ·
**Cafetería móvil / Pizzero móvil / Cortador de jamón**: línea B a 45 €, siempre «para eventos» (no calle) para no
pisar el Plan Food Truck · **Taquería / Pollería / Arepería / Poke / Plant-based**: réplicas de 1 sesión con el
motor de Kit de Tareas; antes de la primera, decidir si el **Mega Pack (89 €, «13 kits») pasa a incluir los nuevos**
(hoy ya hay 19 kits LIVE fuera de esa cifra) · Suplentes por si cae alguno: Sushi pop-up para eventos (#147), Mesa
dulce para bodas (#151), Quesería boutique (#99).

**POLÍTICA DE 3 FASES + PRESUPUESTO PROPORCIONAL AL PRECIO (John, 20-sep-2026; decisión delegada a Claude).**
Sustituye al «método en 3 semanas» del 29-ago, que nunca se cumplió: los 5 productos nuevos (Food Cost 3-4 sep, Manual
Manager 4-5 sep, Chef Ejecutivo 6-sep, Pastelería «noche entera» 10-sep, Chocolatería 12+19 sep con corte de cuota y
kernel panic) se hicieron en maratones de 9-14 h. Lo que faltaba no eran fases sino **un corte duro con entregable
cerrado, commiteado y pusheado al final de cada una**. Objetivo declarado por John: producto de calidad, validado, 100 %
funcional y útil, **sin volverse loco con el gasto: el desarrollo se dimensiona al precio que cobramos**.

| Fase | Produce | Gate de salida (DoD) | Decisión de John | Máquina |
|---|---|---|---|---|
| **F1 Fundamentos** | research con cifras etiquetadas [medido]/[fuente]/[estimado] (DataForSEO ES **y** el país objetivo, GSC, canibalización contra lo LIVE), SPEC con decisiones firmadas, guion, datos de ejemplo, tarjeta con precio en «Próximos Productos» | SPEC refutada, **tope 2 rondas**; guion verde; tildes del fichero de datos medidas contra un hermano | nombre, precio, alcance (delegadas el 20-sep) | Mac (solo API) |
| **F2 Entregables** | xlsx con los motores de familia, documentos por redactores Sonnet, carpeta `public/dl/<pid>/` | `censo-entregables --fail` 0 · `gate-no-latinos` · gate de fechas · dry-run del motor de familia (idempotencia 0 diferencias; **`postprocess-transversal` NO se corre sobre kits v2.0: los degrada a v1.1**) · refutación ≤ 2 rondas con lector de regresiones | ninguna | **L/M → VPS** · **S → Mac en serie con vigilante** (11 xlsx openpyxl no calientan; el ping-pong git con el VPS cuesta más de lo que ahorra) |
| **F3 Producto y lanzamiento** | catálogo, `payment-links`, `product-prices` (`sync-product-prices.py`), functions, `zona-app.ts`, landing con las **3 puertas cripto**, imágenes, FAQ, hub (quitar de `comingSoon` y **entrar en la posición 1** en los DOS ficheros gemelos; «✨ Nuevo» solo los 5 más recientes; Mega Pack siempre el último), PR con preview, Payment Link, merge, gates LIVE, broadcast en la cola de Resend | `gate-flujo-postpago.py` LIVE en verde · `miselup-gate` · `whatsapp-gate` · `robots-gate` · sitemap reenviado | **Payment Link de Stripe** (única no delegable) | Mac o VPS (el build lo hace Netlify) |

**Cada fase cierra con `commit + push`** (firma `Via: Claude Code`) y una línea en el handoff con el comando exacto para
retomar. Si llega el corte de cuota o un panic se pierde media fase, no un producto; y cambiar de máquina entre fases
deja de ser un riesgo (el miedo del 12-sep).

**El TAMAÑO decide las sesiones, no la política:**

| Tamaño | Familias | Sesiones | Techo de tokens de subagentes (producto entero) |
|---|---|---|---|
| **S** | kits de tareas réplica (12-14 €), calculadoras (9 €) | **1 sesión, 3 cortes** | **≤ 2,5 M** |
| **M** | planes de negocio (35-45 €), kits de gestión (19 €), eBooks (24 €) | 2 sesiones (F1+F2 · F3) | **≤ 5 M** |
| **L** | guías «Cómo Montar» y manuales (55-65 €) | 3 sesiones (F1 · F2 · F3), reparto 2 + 6 + 2 M | **≤ 10 M** |

Calibración: la Chocolatería (65 €) costó ≈ 16 M solo en F2+F3 (redactores 7,3 · capa de producto 1,6 · refutación r1
2,3 · r2 2,9 · fixer final) más la F1 de 5 rondas de SPEC. El techo L es la mitad. **Si un producto supera su techo un
30 %, se para y se reporta; no se empuja.** Cómo se llega al techo sin bajar calidad:
- **Tope de 2 rondas** de refutación por artefacto; la ronda 2 = verificadores por lente + lector de regresiones; la 3.ª
  comprobación es un gate de script. En S y M, las 3 lentes (cifras · legal · editorial) van **en un solo prompt Opus**.
- **Capa de producto en S/M**: 1 Sonnet calca los ficheros del hermano más reciente (`kit-tareas-sushi-bar` para kits)
  + gates de script; nada de «3 lotes Opus + revisor + fixer», que es formato L.
- **Redactores siempre Sonnet** (Haiku para erratas); Opus solo para SPEC, refutación y decisiones con criterio; Fable
  orquesta y verifica lo crítico (precios, payment links, functions de entrega, seguridad).
- **Los gates de script van ANTES que los agentes** y no se re-verifica a mano lo que un gate mide.
- **Reutilizar motores** (Kit de Tareas 2.4, planes 2.2, guías 2.0): un producto nuevo de familia existente no rediseña
  nada; escribe contenido y calca la capa de producto.

**Mega Pack (decisión del 20-sep):** queda **congelado en los 13 kits fundacionales** que entrega hoy la function (155
ficheros, verificado en `netlify/functions/get-download-urls.ts`): kit-tareas, bar, cafetería, catering, chef privado,
chocolatería, dark kitchen, hamburguesería, heladería, hotel, pastelería, pizzería, restaurante creativo. Los 6 de nicho
ya LIVE (asador, food truck, marisquería, panadería, sushi bar, tapas bar) y **todos los nuevos** (Taquería, Pollería,
Arepería, Poke, Plant-based…) **se venden aparte**. Motivo: cada kit añadido al pack es tocar function + dashboard +
landing + re-verificar sin ingreso nuevo (el pack ya está vendido a 89 €), y canibaliza la venta individual del nicho.
La landing del pack es exacta («12 kits a 12 € + hotel + chef privado = 13») y no se toca en F3.


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
- **Pasarela cripto (NOWPayments)**: piloto + rediseño UX (6-sep) y **réplica a los 48 productos el 18/19-sep (PR #81)** con `CRYPTO_PRODUCTS=all` y `CRYPTO_PRODUCTS_EXCLUDE=pro-prompts-ebook`; handoff `SESSION_HANDOFF_2026-09-18-cripto-replica-48.md`. **El pago real de prueba sigue pendiente de John** (12 €, USDT-TRC20): sin él, la entrega con IPN real no está verificada. Pendientes de John: sección legal de compra digital en `/terminos`, botón «Continuar al pago» deshabilitado o no, moneda de liquidación, copy del hub.

- **13-oct (sesión Claude Code) — Guía de Equivalencias ES ↔ Hispanoamérica en los 51 productos ES (PR #130).** Correo
  `emails/broadcast-guia-equivalencias-es.html` el **jueves 16-oct 08:00Z** (10:00 Madrid), fuera de la cola de 5 días
  por decisión de John («Jueves 16-oct»), entre la Guía Pastelería (14-oct) y el Kit Pastelería 2.1 (19-oct). ✅ **PROGRAMADO** el 13-oct (`70415899-ca9a-4f6d-a109-91637c607c01`, prueba a John enviada). La cola
  de producto ES no se mueve: siguiente hueco **28-nov 08:00Z**. **Revisión anual de las fichas de país: enero 2027.**

### ▶️ 2026-10-15 (Claude Code en el Mac + VPS) — **Food Cost + Menu Engineering Guide (EN, $59)** — LIVE
- Primera GUÍA de la tienda EN, duplicada de la Guía Food Cost ES (55 €). Elegida en vez de «how to open a restaurant» porque
  la guía Casual ES es v1 (2.917 palabras, PDF de relleno). Método y trazabilidad en `scripts/productos-digitales/guia-food-cost-en/`.
- **LIVE el 15-oct (merge `71eb5f16` del #131).** Stripe `plink_1UQo1e4CcdRGidmEGfzJgiN8` (`buy.stripe.com/8x26oA3Kc78ibnpa3r6oo1N`,
  **$59 USD**, impuesto automático, redirección comprobada con la CLI; el primer link salió en EUR y quedó desactivado) + env
  `VITE_STRIPE_PAYMENT_LINK_FOOD_COST_MENU_ENGINEERING_GUIDE` + mapa de 65 links. Gates LIVE: `--only` 0 fallos · completo
  **65 productos / 904 entregables / 0** · tienda · robots · ES byte a byte 28/29 (preview). Sitemap reenviado. **Tienda EN: 14 productos.**
- Correo EN **29-nov 14:00Z**: borrador `9848e616-82b2-4530-af65-70593ecc63fd` («Lanzamiento Food Cost + Menu Engineering Guide (EN) — 29-nov»,
  prueba a John enviada) + routine `trig_01KYPEeGdcVJbsnb8qCXbFrV` (30-oct 15:07Z). Plantilla
  `broadcast-food-cost-menu-engineering-guide-lanzamiento-en.html`. **Siguiente hueco EN: 4-dic 14:00Z.**

### ▶️ 2026-10-16/17 (Claude Code en el Mac + VPS) — **How to Open a Pastry Shop (EN, $69)** — LIVE
- Producto 15 de la tienda EN, duplicado de la Guía Pastelería ES (65 €). Elegido por demanda US (DataForSEO, 16-oct: «how to
  open a bakery» 720 + «how to start a bakery business» 480; «how to open a restaurant» 1.760 pide antes subir la guía Casual ES a v2).
- El 94 % del ES dependía de España: caso «La Clara» con cifras 1:1 ambientado en Texas (mínimo federal, bollería para llevar
  exenta, rosca de Reyes/comuniones/Día de Muertos), precios pre-tax, ruta de permisos US en 30 pasos P1-P6, cottage food por
  estado, FDA Food Code 2022, FLSA, sales tax «por cómo vendes». Todo en `scripts/productos-digitales/guia-pasteleria-en/`.
- ≈ 8,7 M tokens de subagentes (L, techo 10 M).
- **LIVE el 17-oct (merge `882f6796` del #132).** Stripe `plink_1URUsY4CcdRGidmEk7sNDFEr` (`buy.stripe.com/4gMbIU0y0eAK9fh6Rf6oo1O`,
  **$69 USD**, impuesto automático, redirección comprobada con la CLI `--live`) + env `VITE_STRIPE_PAYMENT_LINK_HOW_TO_OPEN_A_PASTRY_SHOP`
  + mapa de 66 links. Gates LIVE: `--only` 0/0 · completo (VPS) **66 productos / 918 entregables / 0** · tienda (15 vivos fuera de ES) ·
  robots. Sitemap reenviado. **Tienda EN: 15 productos.**
- Correo EN **4-dic 14:00Z**: borrador `1e8b7c2f-5430-4ecb-8566-8b53f960fd3e` («Lanzamiento How to Open a Pastry Shop (EN) — 4-dic»,
  prueba a John enviada) + routine `trig_01LqowZy9azA47FqMag3Ktwn` (4-nov 15:07Z). Plantilla
  `broadcast-how-to-open-a-pastry-shop-lanzamiento-en.html`. **Siguiente hueco EN: 9-dic 14:00Z.**

### ▶️ 2026-10-17 (Claude Code en el Mac + VPS) — **Restaurant Checklists Kit Pro (EN, $19)** — LIVE
- Producto 16 de la tienda EN, edición del `kit-tareas` ES v2.0 (PR #133 draft, rama `feat/restaurant-checklists-en`, `checklists-kit/`).
  Elegido por demanda US (clúster de checklists ~1.300/mes). ≈ 2,1 M tokens (S). Revisión adversarial aplicada (4 MAYOR + 15 menor).
- Cierre y ficha de Stripe: `SESSION_HANDOFF_2026-10-17-restaurant-checklists-en.md` §1. Correo EN propuesto **9-dic 14:00Z** (borrador + routine).
- **LIVE el 17-oct (merge `43793a5b` del #133).** Stripe `plink_1URfCn4CcdRGidmEGm9hyWVC` ($19 USD, impuesto automático, redirección
  comprobada con la CLI `--live`) + env `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT` + mapa de 67 links. Gates LIVE: `--only` 0/0 ·
  completo (VPS) **67 productos / 930 entregables / 0** · tienda · robots. Sitemap reenviado. **Tienda EN: 16 productos.**
- Correo EN **9-dic 14:00Z**: borrador `a52e0565-a6bc-4a56-be43-887b32621033` + routine `trig_01GWsawxCZ8CbSBZ387HsMqo` (9-nov 15:07Z).
  Plantilla `broadcast-restaurant-checklists-lanzamiento-en.html`. **Siguiente hueco EN: 14-dic 14:00Z.**

### ▶️ 2026-10-18 (Claude Code en el Mac + VPS, noche delegada + cierre por la mañana) — **6 Checklists Kits verticales (EN, $19)** — LIVE
- Bar, Coffee Shop, Catering, Pizza Shop, Burger Joint y Ghost Kitchen: hermanos del Restaurant Checklists con el circuito
  `checklists-kit/` (`--kit <vertical>`). PR apilados #134 → #135 → #137 → #138 → #139 → #140, fusionados en ese orden (merge
  `1ce888d2`). ≈ 1,2-1,9 M tokens cada uno. Handoff: `SESSION_HANDOFF_2026-10-18-checklists-verticales-en.md`.
- Stripe: los 6 links comprobados con la CLI `--live` (USD 1900, one_time, exclusive, impuesto automático, redirección a su `/access`)
  + sus env `VITE_STRIPE_PAYMENT_LINK_<VERTICAL>_CHECKLISTS_KIT` + mapa de 73 links (`69bf9ec1`). Gates LIVE: `--only` ×7 kits de
  checklists 12/12 y 0/0 · completo (VPS) **73 productos / 1.002 entregables / 0 / 0** · tienda · robots. Sitemap reenviado. **Tienda EN: 22 productos.**
- Correos EN (borradores; se salta la semana de Navidad a Reyes, la peor para B2B en EE. UU.):
  Bar **14-dic** `32c61f17` · Coffee Shop **19-dic** `ff22235e` → routine `trig_01WXGbQnAuFnc2A9X45imtje` (20-nov 15:00Z) ·
  Catering **4-ene** `07edb170` · Pizza Shop **9-ene** `31c061de` · Burger Joint **14-ene** `3a412ac0` · Ghost Kitchen **19-ene** `b1f582a8`
  → routine `trig_019bxdctG1zV4XcVjbHTzCdu` (20-dic 15:00Z). Todos a las 14:00Z. **Siguiente hueco EN: 24-ene 14:00Z.**

### ▶️ 2026-10-24 (Claude Code en el Mac + VPS) — **Ice Cream Shop Checklists Kit Pro (EN, $19)** — listo a falta del Payment Link

- Elegido por demanda US (DataForSEO, 24-oct): ice cream shop business plan 320 · how to open an ice cream shop 170 · how to start
  an ice cream shop 90. Descartados: Food Truck Checklists (el kit ES es v1.1 con otro molde), «How to Open a Restaurant» (880) y
  «How to Start a Ghost Kitchen» (210), que dependen de guías ES aún en v1.1; «taco truck business plan» 9.900 es la misma serie que
  «food truck business plan» (Google la agrupa; la SERP es genérica de food truck).
- Séptimo hermano del circuito `checklists-kit/` (`--kit icecream`, molde mixto: 01-07 + bonus como el catering, 08-09 como el base).
  PR #156 draft. F1 0,43 M · traducción 0,17 M · F2 0,21 M · F3 0,39 M · revisión 0,22 M · ronda 1 0,36 M ≈ **1,8 M** (S, techo 2,5 M).
- La revisión cazó una **errata de seguridad en el ES LIVE** (heladería 02 «Pasteurización»: grasas y yemas DESPUÉS de pasteurizar):
  parcheada en el mismo PR con otras dos (mantecadora en vacío, cilindro), sin cambio de versión; también en `generate-tareas-heladeria.py`.
- Correo EN: hueco **24-ene 14:00Z** (borrador + routine el 25-dic, Resend no programa a > 30 días). Siguiente hueco EN: 29-ene.

### ▶️ 2026-10-24 (tarde-noche, Claude Code en el Mac + VPS, John fuera) — **Lote EN de 5: 4 productos más listos a falta del Payment Link**

- John: «avances con otras traducciones, tres o cuatro productos más. Cuando tengas cinco productos terminados y yo esté de vuelta
  en el ordenador, hacemos la configuración en Stripe». Lista para John: `PAYMENT_LINKS_PENDIENTES_JOHN.md` (en main).
- **#157 Chocolate Shop + Pastry Shop Checklists Kit Pro ($19 cada uno)**: hermanos 8 y 9 de `checklists-kit/` (`--kit chocolate`,
  11 xlsx, molde híbrido; `--kit pastry`, 15 xlsx con libros propios 10-13, molde base). ≈ 1,2 M y ≈ 1,75 M + F3 conjunta 0,65 M.
  🔴 Parche de seguridad del ES LIVE de chocolatería (ganache de nata fresca en frío y con fecha de caducidad, etiqueta con alérgenos,
  síntomas = no entra en obrador) y de maquetación del ES de pastelería (09). Handoff `SESSION_HANDOFF_2026-10-24-chocolate-pastry-checklists-en.md`.
- **#158 BBQ Catering Business Plan Kit ($39)** desde el parrillero 2.2 (`business-plans-en-6/`, conjunto `bbq`) ≈ 2,8 M y
  **#159 Paella Catering Business Plan Kit ($39)** desde el paellero 2.2 (`business-plans-en-7/`, conjunto `pael`, hermano del `bbq`)
  ≈ 2,4 M. Handoff `SESSION_HANDOFF_2026-10-24-bbq-paella-catering-plans-en.md`.
- PR apilados 156 → 157 → 158 → 159. Correos EN previstos (14:00Z): 24-ene Ice Cream · 29-ene Chocolate · 3-feb Pastry · 8-feb BBQ ·
  13-feb Paella. **Siguiente hueco EN: 18-feb.** Tienda EN tras el lote: 27 productos.

### ✅ 2026-10-25 (madrugada, Claude Code en el Mac) — **Lote EN de 5 LIVE**

- John creó los 5 Payment Links (comprobados con la CLI: USD, pago único, `exclusive`, redirección a `/access`); env `VITE_*` en
  Netlify (builds, all); `payment-links.ts` regenerado (`580c8384`); pila fusionada con el #159 (merge `7e7afc6e`, los 4 PR MERGED).
- LIVE: `gate-flujo-postpago --only` ×5 con 0 fallos y 0 avisos · gate completo en el VPS **78 productos · 1052 entregables · 0 fallos** ·
  `tienda-gate --base https://aichef.pro` verde · `robots-gate --live` verde · sitemap reenviado a GSC (los 5 dentro).
- Correos EN (borradores, segmento EN, `hello@news.aichef.pro`): Ice Cream **24-ene** `46c47e9f` · Chocolate **29-ene** `0735f547` ·
  Pastry **3-feb** `a71df3dc` · BBQ **8-feb** `72b926e7` · Paella **13-feb** `d7cc1366` → routine `trig_011hh6jpM66sktLqw3dDhY8H`
  (16-ene-2027 15:00Z). Todos a las 14:00Z. **Siguiente hueco EN: 18-feb 14:00Z.**

### ▶️ 2026-10-25 (Claude Code en el Mac + VPS) — **Plan de Negocio: Heladería Artesanal (ES, 35 €, producto nuevo nº 52)** — ✅ LIVE 25-oct a las 15:52 (Madrid; 14:52Z)

- Elegido por su gemelo EN (ice cream shop business plan 320/mes US) y por ser el primero de «Próximos» (Q4). Siguiente producto
  nuevo propuesto: **Finca de Eventos y Bodas** (wedding venue business plan 1.000 + event venue 720/mes US, al alza).
- F1 (research + camino + SPEC) → F2 (Excel calibrado en 1 vuelta, Word por 2 redactores Sonnet, checklist 80) → F3 (capa técnica,
  ficha, correo, guía de equivalencias, 7 imágenes) → revisión opus final (0 B / 7 M / 17 m, aplicados). ≈ 2,2 M (techo M 5 M).
  PR #161 → merge `cbdcccd6`. Payment Link de John `plink_1UUSdP4CcdRGidmEm3lXcQyH` (comprobado con la CLI), env
  `VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA`. Gates LIVE: postpago 1/4/0, tienda, robots, Miselup 104/104, fase 6 solo con sus 3
  fallos congelados; sitemap reenviado a GSC. Detalle: `SESSION_HANDOFF_2026-10-25-plan-heladeria.md`.
- **Correo ES: 28-nov 08:00Z**, borrador `3297bad5` (prueba a John enviada) → routine `trig_0196bsymHKgB8728KxtTmBdk`
  (29-oct 15:07Z). **Siguiente hueco ES: 3-dic 08:00Z.**
- Mismo día: **PR #160**, normativa derogada (RD 1420/2006 y RD 3484/2000 → RD 1021/2022) en 7 entregables vendidos, listo y
  verificado; fusionado con el visto bueno de John (merge `daf6f28a`). Arreglo en `censo-terminos-es.py` (leía las propias guías
  de equivalencias). Hallazgo para decidir: 6 guías ES con PDF de portada de 1 página y «60+ páginas» en la landing (handoff §5).
- **Mismo día, por la tarde (John: «adelante con el arreglo rápido de las 6 guías»): PR #162 + #163 LIVE.** Las 6 guías ES v1
  (panadería-obrador, casual, japonés, mexicano, nikkei, peruano) entregan ya el PDF real exportado del Word con LibreOffice en
  el VPS (14 · 21 · 23 · 22 · 24 · 22 págs. A4), con el Word en A4, sin la página en blanco del nikkei y con las listas
  numeradas reiniciando en 1. 137 menciones de páginas cambiadas por las reales (fichas, hubs ×7, SPA). Al cerrarlo,
  `paginas-gate` cazó dos más con el mismo defecto: gastronómico (anunciaba 119; PDF = Word, 24 págs.) y dark kitchen (40 → 27).
  **`paginas-gate` en todo el catálogo: 0 fallos** (estaba en rojo desde el 10-sep). Changelog 1.1.1 en las 7. Scripts:
  `scripts/productos-digitales/guias-v1-pdf/`. LibreOffice + Carlito instalados en el VPS.
  John (25-oct): **no se envía correo** a los compradores por este arreglo; basta el aviso del changelog en su panel.

### ▶️ 2026-10-25, tarde (Claude Code en el Mac + VPS) — **Plan de Negocio: Finca de Eventos y Bodas (ES, 45 €, producto nuevo nº 53)** — ✅ LIVE 25-oct (merge `769a0e26`)

- John: «Finca de Eventos y Bodas como siguiente producto nuevo. Adelante». F1 (research + camino + SPEC) → F2 (motor, calculadora,
  contrato, Word, guía de equivalencias) → F3 (capa de producto, hubs ×7 + SPA) → una revisión opus (0 B · 9 M · 26 m) y una ronda de
  arreglos. ≈ 4 h y ≈ 3,1 M tokens. PR #164 draft. Detalle: `SESSION_HANDOFF_2026-10-25-plan-finca-eventos.md`.
- Modelo: finca arrendada + catering exclusivo concesionado con canon. Caso 120 eventos × 82 invitados × 37 €; neto 8,8 / 11,9 / 12,2 %.
- **Correo ES: 3-dic 08:00Z**, borrador `c41977a6` (prueba a John enviada) → routine `trig_01QkpkZGN18qx4WPpWQBp8FT` (3-nov 15:07Z).
  **Siguiente hueco ES: 8-dic 08:00Z.**

### ▶️ 2026-10-25, noche (Claude Code en el Mac + VPS) — **Plan de Negocio: Pizzería Napolitana (ES, 35 €, nº 54) + Pizza Shop Business Plan Kit (EN, $39)** — ✅ LOS DOS LIVE

- John: «luz verde, decide tú» → Pizzería Napolitana (EN «pizza shop business plan» 320/mes US); luego «dejar la versión en los dos
  idiomas en producción». ES: PR #165 → `2e7a3af5` (link `plink_1UUXG84CcdRGidmEsDF3iCG4`). EN: PR #166 (apilado) → `64ace831` (link
  `plink_1UUXZ54CcdRGidmEovs56WB3`). Detalle: `SESSION_HANDOFF_2026-10-25-plan-pizzeria-es-en.md`.
- Gates LIVE: postpago 0/0 en los dos · tienda verde · robots · Miselup 108/108 · hub PASS · fase 6 = sus 3 congelados · cripto 200 ×2 ·
  sitemap reenviado. Tienda EN: 28 productos.
- **Correo ES: 8-dic 08:00Z**, borrador `92c8a19f` → routine `trig_011hWcNXXF55pgXjW7iGCMjF` (8-nov 15:07Z). **Siguiente hueco ES: 13-dic 08:00Z.**
- **Correo EN: 18-feb-2027 14:00Z**, borrador `c6290aee` → routine `trig_01Htsk9cNWagXEsLcdM4B6hZ` (19-ene 15:07Z). **Siguiente hueco EN: 23-feb 14:00Z.**


### ▶️ 2026-10-27 (Claude Code en el Mac + VPS) — **Tienda EN: Hotel Checklists Kit Pro ($29) + Ice Cream Shop Business Plan Kit ($39) + Wedding Venue Business Plan Kit ($49)** — ✅ LOS TRES LIVE (27-oct, merge `ae531f6b`)

- John: «escoge los tres que siguen y dale luz verde continua… completos me dices y creamos los enlaces de pago en Stripe». Elegidos
  con DataForSEO US del 27-oct: wedding venue business plan 1.000/mes (260 → 1.000 en 6 meses) + event venue 720 · ice cream shop
  business plan 320 + how to open 170 · hotel housekeeping/room cleaning checklist 260 (una serie) + maintenance 70 + otros ≈ 450.
  Descartados: guía Dark Kitchen (ES v1), «housekeeping checklist template» 1.900 (doméstica), el resto < 50/mes.
- PR apilados **#170 (Hotel) → #171 (Ice Cream) → #172 (Wedding)**, fusionar en ese orden. Fichas de Stripe: `PAYMENT_LINKS_PENDIENTES_JOHN.md`.
  Detalle: `SESSION_HANDOFF_2026-10-27-tienda-en-hotel-icecream-wedding.md`.
- Parche de seguridad del **ES LIVE `kit-tareas-hotel`** en el #170 (sin cambio de versión, sin correo): cierre del spa sin apagar la
  filtración del jacuzzi, 35-38 °C solo del jacuzzi, moqueta.
- **Correos EN (14:00Z, segmento EN):** **Wedding 23-feb-2027** · **Ice Cream 28-feb-2027** · **Hotel 5-mar-2027**. Plantillas en
  `emails/broadcast-{wedding-venue-business-plan,ice-cream-shop-business-plan,hotel-checklists}-lanzamiento-en.*`, sin programar:
  borradores `ca9d54a1` (Wedding) · `4692539a` (Ice Cream) · `f191af0f` (Hotel), prueba a John enviada → UNA routine
  `trig_015MWHYv3BP4FYUCeQPQee9K` (3-feb-2027 15:07Z) los programa a los tres. **Siguiente hueco EN: 10-mar-2027 14:00Z.**
- **LIVE 27-oct** (merge `ae531f6b` de la pila por el #172; #170 y #171 quedan «merged»). Links: Hotel `plink_1UV6mM4CcdRGidmEPIg3fmmj` ($29) ·
  Ice Cream `plink_1UV6rK4CcdRGidmE9nLDNQrU` ($39) · Wedding `plink_1UV6uO4CcdRGidmEotbwEDkd` ($49), comprobados con la CLI. Gate completo
  LIVE 85 productos · 1102 entregables · 0 fallos; tienda, robots, hub verdes; Miselup 108/108; cripto 200 ×3 (pedidos QA `qa-hotel-en`,
  `qa-icecream-en`, `qa-wedding-en` y `qa-ctrl`, por purgar); parche ES del spa comprobado en producción; sitemap reenviado. Tienda EN: 31.
