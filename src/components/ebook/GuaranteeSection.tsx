import { ShieldCheck } from 'lucide-react';

const stats = [
  { number: '30', label: 'Días de garantía' },
  { number: '100%', label: 'Reembolso garantizado' },
  { number: '0', label: 'Preguntas incómodas' },
];

export default function GuaranteeSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto text-center">
        <div className="w-20 h-20 rounded-full bg-[#FFD700]/10 flex items-center justify-center mx-auto mb-6">
          <ShieldCheck className="w-10 h-10 text-[#FFD700]" />
        </div>
        <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">
          Garantía de Satisfacción 100%
        </h2>
        <p className="text-gray-400 text-lg leading-relaxed mb-10 max-w-2xl mx-auto">
          Si el eBook no supera tus expectativas, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.
        </p>

        <div className="grid grid-cols-3 gap-6">
          {stats.map(({ number, label }) => (
            <div key={label}>
              <p className="text-3xl md:text-4xl font-extrabold text-[#FFD700]">{number}</p>
              <p className="text-gray-400 text-sm mt-1">{label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
