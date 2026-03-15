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

export default function ProPromptsEbook() {
  return (
    <>
      <Helmet>
        <title>Pro Prompts eBook — El único eBook de prompts de IA para hostelería | AI Chef Pro</title>
        <meta name="description" content="300+ prompts de IA para chefs, gerentes, pasteleros, bartenders y dueños de restaurante. Compatible con ChatGPT, Claude y AI Chef Pro. Solo €9." />
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Pro Prompts eBook — AI Chef Pro" />
        <meta property="og:description" content="El único eBook de prompts de IA para el mundo de la gastronomía. €9." />
        <meta property="og:url" content="https://aichef.pro/pro-prompts-ebook" />
        <meta property="og:type" content="product" />
        <link rel="canonical" href="https://aichef.pro/pro-prompts-ebook" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <HeroSection />
        <BookCover />
        <CategoriesGrid />
        <WhySection />
        <AuthorSection />
        <BonusSection />
        <FreeToolsSection />
        <BuyBox />
        <GuaranteeSection />
        <FaqAccordion />
        <CtaFinal />

        {/* Footer mínimo */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="https://aichef.pro/#pricing" className="text-gray-500 hover:text-[#FFD700] transition-colors">Precios</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:hello@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>

        <StickyBar />
      </div>
    </>
  );
}
