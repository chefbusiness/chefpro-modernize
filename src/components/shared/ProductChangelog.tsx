import { useState } from 'react';
import { PRODUCT_CHANGELOGS, formatFechaLarga, formatFechaCorta } from '@/data/productos-changelog';

// Versionado visible en los dashboards post-pago (patrón portado de ChefBusiness el
// 2026-08-18, adaptado a la paleta de AI Chef Pro). Si el producto no tiene entrada
// en PRODUCT_CHANGELOGS, ambos componentes renderizan null: se pueden montar en
// cualquier dashboard sin romper nada.

/** Badge compacto para la cabecera: "Versión 2.0 · Actualizado 18/08/2026". */
export function ProductVersionBadge({ productId }: { productId: string }) {
  const data = PRODUCT_CHANGELOGS[productId];
  if (!data) return null;
  return (
    <span className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-xs font-semibold tracking-wide">
      Versión {data.version}
      <span className="text-gray-400 font-normal">Actualizado {formatFechaCorta(data.updated)}</span>
    </span>
  );
}

/** Bloque "Novedades y mejoras" para el final del dashboard. */
export default function ProductChangelog({ productId }: { productId: string }) {
  const data = PRODUCT_CHANGELOGS[productId];
  const [open, setOpen] = useState(false);
  if (!data) return null;
  const [latest, ...older] = data.entries;

  return (
    <section className="px-4 pb-12">
      <div className="max-w-3xl mx-auto bg-white/5 border border-white/10 rounded-xl p-6 md:p-7">
        <div className="flex flex-wrap items-baseline justify-between gap-2 mb-1">
          <p className="text-[#FFD700] text-xs font-bold uppercase tracking-wider">Novedades y mejoras</p>
          <span className="text-gray-500 text-xs">
            Versión {data.version} · {formatFechaLarga(data.updated)}
          </span>
        </div>
        <p className="text-gray-400 text-sm leading-relaxed mb-5">
          Tu acceso es de por vida: cada mejora que hacemos en este producto aparece aquí y la tienes
          disponible sin coste. Vuelve a descargar los archivos para tener la última versión.
        </p>

        <div className={`border-l-2 border-[#FFD700] pl-4 ${older.length ? 'mb-4' : ''}`}>
          <div className="flex flex-wrap items-baseline gap-2 mb-2">
            <span className="text-[#FFD700] text-sm font-bold">v{latest.version}</span>
            <span className="text-white text-sm font-semibold">{latest.title}</span>
            <span className="text-gray-500 text-xs">{formatFechaLarga(latest.date)}</span>
          </div>
          <ul className="list-disc pl-5 space-y-1 text-gray-400 text-sm leading-relaxed">
            {latest.changes.map((ch, i) => (
              <li key={i}>{ch}</li>
            ))}
          </ul>
        </div>

        {older.length > 0 && (
          <>
            {open &&
              older.map((entry) => (
                <div key={entry.version + entry.date} className="border-l-2 border-white/15 pl-4 mb-4">
                  <div className="flex flex-wrap items-baseline gap-2 mb-2">
                    <span className="text-[#FFD700]/70 text-sm font-bold">v{entry.version}</span>
                    <span className="text-gray-200 text-sm font-semibold">{entry.title}</span>
                    <span className="text-gray-500 text-xs">{formatFechaLarga(entry.date)}</span>
                  </div>
                  <ul className="list-disc pl-5 space-y-1 text-gray-500 text-sm leading-relaxed">
                    {entry.changes.map((ch, i) => (
                      <li key={i}>{ch}</li>
                    ))}
                  </ul>
                </div>
              ))}
            <button
              type="button"
              onClick={() => setOpen(!open)}
              className="text-[#FFD700] text-xs font-semibold hover:underline"
            >
              {open
                ? 'Ocultar historial'
                : `Ver historial completo (${older.length} ${older.length > 1 ? 'versiones anteriores' : 'versión anterior'})`}
            </button>
          </>
        )}
      </div>
    </section>
  );
}
