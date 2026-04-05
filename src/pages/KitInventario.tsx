import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-inventario/HeroSection';
import ContentGrid from '@/components/kit-inventario/ContentGrid';
import WhySection from '@/components/kit-inventario/WhySection';
import AuthorSection from '@/components/kit-inventario/AuthorSection';
import BonusSection from '@/components/kit-inventario/BonusSection';
import BuyBox from '@/components/kit-inventario/BuyBox';
import GuaranteeSection from '@/components/kit-inventario/GuaranteeSection';
import FaqAccordion from '@/components/kit-inventario/FaqAccordion';
import CtaFinal from '@/components/kit-inventario/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { inventarioTestimonials } from '@/data/testimonials-inventario';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-inventario/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitInventario() {
  return (
    <>
      <Helmet>
        <title>Kit Control de Inventario y Compras — Plantillas Excel para Hosteleria | AI Chef Pro</title>
        <meta name="description" content="9 plantillas Excel con formulas automaticas para controlar inventario, proveedores, pedidos, mermas, FIFO y costes de compras en hosteleria. Solo 14 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="control inventario restaurante, gestion compras hosteleria, plantilla mermas excel, control stock cocina, fifo restaurante, proveedores hosteleria, food cost control, pedidos compra restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-inventario" />
        <meta property="og:title" content="Kit Control de Inventario y Compras — Plantillas Excel para Hosteleria" />
        <meta property="og:description" content="9 plantillas Excel: inventario, proveedores, pedidos, mermas, FIFO, costes. 14 EUR." />
        <meta property="og:url" content="https://aichef.pro/kit-inventario" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-inventario.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit Control de Inventario y Compras — Plantillas para Hosteleria" />
        <meta name="twitter:description" content="Plantillas Excel profesionales para controlar inventario y compras en hosteleria. 14 EUR." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit Control de Inventario y Compras — Plantillas Excel para Hosteleria",
          "description": "9 plantillas Excel con formulas automaticas para controlar inventario, proveedores, pedidos, mermas, FIFO y costes de compras en hosteleria.",
          "image": "https://aichef.pro/og-kit-inventario.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-inventario",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Miguel Fernandez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El control de mermas fue revelador. Descubrimos que perdiamos 400 EUR/mes solo en verdura mal almacenada." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Laura Martinez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La comparativa de proveedores nos ahorro mas de 2.000 EUR el primer trimestre." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Elena Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Es el kit mas completo que he visto en espanol: desde el inventario diario hasta el analisis de costes con dashboard." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Sirve para cualquier tipo de restaurante?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Las categorias estan pre-cargadas para hosteleria: carnicos, pescados, lacteos, verduras, secos, congelados, bebidas, limpieza." }},
            { "@type": "Question", "name": "¿Las plantillas se conectan entre si?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Los niveles de stock alimentan las sugerencias de pedido. Las fichas de proveedores se enlazan con los pedidos de compra." }},
            { "@type": "Question", "name": "¿Cumple con los requisitos de APPCC?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Incluye control de temperaturas en recepcion, trazabilidad FIFO y registro de caducidades con alertas por colores." }},
            { "@type": "Question", "name": "¿Hay garantia de devolucion?", "acceptedAnswer": { "@type": "Answer", "text": "30 dias de garantia completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit Control de Inventario y Compras", "item": "https://aichef.pro/kit-inventario" }
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
          subtitle="Jefes de cocina, gerentes y directores de operaciones que ya controlan su inventario con estas plantillas"
          testimonials={inventarioTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-gestion-personal" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Gestion Personal</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-inventario" label="¿Ya compraste el Kit de Inventario? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
