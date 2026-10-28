/**
 * Island de /en/digital-products/coffee-cart-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioCafeteriaMovilEventosLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `coffee-cart-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import CoffeeCartBusinessPlanDashboard from '../../../../src/pages/CoffeeCartBusinessPlanDashboard';

export default function CoffeeCartBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="coffee-cart-business-plan-jwt" redirectTo="/en/digital-products/coffee-cart-business-plan">
      <CoffeeCartBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
