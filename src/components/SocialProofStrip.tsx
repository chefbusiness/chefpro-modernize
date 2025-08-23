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
            suffix={t('stats.apps').replace('55', '')}
            label={t('stats.apps_label')}
          />
          <CounterStat 
            end={25} 
            suffix={t('stats.cookbooks').replace('25', '')}
            label={t('stats.cookbooks_label')}
          />
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={6} 
              suffix={t('stats.categories').replace('6', '')}
              label={t('stats.categories_label')}
            />
          </div>
          <div className="col-span-2 md:col-span-1">
            <CounterStat 
              end={1} 
              suffix={t('stats.new_app').replace('1', '')}
              label={t('stats.new_app_label')}
            />
          </div>
          <div className="col-span-2 md:col-span-4 lg:col-span-1">
            <CounterStat 
              end={10000} 
              suffix={t('stats.chefs').replace('10,000', '')}
              label={t('stats.chefs_label')}
            />
          </div>
        </div>
      </div>
    </section>
  );
}