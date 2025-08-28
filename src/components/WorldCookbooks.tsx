import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { worldCookbooks } from '@/data/apps';
import { useState } from 'react';
import { useLanguage } from '@/hooks/useLanguage';

// Utility function to normalize cuisine names for translation keys
const normalizeCuisineName = (name: string): string => {
  return name
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Remove accents
    .replace(/\s+/g, '_'); // Replace spaces with underscores
};

export default function WorldCookbooks() {
  const { t } = useLanguage();

  return (
    <section id="recetarios" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">{t('showcase.world_title')}</span>
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          {t('showcase.world_description')}
        </p>
      </div>

      <div className="space-y-8">
        {/* Europa */}
        <div>
          <h3 className="text-xl sm:text-2xl font-semibold mb-4 flex flex-col sm:flex-row items-center justify-center text-center gap-2">
            <span className="flex items-center gap-2">
              🌍 <span className="gradient-text">{t('categories.world_cookbooks.europa.name')}</span>
            </span>
            <Badge variant="secondary" className="text-xs w-fit">{t('categories.world_cookbooks.europa.count')}</Badge>
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 sm:gap-4">
            {worldCookbooks.europa.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50 active:scale-95"
              >
                <CardHeader className="p-3 sm:p-4 pb-2">
                  <CardTitle className="text-center text-sm sm:text-base flex flex-col items-center gap-1">
                    <span className="text-xl sm:text-2xl">{cuisine.flag}</span>
                    <span className="text-xs sm:text-sm leading-tight">{t(`cookbooks.${normalizeCuisineName(cuisine.name)}`)}</span>
                  </CardTitle>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>

        {/* Latinoamérica */}
        <div>
          <h3 className="text-xl sm:text-2xl font-semibold mb-4 flex flex-col sm:flex-row items-center justify-center text-center gap-2">
            <span className="flex items-center gap-2">
              🌎 <span className="gradient-text">{t('categories.world_cookbooks.latinoamerica.name')}</span>
            </span>
            <Badge variant="secondary" className="text-xs w-fit">{t('categories.world_cookbooks.latinoamerica.count')}</Badge>
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 sm:gap-4">
            {worldCookbooks.latinoamerica.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50 active:scale-95"
              >
                <CardHeader className="p-3 sm:p-4 pb-2">
                  <CardTitle className="text-center text-sm sm:text-base flex flex-col items-center gap-1">
                    <span className="text-xl sm:text-2xl">{cuisine.flag}</span>
                    <span className="text-xs sm:text-sm leading-tight">{t(`cookbooks.${normalizeCuisineName(cuisine.name)}`)}</span>
                  </CardTitle>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>

        {/* Asia */}
        <div>
          <h3 className="text-xl sm:text-2xl font-semibold mb-4 flex flex-col sm:flex-row items-center justify-center text-center gap-2">
            <span className="flex items-center gap-2">
              🌏 <span className="gradient-text">{t('categories.world_cookbooks.asia.name')}</span>
            </span>
            <Badge variant="secondary" className="text-xs w-fit">{t('categories.world_cookbooks.asia.count')}</Badge>
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
            {worldCookbooks.asia.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50 active:scale-95"
              >
                <CardHeader className="p-3 sm:p-4 pb-2">
                  <CardTitle className="text-center text-sm sm:text-base flex flex-col items-center gap-1">
                    <span className="text-xl sm:text-2xl">{cuisine.flag}</span>
                    <span className="text-xs sm:text-sm leading-tight">{t(`cookbooks.${normalizeCuisineName(cuisine.name)}`)}</span>
                  </CardTitle>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}