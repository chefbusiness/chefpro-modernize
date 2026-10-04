const pills = [
  { label: 'AI Chef Pro', highlight: true },
  { label: 'ChatGPT' },
  { label: 'Claude' },
  { label: 'Perplexity' },
  { label: 'DeepSeek' },
  { label: 'Gemini' },
  { label: 'KIMI' },
  { label: 'Copilot' },
];

// `lang` (tienda EN, 2026-10-03): solo cambia la etiqueta. Sin la prop (el ES) es lo de siempre.
export default function CompatibilityBanner({ lang = 'es' }: { lang?: 'es' | 'en' }) {
  return (
    <div className="py-6 px-4">
      <div className="max-w-5xl mx-auto bg-white/5 border border-white/10 rounded-xl p-4 flex flex-col sm:flex-row items-center gap-3">
        <span className="text-gray-400 text-sm whitespace-nowrap">{lang === 'en' ? 'Compatible with:' : 'Compatible con:'}</span>
        <div className="flex flex-wrap justify-center gap-2">
          {pills.map((p) => (
            <span
              key={p.label}
              className={`px-3 py-1 rounded-full text-xs font-medium ${
                p.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'
              }`}
            >
              {p.label}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
