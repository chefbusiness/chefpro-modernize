import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-pasteleria/HeroSection';
import ContentGrid from '@/components/kit-tareas-pasteleria/ContentGrid';
import WhySection from '@/components/kit-tareas-pasteleria/WhySection';
import AuthorSection from '@/components/kit-tareas-pasteleria/AuthorSection';
import BonusSection from '@/components/kit-tareas-pasteleria/BonusSection';
import BuyBox from '@/components/kit-tareas-pasteleria/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-pasteleria/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-pasteleria/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-pasteleria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { pasteleriaTestimonials } from '@/data/testimonials-pasteleria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-pasteleria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasPasteleria() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Pastelería / Obrador | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para pastelería y obrador: producción de masas, fermentación, cremas, decoración, vitrina, perfiles y eventos. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist pastelería, tareas obrador, checklist apertura pastelería, tareas pastelero, control producción pastelería, plantilla tareas obrador, checklist vitrina pastelería, fermentación croissant checklist, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-pasteleria" />

        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Pastelería / Obrador" />
        <meta property="og:description" content="9 checklists pre-rellenados: masas, fermentación, cremas, decoración, vitrina. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-pasteleria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Pastelería" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para pastelería y obrador. Imprime, delega y firma. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-image.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Pastelería / Obrador",
          "description": "9 checklists operativos pre-rellenados para pastelería y obrador: producción de masas, fermentación, cremas, decoración, vitrina, perfiles y eventos.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-pasteleria",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "8",
            "bestRating": "5",
            "worstRating": "1"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Marta Vidal" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "El checklist de fermentación y laminado nos salvó. Ahora seguimos el mismo protocolo y los croissants salen perfectos cada día."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Laura Fernández" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestionar un obrador que produce bollería, pan y pastelería era caótico. Los checklists por zona y perfil pusieron orden desde el primer día."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Raquel Sánchez" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Producción, vitrinas, limpieza, inventario... cubren el 95% de lo que necesita cualquier obrador."
            }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para pastelería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de una pastelería / obrador. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu negocio." }},
            { "@type": "Question", "name": "¿Incluye tareas de producción artesanal?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Masas de bollería, fermentación, laminado, cremas, mousses, decoración y montaje de vitrina. Todo detallado por partida de producción." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet." }},
            { "@type": "Question", "name": "¿Puedo usarlo en varias pastelerías?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Licencia personal para todos los establecimientos que gestiones." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Pastelería / Obrador", "item": "https://aichef.pro/kit-tareas-pasteleria" }
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
          subtitle="Pasteleros, encargados y dueños de obrador que ya tienen sus operaciones bajo control"
          testimonials={pasteleriaTestimonials}
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
              <a href="/kit-tareas-cafeteria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Cafetería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-tareas-pasteleria"
              label="¿Ya compraste el Kit de Tareas Pastelería? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
