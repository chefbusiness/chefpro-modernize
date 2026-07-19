/**
 * Island de /plan-negocio-bar-restaurante-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioBarRestauranteDashboard from '../../../../src/pages/PlanNegocioBarRestauranteDashboard';

export default function PlanNegocioBarRestauranteLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-bar-restaurante-jwt" redirectTo="/plan-negocio-bar-restaurante">
      <PlanNegocioBarRestauranteDashboard />
    </ProtectedRoute>
  );
}
