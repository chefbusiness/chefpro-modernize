import Header from '@/components/Header';
import HeroSection from '@/components/HeroSection';
import AboutSection from '@/components/AboutSection';
import FeaturesSection from '@/components/FeaturesSection';
import ChefDiegoSection from '@/components/ChefDiegoSection';
import PricingSection from '@/components/PricingSection';
import FAQSection from '@/components/FAQSection';
import Footer from '@/components/Footer';
import ConversionNotifications from '@/components/ConversionNotifications';

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <HeroSection />
        <AboutSection />
        <FeaturesSection />
        <ChefDiegoSection />
        <PricingSection />
        <FAQSection />
        <ConversionNotifications />
      </main>
      <Footer />
    </div>
  );
};

export default Index;
