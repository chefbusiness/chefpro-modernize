import {
  FileText, Coins, Calculator, Truck, Wrench, ShieldCheck,
  Utensils, ScrollText, Sparkles, Flame, BookOpen,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, segmentación dual B2C íntimo + B2B corporate, modelo sin local fijo, anexo regulación CCAA catering itinerante, financiero 3 años, riesgos, roadmap.' },
  { icon: Coins, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 40 % + B2B 60 %, inversión 4.500-30.000 EUR según escenario, sin estacionalidad fuerte (picos diciembre + verano), break-even por número de eventos.' },
  { icon: Calculator, title: 'Calculadora Pricing B2C + B2B', desc: 'Excel con fórmulas duales B2C cena íntima + B2B corporate showcooking. Inputs: pax, distancia, tipo experiencia, nivel menú (estándar/premium/exclusivo), pairing, branded ⇒ precio sugerido + margen. 10 ejemplos validados.' },
  { icon: Truck, title: 'Plantilla 96 Proveedores Reales', desc: 'Cuchillería japonesa (Tojiro, Yoshihiro, Kai Shun) + sous-vide Anova/Polyscience + vajilla Pordamsa/Steelite/Schönwald + carniceros premium (Cesáreo Gómez, Discarlux) + AOVE DO Castillo de Canena + microbrotes + caviar Riofrío + trufa Soria.' },
  { icon: Wrench, title: 'Catálogo Equipamiento + Cuchillería', desc: 'Cuchillería japonesa (gyuto, petty, sujihiki) + inducción portátil Vollrath/Iwatani + sous-vide + vajilla blanca premium + cristalería + uniformidad chef + furgoneta. Marcas, modelos y precios validados.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil + RGSEAA) · seguros RC eventos con cláusula intoxicación · cuchillería + vajilla + proveedores premium · marca y portfolio · captación B2C+B2B · operativa primer evento. 108 hitos.' },
  { icon: Utensils, title: 'Carta 12 Menús Temáticos', desc: 'Tasting menu degustación 7 pasos + brunch dominical premium + cena maridajes + mediterránea tradicional + asiático fusión showcooking + mexicano premium + ruta tapas privada + caprice del chef + vegetariano + healthy + mariscada premium + Navidad privada.' },
  { icon: ScrollText, title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, aniversarios, San Valentín, Navidad) + B2B corporate (cena directiva, showcooking, hotel, wedding planner) con confidencialidad, MSA y propiedad intelectual del menú.' },
  { icon: Sparkles, title: '10 Experiencias Temáticas', desc: 'Cena romántica San Valentín · cumpleaños familiar · aniversario boda · brunch dominical · cena ejecutiva pairing · showcooking corporate 30-80 pax · cooking class team-building · hotel boutique in-suite · cena ensayo pre-boda · cena directiva fin año.' },
  { icon: Flame, title: 'Manual Técnico Servicio Domicilio', desc: '7 PCC APPCC móvil (recepción, cadena frío, manipulación, cocción, servicio, alérgenos, limpieza) + cronograma evento 8 pax + estaciones de trabajo en cocina del cliente + coordinación servicio en mesa + documentación obligatoria.' },
  { icon: BookOpen, title: 'Guía Sistemas: Chef vs Personal vs Caterer', desc: 'Definición y modelo de cada figura · ticket medio · ICP · margen neto · inversión inicial · cuándo elegir cada figura · modelos híbridos válidos · riesgo de confundir las figuras al posicionarse comercialmente.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-1.jpg',
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-2.jpg',
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-3.jpg',
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-4.jpg',
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-5.jpg',
  '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-6.jpg',
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
              11 entregables profesionales con datos reales del mercado español 2026 para validar la viabilidad de tu servicio premium de chef privado y showcooking a domicilio.
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
