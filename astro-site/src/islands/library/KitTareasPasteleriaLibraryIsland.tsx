/**
 * Island de /kit-tareas-pasteleria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasPasteleriaDashboard from '../../../../src/pages/KitTareasPasteleriaDashboard';

export default function KitTareasPasteleriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-pasteleria-jwt" redirectTo="/kit-tareas-pasteleria">
      <KitTareasPasteleriaDashboard />
    </ProtectedRoute>
  );
}
