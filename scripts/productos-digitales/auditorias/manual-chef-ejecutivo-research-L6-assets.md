# LENTE 6 — Auditoría de lo que ya vendemos + herramientas nuevas que no canibalicen — Manual del Chef Ejecutivo

Fecha de research: 2026-09-06. Trabajo 100 % local (sin web): `openpyxl` (`data_only=True`,
`read_only=True`, un fichero cada vez, `istats cpu temp` antes/después, pico medido 63,6 °C),
lectura de `manual-manager-SPEC.md`, `guion_manual_manager_restaurante.py`, `datos_ejemplo.py`,
`documentos.py`/`motor.py`, 12 posts del blog, `use-cases.ts` + `use-cases-content.es.ts`, y la
capa de producto completa (catálogo, hub, zona-app, functions, footerLinks, robots.txt). Se
combina con la lectura previa de `manual-chef-ejecutivo-research-L2-serp.md` (research de SERP de
otra lente, ya entregado) sólo para no contradecir naming ni conclusiones.

---

## (a) Inventario exacto: qué cubre YA cada herramienta, y qué le falta desde la óptica del chef

### Manual del Manager de Restaurante (`astro-site/public/dl/manual-manager-restaurante/`)

| Fichero | Qué cubre (hojas leídas) | Qué le falta desde la óptica del CHEF |
|---|---|---|
| `cuadro-de-mando-semanal-manager.xlsx` | Instrucciones · Parámetros (objetivo food/labor/prime cost por tipo de negocio, SS empresa 33 %) · Semana (52 filas ISO: ventas, consumo, food/labor/prime cost, ticket medio, cubiertos/hora, ventas/hora trabajada) · KPI y Definiciones | Es financiero y agregado a TODO el restaurante por semana. No baja a partida, no mide tiempos de pase, no cuenta incidencias de alérgenos, no separa horas de cocina de horas de sala. Un chef que quiera saber "¿qué partida se come el margen?" no lo puede sacar de aquí. |
| `matriz-formacion-polivalencia.xlsx` | Instrucciones · Matriz (12×6, niveles 0-3, "quién SOSTIENE la estación") · Plan de Cross-Training (quién enseña a quién, fecha objetivo) · Cobertura por Estación (alerta de punto único de fallo) · Coste de una Baja | Mide COBERTURA operativa (¿hay alguien que pueda cubrir?), no CALIDAD técnica (¿lo hace bien?). No hay prueba práctica, no hay rúbrica de competencias culinarias (cuchillo, cocciones, salsas, emplatado, higiene de manipulación), no hay plan de carrera del cocinero. |
| `quejas-reclamaciones-resenas.xlsx` | Registro de quejas, reclamaciones formales (plazos autonómicos), reseñas, resumen | Vive en sala/atención al cliente. Cuando la causa es de cocina (plato frío, alérgeno, tiempo de espera) no hay enlace hacia una ficha técnica o un registro de incidencia de pase. |
| `seleccion-scorecard-entrevista.xlsx` | Scorecard de competencias GENERALES de contratación, comparativa de candidatos | Sirve para contratar a CUALQUIER puesto; no tiene competencias técnicas de cocina (manejo de cuchillo, conocimiento de técnicas, gestión de partida) como las tendría una entrevista de cocinero/a de partida. |
| `calendario-cumplimiento-legal.xlsx` | Estado Normativo · Calendario y Vencimientos · Documentación Obligatoria · Topes de Jornada · Permisos y Cómputo · Régimen Disciplinario ALEH | Cubre el marco LABORAL completo (también válido para cocina, se reutiliza). No cubre normativa de PROCESO en cocina (fichas técnicas, especificaciones de compra, protocolo de pase). |
| `reuniones-acuerdos-plan-90-dias.xlsx` | Calendario de reuniones, guion de reunión semanal, uno-a-uno, actas, Plan 90 Días | Es la cadencia de gestión del NEGOCIO. No planifica producción de cocina ni desarrollo de carta. |
| `auditoria-interna-servicio.xlsx` | 6 áreas de SERVICIO puntuadas, "excluye APPCC/sanidad a propósito (remite al Pack APPCC)" (`Instrucciones`) | Excluye explícitamente cocina/sanidad. Confirma el hueco: no existe ninguna auditoría interna de ORDEN y OPERACIÓN de cocina en el catálogo. |

### Kit de Tareas (`astro-site/public/dl/kit-tareas/`)

| Fichero | Qué cubre | Qué le falta |
|---|---|---|
| `02-partidas-cocina.xlsx` | Checklists diarios por partida (Calientes, Fríos, Mise en Place): antes/durante/después del servicio, con alérgenos y anisakis ya integrados en las tareas (fila 5 de "Fríos": "prevención de ANISAKIS: confirmar congelación previa ≥24 h a −20 °C…") | Es un checklist de TAREAS DEL DÍA (¿se hizo o no?), no PLANIFICACIÓN DE PRODUCCIÓN (¿cuánto hay que producir hoy según los cubiertos previstos?). No hay proyección de cantidades ni lista de producción cuantificada. |
| `BONUS-01-briefing-servicio.xlsx` | Briefing PRE-SERVICIO de SALA: reservas, ocupación, platos del día, 86s, alérgenos y especiales | Es el briefing de SALA hacia el servicio, responsable "jefe de sala o manager". No es un handover cocina↔cocina entre turnos (relevo, estado de mise en place, incidencias de producción). |

### Pack APPCC (`astro-site/public/dl/pack-appcc/`)

| Fichero | Qué cubre | Qué le falta |
|---|---|---|
| `08-matriz-alergenos.xlsx` | Declaración de los 14 alérgenos POR PLATO de la carta completa, con estado Completo/Falta especie/Sin verificar | Es un registro de CUMPLIMIENTO (¿está declarado?), no una ficha de PROCESO del plato (no lleva pasos, técnica, tiempos, foto ni conservación). |
| `14-fichas-14-alergenos.xlsx` | Cartel/protocolo de referencia de los 14 alérgenos + protocolo de actuación ante reacción | Es un cartel de consulta común a todos los platos, no ficha individual de receta. |
| `12-analisis-peligros-haccp.xlsx` | Los 7 principios APPCC: 21 peligros en 7 fases (Recepción→Servicio), PCC/PPRo, límites críticos, vigilancia, acción correctiva | Es el plan APPCC de LOCAL, no de RECETA. No dice cómo se hace un plato, sólo qué peligro controla en cada fase genérica. |
| `BONUS-01-registro-formacion.xlsx` | Registro de formación OBLIGATORIA en seguridad alimentaria (higiene, alérgenos), con caducidad y estado VIGENTE/RENOVAR/CADUCADO vía `TODAY()` | Es cumplimiento normativo (¿tiene el certificado en vigor?), no desarrollo de COMPETENCIA técnica culinaria. No mide si el cocinero sabe hacer bien una salsa madre o un corte. |

