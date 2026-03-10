import { useState } from 'react';
import { ChevronDown, Copy, Check } from 'lucide-react';

interface Props {
  number: number;
  title: string;
  text: string;
  compatible: string[];
  isOpen: boolean;
  onToggle: () => void;
}

export default function PromptCard({ number, title, text, compatible, isOpen, onToggle }: Props) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const formattedNumber = String(number).padStart(2, '0');

  return (
    <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
      <button
        onClick={onToggle}
        className="w-full flex items-center gap-3 p-4 text-left hover:bg-white/5 transition-colors"
      >
        <span className="text-[#FFD700] text-sm font-mono font-bold flex-shrink-0">
          #{formattedNumber}
        </span>
        <span className="text-white font-medium flex-1">{title}</span>
        <ChevronDown
          className={`w-5 h-5 text-gray-500 flex-shrink-0 transition-transform duration-300 ${
            isOpen ? 'rotate-180' : ''
          }`}
        />
      </button>

      <div
        className={`grid transition-all duration-300 ${
          isOpen ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'
        }`}
      >
        <div className="overflow-hidden">
          <div className="px-4 pb-4">
            {/* Prompt text */}
            <div className="bg-black/30 border border-white/5 rounded-lg p-4 mb-3">
              <pre className="text-gray-300 text-sm whitespace-pre-wrap font-sans leading-relaxed">
                {text}
              </pre>
            </div>

            {/* Actions row */}
            <div className="flex items-center justify-between">
              <button
                onClick={handleCopy}
                className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${
                  copied
                    ? 'bg-green-500/20 text-green-400'
                    : 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90'
                }`}
              >
                {copied ? (
                  <>
                    <Check className="w-4 h-4" />
                    ¡Copiado!
                  </>
                ) : (
                  <>
                    <Copy className="w-4 h-4" />
                    Copiar prompt
                  </>
                )}
              </button>
              <span className="text-gray-500 text-xs">
                {compatible.join(' · ')}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
