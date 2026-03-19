import logo from '@/assets/logo-ai-chef-pro.svg';

/**
 * AI Chef Pro logo in a white rounded card.
 * For use on dark backgrounds (product pages, dashboards).
 * Links back to the homepage.
 */
export default function LogoBadge() {
  return (
    <div className="flex justify-center pt-10 md:pt-14">
      <a
        href="/"
        className="inline-flex items-center px-6 py-3 bg-white rounded-2xl shadow-lg shadow-white/5 hover:shadow-white/10 transition-shadow"
      >
        <img
          src={logo}
          alt="AI Chef Pro"
          className="h-8 md:h-9 w-auto"
        />
      </a>
    </div>
  );
}
