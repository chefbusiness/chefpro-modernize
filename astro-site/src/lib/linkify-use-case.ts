// Port de src/lib/linkify-use-case.tsx (la SPA es la spec) a un helper que
// devuelve un STRING de HTML (para inyectar con set:html en .astro), en vez de
// nodos React. La lógica de matching (productos → link interno; agentes → link al
// app) y las tablas de nombres se copian VERBATIM del original.
//
// FUENTE ÚNICA DE VERDAD: PRODUCTS_CATALOG cross-root, exactamente como el original.
//   astro-site/src/lib/ -> ../../../src/data/products-catalog
import { PRODUCTS_CATALOG } from '../../../src/data/products-catalog';

// Productos digitales descargables: nombre exacto → URL relativa (VERBATIM).
const PRODUCT_LINKS: Record<string, string> = Object.values(PRODUCTS_CATALOG).reduce((acc, p) => {
  acc[p.name] = p.url;
  return acc;
}, {} as Record<string, string>);

// Aliases adicionales (VERBATIM del original).
const PRODUCT_ALIASES: Record<string, string> = {
  'Pro Prompts eBook': '/pro-prompts-ebook',
  'Kit de Escandallos Pro': '/kit-escandallos',
  'Pack de Plantillas APPCC': '/pack-appcc',
  'Pack APPCC': '/pack-appcc',
  'Plantillas APPCC': '/pack-appcc',
  'Kit Plan Financiero': '/kit-plan-financiero',
  'Kit Inventario': '/kit-inventario',
  'Kit de Gestión de Personal': '/kit-gestion-personal',
  'Kit Gestión de Personal y Turnos': '/kit-gestion-personal',
  'Guía Cómo Montar una Dark Kitchen': '/guia-dark-kitchen',
  'Guía Restaurante Gastronómico': '/guia-restaurante-gastronomico',
  'Guía Food Cost + Ingeniería de Menú': '/guia-food-cost-ingenieria-menu',
  'Manual del Manager de Restaurante': '/manual-manager-restaurante',
  'Manual del Chef Ejecutivo': '/manual-chef-ejecutivo',
  'Cómo Montar una Pastelería': '/guia-pasteleria-obrador',
  'Cómo Montar una Chocolatería Boutique & Atelier': '/guia-chocolateria-obrador',
  'Cómo Montar una Churrería-Chocolatería': '/guia-churreria-chocolateria',
  'Guía Restaurante Casual': '/guia-restaurante-casual',
  'Mega Pack Tareas': '/mega-pack-tareas',
  // Nombres EN del catálogo (products-catalog.ts name.en): las páginas /usos/ inglesas
  // los escriben en inglés y PRODUCT_LINKS sólo indexa los ES, así que sin estos alias
  // la mención inglesa queda sin enlace.
  'Guide: How to Open a Chocolate Boutique & Atelier': '/guia-chocolateria-obrador',
  'Guide: How to Open a Churro & Hot Chocolate Shop': '/guia-churreria-chocolateria',
  'Guide: Bakery with Production Room': '/guia-panaderia-obrador',
  // 'Business Plan: Coffee Shop' (nombre EN viejo del catálogo) → landing EN desde el 4-oct-2026.
  'Business Plan: Coffee Shop': '/en/digital-products/coffee-shop-business-plan',
  // Nombre EN viejo del catálogo → landing EN desde el 24-oct-2026 (Ice Cream Shop Checklists Kit Pro).
  'Tasks: Ice Cream Shop': '/en/digital-products/ice-cream-shop-checklist-templates',
  'Tasks: Pizzeria': '/en/digital-products/pizza-shop-checklist-templates', // landing EN viva desde el 18-oct-2026
  // Nombres EN viejos del catálogo → landing EN desde el 24-oct-2026 (Chocolate Shop y Pastry Shop Checklists Kit Pro).
  'Tasks: Chocolate Shop': '/en/digital-products/chocolate-shop-checklist-templates',
  'Tasks: Pastry Shop / Bakery': '/en/digital-products/pastry-shop-checklist-templates',
  // Producto con landing propia en la tienda EN (products-catalog.ts urlByLang.en): la
  // mención inglesa enlaza a ESA landing, no a la española (TIENDA-INTERNACIONAL §3.10).
  'Food Cost Kit Pro': '/en/digital-products/food-cost-templates',
  'Restaurant Inventory Kit Pro': '/en/digital-products/restaurant-inventory-templates',
  'HACCP Food Safety Kit Pro': '/en/digital-products/haccp-templates',
  'Restaurant Staff Scheduling Kit Pro': '/en/digital-products/restaurant-schedule-templates',
  'Restaurant Financial Plan Kit Pro': '/en/digital-products/restaurant-financial-plan-templates',
  'Food Truck Business Plan Kit': '/en/digital-products/food-truck-business-plan',
  'Coffee Shop Business Plan Kit': '/en/digital-products/coffee-shop-business-plan',
  'Restaurant Business Plan Kit': '/en/digital-products/restaurant-business-plan',
  'Bakery Business Plan Kit': '/en/digital-products/bakery-business-plan',
  'Bar Business Plan Kit': '/en/digital-products/bar-business-plan',
  'Catering Business Plan Kit': '/en/digital-products/catering-business-plan',
  'Mobile Bar Business Plan Kit': '/en/digital-products/mobile-bar-business-plan',
  'BBQ Catering Business Plan Kit': '/en/digital-products/bbq-catering-business-plan',
  'Paella Catering Business Plan Kit': '/en/digital-products/paella-catering-business-plan',
  'Pizza Shop Business Plan Kit': '/en/digital-products/pizza-shop-business-plan',
  'Taco Shop Business Plan Kit': '/en/digital-products/taco-shop-business-plan',
  'Rotisserie Chicken Restaurant Business Plan Kit': '/en/digital-products/rotisserie-chicken-restaurant-business-plan',
  'Ice Cream Shop Business Plan Kit': '/en/digital-products/ice-cream-shop-business-plan',
  'Wedding Venue Business Plan Kit': '/en/digital-products/wedding-venue-business-plan',
  'Coffee Cart Business Plan Kit': '/en/digital-products/coffee-cart-business-plan',
  'Food Cost + Menu Engineering Guide': '/en/digital-products/food-cost-menu-engineering-guide',
  'How to Open a Pastry Shop': '/en/digital-products/how-to-open-a-pastry-shop',
  'Restaurant Checklists Kit Pro': '/en/digital-products/restaurant-checklist-templates',
  'Bar Checklists Kit Pro': '/en/digital-products/bar-checklist-templates',
  'Coffee Shop Checklists Kit Pro': '/en/digital-products/coffee-shop-checklist-templates',
  'Catering Checklists Kit Pro': '/en/digital-products/catering-checklist-templates',
  'Pizza Shop Checklists Kit Pro': '/en/digital-products/pizza-shop-checklist-templates',
  'Burger Joint Checklists Kit Pro': '/en/digital-products/burger-joint-checklist-templates',
  'Ghost Kitchen Checklists Kit Pro': '/en/digital-products/ghost-kitchen-checklist-templates',
  'Ice Cream Shop Checklists Kit Pro': '/en/digital-products/ice-cream-shop-checklist-templates',
  'Hotel Checklists Kit Pro': '/en/digital-products/hotel-checklist-templates',
  'Taco Shop Checklists Kit Pro': '/en/digital-products/taco-shop-checklist-templates',
  'Chocolate Shop Checklists Kit Pro': '/en/digital-products/chocolate-shop-checklist-templates',
  'Pastry Shop Checklists Kit Pro': '/en/digital-products/pastry-shop-checklist-templates',
  'Gastro Pro Prompts eBook': '/en/digital-products/ai-prompts-for-restaurants',
};

