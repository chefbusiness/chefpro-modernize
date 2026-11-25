# Handoff 24-25 nov 2026 — Estrategia LowFruits ES (sesión Claude Code, Mac)

> Sesión Claude Code en el Mac. Cursor PARADO en contenidos por orden de John («hasta nuevo aviso»).
> Fuente de la estrategia: `/Users/johnguerrero/aichef-lowfruits/Español/aichef-lowfruits-ES-2026-11.md`
> (hay carpetas hermanas EN, FR, DE, IT, NL, PT-PT y PT-BR con el mismo formato, sin tocar).

## 1. Decisiones de John en esta sesión

- **Motor de redacción:** borrador con `deepseek/deepseek-v4.1-flash-1017` vía **Ori** (CLI de OpenRouter, instalada
  global: `~/.local/bin/ori` + `/usr/local/bin/ori`, login OAuth hecho) y pasada final de Opus (revisión cifra a cifra +
  auditoría adversarial). Recogido en el punto 2 del `CLAUDE.md`. Es ese modelo exacto, no el `~deepseek-v4-flash-latest`.
  Uso: `ori claude --model deepseek/deepseek-v4.1-flash-1017 --reasoning-effort high -- -p "<brief>"`.
- **Escandallo:** lo atacan aichef (IA generativa) **y** Miselup (gestión / base de datos) a la vez. «Uno crea, el otro guarda».
- **«Luz verde hasta completar todo en español».** Los merges necesitan «fusiona #N» explícito (el modo automático no
  acepta «luz verde»).

## 2. Lo publicado / en PR

| PR | Pieza | Volumen (DataForSEO, ES) | Estado |
|---|---|---|---|
| #241 | Pilar escandallo en su URL + plantilla Excel gratis | escandallo 5.400 · cómo hacer 140 · de costes 480 | LIVE (`b0fb7202`) |
| #242 | Glosario: qué es el maridaje · qué es un menú degustación | maridaje: qué es 880+880, significado 390, de vinos 390 | LIVE (`380462d8`) |
| #243 | Software para restaurantes (guía nueva) | ≈ 690 en variantes | LIVE (`2f6a5d3d`) |
| #244 | Ficha técnica de cocina (guía nueva) + plantilla | ≈ 490 en variantes | auditado + corregido |
| #245 | Ingeniería de menú: refresco + plantilla (regla del 70 %) | 90 + menu engineering 260 | auditado + corregido |
| #246 | APPCC: refresco «qué es» + plantilla de temperaturas | **qué es el APPCC 2.400** | auditado + corregido |
| #247 | Bloque A: meta honestas en posts que ya rankean | — | auditado + corregido |
| #248 | Sección «Maridaje de vino y queso» + tabla de quesos (dentro del post del maridaje) | 40 | auditado + corregido |
| #249 | Tutorial «Cómo hacer vídeos de recetas con IA» | vídeos de recetas 110 · con IA 10 | auditado + corregido |

Plantillas gratis en `astro-site/public/descargas/` (todas con `noindex` por `netlify.toml`), generadores en
`scripts/contenidos/` con `inject_cache.py` y gate sobre celdas: escandallo, ficha técnica, ingeniería de menú,
registro de temperaturas APPCC. El ejemplo del salmón (4,29 €) es el mismo en escandallo y ficha (calabacín 89 g).

## 3. Método que funcionó (repetible para los otros idiomas)

GSC (qué URL ya rankea; refrescar en la misma URL si existe) → DataForSEO `vol` (re-medir: LowFruits subestima) +
`serp` → brief con TODAS las cifras calculadas → DeepSeek vía Ori → revisión de Opus → montaje quirúrgico por anclas
(script en el scratchpad, aserciones de conteo) → imágenes Nano Banana (sin caras, sin texto, sin marcas) → banners
del catálogo (`fase8c-libreria-assemble.banner`) → enlaces entrantes → `fase8b-regen-lastmod.py` → gate FAQ → PR →
1 auditor Opus adversarial (de uno en uno por la temperatura) → correcciones → preview con curl.

Lo que cazaron las auditorías (y hay que mirar SIEMPRE): DeepSeek añade cifras que no se le dan; describir productos
propios sin leer su ficha (`astro-site/src/data/productos/`); afirmar cosas falsas de terceros (Last.app sí tiene
escandallos); tablas sin fila de cabecera; FAQ que contradicen el cuerpo; plantillas con celdas cortadas.

## 4. Pendiente (fuera de LowFruits, decidir con John)

- **Reemplazo roto del 15-ago (`e601ba42`)**: «plan gratuito» → «Plan AI Chef Miembro» dejó a competidores con
  nuestro plan y planes inventados en **12 posts** (`git grep -l "Plan AI Chef Miembro" -- astro-site/src/content/blog/es`).
  Peor en `ia-para-recetas-de-cocina-gratis` (top 5) y `generador-de-recetas-con-ingredientes-por-ia`: además, estrellas
  y «Precisión técnica %» de competidores y porcentajes sin fuente. En #247 NO se les subió el modDate.
- `/software-gestion-cocina-ia` promete stock «en tiempo real»; pSEO `software-gestion-restaurante/[ciudad]` dice
  «Comparativa Verificada»; `mejores-ia-restaurantes-2026` conserva 4 «en tiempo real».
- Canibalización «IA para cocinar»: rankean `ia-para-recetas-de-cocina-gratis` (5) y `las-7-mejores-apps…` (5,9), no el
  pilar de Cursor #227 (`mejor-ia-para-cocinar-en-2025`, 11).
- `fase8b-regen-lastmod.py` baja siempre `/blog/ia-gestion-alergenos-hosteleria` a 22-nov (su `.md` dice 22 y el JSON 23).
- `~/chefbusiness-ai/.env` del Mac: `OPENROUTER_API_KEY` revocada (401) → bridge.py no funciona en el Mac.
- **Regla de John (25-nov):** en LowFruits NO aplica la regla de proporcionalidad: se hacen todas las oportunidades, aunque tengan 10 búsquedas (formato más barato que no canibalice: sección dentro del post afín si existe).
- Siguiente: aplicar el mismo método a otro idioma de `/Users/johnguerrero/aichef-lowfruits/`.
