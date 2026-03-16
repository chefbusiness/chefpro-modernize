import { Helmet } from 'react-helmet-async';
import { ArrowRight, BookOpen, FileSpreadsheet, Star, Check, Clock, MessageSquare, ShieldCheck, BarChart3, Utensils, GraduationCap, Palette, Wine } from 'lucide-react';

const products = [
  {
    name: 'Gastro Pro Prompts eBook',
    slug: '/pro-prompts-ebook',
    price: '€9',
    originalPrice: '€50',
    discount: '-90%',
    description: 'Más de 300 prompts de inteligencia artificial específicos para hostelería y restauración. Cocina creativa, pastelería, catering, gestión de equipos, marketing, prompt engineering y más.',
    features: [
      'eBook PDF + Dashboard exclusivo',
      '300+ prompts organizados por categoría',
      '8 herramientas gratuitas incluidas',
      'Compatible con ChatGPT, Claude, Gemini y más',
      'Actualizaciones gratuitas de por vida',
    ],
    icon: BookOpen,
    image: '/ebook-mockup-bundle.webp',
    badge: 'Bestseller',
    badgeColor: 'bg-[#FFD700]/20 text-[#FFD700]',
  },
  {
    name: 'Kit de Escandallos Pro',
    slug: '/kit-escandallos',
    price: '€12',
    originalPrice: '€49',
    discount: '-75%',
    description: '11 plantillas de escandallos en Excel con fórmulas automáticas, mermas precargadas y calculadora de PVP. Controla el food cost real de cada plato de tu restaurante.',
    features: [
      '11 plantillas Excel profesionales',
      'Mermas estándar de la industria precargadas',
      'Calculadora de PVP para 9 tipos de establecimiento',
      'Dashboard de Food Cost mensual',
      'Acceso de por vida + actualizaciones',
    ],
    icon: FileSpreadsheet,
    image: '/kit-escandallos-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-emerald-500/20 text-emerald-400',
  },
];

