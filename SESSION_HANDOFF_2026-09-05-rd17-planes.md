# Handoff — RD-17 en la familia de PLANES: Plan de Negocio Bar-Restaurante 2.1 · sesión Claude Code 2026-09-05 (Mac)

> Sesión IMPAR del ciclo alternado (tras dos productos nuevos seguidos, 3-5 sep). El guion del handoff anterior (§7)
> mandaba «IVA del 21 % vivo en los 10 planes». Lo primero que se hizo fue medirlo, y el encargo se acotó a lo real.

## 1. Estado al cierre — commit `680d939` en `main`, pusheado a las 13:00; verificación LIVE: ver §6

| Pieza | Estado |
|---|---|
| Diagnóstico | Censo con openpyxl sobre los 30 xlsx de los 10 planes + los 408 del resto de `dl/`: **el 21 % en bebida sólo vivía en `plan-negocio-bar-restaurante/plan-financiero-bar-restaurante.xlsx`** (único con el molde v2.0). Los otros 9 planes son v1.1 sin ese parámetro. En las demás familias no hay 21 % ligado a la bebida servida (guía gastronómica ya corregida el 31-ago; Food Cost correcta; kit de catering: 2 notas a revisar, §5) |
| Motor de planes (`planes-v2_0/`) | `iva_bebida` en B63 (10 %); mezcla de VENTAS por canal (`pct_delivery` B16 → el alcohol repartido al 21 %); COMPRAS intactas; `_purgar_dv_celdas()` (bloqueante: DV solapadas al reaplicar); gates de versión comparan `motor.VERSION` (antes literal '2.0'); `VERSION_MES`; guarda numérica en `alta()`; rótulo «ARRANQUE Y AFORO» en A49; cabecera de la tabla de recalibrado con la versión real; nota en la partida Suministros (agua al 10 %) |
| Contenido (`contenido_plan_negocio_bar_restaurante/a.py`) | entrada única del ticket (18,20 €); tabla RECALIBRADO en lenguaje de cliente y con plantilla/alquiler/suministros reales (7 puestos / 151.939 €, 3.000 €/mes, 3,2 %); docstring con los ratios medidos (33,7 / 8,0 / 27,2 / 10,8 %) |
| Entregables LIVE | `plan-financiero-bar-restaurante.xlsx` (64.805 B) y `checklist-apertura-bar-restaurante.xlsx` (13.882 B), versión **2.1 · septiembre 2026**; `dl/` = dry-run celda a celda (0/0). Respaldo previo en el scratchpad (`apply/respaldos/…bak-20260905-125828`, se pierde al reiniciar; la versión anterior está en git: `git show 680d939^:astro-site/public/dl/plan-negocio-bar-restaurante/plan-financiero-bar-restaurante.xlsx`) |
| Paellero | `checklist-apertura-paellero-eventos.xlsx!'Checklist 6 fases'!C23` «Modelo 303 (IVA trimestral 21%)» → «Modelo 303 (autoliquidación trimestral del IVA)», parche a nivel de zip (una celda; censo `--fail` 0) |
| Capa de producto | changelog **2.0 (faltaba) + 2.1**; landing .ts, 6 gemelos de la SPA y el dashboard con 9 hojas / 7 fases / 64 trámites / SS 33 % / tarjeta Word con las 10 secciones reales / «Versión 2.1 · septiembre 2026»; testimonios intactos |
| SPEC | enmienda RD-17 al principio de `planes-v2-SPEC.md` (manda sobre §2.1/§2.7/§2.9), con el alcance real y la decisión pendiente sobre la numeración de los hermanos |
| Informe del APPLY | `auditorias/planes-v2-real-plan-negocio-bar-restaurante-2.1.json` |

Efecto medido en el caso de ejemplo (todas las celdas de valor cambiadas —37— son atribuibles):

| | 2.0 (21 %) | 2.1 (10 %) |
|---|---|---|
| PVP equivalente del ticket (18,20 € sin IVA) | 20,72 € | 20,02 € |
| IVA repercutido, año 1 | 55.562,42 € | 45.136,00 € |
| Cobros con IVA, flujo neto y saldo de cierre | | −10.426,42 € cada uno |
| Saldo mínimo del año | 61.956,61 € | 60.973,53 € |
| Payback del proyecto | 2,58 años | 2,75 años |
| P&L, punto de equilibrio, IVA soportado | sin cambios | sin cambios |

## 2. Método (y lo que costó)

1. Censo de `dl/` antes de creer el guion → alcance real (1 producto, no 10).
2. Parche → dry-run (`main.py --dry-run`, TODO VERDE) → **diff celda a celda contra el LIVE** (`scratchpad/rd17/diff_live_dry.py`:
   fórmulas + caché). El diff cazó que el primer blend único bajaba también el IVA SOPORTADO de las compras de bebida
   (`'2. P&L 3 Años'!G15` alimenta la fila 41 y las filas 11/17 de tesorería). Dos mezclas: ventas y compras.
3. Refutación: workflow de **5 lentes opus** (fiscal, código, cifras, contenido/capa, consumidores) → **57 hallazgos**
   (1 bloqueante, 9 altos). Ronda 2: **3 verificadores sonnet + relectura fiscal opus** → 20 (ninguno alto). Ronda 3: texto.
   Coste: 1,12 M + 1,00 M tokens de subagentes.
4. APPLY con `PLANES_APPLY=1` (respaldo automático) → `dl/` vs dry-run 0/0 → commit → push → gate LIVE con el deploy verde.

## 3. Trampas nuevas (para la memoria)

