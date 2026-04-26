export interface ProductCatalogEntry {
  id: string;
  name: string;
  url: string;
  price: string;
  description: string;
}

export const PRODUCTS_CATALOG: Record<string, ProductCatalogEntry> = {
  'pro-prompts-ebook': {
    id: 'pro-prompts-ebook',
    name: 'Pro Prompts eBook',
    url: '/pro-prompts-ebook',
    price: '€9',
    description: '200+ prompts profesionales probados para chefs y propietarios.',
  },
  'kit-escandallos': {
    id: 'kit-escandallos',
    name: 'Kit de Escandallos Pro',
    url: '/kit-escandallos',
    price: '€12',
    description: 'Plantillas Excel para escandallar en minutos con food cost real.',
  },
  'pack-appcc': {
    id: 'pack-appcc',
    name: 'Pack Plantillas APPCC',
    url: '/pack-appcc',
    price: '€14',
    description: 'APPCC y trazabilidad listos para inspección.',
  },
  'kit-gestion-personal': {
    id: 'kit-gestion-personal',
    name: 'Kit Gestión de Personal y Turnos',
    url: '/kit-gestion-personal',
    price: '€14',
    description: 'Cuadrantes, control de horas, ratios de productividad.',
  },
  'kit-inventario': {
    id: 'kit-inventario',
    name: 'Kit Control de Inventario',
    url: '/kit-inventario',
    price: '€14',
    description: 'Inventario, compras, mermas y proveedores.',
  },
  'kit-plan-financiero': {
    id: 'kit-plan-financiero',
    name: 'Kit Plan Financiero',
    url: '/kit-plan-financiero',
    price: '€39',
    description: 'Cash flow, P&L, escenarios y dashboard de ratios financieros.',
  },
  'kit-tareas': {
    id: 'kit-tareas',
    name: 'Tareas: Restaurante Casual',
    url: '/kit-tareas',
    price: '€14',
    description: 'Listas de turno, apertura, cierre, partidas en formato pro.',
  },
  'kit-tareas-cafeteria': {
    id: 'kit-tareas-cafeteria',
    name: 'Tareas: Cafetería / Brunch',
    url: '/kit-tareas-cafeteria',
    price: '€12',
    description: 'Apertura, cierre, barra y sala con plantilla específica de cafetería.',
  },
  'kit-tareas-pizzeria': {
    id: 'kit-tareas-pizzeria',
    name: 'Tareas: Pizzería',
    url: '/kit-tareas-pizzeria',
    price: '€12',
    description: 'Listas de prep, mise, servicio y delivery específicas.',
  },
  'kit-tareas-hamburgueseria': {
    id: 'kit-tareas-hamburgueseria',
    name: 'Tareas: Hamburguesería',
    url: '/kit-tareas-hamburgueseria',
    price: '€12',
    description: 'Listas de prep, montaje, servicio y delivery.',
  },
  'kit-tareas-dark-kitchen': {
    id: 'kit-tareas-dark-kitchen',
    name: 'Tareas: Dark Kitchen',
    url: '/kit-tareas-dark-kitchen',
    price: '€12',
    description: 'Operativa multi-marca y multi-plataforma.',
  },
  'kit-tareas-pasteleria': {
    id: 'kit-tareas-pasteleria',
    name: 'Tareas: Pastelería / Obrador',
    url: '/kit-tareas-pasteleria',
    price: '€12',
    description: 'Producción, conservación, vitrina, exposición.',
  },
  'kit-tareas-bar': {
    id: 'kit-tareas-bar',
    name: 'Tareas: Bar / Cocktails',
    url: '/kit-tareas-bar',
    price: '€12',
    description: 'Apertura, cierre, mise y prep de garnishes.',
  },
  'kit-tareas-catering': {
    id: 'kit-tareas-catering',
    name: 'Tareas: Catering / Eventos',
    url: '/kit-tareas-catering',
    price: '€12',
    description: 'Listas de evento, montaje, servicio, desmontaje, trazabilidad.',
  },
  'kit-tareas-hotel': {
    id: 'kit-tareas-hotel',
    name: 'Tareas: Hotel Completo',
    url: '/kit-tareas-hotel',
    price: '€18,50',
    description: 'F&B, housekeeping, multi-punto de venta.',
  },
  'kit-tareas-heladeria': {
    id: 'kit-tareas-heladeria',
    name: 'Tareas: Heladería',
    url: '/kit-tareas-heladeria',
    price: '€12',
    description: 'Obrador, vitrina, mantecadora, exposición.',
  },
  'kit-tareas-chocolateria': {
    id: 'kit-tareas-chocolateria',
    name: 'Tareas: Chocolatería',
    url: '/kit-tareas-chocolateria',
    price: '€12',
    description: 'Temperado, moldeado, ensamble, packaging.',
  },
  'kit-tareas-restaurante-creativo': {
    id: 'kit-tareas-restaurante-creativo',
    name: 'Tareas: Restaurante Creativo',
    url: '/kit-tareas-restaurante-creativo',
    price: '€12',
    description: 'Operativa para restaurantes de autor y creativos.',
  },
  'kit-tareas-chef-privado': {
    id: 'kit-tareas-chef-privado',
    name: 'Tareas: Chef Privado',
    url: '/kit-tareas-chef-privado',
    price: '€18',
    description: 'Operativa para chef privado y personal chef.',
  },
  'guia-dark-kitchen': {
    id: 'guia-dark-kitchen',
    name: 'Guía Cómo Montar una Dark Kitchen',
    url: '/guia-dark-kitchen',
    price: '€24',
    description: 'Roadmap completo para abrir una dark kitchen.',
  },
  'guia-restaurante-gastronomico': {
    id: 'guia-restaurante-gastronomico',
    name: 'Guía Restaurante Gastronómico',
    url: '/guia-restaurante-gastronomico',
    price: '€85',
    description: '65 plazas, Michelin/Repsol, 20+ entregables.',
  },
  'guia-restaurante-casual': {
    id: 'guia-restaurante-casual',
    name: 'Guía Restaurante Casual',
    url: '/guia-restaurante-casual',
    price: '€65',
    description: '80 plazas, todo el roadmap para abrir un casual.',
  },
};

export function getProductsByIds(ids: string[]): ProductCatalogEntry[] {
  return ids.map(id => PRODUCTS_CATALOG[id]).filter(Boolean);
}
