import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-restaurante-gastronomico/HeroSection';
import ContentGrid from '@/components/guia-restaurante-gastronomico/ContentGrid';
import WhySection from '@/components/guia-restaurante-gastronomico/WhySection';
import AuthorSection from '@/components/guia-restaurante-gastronomico/AuthorSection';
import BonusSection from '@/components/guia-restaurante-gastronomico/BonusSection';
import BuyBox from '@/components/guia-restaurante-gastronomico/BuyBox';
import GuaranteeSection from '@/components/guia-restaurante-gastronomico/GuaranteeSection';
import FaqAccordion from '@/components/guia-restaurante-gastronomico/FaqAccordion';
import CtaFinal from '@/components/guia-restaurante-gastronomico/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaRestauranteGastronomicoTestimonials } from '@/data/testimonials-guia-restaurante-gastronomico';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-restaurante-gastronomico/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaRestauranteGastronomico() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol) | AI Chef Pro</title>
        <meta name="description" content="Guía premium para montar un restaurante gastronómico en España: 22 capítulos, 80+ páginas, plan financiero, diseño de cocina y sala, brigada, bodega, Michelin, Sol Repsol. 10 plantillas Excel + 8 checklists + business plan. 85 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar restaurante gastronomico, abrir restaurante fine dining, estrella michelin requisitos, sol repsol restaurante, plan financiero restaurante, equipamiento cocina profesional, brigada cocina, restaurante 65 plazas, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-restaurante-gastronomico" />
        <meta property="og:title" content="Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol)" />
        <meta property="og:description" content="Guía premium 80+ págs + 10 plantillas Excel + 8 checklists + business plan + manual de sala. 85 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-restaurante-gastronomico" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-gastro-hero.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España" />
        <meta name="twitter:description" content="Guía premium 80+ págs + 10 plantillas Excel + 8 checklists + business plan + manual de sala. 85 EUR." />
        <meta name="twitter:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-gastro-hero.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol)",
          "description": "Guía premium de 22 capítulos para montar un restaurante gastronómico: plan financiero, diseño cocina y sala, brigada, bodega, Michelin, Sol Repsol. Incluye 10 plantillas Excel, 8 checklists, business plan y manual de sala.",
          "image": "https://aichef.pro/lovable-uploads/ai-gallery/guia-gastro-hero.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/guia-restaurante-gastronomico",
            "priceCurrency": "EUR",
            "price": "85.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cuánto cuesta montar un restaurante gastronómico?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 500.000€ y 900.000€ para 65 plazas de nivel medio-alto en capital de provincia española. La guía desglosa cada partida." }},
            { "@type": "Question", "name": "¿Incluye información sobre cómo aspirar a Estrella Michelin?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Los capítulos 17-19 cubren Michelin, Sol Repsol y The World's 50 Best con criterios, proceso de inspección y estrategia." }},
            { "@type": "Question", "name": "¿Las plantillas Excel incluyen fórmulas?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan financiero a 3 años, escandallos, menu engineering, cash flow, break-even y más. Todo con fórmulas encadenadas." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" },
            { "@type": "ListItem", "position": 3, "name": "Guía Restaurante Gastronómico", "item": "https://aichef.pro/guia-restaurante-gastronomico" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Chefs, sommeliers, inversores y consultores que ya usaron esta guía"
          testimonials={guiaRestauranteGastronomicoTestimonials}
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
              <a href="/kit-tareas-restaurante-creativo" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Restaurante Creativo</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-plan-financiero" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Plan Financiero</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-restaurante-gastronomico" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
