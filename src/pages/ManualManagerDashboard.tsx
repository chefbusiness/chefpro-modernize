import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, ArrowLeft,
  BookOpen, FileText, BarChart3, Layers,
  MessageSquare, UserPlus, ScrollText, ClipboardList,
  ClipboardCheck, GraduationCap, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const SECTIONS = [
  {
    title: 'Manual Principal',
    templates: [
      { key: 'manual-pdf', icon: BookOpen, title: 'Manual Completo (PDF)', desc: '20 capítulos con las tablas construidas desde las herramientas Excel y desde la norma citada.', ext: '.pdf' },
      { key: 'manual-docx', icon: FileText, title: 'Manual Completo (DOCX Editable)', desc: 'Mismo contenido en formato editable para anotar y adaptarlo a tu casa.', ext: '.docx' },
    ],
  },
  {
    title: 'Herramientas Excel (7)',
    templates: [
      { key: 'cuadro-semanal', icon: BarChart3, title: 'Cuadro de Mando Semanal del Manager', desc: '52 semanas ISO con ventas, coste de producto y de personal, prime cost, semáforos y hoja de definiciones.', ext: '.xlsx' },
      { key: 'matriz-polivalencia', icon: Layers, title: 'Matriz de Formación y Polivalencia', desc: 'Quién sabe hacer qué y a qué nivel, plan de formación cruzada, cobertura por estación y coste de una baja.', ext: '.xlsx' },
      { key: 'quejas-resenas', icon: MessageSquare, title: 'Quejas, Reclamaciones y Reseñas', desc: 'Registro de quejas, reclamaciones formales con sus plazos, control de reseñas y resumen del periodo.', ext: '.xlsx' },
      { key: 'scorecard-seleccion', icon: UserPlus, title: 'Scorecard de Selección y Entrevista', desc: 'Scorecard por competencias, comparativa de candidatos y banco de preguntas con la nota legal.', ext: '.xlsx' },
      { key: 'calendario-legal', icon: ScrollText, title: 'Calendario de Cumplimiento Legal', desc: 'Estado normativo, vencimientos, documentación obligatoria, topes de jornada, permisos y régimen disciplinario.', ext: '.xlsx' },
      { key: 'reuniones-plan-90', icon: ClipboardList, title: 'Reuniones, Acuerdos y Plan de 90 Días', desc: 'Calendario de reuniones, guion de la semanal, uno-a-uno, actas con acuerdos y plan de 90 días.', ext: '.xlsx' },
      { key: 'auditoria-servicio', icon: ClipboardCheck, title: 'Auditoría Interna de Servicio', desc: 'Unos 60 puntos de control en 6 áreas, con puntuación, resumen por área e histórico de auditorías.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonus (2)',
    templates: [
      { key: 'bonus-pdf', icon: GraduationCap, title: '12 Situaciones Resueltas (PDF)', desc: 'Situación con datos, qué NO hacer, protocolo, norma aplicable, herramienta usada y guion de la conversación.', ext: '.pdf' },
      { key: 'bonus-docx', icon: FileText, title: '12 Situaciones Resueltas (DOCX Editable)', desc: 'Mismo bonus en formato editable para trabajarlo con tu equipo.', ext: '.docx' },
    ],
  },
];

export default function ManualManagerDashboard() {
  const { token } = useAuth('manual-manager-restaurante-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', { headers: { Authorization: `Bearer ${token}` } })
      .then((r) => r.json())
      .then((data) => { if (data.files) setFiles(data.files); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Manual del Manager de Restaurante — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/manual-manager-restaurante" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Manual del Manager de Restaurante</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Manual del <span className="text-[#FFD700]">Manager de Restaurante</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="manual-manager-restaurante" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu manual completo + 7 herramientas Excel + el bonus de situaciones resueltas, listos para descargar.</p>
        </section>

        {SECTIONS.map((section) => (
          <section key={section.title} className="pb-12 px-4">
            <div className="max-w-5xl mx-auto">
              <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">{section.title}</p>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {section.templates.map((tpl) => {
                  const Icon = tpl.icon;
                  const url = files[tpl.key];
                  return (
                    <div key={tpl.key} className="rounded-xl p-5 bg-white/5 border border-white/10 hover:border-[#FFD700]/30 transition-all">
                      <div className="flex items-start gap-3 mb-3">
                        <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                        <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">{tpl.ext}</p></div>
                      </div>
                      <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>
                      {loading ? <Loader2 className="w-5 h-5 text-gray-500 animate-spin" /> : url ? (
                        <a href={url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10 transition-all">
                          <Download className="w-4 h-4" />Descargar
                        </a>
                      ) : <span className="text-gray-500 text-sm">Disponible pronto</span>}
                    </div>
                  );
                })}
              </div>
            </div>
          </section>
        ))}

        <ProductChangelog productId="manual-manager-restaurante" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">¿Ya tienes el manual? Completa tu toolkit</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-gestion-personal" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit Gestión de Personal — 14 EUR</a>
              <a href="/guia-food-cost-ingenieria-menu" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Guía Food Cost + Ingeniería de Menú — 55 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Manual del Manager de Restaurante · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
