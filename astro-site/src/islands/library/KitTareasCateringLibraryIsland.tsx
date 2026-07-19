/**
 * Island de /kit-tareas-catering-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasCateringDashboard from '../../../../src/pages/KitTareasCateringDashboard';

export default function KitTareasCateringLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-catering-jwt" redirectTo="/kit-tareas-catering">
      <KitTareasCateringDashboard />
    </ProtectedRoute>
  );
}
