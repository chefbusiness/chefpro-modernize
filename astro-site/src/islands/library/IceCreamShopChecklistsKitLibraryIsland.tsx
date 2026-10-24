/**
 * Island de /en/digital-products/ice-cream-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasHeladeriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `ice-cream-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import IceCreamShopChecklistsKitDashboard from '../../../../src/pages/IceCreamShopChecklistsKitDashboard';

export default function IceCreamShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="ice-cream-shop-checklist-templates-jwt" redirectTo="/en/digital-products/ice-cream-shop-checklist-templates">
      <IceCreamShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
