/**
 * Island de /kit-escandallos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitEscandallosDashboard from '../../../../src/pages/KitEscandallosDashboard';

export default function KitEscandallosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-escandallos-jwt" redirectTo="/kit-escandallos">
      <KitEscandallosDashboard />
    </ProtectedRoute>
  );
}
