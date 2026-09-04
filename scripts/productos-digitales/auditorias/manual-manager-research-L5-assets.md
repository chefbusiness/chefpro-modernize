# LENTE 5 — Auditoría de assets existentes, propuesta de herramientas nuevas y mapa de la capa de producto
## Manual del Manager de Restaurante — research local, sin web

Fecha: 2026-09-04. Método: lectura directa con `openpyxl` (`load_workbook(..., read_only=True,
data_only=False)`, un fichero cada vez, `istats cpu temp` entre tandas, sin builds) de los xlsx vivos
en `astro-site/public/dl/`, lectura completa de `kit-gestion-personal-v2-SPEC.md` y
`kit-tareas-v2-SPEC.md`, de `documentos.py` (cabecera, `gates()`, `cargar_guion()`, `main()`), de
`dump_prompts.py`, `check_bloque.py` y de la estructura de `guion_guia_food_cost_ingenieria_menu.py`,
de `types.ts` + `guia-food-cost-ingenieria-menu.ts` + `GuiaLandingPage.astro`, de `git show --stat
19f5ef9` y de los `grep -rn` de `guia-food-cost-ingenieria-menu`/`GuiaFoodCost` por los ficheros que
tocó ese commit, y de `robots.txt` + `robots-gate.py` + `astro.config.mjs` + `whatsapp-gate.py`. Cero
llamadas a bridge.py ni a la web: este documento es research y propuesta, no contenido de producto.

---

## 0. Resumen ejecutivo

1. **La operación diaria/semanal/mensual del manager ya está cubierta a nivel de CHECKLIST** por
   `kit-tareas/03-tareas-manager.xlsx` (110 tareas en 4 hojas: Diario/Semanal/Mensual/Handover) y por
   los ficheros de apertura-cierre (01, 08, 09). Lo que el Manual tiene que aportar es el **CRITERIO**
   detrás de cada tarea — por qué se mide el ticket medio, cómo se lee un semáforo de prime cost, cómo
   se hace un scorecard de selección — no otro checklist con las mismas casillas.
2. **Tres de las diez ideas del encargo duplican, byte a byte, herramientas ya vendidas**: el arqueo de
   caja (`kit-tareas/09-apertura-cierre-caja.xlsx`), el planificador de personal por cubiertos
   (`kit-gestion-personal/BONUS-02-calculadora-plantilla-optima.xlsx` + `03!Previsión por Servicio`) y
   el control de horas/coste por servicio (`kit-gestion-personal/02` + `03`). Se descartan en §2.1.
3. **Dos ideas del encargo se solapan ENTRE SÍ** («P&L diario/semanal con prime cost» y «presupuesto vs
   real semanal») y las dos se acercan a productos ya vendidos en granularidad MENSUAL
   (`kit-plan-financiero/05-pyl-mensual-real-vs-presupuesto.xlsx` y `guia-food-cost/
   cuadro-de-mando-prime-cost.xlsx`). Se fusionan en UNA sola herramienta nueva de granularidad
   SEMANAL — el hueco real que ningún producto cubre hoy (§2.2.1).
4. **El plan de acción a 90 días existe literalmente** en `guia-food-cost-ingenieria-menu/
   plan-accion-90-dias.xlsx` (hojas Decisiones/Calendario 90 Días/KPI de Seguimiento), pero acotado a
   food cost. Se reutiliza el MOLDE (no el contenido) para un plan de 90 días de alcance operativo
   completo (§2.2.5).
5. **`documentos.py` es 100 % reutilizable sin tocar código** — es el mismo motor genérico que ya sirve
   a las 8 guías; sólo hacen falta un `guion_<pid>.py` nuevo y una carpeta de xlsx nueva en `dl/`. Hay
   exactamente **DOS cosas «a fuego»** que dicen «guía» y habría que parametrizar: el texto del prompt
   que ve el agente redactor (`prompt_bloque()`, línea 990-991: «…de la guía profesional «{título}»»)
   y el valor por defecto de la metadata `category` del DOCX (línea 1465: `'Guía profesional'`, sin
   forma de sobreescribirlo para el documento PRINCIPAL — sólo el BONUS puede hacerlo hoy). Ninguna de
   las dos rompe nada: el documento se genera igual, sólo dice «guía profesional» en lugar de «manual
   profesional» en un prompt que el cliente nunca ve y en una propiedad de metadata que casi nadie mira.
6. **La plantilla de landing (`GuiaLandingPage.astro`) también sirve tal cual**, con UNA sola cadena
   fija que dice «Guía» y no sale de `data`: el H2 de la WhySection, «¿Por Qué Esta Guía?» (línea 360).
   El resto del copy variable ya está parametrizado en `GuiaData` (`types.ts`), que no tiene ninguna
   palabra «guía» hardcodeada en su contrato — el nombre del tipo es cosmético.
7. **No existe carpeta `manuales/`** en `astro-site/src/data/productos/` (sólo `guias/`, `kits/`,
   `tareas/`, `planes/`) ni ningún slug que empiece por `manual-` en todo el repo (`grep` en blanco).
   La recomendación de §4.2 es no crearla y reutilizar `guias/` + `GuiaData`, con el matiz del punto 6.
8. **El prefijo `manual-` es una familia NUEVA para `robots.txt`**: hoy las 90 páginas de la zona app
   (45 productos × 2) empiezan por `guia- kit- mega- pack- plan- pro-`, y las reglas de bloqueo van
   ancladas a esos 6 prefijos, 2 líneas × 5 bloques de user-agent = 10 líneas por prefijo. Un slug
   `manual-manager-restaurante` necesita sus 10 líneas nuevas o el gate `robots-gate.py` lo cantará en
   rojo (detecta por `glob('*-access.astro')`/`glob('*-library.astro')`, no por prefijo, así que SÍ lo
   verá). El filtro del sitemap (`astro.config.mjs`) y `whatsapp-gate.py` **no necesitan tocarse**: los
   dos son genéricos por patrón de UN SEGMENTO (`/^\/[^/]+-(access|library)$/`) o por `glob`, sin lista
   de prefijos. Alternativa evaluada en §4.3: `guia-manual-manager-restaurante`, que evita las 10 líneas
   a coste de un slug menos limpio — **no decido, lo dejo para John**.

---

## 1. Inventario de lo que YA cubren nuestros entregables para un manager

### 1.1 `kit-tareas/` — checklists operativos (11 xlsx; 6 abiertos con openpyxl)

