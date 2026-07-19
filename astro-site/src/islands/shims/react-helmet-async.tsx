/**
 * Shim no-op de react-helmet-async para los islands de la zona app (Fase 5).
 *
 * Uso real en el cierre de imports (censo 2026-07-19): 48 ficheros, todos con
 * la MISMA forma — <Helmet><meta robots noindex/><title/></Helmet>. En Astro
 * esos dos tags los emite BaseLayout server-side (prop noindex + title por
 * página), así que el Helmet cliente es redundante: este shim lo anula sin
 * tocar los componentes de la SPA y sin cargar react-helmet-async entero
 * (que además exigiría un HelmetProvider ancestro que no existe en islands).
 */
import type { ReactNode } from 'react';

export function Helmet(_props: { children?: ReactNode }) {
  return null;
}

export function HelmetProvider({ children }: { children?: ReactNode }) {
  return <>{children}</>;
}
