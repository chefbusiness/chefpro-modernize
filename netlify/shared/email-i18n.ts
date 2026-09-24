// ════════════════════════════════════════════════════════════════════════════
// Textos FIJOS del email de acceso, por idioma de la tienda (2026-09-23, tienda
// internacional fase 0.B). Los textos propios de cada producto (asunto, título,
// cuerpo, CTA) siguen en el PRODUCTS de cada function; aquí solo vive lo que
// envuelve a todos: el párrafo «Guarda este email…» y el aviso de las compras
// cripto.
//
// ⚠️ El bloque `es` es VERBATIM el que estaba en línea en verify-purchase.ts,
// resend-access.ts y nowpayments-ipn.ts (incluidos los saltos de línea y la
// indentación del aviso cripto, que se inserta tal cual en el HTML). Tocarlo
// cambia el email de los 50 productos españoles: se verificó byte a byte al
// extraerlo.
//
// El idioma NO viaja en el JWT: sale de `PRODUCTS[productId].lang` (ausente = 'es').
// ════════════════════════════════════════════════════════════════════════════

export type TiendaLang = 'es' | 'en';

export interface EmailI18n {
  /** Párrafo final: el enlace caduca, el acceso no. Texto plano, sin HTML. */
  guardaEmail: string;
  /** `extraHtml` de las compras cripto (lo inserta nowpayments-ipn antes de `guardaEmail`). */
  avisoCripto: string;
}

export const EMAIL_I18N: Record<TiendaLang, EmailI18n> = {
  es: {
    guardaEmail:
      'Guarda este email. El enlace es válido 12 meses; cuando caduque, recupéralo gratis en un clic desde la página del producto («¿Ya compraste…?»): tu acceso no caduca.',
    avisoCripto: `
          <p style="color: #666; font-size: 14px; line-height: 1.6;">
            Compra pagada en criptomoneda. Al solicitar el acceso inmediato al contenido digital renunciaste al derecho de desistimiento de 14 días, tal y como marcaste al pagar. Si necesitas ayuda, escríbenos a <a href="mailto:info@aichef.pro" style="color: #FFD700;">info@aichef.pro</a> con tu número de pedido.
          </p>`,
  },
  en: {
    guardaEmail:
      'Keep this email. The link is valid for 12 months; when it expires, get a new one for free in one click from the product page ("Already purchased?"): your access never expires.',
    avisoCripto: `
          <p style="color: #666; font-size: 14px; line-height: 1.6;">
            Paid in cryptocurrency. By requesting immediate access to the digital content, you waived the 14-day cancellation right where it applies (EU/UK), as you confirmed at checkout. If you need help, email us at <a href="mailto:info@aichef.pro" style="color: #FFD700;">info@aichef.pro</a> with your order number.
          </p>`,
  },
};

/** Normaliza el `lang` de un producto: cualquier cosa que no sea 'en' es 'es'
 *  (así un producto sin campo, o con un valor raro, sigue saliendo en español). */
export function tiendaLang(lang: unknown): TiendaLang {
  return lang === 'en' ? 'en' : 'es';
}

export function emailI18n(lang: unknown): EmailI18n {
  return EMAIL_I18N[tiendaLang(lang)];
}