### Kit de Gestión de Personal (`astro-site/public/dl/kit-gestion-personal/`)

| Fichero | Qué cubre | Qué le falta |
|---|---|---|
| `06-evaluacion-desempeno.xlsx` | 10 competencias GENÉRICAS (puntualidad, higiene personal, trabajo en equipo, iniciativa, limpieza del puesto, rapidez, atención al cliente, conocimiento de carta, gestión del estrés, comunicación), escala 1-5, histórico trimestral con tendencia | Sirve para CUALQUIER puesto del restaurante (de hecho el ejemplo relleno es una jefa de partida, pero las 10 competencias no son técnicas de cocina: no hay "dominio de cortes", "control de cocciones", "montaje/emplatado", "gestión de mermas de su partida", "aplicación de la ficha técnica"). |
| `04-onboarding-nuevo-empleado.xlsx` | Checklist de alta: documentación legal, formación obligatoria, equipamiento/accesos, formación operativa, periodo de prueba | Genérico de RR. HH.; no tiene el bloque específico de incorporación de un cocinero a SU partida (rotación por partidas, quién le enseña qué, ficha técnica de los platos que va a hacer). |

### Kit de Inventario (`astro-site/public/dl/kit-inventario/`)

| Fichero | Qué cubre | Qué le falta |
|---|---|---|
| `05-control-mermas.xlsx` | Registro diario de merma POR PRODUCTO (fecha, producto, categoría, cantidad, motivo, coste), análisis por categoría con 10 categorías fijas, dashboard con objetivo 3 % sobre compras, plan de acción con 5 causas típicas | Mide mermas por PRODUCTO/CATEGORÍA de compra, no por PARTIDA/ESTACIÓN de producción. No conecta la merma con lo que esa partida PRODUJO ese día (no hay % de merma sobre producción, sólo sobre compras totales del mes). |
| `04-recepcion-mercancias.xlsx` | Control de recepción con trazabilidad (albarán, lote), semáforo de temperatura por familia normativa, registro de incidencias con proveedor | Cubre RECEPCIÓN (entrada de producto), no el proceso posterior en cocina. ⚠️ Hallazgo colateral (fuera del alcance de construir, pero relevante para no repetirlo en el manual nuevo): la hoja "Verificación Temperaturas" cita **"RD 3484/2000, art. 6"** para comidas preparadas refrigeradas como si estuviera vigente; el bloque legal ya verificado para el Manual del Manager (D8 de su SPEC) confirma que el **RD 3484/2000 está DEROGADO desde el 22-12-2022 por el RD 1021/2022**. No se toca aquí (instrucción: sólo research), pero el guion del Manual del Chef Ejecutivo NO debe heredar esa cita y sí debe usar la norma vigente (art. 30 RD 1086/2020) citada en el contexto común. |

### Guía Food Cost + Ingeniería de Menú (`astro-site/public/dl/guia-food-cost-ingenieria-menu/`)

| Fichero | Qué cubre | Qué le falta |
|---|---|---|
| `ficha-escandallo-base.xlsx` | Ficha de escandallo: ingrediente, cantidad neta/bruta, merma, precio, IVA soportado (informativo, no entra en coste), coste por ración, PVP objetivo, food cost real con semáforo | Es 100 % COSTE. No hay una sola celda de: pasos de elaboración, técnica, tiempos de cocción, alérgenos, foto del plato terminado, temperatura de servicio ni vida útil/conservación. |
| `rendimiento-mermas-producto.xlsx` | Test de Rendimiento (peso bruto→limpio, subproductos, coste neto con/sin aprovechar), Merma de Cocción (crudo→cocinado, sobrecoste), Mi Tabla de Mermas (mermas de referencia por categoría, editable) | Mide rendimiento y coste del INGREDIENTE, no el rendimiento de la PARTIDA en conjunto ni la merma agregada por estación y turno. |

### Kit de Escandallos (`kit-escandallos/01-escandallo-estandar.xlsx`)

Ingrediente/categoría/ud. compra/precio/cantidad/merma/coste, con una celda reservada literalmente
para **"📷 Foto del Plato"** (nota: "Revisar → Desproteger hoja, luego Insertar → Imagen"). Confirma
que el catálogo YA tiene el hueco visual del plato pensado sólo para el escandallo de coste, nunca
para documentar el PROCESO (pasos, técnica, punto de cocción, montaje) — ese hueco sigue vacío en
todo el catálogo.

**Conclusión del inventario**: el catálogo actual resuelve muy bien tres ejes — **coste** (escandallo,
rendimiento, food cost), **cumplimiento normativo de local** (APPCC, alérgenos por plato, recepción) y
**gestión de personas a nivel de negocio** (evaluación genérica, cobertura de turnos, contratación,
legal laboral). El eje que NINGUNA herramienta cubre es el **criterio técnico de cocina**: cómo se
hace un plato con estándar repetible, cuánto hay que producir cada día según la previsión, cómo se
evalúa la destreza real de la brigada, cómo se organiza el desarrollo de carta y el control de calidad
del pase, y cómo se documenta la responsabilidad y el organigrama específicos de cocina.

---

## (b) Riesgos de canibalización concretos

