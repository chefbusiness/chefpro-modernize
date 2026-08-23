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

---

## 8. Ronda 2 de refutación (2026-08-23) — reglas que CAMBIAN respecto a lo de arriba

61 hallazgos (DOM 30 · TEC 15 · COM 16) sobre la v2.0 construida en copia. 60 corregidos, 1
descartado. Lo que sigue **sustituye** a lo escrito antes en esta misma SPEC; el motor ya lo
implementa y la tanda de hermanos (§5) hereda estas reglas, no las originales.

- **§2.1 — el contador ya NO descuenta «—».** Sólo sale del denominador `N/A` («no aplica en
  este local»). «—» = no hecha: cuenta como pendiente y baja el porcentaje. Con la regla vieja,
  el turno que se saltaba tareas las marcaba «—» y la hoja que el kit manda archivar como prueba
  imprimía 100 % (DOM-R2-02). Numerador con `COUNTIFS` que exige texto en «Tarea»: un ✓ en una
  fila libre vacía daba «32 de 30» (TEC-R2-09).
- **§2.3 — el 07 no lleva placeholders en la columna «Tarea».** El aviso «escribe aquí abajo tus
  tareas de …» va en la BANDA de sección. Como valor de celda lo contaba el `COUNTIF` y la
  plantilla en blanco se entregaba marcando «0 de 3» (DOM-R2-03/TEC-R2-10/COM-R2-15). Ojo si se
  prueba a restarlos por fórmula: `COUNTIF(...,"(Escribe aquí*")` **rompe pycel** (el paréntesis
  entra crudo en un `re.compile`) y el fichero se publicaría sin cache. La columna «Tarea» de las
  tres hojas va en verde (DOM-R2-15) y la fila 2 pierde el «Turno:» en «Por Área» y «Por Perfil»
  (COM-R2-14).
- **§2.5 — la remisión va en la banda de sección, no en una fila numerada** (COM-R2-07), y
  alcanza también al bloque **SISTEMAS** de la apertura, que duplicaba 08 y 09 con tres horas
  distintas para el mismo TPV (DOM-R2-07). `colapsar_duplicados` NO corre sobre el fichero de
  negocio ni sobre el de caja: son el destino de la remisión.
- **§2.4 — cabecera «Cuándo»** cuando la columna mezcla horas con hitos («Cierre», «Servicio»,
  «Si aplica»): impreso, «Hora Límite: Si aplica» no dice nada (DOM-R2-24). Y se decide DESPUÉS
  de las precargas, o la 2.ª pasada lee lo que escribió la 1.ª y la idempotencia se cae.
- **§2.7 — se protegen también las hojas de los dos BONUS** (TEC-R2-14). Las de «Instrucciones»
  no, a propósito. El changelog dice «los 9 checklists», no «las 11 plantillas» (COM-R2-05).
- **§1.2 — el Registro Mensual descuenta el fondo.** La columna pasa a llamarse «Efectivo
  Contado» (el recuento del cajón TAL CUAL) y `Total Facturado = SUM(efectivo:otros) − fondo`.
  Antes el mismo libro calculaba el total de dos maneras incompatibles y el registro marcaba
  +fondo en ámbar todos los días (DOM-R2-01). El total de la columna «Descuadre» es
  `SUMIF(">0") − SUMIF("<0")`: un +50 y un −50 son 100 € de descuadre, no 0 (DOM-R2-26).
  **`fila_registro_mensual` detecta por PREFIJO**, o el renombrado dejaría la hoja fuera de
  alcance en la 2.ª pasada.
- **§1.1 — el Resumen de Cierre expone «Ventas en efectivo (contado − fondo)»**, que es la cifra
  que el registro pide (TEC-R2-11), y la tarea del fondo NO hardcodea la coordenada
  (DOM-R2-18/TEC-R2-04). Anchos de caja A=10 y C=20; alturas fijas en todo el bloque del dinero
  (TEC-R2-02/03/07). **§1.4 — las horas del 09 van DESPUÉS de la apertura del local** y
  escalonadas: 06:45 era antes de desactivar la alarma (DOM-R2-08).
- **§4 — el recuento real del kit son 491 tareas** (111 en el 01), leídas de los denominadores
  del propio Excel. `main.py` lo emite en el informe (`gates.recuento_tareas`) para que la landing
  no vuelva a divergir. El calendario trae **22** fechas, no 17.
- **§6 — la reseña con el precio de Trail se reescribió** en `kit-tareas.ts` y en su gemelo
  `KitTareas.tsx`: era un precio de competidor identificado, en boca de un cliente inventado y
  dentro del JSON-LD de `Product`. Lo aparcado por John era el sistema de reseñas y el
  `aggregateRating`, que no se han tocado.
- **Transversal:** temperaturas normalizadas a «−18 °C» (U+2212 + espacio) en todo el corpus
  (DOM-R2-22) — cualquier ancla de texto con grados en el módulo de contenido tiene que pasar por
  `motor.texto_grados` o no encontrará nada. Son DOS patrones, no uno: `RX_MENOS` sólo ve el signo
  pegado a la unidad, así que en un rango que comparte «°C» al final («pasar de -18 a −12 °C»,
  «(-2 a 0 °C)») el primer signo se quedaba en guion ASCII junto a un hermano ya tipográfico —lo
  cubre `RX_MENOS_RANGO`, que mira a través del conector («a», «y», «hasta», «hacia»)—. Ninguno
  toca el guion de «0-4 °C», que va precedido de dígito; las referencias al Pack APPCC ya no mandan anotar «en
  Notas», columna que sólo existe en 08 y 09 (DOM-R2-09); pie unificado por patrón, no por
  literal (DOM-R2-21); filas libres con la columna «Nº» también en verde (DOM-R2-23 — numerarlas
  haría que `geometria` las contase como tareas y cada pasada añadiría 5 más).

