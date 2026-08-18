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
    version: '1.1',
    updated: '2026-08-18',
    entries: [
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
          'Próximamente (v2.0, sin coste): plan de producción semanal con control de mermas, control de encargos, alérgenos de vitrina (14 UE) y registro de temperaturas / recepción de mercancía.',
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
