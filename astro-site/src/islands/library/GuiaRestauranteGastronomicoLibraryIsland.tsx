/**
 * Island de /guia-restaurante-gastronomico-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaRestauranteGastronomicoDashboard from '../../../../src/pages/GuiaRestauranteGastronomicoDashboard';

export default function GuiaRestauranteGastronomicoLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-restaurante-gastronomico-jwt" redirectTo="/guia-restaurante-gastronomico">
      <GuiaRestauranteGastronomicoDashboard />
    </ProtectedRoute>
  );
}
