import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
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

export default function HeroSocialProof() {
  const { t } = useLanguage();

  return (
    <div className="flex flex-col items-center gap-2 mb-4">
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

      <p className="text-sm font-medium text-foreground text-center text-balance">
        {t('hero.v2_agents_line')}
      </p>
    </div>
  );
}