- **Reaplicar el motor sobre su propia salida duplica validaciones de datos si el rango cambia.** `_purgar_dv_duplicadas`
  comparaba `sqref` por igualdad: al meter B63 en el grupo de porcentajes, la DV nueva ya no era idéntica a la vieja y las
  dos quedaban SOLAPADAS sobre 22 celdas (Excel abre con diálogo de reparación). Ningún gate lo veía: la «huella» de la
  idempotencia no incluye DV. Ahora se purga por solape de celdas. **Regla: al añadir una celda a un grupo con validación,
  contar las DV del LIVE y del regenerado.**
- **El IVA tiene dos sentidos y un solo blend los cruza.** Un tipo «de la bebida» usado a la vez para lo que se repercute
  y para lo que se soporta cambia los dos al tocar uno. Ventas y compras, cada una con su mezcla.
- **Un gate de versión con el número escrito a mano** (`'2.0' in v`) da verde comprobando la versión vieja: es el autotest
  de bodega otra vez. Capturar el número y comparar con la constante.
- **El calendario/handoff sobredimensionaba la deuda 10×**: medir antes de heredar un «está vivo en los 10».
- **`alta()` conserva el valor de una celda si existe**: un rótulo nuevo sobre una celda que ya tenía contenido (A50) no lo
  pisa y el bloque se queda sin título; y un texto heredado en una celda numérica alimentaría 26 fórmulas (guarda nueva).
- **Cambios de código posteriores al último APPLY viajan en la siguiente regeneración** (REF-10, el título real de la hoja
  en Instrucciones!A7): hay que atribuirlos en el diff y declararlos en el changelog.
- **La tabla «qué ha cambiado» de un producto se desincroniza sola**: la 2.0 decía 17,20 € (B5 = 18,20), 6 puestos (7),
  2.900 € (3.000). Los valores derivados que van a una tabla de texto se recalibran cuando cambia el supuesto, o se
  calculan.
- **Los testimonios no se tocan** aunque citen cifras viejas («50+ trámites»): son citas y capa comercial (regla de John).

## 4. Refutación: qué quedó diferido y por qué (ninguno bloquea; los marcados 👁 los ve el comprador)

- 👁 **Docx v1 del bar contradice al xlsx** (40 cubiertos a 22 € frente a ~63 a 20,02 €): T9 de la familia (regenerar el
  docx desde los supuestos). Ya estaba pendiente desde `c0ba0a6`; RD-17 no lo empeora.
- 👁 Fila de aire antes de «UMBRALES Y SUELOS DE CONTROL» (B63 pega con A64): cosmético; mover el bloque son 5 celdas ya
  publicadas (`alta()` dejaría duplicados). Para una 2.2 con purga explícita.
- Notaría y registro llevan IVA al 21 % (`'1. Inversión Inicial'!E41` = «No» → 126 € de IVA deducible perdidos) y la partida
  9 (proyecto técnico + tasas municipales) va entera al 21 %: cambian números → misma tanda 2.2.
- La bebida no alcohólica de compra se aproxima al 10 % (refrescos azucarados van al 21 %) y el canal delivery hereda el
  reparto comida/bebida de la sala: aproximaciones DECLARADAS en las notas; parámetro propio si algún día hace falta.
- Gate ortográfico del motor no lee literales dentro de fórmulas (C9, columna O).
- Nota de inversión del sujeto pasivo para plataformas extranjeras (TheFork, delivery, software).
- `modelos-contrato-paellero-eventos.docx`: «factura … con IVA al 21 %» — un catering para consumir en el acto es hostelería
  al 10 %; decidirlo con la lente fiscal cuando se aplique ese hermano.
- Kit de tareas de catering (`09-cobros-facturacion-eventos.xlsx`, Instrucciones!B20 y «Después del Evento»!B9): gravan la
  bebida alcohólica del evento al 21 %; misma decisión RD-17 pendiente en esa familia.
- **Decisión antes de aplicar los 4 hermanos de línea A** (cafetería, tapas-bar, panadería, food-truck, con contenido ya
  construido): nacen como 2.1 (su changelog cuenta el salto 1.1 → 2.1 entero) o se les estampa primero la 2.0. Además el
  tapas-bar tiene un fallo PREVIO de contenido (RD-34: orígenes ≠ usos, 6,4 % > 5 %), verificado idéntico con el código
  original.

## 5. Pendientes de John (no bloquean)

1. **Informe del buscador del hub**: `ADMIN_PASSWORD='…' python3 scripts/productos-digitales/buscador-report.py --days 7`.
   La contraseña es secreta en Netlify y el CLI no la devuelve; hace falta que la pegue John (deberían aparecer las 3
   búsquedas de prueba de la madrugada; si sale 0, Blobs no está habilitado en el site).
2. **Compra de prueba del Manual del Manager** (o `aichef.pro/admin/generar-acceso`); el mailing sigue programado para el
   lunes 7-sep 10:00.
3. Decisión sobre la numeración de los hermanos (arriba) y sobre el kit de catering.

## 6. Verificación en producción (tras el deploy)

`python3 scripts/productos-digitales/gate-flujo-postpago.py --only plan-negocio-bar-restaurante` compara el `content-length`
LIVE con el tamaño en DISCO: hasta que Netlify termine, dará fallo en los dos xlsx (64.805 y 13.882 B). Resultado: ver el
último apartado de este fichero.

## 7. Próxima sesión

Por la alternancia toca **PAR (producto nuevo)**, y el presupuesto semanal (1 producto/semana) se reabre el lunes 7-sep:
siguiente de la línea «Manuales» (Chef Ejecutivo) o lo que diga el informe del buscador. La siguiente IMPAR: documentos
de la guía gastronómica (handoff B §20.5, 47 bloqueantes en la síntesis del crítico).

Via: Claude Code
