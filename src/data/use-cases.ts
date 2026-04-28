import type { ReactNode } from 'react';

export type UseCaseType = 'role' | 'concept' | 'task';
export type LangCode = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

export interface UseCaseSlug {
  es: string;
  en: string;
  fr: string;
  de: string;
  it: string;
  pt: string;
  nl: string;
}

export interface UseCaseFeature {
  icon: string;
  title: string;
  description: string;
  link?: string;
}

export interface UseCaseFAQ {
  q: string;
  a: string;
}

export interface UseCaseAppHighlight {
  name: string;
  category: string;
  description: string;
}

export interface UseCaseMetric {
  value: string;
  label: string;
}

export interface UseCaseBeforeAfter {
  beforeTitle: string;
  beforeItems: string[];
  afterTitle: string;
  afterItems: string[];
}

export interface UseCaseContent {
  h1: string;
  heroSubtitle: string;
  heroTagline: string;
  badge: string;
  painsTitle: string;
  pains: string[];
  featuresTitle: string;
  features: UseCaseFeature[];
  workflowTitle: string;
  workflow: string[];
  productsTitle: string;
  productIds: string[];
  testimonialQuote: string;
  testimonialAuthor: string;
  testimonialRole: string;
  faqTitle: string;
  faqs: UseCaseFAQ[];
  ctaTitle: string;
  ctaSubtitle: string;
  seo: {
    title: string;
    description: string;
    keywords: string;
    ogImage: string;
  };
  // Secciones opcionales (solo en landings premium enriquecidas)
  personalizationTitle?: string;
  personalizationBody?: string;
  appsTitle?: string;
  apps?: UseCaseAppHighlight[];
  metrics?: UseCaseMetric[];
  beforeAfter?: UseCaseBeforeAfter;
  appUrlPath?: string; // ej. "/chef-ejecutivo-pro" para CTA específico
  galleryImages?: string[]; // 6 imágenes /lovable-uploads/ai-gallery/use-case-*.jpg
  galleryTitle?: string;
  gallerySubtitle?: string;
}

export interface UseCase {
  id: string;
  type: UseCaseType;
  iconKey: string;
  colorTheme: 'amber' | 'blue' | 'emerald' | 'rose' | 'purple' | 'orange' | 'indigo' | 'pink' | 'teal' | 'red';
  slug: UseCaseSlug;
  content: Record<LangCode, UseCaseContent>;
}

const STUB_LANGS: LangCode[] = ['en', 'fr', 'de', 'it', 'pt', 'nl'];

import { USE_CASES_CONTENT_ES } from './use-cases-content.es';
import { USE_CASES_CONTENT_EN } from './use-cases-content.en';

function makeContent(id: string): Record<LangCode, UseCaseContent> {
  const es = USE_CASES_CONTENT_ES[id];
  if (!es) {
    throw new Error(`Missing ES content for use-case id: ${id}`);
  }
  const en = USE_CASES_CONTENT_EN[id] ?? es;
  const out: Record<LangCode, UseCaseContent> = {
    es,
    en,
    fr: es,
    de: es,
    it: es,
    pt: es,
    nl: es,
  };
  return out;
}

// Whether the spoke has a real translation in `lang` (vs. ES fallback baked in by makeContent).
// Use this for hub-card filtering and any "real translation only" logic. The runtime spoke
// page is fine with falling back to ES — the hub should not advertise mixed-language cards.
export function hasNativeContent(id: string, lang: LangCode): boolean {
  if (lang === 'es') return id in USE_CASES_CONTENT_ES;
  if (lang === 'en') return id in USE_CASES_CONTENT_EN;
  return false;
}

