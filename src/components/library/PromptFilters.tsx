const filters = [
  { id: 'all', label: 'Todos' },
  { id: 'cocina', label: 'Cocina' },
  { id: 'gestion', label: 'Gestión y Costes' },
  { id: 'pasteleria', label: 'Pastelería y Pan' },
  { id: 'catering', label: 'Catering' },
  { id: 'marketing', label: 'Marketing' },
  { id: 'alergenos', label: 'Alérgenos' },
  { id: 'food-pairing', label: 'Food Pairing' },
  { id: 'negocio', label: 'Negocio' },
  { id: 'liderazgo', label: 'Liderazgo' },
  { id: 'deep-research', label: 'Deep Research' },
];

// Tienda EN (2026-10-03): mismas ids (las categorías de src/data/prompts-en.ts), etiquetas en inglés.
const filtersEn: typeof filters = [
  { id: 'all', label: 'All' },
  { id: 'cocina', label: 'Cooking' },
  { id: 'gestion', label: 'Management & Costs' },
  { id: 'pasteleria', label: 'Pastry & Bread' },
  { id: 'catering', label: 'Catering' },
  { id: 'marketing', label: 'Marketing' },
  { id: 'alergenos', label: 'Allergens' },
  { id: 'food-pairing', label: 'Food Pairing' },
  { id: 'negocio', label: 'Business' },
  { id: 'liderazgo', label: 'Leadership' },
  { id: 'deep-research', label: 'Deep Research' },
];

interface Props {
  active: string;
  onChange: (id: string) => void;
  /** 'en' = etiquetas en inglés (tienda EN). Sin la prop (el ES) es lo de siempre. */
  lang?: 'es' | 'en';
}

export default function PromptFilters({ active, onChange, lang = 'es' }: Props) {
  return (
    <div className="flex flex-wrap gap-2 py-2">
      {(lang === 'en' ? filtersEn : filters).map((f) => (
        <button
          key={f.id}
          onClick={() => onChange(f.id)}
          className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
            active === f.id
              ? 'bg-[#FFD700] text-black shadow-md shadow-[#FFD700]/20'
              : 'bg-white/5 text-gray-400 hover:bg-white/10 hover:text-white'
          }`}
        >
          {f.label}
        </button>
      ))}
    </div>
  );
}
