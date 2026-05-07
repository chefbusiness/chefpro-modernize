import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-tapas-bar/HeroSection';
import ContentGrid from '@/components/kit-tareas-tapas-bar/ContentGrid';
import WhySection from '@/components/kit-tareas-tapas-bar/WhySection';
import AuthorSection from '@/components/kit-tareas-tapas-bar/AuthorSection';
import BonusSection from '@/components/kit-tareas-tapas-bar/BonusSection';
import BuyBox from '@/components/kit-tareas-tapas-bar/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-tapas-bar/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-tapas-bar/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-tapas-bar/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { tapasBarTestimonials } from '@/data/testimonials-tapas-bar';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-tapas-bar/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasTapasBar() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Tapas Bar / Gastrobar — Checklists Operativos | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones, cerveza de grifo, vinos por copa, vermut, rotación de carta, terraza, perfiles y eventos. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist tapas bar, tareas gastrobar, control cerveza grifo, barra de pinchos, cocina raciones, terraza tapas, vermut, vinos por copa, rotación carta tapas, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-tapas-bar" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Tapas Bar / Gastrobar" />
        <meta property="og:description" content="11 checklists operativos para tapas bar y gastrobar. Barra, cocina raciones, cerveza grifo, vermut, terraza. €14." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-tapas-bar" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-tapas-bar.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Tapas Bar / Gastrobar" />
        <meta name="twitter:description" content="11 checklists operativos para tapas bar y gastrobar. Barra, cocina raciones, cerveza grifo, terraza. €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-tapas-bar.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Tapas Bar / Gastrobar — Checklists Operativos",
          "description": "11 checklists operativos pre-rellenados para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones, cerveza de grifo, vinos por copa y vermut, rotación de carta, terraza, perfiles y eventos.",
          "image": "https://aichef.pro/og-kit-tareas-tapas-bar.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-tapas-bar",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de barra de pinchos y cocina de raciones son muy completos. Plancha, freidora, guisos, cazuelas… todo el equipo sigue el mismo estándar cada turno." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La rotación de la vitrina de tapas con FIFO y el control de mermas en barra nos ha reducido el desperdicio a la mitad. Imprescindible para cualquier tapas bar." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en los 3 locales. La consistencia en el montaje de pinchos y la pizarra de tapas del día es ahora uniforme en todos." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Sirve para un gastrobar moderno?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cubre desde tapas bar clásico hasta gastrobar contemporáneo con cocina de autor en formato tapa. Tapas tradicionales, pinchos, raciones, medias raciones y propuestas creativas. Todo es editable y adaptable a tu formato." }},
            { "@type": "Question", "name": "¿Incluye control de cerveza de grifo?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Control completo de grifos: presión, CO2, temperatura, purga diaria, limpieza de líneas semanal, rotación de barriles y control de mermas. Todo con frecuencias y valores de referencia." }},
            { "@type": "Question", "name": "¿Cubre la terraza?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Apertura y cierre de terraza, montaje de mesas y sillas, limpieza, eventos en terraza, control de stock terraza y protocolo de cierre por climatología." }},
            { "@type": "Question", "name": "¿Incluye rotación de carta estacional?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. El calendario anual incluye tapas por temporada (gazpacho en verano, guisos en invierno, setas en otoño…), eventos gastronómicos, rutas de tapas y fechas clave para planificar la carta." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Tapas Bar / Gastrobar", "item": "https://aichef.pro/kit-tareas-tapas-bar" }
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
          subtitle="Hosteleros, jefes de cocina y consultores que ya tienen su tapas bar o gastrobar bajo control"
          testimonials={tapasBarTestimonials}
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
              <a href="/kit-tareas-bar" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Bar / Cocktails</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-tapas-bar" label="¿Ya compraste el Kit de Tareas Tapas Bar? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