| Fichero | Hojas relevantes | Qué cubre | Fórmulas / mecanismo |
|---|---|---|---|
| **`03-tareas-manager.xlsx`** | Diario Manager (25 tareas, 5 bloques: primera hora/pre-servicio/durante servicio/post-servicio/cierre), Semanal Manager (25 tareas, 5 bloques por día + fin de semana), Mensual Manager (19 tareas, 4 bloques: finanzas/equipo/mantenimiento/marketing), Handover Turno (12 tareas) | El checklist operativo del día a día del manager, YA con «Cerrar y validar el registro diario de jornada», «Calcular food cost real vs objetivo», «Calcular labor cost real vs objetivo», «Analizar reseñas del mes», «Revisar posicionamiento en Google Maps» — todo como CASILLA a marcar, sin criterio ni fórmula detrás | Contador `=COUNTIF(B,"?*")−COUNTIF(F,"N/A")` (§2.1 kit-tareas-v2-SPEC.md, regla vigente desde la ronda 2: «—» SÍ cuenta como pendiente) |
| `01-apertura-cierre.xlsx` | Apertura/Cierre × Cocina/Sala/Barra (6 hojas) | Detalle POR ÁREA de apertura y cierre — el manager no es el usuario principal, pero es lo que supervisa | Igual patrón de casilla + firma |
| `08-apertura-cierre-negocio.xlsx` | Apertura del Negocio, Cierre del Negocio | El MARCO del día (alarma, luces, climatización, TPV) | — |
| **`09-apertura-cierre-caja.xlsx`** | Apertura de Caja, Cierre de Caja, **Registro Mensual** | Arqueo diario completo: fondo de caja, recuento por denominaciones, Z del TPV, descuadre — y un registro mensual de 31 días que acumula el descuadre de cada jornada | `F5='=IF(SUM(C5:E5)=0,0,SUM(C5:E5)-B5)'` (total facturado = efectivo+tarjeta+otros−fondo) · `H5='=IFERROR(F5-G5,0)'` (descuadre = total facturado − Z del TPV) |
| BONUS-01-briefing-servicio.xlsx | Briefing | Ficha de briefing PRE-SERVICIO (reservas, VIPs, grupos) — diario, sin agenda ni acta | — |
| BONUS-02-calendario-anual-tareas.xlsx | Calendario Anual | 30+ fechas clave de hostelería mes a mes con tareas asociadas | — |
| 02, 04, 05, 06, 07 | — | Partidas de cocina, tareas por perfil, semanales/mensuales, eventos/festivos, plantilla personalizable — no específicos del manager, sólo nombrados | — |

**Conclusión 1.1**: el «qué hacer y cuándo» del manager está resuelto como checklist. El Manual no debe
repetir esta lista de tareas — debe explicar el CRITERIO detrás de las que tienen más peso (por qué el
food cost se calcula así, cómo se lee un descuadre de caja recurrente, qué hacer con una reseña
negativa) y remitir al kit para la ejecución diaria, igual que la Guía Food Cost remite al Kit de
Escandallos para el escandallo por plato (patrón ya usado y verificado el 2026-09-03).

### 1.2 `kit-gestion-personal/` — 9 xlsx, los 9 abiertos con openpyxl

| Fichero | Hojas | Qué cubre | Fórmulas / mecanismo clave |
|---|---|---|---|
| `01-cuadrante-turnos-semanal.xlsx` | Turnos, Cuadrante Semanal, Cuadrante Mensual | Cuadrante con 4 alertas legales reales: descanso entre jornadas (art. 34.3 ET), descanso semanal (art. 37.1 ET), jornada semanal excedida, jornada diaria de MENOR (art. 6 ET) | `K6` descanso `<12 h` con VLOOKUP a hoja `Turnos`; `N6` jornada `>9 h` (o `>8 h` si es menor) |
| `02-control-horas-extras.xlsx` | Registro Horas (300 filas), Resumen Mensual | Registro con cruce de medianoche y turno partido (columna Pausa); agrega por `SUMIF`, recargo en celda (1,25×), límite anual 80 h con semáforo | `F5='=IF(...,ROUND(MOD($D5-$C5,1)*24-...,2))'`; `F6` semáforo `⛔ EXCEDE / ⚠ cerca del límite / ✓ dentro` |
| **`03-coste-laboral-mensual.xlsx`** | Nóminas, **Ratio Coste Laboral**, **Previsión por Servicio** | SS empresa en celda (33 %), coste/hora real; semáforo de ratio coste laboral/ventas por 6 tipos de negocio (`VLOOKUP` sobre umbrales objetivo/aceptable); **previsión de personal por CUBIERTOS/SERVICIO** (cubiertos/día → servicios/día → cubiertos por servicio → FTE) | `B7='=IF(...,ROUND($B$5/$B$4,4))'` ratio; `B6` en Previsión `=ROUND($B$4/$B$5,0)` cubiertos/servicio |
| `04-onboarding-nuevo-empleado.xlsx` | Checklist Onboarding | 50 tareas con plazo (Día −1/1/7/30) y fecha límite calculada | `H7='=IF($E$3="","",$E$3+-1)'` |
| `05-planificacion-vacaciones.xlsx` | Calendario Anual (53 semanas), Solicitudes, Saldo Vacaciones, Cobertura | Saldo real desde solicitudes aprobadas (no celdas pintadas), prorrateo por fecha de alta, cobertura mínima por turno | `E5` prorrateo por días trabajados del año; `H5` saldo = derecho−disfrutados−pendientes |
| `06-evaluacion-desempeno.xlsx` | Ficha Evaluación, Ficha (ejemplo relleno), Histórico | Evaluación 1-5 o N/A, media sólo de lo valorado, tendencia trimestral, bloque «Plan de Desarrollo» | `C22='=IF(COUNT($C$12:$C$21)=0,"",ROUND(AVERAGE(...),2))'` |
| `07-directorio-plantilla.xlsx` | Plantilla (21 columnas), Vencimientos | Directorio de 30 empleados con NAF, convenio, carnet de manipulador, PRL; **4 alertas de vencimiento por semáforo de color** (❌ vencido / 🔴 <30 d / 🟡 <60 d / 🟢 OK) | `C7='=IF($B7="","",IF($B7-$B$3<0,"❌ VENCIDO...",IF($B7-$B$3<=$B$4,"🔴...",...)))'` — **este es el patrón de alerta por fecha que reutiliza §2.2.4** |
| BONUS-01-briefing-cambio-turno.xlsx | Briefing | Handover diario con temperaturas (registro APPCC de paso) | — |
| **BONUS-02-calculadora-plantilla-optima.xlsx** | Calculadora, **Ratios por Tipo** | Plantilla óptima de personal por 10 tipos de negocio, con ratios cubiertos/cocinero/camarero/barra y semáforo de ratio coste laboral objetivo/aceptable | `E:G` ratios fijos por tipo; comparación con plantilla actual |

**Conclusión 1.2**: el dimensionamiento de personal por cubiertos (idea del encargo) **ya existe dos
veces** en este kit (BONUS-02 y `03!Previsión por Servicio`, verificados por el propio SPEC como «un
solo modelo de dimensionamiento», DOM-9/TEC-15). El control de horas y coste por servicio también.

### 1.3 `kit-plan-financiero/` — 2 de 10 xlsx abiertos (05 y 06, los pedidos)

