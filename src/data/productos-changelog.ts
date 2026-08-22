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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 9 ficheros',
        changes: [
          'Checklist de onboarding: el porcentaje de progreso ahora se calcula de verdad.',
          'Resaltado en verde al marcar y contador de tareas completadas.',
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 9 ficheros.',
        ],
      },
    ],
  },
  'kit-inventario': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 9 ficheros',
        changes: [
          'Impresión en A4 configurada en todas las hojas: ajuste a una página de ancho, cabecera repetida en cada página y pie con numeración.',
          'Número de versión actualizado a 1.1 en la hoja de instrucciones de cada fichero.',
          'Metadatos, instrucciones y autoría actualizados en los 9 ficheros.',
        ],
      },
    ],
  },
  'kit-plan-financiero': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
      {
        version: '1.1',
        date: '2026-08-22',
        title: 'Revisión completa de los 10 ficheros',
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
          'Línea de autoría anclada en las Instrucciones de las 11 plantillas; versión 2.0 · agosto 2026.',
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
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-cafeteria': {
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
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-catering': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-heladeria': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
          'Datos de autoría actualizados con la biografía vigente del creador.',
          'Metadatos, instrucciones y autoría actualizados en los 11 ficheros.',
        ],
      },
    ],
  },
  'kit-tareas-restaurante-creativo': {
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
