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
];

interface Props {
  active: string;
  onChange: (id: string) => void;
}

export default function PromptFilters({ active, onChange }: Props) {
  return (
    <div className="overflow-x-auto scrollbar-hide py-2 -mx-4 px-4">
      <div className="flex gap-2 min-w-max">
        {filters.map((f) => (
          <button
            key={f.id}
            onClick={() => onChange(f.id)}
            className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-all ${
              active === f.id
                ? 'bg-[#FFD700] text-black'
                : 'bg-white/5 text-gray-400 hover:bg-white/10 hover:text-white'
            }`}
          >
            {f.label}
          </button>
        ))}
      </div>
    </div>
  );
}
