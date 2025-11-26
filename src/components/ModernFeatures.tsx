import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Brain, Utensils, Heart } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import llmAiChefPro from '@/assets/llm-ai-chef-pro.png';
import llmMistral from '@/assets/llm-mistral.png';
import llmOpenAI from '@/assets/llm-openai.png';
import llmAnthropic from '@/assets/llm-anthropic.png';
import llmMetaLlama from '@/assets/llm-meta-llama.png';

export default function ModernFeatures() {
  const { t } = useLanguage();

  const llmModels = [
    { image: llmAiChefPro, name: t('features.llm_models.ai_chef_pro') },
    { image: llmMistral, name: t('features.llm_models.mistral') },
    { image: llmOpenAI, name: t('features.llm_models.openai') },
    { image: llmAnthropic, name: t('features.llm_models.anthropic') },
    { image: llmMetaLlama, name: t('features.llm_models.meta_llama') }
  ];

  const features = [
    {
      icon: Brain,
      title: t('features.ai_assistant'),
      description: t('features.ai_assistant_desc')
    },
    {
      icon: Utensils,
      title: t('features.food_pairing'),
      description: t('features.food_pairing_desc')
    },
    {
      icon: Heart,
      title: t('features.coaching'),
      description: t('features.coaching_desc')
    }
  ];

  return (
    <section id="herramientas" className="container py-8 md:py-12 lg:py-24">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          {t('features.title')}
        </h2>
        <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance">
          {t('features.description')}
        </p>
      </div>

      {/* Main Feature Video */}
      <div className="mx-auto max-w-4xl mt-12 mb-12">
        <div className="relative rounded-xl border bg-muted/30 p-4 overflow-hidden">
          <div className="relative pb-[56.25%] h-0">
            <iframe 
              src="https://www.loom.com/embed/ec50c20372974b76b7c3c000500bf48b"
              frameBorder="0" 
              allowFullScreen
              className="absolute top-0 left-0 w-full h-full rounded-lg"
            />
          </div>
        </div>
      </div>

      {/* Feature Cards */}
      <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3">
        {features.map((feature, index) => (
          <Card key={index} className="category-card-knowledge hover-card">
            <CardHeader>
              <div className="category-icon h-12 w-12 rounded-full flex items-center justify-center mb-2">
                <feature.icon className="h-6 w-6" />
              </div>
              <CardTitle className="text-lg">{feature.title}</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription className="text-sm leading-6">
                {feature.description}
              </CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* LLM Models */}
      <div className="mt-16">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold mb-2">{t('features.llm_title')}</h3>
          <p className="text-muted-foreground">
            {t('features.llm_description')}
          </p>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 max-w-4xl mx-auto">
          {llmModels.map((model, index) => (
            <div key={index} className="rounded-lg border bg-card overflow-hidden hover-card">
              <img 
                src={model.image}
                alt={model.name}
                className="w-full h-20 object-cover"
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}