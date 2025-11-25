import ModernHeader from '@/components/ModernHeader';
import ModernHero from '@/components/ModernHero';
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
import SEOHead from '@/components/SEOHead';

const Index = () => {
  return (
    <div className="min-h-screen bg-background overflow-x-hidden">
      <SEOHead />
      <ModernHeader />
      <main>
        <ModernHero />
        <ScreenshotSection />
        <SocialProofStrip />
        <AppsCategories />
        <AppsFinder />
        <CreatividadShowcase />
        <WorldCookbooks />
        <BusinessToolsShowcase />
        <ModernFeatures />
        <AIImageGallery />
        <FeaturedApps />
        <ModernChefSection />
        <ModernPricing />
        <CategoryCTAs />
        <ModernFAQ />
        <ConversionNotifications />
      </main>
      <ModernFooter />
    </div>
  );
};

export default Index;
