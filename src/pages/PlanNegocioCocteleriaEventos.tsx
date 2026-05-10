import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-cocteleria-eventos/HeroSection';
import ContentGrid from '@/components/plan-negocio-cocteleria-eventos/ContentGrid';
import WhySection from '@/components/plan-negocio-cocteleria-eventos/WhySection';
import AuthorSection from '@/components/plan-negocio-cocteleria-eventos/AuthorSection';
import BonusSection from '@/components/plan-negocio-cocteleria-eventos/BonusSection';
import BuyBox from '@/components/plan-negocio-cocteleria-eventos/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-cocteleria-eventos/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-cocteleria-eventos/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-cocteleria-eventos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planCocteleriaEventosTestimonials } from '@/data/testimonials-plan-cocteleria-eventos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-cocteleria-eventos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioCocteleriaEventos() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio &amp; Kit Coctelería de Eventos / Barra Móvil — 9 Entregables | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio + kit profesional completo para montar tu empresa de coctelería itinerante con barra móvil en España 2026. 9 entregables: DOCX 10 secciones + Plan Financiero Excel + 96 proveedores + Catálogo equipamiento + 15 cocktails + 10 experiencias + Modelo contrato + Checklist 71 trámites. Inversión 18-35K EUR. €55." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio coctelería eventos, barra móvil bodas, empresa coctelería itinerante, montar barra móvil, plan financiero coctelería, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-cocteleria-eventos" />
        <meta property="og:title" content="Plan de Negocio Coctelería de Eventos / Barra Móvil — 9 Entregables" />
        <meta property="og:description" content="Kit profesional completo para montar tu empresa de coctelería itinerante en España 2026. 9 entregables, 96 proveedores, 71 trámites, inversión 18-35K EUR. €55." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-cocteleria-eventos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-cocteleria-eventos.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio Coctelería de Eventos — 9 Entregables" />
        <meta name="twitter:description" content="Kit profesional completo para montar tu barra móvil de coctelería en España. 9 entregables. €55." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-cocteleria-eventos.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio & Kit de Coctelería de Eventos / Barra Móvil — 9 Entregables",
          "description": "Plan de negocio + kit profesional completo para montar una empresa de coctelería itinerante con barra móvil en España 2026. Incluye DOCX 10 secciones, Plan Financiero Excel con estacionalidad de eventos, Calculadora Pricing, plantilla de 96 proveedores reales, catálogo de equipamiento (GGM/Mewindo/Deus), carta de 15 cocktails temáticos, modelo de contrato profesional, 10 experiencias temáticas premium y checklist de apertura con 71 trámites adaptado al modelo itinerante.",
          "image": "https://aichef.pro/og-plan-negocio-cocteleria-eventos.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-cocteleria-eventos",
            "priceCurrency": "EUR",
            "price": "55.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Nadia y Lidia" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Buscábamos un plan específico para nuestro modelo de barra móvil con experiencias temáticas y este es exactamente lo que necesitábamos. Las 10 experiencias y los proveedores nos han ahorrado meses de investigación." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Vela" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Ojalá hubiera tenido este plan cuando arranqué hace dos años. La calculadora de pricing es oro: ahora cobro lo que vale realmente cada evento, no lo que me parecía." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Laura Manchón" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Recomiendo este plan a TODOS los proveedores de coctelería que entran en mi red. La plantilla de proveedores y el modelo de contrato les ahorran 40 horas de trabajo administrativo." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Es válido si nunca he montado una empresa de eventos antes?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye desde la constitución como autónomo hasta los primeros 90 días de operación. El checklist de 71 trámites en 6 fases no deja nada al azar." }},
            { "@type": "Question", "name": "¿Qué diferencia hay con un Plan de Negocio para un bar fijo?", "acceptedAnswer": { "@type": "Answer", "text": "Modelo itinerante: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija (bartenders freelance), inversión 4-7x menor, ingresos por evento, estacionalidad agresiva (60-70 % facturación mayo-septiembre + diciembre), captación B2B intensiva con wedding planners." }},
            { "@type": "Question", "name": "¿La plantilla de 96 proveedores incluye contactos reales?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada proveedor lleva web/contacto, cobertura, precio orientativo y plazo. Distribuidores oficiales como Damm (Fever-Tree), Disbesa (Schweppes HORECA), Latin Hotel (Spiegelau) y SERHS Equipments (Hoshizaki)." }},
            { "@type": "Question", "name": "¿Sirve para presentar al banco?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. El Plan Financiero Excel incluye P&L 3 años, punto de equilibrio (31 eventos/año break-even), escenarios pesimista/realista/optimista y cuadro de personal freelance. Formato ICO/microcrédito." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe. Los 9 entregables son tuyos para siempre + actualizaciones gratuitas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio Coctelería de Eventos", "item": "https://aichef.pro/plan-negocio-cocteleria-eventos" }
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
          subtitle="Bartenders, wedding planners y emprendedores que usaron el plan para montar o impulsar su empresa de coctelería de eventos"
          testimonials={planCocteleriaEventosTestimonials}
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
              <a href="/plan-negocio-food-truck" className="text-gray-500 hover:text-[#FFD700] transition-colors">Plan Food Truck</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-cocteleria-eventos" label="¿Ya compraste el Plan Coctelería de Eventos? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
