// Registra loader.mjs (ver comparar.mjs para el uso).
import { register } from 'node:module';
register(new URL('./loader.mjs', import.meta.url));
