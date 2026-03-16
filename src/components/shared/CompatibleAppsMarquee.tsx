// PNG logos
import aichefproIcon from '@/assets/logos/aichefpro-icon.png';
import openaiLogo from '@/assets/logos/openai.png';
import geminiLogo from '@/assets/logos/gemini.png';
import googleSheetsLogo from '@/assets/logos/google-sheets.png';
import wordLogo from '@/assets/logos/word.png';
import pdfLogo from '@/assets/logos/pdf.png';
import googleLogo from '@/assets/logos/google.png';
import perplexityLogo from '@/assets/logos/perplexity.png';
import excelLogo from '@/assets/logos/excel.png';

interface AppLogo {
  name: string;
  src: string;
}

const apps: AppLogo[] = [
  { name: 'AI Chef Pro', src: aichefproIcon },
  { name: 'ChatGPT', src: openaiLogo },
  { name: 'Gemini', src: geminiLogo },
  { name: 'Google Sheets', src: googleSheetsLogo },
  { name: 'Excel', src: excelLogo },
  { name: 'Word', src: wordLogo },
  { name: 'PDF', src: pdfLogo },
  { name: 'Google', src: googleLogo },
  { name: 'Perplexity', src: perplexityLogo },
];

function LogoCard({ app }: { app: AppLogo }) {
  return (
    <div className="flex-shrink-0 flex flex-col items-center gap-2 group">
      <div className="w-16 h-16 md:w-20 md:h-20 rounded-2xl bg-gray-100 border border-gray-200/50 flex items-center justify-center p-3 md:p-4 group-hover:bg-white group-hover:shadow-md transition-all duration-300">
        <img
          src={app.src}
          alt={app.name}
          className="w-full h-full object-contain"
          loading="lazy"
        />
      </div>
      <span className="text-[10px] md:text-xs text-gray-500 group-hover:text-gray-300 whitespace-nowrap transition-colors duration-300">
        {app.name}
      </span>
    </div>
  );
}

interface CompatibleAppsMarqueeProps {
  variant?: 'ebook' | 'kit';
}

export default function CompatibleAppsMarquee({ variant = 'ebook' }: CompatibleAppsMarqueeProps) {
  const title = variant === 'kit'
    ? <>Compatible con las <span className="text-[#FFD700]">Herramientas</span> que Ya Usas</>
    : <>Funciona con las <span className="text-[#FFD700]">Apps</span> que Usas a Diario</>;

  const subtitle = variant === 'kit'
    ? <>Funciona mejor con <a href="https://aichef.pro" className="text-[#FFD700] hover:underline">AI Chef Pro</a>. Compatible con Excel, Google Sheets, PDF y más</>
    : <>Funciona mejor con <a href="https://aichef.pro" className="text-[#FFD700] hover:underline">AI Chef Pro</a>. Compatible con ChatGPT, Claude, Gemini, Perplexity, Excel, Google Sheets y más</>;

  // Repeat enough times for seamless loop (4x ensures no gaps on any screen)
  const repeated = [...apps, ...apps, ...apps, ...apps];

  return (
    <section className="py-10 md:py-14 overflow-hidden">
      <div className="text-center mb-8 px-4">
        <h2 className="text-xl md:text-2xl font-bold text-white mb-2">
          {title}
        </h2>
        <p className="text-gray-500 text-sm md:text-base">
          {subtitle}
        </p>
      </div>

      <div className="relative overflow-hidden">
        {/* Fade edges */}
        <div className="absolute left-0 top-0 bottom-0 w-16 md:w-24 bg-gradient-to-r from-[#0a0a0a] to-transparent z-10 pointer-events-none" />
        <div className="absolute right-0 top-0 bottom-0 w-16 md:w-24 bg-gradient-to-l from-[#0a0a0a] to-transparent z-10 pointer-events-none" />

        <div
          className="flex items-center gap-6 md:gap-8 animate-marquee-scroll"
          style={{ width: 'max-content' }}
        >
          {repeated.map((app, i) => (
            <LogoCard key={`${app.name}-${i}`} app={app} />
          ))}
        </div>
      </div>
    </section>
  );
}
