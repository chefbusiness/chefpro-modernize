/**
 * Island de /pack-appcc-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PackAppccDashboard from '../../../../src/pages/PackAppccDashboard';

export default function PackAppccLibraryIsland() {
  return (
    <ProtectedRoute storageKey="pack-appcc-jwt" redirectTo="/pack-appcc">
      <PackAppccDashboard />
    </ProtectedRoute>
  );
}
