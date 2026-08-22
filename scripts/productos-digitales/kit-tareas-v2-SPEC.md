# Kit de Tareas Recurrentes (representante de la familia «▸») — v2.0 (SPEC, 2026-08-22)

Origen: R1 de `kit-tareas` (`auditorias/kit-tareas-R1.json`: 81 hallazgos, 7 altas, «no listo» ×3),
con cada hallazgo etiquetado MOTOR (se repite en los hermanos) o CONTENIDO (propio del kit base).
Referencias: `kit-tareas-pasteleria-v2-SPEC.md` y `kit-pasteleria-v2_0-postprocess.py` (el bloque de
caja `ajustar_09`/`_fondo_de_caja`, `normalizar_checklist`, `insertar_fila/columna`,
`linea_instrucciones`), y los paquetes `kit-escandallos-v2_0/` y `pack-appcc-v2_0/` (arquitectura
`main.py --dry-run / --solo / <PID>_APPLY=1` con respaldo, idempotencia por reconstrucción,
`inject_cache.py` al final, verificación `data_only` + pycel + censo). Nada de builds ni Playwright;
python en serie; `istats`.

**Arquitectura obligatoria del paquete `kit-tareas-v2_0/`:** `motor.py` = correcciones ESTRUCTURALES
de la familia, válidas para cualquier kit «▸» (01-07 + BONUS) y para cualquier 08/09 de negocio/caja
(los tienen 12 kits: kit-tareas, cafetería, pizzería, hamburguesería, dark-kitchen, bar, catering,
chocolatería, heladería, hotel 18/19, restaurante-creativo 10/11 — detectar por CABECERA, nunca por
nombre de fichero); `contenido_kit_tareas.py` = cambios de CONTENIDO de este kit; `main.py --producto
<pid>` (por defecto `kit-tareas`) para poder aplicar el motor a un hermano sin su módulo de contenido.
El motor NO debe romper lo que la Fase A dejó (casilla unificada, contadores, A4, metadata).

## 1. MOTOR — caja y negocio (08/09 de los 12 kits)
1.1 **Arqueo correcto** (DOM-01/TEC-01/COM-01, alta): en «Apertura de Caja» un bloque «Fondo de caja
inicial (€)» con celda verde editable (y la tarea «Registrar importe de fondo de caja» apunta a ella:
DOM-05/COM-15); en el Resumen de «Cierre de Caja» fila «Fondo de caja inicial (−)» = esa celda y
`TOTAL FACTURADO = Total efectivo − Fondo + Tarjetas + Otros`; `DESCUADRE = TOTAL FACTURADO − Z del
TPV` con CF ámbar si ≠ 0. Portar de pastelería v2.0. Moneda **0,02 €** en el recuento (DOM-03/COM-04);
DV `whole ≥ 0` y formato `0` en Cantidad (TEC-20); etiquetas con merge A:B y anchos legibles (TEC-03).
1.2 **Registro mensual**: columna «Z del TPV» antes de «Descuadre», `Descuadre = IFERROR(Total
facturado − Z, 0)` en las 31 filas con CF ámbar (DOM-04/TEC-04/COM-14); el total de «Fondo apertura»
deja de sumarse (promedio o «(no sumable)») (TEC-05).
1.3 **Hojas de caja**: columna «Firma» y «Responsable» precargado (TEC-07/COM-21); Instrucciones
PROPIAS de caja (qué resuelve, cómo se cuenta por denominaciones, celdas de entrada, se conecta con
08 y con el registro mensual) (DOM-22/TEC-12); título de metadata descriptivo (COM-27).
1.4 **08 negocio**: «Responsable» y «Hora Límite» precargados en todas las tareas con el criterio
del kit (Encargado / Último en salir; horas ancladas al horario) (DOM-06/TEC-06/COM-10).
1.5 **08/09 al molde «▸»** (DOM-21/COM-19/COM-11/COM-12/TEC-08): DV «✓,—,N/A» (estándar de
pastelería v2.0; explicar «—» = no hecho y «N/A» en Instrucciones), verde `E8F5E9` en celdas
editables (Responsable, Hora, ✓, Firma, Notas, importes), contador agrupado con etiqueta fusionada
(TEC-21), Instrucciones con el molde ▸ (qué resuelve / cómo usar / celdas editables / se conecta con),
apaisado en las hojas de 8 columnas (TEC-19), alturas de fila en Instrucciones sin cortar (TEC-18).
Se conserva la columna «Notas».

