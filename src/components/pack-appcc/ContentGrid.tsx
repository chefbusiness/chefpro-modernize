import {
  Thermometer, SprayCan, Truck, Bug, AlertTriangle,
  Droplets, ClipboardCheck, ShieldCheck, GraduationCap, Flame,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Thermometer, title: 'Control de Temperaturas', desc: '2 plantillas: registro diario (cámaras, congeladores, exposición) con alertas automáticas OK/ALERTA + control en recepción de mercancías con límites por tipo de producto. Las celdas cambian cuando la temperatura sale del rango legal.' },
  { icon: SprayCan, title: 'Limpieza y Desinfección', desc: 'Plan maestro L+D con 32 zonas pre-rellenadas (cocina, sala, baños, almacén, vestuarios y exterior: terraza, contenedores y cámara de residuos) + registro diario por turno con checklist imprimible. Define qué se limpia, cuándo, cómo, con qué producto y quién lo hace.' },
  { icon: Truck, title: 'Recepción y Trazabilidad', desc: 'Checklist de recepción con verificación de temperatura, caducidad, etiquetado y estado del envase + registro de trazabilidad completo con lote, proveedor y destino, más la pestaña de salida y uso interno. Responde de inmediato a la autoridad: de qué proveedor vino cada lote y en qué elaboración y servicio acabó.' },
  { icon: AlertTriangle, title: 'Alérgenos', desc: 'Matriz de los 14 alérgenos obligatorios × todos los platos de tu carta con desplegables S/T/N (contiene, trazas, no contiene) + fichas imprimibles de cada alérgeno para cocina y sala. Cumple el Reglamento UE 1169/2011.' },
  { icon: Droplets, title: 'Aceite y Agua', desc: 'Control de aceite de fritura con test de compuestos polares y alertas (OK/VIGILAR/CAMBIAR) + registro de agua potable con niveles de cloro. Cumple la Orden de 26 de enero de 1989 y el RD 3/2023.' },
  { icon: ClipboardCheck, title: 'HACCP y Acciones Correctivas', desc: 'Análisis de peligros completo pre-rellenado con 21 peligros tipo en 7 fases del proceso (recepción → servicio), cada uno con su registro del pack detrás + registro de acciones correctivas con causa, medida y verificación.' },
  { icon: Bug, title: 'Control de Plagas', desc: 'Registro de actuaciones DDD (desinsectación, desratización, desinfección) con tipo, empresa, productos, zonas y certificados. Calendario de revisiones y espacio para plano de cebos.' },
  { icon: ShieldCheck, title: 'Guía de Inspección', desc: 'Los 25 puntos que revisa el inspector de Sanidad con nivel de gravedad (Leve / Grave / Muy grave, Ley 17/2011). Autoevalúa tu establecimiento antes de la inspección. Incluye resumen automático de cumplimiento.' },
  { icon: GraduationCap, title: 'Higiene y Formación', desc: 'Checklist de higiene personal imprimible para vestuario + registro de formación del personal en seguridad alimentaria. Normas de indumentaria, lavado de manos, conducta y certificaciones.' },
  { icon: Flame, title: 'Cocción, Enfriamiento y Anisakis', desc: '4 registros nuevos que cierran los PCC que el análisis de peligros ya citaba y no tenían ficha detrás: temperatura en el centro del producto (≥75 °C y, en regeneración, en menos de una hora), enfriamiento de 60 a 10 °C en 2 horas, congelación preventiva de anisakis (−20 °C durante 24 h o −35 °C durante 15 h) y verificación mensual de termómetros y sondas.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/appcc-control-temperaturas.jpeg',
  '/lovable-uploads/ai-gallery/appcc-limpieza-cocina.jpeg',
  '/lovable-uploads/ai-gallery/appcc-recepcion-mercancias.jpeg',
  '/lovable-uploads/ai-gallery/appcc-alergenos-carta.jpeg',
  '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg',
  '/lovable-uploads/ai-gallery/appcc-registro-plantilla.jpeg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">19</span> Plantillas de Seguridad Alimentaria
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Los 12 registros de medición traen Estado calculado y semáforo automático; los planes, checklists y carteles llegan desarrollados y listos para imprimir en A4.
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
