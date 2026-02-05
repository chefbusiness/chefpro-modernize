import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { Star } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

// Import chef avatars
import chefAvatar1 from '@/assets/avatars/chef-avatar-1.jpg';
import chefAvatar2 from '@/assets/avatars/chef-avatar-2.jpg';
import chefAvatar3 from '@/assets/avatars/chef-avatar-3.jpg';
import chefAvatar4 from '@/assets/avatars/chef-avatar-4.jpg';
import chefAvatar5 from '@/assets/avatars/chef-avatar-5.jpg';

const avatars = [chefAvatar1, chefAvatar2, chefAvatar3, chefAvatar4, chefAvatar5];

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
    <div className="flex flex-col sm:flex-row items-center gap-3 sm:gap-4 mb-4">
      {/* Overlapping Avatars */}
      <div className="flex -space-x-3">
        {avatars.map((avatar, i) => (
          <Avatar 
            key={i} 
            className="border-2 border-background w-9 h-9 sm:w-10 sm:h-10 ring-2 ring-background"
          >
            <AvatarImage src={avatar} alt={`Chef ${i + 1}`} />
            <AvatarFallback className="bg-muted text-xs">C{i + 1}</AvatarFallback>
          </Avatar>
        ))}
      </div>

      {/* Stars and Counter */}
      <div className="flex flex-col items-center sm:items-start gap-0.5">
        <div className="flex items-center gap-0.5">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star 
              key={i} 
              className={`h-4 w-4 ${i < 4 ? 'fill-accent text-accent' : 'fill-accent/50 text-accent'}`} 
            />
          ))}
        </div>
        <span className="text-sm text-muted-foreground">
          <span className="font-bold text-foreground">{formatNumber(3748149)}</span>{' '}
          {t('hero.social_proof_label')}
        </span>
      </div>
    </div>
  );
}
