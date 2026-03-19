import FadeIn from '../ebook/FadeIn';

export default function AuthorSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <div className="bg-white/[0.03] border border-white/10 rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-8">
            <div className="flex-shrink-0">
              <div className="w-28 h-28 md:w-36 md:h-36 rounded-full overflow-hidden border-[3px] border-[#FFD700]/40 shadow-lg shadow-[#FFD700]/10">
                <img
                  src="/chef-john-guerrero-ebook.jpg"
                  alt="Chef John Guerrero"
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
            <div className="text-center md:text-left">
              <p className="text-[#FFD700] text-xs font-bold tracking-[0.2em] uppercase mb-2">Creado por</p>
              <h3 className="text-white text-xl md:text-2xl font-bold mb-3">Chef John Guerrero</h3>
              <p className="text-gray-400 leading-relaxed text-sm md:text-base mb-4">
                CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha diseñado sistemas operativos y checklists para cientos de restaurantes y cafeterías.
              </p>
              <div className="flex flex-wrap items-center justify-center md:justify-start gap-3">
                <span className="px-3 py-1 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/20 text-[#FFD700] text-xs font-medium">
                  CEO AI Chef Pro
                </span>
                <span className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-400 text-xs font-medium">
                  Consultor Gastronómico
                </span>
                <span className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-400 text-xs font-medium">
                  +29 años en alta hostelería
                </span>
              </div>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
