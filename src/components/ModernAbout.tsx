import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { useLanguage } from '@/hooks/useLanguage';

export default function ModernAbout() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  return (
    <section className="container py-8 md:py-12 lg:py-24">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          {t('about.title')}
        </h2>
        <p 
          className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance"
          dangerouslySetInnerHTML={{ __html: t('about.description') }}
        />
      </div>

      <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3 mt-12">
        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">{t('about.mission_title')}</h3>
            <p 
              className="text-sm text-muted-foreground text-center"
              dangerouslySetInnerHTML={{ __html: t('about.mission_desc') }}
            />
          </CardContent>
        </Card>

        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">{t('about.creativity_title')}</h3>
            <p className="text-sm text-muted-foreground text-center">
              {t('about.creativity_desc')}
            </p>
          </CardContent>
        </Card>

        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">{t('about.chef_title')}</h3>
            <p className="text-sm text-muted-foreground text-center">
              {t('about.chef_desc').split('Diego Schattenhofer')[0]}
              <a 
                href="https://diegoschatten.com/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent hover:underline font-medium"
              >
                Diego Schattenhofer
              </a>
              {t('about.chef_desc').split('Diego Schattenhofer')[1]}
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="flex justify-center mt-12">
        <Button 
          onClick={handleCTAClick}
          size="lg"
          className="bg-primary text-primary-foreground hover:bg-primary/90"
        >
          {t('about.cta')}
        </Button>
      </div>
    </section>
  );
}