import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-cafeteria/HeroSection';
import ContentGrid from '@/components/plan-negocio-cafeteria/ContentGrid';
import WhySection from '@/components/plan-negocio-cafeteria/WhySection';
import AuthorSection from '@/components/plan-negocio-cafeteria/AuthorSection';
import BonusSection from '@/components/plan-negocio-cafeteria/BonusSection';
import BuyBox from '@/components/plan-negocio-cafeteria/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-cafeteria/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-cafeteria/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-cafeteria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planCafeteriaTestimonials } from '@/data/testimonials-plan-cafeteria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-cafeteria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioCafeteria() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio: Cafetería / Brunch — Plan Financiero Excel + Checklist Apertura | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio completo para abrir una cafetería o brunch en España 2026. Plan financiero Excel con P&L 3 años, punto de equilibrio en 53 clientes/día, escenarios y checklist apertura con 65+ trámites bajo licencia inocua. €29." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio cafetería, plan financiero brunch España, abrir cafetería, checklist apertura cafetería, licencia inocua hostelería, máquina espresso profesional, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-cafeteria" />
        <meta property="og:title" content="Plan de Negocio: Cafetería / Brunch — Plan Financiero + Checklist 65 trámites" />
        <meta property="og:description" content="Excel P&L 3 años + checklist apertura 65 trámites para abrir una cafetería o brunch en España. €29." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-cafeteria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-cafeteria.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio: Cafetería / Brunch — Excel + Checklist Apertura" />
        <meta name="twitter:description" content="Plan de negocio profesional para abrir una cafetería o brunch en España. €29." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-cafeteria.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio: Cafetería / Brunch — Plan Financiero Excel, Inversión Inicial y Checklist Apertura",
          "description": "Plan de negocio completo para abrir una cafetería o brunch en España. Incluye plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada (~94K EUR), punto de equilibrio en 53 clientes/día con ticket medio €9,50, escenarios financieros, cuadro de personal con Seg. Social, checklist de apertura con 65+ trámites bajo licencia de actividad inocua y RGSEAA, equipamiento específico cafetería y ratios sectoriales del mercado español 2026.",
          "image": "https://aichef.pro/og-plan-negocio-cafeteria.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-cafeteria",
            "priceCurrency": "EUR",
            "price": "29.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El plan financiero me ayudó a conseguir financiación ICO. El desglose de inversión en máquina de café, horno y mobiliario era exacto." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Gracias al checklist no se me pasó ningún trámite. La licencia de actividad inocua fue clave para abrir rápido." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El punto de equilibrio de 53 clientes/día con ticket medio €9,50 es realista. Números que cuadran con el mercado." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Es un plan genérico o específico para cafetería?", "acceptedAnswer": { "@type": "Answer", "text": "Es 100% específico para cafetería y brunch en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de cafetería con barra, sala y terraza." }},
            { "@type": "Question", "name": "¿Puedo presentar este plan al banco o a inversores?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Incluye P&L 3 años, punto de equilibrio y 3 escenarios. Es exactamente el formato que piden bancos e inversores." }},
            { "@type": "Question", "name": "¿Qué trámites legales incluye el checklist?", "acceptedAnswer": { "@type": "Answer", "text": "Más de 65 trámites en 6 fases: constitución SL, licencias municipales (inocua + RGSEAA + terraza), equipamiento, RRHH, marketing pre-apertura y primeros 90 días." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio: Cafetería / Brunch", "item": "https://aichef.pro/plan-negocio-cafeteria" }
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
          subtitle="Propietarios e inversores que abrieron su cafetería o brunch con un plan financiero profesional"
          testimonials={planCafeteriaTestimonials}
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
              <a href="/plan-negocio-bar-restaurante" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Bar-Restaurante</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas-cafeteria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Cafetería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-cafeteria" label="¿Ya compraste el Plan de Negocio Cafetería? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
