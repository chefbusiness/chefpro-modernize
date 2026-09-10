/**
 * Island de /guia-pasteleria-obrador-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaPasteleriaDashboard from '../../../../src/pages/GuiaPasteleriaDashboard';

export default function GuiaPasteleriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-pasteleria-obrador-jwt" redirectTo="/guia-pasteleria-obrador">
      <GuiaPasteleriaDashboard />
    </ProtectedRoute>
  );
}
