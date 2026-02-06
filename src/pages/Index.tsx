import ModernHeader from '@/components/ModernHeader';
import ModernHero from '@/components/ModernHero';
import TrustedByLogos from '@/components/TrustedByLogos';
import ScreenshotSection from '@/components/ScreenshotSection';
import SocialProofStrip from '@/components/SocialProofStrip';
import AppsCategories from '@/components/AppsCategories';
import AppsFinder from '@/components/AppsFinder';
import CreatividadShowcase from '@/components/CreatividadShowcase';
import WorldCookbooks from '@/components/WorldCookbooks';
import BusinessToolsShowcase from '@/components/BusinessToolsShowcase';
import ModernAbout from '@/components/ModernAbout';
import ModernFeatures from '@/components/ModernFeatures';
import AIImageGallery from '@/components/AIImageGallery';
import FeaturedApps from '@/components/FeaturedApps';
import ModernChefSection from '@/components/ModernChefSection';
import ModernPricing from '@/components/ModernPricing';
import CategoryCTAs from '@/components/CategoryCTAs';
import ModernFAQ from '@/components/ModernFAQ';
import ModernFooter from '@/components/ModernFooter';
import ConversionNotifications from '@/components/ConversionNotifications';
import FormacionPromoPopup from '@/components/FormacionPromoPopup';
import SEOHead from '@/components/SEOHead';
import { useTranslation } from 'react-i18next';

const Index = () => {
  const { t } = useTranslation();
  
  return (
    <div className="min-h-screen bg-background overflow-x-hidden">
      <SEOHead 
        title={t('pages.index.seo_title')}
        description={t('pages.index.seo_description')}
        keywords={t('pages.index.seo_keywords')}
      />
      <ModernHeader />
      <main>
        <ModernHero />
        <TrustedByLogos />
        <ScreenshotSection />
        <SocialProofStrip />
        <AppsCategories />
        <AIImageGallery />
        <AppsFinder />
        <CreatividadShowcase />
        <WorldCookbooks />
        <BusinessToolsShowcase />
        <ModernFeatures />
        <FeaturedApps />
        <ModernChefSection />
        <ModernPricing />
        <CategoryCTAs />
        <ModernFAQ />
        <ConversionNotifications />
        <FormacionPromoPopup />
      </main>
      <ModernFooter />
    </div>
  );
};

export default Index;
