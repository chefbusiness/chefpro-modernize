import { Flame, BarChart3, ShieldCheck, Banknote } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Flame,
    title: 'Único Plan España con Marco CCAA Fuego',
    desc: 'Anexo dedicado con autorización exigida, restricciones por temporada (INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak) y excepciones para finca privada en 8 CCAA. Cubre la excepción cultural valenciana de Falles y festes — vital para paelleros del Levante.',
  },
  {
    icon: BarChart3,
    title: 'Modelo Híbrido B2C + B2B Validado',
    desc: 'Mix B2C 35 % (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B 65 % (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building). Calculadora pricing dual y modelos de contrato para cada canal.',
  },
  {
    icon: ShieldCheck,
    title: '88 Proveedores Reales Validados',
    desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + Bomba Calasparra DO, mariscos Mediterráneo (Linamar, Castellet, Nardín DO Denia), verduras Levante DO, azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa/Steelite.',
  },
  {
    icon: Banknote,
    title: 'Inversión Mínima 3.500 EUR',
    desc: '4-7x menor que un restaurante de arroces con local fijo (70-130K EUR). Escenario mínimo viable o full equipment hasta 25K EUR. Break-even 18-22 eventos año 1. Pago único, sin suscripciones.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Por Qué Este <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No es otra plantilla genérica. Es el único plan completo de España para montar tu empresa premium de paella y arroces para eventos: 11 entregables reales con datos del mercado 2026, marco legal CCAA fuego al aire libre y modelo híbrido B2C+B2B.
            </p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {reasons.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 100}>
              <div className="text-center">
                <div className="w-14 h-14 rounded-2xl bg-[#FFD700]/20 flex items-center justify-center mx-auto mb-4">
                  <Icon className="w-7 h-7 text-[#FFD700]" />
                </div>
                <h3 className="text-white font-bold mb-2">{title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
        <FadeIn>
          <div className="bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 text-center">
            <p className="text-gray-300 mb-4 text-sm">Compatible con cualquier software ofimático:</p>
            <div className="flex flex-wrap justify-center gap-2">
              {[
                { label: 'Excel', highlight: true },
                { label: 'Word' },
                { label: 'Google Sheets' },
                { label: 'Google Docs' },
                { label: 'LibreOffice' },
                { label: 'Apple Numbers' },
              ].map((pill) => (
                <span key={pill.label} className={`px-3 py-1.5 rounded-full text-sm font-medium ${pill.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'}`}>
                  {pill.label}
                </span>
              ))}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
