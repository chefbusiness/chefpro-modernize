import { Helmet } from 'react-helmet-async';
import { Check, Star, Package, ArrowRight } from 'lucide-react';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import PaymentBadges from '@/components/ebook/PaymentBadges';
import LogoBadge from '@/components/shared/LogoBadge';
import FadeIn from '@/components/ebook/FadeIn';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

import avatar1 from '@/assets/avatars/avatar-1.jpg';
import avatar2 from '@/assets/avatars/avatar-2.jpg';
import avatar3 from '@/assets/avatars/avatar-3.jpg';
import avatar4 from '@/assets/avatars/avatar-4.jpg';
import avatar5 from '@/assets/avatars/avatar-5.jpg';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_MEGA_PACK_TAREAS || '#comprar';

const kits = [
  { name: 'Restaurante Casual', templates: 11, slug: '/kit-tareas' },
  { name: 'Cafetería / Brunch', templates: 11, slug: '/kit-tareas-cafeteria' },
  { name: 'Pizzería', templates: 11, slug: '/kit-tareas-pizzeria' },
  { name: 'Hamburguesería', templates: 11, slug: '/kit-tareas-hamburgueseria' },
  { name: 'Dark Kitchen', templates: 11, slug: '/kit-tareas-dark-kitchen' },
  { name: 'Pastelería / Obrador', templates: 11, slug: '/kit-tareas-pasteleria' },
  { name: 'Bar / Cocktails', templates: 11, slug: '/kit-tareas-bar' },
  { name: 'Catering / Eventos', templates: 11, slug: '/kit-tareas-catering' },
  { name: 'Hotel Completo', templates: 19, slug: '/kit-tareas-hotel' },
  { name: 'Heladería Artesanal', templates: 11, slug: '/kit-tareas-heladeria' },
  { name: 'Chocolatería / Bombonería', templates: 11, slug: '/kit-tareas-chocolateria' },
  { name: 'Restaurante Creativo / De Autor', templates: 13, slug: '/kit-tareas-restaurante-creativo' },
  { name: 'Chef Privado / Personal Chef', templates: 9, slug: '/kit-tareas-chef-privado' },
];

const totalTemplates = kits.reduce((sum, k) => sum + k.templates, 0);
const totalIndividual = 12 * 12 + 18.5 + 18; // 12 kits at €12 + hotel €18.50 + chef privado €18

