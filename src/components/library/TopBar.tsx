export default function TopBar() {
  return (
    <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-md border-b border-white/10">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <a href="https://aichef.pro" className="flex items-center gap-2">
          <img src="/ai-chef-pro-logo.svg" alt="AI Chef Pro" className="h-8" />
        </a>
        <span className="px-3 py-1 bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-xs font-bold rounded-full tracking-wider uppercase">
          Pro Prompts Library
        </span>
      </div>
    </header>
  );
}
