import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-dark-kitchen/HeroSection';
import ContentGrid from '@/components/guia-dark-kitchen/ContentGrid';
import WhySection from '@/components/guia-dark-kitchen/WhySection';
import AuthorSection from '@/components/guia-dark-kitchen/AuthorSection';
import BonusSection from '@/components/guia-dark-kitchen/BonusSection';
import BuyBox from '@/components/guia-dark-kitchen/BuyBox';
import GuaranteeSection from '@/components/guia-dark-kitchen/GuaranteeSection';
import FaqAccordion from '@/components/guia-dark-kitchen/FaqAccordion';
import CtaFinal from '@/components/guia-dark-kitchen/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaDarkKitchenTestimonials } from '@/data/testimonials-guia-dark-kitchen';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-dark-kitchen/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaDarkKitchen() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar una Dark Kitchen en España — Guía Completa | AI Chef Pro</title>
        <meta name="description" content="Guía completa para montar una dark kitchen en España: 12 capítulos, requisitos legales, plan financiero, diseño de cocina, tecnología, marketing y 3 checklists Excel. 24 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar dark kitchen, abrir dark kitchen españa, ghost kitchen, cloud kitchen, cocina fantasma, dark kitchen madrid, dark kitchen barcelona, montar negocio delivery, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-dark-kitchen" />
        <meta property="og:title" content="Cómo Montar una Dark Kitchen en España — Guía Completa" />
        <meta property="og:description" content="Guía PDF + DOCX editable + 3 checklists Excel + calculadora de viabilidad. 24 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-dark-kitchen" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-guia-dark-kitchen.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar una Dark Kitchen en España — Guía Completa",
          "description": "Guía completa de 12 capítulos para montar una dark kitchen: requisitos legales, plan financiero, diseño, tecnología, marketing. Incluye 3 checklists Excel y calculadora de viabilidad.",
          "image": "https://aichef.pro/og-guia-dark-kitchen.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/guia-dark-kitchen",
            "priceCurrency": "EUR",
            "price": "24.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cuánto cuesta montar una dark kitchen?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 30.000€ y 80.000€ dependiendo de ubicación, equipamiento y número de marcas. La guía desglosa cada partida." }},
            { "@type": "Question", "name": "¿Incluye los requisitos legales actualizados?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Licencias, APPCC, registro sanitario, seguros, normativa plásticos 2026. Actualizada para España." }},
            { "@type": "Question", "name": "¿El DOCX es editable?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Recibes PDF editorial + DOCX editable para personalizar y presentar a socios o bancos." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Cómo Montar una Dark Kitchen", "item": "https://aichef.pro/guia-dark-kitchen" }
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
          subtitle="Emprendedores, consultores e inversores que ya usaron esta guía para abrir dark kitchens"
          testimonials={guiaDarkKitchenTestimonials}
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
              <a href="/kit-tareas-dark-kitchen" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Dark Kitchen</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-plan-financiero" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Plan Financiero</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-dark-kitchen" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
