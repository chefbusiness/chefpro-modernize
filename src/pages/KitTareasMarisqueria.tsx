import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-marisqueria/HeroSection';
import ContentGrid from '@/components/kit-tareas-marisqueria/ContentGrid';
import WhySection from '@/components/kit-tareas-marisqueria/WhySection';
import AuthorSection from '@/components/kit-tareas-marisqueria/AuthorSection';
import BonusSection from '@/components/kit-tareas-marisqueria/BonusSection';
import BuyBox from '@/components/kit-tareas-marisqueria/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-marisqueria/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-marisqueria/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-marisqueria/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { marisqueriaTestimonials } from '@/data/testimonials-marisqueria';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-marisqueria/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasMarisqueria() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC — Checklists Operativos | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para marisquería y restaurante de pescado: control del vivero (oxígeno, salinidad, temperatura), expositor de hielo, trazabilidad APPCC, alérgenos de crustáceos y moluscos, lonjas y temporadas de pesca de España. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist marisquería, tareas marisquería, control vivero marisco, trazabilidad APPCC pescado, alérgenos crustáceos moluscos, expositor hielo marisco, temporadas pesca España, vedas marisco, restaurante de pescado, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-marisqueria" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC" />
        <meta property="og:description" content="11 checklists operativos para marisquería: vivero, expositor, trazabilidad APPCC, lonjas y temporadas de pesca. €14." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-marisqueria" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-marisqueria.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC" />
        <meta name="twitter:description" content="11 checklists operativos para marisquería. Vivero, expositor, APPCC, lonjas. €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-marisqueria.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC — Checklists Operativos",
          "description": "11 checklists operativos pre-rellenados para marisquería y restaurante de pescado: control del vivero, expositor de hielo, trazabilidad APPCC, alérgenos de crustáceos y moluscos, lonjas y temporadas de pesca de España.",
          "image": "https://aichef.pro/og-kit-tareas-marisqueria.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-marisqueria",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists del vivero son muy completos. Temperatura, oxígeno, salinidad… todo el equipo sigue el mismo estándar cada mañana." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La trazabilidad APPCC con registro de lotes y alérgenos nos ha salvado en dos inspecciones de Sanidad. Imprescindible." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en 3 marisquerías. La consistencia en el control del expositor y la rotación FIFO es ahora uniforme." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye el control completo del vivero?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Temperatura del agua, oxígeno disuelto, salinidad, pH, densidad de carga, limpieza de filtros y control de mortalidad, con frecuencias y valores de referencia por especie." }},
            { "@type": "Question", "name": "¿Sirve para mi tipo de marisquería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cubre marisquería gallega tradicional, restaurante de pescado y marisco, marisquería con barra, locales con vivero propio y restaurantes costeros. 100% editable." }},
            { "@type": "Question", "name": "¿Cubre la trazabilidad obligatoria del marisco?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cumple con el Reglamento UE 1379/2013. Incluye registro de lotes, etiquetado obligatorio, zona FAO, método de captura y alérgenos de crustáceos y moluscos." }},
            { "@type": "Question", "name": "¿Las temporadas de pesca son de España?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Atlántico y Mediterráneo español: percebes, nécoras, centollos, gamba roja, langostinos, cigalas, bogavantes y mejillones, con calendario de vedas actualizado." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC", "item": "https://aichef.pro/kit-tareas-marisqueria" }
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
          subtitle="Mariscadores, propietarios de marisquería y consultores que ya tienen su operativa bajo control"
          testimonials={marisqueriaTestimonials}
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
            <AlreadyBought product="kit-tareas-marisqueria" label="¿Ya compraste el Kit de Tareas Marisquería? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
