/**
 * Island de /en/digital-products/burger-restaurant-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de la isla gemela EN de la familia Planes / PlanNegocioHamburgueseriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `burger-restaurant-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BurgerRestaurantBusinessPlanDashboard from '../../../../src/pages/BurgerRestaurantBusinessPlanDashboard';

export default function BurgerRestaurantBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="burger-restaurant-business-plan-jwt" redirectTo="/en/digital-products/burger-restaurant-business-plan">
      <BurgerRestaurantBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
