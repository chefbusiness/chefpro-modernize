import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-asador/HeroSection';
import ContentGrid from '@/components/kit-tareas-asador/ContentGrid';
import WhySection from '@/components/kit-tareas-asador/WhySection';
import AuthorSection from '@/components/kit-tareas-asador/AuthorSection';
import BonusSection from '@/components/kit-tareas-asador/BonusSection';
import BuyBox from '@/components/kit-tareas-asador/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-asador/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-asador/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-asador/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { asadorTestimonials } from '@/data/testimonials-asador';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-asador/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasAsador() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper — Checklists Operativos | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para asador y parrilla con horno Josper: encendido brasas, protocolo Josper, maduración y despiece de carne, temperaturas por corte, pescados y verduras a la brasa. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist asador, tareas asador, protocolo Josper, horno Josper restaurante, maduración dry-age, despiece carne, temperaturas corte chuletón, parrilla profesional, steakhouse operativa, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-asador" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper" />
        <meta property="og:description" content="11 checklists operativos para asador y parrilla Josper: encendido brasas, maduración, despiece, temperaturas por corte. €14." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-asador" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-asador.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper" />
        <meta name="twitter:description" content="11 checklists operativos para asador y parrilla Josper. Maduración, brasas, cortes. €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-asador.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper — Checklists Operativos",
          "description": "11 checklists operativos pre-rellenados para asador y parrilla con horno Josper: encendido y mantenimiento de brasas, maduración dry-age y despiece, temperaturas por corte, pescados y verduras a la brasa, eventos y temporadas.",
          "image": "https://aichef.pro/og-kit-tareas-asador.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-asador",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists del Josper son muy completos. Encendido, zonas de calor, regulación de compuertas, gestión del carbón… todo el equipo sigue el mismo protocolo." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El control de maduración y temperaturas por corte ha elevado la calidad de nuestras carnes. Los clientes lo notan." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en 3 asadores. La consistencia en puntos de cocción y presentación es ahora uniforme en todos." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye el protocolo del horno Josper?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Encendido, precalentamiento, zonas de calor, tipos de carbón, regulación de compuertas, mantenimiento semanal y limpieza profunda anual." }},
            { "@type": "Question", "name": "¿Sirve para mi tipo de asador?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cubre asador tradicional, steakhouse, parrilla argentina, gastrobar con Josper y cualquier local con cocina a las brasas. 100% editable." }},
            { "@type": "Question", "name": "¿Incluye control de maduración de carne?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Fichas dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara y cálculo de mermas reales." }},
            { "@type": "Question", "name": "¿Qué cortes y puntos de cocción incluye?", "acceptedAnswer": { "@type": "Answer", "text": "Chuletón, entrecot, tomahawk, costillar, hamburguesa. Con temperaturas internas para blue, rare, medium rare, medium, medium well y well done." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper", "item": "https://aichef.pro/kit-tareas-asador" }
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
          subtitle="Parrilleros, propietarios de asador y consultores que ya tienen su operativa bajo control"
          testimonials={asadorTestimonials}
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
              <a href="/kit-tareas" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Restaurante</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-tareas-chef-privado" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Chef Privado</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-asador" label="¿Ya compraste el Kit de Tareas Asador? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
