import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-parrillero-asador-eventos/HeroSection';
import ContentGrid from '@/components/plan-negocio-parrillero-asador-eventos/ContentGrid';
import WhySection from '@/components/plan-negocio-parrillero-asador-eventos/WhySection';
import AuthorSection from '@/components/plan-negocio-parrillero-asador-eventos/AuthorSection';
import BonusSection from '@/components/plan-negocio-parrillero-asador-eventos/BonusSection';
import BuyBox from '@/components/plan-negocio-parrillero-asador-eventos/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-parrillero-asador-eventos/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-parrillero-asador-eventos/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-parrillero-asador-eventos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planParrilleroAsadorEventosTestimonials } from '@/data/testimonials-plan-parrillero-asador-eventos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-parrillero-asador-eventos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioParrilleroAsadorEventos() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio &amp; Kit Parrillero / Asador para Eventos — 11 Entregables | AI Chef Pro</title>
        <meta name="description" content="Plan + kit profesional completo para montar tu servicio premium itinerante de parrilla y asado para eventos en España 2026. Modelo híbrido B2C + B2B. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 96 proveedores + Catálogo equipamiento + Manual técnico + Carta 12 cortes + Modelos contrato B2C/B2B + Guía 8 sistemas + roadmap food truck. Inversión desde 3.500 EUR. €45." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio parrillero, parrilla eventos, asador a la cruz, BBQ pitmaster España, parrilla itinerante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-parrillero-asador-eventos" />
        <meta property="og:title" content="Plan de Negocio Parrillero / Asador para Eventos — 11 Entregables" />
        <meta property="og:description" content="Kit profesional para montar tu servicio premium de parrilla itinerante en España 2026. Modelo B2C+B2B. 11 entregables. Inversión desde 3.500 EUR. €45." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-parrillero-asador-eventos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-parrillero-asador-eventos.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio Parrillero / Asador para Eventos — 11 Entregables" />
        <meta name="twitter:description" content="Kit profesional para montar tu servicio premium de parrilla itinerante en España. Modelo B2C+B2B. 11 entregables. €45." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-parrillero-asador-eventos.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio & Kit de Parrillero / Asador para Eventos — 11 Entregables",
          "description": "Plan + kit profesional completo para montar un servicio premium itinerante de parrilla y asado para eventos en España 2026. Modelo híbrido B2C particular (bodas, cumpleaños, bautizos) + B2B (wedding planners, agencias, hoteles, empresas, restaurantes show cooking). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 96 proveedores reales, catálogo equipamiento + menaje, manual técnico parrillero (8 salmueras + 12 marinados + 18 cortes), carta de 12 cortes, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck y checklist de apertura con anexo CCAA fuego al aire libre.",
          "image": "https://aichef.pro/og-plan-negocio-parrillero-asador-eventos.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-parrillero-asador-eventos",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Mariano Rodríguez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Llevaba 12 años de empleado en parrilla y este plan me dio la hoja de ruta para independizarme. Las 10 experiencias y la calculadora de pricing son lo que más uso ahora." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Lucía Sanz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El manual técnico de salmueras y la tabla de cocción de 18 cortes vale el plan entero. Mis bodas mejoraron en consistencia desde la primera temporada con esta guía." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Diego López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El roadmap del food truck especializado en parrilla es brutal. Invertí 30.000 EUR siguiendo el blueprint y arranqué con eventos corporate en 6 meses." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Para quién está pensado este plan?", "acceptedAnswer": { "@type": "Answer", "text": "Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles — que quieren montar un servicio premium itinerante para eventos en España. Cubre cliente final particular (bodas íntimas, cumpleaños, bautizos) y B2B (wedding planners, agencias, hoteles, restaurantes show cooking)." }},
            { "@type": "Question", "name": "¿Qué diferencia hay con un Plan de Asador con local fijo?", "acceptedAnswer": { "@type": "Answer", "text": "Modelo itinerante sin local: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance), inversión 4-7x menor (3.500 EUR mínimo viable vs 70-130K), ingresos por evento concentrados mayo-septiembre + diciembre, captación B2B intensiva con wedding planners." }},
            { "@type": "Question", "name": "¿Cómo cubre la regulación del fuego al aire libre por CCAA?", "acceptedAnswer": { "@type": "Answer", "text": "Anexo dedicado con autorización exigida y restricciones (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL) en 8 comunidades + excepciones para finca privada. El dolor real que ningún competidor ayuda a resolver." }},
            { "@type": "Question", "name": "¿Sirve para presentar al banco?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan Financiero Excel con P&L 3 años, break-even 8-10 eventos año 1, 3 escenarios, mix B2C+B2B y plan de cashflow estacional. Formato ICO/microcrédito." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio Parrillero / Asador Eventos", "item": "https://aichef.pro/plan-negocio-parrillero-asador-eventos" }
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
          subtitle="Parrilleros, asadores castellanos, BBQ pitmasters y emprendedores latinos que usaron el plan para montar o escalar su servicio itinerante de parrilla"
          testimonials={planParrilleroAsadorEventosTestimonials}
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
              <a href="/plan-negocio-cocteleria-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Coctelería Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas-asador" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Asador</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-parrillero-asador-eventos" label="¿Ya compraste el Plan Parrillero / Asador Eventos? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
