import { useState, useEffect } from 'react';
import { BookOpen, FileText, Download, Loader2 } from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';

interface DownloadUrls {
  ebook?: string;
  bonus1?: string;
  bonus23?: string;
}

export default function DownloadsSection() {
  const { token } = useAuth();
  const [urls, setUrls] = useState<DownloadUrls>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((data) => setUrls(data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  const cards = [
    {
      icon: BookOpen,
      title: 'Pro Prompts eBook',
      desc: 'El eBook completo en PDF con todos los prompts organizados por categorías.',
      url: urls.ebook,
      format: 'PDF',
      primary: true,
    },
    {
      icon: BookOpen,
      title: 'Bonus 1: Guía Prompt Engineering',
      desc: 'Aprende a crear tus propios prompts gastronómicos con el método AI Chef Pro.',
      url: urls.bonus1,
      format: 'Word',
    },
    {
      icon: FileText,
      title: 'Bonus 2: Plantillas + Cheat Sheet',
      desc: 'Plantillas listas para usar y resumen rápido de los mejores prompts.',
      url: urls.bonus23,
      format: 'Excel',
    },
  ];

  return (
    <section className="py-10 px-4">
      <div className="max-w-5xl mx-auto">
        <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">
          Tus descargas
        </p>
        <div className="grid md:grid-cols-3 gap-4">
          {cards.map((card) => {
            const Icon = card.icon;
            return (
              <div
                key={card.title}
                className={`rounded-xl p-5 ${
                  card.primary
                    ? 'bg-white/5 border-2 border-[#FFD700]/50'
                    : 'bg-white/5 border border-white/10'
                }`}
              >
                <Icon className="w-8 h-8 text-[#FFD700] mb-3" />
                <h3 className="text-white font-bold mb-1">{card.title}</h3>
                <p className="text-gray-400 text-sm mb-4">{card.desc}</p>
                {loading ? (
                  <Loader2 className="w-5 h-5 text-gray-500 animate-spin" />
                ) : card.url ? (
                  <a
                    href={card.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${
                      card.primary
                        ? 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90'
                        : 'border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10'
                    }`}
                  >
                    <Download className="w-4 h-4" />
                    Descargar {card.format}
                  </a>
                ) : (
                  <span className="text-gray-500 text-sm">No disponible</span>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
