# Instrucciones del proyecto — aichef.pro (chefpro-modernize)

## 🚨 REGLA CAPITAL — Generación de contenidos (BLOQUEANTE)

Aplica a **cualquier** contenido (artículo, landing, ficha de producto, post, página) en este o cualquier proyecto del grupo ChefBusiness. **Antes de escribir la primera línea:**

1. **Keyword research + análisis SERP PRIMERO.** Nunca escribir sin investigar keywords e inspeccionar la SERP de Google del/los mercado(s) objetivo. Lo que dicte la SERP (formatos, People Also Ask, entidades, intención) manda sobre lo que se incluye.
2. **Texto → `bridge.py` (DeepSeek v4).** Motor de redacción: `/Users/johnguerrero/chefbusiness-ai/bridge.py` (`--task content`/`translation` → `deepseek-v4-pro`). Gotcha: es modelo de razonamiento → usar `--max-tokens` ≥ 8000 o devuelve vacío.
3. **Imágenes → skill `generate-images` (Gemini "Nano Banana 2").** Todas las imágenes del contenido.
4. **Contenido ENRIQUECIDO obligatorio:** tablas, datos, métricas, citas, listados y comparaciones (cuando apliquen) + sección de **Preguntas Frecuentes (FAQ)** + lo que indique el análisis SERP.
5. **Imágenes dentro del cuerpo: mínimo 2.** Además, una **imagen destacada (featured) ÚNICA** que **no** se repite dentro del contenido.
6. **Ortografía y semántica perfectas; tono amigable y humano** (no corporativo, no robótico).

> Un contenido sin research/SERP previo, o sin tablas/datos/FAQ/≥2 imágenes + destacada única, **no está terminado**.

## Stack y notas operativas

- **Stack**: React 18 + TypeScript + Vite + Tailwind + Netlify (auto-deploy desde `main`). Dev server en puerto 8080.
- **i18n**: 7 idiomas (es, en, fr, de, it, pt, nl).
- **Live**: https://aichef.pro
- **SEO**: `SEOHead` + edge function `netlify/edge-functions/og-meta.ts` (OG por ruta) + `public/sitemap.xml` (multi-formato → editar siempre con parser DOTALL, nunca awk línea-a-línea) + GSC `sc-domain:aichef.pro`.
