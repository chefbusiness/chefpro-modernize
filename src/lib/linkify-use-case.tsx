import React from 'react';
import { Link } from 'react-router-dom';
import { PRODUCTS_CATALOG } from '@/data/products-catalog';

// Productos digitales descargables: nombre exacto que aparece en el copy → URL relativa.
// Las claves se ordenan más larga primero para evitar matches parciales.
const PRODUCT_LINKS: Record<string, string> = Object.values(PRODUCTS_CATALOG).reduce((acc, p) => {
  acc[p.name] = p.url;
  return acc;
}, {} as Record<string, string>);

// Aliases adicionales (cómo se mencionan en copy vs nombre canónico)
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
  'Guía Restaurante Casual': '/guia-restaurante-casual',
  'Mega Pack Tareas': '/mega-pack-tareas',
};

const ALL_PRODUCT_LINKS: Record<string, string> = { ...PRODUCT_LINKS, ...PRODUCT_ALIASES };

// Agentes / apps de la suite — se enlazan a la home de la app (getAppUrl(lang))
// Lista canónica desde el catálogo live (audit 2026-04-26)
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

// Combinamos productos + agentes en un único array, ordenado por longitud descendente.
// El orden importa: matches más específicos primero (p. ej. "Kit de Escandallos Pro" antes
// de "Kit" o "Escandallos" sueltos) — además evita superposiciones.
function buildPattern(): { regex: RegExp; entries: Array<{ text: string; type: 'product' | 'agent'; href: string }> } {
  const entries: Array<{ text: string; type: 'product' | 'agent'; href: string }> = [];
  for (const [name, url] of Object.entries(ALL_PRODUCT_LINKS)) {
    entries.push({ text: name, type: 'product', href: url });
  }
  for (const name of AGENT_NAMES) {
    entries.push({ text: name, type: 'agent', href: '__APP_URL__' });
  }
  // Ordenar por longitud descendente para que los matches largos vayan primero
  entries.sort((a, b) => b.text.length - a.text.length);
  // Escapar caracteres regex especiales en cada texto
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

interface LinkifyTextProps {
  text: string;
  appUrl: string;
  className?: string;
  linkClassName?: string;
}

/**
 * Recorre `text` y convierte ocurrencias de productos descargables y agentes IA
 * conocidos en hyperlinks. Productos → Link interno; agentes → window al app.
 */
export function LinkifyText({ text, appUrl, linkClassName = 'text-primary font-semibold underline-offset-2 hover:underline' }: LinkifyTextProps): JSX.Element {
  const parts = text.split(LINK_REGEX);
  return (
    <>
      {parts.map((part, i) => {
        const link = LINK_BY_TEXT[part];
        if (!link) return <React.Fragment key={i}>{part}</React.Fragment>;
        if (link.type === 'product') {
          return (
            <Link key={i} to={link.href} className={linkClassName}>
              {part}
            </Link>
          );
        }
        return (
          <a key={i} href={appUrl} target="_blank" rel="noopener noreferrer" className={linkClassName}>
            {part}
          </a>
        );
      })}
    </>
  );
}
