import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-bar/HeroSection';
import ContentGrid from '@/components/kit-tareas-bar/ContentGrid';
import WhySection from '@/components/kit-tareas-bar/WhySection';
import AuthorSection from '@/components/kit-tareas-bar/AuthorSection';
import BonusSection from '@/components/kit-tareas-bar/BonusSection';
import BuyBox from '@/components/kit-tareas-bar/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-bar/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-bar/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-bar/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { barTestimonials } from '@/data/testimonials-bar';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-bar/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasBar() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Bar / Cocktails | AI Chef Pro</title>
        <meta name="description" content="9 checklists operativos pre-rellenados para bar y cocktail bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario y eventos. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist bar, tareas bartender, checklist apertura bar, tareas coctelería, control stock bar, plantilla tareas barra, checklist cierre bar, inventario bar, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-bar" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Bar / Cocktails" />
        <meta property="og:description" content="9 checklists pre-rellenados: coctelería, barra, grifo, vinos, terraza. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-bar" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Bar / Cocktails" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para bar y cocktail bar. €12." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Bar / Cocktails",
          "description": "9 checklists operativos pre-rellenados para bar y cocktail bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario y eventos.",
          "image": "https://aichef.pro/og-image.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-bar",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Álvaro Reyes" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de mise en place de barra me cambió la vida. Ahora todo está listo antes de abrir." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Roberto Vega" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Tenemos 4 bares y ahora con los checklists hemos estandarizado la operación." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Pablo García" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Lo primero que hago con cada cliente nuevo es entregarle estos checklists. Cubren el 95% de lo que necesita cualquier bar." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para bar?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Cada checklist viene pre-rellenado con las tareas reales de un bar profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico." }},
            { "@type": "Question", "name": "¿Incluye tareas de coctelería?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Mise en place de coctelería, batches, jarabes, garnish, control de spirits y técnicas clásicas." }},
            { "@type": "Question", "name": "¿En qué se diferencia de Trail?", "acceptedAnswer": { "@type": "Answer", "text": "Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único." }},
            { "@type": "Question", "name": "¿Hay garantía de devolución?", "acceptedAnswer": { "@type": "Answer", "text": "30 días de garantía completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Bar / Cocktails", "item": "https://aichef.pro/kit-tareas-bar" }
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
          subtitle="Bartenders, encargados y dueños de bar que ya tienen sus operaciones bajo control"
          testimonials={barTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-bar" label="¿Ya compraste el Kit de Tareas Bar? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
