import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-hotel/HeroSection';
import ContentGrid from '@/components/kit-tareas-hotel/ContentGrid';
import WhySection from '@/components/kit-tareas-hotel/WhySection';
import AuthorSection from '@/components/kit-tareas-hotel/AuthorSection';
import BonusSection from '@/components/kit-tareas-hotel/BonusSection';
import BuyBox from '@/components/kit-tareas-hotel/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-hotel/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-hotel/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-hotel/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { hotelTestimonials } from '@/data/testimonials-hotel';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-hotel/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasHotel() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — 46 Checklists Operativos para Hotel Completo | AI Chef Pro</title>
        <meta name="description" content="46 checklists operativos en 15 plantillas Excel para 11 departamentos de hotel: F&B, recepción, housekeeping, piscina, mantenimiento, spa y más. Solo €18,50." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist hotel, tareas hotel, checklist housekeeping, checklist recepción hotel, checklist mantenimiento hotel, tareas buffet hotel, checklist room service, plantilla tareas hotel, checklist piscina, spa hotel, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-hotel" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — 46 Checklists para Hotel Completo" />
        <meta property="og:description" content="46 checklists en 15 plantillas para 11 departamentos de hotel. €18,50." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-hotel" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-hotel.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — 46 Checklists para Hotel Completo" />
        <meta name="twitter:description" content="46 checklists para 11 departamentos de hotel. €18,50." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — 46 Checklists Operativos para Hotel Completo",
          "description": "46 checklists operativos en 15 plantillas Excel para 11 departamentos de hotel: F&B (6 outlets), recepción, housekeeping, piscina, terraza, mantenimiento, administración y spa.",
          "image": "https://aichef.pro/og-kit-tareas-hotel.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-hotel",
            "priceCurrency": "EUR",
            "price": "18.50",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Patricia Moreno" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de desayuno buffet eliminó los olvidos en el montaje. Ahora el estándar es el mismo en cada turno." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Elena Vargas" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de banquetes cubren bodas, convenciones y cenas de gala con el nivel de detalle que necesitamos." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Isabel Fernández" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Recomiendo este kit a todos mis clientes hoteleros. Cubren el 95% de la operativa F&B." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para hotel?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de un departamento F&B de hotel profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico." }},
            { "@type": "Question", "name": "¿Cubre todos los departamentos del hotel?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Incluye 11 departamentos: F&B (6 outlets), recepción, housekeeping, áreas públicas, piscina, terraza, mantenimiento, administración, guest services y spa." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da 46 checklists para todo el hotel en Excel por €18,50, pago único." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Hotel F&B / Buffet", "item": "https://aichef.pro/kit-tareas-hotel" }
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
          subtitle="F&B managers, chefs ejecutivos y directores de hotel que ya tienen sus operaciones bajo control"
          testimonials={hotelTestimonials}
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
              <a href="/kit-tareas-catering" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Catering</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-hotel" label="¿Ya compraste el Kit de Tareas Hotel? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