const ALL_PRODUCT_LINKS: Record<string, string> = { ...PRODUCT_LINKS, ...PRODUCT_ALIASES };

// Agentes / apps de la suite — enlazan a la home del app (VERBATIM del original).
const AGENT_NAMES: string[] = [
  // Gastro Profile Pro
  'Chef Ejecutivo Pro',
  'Chef Privado Pro',
  'Gerente de Restaurante Pro',
  'Comida de Personal',
  // Creatividad Culinaria
  'Cocina Creativa',
  'Pastelería Creativa',
  'Chocolatería Creativa',
  'Heladería Creativa',
  'Panadería Creativa',
  'Fermentus Con AI+',
  'VegChef Plant-Based',
  'Food Pairing AI',
  // Gastro Conocimiento
  'Gastro Lexicum',
  'GastroIMG Gen+',
  'Sonar Deep Research',
  // Herramientas y Utilities
  'ChatGPT 5',
  'Mermas GenCal',
  'ID Alérgenos',
  'Mental Coach',
  'Conversor Ing',
  'Calcula Pax',
  '¿Quién Soy?',
  // Conceptos de Negocio
  'Catering AI+',
  'Burger Pro AI+',
  'Food Truck AI+',
  'Bar & Lounge AI+',
  'Casual Restaurants AI+',
  // Proveedores
  'Sosa Ingredients Agent',
  'tSpoonLab Agent',
  // Contenidos y RRSS
  'MenuDish Local SEO',
  'Gastro Calendar',
  'InstaFlow AI Pro',
  'PinterAI Content Pro',
  'Pinterest Pins Gen',
  'BlogPost SEO Gen+',
  'Keyword Discovery AI+',
];