**Descartado:** DOM-R2-04 («las hojas van con `insertRows=False` y Excel no deja insertar filas»).
Es una lectura invertida del booleano de openpyxl: `ws.protection.insertRows = False` serializa
`insertRows="0"` y en OOXML **0 = NO bloqueado**. Verificado en el XML de la copia del dry-run
(`<sheetProtection … insertRows="0" deleteRows="0" …>`), y coincide con lo que midió la lente
TEC-R2-14. Las Instrucciones dicen la verdad.

---

## 9. Tandas 3, 4 y 5 (2026-08-23) — reglas que CAMBIAN o AMPLÍAN lo anterior

Mismo estatuto que el §8: **lo que sigue sustituye a lo escrito más arriba**, el motor ya lo
implementa y la tanda de hermanos (§5) hereda estas reglas, no las originales. Las decisiones se
citan con la letra o el código con que las firmó el orquestador, para que la próxima ronda no
vuelva a discutirlas.

### 9.1 Tanda 3 — el motor deja de suponer que todos los kits son el representante

- **(i) El 07 no se llama igual en todos los hermanos, y sus secciones son SUYAS.** `SINONIMOS_07`
  + `_Plantillas07` resuelven «Por Zona» ≡ «Por Área», «Por Franja» ≡ «Por Franja Horaria» y los
  plurales; `cfg_07` sólo impone el molde del representante (APERTURA/SERVICIO/CIERRE …) cuando la
  hoja no tiene nada que perder: o sus rótulos son el placeholder «(Sección N — Personaliza este
  título)» del generador v1.1, o ya son los canónicos. Bar entrega cuatro secciones escritas para un
  bar y su columna «Zona» precargada: se le aplica lo UNIVERSAL (subtítulo sin «Turno:» donde no hay
  turno, banda con el aviso de dónde se escribe, «Tarea» vacía y en verde) con SUS nombres. «Por
  Fase» y «Por Turno» quedan fuera a propósito: son del molde P4. Trampa de idempotencia:
  `RX_SEC_ROTULO` quita la cola que escribe el propio motor antes de leer el nombre de la sección, o
  cada pasada añadiría otra.
- **(j) La bio y la versión se exigen en TODO fichero con hoja «Instrucciones»,** esté o no en
  alcance del molde «▸». `normalizar_p4` llama siempre a `bio_en_instrucciones` y el gate
  `dv_y_bio` censa delante del `continue` de `en_alcance`. Es lo que alcanza a los BONUS-02 de
  catering y de hotel, que se publicaban diciendo «Versión 1.1 · agosto 2026» y sin autoría dentro
  de un producto v2.0. Sólo se escribe en celdas que YA existen (la línea de versión y la vacía de
  debajo): si no hay dónde anclar no se inventa nada y lo canta `version_desfasada` /
  `sin_hoja_instrucciones`.
- **(k) SIN ACCIÓN, decidido:** `kit-tareas-catering/07-plantilla-personalizable.xlsx` se queda sin
  contador. Sus tres hojas no son ni «▸» ni P4 (`geometria_p4` no encuentra fila libre sobre el
  pie), así que sólo reciben el desplegable y la bio.
- **(l) El contador del molde P4 se DEMUESTRA sobre la hoja tal y como se entrega.** `demo_p4` no
  toca el fichero: compara el contador contra un recuento hecho a mano y publica además lo que habría
  dicho la fórmula vieja. El molde P4 repite la fila de cabecera en cada sección, así que el
  `COUNTIF` original contaba los rótulos: heladería, `01-apertura-cierre.xlsx:'Apertura'!C29/E29`
  anunciaba «2 de 19» recién impresa con 17 tareas. `demo_07` se endurece en la misma tanda (exige
  `motor.geometria` además del título) o con los sinónimos de (i) se llevaría una hoja P4 y
  reventaría.

### 9.2 Tanda 4 — T-01 … T-08

- **T-01. El fichero que ES el marco no puede remitir a otro como marco.** `_bloque_conecta`
  contempla `fname == f_negocio` y `fname == f_caja` ANTES que ninguna otra rama de la cola. En
  producción, `08-apertura-cierre-negocio.xlsx:Instrucciones!B36` decía «08 … es el MARCO del día» y
  cuatro líneas más abajo `!B40` «el marco del día está en 01-apertura-cierre.xlsx»: dos
  afirmaciones opuestas en la misma hoja impresa. La rama genérica excluía `fname` de los candidatos
  pero nunca comprobaba si `fname` ERA el marco.
- **T-02. El TPV se enciende UNA vez por kit, y es en el fichero de negocio.** En el de caja la
  tarea pasa a «Comprobar que el TPV está encendido y abrir turno de caja» (`RX_TPV_CAJA` +
  `texto_tpv_caja` + `tpv_de_caja`, paso 0 de `aplicar`, sólo si `fname == CTX['f_caja']`). Es regla
  de FAMILIA, no de contenido. La HORA no se toca (la escribe `precargar_caja`, escalonada tras la
  apertura). El regex sólo pica cuando la tarea ENTERA es «encender el TPV»: la de pastelería y la
  de heladería 01 quedan intactas. **La trampa no era el regex, era la idempotencia:**
  `tareas_del_libro(wb, caja=True)` aplica la misma normalización al leer el marco en `contexto()`,
  o la 1.ª pasada compararía «Encender TPV / POS» y la 2.ª «Comprobar que el TPV…» y
  `anotar_duplicados` mediría distinto en cada una.
