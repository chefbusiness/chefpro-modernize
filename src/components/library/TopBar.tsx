import logo from '@/assets/logo-ai-chef-pro.svg';

export default function TopBar() {
  return (
    <header className="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <a href="https://aichef.pro" className="flex items-center gap-2">
          <img src={logo} alt="AI Chef Pro" className="h-8" />
        </a>
        <span className="px-3 py-1 bg-amber-100 border border-amber-300 text-amber-800 text-xs font-bold rounded-full tracking-wider uppercase">
          Pro Prompts Library
        </span>
      </div>
    </header>
  );
}
