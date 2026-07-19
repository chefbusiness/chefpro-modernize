/**
 * Island de /guia-dark-kitchen-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaDarkKitchenDashboard from '../../../../src/pages/GuiaDarkKitchenDashboard';

export default function GuiaDarkKitchenLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-dark-kitchen-jwt" redirectTo="/guia-dark-kitchen">
      <GuiaDarkKitchenDashboard />
    </ProtectedRoute>
  );
}
