import { ArrowRight } from 'lucide-react';

export default function CtaToApp() {
  return (
    <section className="py-16 px-4">
      <div className="max-w-3xl mx-auto text-center bg-gradient-to-br from-white/5 to-white/[0.02] border border-white/10 rounded-2xl p-8 md:p-12">
        <h2 className="text-2xl md:text-3xl font-bold text-white mb-3">
          ¿Quieres usar estos prompts con las 55+ apps de AI Chef Pro?
        </h2>
        <p className="text-gray-400 leading-relaxed mb-6 max-w-xl mx-auto">
          La suite completa para toda la hostelería: chefs, gerentes, pasteleros, bartenders y dueños de negocio. Food Pairing AI, Mermas GenCal, Catering AI+ y mucho más.
        </p>
        <a
          href="https://aichef.pro"
          className="inline-flex items-center gap-2 px-8 py-3.5 bg-[#FFD700] text-black font-bold rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02]"
        >
          Descubrir AI Chef Pro
          <ArrowRight className="w-5 h-5" />
        </a>
      </div>
    </section>
  );
}