- **T-03. `gate_recuento` suma TODAS las hojas de checklist del producto,** molde «▸» y molde P4,
  leyendo el denominador cacheado. Antes sólo sumaba el molde «▸» y en los cinco kits P4 devolvía 56
  —las tareas de 08 y 09— ignorando los cientos de los 01-07: hotel habría anunciado 56 en vez de
  636. Publica `recuento_por_molde` y `por_hoja` (fichero:hoja:celda). Un denominador sin valor
  cacheado se ANOTA como aviso en vez de sumar 0 en silencio. **Desde la tanda 4,
  `gates.recuento_tareas.total` SÍ es la fuente para la landing** (los 11 recuentos cuadran al
  0,0 % contra recuentos manuales independientes): 491 kit-tareas · 500 cafetería · 373 pizzería ·
  346 hamburguesería · 331 dark-kitchen · 342 bar · 346 catering · 338 chocolatería · 298 heladería ·
  636 hotel · 477 restaurante-creativo.
- **T-04. Los paréntesis de «Se conecta con» salen de la ESTRUCTURA del kit,** no de un literal.
  `_zonas_del_fichero` (nombres reales de hoja del fichero de áreas: «Apertura Cocina» → «cocina»),
  `_bandas_del_fichero` (rótulos reales de las bandas del de negocio) y `parentesis()`, que devuelve
  cadena VACÍA si no hay nada que enumerar. Iban hardcodeados para los 12 kits y dark-kitchen
  imprimía «(accesos, luces, clima, terraza)» y «(cocina, sala, barra)» en sus 11 ficheros teniendo
  sólo «Apertura Cocina» y «Cierre Cocina». **Sin datos, sin paréntesis: se omite antes que
  inventar.**
- **T-05. `gates.bandas_solapadas` se deduplica antes de emitirse.** El duplicado venía de
  `procesar`, que vuelve a pasar el motor cuando el módulo de contenido cambia la estructura del
  libro. Si una misma banda apareciera con DOS medidas distintas se conservan las dos: eso no sería
  ruido del informe, sería el motor midiendo distinto en cada pasada. (Corregido en m2, abajo.)
- **T-06. SIN ACCIÓN, decidido:** los BONUS-01/02 de catering, hotel y chocolatería siguen sin
  protección, sin `print_area` y sin el pie del kit. Meterlos en el molde «▸» exigiría ampliar
  `fila_calendario` a su cabecera, que es justo lo que excluye el alcance «sólo 08/09» de esos kits.
- **T-07.** Documental (trazabilidad del fix de `contexto`): no toca código.
- **T-08. La promesa impresa era más fuerte que lo que el motor garantiza.** «No se duplican: cada
  uno cubre un nivel.» se sustituye por `FRASE_NIVELES`, que admite el solape deliberado, DENTRO de
  la misma viñeta «Orden de uso: …». Va en una sola viñeta a propósito: emitirla como línea nueva
  desplazaría una fila TODAS las Instrucciones y convertiría un cambio de 11 celdas en uno de ~200.
  Coste aceptado: esa fila pasa de 16 a 48 pt. **`UMBRAL_BANDA` se mantiene en 0,8**; el solape
  residual del 25-40 % (cafetería, pizzería) es una decisión de umbral abierta, no un defecto.

### 9.3 Tanda 5 — firmas del orquestador sobre el diff del representante

Las tres se firman contra `auditorias/kit-tareas-hermanos/kit-tareas-diff-firmado.json`, que es
**el diff de referencia** (177 diferencias) y sustituye al recuento de 127 de `motor-2.3.json`.

- **(d) FIRMADO.** El paréntesis del fichero de negocio se deriva de sus bandas reales y, si no se
  puede, se OMITE (nunca una «terraza» inventada). En el representante queda SIN paréntesis: 11
  celdas, `01!B35 · 02!B29 · 03!B34 · 04!B28 · 05!B34 · 06!B28 · 07!B41 · 08!B36 · 09!B46 ·
  BONUS-01!B12 · BONUS-02!B12`. Motivo: los 08/18/10 de los 11 kits se entregan como listas PLANAS,
  sin una sola banda de sección. La otra fuente posible —la columna «Zona»— es la misma en los 11
  kits (sale del generador v1.1) y seguiría diciendo «Terraza» en una dark kitchen.
- **(e) FIRMADO.** La cola «Estás en …» del fichero de CAJA es la específica de caja
  (`09-apertura-cierre-caja.xlsx:Instrucciones!B50` en el representante): «esta es la CAJA — el
  DINERO del día (fondo, recuento, Z del TPV y descuadre); el marco del día está en 08 … y el
  detalle por zona, en 01 …». La rama `elif caja and fname == caja` de `_bloque_conecta` se queda.
- **(f) ACEPTADO.** El calendario del representante desbloquea `A5:D27` — 23 filas, 92 celdas, no
  las 22 filas / 88 celdas que se habían comunicado. La fila 27 está VACÍA (es la última libre del
  molde), así que el efecto es inocuo; lo que se firma es el ALCANCE. Sale de que `calendario()`
  devuelve el cuerpo hasta la última fila libre y `proteger` desbloquea ese rango entero.
- **(c) ACEPTADO.** Las 26 alturas de fila que cambian son consecuencia mecánica de (d), T-08, T-01
  y (e): 22 en las 11 Instrucciones (la línea del negocio baja de 32 a 16 pt al perder el paréntesis
  y la de T-08 sube de 16 a 48 pt), 2 en las colas «Estás en …» de 08 y 09, y 2 en
  `09:'Apertura de Caja'!9` y `09:'Cierre de Caja'!10`, que pasan de 24 pt FIJOS a `None` porque
  `autoalto` (TEC-R2-13) ve que el texto nuevo no cabe en una línea.
