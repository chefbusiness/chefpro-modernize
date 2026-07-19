/**
 * Island de /plan-negocio-cafeteria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioCafeteriaDashboard from '../../../../src/pages/PlanNegocioCafeteriaDashboard';

export default function PlanNegocioCafeteriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-cafeteria-jwt" redirectTo="/plan-negocio-cafeteria">
      <PlanNegocioCafeteriaDashboard />
    </ProtectedRoute>
  );
}
