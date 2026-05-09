import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-tapas-bar/HeroSection';
import ContentGrid from '@/components/plan-negocio-tapas-bar/ContentGrid';
import WhySection from '@/components/plan-negocio-tapas-bar/WhySection';
import AuthorSection from '@/components/plan-negocio-tapas-bar/AuthorSection';
import BonusSection from '@/components/plan-negocio-tapas-bar/BonusSection';
import BuyBox from '@/components/plan-negocio-tapas-bar/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-tapas-bar/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-tapas-bar/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-tapas-bar/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planTapasBarTestimonials } from '@/data/testimonials-plan-tapas-bar';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-tapas-bar/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioTapasBar() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio: Tapas Bar / Gastrobar — Plan Financiero Excel + DOCX + Checklist Apertura | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio completo para abrir un tapas bar o gastrobar en España 2026. Documento DOCX 10 secciones + plan financiero Excel con P&L 3 años + checklist apertura con 63 trámites incluyendo licencia clasificada y salida de humos. €35." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio tapas bar, plan financiero gastrobar España, abrir tapas bar, checklist apertura tapas bar, licencia clasificada hostelería, salida de humos restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-tapas-bar" />
        <meta property="og:title" content="Plan de Negocio: Tapas Bar / Gastrobar — Plan Financiero + DOCX + Checklist" />
        <meta property="og:description" content="Documento DOCX 10 secciones + Excel P&L 3 años + checklist apertura 63 trámites para abrir un tapas bar o gastrobar en España. €35." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-tapas-bar" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-tapas-bar.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio: Tapas Bar / Gastrobar — DOCX + Excel + Checklist" />
        <meta name="twitter:description" content="Plan de negocio profesional para abrir un tapas bar o gastrobar en España. €35." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-tapas-bar.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio: Tapas Bar / Gastrobar — Plan Financiero Excel + DOCX + Checklist Apertura",
          "description": "Plan de negocio completo para abrir un tapas bar o gastrobar en España. Incluye documento DOCX de 10 secciones (resumen ejecutivo, concepto, mercado, DAFO, marketing, operaciones, RRHH, financiero, legal, conclusiones), plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada, punto de equilibrio, 3 escenarios financieros, cuadro de personal con Seg. Social, checklist de apertura con 63 trámites incluyendo licencia clasificada y salida de humos, y ratios sectoriales del mercado español 2026.",
          "image": "https://aichef.pro/og-plan-negocio-tapas-bar.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-tapas-bar",
            "priceCurrency": "EUR",
            "price": "35.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El plan financiero me ayudó a conseguir el préstamo ICO en 2 semanas. El desglose de inversión para cocina y barra fue exacto." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de apertura fue clave. Descubrí que necesitaba licencia clasificada y no inocua por la potencia de cocina. Me ahorré meses de retrasos." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El break-even de 34 clientes al día es realista para un tapas bar bien ubicado. Los márgenes en tapas y bebidas dan mucha confianza." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Es un plan genérico o específico para tapas bar?", "acceptedAnswer": { "@type": "Answer", "text": "Es 100% específico para tapas bar y gastrobar en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de tapas bar con barra y sala, incluyendo licencia clasificada, salida de humos y equipamiento específico." }},
            { "@type": "Question", "name": "¿Puedo presentar este plan al banco o a inversores?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. El plan financiero Excel incluye P&L 3 años, punto de equilibrio y 3 escenarios. El documento DOCX de 10 secciones tiene formato profesional, exactamente lo que piden bancos e inversores." }},
            { "@type": "Question", "name": "¿Qué trámites legales incluye el checklist de apertura?", "acceptedAnswer": { "@type": "Answer", "text": "63 trámites en 6 fases: constitución de la SL, licencia clasificada (no inocua, por potencia de cocina), salida de humos obligatoria, equipamiento, contratación de personal, marketing pre-apertura y primeros 90 días." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio: Tapas Bar / Gastrobar", "item": "https://aichef.pro/plan-negocio-tapas-bar" }
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
          subtitle="Propietarios e inversores que abrieron su tapas bar o gastrobar con un plan financiero profesional"
          testimonials={planTapasBarTestimonials}
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
              <a href="/kit-tareas-tapas-bar" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Tapas Bar</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-tapas-bar" label="¿Ya compraste el Plan de Negocio Tapas Bar? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
