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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
    version: '1.1',
    updated: '2026-08-22',
    entries: [
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
