import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/plan-negocio-food-truck/HeroSection';
import ContentGrid from '@/components/plan-negocio-food-truck/ContentGrid';
import WhySection from '@/components/plan-negocio-food-truck/WhySection';
import AuthorSection from '@/components/plan-negocio-food-truck/AuthorSection';
import BonusSection from '@/components/plan-negocio-food-truck/BonusSection';
import BuyBox from '@/components/plan-negocio-food-truck/BuyBox';
import GuaranteeSection from '@/components/plan-negocio-food-truck/GuaranteeSection';
import FaqAccordion from '@/components/plan-negocio-food-truck/FaqAccordion';
import CtaFinal from '@/components/plan-negocio-food-truck/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { planFoodTruckTestimonials } from '@/data/testimonials-plan-food-truck';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/plan-negocio-food-truck/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PlanNegocioFoodTruck() {
  return (
    <>
      <Helmet>
        <title>Plan de Negocio: Food Truck — Plan Financiero Excel + DOCX + Checklist Apertura | AI Chef Pro</title>
        <meta name="description" content="Plan de negocio completo para montar un food truck en España 2026. Documento DOCX 10 secciones + plan financiero Excel con P&L 3 años + checklist apertura con 59 trámites incluyendo licencia venta ambulante e ITV vehículo adaptado. €29." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plan de negocio food truck, plan financiero food truck España, montar food truck, licencia venta ambulante, ITV vehículo adaptado, street food España, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/plan-negocio-food-truck" />
        <meta property="og:title" content="Plan de Negocio: Food Truck — Plan Financiero + DOCX + Checklist 59 trámites" />
        <meta property="og:description" content="DOCX 10 secciones + Excel P&L 3 años + checklist apertura 59 trámites para montar tu food truck en España. €29." />
        <meta property="og:url" content="https://aichef.pro/plan-negocio-food-truck" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-plan-negocio-food-truck.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Plan de Negocio: Food Truck — DOCX + Excel + Checklist Apertura" />
        <meta name="twitter:description" content="Plan profesional para montar un food truck en España con bajo riesgo. €29." />
        <meta name="twitter:image" content="https://aichef.pro/og-plan-negocio-food-truck.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Plan de Negocio: Food Truck — Plan Financiero Excel, Inversión Inicial y Checklist Apertura",
          "description": "Plan de negocio completo para montar un food truck en España. Incluye documento DOCX de 10 secciones, plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada (~62K EUR), punto de equilibrio en 27 clientes/día con ticket €12, escenarios financieros, cuadro de personal, checklist de apertura con 59 trámites incluyendo licencia de venta ambulante, ITV vehículo adaptado y autorización sanitaria RGSEAA, equipamiento cocina móvil y guía de permisos por CCAA.",
          "image": "https://aichef.pro/og-plan-negocio-food-truck.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/plan-negocio-food-truck",
            "priceCurrency": "EUR",
            "price": "29.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Presenté el plan financiero al banco y me aprobaron el microcrédito en 2 semanas. Inversión total: 62K EUR." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de apertura con 59 trámites me salvó meses de trabajo. Permisos municipales, ITV vehículo, venta ambulante." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "27 clientes/día a €12 de ticket medio cubre costes. La inversión es mucho menor que un restaurante y el retorno más rápido." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Qué permisos necesito para operar un food truck en España?", "acceptedAnswer": { "@type": "Answer", "text": "Licencia de venta ambulante, autorización sanitaria RGSEAA, ITV del vehículo adaptado, alta en Hacienda (modelo 036/037), seguro de responsabilidad civil y permiso de ocupación de vía pública. El checklist incluye los 59 trámites organizados por fases y por CCAA." }},
            { "@type": "Question", "name": "¿Cuánto cuesta montar un food truck en España?", "acceptedAnswer": { "@type": "Answer", "text": "Entre 45K y 85K EUR según vehículo nuevo o segunda mano, equipamiento de cocina y permisos municipales. El plan financiero Excel desglosa todas las partidas." }},
            { "@type": "Question", "name": "¿Puedo presentar este plan al banco o a inversores?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Incluye P&L 3 años, punto de equilibrio y 3 escenarios. Es el formato profesional que piden bancos y entidades como ICO emprendedores o ENISA." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Plan de Negocio: Food Truck", "item": "https://aichef.pro/plan-negocio-food-truck" }
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
          subtitle="Propietarios de food trucks, flotas de gastro móvil e inversores que montaron su negocio con un plan financiero profesional"
          testimonials={planFoodTruckTestimonials}
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
              <a href="/kit-tareas-food-truck" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Food Truck</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="plan-negocio-food-truck" label="¿Ya compraste el Plan de Negocio Food Truck? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
