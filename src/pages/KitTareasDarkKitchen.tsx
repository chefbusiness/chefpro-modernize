import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-dark-kitchen/HeroSection';
import ContentGrid from '@/components/kit-tareas-dark-kitchen/ContentGrid';
import WhySection from '@/components/kit-tareas-dark-kitchen/WhySection';
import AuthorSection from '@/components/kit-tareas-dark-kitchen/AuthorSection';
import BonusSection from '@/components/kit-tareas-dark-kitchen/BonusSection';
import BuyBox from '@/components/kit-tareas-dark-kitchen/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-dark-kitchen/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-dark-kitchen/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-dark-kitchen/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { darkKitchenTestimonials } from '@/data/testimonials-dark-kitchen';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-dark-kitchen/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasDarkKitchen() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para dark kitchen multi-marca: estaciones de produccion, empaquetado, plataformas (Glovo, Uber Eats, Just Eat), riders, perfiles y eventos. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist dark kitchen, tareas dark kitchen, checklist ghost kitchen, checklist cocina fantasma, tareas cocina virtual, dark kitchen multi-marca, gestion plataformas delivery, empaquetado dark kitchen, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-dark-kitchen" />

        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen" />
        <meta property="og:description" content="9 checklists pre-rellenados: estaciones produccion, empaquetado multi-marca, plataformas delivery, riders. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-dark-kitchen" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-dark-kitchen.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Dark Kitchen" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para dark kitchen multi-marca. Imprime, delega y firma. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-dark-kitchen.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen",
          "description": "9 checklists operativos pre-rellenados para dark kitchen multi-marca: estaciones de produccion, empaquetado, plataformas delivery, riders, perfiles y eventos.",
          "image": "https://aichef.pro/og-kit-tareas-dark-kitchen.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-dark-kitchen",
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
              "author": { "@type": "Person", "name": "Roberto Navarro" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestionar 4 marcas en la misma cocina era un caos. Desde que imprimimos los checklists, los errores de empaquetado bajaron un 85%."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Elena Morales" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Abri mi dark kitchen hace 6 meses y me perdia con las tablets y el packaging. Estas checklists me organizaron desde el dia uno."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Daniel Ortiz" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "El checklist de gestion de plataformas es oro puro. Activar marcas, pausar en horas pico, revisar valoraciones. Cero incidencias."
            }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para dark kitchen multi-marca?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Cada checklist viene pre-rellenado con las tareas reales de una dark kitchen multi-marca. Solo personaliza: ajustar, borrar lo que no aplique y anadir lo especifico de tus marcas." }},
            { "@type": "Question", "name": "¿Incluye gestion de plataformas como Glovo, Uber Eats y Just Eat?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Activacion/pausa de marcas, control de tiempos <12 min, gestion de incidencias, revision de valoraciones y facturacion por marca/plataforma." }},
            { "@type": "Question", "name": "¿En que se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago unico. Sin suscripcion, sin internet." }},
            { "@type": "Question", "name": "¿Puedo usarlo en varias dark kitchens?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Licencia personal para todos los establecimientos y marcas que gestiones." }},
            { "@type": "Question", "name": "¿Incluye tareas de empaquetado y packaging por marca?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Packaging diferenciado por marca virtual, precintos de seguridad, etiquetado correcto y verificacion de pedido completo." }},
            { "@type": "Question", "name": "¿Hay garantia de devolucion?", "acceptedAnswer": { "@type": "Answer", "text": "30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Dark Kitchen", "item": "https://aichef.pro/kit-tareas-dark-kitchen" }
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
          subtitle="Operadores de dark kitchen, gestores de plataformas y empaquetadores que ya tienen sus operaciones bajo control"
          testimonials={darkKitchenTestimonials}
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
              <a href="/kit-tareas-hamburgueseria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Hamburgueseria</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-tareas-dark-kitchen"
              label="¿Ya compraste el Kit de Tareas Dark Kitchen? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
