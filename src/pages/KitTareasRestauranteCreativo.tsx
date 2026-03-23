import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-tareas-restaurante-creativo/HeroSection';
import ContentGrid from '@/components/kit-tareas-restaurante-creativo/ContentGrid';
import WhySection from '@/components/kit-tareas-restaurante-creativo/WhySection';
import AuthorSection from '@/components/kit-tareas-restaurante-creativo/AuthorSection';
import BonusSection from '@/components/kit-tareas-restaurante-creativo/BonusSection';
import BuyBox from '@/components/kit-tareas-restaurante-creativo/BuyBox';
import GuaranteeSection from '@/components/kit-tareas-restaurante-creativo/GuaranteeSection';
import FaqAccordion from '@/components/kit-tareas-restaurante-creativo/FaqAccordion';
import CtaFinal from '@/components/kit-tareas-restaurante-creativo/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { restauranteCreativoTestimonials } from '@/data/testimonials-restaurante-creativo';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-tareas-restaurante-creativo/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitTareasRestauranteCreativo() {
  return (
    <>
      <Helmet>
        <title>Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor | AI Chef Pro</title>
        <meta name="description" content="11 checklists operativos pre-rellenados para restaurante creativo y de autor: I+D, menu degustacion, brigada creativa, sumiller, eventos. Imprime, delega y firma. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="checklist restaurante creativo, tareas restaurante de autor, checklist menu degustacion, mise en place fine dining, checklist sumiller, tareas brigada cocina creativa, plantilla tareas chef ejecutivo, checklist I+D cocina, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-tareas-restaurante-creativo" />
        <meta property="og:title" content="Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor" />
        <meta property="og:description" content="11 checklists pre-rellenados: I+D, degustacion, brigada creativa, sumiller, eventos. Imprime, delega y firma. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-tareas-restaurante-creativo" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-tareas-restaurante-creativo.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit de Tareas Recurrentes — Checklists para Restaurante Creativo / De Autor" />
        <meta name="twitter:description" content="Checklists operativos pre-rellenados para restaurante creativo y de autor. €12." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor",
          "description": "11 checklists operativos pre-rellenados para restaurante creativo: I+D, menu degustacion, brigada creativa, sumiller y eventos.",
          "image": "https://aichef.pro/og-kit-tareas-restaurante-creativo.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-tareas-restaurante-creativo",
            "priceCurrency": "EUR",
            "price": "12.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "Alberto Riera" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El checklist de mise en place para degustacion me cambio la vida. Cada pase documentado con timing, temperaturas y responsable." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Marina Delgado" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La plantilla de I+D es increible. Fichas tecnicas, pruebas de concepto, evaluacion sensorial... por fin tengo un sistema." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Patricia Vega" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Lo primero que hago con cada cliente de restaurante creativo es entregarle estos checklists. Cubren el 95% de lo que necesita." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Las tareas vienen ya rellenadas para restaurante creativo?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D, degustacion, brigada, sumiller y eventos. Solo personaliza: ajustar, borrar lo que no aplique y anadir lo especifico." }},
            { "@type": "Question", "name": "¿Cubre I+D y desarrollo de menu?", "acceptedAnswer": { "@type": "Answer", "text": "Si. Fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes I+D y registro fotografico." }},
            { "@type": "Question", "name": "¿En que se diferencia de apps de gestion?", "acceptedAnswer": { "@type": "Answer", "text": "Apps cobran €40/mes por local. Este kit da las mismas listas en Excel por €12, pago unico." }},
            { "@type": "Question", "name": "¿Hay garantia de devolucion?", "acceptedAnswer": { "@type": "Answer", "text": "30 dias de garantia completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit de Tareas Recurrentes: Restaurante Creativo / De Autor", "item": "https://aichef.pro/kit-tareas-restaurante-creativo" }
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
          subtitle="Chefs ejecutivos, sous-chefs, sumilleres y gerentes de restaurante creativo que ya tienen sus operaciones bajo control"
          testimonials={restauranteCreativoTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-tareas-restaurante-creativo" label="¿Ya compraste el Kit de Tareas Restaurante Creativo? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
