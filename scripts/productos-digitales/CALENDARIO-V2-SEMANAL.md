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
- **Segmento EN, lunes 28-sep 14:00 UTC** (`d3bd1f9c-…`): presentación de la tienda EN + primer producto en un solo correo.
- La cola EN es **independiente** de la ES (otro segmento): hueco = último envío al segmento EN + 5 días, sin coincidir con un
  correo de producto ES el mismo día. Detalle: handoff `SESSION_HANDOFF_2026-09-25-food-cost-kit-en.md` (bloque de la tarde).
- Cola ES sin cambios: Chocolatería 24-oct **pendiente de D53** (John) · Taquería 29-oct (desde el 29-sep) · Escandallos 2.1 3-nov (desde el 4-oct).

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
| Cómo Montar una Churrería-Chocolatería | Guías Cómo Montar | 65 € | Q4 2026 |
| Plan de Negocio: Heladería Artesanal | Planes de negocio | 35 € | Q4 2026 |
| ~~Tareas Recurrentes: Taquería Mexicana~~ **✅ LIVE 20-sep-2026** (producto 50, 14 €, PR #85 → `4f214a0`; correo el 29-oct) | Kits de tareas | 14 € | — |
| Kit Cuadro de Mando Operativo | Kits de gestión | 19 € | Q4 2026 |
| Plan de Negocio: Hamburguesería Smash | Planes de negocio | 35 € | Q4 2026 |
| Plan de Negocio: Finca de Eventos y Bodas | Planes de negocio | 45 € | Q1 2027 |
| Tareas Recurrentes: Pollería y Pollo a la Brasa | Kits de tareas | 12 € | Q1 2027 |
| Tareas Recurrentes: Arepería | Kits de tareas | 12 € | Q1 2027 |
| Plan de Negocio: Pizzería Napolitana | Planes de negocio | 35 € | Q1 2027 |
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
