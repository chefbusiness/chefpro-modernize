import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-restaurante-nikkei/HeroSection';
import ContentGrid from '@/components/guia-restaurante-nikkei/ContentGrid';
import WhySection from '@/components/guia-restaurante-nikkei/WhySection';
import AuthorSection from '@/components/guia-restaurante-nikkei/AuthorSection';
import BonusSection from '@/components/guia-restaurante-nikkei/BonusSection';
import BuyBox from '@/components/guia-restaurante-nikkei/BuyBox';
import GuaranteeSection from '@/components/guia-restaurante-nikkei/GuaranteeSection';
import FaqAccordion from '@/components/guia-restaurante-nikkei/FaqAccordion';
import CtaFinal from '@/components/guia-restaurante-nikkei/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaRestauranteNikkeiTestimonials } from '@/data/testimonials-guia-restaurante-nikkei';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-restaurante-nikkei/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaRestauranteNikkei() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España | AI Chef Pro</title>
        <meta name="description" content="Guía premium para montar un restaurante nikkei (fusión peruano-japonesa) en España: 20 capítulos, tiraditos, ceviches nikkei, omakase, barra de pisco y sake. 9 plantillas Excel + 6 checklists + business plan. 65 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar restaurante nikkei españa, cocina nikkei fusion peruano japonesa, tiraditos, ceviche nikkei, omakase nikkei, leche de tigre, aji amarillo, barra pisco sake, proveedores pescado sashimi grade españa, anisakis, plan financiero restaurante nikkei, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-restaurante-nikkei" />
        <meta property="og:title" content="Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España" />
        <meta property="og:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-restaurante-nikkei" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Cómo Montar un Restaurante Nikkei 60 Plazas — Guía España" />
        <meta name="twitter:description" content="Guía premium 60+ págs + 8 plantillas Excel + 6 checklists + business plan + manual de operaciones. 65 EUR." />
        <meta name="twitter:image" content="https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España",
          "description": "Guía premium de 20 capítulos para montar un restaurante nikkei (fusión peruano-japonesa): tiraditos, ceviches nikkei, omakase, barra de pisco y sake, proveedores de ají amarillo, rocoto y pescado sashimi-grade en España. Incluye 9 plantillas Excel, 6 checklists, business plan y manual de operaciones.",
          "image": "https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": { "@type": "Offer", "url": "https://aichef.pro/guia-restaurante-nikkei", "priceCurrency": "EUR", "price": "65.00", "priceValidUntil": "2026-12-31", "availability": "https://schema.org/InStock" },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cuánto cuesta montar un restaurante nikkei en España?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 280.000€ y 520.000€ para 60 plazas. El equipamiento mixto (barra de tiraditos, robata/josper, wok station, licuadoras para leches de tigre, cuchillos yanagiba y molcajete) y la brigada especializada son el mayor coste, pero los márgenes en pisco, sake y coctelería nikkei (75-85%) lo compensan." }},
            { "@type": "Question", "name": "¿Qué normativa de anisakis aplica a tiraditos y leches de tigre?", "acceptedAnswer": { "@type": "Answer", "text": "El RD 1420/2006 OBLIGA a congelar preventivamente todo pescado para consumo crudo (incluidos tiraditos, ceviches nikkei y marinados en leche de tigre) a -20°C durante mínimo 24 horas. La guía incluye PCC específico, checklist y protocolo de trazabilidad." }},
            { "@type": "Question", "name": "¿Dónde consigo ají amarillo, rocoto y productos peruanos en España?", "acceptedAnswer": { "@type": "Answer", "text": "La guía incluye directorio de importadores peruanos en España (Inkawasi, Latin Products y otros), productos japoneses (arroz Koshihikari, sake, nori) y pescado sashimi-grade en Mercamadrid/Mercabarna." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" },
            { "@type": "ListItem", "position": 3, "name": "Guía Restaurante Nikkei", "item": "https://aichef.pro/guia-restaurante-nikkei" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Itamae, chefs, propietarios, inversores y consultores que ya usaron esta guía"
          testimonials={guiaRestauranteNikkeiTestimonials}
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
              <a href="/guia-restaurante-peruano" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Peruano</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/guia-restaurante-mexicano" className="text-gray-500 hover:text-[#FFD700] transition-colors">Guía Restaurante Mexicano</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-restaurante-nikkei" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
