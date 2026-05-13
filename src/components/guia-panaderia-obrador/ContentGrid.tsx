import {
  Wheat, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Package,
  FlaskConical, Croissant, FileSpreadsheet, Store,
  Users, Clock, Sun, Recycle, Megaphone, Award,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Wheat, num: '01', title: 'Qué es una Panadería con Obrador', desc: 'Modelo artesanal con producción propia desde harina. Ticket medio 4,80-8,50€, margen 45-58%.' },
  { icon: TrendingUp, num: '02', title: 'El Sector de la Panadería Artesanal 2026', desc: '30.500 establecimientos España, masa madre pasa del 14% al 26% del mercado, +9% interanual.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio Panadería', desc: 'Obrador+tienda, despacho, panadería-bistró y boutique especializada. Inversión 35K-250K€.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 120K-200K€, food cost 18-22%, EBITDA 15-22%, break-even mes 8-14.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales España 2026', desc: 'RGSEAA + licencia clasificada + salida humos + APPCC + Verifactu + control horario digital.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC Obrador + Alérgenos Cruzados', desc: 'Trazabilidad harinas, contaminación gluten/sin gluten, control plagas en silos.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Salida humos viable (killer), paso peatonal, 60-90 m², trifásica 30 kW mínimo.' },
  { icon: Layout, num: '08', title: 'Diseño del Obrador Profesional', desc: 'Flujo lineal harina → pan: amasado, división, fermentación, horneado, enfriamiento.' },
  { icon: Wrench, num: '09', title: 'Equipamiento Profesional', desc: 'Hornos piso vs rotativo, amasadora espiral, cámara fermentación, divisora, formadora.' },
  { icon: Package, num: '10', title: 'Materias Primas: Harinas y Proveedores', desc: 'T55/T65/T80/T110, espelta, centeno, kamut. Vilafranquina, Claudio Aponte, Puratos.' },
  { icon: FlaskConical, num: '11', title: 'Masa Madre y Fermentaciones Largas', desc: 'Líquida vs sólida, refrescos diarios, plan fermentación 18-72h por tipo de pan.' },
  { icon: Croissant, num: '12', title: 'Carta de Producto: 25 Referencias', desc: '12 panes + 8 bollerías + 5 pastelerías. Rotación semanal pan especial del chef.' },
  { icon: FileSpreadsheet, num: '13', title: 'Pricing y Escandallos por Tipo', desc: 'Food cost real 14-26% según pan. Escandallos masa madre, baguette, croissant, sin gluten.' },
  { icon: Store, num: '14', title: 'Diseño de Tienda y Vitrina', desc: 'Vitrina seca pan + refrigerada bollería. Cestos mimbre, etiquetado kraft, iluminación cálida.' },
  { icon: Users, num: '15', title: 'Brigada de Obrador', desc: 'Panadero of.1ª + ayudante + bollero + dependientes. Salarios España 2026 + plus nocturnidad.' },
  { icon: Clock, num: '16', title: 'Operativa Diaria del Obrador', desc: 'Jornada 03:00-11:00: refresco masa madre, formado, fermentación final, hornadas.' },
  { icon: Sun, num: '17', title: 'Plan de Producción Semanal', desc: 'Ajuste tirada por día de la semana + clima + festivos. Reducir mermas con histórico.' },
  { icon: Recycle, num: '18', title: 'Mermas y Devoluciones Cero Residuos', desc: 'Pan del día -40% / 2 días donación Banco Alimentos. Reduce mermas 12% → 4%.' },
  { icon: Megaphone, num: '19', title: 'Marketing Local + Digital + B2B Horeca', desc: 'Google Local, Instagram obrador, suscripción pan semanal, contratos restaurantes y hoteles.' },
  { icon: Award, num: '20', title: 'Casos Éxito y Roadmap Escalado', desc: 'Levaduramadre, Panic, Crustó, Hofmann. Escalado a 2º local, obrador central o franquicia.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-panaderia-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-panaderia-1.jpg',
  '/lovable-uploads/ai-gallery/guia-panaderia-2.jpg',
  '/lovable-uploads/ai-gallery/guia-panaderia-3.jpg',
  '/lovable-uploads/ai-gallery/guia-panaderia-4.jpg',
  '/lovable-uploads/ai-gallery/guia-panaderia-5.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">20</span> Capítulos + 9 Plantillas + 6 Checklists + 2 Documentos
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Todo lo que necesitas saber para montar tu panadería con obrador en España, con recetario de masa madre y planes de fermentación 18-72h.
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
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {chapters.map(({ icon: Icon, num, title, desc }, i) => (
            <FadeIn key={title} delay={i * 40}>
              <div className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/50 transition-all duration-300 h-full">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-[#FFD700] text-xs font-bold opacity-50">{num}</span>
                  <Icon className="w-6 h-6 text-[#FFD700]" />
                </div>
                <h3 className="text-white font-semibold text-sm mb-1.5">{title}</h3>
                <p className="text-gray-400 text-xs leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
