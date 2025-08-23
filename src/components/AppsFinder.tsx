import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { personas, getRecommendedApps } from '@/data/personas';
import { useLanguage } from '@/hooks/useLanguage';
import { useTranslation } from 'react-i18next';

export default function AppsFinder() {
  const { getAppUrl, currentLanguage } = useLanguage();
  const { t } = useTranslation();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="filtro-apps" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          {t('finder.title_prefix')} <span className="gradient-text">{t('finder.title_highlight')}</span>
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          {t('finder.description')}
        </p>
      </div>

      <Tabs defaultValue="chef-ejecutivo" className="w-full">
        <TabsList className="grid w-full grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 mb-6 sm:mb-8 h-auto">
          {personas.map((persona) => (
            <TabsTrigger key={persona.id} value={persona.id} className="text-xs sm:text-sm p-2 sm:p-3 flex-col sm:flex-row gap-1 h-auto min-h-[3rem] sm:min-h-[2.5rem]">
              <span className="text-sm sm:text-base">{persona.emoji}</span>
              <span className="hidden md:inline text-center leading-tight">{t(`finder.personas.${persona.id}.short_name`)}</span>
              <span className="md:hidden text-center text-xs leading-tight">{t(`finder.personas.${persona.id}.mobile_name`)}</span>
            </TabsTrigger>
          ))}
        </TabsList>

        {personas.map((persona) => {
          const recommendedApps = getRecommendedApps(persona.id);
          
          return (
            <TabsContent key={persona.id} value={persona.id}>
              <div className="text-center mb-8">
                <h3 className="text-xl font-semibold mb-2">
                  {persona.emoji} {t(`finder.personas.${persona.id}.name`)}
                </h3>
                <p className="text-muted-foreground">{t(`finder.personas.${persona.id}.description`)}</p>
              </div>
              
              <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 sm:gap-6">
                {recommendedApps.map((app) => {
                  if (!app) return null;
                  const IconComponent = app.icon;
                  
                  return (
                    <Card key={app.id} className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-accent/50">
                      <CardHeader className="p-4 sm:p-6">
                        <div className="flex items-center justify-between mb-2">
                          <IconComponent className="h-5 w-5 sm:h-6 sm:w-6 text-accent" />
                        </div>
                        <CardTitle className="text-base sm:text-lg leading-tight">{t(`apps.${app.category}.${app.id.replace(/-/g, '_')}.name`)}</CardTitle>
                        <CardDescription className="text-sm leading-relaxed">{t(`apps.${app.category}.${app.id.replace(/-/g, '_')}.description`)}</CardDescription>
                      </CardHeader>
                      <CardContent className="p-4 sm:p-6 pt-0">
                        <div className="bg-muted/50 p-3 rounded text-sm">
                          <p className="text-muted-foreground mb-1 text-xs">{t('finder.preview_label')}:</p>
                          <p className="font-medium text-xs sm:text-sm leading-relaxed">"{t(`apps.${app.category}.${app.id.replace(/-/g, '_')}.preview`)}"</p>
                        </div>
                      </CardContent>
                      <CardFooter className="p-4 sm:p-6 pt-0">
                        <Button 
                          variant="outline" 
                          className="w-full group-hover:bg-accent group-hover:text-accent-foreground transition-colors text-sm py-2 h-auto min-h-[2.5rem]"
                          onClick={() => handleAppClick(app.slug)}
                        >
                          {t('cta.explore')}
                        </Button>
                      </CardFooter>
                    </Card>
                  );
                })}
              </div>
            </TabsContent>
          );
        })}
      </Tabs>
    </section>
  );
}