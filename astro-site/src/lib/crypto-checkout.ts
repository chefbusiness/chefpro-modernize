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
 * Y una segunda variable, `CRYPTO_PRODUCTS_EXCLUDE` (CSV de productIds, vacía por
 * defecto), que se RESTA SIEMPRE — también con `all`. Existe porque hay exclusiones
 * permanentes que no dependen de en qué fase del despliegue estemos: `pro-prompts-ebook`
 * cuesta 9 € y está por debajo del mínimo por transacción de NOWPayments, así que su
 * botón no debe pintarse ni con el interruptor en `all`. Se apaga por CONFIGURACIÓN, no
 * quitándole el componente a su página: así el día que cambie el mínimo basta con vaciar
 * la variable. Ante el empate manda la exclusión.
 *
 * ⚠️ Scope en Netlify: las DOS variables van declaradas en scope **`functions` Y `builds`**.
 *   - `functions`, porque `crypto-checkout` vuelve a comprobar el allowlist en runtime
 *     (el botón del HTML no es una autorización: la puerta la guarda el backend).
 *   - `builds`, porque ESTE fichero se evalúa en el BUILD de Astro: el HTML sale ya con
 *     el botón o ya sin él. Consecuencia práctica: **cambiarlas no surte efecto hasta que
 *     se vuelve a desplegar el sitio** (redeploy en la nube, nunca build local — regla
 *     térmica del Mac).
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

function rawExcludelist(): string {
  const value = nodeEnv?.CRYPTO_PRODUCTS_EXCLUDE ?? import.meta.env.CRYPTO_PRODUCTS_EXCLUDE;
  return typeof value === 'string' ? value.trim() : '';
}

/** CSV → conjunto de ids normalizados. MISMA normalización que el `productId`
 *  (`trim().toLowerCase()`), y la misma que aplica `allowlist()` en
 *  `netlify/functions/crypto-checkout.ts`: si las dos capas normalizaran distinto, el
 *  botón podría salir en el HTML y el backend responder 403 al pulsarlo. */
function comoConjunto(csv: string): Set<string> {
  return new Set(
    csv
      .split(',')
      .map((entry) => entry.trim().toLowerCase())
      .filter(Boolean),
  );
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

  const target = String(productId ?? '').trim().toLowerCase();
  if (!target) return false;

  // La exclusión se resta SIEMPRE, y se comprueba ANTES que `all`: es la única forma de
  // que `CRYPTO_PRODUCTS=all` no encienda el eBook de 9 €, por debajo del mínimo de
  // NOWPayments. Ante el empate (un id en las dos listas), manda la exclusión.
  if (comoConjunto(rawExcludelist()).has(target)) return false;

  const allowlist = raw.toLowerCase();
  if (allowlist === 'all') return true;

  return comoConjunto(allowlist).has(target);
}
