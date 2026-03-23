import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-chef-privado/HeroSection';
import ContentGrid from '@/components/kit-tareas-chef-privado/ContentGrid';
import WhySection from '@/components/kit-tareas-chef-privado/WhySection';
import AuthorSection from '@/components/kit-tareas-chef-privado/AuthorSection';
import BonusSection from '@/components/kit-tareas-chef-privado/BonusSection';
import BuyBox from '@/components/kit-tareas-chef-privado/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-chef-privado/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-chef-privado/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-chef-privado/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { chefPrivadoTestimonials } from '@/data/testimonials-chef-privado';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-chef-privado/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasChefPrivado() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Chef Privado / Personal Chef | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para chef privado: ficha de cliente con alergias, equipo y transporte, APPCC móvil, servicio completo, fidelización y administración del autónomo. Solo €18." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist chef privado, tareas personal chef, chef a domicilio checklist, APPCC chef privado, gestión cliente chef, equipo chef portátil, ficha alergias chef, checklist servicio catering, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-chef-privado" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Chef Privado / Personal Chef" />
        <meta property="og:description" content="9 checklists pre-rellenados: clientes, equipo, APPCC, servicio, fidelización, administración. €18." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-chef-privado" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-chef-privado.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Chef Privado" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para chef privado. €18." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Chef Privado / Personal Chef",
          "description": "9 checklists operativos pre-rellenados para chef privado: ficha de cliente, equipo, APPCC móvil, servicio, fidelización y administración.",
          "image": "https://aichef.pro/og-kit-tareas-chef-privado.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-chef-privado",
            "priceCurrency": "EUR",
            "price": "18.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Raúl Ibáñez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La ficha de cliente me cambió la vida. Ahora tengo todo centralizado: preferencias, equipamiento de cocina, historial de menús. Cero errores en 6 meses." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carolina Valls" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de equipo y transporte es imprescindible. Ya no llego a la villa de un cliente y descubro que olvidé algo." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Martín del Río" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "En un yate no hay segunda oportunidad. El briefing pre-servicio me salvó de más de un desastre." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para chef privado?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de un chef privado profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico." }},
            { "@type": "Question", "name": "¿Sirve para diferentes tipos de chef privado?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cenas a domicilio, meal prep, eventos, yates, villas, clases de cocina y corporativo." }},
            { "@type": "Question", "name": "¿En qué se diferencia de apps de gestión?", "acceptedAnswer": { "@type": "Answer", "text": "Apps cobran €40/mes. Este kit da las mismas listas en Excel por €18, pago único." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Chef Privado / Personal Chef", "item": "https://aichef.pro/kit-tareas-chef-privado" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <CompatibleAppsMarquee variant="tareas" />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Chefs privados, personal chefs y consultores que ya tienen sus operaciones bajo control"
          testimonials={chefPrivadoTestimonials}
        />
        <WhySection />
        <AuthorSection />
        <BonusSection />
        <FreeToolsSection />
        <BuyBox />
        <GuaranteeSection />
        <FaqAccordion />
        <CtaFinal />
        <WorldwideBanner />
        <TryPlatformBanner />

        <footer className="py-8 pb-24 md:pb-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Todos los derechos reservados</p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Restaurante</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas-chocolateria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Chocolatería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-chef-privado" label="¿Ya compraste el Kit de Tareas Chef Privado? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
