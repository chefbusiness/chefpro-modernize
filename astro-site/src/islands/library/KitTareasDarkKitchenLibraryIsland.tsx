/**
 * Island de /kit-tareas-dark-kitchen-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasDarkKitchenDashboard from '../../../../src/pages/KitTareasDarkKitchenDashboard';

export default function KitTareasDarkKitchenLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-dark-kitchen-jwt" redirectTo="/kit-tareas-dark-kitchen">
      <KitTareasDarkKitchenDashboard />
    </ProtectedRoute>
  );
}
