import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaPasteleriaAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-pasteleria-obrador"
      storageKey="guia-pasteleria-obrador-jwt"
      dashboardPath="/guia-pasteleria-obrador-library"
      landingPath="/guia-pasteleria-obrador"
      productLabel="Cómo Montar una Pastelería"
    />
  );
}
