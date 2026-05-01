import { useParams, Link, Navigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import {
  ArrowRight, MapPin, FileText, Users, Building2, TrendingUp,
  CheckCircle, Sparkles, Calculator, ScrollText, ShieldCheck,
} from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import {
  PSEO_CITIES,
  PSEO_CITY_SLUGS,
  PSEO_MODIFIERS,
  type CityData,
  type PSeoModifier,
} from '@/data/pseo-cities';
import { PSEO_CONTENT_ES, fillTemplate } from '@/data/pseo-cities-content.es';
import { getProductsByIds } from '@/data/products-catalog';

const SITE_URL = 'https://aichef.pro';

interface PSeoCityPageProps {
  modifier: PSeoModifier;
}

const MODIFIER_PATH: Record<PSeoModifier, string> = {
  'abrir-restaurante': 'abrir-restaurante',
  'licencia-restaurante': 'licencia-restaurante',
  'software-gestion-restaurante': 'software-gestion-restaurante',
  'escandallo-restaurante': 'escandallo-restaurante',
  'plan-negocio-restaurante': 'plan-negocio-restaurante',
};

const MODIFIER_LABEL: Record<PSeoModifier, string> = {
  'abrir-restaurante': 'Abrir restaurante',
  'licencia-restaurante': 'Licencia restaurante',
  'software-gestion-restaurante': 'Software gestión',
  'escandallo-restaurante': 'Escandallo',
  'plan-negocio-restaurante': 'Plan de negocio',
};

const PSeoCityPage = ({ modifier }: PSeoCityPageProps) => {
  const { ciudad } = useParams<{ ciudad: string }>();
  const city: CityData | undefined = ciudad ? PSEO_CITIES[ciudad] : undefined;

  if (!city) {
    return <Navigate to="/seo-restaurantes-por-ciudad" replace />;
  }

  const content = PSEO_CONTENT_ES[modifier];
  const fill = (s: string) => fillTemplate(s, city);
  const otherCities = PSEO_CITY_SLUGS.filter((s) => s !== city.slug).slice(0, 6);
  const products = getProductsByIds(
    [content.primaryProductSlug, 'kit-plan-financiero', 'pack-appcc', 'kit-escandallos'].filter(
      (id, i, arr) => arr.indexOf(id) === i && id !== 'saas-trial'
    ),
    'es',
  );

  const canonicalPath = `/${MODIFIER_PATH[modifier]}/${city.slug}`;
  const canonicalUrl = `${SITE_URL}${canonicalPath}`;

  // Schema.org JSON-LD
  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'SEO Restaurantes por Ciudad', item: `${SITE_URL}/seo-restaurantes-por-ciudad` },
      { '@type': 'ListItem', position: 3, name: `${MODIFIER_LABEL[modifier]} ${city.displayName}`, item: canonicalUrl },
    ],
  };

  const serviceSchema = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    serviceType: fill(content.schemaServiceCategory),
    name: fill(content.schemaServiceName),
    provider: {
      '@type': 'Organization',
      name: 'AI Chef Pro',
      url: SITE_URL,
    },
    areaServed: {
      '@type': 'City',
      name: city.displayName,
      containedInPlace: { '@type': 'Country', name: city.countryName },
    },
    description: fill(content.metaDescription),
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: content.faqs.map((f) => ({
      '@type': 'Question',
      name: fill(f.q),
      acceptedAnswer: { '@type': 'Answer', text: fill(f.a) },
    })),
  };

  return (
    <div className="min-h-screen bg-background text-foreground">
      <SEOHead
        title={fill(content.metaTitle)}
        description={fill(content.metaDescription)}
        keywords={fill(content.keywords)}
        canonical={canonicalUrl}
        ogImage={`${SITE_URL}/og-pseo-${modifier}.jpg`}
        disableAutoHreflang
      />

      <Helmet>
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(serviceSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      {/* Hero */}
      <section className="relative pt-28 pb-16 px-4 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-accent/5 via-background to-background pointer-events-none" />
        <div className="container mx-auto max-w-5xl relative">
          <Badge className="mb-4 bg-accent/15 text-accent border-accent/30">
            {content.heroBadge} · {city.displayName}, {city.countryName}
          </Badge>
          <h1 className="text-4xl md:text-6xl font-bold leading-tight mb-6">
            {fill(content.h1Template)}
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground max-w-3xl mb-8">
            {fill(content.heroSubtitle)}
          </p>
          <div className="flex flex-wrap gap-4">
            <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
              <Link to={`/${content.primaryProductSlug}`}>
                {content.primaryProductLabel} <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
            </Button>
            <Button asChild size="lg" variant="outline">
              <Link to="/herramientas-ia-para-restaurantes">
                Probar AI Chef Pro Gratis
              </Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Intro */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">{fill(content.introTitle)}</h2>
          <p className="text-lg text-muted-foreground leading-relaxed">{fill(content.introBody)}</p>
        </div>
      </section>

      {/* Cost Breakdown */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-5xl">
          <div className="flex items-center gap-3 mb-2">
            <Calculator className="h-7 w-7 text-accent" />
            <Badge variant="outline">Datos verificados {city.countryName}</Badge>
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-3">
            Inversión Total Real para Abrir un Restaurante en {city.displayName}
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            Cifras de mercado verificadas {city.countryName} 2026. Rango refleja diferencias por barrio, tamaño del local y nivel de acabados.
          </p>
          <div className="grid md:grid-cols-2 gap-6">
            <Card className="border-accent/30">
              <CardContent className="p-6">
                <div className="text-sm font-medium text-muted-foreground uppercase tracking-wide mb-2">
                  Inversión Total
                </div>
                <div className="text-3xl font-bold text-accent mb-3">{city.cost.totalRange}</div>
                {city.cost.notes && (
                  <p className="text-sm text-muted-foreground">{city.cost.notes}</p>
                )}
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6 space-y-3">
                <CostRow label="Obra y reforma" value={city.cost.obra} />
                <CostRow label="Equipamiento (cocina + sala)" value={city.cost.equipamiento} />
                <CostRow label="Licencias y trámites" value={city.cost.licencias} />
                <CostRow label="Fianza + alquiler inicial" value={city.cost.fianzaAlquiler} />
                <CostRow label="Capital circulante 3-6m" value={city.cost.capitalCirculante} />
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Regulation */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-5xl">
          <div className="flex items-center gap-3 mb-2">
            <ShieldCheck className="h-7 w-7 text-accent" />
            <Badge variant="outline">Marco regulatorio 2026</Badge>
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-3">
            Licencias y Marco Regulatorio Específico de {city.displayName}
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            Trámites obligatorios sector hostelería {city.countryName} con tiempos reales en {city.displayName}.
          </p>
          <div className="grid md:grid-cols-3 gap-4">
            <RegulationCard
              icon={<ScrollText className="h-5 w-5" />}
              title="Marco Normativo"
              body={city.regulation.framework}
            />
            <RegulationCard
              icon={<FileText className="h-5 w-5" />}
              title="Tipo de Licencia"
              body={city.regulation.licenseType}
            />
            <RegulationCard
              icon={<TrendingUp className="h-5 w-5" />}
              title="Tiempo de Trámite"
              body={city.regulation.tramitTime}
            />
          </div>
          {city.regulation.notes && (
            <Card className="mt-6 border-accent/30 bg-accent/5">
              <CardContent className="p-6">
                <div className="flex gap-3">
                  <Sparkles className="h-5 w-5 text-accent flex-shrink-0 mt-0.5" />
                  <p className="text-base">{city.regulation.notes}</p>
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </section>

      {/* Salaries */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-5xl">
          <div className="flex items-center gap-3 mb-2">
            <Users className="h-7 w-7 text-accent" />
            <Badge variant="outline">Datos sectoriales</Badge>
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-3">
            Salarios del Sector Hostelero en {city.displayName}
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            Convenios y mercado real {city.displayName} 2026. Cifras brutas mensuales — calcula seguridad social aparte (~30% adicional sobre coste empresa).
          </p>
          <div className="grid md:grid-cols-3 gap-6">
            <SalaryCard role="Jefe de Cocina" range={city.salaries.jefeCocina} />
            <SalaryCard role="Ayudante de Cocina" range={city.salaries.ayudante} />
            <SalaryCard role="Camarero" range={city.salaries.camarero} />
          </div>
          {city.salaries.source && (
            <p className="text-sm text-muted-foreground mt-6">Fuente: {city.salaries.source}</p>
          )}
        </div>
      </section>

      {/* Neighborhoods */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-5xl">
          <div className="flex items-center gap-3 mb-2">
            <MapPin className="h-7 w-7 text-accent" />
            <Badge variant="outline">Análisis de zonas</Badge>
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-3">
            Mejores Barrios para Abrir un Restaurante en {city.displayName}
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            Zonas con ticket medio del mercado y consideraciones de alquiler. Tu barrio ideal depende del concepto, no del prestigio.
          </p>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {city.neighborhoods.map((n) => (
              <Card key={n.name} className="hover:border-accent/50 transition-colors">
                <CardContent className="p-6">
                  <div className="flex items-start gap-3 mb-2">
                    <Building2 className="h-5 w-5 text-accent flex-shrink-0 mt-1" />
                    <div>
                      <h3 className="font-semibold text-lg">{n.name}</h3>
                      <div className="text-sm text-accent font-medium">Ticket medio {n.ticketMedio}</div>
                    </div>
                  </div>
                  {n.notes && <p className="text-sm text-muted-foreground mt-3">{n.notes}</p>}
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Market Notes */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-4xl">
          <div className="flex items-center gap-3 mb-3">
            <TrendingUp className="h-7 w-7 text-accent" />
            <Badge variant="outline">Análisis de mercado 2026</Badge>
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Tendencias del Mercado Gastronómico en {city.displayName}
          </h2>
          <p className="text-lg text-muted-foreground leading-relaxed">{city.marketNotes}</p>
          {city.restaurantsCount && (
            <Card className="mt-6 border-accent/30">
              <CardContent className="p-4">
                <div className="text-sm font-medium text-muted-foreground">Tamaño del mercado</div>
                <div className="text-lg font-semibold">{city.restaurantsCount}</div>
              </CardContent>
            </Card>
          )}
        </div>
      </section>

      {/* Primary Product CTA */}
      <section className="py-20 px-4">
        <div className="container mx-auto max-w-4xl">
          <Card className="border-accent/40 bg-gradient-to-br from-accent/10 to-background">
            <CardContent className="p-8 md:p-12">
              <Badge className="mb-4 bg-accent text-accent-foreground">Producto Recomendado</Badge>
              <h2 className="text-3xl md:text-4xl font-bold mb-4">{fill(content.primaryCtaTitle)}</h2>
              <p className="text-lg text-muted-foreground mb-6 leading-relaxed">
                {fill(content.primaryCtaBody)}
              </p>
              <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
                <Link to={`/${content.primaryProductSlug}`}>
                  {content.primaryProductLabel} <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
              </Button>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Cross-sell products */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-5xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-3">Plantillas Profesionales que Acortan el Proceso</h2>
          <p className="text-lg text-muted-foreground mb-8">
            Productos del catálogo AI Chef Pro listos para tu restaurante en {city.displayName}.
          </p>
          <div className="grid md:grid-cols-3 gap-6">
            {products.slice(0, 3).map((p) => (
              <Card key={p.id} className="hover:border-accent/50 transition-colors">
                <CardContent className="p-6">
                  <Badge variant="outline" className="mb-3">{p.price}</Badge>
                  <h3 className="text-lg font-semibold mb-2">{p.name}</h3>
                  <p className="text-sm text-muted-foreground mb-4">{p.description}</p>
                  <Button asChild variant="outline" size="sm">
                    <Link to={p.url}>Ver detalle <ArrowRight className="ml-2 h-4 w-4" /></Link>
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* SaaS CTA */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <Card className="bg-gradient-to-br from-accent/15 via-background to-background border-accent/30">
            <CardContent className="p-8 md:p-12 text-center">
              <Sparkles className="h-12 w-12 text-accent mx-auto mb-4" />
              <h2 className="text-3xl md:text-4xl font-bold mb-4">{content.saasCtaTitle}</h2>
              <p className="text-lg text-muted-foreground mb-6 max-w-2xl mx-auto">{content.saasCtaBody}</p>
              <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
                <Link to="/herramientas-ia-para-restaurantes">
                  Probar AI Chef Pro Gratis <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
              </Button>
              <p className="text-xs text-muted-foreground mt-4">5 usos gratis al mes · Sin tarjeta</p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-16 px-4 bg-muted/30">
        <div className="container mx-auto max-w-4xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-8">Preguntas Frecuentes</h2>
          <div className="space-y-4">
            {content.faqs.map((f, i) => (
              <Card key={i}>
                <CardContent className="p-6">
                  <h3 className="font-semibold text-lg mb-2 flex gap-2">
                    <CheckCircle className="h-5 w-5 text-accent flex-shrink-0 mt-1" />
                    {fill(f.q)}
                  </h3>
                  <p className="text-muted-foreground ml-7">{fill(f.a)}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Other cities + modifiers cross-link */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-5xl">
          <h2 className="text-2xl md:text-3xl font-bold mb-6">
            {MODIFIER_LABEL[modifier]} en Otras Ciudades
          </h2>
          <div className="flex flex-wrap gap-2 mb-10">
            {otherCities.map((slug) => (
              <Link
                key={slug}
                to={`/${MODIFIER_PATH[modifier]}/${slug}`}
                className="px-4 py-2 bg-muted hover:bg-accent/15 hover:text-accent rounded-full text-sm font-medium transition-colors border border-border"
              >
                {PSEO_CITIES[slug].displayName}
              </Link>
            ))}
            <Link
              to="/seo-restaurantes-por-ciudad"
              className="px-4 py-2 bg-accent text-accent-foreground hover:bg-accent/90 rounded-full text-sm font-medium transition-colors"
            >
              Ver todas las ciudades →
            </Link>
          </div>

          <h2 className="text-2xl md:text-3xl font-bold mb-6">
            Otros Recursos para Restaurantes en {city.displayName}
          </h2>
          <div className="flex flex-wrap gap-2">
            {PSEO_MODIFIERS.filter((m) => m !== modifier).map((m) => (
              <Link
                key={m}
                to={`/${MODIFIER_PATH[m]}/${city.slug}`}
                className="px-4 py-2 bg-muted hover:bg-accent/15 hover:text-accent rounded-full text-sm font-medium transition-colors border border-border"
              >
                {MODIFIER_LABEL[m]} en {city.displayName}
              </Link>
            ))}
          </div>
        </div>
      </section>

      <ModernFooter />
      <WhatsAppFloatingButton />
    </div>
  );
};

const CostRow = ({ label, value }: { label: string; value: string }) => (
  <div className="flex justify-between items-center pb-2 border-b border-border/50 last:border-0 last:pb-0">
    <span className="text-sm text-muted-foreground">{label}</span>
    <span className="font-medium text-right">{value}</span>
  </div>
);

const RegulationCard = ({ icon, title, body }: { icon: React.ReactNode; title: string; body: string }) => (
  <Card>
    <CardContent className="p-6">
      <div className="flex items-center gap-2 text-accent mb-3">
        {icon}
        <span className="font-semibold text-sm uppercase tracking-wide">{title}</span>
      </div>
      <p className="text-sm leading-relaxed">{body}</p>
    </CardContent>
  </Card>
);

const SalaryCard = ({ role, range }: { role: string; range: string }) => (
  <Card>
    <CardContent className="p-6">
      <div className="text-sm font-medium text-muted-foreground uppercase tracking-wide mb-2">{role}</div>
      <div className="text-xl font-bold">{range}</div>
    </CardContent>
  </Card>
);

export default PSeoCityPage;
