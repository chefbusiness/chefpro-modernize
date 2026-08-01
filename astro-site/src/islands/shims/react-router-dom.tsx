/**
 * Shim mínimo de react-router-dom para los islands de la zona app (Fase 5).
 *
 * La SPA monta gates/dashboards bajo <BrowserRouter>; en Astro no hay router:
 * navegar de /X-access a /X-library es una carga de página completa normal.
 * Se resuelve vía alias de Vite en astro.config.mjs para que los componentes
 * de la SPA se importen cross-root SIN tocar ni un byte de sus ficheros.
 *
 * Superficie EXACTA usada por el cierre de imports de la zona app (censo
 * 2026-07-19, 107 ficheros): useSearchParams, useNavigate, Navigate,
 * useLocation. Fase 6 (censo 2026-07-19, 56 ficheros marketing/legales):
 * + useParams (useLanguage sincroniza idioma desde /:lang) y + Link
 * (OtherFreeTools). Nada más — no ampliar sin re-censar.
 *
 * Los islands de la zona APP siguen yendo con client:only="react" (contenido
 * de pago: renderizarlo en servidor lo metería en el HTML público). Los de
 * MARKETING pasan por SSR desde 2026-08-01, así que aquí `window` puede no
 * existir: la ubicación llega entonces por <SsrLocation>, que la página Astro
 * rellena con el path que está construyendo. Sin eso, `useParams` devolvía {} en
 * el servidor y las seis versiones no españolas se renderizaban EN ESPAÑOL.
 *
 * ⚠️ Referencias ESTABLES obligatorias: ProductAccessGate mete `params` y
 * `navigate` en las deps de su useEffect de verificación — devolver un objeto
 * nuevo por render relanzaría el fetch a verify-purchase en bucle infinito.
 */
import { createContext, useContext, useEffect, useState, type ReactNode } from 'react';

interface Ubicacion {
  pathname: string;
  search: string;
  hash: string;
}

const VACIA: Ubicacion = { pathname: '/', search: '', hash: '' };
const UbicacionSSR = createContext<Ubicacion | null>(null);

export function SsrLocation({ pathname, children }: { pathname: string; children: ReactNode }) {
  const [valor] = useState<Ubicacion>(() => ({ pathname, search: '', hash: '' }));
  return <UbicacionSSR.Provider value={valor}>{children}</UbicacionSSR.Provider>;
}

/** En el navegador manda window; en el servidor, lo que inyectó la página Astro. */
function useUbicacion(): Ubicacion {
  const delServidor = useContext(UbicacionSSR);
  if (typeof window === 'undefined') return delServidor ?? VACIA;
  return {
    pathname: window.location.pathname,
    search: window.location.search,
    hash: window.location.hash,
  };
}

export interface NavigateOptions {
  replace?: boolean;
}

// Función a nivel de módulo → referencia estable entre renders.
function navigateImpl(to: string, options?: NavigateOptions): void {
  if (typeof window === 'undefined') return;   // en SSR no se navega
  if (options?.replace) window.location.replace(to);
  else window.location.assign(to);
}

export function useNavigate() {
  return navigateImpl;
}

export function useSearchParams(): [URLSearchParams] {
  // useState con initializer → la MISMA instancia de URLSearchParams
  // durante toda la vida del componente (estabilidad para deps de efectos).
  const ubicacion = useUbicacion();
  const [params] = useState(() => new URLSearchParams(ubicacion.search));
  return [params];
}

export function useLocation() {
  const ubicacion = useUbicacion();
  const [location] = useState(() => ubicacion);
  return location;
}

export function useParams<T extends Record<string, string | undefined>>(): T {
  // Única forma usada por el cierre de imports: useParams<{ lang?: string }>()
  // en useLanguage.ts (rutas /:lang/...). En Astro el idioma va en el primer
  // segmento del path (es = sin prefijo → {}). useState initializer → misma
  // referencia entre renders (useLanguage la mete en deps de su useEffect).
  const ubicacion = useUbicacion();
  const [params] = useState(() => {
    const seg = ubicacion.pathname.split('/')[1];
    return (['en', 'fr', 'de', 'it', 'pt', 'nl'].includes(seg)
      ? { lang: seg }
      : {}) as T;
  });
  return params;
}

export function Link({
  to,
  replace: _replace,
  state: _state,
  children,
  ...rest
}: {
  to: string | { pathname?: string; search?: string; hash?: string };
  replace?: boolean;
  state?: unknown;
  children?: ReactNode;
  [key: string]: unknown;
}) {
  // Sin router, un <Link> es un <a>: navegar entre páginas Astro es una carga
  // de página completa normal. Se ignoran replace/state (semántica de historial
  // SPA sin equivalente aquí).
  const href =
    typeof to === 'string'
      ? to
      : `${to?.pathname ?? ''}${to?.search ?? ''}${to?.hash ?? ''}`;
  return (
    <a href={href} {...rest}>
      {children}
    </a>
  );
}

export function Navigate({ to, replace = false }: { to: string; replace?: boolean }) {
  // La SPA lo usa como <Navigate to={redirectTo} replace /> en ProtectedRoute.
  // Redirigir en useEffect (no en el cuerpo del render): seguro ante dobles
  // renders de React y sin side effects durante el render.
  useEffect(() => {
    navigateImpl(to, { replace });
  }, [to, replace]);
  return null;
}