| Par en riesgo | Por qué NO son lo mismo (evidencia) | Regla de no-solape para el manual nuevo |
|---|---|---|
| **Matriz de polivalencia (manager)** ↔ **Evaluación técnica de brigada (chef, propuesta)** | La matriz mide **cobertura** ("¿puede SOSTENER la estación en un servicio lleno?", niveles 0-3 sin prueba) — es la herramienta de PLANIFICACIÓN DE TURNOS del manager. Una evaluación técnica mide **calidad de ejecución** con una prueba práctica puntuada por competencia (cuchillo, cocciones, salsas, emplatado, higiene de manipulación, conocimiento de ficha técnica) y genera un plan de desarrollo INDIVIDUAL, no de cobertura de turno. | La herramienta nueva NO vuelve a preguntar "¿puede cubrir la estación?" (eso ya lo hace `matriz-formacion-polivalencia.xlsx`). Su output (plan de desarrollo por persona) se **cita por referencia** hacia la hoja "Plan de Cross-Training" de esa matriz — no la duplica ni la reconstruye. |
| **Registro de formación APPCC (`BONUS-01`)** ↔ **Plan de formación técnica de cocina** | El registro APPCC es **cumplimiento**: certificado, entidad formadora, fecha de caducidad, estado VIGENTE/RENOVAR/CADUCADO vía `TODAY()`. Es un archivo legal, no un plan de desarrollo. Y la propia matriz de polivalencia YA tiene una hoja "Plan de Cross-Training" (quién enseña qué estación a quién, con fecha objetivo) — un tercer fichero de "plan de formación" sería el TERCERO sobre el mismo asunto. | **Decisión: no se construye un libro de "plan de formación técnica" separado.** Precedente directo en la propia SPEC del Manual del Manager (D3): la hoja de briefing "desaparece (existe 20 veces en el catálogo)". El desarrollo técnico individual vive como una HOJA dentro de la evaluación técnica (ver (c).5), que alimenta —no sustituye— el Plan de Cross-Training existente. |
| **Control de mermas (inventario, `05-control-mermas.xlsx`)** ↔ **Mermas por partida (chef)** | El control de mermas es por **PRODUCTO/CATEGORÍA DE COMPRA** (10 categorías fijas: Cárnicos, Pescados, Lácteos…) y mide el % sobre COMPRAS DEL MES, sin partida ni responsable de producción. Una vista "mermas por partida" necesita otra dimensión: cuánto produjo esa partida ese día/semana y qué % de eso se perdió — es una métrica de RENDIMIENTO DE PRODUCCIÓN, no de compra. | No se reconstruye un registro de mermas alternativo (duplicaría `05-control-mermas.xlsx` línea a línea). La cifra "mermas por partida" del cuadro de mando de cocina (ver (c).1) se **alimenta de un total que el usuario copia** desde su propio registro de mermas (cualquiera de los dos: el de inventario o uno propio), agregado por estación en una hoja nueva y pequeña — nunca vuelve a pedir fecha/producto/motivo línea a línea. |
| **Ficha de escandallo (`ficha-escandallo-base.xlsx`)** ↔ **Ficha técnica de proceso (chef, propuesta)** | El escandallo es exclusivamente COSTE (ingrediente, cantidad, merma, precio, IVA, food cost). No tiene pasos, foto, alérgenos, temperatura de servicio ni conservación. El kit de escandallos ya reserva una celda de foto, pero ligada al coste. | La ficha técnica de proceso **no vuelve a calcular coste**: su fila de "coste por ración" se **enlaza por referencia** a la celda ya calculada en `ficha-escandallo-base.xlsx` (mismo número, una sola fuente), y añade lo que el escandallo no tiene — pasos numerados, técnica, tiempos, punto de cocción, alérgenos (enlazado también a la matriz de alérgenos, no reescrito), temperatura de servicio, conservación y vida útil. |
| **Auditoría interna de servicio (manager)** ↔ **Auditoría interna de cocina (chef, propuesta)** | La del manager dice explícitamente en su hoja Instrucciones: **"excluye APPCC/sanidad a propósito (remite al Pack APPCC)"** y puntúa 6 áreas de SERVICIO (sala). | La auditoría de cocina puntúa áreas DISTINTAS —orden y mise en place, aplicación de fichas técnicas, gestión de mermas por partida, PRL en cocina, alérgenos en el pase— y **remite al Pack APPCC** para todo lo que ya es checklist de cumplimiento sanitario (limpieza, plagas, temperaturas): no reconstruye `15-guia-inspeccion-sanidad.xlsx` ni los registros diarios. |
| **Briefing pre-servicio (`BONUS-01`, kit-tareas)** ↔ **Handover de cocina (idea descartada)** | El briefing de sala ya cubre reservas, 86s y alérgenos/especiales antes del servicio, con responsable "jefe de sala o manager". Un "handover de cocina" turno a turno sería el mismo objeto (parte de traspaso antes/después del servicio) visto desde cocina. | **Se descarta como libro independiente** por el mismo motivo que el D3 de la SPEC del manager retiró la hoja de briefing: ya existe una plantilla de esta familia en el catálogo. Si se necesita matiz de cocina (estado de mise en place, incidencias de producción), se resuelve como una fila más en la lista de producción diaria del libro (c).2, no como un libro o una hoja nueva de briefing. |
| **Registro de recepción de mercancías (inventario)** ↔ **Compras y especificaciones desde cocina** | Cubre la recepción (documental, temperatura, trazabilidad). No cubre la especificación técnica que el chef le da al proveedor (calibre, corte, grado de maduración, formato de envío) ni el criterio de selección de proveedor por partida. | Fuera del alcance de los 6-8 libros de esta sesión (el research no lo trae como prioridad de las 9 ideas de partida); si se aborda en el futuro, la especificación de compra debe VIVIR aparte de la recepción documental y citarla, no fusionarse con `04-recepcion-mercancias.xlsx`. |

---

## (c) Propuesta razonada de 8 libros de Excel nuevos

Convención de familia idéntica a los 7 libros del Manual del Manager (SPEC §2.2, ya verificada en
los ficheros leídos): hoja «Instrucciones» primero, celdas verdes = editables, cero constantes
dentro de fórmula, `IFERROR(...,"")`, semáforos con `ISNUMBER`, «sin dato» = `""`, prohibido
`INDIRECT`/`COUNTA`/`PMT`/`OFFSET`, formatos `#,##0.00 €` / `0.0 %` / `dd/mm/yyyy`, A4 con
`print_setup`, metadata `author='AI Chef Pro'`, datos desde un `datos_ejemplo.py` propio que
**importa** (no copia) `RESTAURANTE`, `ESTACIONES`, `POLIVALENCIA` y `PLANTILLA` del
`manual-manager/datos_ejemplo.py` (que a su vez importa los de la Guía Food Cost) para que los
cuatro productos cuadren entre sí sin una sola cifra nueva inventada. Los 8 libros reutilizan
`motor.py` **tal cual** (`f`, `val`, `verde`, `dv_lista`, `semaforo_isnumber`, `version_line`,
`hoja_instrucciones`, `PARAMETROS`) — cero cambios de helper.

