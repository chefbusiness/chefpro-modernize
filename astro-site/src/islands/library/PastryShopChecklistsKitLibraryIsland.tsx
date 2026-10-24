/**
 * Island de /en/digital-products/pastry-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasPasteleriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `pastry-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PastryShopChecklistsKitDashboard from '../../../../src/pages/PastryShopChecklistsKitDashboard';

export default function PastryShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="pastry-shop-checklist-templates-jwt" redirectTo="/en/digital-products/pastry-shop-checklist-templates">
      <PastryShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
