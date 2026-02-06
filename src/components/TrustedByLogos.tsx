import { useTranslation } from 'react-i18next';
import { Badge } from '@/components/ui/badge';
import { Sparkles } from 'lucide-react';

const logos = [
  // Hoteles & Wellness
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  { src: '/logos/villa-cortes-hotel.png', alt: 'Villa Cortés Deluxe Hotel' },
  { src: '/logos/shawellness.png', alt: 'SHA Masters of Longevity' },
  // Aerolíneas
  { src: '/logos/qatar-airways.png', alt: 'Qatar Airways' },
  { src: '/logos/singapore-airlines.png', alt: 'Singapore Airlines' },
  // Restaurantes/Bares/Chefs
  { src: '/logos/fierro.png', alt: 'Fierro by Carito y Germán' },
  { src: '/logos/stillroom.png', alt: 'Stillroom - El Arte de lo Invisible' },
  { src: '/logos/taste-1973.png', alt: '1973 Taste Restaurant' },
  { src: '/logos/grupo-dani-garcia.png', alt: 'Grupo Dani García' },
  // Grupos Hostelería & Restauración
  { src: '/logos/amrest-group.png', alt: 'AmRest Group' },
  { src: '/logos/restaurant-brands-europe.png', alt: 'Restaurant Brands Europe' },
  { src: '/logos/tragaluz.png', alt: 'Grupo Tragaluz' },
  { src: '/logos/la-maquina.png', alt: 'La Máquina Grupo de Restauración' },
  // Escuelas & Formación
  { src: '/logos/hecansa-canarias.png', alt: 'Hecansa Hoteles Escuela de Canarias' },
  { src: '/logos/basque-culinary-center.png', alt: 'Basque Culinary Center' },
  { src: '/logos/hosteleria-leioa.png', alt: 'Ostalaritza Leioa Hostelería' },
  // Alimentación & Proveedores
  { src: '/logos/albi-alimentacion.png', alt: 'Albi Alimentación & Bienestar' },
  // Grupos Empresariales & Innovación
  { src: '/logos/venture-group-tenerife.png', alt: 'Venture Group Tenerife' },
  { src: '/logos/labe.png', alt: 'Lab-e' },
];

export default function TrustedByLogos() {
  const { t } = useTranslation();

  return (
    <section className="relative py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 overflow-hidden">
      {/* Borde superior dorado */}
      <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-amber-500/60 to-transparent" />
      
      {/* Header con badge y título */}
      <div className="container mb-10">
        <div className="flex flex-col items-center gap-4">
          {/* Badge dorado */}
          <Badge 
            variant="outline" 
            className="border-amber-500/50 bg-amber-500/10 text-amber-400 px-4 py-1.5 text-sm font-medium backdrop-blur-sm"
          >
            <Sparkles className="w-3.5 h-3.5 mr-1.5" />
            {t('trusted_by.badge')}
          </Badge>
          
          {/* Título principal */}
          <h2 className="text-center text-lg md:text-xl lg:text-2xl font-bold text-white/95 uppercase tracking-wide leading-relaxed max-w-4xl mx-auto">
            {t('trusted_by.title')}
          </h2>
          
          {/* Separador dorado decorativo */}
          <div className="flex items-center gap-3 mt-2">
            <div className="w-12 md:w-20 h-px bg-gradient-to-r from-transparent to-amber-500/60" />
            <div className="w-2 h-2 rounded-full bg-amber-500/80" />
            <div className="w-12 md:w-20 h-px bg-gradient-to-l from-transparent to-amber-500/60" />
          </div>
        </div>
      </div>
      
      {/* Carrusel de logos */}
      <div className="relative">
        {/* Fade edges para fondo oscuro */}
        <div className="absolute left-0 top-0 bottom-0 w-20 md:w-40 bg-gradient-to-r from-slate-900 to-transparent z-10 pointer-events-none" />
        <div className="absolute right-0 top-0 bottom-0 w-20 md:w-40 bg-gradient-to-l from-slate-900 to-transparent z-10 pointer-events-none" />
        
        <div className="logo-track flex items-center gap-12 md:gap-16 lg:gap-20">
          {/* Duplicate logos for infinite loop effect */}
          {[...logos, ...logos, ...logos, ...logos].map((logo, i) => (
            <div 
              key={i}
              className="flex-shrink-0 bg-white/10 backdrop-blur-sm rounded-xl p-3 md:p-4 logo-glow transition-all duration-300"
            >
              <img 
                src={logo.src} 
                alt={logo.alt}
                loading="lazy"
                className="h-10 md:h-12 lg:h-14 w-auto object-contain"
              />
            </div>
          ))}
        </div>
      </div>
      
      {/* Borde inferior dorado */}
      <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-amber-500/60 to-transparent" />
    </section>
  );
}
