import { useState, useEffect } from 'react';
import { X } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';

interface Notification {
  id: number;
  location: string;
  plan: string;
  price: string;
  flag: string;
}

const ConversionNotifications = () => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [currentNotification, setCurrentNotification] = useState<Notification | null>(null);

  const sampleNotifications: Notification[] = [
    { id: 1, location: 'Madrid', plan: 'Premium', price: '15€', flag: '🇪🇸' },
    { id: 2, location: 'Miami, FL', plan: 'Premium Plus', price: '50€', flag: '🇺🇸' },
    { id: 3, location: 'Arona, Tenerife', plan: 'Premium Pro', price: '25€', flag: '🇪🇸' },
    { id: 4, location: 'Bogotá, Colombia', plan: 'Premium', price: '15€', flag: '🇨🇴' },
    { id: 5, location: 'Barcelona, Cataluña', plan: 'Premium Plus', price: '50€', flag: '🇪🇸' },
    { id: 6, location: 'París, Francia', plan: 'Pro', price: '10€', flag: '🇫🇷' },
    { id: 7, location: 'Roma, Italia', plan: 'Premium', price: '15€', flag: '🇮🇹' },
  ];

  useEffect(() => {
    const showRandomNotification = () => {
      const randomNotification = sampleNotifications[Math.floor(Math.random() * sampleNotifications.length)];
      setCurrentNotification(randomNotification);

      // Auto hide after 5 seconds
      setTimeout(() => {
        setCurrentNotification(null);
      }, 5000);
    };

    // Show first notification after 3 seconds
    const initialTimeout = setTimeout(showRandomNotification, 3000);

    // Then show notifications every 15-30 seconds
    const interval = setInterval(() => {
      if (Math.random() > 0.7) { // 30% chance to show
        showRandomNotification();
      }
    }, 20000);

    return () => {
      clearTimeout(initialTimeout);
      clearInterval(interval);
    };
  }, []);

  if (!currentNotification) return null;

  return (
    <div className="fixed bottom-6 left-6 z-50 animate-fade-in-up">
      <Card className="chef-card border-chef-gold/20 bg-white/95 backdrop-blur-sm shadow-glow max-w-sm">
        <CardContent className="p-4">
          <div className="flex items-start justify-between gap-3">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-full bg-gradient-cta flex items-center justify-center flex-shrink-0">
                <img 
                  src="https://blog.aichef.pro/wp-content/uploads/2024/09/Alguien-AI-Chef-Pro.png"
                  alt="Usuario AI Chef Pro"
                  className="w-10 h-10 rounded-full object-cover"
                />
              </div>
              <div className="min-w-0">
                <div className="flex items-center gap-1 text-sm font-medium text-chef-dark">
                  <span>Alguien de {currentNotification.location}</span>
                  <span>{currentNotification.flag}</span>
                </div>
                <p className="text-sm text-chef-gray">
                  Se ha registrado 💜 al Plan {currentNotification.plan} {currentNotification.price} 😊
                </p>
                <p className="text-xs text-chef-gray/70 mt-1">
                  Hace 10 minutos
                </p>
              </div>
            </div>
            <button
              onClick={() => setCurrentNotification(null)}
              className="text-chef-gray hover:text-chef-dark transition-colors p-1"
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