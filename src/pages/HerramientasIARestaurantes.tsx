import { Helmet } from 'react-helmet-async';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, ArrowRight, ChefHat, TrendingDown, Clock, Star, Utensils, BarChart3, Megaphone, BookOpen } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';

const APP_URL = 'https://app.aichef.pro';

const breadcrumbSchema = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
    { "@type": "ListItem", "position": 2, "name": "Herramientas IA para Restaurantes", "item": "https://aichef.pro/herramientas-ia-para-restaurantes" }
  ]
};

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Qué herramientas de IA son útiles para un restaurante?",
      "acceptedAnswer": { "@type": "Answer", "text": "Las herramientas de IA más útiles para restaurantes incluyen: generadores de carta y menú digital, calculadoras de coste de plato, gestores de alérgenos, herramientas de marketing gastronómico para redes sociales, planificadores de compras y control de mermas. AI Chef Pro agrupa 55+ de estas herramientas especializadas en una sola suite." }
    },
    {
      "@type": "Question",
      "name": "¿Puede la inteligencia artificial ayudar a reducir costes en un restaurante?",
      "acceptedAnswer": { "@type": "Answer", "text": "Sí. La IA permite optimizar el food cost calculando el coste exacto de cada plato, detectar mermas innecesarias, planificar compras según la demanda y ajustar precios de carta para maximizar el margen. Los usuarios de AI Chef Pro reportan una reducción media del 22% en costes de ingredientes." }
    },
    {
      "@type": "Question",
      "name": "¿Necesito conocimientos técnicos para usar herramientas de IA en mi restaurante?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. AI Chef Pro está diseñado para dueños y gestores de restaurantes sin formación técnica. Las herramientas funcionan con lenguaje natural: describes lo que necesitas y la IA genera el resultado. Sin programación ni configuraciones complejas." }
    },
    {
      "@type": "Question",
      "name": "¿Cuánto cuesta usar IA para la gestión de restaurantes?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI Chef Pro tiene un plan gratuito (AI Chef Miembro) con 5 usos al mes. Los planes de pago empiezan en 25€/mes (AI Chef Premium Pro, 150 usos) y llegan hasta 95€/mes para uso ilimitado. También hay un plan anual a 950€ que equivale a 79€/mes." }
    }
  ]
};

const tools = [
  {
    icon: <BookOpen className="h-7 w-7 text-primary" />,
    title: "Diseño de carta y menú",
    description: "Genera cartas completas adaptadas a tu concepto, temporada y food cost objetivo. Incluye descripciones atractivas y maridajes.",
    keywords: ["carta digital", "menú IA", "ingeniería de menú"]
  },
  {
    icon: <BarChart3 className="h-7 w-7 text-primary" />,
    title: "Control de costes y food cost",
    description: "Calcula el coste exacto de cada plato, establece precios de venta con el margen que necesitas y detecta dónde pierdes dinero.",
    keywords: ["food cost", "coste plato", "precio venta"]
  },
  {
    icon: <TrendingDown className="h-7 w-7 text-primary" />,
    title: "Reducción de mermas",
    description: "Planifica compras según la demanda real, aprovecha géneros al máximo con recetas de aprovechamiento y elimina el desperdicio.",
    keywords: ["mermas cocina", "desperdicio alimentario", "planificación compras"]
  },
  {
    icon: <Utensils className="h-7 w-7 text-primary" />,
    title: "Gestión de alérgenos",
    description: "Identifica y etiqueta automáticamente los 14 alérgenos de obligatoria declaración en todos tus platos. Cumplimiento legal simplificado.",
    keywords: ["alérgenos restaurante", "normativa alérgenos", "etiquetado"]
  },
  {
    icon: <Megaphone className="h-7 w-7 text-primary" />,
    title: "Marketing gastronómico",
    description: "Crea contenido para redes sociales, fichas de Google My Business, respuestas a reseñas y campañas promocionales en minutos.",
    keywords: ["marketing restaurante", "redes sociales hostelería", "Google My Business"]
  },
  {
    icon: <ChefHat className="h-7 w-7 text-primary" />,
    title: "Creatividad culinaria",
    description: "Desarrolla nuevos platos, experimenta con maridajes y adapta recetas de 25 cocinas del mundo a tu concepto.",
    keywords: ["creatividad culinaria", "nuevos platos", "recetas IA"]
  }
];