- **BAR 07 «Zona» vacía en verde: ACEPTADO** (decisión heredada de motor-2.2, ya sin abrir).
- **T-06: sin acción**, reconfirmado.

### 9.4 Motor 2.4 — m1, m2, m3

- **m1. `FRASE_NIVELES` enumera SÓLO los niveles que el kit tiene.** La frase de T-08 nombra tres
  ficheros («…el de áreas detalla CÓMO se hace en cada zona…») y en los cinco kits del molde P4 no
  hay fichero de ÁREAS: la misma viñeta abría «Orden de uso: local → caja» (dos pasos) y seguía
  enumerando tres. Se condiciona a `CTX['f_areas']` con `frase_niveles()` /
  `FRASE_NIVELES_SIN_AREAS`: «Cada fichero cubre un nivel: el de negocio marca el HITO (encender,
  abrir, cerrar) y el de caja lleva el DINERO. Si una tarea aparece en los dos, es a propósito: una
  es el hito y la otra el detalle.» Afecta a 10 celdas: catering `08!B37`/`09!B48`, chocolatería
  `08!B37`/`09!B48`, heladería `08!B37`/`09!B48`, hotel `18!B37`/`19!B48`, restaurante-creativo
  `10!B37`/`11!B48`. **Ojo:** `critico-3.json` citaba las de catering como `08!B38`/`09!B49`, que es
  la fila SIGUIENTE (la cola «Estás en …»); las medidas en el dry-run son B37 y B48. Es la misma
  clase de defecto que T-01: una rama que no comprueba el caso que la contradice.
- **m2. La deduplicación de T-05 ya no incluye el nº de fila.** La clave llevaba la referencia de
  celda («Cierre Cocina!A28») y el módulo de contenido que inserta una fila por encima de la banda
  la mueve: la 2.ª pasada del motor medía la MISMA banda en A29 y las dos entradas sobrevivían
  (dark-kitchen, «PREPARACIÓN MAÑANA», tareas=4, casadas=1, ratio=0,25). La clave pasa a ser
  **(hoja SIN nº de fila, banda, tareas, casadas, ratio)** y se conserva la ÚLTIMA medida, que es la
  tomada sobre la geometría FINAL del libro: quedarse con la primera citaría una fila en la que ya
  no está la banda. `destinos` y `anotada` no entran en la clave pero sí se vigilan: si dos
  mediciones discrepasen en ellos se publican las dos (criterio de T-05).
- **m3. `main.digest` compara el MENSAJE de las validaciones y el bloqueo de TODAS las celdas.**
  Eran dos puntos ciegos que hacían que el diff saliera corto: la huella de DV era
  `type:formula1:sqref` —así que el cambio de `DV_ERROR` en 33 hojas no aparecía y hubo que
  verificarlo aparte— y `locked` sólo se miraba en las celdas CON valor, así que las 4 celdas vacías
  de la fila 27 del calendario no se contaban. Ahora la DV incluye `errorTitle`, `error` y `prompt`,
  `locked` es un mapa aparte de todas las celdas del rango usado, y `diff_digest` desglosa
  `alturas` y `locked` elemento a elemento (antes daban UNA línea por hoja recortada a 300
  caracteres, imposible de contar). Con esto el diff del representante da **177 = 26 valor + 33 DV +
  26 alturas + 92 locked**, exactamente lo que había contado por su cuenta el verificador, y el
  digest vuelve a ser utilizable como prueba de «no cambia nada más».

### 9.5 Pendiente documentado — «caja» pedida FUERA del fichero 09

Mismo patrón que T-02 resolvió para el TPV, pero sin criterio único todavía: hay tareas que mandan
hacer caja en ficheros que no son el de caja, sin remisión. Censadas: hamburguesería
`01:'Apertura Sala'!B11-B12` y `'Cierre Sala'!B12` + `04:'Encargado'!B10/B17`; pizzería
`01:'Apertura Sala'!B11-B12`; restaurante-creativo `01:'Cierre PM'!B25` («Cierre de caja y registro
de ventas del día», que describe el fichero 11 entero); heladería `01:'Apertura'!B36` («Encender TPV
/ caja registradora y verificar fondo de caja», que `gates.tpv_duplicado` ya etiqueta como «otro
fichero: se deja»). `colapsar_duplicados` no cruza 01/04 contra el fichero de caja. **NO bloquea la
tanda 5** por decisión del orquestador; queda aquí para que la próxima ronda fije UN criterio
(reescritura de texto con remisión, como en T-02) en vez de arrastrar cuatro severidades distintas.

---

## 10. Motor 2.5 (2026-08-23) — m5, m6, m7 y el 09 de catering

Mismo estatuto que §8 y §9: **lo que sigue sustituye a lo escrito más arriba**, el motor ya lo
implementa y la tanda de hermanos (§5) hereda estas reglas. Lo firma el orquestador sobre
`auditorias/kit-tareas-hermanos/motor-2.5.json`.

### 10.1 m5 — la metadata se fija en TODOS los ficheros, no sólo en los del molde «▸»

`set_metadata` vivía **dentro de `motor.cerrar`**, que sale antes de llamarlo cuando `estado` es
`None` — es decir, en todo fichero fuera del molde «▸». Resultado: los ficheros del molde P4 y los
dos BONUS de los cinco kits con alcance «sólo 08/09» se **guardaban** (reciben desplegable,
contador honesto, CF, bio y versión 2.0 desde `normalizar_p4`) pero conservaban `subject`
«… · **v1.1**». El cliente abría un producto v2.0 y las propiedades de la mayoría de sus ficheros
decían otra versión.

