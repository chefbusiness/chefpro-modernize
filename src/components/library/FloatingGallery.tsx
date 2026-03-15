const BASE = '/lovable-uploads/ai-gallery';

const row1 = [
  'tataki-presa-iberica-chimichurri.jpeg',
  'tartaleta-de-yuzu-y-merengue.jpeg',
  'cocktail-green-margarita.jpeg',
  'croqueta-jamon.jpeg',
  'croissant-bicolor-de-mantequilla-aichefpro.jpeg',
  'huevo-baja-temperatura-trufa.jpeg',
  'ostra-aire-gintonic.jpeg',
  'gambas-al-ajillo.jpeg',
];

const row2 = [
  'focaccia-jardin-alta-hidratacion-aichefpro.jpeg',
  'cochinillo-asado.jpeg',
  'carpaccio-gambas.jpeg',
  'cocktail-garibaldi-fermentado.jpeg',
  'milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
  'aceitunas-liquidas.jpeg',
  'torrija-caramelizada-con-helado.jpeg',
  'gazpacho-clasico.jpeg',
];

const row3 = [
  'falso-risotto-semillas-plancton.jpeg',
  'cocktail-tepache-pina-asada.jpeg',
  'hogaza-masa-madre-oreja-perfecta-aichefpro.jpeg',
  'canelon-aguacate-cangrejo.jpeg',
  'cocktail-gin-game.jpeg',
  'cocktail-super-fashion.jpeg',
  'tres-tostadas-francesas-aichefpro.jpeg',
  'innovacion-diseno-restaurantes-2.jpeg',
];

function MarqueeRow({ images, reverse = false, duration = 40 }: { images: string[]; reverse?: boolean; duration?: number }) {
  // Duplicate for seamless loop
  const doubled = [...images, ...images];

  return (
    <div className="overflow-hidden py-1.5">
      <div
        className={`flex gap-3 ${reverse ? 'animate-marquee-reverse' : 'animate-marquee'}`}
        style={{ animationDuration: `${duration}s` }}
      >
        {doubled.map((img, i) => (
          <div
            key={`${img}-${i}`}
            className="flex-shrink-0 w-32 h-20 md:w-44 md:h-28 rounded-lg overflow-hidden"
          >
            <img
              src={`${BASE}/${img}`}
              alt=""
              className="w-full h-full object-cover"
              loading="lazy"
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default function FloatingGallery() {
  return (
    <div className="relative overflow-hidden py-6">
      {/* Fade edges */}
      <div className="absolute inset-y-0 left-0 w-1/4 bg-gradient-to-r from-[#0a0a0a] to-transparent z-10 pointer-events-none" />
      <div className="absolute inset-y-0 right-0 w-1/4 bg-gradient-to-l from-[#0a0a0a] to-transparent z-10 pointer-events-none" />
      {/* Fade top/bottom */}
      <div className="absolute inset-x-0 top-0 h-8 bg-gradient-to-b from-[#0a0a0a] to-transparent z-10 pointer-events-none" />
      <div className="absolute inset-x-0 bottom-0 h-8 bg-gradient-to-t from-[#0a0a0a] to-transparent z-10 pointer-events-none" />

      <div className="opacity-40 space-y-3">
        <MarqueeRow images={row1} duration={50} />
        <MarqueeRow images={row2} reverse duration={60} />
        <MarqueeRow images={row3} duration={55} />
      </div>
    </div>
  );
}