## 2. MOTOR — checklists «▸» (01-07 + BONUS, y los 08/09 ya unificados)
2.1 **Contador honesto** (DOM-10/TEC-09/COM-22): denominador `=COUNTIF(B,"?*") − COUNTIF(F,"N/A")
− COUNTIF(F,"—")` (texto en Instrucciones: «las tareas marcadas N/A o — salen del total»).
2.2 **Filas libres** (DOM-11/TEC-11/COM-17): 5 filas libres con formato, DV y CF DENTRO del rango
contado (insertar antes de la fila de holgura existente; como pastelería `HOLGURA`), Instrucciones
«en las filas verdes libres; si necesitas más, inserta filas dentro de la tabla».
2.3 **07 plantilla personalizable** (TEC-02/COM-05/DOM-07/TEC-13/COM-16): denominador por fórmula
(la excepción INT-03 de la Fase A deja de aplicar: ya no conserva el 15) y las tres hojas
DIFERENCIADAS: «Por Franja Horaria» con secciones APERTURA / SERVICIO / CIERRE; «Por Área» con
COCINA / SALA / BARRA y Zona precargada; «Por Perfil» con COCINA / SALA / GERENCIA y Responsable
precargado; placeholders «(Escribe aquí tu tarea)» solo en la primera fila de cada sección.
2.4 **Cabeceras** (DOM-25/TEC-10): E4 «Hora Límite» → «Día» (semanales), «Cadencia» (mensuales),
«Antelación» (eventos); fila 2 de semanales «Semana del ___ al ___ · Responsable» y de mensuales
«Mes · Año · Responsable» (TEC-16/COM-23); verde también en la columna Hora/Día de las filas de tarea
y fuera de las cabeceras de sección (TEC-15).
2.5 **Se conecta con + jerarquía** (DOM-09/TEC-14/COM-20/DOM-23): bloque «Se conecta con» en las
Instrucciones de los 11 ficheros: 08 = checklist del LOCAL (marco), 01 = detalle por ÁREA, 09 =
CAJA; los bloques «CIERRE GENERAL» y «CIERRE DE CAJA» de 01!Cierre Sala se reducen a una línea
«→ ver 08 / 09»; las referencias a registros APPCC pasan a «si tienes el Pack APPCC, regístralo en
…; si no, anótalo en Notas».
2.6 **Autoría** (DOM-30/COM-13): línea de bio anclada en las Instrucciones de los 9 ficheros que no
la tienen, encima de la versión; versión «2.0 · agosto 2026». Añadir la comprobación al censo (campo
informativo `autoria`).
2.7 **Protección** (TEC-23): hojas protegidas sin contraseña con las celdas de entrada
desbloqueadas (como escandallos); Instrucciones lo dicen.
2.8 **Impresión** (TEC-24/COM-25): print_area en los dos BONUS; placeholder y verde en D23:D27 del
calendario.
2.9 **Temperaturas** (DOM-14): las tareas «Registrar temperatura …» llevan el objetivo en el texto
(«refrigeración 0-4 °C / congelación ≤ −18 °C») y «anota la lectura: ____ °C» (sin columna nueva).

## 3. CONTENIDO del kit base (`contenido_kit_tareas.py`, sustituciones 1:1 y filas nuevas)
- 01 Apertura Cocina: bloque «HIGIENE PERSONAL» al inicio (uniforme y calzado, pelo, joyas, uñas,
  heridas cubiertas, síntomas) (DOM-12); orden seguro: campana → comprobar gas → encender equipos
  (DOM-13); B6 → «Comprobar que las cámaras han funcionado toda la noche y registrar temperatura…»
  (DOM-24); calefactores «si la terraza opera en temporada fría» (COM-26).
- 02 Fríos / Mise en Place: tarea de **anisakis** («Pescado para consumo crudo o semicrudo: confirmar
  congelación previa ≥24 h a −20 °C (o −35 °C 15 h) y anotarlo») (DOM-02, alta); lechugas: «lejía apta
  para uso alimentario según dosis (≈70 ppm, 5 min) y ACLARAR con agua potable» (DOM-26); aceite de
  freidora «SOLO por debajo de 40 °C, nunca en caliente» (DOM-27); mermas: «Anotar mermas del día
  (producto, cantidad, motivo)» en cierre de cocina y en Calientes (DOM-18).
