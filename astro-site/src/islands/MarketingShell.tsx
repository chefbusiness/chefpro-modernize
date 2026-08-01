/**
 * Envoltorio SSR de los islands de MARKETING (free tools y landings).
 *
 * POR QUÉ EXISTE: hasta 2026-08-01 estas 119 URLs indexables se montaban con
 * `client:only="react"`, así que Astro no las renderizaba en servidor y el HTML
 * crudo salía con CERO texto visible — title y meta correctos, cuerpo vacío
 * hasta que corriera el JS. Es exactamente la patología que motivó migrar a
 * Astro (§1 del plan maestro) y este clúster se quedó fuera del cambio.
 *
 * Pasar a `client:load` renderiza en build, pero hacen falta dos cosas que en el
 * navegador se dan por supuestas:
 *
 *   1. **La ubicación.** El shim del router leía `window.location` en el
 *      initializer de un useState, que corre DURANTE el render. En servidor
 *      reventaba con «window is not defined». Ahora la página Astro inyecta su
 *      propio path por contexto (<SsrLocation>).
 *
 *   2. **El idioma.** i18next detecta por localStorage/navigator, que no existen
 *      en servidor, y `useLanguage` lo corrige en un `useEffect` que en SSR NO
 *      corre. Sin fijarlo aquí, las seis versiones no españolas se renderizarían
 *      EN ESPAÑOL: contenido equivocado servido a Google en /en/, /fr/, /de/…
 *      Peor que no tener contenido, porque además es indexable.
 *
 * El idioma se fija con `changeLanguage` síncrono: los siete idiomas van
 * empaquetados como `resources` en src/i18n/config.ts, no hay carga asíncrona.
 * Se aplica también en cliente para que la hidratación coincida con lo servido.
 *
 * La zona APP (gates, dashboards, biblioteca Pro Prompts) NO usa esto y sigue
 * con client:only a propósito: es contenido de pago y renderizarlo en servidor
 * lo metería en el HTML público.
 */
import { useState, type ReactNode } from 'react';
// '@/' resuelve al src/ de la RAÍZ del repo; 'react-router-dom' está aliasado
// en astro.config.mjs al shim local. Ver la nota de alias en ese fichero.
import i18n from '@/i18n/config';
import { SsrLocation } from 'react-router-dom';

export default function MarketingShell({
  lang,
  pathname,
  children,
}: {
  lang: string;
  pathname: string;
  children: ReactNode;
}) {
  // useState initializer → corre una vez, ANTES del primer render de los hijos,
  // tanto en servidor como en cliente. En un useEffect llegaría tarde para SSR.
  useState(() => {
    if (i18n.language !== lang) i18n.changeLanguage(lang);
    return null;
  });
  return <SsrLocation pathname={pathname}>{children}</SsrLocation>;
}
