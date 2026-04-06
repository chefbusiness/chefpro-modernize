import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-restaurante-peruano/HeroSection';
import ContentGrid from '@/components/guia-restaurante-peruano/ContentGrid';
import WhySection from '@/components/guia-restaurante-peruano/WhySection';
import AuthorSection from '@/components/guia-restaurante-peruano/AuthorSection';
import BonusSection from '@/components/guia-restaurante-peruano/BonusSection';
import BuyBox from '@/components/guia-restaurante-peruano/BuyBox';
import GuaranteeSection from '@/components/guia-restaurante-peruano/GuaranteeSection';
import FaqAccordion from '@/components/guia-restaurante-peruano/FaqAccordion';
import CtaFinal from '@/components/guia-restaurante-peruano/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaRestaurantePeruanoTestimonials } from '@/data/testimonials-guia-restaurante-peruano';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-restaurante-peruano/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaRestaurantePeruano() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España | AI Chef Pro</title>
        <meta name="description" content="Guía premium para montar un restaurante peruano en España: 20 capítulos, 60+ páginas, cevichería, Nikkei, barra de piscos, proveedores peruanos. 8 plantillas Excel + 6 checklists + business plan. 65 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar restaurante peruano españa, abrir cevicheria, restaurante peruano autentico, cocina nikkei, proveedores productos peruanos españa, barra piscos, ceviche, lomo saltado, plan financiero restaurante peruano, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-restaurante-peruano" />
        <meta property="og:title" content="Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España" />
        <meta property="og:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-restaurante-peruano" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-peruano-hero.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Cómo Montar un Restaurante Peruano 80 Plazas — Guía España" />
        <meta name="twitter:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta name="twitter:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-peruano-hero.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España",
          "description": "Guía premium de 20 capítulos para montar un restaurante peruano: cevichería, Nikkei, barra de piscos, proveedores peruanos en España. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.",
          "image": "https://aichef.pro/lovable-uploads/ai-gallery/guia-peruano-hero.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": { "@type": "Offer", "url": "https://aichef.pro/guia-restaurante-peruano", "priceCurrency": "EUR", "price": "65.00", "priceValidUntil": "2026-12-31", "availability": "https://schema.org/InStock" },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cuánto cuesta montar un restaurante peruano en España?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 130.000€ y 300.000€ para 80 plazas. La estación de ceviche y barra de piscos añaden inversión, pero los márgenes en coctelería (78%) compensan." }},
            { "@type": "Question", "name": "¿Dónde consigo productos peruanos auténticos en España?", "acceptedAnswer": { "@type": "Answer", "text": "La guía incluye un capítulo completo con proveedores de ají amarillo, rocoto, maíz morado, pisco y chicha morada con distribución nacional." }},
            { "@type": "Question", "name": "¿Las plantillas Excel incluyen fórmulas?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan financiero a 3 años, escandallos de 15 platos peruanos, menú engineering con coctelería de pisco, cash flow y break-even." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" },
            { "@type": "ListItem", "position": 3, "name": "Guía Restaurante Peruano", "item": "https://aichef.pro/guia-restaurante-peruano" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Chefs, propietarios, inversores y consultores que ya usaron esta guía"
          testimonials={guiaRestaurantePeruanoTestimonials}
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
              <a href="/guia-restaurante-mexicano" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Mexicano</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/guia-restaurante-casual" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Casual</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-restaurante-peruano" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
