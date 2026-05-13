import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/guia-panaderia-obrador/HeroSection';
import ContentGrid from '@/components/guia-panaderia-obrador/ContentGrid';
import WhySection from '@/components/guia-panaderia-obrador/WhySection';
import AuthorSection from '@/components/guia-panaderia-obrador/AuthorSection';
import BonusSection from '@/components/guia-panaderia-obrador/BonusSection';
import BuyBox from '@/components/guia-panaderia-obrador/BuyBox';
import GuaranteeSection from '@/components/guia-panaderia-obrador/GuaranteeSection';
import FaqAccordion from '@/components/guia-panaderia-obrador/FaqAccordion';
import CtaFinal from '@/components/guia-panaderia-obrador/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { guiaPanaderiaObradorTestimonials } from '@/data/testimonials-guia-panaderia-obrador';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/guia-panaderia-obrador/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function GuiaPanaderiaObrador() {
  return (
    <>
      <Helmet>
        <title>Cómo Montar una Panadería con Obrador — Guía Completa España 2026 | AI Chef Pro</title>
        <meta name="description" content="Guía premium para montar una panadería con obrador en España 2026: 20 capítulos, 70+ páginas, plan financiero, recetario masa madre, salida de humos, APPCC obrador, alérgenos. 9 plantillas Excel + 6 checklists + business plan + manual del obrador. 65 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="como montar panaderia, abrir panaderia con obrador, panaderia masa madre España, plan financiero panaderia, salida de humos panaderia, licencia clasificada panaderia, APPCC obrador panaderia, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/guia-panaderia-obrador" />
        <meta property="og:title" content="Cómo Montar una Panadería con Obrador — Guía Completa España 2026" />
        <meta property="og:description" content="Guía premium 70+ págs + 9 plantillas Excel + 6 checklists + business plan + manual del obrador con recetario masa madre. 65 EUR." />
        <meta property="og:url" content="https://aichef.pro/guia-panaderia-obrador" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-guia-panaderia-obrador.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Cómo Montar una Panadería con Obrador — Guía España 2026" />
        <meta name="twitter:description" content="Guía premium 70+ págs + 9 plantillas Excel + 6 checklists + business plan + manual del obrador. 65 EUR." />
        <meta name="twitter:image" content="https://aichef.pro/og-guia-panaderia-obrador.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Cómo Montar una Panadería con Obrador — Guía Completa España 2026",
          "description": "Guía premium de 20 capítulos para montar una panadería con obrador artesanal: plan financiero, recetario masa madre, salida de humos, licencia clasificada, APPCC obrador con alérgenos cruzados, planes de fermentación 18-72h. Incluye 9 plantillas Excel, 6 checklists, business plan y manual del obrador.",
          "image": "https://aichef.pro/og-guia-panaderia-obrador.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/guia-panaderia-obrador",
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
            { "@type": "Question", "name": "¿Cuánto cuesta montar una panadería con obrador en España?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 120.000€ y 200.000€ para 60-90 m² con obrador propio. La guía desglosa cada partida con costes reales del mercado español 2026 e incluye calculadora CAPEX en Excel." }},
            { "@type": "Question", "name": "¿Incluye recetario de masa madre?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Manual del obrador con recetario técnico: baguette tradition, hogaza T80 masa madre, croissant clásico, brioche, panettone. Incluye refrescos diarios masa madre líquida y sólida." }},
            { "@type": "Question", "name": "¿Cubre la salida de humos y licencia clasificada?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Capítulo 5 + checklist específico de 28 ítems con todos los pasos: verificación pre-alquiler, proyecto técnico, licencia municipal y ejecución. Killer #1 de aperturas frustradas." }},
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" },
            { "@type": "ListItem", "position": 3, "name": "Guía Panadería con Obrador", "item": "https://aichef.pro/guia-panaderia-obrador" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Panaderos</span></>}
          subtitle="Maestros panaderos, emprendedores e inversores que ya usaron esta guía"
          testimonials={guiaPanaderiaObradorTestimonials}
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
              <a href="/kit-tareas-panaderia" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Panadería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/plan-negocio-panaderia" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Negocio Panadería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/productos-digitales" className="text-gray-500 hover:text-[#FFD700] transition-colors">Todos los Productos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="guia-panaderia-obrador" label="¿Ya compraste la guía? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
