/**
 * Island de /en/digital-products/food-truck-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasFoodTruckLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `food-truck-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import FoodTruckChecklistsKitDashboard from '../../../../src/pages/FoodTruckChecklistsKitDashboard';

export default function FoodTruckChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="food-truck-checklist-templates-jwt" redirectTo="/en/digital-products/food-truck-checklist-templates">
      <FoodTruckChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
