#!/usr/bin/env node
// CLI fallback to mint a magic-link JWT locally without hitting the backend.
// Requires JWT_SECRET in env (or in .env). Useful when Netlify is down or
// when the admin UI is not reachable.
//
// Usage:
//   node scripts/generate-access-link.mjs <email> <product-id>
//
// Example:
//   node scripts/generate-access-link.mjs alfonso.a74@gmail.com pack-appcc

import jwt from 'jsonwebtoken';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const PRODUCTS = {
  'pro-prompts-ebook': '/pro-prompts-library-access',
  'kit-escandallos': '/kit-escandallos-access',
  'pack-appcc': '/pack-appcc-access',
  'kit-tareas': '/kit-tareas-access',
  'kit-tareas-cafeteria': '/kit-tareas-cafeteria-access',
  'kit-tareas-pizzeria': '/kit-tareas-pizzeria-access',
  'kit-tareas-hamburgueseria': '/kit-tareas-hamburgueseria-access',
  'kit-tareas-dark-kitchen': '/kit-tareas-dark-kitchen-access',
  'kit-tareas-pasteleria': '/kit-tareas-pasteleria-access',
  'kit-tareas-bar': '/kit-tareas-bar-access',
  'kit-tareas-catering': '/kit-tareas-catering-access',
  'kit-tareas-hotel': '/kit-tareas-hotel-completo-access',
  'kit-tareas-heladeria': '/kit-tareas-heladeria-access',
  'kit-tareas-chocolateria': '/kit-tareas-chocolateria-access',
  'kit-tareas-restaurante-creativo': '/kit-tareas-restaurante-creativo-access',
  'kit-tareas-chef-privado': '/kit-tareas-chef-privado-access',
  'kit-gestion-personal': '/kit-gestion-personal-access',
  'kit-inventario': '/kit-inventario-access',
  'kit-plan-financiero': '/kit-plan-financiero-access',
  'guia-dark-kitchen': '/guia-dark-kitchen-access',
  'guia-restaurante-gastronomico': '/guia-restaurante-gastronomico-access',
  'guia-restaurante-casual': '/guia-restaurante-casual-access',
  'guia-restaurante-mexicano': '/guia-restaurante-mexicano-access',
  'guia-restaurante-peruano': '/guia-restaurante-peruano-access',
  'guia-restaurante-japones': '/guia-restaurante-japones-access',
  'guia-restaurante-nikkei': '/guia-restaurante-nikkei-access',
  'mega-pack-tareas': '/mega-pack-tareas-access',
};

function loadEnv() {
  // Best-effort .env loader (no dependency on dotenv).
  const envPath = path.join(__dirname, '..', '.env');
  if (!fs.existsSync(envPath)) return;
  const content = fs.readFileSync(envPath, 'utf8');
  for (const line of content.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const idx = trimmed.indexOf('=');
    if (idx === -1) continue;
    const key = trimmed.slice(0, idx).trim();
    let value = trimmed.slice(idx + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    if (!(key in process.env)) process.env[key] = value;
  }
}

function main() {
  loadEnv();
  const [, , email, productId] = process.argv;

  if (!email || !productId) {
    console.error('Usage: node scripts/generate-access-link.mjs <email> <product-id>');
    console.error('\nValid product IDs:');
    for (const id of Object.keys(PRODUCTS)) console.error(`  - ${id}`);
    process.exit(1);
  }
  if (!PRODUCTS[productId]) {
    console.error(`Unknown product: ${productId}`);
    process.exit(1);
  }
  if (!process.env.JWT_SECRET) {
    console.error('JWT_SECRET not set. Add it to .env or export JWT_SECRET=<secret>.');
    process.exit(1);
  }

  const token = jwt.sign({ email, product: productId }, process.env.JWT_SECRET, { expiresIn: '365d' });
  const link = `https://aichef.pro${PRODUCTS[productId]}?jwt=${token}`;

  console.log('Magic link:');
  console.log(link);
}

main();
