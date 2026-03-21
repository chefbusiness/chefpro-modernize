import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-catering/HeroSection';
import ContentGrid from '@/components/kit-tareas-catering/ContentGrid';
import WhySection from '@/components/kit-tareas-catering/WhySection';
import AuthorSection from '@/components/kit-tareas-catering/AuthorSection';
import BonusSection from '@/components/kit-tareas-catering/BonusSection';
import BuyBox from '@/components/kit-tareas-catering/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-catering/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-catering/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-catering/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { cateringTestimonials } from '@/data/testimonials-catering';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-catering/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasCatering() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Catering / Eventos | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para empresas de catering y eventos: producción off-site, transporte, montaje, servicio, desmontaje. Bodas, corporativos, cocktails. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist catering, tareas evento, checklist montaje evento, tareas catering bodas, control logística catering, plantilla tareas evento, checklist desmontaje, inventario catering, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-catering" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Catering / Eventos" />
        <meta property="og:description" content="9 checklists pre-rellenados: producción, transporte, montaje, servicio. Bodas, corporativos, cocktails. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-catering" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Catering / Eventos" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para empresas de catering y eventos. €12." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Catering / Eventos",
          "description": "9 checklists operativos pre-rellenados para empresas de catering y eventos: producción off-site, transporte, montaje, servicio, desmontaje y post-evento.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-catering",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Marta Domínguez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de producción y transporte eliminaron el 90% de los olvidos. El equipo eventual sabe exactamente qué hacer." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Laura Sánchez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Hago 3-4 bodas por semana en temporada alta. Los checklists por tipo de evento me ahorran horas de preparación." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Isabel García" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Recomiendo este kit a todos mis clientes de catering. Cubren el ciclo completo del evento." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para catering?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de una empresa de catering profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico." }},
            { "@type": "Question", "name": "¿Cubre todo el ciclo del evento?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Incluye producción off-site, transporte y logística, montaje del venue, servicio durante el evento, desmontaje y post-evento." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Catering / Eventos", "item": "https://aichef.pro/kit-tareas-catering" }
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
          subtitle="Event managers, chefs de catering y coordinadores que ya tienen sus operaciones bajo control"
          testimonials={cateringTestimonials}
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
              <a href="/kit-tareas-bar" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Bar</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-catering" label="¿Ya compraste el Kit de Tareas Catering? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