- Ahora lo llama **`main.procesar`**, para todos los ficheros, **después** de `cerrar` (el título
  sale de la hoja «Instrucciones», que `cerrar` reescribe) y **antes** de calcular `guardado`, para
  que un fichero cuyo único cambio sea la metadata también se guarde.
- `subject` = `«<sufijo> · v2.0»`, escritura ABSOLUTA. El sufijo sale de `CTX['sufijo']`, que
  `contexto()` deriva del propio `title` de los ficheros — no hay literal por kit.
- `creator` y `lastModifiedBy` = «AI Chef Pro».
- `title` se recompone **sólo si no está ya en la forma canónica «<nombre> · <sufijo>»** (COM-27:
  había títulos genéricos «Kit de Tareas — …»). Reescribirlo siempre no aporta nada y pondría en
  riesgo los 11 títulos del representante, que la regresión exige byte a byte. Medido: de los 221
  ficheros de las 19 carpetas `kit-tareas*` de `dl/`, **0** tienen el título fuera de la forma
  canónica, así que esa rama es una red de seguridad, no un cambio.
- **`keywords` se escribe SÓLO si falta o si no sigue la convención «…, AI Chef Pro»**
  (`motor.keywords_ok`), y el valor por defecto se DERIVA del identificador del producto
  (`kit-tareas-heladeria` → «kit tareas heladeria, AI Chef Pro»), que es exactamente lo que ya hay
  en 206 de esos 221 ficheros. La escritura absoluta era la tentación obvia y habría **borrado
  metadatos buenos**: los 15 ficheros de `kit-tareas-pasteleria` llevan «pastelería, obrador,
  checklist, tareas, AI Chef Pro», escrito a mano y más rico que nada derivable del identificador.
  El gate lo publica como AVISO (`gates.metadata.keywords_propias`), nunca como fallo.
- Gate nuevo: **`gates.metadata`** (`main.gate_metadata`), que censa `subject`/`title`/`creator`/
  `keywords` de TODOS los ficheros del producto y entra en `fallos`. Sin él m5 no sería auditable:
  el defecto vivió cuatro tandas precisamente porque ningún gate miraba las propiedades de los
  ficheros fuera del molde «▸» — el censo mira las hojas.
- **`main.digest` incluye ahora las propiedades** bajo la pseudo-hoja `·propiedades·`
  (`title`, `subject`, `creator`, `keywords`, `category`, `description`; `lastModifiedBy`,
  `created` y `modified` fuera, que cambian en cada guardado). Sin esto, un cambio que es SÓLO de
  metadata salía con «0 diferencias» y ni la idempotencia ni el diff contra producción podían
  demostrarlo. El diff del representante sigue en 0: sus propiedades no cambian.

**Alcance real, medido el 2026-08-23** (y corrige la cifra de «26 xlsx» del encargo): en los cinco
kits con alcance «sólo 08/09» son **55** ficheros con `subject` v1.1 — hotel 17, restaurante-creativo
11, catering 9, chocolatería 9, heladería 9. Los otros 90 que aparecen en un censo de todo `dl/`
(asador, chef-privado, food-truck, marisquería, panadería, pastelería, sushi-bar, tapas-bar) **no
son de esta familia**: nunca han pasado por este motor y m5 no los toca mientras nadie corra
`main.py --producto` sobre ellos.

### 10.2 m6 — MODELO DE CAJA POR EVENTOS (el 09 de catering)

Diseño firmado por John: una empresa de catering **no tiene mostrador**. Factura por EVENTO y cobra
mayoritariamente por transferencia (anticipo del 30-50 % + saldo), así que modelar su 09 como un
arqueo de cajón —fondo, cambio, Z del TPV por turno— describe un negocio que no es el suyo.
`09-apertura-cierre-caja.xlsx` se sustituye por **`09-cobros-facturacion-eventos.xlsx`**, «Cobros y
Facturación por Evento — Catering / Eventos» (el `git mv` y el redirect los hace el ORQUESTADOR).

**El modelo se detecta por CABECERA, como todo lo demás.** `CTX['modelo_caja']` vale `'mostrador'`
(los 10 kits con arqueo) o `'eventos'`, y lo decide `contexto()` a partir de dos firmas nuevas:
`fila_liquidacion` (la pareja de rótulos «TOTAL FACTURA» + «PENDIENTE DE COBRO», que sólo aparece
junta en la hoja de liquidación) y `fila_registro_eventos` (cabecera por PREFIJO, como el registro
mensual). `papel_del_fichero` devuelve `'cobros'`.

> **Trampa cazada en el dry-run:** el 09 de eventos lleva una sección OPCIONAL «Solo si hubo barra
> con cobro en efectivo» con la **misma tabla «Denominación | Cantidad»** del modelo de mostrador.
> Con el orden de comprobación natural (`recuento` antes que `liquidacion`), `fila_recuento` la
> encontraba y el fichero se llevaba el papel **'caja'**: `precargar_caja` le habría escrito
> «Responsable de caja» y horas de reloj encima de los responsables y de los D-15/D+7,
> `instrucciones_caja` le habría puesto un manual de arqueo de cuatro hojas y §6 habría intentado
> demostrar un descuadre que ese fichero no calcula. **La firma de EVENTOS se mira primero**: es
> específica, mientras que la del recuento la comparten los dos modelos.

El fichero del dinero **sigue ocupando la ranura `CTX['f_caja']`**, sea de mostrador o de eventos:
así las referencias que ya existen (el bloque «Se conecta con», `colapsar_duplicados`, `aplicar`,
los gates) siguen apuntando al mismo sitio y lo que cambia es el VOCABULARIO, no la topología del
kit. Un kit con los DOS modelos a la vez aborta con `KitAmbiguo`.