### 1. `cuadro-de-mando-cocina.xlsx` ⭐
- **Hojas**: Instrucciones · Parámetros (objetivos de KPI de cocina por tipo de carta) · Semana (52 filas ISO) · KPI y Definiciones.
- **Inputs**: mermas totales de la semana por partida (6 columnas, una por estación de `ESTACIONES`), tiempos de pase medidos (muestreo manual: minutos desde comanda a servido, por franja), incidencias de alérgenos (nº y gravedad), horas de cocina trabajadas, cubiertos servidos.
- **Fórmulas clave**: % mermas por partida = mermas de la partida ÷ producción estimada de la partida (celda editable, no recalculada desde cero); horas de cocina por cubierto = horas de cocina ÷ cubiertos; tendencia de tiempos de pase con semáforo `ISNUMBER` contra el objetivo de la casa.
- **Decisión que permite tomar**: qué partida concreta se come el margen y si el problema es de producto (food cost, ya lo mide el manager) o de eficiencia de cocina (tiempos, mermas, alérgenos) — un eje que el cuadro semanal del manager NO mide.
- **Reutiliza motor.py**: sí, sin cambios (misma estructura de hoja `Semana` con 52 filas ISO que `cuadro-de-mando-semanal-manager.xlsx`).
- **Diferencia del hermano más parecido** (`cuadro-de-mando-semanal-manager.xlsx`): **no repite ni una sola columna financiera** (nada de ventas, food cost %, labor cost %, prime cost %, ticket medio): esas columnas se **citan por referencia** en la hoja Instrucciones ("el food cost real de la semana vive en `cuadro-de-mando-semanal-manager.xlsx`, hoja Semana"). Aporta sólo KPIs que ese libro no tiene: mermas por partida, tiempos de pase, incidencias de alérgenos, horas de cocina por cubierto.

### 2. `planificacion-produccion-semanal.xlsx` ⭐
- **Hojas**: Instrucciones · Previsión de Cubiertos (por día, desde reservas + histórico) · Producción por Partida (una tabla por cada una de las 6 `ESTACIONES`) · Lista de Producción Diaria (imprimible) · Ajuste por Desviación.
- **Inputs**: cubiertos previstos por servicio, % de mix de venta por plato/familia (de la carta), cantidad de producción unitaria por ración (de la ficha técnica, libro 3), stock de producto ya elaborado.
- **Fórmulas clave**: cantidad a producir = cubiertos previstos × % mix del plato − stock ya elaborado; total de materia prima necesaria = cantidad a producir × cantidad bruta por ración (enlazada a `ficha-escandallo-base.xlsx`, no recalculada); alerta de sobreproducción si la lista del día anterior quedó con sobrante sin vender.
- **Decisión que permite tomar**: cuánto hay que producir HOY en cada partida para no faltar ni sobrar, en vez de producir "por costumbre" (causa raíz nº 1 del propio `Plan de Acción` de `05-control-mermas.xlsx`: "se produce por costumbre, no contra la previsión de cubiertos").
- **Reutiliza motor.py**: sí. Necesita una función de reparto proporcional que ya existe en el patrón de `PARAMETROS`/`dv_lista` (listas desplegables de plato/familia); no requiere helper nuevo.
- **Diferencia del hermano más parecido** (`02-partidas-cocina.xlsx` del Kit de Tareas): ese fichero es un CHECKLIST de tareas (¿se hizo o no, con firma?); este es una PROYECCIÓN CUANTITATIVA (cuánto producir). No se solapan: la lista de producción diaria de este libro puede imprimirse junto al checklist de partidas sin repetir ni una columna.

### 3. `ficha-tecnica-proceso.xlsx` ⭐
- **Hojas**: Instrucciones · Ficha (plantilla a duplicar por plato) · Ficha (ejemplo relleno) · Índice de Fichas.
- **Inputs**: nombre del plato, familia, pasos de elaboración numerados, técnica de cocción, tiempos, punto de cocción, temperatura de servicio, montaje/emplatado (con hueco de foto, igual convención que `01-escandallo-estandar.xlsx`), alérgenos (14 columnas S/T/N idénticas a `08-matriz-alergenos.xlsx`, **enlazadas** a esa matriz cuando el pack APPCC está en la misma carpeta, o repetidas manualmente si no), conservación y vida útil en cámara/congelador.
- **Fórmulas clave**: **ninguna de coste**: la celda "coste por ración" y "food cost real" se enlazan por fórmula externa a `ficha-escandallo-base.xlsx!Ficha!<celda>` cuando el usuario tiene la Guía Food Cost, con `IFERROR(...,"completa con tu escandallo")` si no la tiene.
- **Decisión que permite tomar**: que el plato salga IGUAL lo sirva quien lo sirva — es el estándar de proceso que hoy no existe en ningún fichero del catálogo (el escandallo dice cuánto cuesta, la matriz de alérgenos dice qué lleva, pero nada dice CÓMO se hace).
- **Reutiliza motor.py**: sí (mismo patrón de `verde()` para las celdas editables y `dv_lista()` para el desplegable S/T/N de alérgenos).
- **Diferencia del hermano más parecido** (`ficha-escandallo-base.xlsx`): cero superposición de columnas — el escandallo no toca proceso, esta ficha no recalcula coste. Se presentan como PAREJA en el copy: "escandallo (cuánto cuesta) + ficha técnica de proceso (cómo se hace)".

