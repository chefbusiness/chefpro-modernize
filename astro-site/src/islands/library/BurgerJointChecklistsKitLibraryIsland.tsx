/**
 * Island de /en/digital-products/burger-joint-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasHamburgueseriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `burger-joint-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BurgerJointChecklistsKitDashboard from '../../../../src/pages/BurgerJointChecklistsKitDashboard';

export default function BurgerJointChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="burger-joint-checklist-templates-jwt" redirectTo="/en/digital-products/burger-joint-checklist-templates">
      <BurgerJointChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
