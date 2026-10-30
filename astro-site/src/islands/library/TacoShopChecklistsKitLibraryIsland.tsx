/**
 * Island de /en/digital-products/taco-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasTaqueriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `taco-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import TacoShopChecklistsKitDashboard from '../../../../src/pages/TacoShopChecklistsKitDashboard';

export default function TacoShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="taco-shop-checklist-templates-jwt" redirectTo="/en/digital-products/taco-shop-checklist-templates">
      <TacoShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
