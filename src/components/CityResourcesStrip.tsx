import { Link } from 'react-router-dom';
import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ArrowRight, MapPin, FileText, Calculator, ScrollText, Layers } from 'lucide-react';
import { useTranslation } from 'react-i18next';

const CITY_CARDS = [
  { slug: 'madrid', label: 'Madrid', cost: '€110.000 - €280.000', country: '🇪🇸 España' },
  { slug: 'barcelona', label: 'Barcelona', cost: '€100.000 - €260.000', country: '🇪🇸 España' },
  { slug: 'ciudad-de-mexico', label: 'Ciudad de México', cost: 'MXN $1.5M - $5M', country: '🇲🇽 México' },
  { slug: 'bogota', label: 'Bogotá', cost: 'COP $300M - $1.200M', country: '🇨🇴 Colombia' },
  { slug: 'buenos-aires', label: 'Buenos Aires', cost: 'USD $50k - $200k', country: '🇦🇷 Argentina' },
];

const RESOURCE_PILLS = [
  { path: 'abrir-restaurante', label: 'Cómo abrir restaurante', icon: <Layers className="h-4 w-4" /> },
  { path: 'licencia-restaurante', label: 'Licencia y trámites', icon: <ScrollText className="h-4 w-4" /> },
  { path: 'software-gestion-restaurante', label: 'Software gestión', icon: <FileText className="h-4 w-4" /> },
  { path: 'escandallo-restaurante', label: 'Escandallo', icon: <Calculator className="h-4 w-4" /> },
  { path: 'plan-negocio-restaurante', label: 'Plan de negocio', icon: <FileText className="h-4 w-4" /> },
];

export default function CityResourcesStrip() {
  const { i18n } = useTranslation();
  if (i18n.language !== 'es') return null;

  return (
    <section className="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center mb-12">
          <Badge className="mb-4 bg-accent/15 text-accent border-accent/30">
            Recursos por ciudad · 15 ciudades · Datos verificados 2026
          </Badge>
          <h2 className="text-3xl md:text-5xl font-bold mb-4">
            Cómo Abrir un Restaurante en tu Ciudad
          </h2>
          <p className="text-lg text-muted-foreground max-w-3xl mx-auto">
            Costes reales, licencias específicas, salarios sectoriales y mejores barrios para España, México, Colombia, Argentina y Chile.
          </p>
        </div>

        <div className="grid sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-10">
          {CITY_CARDS.map((c) => (
            <Link key={c.slug} to={`/abrir-restaurante/${c.slug}`} className="group">
              <Card className="h-full hover:border-accent transition-all hover:shadow-md">
                <CardContent className="p-5">
                  <div className="flex items-center gap-2 mb-2 text-xs text-muted-foreground">
                    <span>{c.country}</span>
                  </div>
                  <div className="flex items-center gap-2 mb-3">
                    <MapPin className="h-5 w-5 text-accent" />
                    <h3 className="font-semibold text-lg group-hover:text-accent transition-colors">
                      {c.label}
                    </h3>
                  </div>
                  <p className="text-xs text-muted-foreground mb-1">Inversión total estimada</p>
                  <p className="text-sm font-medium">{c.cost}</p>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>

        <div className="flex flex-wrap justify-center gap-2 mb-8">
          {RESOURCE_PILLS.map((r) => (
            <Link
              key={r.path}
              to={`/${r.path}/madrid`}
              className="inline-flex items-center gap-2 px-4 py-2 bg-muted hover:bg-accent/15 hover:text-accent rounded-full text-sm font-medium transition-colors border border-border"
            >
              {r.icon}
              {r.label}
            </Link>
          ))}
        </div>

        <div className="text-center">
          <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
            <Link to="/seo-restaurantes-por-ciudad">
              Ver las 15 ciudades + 5 recursos <ArrowRight className="ml-2 h-5 w-5" />
            </Link>
          </Button>
        </div>
      </div>
    </section>
  );
}
