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
      // COM-22/RC-05/RD-25 · decía «ratios de productividad», que no existen
      // en ninguno de los 9 ficheros del kit: lo más cercano son los
      // cubiertos por empleado y servicio del BONUS-02, que son un ratio de
      // DIMENSIONAMIENTO y viven en el bonus. Y se omitían onboarding,
      // vacaciones y evaluación, que sí están. Este texto se sirve en producción (UseCasePageContent
      // y PSeoCityPageContent vía getProductsByIds).
      es: 'Cuadrantes de turnos, horas extra, coste laboral, onboarding, vacaciones y evaluación de equipo.',
      en: 'Shift schedules, overtime, labor cost, onboarding, holidays, and team performance reviews.',
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
  // ── Guías «Cómo Montar…» (línea de guías de apertura) ────────────────────
  'guia-panaderia-obrador': {
    id: 'guia-panaderia-obrador',
    url: '/guia-panaderia-obrador',
    price: '€65',
    name: { es: 'Guía Panadería con Obrador', en: 'Guide: Bakery with Production Room' },
    description: {
      es: 'Modelo artesanal con masa madre: 20 capítulos, 9 Excel y manual del obrador.',
      en: 'Artisan sourdough model: 20 chapters, 9 Excel files and a production-room manual.',
    },
  },
  'guia-restaurante-japones': {
    id: 'guia-restaurante-japones',
    url: '/guia-restaurante-japones',
    price: '€65',
    name: { es: 'Guía Restaurante Japonés', en: 'Guide: Japanese Restaurant' },
    description: {
      es: '60 plazas, todo el roadmap para abrir un japonés en España.',
      en: '60 seats, the full roadmap to open a Japanese restaurant in Spain.',
    },
  },
  'guia-restaurante-mexicano': {
    id: 'guia-restaurante-mexicano',
    url: '/guia-restaurante-mexicano',
    price: '€65',
    name: { es: 'Guía Restaurante Mexicano', en: 'Guide: Mexican Restaurant' },
    description: {
      es: '80 plazas: 20 capítulos, 8 plantillas Excel y business plan modelo.',
      en: '80 seats: 20 chapters, 8 Excel templates and a model business plan.',
    },
  },
  'guia-restaurante-nikkei': {
    id: 'guia-restaurante-nikkei',
    url: '/guia-restaurante-nikkei',
    price: '€65',
    name: { es: 'Guía Restaurante Nikkei', en: 'Guide: Nikkei Restaurant' },
    description: {
      es: '60 plazas, la fusión peruano-japonesa con su roadmap completo.',
      en: '60 seats, Peruvian-Japanese fusion with its full roadmap.',
    },
  },
  'guia-restaurante-peruano': {
    id: 'guia-restaurante-peruano',
    url: '/guia-restaurante-peruano',
    price: '€65',
    name: { es: 'Guía Restaurante Peruano', en: 'Guide: Peruvian Restaurant' },
    description: {
      es: '80 plazas: 20 capítulos, 8 plantillas Excel y manual de operaciones.',
      en: '80 seats: 20 chapters, 8 Excel templates and an operations manual.',
    },
  },
  // ── Planes de negocio (Excel financiero + checklist de apertura) ─────────
  'plan-negocio-cafeteria': {
    id: 'plan-negocio-cafeteria',
    url: '/plan-negocio-cafeteria',
    price: '€29',
    name: { es: 'Plan de Negocio: Cafetería', en: 'Business Plan: Coffee Shop' },
    description: {
      es: 'Plan financiero Excel, inversión inicial y checklist de apertura.',
      en: 'Excel financial plan, start-up investment and opening checklist.',
    },
  },
  'plan-negocio-food-truck': {
    id: 'plan-negocio-food-truck',
    url: '/plan-negocio-food-truck',
    price: '€29',
    name: { es: 'Plan de Negocio: Food Truck', en: 'Business Plan: Food Truck' },
    description: {
      es: 'Plan financiero Excel, inversión inicial y checklist de apertura.',
      en: 'Excel financial plan, start-up investment and opening checklist.',
    },
  },
  'plan-negocio-bar-restaurante': {
    id: 'plan-negocio-bar-restaurante',
    url: '/plan-negocio-bar-restaurante',
    price: '€35',
    name: { es: 'Plan de Negocio: Bar-Restaurante', en: 'Business Plan: Bar-Restaurant' },
    description: {
      es: 'Plan financiero Excel, inversión inicial y checklist de apertura.',
      en: 'Excel financial plan, start-up investment and opening checklist.',
    },
  },
  'plan-negocio-panaderia': {
    id: 'plan-negocio-panaderia',
    url: '/plan-negocio-panaderia',
    price: '€35',
    name: { es: 'Plan de Negocio: Panadería', en: 'Business Plan: Bakery' },
    description: {
      es: 'Obrador incluido: plan financiero Excel e inversión inicial.',
      en: 'Production room included: Excel financial plan and start-up investment.',
    },
  },
  'plan-negocio-tapas-bar': {
    id: 'plan-negocio-tapas-bar',
    url: '/plan-negocio-tapas-bar',
    price: '€35',
    name: { es: 'Plan de Negocio: Tapas Bar', en: 'Business Plan: Tapas Bar' },
    description: {
      es: 'Gastrobar: plan financiero Excel, DOCX y checklist de apertura.',
      en: 'Gastrobar: Excel financial plan, DOCX and opening checklist.',
    },
  },
  'plan-catering-tematico-eventos': {
    id: 'plan-catering-tematico-eventos',
    url: '/plan-catering-tematico-eventos',
    price: '€45',
    name: { es: 'Plan de Negocio: Catering Temático', en: 'Business Plan: Themed Catering' },
    description: {
      es: 'Catering y kit temático para eventos, con 11 entregables.',
      en: 'Catering and themed event kit, with 11 deliverables.',
    },
  },
  'plan-chef-privado-showcooking-eventos': {
    id: 'plan-chef-privado-showcooking-eventos',
    url: '/plan-chef-privado-showcooking-eventos',
    price: '€45',
    name: { es: 'Plan de Negocio: Chef Privado', en: 'Business Plan: Private Chef' },
    description: {
      es: 'Showcooking a domicilio y eventos, con 11 entregables.',
      en: 'At-home showcooking and events, with 11 deliverables.',
    },
  },
  'plan-negocio-paellero-eventos': {
    id: 'plan-negocio-paellero-eventos',
    url: '/plan-negocio-paellero-eventos',
    price: '€45',
    name: { es: 'Plan de Negocio: Paellero para Eventos', en: 'Business Plan: Paella Catering' },
    description: {
      es: 'Paella para eventos: plan de negocio y kit con 11 entregables.',
      en: 'Paella for events: business plan and kit with 11 deliverables.',
    },
  },
  'plan-negocio-parrillero-asador-eventos': {
    id: 'plan-negocio-parrillero-asador-eventos',
    url: '/plan-negocio-parrillero-asador-eventos',
    price: '€45',
    name: { es: 'Plan de Negocio: Parrillero para Eventos', en: 'Business Plan: Grill Catering' },
    description: {
      es: 'Asador y parrilla para eventos, con 11 entregables.',
      en: 'Grill and barbecue catering for events, with 11 deliverables.',
    },
  },
  'plan-negocio-cocteleria-eventos': {
    id: 'plan-negocio-cocteleria-eventos',
    url: '/plan-negocio-cocteleria-eventos',
    price: '€55',
    name: { es: 'Plan de Negocio: Coctelería de Eventos', en: 'Business Plan: Event Bartending' },
    description: {
      es: 'Barra móvil y coctelería para eventos, con 9 entregables.',
      en: 'Mobile bar and event cocktails, with 9 deliverables.',
    },
  },
  // ── Kits de tareas recurrentes por concepto ─────────────────────────────
  'kit-tareas-food-truck': {
    id: 'kit-tareas-food-truck',
    url: '/kit-tareas-food-truck',
    price: '€12',
    name: { es: 'Tareas: Food Truck', en: 'Tasks: Food Truck' },
    description: {
      es: 'Setup y teardown, APPCC móvil, permisos y eventos.',
      en: 'Setup and teardown, mobile HACCP, permits and events.',
    },
  },
  'kit-tareas-panaderia': {
    id: 'kit-tareas-panaderia',
    url: '/kit-tareas-panaderia',
    price: '€12',
    name: { es: 'Tareas: Panadería / Obrador', en: 'Tasks: Bakery' },
    description: {
      es: 'Turno de madrugada, masa madre, hornos y expositor.',
      en: 'Night shift, sourdough, ovens and display case.',
    },
  },
  'kit-tareas-asador': {
    id: 'kit-tareas-asador',
    url: '/kit-tareas-asador',
    price: '€14',
    name: { es: 'Tareas: Asador / Parrilla', en: 'Tasks: Grill House' },
    description: {
      es: 'Encendido de brasas, protocolo Josper, maduración y despiece.',
      en: 'Lighting the embers, Josper protocol, ageing and butchery.',
    },
  },
  'kit-tareas-marisqueria': {
    id: 'kit-tareas-marisqueria',
    url: '/kit-tareas-marisqueria',
    price: '€14',
    name: { es: 'Tareas: Marisquería', en: 'Tasks: Seafood Restaurant' },
    description: {
      es: 'Vivero, cadena de frío y APPCC de producto vivo.',
      en: 'Live tank, cold chain and HACCP for live shellfish.',
    },
  },
  'kit-tareas-sushi-bar': {
    id: 'kit-tareas-sushi-bar',
    url: '/kit-tareas-sushi-bar',
    price: '€14',
    name: { es: 'Tareas: Sushi Bar', en: 'Tasks: Sushi Bar' },
    description: {
      es: 'Arroz y corte de pescado, barra, y protocolo anisakis.',
      en: 'Rice and fish cutting, counter service, and anisakis protocol.',
    },
  },
  'kit-tareas-tapas-bar': {
    id: 'kit-tareas-tapas-bar',
    url: '/kit-tareas-tapas-bar',
    price: '€14',
    name: { es: 'Tareas: Tapas Bar / Gastrobar', en: 'Tasks: Tapas Bar' },
    description: {
      es: 'Barra, vitrina de tapas y rotación en servicio continuo.',
      en: 'Counter, tapas display and turnover in continuous service.',
    },
  },
  // ── Bundle ───────────────────────────────────────────────────────────────
  'mega-pack-tareas': {
    id: 'mega-pack-tareas',
    url: '/mega-pack-tareas',
    price: '€89',
    name: { es: 'Mega Pack Tareas Recurrentes', en: 'Mega Pack: Recurring Tasks' },
    description: {
      es: 'Los 13 kits de tareas de hostelería en un solo pack.',
      en: 'All 13 hospitality task kits in a single bundle.',
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
