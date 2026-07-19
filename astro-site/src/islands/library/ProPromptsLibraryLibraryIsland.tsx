/**
 * Island de /pro-prompts-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA: en App.tsx esta ruta usa
 * <ProtectedRoute> SIN props (defaults 'pro-prompts-jwt' / '/pro-prompts-ebook'
 * de ProtectedRoute.tsx) — se replica igual, sin hardcodear los defaults.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import ProPromptsLibrary from '../../../../src/pages/ProPromptsLibrary';

export default function ProPromptsLibraryLibraryIsland() {
  return (
    <ProtectedRoute>
      <ProPromptsLibrary />
    </ProtectedRoute>
  );
}
