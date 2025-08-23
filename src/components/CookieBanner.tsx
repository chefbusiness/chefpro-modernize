import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { X } from 'lucide-react';

const CookieBanner = () => {
  const { t } = useTranslation();
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const consent = localStorage.getItem('cookie-consent');
    if (!consent) {
      setIsVisible(true);
    }
  }, []);

  const acceptCookies = () => {
    localStorage.setItem('cookie-consent', 'accepted');
    setIsVisible(false);
  };

  const rejectCookies = () => {
    localStorage.setItem('cookie-consent', 'rejected');
    setIsVisible(false);
  };

  if (!isVisible) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 p-4">
      <Card className="mx-auto max-w-4xl p-6 bg-background/95 backdrop-blur-sm border shadow-lg">
        <div className="flex items-start justify-between gap-4">
          <div className="flex-1">
            <h3 className="font-semibold text-foreground mb-2">
              {t('cookies.banner.title')}
            </h3>
            <p className="text-sm text-muted-foreground mb-4">
              {t('cookies.banner.description')}
            </p>
            <div className="flex flex-wrap gap-3">
              <Button onClick={acceptCookies} size="sm">
                {t('cookies.banner.accept')}
              </Button>
              <Button onClick={rejectCookies} variant="outline" size="sm">
                {t('cookies.banner.reject')}
              </Button>
              <Button variant="ghost" size="sm" asChild>
                <a href="/cookies" target="_blank" rel="noopener noreferrer">
                  {t('cookies.banner.learn_more')}
                </a>
              </Button>
            </div>
          </div>
          <Button
            variant="ghost"
            size="sm"
            onClick={rejectCookies}
            className="shrink-0"
          >
            <X className="h-4 w-4" />
          </Button>
        </div>
      </Card>
    </div>
  );
};

export default CookieBanner;