import { useTranslation } from 'react-i18next';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';

const Privacy = () => {
  const { t } = useTranslation();

  return (
    <div className="min-h-screen bg-background">
      <SEOHead 
        title={t('pages.privacy.title')}
        description={t('pages.privacy.description')}
      />
      <ModernHeader />
      <main className="py-20">
        <div className="container mx-auto px-4">
          <div className="max-w-4xl mx-auto">
            <h1 className="text-4xl font-bold text-foreground mb-8">
              {t('pages.privacy.heading')}
            </h1>
            <div className="prose prose-lg max-w-none text-muted-foreground space-y-4">
              {(() => {
                const paragraphs = t('pages.privacy.content_paragraphs', { returnObjects: true });
                if (Array.isArray(paragraphs)) {
                  return paragraphs.map((paragraph, index) => (
                    <div key={index} dangerouslySetInnerHTML={{ __html: paragraph.replace(/\n/g, '<br />') }} />
                  ));
                }
                return <p>{t('pages.privacy.content')}</p>;
              })()}
            </div>
          </div>
        </div>
      </main>
      <ModernFooter />
    </div>
  );
};

export default Privacy;