| Fichero | Hojas | Qué cubre |
|---|---|---|
| **`05-pyl-mensual-real-vs-presupuesto.xlsx`** | 12 pestañas mensuales + Resumen Anual | P&L MENSUAL real vs presupuesto por concepto (ingresos por canal, gastos), desviación € y %, semáforo CON SIGNO editable (`Resumen Anual!B22:B25`) |
| **`06-dashboard-ratios-financieros.xlsx`** | Ratios, **Benchmarks** | Dashboard de 10 ratios (Food Cost %, Labor Cost %, **Prime Cost %**, GOP %, Alquiler/Ventas, Marketing/Ventas, EBITDA %, Beverage Cost %, RevPASH, Margen bruto) con semáforo óptimo/aceptable/peligro |

**Hallazgo relevante para §2.2.6**: `06-dashboard-ratios-financieros.xlsx!Benchmarks!C6:G6` YA trae un
benchmark de **Prime Cost % óptimo <60 %, aceptable 60-65 %, peligro >65 %** — la cifra exacta que la
Guía Food Cost (§3.2.6 de su propio research L5) marcaba como «hueco pendiente, sin fuente verificada».
**Pero esos números están en el xlsx SIN cita ni URL** (`Benchmarks!row17` sólo dice que son la única
fuente de umbrales del kit, no de dónde salen): sigue siendo un hueco de research, no una fuente
citable — sólo confirma que la CIFRA que se usaría ya circula en el catálogo, no que esté verificada.

### 1.4 `guia-food-cost-ingenieria-menu/` — 2 xlsx pedidos, abiertos

| Fichero | Hojas | Qué cubre |
|---|---|---|
| **`cuadro-de-mando-prime-cost.xlsx`** | Parámetros, Mensual | Prime cost MES A MES con objetivo por tipo de negocio (65 % servicio en mesa / 55 % barra o autoservicio, celda verde ajustable), lectura «En objetivo / Por encima del objetivo» |
| **`plan-accion-90-dias.xlsx`** | Decisiones, Calendario 90 Días, KPI de Seguimiento | Plan de 90 días CON el molde exacto que pide el encargo: decisiones con responsable+semana+fecha objetivo (`=D36+7*(semana-1)`) calculada desde una fecha de inicio en celda verde, calendario de 13 semanas con hitos, KPI mes 0 vs mes 3 con lectura automática «Mejora/Empeora» según si el KPI es «bajar es bueno» o no |

**Conclusión 1.4**: el molde de plan a 90 días con responsable/fecha/estado/impacto está resuelto y
verificado (viene del producto que se acaba de lanzar el 2026-09-03/04). Es candidato directo a
reutilizar la ESTRUCTURA para el manual, cambiando el ALCANCE de «decisiones de carta» a «decisiones
operativas del negocio» (§2.2.5).

### 1.5 `pack-appcc/` — 21 xlsx, 2 abiertos con openpyxl, 19 nombrados

Registros ya cubiertos (por nombre de fichero, confirmado en el listado del directorio):
temperaturas (01 diario, 02 recepción), limpieza (03 plan, 04 registro diario), recepción de
mercancías (05), trazabilidad (06), plagas/DDD (07), alérgenos — matriz (08) y fichas de los 14 (14),
aceite de fritura (09), agua potable (10), acciones correctivas (11), análisis de peligros HACCP (12),
higiene personal (13), inspección de sanidad (15, abierto — ver abajo), cocción/regeneración (16),
enfriamiento/descongelación (17), congelación anisakis (18), verificación de termómetros (19).

- **`BONUS-01-registro-formacion.xlsx`** (abierto): registro de formación en SEGURIDAD ALIMENTARIA
  (higiene, APPCC, alérgenos) por empleado, con estado VIGENTE/RENOVAR/CADUCADO por fórmula de fecha
  (`=IF(NOT(ISNUMBER($I5)),"",IF($I5<TODAY(),"CADUCADO",IF($I5-TODAY()<60,"RENOVAR","VIGENTE")))`). **Es
  SÓLO formación de seguridad alimentaria**, no una matriz de polivalencia operativa — no compite con
  §2.2.7, pero SÍ aporta el patrón de alerta a reutilizar.
- **`15-guia-inspeccion-sanidad.xlsx`** (abierto): autoevaluación de los 25 puntos que revisa un
  inspector de Sanidad, con gravedad según Ley 17/2011 y % de cumplimiento automático. **Es
  exclusivamente de cumplimiento APPCC/sanitario**, no una auditoría operativa general (servicio,
  presentación, upselling, experiencia de cliente) — no compite con §2.2.10, pero fija el patrón de
  puntuación por área a no reinventar.
- `BONUS-02-protocolo-alerta-alimentaria.xlsx`: protocolo de alerta alimentaria (retirada de producto),
  no gestión de quejas de cliente — no compite con §2.2.8.

### 1.6 `kit-inventario/` — 9 xlsx, sólo nombrados (no abiertos, fuera del alcance del encargo)

`01-inventario-stock-diario`, `02-fichas-proveedores`, `03-pedidos-compra`, `04-recepcion-mercancias`,
`05-control-mermas`, `06-fifo-caducidades`, `07-analisis-costes-compras`,
`BONUS-08-inventario-rapido-mensual`, `BONUS-09-calculadora-punto-pedido`. Cubre gestión de stock y
compras — colinda con el manual (el manager gestiona proveedores) pero es material de otro producto ya
vendido; el manual debe remitir, no repetir.

### 1.7 Documentos PDF/DOCX dentro de estos kits — NO hay ningún «manual» ni «guía»

`find` sobre `kit-gestion-personal/`, `kit-tareas/`, `pack-appcc/` y `kit-inventario/` con extensión
`.pdf`/`.docx`/`.md` **no devuelve nada**: son kits 100 % de plantillas Excel. El único material
narrativo adyacente es el bono `bono-guia-food-cost-30-dias.md` del Kit de Escandallos (fuera del
alcance de estos 4 kits) y las 8 guías de la línea `guias/`. **No hay ningún documento de prosa
existente que el Manual del Manager pudiera estar duplicando.**

### 1.8 Tabla resumen — necesidad del manager → ¿ya existe? → dónde → decisión

