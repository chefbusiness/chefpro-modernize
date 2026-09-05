# Handoff — Planes de Negocio, línea A completa en v2.2 · sesión Claude Code 2026-09-05 (Mac), segunda parte

> Continuación de `SESSION_HANDOFF_2026-09-05-rd17-planes.md`. John a las 13:50: «suspende el presupuesto semanal, luz verde,
> decide tú… avanza con todo a producción». Decisión: subir los 4 hermanos de línea A a la nueva versión (su contenido
> y su refutación existían desde el 29-ago) y arrastrar al representante con el motor mejorado.

## 1. Estado al cierre — commit `f9283b3` en `main` (17:32) · verificación LIVE en §6

| Producto | Antes | Ahora | Ficheros regenerados |
|---|---|---|---|
| plan-negocio-bar-restaurante | 2.1 (13:00 de hoy) | **2.2** | plan-financiero (67.094 B) + checklist (13.940 B); docx 1.1 |
| plan-negocio-cafeteria | 1.1 | **2.2** | plan-financiero-cafeteria-brunch (65.598 B) + checklist (22.245 B, 75 trámites); docx 1.1 |
| plan-negocio-tapas-bar | 1.1 | **2.2** | plan-financiero-tapas-bar (66.327 B) + checklist (21.743 B, 73 trámites); docx 1.1 |
| plan-negocio-panaderia | 1.1 | **2.2** | plan-financiero-panaderia (66.513 B) + checklist (20.583 B, 66 trámites); docx 1.1 |
| plan-negocio-food-truck | 1.1 | **2.2** | plan-financiero-food-truck (66.454 B) + checklist (21.217 B, 68 trámites); docx 1.1 |

Cifras estrella finales (leídas del libro): payback del proyecto antes de la deuda — bar 2,3 años (CAPEX 1,6) · cafetería
2,8 (2,0) · tapas-bar 2,8 (2,2) · panadería «Más de 3 años» (2,4) · food-truck «Más de 3 años» (2,9). DSCR mínimo: 3,31 ·
2,10 · 2,29 · 2,01 · 1,37. Todos: 9 hojas, 13/13 gates, idempotencia 0, blancos 0.

## 2. Qué se hizo, en orden (y cuánto costó)

1. **Dry-run de los 4 hermanos con el motor 2.1** (en serie, cerrojo): panadería y food-truck verdes, cafetería y tapas-bar con
   RD-34 (orígenes ≠ usos). CPU rozó los 65 °C: desde aquí, TODA regeneración pasa por `mkdir $S/lock.main` + `istats`.
2. **4 correctores opus de contenido** (42 min, 1,6 M): refutaciones del 29-ago resueltas en `contenido_<pid>/a.py`; devolvieron
   53 hallazgos de nivel motor. Commit `3ddd489`.
3. **Motor 2.2** (1 opus, 56 min, 0,5 M) sobre `scripts/productos-digitales/planes-v2-motor-2.2-SPEC.md`: A1-A8 + B1-B15;
   diff del bar 100 % atribuido. Commit `b6aa6d5`. Verificado por mí con 5 dry-runs propios.
4. **Refutación 2.2** (5 opus, 36 min, 1,8 M): 94 hallazgos (4 bloqueantes de contenido/docx) + 130 frases de capa de producto.
5. **Motor 2.2.1** (1 opus, 52 min, 0,45 M): 24 ítems (payback en base contable única, escenarios comparables, interpretación del
   equilibrio, VOCABULARIO, IVA_COMPRAS, títulos, guardas, reemplazos auditados). Commit `38057e9`.
6. **Capa de producto** (4 sonnet, 16 min, 1,1 M): landing, dashboard, gemelos SPA, borradores de broadcast; propuestas de
   changelog y emailBody fusionadas por el orquestador. Commits `ae57b6b`, `9924088`.
7. **Segunda vuelta de contenido** (4 opus, 23 min, 1,1 M): bloqueantes de cifras estancadas en las tablas que lee el comprador.
   Commit `a31751b`.
8. Dry-runs finales propios (5, verdes) → cruce de cifras citadas (`$S/verificar_cifras_capa.py`: recuentos de fórmulas
   corregidos a 742/742/737/722; el resto de discrepancias están dentro de testimonios, que no se tocan) → **APPLY de los
   cinco** con respaldo → dl/ = dry-run final celda a celda (0/0 en los 10 xlsx) → commit `f9283b3` → push.

Subagentes: ≈ 6,6 M tokens en esta parte (+ 2,1 M de RD-17 por la mañana).

## 3. Trampas nuevas (para la memoria)

- **Un payback que divide la necesidad total de caja entre flujos después de la deuda cuenta la deuda dos veces** (y «Más de 3
  años» sale de eso, no del negocio). Y mezclar caja real del año 1 con base contable en los años 2-3 mueve medio año la cifra.
  Una sola base, declarada.
