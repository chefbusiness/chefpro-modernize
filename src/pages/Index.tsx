import ModernHeader from '@/components/ModernHeader';
import ModernHero from '@/components/ModernHero';
import ModernAbout from '@/components/ModernAbout';
import ModernFeatures from '@/components/ModernFeatures';
import ModernChefSection from '@/components/ModernChefSection';
import ModernPricing from '@/components/ModernPricing';
import ModernFAQ from '@/components/ModernFAQ';
import ModernFooter from '@/components/ModernFooter';
import ConversionNotifications from '@/components/ConversionNotifications';

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <ModernHeader />
      <main>
        <ModernHero />
        <ModernAbout />
        <ModernFeatures />
        <ModernChefSection />
        <ModernPricing />
        <ModernFAQ />
        <ConversionNotifications />
      </main>
      <ModernFooter />
    </div>
  );
};

export default Index;