export const USE_CASES: UseCase[] = [
  {
    id: 'propietario-restaurante',
    type: 'role',
    iconKey: 'Crown',
    colorTheme: 'amber',
    slug: {
      es: 'propietario-restaurante',
      en: 'restaurant-owner',
      fr: 'proprietaire-restaurant',
      de: 'restaurantbesitzer',
      it: 'proprietario-ristorante',
      pt: 'proprietario-restaurante',
      nl: 'restauranteigenaar',
    },
    content: makeContent('propietario-restaurante'),
  },
  {
    id: 'gerente-restaurante',
    type: 'role',
    iconKey: 'BriefcaseBusiness',
    colorTheme: 'blue',
    slug: {
      es: 'gerente-restaurante',
      en: 'restaurant-manager',
      fr: 'gerant-restaurant',
      de: 'restaurantleiter',
      it: 'gestore-ristorante',
      pt: 'gerente-restaurante',
      nl: 'restaurantmanager',
    },
    content: makeContent('gerente-restaurante'),
  },
  {
    id: 'director-operaciones-grupo',
    type: 'role',
    iconKey: 'Building2',
    colorTheme: 'indigo',
    slug: {
      es: 'director-operaciones-grupo-restauracion',
      en: 'operations-director-restaurant-group',
      fr: 'directeur-operations-groupe-restauration',
      de: 'betriebsleiter-restaurantgruppe',
      it: 'direttore-operazioni-gruppo-ristorazione',
      pt: 'diretor-operacoes-grupo-restauracao',
      nl: 'operations-directeur-restaurantgroep',
    },
    content: makeContent('director-operaciones-grupo'),
  },
  {
    id: 'chef-ejecutivo',
    type: 'role',
    iconKey: 'ChefHat',
    colorTheme: 'rose',
    slug: {
      es: 'chef-ejecutivo-corporativo',
      en: 'executive-corporate-chef',
      fr: 'chef-executif-corporatif',
      de: 'kuechenchef-corporate',
      it: 'chef-esecutivo-corporativo',
      pt: 'chef-executivo-corporativo',
      nl: 'executive-chef-corporate',
    },
    content: makeContent('chef-ejecutivo'),
  },
  {
    id: 'chef-cocina',
    type: 'role',
    iconKey: 'Utensils',
    colorTheme: 'orange',
    slug: {
      es: 'chef-jefe-cocina',
      en: 'head-chef',
      fr: 'chef-cuisinier',
      de: 'kuechenchef',
      it: 'capo-cuoco',
      pt: 'chefe-cozinha',
      nl: 'chef-kok',
    },
    content: makeContent('chef-cocina'),
  },
  {
    id: 'sous-chef',
    type: 'role',
    iconKey: 'Flame',
    colorTheme: 'red',
    slug: {
      es: 'sous-chef',
      en: 'sous-chef',
      fr: 'sous-chef',
      de: 'sous-chef',
      it: 'sous-chef',
      pt: 'sous-chef',
      nl: 'sous-chef',
    },
    content: makeContent('sous-chef'),
  },
  {
    id: 'chef-catering',
    type: 'role',
    iconKey: 'PartyPopper',
    colorTheme: 'purple',
    slug: {
      es: 'chef-catering',
      en: 'catering-chef',
      fr: 'chef-traiteur',
      de: 'catering-chef',
      it: 'chef-catering',
      pt: 'chef-catering',
      nl: 'cateringchef',
    },
    content: makeContent('chef-catering'),
  },
  {
    id: 'propietario-catering',
    type: 'role',
    iconKey: 'Briefcase',
    colorTheme: 'teal',
    slug: {
      es: 'propietario-empresa-catering',
      en: 'catering-business-owner',
      fr: 'proprietaire-entreprise-traiteur',
      de: 'cateringbetriebsbesitzer',
      it: 'proprietario-azienda-catering',
      pt: 'proprietario-empresa-catering',
      nl: 'cateringbedrijfseigenaar',
    },
    content: makeContent('propietario-catering'),
  },
  {
    id: 'bartender-coctelero',
    type: 'role',
    iconKey: 'Wine',
    colorTheme: 'purple',
    slug: {
      es: 'bartender-coctelero',
      en: 'bartender-mixologist',
      fr: 'bartender-mixologue',
      de: 'barkeeper-mixologe',
      it: 'bartender-mixologo',
      pt: 'bartender-mixologista',
      nl: 'bartender-mixoloog',
    },
    content: makeContent('bartender-coctelero'),
  },
  {
    id: 'pizzero',
    type: 'role',
    iconKey: 'Pizza',
    colorTheme: 'red',
    slug: {
      es: 'pizzero-pizzaiolo',
      en: 'pizzaiolo',
      fr: 'pizzaiolo',
      de: 'pizzaiolo',
      it: 'pizzaiolo',
      pt: 'pizzaiolo',
      nl: 'pizzaiolo',
    },
    content: makeContent('pizzero'),
  },
  {
    id: 'panadero',
    type: 'role',
    iconKey: 'Wheat',
    colorTheme: 'amber',
    slug: {
      es: 'panadero-artesanal',
      en: 'artisan-baker',
      fr: 'boulanger-artisan',
      de: 'handwerksbaecker',
      it: 'fornaio-artigianale',
      pt: 'padeiro-artesanal',
      nl: 'ambachtelijke-bakker',
    },
    content: makeContent('panadero'),
  },
  {
    id: 'chocolatero',
    type: 'role',
    iconKey: 'Cookie',
    colorTheme: 'orange',
    slug: {
      es: 'chocolatero-bombonero',
      en: 'chocolatier',
      fr: 'chocolatier',
      de: 'chocolatier',
      it: 'cioccolatiere',
      pt: 'chocolateiro',
      nl: 'chocolatier',
    },
    content: makeContent('chocolatero'),
  },
  {
    id: 'chef-privado-personal',
    type: 'role',
    iconKey: 'ChefHat',
    colorTheme: 'teal',
    slug: {
      es: 'chef-privado-personal-chef',
      en: 'private-personal-chef',
      fr: 'chef-prive-personnel',
      de: 'privatkoch-personal-chef',
      it: 'chef-privato-personale',
      pt: 'chef-privado-pessoal',
      nl: 'prive-chef-personal-chef',
    },
    content: makeContent('chef-privado-personal'),
  },
  {
    id: 'fb-manager-hotel',
    type: 'role',
    iconKey: 'Hotel',
    colorTheme: 'blue',
    slug: {
      es: 'fb-manager-hotel',
      en: 'hotel-fb-manager',
      fr: 'fb-manager-hotel',
      de: 'fb-manager-hotel',
      it: 'fb-manager-hotel',
      pt: 'fb-manager-hotel',
      nl: 'fb-manager-hotel',
    },
    content: makeContent('fb-manager-hotel'),
  },
  {
    id: 'maitre-jefe-sala',
    type: 'role',
    iconKey: 'Crown',
    colorTheme: 'indigo',
    slug: {
      es: 'maitre-jefe-sala',
      en: 'maitre-d-head-waiter',
      fr: 'maitre-d-hotel-chef-de-rang',
      de: 'maitre-oberkellner',
      it: 'maitre-capo-sala',
      pt: 'maitre-chefe-sala',
      nl: 'maitre-d-hoofdkelner',
    },
    content: makeContent('maitre-jefe-sala'),
  },
  {
    id: 'sommelier',
    type: 'role',
    iconKey: 'Wine',
    colorTheme: 'purple',
    slug: {
      es: 'sommelier',
      en: 'sommelier',
      fr: 'sommelier',
      de: 'sommelier',
      it: 'sommelier',
      pt: 'sommelier',
      nl: 'sommelier',
    },
    content: makeContent('sommelier'),
  },
  {
    id: 'maestro-asador',
    type: 'role',
    iconKey: 'Flame',
    colorTheme: 'red',
    slug: {
      es: 'maestro-asador-parrillero',
      en: 'master-grillmaster',
      fr: 'maitre-grilladeur',
      de: 'grillmeister',
      it: 'maestro-grigliatore',
      pt: 'mestre-grelhador',
      nl: 'meester-grillmeester',
    },
    content: makeContent('maestro-asador'),
  },
  {
    id: 'maestro-heladero',
    type: 'role',
    iconKey: 'IceCream',
    colorTheme: 'pink',
    slug: {
      es: 'maestro-heladero',
      en: 'master-gelato-maker',
      fr: 'maitre-glacier',
      de: 'eismeister',
      it: 'maestro-gelatiere',
      pt: 'mestre-gelataria',
      nl: 'meester-ijsbereider',
    },
    content: makeContent('maestro-heladero'),
  },
  {
    id: 'repostero-pastelero',
    type: 'role',
    iconKey: 'Cake',
    colorTheme: 'pink',
    slug: {
      es: 'repostero-pastelero',
      en: 'pastry-chef',
      fr: 'patissier',
      de: 'konditor',
      it: 'pasticciere',
      pt: 'pasteleiro',
      nl: 'banketbakker',
    },
    content: makeContent('repostero-pastelero'),
  },
];