Qué cambia con `modelo_caja == 'eventos'`:

| Pieza | Mostrador | Eventos |
|---|---|---|
| `tpv_de_caja` (T-02) | se aplica | **no** — ese fichero no abre ningún turno de TPV |
| `texto_facturado` (DOM-01) | se aplica | **no** — reescribe una cuenta de arqueo que aquí no existe (`forma_estable(..., facturado=False)`) |
| `caja_columnas` · `registro_mensual` · `precargar_caja` · `moneda_002` · `recuento` · `fondo_de_caja` · `resumen_cierre` | se aplican | **no** (`es_mostrador`) |
| Instrucciones propias | `instrucciones_caja` | **`instrucciones_cobros`** |
| Línea de «Se conecta con» | «la CAJA: fondo, recuento por denominaciones, Z del TPV y descuadre» | «**la FACTURACIÓN: anticipos, liquidación y cobro de cada evento**» |
| Orden de uso | «local → caja» | «**local → eventos**» |
| Cola «Estás en …» (e) | «esta es la CAJA — el DINERO del día …» | «esta es la FACTURACIÓN — el DINERO de cada evento (anticipo, liquidación, factura y saldo pendiente)» |
| `FRASE_NIVELES` (T-08/m1) | «…el de caja lleva el DINERO» | `FRASE_NIVELES_EVENTOS` / `…_AREAS` |
| `COLAPSO` (§2.5) | «fondo, recuento…» | `COLAPSO_EVENTOS` |
| `instrucciones_negocio` | sin línea de dinero | añade «El DINERO no está aquí: … van en 09-…» |
| §6 | `demo_arqueo` (cuadra / descuadra) | **`demo_liquidacion`** (`liquidacion-cuadra` / `liquidacion-vencida`) |
| `gates.tpv_duplicado` | «caja (T-02 NO aplicado: revisar)» | «cobros (modelo por eventos: T-02 no aplica)» — no se le exige nada |

`hojas_reconocidas` gana dos tipos, **`liquidacion`** y **`registro_eventos`**, y `cerrar` los trata
como hojas de datos: A4, `print_area`, pie del kit y **protección** (sus celdas verdes quedan
desbloqueadas; las fórmulas del IVA, el total, el saldo, el pendiente y el ESTADO, bloqueadas). Sin
esto se habrían publicado como las dos únicas hojas sueltas de un producto v2.0.

**§6 en el modelo por eventos** — `demo_liquidacion` localiza las celdas **por su rótulo** (nunca
por coordenada) y demuestra con pycel: base 10 % = 8.000 € y base 21 % = 2.000 € → TOTAL FACTURA
11.220 €; anticipo 4.000 € → saldo 7.220 €. Caso **`liquidacion-cuadra`**: se cobra el saldo →
PENDIENTE 0 y ESTADO «Cobrado». Caso **`liquidacion-vencida`**: no se cobra nada y el vencimiento ya
pasó → PENDIENTE 7.220 € y ESTADO «VENCIDO». El contador honesto se sigue demostrando, ahora sobre
«Antes del Evento» / la apertura del 08.

### 10.3 El fichero: «Cobros y Facturación por Evento — Catering / Eventos»

Cinco hojas. Constructor esbozado en `kit-tareas-v2_0/construir_09_catering.py`
(`construir(ruta_destino, ctx)`).

1. **Instrucciones** — la reconstruye `motor.reescribir_instrucciones` desde
   `motor.instrucciones_cobros()`. El constructor sólo deja la hoja creada con su línea de versión,
   que es donde se ancla la bio (§2.6).
2. **Antes del Evento** — molde «▸» (`# · Tarea · Responsable · Cuándo · ✓ Completada · Firma`), 12
   tareas precargadas + las 5 filas libres que mete el motor + contador honesto. La columna se llama
   **«Cuándo»** y va en días ANTES del evento (**D-15, D-7, D-3, D-1**), no en horas: es lo que
   `motor.cadencia` decidiría de todos modos (DOM-R2-24), escrito ya bien para que la 1.ª pasada no
   tenga nada que corregir. Contenido: presupuesto firmado por escrito · comensales y fecha límite de
   cambios · anticipo (30-50 %) cobrado y registrado con fecha y medio · forma de pago del saldo y
   plazo · datos de facturación (razón social, CIF/NIF, dirección, email) · facturas anteriores
   pendientes del cliente · condiciones de cancelación y modificación por escrito · proveedores
   externos (carpa, sonido, menaje) con pedido y anticipo propios · escandallo del evento y margen ·
   seguro de RC del evento y del recinto · alérgenos e intolerancias por escrito · y **sólo si habrá
   barra con cobro en efectivo**, el fondo de caja.
3. **Después del Evento** — mismo molde, «Cuándo» en **D+0, D+1, D+7, D+30**: comensales reales vs
   contratados · extras (horas extra, bebidas, suplementos, roturas) · arqueo de la barra si la hubo ·
   cargos por roturas comunicados · factura con desglose de IVA · saldo comunicado con vencimiento ·
   liquidación volcada al registro · cobro del saldo registrado · conciliación bancaria · reseña ·
   expediente archivado · saldos VENCIDOS reclamados.