- **Una clave de contenido nueva no sirve si el motor no la lee**: la tabla de cambios (RECALIBRADO) es contenido y envejece sola
  cuando el motor mueve una cifra. Regla aplicada: lo que el motor calcula (payback, equilibrio, cuadre) se compone por fórmula;
  la tabla no lleva esas cifras a mano.
- **El §1 transversal (tildes, €, erratas) corre ANTES que los reemplazos del checklist**: al ampliar TILDES dejaron de casar 4
  patrones del tapas-bar en silencio. Ahora los patrones que no casan se reintentan contra el texto sin sanear y un gate cuenta
  los «no entregados» como fallo.
- **Los correos y las landings no citan cifras que un parche en curso pueda mover** (payback, DSCR, saldos): se citan
  hojas, fórmulas, trámites, ticket e inversión, y se reverifican contra el libro final antes del push.
- **El push puede fallar por un commit ajeno** (otra sesión subió un handoff a las 14:03): `git fetch` + `rebase` antes de
  reintentar, nunca `--force`.

## 4. Diferido con motivo (nada bloquea; 👁 = lo ve el comprador)

- 👁 **Los 5 docx siguen en 1.1** y contradicen al Excel (facturación, ticket, inversión, plantilla): T9 de la familia
  (`documentos.py` para planes no existe aún; los productos se escriben con subagentes Anthropic, no con bridge). Declarado en
  Instrucciones del libro, landing, dashboard, changelog y correo.
- IVA por FILA en la hoja de Inversión (hoy Sí/No al 21 %): stock inicial de panadería al 4 %, tasas sin IVA.
- Cobertura de tienda y obrador por separado (panadería); ámbar por arriba en la cobertura (tapas-bar, 138 %: la plantilla se
  dimensionó contra el cuadrante de restaurante y ahora sobran ~2.200 h: recalibrar plantilla = decisión de contenido).
- Vocabulario restante en panadería/food-truck («aforo», «barra» en el bloque apagado de rotación); fila vacía A50 con ROTACION
  apagada (mover celdas de Supuestos está prohibido por idempotencia).
- Parámetro para la bebida no alcohólica de compra al 21 % (refrescos azucarados): hoy sólo declarado en la nota.
- SMI 2026 = 17.094 € sin verificar contra el BOE (se retiró el número de RD de todas las notas).
- Cafetería: préstamo 112.000 € con 2,8 % de margen sobre la necesidad (decisión de John si se baja a 108.000 €).
- Nombres de hoja > 31 caracteres del parrillero (RC-29) y grupo_b/grupo_c (línea B) — fuera de esta tanda.

## 5. Correos (regla de John: uno por producto actualizado/nuevo, cola de 5 días)

| Slot (08:00 UTC) | Correo | Estado |
|---|---|---|
| 07-sep | Lanzamiento Manual del Manager | programado (`3749f084…`) |
| 12-sep | Bar-Restaurante **2.2** (`broadcast-plan-negocio-bar-restaurante-v2.2-es.html`) | programado `98f9081d…`; el 2.1 (`7d49e0a3…`) BORRADO |
| 17-sep | Cafetería 2.2 | ver §6 |
| 22-sep | Tapas Bar 2.2 | ver §6 |
| 27-sep | Panadería 2.2 | ver §6 |
| 02-oct | Food Truck 2.2 | ver §6 |

## 6. Verificación LIVE y correos programados (17:45)

- Deploy de `f9283b3` en verde; `gate-flujo-postpago.py --only <pid>` en los cinco: **3 entregables, landing/access/library 200,
  0 fallos, 0 avisos**; los 10 xlsx servidos por el CDN son **byte a byte** los del repo (`cmp`); las cinco landings sirven
  «Versión 2.2 · septiembre 2026» y «(9 hojas)». El changelog se pinta en los dashboards (island `client:only`): comprobarlo en
  la compra de prueba.
- Correos programados (segmento «AI Chef Pro ES», 08:00 UTC; prueba de cada uno enviada al buzón de John):
  Cafetería 17-sep `9c9d9b0c…` · Tapas Bar 22-sep `d5db4679…` · Panadería 27-sep `021b364e…` · Food Truck 2-oct `f75380d7…`
  (+ Manual 7-sep `3749f084…` y Bar 2.2 12-sep `98f9081d…`). Próximo hueco libre: **7-oct**.

## 7. Próxima sesión

Alternancia: toca **PAR (producto nuevo)** con el presupuesto semanal reabierto el lunes 7-sep (Manual del Chef Ejecutivo o lo
que diga el informe del buscador, pendiente de John con `ADMIN_PASSWORD`). Siguiente IMPAR: documentos de la guía gastronómica
(handoff B §20.5) o T9 de los 5 docx de planes (los ve el comprador). Línea B de planes (5 productos v1.1) necesita `grupo_b`.

Via: Claude Code
