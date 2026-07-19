/**
 * Island de /kit-tareas-sushi-bar-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasSushiBarDashboard from '../../../../src/pages/KitTareasSushiBarDashboard';

export default function KitTareasSushiBarLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-sushi-bar-jwt" redirectTo="/kit-tareas-sushi-bar">
      <KitTareasSushiBarDashboard />
    </ProtectedRoute>
  );
}
