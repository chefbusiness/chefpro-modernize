import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-plan-financiero/HeroSection';
import ContentGrid from '@/components/kit-plan-financiero/ContentGrid';
import WhySection from '@/components/kit-plan-financiero/WhySection';
import AuthorSection from '@/components/kit-plan-financiero/AuthorSection';
import BonusSection from '@/components/kit-plan-financiero/BonusSection';
import BuyBox from '@/components/kit-plan-financiero/BuyBox';
import GuaranteeSection from '@/components/kit-plan-financiero/GuaranteeSection';
import FaqAccordion from '@/components/kit-plan-financiero/FaqAccordion';
import CtaFinal from '@/components/kit-plan-financiero/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planFinancieroTestimonials } from '@/data/testimonials-plan-financiero';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-plan-financiero/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitPlanFinanciero() {
  return (
    <>
      <Helmet>
        <title>Kit Plan Financiero para Restaurantes — Plantillas Excel | AI Chef Pro</title>
        <meta name="description" content="10 plantillas Excel con fórmulas automáticas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, P&L, CAPEX, ratios e informe de viabilidad para bancos. 19 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan financiero restaurante, plan de negocio restaurante, punto equilibrio restaurante, cash flow restaurante, P&L hosteleria, viabilidad restaurante, CAPEX restaurante, food cost, abrir restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-plan-financiero" />
        <meta property="og:title" content="Kit Plan Financiero para Restaurantes — Plantillas Excel" />
        <meta property="og:description" content="10 plantillas Excel: plan financiero 3 y 5 años, break-even, cash flow, P&L, ratios, informe bancario. 19 EUR." />
        <meta property="og:url" content="https://aichef.pro/kit-plan-financiero" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-plan-financiero.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit Plan Financiero para Restaurantes" />
        <meta name="twitter:description" content="Plantillas Excel profesionales para planificar las finanzas de tu restaurante. 19 EUR." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit Plan Financiero para Restaurantes — Plantillas Excel",
          "description": "10 plantillas Excel con fórmulas automáticas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, P&L, CAPEX, ratios e informe de viabilidad para bancos.",
          "image": "https://aichef.pro/og-kit-plan-financiero.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-plan-financiero",
            "priceCurrency": "EUR",
            "price": "19.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Ricardo Gomez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El plan previsional a 3 anos fue lo que me pidio el banco. Lo presente tal cual y me aprobaron 120.000 EUR." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Ana Beltran" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Lo uso con todos mis clientes. El simulador de escenarios profesionaliza cualquier proyecto de apertura." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Isabel Campos" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El dashboard de ratios con benchmarks del sector es exactamente lo que necesitaba para los comites de direccion." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Sirve para un restaurante que ya esta abierto?", "acceptedAnswer": { "@type": "Answer", "text": "Si. El P&L mensual, el dashboard de ratios y el cash flow son especialmente utiles para restaurantes en funcionamiento." }},
            { "@type": "Question", "name": "¿Necesito conocimientos de contabilidad?", "acceptedAnswer": { "@type": "Answer", "text": "No. Solo introduces tus numeros y las formulas calculan todo automaticamente: ratios, graficos, escenarios." }},
            { "@type": "Question", "name": "¿El banco aceptara este informe?", "acceptedAnswer": { "@type": "Answer", "text": "Si. El formato sigue la estructura que las entidades financieras esperan: TIR, VAN, payback period, escenarios." }},
            { "@type": "Question", "name": "¿Hay garantia de devolucion?", "acceptedAnswer": { "@type": "Answer", "text": "30 dias de garantia completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit Plan Financiero para Restaurantes", "item": "https://aichef.pro/kit-plan-financiero" }
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
          subtitle="Propietarios, inversores y consultores que ya planifican sus finanzas con estas plantillas"
          testimonials={planFinancieroTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-inventario" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Inventario</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-gestion-personal" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Gestion Personal</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-plan-financiero" label="¿Ya compraste el Kit Plan Financiero? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