export default function MegaPackTareas() {
  return (
    <>
      <Helmet>
        <title>Mega Pack Tareas Recurrentes — 13 Kits Hostelería | AI Chef Pro</title>
        <meta name="description" content={`${totalTemplates} plantillas Excel en 13 kits de tareas recurrentes para hostelería. Restaurante, cafetería, pizzería, bar, hotel, catering y más. Ahorra más del 45%. Solo 89 EUR.`} />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href="https://aichef.pro/mega-pack-tareas" />
        <meta property="og:title" content="Mega Pack Tareas Recurrentes — 13 Kits Hostelería" />
        <meta property="og:description" content={`${totalTemplates} plantillas Excel: todos los kits de tareas recurrentes en un solo pack. 89 EUR.`} />
        <meta property="og:url" content="https://aichef.pro/mega-pack-tareas" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-hotel.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": `Mega Pack Tareas Recurrentes — ${totalTemplates} Plantillas en 13 Kits`,
          "description": `Pack completo con los 13 kits de tareas recurrentes para hostelería. ${totalTemplates} plantillas Excel editables.`,
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/mega-pack-tareas",
            "priceCurrency": "EUR",
            "price": "89.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
          },
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />

        {/* Hero */}
        <section className="relative px-4 pt-8 pb-16 md:pt-12 md:pb-24 overflow-hidden">
          <div className="absolute inset-0" style={{
            background: 'radial-gradient(ellipse 80% 60% at 50% -10%, rgba(34,197,94,0.12) 0%, transparent 70%)',
          }} />
          <div className="relative max-w-4xl mx-auto text-center z-10">
            <LogoBadge />
            <div className="flex flex-col items-center gap-2 mb-6">
              <div className="flex -space-x-3 justify-center">
                {[avatar1, avatar2, avatar3, avatar4, avatar5].map((av, i) => (
                  <Avatar key={i} className="border-2 border-[#0a0a0a] w-9 h-9 sm:w-10 sm:h-10 ring-2 ring-[#0a0a0a]">
                    <AvatarImage src={av} /><AvatarFallback className="bg-gray-800 text-xs text-gray-400">P</AvatarFallback>
                  </Avatar>
                ))}
              </div>
              <div className="flex items-center gap-0.5">
                {Array.from({ length: 5 }).map((_, i) => <Star key={i} className="h-4 w-4 fill-[#FFD700] text-[#FFD700]" />)}
              </div>
            </div>

            <span className="inline-block mb-6 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-sm font-bold animate-fade-in">
              🎁 MEGA PACK — 13 Kits · {totalTemplates} Plantillas · Ahorra más del 45%
            </span>

            <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
              Mega Pack <span className="text-emerald-400">Tareas Recurrentes</span>
              <span className="block text-2xl md:text-4xl lg:text-5xl mt-2 text-gray-200">
                Los 13 Kits en Un Solo Pack
              </span>
            </h1>

            <p className="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto mb-10 leading-relaxed">
              {totalTemplates} plantillas Excel editables para 13 conceptos de hostelería. Desde restaurante casual hasta hotel completo. Apertura, cierre, tareas por perfil, gestión de negocio, caja y más.
            </p>

            <div className="inline-block bg-white/5 border-2 border-emerald-500/30 rounded-2xl p-6 md:p-8 backdrop-blur-sm">
              <div className="flex items-center justify-center gap-2 mb-2">
                <span className="text-sm text-gray-400">Si compras los 13 por separado:</span>
                <span className="text-lg text-gray-500 line-through">{Math.round(totalIndividual)} EUR</span>
              </div>
              <div className="flex items-center justify-center gap-4 mb-3">
                <span className="text-5xl md:text-6xl font-extrabold text-emerald-400">89 EUR</span>
                <span className="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-sm font-bold">-{Math.round((1 - 89/totalIndividual) * 100)}%</span>
              </div>
              <p className="text-sm text-gray-400 mb-5">Pago único · Sin suscripción · Acceso inmediato a los 13 kits</p>
              <a href={stripeLink} className="inline-block w-full md:w-auto px-10 py-4 bg-emerald-500 text-white font-bold text-lg rounded-xl hover:bg-emerald-600 transition-all hover:scale-[1.02] active:scale-[0.98]">
                COMPRAR MEGA PACK — 89 EUR
              </a>
              <PaymentBadges className="mt-4" />
            </div>
          </div>
        </section>

        {/* 13 Kits Grid */}
        <section className="py-16 md:py-24 px-4">
          <div className="max-w-6xl mx-auto">
            <FadeIn>
              <div className="text-center mb-12">
                <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
                  <span className="text-emerald-400">13</span> Kits Incluidos
                </h2>
                <p className="text-gray-400 text-lg">{totalTemplates} plantillas Excel editables · Cada kit personalizado para su concepto de negocio</p>
              </div>
            </FadeIn>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {kits.map((kit, i) => (
                <FadeIn key={kit.slug} delay={i * 30}>
                  <div className="bg-white/5 border border-white/10 rounded-xl p-5 hover:border-emerald-500/40 transition-all h-full group">
                    <Package className="w-7 h-7 text-emerald-400 mb-3" />
                    <h3 className="text-white font-semibold text-sm mb-1">{kit.name}</h3>
                    <p className="text-gray-500 text-xs">{kit.templates} plantillas</p>
                    <a href={kit.slug} className="inline-flex items-center gap-1 text-emerald-400 text-xs mt-3 opacity-0 group-hover:opacity-100 transition-opacity">
                      Ver detalle <ArrowRight className="w-3 h-3" />
                    </a>
                  </div>
                </FadeIn>
              ))}
            </div>
          </div>
        </section>

        {/* What's in each kit */}
        <section className="py-16 md:py-24 px-4 bg-white/[0.02]">
          <div className="max-w-4xl mx-auto">
            <FadeIn>
              <div className="text-center mb-12">
                <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">¿Qué Incluye <span className="text-emerald-400">Cada Kit</span>?</h2>
              </div>
            </FadeIn>
            <div className="grid md:grid-cols-2 gap-4">
              {[
                'Apertura y cierre operativo (cocina, sala, barra)',
                'Apertura y cierre del negocio/local',
                'Apertura y cierre de caja (arqueo, cuadre)',
                'Tareas por perfil profesional',
                'Tareas del manager (diario, semanal, mensual)',
                'Tareas semanales y mensuales',
                'Eventos y festivos del concepto',
                'Plantilla personalizable en blanco',
                'BONUS: Briefing de servicio',
                'BONUS: Calendario anual de fechas clave',
              ].map((item) => (
                <FadeIn key={item}>
                  <div className="flex items-center gap-3 p-3">
                    <Check className="w-5 h-5 text-emerald-400 flex-shrink-0" />
                    <span className="text-gray-200">{item}</span>
                  </div>
                </FadeIn>
              ))}
            </div>
          </div>
        </section>

        {/* Guarantee */}
        <section className="py-16 md:py-24 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <FadeIn>
              <img src="/money-back-badge.png" alt="100% Money Back" className="w-28 h-28 mx-auto mb-6 object-contain" />
              <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">Garantía de Satisfacción <span className="text-emerald-400">100%</span></h2>
              <p className="text-gray-400 text-lg leading-relaxed mb-8 max-w-2xl mx-auto">
                Si el Mega Pack no te ayuda a organizar tu negocio, te devolvemos el 100% de tu dinero. 30 días, sin preguntas.
              </p>
            </FadeIn>
          </div>
        </section>

        {/* Final CTA */}
        <section className="py-16 md:py-24 px-4">
          <div className="max-w-lg mx-auto">
            <div className="bg-white/5 border-2 border-emerald-500/50 rounded-2xl p-8 md:p-10 text-center">
              <p className="text-gray-400 mb-2">Los 13 kits por separado: <span className="line-through">{Math.round(totalIndividual)} EUR</span></p>
              <p className="text-5xl md:text-6xl font-extrabold text-emerald-400 mb-2">89 EUR</p>
              <p className="text-emerald-400 font-bold text-lg mb-6">Ahorra {Math.round(totalIndividual - 89)} EUR</p>
              <a href={stripeLink} className="inline-block w-full px-8 py-4 bg-emerald-500 text-white font-bold text-lg rounded-xl hover:bg-emerald-600 transition-all hover:scale-[1.02] active:scale-[0.98]">
                SÍ, QUIERO EL MEGA PACK — 89 EUR
              </a>
              <PaymentBadges className="mt-5" />
            </div>
          </div>
        </section>

        <WorldwideBanner />

        <footer className="py-8 pb-24 md:pb-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Todos los derechos reservados</p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-emerald-400 transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-emerald-400 transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-emerald-400 transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="mega-pack-tareas" label="¿Ya compraste el Mega Pack? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />

        {/* Sticky Bar */}
        <div className="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-gray-900/95 backdrop-blur-md border-t border-emerald-500/30 px-3 py-3">
          <div className="flex items-center justify-between gap-2 max-w-screen-sm mx-auto">
            <p className="text-white text-xs font-bold truncate">MEGA PACK 13 KITS — 89 EUR</p>
            <a href={stripeLink} className="flex-shrink-0 px-5 py-2.5 bg-emerald-500 text-white font-bold text-sm rounded-lg hover:bg-emerald-600 transition-all">
              COMPRAR
            </a>
          </div>
        </div>
      </div>
    </>
  );
}
