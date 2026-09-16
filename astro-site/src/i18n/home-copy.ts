// Overrides de copy para el embudo home + Business → trial créditos ES.
// Vive AQUÍ (astro-site) a propósito: no se toca src/i18n/locales/*.json de la SPA.
import type { Locale } from './config';

type OverlayValue = string | string[];

export const HOME_COPY_OVERRIDES: Partial<Record<Locale, Record<string, OverlayValue>>> = {
  es: {
    'hero.subtitle': 'Agentes de negocio para food cost, alérgenos, mermas y la operación diaria. La creatividad culinaria está, pero no es lo primero.',
    'hero.description': 'Empieza el trial con créditos en la plataforma ES: calcula mermas, identifica alérgenos, escala recetas por pax y toma decisiones de coste. 75+ agentes de IA para el restaurante.',
    'hero.cta_trial': 'Probar con créditos',
    'hero.trial_note': 'Alta en 1 minuto · créditos de prueba · sin permanencia',
    'hero.see_resources': 'Ver agentes de negocio',
    'hero.social_proof_label': 'decisiones de coste, cartas y recetas generadas',
    'hero.business_pills': [
      'Food cost y mermas',
      'Alérgenos y normativa',
      'Pax y escandallo',
      'ChatGPT 5.5 para el local',
    ],
    'showcase.business_title': 'Agentes de negocio para el restaurante',
    'showcase.business_description': 'Las herramientas que bajan el food cost, evitan errores de alérgenos y ajustan la producción. Prueba con créditos, sin compromiso.',
    'showcase.use_tool': 'Probar con créditos',
    'showcase.trial_cta': 'Empezar el trial con créditos',
    'stats.tools_label': 'Agentes de negocio',
    'category_ctas.business.title': 'Optimiza el negocio',
    'category_ctas.business.description': 'Mermas, alérgenos, pax y food cost',
  },
};
