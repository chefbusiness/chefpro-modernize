import { Globe, BarChart3, ShieldCheck, Banknote } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Globe,
    title: 'Único Plan España con Modelo Multi-concepto',
    desc: 'El ÚNICO plan del mercado español que enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente), no monoconcepto. Justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto, con márgenes 30-40 % más altos.',
  },
  {
    icon: BarChart3,
    title: 'Modelo Dual B2C Bodas Multiculturales + B2B Corporate',
    desc: 'Mix B2C 35 % (bodas multiculturales, cumpleaños temáticos, aniversarios) + B2B 65 % (corporate brand events, embajadas, wedding planners, festivales gastronómicos, hoteles boutique). Calculadora pricing dual con factor multi-concepto y modelos de contrato para cada canal.',
  },
  {
    icon: ShieldCheck,
    title: '96 Proveedores · 12 Cocinas del Mundo',
    desc: 'Importadores asiáticos premium (EMB Food, Cominport, Garmiko) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ texano (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.',
  },
  {
    icon: Banknote,
    title: 'Inversión Mínima 5.500 EUR',
    desc: '5-9x menor que un catering con cocina central (45-120K EUR). Escenario mínimo viable, recomendado 11.500 EUR o premium hasta 35.000 EUR. Break-even 14 eventos/mes año 1. Pago único, sin suscripciones.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-2.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Por Qué Este <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No es otra plantilla genérica. Es el único plan completo del mercado español para montar tu catering temático multi-concepto premium: 11 entregables con 12 cocinas del mundo, 96 proveedores especializados (importadores asiáticos, latinos, italianos, BBQ texano), datos reales 2026 (4.585 M€ catering España, boda media 25.183 €) y anexo regulación 17 CCAA.
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
