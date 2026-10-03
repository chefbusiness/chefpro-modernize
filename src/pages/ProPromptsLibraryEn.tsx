import { useState, useMemo, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import { BookOpen, FileText, Download, Loader2 } from 'lucide-react';
import TopBar from '@/components/library/TopBar';
import FloatingGallery from '@/components/library/FloatingGallery';
import CompatibilityBanner from '@/components/library/CompatibilityBanner';
import PromptFilters from '@/components/library/PromptFilters';
import PromptCategory from '@/components/library/PromptCategory';
import PromptModal from '@/components/library/PromptModal';
import FreeToolsGrid from '@/components/library/FreeToolsGrid';
import CtaToApp from '@/components/library/CtaToApp';
import ChefBusinessGroup from '@/components/library/ChefBusinessGroup';
import { categories } from '@/data/prompts-en';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import ProductChangelog from '@/components/shared/ProductChangelog';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Pro Prompts Library EN — dashboard del Gastro Pro Prompts eBook (tienda EN, 3-oct-2026).
// COPIA TRADUCIDA de ProPromptsLibrary.tsx (ES): mismas secciones, orden y clases; los componentes de
// src/components/library/* reciben lang="en" (el ES no la pasa y se pinta como siempre) y los prompts
// salen de src/data/prompts-en.ts (los 76 del ES traducidos).
//
// Diferencia deliberada con el ES: la sección de descargas va AQUÍ (copia de DownloadsSection.tsx) y no
// en el componente compartido, porque el EN nace con el patrón moderno de entrega:
//  - JWT propio (storageKey `ai-prompts-for-restaurants-jwt`; el ES usa el default `pro-prompts-jwt`);
//  - get-download-urls responde `{ files }` desde PRODUCT_FILES (no la rama de env vars del ES).
// Las `key` de DOWNLOADS son las de la entrada `ai-prompts-for-restaurants` de
// netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza leyendo este fichero).
// Y el bloque de novedades (ProductChangelog), estándar de los dashboards EN, con su primera edición.

const DOWNLOADS = [
  {
    key: 'ebook',
    icon: BookOpen,
    title: 'Gastro Pro Prompts eBook',
    desc: 'The complete eBook in PDF, with all 300 prompts organized by section.',
    format: 'PDF',
    primary: true,
  },
  {
    key: 'bonus1',
    icon: BookOpen,
    title: 'Bonus 1: Prompt Engineering Guide',
    desc: 'Learn to write your own hospitality prompts with the AI Chef Pro method.',
    format: 'Word',
  },
  {
    key: 'bonus23',
    icon: FileText,
    title: 'Bonus 2: Templates + Cheat Sheet',
    desc: 'Ready-to-use templates and a quick summary of the best prompts.',
    format: 'Excel',
  },
];

function DownloadsSectionEn() {
  const { token } = useAuth('ai-prompts-for-restaurants-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.files) setFiles(data.files);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <section className="py-10 px-4">
      <div className="max-w-5xl mx-auto">
        <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">
          Your downloads
        </p>
        <div className="grid md:grid-cols-3 gap-4">
          {DOWNLOADS.map((card) => {
            const Icon = card.icon;
            const url = files[card.key];
            return (
              <div
                key={card.key}
                className={`rounded-xl p-5 ${
                  card.primary
                    ? 'bg-white/5 border-2 border-[#FFD700]/50'
                    : 'bg-white/5 border border-white/10'
                }`}
              >
                <Icon className="w-8 h-8 text-[#FFD700] mb-3" />
                <h3 className="text-white font-bold mb-1">{card.title}</h3>
                <p className="text-gray-400 text-sm mb-4">{card.desc}</p>
                {loading ? (
                  <Loader2 className="w-5 h-5 text-gray-500 animate-spin" />
                ) : url ? (
                  <a
                    href={url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${
                      card.primary
                        ? 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90'
                        : 'border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10'
                    }`}
                  >
                    <Download className="w-4 h-4" />
                    Download {card.format}
                  </a>
                ) : (
                  <span className="text-gray-500 text-sm">Not available</span>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default function ProPromptsLibraryEn() {
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
        <title>Pro Prompts Library — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        <TopBar lang="en" />

        {/* Hero with floating gallery */}
        <section className="relative overflow-hidden">
          <FloatingGallery />
          <div className="absolute inset-0 flex items-center justify-center z-20">
            <div className="text-center px-4">
              <LogoBadge lang="en" />
              <h1 className="text-4xl md:text-6xl font-extrabold text-white mb-4 mt-4 drop-shadow-lg">
                Pro Prompts Library <span className="text-[#FFD700]">by AI Chef Pro</span>
              </h1>
              <p className="text-gray-300 text-base md:text-lg leading-relaxed max-w-2xl mx-auto drop-shadow-md">
                Your exclusive dashboard with 76 copy-ready prompts curated by <span className="whitespace-nowrap">Chef John Guerrero</span>, CEO of AI Chef Pro, plus downloadable bonuses and professional tools. Copy, use and master AI in your food business.
              </p>
            </div>
          </div>
        </section>

        <DownloadsSectionEn />
        <ProductChangelog productId="ai-prompts-for-restaurants" lang="en" />
        <CompatibilityBanner lang="en" />

        {/* Prompts section */}
        <section className="py-10 px-4">
          <div className="max-w-6xl mx-auto">
            <div className="flex flex-col sm:flex-row sm:items-center gap-3 mb-6">
              <h2 className="text-2xl font-bold text-white">Certified Prompts</h2>
              <span className="px-3 py-1 bg-white/10 text-gray-400 text-sm rounded-full w-fit">
                {totalPrompts} prompts · {categories.length} categories
              </span>
            </div>

            <PromptFilters active={activeFilter} onChange={setActiveFilter} lang="en" />

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

        <FreeToolsGrid lang="en" />
        <CtaToApp lang="en" />

        <ChefBusinessGroup lang="en" />

        {/* Minimal footer */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Pro Prompts Library · All rights reserved
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro/en" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contact</a>
            </div>
          </div>
        </footer>
        <WhatsAppProductSupport lang="en" />
      </div>

      {/* Prompt Modal */}
      {selectedPrompt && (
        <PromptModal
          number={selectedPrompt.id}
          title={selectedPrompt.title}
          text={selectedPrompt.text}
          compatible={selectedPrompt.compatible}
          onClose={() => setSelectedPromptId(null)}
          lang="en"
        />
      )}
    </>
  );
}
