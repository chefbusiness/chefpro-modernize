/**
 * Island de /kit-tareas-pizzeria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasPizzeriaDashboard from '../../../../src/pages/KitTareasPizzeriaDashboard';

export default function KitTareasPizzeriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-pizzeria-jwt" redirectTo="/kit-tareas-pizzeria">
      <KitTareasPizzeriaDashboard />
    </ProtectedRoute>
  );
}
