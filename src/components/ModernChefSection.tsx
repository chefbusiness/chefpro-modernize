import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { ExternalLink } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import chefTeam1 from '@/assets/chef-team-1.jpg';
import chefTeam2 from '@/assets/chef-team-2.jpg';
import chefTeam3 from '@/assets/chef-team-3.jpg';

export default function ModernChefSection() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  const handleDiegoLink = () => {
    window.open('https://diegoschatten.com/', '_blank');
  };

  return (
    <section className="border-t bg-muted/20">
      <div className="container py-8 md:py-12 lg:py-24">
        <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
          <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
            {t('chef_section.title_part1')} {t('chef_section.title_part2')}{" "}
            <span className="gradient-text">{t('chef_section.title_part3')}</span>
          </h2>
          
          <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
            {t('chef_section.description_start')}{" "}
            <button 
              onClick={handleDiegoLink}
              className="font-semibold text-foreground hover:text-accent inline-flex items-center gap-1 underline underline-offset-4"
            >
              Diego Schattenhofer
              <ExternalLink className="h-4 w-4" />
            </button>
            {" "}{t('chef_section.description_end')}
          </p>

          <Button 
            onClick={handleCTAClick}
            size="lg"
            className="bg-primary text-primary-foreground hover:bg-primary/90 mt-4"
          >
            {t('chef_section.cta')}
          </Button>
        </div>

        {/* Images Grid */}
        <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3 mt-12">
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
               <img 
                 src={chefTeam1}
                 alt={t('chef_section.image1_alt')}
                 className="w-full h-64 object-cover"
               />
            </CardContent>
          </Card>
          
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
               <img 
                 src={chefTeam2}
                 alt={t('chef_section.image2_alt')}
                 className="w-full h-64 object-cover"
               />
            </CardContent>
          </Card>
          
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
               <img 
                 src={chefTeam3}
                 alt={t('chef_section.image3_alt')}
                 className="w-full h-64 object-cover"
               />
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}