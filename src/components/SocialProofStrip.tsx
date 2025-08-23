import CounterStat from './CounterStat';
import { useLanguage } from '@/hooks/useLanguage';

export default function SocialProofStrip() {
  const { t } = useLanguage();

  return (
    <section className="border-y bg-muted/30 py-12">
      <div className="container">
        <div className="grid grid-cols-2 gap-4 sm:gap-6 md:grid-cols-4 lg:grid-cols-5 lg:gap-8 text-center">
          <CounterStat 
            end={55} 
            suffix="+"
            label={t('stats.apps_label')}
          />
          <CounterStat 
            end={25} 
            suffix="+"
            label={t('stats.cookbooks_label')}
          />
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={6} 
              suffix=""
              label={t('stats.categories_label')}
            />
          </div>
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={1} 
              suffix=""
              label={t('stats.new_app_label')}
            />
          </div>
          <div className="col-span-2 md:col-span-4 lg:col-span-1">
            <CounterStat 
              end={764} 
              suffix="+"
              label={t('stats.chefs_label')}
            />
          </div>
        </div>
      </div>
    </section>
  );
}