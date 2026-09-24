/**
 * Island de /en/digital-products/food-cost-templates/library (tienda EN, escrito a mano: el
 * generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de KitEscandallosLibraryIsland.tsx: ProtectedRoute + dashboard, con el storageKey y la
 * landing EN de la entrada `food-cost-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import FoodCostKitDashboard from '../../../../src/pages/FoodCostKitDashboard';

export default function FoodCostKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="food-cost-templates-jwt" redirectTo="/en/digital-products/food-cost-templates">
      <FoodCostKitDashboard />
    </ProtectedRoute>
  );
}
