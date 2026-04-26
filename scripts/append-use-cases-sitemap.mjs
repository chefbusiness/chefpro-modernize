#!/usr/bin/env node
/**
 * Inyecta URLs de Casos de Uso (hub + spokes en 7 idiomas) al sitemap existente.
 * Se ejecuta tras generate-sitemap.mjs o sobre el sitemap.xml estático.
 */
import fs from 'fs';
import path from 'path';

const SITE_URL = 'https://aichef.pro';
const TODAY = new Date().toISOString().split('T')[0];

// Hub paths por idioma
const HUB_PATHS = {
  es: '/usos',
  en: '/en/use-cases',
  fr: '/fr/cas-d-usage',
  de: '/de/anwendungsfaelle',
  it: '/it/casi-uso',
  pt: '/pt/casos-uso',
  nl: '/nl/use-cases',
};

// Type segments por idioma
const TYPE_SEGMENT = {
  role: { es: 'rol', en: 'role', fr: 'role', de: 'rolle', it: 'ruolo', pt: 'funcao', nl: 'rol' },
  concept: { es: 'concepto', en: 'concept', fr: 'concept', de: 'konzept', it: 'concetto', pt: 'conceito', nl: 'concept' },
};

// Slugs por idioma — deben coincidir con src/data/use-cases.ts
const ROLE_SLUGS = [
  { es: 'propietario-restaurante', en: 'restaurant-owner', fr: 'proprietaire-restaurant', de: 'restaurantbesitzer', it: 'proprietario-ristorante', pt: 'proprietario-restaurante', nl: 'restauranteigenaar' },
  { es: 'gerente-restaurante', en: 'restaurant-manager', fr: 'gerant-restaurant', de: 'restaurantleiter', it: 'gestore-ristorante', pt: 'gerente-restaurante', nl: 'restaurantmanager' },
  { es: 'director-operaciones-grupo-restauracion', en: 'operations-director-restaurant-group', fr: 'directeur-operations-groupe-restauration', de: 'betriebsleiter-restaurantgruppe', it: 'direttore-operazioni-gruppo-ristorazione', pt: 'diretor-operacoes-grupo-restauracao', nl: 'operations-directeur-restaurantgroep' },
  { es: 'chef-ejecutivo-corporativo', en: 'executive-corporate-chef', fr: 'chef-executif-corporatif', de: 'kuechenchef-corporate', it: 'chef-esecutivo-corporativo', pt: 'chef-executivo-corporativo', nl: 'executive-chef-corporate' },
  { es: 'chef-jefe-cocina', en: 'head-chef', fr: 'chef-cuisinier', de: 'kuechenchef', it: 'capo-cuoco', pt: 'chefe-cozinha', nl: 'chef-kok' },
  { es: 'sous-chef', en: 'sous-chef', fr: 'sous-chef', de: 'sous-chef', it: 'sous-chef', pt: 'sous-chef', nl: 'sous-chef' },
  { es: 'chef-catering', en: 'catering-chef', fr: 'chef-traiteur', de: 'catering-chef', it: 'chef-catering', pt: 'chef-catering', nl: 'cateringchef' },
  { es: 'propietario-empresa-catering', en: 'catering-business-owner', fr: 'proprietaire-entreprise-traiteur', de: 'cateringbetriebsbesitzer', it: 'proprietario-azienda-catering', pt: 'proprietario-empresa-catering', nl: 'cateringbedrijfseigenaar' },
];

const CONCEPT_SLUGS = [
  { es: 'restaurante-casual', en: 'casual-restaurant', fr: 'restaurant-decontracte', de: 'casual-restaurant', it: 'ristorante-casual', pt: 'restaurante-casual', nl: 'casual-restaurant' },
  { es: 'cafeteria-brunch', en: 'cafe-brunch', fr: 'cafeteria-brunch', de: 'cafe-brunch', it: 'caffetteria-brunch', pt: 'cafeteria-brunch', nl: 'cafe-brunch' },
  { es: 'pizzeria', en: 'pizzeria', fr: 'pizzeria', de: 'pizzeria', it: 'pizzeria', pt: 'pizzaria', nl: 'pizzeria' },
  { es: 'hamburgueseria', en: 'burger-restaurant', fr: 'restaurant-burger', de: 'burger-restaurant', it: 'hamburgheria', pt: 'hamburgueria', nl: 'burgerrestaurant' },
  { es: 'dark-kitchen', en: 'dark-kitchen', fr: 'dark-kitchen', de: 'dark-kitchen', it: 'dark-kitchen', pt: 'dark-kitchen', nl: 'dark-kitchen' },
  { es: 'pasteleria-obrador', en: 'bakery-pastry-shop', fr: 'patisserie-fournil', de: 'konditorei-baeckerei', it: 'pasticceria-laboratorio', pt: 'pastelaria-obrador', nl: 'banketbakkerij' },
  { es: 'bar-cocktails', en: 'bar-cocktails', fr: 'bar-cocktails', de: 'bar-cocktails', it: 'bar-cocktail', pt: 'bar-cocktails', nl: 'bar-cocktails' },
  { es: 'catering-eventos', en: 'catering-events', fr: 'traiteur-evenements', de: 'catering-events', it: 'catering-eventi', pt: 'catering-eventos', nl: 'catering-evenementen' },
  { es: 'hotel-completo-fb', en: 'hotel-fb-complete', fr: 'hotel-restauration-complete', de: 'hotel-fb-komplett', it: 'hotel-fb-completo', pt: 'hotel-fb-completo', nl: 'hotel-fb-compleet' },
  { es: 'heladeria-artesanal', en: 'artisan-ice-cream-shop', fr: 'glacier-artisanal', de: 'eisdiele', it: 'gelateria-artigianale', pt: 'gelataria-artesanal', nl: 'ambachtelijke-ijssalon' },
  { es: 'chocolateria-bomboneria', en: 'chocolate-shop', fr: 'chocolaterie', de: 'schokoladenmanufaktur', it: 'cioccolateria', pt: 'chocolataria', nl: 'chocolaterie' },
  { es: 'restaurante-creativo-autor', en: 'creative-signature-restaurant', fr: 'restaurant-creatif-auteur', de: 'kreatives-autorenrestaurant', it: 'ristorante-creativo-autore', pt: 'restaurante-criativo-autor', nl: 'creatief-auteursrestaurant' },
  { es: 'restaurante-gastronomico-michelin', en: 'fine-dining-michelin', fr: 'restaurant-gastronomique-etoile', de: 'gourmet-restaurant-michelin', it: 'ristorante-gastronomico-stellato', pt: 'restaurante-gastronomico-michelin', nl: 'gastronomisch-restaurant-michelin' },
];

const LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];

function buildHreflangs(spokeType, slugObj) {
  const segMap = TYPE_SEGMENT[spokeType];
  return LANGS.map(l => {
    const prefix = l === 'es' ? '' : `/${l}`;
    const segment = segMap[l];
    const slug = slugObj[l];
    return `    <xhtml:link rel="alternate" hreflang="${l}" href="${SITE_URL}${prefix}${l === 'es' ? '/usos' : (l === 'en' ? '/en/use-cases' : l === 'fr' ? '/fr/cas-d-usage' : l === 'de' ? '/de/anwendungsfaelle' : l === 'it' ? '/it/casi-uso' : l === 'pt' ? '/pt/casos-uso' : '/nl/use-cases')}/${segment}/${slug}" />`;
  }).join('\n') + `\n    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE_URL}/usos/${segMap.es}/${slugObj.es}" />`;
}

function buildHubHreflangs() {
  return LANGS.map(l => {
    return `    <xhtml:link rel="alternate" hreflang="${l}" href="${SITE_URL}${HUB_PATHS[l]}" />`;
  }).join('\n') + `\n    <xhtml:link rel="alternate" hreflang="x-default" href="${SITE_URL}/usos" />`;
}

function buildUrl(loc, hreflangs, priority = '0.7', changefreq = 'weekly') {
  return `  <url>
    <loc>${loc}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
${hreflangs}
  </url>`;
}

function generateUseCasesUrls() {
  const urls = [];

  // Hub en cada idioma
  LANGS.forEach(l => {
    urls.push(buildUrl(`${SITE_URL}${HUB_PATHS[l]}`, buildHubHreflangs(), l === 'es' ? '0.9' : '0.8', 'weekly'));
  });

  // Spokes - roles
  ROLE_SLUGS.forEach(slugObj => {
    LANGS.forEach(l => {
      const prefix = HUB_PATHS[l];
      const segment = TYPE_SEGMENT.role[l];
      const slug = slugObj[l];
      urls.push(buildUrl(`${SITE_URL}${prefix}/${segment}/${slug}`, buildHreflangs('role', slugObj), l === 'es' ? '0.8' : '0.7', 'weekly'));
    });
  });

  // Spokes - conceptos
  CONCEPT_SLUGS.forEach(slugObj => {
    LANGS.forEach(l => {
      const prefix = HUB_PATHS[l];
      const segment = TYPE_SEGMENT.concept[l];
      const slug = slugObj[l];
      urls.push(buildUrl(`${SITE_URL}${prefix}/${segment}/${slug}`, buildHreflangs('concept', slugObj), l === 'es' ? '0.8' : '0.7', 'weekly'));
    });
  });

  return urls.join('\n');
}

function appendToSitemap() {
  const sitemapPath = path.join(process.cwd(), 'public', 'sitemap.xml');
  let content = fs.readFileSync(sitemapPath, 'utf8');

  // Quitar URLs ya existentes de use cases (re-ejecución idempotente).
  // Buscamos solo bloques cuyo <loc> contiene los path exactos del hub o de los
  // segmentos rol/concepto en cualquier idioma — sin tocar otras URLs base.
  const useCasePathRegex = /\n  <url>\s*<loc>https:\/\/aichef\.pro(?:\/(?:en|fr|de|it|pt|nl))?\/(?:usos|use-cases|cas-d-usage|anwendungsfaelle|casi-uso|casos-uso)(?:\/(?:rol|role|rolle|ruolo|funcao|concepto|concept|konzept|concetto|conceito)\/[^<]+)?<\/loc>[\s\S]*?<\/url>/g;
  content = content.replace(useCasePathRegex, '');

  const newUrls = generateUseCasesUrls();
  content = content.replace('</urlset>', `\n${newUrls}\n</urlset>`);

  fs.writeFileSync(sitemapPath, content);
  const totalUrls = (content.match(/<url>/g) || []).length;
  const useCasesUrls = (newUrls.match(/<url>/g) || []).length;
  console.log(`✅ Sitemap updated: +${useCasesUrls} use-cases URLs · ${totalUrls} total`);
}

appendToSitemap();