| Necesidad | ¿Ya existe? | Dónde | Decisión para el Manual |
|---|---|---|---|
| Checklist diario/semanal/mensual del manager | Sí, completo | `kit-tareas/03-tareas-manager.xlsx` | CITAR, no repetir; explicar el criterio detrás de las tareas de mayor peso |
| Arqueo de caja | Sí, completo | `kit-tareas/09-apertura-cierre-caja.xlsx` | CITAR; el manual explica cómo LEER un descuadre recurrente, no recalcula el arqueo |
| Cuadrante de turnos y alertas legales | Sí, completo | `kit-gestion-personal/01` | CITAR |
| Coste laboral y ratio | Sí, completo | `kit-gestion-personal/03` | CITAR |
| Dimensionamiento de personal por cubiertos | Sí, DOS VECES | `kit-gestion-personal/03!Previsión` + `BONUS-02` | CITAR; no construir un tercero |
| P&L mensual real vs presupuesto | Sí | `kit-plan-financiero/05` | CITAR; construir sólo la variante SEMANAL (§2.2.1) |
| Prime cost mensual con semáforo | Sí, DOS VECES | `kit-plan-financiero/06!Benchmarks` + `guia-food-cost/cuadro-de-mando-prime-cost.xlsx` | CITAR; construir sólo si se amplía a KPI operativos no financieros (§2.2.1) |
| Plan de acción a 90 días | Sí, molde completo (alcance food cost) | `guia-food-cost/plan-accion-90-dias.xlsx` | REUTILIZAR EL MOLDE con alcance operativo distinto (§2.2.5) |
| Formación de seguridad alimentaria con alerta de caducidad | Sí | `pack-appcc/BONUS-01-registro-formacion.xlsx` | CITAR; no incluir formación APPCC en la matriz de polivalencia nueva |
| Autoevaluación de inspección de Sanidad | Sí | `pack-appcc/15-guia-inspeccion-sanidad.xlsx` | CITAR; el mystery audit nuevo NO reaudita APPCC |
| Gestión de quejas/incidencias con SLA | No | — | CONSTRUIR (§2.2.8) |
| Seguimiento de reseñas online | No (sólo tareas sueltas en 03-tareas-manager) | — | CONSTRUIR (§2.2.9) |
| Matriz de formación y polivalencia operativa (no APPCC) | No | — | CONSTRUIR (§2.2.7) |
| Calendario de cumplimiento legal/mantenimiento con alertas | Parcial (checklist sin fechas) | `kit-tareas/05!Trimestral y Anual` (SPEC, DOM-16) | CONSTRUIR combinando el patrón de alerta de `07!Vencimientos` con el contenido del checklist (§2.2.6 — renumerado abajo) |
| Entrevista y scorecard de selección | No | — | CONSTRUIR (§2.2.4) |
| Checklist de auditoría interna puntuable (mystery audit) | Parcial (sólo APPCC) | `pack-appcc/15` | CONSTRUIR, ámbito operativo general (§2.2.10) |
| Plan de reuniones/briefings y acta | Parcial (briefings diarios, no reuniones periódicas) | `kit-tareas/BONUS-01` + `kit-gestion-personal/BONUS-01` | CONSTRUIR, cadencia distinta (§2.2.6) |

---

## 2. Propuesta de herramientas Excel nuevas

Evalué las 10 ideas del encargo una a una. **3 se descartan** por duplicar mecanismos ya vendidos con
fórmulas verificadas; **2 se fusionan** en una porque se solapaban entre sí y con lo ya vendido; quedan
**7 recomendadas** (dentro del rango 6-10 que pedía el encargo), cada una con reutilización de motor
explícita.

### 2.1 Descartadas (con motivo verificado)

| Idea del encargo | Motivo del descarte | Evidencia |
|---|---|---|
| Arqueo y cuadre de caja | **Ya existe, idéntico**: fondo, recuento por denominaciones, Z del TPV, descuadre, registro mensual con 31 días | `kit-tareas/09-apertura-cierre-caja.xlsx`, fórmulas citadas en §1.1 |
| Planificador de necesidades de personal por previsión de cubiertos | **Ya existe DOS VECES**, con el mismo modelo cubiertos/día → servicios → cubiertos/servicio → FTE, verificado por el propio SPEC como intencionalmente unificado (DOM-9) | `kit-gestion-personal/03!Previsión por Servicio` + `BONUS-02-calculadora-plantilla-optima.xlsx`, fórmulas citadas en §1.2 |
| Control de horas y coste por servicio | **Ya existe**: registro con cruce de medianoche, recargo en celda, coste/hora real con SS prorrateada | `kit-gestion-personal/02` + `03!Nóminas`, fórmulas citadas en §1.2 |

### 2.2 Recomendadas (7, todas con reutilización de motor explícita)

#### 2.2.1 `cuadro-de-mando-semanal-manager.xlsx` — fusiona «P&L diario/semanal» y «presupuesto vs real semanal»

Las dos ideas del encargo pedían esencialmente lo mismo (ventas reales vs objetivo, a una cadencia que
NINGÚN producto vendido cubre hoy: `kit-plan-financiero/05` es mensual y `guia-food-cost/
cuadro-de-mando-prime-cost.xlsx` también). Construir las dos por separado habría producido un
duplicado interno del propio Manual.

- **Hojas**: `Semana` (52 filas, una por semana ISO) · `Parámetros` (objetivo de food cost, labor cost
  y prime cost, celdas verdes con el mismo mecanismo de `03!Nóminas!C2` del kit de personal) ·
  `KPI operativos` (ticket medio, cubiertos totales, ventas por hora de apertura, ratio personal —
  ninguno de estos vive hoy en una hoja semanal).
- **Fórmulas clave**: prime cost semanal = `(consumo materia prima + coste personal con SS) / ventas
  netas` — la MISMA fórmula de `cuadro-de-mando-prime-cost.xlsx!Mensual!N5`, aplicada por semana en vez
  de por mes; semáforo con el mismo patrón `IFERROR(...,IF($N<=$O,"En objetivo","Por encima"))`.
- **Qué decisión permite tomar**: detectar una semana mala ANTES de que se diluya en el promedio del
  mes — el P&L mensual ya vendido no puede aislar una semana de eventos especiales o una mala semana de
  personal de las otras tres.
- **Reutiliza**: la fórmula de prime cost de `guia-food-cost/cuadro-de-mando-prime-cost.xlsx!Mensual`
  (cambiando el periodo) y el patrón de semáforo con signo de `kit-plan-financiero/05!Resumen Anual`.
- **No reutiliza ni repite**: los 12 meses completos del P&L mensual — esta hoja es un radar semanal de
  alerta temprana, no una contabilidad completa; su Instrucciones debe decirlo en la primera línea para
  no leerse como «el mismo dashboard, más corto».

#### 2.2.2 `matriz-formacion-polivalencia.xlsx`

- **Hojas**: `Matriz` (empleado × puesto/estación, con nivel 0-3: 0=sin formar, 1=supervisado,
  2=autónomo, 3=puede formar a otros) · `Plan de Cross-Training` (empleado, estación objetivo,
  responsable, fecha objetivo, estado) · `Cobertura por Estación` (cuántos empleados están en nivel ≥2
  por estación, con alerta si sólo hay 1 — riesgo de punto único de fallo).
- **Fórmulas clave**: `COUNTIFS` para contar polivalentes por estación; alerta
  `=IF(cobertura<=1,"⚠ RIESGO: sólo 1 persona sabe esta estación","")`.
- **Qué decisión permite tomar**: quién puede cubrir una baja o vacaciones sin recurrir a un externo, y
  dónde hay un punto único de fallo (una sola persona sabe hacer la partida fría).
- **Reutiliza**: el patrón de cabecera y de 30 empleados de `kit-gestion-personal/07-directorio-
  plantilla.xlsx!Plantilla`, y el semáforo de alerta de `07!Vencimientos`.
