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
    jwt.verify(token, process.env.JWT_SECRET!);

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        ebook: process.env.PDF_EBOOK_URL || null,
        bonus1: process.env.PDF_BONUS1_URL || null,
        bonus23: process.env.PDF_BONUS23_URL || null,
      }),
    };
  } catch {
    return { statusCode: 403, headers, body: JSON.stringify({ error: 'Invalid token' }) };
  }
};
