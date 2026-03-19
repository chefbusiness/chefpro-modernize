import { useState, useMemo } from 'react';
import { Helmet } from 'react-helmet-async';
import TopBar from '@/components/library/TopBar';
import FloatingGallery from '@/components/library/FloatingGallery';
import DownloadsSection from '@/components/library/DownloadsSection';
import CompatibilityBanner from '@/components/library/CompatibilityBanner';
import PromptFilters from '@/components/library/PromptFilters';
import PromptCategory from '@/components/library/PromptCategory';
import PromptModal from '@/components/library/PromptModal';
import FreeToolsGrid from '@/components/library/FreeToolsGrid';
import CtaToApp from '@/components/library/CtaToApp';
import ChefBusinessGroup from '@/components/library/ChefBusinessGroup';
import { categories } from '@/data/prompts';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';

export default function ProPromptsLibrary() {
  const [activeFilter, setActiveFilter] = useState('all');
  const [selectedPromptId, setSelectedPromptId] = useState<number | null>(null);

  const filteredCategories =
    activeFilter === 'all'
      ? categories
      : categories.filter((c) => c.id === activeFilter);

  const totalPrompts = categories.reduce((sum, c) => sum + c.promptCount, 0);

  // Find selected prompt across all categories
  const selectedPrompt = useMemo(() => {
    if (!selectedPromptId) return null;
    for (const cat of categories) {
      const found = cat.prompts.find((p) => p.id === selectedPromptId);
      if (found) return found;
    }
    return null;
  }, [selectedPromptId]);

  return (
    <>
      <Helmet>
        <title>Pro Prompts Library | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <TopBar />

        {/* Hero with floating gallery */}
        <section className="relative overflow-hidden">
          <FloatingGallery />
          <div className="absolute inset-0 flex items-center justify-center z-20">
            <div className="text-center px-4">
              <LogoBadge />
              <h1 className="text-4xl md:text-6xl font-extrabold text-white mb-4 mt-4 drop-shadow-lg">
                Pro Prompts Library <span className="text-[#FFD700]">by AI Chef Pro</span>
              </h1>
              <p className="text-gray-300 text-base md:text-lg leading-relaxed max-w-2xl mx-auto drop-shadow-md">
                Tu dashboard exclusivo con todos los prompts curados por el <span className="whitespace-nowrap">Chef John Guerrero</span>, CEO de AI Chef Pro, bonos descargables y herramientas profesionales. Copia, usa y domina la IA en gastronomía.
              </p>
            </div>
          </div>
        </section>

        <DownloadsSection />
        <CompatibilityBanner />

        {/* Prompts section */}
        <section className="py-10 px-4">
          <div className="max-w-6xl mx-auto">
            <div className="flex flex-col sm:flex-row sm:items-center gap-3 mb-6">
              <h2 className="text-2xl font-bold text-white">Prompts Certificados</h2>
              <span className="px-3 py-1 bg-white/10 text-gray-400 text-sm rounded-full w-fit">
                {totalPrompts} prompts · {categories.length} categorías
              </span>
            </div>

            <PromptFilters active={activeFilter} onChange={setActiveFilter} />

            <div className="mt-8">
              {filteredCategories.map((cat) => (
                <PromptCategory
                  key={cat.id}
                  category={cat}
                  onSelectPrompt={setSelectedPromptId}
                />
              ))}
            </div>
          </div>
        </section>

        <FreeToolsGrid />
        <CtaToApp />

        <ChefBusinessGroup />

        {/* Footer mínimo */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Pro Prompts Library · Todos los derechos reservados
            </p>
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
      </div>

      {/* Prompt Modal */}
      {selectedPrompt && (
        <PromptModal
          number={selectedPrompt.id}
          title={selectedPrompt.title}
          text={selectedPrompt.text}
          compatible={selectedPrompt.compatible}
          onClose={() => setSelectedPromptId(null)}
        />
      )}
    </>
  );
}
