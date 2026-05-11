import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-catering-tematico-eventos/HeroSection';
import ContentGrid from '@/components/plan-catering-tematico-eventos/ContentGrid';
import WhySection from '@/components/plan-catering-tematico-eventos/WhySection';
import AuthorSection from '@/components/plan-catering-tematico-eventos/AuthorSection';
import BonusSection from '@/components/plan-catering-tematico-eventos/BonusSection';
import BuyBox from '@/components/plan-catering-tematico-eventos/BuyBox';
import GuaranteeSection from '@/components/plan-catering-tematico-eventos/GuaranteeSection';
import FaqAccordion from '@/components/plan-catering-tematico-eventos/FaqAccordion';
import CtaFinal from '@/components/plan-catering-tematico-eventos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planCateringTematicoEventosTestimonials } from '@/data/testimonials-plan-catering-tematico-eventos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-catering-tematico-eventos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanCateringTematicoEventos() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio para Catering &amp; Kit Temático para Eventos — 11 Entregables | AI Chef Pro</title>
        <meta name="description" content="Plan + kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit que enseña a montar 5 conceptos en paralelo (sushi-bar, tacos al pastor, pizza al horno de leña, asado argentino, ceviche peruano, vegano premium, BBQ texano, tandoor indio…). Modelo dual B2C bodas multiculturales + B2B corporate brand events. 11 entregables. Inversión desde 5.500 EUR. €45." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan negocio catering temático, catering eventos multi-concepto, catering bodas multiculturales, brand events corporate, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-catering-tematico-eventos" />
        <meta property="og:title" content="Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables" />
        <meta property="og:description" content="Kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España 2026. Modelo B2C bodas multiculturales + B2B corporate. 11 entregables. €45." />
        <meta property="og:url" content="https://aichef.pro/plan-catering-tematico-eventos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-catering-tematico-eventos.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables" />
        <meta name="twitter:description" content="Kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España. Modelo B2C+B2B. 11 entregables. €45." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-catering-tematico-eventos.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables",
          "description": "Plan + kit profesional completo para montar un servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit del mercado español enfocado en multi-concepto (3-5 cocinas del mundo en paralelo en un mismo evento). Modelo dual B2C bodas multiculturales + B2B corporate brand events. Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C 35 % + B2B 65 %, Calculadora Pricing multi-concepto, plantilla de 96 proveedores especializados en 12 cocinas del mundo (importadores asiáticos, latinos, italianos, BBQ texano, indios), catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok), 12 conceptos pre-empaquetados, carta 12 menús cocinas del mundo, manual técnico APPCC multi-concepto, modelos contrato B2C + B2B corporate, guía especialización progresiva y checklist apertura con anexo regulación 17 CCAA catering itinerante.",
          "image": "https://aichef.pro/og-plan-catering-tematico-eventos.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-catering-tematico-eventos",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Yuki Tanaka" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El kit me dio el blueprint para escalar de hacer sushi en mi casa a montar 4 estaciones (sushi + ramen + dim sum + bao) en bodas multiculturales premium. Subí ticket de 38 € a 75 €/pax en 8 meses." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Miguel Hernández" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Empecé con tacos al pastor en cumpleaños familiares. Tras el plan añadí cochinita pibil + ceviche peruano + barra mezcal y ahora hago corporate brand events de 80-150 pax con 4 estaciones." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Giuseppe Romano" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Tenía un horno de leña móvil y hacía bodas con sólo pizza. El kit me enseñó a integrar pasta fresca + antipasti + dolci en mi servicio. Ahora ofrezco trattoria completa por 65 €/pax y subí volumen 3x." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Para quién está pensado este plan?", "acceptedAnswer": { "@type": "Answer", "text": "Para chefs y emprendedores en España que quieren montar un servicio premium de catering temático multi-concepto para eventos especializado en 12 cocinas del mundo. Cubre B2C (bodas multiculturales, cumpleaños temáticos, aniversarios) y B2B (corporate brand events, embajadas, wedding planners, festivales gastronómicos). Es el único plan del mercado español enfocado en multi-concepto." }},
            { "@type": "Question", "name": "¿Qué hace este kit diferente del Parrillero, Paellero o Chef Privado?", "acceptedAnswer": { "@type": "Answer", "text": "Esos productos son monoconcepto. Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente). Justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto." }},
            { "@type": "Question", "name": "¿Cuántos conceptos temáticos cubre?", "acceptedAnswer": { "@type": "Answer", "text": "12 conceptos pre-empaquetados: sushi-bar omakase, tacos al pastor, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional. Cada uno con menú + escandallo + equipamiento + ambientación + operativa." }},
            { "@type": "Question", "name": "¿Cómo cubre la regulación catering itinerante por CCAA?", "acceptedAnswer": { "@type": "Answer", "text": "Anexo dedicado con resumen operativo de 17 CCAA: Registro Sanitario + RGSEAA, requisitos cocina cliente, normativa transporte alimentos, etiquetado bilingüe Cataluña/País Vasco, trámites telemáticos vs presenciales. Plus orientación específica APPCC multi-concepto." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio Catering Temático Eventos", "item": "https://aichef.pro/plan-catering-tematico-eventos" }
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
          subtitle="Sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche peruano, tandoor masters, plant-based premium y BBQ pitmasters que usaron el plan para montar o escalar su catering temático multi-concepto en España"
          testimonials={planCateringTematicoEventosTestimonials}
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
              <a href="/plan-chef-privado-showcooking-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Chef Privado / Showcooking</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/plan-negocio-paellero-eventos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Paellero Eventos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-catering-tematico-eventos" label="¿Ya compraste el Plan Catering Temático? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
