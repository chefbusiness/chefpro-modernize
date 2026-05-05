import FadeIn from '../ebook/FadeIn';

const stats = [
  { number: '30', label: 'Días de garantía' },
  { number: '100%', label: 'Reembolso garantizado' },
  { number: '0', label: 'Preguntas incómodas' },
];

export default function GuaranteeSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto text-center">
        <FadeIn>
          <img src="/money-back-badge.png" alt="100% Money Back Guaranteed" className="w-28 h-28 md:w-32 md:h-32 mx-auto mb-6 object-contain" />
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">Garantía de Satisfacción <span className="text-[#FFD700]">100%</span></h2>
          <p className="text-gray-400 text-lg leading-relaxed mb-10 max-w-2xl mx-auto">
            Si los checklists no te ayudan a profesionalizar tu asador y dominar el horno Josper, las brasas y la maduración, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.
          </p>
        </FadeIn>
        <FadeIn delay={150}>
          <div className="grid grid-cols-3 gap-6">
            {stats.map(({ number, label }) => (
              <div key={label}>
                <p className="text-3xl md:text-4xl font-extrabold text-[#FFD700]">{number}</p>
                <p className="text-gray-400 text-sm mt-1">{label}</p>
              </div>
            ))}
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
