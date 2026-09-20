/**
 * PricingPlans — bloque de precios de las 6 herramientas gratuitas.
 *
 * Desde la v2 de CRO (Keak, 20-sep-2026) es un simple envoltorio de
 * <PricingV2>: la tabla de precios es la MISMA en todo el sitio (portadas,
 * páginas de precios, landings y herramientas). Se conserva la firma
 * `{ toolKey }` para no tocar a sus 6 consumidores (TestDigitalizacion,
 * CalendarioContenidos, CalculadoraBrigada, GeneradorMenuDegustacion,
 * DetectorAlergenos, GeneradorTextosCarta), y ese toolKey pasa a ser el
 * utm_medium (`tool-<toolKey>`) para poder medir qué herramienta vende.
 *
 * Las claves i18n viejas de esta sección (`<toolKey>.pricing.*`) quedan sin
 * uso pero NO se borran de los JSON.
 */
import PricingV2 from '@/components/PricingV2';

interface PricingPlansProps {
  toolKey: string;
}

export default function PricingPlans({ toolKey }: PricingPlansProps) {
  return <PricingV2 medium={`tool-${toolKey}`} />;
}
