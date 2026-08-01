// GENERADO por scripts/astro-migration/fase6-generate-marketing.py — NO editar a mano.
// Island full-page (Fase 6): reutiliza la página de la SPA TAL CUAL (D5, cero
// copias). El import de i18n/config inicializa i18next global como side effect
// ANTES de montar (en la SPA lo hace main.tsx).
// Desde 2026-08-01 pasa por SSR (client:load). MarketingShell hace las dos cosas
// que en el navegador se dan por supuestas y en servidor no: fijar el idioma
// —useLanguage lo sincroniza en un useEffect, que en SSR no corre, así que sin
// esto las seis versiones no españolas se renderizarían EN ESPAÑOL— e inyectar
// la ubicación, que el shim del router leía de window.
import '@/i18n/config';
import Page from '@/pages/HerramientasGratuitas';
import MarketingShell from '../MarketingShell';

export default function Island({ lang, pathname }: { lang: string; pathname: string }) {
  return (
    <MarketingShell lang={lang} pathname={pathname}>
      <Page />
    </MarketingShell>
  );
}
