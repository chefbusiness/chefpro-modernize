import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-sushi-bar/HeroSection';
import ContentGrid from '@/components/kit-tareas-sushi-bar/ContentGrid';
import WhySection from '@/components/kit-tareas-sushi-bar/WhySection';
import AuthorSection from '@/components/kit-tareas-sushi-bar/AuthorSection';
import BonusSection from '@/components/kit-tareas-sushi-bar/BonusSection';
import BuyBox from '@/components/kit-tareas-sushi-bar/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-sushi-bar/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-sushi-bar/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-sushi-bar/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { sushiBarTestimonials } from '@/data/testimonials-sushi-bar';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-sushi-bar/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasSushiBar() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Sushi Bar — Checklists Operativos con Protocolo Anisakis | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para sushi bar: barra sushi, arroz con control pH, protocolo anisakis APPCC obligatorio (RD 1420/2006), vitrina neta case, perfiles itamae, temporadas pescado y omakase. Solo €14." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist sushi bar, tareas sushi bar, protocolo anisakis APPCC, control pH arroz sushi, vitrina neta case, itamae checklist, restaurante japonés operativa, RD 1420/2006, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-sushi-bar" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Sushi Bar — Protocolo Anisakis APPCC" />
        <meta property="og:description" content="11 checklists operativos para sushi bar con protocolo anisakis APPCC. Arroz con pH, neta case, itamae, omakase. €14." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-sushi-bar" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-sushi-bar.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Sushi Bar — Protocolo Anisakis APPCC" />
        <meta name="twitter:description" content="11 checklists operativos para sushi bar con protocolo anisakis APPCC. €14." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-sushi-bar.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Sushi Bar — Checklists Operativos con Protocolo Anisakis",
          "description": "11 checklists operativos pre-rellenados para sushi bar: barra sushi, preparación arroz con control pH, protocolo anisakis APPCC obligatorio, vitrina neta case, perfiles itamae, temporadas pescado y omakase.",
          "image": "https://aichef.pro/og-kit-tareas-sushi-bar.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-sushi-bar",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de barra sushi son muy completos. Neta case, arroz, cuchillería japonesa, rotación FIFO… todo el equipo sigue el mismo estándar." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El protocolo de anisakis con registro de congelación a -20 ºC durante 7 días nos ha salvado en dos inspecciones de Sanidad. Imprescindible." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en 3 locales. La consistencia en preparación de arroz (control pH ≤4.6) y corte de pescado es ahora uniforme." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye el protocolo de anisakis obligatorio por ley?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Registro de congelación a -20 ºC durante 7 días por lote y proveedor, control de temperaturas y trazabilidad completa del pescado. Cumple con el RD 1420/2006." }},
            { "@type": "Question", "name": "¿Sirve para mi tipo de restaurante japonés?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Sushi bar tradicional, japonés con cocina caliente, nikkei, kaiten, omakase y cualquier local que sirva pescado crudo. 100% editable." }},
            { "@type": "Question", "name": "¿Incluye preparación de arroz sushi profesional?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Lavado, cocción, sazonado con sushi-zu, control de pH obligatorio (≤4.6), tiempos de descarte y temperaturas de servicio." }},
            { "@type": "Question", "name": "¿Qué es la vitrina neta case?", "acceptedAnswer": { "@type": "Answer", "text": "La vitrina refrigerada de la barra de sushi (2-4 ºC). El kit incluye montaje, rotación FIFO y exposición máxima de 2 horas." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Sushi Bar", "item": "https://aichef.pro/kit-tareas-sushi-bar" }
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
          subtitle="Itamaes, propietarios de sushi bar y consultores que ya tienen su operativa bajo control"
          testimonials={sushiBarTestimonials}
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
            <AlreadyBought product="kit-tareas-sushi-bar" label="¿Ya compraste el Kit de Tareas Sushi Bar? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
