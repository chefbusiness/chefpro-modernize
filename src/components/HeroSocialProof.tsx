import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { Star } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

// Import diverse professional avatars
import avatar1 from '@/assets/avatars/avatar-1.jpg';
import avatar2 from '@/assets/avatars/avatar-2.jpg';
import avatar3 from '@/assets/avatars/avatar-3.jpg';
import avatar4 from '@/assets/avatars/avatar-4.jpg';
import avatar5 from '@/assets/avatars/avatar-5.jpg';
import avatar6 from '@/assets/avatars/avatar-6.jpg';
import avatar7 from '@/assets/avatars/avatar-7.jpg';
import avatar8 from '@/assets/avatars/avatar-8.jpg';

const avatars = [avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7, avatar8];

function getDynamicCount(): number {
  const BASE_DATE = new Date('2026-02-12');
  const BASE_COUNT = 48149;
  const today = new Date();
  const diffTime = today.getTime() - BASE_DATE.getTime();
  const diffDays = Math.max(0, Math.floor(diffTime / (1000 * 60 * 60 * 24)));
  let total = BASE_COUNT;
  for (let i = 1; i <= diffDays; i++) {
    const seed = (i * 7 + 13) % 21;
    total += 60 + seed;
  }
  return total;
}

export default function HeroSocialProof() {
  const { t, currentLanguage } = useLanguage();

  // Format number based on locale
  const formatNumber = (num: number) => {
    if (currentLanguage === 'en') {
      return num.toLocaleString('en-US');
    }
    return num.toLocaleString('es-ES');
  };

  return (
    <div className="flex flex-col items-center gap-2 mb-4">
      {/* Overlapping Avatars - Centered */}
      <div className="flex -space-x-3 justify-center">
        {avatars.map((avatar, i) => (
          <Avatar 
            key={i} 
            className="border-2 border-background w-9 h-9 sm:w-10 sm:h-10 ring-2 ring-background"
          >
            <AvatarImage src={avatar} alt={`Professional ${i + 1}`} />
            <AvatarFallback className="bg-muted text-xs">P{i + 1}</AvatarFallback>
          </Avatar>
        ))}
      </div>

      {/* Stars and Counter - Centered */}
      <div className="flex flex-col items-center gap-0.5">
        <div className="flex items-center gap-0.5">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star 
              key={i} 
              className={`h-4 w-4 ${i < 4 ? 'fill-accent text-accent' : 'fill-accent/50 text-accent'}`} 
            />
          ))}
        </div>
        <span className="text-sm text-muted-foreground">
          <span className="font-bold text-foreground">{formatNumber(getDynamicCount())}</span>{' '}
          {t('hero.social_proof_label')}
        </span>
      </div>
    </div>
  );
}
