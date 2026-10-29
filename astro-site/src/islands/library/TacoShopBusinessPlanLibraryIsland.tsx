/**
 * Island de /en/digital-products/taco-shop-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de la isla gemela EN de la familia Planes / PlanNegocioTaqueriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `taco-shop-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import TacoShopBusinessPlanDashboard from '../../../../src/pages/TacoShopBusinessPlanDashboard';

export default function TacoShopBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="taco-shop-business-plan-jwt" redirectTo="/en/digital-products/taco-shop-business-plan">
      <TacoShopBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
