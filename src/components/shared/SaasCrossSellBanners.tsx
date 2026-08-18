import { ExternalLink } from 'lucide-react';

// Tarjetas de cross-sell a los SaaS hermanos del grupo ChefBusiness, para los dashboards
// post-pago de los productos digitales. Regla (John, 2026-07-21): en aichef.pro SOLO
// Miselup + Timlup — NUNCA autorreferenciar AI Chef Pro aquí (el upsell propio ya lo hace
// SaasDiscoveryBanner en la cabecera). Sin emojis. Portado de chefbusiness-astro
// (src/components/productos-digitales/SaasCrossSellBanners.tsx) el 2026-08-18.

const SAAS = [
  {
    name: 'Miselup',
    url: 'https://miselup.pro',
    domain: 'miselup.pro',
    tagline: 'Recetario digital con escandallos 100 % dinámicos',
    desc: 'Calcula el coste real y el margen de cada elaboración. Cambia el precio de un ingrediente y se recalculan al instante todos tus escandallos y cartas. Food cost y márgenes siempre bajo control.',
    free: 'Plan gratis sin tarjeta',
  },
  {
    name: 'Timlup',
    url: 'https://timlup.pro',
    domain: 'timlup.pro',
    tagline: 'Checklists digitales para las tareas que se repiten',
    desc: 'Apertura, cierre, limpieza y registros APPCC en su franja horaria. Tu equipo las completa y firma desde el móvil con un PIN, y tú lo ves en tiempo real con un semáforo de cumplimiento.',
    free: 'Plan gratis siempre',
  },
];

export default function SaasCrossSellBanners() {
  return (
    <section className="px-4 pb-12">
      <div className="max-w-5xl mx-auto">
        <p className="text-[#FFD700] text-xs font-bold uppercase tracking-wider text-center mb-5">
          Software del grupo ChefBusiness para llevar esto al día a día
        </p>
        <div className="grid sm:grid-cols-2 gap-4">
          {SAAS.map((s) => (
            <div
              key={s.name}
              className="bg-white/5 border border-white/10 rounded-xl p-6 flex flex-col gap-2.5 hover:border-[#FFD700]/30 transition-all"
            >
              <div className="flex items-baseline gap-2 flex-wrap">
                <h3 className="text-white font-bold text-lg">{s.name}</h3>
                <span className="text-gray-500 text-xs">{s.domain}</span>
              </div>
              <p className="text-[#FFD700] text-sm font-semibold">{s.tagline}</p>
              <p className="text-gray-400 text-sm leading-relaxed">{s.desc}</p>
              <div className="flex items-center gap-3 flex-wrap mt-auto pt-2">
                <a
                  href={s.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-[#FFD700] text-black text-sm font-bold hover:bg-[#FFD700]/90 transition-all"
                >
                  Probar gratis
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
                <span className="text-gray-500 text-xs">{s.free}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
