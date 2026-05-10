import {
  FileText, Coins, Calculator, Truck, Wrench,
  ShieldCheck, GlassWater, ScrollText, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Resumen ejecutivo, concepto itinerante, mercado eventos España, competencia, marketing B2B, operaciones, RRHH freelance, financiero, legal y plan de financiación. ~6.600 palabras editables.' },
  { icon: Coins, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con estacionalidad eventos, inversión inicial 18-35K EUR, break-even por nº de eventos (31/año), 3 escenarios y ratios sector itinerante.' },
  { icon: Calculator, title: 'Calculadora Pricing por Evento', desc: 'Excel con fórmulas: invitados + horas + tipo + complejidad ⇒ precio sugerido en 3 niveles + margen estimado. Con 10 ejemplos reales del sector.' },
  { icon: Truck, title: 'Plantilla 96 Proveedores Reales', desc: 'Excel categorizado: licores, mixers (Damm/Disbesa), cristalería (Schott Zwiesel/Spiegelau), hielo (Hoshizaki) y captación B2B con wedding planners.' },
  { icon: Wrench, title: 'Catálogo Equipamiento (SKU reales)', desc: 'Barras móviles GGM MCSH 2.420 EUR + Mewindo + Station Deus + Flexbar. Máquinas de hielo Hoshizaki/ITV. Cristalería profesional con precios orientativos.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (71 trámites)', desc: 'Constitución, seguros (RC obligatorio), equipamiento, marca y web, captación B2B y operativa primeros 90 días. Modelo itinerante sin licencia clasificada.' },
  { icon: GlassWater, title: 'Carta 15 Cocktails Temáticos', desc: 'Speakeasy + Gin Lounge + Tropical + Mediterranean + Signature. Receta + escandallo + escalado a 50/100/200 invitados + glasería recomendada.' },
  { icon: ScrollText, title: 'Modelo de Contrato Profesional', desc: '11 cláusulas listas para firmar: anticipo, cancelación 30/60 días, fuerza mayor, RC, derechos imagen, RGPD, jurisdicción. Plantilla DOCX editable.' },
  { icon: Sparkles, title: '10 Experiencias Temáticas Premium', desc: 'Speakeasy Años 20, Gin Lounge, Tropical Tiki, Mixología Molecular, Bourbon Tasting, Mediterranean, Latin, Whisky Tasting, Champagne y Signature.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-1.jpeg',
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-2.jpeg',
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
  '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-6.jpeg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Qué Incluye el <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              9 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu barra móvil de coctelería.
            </p>
          </div>
        </FadeIn>
        <FadeIn>
          <div className="grid grid-cols-3 md:grid-cols-6 gap-2 mb-12 rounded-xl overflow-hidden">
            {galleryImages.map((src, i) => (
              <div key={i} className="aspect-square overflow-hidden rounded-lg">
                <img src={src} alt="" className="w-full h-full object-cover hover:scale-110 transition-transform duration-500" loading="lazy" />
              </div>
            ))}
          </div>
        </FadeIn>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {categories.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 50}>
              <div className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/50 transition-all duration-300 h-full">
                <Icon className="w-8 h-8 text-[#FFD700] mb-3" />
                <h3 className="text-white font-semibold text-sm md:text-base mb-1.5">{title}</h3>
                <p className="text-gray-400 text-sm md:text-base leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
