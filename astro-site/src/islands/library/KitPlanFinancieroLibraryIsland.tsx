/**
 * Island de /kit-plan-financiero-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitPlanFinancieroDashboard from '../../../../src/pages/KitPlanFinancieroDashboard';

export default function KitPlanFinancieroLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-plan-financiero-jwt" redirectTo="/kit-plan-financiero">
      <KitPlanFinancieroDashboard />
    </ProtectedRoute>
  );
}