### 4. `organigrama-cocina-raci.xlsx`
- **Hojas**: Instrucciones · Organigrama de Cocina (puestos y niveles: chef ejecutivo/corporativo, jefe de cocina, sous chef, jefe de partida, cocinero, ayudante/auxiliar — con la equivalencia LATAM la primera vez) · Descripción de Puestos (responsabilidades por puesto) · Matriz RACI Cocina↔Sala↔Dirección (decisiones típicas: cambio de carta, 86 de un plato, incidencia de alérgeno, compra de producto fuera de escandallo, ficha técnica nueva).
- **Inputs**: nombres/puestos de la plantilla (reutiliza `PLANTILLA` de `datos_ejemplo.py`), lista de decisiones tipo (editable).
- **Fórmulas clave**: ninguna de cálculo; es una matriz de texto con validación de datos (`dv_lista` para R/A/C/I por celda) y formato condicional por rol.
- **Decisión que permite tomar**: quién decide qué cuando cocina, sala y dirección no coinciden (ej. quién autoriza un 86, quién aprueba una ficha técnica nueva antes de subirla a carta) — el organigrama del cap. 01 del Manual del Manager es de NEGOCIO completo (con el ALEH VI real); este es el de COCINA con el cruce operativo con sala/dirección que aquél no baja a ese detalle.
- **Reutiliza motor.py**: sí (`dv_lista`, `hoja_instrucciones`).
- **Diferencia del hermano más parecido** (organigrama del cap. 01 del Manual del Manager, que vive en TEXTO del capítulo, no en xlsx): no hay fichero xlsx de organigrama en todo el catálogo actual — cero riesgo de duplicar una hoja de cálculo existente; el riesgo es de CONTENIDO (no repetir la cita del ALEH VI ya escrita en el Manual del Manager: se cita por referencia "ver Manual del Manager, cap. 01").

### 5. `evaluacion-tecnica-brigada.xlsx` ⭐
- **Hojas**: Instrucciones · Rúbrica de Competencias Técnicas (cuchillo/cortes, cocciones, salsas y fondos, emplatado/montaje, higiene de manipulación, conocimiento de ficha técnica, gestión de mermas de su partida — puntuación 1-5 con prueba práctica, NO las 10 genéricas de `06-evaluacion-desempeno.xlsx`) · Prueba Práctica (guion de la prueba: plato a elaborar, tiempo máximo, criterios) · Plan de Desarrollo Individual · Histórico.
- **Inputs**: puntuación por competencia (prueba práctica, no autoevaluación), fecha, evaluador.
- **Fórmulas clave**: media ponderada por competencia (pesos editables según el puesto: un ayudante no pesa igual "gestión de mermas" que un jefe de partida), semáforo de nivel, columna "próxima estación a aprender" que **remite** (no repite) a la fila de esa persona en `matriz-formacion-polivalencia.xlsx!Plan de Cross-Training`.
- **Decisión que permite tomar**: a quién promocionar, a quién formar en qué técnica y quién no supera el periodo de prueba en su partida — con una prueba práctica puntuada, no con una opinión.
- **Reutiliza motor.py**: sí (mismo patrón de `06-evaluacion-desempeno.xlsx`: media que ignora N/A, histórico con tendencia).
- **Diferencia del hermano más parecido** (`06-evaluacion-desempeno.xlsx` del Kit de Gestión de Personal): ese es GENÉRICO (puntualidad, higiene personal, trabajo en equipo…) y vale para cualquier puesto del restaurante; este es TÉCNICO DE COCINA con prueba práctica y ligado a la partida. El manual explica cuándo usar cada uno (evaluación general de comportamiento → Kit de Gestión de Personal; evaluación técnica de oficio → este libro).

### 6. `desarrollo-carta-control-calidad.xlsx`
- **Hojas**: Instrucciones · Calendario de Temporada (hitos: prueba de plato, coste, ficha técnica, formación del equipo, lanzamiento — con fecha objetivo por hito) · Registro de Pruebas de Plato (fecha, plato probado, resultado, ajustes, coste de la prueba) · Control de Calidad del Pase (muestreo de platos servidos: temperatura de emplatado, tiempo de espera, conformidad con la ficha técnica, devoluciones).
- **Inputs**: fechas de hito por plato nuevo, resultado de cada prueba, muestreo de calidad del pase (frecuencia editable).
- **Fórmulas clave**: días hasta el próximo hito (idéntica lógica de fechas que `Plan de Cross-Training`), % de conformidad del pase, alerta si un plato lleva más de N días "en prueba" sin ficha técnica cerrada.
- **Decisión que permite tomar**: si la carta se renueva con MÉTODO (probar→costear→documentar→formar→lanzar) en vez de "porque lo dice el chef", y si lo que sale del pase es lo que dice la ficha.
- **Reutiliza motor.py**: sí (fechas objetivo con el mismo patrón que `Plan de Cross-Training` y `Calendario y Vencimientos`).
- **Diferencia del hermano más parecido**: no existe nada parecido en el catálogo (confirmado también por L2-SERP: "ni una sola de las 20 fuentes une… planificación… calendario de temporada… control de calidad" en la SERP española). Fusiona 3 ideas del research original (calendario de cartas + registro de pruebas + control de calidad del pase) en UN libro para no salirse del rango de 6-8.

### 7. `plan-desperdicio-ley-1-2025.xlsx`
- **Hojas**: Instrucciones · Jerarquía de Prevención (las opciones que marca la ley: prevenir→redistribuir/donar→alimentación animal→compostaje, en ese orden) · Registro de Donaciones y Doggy Bag · Panel de Cumplimiento (qué obliga a este local según su tamaño, con la distinción ya verificada: la exención de 1.300 m² **sólo** alcanza al apartado 4 del art. 6, el resto obliga a todo restaurante que no sea microempresa).
- **Inputs**: cantidad donada/mes, nº de doggy bags entregados, tamaño del local (m²), forma jurídica (para el criterio de microempresa).
- **Fórmulas clave**: ninguna de coste; es un panel de checklist con semáforo de cumplimiento por apartado del art. 6, citando norma y fecha de verificación en cada fila (mismo patrón "Verificado el 04-09-2026 · norma · URL" que `calendario-cumplimiento-legal.xlsx`).
- **Decisión que permite tomar**: qué obliga y qué no a ESTE local concreto (ninguna herramienta del catálogo aterriza hoy la Ley 1/2025 a una checklist operativa desde cocina; el Manual del Manager sólo la EXPLICA en texto, cap. 19).
- **Reutiliza motor.py**: sí (`semaforo_isnumber`, `dv_lista` para el desplegable de forma jurídica).
- **Diferencia del hermano más parecido** (`05-control-mermas.xlsx`): esa mide COSTE de la merma para el negocio; este mide CUMPLIMIENTO legal de qué se hace con el excedente. No se tocan: una merma de cocina (producto que se tira) no es lo mismo que un excedente servible que la ley obliga a poder donar o embolsar.

