/**
 * Island de /en/digital-products/ai-prompts-for-restaurants/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Gemelo de ProPromptsLibraryLibraryIsland.tsx (ES), pero con el storageKey y la landing EN de la
 * entrada `ai-prompts-for-restaurants` de astro-site/src/lib/zona-app.ts EXPLÍCITOS (el ES usa los
 * defaults de ProtectedRoute, que son los del eBook español).
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import ProPromptsLibraryEn from '../../../../src/pages/ProPromptsLibraryEn';

export default function AiPromptsForRestaurantsLibraryIsland() {
  return (
    <ProtectedRoute storageKey="ai-prompts-for-restaurants-jwt" redirectTo="/en/digital-products/ai-prompts-for-restaurants">
      <ProPromptsLibraryEn />
    </ProtectedRoute>
  );
}