const results = [
  { metric: "22%", label: "reducción media en costes de ingredientes" },
  { metric: "35%", label: "menos tiempo en desarrollo de nuevos platos" },
  { metric: "30%", label: "reducción en desperdicio de comida" },
  { metric: "55+", label: "herramientas especializadas en gastronomía" }
];

const profiles = [
  { title: "Restaurante independiente", description: "Gestiona tu carta, costes y marketing sin depender de agencias ni consultores caros." },
  { title: "Bar y cafetería", description: "Crea tu oferta gastronómica, controla el género y atrae más clientes con contenido profesional." },
  { title: "Cadena de restaurantes", description: "Estandariza procesos, controla costes en múltiples locales y escala tu operación." },
  { title: "Chef ejecutivo", description: "Agiliza la ingeniería de menú, el análisis nutricional y el desarrollo de recetas de autor." }
];

export default function HerramientasIARestaurantes() {
  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title="Herramientas de IA para Restaurantes | AI Chef Pro"
        description="55+ herramientas de inteligencia artificial para dueños de restaurantes. Controla costes, diseña carta, gestiona alérgenos y automatiza el marketing. Empieza gratis."
        keywords="herramientas ia restaurante, inteligencia artificial restaurante, software ia hostelería, ia para dueños de restaurante, gestión restaurante con ia, food cost ia, carta digital ia, marketing restaurante ia"
        canonical="https://aichef.pro/herramientas-ia-para-restaurantes"
      />
      <Helmet>
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <Badge className="mb-6 text-sm px-4 py-2">55+ herramientas especializadas en hostelería</Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                Herramientas de IA para Restaurantes
              </h1>
              <p className="text-xl text-muted-foreground mb-4 max-w-3xl mx-auto text-balance">
                La suite de inteligencia artificial diseñada para dueños de restaurantes, bares y cafeterías. Sin conocimientos técnicos. Sin curva de aprendizaje.
              </p>
              <p className="text-lg font-semibold text-primary mb-10">
                Controla costes · Diseña tu carta · Automatiza el marketing · Reduce mermas
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  Empezar gratis ahora
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button size="lg" variant="outline" onClick={() => window.open(APP_URL + '/pricing', '_blank')}>
                  Ver planes y precios
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">Sin tarjeta de crédito · Plan gratuito disponible</p>
            </div>
          </div>
        </section>

        {/* Resultados */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
              {results.map((r, i) => (
                <div key={i}>
                  <div className="text-4xl font-bold text-primary mb-2">{r.metric}</div>
                  <div className="text-sm text-muted-foreground">{r.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Herramientas */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                ¿Qué puede hacer la IA por tu restaurante?
              </h2>
              <p className="text-lg text-muted-foreground">
                Cada herramienta de AI Chef Pro resuelve un problema real del día a día en hostelería. Sin tecnicismos, sin configuraciones complejas.
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
              {tools.map((tool, i) => (
                <Card key={i} className="border shadow-md hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <div className="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center mb-4">
                      {tool.icon}
                    </div>
                    <CardTitle className="text-xl">{tool.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground mb-4">{tool.description}</p>
                    <div className="flex flex-wrap gap-2">
                      {tool.keywords.map((kw, j) => (
                        <Badge key={j} variant="secondary" className="text-xs">{kw}</Badge>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Para quién es */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                Diseñado para profesionales de la restauración
              </h2>
              <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
                Tanto si tienes un bar de barrio como una cadena de restaurantes, AI Chef Pro tiene herramientas adaptadas a tu realidad.
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
              {profiles.map((p, i) => (
                <Card key={i} className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                  <CardHeader>
                    <div className="w-14 h-14 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                      <ChefHat className="h-7 w-7 text-primary" />
                    </div>
                    <CardTitle className="text-lg">{p.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground text-sm">{p.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Por qué IA */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
              <div>
                <h2 className="text-3xl font-bold text-foreground mb-6">
                  Por qué la inteligencia artificial está cambiando la hostelería
                </h2>
                <p className="text-lg text-muted-foreground mb-6">
                  Los restaurantes que adoptan herramientas de IA no compiten con los que no las usan. La diferencia está en la velocidad de decisión, el control de costes y la capacidad de crear una oferta gastronómica diferenciada.
                </p>
                <ul className="space-y-4">
                  {[
                    "Diseña la carta de tu restaurante en horas, no en semanas",
                    "Calcula el food cost de cada plato al céntimo",
                    "Genera contenido para redes en minutos, no en días",
                    "Identifica alérgenos automáticamente en todos tus platos",
                    "Reduce mermas con planificación inteligente de compras",
                    "Accede a recetas de 25 cocinas del mundo adaptadas a tu negocio"
                  ].map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span className="text-muted-foreground">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="bg-muted/30 rounded-2xl p-8">
                <div className="flex items-center gap-1 mb-4">
                  {[...Array(5)].map((_, i) => <Star key={i} className="h-5 w-5 fill-yellow-400 text-yellow-400" />)}
                </div>
                <p className="text-lg italic text-foreground mb-6">
                  "Reducimos nuestras mermas del 14% al 5% en menos de un mes. El ROI fue inmediato: pagamos la suscripción con lo que ahorramos la primera semana."
                </p>
                <div>
                  <p className="font-semibold">Laura García</p>
                  <p className="text-sm text-muted-foreground">Directora de Operaciones, Grupo Gastronómico BCN</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Precios */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold text-foreground mb-4">
              Planes para cada tipo de negocio gastronómico
            </h2>
            <p className="text-lg text-muted-foreground mb-12 max-w-2xl mx-auto">
              Desde el plan gratuito para empezar hasta el uso ilimitado para grandes operaciones.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto mb-10">
              {[
                { name: "AI Chef Miembro", price: "Gratis", uses: "5 usos/mes", cta: "Empezar gratis", highlight: false },
                { name: "AI Chef Premium Pro", price: "25€/mes", uses: "150 usos/mes", cta: "Seleccionar", highlight: false },
                { name: "AI Chef Premium Plus", price: "50€/mes", uses: "350 usos/mes", cta: "Más popular", highlight: true },
                { name: "AI Chef Premium Max", price: "95€/mes", uses: "Ilimitado", cta: "Seleccionar", highlight: false },
              ].map((plan, i) => (
                <Card key={i} className={`text-center ${plan.highlight ? 'ring-2 ring-primary shadow-xl scale-105' : 'shadow-md'}`}>
                  {plan.highlight && <Badge className="absolute -top-3 left-1/2 -translate-x-1/2">⭐ Más Popular</Badge>}
                  <CardHeader className="relative">
                    <CardTitle className="text-lg">{plan.name}</CardTitle>
                    <div className="text-3xl font-bold text-primary">{plan.price}</div>
                    <div className="text-sm text-muted-foreground">{plan.uses}</div>
                  </CardHeader>
                  <CardContent>
                    <Button
                      className={`w-full ${plan.highlight ? 'btn-gold' : ''}`}
                      variant={plan.highlight ? 'default' : 'outline'}
                      onClick={() => window.open(APP_URL + '/pricing', '_blank')}
                    >
                      {plan.cta}
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
            <p className="text-sm text-muted-foreground">
              También disponible plan anual AI Chef Premium Plus Anual a 950€/año · Ahorra 2 meses
            </p>
          </div>
        </section>

        {/* FAQ */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-12 text-center">
                Preguntas frecuentes sobre IA para restaurantes
              </h2>
              <div className="space-y-6">
                {faqSchema.mainEntity.map((item, i) => (
                  <div key={i} className="border-b pb-6">
                    <h3 className="text-lg font-semibold text-foreground mb-3">{item.name}</h3>
                    <p className="text-muted-foreground">{item.acceptedAnswer.text}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* CTA final */}
        <section className="py-20 bg-gradient-to-r from-primary to-primary/80">
          <div className="container mx-auto px-4 text-center text-primary-foreground">
            <h2 className="text-3xl font-bold mb-4">
              Empieza hoy con las herramientas de IA para tu restaurante
            </h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">
              Plan gratuito disponible. Sin tarjeta de crédito. Acceso inmediato a 55+ herramientas especializadas en gastronomía y hostelería.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" variant="secondary" className="bg-white text-primary hover:bg-white/90" onClick={() => window.open(APP_URL, '_blank')}>
                Probar gratis ahora
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10" onClick={() => window.open(APP_URL + '/pricing', '_blank')}>
                Ver todos los planes
              </Button>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
      <WhatsAppFloatingButton />
    </div>
  );
}
