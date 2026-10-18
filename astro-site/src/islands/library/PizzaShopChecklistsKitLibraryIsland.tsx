/**
 * Island de /en/digital-products/pizza-shop-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasPizzeriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `pizza-shop-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PizzaShopChecklistsKitDashboard from '../../../../src/pages/PizzaShopChecklistsKitDashboard';

export default function PizzaShopChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="pizza-shop-checklist-templates-jwt" redirectTo="/en/digital-products/pizza-shop-checklist-templates">
      <PizzaShopChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
