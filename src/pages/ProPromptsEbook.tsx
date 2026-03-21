import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/ebook/HeroSection';
import BookCover from '@/components/ebook/BookCover';
import CategoriesGrid from '@/components/ebook/CategoriesGrid';
import WhySection from '@/components/ebook/WhySection';
import AuthorSection from '@/components/ebook/AuthorSection';
import BonusSection from '@/components/ebook/BonusSection';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import BuyBox from '@/components/ebook/BuyBox';
import GuaranteeSection from '@/components/ebook/GuaranteeSection';
import FaqAccordion from '@/components/ebook/FaqAccordion';
import CtaFinal from '@/components/ebook/CtaFinal';
import StickyBar from '@/components/ebook/StickyBar';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { ebookTestimonials } from '@/data/testimonials-ebook';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function ProPromptsEbook() {
  return (
    <>
      <Helmet>
        <title>Pro Prompts eBook — El único eBook de prompts de IA para hostelería | AI Chef Pro</title>
        <meta name="description" content="300+ prompts de IA para chefs, gerentes, pasteleros, bartenders y dueños de restaurante. Compatible con ChatGPT, Claude y AI Chef Pro. Solo €9." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="prompts IA hostelería, prompts ChatGPT restaurante, prompts para chefs, inteligencia artificial restaurantes, IA para hostelería, ebook prompts cocina, ChatGPT cocina profesional, prompts pastelería IA, prompts catering IA, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/pro-prompts-ebook" />

        {/* Open Graph */}
        <meta property="og:title" content="Pro Prompts eBook — 300+ prompts de IA para hostelería" />
        <meta property="og:description" content="El único eBook de prompts de IA para el mundo de la gastronomía. Compatible con ChatGPT, Claude, Gemini y AI Chef Pro. Solo €9." />
        <meta property="og:url" content="https://aichef.pro/pro-prompts-ebook" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/ebook-mockup-bundle.jpg" />
        <meta property="og:image:secure_url" content="https://aichef.pro/ebook-mockup-bundle.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="Pro Prompts eBook — 300+ prompts de IA para hostelería profesional" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Pro Prompts eBook — 300+ prompts de IA para hostelería" />
        <meta name="twitter:description" content="300+ prompts de IA para chefs, gerentes, pasteleros, bartenders y dueños de restaurante. Solo €9." />
        <meta name="twitter:image" content="https://aichef.pro/ebook-mockup-bundle.jpg" />
        <meta name="twitter:image:alt" content="Pro Prompts eBook — AI Chef Pro" />

        {/* Product Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Pro Prompts eBook — 300+ prompts de IA para hostelería",
          "description": "eBook con 300+ prompts de IA específicos para hostelería y restauración. Cocina creativa, pastelería, catering, gestión, liderazgo, marketing y más.",
          "image": "https://aichef.pro/ebook-mockup-bundle.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/pro-prompts-ebook",
            "priceCurrency": "EUR",
            "price": "9.00",
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
              "author": { "@type": "Person", "name": "Carlos Martínez" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Llevo 20 años en cocina y nunca pensé que la IA me ahorraría tanto tiempo. Los prompts de recetas creativas me han dado ideas que a mí solo me habrían costado semanas de I+D."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Laura Sánchez" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Los prompts de gestión y costes son oro puro. En una semana ya tenía controlado el food cost de 3 restaurantes con las plantillas que genera la IA."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Roberto García" },
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Recomiendo el eBook a todos mis clientes. Es la forma más rápida de que un restaurante empiece a usar IA sin necesitar formación técnica."
            }
          ]
        })}</script>

        {/* FAQPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Cómo recibo el acceso después del pago?", "acceptedAnswer": { "@type": "Answer", "text": "Inmediatamente después del pago recibirás un email con tu enlace de acceso personal y único a la Pro Prompts Library, donde encontrarás el eBook descargable y todos los bonos." }},
            { "@type": "Question", "name": "¿Funciona solo con AI Chef Pro o con otras IAs?", "acceptedAnswer": { "@type": "Answer", "text": "Los prompts están optimizados para AI Chef Pro pero funcionan perfectamente con ChatGPT, Claude, Perplexity, DeepSeek, Gemini, KIMI y cualquier IA conversacional." }},
            { "@type": "Question", "name": "¿Qué formato tiene el eBook?", "acceptedAnswer": { "@type": "Answer", "text": "PDF de alta calidad, compatible con todos los dispositivos: móvil, tablet y ordenador." }},
            { "@type": "Question", "name": "¿Recibiré actualizaciones?", "acceptedAnswer": { "@type": "Answer", "text": "Sí. Todas las actualizaciones futuras son gratuitas. A medida que AI Chef Pro lance nuevas apps, el eBook se actualiza y tú las recibes automáticamente." }},
            { "@type": "Question", "name": "¿Cómo funciona la garantía?", "acceptedAnswer": { "@type": "Answer", "text": "Tienes 30 días completos para probarlo. Si no estás satisfecho por cualquier motivo, te devolvemos el 100% sin hacer ninguna pregunta." }},
            { "@type": "Question", "name": "¿Necesito experiencia previa con IA?", "acceptedAnswer": { "@type": "Answer", "text": "Para nada. Los prompts están listos para copiar y pegar. Resultados profesionales desde el primer día, independientemente de tu nivel." }}
          ]
        })}</script>

        {/* BreadcrumbList Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Pro Prompts eBook", "item": "https://aichef.pro/pro-prompts-ebook" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <HeroSection />
        <BookCover />
        <CompatibleAppsMarquee variant="ebook" />
        <CategoriesGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Profesionales de la hostelería que ya usan los prompts del eBook en su día a día"
          testimonials={ebookTestimonials}
        />
        <WhySection />
        <AuthorSection />
        <BonusSection />
        <FreeToolsSection />
        <BuyBox />
        <GuaranteeSection />
        <FaqAccordion />
        <CtaFinal />
        <TryPlatformBanner />

        {/* Footer mínimo */}
        <footer className="py-8 pb-24 md:pb-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought />
          </div>
        </footer>

        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
