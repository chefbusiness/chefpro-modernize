import {
  FileText, Coins, Calculator, Truck, Wrench, ShieldCheck,
  Beef, ScrollText, Sparkles, Flame, Tent,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, 10 competidores reales, doble embudo B2C+B2B, marco legal CCAA fuego, financiero 3 años, riesgos, roadmap 3 años.' },
  { icon: Coins, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 40 % + B2B 60 %, inversión 3.500-25.000 EUR según escenario, estacionalidad mayo-septiembre 70 %, break-even 8-10 eventos año 1.' },
  { icon: Calculator, title: 'Calculadora Pricing Eventos', desc: 'Excel con fórmulas duales B2C particular + B2B planner. Inputs: pax, distancia, concepto, ayudantes ⇒ precio sugerido + margen. Con 10 ejemplos validados.' },
  { icon: Truck, title: 'Plantilla 96 Proveedores Reales', desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas), GGM Gastro (parrillas), Tienda Biomasa (carbón quebracho), Texfire (EPI), Hosply.pro y más.' },
  { icon: Wrench, title: 'Catálogo Equipamiento + Menaje', desc: 'Parrilla GGM KGE1200 709 EUR + Brogas asador cruz + Comander COMPER-M ahumador + cuchillería Arcos + vajilla eventos + EPI Texfire. SKU + URL + precio.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC) · seguros RC eventos · equipamiento + carniceros · marca y web · captación B2C+B2B · operativa primer evento.' },
  { icon: Beef, title: 'Carta 12 Cortes de Carne', desc: 'Argentinos (asado tira, bife chorizo, vacío) + castellanos (cordero a la cruz, cochinillo) + ibéricos (pluma, secreto) + BBQ texano (brisket, ribs). Técnica + Tº + merma + maridaje.' },
  { icon: ScrollText, title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias) con anexo tarifario y SLA.' },
  { icon: Sparkles, title: '10 Experiencias Temáticas', desc: 'Asado argentino, asador a la cruz, parrilla uruguaya, BBQ texano, rodizio brasileño, asador criollo, mediterránea, llanera, show de fuego y brunch parrillero corporate.' },
  { icon: Flame, title: 'Manual Técnico Parrillero', desc: '8 salmueras + 12 marinados + tabla cocción 18 cortes con Tº interna y merma + chimichurri 3 versiones + 5 salsas profesionales. Lo que separa al amateur del profesional.' },
  { icon: Tent, title: 'Guía 8 Sistemas + Food Truck', desc: 'Comparativa parrilla argentina, asador cruz, BBQ pit, caja china, barril llanero, modular inox, brasero, lift-grill. + Roadmap food truck especializado: inversión 30-75K EUR, regulación 8 CCAA.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-1.jpg',
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-3.jpg',
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-4.jpg',
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-5.jpg',
  '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
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
              11 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu servicio premium itinerante de parrilla y asado.
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
