import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-restaurante-mexicano/HeroSection';
import ContentGrid from '@/components/guia-restaurante-mexicano/ContentGrid';
import WhySection from '@/components/guia-restaurante-mexicano/WhySection';
import AuthorSection from '@/components/guia-restaurante-mexicano/AuthorSection';
import BonusSection from '@/components/guia-restaurante-mexicano/BonusSection';
import BuyBox from '@/components/guia-restaurante-mexicano/BuyBox';
import GuaranteeSection from '@/components/guia-restaurante-mexicano/GuaranteeSection';
import FaqAccordion from '@/components/guia-restaurante-mexicano/FaqAccordion';
import CtaFinal from '@/components/guia-restaurante-mexicano/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaRestauranteMexicanoTestimonials } from '@/data/testimonials-guia-restaurante-mexicano';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-restaurante-mexicano/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaRestauranteMexicano() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España | AI Chef Pro</title>
        <meta name="description" content="Guía premium para montar un restaurante mexicano en España: 20 capítulos, 60+ páginas, proveedores de productos mexicanos, barra de tequilas, tacos, escandallos. 8 plantillas Excel + 6 checklists + business plan. 65 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar restaurante mexicano españa, abrir taqueria, restaurante mexicano autentico, proveedores productos mexicanos españa, barra tequilas mezcal, tacos al pastor, plan financiero restaurante mexicano, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-restaurante-mexicano" />
        <meta property="og:title" content="Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España" />
        <meta property="og:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-restaurante-mexicano" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Cómo Montar un Restaurante Mexicano 80 Plazas — Guía España" />
        <meta name="twitter:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta name="twitter:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España",
          "description": "Guía premium de 20 capítulos para montar un restaurante mexicano: plan financiero, proveedores de productos mexicanos, barra de tequilas, escandallos de tacos. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.",
          "image": "https://aichef.pro/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/guia-restaurante-mexicano",
            "priceCurrency": "EUR",
            "price": "65.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cuánto cuesta montar un restaurante mexicano en España?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 120.000€ y 280.000€ para 80 plazas. La cocina mexicana requiere equipamiento específico (comal, tortillera) pero es más económica que otros conceptos." }},
            { "@type": "Question", "name": "¿Dónde consigo productos mexicanos auténticos en España?", "acceptedAnswer": { "@type": "Answer", "text": "La guía incluye un capítulo completo con proveedores de importación de chiles, masa de maíz, tortillas, tequila y mezcal con distribución nacional." }},
            { "@type": "Question", "name": "¿Las plantillas Excel incluyen fórmulas?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan financiero a 3 años, escandallos de 15 platos mexicanos clave, menú engineering, cash flow y break-even. Todo con fórmulas automáticas." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" },
            { "@type": "ListItem", "position": 3, "name": "Guía Restaurante Mexicano", "item": "https://aichef.pro/guia-restaurante-mexicano" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Propietarios, chefs, inversores y consultores que ya usaron esta guía"
          testimonials={guiaRestauranteMexicanoTestimonials}
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
              <a href="/guia-restaurante-casual" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Casual</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/guia-restaurante-gastronomico" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Gastronómico</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-restaurante-mexicano" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
