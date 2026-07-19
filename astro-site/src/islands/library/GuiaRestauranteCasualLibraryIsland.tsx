/**
 * Island de /guia-restaurante-casual-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaRestauranteCasualDashboard from '../../../../src/pages/GuiaRestauranteCasualDashboard';

export default function GuiaRestauranteCasualLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-restaurante-casual-jwt" redirectTo="/guia-restaurante-casual">
      <GuiaRestauranteCasualDashboard />
    </ProtectedRoute>
  );
}
