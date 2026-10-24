/**
 * Island de /en/digital-products/chocolate-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasChocolateriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `chocolate-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import ChocolateShopChecklistsKitDashboard from '../../../../src/pages/ChocolateShopChecklistsKitDashboard';

export default function ChocolateShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="chocolate-shop-checklist-templates-jwt" redirectTo="/en/digital-products/chocolate-shop-checklist-templates">
      <ChocolateShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
