/**
 * Island de /kit-tareas-cafeteria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasCafeteriaDashboard from '../../../../src/pages/KitTareasCafeteriaDashboard';

export default function KitTareasCafeteriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-cafeteria-jwt" redirectTo="/kit-tareas-cafeteria">
      <KitTareasCafeteriaDashboard />
    </ProtectedRoute>
  );
}
