/**
 * Island de /plan-negocio-panaderia-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioPanaderiaDashboard from '../../../../src/pages/PlanNegocioPanaderiaDashboard';

export default function PlanNegocioPanaderiaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-panaderia-jwt" redirectTo="/plan-negocio-panaderia">
      <PlanNegocioPanaderiaDashboard />
    </ProtectedRoute>
  );
}