export const USE_CASES_CONCEPTS: UseCase[] = [
  {
    id: 'restaurante-casual',
    type: 'concept',
    iconKey: 'UtensilsCrossed',
    colorTheme: 'amber',
    slug: {
      es: 'restaurante-casual',
      en: 'casual-restaurant',
      fr: 'restaurant-decontracte',
      de: 'casual-restaurant',
      it: 'ristorante-casual',
      pt: 'restaurante-casual',
      nl: 'casual-restaurant',
    },
    content: makeContent('restaurante-casual'),
  },
  {
    id: 'cafeteria-brunch',
    type: 'concept',
    iconKey: 'Coffee',
    colorTheme: 'orange',
    slug: {
      es: 'cafeteria-brunch',
      en: 'cafe-brunch',
      fr: 'cafeteria-brunch',
      de: 'cafe-brunch',
      it: 'caffetteria-brunch',
      pt: 'cafeteria-brunch',
      nl: 'cafe-brunch',
    },
    content: makeContent('cafeteria-brunch'),
  },
  {
    id: 'pizzeria',
    type: 'concept',
    iconKey: 'Pizza',
    colorTheme: 'red',
    slug: {
      es: 'pizzeria',
      en: 'pizzeria',
      fr: 'pizzeria',
      de: 'pizzeria',
      it: 'pizzeria',
      pt: 'pizzaria',
      nl: 'pizzeria',
    },
    content: makeContent('pizzeria'),
  },
  {
    id: 'hamburgueseria',
    type: 'concept',
    iconKey: 'Beef',
    colorTheme: 'orange',
    slug: {
      es: 'hamburgueseria',
      en: 'burger-restaurant',
      fr: 'restaurant-burger',
      de: 'burger-restaurant',
      it: 'hamburgheria',
      pt: 'hamburgueria',
      nl: 'burgerrestaurant',
    },
    content: makeContent('hamburgueseria'),
  },
  {
    id: 'dark-kitchen',
    type: 'concept',
    iconKey: 'Smartphone',
    colorTheme: 'purple',
    slug: {
      es: 'dark-kitchen',
      en: 'dark-kitchen',
      fr: 'dark-kitchen',
      de: 'dark-kitchen',
      it: 'dark-kitchen',
      pt: 'dark-kitchen',
      nl: 'dark-kitchen',
    },
    content: makeContent('dark-kitchen'),
  },
  {
    id: 'pasteleria-obrador',
    type: 'concept',
    iconKey: 'Cake',
    colorTheme: 'pink',
    slug: {
      es: 'pasteleria-obrador',
      en: 'bakery-pastry-shop',
      fr: 'patisserie-fournil',
      de: 'konditorei-baeckerei',
      it: 'pasticceria-laboratorio',
      pt: 'pastelaria-obrador',
      nl: 'banketbakkerij',
    },
    content: makeContent('pasteleria-obrador'),
  },
  {
    id: 'bar-cocktails',
    type: 'concept',
    iconKey: 'Wine',
    colorTheme: 'purple',
    slug: {
      es: 'bar-cocktails',
      en: 'bar-cocktails',
      fr: 'bar-cocktails',
      de: 'bar-cocktails',
      it: 'bar-cocktail',
      pt: 'bar-cocktails',
      nl: 'bar-cocktails',
    },
    content: makeContent('bar-cocktails'),
  },
  {
    id: 'catering-eventos',
    type: 'concept',
    iconKey: 'PartyPopper',
    colorTheme: 'teal',
    slug: {
      es: 'catering-eventos',
      en: 'catering-events',
      fr: 'traiteur-evenements',
      de: 'catering-events',
      it: 'catering-eventi',
      pt: 'catering-eventos',
      nl: 'catering-evenementen',
    },
    content: makeContent('catering-eventos'),
  },
  {
    id: 'hotel-completo',
    type: 'concept',
    iconKey: 'Hotel',
    colorTheme: 'blue',
    slug: {
      es: 'hotel-completo-fb',
      en: 'hotel-fb-complete',
      fr: 'hotel-restauration-complete',
      de: 'hotel-fb-komplett',
      it: 'hotel-fb-completo',
      pt: 'hotel-fb-completo',
      nl: 'hotel-fb-compleet',
    },
    content: makeContent('hotel-completo'),
  },
  {
    id: 'heladeria',
    type: 'concept',
    iconKey: 'IceCream',
    colorTheme: 'pink',
    slug: {
      es: 'heladeria-artesanal',
      en: 'artisan-ice-cream-shop',
      fr: 'glacier-artisanal',
      de: 'eisdiele',
      it: 'gelateria-artigianale',
      pt: 'gelataria-artesanal',
      nl: 'ambachtelijke-ijssalon',
    },
    content: makeContent('heladeria'),
  },
  {
    id: 'chocolateria',
    type: 'concept',
    iconKey: 'Cookie',
    colorTheme: 'amber',
    slug: {
      es: 'chocolateria-bomboneria',
      en: 'chocolate-shop',
      fr: 'chocolaterie',
      de: 'schokoladenmanufaktur',
      it: 'cioccolateria',
      pt: 'chocolataria',
      nl: 'chocolaterie',
    },
    content: makeContent('chocolateria'),
  },
  {
    id: 'restaurante-creativo',
    type: 'concept',
    iconKey: 'Sparkles',
    colorTheme: 'indigo',
    slug: {
      es: 'restaurante-creativo-autor',
      en: 'creative-signature-restaurant',
      fr: 'restaurant-creatif-auteur',
      de: 'kreatives-autorenrestaurant',
      it: 'ristorante-creativo-autore',
      pt: 'restaurante-criativo-autor',
      nl: 'creatief-auteursrestaurant',
    },
    content: makeContent('restaurante-creativo'),
  },
  {
    id: 'restaurante-gastronomico',
    type: 'concept',
    iconKey: 'Crown',
    colorTheme: 'purple',
    slug: {
      es: 'restaurante-gastronomico-michelin',
      en: 'fine-dining-michelin',
      fr: 'restaurant-gastronomique-etoile',
      de: 'gourmet-restaurant-michelin',
      it: 'ristorante-gastronomico-stellato',
      pt: 'restaurante-gastronomico-michelin',
      nl: 'gastronomisch-restaurant-michelin',
    },
    content: makeContent('restaurante-gastronomico'),
  },
  {
    id: 'restaurante-mexicano',
    type: 'concept',
    iconKey: 'UtensilsCrossed',
    colorTheme: 'red',
    slug: {
      es: 'restaurante-mexicano',
      en: 'mexican-restaurant',
      fr: 'restaurant-mexicain',
      de: 'mexikanisches-restaurant',
      it: 'ristorante-messicano',
      pt: 'restaurante-mexicano',
      nl: 'mexicaans-restaurant',
    },
    content: makeContent('restaurante-mexicano'),
  },
  {
    id: 'restaurante-peruano',
    type: 'concept',
    iconKey: 'UtensilsCrossed',
    colorTheme: 'amber',
    slug: {
      es: 'restaurante-peruano',
      en: 'peruvian-restaurant',
      fr: 'restaurant-peruvien',
      de: 'peruanisches-restaurant',
      it: 'ristorante-peruviano',
      pt: 'restaurante-peruano',
      nl: 'peruaans-restaurant',
    },
    content: makeContent('restaurante-peruano'),
  },
  {
    id: 'restaurante-japones',
    type: 'concept',
    iconKey: 'Fish',
    colorTheme: 'rose',
    slug: {
      es: 'restaurante-japones',
      en: 'japanese-restaurant',
      fr: 'restaurant-japonais',
      de: 'japanisches-restaurant',
      it: 'ristorante-giapponese',
      pt: 'restaurante-japones',
      nl: 'japans-restaurant',
    },
    content: makeContent('restaurante-japones'),
  },
  {
    id: 'restaurante-nikkei',
    type: 'concept',
    iconKey: 'Sparkles',
    colorTheme: 'emerald',
    slug: {
      es: 'restaurante-nikkei',
      en: 'nikkei-restaurant',
      fr: 'restaurant-nikkei',
      de: 'nikkei-restaurant',
      it: 'ristorante-nikkei',
      pt: 'restaurante-nikkei',
      nl: 'nikkei-restaurant',
    },
    content: makeContent('restaurante-nikkei'),
  },
  {
    id: 'restaurante-plant-based',
    type: 'concept',
    iconKey: 'Sprout',
    colorTheme: 'emerald',
    slug: {
      es: 'restaurante-plant-based-vegano',
      en: 'plant-based-vegan-restaurant',
      fr: 'restaurant-vegan-plant-based',
      de: 'plant-based-veganes-restaurant',
      it: 'ristorante-plant-based-vegano',
      pt: 'restaurante-plant-based-vegano',
      nl: 'plant-based-veganistisch-restaurant',
    },
    content: makeContent('restaurante-plant-based'),
  },
  {
    id: 'asador-parrilla',
    type: 'concept',
    iconKey: 'Flame',
    colorTheme: 'red',
    slug: {
      es: 'asador-parrilla-steakhouse',
      en: 'steakhouse-grill',
      fr: 'grill-steakhouse',
      de: 'steakhouse-grill',
      it: 'griglieria-steakhouse',
      pt: 'churrascaria-steakhouse',
      nl: 'steakhouse-grill',
    },
    content: makeContent('asador-parrilla'),
  },
  {
    id: 'coffee-shop-specialty',
    type: 'concept',
    iconKey: 'Coffee',
    colorTheme: 'amber',
    slug: {
      es: 'coffee-shop-specialty',
      en: 'specialty-coffee-shop',
      fr: 'coffee-shop-specialty',
      de: 'specialty-coffee-shop',
      it: 'coffee-shop-specialty',
      pt: 'coffee-shop-specialty',
      nl: 'specialty-coffee-shop',
    },
    content: makeContent('coffee-shop-specialty'),
  },
  {
    id: 'sushi-bar',
    type: 'concept',
    iconKey: 'Fish',
    colorTheme: 'rose',
    slug: {
      es: 'sushi-bar',
      en: 'sushi-bar',
      fr: 'sushi-bar',
      de: 'sushi-bar',
      it: 'sushi-bar',
      pt: 'sushi-bar',
      nl: 'sushi-bar',
    },
    content: makeContent('sushi-bar'),
  },
  {
    id: 'gastrobar-tapas',
    type: 'concept',
    iconKey: 'Wine',
    colorTheme: 'amber',
    slug: {
      es: 'gastrobar-tapas',
      en: 'gastrobar-tapas-bar',
      fr: 'gastrobar-tapas',
      de: 'gastrobar-tapas',
      it: 'gastrobar-tapas',
      pt: 'gastrobar-tapas',
      nl: 'gastrobar-tapas',
    },
    content: makeContent('gastrobar-tapas'),
  },
  {
    id: 'food-truck',
    type: 'concept',
    iconKey: 'Truck',
    colorTheme: 'orange',
    slug: {
      es: 'food-truck',
      en: 'food-truck',
      fr: 'food-truck',
      de: 'food-truck',
      it: 'food-truck',
      pt: 'food-truck',
      nl: 'food-truck',
    },
    content: makeContent('food-truck'),
  },
  {
    id: 'restaurante-italiano',
    type: 'concept',
    iconKey: 'UtensilsCrossed',
    colorTheme: 'red',
    slug: {
      es: 'restaurante-italiano',
      en: 'italian-restaurant',
      fr: 'restaurant-italien',
      de: 'italienisches-restaurant',
      it: 'ristorante-italiano',
      pt: 'restaurante-italiano',
      nl: 'italiaans-restaurant',
    },
    content: makeContent('restaurante-italiano'),
  },
];

