/**
 * Island de /guia-restaurante-mexicano-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaRestauranteMexicanoDashboard from '../../../../src/pages/GuiaRestauranteMexicanoDashboard';

export default function GuiaRestauranteMexicanoLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-restaurante-mexicano-jwt" redirectTo="/guia-restaurante-mexicano">
      <GuiaRestauranteMexicanoDashboard />
    </ProtectedRoute>
  );
}
