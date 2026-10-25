/**
 * Island de /en/digital-products/pizza-shop-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioPizzeriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `pizza-shop-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PizzaShopBusinessPlanDashboard from '../../../../src/pages/PizzaShopBusinessPlanDashboard';

export default function PizzaShopBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="pizza-shop-business-plan-jwt" redirectTo="/en/digital-products/pizza-shop-business-plan">
      <PizzaShopBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
