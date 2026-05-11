import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-chef-privado-showcooking-eventos/HeroSection';
import ContentGrid from '@/components/plan-chef-privado-showcooking-eventos/ContentGrid';
import WhySection from '@/components/plan-chef-privado-showcooking-eventos/WhySection';
import AuthorSection from '@/components/plan-chef-privado-showcooking-eventos/AuthorSection';
import BonusSection from '@/components/plan-chef-privado-showcooking-eventos/BonusSection';
import BuyBox from '@/components/plan-chef-privado-showcooking-eventos/BuyBox';
import GuaranteeSection from '@/components/plan-chef-privado-showcooking-eventos/GuaranteeSection';
import FaqAccordion from '@/components/plan-chef-privado-showcooking-eventos/FaqAccordion';
import CtaFinal from '@/components/plan-chef-privado-showcooking-eventos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planChefPrivadoShowcookingEventosTestimonials } from '@/data/testimonials-plan-chef-privado-showcooking-eventos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-chef-privado-showcooking-eventos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanChefPrivadoShowcookingEventos() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio &amp; Kit Chef Privado / Showcooking a Domicilio — 11 Entregables | AI Chef Pro</title>
        <meta name="description" content="Plan + kit profesional completo para montar tu servicio premium de chef privado y showcooking a domicilio en España 2026. Modelo dual B2C íntimo + B2B corporate. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 96 proveedores premium + Catálogo cuchillería japonesa + Manual técnico APPCC móvil + Carta 12 menús + Modelos contrato B2C/B2B + Guía sistemas Chef Privado vs Personal Chef vs Caterer. Inversión desde 4.500 EUR. €45." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio chef privado, showcooking a domicilio, personal chef España, cena privada premium, chef boda boutique, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-chef-privado-showcooking-eventos" />
        <meta property="og:title" content="Plan de Negocio Chef Privado / Showcooking a Domicilio — 11 Entregables" />
        <meta property="og:description" content="Kit profesional para montar tu servicio premium de chef privado y showcooking a domicilio en España 2026. Modelo B2C+B2B. 11 entregables. Inversión desde 4.500 EUR. €45." />
        <meta property="og:url" content="https://aichef.pro/plan-chef-privado-showcooking-eventos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-chef-privado-showcooking-eventos.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio Chef Privado / Showcooking a Domicilio — 11 Entregables" />
        <meta name="twitter:description" content="Kit profesional para montar tu servicio premium de chef privado y showcooking a domicilio en España. Modelo B2C+B2B. 11 entregables. €45." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-chef-privado-showcooking-eventos.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio & Kit de Chef Privado / Showcooking a Domicilio — 11 Entregables",
          "description": "Plan + kit profesional completo para montar un servicio premium de chef privado y showcooking a domicilio en España 2026. Modelo dual B2C íntimo (cenas en pareja, cumpleaños, aniversarios, brunch privado) + B2B corporate (showcooking empresa, hoteles boutique, wedding planners, cooking class team-building, cena directiva fin de año). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 96 proveedores premium (cuchillería japonesa, vajilla Pordamsa, AOVE DO, caviar Riofrío), catálogo equipamiento + cuchillería, manual técnico servicio domicilio APPCC móvil con 7 PCC, carta de 12 menús temáticos, modelos de contrato B2C+B2B con confidencialidad y MSA, 10 experiencias temáticas, guía sistemas Chef Privado vs Personal Chef vs Caterer y checklist de apertura con anexo regulación CCAA catering itinerante.",
          "image": "https://aichef.pro/og-plan-chef-privado-showcooking-eventos.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-chef-privado-showcooking-eventos",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "David Ramírez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Llevaba 3 años haciendo cenas en domicilios con boca-oreja. El plan me dio la marca personal, el portfolio profesional y el dossier B2B. En 4 meses cerré 6 acuerdos con hoteles boutique de Madrid." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Marta Soriano" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La calculadora pricing dual B2C + B2B me ahorró 6 meses de prueba y error. Antes tiraba precios al aire, ahora cierro presupuestos en 10 minutos con margen real del 60 %." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Mendieta" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Las 10 experiencias temáticas se convirtieron en mi catálogo comercial B2B. Subí el ticket medio de showcooking corporate de 1.250 € a 1.850 € en 8 meses sin perder clientes." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Para quién está pensado este plan?", "acceptedAnswer": { "@type": "Answer", "text": "Para chefs profesionales que quieren montar un servicio premium de chef privado y showcooking a domicilio en España. Cubre cliente final particular (cumpleaños, aniversarios, San Valentín, brunch privado) y B2B (showcooking corporate, hoteles boutique 4-5*, wedding planners, agencias con cooking class team-building y cenas directiva fin de año)." }},
            { "@type": "Question", "name": "¿Qué diferencia hay con un Personal Chef o un Caterer?", "acceptedAnswer": { "@type": "Answer", "text": "Mucha. Chef Privado (modelo por evento, ticket 580-2.200 EUR, marca personal, multi-cliente), Personal Chef (recurrente con 1-3 clientes high-net-worth, 1.800-4.500 EUR/mes), Caterer (escalable con cocina central y plantilla, 8.000-150.000 EUR por evento). El plan recomienda empezar siempre por chef privado y pivotar después si encaja con tu vida y negocio." }},
            { "@type": "Question", "name": "¿Cómo cubre la regulación de catering itinerante por CCAA?", "acceptedAnswer": { "@type": "Answer", "text": "Anexo dedicado con resumen operativo de 17 CCAA: tipo de Registro Sanitario + RGSEAA, requisitos cocina del cliente, normativa transporte alimentos, etiquetado bilingüe Cataluña/País Vasco, trámites telemáticos vs presenciales y plazos por CCAA." }},
            { "@type": "Question", "name": "¿Sirve para presentar al banco?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Plan Financiero Excel con P&L 3 años, break-even 9-12 eventos/mes año 1, 3 escenarios de inversión (4.500 / 11.500 / 30.000 EUR), mix B2C+B2B desglosado y plan de cashflow con picos diciembre y verano. Formato ICO/microcrédito." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio Chef Privado / Showcooking", "item": "https://aichef.pro/plan-chef-privado-showcooking-eventos" }
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
          subtitle="Chefs privados, showcookers corporate, personal chefs y wedding planners que usaron el plan para montar o impulsar su empresa premium de chef privado a domicilio"
          testimonials={planChefPrivadoShowcookingEventosTestimonials}
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
              <a href="/plan-negocio-paellero-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Paellero Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/plan-negocio-parrillero-asador-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Parrillero Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-chef-privado-showcooking-eventos" label="¿Ya compraste el Plan Chef Privado / Showcooking? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
