import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import { Download, Loader2, FileSpreadsheet, ArrowLeft, Package, ChevronDown } from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const KITS = [
  { id: 'kit-tareas', name: 'Restaurante Casual', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Partidas de Cocina' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-cafeteria', name: 'Cafetería / Brunch', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'barista', title: 'Tareas del Barista' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-pizzeria', name: 'Pizzería', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'horno', title: 'Tareas del Horno' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-hamburgueseria', name: 'Hamburguesería', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'plancha-grill', title: 'Plancha y Grill' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-dark-kitchen', name: 'Dark Kitchen', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Estaciones de Producción' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-pasteleria', name: 'Pastelería / Obrador', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Partidas de Producción' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-bar', name: 'Bar / Cocktails', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Partidas de Barra' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Festivos' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-catering', name: 'Catering / Eventos', templates: [
    { key: 'apertura-cierre', title: 'Producción Off-Site' },
    { key: 'partidas', title: 'Transporte y Logística' },
    { key: 'manager', title: 'Tareas del Event Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Montaje y Desmontaje' },
    { key: 'eventos', title: 'Tipos de Evento' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Pre-Evento' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-hotel', name: 'Hotel Completo', templates: [
    { key: 'fb-buffet-desayuno', title: 'Buffet Desayuno' },
    { key: 'fb-buffet-comida-cena', title: 'Buffet Almuerzo/Cena' },
    { key: 'fb-restaurante-carte', title: 'Restaurante À la Carte' },
    { key: 'fb-outlets', title: 'Pool/Lobby/Snack Bar' },
    { key: 'fb-room-service-minibar', title: 'Room Service + Minibar' },
    { key: 'fb-banquetes-eventos', title: 'Banquetes y Eventos' },
    { key: 'recepcion-turnos', title: 'Recepción — 3 Turnos' },
    { key: 'guest-services', title: 'Guest Services' },
    { key: 'housekeeping', title: 'Housekeeping' },
    { key: 'areas-publicas', title: 'Áreas Públicas' },
    { key: 'piscina', title: 'Piscina' },
    { key: 'terraza', title: 'Terraza' },
    { key: 'mantenimiento', title: 'Mantenimiento' },
    { key: 'administracion', title: 'Administración' },
    { key: 'spa-wellness', title: 'Spa / Wellness' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Hotel' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing F&B' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-heladeria', name: 'Heladería Artesanal', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Partidas de Producción' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Temporada' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Diario' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-chocolateria', name: 'Chocolatería / Bombonería', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'partidas', title: 'Partidas de Producción' },
    { key: 'manager', title: 'Tareas del Manager' },
    { key: 'perfiles', title: 'Tareas por Perfil' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'eventos', title: 'Eventos y Temporada' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Diario' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-restaurante-creativo', name: 'Restaurante Creativo / De Autor', templates: [
    { key: 'apertura-cierre', title: 'Apertura y Cierre Operativo' },
    { key: 'mise-en-place', title: 'Mise en Place Degustación' },
    { key: 'id-menu', title: 'I+D y Desarrollo de Menú' },
    { key: 'brigada', title: 'Brigada Creativa' },
    { key: 'periodicas', title: 'Semanales y Mensuales' },
    { key: 'sumiller', title: 'Sumiller y Maridajes' },
    { key: 'eventos', title: "Chef's Table y Eventos" },
    { key: 'fotografia', title: 'Fotografía y Storytelling' },
    { key: 'personalizable', title: 'Plantilla Personalizable' },
    { key: 'apertura-negocio', title: 'Apertura/Cierre del Negocio' },
    { key: 'apertura-caja', title: 'Apertura/Cierre de Caja' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Diario' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Anual' },
  ]},
  { id: 'kit-tareas-chef-privado', name: 'Chef Privado / Personal Chef', templates: [
    { key: 'ficha-cliente', title: 'Ficha Cliente y Consulta' },
    { key: 'menu-compras', title: 'Planificación Menú y Compras' },
    { key: 'equipo-transporte', title: 'Equipo y Transporte' },
    { key: 'appcc', title: 'Seguridad Alimentaria' },
    { key: 'servicio', title: 'Checklist Servicio' },
    { key: 'fidelizacion', title: 'Seguimiento y Fidelización' },
    { key: 'admin', title: 'Administración Autónomo' },
    { key: 'bonus-briefing', title: 'BONUS: Briefing Pre-Servicio' },
    { key: 'bonus-calendario', title: 'BONUS: Calendario Demanda' },
  ]},
];

export default function MegaPackTareasDashboard() {
  const { token } = useAuth('mega-pack-tareas-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);
  const [openKits, setOpenKits] = useState<Set<string>>(new Set(['kit-tareas']));

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', { headers: { Authorization: `Bearer ${token}` } })
      .then((r) => r.json())
      .then((data) => { if (data.files) setFiles(data.files); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  const toggleKit = (id: string) => {
    setOpenKits(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id); else next.add(id);
      return next;
    });
  };

  return (
    <>
      <Helmet>
        <title>Mega Pack Tareas Recurrentes — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/mega-pack-tareas" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Mega Pack</a>
            <div className="flex items-center gap-2"><FileSpreadsheet className="w-5 h-5 text-emerald-400" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-emerald-400 text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Mega Pack <span className="text-emerald-400">Tareas Recurrentes</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tus 13 kits con {KITS.reduce((s, k) => s + k.templates.length, 0)} plantillas listos para descargar.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-4xl mx-auto space-y-3">
            {KITS.map((kit) => {
              const isOpen = openKits.has(kit.id);
              return (
                <div key={kit.id} className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
                  <button onClick={() => toggleKit(kit.id)} className="w-full flex items-center justify-between p-4 text-left hover:bg-white/5 transition-colors">
                    <div className="flex items-center gap-3">
                      <Package className="w-5 h-5 text-emerald-400" />
                      <span className="text-white font-semibold">{kit.name}</span>
                      <span className="text-gray-500 text-xs">{kit.templates.length} plantillas</span>
                    </div>
                    <ChevronDown className={`w-5 h-5 text-emerald-400 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
                  </button>
                  {isOpen && (
                    <div className="border-t border-white/5 p-4 grid sm:grid-cols-2 gap-2">
                      {kit.templates.map((tpl) => {
                        const fileKey = `${kit.id}__${tpl.key}`;
                        const url = files[fileKey];
                        return (
                          <div key={tpl.key} className="flex items-center justify-between p-2 rounded-lg hover:bg-white/5">
                            <div className="flex items-center gap-2">
                              <FileSpreadsheet className="w-4 h-4 text-emerald-400/60" />
                              <span className="text-gray-300 text-sm">{tpl.title}</span>
                            </div>
                            {loading ? <Loader2 className="w-4 h-4 text-gray-500 animate-spin" /> : url ? (
                              <a href={url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-3 py-1 border border-emerald-500/50 text-emerald-400 rounded-md text-xs font-bold hover:bg-emerald-500/10">
                                <Download className="w-3 h-3" />xlsx
                              </a>
                            ) : <span className="text-gray-600 text-xs">—</span>}
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
          <div className="max-w-4xl mx-auto mt-8 bg-white/5 border border-white/10 rounded-xl p-6 text-center">
            <p className="text-white font-semibold mb-1">Compatibles con Excel, Google Sheets, LibreOffice, Numbers + Imprimible A4</p>
            <p className="text-gray-400 text-sm">Descarga los archivos .xlsx y ábrelos con tu programa favorito.</p>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Mega Pack Tareas Recurrentes · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
