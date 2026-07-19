/**
 * Island de /kit-tareas-restaurante-creativo-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasRestauranteCreativoDashboard from '../../../../src/pages/KitTareasRestauranteCreativoDashboard';

export default function KitTareasRestauranteCreativoLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-restaurante-creativo-jwt" redirectTo="/kit-tareas-restaurante-creativo">
      <KitTareasRestauranteCreativoDashboard />
    </ProtectedRoute>
  );
}
