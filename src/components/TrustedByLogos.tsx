import { useTranslation } from 'react-i18next';

const logos = [
  // Hoteles
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  { src: '/logos/villa-cortes-hotel.png', alt: 'Villa Cortés Deluxe Hotel' },
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
  // Escuelas & Formación
  { src: '/logos/hecansa-canarias.png', alt: 'Hecansa Hoteles Escuela de Canarias' },
  { src: '/logos/basque-culinary-center.png', alt: 'Basque Culinary Center' },
  // Alimentación & Proveedores
  { src: '/logos/albi-alimentacion.png', alt: 'Albi Alimentación & Bienestar' },
  // Grupos Empresariales & Innovación
  { src: '/logos/venture-group-tenerife.png', alt: 'Venture Group Tenerife' },
  { src: '/logos/labe.png', alt: 'Lab-e' },
];

export default function TrustedByLogos() {
  const { t } = useTranslation();

  return (
    <section className="py-10 md:py-12 bg-muted/30 overflow-hidden">
      <div className="container mb-8">
        <h2 className="text-center text-sm md:text-base lg:text-lg font-semibold text-muted-foreground uppercase tracking-wide leading-relaxed max-w-4xl mx-auto">
          {t('trusted_by.title')}
        </h2>
      </div>
      
      <div className="relative">
        {/* Fade edges */}
        <div className="absolute left-0 top-0 bottom-0 w-16 md:w-32 bg-gradient-to-r from-muted/30 to-transparent z-10 pointer-events-none" />
        <div className="absolute right-0 top-0 bottom-0 w-16 md:w-32 bg-gradient-to-l from-muted/30 to-transparent z-10 pointer-events-none" />
        
        <div className="logo-track flex items-center gap-12 md:gap-16 lg:gap-20">
          {/* Duplicate logos for infinite loop effect */}
          {[...logos, ...logos, ...logos, ...logos].map((logo, i) => (
            <img 
              key={i}
              src={logo.src} 
              alt={logo.alt}
              loading="lazy"
              className="h-12 md:h-16 lg:h-20 w-auto flex-shrink-0 opacity-70 hover:opacity-100 transition-all duration-300 grayscale hover:grayscale-0"
            />
          ))}
        </div>
      </div>
    </section>
  );
}
