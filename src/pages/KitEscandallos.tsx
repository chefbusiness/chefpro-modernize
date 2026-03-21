import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-escandallos/HeroSection';
import ContentGrid from '@/components/kit-escandallos/ContentGrid';
import WhySection from '@/components/kit-escandallos/WhySection';
import AuthorSection from '@/components/kit-escandallos/AuthorSection';
import BonusSection from '@/components/kit-escandallos/BonusSection';
import BuyBox from '@/components/kit-escandallos/BuyBox';
import GuaranteeSection from '@/components/kit-escandallos/GuaranteeSection';
import FaqAccordion from '@/components/kit-escandallos/FaqAccordion';
import CtaFinal from '@/components/kit-escandallos/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { escandallosTestimonials } from '@/data/testimonials-escandallos';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-escandallos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitEscandallos() {
  return (
    <>
      <Helmet>
        <title>Kit de Escandallos Pro — 11 Plantillas Excel Profesionales | AI Chef Pro</title>
        <meta name="description" content="11 plantillas de escandallos con fórmulas automáticas, mermas precargadas y calculadora de PVP. Para chefs, gerentes y dueños de restaurante. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plantilla escandallo excel, calcular food cost restaurante, plantilla food cost excel, control costes restaurante, escandallo hostelería, calculadora PVP restaurante, mermas restaurante excel, escandallo pastelería, escandallo catering, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-escandallos" />

        {/* Open Graph */}
        <meta property="og:title" content="Kit de Escandallos Pro — 11 Plantillas Excel Profesionales" />
        <meta property="og:description" content="Controla tu food cost con 11 plantillas Excel profesionales. Fórmulas automáticas, mermas precargadas y calculadora de PVP. Solo €12." />
        <meta property="og:url" content="https://aichef.pro/kit-escandallos" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:secure_url" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="Kit de Escandallos Pro — 11 Plantillas Excel para hostelería" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Escandallos Pro — 11 Plantillas Excel" />
        <meta name="twitter:description" content="Plantillas Excel profesionales con fórmulas automáticas, mermas precargadas y calculadora de PVP. Solo €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-image.jpg" />
        <meta name="twitter:image:alt" content="Kit de Escandallos Pro — AI Chef Pro" />

        {/* Product Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Escandallos Pro — 11 Plantillas Excel Profesionales",
          "description": "11 plantillas de escandallos con fórmulas automáticas, mermas precargadas y calculadora de PVP. Para chefs, gerentes y dueños de restaurante.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-escandallos",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "10",
            "bestRating": "5",
            "worstRating": "1"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Alejandro Ruiz" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Antes hacía los escandallos en un cuaderno. Ahora con estas plantillas tengo el food cost de cada plato controlado al céntimo. He bajado del 35% al 28% en dos meses."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "María José Pérez" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestiono 4 restaurantes y estas plantillas me permiten estandarizar los escandallos en todos. El dashboard mensual es lo que más uso."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Antonio Delgado" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Uso el kit con todos mis clientes de consultoría. Es la herramienta más práctica que he encontrado para enseñar control de costes."
            }
          ]
        })}</script>

        {/* FAQPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Necesito Excel avanzado para usar las plantillas?", "acceptedAnswer": { "@type": "Answer", "text": "No. Las plantillas vienen con todo configurado: fórmulas, mermas, validaciones. Solo introduces tus ingredientes, cantidades y precios. Todo se calcula automáticamente." }},
            { "@type": "Question", "name": "¿Funcionan con Google Sheets?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers." }},
            { "@type": "Question", "name": "¿Los datos de merma son fiables?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Son los estándares utilizados en hostelería profesional y en consultoría gastronómica. Cubren 16 categorías de ingredientes con mermas mínimas, máximas y típicas." }},
            { "@type": "Question", "name": "¿Puedo personalizar las plantillas?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. Puedes añadir ingredientes, modificar precios, ajustar mermas, cambiar el food cost objetivo y añadir tus propias fotos de platos." }},
            { "@type": "Question", "name": "¿Incluye actualizaciones futuras?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Tienes acceso de por vida al dashboard online. Cuando añadamos nuevas plantillas o mejoras, las recibirás sin coste adicional." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. 30 días de garantía completa. Si las plantillas no te ayudan a controlar tu food cost, te devolvemos el 100% sin hacer ninguna pregunta." }}
          ]
        })}</script>

        {/* BreadcrumbList Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Escandallos Pro", "item": "https://aichef.pro/kit-escandallos" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <CompatibleAppsMarquee variant="kit" />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Profesionales de la hostelería que ya controlan su food cost con el Kit de Escandallos Pro"
          testimonials={escandallosTestimonials}
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
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="kit-escandallos"
              label="¿Ya compraste el Kit? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
