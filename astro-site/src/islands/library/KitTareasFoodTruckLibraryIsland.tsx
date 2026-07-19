/**
 * Island de /kit-tareas-food-truck-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasFoodTruckDashboard from '../../../../src/pages/KitTareasFoodTruckDashboard';

export default function KitTareasFoodTruckLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-food-truck-jwt" redirectTo="/kit-tareas-food-truck">
      <KitTareasFoodTruckDashboard />
    </ProtectedRoute>
  );
}
