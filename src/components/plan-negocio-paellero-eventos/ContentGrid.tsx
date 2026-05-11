import {
  FileText, Coins, Calculator, Truck, Wrench, ShieldCheck,
  Utensils, ScrollText, Sparkles, Flame, Tent,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, 10 competidores reales, doble embudo B2C+B2B, marco legal CCAA fuego al aire libre, financiero 3 años, riesgos, roadmap 3 años.' },
  { icon: Coins, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 3.500-25.000 EUR según escenario, estacionalidad mayo-octubre + Falles, break-even por número de eventos.' },
  { icon: Calculator, title: 'Calculadora Pricing Eventos', desc: 'Excel con fórmulas duales B2C particular + B2B planner. Inputs: pax, distancia, tipo de paella, concepto premium, ayudantes ⇒ precio sugerido + margen. 10 ejemplos validados.' },
  { icon: Truck, title: 'Plantilla 88 Proveedores Reales', desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Calasparra), carniceros, mariscos Mediterráneo, verduras Levante (garrofó, ferraura), azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa.' },
  { icon: Wrench, title: 'Catálogo Equipamiento + Menaje', desc: 'Paelleras Garcima 60-90-120 cm + paellero Vaello 4 fuegos 50 kW + trípode leña + cuchillería Arcos + vajilla Pordamsa + EPI Texfire. SKU + URL + precio actualizado.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC + RGSEAA) · seguros RC eventos con cláusula intoxicación · equipamiento + arroceros DO · marca y web · captación B2C+B2B · operativa primer evento. 110 hitos.' },
  { icon: Utensils, title: 'Carta 12 Paellas y Arroces', desc: 'Valenciana DO + marisco premium + senyoret + arroz negro + mixta + arroz a banda + fideuá + meloso bogavante + caldoso bogavante + montaña + alicantina con costra + vegetal DO. Receta + escandallo + maridaje.' },
  { icon: ScrollText, title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias, ayuntamientos) con anexo tarifario, briefing y SLA.' },
  { icon: Sparkles, title: '10 Experiencias Temáticas', desc: 'Boda en finca · corporate showcooking · fiesta del pueblo popular · bautizo familiar · cumpleaños senyoret · Falles + festes · boda exclusiva 5* · hotel show cooking · vegetal DO inclusive · brunch banda + fideuá.' },
  { icon: Flame, title: 'Manual Técnico Paellero', desc: 'Técnica del fuego en 4 fases (sofrito, proteínas, caldo+arroz, socarrat) + 6 tipos arroz Bomba/Sendra/Albufera + 3 caldos pro + salmueras + tabla cocción 12 paellas + 4 salsas + errores frecuentes.' },
  { icon: Tent, title: 'Guía 8 Sistemas + Food Truck', desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico inducción, gas industrial, portátil camping, caja china peruana, paellero solar. + Roadmap food truck arrocería: inversión 30-75K EUR, regulación 8 CCAA.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-1.jpg',
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-3.jpg',
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-5.jpg',
  '/lovable-uploads/ai-gallery/plan-paellero-eventos-6.jpg',
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
              11 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu servicio premium itinerante de paella y arroces.
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