4. **Liquidación del Evento** — formulario, importes en la columna C **en verde** lo editable:
   evento/cliente, fecha, comensales contratados y reales; presupuesto aceptado (base, sin IVA);
   extras (base); **base imponible al 10 %** y **al 21 %** (dos celdas verdes que reparte el usuario,
   con un aviso por fórmula si su suma ≠ presupuesto + extras); IVA 10 % e IVA 21 % (fórmula); TOTAL
   FACTURA; anticipo cobrado (−); saldo tras anticipo; cobrado tras el evento; **PENDIENTE DE COBRO**
   (fórmula, ámbar por CF si > 0,01 €); fecha de vencimiento del saldo; y **ESTADO** («Cobrado» si el
   pendiente ≤ 0,01 € · «VENCIDO» si queda pendiente y hoy > vencimiento · si no «Pendiente»).
   Debajo, la sección **opcional** «Solo si hubo barra con cobro en EFECTIVO»: recuento por
   denominaciones (500 € … 0,01 €, con la de 0,02 € que DOM-03 echó en falta), TOTAL EFECTIVO, fondo
   (−) y efectivo neto. **No se enlaza automáticamente** a «Cobrado tras el evento» —lo explica
   Instrucciones—: en la mayoría de los eventos no hay barra en efectivo y una fórmula fija dejaría
   un 0 restando donde no debe.
   El reparto 10/21 % es del cliente y de su asesor (10 % en alimentos y bebidas no alcohólicas del
   servicio de catering, 21 % en alquileres, decoración, servicios y bebidas alcohólicas), así que el
   aviso **informa, no bloquea**: una validación dura le impediría guardar un evento 100 % al 21 %.
5. **Registro de Eventos** — una fila por evento (25 + TOTALES): Fecha · Evento / Cliente ·
   Comensales · Base (presupuesto + extras) · Total factura · Anticipo · Cobrado · Pendiente ·
   Medio de pago · Vencimiento · Estado, con las mismas fórmulas de pendiente y estado y CF ámbar en
   «Pendiente». Bajo TOTALES, el recuento de eventos PENDIENTES y VENCIDOS.

**Vocabulario:** catering/eventos. «Caja», «turno de caja» y «Z del TPV» aparecen únicamente en la
sección opcional de la barra en efectivo, que es la única parte del fichero donde hay un cajón.

**Contrato de rótulos:** `ETIQ_EV_*`, `CAB_EVENTOS`, `EV_COBRADO/EV_PENDIENTE/EV_VENCIDO` y
`EV_TOLERANCIA` viven en **`motor.py`**, no en el constructor, porque son lo que usan a la vez la
detección por cabecera y la demostración §6. Cambiar un rótulo en el constructor y no en el motor
deja el fichero sin papel, `CTX['f_caja']` a `None` y los 11 ficheros del kit sin la línea del dinero
en sus Instrucciones, sin que ningún gate lo cante.

### 10.4 m7 — `--producto kit-tareas-catering` sigue funcionando con 11 ficheros

Verificado en dry-run con el 09 nuevo: **exit 0**, 11 ficheros, idempotencia 0, censo `--fail` 0
defectos, §6 4/4 (`liquidacion-cuadra` · `liquidacion-vencida` · `contador-honesto` ·
`contador-p4-sin-rotulos`), DV 0 incorrectas, bio y versión 2.0 en 11/11, metadata 0 incoherencias,
recuento 347 tareas (▸ 57 + P4 290; eran 346 con el 09 viejo: el de eventos entrega **24** tareas
frente a 23).

**`main.py --origen <carpeta>`** (sólo con `--dry-run`) permite probar el motor contra un producto
que todavía no está en `dl/`, que es como se ha verificado esto sin tocar `astro-site/public/dl/**`.

### 10.5 Pendiente de firma del orquestador

- El **«IVA medio aplicado»** de «Registro de Eventos» (celda verde, 10 % por defecto) es una
  decisión del esbozo: el diseño pide «Total factura (fórmula con IVA medio o introducido)». La
  alternativa es que «Total factura» sea celda verde y se copie de la liquidación — pero un total
  tecleado a mano es justo lo que hace que las dos hojas dejen de cuadrar.
- Los **textos de las 24 tareas** del constructor son los del brief, sin pasar por revisión de
  redacción. Los pule el agente que construya el 09 definitivo.
- La línea nueva de `instrucciones_negocio` («El DINERO no está aquí…») **desplaza una fila** las
  Instrucciones del 08 de catering: 77 de las 88 diferencias contra producción de ese kit son eso.
- §9.5 (**«caja» pedida FUERA del fichero 09**) sigue abierto y no lo toca esta tanda.

## 11. Motor 2.6 (2026-08-23) — m8: el 09 de catering deja de ser un esbozo

Sustituye a lo que §10.3 y §10.5 daban por pendiente. `construir_09_catering.py` es ya el
constructor definitivo y `main.py` lo llama solo: **`--origen` deja de ser necesario** para probar
el kit de catering.

### 11.1 El paso vive en `main.py`, no en el orquestador

`main.sustituir_09_catering(carpeta, pid)` corre **antes** de `ficheros_de` y de `motor.contexto`
(que es quien lee la carpeta para decidir `modelo_caja`), sobre la copia de trabajo:

1. **Construye siempre** `09-cobros-facturacion-eventos.xlsx`, esté o no ya ese nombre en la
   carpeta. Aquí está la sutileza que hace que el paso funcione en los dos estados del repositorio:
   **`git mv` sólo RENOMBRA**. Un fichero que ya se llame `09-cobros-facturacion-eventos.xlsx`
   puede seguir siendo por dentro el arqueo de cajón de la v1.1, y saltarse la construcción
   «porque el nombre nuevo ya está» publicaría el kit con el nombre bueno y el fichero viejo
   dentro — con `papel_del_fichero` devolviendo `'caja'` y todo el vocabulario de mostrador
   detrás.
2. **Borra** `09-apertura-cierre-caja.xlsx` de la copia si sigue ahí.

