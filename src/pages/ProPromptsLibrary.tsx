import { useState } from 'react';
import { Helmet } from 'react-helmet-async';
import TopBar from '@/components/library/TopBar';
import DownloadsSection from '@/components/library/DownloadsSection';
import CompatibilityBanner from '@/components/library/CompatibilityBanner';
import PromptFilters from '@/components/library/PromptFilters';
import PromptCategory from '@/components/library/PromptCategory';
import CtaToApp from '@/components/library/CtaToApp';
import { categories } from '@/data/prompts';

export default function ProPromptsLibrary() {
  const [activeFilter, setActiveFilter] = useState('all');
  const [openPromptId, setOpenPromptId] = useState<number | null>(null);

  const filteredCategories =
    activeFilter === 'all'
      ? categories
      : categories.filter((c) => c.id === activeFilter);

  const totalPrompts = categories.reduce((sum, c) => sum + c.promptCount, 0);

  const handleTogglePrompt = (id: number) => {
    setOpenPromptId((prev) => (prev === id ? null : id));
  };

  return (
    <>
      <Helmet>
        <title>Pro Prompts Library | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <TopBar />

        {/* Hero */}
        <section className="py-10 md:py-16 px-4">
          <div className="max-w-5xl mx-auto">
            <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-4">
              Tu Pro Prompts Library
            </h1>
            <p className="text-gray-400 text-lg leading-relaxed max-w-3xl">
              Bienvenido. Aquí tienes todos tus prompts certificados para hostelería y restauración — para chefs, gerentes, pasteleros, bartenders y dueños de negocio. Copia, usa y domina la IA.
            </p>
          </div>
        </section>

        <DownloadsSection />
        <CompatibilityBanner />

        {/* Prompts section */}
        <section className="py-10 px-4">
          <div className="max-w-5xl mx-auto">
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
                  openPromptId={openPromptId}
                  onTogglePrompt={handleTogglePrompt}
                />
              ))}
            </div>
          </div>
        </section>

        <CtaToApp />

        {/* Footer mínimo */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Pro Prompts Library · Todos los derechos reservados
            </p>
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:hello@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}
