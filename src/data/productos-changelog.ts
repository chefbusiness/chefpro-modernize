// Versionado y changelog de los productos digitales (dashboards post-pago).
//
// Cada producto que se repara/mejora recibe una entrada aquí; el dashboard la pinta
// con <ProductVersionBadge/> (cabecera) y <ProductChangelog/> (bloque "Novedades").
// El acceso es de por vida: el cliente vuelve a descargar y tiene la última versión.
// Patrón portado de chefbusiness-astro (src/data/productos-changelog.ts) el 2026-08-18.
//
// Fechas en ISO (YYYY-MM-DD). Los textos van al cliente: sin notas internas de
// construcción («antes decía…»), sin cifras que haya que sincronizar con los ficheros.

export interface ProductChangelogEntry {
  version: string;
  date: string; // ISO
  title: string;
  changes: string[];
}

export interface ProductChangelogData {
  version: string; // versión vigente
  updated: string; // ISO de la última actualización
  entries: ProductChangelogEntry[]; // de más reciente a más antigua
}

export const PRODUCT_CHANGELOGS: Record<string, ProductChangelogData> = {
  'kit-tareas-pasteleria': {
    version: '2.0',
    updated: '2026-08-21',
    entries: [
      {
        version: '2.0',
        date: '2026-08-21',
        title: 'Cuatro plantillas nuevas y el kit convertido en un sistema',
        changes: [
          'Nueva plantilla 10 — Plan de Producción Semanal + Control de Mermas: previsión por producto y partida (Lun–Dom), producido vs vendido, merma en % y en euros, y resumen semanal por partida con semáforo.',
          'Nueva plantilla 11 — Ficha de Encargo + Registro de Encargos: ficha imprimible con alérgenos, señal y pendiente, registro mensual, agenda semanal de entregas y aviso RGPD.',
          'Nueva plantilla 12 — Alérgenos de Vitrina (14 UE): matriz de partida con más de 30 productos de pastelería para verificar con tus fichas técnicas, carta de alérgenos, cartel para la tienda y etiquetas de vitrina imprimibles.',
          'Nueva plantilla 13 — Registro de Temperaturas, Recepción de Mercancía y Etiquetas de Elaborado: hoja mensual por equipo con rangos objetivo, control de recepción con criterios de rechazo y etiquetas con vidas útiles orientativas.',
          'Apertura y Cierre del Negocio rediseñado para pastelería con tienda: vitrinas, etiquetado, encargos del día, sobrante y comprobaciones finales de obrador.',
          'Apertura y Cierre de Caja: descuadre diario frente a la Z del TPV en el registro mensual y formatos de moneda.',
          'Eventos y Festivos: campañas de Todos los Santos y comuniones, y cierre post-campaña (sobrante, mermas, qué se vendió).',
          'Referencias cruzadas entre plantillas: cada tarea que remite a una ficha, un registro o un control cita la plantilla por su número.',
          'Columna de marca unificada en las 15 plantillas: «✓ Completada» con desplegable ✓ / — / N/A, resaltado en verde al marcar y total que se recalcula si añades o quitas tareas (antes «Hecha» con total fijo).',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-18',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Casilla de completado unificada: se marca con ✓ en la columna «Hecha» (desplegable) y el total de tareas completadas se calcula solo; la primera columna pasa a numerar las tareas.',
          'Los totales y cálculos se ven también en el móvil y en visores que no recalculan (valores guardados en el fichero).',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Correcciones de un jefe de obrador: amasado corto y temperatura de la masa de croissant, entremets congelados el día anterior para el glaseado, campaña de roscón (venta de la tarde del 5 de enero), torrijas y monas de Pascua en sus fechas reales, Black Friday como fecha variable.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
      {
        version: '1.0',
        date: '2026-03-21',
        title: 'Lanzamiento',
        changes: [
          '9 plantillas de checklists operativos para pastelería / obrador + 2 bonus (briefing de servicio y calendario anual).',
        ],
      },
    ],
  },
  'guia-dark-kitchen': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 3 plantillas',
        changes: [
          'Calculadora de viabilidad: corregidos el margen bruto, el EBITDA y el food cost de los escenarios, que se calculaban sobre las celdas equivocadas.',
          'Corregidas etiquetas de la calculadora que Excel abría con error (#¿NOMBRE?): ahora se guardan como texto, no como fórmula rota.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 3 ficheros.',
        ],
      },
    ],
  },
  'guia-panaderia-obrador': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'manual-manager-restaurante': {
    version: '1.0',
    updated: '2026-09-04',
    entries: [
      {
        version: '1.0',
        date: '2026-09-04',
        title: 'Lanzamiento',
        changes: [
          'Manual completo en PDF y en DOCX editable: 20 capítulos de criterio para dirigir un restaurante o un turno — operación del día, personas, números, servicio y cumplimiento legal.',
          '7 herramientas Excel con fórmulas vivas: cuadro de mando semanal, matriz de formación y polivalencia, quejas y reseñas, scorecard de selección, calendario de cumplimiento legal, reuniones con plan de 90 días y auditoría interna de servicio.',
          'Bloque normativo actualizado a 4 de septiembre de 2026, incluida la modificación del convenio estatal de hostelería publicada ese mismo día. Cada tabla legal lleva al pie norma, enlace a la fuente oficial y fecha de verificación.',
          'Los datos normativos (tipos de cotización, topes, plazos y periodicidades) nunca viven dentro de una fórmula: van en casillas editables con su nota y su fecha, y hay una hoja de estado normativo con fecha de corte.',
          'Bonus: 12 situaciones resueltas del manager, cada una con qué NO hacer, protocolo, norma aplicable, herramienta del pack y el guion literal de la conversación cuando la hay.',
        ],
      },
    ],
  },
  'guia-food-cost-ingenieria-menu': {
    version: '1.0',
    updated: '2026-09-03',
    entries: [
      {
        version: '1.0',
        date: '2026-09-03',
        title: 'Lanzamiento',
        changes: [
          'Guía completa en PDF y en DOCX editable: 20 capítulos de método para escandallar, poner precio y decidir qué hacer con cada plato de la carta.',
          '8 herramientas Excel con fórmulas vivas: ficha de escandallo, rendimiento y mermas, precio objetivo multi-método, matriz de carta, simulador multicanal, carta de bebidas, cuadro de mando de prime cost y plan de acción de 90 días.',
          'El IVA por canal (sala, para llevar y delivery) va en casillas editables de los libros, con la base legal citada en la guía: cambias el tipo y todo se recalcula.',
          'Bonus: 12 ejercicios resueltos paso a paso, con los mismos platos de ejemplo que las herramientas.',
        ],
      },
    ],
  },
  'guia-restaurante-casual': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Cash-flow: corregido el margen de contribución mensual.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'guia-restaurante-gastronomico': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 18 plantillas',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 18 ficheros.',
        ],
      },
    ],
  },
  'guia-restaurante-japones': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Cash-flow: corregido el margen de contribución mensual.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'guia-restaurante-mexicano': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Cash-flow: corregido el margen de contribución mensual.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'guia-restaurante-nikkei': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Cash-flow: corregido el margen de contribución mensual.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'guia-restaurante-peruano': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 15 plantillas',
        changes: [
          'Cash-flow: corregido el margen de contribución mensual.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 15 ficheros.',
        ],
      },
    ],
  },
  'kit-escandallos': {
    version: '2.0',
    updated: '2026-08-22',
    entries: [
      {
        version: '2.0',
        date: '2026-08-22',
        title: 'Motor de escandallo unificado + nuevo bono',
        changes: [
          'Corregido el factor de conversión en las 17 filas con unidad de compra distinta de la unidad de uso: el coste real ya no se calcula ×1.000 de más.',
          'La merma ahora se rellena sola al elegir la categoría del ingrediente (carne, pescado, verdura…), con el estándar de la hoja «Mermas» de cada plantilla.',
          'IVA visible en una celda propia y PVP con IVA calculado aparte del PVP sin IVA.',
          'Hojas protegidas SIN contraseña: sólo las celdas verdes se escriben, las fórmulas no se pueden borrar sin querer. Revisar → Desproteger hoja para tocar el resto.',
          'Food cost objetivo único por libro: se edita en el Resumen y todas las pestañas lo leen de allí, así que ya no hay dos objetivos distintos para el mismo menú.',
          'Zona de foto del plato utilizable de verdad, y todas las hojas con gráfico imprimen la gráfica junto a la tabla.',
          'Menú Degustación amplía a 9 pases: los cinco de siempre con ejemplo y cuatro libres con la rejilla completa, que no cuentan hasta que los rellenas.',
          'Menú del Día: nueva hoja de rotación semanal de lunes a viernes, con el coste, el PVP y el food cost de cada día y la media de la semana.',
          'Cafetería/Brunch: nueva receta de carrot cake escandallada por tanda de 12 raciones, con el coste y el PVP por porción.',
          'Cócteles: nueva hoja «Formatos de Compra» que pasa el precio de la botella de la factura al €/litro que pide el escandallo — y que ahora alimenta directamente el precio de los destilados, el vino y el espumoso.',
          'Pastelería: rendimiento por tanda con coste y PVP POR UNIDAD, que es lo que va a la vitrina, no el total de la receta.',
          'Catering: dos hojas nuevas — la checklist del evento (con desplegable y contador de tareas) y un presupuesto listo para enviar al cliente, sin costes ni margen a la vista.',
          'Catering: el presupuesto se calcula por bloques. El food cost objetivo se aplica sólo a la comida; el personal, el menaje, el transporte y el montaje van a coste más un margen de servicios editable, con mínimo de facturación por evento.',
          'Food Truck: nueva hoja de punto de equilibrio diario — cuántas unidades hay que vender y con qué facturación para cubrir los costes fijos del día.',
          'Calculadora de PVP: nueva fila de delivery con la comisión de la plataforma descontada antes del precio, y columna de multiplicador para calcular a ojo.',
          'Control de Mermas: semáforo OK/ALERTA por categoría y hoja de evolución del desperdicio a 12 semanas con gráfico.',
          'Food cost REAL en cada escandallo: escribe el PVP que ya cobras en carta y la hoja te dice tu food cost de verdad, en rojo si supera tu objetivo. Es el cálculo inverso al PVP sugerido.',
          'Dashboard mensual: se añaden stock inicial y stock final, y el food cost pasa a calcularse sobre el CONSUMO (stock inicial + compras − stock final) en vez de sobre las compras del mes. El gráfico anual y la tabla salen ya dentro del área de impresión.',
          'Bonus de inventario: nueva hoja «Ventas del periodo» que calcula el consumo teórico a partir de lo que vendiste, y el desvío contra el consumo real valorado en euros — la pérdida oculta, en dinero y ordenada de mayor a menor.',
          'Control de Mermas: la columna de referencia pasa a ser el DESPERDICIO sobre la compra (2-8 % según familia), no la merma de despiece. Si venías de la versión anterior, revisa lo que anotabas: la merma de limpieza y despiece ya va dentro del coste del plato, en la hoja «Mermas» de cada escandallo.',
          'Nuevo bono: guía "Controla tu Food Cost en 30 Días" en PDF — plan semana a semana (medir, escandallar, negociar, controlar), tácticas de negociación con proveedores, checklist de cada semana y un caso práctico con las cifras desarrolladas paso a paso.',
          'Número de versión actualizado a 2.0 en la hoja de instrucciones de cada fichero.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 12 ficheros',
        changes: [
          'Calculadora de PVP: corregidas nueve fórmulas que no calculaban.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 12 ficheros.',
        ],
      },
    ],
  },
  'kit-gestion-personal': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Turnos de noche sin horas negativas, las 4 alertas legales y coste laboral que ya no felicita a la hoja vacía',
        changes: [
          'Cuadrante de Turnos: entran las 4 alertas que faltaban — descanso mínimo de 12h entre jornadas (art. 34.3 ET), descanso semanal (art. 37.1 ET), jornada diaria máxima y horas semanales sobre lo que tiene contratado cada empleado, no un 40h fijo para todos.',
          'Cuadrante Mensual: deja de ser una rejilla en blanco y pasa a calcular horas y avisos por semana, con los nombres enlazados al cuadrante semanal.',
          'Control de Horas Extra: el turno que cruza la medianoche (por ejemplo 23:00 a 07:00) ya no ficha horas negativas, y el turno partido ya cabe en un solo registro gracias a la nueva columna "Pausa".',
          'Si dejas la columna "Horas Contratadas" vacía, la plantilla ya no declara extra la jornada entera: se queda en blanco hasta que la rellenes.',
          'El recargo de la hora extra pasa a ser una celda editable (1,25x por defecto, según tu convenio) y las horas acumuladas del año —que arrastras tú de mes en mes— llevan ahora un semáforo del tope legal de 80h/año (art. 35.2 ET), con las excepciones que no computan en ese tope: fuerza mayor, compensadas con descanso y horas complementarias del contrato a tiempo parcial.',
          'Coste Laboral Mensual: la cotización a la Seguridad Social (33% por defecto) y las pagas extra prorrateadas pasan a celdas editables, así que el coste por hora ya tiene en cuenta tu convenio real.',
          'El semáforo de coste laboral compara tu ratio con el umbral de tu tipo de negocio (fast casual, casual, fine dining, catering, cafetería o bar), en vez de aprobar a cualquiera por debajo del 30% y suspender a la alta cocina.',
          'Previsión de Plantilla por Servicio y Calculadora de Plantilla Óptima calculan ahora los cubiertos por SERVICIO (no por día completo): para 80 cubiertos/día en un casual, el resultado por defecto son 7 puestos, con el día pico añadiendo el refuerzo real que necesitas ese día.',
          'Planificación de Vacaciones: el calendario pasa de una casilla por mes a una fila por semana con saldo real, calculado desde tus solicitudes aprobadas y con prorrateo automático si el empleado se da de alta a mitad de año.',
          'Nueva hoja "Cobertura": mínimo de personal por turno, aviso cuando coincide temporada alta con ausencias y tabla de sustituciones.',
          'Onboarding Nuevo Empleado: el progreso ya se calcula bien (antes se comía las cabeceras de sección y abría en "4 de 51" con el checklist en blanco) y suma 50 tareas, con el alta en la Seguridad Social antes del inicio de jornada, Contrat@, la copia básica a la RLT y el modelo 145.',
          'Evaluación de Desempeño: la ficha nunca se abre con un error de Excel, la escala admite "N/A" sin penalizar la media y se añade un plan de desarrollo individual con acción formativa, responsable y fecha objetivo.',
          'BONUS Briefing de Cambio de Turno: gana el ARQUEO DE CAJA (fondo inicial, efectivo contado y ventas en efectivo según la lectura Z del TPV, con el descuadre calculado y su tolerancia editable) y las TEMPERATURAS al relevo con validez APPCC — cámara, congelador, vitrina fría y los dos puntos de mantenimiento en caliente—, cada uno con su mínimo y su máximo.',
          'Directorio de Plantilla: capacidad para 30 empleados, columnas de convenio aplicable, carnets (manipulador, PRL) y vencimientos, aviso automático si un empleado es menor de edad, y se elimina el campo de alérgenos propios (dato de salud protegido por el RGPD que no debía pedirse ahí).',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 9 ficheros',
        changes: [
          'Checklist de onboarding: se añade el contador de progreso (el cálculo se corrigió después, en la versión 2.0: contaba las cabeceras de sección como tareas hechas).',
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 9 ficheros.',
        ],
      },
    ],
  },
  'kit-inventario': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Categorías unificadas, fórmulas reales y plantillas coherentes entre sí',
        changes: [
          'Las 10 categorías de la hostelería iguales en las 9 plantillas: cárnicos, pescados, lácteos, verduras/frutas, secos/granos, congelados, bebidas alcohólicas, bebidas no alcohólicas, limpieza y otros (antes había tres formas distintas de nombrarlas según el fichero).',
          'Inventario de Stock Diario: las 50 filas de ejemplo llevan ahora la categoría, la unidad de compra y el par level real de cada producto — nueva columna de precio por unidad, valoración de tu stock y un Resumen con el valor total y por categoría.',
          'Fichas de Proveedores: la comparativa de precios ya te dice quién es el proveedor más barato de cada producto, con CIF/NIF, nº de RGSEAA y fecha de homologación.',
          'Pedidos de Compra: el IVA se aplica solo —primero busca el producto y, si no lo encuentra, aplica el de su categoría, porque el arroz va al 4 % y el aceite al 10 % aunque compartan categoría—, el desplegable de proveedores sale de la hoja Proveedores del propio fichero, te avisa si el pedido no llega al mínimo del proveedor y el historial queda enlazado al pedido en curso.',
          'Recepción de Mercancías: pasa de ser una checklist en blanco a calcular la diferencia entre lo pedido y lo recibido —y su valor en euros, que es lo que le reclamas al proveedor—, comparar la temperatura contra el rango legal de cada familia (por arriba y por abajo: un pescado a -20 °C venía congelado) y avisarte en rojo si hay que rechazar. Si la familia no tiene límite en la tabla legal, lo dice en vez de darte un visto bueno que no puede sostener.',
          'Control de Mermas: el coste por categoría y el dashboard mensual ya suman de verdad, con una celda para tus compras del mes y un Plan de Acción con 5 causas típicas precargadas.',
          'FIFO y Caducidades: semáforo de 5 estados (antes 3) que distingue "caducado, retirar" de "consumo preferente vencido, revísalo antes de decidir" y de "urgente, se sirve hoy" —es el que impide tirar una conserva buena—, con la cantidad y el valor en riesgo de cada lote, seis lotes de ejemplo para que la hoja abra funcionando, y un Mapa de Almacén con 11 zonas: los productos de limpieza salen del economato de los alimentos y los huevos dejan de mandarse a la cámara.',
          'Análisis de Costes de Compras: nueva hoja de Evolución Mensual, el Top 20 avisa cuando un producto sube más de un 5 % de precio, y el Dashboard de KPIs calcula el food cost sobre lo que consumes (no sobre lo que compras) y el coste por cubierto.',
          'BONUS Inventario Rápido Mensual: ahora sí calcula tu consumo real del mes, no solo el stock contado.',
          'BONUS Calculadora de Punto de Pedido: el coste de pedido, el % de almacenamiento y el factor de vida útil son celdas editables (antes iban fijos dentro de la fórmula), y la cantidad a pedir no supera nunca ni lo que tu producto aguanta sin caducar ni tu stock máximo. El punto de pedido que calcula es exactamente el par level del inventario: los dos ficheros dan el mismo número.',
          'Ninguna línea sin precio se suma como si fuera gratis: toda división y todo cálculo de coste avisa en vez de fallar o mentir.',
          'Semáforos de color reales (antes eran solo un emoji dentro del texto) en inventario, recepción, mermas, FIFO y en el Dashboard de KPIs de costes, que ahora tiene columna de Estado y objetivos que puedes cambiar tú.',
          'Un solo juego de datos de ejemplo en los nueve ficheros: los mismos productos, los mismos precios y los mismos seis proveedores. Antes había dos directorios de proveedores inventados que no coincidían entre sí.',
          'Todas las hojas se entregan protegidas sin contraseña, también las que son solo fórmulas y las tablas de referencia: un clic ya no borra el resumen del inventario ni la tabla legal de temperaturas.',
          'Número de versión actualizado a 2.0 en la hoja de instrucciones de cada fichero.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Mejoras de formato e impresión (A4) en los 9 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 9 ficheros.',
        ],
      },
    ],
  },
  'kit-plan-financiero': {
    version: '2.0',
    updated: '2026-08-29',
    entries: [
      {
        version: '2.0',
        date: '2026-08-29',
        title: 'Los cálculos que faltaban: tesorería encadenada, informe bancario que calcula y ratios con una sola vara de medir',
        changes: [
          'Tesorería (03): el saldo con el que abre cada mes es ahora el saldo con el que cerró el anterior. Antes arrastraba la línea «Otros pagos», así que once de los doce meses salían mal.',
          'Tesorería (03): pestaña «Parámetros» nueva — % de cobro con tarjeta y su desfase, plazo de pago a proveedores, tipos de IVA y estacionalidad. La liquidación de IVA se calcula sola en abril, julio y octubre (modelo 303), y la Seguridad Social se paga al mes siguiente.',
          'Informe de viabilidad (07): el P&L calcula de verdad. Total gastos, EBITDA, BAI, Impuesto de Sociedades, beneficio neto y cash flow operativo eran ceros escritos a mano.',
          'Informe de viabilidad (07): TIR, VAN y payback reales, sobre los cinco años y con el año 0 de la inversión. Se calculan sobre el dinero que genera el negocio antes de la deuda —es decir, miden si el proyecto se sostiene por sí mismo—, y si puedes pagar la cuota del préstamo te lo dice el DSCR de la pestaña Ratios. La tasa de descuento y el tipo del Impuesto de Sociedades son ahora celdas que puedes cambiar (25 % general; 15 % si eres entidad de nueva creación).',
          'Informe de viabilidad (07): pestaña «Financiación» nueva con el cuadro de amortización del préstamo. De ahí salen los intereses del P&L y el DSCR que mira el banco, que antes había que teclear a mano. Si pides carencia, los primeros años pagas solo intereses y la cuota se recalcula sobre el plazo que queda.',
          'Los tres «Resumen» (01, 01b y 05) consolidan por referencia: cambias un mes o un año y el resumen se mueve. Antes eran ceros fijos con un gráfico plano encima.',
          'P&L mensual (05): el semáforo ya no castiga vender por encima del presupuesto ni gastar de menos, y con EBITDA presupuestado negativo deja de invertir el signo. Las filas de ratios tienen por fin su desviación en puntos porcentuales.',
          'Dashboard (06): el RevPASH se mide por plaza y hora, no por metro cuadrado, y los umbrales viven en una sola tabla numérica — el food cost decía 32 % en un sitio y 33 % en otro.',
          'Punto de equilibrio (02): los cubiertos necesarios se redondean hacia arriba (con «51» no se llegaba), aparece el ticket medio necesario y hay dos umbrales: el operativo y el de caja. La cuota del préstamo sale del EBITDA.',
          'CAPEX (04): cada partida lleva base, IVA y total con IVA — el desembolso real es un 21 % mayor —, coeficiente de amortización por categoría y una pestaña nueva de conceptos de apertura con stock inicial, fianza, imprevistos y fondo de maniobra.',
          'Nuevas líneas de gasto en los P&L: comisiones de las plataformas de delivery y coste de bebida separado del de comida, para que el food cost no se diluya con la barra dentro.',
          'Simulador (BONUS 08): los costes fijos ya no incluían las nóminas dos veces. El escenario base deja de salir en pérdidas.',
          'Checklist (BONUS 09): 54 tareas en 7 fases — la nueva es Personal y obligaciones laborales (SS, RETA, apertura del centro de trabajo, contratos, altas previas, registro de jornada). El porcentaje completado cuenta las tareas que hay, no un 48 escrito a mano.',
          'Gráficos de verdad en 9 de las 10 plantillas, colores que se encienden solos en los semáforos, hojas protegidas sin contraseña con las celdas editables abiertas, y validación de datos que ya no rechaza un saldo negativo.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Formato de impresión (A4), metadatos y versión en los 10 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 10 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas': {
    version: '2.0',
    updated: '2026-08-22',
    entries: [
      {
        version: '2.0',
        date: '2026-08-22',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 491 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre de Negocio: checklist del local completo (no solo cocina), con responsable y hora límite precargados en cada tarea.',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €), y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu local), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Plantilla 07 (personalizable) con denominador por fórmula y tres hojas diferenciadas: por franja horaria, por área y por perfil.',
          'Bloque de higiene personal y orden seguro de apertura en Cocina; tarea de prevención de ANISAKIS (congelación ≥24 h a −20 °C), nombrada así en el propio texto, en Fríos/Mise en Place; registro de mermas en cierre de cocina.',
          'Sin duplicidades: el cierre general del local, el cierre de caja y el bloque SISTEMAS de la apertura salen de 01 (Sala) y viven ahora en 08 y 09, con una línea de remisión en su sitio. Por eso «Cierre Sala» y «Apertura Sala» tienen menos tareas que en la v1.1: ninguna se ha perdido, cada una está en el fichero que manda y con una sola hora.',
          'Hoja nueva «Trimestral y Anual» (05): DDD, extracción, extintores, gas, legionela y revisión del TPV/Verifactu con nº de parte y firma.',
          'Validación de datos unificada a «✓, —, N/A» en las 33 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en todas las hojas de datos de los 11 ficheros (las de Instrucciones se dejan libres a propósito).',
          'Línea de autoría anclada en las Instrucciones de los 11 ficheros (9 plantillas + 2 bonus); versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) con 5 fechas nuevas: Día del Padre, comuniones y bautizos, 15 de agosto, Todos los Santos y el puente del 6-8 de diciembre — 22 en total.',
          'Registro mensual de caja: la columna del efectivo pasa a pedir el recuento del cajón TAL CUAL («Efectivo Contado») y el fondo lo descuenta la fórmula, igual que en el cierre; el descuadre del mes se acumula en valor absoluto.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 491 tareas recontadas sobre los propios ficheros y comparación con SaaS de checklists (tipo Trail) generalizada, sin cifras de precio ajenas.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos e instrucciones actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-asador': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-bar': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 342 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre de Negocio: checklist del local completo (no solo barra), con responsable y hora límite precargados en las 33 tareas.',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €), y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas del mes.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu local), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Bloque de higiene personal al inicio de la apertura de barra, y las cámaras se comprueban (no se encienden): la desviación de temperatura bloquea el género.',
          'Mermas del turno con su consecuencia en el pour cost al cierre de barra, y alérgenos de la carta de cócteles por escrito antes del servicio.',
          'Hoja nueva «Trimestral y Anual»: DDD, extintores y BIE, conductos de extracción, gas, frigorista, legionela, limitador acústico, licencia de terraza, seguro y revisión del TPV/Verifactu, con nº de parte y firma.',
          'Tabla editable de vida útil del producto abierto y elaborado en barra (10 familias) al pie de «Inventario».',
          'Validación de datos unificada a «✓, —, N/A» en las 28 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en todas las hojas de datos de los 11 ficheros (las de Instrucciones se dejan libres a propósito).',
          'Línea de autoría anclada en las Instrucciones de los 11 ficheros (9 plantillas + 2 bonus); versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) con 6 fechas nuevas (Año Nuevo, Carnaval, 1 de mayo, 15 de agosto, puente de diciembre y Nochebuena) y meses en español en vez de en inglés abreviado — 23 en total.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 342 tareas recontadas sobre los propios ficheros y comparación con SaaS de checklists (tipo Trail) generalizada, sin cifras de precio ajenas.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-cafeteria': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 500 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre de Negocio: checklist del local completo (no solo barra), con responsable y hora límite precargados en las 31 tareas (ancla 06:45, la máquina de espresso).',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €), y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas del mes.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu local), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Bloque de higiene personal al inicio de la apertura de cocina (antes quedaba al final) y orden seguro de encendido: campana extractora → llave de gas → fuego, con la comprobación de gas que no existía.',
          'Prevención de ANISAKIS en el salmón ahumado que se sirve sin cocinar (congelación previa ≥24 h a −20 °C) en la partida de Calientes, y registro de mermas del turno en Calientes, Fríos y Pastelería Vitrina.',
          'Hoja nueva «Trimestral y Anual»: DDD, limpieza de conductos de extracción, extintores y BIE, gas, legionela, cambio del filtro de agua de la máquina de espresso y revisión del TPV/Verifactu, con nº de parte y firma.',
          'Tabla editable de vida útil en congelación (8 familias, de la bollería cruda al café en grano) al pie de «FIFO Semanal».',
          'Validación de datos unificada a «✓, —, N/A» en las 33 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en todas las hojas de datos de los 11 ficheros (las de Instrucciones se dejan libres a propósito).',
          'Línea de autoría anclada en las Instrucciones de los 11 ficheros (9 plantillas + 2 bonus); versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) con 5 fechas nuevas: Día del Padre, comuniones y bautizos, 15 de agosto, Todos los Santos y el puente del 6-8 de diciembre — 22 en total.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 500 tareas recontadas sobre los propios ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-catering': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, cobros y facturación por evento y las 347 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre de Negocio: checklist del obrador y la base de operaciones completa (no solo cocina), con responsable y hora precargados en 33 tareas — traducida al oficio del catering (órdenes de servicio, hoja de ruta de vehículos, carga de isotermos con temperatura de salida, accesos de cada recinto), no al vocabulario de un restaurante con sala.',
          'La plantilla 09 deja de ser un arqueo de caja y pasa a ser «Cobros y Facturación por Evento»: una empresa de catering no tiene mostrador ni turno de TPV — factura por evento y cobra casi siempre por transferencia, con un anticipo del 30-50 % al firmar y el saldo después. El fichero anterior modelaba un negocio que no era el tuyo.',
          'Dos checklists nuevos con 24 tareas: «Antes del Evento» (presupuesto firmado por escrito, comensales y fecha límite de cambios, anticipo cobrado y registrado, forma de pago del saldo, datos de facturación, condiciones de cancelación, proveedores externos, escandallo y margen, seguro de RC, alérgenos por escrito) y «Después del Evento» (comensales reales frente a contratados, extras, cargos por roturas, factura con desglose de IVA, saldo comunicado, cobro registrado, conciliación bancaria, reseña y expediente archivado). La columna «Cuándo» va en días respecto al evento — D-15, D-7, D-3, D-1 y D+0, D+1, D+7, D+30 — porque en catering el calendario lo marca la fecha del evento, no la hora de apertura de un local.',
          'Hoja «Liquidación del Evento»: escribes el presupuesto, los extras y cómo se reparte la base entre el 10 % (alimentos y bebidas no alcohólicas del servicio de catering) y el 21 % (alquileres, decoración, servicios y bebidas alcohólicas), y la hoja calcula los dos IVA, el TOTAL FACTURA, el saldo tras anticipo y el PENDIENTE DE COBRO, que se pone en ámbar mientras quede algo. El ESTADO es automático: «Cobrado», «Pendiente» o «VENCIDO» en rojo cuando la fecha de vencimiento ya ha pasado. Si las dos bases no suman presupuesto + extras te avisa, pero no te bloquea: el reparto lo decides tú con tu asesor.',
          'Hoja «Registro de Eventos»: 25 eventos con base, total, anticipo, cobrado, pendiente, medio de pago, vencimiento y estado, fila de TOTALES y recuento de cuántos eventos están pendientes y cuántos vencidos. Es la vista que dice de un vistazo cuánto dinero hay en la calle.',
          'La barra en efectivo no desaparece, pasa a ser opcional: al final de la liquidación hay una sección «Solo si hubo barra con cobro en EFECTIVO» con el recuento por denominaciones (500 € a 0,01 €), el fondo y el efectivo neto. No se suma sola al cobro del evento, a propósito: en la mayoría de los eventos no hay efectivo y una fórmula fija dejaría un 0 restando donde no debe.',
          'El enlace de descarga del antiguo «09-apertura-cierre-caja.xlsx» redirige al fichero nuevo, así que los accesos ya enviados por email siguen funcionando. Recuento del kit actualizado: 347 tareas (el 09 nuevo entrega 24 frente a las 23 del anterior).',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu operación), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          'Bloque de higiene personal y arranque seguro de la cocina (campana → gas → equipos) al inicio de «Producción»; prevención de ANISAKIS en el pescado que se sirve crudo o semicrudo (ceviche, tartar, marinados, ahumado) en Producción y en las estaciones de cocktail/standing; registro de mermas de producción del día.',
          'Tabla editable de vida útil en congelación (10 familias) al pie de «Producción».',
          'Hoja nueva «Trimestral y Anual» en el fichero del Event Manager: DDD de la cocina central, conductos de extracción, extintores y BIE, certificado ATP del vehículo, calibración de sondas, gas, aceite usado, RGSEAA, carnés de manipulador, póliza de responsabilidad civil de eventos y revisión del TPV/Verifactu, con nº de parte y firma.',
          'Alérgenos e intolerancias por escrito en bodas y corporativos, y señalizados por bandeja en las estaciones de cocktail/standing; en montaje, señalización de los 14 alérgenos declarados en el buffet.',
          'Criterio de sobrantes en el desmontaje: ya no es «lo recuperable», sino si ha salido a sala y ha mantenido la cadena de frío, con la merma anotada.',
          'Calendario anual (BONUS-02) con 2 fechas nuevas — Día del Padre y el puente de diciembre — 22 en total.',
          'Validación de datos unificada a «✓, —, N/A» en las 22 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en los 11 ficheros (las de Instrucciones se dejan libres a propósito).',
          'Línea de autoría anclada en las Instrucciones de los 11 ficheros (9 plantillas + 2 bonus); versión 2.0 · agosto 2026.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 347 tareas recontadas sobre los propios ficheros y comparación con Trail generalizada, sin cifras de precio ajenas.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas en las hojas de checklist.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-chef-privado': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 9 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 9 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-chocolateria': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 338 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre del Negocio: el vocabulario de restaurante (pizarra de menú, sistema de reservas, sillas y mesas, cartas) pasa al de un obrador con tienda — encendido y comprobación de las vitrinas temperadas (16-18 °C, menos del 55 % de humedad), escaparate al sol, encargos comprometidos del día y mobiliario de mostrador —, con responsable y hora precargados en 32 tareas.',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €) y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra, más la báscula de mostrador (tara y peso patrón) y el cuadre del precio por kilo entre cartel y TPV que la venta al peso necesita y el fichero genérico no cubría.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas del mes.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu obrador), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Bloque de higiene personal y arranque seguro del obrador (7 tareas) al INICIO de la Apertura —antes quedaba al final—, con el orden extracción → gas → equipos, y las cuatro temperaturas del oficio (cámara, nevera de rellenos, obrador y vitrina) con su objetivo, su humedad y un hueco para la lectura.',
          'Test de templado con criterio de paso/no-paso (cristaliza en 3-5 min a 18-20 °C, con brillo uniforme y sin vetas) extendido a las tres coberturas —negra, con leche y blanca—, que antes solo lo tenía la negra; y tabla de vida útil portada de CONGELACIÓN a CONSERVACIÓN (10 familias), porque congelar chocolate acabado produce sugar bloom.',
          'Hoja nueva «Trimestral y Anual» (05): mantenimiento contratado — DDD, conductos de extracción, extintores y BIE, gas, legionela, SAT de temperadora y cámaras, calibración de sondas y báscula, RGSEAA, póliza de RC por producto y Verifactu — con nº de parte y firma.',
          'Registro y cierre del registro de jornada del equipo (RD-ley 8/2019, conservación 4 años) en el checklist del manager, y sección nueva «Sábado y domingo — Tienda a pleno» en el semanal, que antes terminaba el viernes en una tienda que factura fin de semana.',
          'Confirmación por escrito de alérgenos, hora de recogida, señal y cancelación al tomar un encargo (apertura, perfiles y eventos), etiquetado con los alérgenos reales de una vitrina de bombonería y el precio por kilo de la venta al peso (Rgto. 1169/2011), y fecha límite de encargos y horarios del 24 y el 31 publicados en octubre.',
          'Validación de datos unificada a «✓, —, N/A» en las 24 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en los 11 ficheros (las hojas de Instrucciones se dejan libres a propósito). Línea de autoría anclada en las Instrucciones de las 11 plantillas; versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) reescrito como tabla real de 12 meses (Enero-Diciembre) con 5 campañas nuevas de tienda llena —Reyes, comuniones, 15 de agosto, Todos los Santos y el puente del 6-8 de diciembre— y las Instrucciones dejan de prometer «15 fechas clave» cuando la hoja tiene 12 filas: ahora dicen lo que hay.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 338 tareas recontadas sobre los propios ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-dark-kitchen': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 331 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre del Negocio: el vocabulario de restaurante con comedor (reservas, mobiliario de sala, terraza, música ambiente) pasa al de una cocina 100 % delivery (impresoras de plataforma, pedidos programados, zona y puerta de recogida de riders, puesto de empaquetado y etiquetado, activar las marcas), con responsable y hora precargados en 33 tareas.',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €), y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas del mes.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu marca), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Bloque de higiene personal al INICIO de la Apertura Cocina (antes quedaba al final) y orden seguro de encendido de equipos: campana extractora → comprobar gas → encender fuego.',
          'Prevención de ANISAKIS del pescado que se sirve crudo o marinado en la Estación Fría (congelación ≥24 h a −20 °C, Rgto. CE 853/2004), y comprobación diaria de los alérgenos publicados en cada marca (RD 126/2015, venta a distancia).',
          'Registro de mermas del turno en Estación Caliente, Estación Fría y Cierre Cocina; el aceite se manipula por debajo de 40 °C y el usado va a gestor autorizado.',
          'Hoja nueva «Trimestral y Anual» (05): mantenimiento contratado — DDD, conductos de extracción, extintores y BIE, gas, legionela, frigorista, gestor de aceite y de cartón, seguro de RC por producto y Verifactu — con nº de parte y firma.',
          'Tabla editable de vida útil en congelación (8 familias) al pie de «FIFO Semanal».',
          'Validación de datos unificada a «✓, —, N/A» en las 28 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en los 11 ficheros (las hojas de Instrucciones se dejan libres a propósito). Línea de autoría anclada en las Instrucciones de las 11 plantillas; versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) con 5 fechas nuevas: Día del Padre, comuniones y bautizos, 15 de agosto, Todos los Santos y el puente del 6-8 de diciembre — 22 en total.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 331 tareas recontadas sobre los propios ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-food-truck': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Desplegable ✓ / — / N/A y resaltado en verde al marcar en la columna OK.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-hamburgueseria': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Higiene, gas y arqueo de caja: revisión de las 346 tareas del kit',
        changes: [
          'Bloque de HIGIENE PERSONAL al inicio del turno en «Apertura Cocina» (5 tareas), antes de tocar carne, pan, queso o salsas; y orden seguro de encendido en «Apertura Cocina» y «Plancha Grill»: campana → comprobar gas → encender equipos.',
          'El filtrado del aceite de la freidora se corrige: primero se apaga el equipo y se deja enfriar, y el filtrado se acota a menos de 40 °C — antes se filtraba con la freidora todavía encendida, inconsistente con la propia partida «Freidora» del kit.',
          'El punto de la carne PICADA se fija en 70 °C de núcleo (75 °C en población de riesgo) y con sonda en «Plancha Grill», en vez de la referencia genérica «medio, hecho, muy hecho»; utillaje de crudo separado y marcado antes del servicio.',
          'Verificación de las cámaras al abrir (con registro de temperatura) antes de sacar la carne picada, y registro DIARIO de mermas (producto, cantidad, motivo) en cierre de cocina y en línea de montaje.',
          'Cierre y validación del registro diario de jornada del equipo (obligatorio desde 2019) en «Diario Manager», con archivo de 4 años de esos registros en «Mensual Manager».',
          'Hoja nueva «Trimestral y Anual» (05): mantenimiento contratado — DDD, conductos de extracción, extintores y BIE, gas, frigorista, aceite usado por gestor autorizado, legionela, agua, seguro y Verifactu — con nº de parte y firma.',
          'Tabla editable de vida útil en congelación por familia de producto (9 familias de una hamburguesería) al pie de «FIFO Semanal».',
          'Apertura y Cierre de Caja (09): fondo de caja inicial editable, recuento por denominaciones (con la de 0,02 €), columna «Z del TPV» y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra; registro mensual con las 31 filas del mes.',
          'Apertura y Cierre de Negocio (08): Responsable y hora límite precargados en las 31 tareas del checklist del local completo.',
          'Contador honesto en los 9 checklists: descuentan las tareas marcadas N/A, pero no las marcadas «—» (pendientes), que siguen bajando el porcentaje; 5 filas libres dentro del rango contado en cada uno para añadir tareas propias.',
          'Calendario anual (BONUS-02) con 5 fechas nuevas — Día del Padre, comuniones y bautizos, 15 de agosto, Todos los Santos y el puente del 6-8 de diciembre — hasta las 22 en total.',
          'Validación de datos unificada a «✓, —, N/A» y protección sin contraseña en las 31 hojas de checklist de los 11 ficheros.',
          'Línea de autoría anclada en las Instrucciones de las 11 plantillas, versión 2.0 · agosto 2026. Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 346 tareas recontadas sobre los propios ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-heladeria': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 298 tareas del kit revisadas',
        changes: [
          'Nueva plantilla 08 — Apertura y Cierre de Negocio: checklist del local completo (no solo obrador), con responsable y hora límite precargados en las 33 tareas.',
          'Nueva plantilla 09 — Apertura y Cierre de Caja: fondo de caja inicial editable, recuento por denominaciones (con monedas de 0,02 €), y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra.',
          'Registro mensual de caja con columna «Z del TPV» y descuadre calculado por fórmula en las 31 filas del mes.',
          'Contador honesto en los 9 checklists: del total salen las tareas marcadas N/A (no aplican en tu local), pero NO las marcadas «—» (no hechas), que siguen contando como pendientes y bajan el porcentaje. Los dos BONUS no llevan contador porque no son listas de tareas.',
          '5 filas libres con formato y validación dentro del rango contado en cada checklist, para añadir tareas propias sin romper el total.',
          'Bloque de higiene personal y arranque seguro al inicio de la apertura de obrador (extracción antes de encender y comprobación del gas si lo hay); las cámaras y la vitrina se comprueban desde la noche anterior, no se «encienden», y quedan diferenciados los tres niveles de temperatura de una heladería: conservación (−18 °C), servicio de vitrina (−14 a −12 °C) y maduración de la mezcla (2-4 °C).',
          'Alérgenos de mostrador: un porcionador por cubeta para pistacho, avellana y almendra, y carta de alérgenos contrastada con la vitrina del día; fruta cruda de los toppings con desinfección y aclarado antes de servir. Mermas del día registradas con sabor, kg y motivo al cierre.',
          'Hoja nueva «Trimestral y Anual»: DDD, conductos de extracción, gases fluorados, calibración de sondas, extintores, gas, legionela, registro sanitario, formación en alérgenos, póliza del frío y facturación, con nº de parte y firma.',
          'Validación de datos unificada a «✓, —, N/A» en las 25 hojas de checklist y protección sin contraseña, con las celdas de entrada desbloqueadas, en todas las hojas de datos de los 11 ficheros (las de Instrucciones se dejan libres a propósito).',
          'Línea de autoría anclada en las Instrucciones de los 11 ficheros (9 plantillas + 2 bonus); versión 2.0 · agosto 2026.',
          'Calendario anual (BONUS-02) reescrito como tabla de los 12 meses del año con las fechas señaladas de heladería dentro de cada mes: 7 meses con fechas que faltaban (Día del Padre, comuniones, San Juan, 15 de agosto, Todos los Santos y puente del 6-8 de diciembre) y el Día de la Madre corregido de junio a mayo.',
          'Landing actualizada: 9 plantillas + 2 bonus (11 ficheros), 298 tareas recontadas sobre los propios ficheros y comparación con el software de gestión generalizada, sin cifras de precio ajenas.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-hotel': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Higiene, anisakis, mantenimiento legal y arqueo de caja revisados en las 53 hojas de checklist',
        changes: [
          'Nueva sección «Higiene personal y arranque seguro de la cocina» en el buffet de desayuno: uniforme, lavado de manos, comprobación nocturna de cámaras y el orden campana → gas → equipos antes de encender nada.',
          'Prevención de ANISAKIS (Rgto. CE 853/2004) en el pescado crudo, marinado o ahumado del buffet de desayuno, del buffet de almuerzo/cena y de los outlets (carpaccio, salmón, tartar, ceviche).',
          'Hoja nueva «Trimestral y Anual» en Mantenimiento: DDD, conductos de extracción, extintores y BIE, revisión de gas, legionela, OCA de baja tensión, ascensores y RITE, cada una con su periodicidad contratada y espacio para nº de parte y firma.',
          'Banquetes y Eventos: bloque nuevo «Al confirmar la reserva del evento» — alérgenos por escrito, nº garantizado, precio por comensal y qué incluye, condiciones de cancelación y aforo — antes de la coordinación pre-evento.',
          'RRHH Operativo: el fichaje se cierra y se valida a diario (con los extras de banquete y los turnos de noche nombrados) y se archiva el registro de jornada al cerrar el mes, con la obligación legal de conservarlo 4 años (RD-ley 8/2019).',
          'Apertura y Cierre de Caja: recuento por denominaciones (incluida la de 0,02 €), descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra, y Registro Mensual con columna «Z del TPV» y descuadre por fórmula en las 31 filas.',
          'Apertura y Cierre del Negocio: Responsable y Hora Límite precargados en cada tarea (ancla 05:30) y contador agrupado con filas libres para añadir tareas propias.',
          'Contador honesto en las 53 hojas de checklist: las filas de rótulo repetidas por sección dejan de contar como tarea y el numerador exige texto real en la columna «Tarea».',
          'Validación de datos unificada a «✓, —, N/A» en las 53 hojas de checklist de los 19 ficheros (antes convivían dos listas distintas, una de ellas sin N/A).',
          'Calendario Anual (BONUS-02) con 4 fechas nuevas de hotel: Día del Padre, comuniones y bautizos, el puente de Todos los Santos y el puente de la Constitución — 24 fechas en total.',
          'Línea de autoría anclada en las Instrucciones de los 19 ficheros; versión 2.0 · agosto 2026.',
          'Landing actualizada: 53 hojas de checklist en 19 ficheros (antes se anunciaban 46 checklists en 15 plantillas), 636 tareas recontadas sobre los propios ficheros y comparación con Trail generalizada con la cifra nueva.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 19 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 19 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-marisqueria': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Desplegable ✓ / — / N/A y resaltado en verde al marcar en la columna OK.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-panaderia': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Desplegable ✓ / — / N/A y resaltado en verde al marcar en la columna OK.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-pizzeria': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Motor 2.0: 373 tareas ordenadas, hoja Trimestral y Anual y arqueo de caja con descuadre automático',
        changes: [
          'Contador honesto de tareas completadas: la casilla "N/A" ya no cuenta como pendiente en el recuento de cada checklist.',
          'Línea de autoría: bio del creador y versión 2.0 ancladas en la hoja de Instrucciones de los 11 ficheros.',
          'Bloque «HIGIENE PERSONAL» al inicio de la Apertura de Cocina (5 tareas), antes de tocar masa, salsa, mozzarella o toppings — y el lavado de manos del cierre ya no repite el mismo gesto, cubre el cruce reparto/dinero → masa.',
          'Orden seguro de encendido del horno de leña/piedra: campana y tiro → comprobar gas → encender, con el aviso de "si huele a gas, no enciendas" en la propia tarea.',
          'Hoja nueva «Trimestral y Anual» en el fichero de Semanales y Mensuales: mantenimiento contratado con nº de parte y firma — control de plagas (DDD), conductos y chimenea del horno de leña, extintores y BIE, instalación de gas, legionela, agua, seguro y Verifactu.',
          'Ficha de Apertura y Cierre de Caja rehecha: recuento de efectivo por 15 denominaciones (incluida la de 0,02 €), fondo de caja editable y descuadre automático frente al Z del TPV con aviso en ámbar.',
          'Ficha de Apertura y Cierre de Negocio con responsable y hora precargados en las 31 tareas del checklist del local completo (luces, alarma, TPV, terraza).',
          'Las 3 plantillas personalizables (por franja horaria, por área y por perfil) dejan de ser una única plantilla en blanco repetida: cada una tiene ya sus propias secciones y columnas.',
          'Calendario Anual ampliado de 17 a 22 fechas: se añaden Día del Padre, comuniones, 15 de agosto, Todos los Santos y el puente de diciembre.',
          'Higiene alimentaria: lavado y desinfección con dosis y aclarado de los vegetales de consumo crudo (ensaladas y guarniciones) y de la rúcula/albahaca que va cruda tras el horno; registro diario de mermas por producto, cantidad y motivo.',
          'Registro diario de jornada del equipo (obligatorio desde 2019) con cierre y validación en la hoja del manager, y archivo mensual con conservación de 4 años.',
          'Impresión en A4 configurada en las 31 hojas de checklist: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-restaurante-creativo': {
    version: '2.0',
    updated: '2026-08-23',
    entries: [
      {
        version: '2.0',
        date: '2026-08-23',
        title: 'Apertura y cierre de negocio, arqueo de caja y las 477 tareas del kit revisadas',
        changes: [
          'Apertura y Cierre de Negocio (10) y Apertura y Cierre de Caja (11) rediseñados: responsable y hora límite precargados en 33 tareas, columna «Firma», recuento de caja por denominaciones (con monedas de 0,02 €) y descuadre automático (Total facturado − Z del TPV) resaltado en ámbar si no cuadra; Registro Mensual con columna «Z del TPV» y descuadre por fórmula.',
          'Contador honesto en las 34 hojas de checklist: el denominador ya no cuenta las cabeceras repetidas de cada sección y el numerador exige texto en «Tarea»; desplegable unificado a «✓, —, N/A» (antes «✓, ✗, —», sin N/A).',
          'Bloque nuevo «🧼 Apertura — Higiene Personal y Arranque Seguro» en Apertura AM (01): 8 tareas delante del equipamiento, con el orden seguro campana → gas → equipos y comprobación nocturna de cámaras frigoríficas y de congelación con objetivo de temperatura.',
          'Registro de jornada de la brigada (RD-ley 8/2019, conservación 4 años) en el cierre de Apertura y Cierre (01) y su archivo mensual en Semanales y Mensuales (05).',
          'Prevención de ANISAKIS (congelación previa ≥24 h a −20 °C) para el pescado que se sirve crudo o semicrudo en Mise en Place Degustación (02), remitida también desde la hoja de rol de Partida Fría en Tareas por Brigada Creativa (04).',
          'Hoja nueva «Trimestral y Anual» en Semanales y Mensuales (05): mantenimiento y documentación que se contrata (DDD, conductos de extracción, extintores y BIE, gas, legionela, calibración de básculas y sondas, RGSEAA, carnés de manipulador y revisión del TPV/Verifactu), con nº de parte y firma. Tabla editable de vida útil en congelación (10 familias) al pie de la misma hoja.',
          'Bloque nuevo «📝 Al Confirmar la Reserva» en Cenas Especiales (Chef\'s Table y Eventos, 07): alérgenos por escrito, número cerrado, precio por comensal, señal y condiciones de cancelación; las tareas que antes duplicaban ese control pasan a cubrir la producción del menú, el servicio en el pase y el cierre de factura.',
          'Plantilla Personalizable (09) deja de ser la misma hoja en blanco repetida tres veces: cada plantilla va ahora por un eje distinto —A por franja horaria, B por partida, C por perfil— con 3 filas de ejemplo marcadas N/A para que no cuenten.',
          'Calendario Anual (BONUS: Calendario Anual de Eventos y Carta) con 7 fechas del calendario español que faltaban: Día del Padre, comuniones, Día de la Madre, 15 de agosto, 1 de noviembre y el puente del 6-8 de diciembre.',
          'Línea de autoría anclada en las Instrucciones de las 13 plantillas; versión 2.0 · agosto 2026.',
          'Landing actualizada: 11 plantillas + 2 bonus (13 ficheros), 477 tareas recontadas sobre los propios ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 13 plantillas',
        changes: [
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 13 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-sushi-bar': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Columna «✓ Completada» con desplegable ✓ / — / N/A, fila en verde al marcar y total que se recalcula en las hojas de checklist si añades o quitas tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-tapas-bar': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de las 11 plantillas',
        changes: [
          'Desplegable ✓ / — / N/A y resaltado en verde al marcar en la columna OK.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'pack-appcc': {
    version: '2.0',
    updated: '2026-08-22',
    entries: [
      {
        version: '2.0',
        date: '2026-08-22',
        title: 'De 15 a 19 registros (21 ficheros con los 2 bonos) + normativa vigente actualizada',
        changes: [
          '4 registros nuevos: Cocción y Regeneración, Enfriamiento y Descongelación, Congelación Anisakis y Verificación de Termómetros — cerraban los PCC que el análisis de peligros ya citaba y no tenían ficha detrás.',
          'Semáforo de color (verde/ámbar/rojo) en todas las columnas de estado, en los 19 registros.',
          'Análisis de Peligros ampliado a 21 peligros en 7 fases del proceso, con nivel de riesgo calculado automáticamente y descongelación, huevo fresco, Anisakis, plagas, agua de consumo y aceite de fritura incorporados: ya no hay ningún registro del pack sin su peligro analizado detrás.',
          'Nivel de gravedad de las sanciones actualizado a la Ley 17/2011 (Leve / Grave / Muy grave), sustituyendo la escala anterior.',
          'Aceite de fritura y agua potable: referencias normativas actualizadas (Orden de 26 de enero de 1989 y RD 3/2023).',
          'Comidas preparadas: las citas al RD 3484/2000 pasan al RD 1021/2022, que lo derogó. Los 75 °C de cocción y regeneración y el 60 → 10 °C en 2 horas se presentan ya como el límite crítico que fija tu propio APPCC, que es justo lo que exige la norma nueva.',
          'Recepción: la carne picada (máx. 2 °C) y los preparados de carne (máx. 4 °C) se separan en dos familias, igual que hace el Reglamento 853/2004, y la caza mayor pasa a 7 °C. Antes el registro rechazaba entregas perfectamente legales.',
          'Registro de cocción: en regeneración el veredicto mira también el tiempo. Más de una hora en llegar a los 75 °C es REPETIR aunque los alcance.',
          'Verificación de termómetros: casilla de altitud en la cabecera. Con el método de la ebullición, la referencia se corrige sola (en Madrid el agua hierve a 97,8 °C, no a 100), así que una sonda buena deja de salir NO APTA.',
          'Cartel de alérgenos: el protocolo de reacción se reordena por urgencia. Primero el 112 y la adrenalina; guardar el plato y la etiqueta, después.',
          'Higiene personal: formación acreditada por la empresa en vez del carné de manipulador, suprimido desde 2010.',
          'Guía de Inspección con los 25 puntos reales (antes numeraba 25 y traía 23) y resumen automático que distingue incumplimientos muy graves de graves.',
          'Plan de Limpieza y Desinfección ampliado con el bloque exterior, lavamanos, maquinaria y pestaña de productos químicos; corregida la mezcla de ácido y lejía.',
          'Registro de trazabilidad con pestaña de salida/uso interno para cerrar el rastreo hasta el plato servido.',
          'Ejemplos sembrados en cada registro que se entrega vacío, todos marcados «(ejemplo)» para que no se archiven como reales, y pie con la frecuencia de conservación de registros en los 21 ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 17 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 17 ficheros.',
        ],
      },
    ],
  },
  'plan-catering-tematico-eventos': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 4 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 4 ficheros.',
        ],
      },
    ],
  },
  'plan-chef-privado-showcooking-eventos': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 4 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 4 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-bar-restaurante': {
    version: '2.2',
    updated: '2026-09-05',
    entries: [
      {
        version: '2.2',
        date: '2026-09-05',
        title: 'El payback y la cobertura de la deuda, con la vara del banco: el proyecto se mide antes de la deuda y después de impuestos',
        changes: [
          'Payback del proyecto: la inversión a recuperar es el CAPEX más el fondo de maniobra (sin el IVA, que se recupera por el modelo 303) y se compara con lo que el negocio genera ANTES de pagar al banco (resultado neto más amortización más intereses), con la misma base los tres años. La 2.1 dividía la necesidad total de caja, financiación incluida, entre un flujo al que ya se le había quitado la cuota: contaba la deuda dos veces y daba 2,75 años. En el ejemplo son 2,3 años; sobre el CAPEX solo, 1,6 (fila informativa nueva).',
          'Cobertura de la deuda (DSCR) después de impuestos, como la mira una entidad: en el ejemplo el mínimo del cuadro pasa de 3,79 a 3,31. En la hoja de Financiación, los años 4 a 7 del cuadro mantienen el flujo del año 3 y la nota lo declara.',
          'Escenarios comparables: el saldo de caja al cierre del año 1 se calcula con el mismo método en las tres columnas (118.187 € en el realista) y el saldo real de la tesorería mensual (155.793 €) tiene ahora su propia fila.',
          'Los imprevistos de obra se calculan sólo sobre las partidas de obra del bloque de local, no sobre todo el bloque, y capitalizan con la obra: 3.650 € en el ejemplo (antes 3.800 €), amortización 8.761 €/año, inversión total sin IVA 179.014,80 €.',
          'IVA por línea de venta: cada línea de ingreso del P&L lleva su tipo en la columna de al lado (10 % en sala, alcohol incluido; el alcohol repartido, al 21 %) y de ahí salen los cobros, el IVA repercutido y el PVP equivalente. Los valores del ejemplo no cambian.',
          'El punto de equilibrio explica sus dos lecturas en una frase: 66 cubiertos al día para no perder dinero (con la amortización dentro) y 63 para que la caja aguante (sin amortización y con la cuota del préstamo del año). Notas afinadas: SMI 2026 sin cita de norma no verificada, refrescos azucarados al 21 % también en la compra, notaría con IVA, redacción de la renta previa, leyenda ☐ del checklist, tildes y títulos del fichero.',
          'Número de versión (2.2) en los dos ficheros.',
        ],
      },
      {
        version: '2.1',
        date: '2026-09-05',
        title: 'El IVA de la bebida servida en sala es el 10 %: el plan financiero repercutía el 21 % a la parte alcohólica',
        changes: [
          'Plan financiero: la bebida alcohólica servida en sala tributa al 10 %, igual que la comida (art. 91.Uno.2.2.º de la Ley 37/1992 del IVA: servicios de hostelería y suministro de comidas y bebidas para consumir en el acto, sin excluir el alcohol). El libro repercutía el 21 % a la parte alcohólica de la bebida en el IVA del año, y a TODA la bebida en el PVP equivalente del ticket (de ahí los 20,72 €): el 21 % es el tipo general y en hostelería sólo alcanza al alcohol y a los refrescos con azúcares añadidos que salen para llevar o a domicilio.',
          'Celda nueva en «0. Supuestos», «IVA de la bebida ALCOHÓLICA servida en sala», con la referencia legal en su nota. El alcohol que sale por delivery sí va al 21 %, y el libro se lo aplica solo según el peso que pongas en «Ventas por delivery sobre el total» (a cero por defecto). El tipo general del libro queda para el alcohol que compras al proveedor y para ese alcohol repartido; suministros, equipamiento y servicios tienen su propia celda de IVA soportado.',
          'Efecto en el caso de ejemplo: el PVP equivalente del ticket pasa de 20,72 € a 20,02 €; el IVA repercutido del año 1, de 55.562 € a 45.136 €; y los cobros, el flujo de caja del año y el saldo de cierre bajan esos mismos 10.426 € (el saldo mínimo del año baja 983 €, de 61.957 € a 60.974 €). La versión anterior repercutía un IVA que la ley no permite cobrar al cliente, y lo guardaba en caja los doce meses porque el IVA de la inversión absorbe las liquidaciones del año 1. Por la misma razón el payback del proyecto pasa de 2,58 a 2,75 años: ahora es el número defendible ante un banco. El P&L y el punto de equilibrio no cambian porque van sin IVA; en «4. Escenarios» sólo se mueve el saldo de caja al cierre del escenario realista, que lee la tesorería.',
          'El IVA soportado en compras no cambia: el proveedor sigue facturando el alcohol al 21 % y la tesorería lo sigue deduciendo así. La partida de suministros avisa ahora de que la factura del agua va al 10 %.',
          'Instrucciones: para pasar un PVP a precio sin IVA se divide entre 1,10 en sala (comida y bebida); el 21 % sólo alcanza a lo que sale del local como entrega de bienes excluida del tipo reducido (alcohol y refrescos con azúcares añadidos para llevar o a domicilio; la comida para llevar sigue al 10 %). La tabla de recalibrado dice ya el ticket real del libro (18,20 € sin IVA, 20,02 € de PVP), la plantilla y el alquiler reales (7 puestos y 3.000 €/mes), y explica cada cambio en lenguaje llano, sin códigos internos. El punto 3 llama a la hoja «3. Punto Equilibrio» por su nombre exacto y el bloque «ARRANQUE Y AFORO» de la hoja de supuestos recupera su título.',
          'Número de versión (2.1) en los dos ficheros.',
        ],
      },
      {
        version: '2.0',
        date: '2026-08-29',
        title: 'El plan financiero pasa a ser un modelo: una hoja de supuestos manda y el resto del libro se calcula',
        changes: [
          'Hoja nueva «0. Supuestos»: cubiertos, ticket sin IVA, días de apertura, mezcla de comida y bebida, coste de mercancía, alquiler, financiación e impuestos se teclean una sola vez en celdas verdes y las demás hojas se derivan por fórmula (766 fórmulas). Antes había cifras escritas a mano que no se movían al cambiar un supuesto.',
          'Hojas nuevas «6. Tesorería 12 meses» (cobros con su desfase, pagos por partida, IVA repercutido y soportado con liquidación trimestral, devolución del préstamo y saldo acumulado con su mínimo) y «7. Financiación» (cuadro de amortización francés con carencia, del que salen los intereses del P&L).',
          'El coste de personal del P&L sale de la hoja «5. Personal», con la Seguridad Social a cargo de la empresa en una celda, no de una cifra aparte; la bebida ya no se contaba dos veces; el Impuesto de Sociedades aplica el 15 % de entidad de nueva creación en los dos primeros ejercicios con base imponible positiva y compensa las bases negativas.',
          'Punto de equilibrio derivado del P&L con dos lecturas: la contable, que incluye la amortización (65,10 cubiertos/día en el caso de ejemplo), y la de caja, que la quita y añade la cuota del préstamo (62,93); las existencias iniciales ya no se amortizan.',
          'Inversión inicial: cada partida declara si lleva IVA (la fianza, las licencias y tasas y el colchón operativo ya no lo soportan), con imprevistos de obra y meses de alquiler previos a la apertura en celda. Aforo, rampa de arranque y rotación implícita calculada en «0. Supuestos».',
          'Checklist de apertura: 64 ítems con desplegable ✓ / — / N/A y resaltado al marcar.',
          'Número de versión (2.0) en los dos ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 2 ficheros',
        changes: [
          'Corregidas dos etiquetas que Excel abría con error (#¿NOMBRE?): ahora se guardan como texto, no como fórmula rota.',
          'Desplegable ✓ / — / N/A y resaltado en verde al marcar en la columna OK.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 2 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-cafeteria': {
    version: '2.2',
    updated: '2026-09-05',
    entries: [
      {
        version: '2.2',
        date: '2026-09-05',
        title: 'Plan financiero reconstruido: 9 hojas y 742 fórmulas, con tesorería, financiación y el oficio de la cafetería',
        changes: [
          'El plan financiero pasa de 6 hojas de cifras tecleadas a 9 hojas enlazadas por fórmula (742 en total): cambias una celda verde de «0. Supuestos» y se recalcula el libro entero.',
          'Hojas nuevas: «Tesorería 12 meses» (cobros, pagos, liquidación de IVA por trimestres y saldo mes a mes) y «Financiación» (origen de fondos, cuadro de amortización francés con carencia y cobertura de la deuda).',
          'El coste de personal sale ya de su propia hoja: 6 puestos —propietario-barista, baristas de mañana y tarde, ayudante de brunch, extra de fin de semana y suplencias—, 100.083 €/año, con dos avisos automáticos: ningún sueldo por debajo del SMI según su jornada, y la plantilla cubriendo el 100 % de las horas de servicio de barra, sala y terraza.',
          'Caso base recalibrado con datos defendibles: 100 clientes al día y 9,80 € de ticket sin IVA (10,78 € de PVP), con los cinco ratios del sector cumplidos los tres años; punto de equilibrio en 84 clientes/día (79 en el umbral de caja) e inversión inicial de 130.176 € (91.650 € de CAPEX más 38.526 € de fondo de maniobra).',
          'IVA propio de la barra: el consumo en sala tributa al 10 % con el alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992), y el IVA de la inversión se adelanta y se compensa en la hoja de tesorería.',
          'Checklist de apertura: de 69 a 75 trámites, con el registro sanitario autonómico —sustituye al RGSEAA estatal, que no aplica al minorista que sirve al consumidor final—, RGPD, adaptación a Veri*factu, gestor de residuos, DDD y registro horario.',
          'El documento Word sigue en la versión anterior por ahora: las cifras válidas son las del Excel (se actualizará en la próxima versión).',
          'Número de versión (2.2) en los dos ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 2 ficheros',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 2 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-cocteleria-eventos': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 4 ficheros',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas en las hojas de checklist (la plantilla de proveedores lleva desplegable pero no contador).',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 4 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-food-truck': {
    version: '2.2',
    updated: '2026-09-05',
    entries: [
      {
        version: '2.2',
        date: '2026-09-05',
        title: 'El plan financiero pasa a ser un modelo de verdad',
        changes: [
          'Hoja nueva de Supuestos: cambias los clientes al día, el ticket o el coste de mercancía y se recalculan el P&L, el punto de equilibrio, los escenarios, la tesorería y la financiación (722 fórmulas enlazadas; antes el libro eran cifras tecleadas).',
          'Hoja nueva de Tesorería 12 meses: cobros, pagos, liquidación trimestral de IVA y saldo acumulado mes a mes, para saber de un vistazo si la caja aguanta.',
          'Hoja nueva de Financiación: origen y usos de los fondos (25.000 € de recursos propios más 72.000 € de préstamo), cuadro de amortización del préstamo año a año y cobertura del servicio de la deuda (DSCR).',
          'El coste de personal del P&L ya sale de la hoja de Personal: 42.081 € al año con 4 puestos dimensionados para los 250 días de servicio (propietario/a a jornada completa, ayudante de cocina y servicio al 45 %, refuerzo de festivales al 10 % y suplencias de vacaciones al 6 %). Antes la cuenta de resultados tecleaba 42.000 € mientras su propia hoja sumaba 76.566 €.',
          'El aparcamiento y la base del vehículo tienen ahora su propia partida (400 €/mes, 4.800 € al año) en vez del alquiler que este negocio no paga, y la amortización se calcula sobre lo que de verdad es inmovilizado: el vehículo y su adaptación a 8 años, el equipamiento a 10, con el Impuesto de Sociedades al 15 % los dos primeros ejercicios con beneficio.',
          'El checklist pasa de 59 a 68 trámites: Veri*factu, registro horario, RGPD, hojas de reclamaciones, gestor de residuos y aceite usado, DDD y canon de música. El registro sanitario ya no es el estatal (RGSEAA) sino el de tu comunidad autónoma, y el epígrafe de IAE deja de ser el de un restaurante fijo.',
          'El documento Word sigue en la versión anterior: las cifras válidas hoy son las del Excel actualizado (el Word se pondrá al día en la próxima versión).',
          'Número de versión (2.2) en los dos ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 2 ficheros',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 2 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-paellero-eventos': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 4 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Metadatos y autoría actualizados en los 4 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-panaderia': {
    version: '2.2',
    updated: '2026-09-05',
    entries: [
      {
        version: '2.2',
        date: '2026-09-05',
        title: 'El plan financiero pasa a ser un modelo completo: personal por fórmula, tesorería y financiación nuevas, y el pan común al 4 % de IVA',
        changes: [
          'El coste de personal del P&L sale ahora de la hoja Personal, calculado puesto por puesto y no a mano aparte: seis puestos —maestro panadero, oficial panadero, ayudante de obrador, dependienta, un refuerzo de fin de semana y una línea de suplencias de vacaciones— por 113.861 € al año, con la comprobación de que las horas contratadas cubren el turno de madrugada del obrador y el horario de la tienda.',
          'Dos hojas nuevas: «Tesorería 12 meses» (cobros, pagos y liquidación trimestral del IVA, mes a mes) y «Financiación» (origen de los fondos, cuadro de amortización del préstamo con carencia y comprobación de la capacidad de pago año a año).',
          'El IVA se reparte ahora por línea de venta: el pan común y las harinas panificables al 4 % —el tipo superreducido del art. 91.Dos.1.1.º de la Ley del IVA—, y la bollería, la pastelería y el café al 10 %, con una celda para ajustar el peso del pan común según tu carta.',
          'Un solo calendario de apertura (310 días al año) y el ticket declarado sin IVA (5,50 €), con el caso base recalculado: los cinco ratios del libro —coste de mercancía, personal, alquiler, resultado neto y margen bruto— cumplen en los tres años.',
          'El punto de equilibrio pasa a expresarse en transacciones diarias de mostrador, no en kilos de pan: 162 al día para cubrir los costes y 155 en términos de caja.',
          'Checklist de apertura ampliado a 66 trámites en 6 fases: RGPD, Veri*factu, gestor de residuos autorizado, control de plagas, registro horario y licencia de música ambiental, con el epígrafe de IAE corregido (644.1 para la venta en tienda, con aviso del 419.1 si el canal mayorista crece) y el registro sanitario correcto: el de tu Comunidad Autónoma, no el RGSEAA estatal, salvo que tu volumen mayorista te obligue a consultarlo con tu gestoría.',
          'El plan de negocio en Word sigue siendo el de la versión 1.1 —no se ha actualizado en este lanzamiento— y sus cifras (facturación, inversión, plantilla) no coinciden con las del Excel: mientras tanto, las cifras válidas son las del plan financiero Excel; el documento Word se actualizará en la próxima versión.',
          'Número de versión (2.2) en los dos ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 2 ficheros',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 2 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-parrillero-asador-eventos': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 4 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 4 ficheros.',
        ],
      },
    ],
  },
  'plan-negocio-tapas-bar': {
    version: '2.2',
    updated: '2026-09-05',
    entries: [
      {
        version: '2.2',
        date: '2026-09-05',
        title: 'El plan financiero se convierte en un modelo con fórmulas, con el IVA de sala del tapas bar al 10 %',
        changes: [
          'El Excel pasa de 6 hojas con cifras fijas a 9 hojas con 742 fórmulas: cambias un dato en una celda verde —el ticket, los clientes al día, el alquiler— y el libro entero se recalcula solo.',
          'Tres hojas nuevas: «0. Supuestos», que concentra todos los datos de partida en un único sitio; «Tesorería 12 meses», con la liquidación del IVA mes a mes; y «Financiación», con el cuadro de amortización del préstamo.',
          'El coste de personal del P&L ya sale de la hoja «Personal» —108.368 € al año para los 7 puestos del tapas bar, con semáforo si un sueldo baja del salario mínimo según su jornada—, y no de una cifra escrita aparte.',
          'IVA por línea de venta: en sala todo va al 10 %, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992 del IVA); el 21 % general sólo alcanza al alcohol que sale por delivery.',
          'Impuesto de Sociedades al 15 % en los dos primeros ejercicios con beneficio, compensando pérdidas anteriores: el tipo que corresponde a una empresa de nueva creación.',
          'El checklist de apertura pasa de 63 a 73 trámites: suma RGPD, registro horario, Veri*factu, gestor de residuos, desinsectación/desratización (DDD) y derechos de autor por la música ambiental de la barra.',
          'El documento Word (plan de negocio DOCX) sigue en la versión anterior y no se ha actualizado en esta revisión: las cifras válidas de este plan son las del Excel; el Word se pondrá al día en la próxima versión.',
          'Número de versión (2.2) en los dos ficheros.',
        ],
      },
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 2 ficheros',
        changes: [
          'Desplegable ✓ / ☐ / N/A en la columna de marca, resaltado en verde al marcar y contador de tareas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión (1.1) en la hoja de instrucciones de los ficheros que la incluyen.',
          'Metadatos, instrucciones y autoría actualizados en los 2 ficheros.',
        ],
      },
    ],
  },
  'mega-pack-tareas': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión 1.1 de todos los kits incluidos',
        changes: [
          'Los totales de los checklists se ven también en el móvil y en visores que no recalculan (valores guardados en el fichero).',
          'Impresión en A4 configurada en todas las hojas de los 13 kits: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Columna de marca con desplegable y resaltado en verde al marcar en todos los kits; el total de tareas completadas se recalcula en las hojas de checklist (en marisquería, panadería, food truck y tapas bar la marca va en la columna OK, sin contador).',
          'Metadatos y autoría actualizados en los ficheros de los 13 kits.',
          'El Kit Pastelería incluido pasa a su versión 2.0, con cuatro plantillas nuevas.',
        ],
      },
    ],
  },
};

const MESES = [
  'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
  'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
];

/** "18 de agosto de 2026" a partir de "2026-08-18" (sin depender de Intl/timezone). */
export function formatFechaLarga(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  if (!y || !m || !d) return iso;
  return `${d} de ${MESES[m - 1]} de ${y}`;
}

/** "18/08/2026" a partir de "2026-08-18". */
export function formatFechaCorta(iso: string): string {
  const [y, m, d] = iso.split('-');
  if (!y || !m || !d) return iso;
  return `${d}/${m}/${y}`;
}
