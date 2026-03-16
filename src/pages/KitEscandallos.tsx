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
import TryPlatformBanner from '@/components/ebook/TryPlatformBanner';
import StickyBar from '@/components/kit-escandallos/StickyBar';
import AlreadyBought from '@/components/ebook/AlreadyBought';

export default function KitEscandallos() {
  return (
    <>
      <Helmet>
        <title>Kit de Escandallos Pro — 11 Plantillas Excel Profesionales | AI Chef Pro</title>
        <meta name="description" content="11 plantillas de escandallos con fórmulas automáticas, mermas precargadas y calculadora de PVP. Para chefs, gerentes y dueños de restaurante. Solo €12." />
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Kit de Escandallos Pro — AI Chef Pro" />
        <meta property="og:description" content="Controla tu food cost con 11 plantillas Excel profesionales. €12." />
        <meta property="og:url" content="https://aichef.pro/kit-escandallos" />
        <meta property="og:type" content="product" />
        <link rel="canonical" href="https://aichef.pro/kit-escandallos" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <HeroSection />
        <ContentGrid />
        <TestimonialsMarquee
          title={<>Lo Que Dicen los <span className="text-[#FFD700]">Profesionales</span></>}
          subtitle="Profesionales de la hostelería que ya controlan su food cost con el Kit de Escandallos Pro"
          testimonials={escandallosTestimonials}
        />
        <WhySection />
        <AuthorSection />
        <BonusSection />
        <BuyBox />
        <GuaranteeSection />
        <FaqAccordion />
        <CtaFinal />
        <TryPlatformBanner />

        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="https://aichef.pro/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
            <AlreadyBought />
          </div>
        </footer>

        <StickyBar />
      </div>
    </>
  );
}
