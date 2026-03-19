import type { Handler } from '@netlify/functions';

export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  if (event.httpMethod !== 'GET') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  // Verify JWT from Authorization header
  const authHeader = event.headers.authorization || event.headers.Authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return { statusCode: 401, headers, body: JSON.stringify({ error: 'Unauthorized' }) };
  }

  try {
    const jwt = (await import('jsonwebtoken')).default;
    const token = authHeader.split(' ')[1];
    const payload = jwt.verify(token, process.env.JWT_SECRET!) as { product?: string };

    const product = payload.product || 'pro-prompts-ebook';

    // ── Pro Prompts eBook downloads ───────────────────────────
    if (product === 'pro-prompts-ebook') {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product: 'pro-prompts-ebook',
          ebook: process.env.PDF_EBOOK_URL || null,
          bonus1: process.env.PDF_BONUS1_URL || null,
          bonus23: process.env.PDF_BONUS23_URL || null,
        }),
      };
    }

    // ── Kit de Escandallos Pro downloads ──────────────────────
    if (product === 'kit-escandallos') {
      // Parse JSON env var: {"estandar":"url","degustacion":"url",...}
      let kitFiles: Record<string, string> = {};
      try {
        kitFiles = JSON.parse(process.env.KIT_ESCANDALLOS_URLS || '{}');
      } catch {
        kitFiles = {};
      }

      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product: 'kit-escandallos',
          files: kitFiles,
        }),
      };
    }

    // ── Pack de Plantillas APPCC downloads ────────────────────
    if (product === 'pack-appcc') {
      let appccFiles: Record<string, string> = {};
      try {
        appccFiles = JSON.parse(process.env.PACK_APPCC_URLS || '{}');
      } catch {
        appccFiles = {};
      }

      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product: 'pack-appcc',
          files: appccFiles,
        }),
      };
    }

    // ── Kit de Tareas Recurrentes downloads ────────────────────
    if (product === 'kit-tareas') {
      let tareasFiles: Record<string, string> = {};
      try {
        tareasFiles = JSON.parse(process.env.KIT_TAREAS_URLS || '{}');
      } catch {
        tareasFiles = {};
      }

      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product: 'kit-tareas',
          files: tareasFiles,
        }),
      };
    }

    // Unknown product — return empty
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ product, error: 'Unknown product' }),
    };
  } catch {
    return { statusCode: 403, headers, body: JSON.stringify({ error: 'Invalid token' }) };
  }
};
