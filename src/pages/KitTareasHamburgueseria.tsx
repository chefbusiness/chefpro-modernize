import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-hamburgueseria/HeroSection';
import ContentGrid from '@/components/kit-tareas-hamburgueseria/ContentGrid';
import WhySection from '@/components/kit-tareas-hamburgueseria/WhySection';
import AuthorSection from '@/components/kit-tareas-hamburgueseria/AuthorSection';
import BonusSection from '@/components/kit-tareas-hamburgueseria/BonusSection';
import BuyBox from '@/components/kit-tareas-hamburgueseria/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-hamburgueseria/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-hamburgueseria/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-hamburgueseria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { hamburguseriaTestimonials } from '@/data/testimonials-hamburgueseria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-hamburgueseria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasHamburgueseria() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Hamburguesería | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para hamburguesería: plancha/grill, smash burgers, freidora, línea de montaje, delivery, perfiles y eventos. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist hamburguesería, tareas apertura hamburguesería, checklist smash burger, tareas parrillero, checklist delivery hamburguesería, lista tareas hamburguesería, plantilla tareas hamburguesería, control plancha grill, freidora checklist, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-hamburgueseria" />

        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Hamburguesería" />
        <meta property="og:description" content="9 checklists pre-rellenados: plancha/grill, smash burger, freidora, línea de montaje, delivery. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-hamburgueseria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-hamburgueseria.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Hamburguesería" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para hamburguesería. Imprime, delega y firma. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-hamburgueseria.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Hamburguesería",
          "description": "9 checklists operativos pre-rellenados para hamburguesería: plancha/grill, smash burgers, freidora, línea de montaje, delivery, perfiles y eventos.",
          "image": "https://aichef.pro/og-kit-tareas-hamburgueseria.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-hamburgueseria",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "10",
            "bestRating": "5",
            "worstRating": "1"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Carlos Méndez" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "El checklist de plancha y grill me ha cambiado el turno. Ahora seguimos el mismo protocolo y el smash sale perfecto cada vez."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Marta Iglesias" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestionar la apertura de una hamburguesería con delivery y sala era un caos. Los checklists por zona nos organizaron desde el día uno."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Alejandro Fuentes" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "La línea de montaje de burger es donde más nos ayudó. Cada ingrediente en su sitio, salsas repuestas, pan tostado a tiempo."
            }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para hamburguesería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de una hamburguesería. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local." }},
            { "@type": "Question", "name": "¿Incluye tareas de plancha, grill y smash burger?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Encendido, limpieza, temperatura, técnica smash burger, punto de carne (rare a well done) y limpieza entre turnos." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet." }},
            { "@type": "Question", "name": "¿Puedo usarlo en varias hamburgueserías?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Licencia personal para todos los establecimientos que gestiones." }},
            { "@type": "Question", "name": "¿Incluye tareas de delivery y packaging?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Packaging correcto de burger, control de tiempos, gestión de riders, etiquetado y cierre de plataformas de delivery." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Hamburguesería", "item": "https://aichef.pro/kit-tareas-hamburgueseria" }
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
          subtitle="Parrilleros, encargados y dueños de hamburguesería que ya tienen sus operaciones bajo control"
          testimonials={hamburguseriaTestimonials}
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
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Restaurante</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas-pizzeria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Pizzería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-tareas-hamburgueseria"
              label="¿Ya compraste el Kit de Tareas Hamburguesería? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