- **No duplica**: `pack-appcc/BONUS-01-registro-formacion.xlsx`, que es formación de SEGURIDAD
  ALIMENTARIA con caducidad — esta matriz es polivalencia OPERATIVA (estaciones, puestos), sin fecha de
  caducidad. Se cita explícitamente: «la formación de higiene y APPCC se lleva en el Pack APPCC; esta
  matriz es de quién sabe hacer qué».

#### 2.2.3 `registro-quejas-incidencias-sla.xlsx`

- **Hojas**: `Registro` (fecha, canal — sala/Google/TripAdvisor/teléfono/email —, cliente, motivo,
  gravedad, responsable, acción tomada, fecha de cierre, SLA en horas, `Cumplido S/N`) · `Resumen`
  (incidencias abiertas, tiempo medio de cierre, motivo más repetido, gravedad más repetida).
- **Fórmulas clave**: `SLA cumplido = IF(fecha_cierre-fecha_apertura<=sla_horas/24,"Sí","No")`; resumen
  con `COUNTIFS` por motivo y por gravedad, tiempo medio con `AVERAGEIFS`.
- **Qué decisión permite tomar**: si las quejas se repiten por el MISMO motivo (cocina lenta, error de
  comanda, temperatura de plato) en vez de perderse una a una en la memoria del turno; y si el equipo
  cierra las incidencias dentro del plazo que la casa se ha marcado.
- **Reutiliza**: el patrón `Estado ✓/—/N/A` de los checklists de `kit-tareas` para el campo «Acción
  tomada» y el semáforo de gravedad de `pack-appcc/15!25 Puntos Inspección!D` (Grave/Muy grave).
- **Hueco declarado**: no hay ningún fichero del catálogo hoy con esta función — es una necesidad no
  cubierta y verificada como tal en §1.8.

#### 2.2.4 `entrevista-scorecard-seleccion.xlsx`

- **Hojas**: `Scorecard` (candidato, puesto, 6-8 competencias del puesto puntuadas 1-5, con las mismas
  reglas de N/A que la evaluación de desempeño) · `Comparativa de Candidatos` (una fila por candidato
  para el mismo puesto, media ponderada, recomendación) · `Preguntas por Competencia` (banco de
  preguntas de entrevista estructuradas, una por competencia, para no improvisar).
- **Fórmulas clave**: media `=IF(COUNT(rango)=0,"",ROUND(AVERAGE(rango),2))` — literal la de
  `kit-gestion-personal/06-evaluacion-desempeno.xlsx!Ficha Evaluación!C22`.
- **Qué decisión permite tomar**: comparar candidatos con el mismo criterio en vez de con la
  impresión del momento, y dejar un rastro de POR QUÉ se contrató a alguien (para el propio onboarding
  del `04` si entra).
- **Reutiliza**: la fórmula de media condicional y la escala 1-5/N/A de
  `kit-gestion-personal/06-evaluacion-desempeno.xlsx`.
- **Cierra el ciclo con**: `04-onboarding-nuevo-empleado.xlsx` (contratación → onboarding → evaluación
  de desempeño, los tres kits de personas encadenados).

#### 2.2.5 `plan-accion-90-dias-operativo.xlsx` — reutiliza el MOLDE de la Guía Food Cost, cambia el alcance

- **Hojas**: `Decisiones` (mismo esquema: #, área, herramienta de origen, decisión, responsable, semana,
  fecha objetivo, estado, impacto estimado) · `Calendario 90 Días` (13 semanas, bloques: semanas 1-3
  diagnóstico con las herramientas nuevas de este manual, 4-8 ejecución, 9-11 formación y cobertura,
  12-13 revisión) · `KPI de Seguimiento` (mes 0 vs mes 3, con lectura automática Mejora/Empeora).
- **Fórmulas clave**: idénticas letra por letra a `guia-food-cost/plan-accion-90-dias.xlsx` — fecha
  objetivo `=IFERROR(IF(OR($F5="",$D$36=""),"",$D$36+7*($F5-1)),"")`, lectura de KPI con el `IF` de
  «¿bajar es bueno?» que ya tiene esa hoja.
- **Qué decisión permite tomar**: da un ORDEN de ejecución a las salidas de las otras 6 herramientas de
  este manual, igual que el de food cost lo da a la matriz multi-método — es la misma pieza, pero para
  decisiones de PERSONAS, SERVICIO y CUMPLIMIENTO en vez de decisiones de CARTA.
- **No duplica**: el ámbito de KPI es distinto (rotación de personal, NPS/reseñas, cumplimiento de
  formación) y el manual, en su primera hoja, debe decir explícitamente que este plan no repite el de
  food cost — quien tenga los dos productos, los usa en paralelo sobre áreas distintas del negocio.

#### 2.2.6 `calendario-cumplimiento-reuniones.xlsx`

Fusiona dos ideas del encargo («calendario de cumplimiento legal y mantenimiento» y «plan de reuniones/
briefings y acta») porque comparten el mismo mecanismo (fecha + alerta + registro), y separarlas habría
sido dos ficheros casi idénticos por dentro.

- **Hojas**: `Cumplimiento y Mantenimiento` (inspecciones, extintores, plagas/DDD, seguro, revisión
  TPV/Verifactu, formación — con fecha de la última y periodicidad, calculando la próxima y el
  semáforo) · `Reuniones Periódicas` (fecha, tipo — briefing semanal/reunión mensual de equipo/comité
  de dirección —, asistentes, agenda) · `Acta` (por reunión: puntos tratados, decisiones, responsable,
  fecha de seguimiento — enlaza con `plan-accion-90-dias-operativo.xlsx` cuando una decisión de reunión
  se convierte en tarea con fecha).
- **Fórmulas clave**: alerta de vencimiento **literal** la de `kit-gestion-personal/07!Vencimientos!C7`
  (`❌ VENCIDO / 🔴 <30 d / 🟡 <60 d / 🟢 OK`), aplicada a próxima inspección/extintor/plaga en vez de a
  contrato/carnet.
