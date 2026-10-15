/**
 * Island de /en/digital-products/food-cost-menu-engineering-guide/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / GuiaFoodCostLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `food-cost-menu-engineering-guide`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import FoodCostMenuEngineeringGuideDashboard from '../../../../src/pages/FoodCostMenuEngineeringGuideDashboard';

export default function FoodCostMenuEngineeringGuideLibraryIsland() {
  return (
    <ProtectedRoute storageKey="food-cost-menu-engineering-guide-jwt" redirectTo="/en/digital-products/food-cost-menu-engineering-guide">
      <FoodCostMenuEngineeringGuideDashboard />
    </ProtectedRoute>
  );
}
