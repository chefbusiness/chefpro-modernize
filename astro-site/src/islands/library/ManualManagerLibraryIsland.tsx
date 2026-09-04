/**
 * Island de /manual-manager-restaurante-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import ManualManagerDashboard from '../../../../src/pages/ManualManagerDashboard';

export default function ManualManagerLibraryIsland() {
  return (
    <ProtectedRoute storageKey="manual-manager-restaurante-jwt" redirectTo="/manual-manager-restaurante">
      <ManualManagerDashboard />
    </ProtectedRoute>
  );
}
