import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas/HeroSection';
import ContentGrid from '@/components/kit-tareas/ContentGrid';
import WhySection from '@/components/kit-tareas/WhySection';
import AuthorSection from '@/components/kit-tareas/AuthorSection';
import BonusSection from '@/components/kit-tareas/BonusSection';
import BuyBox from '@/components/kit-tareas/BuyBox';
import GuaranteeSection from '@/components/kit-tareas/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas/FaqAccordion';
import CtaFinal from '@/components/kit-tareas/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { tareasTestimonials } from '@/data/testimonials-tareas';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';

export default function KitTareas() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Restaurante | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para restaurante casual: apertura, cierre, partidas, manager, perfiles, eventos. Imprime, delega y firma. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist restaurante, tareas apertura restaurante, checklist cierre cocina, lista tareas cocina, checklist manager restaurante, tareas recurrentes hostelería, mise en place checklist, plantilla tareas restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas" />

        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Restaurante" />
        <meta property="og:description" content="9 checklists pre-rellenados: apertura, cierre, partidas, manager, perfiles, eventos. Imprime, delega y firma. €14." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Restaurante" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados. Imprime, delega y firma. €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-image.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes Pro — Checklists Operativos para Restaurante",
          "description": "9 checklists operativos pre-rellenados para restaurante casual: apertura, cierre, partidas de cocina, manager, perfiles profesionales, eventos y festivos.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas",
            "priceCurrency": "EUR",
            "price": "14.00",
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
              "author": { "@type": "Person", "name": "Diego Martín" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Desde que imprimimos los checklists de apertura y cierre, no se olvida ni una tarea. El equipo sabe exactamente qué hacer."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Ana Belén Roca" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestiono 3 restaurantes y ahora todos siguen el mismo estándar. Las listas por perfil son geniales para el onboarding."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Javier López" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Pagábamos €60 al mes por Trail. Esto hace lo mismo en Excel por €14. No necesito más."
            }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de un restaurante casual. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local." }},
            { "@type": "Question", "name": "¿Cómo funciona el sistema de firma?", "acceptedAnswer": { "@type": "Answer", "text": "Cada checklist tiene columnas de responsable, hora límite, completada y firma. El manager imprime, entrega al equipo, cada persona marca y firma." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €14, pago único. Sin suscripción, sin internet." }},
            { "@type": "Question", "name": "¿Puedo usarlo en varios restaurantes?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Licencia personal para todos los establecimientos que gestiones." }},
            { "@type": "Question", "name": "¿Incluye tareas para eventos?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Checklists para eventos privados, San Valentín, Navidad, apertura y cierre de terraza." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes", "item": "https://aichef.pro/kit-tareas" }
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
          subtitle="Hosteleros que ya tienen sus operaciones bajo control con los checklists"
          testimonials={tareasTestimonials}
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
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-tareas"
              label="¿Ya compraste el Kit de Tareas? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <StickyBar />
      </div>
    </>
  );
}