- **Qué decisión permite tomar**: no llegar a una inspección de Sanidad con el extintor caducado
  (motivo #14 de multa muy grave según `pack-appcc/15`), y que una reunión de equipo deje una decisión
  con fecha en vez de una conversación que nadie recuerda al mes siguiente.
- **Reutiliza**: la fórmula de alerta de `07-directorio-plantilla.xlsx!Vencimientos` y el CONTENIDO ya
  redactado (sin repetirlo, remitiendo) de la hoja «Trimestral y Anual» que el SPEC de `kit-tareas`
  añade al `05-tareas-semanales-mensuales.xlsx` (DOM-16: DDD, extintores/BIE, gas, legionela, seguro,
  TPV/Verifactu) — esa hoja es un CHECKLIST sin fecha de vencimiento; esta herramienta nueva es el
  CALENDARIO con alerta que el checklist no tiene.
- **No duplica**: los briefings diarios de `kit-tareas/BONUS-01-briefing-servicio.xlsx` ni
  `kit-gestion-personal/BONUS-01-briefing-cambio-turno.xlsx` — esos son de CADA turno; esta hoja es de
  reuniones PERIÓDICAS (semanal/mensual) con acta, cadencia y propósito distintos.

#### 2.2.7 `checklist-auditoria-interna-puntuable.xlsx` (mystery audit)

- **Hojas**: `Auditoría` (área — sala/cocina/barra/baños/servicio/marca —, punto de control, peso,
  puntuación 0-5, observación) · `Resumen por Área` (puntuación media ponderada por área, con semáforo)
  · `Histórico` (una columna por visita, para ver tendencia).
- **Fórmulas clave**: puntuación ponderada `=SUMPRODUCT(peso,puntuacion)/SUM(peso)`; % de cumplimiento
  igual al patrón de `pack-appcc/15!25 Puntos Inspección` (`incumplimientos/total`).
- **Qué decisión permite tomar**: puntuar la experiencia de cliente y los estándares de marca (no la
  seguridad alimentaria, que ya tiene su propia auditoría) de forma repetible, visita a visita, con una
  cifra comparable en el tiempo.
- **Reutiliza**: el patrón de puntuación y % de cumplimiento de `pack-appcc/15-guia-inspeccion-
  sanidad.xlsx!25 Puntos Inspección`.
- **No duplica**: esta herramienta EXCLUYE a propósito los puntos de APPCC/sanidad — remite al Pack
  APPCC para eso — y cubre sólo servicio, presentación, limpieza no-APPCC (zona de sala, no cocina),
  marca y experiencia de cliente.

**Total: 6 herramientas nuevas** (2.2.1 a 2.2.7, con la numeración 2.2.2 a 2.2.7 = 6, más la 2.2.1 =
7 en total), dentro del rango 6-10 pedido, sin ninguna que duplique una ya vendida.

---

## 3. Reutilización del pipeline de documentos y de la landing

### 3.1 `documentos.py`, `dump_prompts.py`, `check_bloque.py` — genéricos, sirven tal cual

`documentos.py` (2.036 líneas) es un motor parametrizado por `guion_<pid>.py` con tres símbolos:
`GUIA` (dict), `CAPITULOS` (lista de dicts) y `BONUS` (lista de documentos bonus con su propio
`CAPITULOS`). `cargar_guion(pid)` (línea 1886) resuelve `guion_{pid}.py` de forma genérica —
**funciona para `manual-manager-restaurante` sin tocar una línea**, igual que ya funciona para
`guia-food-cost-ingenieria-menu`. `main()` (línea 1950) acepta `--producto <pid>` sin ninguna referencia
a «guía» en su lógica de control.

**Claves obligatorias del guion** (deducidas de `cargar_guion`/`construir_documento`/`main`, verificado
contra el guion real de food cost):
- `GUIA`: `pid`, `titulo`, `subtitulo`, `autor_linea`, `cabecera`, `fecha`, `version`, `bio`, `legal`,
  `portada_texto`, `gates` (con `paginas_prometidas`, `palabras_objetivo`, `min_palabras_cap`,
  `cifras_extra`, `cifras_ignorar`, `erratas_permitidas`, `mortalidad_permitida`).
- `CAPITULOS`: lista de dicts con `n`, `titulo`, `resumen_indice`, `palabras`, `bloques`, `objetivo`,
  `epigrafes`, `puntos`, `cifras` (tuplas `(etiqueta, 'fichero.xlsx!Hoja!Celda', formato)` vía el
  helper `C()`), `sector` (ids de `guias-v2-research-sector.json`), `tablas` (con `src` xlsx/hoja/cols
  o `cabecera`/`filas` manual), `prohibido` (lista de restricciones, normalmente `NO_COMUN` + propias).
- `BONUS`: lista de dicts con `nombre`, `guia` (overrides parciales del `GUIA` padre), `gates`
  (overrides, incluye `meta` con `title`/`subject` propios) y `capitulos` (mismo esquema que arriba).

**Dos cosas «a fuego» que dicen «guía» literal y habría que parametrizar** (ninguna rompe la
generación, las dos son cosméticas pero visibles):

1. `prompt_bloque()` (línea 990-991): `f'Escribe un tramo del capítulo {cap["n"]} — «{cap["titulo"]}»
   de la guía profesional «{guia["titulo"]}» ({guia["subtitulo"]}).'` — el agente que redacta el bloque
   ve literalmente «guía profesional» aunque el producto sea un manual. Fix mínimo: añadir una clave
   `guia.get('tipo_documento', 'guía')` y usarla ahí («manual profesional» para el nuevo producto).
2. `construir_documento()`/`maquetar()` → `cp.category = meta.get('category', 'Guía profesional')`
   (línea 1465): el DOCX del documento PRINCIPAL (no el BONUS) siempre recibe `category='Guía
   profesional'` porque `main()` llama a `construir_documento(pid, guia, ...)` **sin** `cfg_extra`
   (sólo los BONUS reciben `cfg_extra=b['gates']`, que sí puede traer `meta.category`). Fix mínimo:
   permitir que `GUIA['gates']` lleve una clave `meta` que `main()` pase como `cfg_extra` también para
   el documento principal, o cambiar el default a algo neutro como `'Documento profesional'`.

`dump_prompts.py` y `check_bloque.py` son igual de genéricos: el primero vuelca los prompts EXACTOS que
`documentos.py` mandaría a bridge (ahora a los subagentes) leyendo `guion.CAPITULOS`/`guion.BONUS` sin
ninguna referencia a «guía»; el segundo comprueba un bloque con los mismos detectores de
`documentos.py` (formato `### `, sin tabla Markdown, sin caracteres no latinos, sin cita
`fichero!Hoja!Celda`, epígrafes literales presentes) — ninguno de los dos necesita cambio.

### 3.2 Landing — `types.ts` + `guia-food-cost-ingenieria-menu.ts` + `GuiaLandingPage.astro`

`GuiaData` (types.ts, 160 líneas) **no tiene ninguna palabra «guía» hardcodeada en su contrato**: es
`slug`, `stripeEnvKey`, `seo`, `hero`, `pricing`, `images`, `grid`, `testimonials`, `why`, `author`,
`bonus`, `buyBox`, `guarantee`, `faqs`, `cta`, `stickyLabel`, `footerLinks`, `alreadyBought`, `schema`,
`updateNote?` — todo dato, ningún literal de plantilla. El nombre del tipo (`GuiaData`) es cosmético y
no afecta al build.

`GuiaLandingPage.astro` (829 líneas) **tiene UNA sola cadena fija que dice «Guía»** y no sale de
`data`: la WhySection, línea 360, `¿Por Qué Esta <span class="text-[#FFD700]">Guía</span>?` — el propio
comentario de `types.ts` (línea 93) lo confirma: «WhySection — H2 fijo "¿Por Qué Esta Guía?"; sólo
varían las 4 razones». **Fix mínimo**: añadir un campo opcional `why.titleGold?: string` (default
`'Guía'`) a `GuiaData` y usarlo en la plantilla, o — más simple, dado que es un solo H2 — parametrizar
directamente `data.why.titleWord` sin tocar el resto del contrato.

Todo lo demás (el resto de la interfaz, el ORDEN de las 12 secciones del template, el DOM de cada
componente) es agnóstico de si el producto se llama guía, manual, kit o plan: sólo pinta lo que le
llega en `data`.

### 3.3 No existe `manuales/` — recomendación

No hay ninguna carpeta `astro-site/src/data/productos/manuales/` ni ningún fichero con `slug` que
empiece por `manual-`. Con el matiz del punto 6 del resumen ejecutivo (dos strings «a fuego» en el
motor y una en la plantilla), **reutilizar `guias/` + `GuiaData` es la opción de menor fricción**: cero
tipos nuevos, cero plantilla nueva, y los tres fixes de parametrización son opcionales — si no se
tocan, el producto se genera igual y sólo dice «guía profesional»/«¿Por Qué Esta Guía?» en dos sitios
de bajo impacto (un prompt que el cliente no ve y un H2 visible pero menor). Crear una carpeta
`manuales/` con un `ManualData` idéntico a `GuiaData` sólo tendría sentido si la línea de manuales va a
tener MÁS de un producto con divergencias estructurales propias (como ya las tiene `guias/` documentadas
en el comentario de cabecera de `types.ts`); con un solo producto, es sobre-ingeniería.

---

## 4. Mapa exacto de la capa de producto (checklist de ficheros)

Basado en `git show --stat 19f5ef9` (61 ficheros, +12.438/−81) y en el `grep -rn` de
`guia-food-cost-ingenieria-menu`/`GuiaFoodCost`/`GUIA_FOOD_COST` sobre cada uno (excluyendo
`dist/node_modules/.astro`).

### 4.1 Qué se añadió para el producto 45 (una línea cada uno) → qué haría falta para el 46

| Fichero | Qué llevó el producto 45 | Qué llevaría `manual-manager-restaurante` |
|---|---|---|
| `src/App.tsx` | 2 imports + 3 líneas de rutas `-access`/`-library` (la landing NACE en Astro, no tiene ruta SPA) | Igual: 2 imports (`ManualManagerAccessGate`, `ManualManagerDashboard`) + rutas `-access`/`-library` |
| `src/pages/GuiaFoodCostAccessGate.tsx` | Wrapper de 12 líneas sobre `ProductAccessGate` con `productId`/`storageKey`/`dashboardPath`/`landingPath`/`productLabel` | Fichero nuevo análogo, mismo patrón de 5 props |
| `src/pages/GuiaFoodCostDashboard.tsx` | 130 líneas: `SECTIONS` con 3 bloques (Guía Principal, Herramientas Excel ×8, Bonus ×2) | Fichero nuevo: `SECTIONS` con Manual Principal (PDF+DOCX) + Herramientas Excel ×6-7 + Bonus si los hay |
| `astro-site/src/lib/zona-app.ts` | 1 línea de registro (`productId`, `accessPath`, `libraryPath`, `landingPath`, `storageKey`, `productLabel`, `gateComponent`, `dashboardComponent`, `notas`) | 1 línea igual — **fuente de verdad que `fase5-generate-zona-app.py` lee** |
| `astro-site/src/lib/linkify-use-case.ts` | 1 línea (`'Guía Food Cost + Ingeniería de Menú': '/guia-food-cost-ingenieria-menu'`) | 1 línea igual con el nombre del manual |
| `src/data/products-catalog.ts` | 1 entrada (id/url/…) | 1 entrada igual |
| `src/data/productos-changelog.ts` | 1 entrada `'guia-food-cost-ingenieria-menu': {...}` | 1 entrada igual, versión 1.0 |
| `src/data/productos-digitales-config.ts` | 1 bloque con `accessPath` + mapa `downloads` (clave lógica → ruta `/dl/<pid>/<fichero>`) | 1 bloque igual, con las claves de las 6-7 herramientas + manual PDF/DOCX + bonus |
| `src/pages/ProductosDigitales.tsx` | 1 entrada de catálogo (slug) + 1 `ListItem` en el `BreadcrumbList` del JSON-LD (position 11) | 1 entrada + 1 `ListItem` (position 46 o la que toque) |
| `astro-site/src/components/pages/ProductosDigitalesHubPage.astro` | Mismo patrón: 1 entrada de catálogo + 1 `ListItem` | Igual |
| `astro-site/src/pages/<slug>.astro` (landing) | Fichero NUEVO de 33 líneas: thin wrapper `BaseLayout` + `GuiaLandingPage` + `import data from '../data/productos/guias/<pid>'`; resuelve `VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST` a mano (no es fiable `import.meta.env[clave]` dinámico) | Fichero nuevo análogo, resolviendo `VITE_STRIPE_PAYMENT_LINK_MANUAL_MANAGER_RESTAURANTE` (o el nombre que se elija) a mano |
| `astro-site/src/pages/<slug>-access.astro` | **GENERADO** por `fase5-generate-zona-app.py` a partir del registro de `zona-app.ts` | Se genera solo, no se escribe a mano |
| `astro-site/src/pages/<slug>-library.astro` | **GENERADO**, con `whatsapp={false}` (el dashboard monta su propio botón de soporte) | Igual, generado |
| `astro-site/src/islands/library/<X>LibraryIsland.tsx` | **GENERADO**, wrapper de `ProtectedRoute` + el Dashboard | Igual, generado |
| `netlify/functions/verify-purchase.ts` | 1 entrada en `PRODUCTS` (`accessPath`) | 1 entrada igual |
| `netlify/functions/resend-access.ts` | 1 entrada análoga | 1 entrada igual |
| `netlify/functions/get-download-urls.ts` | 1 bloque con el mapa clave→ruta `/dl/<pid>/<fichero>` (10 claves: guía-pdf, guía-docx, bonus-pdf, bonus-docx + 8 herramientas… en realidad 12 claves para 8 xlsx+2 bonus+2 guía) | 1 bloque igual con las claves del manual |
| `netlify/functions/admin-generate-access.ts` | 1 entrada (`accessPath` + `label`) en el mapa de fallback admin | 1 entrada igual |
| `netlify/shared/payment-links.ts` | 1 línea (`productId: 'URL de Stripe'`) | **NO se edita a mano**: la regenera `sync-payment-links.py` leyendo `slug`+`stripeEnvKey` de la landing y cruzando con `verify-purchase.ts` + la env var real de Netlify — requiere que John haya creado el Payment Link y la env var antes |
| `scripts/astro-migration/fase5-generate-zona-app.py` | 2 constantes bumped de 44→45 (el `if len(entries) != 44` y los 2 mensajes de conteo) | Bump 45→46 en las mismas 3 líneas; el resto del script es genérico (extrae de `zona-app.ts`+`App.tsx`+los ficheros `*AccessGate.tsx`) |
| `scripts/productos-digitales/sync-payment-links.py` | Ninguna edición — es genérico: lee `slug`/`stripeEnvKey` de `astro-site/src/data/productos/**/*.ts` por regex, sin lista de productos hardcodeada | Ninguna edición necesaria |

### 4.2 Ficheros del guion/documentos (no estaban en el commit 19f5ef9, se añadieron el 2026-09-04)

- `scripts/productos-digitales/guias-v2_0/guion_manual_manager_restaurante.py` — nuevo, con `GUIA`/
  `CAPITULOS`/`BONUS` (§3.1).
- `astro-site/public/dl/manual-manager-restaurante/` — carpeta nueva con las 6-7 herramientas xlsx de
  §2.2 y, tras `documentos.py`, el PDF+DOCX del manual y del bonus si lo hay.

### 4.3 ⚠️ El prefijo `manual-` — qué hay que tocar exactamente

**`robots.txt`**: hoy protege 6 prefijos (`guia- kit- mega- pack- plan- pro-`), 2 líneas
(`Disallow: /<prefijo>-*-access` + `Disallow: /<prefijo>-*-library`) repetidas en **5 bloques de
user-agent** (Googlebot, Bingbot, Twitterbot, facebookexternalhit, `*`) = 10 líneas por prefijo. Un
slug `manual-manager-restaurante` (familia `manual-`) necesita:

```
Disallow: /manual-*-access
Disallow: /manual-*-library
```

insertadas en los 5 bloques (10 líneas totales), en el mismo punto donde están las de `plan-`/`pro-`.
**Verificado que hace falta**: `scripts/astro-migration/robots-gate.py` línea 131 descubre las rutas de
la zona app por `glob('*-access.astro')`/`glob('*-library.astro')` sobre `astro-site/src/pages/`, NO
por prefijo — así que en cuanto `fase5-generate-zona-app.py` genere
`manual-manager-restaurante-access.astro` y `-library.astro`, el gate las verá y las exigirá
bloqueadas; sin las 10 líneas nuevas, `robots-gate.py` fallará con «N ruta(s) de la ZONA APP
rastreables».

**`astro.config.mjs`** (filtro del sitemap, línea 61): `/^\/[^/]+-(access|library)$/` — regex genérico
de UN SEGMENTO que acaba en `-access`/`-library`, **sin lista de prefijos**. No necesita ningún cambio:
ya excluirá `manual-manager-restaurante-access` y `-library` del sitemap automáticamente.

**`scripts/astro-migration/whatsapp-gate.py`**: descubre los dashboards con
`glob('*-library.astro')` sobre `astro-site/src/pages/` (línea 102), sin lista de prefijos. No necesita
cambio — sólo que la nueva `-library.astro` (generada) traiga `whatsapp={false}` y la landing NO lo
traiga, igual que el patrón de food cost.

**Alternativa evaluada (no decidida — para John)**: usar el slug `guia-manual-manager-restaurante` en
vez de `manual-manager-restaurante`.

| | `manual-manager-restaurante` (prefijo nuevo) | `guia-manual-manager-restaurante` (prefijo `guia-` existente) |
|---|---|---|
| Cambios en `robots.txt` | 10 líneas nuevas (5 bloques × 2 reglas) | Ninguno — ya cubierto por `Disallow: /guia-*-access`/`-library` |
| Legibilidad de la URL | Limpia: `aichef.pro/manual-manager-restaurante` | Redundante: «guía manual» repite la categoría del producto en la URL |
| Coherencia con la categoría NUEVA «Manuales operativos» que pide el encargo | Alta — el slug refleja la categoría real | Baja — la URL dice «guía» para un producto que la landing y el copy llamarían «manual» |
| Riesgo de futuro (si nacen más manuales) | Cada uno necesita su propio slug `manual-*`, pero el prefijo YA está declarado en `robots.txt` desde el primero — el coste de las 10 líneas se paga UNA vez | Cero coste adicional nunca, pero la deuda de nomenclatura (URLs «guía-manual-…») se acumula con cada manual nuevo |
| Coherencia con la reutilización de `GuiaData`/`GuiaLandingPage` (§3.3) | El slug es independiente del tipo de datos interno — no hay conflicto técnico en usar `manual-*` con `GuiaData` | Igual de compatible |

No decido cuál: es una decisión de nomenclatura de producto, no técnica — las dos son viables y el
coste de la primera (10 líneas de `robots.txt`, una vez) es bajo.

---

## 5. Riesgos y dudas

1. **El benchmark de Prime Cost % (60-65 %) de `kit-plan-financiero/06!Benchmarks` no tiene fuente
   citable** (§1.3) — sigue siendo un hueco de research para cualquier capítulo del manual que quiera
   dar ese rango como referencia de sector; hace falta un paso de research con web antes de escribirlo,
   igual que ya se marcó como pendiente en el research L5 de la Guía Food Cost.
2. **Los dos «a fuego» de `documentos.py` (§3.1) y el H2 fijo de `GuiaLandingPage.astro` (§3.2) no
   bloquean nada** si no se tocan — el documento y la landing se generan igual, sólo con dos strings
   cosméticos que dicen «guía» en vez de «manual». Si se decide corregirlos, es un cambio de una línea
   cada uno, pero toca un fichero compartido por las 8 guías existentes: **cualquier cambio en
   `documentos.py`/`GuiaLandingPage.astro` debe regenerarse contra al menos un producto ya vendido
   (food cost) para confirmar que no rompe nada**, siguiendo la disciplina de gates de la familia.
3. **No verifiqué con pycel ninguna fórmula de las 6 herramientas nuevas propuestas** (son diseño, no
   ficheros construidos) — la verificación pycel es tarea de la fase de construcción, no de esta
   auditoría, igual que en el research L5 de referencia.
4. **La decisión del slug (§4.3) queda abierta para John** — no se ha tocado `robots.txt` ni ningún
   otro fichero de la capa de producto en este research: es sólo el mapa de lo que habría que tocar.
5. **No se ha auditado el precio ni el `products-catalog.ts` con una entrada real** — se confirma que
   hoy NO existe ningún producto `manual-*` (grep en blanco), que es la fuente de verdad correcta, pero
   la entrada en sí es tarea de integración, fuera de esta LENTE.
6. **`04-onboarding-nuevo-empleado.xlsx`, `05-planificacion-vacaciones.xlsx`, `06-evaluacion-desempeno.xlsx`
   y `07-directorio-plantilla.xlsx`** de `kit-gestion-personal` se auditaron con detalle por venir en el
   mismo `for` de apertura del kit completo (§1.2), aunque el encargo sólo pedía «en especial» los
   ficheros del manager — se documentan igualmente porque su patrón de alerta por fecha (`07!
   Vencimientos`) es la pieza que reutilizan DOS de las herramientas nuevas (§2.2.2 y §2.2.6).
