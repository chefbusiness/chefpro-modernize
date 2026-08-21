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