export const USE_CASES_TASKS: UseCase[] = [
  {
    id: 'task-escandallos-con-ia',
    type: 'task',
    iconKey: 'Calculator',
    colorTheme: 'blue',
    slug: {
      es: 'escandallos-con-ia',
      en: 'recipe-costing-with-ai',
      fr: 'fiches-cout-avec-ia',
      de: 'rezeptkalkulation-mit-ki',
      it: 'schede-costo-con-ia',
      pt: 'fichas-custo-com-ia',
      nl: 'receptkostprijs-met-ai',
    },
    content: makeContent('task-escandallos-con-ia'),
  },
  {
    id: 'task-menu-degustacion-con-ia',
    type: 'task',
    iconKey: 'UtensilsCrossed',
    colorTheme: 'indigo',
    slug: {
      es: 'menu-degustacion-con-ia',
      en: 'tasting-menu-with-ai',
      fr: 'menu-degustation-avec-ia',
      de: 'degustationsmenue-mit-ki',
      it: 'menu-degustazione-con-ia',
      pt: 'menu-degustacao-com-ia',
      nl: 'proefmenu-met-ai',
    },
    content: makeContent('task-menu-degustacion-con-ia'),
  },
  {
    id: 'task-fichas-tecnicas-con-ia',
    type: 'task',
    iconKey: 'BookOpen',
    colorTheme: 'amber',
    slug: {
      es: 'fichas-tecnicas-con-ia',
      en: 'technical-recipe-sheets-with-ai',
      fr: 'fiches-techniques-avec-ia',
      de: 'technische-rezeptkarten-mit-ki',
      it: 'schede-tecniche-con-ia',
      pt: 'fichas-tecnicas-com-ia',
      nl: 'technische-receptkaarten-met-ai',
    },
    content: makeContent('task-fichas-tecnicas-con-ia'),
  },
  {
    id: 'task-maridajes-con-ia',
    type: 'task',
    iconKey: 'Wine',
    colorTheme: 'purple',
    slug: {
      es: 'maridajes-con-ia',
      en: 'wine-pairings-with-ai',
      fr: 'accords-mets-vins-avec-ia',
      de: 'food-pairing-mit-ki',
      it: 'abbinamenti-con-ia',
      pt: 'harmonizacoes-com-ia',
      nl: 'wijn-spijs-combinaties-met-ai',
    },
    content: makeContent('task-maridajes-con-ia'),
  },
  {
    id: 'task-reducir-mermas-con-ia',
    type: 'task',
    iconKey: 'BarChart3',
    colorTheme: 'emerald',
    slug: {
      es: 'reducir-mermas-con-ia',
      en: 'reduce-food-waste-with-ai',
      fr: 'reduire-pertes-avec-ia',
      de: 'verluste-reduzieren-mit-ki',
      it: 'ridurre-sprechi-con-ia',
      pt: 'reduzir-perdas-com-ia',
      nl: 'verspilling-verminderen-met-ai',
    },
    content: makeContent('task-reducir-mermas-con-ia'),
  },
  {
    id: 'task-appcc-digital-con-ia',
    type: 'task',
    iconKey: 'ShieldCheck',
    colorTheme: 'blue',
    slug: {
      es: 'appcc-digital-con-ia',
      en: 'digital-haccp-with-ai',
      fr: 'haccp-numerique-avec-ia',
      de: 'digitales-haccp-mit-ki',
      it: 'haccp-digitale-con-ia',
      pt: 'haccp-digital-com-ia',
      nl: 'digitale-haccp-met-ai',
    },
    content: makeContent('task-appcc-digital-con-ia'),
  },
  {
    id: 'task-carta-estacional-con-ia',
    type: 'task',
    iconKey: 'Calendar',
    colorTheme: 'orange',
    slug: {
      es: 'carta-estacional-con-ia',
      en: 'seasonal-menu-with-ai',
      fr: 'carte-saisonniere-avec-ia',
      de: 'saisonkarte-mit-ki',
      it: 'menu-stagionale-con-ia',
      pt: 'cardapio-sazonal-com-ia',
      nl: 'seizoensmenu-met-ai',
    },
    content: makeContent('task-carta-estacional-con-ia'),
  },
  {
    id: 'task-foto-gastronomica-con-ia',
    type: 'task',
    iconKey: 'Image',
    colorTheme: 'pink',
    slug: {
      es: 'foto-gastronomica-con-ia',
      en: 'food-photography-with-ai',
      fr: 'photo-gastronomique-avec-ia',
      de: 'food-fotografie-mit-ki',
      it: 'foto-gastronomica-con-ia',
      pt: 'foto-gastronomica-com-ia',
      nl: 'food-fotografie-met-ai',
    },
    content: makeContent('task-foto-gastronomica-con-ia'),
  },
];

export const ALL_USE_CASES: UseCase[] = [...USE_CASES, ...USE_CASES_CONCEPTS, ...USE_CASES_TASKS];

export function getUseCaseBySlug(slug: string, lang: LangCode = 'es'): UseCase | undefined {
  return ALL_USE_CASES.find(uc => uc.slug[lang] === slug);
}

export function getUseCasesByType(type: UseCaseType): UseCase[] {
  return ALL_USE_CASES.filter(uc => uc.type === type);
}