Verificado con las DOS entradas (carpeta con el 09 viejo · carpeta ya renombrada a mano
simulando el `git mv`): **0 diferencias entre los dos resultados**, medidas con `main.digest` /
`main.diff_digest` sobre los 11 ficheros. El informe publica `sustitucion_09_catering` para que se
pueda distinguir una pasada de la otra.

El `git mv` del entregable en `astro-site/public/dl/` y el 301 lo siguen haciendo el orquestador y
`_redirects`; ningún script de este paquete toca `git`.

### 11.2 m8 — DEFECTO CAZADO: `aplicar` borraba el formato condicional del modelo por eventos

`aplicar` vacía `ws.conditional_formatting` de **todas** las hojas reconocidas para ser idempotente
(«DV y CF se vacían y se reconstruyen enteros»), pero sólo lo reconstruía para los checklists y
para el arqueo de mostrador. Las dos hojas nuevas —`liquidacion` y `registro_eventos`— entraban en
el vaciado y no salían de ninguna reconstrucción: **el ámbar del PENDIENTE y el rojo del VENCIDO
existían en el fichero recién construido y desaparecían en la primera pasada del motor**, con el
dry-run en verde, la idempotencia en 0 y el censo en 0 defectos. Medido el 2026-08-23:
`conditional_formatting` de «Liquidación del Evento» = `[]` después del motor.

Es el mismo patrón que la caché del frontmatter del blog: el cambio *parece* aplicado porque el
resto de la hoja sí lo está, y ningún gate mira esa propiedad.

Arreglo: **`motor.cf_eventos(ws, tipo)`**, con `ROJO`/`ROJO_TXT`, llamada al final de `aplicar`
para los dos tipos. Vive en `motor.py` por el mismo motivo que los `ETIQ_EV_*`: es una regla que
comparten el constructor y el motor, y dejarla sólo en el constructor es exactamente lo que
produjo el defecto. Localiza las celdas por RÓTULO (nunca por coordenada) y delimita el cuerpo del
registro por la fila `TOTALES`. El constructor la llama también, para que un fichero generado
suelto ya salga completo. Comprobado tras el motor: 4 reglas vivas —`C22` ámbar, `C24` rojo,
`H6:H30` ámbar y `A6:K30` rojo por `$K6="VENCIDO"`— más las dos de fila completada de los
checklists.

### 11.3 Lo que el constructor copia y lo que no

La paleta NO se inventa: sale de medir `dl/kit-tareas-catering/08-apertura-cierre-negocio.xlsx` y
el propio `09-apertura-cierre-caja.xlsx`. Título blanco 16 sobre `1A1A1A` combinado en toda la
fila · banda dorada `FFD700` en la fila 2 · separador de 8 px en la 3 · cabecera `2D2D2D` blanca en
la 4 · zebrado `F5F5F5`/blanco en las columnas fijas · `E8F5E9` en todo lo editable · borde `thin`
`E0E0E0` · Calibri · alturas 40/28/8/28/24 · `freeze_panes` en la primera fila de datos · fila de
firma dorada y pie gris de 9 pt. El esbozo usaba `2E3B4E` y `Nº`: ninguna de las dos cosas existe
en esta familia, y `Nº` además deja la hoja fuera de `cabecera_checklist`.

Dos invariantes que **`main.demo_liquidacion` da por ciertas** y que no se pueden mover sin tocar
la demo en el mismo commit: el rótulo va en la columna **A o B** (`motor._buscar` sólo mira esas
dos) y el importe en la **C** (la demo escribe `column=3`).

### 11.4 Decisiones que el esbozo dejaba abiertas, ya tomadas

- **«IVA medio aplicado»** se queda como celda verde (10 % por defecto) con «Total factura» por
  FÓRMULA, como pedía §10.5: un total tecleado a mano es lo que hace que las dos hojas dejen de
  cuadrar. La nota de la propia hoja remite a «Liquidación del Evento» para el desglose exacto.
- **El aviso de las bases calla con la hoja en blanco** (`IF(suma=0,"",…)`). Con la comprobación
  desnuda, un fichero recién abierto felicitaba por un cuadre de ceros.
- **El ESTADO calla mientras no haya factura** (`IF(TOTAL<=0,"",…)`). Sin eso, una liquidación
  vacía se anunciaba como «Cobrado». Es también lo que deja 27 fórmulas sin caché en el 09 (las 25
  del registro vacío más estas dos), todas devolviendo `""` **por diseño** y con `fallos_pycel=0`.
- **La columna «Medio de pago» del registro NO lleva desplegable.** El gate `dv_y_bio` censa las
  listas de todo el producto y avisa si hay más de una (`aviso_dv_mezcladas`): un segundo
  desplegable metería ruido permanente en el gate a cambio de nada.
- **Los textos de las 24 tareas** están redactados para el cliente final (§10.5 los dejaba sin
  revisar).

### 11.5 Pendiente para el orquestador

- **`_bloques_contador` dice «no aplica en tu local»** — texto de FAMILIA, presente en las
  Instrucciones de los 11 ficheros de los 12 kits. En un kit de catering la palabra «local» chirría,
  pero cambiarla aquí mueve los 11 ficheros de catering y, si se hace en general, los de los 12
  kits. No se toca en esta tanda.
- **`resend-access.ts` sigue diciendo «(v2.0)»** para catering y NO se ha cambiado a propósito:
  `motor.version_line()` escribe «Versión 2.0 · agosto 2026» dentro de los 11 ficheros, así que
  poner v2.1 en el correo dejaría el correo diciendo una versión y el entregable otra. El bump de
  `version_line` es de familia y lo decide el orquestador.
