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
  'Guía Restaurante Casual': '/guia-restaurante-casual',
  'Mega Pack Tareas': '/mega-pack-tareas',
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
