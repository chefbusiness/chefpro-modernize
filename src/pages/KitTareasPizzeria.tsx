import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-pizzeria/HeroSection';
import ContentGrid from '@/components/kit-tareas-pizzeria/ContentGrid';
import WhySection from '@/components/kit-tareas-pizzeria/WhySection';
import AuthorSection from '@/components/kit-tareas-pizzeria/AuthorSection';
import BonusSection from '@/components/kit-tareas-pizzeria/BonusSection';
import BuyBox from '@/components/kit-tareas-pizzeria/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-pizzeria/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-pizzeria/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-pizzeria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { pizzeriaTestimonials } from '@/data/testimonials-pizzeria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-pizzeria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';

export default function KitTareasPizzeria() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Pizzería | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para pizzería: horno de leña/piedra, masa napolitana, línea de montaje, delivery, perfiles y eventos. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist pizzería, tareas apertura pizzería, checklist horno pizza, tareas pizzero, checklist delivery pizzería, lista tareas pizzería, plantilla tareas pizzería, control horno pizza, masa napolitana checklist, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-pizzeria" />

        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Pizzería" />
        <meta property="og:description" content="9 checklists pre-rellenados: horno, masa, línea de montaje, delivery. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-pizzeria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Pizzería" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para pizzería. Imprime, delega y firma. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-image.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Pizzería",
          "description": "9 checklists operativos pre-rellenados para pizzería: horno de leña/piedra, masa napolitana, línea de montaje, delivery, perfiles y eventos.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-pizzeria",
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
              "author": { "@type": "Person", "name": "Marco Ferrara" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "El checklist de horno de leña me ha salvado. Ahora seguimos el mismo protocolo y el leopardo sale perfecto en cada pizza."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Elena Campos" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestionar la apertura de una pizzería con delivery y sala era un caos. Los checklists por zona nos organizaron desde el día uno."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Daniel Ortiz" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Las tareas de fermentación, estirado a mano y control de cocción están perfectamente estructuradas. Es lo que debería tener toda pizzería."
            }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para pizzería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de una pizzería. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local." }},
            { "@type": "Question", "name": "¿Sirve para horno de leña y horno eléctrico?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Las tareas cubren horno de leña (encendido, gestión de leña, limpieza ceniza) y horno eléctrico/piedra (precalentamiento, limpieza solera, control resistencias)." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet." }},
            { "@type": "Question", "name": "¿Puedo usarlo en varias pizzerías?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Licencia personal para todos los establecimientos que gestiones." }},
            { "@type": "Question", "name": "¿Incluye tareas de delivery y take-away?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Gestión de riders, control de tiempos, packaging, etiquetado y cierre de plataformas de delivery." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Pizzería", "item": "https://aichef.pro/kit-tareas-pizzeria" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <LogoBadge />
        <HeroSection />
        <CompatibleAppsMarquee variant="tareas" />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Pizzeros, encargados y dueños de pizzería que ya tienen sus operaciones bajo control"
          testimonials={pizzeriaTestimonials}
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
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700">·</span>
              <a href="/kit-tareas" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Restaurante</a>
              <span className="text-gray-700">·</span>
              <a href="/kit-tareas-cafeteria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Cafetería</a>
              <span className="text-gray-700">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-tareas-pizzeria"
              label="¿Ya compraste el Kit de Tareas Pizzería? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <StickyBar />
      </div>
    </>
  );
}
