export type ProductLang = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

export interface ProductCatalogEntry {
  id: string;
  name: string;
  url: string;
  price: string;
  description: string;
}

interface ProductCatalogRaw {
  id: string;
  url: string;
  price: string;
  name: { es: string; en?: string };
  description: { es: string; en?: string };
}

const RAW: Record<string, ProductCatalogRaw> = {
  'pro-prompts-ebook': {
    id: 'pro-prompts-ebook',
    url: '/pro-prompts-ebook',
    price: '€9',
    name: { es: 'Pro Prompts eBook', en: 'Pro Prompts eBook' },
    description: {
      es: '200+ prompts profesionales probados para chefs y propietarios.',
      en: '200+ proven professional prompts for chefs and owners.',
    },
  },
  'kit-escandallos': {
    id: 'kit-escandallos',
    url: '/kit-escandallos',
    price: '€12',
    name: { es: 'Kit de Escandallos Pro', en: 'Recipe Costing Kit Pro' },
    description: {
      es: 'Plantillas Excel para escandallar en minutos con food cost real.',
      en: 'Excel templates that cost out recipes in minutes with real food cost.',
    },
  },
  'pack-appcc': {
    id: 'pack-appcc',
    url: '/pack-appcc',
    price: '€14',
    name: { es: 'Pack Plantillas APPCC', en: 'HACCP Templates Pack' },
    description: {
      es: 'APPCC y trazabilidad listos para inspección.',
      en: 'HACCP and traceability templates ready for inspection.',
    },
  },
  'kit-gestion-personal': {
    id: 'kit-gestion-personal',
    url: '/kit-gestion-personal',
    price: '€14',
    name: { es: 'Kit Gestión de Personal y Turnos', en: 'Staff Scheduling & Management Kit' },
    description: {
      es: 'Cuadrantes, control de horas, ratios de productividad.',
      en: 'Schedules, hour tracking, and productivity ratios.',
    },
  },
  'kit-inventario': {
    id: 'kit-inventario',
    url: '/kit-inventario',
    price: '€14',
    name: { es: 'Kit Control de Inventario', en: 'Inventory Management Kit' },
    description: {
      es: 'Inventario, compras, mermas y proveedores.',
      en: 'Inventory, purchasing, waste tracking, and supplier management.',
    },
  },
  'kit-plan-financiero': {
    id: 'kit-plan-financiero',
    url: '/kit-plan-financiero',
    price: '€39',
    name: { es: 'Kit Plan Financiero', en: 'Financial Plan Kit' },
    description: {
      es: 'Cash flow, P&L, escenarios y dashboard de ratios financieros.',
      en: 'Cash flow, P&L, scenarios, and a financial ratios dashboard.',
    },
  },
  'kit-tareas': {
    id: 'kit-tareas',
    url: '/kit-tareas',
    price: '€14',
    name: { es: 'Tareas: Restaurante Casual', en: 'Tasks: Casual Restaurant' },
    description: {
      es: 'Listas de turno, apertura, cierre, partidas en formato pro.',
      en: 'Shift checklists, opening, closing, and station tasks in pro format.',
    },
  },
  'kit-tareas-cafeteria': {
    id: 'kit-tareas-cafeteria',
    url: '/kit-tareas-cafeteria',
    price: '€12',
    name: { es: 'Tareas: Cafetería / Brunch', en: 'Tasks: Café / Brunch' },
    description: {
      es: 'Apertura, cierre, barra y sala con plantilla específica de cafetería.',
      en: 'Opening, closing, bar, and floor with a café-specific template.',
    },
  },
  'kit-tareas-pizzeria': {
    id: 'kit-tareas-pizzeria',
    url: '/kit-tareas-pizzeria',
    price: '€12',
    name: { es: 'Tareas: Pizzería', en: 'Tasks: Pizzeria' },
    description: {
      es: 'Listas de prep, mise, servicio y delivery específicas.',
      en: 'Prep, mise, service, and delivery checklists tailored to pizzerias.',
    },
  },
  'kit-tareas-hamburgueseria': {
    id: 'kit-tareas-hamburgueseria',
    url: '/kit-tareas-hamburgueseria',
    price: '€12',
    name: { es: 'Tareas: Hamburguesería', en: 'Tasks: Burger Joint' },
    description: {
      es: 'Listas de prep, montaje, servicio y delivery.',
      en: 'Prep, build, service, and delivery checklists.',
    },
  },
  'kit-tareas-dark-kitchen': {
    id: 'kit-tareas-dark-kitchen',
    url: '/kit-tareas-dark-kitchen',
    price: '€12',
    name: { es: 'Tareas: Dark Kitchen', en: 'Tasks: Dark Kitchen' },
    description: {
      es: 'Operativa multi-marca y multi-plataforma.',
      en: 'Multi-brand, multi-platform operations.',
    },
  },
  'kit-tareas-pasteleria': {
    id: 'kit-tareas-pasteleria',
    url: '/kit-tareas-pasteleria',
    price: '€12',
    name: { es: 'Tareas: Pastelería / Obrador', en: 'Tasks: Pastry Shop / Bakery' },
    description: {
      es: 'Producción, conservación, vitrina, exposición.',
      en: 'Production, storage, display case, and merchandising.',
    },
  },
  'kit-tareas-bar': {
    id: 'kit-tareas-bar',
    url: '/kit-tareas-bar',
    price: '€12',
    name: { es: 'Tareas: Bar / Cocktails', en: 'Tasks: Bar / Cocktails' },
    description: {
      es: 'Apertura, cierre, mise y prep de garnishes.',
      en: 'Opening, closing, mise, and garnish prep.',
    },
  },
  'kit-tareas-catering': {
    id: 'kit-tareas-catering',
    url: '/kit-tareas-catering',
    price: '€12',
    name: { es: 'Tareas: Catering / Eventos', en: 'Tasks: Catering / Events' },
    description: {
      es: 'Listas de evento, montaje, servicio, desmontaje, trazabilidad.',
      en: 'Event checklists: setup, service, breakdown, traceability.',
    },
  },
  'kit-tareas-hotel': {
    id: 'kit-tareas-hotel',
    url: '/kit-tareas-hotel',
    price: '€18,50',
    name: { es: 'Tareas: Hotel Completo', en: 'Tasks: Full Hotel' },
    description: {
      es: 'F&B, housekeeping, multi-punto de venta.',
      en: 'F&B, housekeeping, and multi-outlet operations.',
    },
  },
  'kit-tareas-heladeria': {
    id: 'kit-tareas-heladeria',
    url: '/kit-tareas-heladeria',
    price: '€12',
    name: { es: 'Tareas: Heladería', en: 'Tasks: Ice Cream Shop' },
    description: {
      es: 'Obrador, vitrina, mantecadora, exposición.',
      en: 'Production, display case, batch freezer, and merchandising.',
    },
  },
  'kit-tareas-chocolateria': {
    id: 'kit-tareas-chocolateria',
    url: '/kit-tareas-chocolateria',
    price: '€12',
    name: { es: 'Tareas: Chocolatería', en: 'Tasks: Chocolate Shop' },
    description: {
      es: 'Temperado, moldeado, ensamble, packaging.',
      en: 'Tempering, molding, assembly, and packaging.',
    },
  },
  'kit-tareas-restaurante-creativo': {
    id: 'kit-tareas-restaurante-creativo',
    url: '/kit-tareas-restaurante-creativo',
    price: '€12',
    name: { es: 'Tareas: Restaurante Creativo', en: 'Tasks: Creative Restaurant' },
    description: {
      es: 'Operativa para restaurantes de autor y creativos.',
      en: 'Operations playbook for chef-driven and creative restaurants.',
    },
  },
  'kit-tareas-chef-privado': {
    id: 'kit-tareas-chef-privado',
    url: '/kit-tareas-chef-privado',
    price: '€18',
    name: { es: 'Tareas: Chef Privado', en: 'Tasks: Private Chef' },
    description: {
      es: 'Operativa para chef privado y personal chef.',
      en: 'Operations playbook for private chefs and personal chefs.',
    },
  },
  'guia-dark-kitchen': {
    id: 'guia-dark-kitchen',
    url: '/guia-dark-kitchen',
    price: '€24',
    name: { es: 'Guía Cómo Montar una Dark Kitchen', en: 'Guide: How to Open a Dark Kitchen' },
    description: {
      es: 'Roadmap completo para abrir una dark kitchen.',
      en: 'Complete roadmap to launch a dark kitchen.',
    },
  },
  'guia-restaurante-gastronomico': {
    id: 'guia-restaurante-gastronomico',
    url: '/guia-restaurante-gastronomico',
    price: '€85',
    name: { es: 'Guía Restaurante Gastronómico', en: 'Guide: Fine-Dining Restaurant' },
    description: {
      es: '65 plazas, Michelin/Repsol, 20+ entregables.',
      en: '65 seats, Michelin-track, 20+ deliverables.',
    },
  },
  'guia-restaurante-casual': {
    id: 'guia-restaurante-casual',
    url: '/guia-restaurante-casual',
    price: '€65',
    name: { es: 'Guía Restaurante Casual', en: 'Guide: Casual Restaurant' },
    description: {
      es: '80 plazas, todo el roadmap para abrir un casual.',
      en: '80 seats, full roadmap to open a casual restaurant.',
    },
  },
};

function localize(entry: ProductCatalogRaw, lang: ProductLang): ProductCatalogEntry {
  return {
    id: entry.id,
    url: entry.url,
    price: entry.price,
    name: entry.name[lang as 'es' | 'en'] ?? entry.name.es,
    description: entry.description[lang as 'es' | 'en'] ?? entry.description.es,
  };
}

// Backwards-compatible: returns ES entries by default. Pass lang for localized output.
export const PRODUCTS_CATALOG: Record<string, ProductCatalogEntry> = Object.fromEntries(
  Object.entries(RAW).map(([id, raw]) => [id, localize(raw, 'es')])
);

export function getProductsByIds(ids: string[], lang: ProductLang = 'es'): ProductCatalogEntry[] {
  return ids.map(id => RAW[id]).filter(Boolean).map(raw => localize(raw, lang));
}
