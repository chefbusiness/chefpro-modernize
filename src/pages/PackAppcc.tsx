import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/pack-appcc/HeroSection';
import ContentGrid from '@/components/pack-appcc/ContentGrid';
import WhySection from '@/components/pack-appcc/WhySection';
import AuthorSection from '@/components/pack-appcc/AuthorSection';
import BonusSection from '@/components/pack-appcc/BonusSection';
import BuyBox from '@/components/pack-appcc/BuyBox';
import GuaranteeSection from '@/components/pack-appcc/GuaranteeSection';
import FaqAccordion from '@/components/pack-appcc/FaqAccordion';
import CtaFinal from '@/components/pack-appcc/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { appccTestimonials } from '@/data/testimonials-appcc';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/pack-appcc/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function PackAppcc() {
  return (
    <>
      <Helmet>
        <title>Pack Plantillas APPCC — 17 Registros de Seguridad Alimentaria | AI Chef Pro</title>
        <meta name="description" content="17 plantillas APPCC profesionales para restaurantes: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP. Obligatorio por ley. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="plantillas APPCC restaurante, registros APPCC hostelería, control temperaturas restaurante, carta alergenos obligatoria, registro limpieza restaurante, inspección sanidad restaurante, HACCP hostelería, trazabilidad restaurante, control plagas restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/pack-appcc" />

        {/* Open Graph */}
        <meta property="og:title" content="Pack Plantillas APPCC — 17 Registros de Seguridad Alimentaria" />
        <meta property="og:description" content="Pasa la inspección de Sanidad con nota. 17 plantillas profesionales con fórmulas y alertas automáticas. Solo €14." />
        <meta property="og:url" content="https://aichef.pro/pack-appcc" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-pack-appcc.jpg" />
        <meta property="og:image:secure_url" content="https://aichef.pro/og-pack-appcc.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="Pack de Plantillas APPCC — Seguridad alimentaria para hostelería" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Pack Plantillas APPCC — 17 Registros Profesionales" />
        <meta name="twitter:description" content="Plantillas APPCC profesionales: temperaturas, limpieza, alérgenos, HACCP. Obligatorio por ley. Solo €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-pack-appcc.jpg" />
        <meta name="twitter:image:alt" content="Pack de Plantillas APPCC — AI Chef Pro" />

        {/* Product Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Pack de Plantillas APPCC — 17 Registros de Seguridad Alimentaria",
          "description": "17 plantillas profesionales de seguridad alimentaria para hostelería: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP, control de plagas. Obligatorio por ley en España.",
          "image": "https://aichef.pro/og-pack-appcc.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/pack-appcc",
            "priceCurrency": "EUR",
            "price": "14.00",
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
              "author": { "@type": "Person", "name": "Carlos Moreno" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Pasamos la inspección de Sanidad sin una sola incidencia. Las plantillas cubren todo lo que pide el inspector."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Laura García" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Gestiono 3 hoteles y estas plantillas me permiten estandarizar los registros APPCC en todos. Imprescindible."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Miguel Torres" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Antes usaba hojas fotocopiadas de hace 10 años. Ahora tengo registros profesionales con alertas automáticas."
            }
          ]
        })}</script>

        {/* FAQPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Necesito conocimientos técnicos para usar las plantillas?", "acceptedAnswer": { "@type": "Answer", "text": "No. Todo viene pre-rellenado con datos reales de hostelería. Solo tienes que personalizar con los datos de tu establecimiento." }},
            { "@type": "Question", "name": "¿Estas plantillas sirven para pasar la inspección de Sanidad?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cubren todos los registros que exige la normativa APPCC en España: temperaturas, limpieza, trazabilidad, alérgenos, HACCP, control de plagas, aceite y agua." }},
            { "@type": "Question", "name": "¿Funcionan con Google Sheets?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers." }},
            { "@type": "Question", "name": "¿Puedo personalizar las plantillas para mi restaurante?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. Puedes añadir zonas de limpieza, equipos de frío, platos a la matriz de alérgenos, peligros al análisis HACCP. Las celdas editables están marcadas en verde." }},
            { "@type": "Question", "name": "¿Incluye actualizaciones si cambia la normativa?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Tienes acceso de por vida al dashboard online. Si hay cambios en la normativa APPCC, actualizaremos las plantillas sin coste adicional." }},
            { "@type": "Question", "name": "¿Para qué tipo de establecimiento sirven?", "acceptedAnswer": { "@type": "Answer", "text": "Para cualquier negocio de hostelería: restaurantes, bares, cafeterías, hoteles, catering, obradores, food trucks, comedores colectivos." }}
          ]
        })}</script>

        {/* BreadcrumbList Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Pack Plantillas APPCC", "item": "https://aichef.pro/pack-appcc" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <CompatibleAppsMarquee variant="appcc" />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Hosteleros que ya tienen sus registros APPCC al día con el Pack de Plantillas"
          testimonials={appccTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit de Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought
              product="pack-appcc"
              label="¿Ya compraste el Pack APPCC? Vuelve a entrar al dashboard"
            />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
