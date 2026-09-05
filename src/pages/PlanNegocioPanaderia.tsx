import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-panaderia/HeroSection';
import ContentGrid from '@/components/plan-negocio-panaderia/ContentGrid';
import WhySection from '@/components/plan-negocio-panaderia/WhySection';
import AuthorSection from '@/components/plan-negocio-panaderia/AuthorSection';
import BonusSection from '@/components/plan-negocio-panaderia/BonusSection';
import BuyBox from '@/components/plan-negocio-panaderia/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-panaderia/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-panaderia/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-panaderia/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planPanaderiaTestimonials } from '@/data/testimonials-plan-panaderia';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-panaderia/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioPanaderia() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio: Panadería / Obrador — Plan Financiero Excel + Checklist Apertura | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio completo para abrir una panadería u obrador artesanal en España 2026. Plan financiero Excel de 9 hojas con P&L 3 años + estacionalidad navideña, tesorería mes a mes, plan de financiación con DSCR, inversión inicial y punto de equilibrio en transacciones diarias, plan de negocio en Word de 10 secciones y checklist de apertura con 66 trámites, incluida la inscripción en el registro sanitario autonómico. €35." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio panadería, plan financiero obrador artesanal, abrir panadería España, RGSEAA obrador, horno pisos rotativo, masa madre, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-panaderia" />
        <meta property="og:title" content="Plan de Negocio: Panadería / Obrador — Plan Financiero + Checklist 66 trámites" />
        <meta property="og:description" content="Excel de 9 hojas con P&L 3 años, tesorería y financiación + checklist de apertura con 66 trámites, incluido el registro sanitario autonómico, para abrir tu panadería en España. €35." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-panaderia" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-panaderia.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio: Panadería / Obrador — Excel + Checklist Apertura" />
        <meta name="twitter:description" content="Plan de negocio profesional para abrir una panadería u obrador artesanal en España. €35." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-panaderia.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio: Panadería / Obrador — Plan Financiero Excel, Inversión Inicial y Checklist Apertura",
          "description": "Plan de negocio completo para abrir una panadería u obrador artesanal en España. Incluye plan financiero Excel de 9 hojas con P&L previsional a 3 años con estacionalidad navideña, inversión inicial detallada (101.600 € de CAPEX y 145.215 € con el colchón de caja), punto de equilibrio en 162 transacciones diarias con ticket medio de 5,50 € sin IVA, escenarios financieros, tesorería mes a mes con liquidación de IVA, plan de financiación con cuadro de amortización francés y DSCR, cuadro de personal panadero de 6 puestos con turno de madrugada y auditoría de horas, checklist de apertura con 66 trámites incluida la inscripción en el registro sanitario de tu Comunidad Autónoma, equipamiento específico (horno de pisos o rotativo, amasadora espiral 25-50 kg, cámara de fermentación) y los rangos de referencia del sector panadero español 2026.",
          "image": "https://aichef.pro/og-plan-negocio-panaderia.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-panaderia",
            "priceCurrency": "EUR",
            "price": "35.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Presenté el plan al banco y me aprobaron 65K EUR de financiación con leasing del horno. La proyección a 3 años con estacionalidad navideña fue clave." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist con 60+ trámites me salvó del laberinto del RGSEAA y la licencia de obrador. Hubiera tardado el doble." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El break-even por kilos de pan diarios y el mix bollería son exactamente los ratios que necesito ver." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Es un plan genérico o específico para panadería?", "acceptedAnswer": { "@type": "Answer", "text": "Es 100% específico para panadería y obrador artesanal en España. Las partidas de inversión, ratios financieros, costes de personal con turno madrugada y trámites legales (registro sanitario autonómico, licencia de actividad) están adaptados al modelo panadero." }},
            { "@type": "Question", "name": "¿Puedo presentar este plan al banco o a inversores?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Incluye P&L a 3 años con estacionalidad navideña, tesorería mes a mes, plan de financiación con cuadro de amortización y DSCR año a año, punto de equilibrio en transacciones diarias y 3 escenarios. Es el formato que piden los bancos para microcrédito ICO y leasing de horno y amasadora." }},
            { "@type": "Question", "name": "¿Qué trámites legales incluye el checklist?", "acceptedAnswer": { "@type": "Answer", "text": "66 trámites en 6 fases: constitución de la SL, local y licencias (registro sanitario autonómico, licencia clasificada, salida de humos), equipamiento, personal (turno de madrugada, PRL, registro horario), marketing y primeros 90 días." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio: Panadería / Obrador", "item": "https://aichef.pro/plan-negocio-panaderia" }
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
          subtitle="Maestros panaderos, propietarios de obrador artesanal e inversores que abrieron su panadería con un plan financiero profesional"
          testimonials={planPanaderiaTestimonials}
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
              <a href="/kit-tareas-panaderia" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Panadería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-panaderia" label="¿Ya compraste el Plan de Negocio Panadería? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
