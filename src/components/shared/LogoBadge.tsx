import { useLocation } from 'react-router-dom';
import logo from '@/assets/logo-ai-chef-pro.svg';

/**
 * AI Chef Pro logo in a white rounded card with a back-nav pill above it.
 * The pill is hidden on the products hub (you are already there); on every
 * other dark-bg page (landings, access gates, dashboards) it gives an
 * explicit way back to /productos-digitales and /.
 */
export default function LogoBadge() {
  const { pathname } = useLocation();
  const isHub = pathname === '/productos-digitales';

  return (
    <div>
      {!isHub && (
        <nav className="flex justify-center pt-1 mb-2 md:mb-3">
          <div className="inline-flex items-center gap-2 md:gap-3 px-3 md:px-4 py-1.5 rounded-full bg-white/[0.04] border border-white/10 backdrop-blur-sm text-xs text-gray-400">
            <a
              href="/productos-digitales"
              className="hover:text-[#FFD700] transition-colors whitespace-nowrap"
            >
              ← Productos Digitales
            </a>
            <span className="text-white/20" aria-hidden="true">·</span>
            <a
              href="/"
              className="hover:text-[#FFD700] transition-colors"
            >
              Inicio
            </a>
          </div>
        </nav>
      )}
      <div className="flex justify-center py-6 md:py-8">
        <a
          href="/"
          className="inline-flex items-center px-6 py-3 bg-white rounded-2xl shadow-lg shadow-white/5 hover:shadow-white/10 transition-shadow"
        >
          <img
            src={logo}
            alt="AI Chef Pro"
            className="h-8 md:h-9 w-auto"
          />
        </a>
      </div>
    </div>
  );
}
