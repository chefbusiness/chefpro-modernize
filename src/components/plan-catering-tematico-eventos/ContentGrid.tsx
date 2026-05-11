import {
  FileText, Coins, Calculator, Truck, Wrench, ShieldCheck,
  LayoutGrid, Utensils, ScrollText, Flame, BookOpen,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026 (4.585 M€ catering, 25.183 € boda media), top 14 conceptos temáticos validados, modelo multi-concepto sin local fijo, anexo 17 CCAA, financiero 3 años, riesgos, roadmap progresivo.' },
  { icon: Coins, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 5.500-35.000 EUR según escenario, estacionalidad bodas mayo-octubre + corporate diciembre, break-even 14 eventos/mes año 1, ticket medio 2.200-4.500 €.' },
  { icon: Calculator, title: 'Calculadora Pricing Multi-concepto', desc: 'Excel con fórmulas duales B2C + B2B + factor multi-concepto. Inputs: pax, distancia, número conceptos (1-5+), nivel calidad, pairing, branded experience, freelance especializado ⇒ precio sugerido + margen. 10 ejemplos validados.' },
  { icon: Truck, title: 'Plantilla 96 Proveedores · 12 Cocinas', desc: 'Importadores asiáticos (EMB Food, Cominport, Garmiko) + latinos (Imp. Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.' },
  { icon: Wrench, title: 'Catálogo Equipamiento Multi-cocina', desc: 'Por concepto: cuchillería japonesa sushi (Tojiro, Yoshihiro) + horno leña pizza (Pizza Party, Ooni Pro) + parrilla argentina + trompo pastor + tandoor portátil + smoker offset texano + wok pro (Wokinox) + sous-vide (Anova, Sammic) + vajilla premium.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil multi-concepto + RGSEAA) · seguros RC eventos con cláusula intoxicación · proveedores especializados 12 cocinas · marca multi-concepto · captación B2C+B2B · operativa primer evento multi-station. 110 hitos.' },
  { icon: LayoutGrid, title: '12 Conceptos Temáticos Pre-empaquetados', desc: 'Sushi-bar omakase + tacos al pastor + trattoria italiana + asado argentino + ceviche peruano + marisquería gallega + tandoor indio + mediterráneo + vegano premium + brasileño rodízio + BBQ texano + brunch internacional. Cada uno con menú + ambientación + equipamiento + operativa.' },
  { icon: ScrollText, title: 'Modelos Contrato B2C + B2B Corporate', desc: 'Plantillas legales editables: B2C particular (boda multicultural, cumpleaños temático, aniversarios) + B2B corporate (brand event, embajada, festival gastronómico, planner) con MSA acuerdo marco anual, confidencialidad y propiedad intelectual del menú multi-concepto.' },
  { icon: Utensils, title: 'Carta 12 Menús Cocinas del Mundo', desc: 'Boda multicultural premium 7 estaciones + tasting Asia 7 pasos + mexicano Día de Muertos + italiano trattoria + argentino tradicional + peruano Lima + indio Bollywood + griego/turco + vegano premium + BBQ texano + brunch internacional + mariscada gallega.' },
  { icon: Flame, title: 'Manual Técnico APPCC Multi-concepto', desc: '7 PCC adaptados a multi-cocina simultánea (cadena frío diferenciada, T° servicio por concepto, alérgenos en multi-station) + cronograma evento 80 pax + layout multi-station + coordinación equipo freelance especializado por concepto.' },
  { icon: BookOpen, title: 'Guía Especialización Progresiva', desc: 'Cómo construir tu portafolio de cocinas del mundo: empieza con 1-2 conceptos, añade 1-2/año validando demanda. Roadmap 12 meses para llegar a 6 conceptos. Top 5 mejores conceptos para empezar + 4 sub-explotados (oportunidad). Modelo escalable y validado España 2026.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-1.jpg',
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-2.jpg',
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-3.jpg',
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-4.jpg',
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-5.jpg',
  '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-6.jpg',
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
              11 entregables profesionales con datos reales del mercado español 2026 para montar tu catering temático multi-concepto premium con 12 cocinas del mundo en portafolio.
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
