import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-chocolateria/HeroSection';
import ContentGrid from '@/components/kit-tareas-chocolateria/ContentGrid';
import WhySection from '@/components/kit-tareas-chocolateria/WhySection';
import AuthorSection from '@/components/kit-tareas-chocolateria/AuthorSection';
import BonusSection from '@/components/kit-tareas-chocolateria/BonusSection';
import BuyBox from '@/components/kit-tareas-chocolateria/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-chocolateria/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-chocolateria/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-chocolateria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { chocolateriaTestimonials } from '@/data/testimonials-chocolateria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-chocolateria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasChocolateria() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Chocolatería / Obrador de Chocolate | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para chocolatería artesanal: producción (templado, moldeado, bombones), vitrina, servicio, gestión y temporada. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist chocolatería, tareas chocolatero, checklist apertura chocolatería, tareas producción chocolate, control stock chocolatería, plantilla tareas obrador chocolate, checklist cierre chocolatería, inventario chocolatería, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-chocolateria" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Chocolatería / Obrador de Chocolate" />
        <meta property="og:description" content="9 checklists pre-rellenados: producción, vitrina, servicio, gestión, temporada. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-chocolateria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Chocolatería Artesanal" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para chocolatería artesanal. €12." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Chocolatería / Obrador de Chocolate",
          "description": "9 checklists operativos pre-rellenados para chocolatería artesanal: producción, vitrina, servicio, gestión y temporada.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-chocolateria",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Miguel Ángel Roca" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de producción me salvó. Ahora el templado, moldeado y envasado quedan documentados y el control de calidad es impecable." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Elena Montero" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Tenemos 4 tiendas y ahora con los checklists estandarizados la experiencia es la misma en todas." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Patricia Vega" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Lo primero que hago con cada cliente de chocolatería es entregarle estos checklists. Cubren el 95% de lo que necesita." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para chocolatería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de una chocolatería artesanal. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico." }},
            { "@type": "Question", "name": "¿Cubre producción artesanal y tienda?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Templado, moldeado, bombones, tabletas, envasado, vitrina, mostrador y gestión." }},
            { "@type": "Question", "name": "¿En qué se diferencia de apps de gestión?", "acceptedAnswer": { "@type": "Answer", "text": "Apps cobran €40/mes por local. Este kit da las mismas listas en Excel por €12, pago único." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Chocolatería / Obrador de Chocolate", "item": "https://aichef.pro/kit-tareas-chocolateria" }
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
          subtitle="Chocolateros, encargados y dueños de chocolatería que ya tienen sus operaciones bajo control"
          testimonials={chocolateriaTestimonials}
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
              <a href="/kit-tareas-heladeria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Heladería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-chocolateria" label="¿Ya compraste el Kit de Tareas Chocolatería? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
