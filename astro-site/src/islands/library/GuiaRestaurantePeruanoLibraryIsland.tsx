/**
 * Island de /guia-restaurante-peruano-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaRestaurantePeruanoDashboard from '../../../../src/pages/GuiaRestaurantePeruanoDashboard';

export default function GuiaRestaurantePeruanoLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-restaurante-peruano-jwt" redirectTo="/guia-restaurante-peruano">
      <GuiaRestaurantePeruanoDashboard />
    </ProtectedRoute>
  );
}