export default function ProductosDigitales() {
  return (
    <>
      <Helmet>
        <title>Productos Digitales para Hostelería — Prompts IA, Plantillas Excel | AI Chef Pro</title>
        <meta name="description" content="eBooks, plantillas Excel, prompts de IA y herramientas digitales para chefs, gerentes y dueños de restaurante. Recursos profesionales desde €9. Por AI Chef Pro." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="productos digitales hostelería, prompts IA restaurante, plantilla escandallo excel, ebook hostelería, herramientas digitales restaurante, food cost excel, ChatGPT restaurante, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/productos-digitales" />

        {/* Open Graph */}
        <meta property="og:title" content="Productos Digitales para Hostelería — AI Chef Pro" />
        <meta property="og:description" content="eBooks, plantillas Excel y prompts de IA para profesionales de hostelería. Desde €9." />
        <meta property="og:url" content="https://aichef.pro/productos-digitales" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-image.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Productos Digitales para Hostelería — AI Chef Pro" />
        <meta name="twitter:description" content="eBooks, plantillas Excel y prompts de IA para profesionales de hostelería." />
        <meta name="twitter:image" content="https://aichef.pro/og-image.jpg" />

        {/* CollectionPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "CollectionPage",
          "name": "Productos Digitales para Hostelería — AI Chef Pro",
          "description": "eBooks, plantillas Excel, prompts de IA y herramientas digitales para chefs, gerentes y dueños de restaurante.",
          "url": "https://aichef.pro/productos-digitales",
          "publisher": {
            "@type": "Organization",
            "name": "AI Chef Pro",
            "url": "https://aichef.pro"
          },
          "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "url": "https://aichef.pro/pro-prompts-ebook",
                "name": "Gastro Pro Prompts eBook — 300+ prompts de IA para hostelería"
              },
              {
                "@type": "ListItem",
                "position": 2,
                "url": "https://aichef.pro/kit-escandallos",
                "name": "Kit de Escandallos Pro — 11 Plantillas Excel Profesionales"
              }
            ]
          }
        })}</script>

        {/* BreadcrumbList Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        {/* Hero */}
        <section className="relative px-4 pt-24 pb-16 md:pt-32 md:pb-20 overflow-hidden">
          <div className="absolute inset-0" style={{
            background: 'radial-gradient(ellipse 80% 60% at 50% -10%, rgba(255,215,0,0.08) 0%, transparent 70%)',
          }} />

          <div className="relative max-w-4xl mx-auto text-center z-10">
            <span className="inline-block mb-6 px-4 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-sm font-medium">
              Recursos profesionales para hostelería
            </span>

            <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
              Productos <span className="text-[#FFD700]">Digitales</span> para Profesionales de Hostelería
            </h1>

            <p className="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
              eBooks de prompts de inteligencia artificial, plantillas Excel de escandallos, guías profesionales y herramientas digitales. Creados por profesionales del sector para chefs, gerentes, pasteleros, bartenders, catering y dueños de restaurante.
            </p>
          </div>
        </section>

        {/* Products Grid */}
        <section className="px-4 pb-20 md:pb-28">
          <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            {products.map((product) => {
              const Icon = product.icon;
              return (
                <a
                  key={product.slug}
                  href={product.slug}
                  className="group relative bg-white/[0.03] border border-white/10 rounded-2xl overflow-hidden hover:border-[#FFD700]/30 hover:bg-white/[0.05] transition-all duration-300"
                >
                  {/* Badge */}
                  <div className="absolute top-4 right-4 z-10">
                    <span className={`px-3 py-1 rounded-full text-xs font-bold ${product.badgeColor}`}>
                      {product.badge}
                    </span>
                  </div>

                  {/* Image */}
                  <div className="relative h-48 md:h-56 overflow-hidden bg-gradient-to-b from-white/[0.05] to-transparent">
                    <img
                      src={product.image}
                      alt={product.name}
                      className="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500"
                      loading="lazy"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0a] via-transparent to-transparent" />
                  </div>

                  {/* Content */}
                  <div className="p-6 md:p-8">
                    <div className="flex items-center gap-3 mb-3">
                      <div className="w-10 h-10 rounded-xl bg-[#FFD700]/10 flex items-center justify-center">
                        <Icon className="w-5 h-5 text-[#FFD700]" />
                      </div>
                      <h2 className="text-xl font-bold text-white group-hover:text-[#FFD700] transition-colors">
                        {product.name}
                      </h2>
                    </div>

                    <p className="text-gray-400 text-sm leading-relaxed mb-5">
                      {product.description}
                    </p>

                    {/* Features */}
                    <ul className="space-y-2 mb-6">
                      {product.features.map((feature) => (
                        <li key={feature} className="flex items-start gap-2 text-sm text-gray-300">
                          <Check className="w-4 h-4 text-[#FFD700] flex-shrink-0 mt-0.5" />
                          <span>{feature}</span>
                        </li>
                      ))}
                    </ul>

                    {/* Price + CTA */}
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <span className="text-3xl font-extrabold text-[#FFD700]">{product.price}</span>
                        <span className="text-lg text-gray-500 line-through">{product.originalPrice}</span>
                        <span className="px-2 py-0.5 rounded-full bg-[#FFD700]/20 text-[#FFD700] text-xs font-bold">
                          {product.discount}
                        </span>
                      </div>
                      <div className="flex items-center gap-1 text-[#FFD700] text-sm font-medium group-hover:gap-2 transition-all">
                        Ver producto
                        <ArrowRight className="w-4 h-4" />
                      </div>
                    </div>
                  </div>
                </a>
              );
            })}
          </div>
        </section>

        {/* Coming Soon */}
        <section className="px-4 pb-16 md:pb-24">
          <div className="max-w-5xl mx-auto">
            <div className="text-center mb-10">
              <span className="inline-block mb-4 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-gray-400 text-sm font-medium">
                <Clock className="w-4 h-4 inline mr-2" />
                En Desarrollo
              </span>
              <h2 className="text-2xl md:text-3xl font-bold text-white mb-3">
                Próximos <span className="text-[#FFD700]">Productos</span>
              </h2>
              <p className="text-gray-400 text-sm max-w-2xl mx-auto">
                Estamos preparando nuevos recursos digitales para profesionales de hostelería. Cada uno sigue el mismo estándar de calidad: acceso inmediato, actualizaciones de por vida y garantía de 30 días.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {[
                { icon: MessageSquare, name: 'Banco de Respuestas a Reseñas', desc: '200+ respuestas profesionales para Google, TripAdvisor y Yelp', tag: 'Próximamente' },
                { icon: ShieldCheck, name: 'Pack de Plantillas APPCC', desc: 'Registros de temperatura, limpieza, recepción y trazabilidad', tag: 'Próximamente' },
                { icon: BarChart3, name: 'Guía Completa de Food Cost', desc: 'Cálculo, control y optimización del food cost con ejemplos reales', tag: 'Próximamente' },
                { icon: Palette, name: 'Kit de Social Media para Restaurantes', desc: '100+ plantillas de posts, stories y reels + calendario editorial', tag: 'Próximamente' },
                { icon: Utensils, name: 'Manual de Escandallos Profesional', desc: '50+ ejemplos de escandallos por tipo de cocina y establecimiento', tag: 'Próximamente' },
                { icon: GraduationCap, name: 'Curso: Domina la IA en tu Restaurante', desc: '10 módulos progresivos de principiante a avanzado con ejercicios', tag: '2026' },
                { icon: Wine, name: 'Manual de Coctelería y Mixología Moderna', desc: 'Recetas clásicas + creaciones con IA, maridajes y costes', tag: '2026' },
                { icon: BookOpen, name: 'eBook de Marketing Gastronómico con IA', desc: 'Estrategias de marketing digital para restaurantes usando IA', tag: '2026' },
              ].map((item) => {
                const Icon = item.icon;
                return (
                  <div
                    key={item.name}
                    className="bg-white/[0.02] border border-white/[0.06] rounded-xl p-5 opacity-70 hover:opacity-90 transition-opacity"
                  >
                    <div className="flex items-start gap-3 mb-2">
                      <div className="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center flex-shrink-0">
                        <Icon className="w-4 h-4 text-gray-400" />
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2 mb-1">
                          <h3 className="text-sm font-semibold text-white truncate">{item.name}</h3>
                        </div>
                        <p className="text-xs text-gray-500 leading-relaxed">{item.desc}</p>
                      </div>
                    </div>
                    <div className="flex justify-end">
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/5 text-gray-500 font-medium">
                        {item.tag}
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </section>

        {/* Trust section */}
        <section className="px-4 pb-16 md:pb-24">
          <div className="max-w-3xl mx-auto text-center">
            <div className="flex items-center justify-center gap-1 mb-3">
              {Array.from({ length: 5 }).map((_, i) => (
                <Star key={i} className="h-5 w-5 fill-[#FFD700] text-[#FFD700]" />
              ))}
            </div>
            <p className="text-gray-400 text-sm mb-6">
              Valoración media de 4.9/5 por profesionales de hostelería
            </p>
            <div className="flex flex-wrap items-center justify-center gap-6 text-sm text-gray-500">
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Garantía 30 días
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Acceso inmediato
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Actualizaciones gratis
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Pago seguro con Stripe
              </span>
            </div>
          </div>
        </section>

        {/* SEO content block */}
        <section className="px-4 pb-16 md:pb-24 border-t border-white/5 pt-12">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-xl md:text-2xl font-bold text-white mb-4 text-center">
              Recursos Digitales Profesionales para <span className="text-[#FFD700]">Hostelería</span>
            </h2>
            <div className="text-gray-400 text-sm leading-relaxed space-y-4">
              <p>
                AI Chef Pro ofrece una colección de productos digitales diseñados específicamente para profesionales de hostelería y restauración. Desde prompts de inteligencia artificial optimizados para ChatGPT, Claude, Gemini y Perplexity, hasta plantillas de escandallos en Excel con fórmulas automáticas para controlar el food cost de tu restaurante.
              </p>
              <p>
                Cada producto ha sido creado por profesionales con más de 29 años de experiencia en alta hostelería y 15 años en consultoría gastronómica. No son recursos genéricos: son herramientas específicas para chefs ejecutivos, jefes de cocina, gerentes de restaurante, pasteleros, bartenders, directores de catering y dueños de establecimientos de hostelería.
              </p>
              <p>
                Todos nuestros productos incluyen acceso inmediato tras la compra, actualizaciones gratuitas de por vida, 8 herramientas profesionales gratuitas y garantía de devolución de 30 días. Pago seguro procesado por Stripe.
              </p>
            </div>
          </div>
        </section>

        {/* Minimal footer */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex items-center justify-center gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}
