import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-paellero-eventos/HeroSection';
import ContentGrid from '@/components/plan-negocio-paellero-eventos/ContentGrid';
import WhySection from '@/components/plan-negocio-paellero-eventos/WhySection';
import AuthorSection from '@/components/plan-negocio-paellero-eventos/AuthorSection';
import BonusSection from '@/components/plan-negocio-paellero-eventos/BonusSection';
import BuyBox from '@/components/plan-negocio-paellero-eventos/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-paellero-eventos/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-paellero-eventos/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-paellero-eventos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planPaelleroEventosTestimonials } from '@/data/testimonials-plan-paellero-eventos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-paellero-eventos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioPaelleroEventos() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio &amp; Kit Paellero / Paella para Eventos — 11 Entregables | AI Chef Pro</title>
        <meta name="description" content="Plan + kit profesional completo para montar tu servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido B2C + B2B. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 88 proveedores DO Valencia + Catálogo equipamiento + Manual técnico del fuego + socarrat + Carta 12 paellas + Modelos contrato B2C/B2B + Guía 8 sistemas + roadmap food truck arrocería. Inversión desde 3.500 EUR. €45." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio paellero, paella eventos, arroz para eventos, mestre arrosser, paella valenciana premium, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-paellero-eventos" />
        <meta property="og:title" content="Plan de Negocio Paellero / Paella para Eventos — 11 Entregables" />
        <meta property="og:description" content="Kit profesional para montar tu servicio premium de paella itinerante en España 2026. Modelo B2C+B2B. 11 entregables. Inversión desde 3.500 EUR. €45." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-paellero-eventos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-paellero-eventos.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio Paellero / Paella para Eventos — 11 Entregables" />
        <meta name="twitter:description" content="Kit profesional para montar tu servicio premium de paella itinerante en España. Modelo B2C+B2B. 11 entregables. €45." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-paellero-eventos.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio & Kit de Paellero / Paella para Eventos — 11 Entregables",
          "description": "Plan + kit profesional completo para montar un servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido B2C particular (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 88 proveedores reales DO Valencia + Calasparra, catálogo equipamiento + menaje, manual técnico paellero (técnica del fuego + socarrat + 6 arroces + 3 caldos + 12 paellas), carta de 12 paellas, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck arrocería y checklist de apertura con anexo CCAA fuego al aire libre y excepción Falles.",
          "image": "https://aichef.pro/og-plan-negocio-paellero-eventos.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-paellero-eventos",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Vicent Pellicer" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Llevo 25 años haciendo paellas en fiestas del pueblo y siempre me faltó el plan de negocio para escalar a bodas premium. La calculadora pricing y el modelo contrato B2B me cerraron 4 wedding planners en 2 meses." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carmen Soler" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El manual técnico del fuego y el socarrat es oro puro. La tabla de cocción de 12 paellas la imprimí y la tengo plastificada en la furgo. Mis bodas en finca mejoraron en consistencia desde la primera temporada." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Marc Esteve" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Empecé con 4.200 EUR siguiendo el escenario mínimo viable. En el segundo año ya facturo más de 95.000 EUR. La plantilla de 88 proveedores DO Valencia me ahorró 3 meses de búsqueda." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Para quién está pensado este plan?", "acceptedAnswer": { "@type": "Answer", "text": "Para profesionales del arroz y la paella — mestres arrossers valencianos, paelleros murcianos, alicantinos, paelleros corporate o emprendedores españoles — que quieren montar un servicio premium itinerante para eventos en España. Cubre cliente final particular (bodas íntimas, cumpleaños, comuniones, fiestas del pueblo) y B2B (wedding planners, agencias, hoteles, ayuntamientos, empresas team-building)." }},
            { "@type": "Question", "name": "¿Qué diferencia hay con un Restaurante de Arroces con local fijo?", "acceptedAnswer": { "@type": "Answer", "text": "Modelo itinerante sin local: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija, inversión 4-7x menor (3.500-25.000 EUR vs 70-130K), ingresos concentrados mayo-octubre + Falles (70-75 % facturación), captación B2B intensiva con wedding planners." }},
            { "@type": "Question", "name": "¿Cómo cubre la regulación del fuego al aire libre por CCAA?", "acceptedAnswer": { "@type": "Answer", "text": "Anexo dedicado con autorización exigida y restricciones (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak, PIDOM) en 8 comunidades + excepciones para finca privada y excepción cultural Falles/festes valencianas — vital para paelleros del Levante." }},
            { "@type": "Question", "name": "¿Sirve para presentar al banco?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan Financiero Excel con P&L 3 años, break-even 18-22 eventos año 1, 3 escenarios de inversión, mix B2C+B2B y plan de cashflow estacional. Formato ICO/microcrédito." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio Paellero / Paella Eventos", "item": "https://aichef.pro/plan-negocio-paellero-eventos" }
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
          subtitle="Paelleros profesionales, mestres arrossers y wedding planners que usaron el plan para montar o impulsar su empresa premium de paella y arroces para eventos"
          testimonials={planPaelleroEventosTestimonials}
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
              <a href="/plan-negocio-parrillero-asador-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Parrillero Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/plan-negocio-cocteleria-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Coctelería Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-paellero-eventos" label="¿Ya compraste el Plan Paellero / Paella Eventos? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
