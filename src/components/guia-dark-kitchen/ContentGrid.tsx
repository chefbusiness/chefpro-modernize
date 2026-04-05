import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Tablet, Package, Rocket,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: '¿Qué es una Dark Kitchen?', desc: 'Definiciones, origen del modelo y diferencias clave con un restaurante tradicional.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado Delivery en España', desc: 'Datos de Glovo, Uber Eats, Just Eat. Ciudades con mayor demanda y ticket medio.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio', desc: 'Marca única, multi-marca, cocina compartida, franquicia virtual. Pros y contras.' },
  { icon: Calculator, num: '04', title: 'Viabilidad y Plan Financiero', desc: 'Inversión (30K-80K€), costes, break-even y márgenes reales tras comisiones.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales en España', desc: 'Licencia de actividad, registro sanitario, Hacienda, seguros, LOPD.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad, alérgenos, temperaturas, inspecciones.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas industriales vs. comerciales, metros mínimos, ventilación, acceso riders.' },
  { icon: Layout, num: '08', title: 'Diseño y Layout de Cocina', desc: 'Flujo delivery-only: recepción, preparación, emplatado, expedición.' },
  { icon: Wrench, num: '09', title: 'Equipamiento y Proveedores', desc: 'Lista completa con costes: hornos, freidoras, cámaras, estanterías.' },
  { icon: Tablet, num: '10', title: 'Tecnología y Gestión de Pedidos', desc: 'Integradores, TPV, KDS, gestión de stock, automatización.' },
  { icon: Package, num: '11', title: 'Packaging y Sostenibilidad', desc: 'Envases delivery, temperatura de llegada, branding, normativa plásticos 2026.' },
  { icon: Rocket, num: '12', title: 'Marketing y Lanzamiento', desc: 'Alta en plataformas, fotos, promos de lanzamiento y 10 errores fatales.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-dk-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-dk-packaging.jpg',
  '/lovable-uploads/ai-gallery/guia-dk-tablets.jpg',
  '/lovable-uploads/ai-gallery/guia-dk-delivery.jpg',
  '/lovable-uploads/ai-gallery/guia-dk-plano.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">12</span> Capítulos + 3 Checklists + Calculadora
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Todo lo que necesitas saber para montar tu dark kitchen en España, escrito por un profesional con 29 años en hostelería.
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
