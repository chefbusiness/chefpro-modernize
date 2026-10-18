/**
 * Island de /en/digital-products/coffee-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasCafeteriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `coffee-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import CoffeeShopChecklistsKitDashboard from '../../../../src/pages/CoffeeShopChecklistsKitDashboard';

export default function CoffeeShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="coffee-shop-checklist-templates-jwt" redirectTo="/en/digital-products/coffee-shop-checklist-templates">
      <CoffeeShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
