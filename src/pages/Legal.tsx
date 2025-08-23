import { useTranslation } from 'react-i18next';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';

const Legal = () => {
  const { t } = useTranslation();

  return (
    <div className="min-h-screen bg-background">
      <SEOHead 
        title={t('pages.legal.title')}
        description={t('pages.legal.description')}
      />
      <ModernHeader />
      <main className="py-20">
        <div className="container mx-auto px-4">
          <div className="max-w-4xl mx-auto">
            <h1 className="text-4xl font-bold text-foreground mb-8">
              {t('pages.legal.heading')}
            </h1>
            <div className="prose prose-lg max-w-none text-muted-foreground">
              <p>{t('pages.legal.content')}</p>
            </div>
          </div>
        </div>
      </main>
      <ModernFooter />
    </div>
  );
};

export default Legal;