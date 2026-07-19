/**
 * Island de /guia-restaurante-japones-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaRestauranteJaponesDashboard from '../../../../src/pages/GuiaRestauranteJaponesDashboard';

export default function GuiaRestauranteJaponesLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-restaurante-japones-jwt" redirectTo="/guia-restaurante-japones">
      <GuiaRestauranteJaponesDashboard />
    </ProtectedRoute>
  );
}
