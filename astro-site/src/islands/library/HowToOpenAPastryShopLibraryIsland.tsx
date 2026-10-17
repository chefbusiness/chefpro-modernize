/**
 * Island de /en/digital-products/how-to-open-a-pastry-shop/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de FoodCostMenuEngineeringGuideLibraryIsland.tsx (EN) / GuiaPasteleriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `how-to-open-a-pastry-shop`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import HowToOpenAPastryShopDashboard from '../../../../src/pages/HowToOpenAPastryShopDashboard';

export default function HowToOpenAPastryShopLibraryIsland() {
  return (
    <ProtectedRoute storageKey="how-to-open-a-pastry-shop-jwt" redirectTo="/en/digital-products/how-to-open-a-pastry-shop">
      <HowToOpenAPastryShopDashboard />
    </ProtectedRoute>
  );
}
