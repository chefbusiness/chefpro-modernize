// Copy localizado de las páginas de paridad (contacto, FAQ, sobre, formación,
// hubs de prompts). El texto visible y el JSON-LD salen de los mismos campos:
// la respuesta que cita un motor de respuestas es la que lee una persona.

export type ParityLang = 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';
export type PromptLang = 'fr' | 'de' | 'it' | 'pt' | 'nl';

export interface FaqItem {
  q: string;
  a: string;
}

export interface Block {
  id: string;
  h2: string;
  /** Respuesta directa de la sección: el primer párrafo visible. */
  answer: string;
  paragraphs?: string[];
  bullets?: string[];
  faqs?: FaqItem[];
}

export interface ChannelCopy {
  icon: 'mail' | 'app' | 'whatsapp';
  tag: string;
  title: string;
  body: string;
  meta: string;
  cta: string;
}

export interface OfferCopy {
  name: string;
  /** Importe publicado en la página española. Sin IVA. */
  amount?: number;
  priceLabel: string;
  meta: string;
  detail: string;
  popular?: boolean;
}

export interface HowToCopy {
  name: string;
  description: string;
  steps: { name: string; text: string }[];
}

export interface PlanRow {
  name: string;
  price: string;
  detail: string;
}

export interface Stat {
  big: string;
  label: string;
}

export interface Standard {
  title: string;
  body: string;
}

export interface CatalogLink {
  href: string;
  title: string;
  body: string;
}

export interface PageCopy {
  title: string;
  description: string;
  keywords: string;
  eyebrow: string;
  h1: string;
  lead: string;
  answerLabel: string;
  answer: string;
  homeLabel: string;
  crumb: string;
  faqHeading: string;
  blocks: Block[];
  /** FAQ de página que no viven dentro de un bloque (contacto, sobre). */
  faqs?: FaqItem[];
  channels?: ChannelCopy[];
  waText?: string;
  emailCta?: string;
  appCta?: string;
  honesty?: string;
  offers?: OfferCopy[];
  priceNote?: string;
  howto?: HowToCopy;
  chips?: string[];
  stats?: Stat[];
  plans?: PlanRow[];
  plansHeading?: string;
  standards?: Standard[];
  standardsHeading?: string;
  catalogs?: CatalogLink[];
  ctaTitle: string;
  ctaBody: string;
  ctaPrimary: string;
  ctaSecondary: string;
}
