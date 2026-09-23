/**
 * Datos del HUB de la tienda EN (/en/digital-products) que NO son copy: tarjetas, iconos y
 * enlaces. El copy vive en ./en.json (bridge.py, revisado a mano) y el markup en
 * components/TiendaHubPage.astro (uno para todos los idiomas que vayan abriendo tienda).
 * Plan: scripts/productos-digitales/TIENDA-INTERNACIONAL.md §3.8.
 *
 * Qué producto está VIVO no se decide aquí: lo dice FAMILIAS de lib/tienda.ts. Una tarjeta
 * de `productos` solo se pinta en la rejilla cuando su familia tiene el idioma con vivo: true;
 * mientras tanto el hub la enseña como «First release» sin enlace. Así, publicar un producto
 * es cambiar UN booleano y el hub se entera solo.
 *
 * Precios: NUNCA aquí. Salen de netlify/shared/product-prices.ts (el mismo importe que cobra
 * el checkout); la tarjeta EN lee `usd` y la selección ES lee `eur`.
 */

export interface TarjetaProductoTienda {
  /** Familia de lib/tienda.ts (FAMILIAS[].familia). */
  familia: string;
  /** productId del producto en SU idioma (= slug EN), para leer el precio. */
  productId: string;
  name: string;
  image: string;
  icon: string;
}

export const PRODUCTOS_EN: TarjetaProductoTienda[] = [
  {
    familia: 'kit-escandallos',
    productId: 'recipe-costing-kit',
    name: 'Recipe Costing Kit',
    image: '/tienda-en/recipe-costing-kit-card.jpg',
    icon: 'Calculator',
  },
];

/** Iconos de la hoja de ruta, en el MISMO orden que copy.roadmap.items. */
export const ROADMAP_ICONS_EN = ['Package', 'Sparkles', 'ShieldCheck', 'ClipboardCheck', 'Users', 'BarChart3'];

/** «¿Hablas español?»: seis productos ES para el mercado hispano de EE. UU. Nombre en español
 *  (es lo que verán en la landing), una línea en inglés y precio en € leído de product-prices.
 *  Va dentro del bloque data-lang-es: tienda-gate.py lo excluye de sus barridos de español y €. */
export const SELECCION_ES = [
  { productId: 'kit-escandallos', name: 'Kit de Escandallos', blurb: 'Recipe costing templates, the Spanish edition.', href: '/kit-escandallos', image: '/kit-escandallos-hero.jpg' },
  { productId: 'guia-food-cost-ingenieria-menu', name: 'Guía Food Cost + Ingeniería de Menú', blurb: 'Food cost control and menu engineering, step by step.', href: '/guia-food-cost-ingenieria-menu', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
  { productId: 'pack-appcc', name: 'Pack APPCC', blurb: 'Food safety plan and logs (HACCP) under Spanish rules.', href: '/pack-appcc', image: '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg' },
  { productId: 'kit-inventario', name: 'Kit de Inventario', blurb: 'Stock counts, par levels and waste tracking.', href: '/kit-inventario', image: '/lovable-uploads/ai-gallery/inventario-hero.jpg' },
  { productId: 'manual-manager-restaurante', name: 'Manual del Manager de Restaurante', blurb: 'The restaurant manager’s operations manual.', href: '/manual-manager-restaurante', image: '/lovable-uploads/ai-gallery/manual-manager-hero.jpg' },
  { productId: 'pro-prompts-ebook', name: 'Pro Prompts Library', blurb: 'Ready-to-use AI prompts for hospitality.', href: '/pro-prompts-ebook', image: '/ebook-mockup-bundle.webp' },
];

/** Herramientas gratuitas enlazadas desde el hub (puerta de «food cost calculator», 1.900/mes en US). */
export const HERRAMIENTAS_EN = [
  { title: 'Food Cost Calculator', desc: 'The real cost of every dish, down to the cent.', href: '/en/food-cost-calculator-restaurant', icon: 'Calculator' },
  { title: 'Allergen Detector', desc: 'Spot the allergens in your recipes automatically.', href: '/en/restaurant-allergen-detector', icon: 'ShieldAlert' },
  { title: 'Profit Simulator', desc: 'Project revenue, costs and net profit.', href: '/en/restaurant-profit-simulator', icon: 'TrendingUp' },
  { title: 'Menu Copy Generator', desc: 'Irresistible descriptions for your menu.', href: '/en/restaurant-menu-copy-generator', icon: 'FileEdit' },
  { title: 'Brigade Calculator', desc: 'The right staffing for your service volume.', href: '/en/restaurant-brigade-calculator', icon: 'Users' },
  { title: 'Tasting Menu Generator', desc: 'Build tasting menus with AI in seconds.', href: '/en/tasting-menu-generator', icon: 'ChefHat' },
];
