// Lib de rutas para las 76 URLs del cluster pSEO Ciudades (Fase 3 migración Astro).
//
// FUENTE ÚNICA DE VERDAD = los datos de la SPA. NO se copian ni se traducen textos:
// se importan PSEO_CITIES / PSEO_MODIFIERS / PSEO_CONTENT_ES cross-root por ruta
// relativa, EXACTAMENTE igual que hace use-cases.ts con ../../../src/data/use-cases.
//   astro-site/src/lib/  ->  ../../../src/data/pseo-cities
//   ..      = astro-site/src
//   ../..   = astro-site
//   ../../.. = raíz del repo
//
// Cluster SOLO en español (paridad con App.tsx 418-424 + PSeoCityPage/Hub, que
// hardcodean literales ES y pasan disableAutoHreflang a SEOHead). Por eso NO hay
// prefijo de idioma en ninguna ruta y los componentes de contenido montan el
// BaseLayout con lang="es" + locales={['es']} (solo hreflang es + x-default).
import {
  PSEO_CITIES,
  PSEO_CITY_SLUGS,
  PSEO_MODIFIERS,
  type CityData,
  type PSeoModifier,
} from '../../../src/data/pseo-cities';
import {
  PSEO_CONTENT_ES,
  fillTemplate,
  type PSeoModifierContent,
} from '../../../src/data/pseo-cities-content.es';

// Re-export: superficie única de import para los componentes de contenido, de modo
// que PSeoCityPageContent / PSeoCitiesHubPage tiren todo de '../../lib/pseo-cities'.
export { PSEO_CITIES, PSEO_CITY_SLUGS, PSEO_MODIFIERS, PSEO_CONTENT_ES, fillTemplate };
export type { CityData, PSeoModifier, PSeoModifierContent };

// ─────────────────────────────────────────────────────────────────────────────
// Helpers de path (SIN dominio, con barra inicial, sin barra final → trailingSlash
// 'never'). El segmento de modifier ES el propio valor de PSeoModifier: en la SPA
// MODIFIER_PATH (PSeoCityPage.tsx ~30-36) es una identidad modifier→segment.
// ─────────────────────────────────────────────────────────────────────────────

/** Ruta del hub del cluster. Paridad con App.tsx: /seo-restaurantes-por-ciudad. */
export const HUB_PATH = '/seo-restaurantes-por-ciudad' as const;

/** Path del hub pSEO ciudades. Ej: /seo-restaurantes-por-ciudad */
export function hubPath(): string {
  return HUB_PATH;
}

/** Path de una página de ciudad. Ej: cityPath('abrir-restaurante','madrid')
 *  -> /abrir-restaurante/madrid  (idéntico a `/${MODIFIER_PATH[m]}/${slug}` de la SPA). */
export function cityPath(modifier: PSeoModifier, citySlug: string): string {
  return `/${modifier}/${citySlug}`;
}

// ─────────────────────────────────────────────────────────────────────────────
// getStaticPaths por modifier
// ─────────────────────────────────────────────────────────────────────────────

export interface CityRouteParams {
  /** Slug de la ciudad (segmento :ciudad de /{modifier}/:ciudad en App.tsx). */
  ciudad: string;
}
export interface CityRouteProps {
  /** Objeto CityData de PSEO_CITIES (data moat por ciudad). */
  city: CityData;
}

/**
 * Rutas estáticas de UN modifier: 1 entrada por ciudad de PSEO_CITIES.
 *
 * Cobertura: TODOS los modifiers cubren TODAS las ciudades. La SPA no tiene lista
 * de ciudades por modifier — PSeoCityPage resuelve `city = PSEO_CITIES[ciudad]`
 * con el mismo record para los 5 modifiers (App.tsx 420-424). Por eso el parámetro
 * `modifier` NO filtra el conjunto de rutas; se mantiene en la firma para dejar el
 * contrato explícito y por si en el futuro la cobertura dejara de ser uniforme.
 *
 * Devuelve PSEO_CITY_SLUGS.length (= 15) entradas. 15 × 5 modifiers = 75 páginas
 * de ciudad; + 1 hub = 76 URLs (paridad exacta con el sitemap de la SPA).
 */
export function cityStaticPaths(
  modifier: PSeoModifier,
): Array<{ params: CityRouteParams; props: CityRouteProps }> {
  void modifier; // cobertura uniforme: el modifier no altera el set de ciudades.
  return PSEO_CITY_SLUGS.map((slug) => ({
    params: { ciudad: slug },
    props: { city: PSEO_CITIES[slug] },
  }));
}
