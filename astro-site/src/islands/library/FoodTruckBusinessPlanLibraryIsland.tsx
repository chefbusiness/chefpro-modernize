/**
 * Island de /en/digital-products/food-truck-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantFinancialPlanKitLibraryIsland.tsx (EN) / PlanNegocioFoodTruckLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `food-truck-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import FoodTruckBusinessPlanDashboard from '../../../../src/pages/FoodTruckBusinessPlanDashboard';

export default function FoodTruckBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="food-truck-business-plan-jwt" redirectTo="/en/digital-products/food-truck-business-plan">
      <FoodTruckBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