### 8. `auditoria-interna-cocina.xlsx`
- **Hojas**: Instrucciones · Auditoría (puntos en 4-5 áreas: orden y mise en place, aplicación de fichas técnicas, gestión de mermas por partida, PRL en cocina, alérgenos en el pase — EXCLUYE explícitamente limpieza/plagas/temperaturas, que ya cubre el Pack APPCC) · Resumen por Área · Histórico.
- **Inputs**: puntuación por punto de auditoría (mismo formato que `auditoria-interna-servicio.xlsx`).
- **Fórmulas clave**: idénticas en estructura a `auditoria-interna-servicio.xlsx` (semáforo por área, histórico).
- **Decisión que permite tomar**: puntuar la disciplina de cocina (no la sanitaria, que ya se audita con el Pack APPCC) con una cadencia propia, y verla junto a la auditoría de servicio del manager para tener las dos caras del negocio.
- **Reutiliza motor.py**: sí, 100 % (mismo esqueleto que su hermano).
- **Diferencia del hermano más parecido** (`auditoria-interna-servicio.xlsx`): áreas completamente distintas y frontera explícita con el Pack APPCC igual que hace el original con el servicio ("remite al Pack APPCC" para todo lo sanitario).

**Candidatos descartados del listado original de 9-10 ideas** (para no exceder 8 libros y no
duplicar lo que ya existe): *briefing/handover de cocina* (redundante con `BONUS-01-briefing-servicio.xlsx`
y con el precedente D3 de la propia SPEC del manager) y *plan de formación técnica independiente*
(redundante con el "Plan de Cross-Training" ya existente en `matriz-formacion-polivalencia.xlsx`;
absorbido como columna de salida en el libro 5). *Calendario de cartas* y *registro de pruebas de
plato + control de calidad del pase* se fusionaron en un solo libro (6).

---

## (d) Qué del pipeline se reutiliza tal cual y qué hay que tocar

**Se reutiliza al 100 %, sin tocar una línea:**
- `guias-v2_0/motor.py` — los 8 libros usan exactamente `f()`, `val()`, `verde()`, `dv_lista()`,
  `semaforo_isnumber()`, `version_line()`, `hoja_instrucciones()`, `PARAMETROS` (confirmado
  `motor.py:203,231,245,297,541,613,1669`; `COUNTA`/`PMT` ya están fuera del alcance del motor,
  documentado en su cabecera).
- `guias-v2_0/documentos.py` — `tipo_doc='manual'`, `tipo_doc_art`, `tipo_doc_dem`, `categoria_doc`
  **ya están parametrizados** desde D19 de la SPEC del Manual del Manager (confirmado en
  `documentos.py:1003,1039,1943`: el residuo "esta guía" sólo aparece como valor por DEFECTO de
  `guia.get(...)`, nunca hardcodeado). Cero cambios de código: basta con que el nuevo `guion_*.py`
  rellene esas claves, exactamente como ya hace `guion_manual_manager_restaurante.py:88-95`.
- `guias-v2_0/dump_prompts.py` y `guias-v2_0/check_bloque.py` — genéricos por `--producto <pid>`,
  no requieren ningún cambio.
- El patrón de blog: `scripts/astro-migration/fase8g-manual-manager-blog.py` es la plantilla a
  clonar (igual que él mismo se clonó de `fase8f`, según D16 de la SPEC del manager) con
  `PRODUCTO`/`HOY`/`PRIORIDAD_SUSTITUIR`/`NUNCA` propios.

**Hay que crear (no tocar, CREAR de cero, siguiendo el molde exacto):**
- `scripts/productos-digitales/manual-chef-ejecutivo-SPEC.md` (molde: `manual-manager-SPEC.md`).
- `scripts/productos-digitales/guias-v2_0/guion_manual_chef_ejecutivo.py` (molde: `guion_manual_manager_restaurante.py`, con su propio `CAPITULOS`, `BONUS` y `NO_COMUN` — el `NO_COMUN` de cocina necesita SU PROPIA lista negra: normativa de alérgenos, anisakis, aceites de fritura, PRL específico de cocina, que aún no se ha verificado con la misma exhaustividad que el laboral del Manual del Manager — pendiente de una lente 3 legal específica de cocina, ya señalado como hueco en el contexto de esta tarea).
- `scripts/productos-digitales/manual-chef-ejecutivo/datos_ejemplo.py` — **debe importar**, no
  reinventar, `RESTAURANTE`, `ESTACIONES`, `POLIVALENCIA` y `PLANTILLA` desde
  `manual-manager/datos_ejemplo.py` (que a su vez importa de `guia-food-cost/datos_ejemplo.py` vía
  `importlib.util`, patrón ya usado y confirmado en su cabecera) para que los 8 libros cuadren con
  los 7 del manager y los de la Guía Food Cost sin inventar una sola cifra nueva de "La Encina".
