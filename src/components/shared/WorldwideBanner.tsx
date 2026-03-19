import { Globe } from 'lucide-react';

export default function WorldwideBanner() {
  return (
    <section className="py-10 px-4">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white/[0.03] border border-white/10 rounded-2xl p-6 md:p-8 flex flex-col md:flex-row items-center gap-5">
          <div className="w-14 h-14 rounded-full bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0">
            <Globe className="w-7 h-7 text-[#FFD700]" />
          </div>
          <div className="text-center md:text-left">
            <p className="text-white font-semibold mb-1">
              Compra desde cualquier parte del mundo
            </p>
            <p className="text-gray-400 text-sm leading-relaxed">
              Productos digitales en espa&ntilde;ol con descarga inmediata. Paga con tarjeta, Apple Pay o Google Pay desde Espa&ntilde;a, M&eacute;xico, Colombia, Argentina, Chile, EE.UU. o cualquier otro pa&iacute;s.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