- 03 Manager: «Cerrar y validar el registro diario de jornada del equipo» (diario) y «Archivar los
  registros de jornada del mes» (mensual) (DOM-17); semanal por función («DÍA 1 — Planificación»…)
  + bloque corto de fin de semana (DOM-28).
- 05 Semanales/Mensuales: backflush del grupo de café y limpieza del lavavajillas en vez de
  «descalcificar» semanal (DOM-15); hoja nueva «Trimestral y Anual» (DDD por empresa autorizada,
  conductos de extracción, extintores/BIE, gas, legionela si aplica, seguro, revisión del TPV/Verifactu)
  con nº de parte y firma (DOM-16); vida útil de congelación por familia con tabla editable (DOM-29).
- 06 Eventos: bloque «AL CONFIRMAR LA RESERVA» (alérgenos e intolerancias por escrito, señal, precio
  por comensal, condiciones de cancelación) (DOM-19); Temporada Terraza en orden cronológico
  (TEC-17); Navidad «2-3 SEMANAS ANTES» coherente con sus plazos (TEC-22).
- BONUS-02 Calendario: Día del Padre, comuniones (abr-jun), 15 de agosto, 1 de noviembre, puente
  6-8 de diciembre (DOM-20).

## 4. Producto (integración, sonnet)
- Landing `astro-site/src/data/productos/tareas/kit-tareas.ts`: «**9 plantillas + 2 bonus (11
  ficheros)**» en seo/schema/hero/grid/cta (DOM-08/COM-06/COM-09); tarjetas nuevas para 08 y 09
  (arqueo con recuento por denominaciones, registro mensual de caja); «~90 tareas» → «121 tareas»
  (COM-24; recontar tras la v2.0); «pre-rellenadas» matizado (COM-10); comparación con Trail → genérica
  y verificable («los SaaS de checklists cobran suscripción mensual por local») (COM-18); **NO tocar**
  `aggregateRating`/`reviews`/`priceOld`/`discountBadge` (COM-02/03 aparcados).
- Emails `verify-purchase.ts`/`resend-access.ts` y `productos-digitales-config.ts`: «9 checklists +
  2 bonus (11 ficheros)» (COM-07). Dashboard: «Tus 11 plantillas» / «9 Checklists + 2 Bonus» (COM-08).
- Changelog 2.0, `updateNote` 2.0, gemelos SPA si existen.

## 5. Hermanos (después de la v2.0 del representante; sonnet + motor)
`main.py --producto <hermano> --dry-run` aplica SOLO el motor (§1-§2) a cafetería, pizzería,
hamburguesería, dark-kitchen, bar (▸ completos) y a los 08/09 de catering, chocolatería, heladería,
hotel, restaurante-creativo. Un agente sonnet por hermano verifica cada hallazgo MOTOR de la R1
contra el fichero regenerado, y revisa los hallazgos de CONTENIDO equivalentes (anisakis en kits con
pescado crudo; gas; aceite; descalcificar; jornada; calendario) anotando lo que encaje para una
mini-ronda. Gates por hermano: censo `--fail`, data_only, pycel del arqueo (fondo 150 €, ventas
1.000 €, Z 1.000 € → descuadre 0), idempotencia.

## 6. Demostraciones exigibles en la refutación
Arqueo: fondo 150, efectivo contado 1.150, tarjetas 800, Z 1.800 → descuadre 0; con Z 1.790 → +10 y
CF ámbar. Contador: 25 tareas, 3 N/A, 22 ✓ → «22 de 22». 07: 8 tareas escritas → «x de 8». 08:
ninguna tarea sin Responsable/Hora. DV de los 11 ficheros = «✓,—,N/A». Bio en 11/11 Instrucciones.
Hojas protegidas con entradas desbloqueadas. 0 menciones a «Trail» con precio en la landing.

## 7. Descartado con motivo
COM-02/COM-03 (reseñas, ancla): aparcado por John. Columna «Valor» para temperaturas: se resuelve en
el texto (§2.9). Regenerar 08/09 con otro generador desde cero: no, se unifican por post-proceso.
