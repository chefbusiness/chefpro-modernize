import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { ArrowRight, MapPin, FileText, Calculator, ScrollText, Layers } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import { PSEO_CITIES, PSEO_MODIFIERS } from '@/data/pseo-cities';

const SITE_URL = 'https://aichef.pro';

const MODIFIER_META: Record<string, { label: string; path: string; icon: React.ReactNode; description: string }> = {
  'abrir-restaurante': {
    label: 'Cómo Abrir un Restaurante',
    path: 'abrir-restaurante',
    icon: <Layers className="h-5 w-5" />,
    description: 'Costes reales, licencias y barrios.',
  },
  'licencia-restaurante': {
    label: 'Licencia para Restaurante',
    path: 'licencia-restaurante',
    icon: <ScrollText className="h-5 w-5" />,
    description: 'Trámites completos y tiempos reales.',
  },
  'software-gestion-restaurante': {
    label: 'Software de Gestión',
    path: 'software-gestion-restaurante',
    icon: <FileText className="h-5 w-5" />,
    description: 'Comparativa y mejor opción 2026.',
  },
  'escandallo-restaurante': {
    label: 'Escandallo de Restaurante',
    path: 'escandallo-restaurante',
    icon: <Calculator className="h-5 w-5" />,
    description: 'Cómo calcular costes y margen.',
  },
  'plan-negocio-restaurante': {
    label: 'Plan de Negocio',
    path: 'plan-negocio-restaurante',
    icon: <FileText className="h-5 w-5" />,
    description: 'Plantilla bancable con cifras reales.',
  },
};

const COUNTRY_GROUPS: { country: string; emoji: string; slugs: string[] }[] = [
  { country: 'España', emoji: '🇪🇸', slugs: ['madrid', 'barcelona', 'valencia', 'sevilla', 'malaga', 'bilbao', 'zaragoza'] },
  { country: 'México', emoji: '🇲🇽', slugs: ['ciudad-de-mexico', 'guadalajara', 'monterrey', 'queretaro'] },
  { country: 'Colombia', emoji: '🇨🇴', slugs: ['bogota', 'medellin'] },
  { country: 'Argentina', emoji: '🇦🇷', slugs: ['buenos-aires'] },
  { country: 'Chile', emoji: '🇨🇱', slugs: ['santiago'] },
];

const PSeoCitiesHub = () => {
  const canonicalUrl = `${SITE_URL}/seo-restaurantes-por-ciudad`;

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'SEO Restaurantes por Ciudad', item: canonicalUrl },
    ],
  };

  const collectionSchema = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: 'Recursos para Restaurantes por Ciudad',
    description: 'Guías profesionales para abrir restaurante, licencia, software de gestión, escandallo y plan de negocio en 15 ciudades de España y LATAM.',
    url: canonicalUrl,
  };

  return (
    <div className="min-h-screen bg-background text-foreground">
      <SEOHead
        title="Recursos para Restaurantes por Ciudad: Abrir, Licencia, Software, Escandallo y Plan de Negocio"
        description="Guías profesionales 2026 para restauradores en España y LATAM: cómo abrir restaurante, licencias, software de gestión, escandallo y plan de negocio. 15 ciudades con datos reales."
        keywords="abrir restaurante por ciudad, licencia restaurante por ciudad, plan de negocio restaurante por ciudad, software gestión restaurante por ciudad, recursos restaurante España México Colombia Argentina Chile"
        canonical={canonicalUrl}
        disableAutoHreflang
      />

      <Helmet>
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(collectionSchema)}</script>
      </Helmet>

      <ModernHeader />

      {/* Hero */}
      <section className="relative pt-28 pb-16 px-4 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-accent/5 via-background to-background pointer-events-none" />
        <div className="container mx-auto max-w-5xl relative">
          <Badge className="mb-4 bg-accent/15 text-accent border-accent/30">
            15 ciudades · 5 recursos · Datos verificados 2026
          </Badge>
          <h1 className="text-4xl md:text-6xl font-bold leading-tight mb-6">
            Recursos para Restaurantes por Ciudad
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground max-w-3xl">
            Cómo abrir un restaurante, licencias, software de gestión, escandallo y plan de negocio.
            Cifras reales por ciudad en España, México, Colombia, Argentina y Chile.
          </p>
        </div>
      </section>

      {/* Modifiers grid */}
      <section className="py-12 px-4">
        <div className="container mx-auto max-w-5xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-8">5 Tipos de Recursos por Ciudad</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {PSEO_MODIFIERS.map((m) => {
              const meta = MODIFIER_META[m];
              return (
                <Card key={m} className="hover:border-accent/50 transition-colors">
                  <CardContent className="p-6">
                    <div className="flex items-center gap-3 text-accent mb-3">
                      {meta.icon}
                      <h3 className="font-semibold">{meta.label}</h3>
                    </div>
                    <p className="text-sm text-muted-foreground mb-4">{meta.description}</p>
                    <Link
                      to={`/${meta.path}/madrid`}
                      className="text-sm text-accent font-medium inline-flex items-center gap-1 hover:underline"
                    >
                      Ver ejemplo (Madrid) <ArrowRight className="h-4 w-4" />
                    </Link>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Cities by country */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-5xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-2">15 Ciudades Cubiertas</h2>
          <p className="text-lg text-muted-foreground mb-10">
            Cada ciudad incluye datos verificados: inversión real, marco regulatorio, salarios sectoriales y mejores barrios.
          </p>

          {COUNTRY_GROUPS.map((group) => (
            <div key={group.country} className="mb-10">
              <h3 className="text-2xl font-bold mb-4 flex items-center gap-2">
                <span>{group.emoji}</span> {group.country}
              </h3>
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                {group.slugs.map((slug) => {
                  const city = PSEO_CITIES[slug];
                  if (!city) return null;
                  return (
                    <Card key={slug} className="hover:border-accent/50 transition-colors">
                      <CardContent className="p-6">
                        <div className="flex items-center gap-2 mb-3">
                          <MapPin className="h-5 w-5 text-accent" />
                          <h4 className="font-semibold text-lg">{city.displayName}</h4>
                        </div>
                        <p className="text-xs text-muted-foreground mb-2">Inversión total estimada</p>
                        <p className="text-base font-medium mb-4">{city.cost.totalRange}</p>
                        <div className="flex flex-wrap gap-1">
                          {PSEO_MODIFIERS.map((m) => (
                            <Link
                              key={m}
                              to={`/${MODIFIER_META[m].path}/${slug}`}
                              className="text-xs px-2 py-1 bg-muted hover:bg-accent/15 hover:text-accent rounded transition-colors"
                            >
                              {MODIFIER_META[m].label.split(' ').slice(-2).join(' ')}
                            </Link>
                          ))}
                        </div>
                      </CardContent>
                    </Card>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            ¿Buscas Plantillas y Software para tu Restaurante?
          </h2>
          <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
            AI Chef Pro tiene +30 herramientas de IA específicas para hostelería + 26 productos digitales descargables.
            Pruébalo gratis sin tarjeta.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
              <Link to="/herramientas-ia-para-restaurantes">
                Probar AI Chef Pro Gratis <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
            </Button>
            <Button asChild size="lg" variant="outline">
              <Link to="/productos-digitales">Ver Catálogo de Productos</Link>
            </Button>
          </div>
        </div>
      </section>

      <ModernFooter />
      <WhatsAppFloatingButton />
    </div>
  );
};

export default PSeoCitiesHub;
