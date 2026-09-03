/**
 * Island de /guia-food-cost-ingenieria-menu-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaFoodCostDashboard from '../../../../src/pages/GuiaFoodCostDashboard';

export default function GuiaFoodCostLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-food-cost-ingenieria-menu-jwt" redirectTo="/guia-food-cost-ingenieria-menu">
      <GuiaFoodCostDashboard />
    </ProtectedRoute>
  );
}
