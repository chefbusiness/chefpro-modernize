/**
 * Interruptor de la segunda puerta de pago: «Pagar con cripto» (NOWPayments).
 *
 * Piloto (2026-09-05, PAGOS_CRYPTO_NOWPAYMENTS.md): Stripe sigue siendo el método
 * PRINCIPAL —botón dorado— y la cripto es el secundario. Qué productos la ofrecen lo
 * decide una sola variable de entorno, `CRYPTO_PRODUCTS`, para poder encender el piloto
 * en un producto, replicarlo a los 46 (`all`) o apagarlo entero sin tocar una línea:
 *
 *   - vacía o ausente → apagado en TODO el sitio (interruptor de emergencia)
 *   - `all`           → encendido en todos los productos
 *   - CSV de productIds (`kit-tareas-cafeteria,kit-escandallos`) → solo esos
 *
 * ⚠️ Scope en Netlify: la variable va declarada en scope **`functions` Y `builds`**.
 *   - `functions`, porque `crypto-checkout` vuelve a comprobar el allowlist en runtime
 *     (el botón del HTML no es una autorización: la puerta la guarda el backend).
 *   - `builds`, porque ESTE fichero se evalúa en el BUILD de Astro: el HTML sale ya con
 *     el botón o ya sin él. Consecuencia práctica: **cambiar `CRYPTO_PRODUCTS` no surte
 *     efecto hasta que se vuelve a desplegar el sitio** (redeploy en la nube, nunca build
 *     local — regla térmica del Mac).
 *
 * ⚠️ Acceso LITERAL a la variable, nunca `import.meta.env[clave]`: el acceso dinámico no
 * lo puede sustituir Vite en build y devuelve `undefined` en producción (misma trampa
 * documentada para `VITE_STRIPE_PAYMENT_LINK_*` en los wrappers de landing). Se lee
 * primero de `process.env` —que es donde Netlify la pone durante el build de Astro— y se
 * cae a `import.meta.env` por si algún día se declara con prefijo público o en un `.env`.
 */

/** Monedas que se anuncian en el botón. Texto único para no divergir entre plantillas. */
export const CRYPTO_COINS_LABEL = 'USDT · USDC · BTC · ETH y más';

/** `process` sin depender de @types/node (astro-site no lo tiene instalado). El acceso a
 *  la propiedad sigue siendo literal: `.CRYPTO_PRODUCTS`. */
const nodeEnv = (globalThis as { process?: { env?: Record<string, string | undefined> } })
  .process?.env;

function rawAllowlist(): string {
  const value = nodeEnv?.CRYPTO_PRODUCTS ?? import.meta.env.CRYPTO_PRODUCTS;
  return typeof value === 'string' ? value.trim() : '';
}

/**
 * ¿Este producto ofrece el pago en cripto?
 *
 * @param productId identificador del producto (= slug de su landing en los 46 productos;
 *                  verificado contra `zona-app.ts`: `landingPath === '/' + productId`).
 */
export function cryptoEnabledFor(productId: string): boolean {
  const raw = rawAllowlist();
  if (!raw) return false; // vacía o ausente = apagado

  const allowlist = raw.toLowerCase();
  if (allowlist === 'all') return true;

  const target = String(productId ?? '').trim().toLowerCase();
  if (!target) return false;

  return allowlist
    .split(',')
    .map((entry) => entry.trim())
    .filter(Boolean)
    .includes(target);
}
