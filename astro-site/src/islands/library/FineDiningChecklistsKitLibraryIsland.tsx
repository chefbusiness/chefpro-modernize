/**
 * Island de /en/digital-products/fine-dining-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasRestauranteCreativoLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `fine-dining-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import FineDiningChecklistsKitDashboard from '../../../../src/pages/FineDiningChecklistsKitDashboard';

export default function FineDiningChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="fine-dining-checklist-templates-jwt" redirectTo="/en/digital-products/fine-dining-checklist-templates">
      <FineDiningChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
