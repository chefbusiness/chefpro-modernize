import { useRef, useEffect } from 'react';

interface Testimonial {
  name: string;
  role: string;
  text: string;
  avatar: string;
}

interface Props {
  title?: React.ReactNode;
  subtitle?: string;
  testimonials: Testimonial[];
}

function MarqueeRow({ items, direction = 'left', duration = 40 }: { items: Testimonial[]; direction?: 'left' | 'right'; duration?: number }) {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;

    let animationId: number;
    let position = direction === 'left' ? 0 : -(el.scrollWidth / 2);
    const speed = (el.scrollWidth / 2) / (duration * 60); // pixels per frame at 60fps

    const animate = () => {
      if (direction === 'left') {
        position -= speed;
        if (position <= -(el.scrollWidth / 2)) position = 0;
      } else {
        position += speed;
        if (position >= 0) position = -(el.scrollWidth / 2);
      }
      el.style.transform = `translateX(${position}px)`;
      animationId = requestAnimationFrame(animate);
    };

    animationId = requestAnimationFrame(animate);

    const handleMouseEnter = () => cancelAnimationFrame(animationId);
    const handleMouseLeave = () => { animationId = requestAnimationFrame(animate); };

    el.addEventListener('mouseenter', handleMouseEnter);
    el.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      cancelAnimationFrame(animationId);
      el.removeEventListener('mouseenter', handleMouseEnter);
      el.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, [direction, duration]);

  // Duplicate items for seamless loop
  const duplicated = [...items, ...items];

  return (
    <div className="overflow-hidden relative">
      {/* Fade edges */}
      <div className="absolute left-0 top-0 bottom-0 w-16 md:w-32 bg-gradient-to-r from-[#0a0a0a] to-transparent z-10 pointer-events-none" />
      <div className="absolute right-0 top-0 bottom-0 w-16 md:w-32 bg-gradient-to-l from-[#0a0a0a] to-transparent z-10 pointer-events-none" />

      <div ref={scrollRef} className="flex gap-4 will-change-transform">
        {duplicated.map((t, i) => (
          <div
            key={`${t.name}-${i}`}
            className="flex-shrink-0 w-[300px] md:w-[360px] relative group"
          >
            {/* 3D shadow layer */}
            <div className="absolute inset-0 rounded-xl bg-[#FFD700]/20 translate-y-1 translate-x-1 opacity-0 group-hover:opacity-100 transition-all duration-300" />
            <div className="relative bg-[#0a0a0a] border border-white/10 rounded-xl p-5 group-hover:border-[#FFD700]/40 group-hover:-translate-y-0.5 group-hover:-translate-x-0.5 transition-all duration-300"
          >
            <div className="flex items-center gap-3 mb-3">
              <img
                src={t.avatar}
                alt={t.name}
                className="w-10 h-10 rounded-full object-cover border border-white/10"
              />
              <div>
                <p className="text-white font-semibold text-sm">{t.name}</p>
                <p className="text-gray-500 text-xs">{t.role}</p>
              </div>
            </div>
            <p className="text-gray-300 text-sm leading-relaxed">"{t.text}"</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function TestimonialsMarquee({ title, subtitle, testimonials }: Props) {
  const mid = Math.ceil(testimonials.length / 2);
  const topRow = testimonials.slice(0, mid);
  const bottomRow = testimonials.slice(mid);

  return (
    <section className="py-16 md:py-24 overflow-hidden">
      {(title || subtitle) && (
        <div className="text-center mb-10 px-4">
          {title && (
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">{title}</h2>
          )}
          {subtitle && (
            <p className="text-gray-400 text-lg max-w-2xl mx-auto">{subtitle}</p>
          )}
        </div>
      )}

      <div className="space-y-4">
        <MarqueeRow items={topRow} direction="left" duration={45} />
        <MarqueeRow items={bottomRow} direction="right" duration={50} />
      </div>
    </section>
  );
}