function buildPattern(): { regex: RegExp; entries: Array<{ text: string; type: 'product' | 'agent'; href: string }> } {
  const entries: Array<{ text: string; type: 'product' | 'agent'; href: string }> = [];
  for (const [name, url] of Object.entries(ALL_PRODUCT_LINKS)) {
    entries.push({ text: name, type: 'product', href: url });
  }
  for (const name of AGENT_NAMES) {
    entries.push({ text: name, type: 'agent', href: '__APP_URL__' });
  }
  // Ordenar por longitud descendente para que los matches largos vayan primero.
  entries.sort((a, b) => b.text.length - a.text.length);
  const escaped = entries.map(e => e.text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  const regex = new RegExp(`(${escaped.join('|')})`, 'g');
  return { regex, entries };
}

const { regex: LINK_REGEX, entries: LINK_ENTRIES } = buildPattern();
const LINK_BY_TEXT: Record<string, { type: 'product' | 'agent'; href: string }> = LINK_ENTRIES.reduce(
  (acc, e) => {
    if (!acc[e.text]) acc[e.text] = { type: e.type, href: e.href };
    return acc;
  },
  {} as Record<string, { type: 'product' | 'agent'; href: string }>
);

const LINK_CLASS = 'text-primary font-semibold underline-offset-2 hover:underline';

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/**
 * Equivalente a <LinkifyText> de la SPA, pero devuelve una cadena HTML segura
 * para set:html. Productos → <a> interno; agentes → <a> externo al app (target=_blank).
 * El texto NO enlazado se escapa (los enlaces envuelven el texto escapado).
 */
export function linkifyHtml(text: string, appUrl: string): string {
  const parts = text.split(LINK_REGEX);
  return parts
    .map(part => {
      const link = LINK_BY_TEXT[part];
      if (!link) return escapeHtml(part);
      const label = escapeHtml(part);
      if (link.type === 'product') {
        return `<a href="${link.href}" class="${LINK_CLASS}">${label}</a>`;
      }
      return `<a href="${escapeHtml(appUrl)}" target="_blank" rel="noopener noreferrer" class="${LINK_CLASS}">${label}</a>`;
    })
    .join('');
}
