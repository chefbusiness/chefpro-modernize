import { Helmet } from 'react-helmet-async';
import HeroSection from '@/components/kit-gestion-personal/HeroSection';
import ContentGrid from '@/components/kit-gestion-personal/ContentGrid';
import WhySection from '@/components/kit-gestion-personal/WhySection';
import AuthorSection from '@/components/kit-gestion-personal/AuthorSection';
import BonusSection from '@/components/kit-gestion-personal/BonusSection';
import BuyBox from '@/components/kit-gestion-personal/BuyBox';
import GuaranteeSection from '@/components/kit-gestion-personal/GuaranteeSection';
import FaqAccordion from '@/components/kit-gestion-personal/FaqAccordion';
import CtaFinal from '@/components/kit-gestion-personal/CtaFinal';
import TestimonialsMarquee from '@/components/shared/TestimonialsMarquee';
import { gestionPersonalTestimonials } from '@/data/testimonials-gestion-personal';
import FreeToolsSection from '@/components/ebook/FreeToolsSection';
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-gestion-personal/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';
import CompatibleAppsMarquee from '@/components/shared/CompatibleAppsMarquee';
import WorldwideBanner from '@/components/shared/WorldwideBanner';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

export default function KitGestionPersonal() {
  return (
    <>
      <Helmet>
        <title>Kit Gestion de Personal y Turnos — Plantillas Excel para Hosteleria | AI Chef Pro</title>
        <meta name="description" content="9 plantillas Excel con formulas automaticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluacion de equipo en hosteleria. Solo 14 EUR." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="gestion personal restaurante, cuadrante turnos hosteleria, control horario restaurante, coste laboral hosteleria, plantilla turnos excel, onboarding empleado restaurante, evaluacion desempeno hosteleria, vacaciones restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/kit-gestion-personal" />
        <meta property="og:title" content="Kit Gestion de Personal y Turnos — Plantillas Excel para Hosteleria" />
        <meta property="og:description" content="9 plantillas Excel: cuadrante turnos, horas extra, coste laboral, onboarding, vacaciones, evaluacion. 14 EUR." />
        <meta property="og:url" content="https://aichef.pro/kit-gestion-personal" />
        <meta property="og:type" content="product" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-kit-gestion-personal.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Kit Gestion de Personal y Turnos — Plantillas para Hosteleria" />
        <meta name="twitter:description" content="Plantillas Excel profesionales para gestionar personal en hosteleria. 14 EUR." />

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "Product",
          "name": "Kit Gestion de Personal y Turnos — Plantillas Excel para Hosteleria",
          "description": "9 plantillas Excel con formulas automaticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluacion de equipo en hosteleria.",
          "image": "https://aichef.pro/og-kit-gestion-personal.jpg",
          "brand": { "@type": "Brand", "name": "AI Chef Pro" },
          "offers": {
            "@type": "Offer",
            "url": "https://aichef.pro/kit-gestion-personal",
            "priceCurrency": "EUR",
            "price": "14.00",
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": { "@type": "Organization", "name": "AI Chef Pro", "url": "https://aichef.pro" }
          },
          "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "8", "bestRating": "5", "worstRating": "1" },
          "review": [
            { "@type": "Review", "author": { "@type": "Person", "name": "David Ruiz" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "El cuadrante de turnos me ha cambiado la vida. Las alertas de 11h entre turnos y maximo 40h/semana me avisan automaticamente." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Carmen Delgado" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "La plantilla de onboarding es brutal. El tiempo de incorporacion bajo de 2 semanas a 4 dias en todas las unidades." },
            { "@type": "Review", "author": { "@type": "Person", "name": "Marta Jimenez" }, "reviewRating": { "@type": "Rating", "ratingValue": "5" }, "reviewBody": "Lo recomiendo a todos mis clientes. Las plantillas cumplen con la normativa vigente: descansos, jornada maxima, vacaciones." }
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "¿Incluye registro horario digital?", "acceptedAnswer": { "@type": "Answer", "text": "No. El registro/fichaje horario digital requiere una app homologada. Este kit es para planificacion de turnos, control de costes laborales, onboarding y gestion de equipo." }},
            { "@type": "Question", "name": "¿Las formulas calculan horas extra automaticamente?", "acceptedAnswer": { "@type": "Answer", "text": "Si. La plantilla calcula automaticamente el coste de cada hora extra segun el porcentaje de tu convenio colectivo." }},
            { "@type": "Question", "name": "¿En que se diferencia de apps de RRHH?", "acceptedAnswer": { "@type": "Answer", "text": "Las apps cobran entre 30 y 60 EUR/mes. Este kit cuesta 14 EUR, pago unico, sin suscripcion." }},
            { "@type": "Question", "name": "¿Hay garantia de devolucion?", "acceptedAnswer": { "@type": "Answer", "text": "30 dias de garantia completa. 100% reembolso sin preguntas." }}
          ]
        })}</script>

        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Kit Gestion de Personal y Turnos", "item": "https://aichef.pro/kit-gestion-personal" }
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
          subtitle="Gerentes, directores de RRHH y propietarios que ya gestionan su equipo con estas plantillas"
          testimonials={gestionPersonalTestimonials}
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
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought product="kit-gestion-personal" label="¿Ya compraste el Kit de Gestion de Personal? Vuelve a entrar al dashboard" />
          </div>
        </footer>
        <WhatsAppProductSupport />
        <StickyBar />
      </div>
    </>
  );
}
