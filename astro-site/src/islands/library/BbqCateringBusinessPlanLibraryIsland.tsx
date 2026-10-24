/**
 * Island de /en/digital-products/bbq-catering-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioParrilleroAsadorEventosLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `bbq-catering-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BbqCateringBusinessPlanDashboard from '../../../../src/pages/BbqCateringBusinessPlanDashboard';

export default function BbqCateringBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="bbq-catering-business-plan-jwt" redirectTo="/en/digital-products/bbq-catering-business-plan">
      <BbqCateringBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
