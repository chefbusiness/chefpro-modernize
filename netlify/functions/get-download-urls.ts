import type { Handler } from '@netlify/functions';
import {
  PRODUCTS_CONFIG,
  DEFAULT_PRODUCT_ID,
  SPECIAL_DOWNLOAD_PRODUCTS,
} from '../../src/data/productos-digitales-config';

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

  const authHeader = event.headers.authorization || event.headers.Authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return { statusCode: 401, headers, body: JSON.stringify({ error: 'Unauthorized' }) };
  }

  try {
    const jwt = (await import('jsonwebtoken')).default;
    const token = authHeader.split(' ')[1];
    const payload = jwt.verify(token, process.env.JWT_SECRET!) as { product?: string };

    const product = payload.product || DEFAULT_PRODUCT_ID;

    // ── Pro Prompts eBook (special: PDF downloads from env vars) ──
    if (SPECIAL_DOWNLOAD_PRODUCTS.has(product)) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product,
          ebook: process.env.PDF_EBOOK_URL || null,
          bonus1: process.env.PDF_BONUS1_URL || null,
          bonus23: process.env.PDF_BONUS23_URL || null,
        }),
      };
    }

    // ── All other products: read file map from config ──
    const config = PRODUCTS_CONFIG[product];
    if (config && Object.keys(config.files).length > 0) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ product, files: config.files }),
      };
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ product, error: 'Unknown product' }),
    };
  } catch {
    return { statusCode: 403, headers, body: JSON.stringify({ error: 'Invalid token' }) };
  }
};
