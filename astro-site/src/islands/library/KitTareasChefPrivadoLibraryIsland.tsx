/**
 * Island de /kit-tareas-chef-privado-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasChefPrivadoDashboard from '../../../../src/pages/KitTareasChefPrivadoDashboard';

export default function KitTareasChefPrivadoLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-chef-privado-jwt" redirectTo="/kit-tareas-chef-privado">
      <KitTareasChefPrivadoDashboard />
    </ProtectedRoute>
  );
}
