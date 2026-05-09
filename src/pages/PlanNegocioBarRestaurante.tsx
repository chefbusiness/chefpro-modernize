import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-bar-restaurante/HeroSection';
import ContentGrid from '@/components/plan-negocio-bar-restaurante/ContentGrid';
import WhySection from '@/components/plan-negocio-bar-restaurante/WhySection';
import AuthorSection from '@/components/plan-negocio-bar-restaurante/AuthorSection';
import BonusSection from '@/components/plan-negocio-bar-restaurante/BonusSection';
import BuyBox from '@/components/plan-negocio-bar-restaurante/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-bar-restaurante/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-bar-restaurante/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-bar-restaurante/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planBarRestauranteTestimonials } from '@/data/testimonials-plan-bar-restaurante';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-bar-restaurante/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioBarRestaurante() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio: Bar-Restaurante — Plan Financiero Excel, Inversión Inicial y Checklist Apertura | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio completo para abrir un bar-restaurante en España 2026. Plan financiero Excel con P&L 3 años, punto de equilibrio, escenarios. Checklist apertura con 50+ trámites. Datos reales mercado español. €35." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio bar-restaurante, plan financiero restaurante España, abrir restaurante, checklist apertura restaurante, inversión inicial restaurante, punto de equilibrio hostelería, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-bar-restaurante" />
        <meta property="og:title" content="Plan de Negocio: Bar-Restaurante — Plan Financiero Excel + Checklist Apertura" />
        <meta property="og:description" content="Plan financiero Excel con P&L 3 años, inversión inicial, punto de equilibrio, escenarios y checklist apertura con 50+ trámites para abrir un bar-restaurante en España. €35." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-bar-restaurante" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-bar-restaurante.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio: Bar-Restaurante — Plan Financiero + Checklist Apertura" />
        <meta name="twitter:description" content="Plan financiero Excel con P&L 3 años + checklist apertura con 50+ trámites. €35." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-bar-restaurante.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio: Bar-Restaurante — Plan Financiero Excel, Inversión Inicial y Checklist Apertura",
          "description": "Plan de negocio completo para abrir un bar-restaurante en España. Incluye plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada, punto de equilibrio, 3 escenarios financieros, cuadro de personal con Seg. Social, checklist de apertura con 50+ trámites y análisis de mercado España 2026.",
          "image": "https://aichef.pro/og-plan-negocio-bar-restaurante.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-bar-restaurante",
            "priceCurrency": "EUR",
            "price": "35.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Presenté el plan financiero al banco y me aprobaron la financiación en 10 días. Las proyecciones a 3 años con escenarios les dieron mucha confianza." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de apertura me salvó meses de trabajo. 50+ trámites organizados por fases, desde constituir la SL hasta la licencia de actividad." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Uso este plan como base para evaluar proyectos de restauración. El punto de equilibrio y los escenarios financieros son exactamente lo que necesito." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Es un plan genérico o específico para bar-restaurante?", "acceptedAnswer": { "@type": "Answer", "text": "Es 100% específico para bar-restaurante en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de bar-restaurante con barra y sala, incluyendo licencias de hostelería españolas actualizadas a 2026." }},
            { "@type": "Question", "name": "¿Puedo presentar este plan al banco o a inversores?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. El plan financiero Excel incluye cuenta de resultados (P&L) previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos e inversores." }},
            { "@type": "Question", "name": "¿Puedo modificar las cifras del Excel?", "acceptedAnswer": { "@type": "Answer", "text": "Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, el número de cubiertos, el ticket medio, los salarios y cualquier partida de inversión." }},
            { "@type": "Question", "name": "¿Qué trámites legales incluye el checklist de apertura?", "acceptedAnswer": { "@type": "Answer", "text": "Más de 50 trámites en 6 fases: constitución de la SL, licencias municipales, obra y acondicionamiento, RRHH, marketing pre-apertura y primeros 90 días de operación." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio: Bar-Restaurante", "item": "https://aichef.pro/plan-negocio-bar-restaurante" }
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
          subtitle="Emprendedores e inversores que usaron el plan de negocio para abrir su restaurante en España"
          testimonials={planBarRestauranteTestimonials}
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
              <a href="/kit-plan-financiero" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Plan Financiero</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/guia-restaurante-casual" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Casual</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-bar-restaurante" label="¿Ya compraste el Plan de Negocio Bar-Restaurante? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