- 3 constructores opus de xlsx (siguiendo el reparto de la SPEC del manager: "libros 1-2 · 3-4 ·
  5-6-7-8"), un refutador de los xlsx y un fixer — mismo reparto de modelos que §7 de la SPEC del
  manager.
- Una investigación **legal específica de cocina** (ids nuevos, p. ej. `CE-*`, en un JSON hermano de
  `guias-v2-research-sector.json`): PRL en cocina (arts. 19/22 Ley 31/1995 ya verificados para el
  manager, pero aplicados a maquinaria de cocina, quemaduras, cortes), normativa de ficha técnica
  y etiquetado, aceites de fritura (Orden 26-01-1989, ya verificada), anisakis y temperaturas
  (RD 1086/2020 art. 30, ya verificado) — **gran parte del bloque legal YA está verificado** para el
  Manual del Manager y se reutiliza citando el mismo id; sólo falta lo estrictamente de PROCESO de
  cocina que ese manual no tocó (especificaciones de compra, normativa de ficha técnica si existe).

---

## (e) Huecos técnicos de la capa de producto para el slug `manual-chef-ejecutivo`

`robots.txt` **no necesita ningún cambio**: las reglas `Disallow: /manual-*-access` y
`Disallow: /manual-*-library` (confirmado en `astro-site/public/robots.txt:39-40,57-58,75-76,93-94,111-112`)
son un comodín que ya cubre cualquier slug que empiece por `manual-`, incluido
`manual-chef-ejecutivo-access`/`-library`.

Ficheros a CREAR:

| Fichero | Qué añadir |
|---|---|
| `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts` | Landing `GuiaData` nueva, molde exacto `manual-manager-restaurante.ts` (mismas reglas de copy: sin `priceOld`/`aggregateRating`, `testimonials.items: []`, ancla externa homogénea si aplica, vocabulario con equivalencia LATAM la primera vez). |
| `astro-site/src/pages/manual-chef-ejecutivo.astro` | Wrapper de landing (molde: `manual-manager-restaurante.astro:23`, con `VITE_STRIPE_PAYMENT_LINK_MANUAL_CHEF_EJECUTIVO`). |
| `astro-site/src/pages/manual-chef-ejecutivo-access.astro` | Molde: `manual-manager-restaurante-access.astro`. |
| `astro-site/src/pages/manual-chef-ejecutivo-library.astro` | Molde: `manual-manager-restaurante-library.astro`. |
| `src/pages/ManualChefEjecutivoAccessGate.tsx` | Wrapper de `ProductAccessGate` (molde: `ManualManagerAccessGate.tsx`). |
| `src/pages/ManualChefEjecutivoDashboard.tsx` | Dashboard con Manual (2) · Herramientas (8) · Bonus (2) (molde: `ManualManagerDashboard.tsx`). |

Ficheros a EDITAR (añadir una entrada, sin tocar las existentes):

| Fichero | Qué añadir |
|---|---|
| `astro-site/src/lib/zona-app.ts` (`zona-app.ts:88` es el molde) | Nueva fila `{ productId: 'manual-chef-ejecutivo', accessPath: '/manual-chef-ejecutivo-access', libraryPath: '/manual-chef-ejecutivo-library', landingPath: '/manual-chef-ejecutivo', storageKey: 'manual-chef-ejecutivo-jwt', productLabel: 'Manual del Chef Ejecutivo', gateComponent: 'ManualChefEjecutivoAccessGate', dashboardComponent: 'ManualChefEjecutivoDashboard' }` — producto 47. |
| `src/App.tsx` (líneas 161-162 y 866-871 son el molde) | Import + 2 rutas (`-access`, `-library`; landing nativa Astro, sin ruta SPA, igual que el manager). |
| `netlify/functions/verify-purchase.ts:161` | Entrada `'manual-chef-ejecutivo': { accessPath: ... }`. |
| `netlify/functions/resend-access.ts:162` | Misma entrada. |
| `netlify/functions/admin-generate-access.ts:28` | Misma entrada (fallback admin). |
| `netlify/functions/get-download-urls.ts:301-312` | Entrada con `manual-pdf`, `manual-docx`, `bonus-pdf`, `bonus-docx` + 8 claves de herramienta (`cuadro-cocina`, `plan-produccion`, `ficha-tecnica-proceso`, `organigrama-raci`, `evaluacion-tecnica`, `desarrollo-carta`, `plan-desperdicio`, `auditoria-cocina`). |
| `src/data/productos-digitales-config.ts:975-997` | Misma estructura, producto 47. |
| `src/data/products-catalog.ts:307-316` | Nueva entrada `'manual-chef-ejecutivo'` (id, url, price, name es/en, description es/en) — **con `en` relleno aunque no haya landing inglesa**, igual que hace hoy `manual-manager-restaurante` (`products-catalog.ts:311`). |
| `src/pages/ProductosDigitales.tsx:927` | Retirar la entrada de `comingSoon` y añadirla al array de productos LIVE del hub (D18-equivalente). |
| `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:942` | Mismo retiro de `comingSoon` + alta en productos live. |
| `astro-site/src/lib/linkify-use-case.ts:29-30` | Añadir `'Manual del Chef Ejecutivo': '/manual-chef-ejecutivo'`. |
| `src/lib/linkify-use-case.tsx` | Misma entrada (vista parcial de la SPA; mantener paridad con la de Astro). |
| `src/data/productos-changelog.ts:100-118` (molde: entradas `manual-manager-restaurante` y `guia-food-cost-ingenieria-menu`) | Entrada nueva, versión 1.0. |
| `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts:188-197` | Añadir `{ label: 'Manual del Chef Ejecutivo', href: '/manual-chef-ejecutivo' }` a su `footerLinks` (cross-sell recíproco). |
| `astro-site/src/data/productos/kits/kit-gestion-personal.ts:305-313` | Añadir la misma fila (ya enlaza con el Manager; falta el Chef). |
| `astro-site/src/data/productos/tareas/kit-tareas.ts:392-399` | Ídem. |
| `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:176-183` | Ídem (ya enlaza con Manager; falta el Chef). |
| `astro-site/src/data/productos/kits/pack-appcc.ts:294-299` | Añadir enlace al Chef **y de paso** al Manager (hueco preexistente: hoy `pack-appcc.ts` no enlaza a `manual-manager-restaurante` tampoco). |
| `src/data/use-cases-content.es.ts` (patrón `productIds`/`productsTitle` confirmado en la entrada `sous-chef`) | Añadir `productIds` (hoy **vacío** en las 4 páginas de rol que más importan a este producto: `chef-ejecutivo`, `chef-cocina`, `chef-catering`, `fb-manager-hotel`) incluyendo `'manual-chef-ejecutivo'` junto con los kits ya relevantes (`kit-escandallos`, `pack-appcc`, `kit-tareas`) — hueco de cross-sell preexistente, no causado por este lanzamiento, pero el sitio natural para cerrarlo a la vez. |
| `scripts/astro-migration/fase8g-manual-manager-blog.py` | Clonar a `fase8g-manual-chef-ejecutivo-blog.py` con `PRODUCTO`/`HOY`/`PRIORIDAD_SUSTITUIR` propios (D16-equivalente). |

**Nota de nomenclatura de rol verificada**: el `id` interno es `chef-cocina` pero el **slug real en
español** es `chef-jefe-cocina` (`src/data/use-cases.ts`, bloque `id: 'chef-cocina'` → `slug.es:
'chef-jefe-cocina'`), no `chef-cocina` como sugería el contexto de la tarea. Cualquier enlace interno
nuevo debe usar `/usos/rol/chef-jefe-cocina`, verificado por `ls`/grep antes de publicar (regla D15
del manager).

**Env var Stripe**: `VITE_STRIPE_PAYMENT_LINK_MANUAL_CHEF_EJECUTIVO`, añadida por John en Netlify
(scope builds, todos los contextos) tras crear el Payment Link; `sync-payment-links.py` la recoge
solo con que el fichero de landing exista en `productos/manuales/` (glob ya cubierto, D20 del manager).

---

## (f) Posicionamiento y cross-sell explícito en las dos direcciones

**Frontera de producto (para el copy y para el guion, no se reabre en esta sesión):** el Manual del
Manager gobierna NEGOCIO/SALA — cuadrante, jornada, contratación, quejas, cumplimiento legal
transversal, cuadro de mando financiero. El Manual del Chef Ejecutivo gobierna COCINA — brigada y
partidas, producción, estandarización (ficha técnica de proceso), responsabilidad real de seguridad
alimentaria y alérgenos desde dentro de cocina, PRL de cocina, compras/especificaciones desde cocina,
desarrollo de carta con criterio de coste, evaluación técnica y KPIs de cocina, relación
cocina↔sala↔dirección. Los DOS comparten el mismo caso modelado («La Encina», 12 personas, 6
estaciones) y el mismo marco legal laboral base (ALEH VI, jornada, permisos), que el manual del chef
**cita por capítulo, no reescribe**.

**Cross-sell MANUAL DEL CHEF → catálogo existente** (a incluir en cap. 01 del guion nuevo, tabla
"qué incluye este pack / qué es cross-sell", mismo patrón que D4 del Manual del Manager):
- **Manual del Manager de Restaurante (55 €)** — el lado negocio/sala/ley que este manual no repite; cita expresa: "quien dirige el negocio completo, no sólo cocina, necesita los dos".
- **Pack APPCC (14 €)** — todos los REGISTROS diarios de cumplimiento (temperaturas, limpieza, plagas, trazabilidad): el manual da el criterio, el pack da el papel que hay que rellenar cada día.
- **Kit de Tareas (12 €)** — los checklists operativos del día a día por partida (`02-partidas-cocina.xlsx`), que el manual complementa con planificación y estandarización, no sustituye.
- **Guía Food Cost + Ingeniería de Menú (55 €)** — el escandallo y el rendimiento/mermas por ingrediente, que la ficha técnica de proceso enlaza por referencia en vez de recalcular.
- **Kit de Gestión de Personal (14 €)** y **Kit de Inventario (14 €)** — evaluación GENERAL y control de mermas por PRODUCTO respectivamente, frente a la evaluación TÉCNICA y las mermas por PARTIDA del manual nuevo.

**Cross-sell catálogo existente → MANUAL DEL CHEF** (footerLinks y páginas de rol, tabla (e)):
- `manual-manager-restaurante.ts`, `kit-gestion-personal.ts`, `kit-tareas.ts`,
  `guia-food-cost-ingenieria-menu.ts` y `pack-appcc.ts` — añadir el enlace recíproco (hoy sólo 3 de
  los 5 enlazan al Manager, y NINGUNO enlaza todavía al Chef porque el producto no existe).
- Páginas de rol `/usos/rol/chef-ejecutivo-corporativo`, `/usos/rol/chef-jefe-cocina`,
  `/usos/rol/chef-catering`, `/usos/rol/fb-manager-hotel` — las 4 tienen HOY `productIds` **vacío**
  (verificado en `use-cases-content.es.ts`: sólo `sous-chef` trae `productIds: ['kit-tareas',
  'kit-escandallos', 'pack-appcc', 'pro-prompts-ebook', 'kit-inventario', 'kit-gestion-personal']`).
  Es el hueco de cross-sell más grande y más barato de cerrar: cuatro páginas de rol construidas
  para el público exacto de este producto, sin un solo banner de producto hoy.
- Blog: los 12 posts de contexto **ya tienen sus 3 banners** (`fase8e-banners-corpus.py`, verificado
  con `utm_medium=banner` = 3 en los 12 ficheros). El más on-topic para una inserción contextual
  adicional —no un cuarto banner, sino un enlace de texto o el intercambio de uno de los tres— es
  `libreria-de-prompts-para-chef-ejecutivo-pro-ai.md` (agente "Chef Ejecutivo Pro AI" ya vivo en la
  plataforma, título literal "Chef Ejecutivo"), seguido de `escandallos-ia-cocina-profesional`,
  `que-son-las-mermas-en-cocina`, `tipos-de-cortes-en-la-cocina-profesional`,
  `de-chef-tradicional-a-chef-ia` y la familia de alérgenos (`alergenos`,
  `ia-gestion-alergenos-hosteleria`, `gestion-de-alergenos-con-ia-en-restaurantes`). Decisión
  pendiente de John (igual que D16 del manager): clonar `fase8g` y decidir si sustituye uno de los
  3 banners existentes en 5 de estos posts o añade enlace contextual sin tocar el cupo de 3.

---

## Huecos de esta lente (no se pudo medir / queda para otra sesión)

- No se ha hecho research legal específico de cocina (PRL de maquinaria, normativa de ficha técnica,
  responsabilidad penal/administrativa del jefe de cocina en intoxicaciones) — pendiente de una
  lente legal dedicada antes de escribir el `guion_manual_chef_ejecutivo.py` y su `NO_COMUN`.
- No se han verificado los otros 39 xlsx del catálogo que no estaban en el alcance de esta lente
  (p. ej. el resto de `kit-tareas-*` por concepto, o `03-tareas-manager.xlsx`); el barrido se limitó
  a los 15 ficheros que el encargo señaló como frontera más probable.
- No se ha comprobado si `use-cases-content.{en,fr,de,it,pt,nl}.ts` replican el mismo hueco de
  `productIds` vacío en las páginas de rol equivalentes (D21 del Manager: este producto es sólo ES,
  pero las páginas de rol si existen en otros idiomas podrían enlazar igualmente al Kit/Pack en
  español con nota de idioma, fuera del alcance de esta lente).
- No se ha contado cuántas veces aparece la cita "RD 3484/2000, art. 6" en el resto del catálogo
  (sólo se detectó en `04-recepcion-mercancias.xlsx`, hoja "Verificación Temperaturas"); si se
  decide corregirla, requiere un censo aparte con `grep` sobre los xlsx del catálogo completo.

Via: Claude Code
