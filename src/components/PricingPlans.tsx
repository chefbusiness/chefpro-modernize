/**
 * PricingPlans — bloque de precios de las 6 herramientas gratuitas.
 *
 * Desde la v2 de CRO (Keak, 20-sep-2026) es un simple envoltorio de
 * <PricingV2>: la tabla de precios es la MISMA en todo el sitio (portadas,
 * páginas de precios, landings y herramientas). Se conserva la firma
 * `{ toolKey }` para no tocar a sus 6 consumidores (TestDigitalizacion,
 * CalendarioContenidos, CalculadoraBrigada, GeneradorMenuDegustacion,
 * DetectorAlergenos, GeneradorTextosCarta).
 *
 * El toolKey se traduce a un utm_medium en kebab-case para poder medir qué
 * herramienta vende. NO se usa el toolKey crudo: es camelCase («toolScore»,
 * «toolMenuCopy») y llegaría así a Google Ads/GA, donde el resto de medios son
 * kebab (`home-pricing`, `landing-reducir-costes`), rompiendo los informes.
 * El mapa es explícito porque dos claves no se derivan de su nombre
 * (toolScore → digitalización, toolMenuCopy → textos de carta).
 *
 * Las claves i18n viejas de esta sección (`<toolKey>.pricing.*`) quedan sin
 * uso pero NO se borran de los JSON.
 */
import PricingV2 from '@/components/PricingV2';

interface PricingPlansProps {
  toolKey: string;
}

const MEDIUM_POR_TOOL: Record<string, string> = {
  toolScore: 'tool-digitalizacion',
  toolCalendario: 'tool-calendario',
  toolDegustacion: 'tool-degustacion',
  toolAlergenos: 'tool-alergenos',
  toolBrigada: 'tool-brigada',
  toolMenuCopy: 'tool-textos-carta',
};

/** Red de seguridad para un toolKey nuevo: camelCase → kebab, sin el prefijo «tool». */
const mediumDe = (toolKey: string) =>
  MEDIUM_POR_TOOL[toolKey] ??
  `tool-${toolKey.replace(/^tool/, '').replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase()}`;

export default function PricingPlans({ toolKey }: PricingPlansProps) {
  return <PricingV2 medium={mediumDe(toolKey)} />;
}
