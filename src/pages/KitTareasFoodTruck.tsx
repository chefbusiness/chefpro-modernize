import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-food-truck/HeroSection';
import ContentGrid from '@/components/kit-tareas-food-truck/ContentGrid';
import WhySection from '@/components/kit-tareas-food-truck/WhySection';
import AuthorSection from '@/components/kit-tareas-food-truck/AuthorSection';
import BonusSection from '@/components/kit-tareas-food-truck/BonusSection';
import BuyBox from '@/components/kit-tareas-food-truck/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-food-truck/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-food-truck/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-food-truck/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { foodTruckTestimonials } from '@/data/testimonials-food-truck';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-food-truck/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasFoodTruck() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Food Truck — Checklists Operativos con Setup, APPCC Móvil y Permisos | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para food truck: setup y teardown, operaciones móviles, APPCC seguridad alimentaria móvil, permisos y eventos, perfiles, temporadas y calendario anual. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist food truck, tareas cocina móvil, setup teardown food truck, APPCC móvil, permisos food truck, eventos food truck, generador food truck, calendario anual food truck, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-food-truck" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Food Truck" />
        <meta property="og:description" content="11 checklists operativos para food truck. Setup, teardown, APPCC móvil, permisos, eventos y calendario anual. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-food-truck" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-food-truck.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Food Truck" />
        <meta name="twitter:description" content="11 checklists operativos para food truck. Setup, APPCC móvil, permisos, eventos. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-food-truck.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Food Truck — Checklists Operativos",
          "description": "11 checklists operativos pre-rellenados para food truck: setup y teardown, operaciones móviles y vehículo, APPCC seguridad alimentaria móvil, permisos y licencias, gestión de eventos, perfiles y calendario anual.",
          "image": "https://aichef.pro/og-kit-tareas-food-truck.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-food-truck",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de setup y teardown son imprescindibles. Montaje del generador, gas, cocina… todo el equipo sigue el mismo protocolo en cada evento." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El APPCC móvil nos salvó en la última inspección. Temperaturas, cadena de frío, documentación… todo al día y listo para mostrar." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en 3 trucks. La consistencia en operaciones móviles y el control del vehículo es ahora uniforme en toda la flota." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye gestión de permisos y licencias?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Control completo de permisos municipales, licencias de actividad, seguros de responsabilidad civil, certificados de manipulador y documentación sanitaria, con checklist pre-evento para verificar que toda la documentación está en regla antes de cada localización." }},
            { "@type": "Question", "name": "¿Cómo funciona el APPCC móvil?", "acceptedAnswer": { "@type": "Answer", "text": "Adaptado específicamente para cocinas móviles: control de temperaturas en condiciones variables, cadena de frío durante transporte, manipulación de alimentos en espacios reducidos, gestión de alérgenos y toda la documentación que exige sanidad para food trucks." }},
            { "@type": "Question", "name": "¿Cubre el mantenimiento del generador?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Checklist completo de generador: nivel de combustible, aceite, arranque, potencia, conexiones eléctricas, mantenimiento preventivo y protocolo de emergencia, tanto en tareas diarias como en revisiones semanales y mensuales." }},
            { "@type": "Question", "name": "¿Sirve para diferentes tipos de evento?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cubre festivales de música, bodas, eventos corporativos, mercados gastronómicos, ferias, fiestas patronales y eventos privados. Cada tipo tiene sus particularidades en logística, menú, stock y equipo necesario." }},
            { "@type": "Question", "name": "¿Funcionan en Google Sheets?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Compatibles con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días. Si no estás satisfecho, devolución 100% sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Food Truck", "item": "https://aichef.pro/kit-tareas-food-truck" }
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
          subtitle="Operadores de food trucks, chefs de cocina móvil y consultores de street food que ya tienen sus operaciones bajo control"
          testimonials={foodTruckTestimonials}
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
            <AlreadyBought product="kit-tareas-food-truck" label="¿Ya compraste el Kit de Tareas Food Truck? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
