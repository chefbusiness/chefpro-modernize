/**
 * Island de /guia-panaderia-obrador-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaPanaderiaObradorDashboard from '../../../../src/pages/GuiaPanaderiaObradorDashboard';

export default function GuiaPanaderiaObradorLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-panaderia-obrador-jwt" redirectTo="/guia-panaderia-obrador">
      <GuiaPanaderiaObradorDashboard />
    </ProtectedRoute>
  );
}
