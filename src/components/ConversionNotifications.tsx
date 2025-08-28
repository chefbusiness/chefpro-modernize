import { useState, useEffect } from 'react';
import { X } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';
import { useLanguage } from '@/hooks/useLanguage';
import { getRandomNotification } from '@/data/conversion-notifications';

const ConversionNotifications = () => {
  const [currentNotification, setCurrentNotification] = useState<any>(null);
  const { currentLanguage, t } = useLanguage();

  const SESSION_KEY = 'hideConversionNotifications';

  const isHiddenForSession = () => {
    return sessionStorage.getItem(SESSION_KEY) === 'true';
  };

  const hideForSession = () => {
    sessionStorage.setItem(SESSION_KEY, 'true');
    setCurrentNotification(null);
  };

  useEffect(() => {
    if (isHiddenForSession()) return;

    const showRandomNotification = () => {
      if (isHiddenForSession()) return;
      
      const notification = getRandomNotification(currentLanguage);
      setCurrentNotification(notification);

      // Auto hide after 6 seconds
      setTimeout(() => {
        setCurrentNotification(null);
      }, 6000);
    };

    // Show first notification after 4 seconds
    const initialTimeout = setTimeout(showRandomNotification, 4000);

    // Then show notifications every 25-40 seconds
    const interval = setInterval(() => {
      if (!isHiddenForSession() && Math.random() > 0.6) { // 40% chance to show
        showRandomNotification();
      }
    }, 32000);

    return () => {
      clearTimeout(initialTimeout);
      clearInterval(interval);
    };
  }, [currentLanguage]);

  if (!currentNotification) return null;

  return (
    <div 
      className="fixed inset-x-4 bottom-4 md:left-6 md:right-auto md:bottom-6 z-50 animate-fade-in-up"
      aria-live="polite"
    >
      <Card className="border-accent shadow-lg w-full md:max-w-sm" style={{
        background: 'linear-gradient(135deg, hsl(var(--accent-light) / 0.1) 0%, hsl(var(--accent) / 0.05) 100%)',
        backdropFilter: 'blur(8px)'
      }}>
        <CardContent className="p-4">
          <div className="flex items-start justify-between gap-3">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-full bg-accent flex items-center justify-center flex-shrink-0">
                <img 
                  src="https://blog.aichef.pro/wp-content/uploads/2024/09/Alguien-AI-Chef-Pro.png"
                  alt="AI Chef Pro User"
                  className="w-10 h-10 rounded-full object-cover"
                />
              </div>
              <div className="min-w-0">
                <div className="flex items-center gap-1 text-sm font-medium text-chef-dark">
                  <span>
                    {t('notifications.someone_from')} {currentNotification.city.city}
                  </span>
                  <span>{currentNotification.city.flag}</span>
                </div>
                <p className="text-sm text-chef-gray">
                  {currentLanguage === 'en' ? 
                    t('notifications.registered', { plan: currentNotification.plan.name }) :
                    `${t('notifications.registered')} ${currentNotification.plan.name} ${currentNotification.plan.price}${currentNotification.plan.currency} 😊`
                  }
                </p>
                <p className="text-xs text-chef-gray/70 mt-1">
                  {t('notifications.minutes_ago', { minutes: currentNotification.minutesAgo })}
                </p>
              </div>
            </div>
            <button
              onClick={hideForSession}
              className="text-chef-gray hover:text-chef-dark transition-colors p-1"
              aria-label="Hide notifications"
            >
              <X className="h-4 w-4" />
            </button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default ConversionNotifications;