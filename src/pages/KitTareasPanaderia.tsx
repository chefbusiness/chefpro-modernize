import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-panaderia/HeroSection';
import ContentGrid from '@/components/kit-tareas-panaderia/ContentGrid';
import WhySection from '@/components/kit-tareas-panaderia/WhySection';
import AuthorSection from '@/components/kit-tareas-panaderia/AuthorSection';
import BonusSection from '@/components/kit-tareas-panaderia/BonusSection';
import BuyBox from '@/components/kit-tareas-panaderia/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-panaderia/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-panaderia/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-panaderia/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { panaderiaTestimonials } from '@/data/testimonials-panaderia';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-panaderia/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasPanaderia() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes: Panadería / Obrador — Checklists con Masas Madre, Hornos y Turno Madrugada | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos para panadería y obrador: turno madrugada, masas madre y fermentación, hornos y cocción, expositor, perfiles del equipo, temporadas y calendario anual. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist panadería, tareas obrador, masas madre, pre-fermentos poolish biga, hornos panadería, turno madrugada panadería, expositor panadería, calendario anual panadería, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-panaderia" />
        <meta property="og:title" content="Kit de Tareas Recurrentes: Panadería / Obrador" />
        <meta property="og:description" content="11 checklists operativos para panadería: turno madrugada, masas madre, hornos, expositor y calendario anual. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-panaderia" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-panaderia.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes: Panadería / Obrador" />
        <meta name="twitter:description" content="11 checklists operativos para panadería: turno madrugada, masas madre, hornos, expositor y calendario anual. €12." />
        <meta name="twitter:image" content="https://aichef.pro/og-kit-tareas-panaderia.jpg" />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes: Panadería / Obrador — Checklists Operativos",
          "description": "11 checklists operativos pre-rellenados para panadería y obrador: turno madrugada, masas madre y pre-fermentos, hornos y cocción, expositor y venta, tareas del manager, perfiles del equipo, semanales y mensuales, eventos y temporadas, plantilla personalizable, briefing de producción diaria y calendario anual.",
          "image": "https://aichef.pro/og-kit-tareas-panaderia.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-panaderia",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alejandro Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Los checklists de turno madrugada son imprescindibles. Encendido de hornos, masas del día, fermentaciones… todo el equipo sigue el mismo protocolo desde las 03:00." },
            { "@type": "Review", "author": { "@type": "Person", "name": "María López" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El control de masas madre y pre-fermentos nos salvó. Cada refresco, cada poolish y cada biga está documentado con temperaturas y tiempos exactos." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carlos Méndez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Implementamos en 4 obradores. La consistencia en hornos, fermentaciones y producción es ahora uniforme en todas las tiendas." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye control de masas madre y pre-fermentos?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Control completo de masa madre natural: refresco, temperatura, hidratación y tiempos de fermentación. También pre-fermentos como poolish, biga y esponja, con registros de actividad y protocolos de recuperación si la masa pierde fuerza." }},
            { "@type": "Question", "name": "¿Cómo gestiona el turno de madrugada?", "acceptedAnswer": { "@type": "Answer", "text": "Checklist completo desde las 03:00: encendido y precalentamiento de hornos, preparación de masas del día, división y formado, control de fermentación en cámara y a temperatura ambiente, primera hornada y apertura de tienda." }},
            { "@type": "Question", "name": "¿Cubre diferentes tipos de horno?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Protocolos para horno de piso (solera refractaria), horno rotativo y horno de convección con vapor. Incluye temperaturas, tiempos de cocción, uso de vapor, grenado y carga óptima para cada tipo de pan y bollería." }},
            { "@type": "Question", "name": "¿Sirve también para bollería y panes especiales?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Además del pan básico, cubre bollería fermentada (croissants, brioches, ensaimadas), panes especiales (centeno, espelta, semillas), panes de temporada y productos de pastelería de obrador." }},
            { "@type": "Question", "name": "¿Funcionan en Google Sheets?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Compatibles con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días. Si no estás satisfecho, devolución 100% sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Panadería / Obrador", "item": "https://aichef.pro/kit-tareas-panaderia" }
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
          subtitle="Maestros panaderos, oficiales de obrador y consultores de panificación que ya tienen su producción bajo control"
          testimonials={panaderiaTestimonials}
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
              <a href="/kit-tareas-pasteleria" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Tareas Pastelería</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-panaderia" label="¿Ya compraste el Kit de Tareas Panadería? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
