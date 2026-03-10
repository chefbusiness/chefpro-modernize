import PromptCard from './PromptCard';
import type { Category } from '@/data/prompts';

interface Props {
  category: Category;
  openPromptId: number | null;
  onTogglePrompt: (id: number) => void;
}

export default function PromptCategory({ category, openPromptId, onTogglePrompt }: Props) {
  return (
    <div className="mb-10">
      <div className="flex items-center gap-3 mb-4">
        <h3 className="text-white font-bold text-lg">{category.title}</h3>
        <span className="px-2 py-0.5 bg-white/10 text-gray-400 text-xs rounded-full">
          {category.promptCount} prompts
        </span>
      </div>
      <div className="space-y-2">
        {category.prompts.map((prompt) => (
          <PromptCard
            key={prompt.id}
            number={prompt.id}
            title={prompt.title}
            text={prompt.text}
            compatible={prompt.compatible}
            isOpen={openPromptId === prompt.id}
            onToggle={() => onTogglePrompt(prompt.id)}
          />
        ))}
      </div>
    </div>
  );
}
