import {
  Thermometer, SprayCan, Truck, Bug, AlertTriangle,
  Droplets, ClipboardCheck, ShieldCheck, GraduationCap,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Thermometer, title: 'Control de Temperaturas', desc: '2 plantillas: registro diario (cámaras, congeladores, exposición) con alertas automáticas OK/ALERTA + control en recepción de mercancías con límites por tipo de producto. Las celdas cambian cuando la temperatura sale del rango legal.' },
  { icon: SprayCan, title: 'Limpieza y Desinfección', desc: 'Plan maestro L+D con 25+ zonas pre-rellenadas (cocina, sala, baños, almacén) + registro diario por turno con checklist imprimible. Define qué se limpia, cuándo, cómo, con qué producto y quién lo hace.' },
  { icon: Truck, title: 'Recepción y Trazabilidad', desc: 'Checklist de recepción con verificación de temperatura, caducidad, etiquetado y estado del envase + registro de trazabilidad completo con lote, proveedor y destino. Localiza cualquier producto en menos de 4 horas.' },
  { icon: AlertTriangle, title: 'Alérgenos', desc: 'Matriz de los 14 alérgenos obligatorios × todos los platos de tu carta con desplegables S/T/N (contiene, trazas, no contiene) + fichas imprimibles de cada alérgeno para cocina y sala. Cumple el Reglamento UE 1169/2011.' },
  { icon: Droplets, title: 'Aceite y Agua', desc: 'Control de aceite de fritura con test de compuestos polares y alertas (OK/VIGILAR/CAMBIAR) + registro de agua potable con niveles de cloro. Cumple RD 2207/1995 y RD 140/2003.' },
  { icon: ClipboardCheck, title: 'HACCP y Acciones Correctivas', desc: 'Análisis de peligros completo pre-rellenado con 13 peligros tipo en 6 fases del proceso (recepción → servicio) + registro de acciones correctivas con causa, medida y verificación.' },
  { icon: Bug, title: 'Control de Plagas', desc: 'Registro de actuaciones DDD (desinsectación, desratización, desinfección) con tipo, empresa, productos, zonas y certificados. Calendario de revisiones y espacio para plano de cebos.' },
  { icon: ShieldCheck, title: 'Guía de Inspección', desc: 'Los 25 puntos que revisa el inspector de Sanidad con nivel de gravedad (GRAVE/MODERADA/LEVE). Autoevalúa tu establecimiento antes de la inspección. Incluye resumen automático de cumplimiento.' },
  { icon: GraduationCap, title: 'Higiene y Formación', desc: 'Checklist de higiene personal imprimible para vestuario + registro de formación del personal en seguridad alimentaria. Normas de indumentaria, lavado de manos, conducta y certificaciones.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg',
  '/lovable-uploads/ai-gallery/milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
  '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg',
  '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">17</span> Plantillas de Seguridad Alimentaria
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla incluye fórmulas automáticas, alertas visuales, datos pre-rellenados y formato listo para imprimir.
            </p>
          </div>
        </FadeIn>

        {/* Gallery strip */}
        <FadeIn>
          <div className="grid grid-cols-3 md:grid-cols-6 gap-2 mb-12 rounded-xl overflow-hidden">
            {galleryImages.map((src, i) => (
              <div key={i} className="aspect-square overflow-hidden rounded-lg">
                <img
                  src={src}
                  alt=""
                  className="w-full h-full object-cover hover:scale-110 transition-transform duration-500"
                  loading="lazy"
                />
              </div>
            ))}
          </div>
        </FadeIn>

        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {templates.map(({ icon: Icon, title, desc }, i) => (
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
