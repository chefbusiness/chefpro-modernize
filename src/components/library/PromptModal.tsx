import { useState, useEffect } from 'react';
import { X, Copy, Check } from 'lucide-react';

interface Props {
  number: number;
  title: string;
  text: string;
  compatible: string[];
  onClose: () => void;
}

export default function PromptModal({ number, title, text, compatible, onClose }: Props) {
  const [copied, setCopied] = useState(false);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    requestAnimationFrame(() => setVisible(true));
    const handleEsc = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose(); };
    document.addEventListener('keydown', handleEsc);
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', handleEsc);
      document.body.style.overflow = '';
    };
  }, [onClose]);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const formattedNumber = String(number).padStart(2, '0');

  return (
    <div
      className={`fixed inset-0 z-50 flex items-center justify-center p-4 transition-all duration-200 ${
        visible ? 'bg-black/70 backdrop-blur-sm' : 'bg-black/0'
      }`}
      onClick={onClose}
    >
      <div
        className={`relative w-full max-w-2xl max-h-[85vh] bg-[#141414] border border-[#FFD700]/30 rounded-2xl overflow-hidden shadow-2xl shadow-[#FFD700]/10 transition-all duration-300 ${
          visible ? 'opacity-100 scale-100 translate-y-0' : 'opacity-0 scale-95 translate-y-4'
        }`}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-5 border-b border-white/10">
          <div className="flex items-center gap-3">
            <span className="text-[#FFD700] text-sm font-mono font-bold bg-[#FFD700]/10 px-2.5 py-1 rounded">
              #{formattedNumber}
            </span>
            <h3 className="text-white font-bold text-lg">{title}</h3>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 transition-colors text-gray-400 hover:text-white"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Prompt text */}
        <div className="p-5 overflow-y-auto max-h-[60vh]">
          <div className="bg-black/40 border border-white/5 rounded-xl p-5">
            <pre className="text-gray-300 text-sm whitespace-pre-wrap font-sans leading-relaxed">
              {text}
            </pre>
          </div>
        </div>

        {/* Footer */}
        <div className="flex items-center justify-between p-5 border-t border-white/10 bg-white/[0.02]">
          <span className="text-gray-500 text-xs">
            {compatible.join(' · ')}
          </span>
          <button
            onClick={handleCopy}
            className={`inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-bold transition-all ${
              copied
                ? 'bg-green-500/20 text-green-400'
                : 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90 hover:scale-[1.02] active:scale-[0.98]'
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
        </div>
      </div>
    </div>
  );
}
