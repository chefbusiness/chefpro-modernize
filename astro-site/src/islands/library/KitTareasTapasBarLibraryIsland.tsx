/**
 * Island de /kit-tareas-tapas-bar-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasTapasBarDashboard from '../../../../src/pages/KitTareasTapasBarDashboard';

export default function KitTareasTapasBarLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-tapas-bar-jwt" redirectTo="/kit-tareas-tapas-bar">
      <KitTareasTapasBarDashboard />
    </ProtectedRoute>
  );
}
