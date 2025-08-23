import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { 
  ChefHat, 
  Globe, 
  Calculator, 
  Building, 
  Camera 
} from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const scrollToSection = (categoryId: string) => {
  const sectionIds: { [key: string]: string } = {
    'creativity': 'creatividad-showcase',
    'worldCookbooks': 'recetarios-mundiales',
    'knowledge': 'gastro-conocimiento',
    'business': 'herramientas-business',
    'concepts': 'conceptos-negocio',
    'marketing': 'marketing-contenido'
  };
  
  const targetId = sectionIds[categoryId] || categoryId;
  const element = document.getElementById(targetId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

export default function AppsCategories() {
  const { t } = useLanguage();

  const appCategories = [
    {
      id: 'creativity',
      name: t('categories.creativity.title'),
      description: t('categories.creativity.description'),
      icon: ChefHat,
      count: t('categories.creativity.count'),
      apps: [
        t('apps.creativity.cocina_creativa.name'),
        t('apps.creativity.pasteleria_creativa.name'),
        t('apps.creativity.chocolateria_creativa.name'),
        '+5 ' + t('common.more')
      ]
    },
    {
      id: 'worldCookbooks',
      name: t('categories.cookbooks.title'),
      description: t('categories.cookbooks.description'),
      icon: Globe,
      count: t('categories.cookbooks.count'),
      apps: [
        t('cookbooks.europa') + ' (10)',
        t('cookbooks.latinoamerica') + ' (11)',
        t('cookbooks.asia') + ' (4)'
      ]
    },
    {
      id: 'knowledge',
      name: t('categories.knowledge.title'),
      description: t('categories.knowledge.description'),
      icon: Globe,
      count: t('categories.knowledge.count'),
      apps: [t('apps.knowledge.gastro_lexicum.name')]
    },
    {
      id: 'business',
      name: t('categories.tools.title'),
      description: t('categories.tools.description'),
      icon: Calculator,
      count: t('categories.tools.count'),
      apps: [
        t('apps.business.chatgpt_4o.name'),
        t('apps.business.mermas_gencal.name'),
        t('apps.business.id_alergenos.name'),
        '+3 ' + t('common.more')
      ]
    },
    {
      id: 'concepts',
      name: t('categories.business.title'),
      description: t('categories.business.description'),
      icon: Building,
      count: t('categories.business.count'),
      apps: [
        t('apps.concepts.catering_ai.name'),
        t('apps.concepts.burger_pro_ai.name'),
        t('apps.concepts.food_truck_ai.name'),
        '+2 ' + t('common.more')
      ]
    },
    {
      id: 'marketing',
      name: t('categories.marketing.title'),
      description: t('categories.marketing.description'),
      icon: Camera,
      count: t('categories.marketing.count'),
      apps: [
        t('apps.marketing.menu_plate_seo.name'),
        t('apps.marketing.gastro_calendar.name'),
        t('apps.marketing.instaflow_ai.name'),
        '+1 ' + t('common.more')
      ]
    }
  ];

  return (
    <section className="container py-8 md:py-12 lg:py-24">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          {t('categories.title')}
        </h2>
        <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance">
          {t('categories.description')}
        </p>
      </div>

      <div className="mx-auto grid justify-center gap-6 sm:grid-cols-2 lg:grid-cols-3 mt-12">
        {appCategories.map((category) => (
          <Card 
            key={category.id} 
            className="cursor-pointer hover-card group"
            onClick={() => scrollToSection(category.id)}
          >
            <CardHeader>
              <div className="flex items-center justify-between">
                <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
                  <category.icon className="h-6 w-6 text-primary" />
                </div>
                <Badge variant="secondary">{category.count}</Badge>
              </div>
              <CardTitle className="text-lg group-hover:text-primary transition-colors">
                {category.name}
              </CardTitle>
              <CardDescription>{category.description}</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-1">
                {category.apps.map((app, index) => (
                  <Badge key={index} variant="outline" className="text-xs">
                    {app}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  );
}