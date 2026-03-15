import PromptCard from './PromptCard';
import type { Category } from '@/data/prompts';

interface Props {
  category: Category;
  onSelectPrompt: (promptId: number) => void;
}

export default function PromptCategory({ category, onSelectPrompt }: Props) {
  return (
    <div className="mb-10">
      <div className="flex items-center gap-3 mb-4">
        <h3 className="text-white font-bold text-lg">{category.title}</h3>
        <span className="px-2 py-0.5 bg-white/10 text-gray-400 text-xs rounded-full">
          {category.promptCount} prompts
        </span>
      </div>
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
        {category.prompts.map((prompt) => (
          <PromptCard
            key={prompt.id}
            number={prompt.id}
            title={prompt.title}
            onClick={() => onSelectPrompt(prompt.id)}
          />
        ))}
      </div>
    </div>
  );
}
