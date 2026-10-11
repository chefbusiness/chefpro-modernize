/**
 * Island de /en/digital-products/catering-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantBusinessPlanLibraryIsland.tsx (EN) / PlanCateringTematicoEventosLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `catering-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import CateringBusinessPlanDashboard from '../../../../src/pages/CateringBusinessPlanDashboard';

export default function CateringBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="catering-business-plan-jwt" redirectTo="/en/digital-products/catering-business-plan">
      <CateringBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
