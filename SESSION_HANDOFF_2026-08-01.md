# SESSION HANDOFF — 2026-07-31/08-01 (8C arranca: librerías de prompts, hub y salto al inglés)

> Continúa `SESSION_HANDOFF_2026-07-30.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión larga, trabajada desde el **VPS**; la última parte en modo **UltraCode**.

## ✅ Hecho y verificado en producción

1. **Dos librerías de prompts nuevas** — `ID Alérgenos` (105 prompts) y `Comida de Personal`
   (105 prompts). 7 bloques × 15, 10 FAQ **en frontmatter** (emiten `FAQPage`, cosa que los 25
   heredados no hacían), 3 imágenes propias cada una.
2. **Generador reutilizable** `fase8c-libreria-assemble.py` + config JSON por agente. Cachea cada
   sección, así que un fallo se reintenta solo esa parte. Aborta si la config trae menos de 3
   productos.
3. **Hub `/libreria-de-prompts` reconstruido** — la migración lo había degradado a un 301 hacia la
   archive cronológica. Ahora es página propia con **85 agentes en los 15 módulos reales de la
   plataforma** y 27 librerías enlazadas. El 301 del subdominio y el enlace del pie apuntan aquí.
4. **🐛 Tablas de prompts: escondían el 72 % del contenido** (2.205 px fuera de pantalla en
   escritorio, 88 % en móvil). Medido con Chromium headless, no a ojo. Arreglado en dos capas:
   global (las tablas se ajustan y el texto rompe línea) y `.tabla-prompts` (columnas 58/24/18 en
   escritorio; en móvil cada fila es una tarjeta). 177 tablas en 26 posts.
5. **81 banners de productos digitales** en 27 posts (política nueva: mínimo 3 por post, a tres
   alturas). Datos leídos del catálogo real, elección por relevancia temática, UTM por post.
6. **Marca**: canal oficial `@aichefpro` en el icono social **y** en la columna de Formación (7
   idiomas); el nombre de John enlaza a johnguerrero.es en las 361 firmas del blog, `/sobre-nosotros`,
   `/faq` y 6 landings; `sameAs` de la Organization cuadrado con los perfiles que enlaza el pie.
7. **DataForSEO operativo** (saldo 44 $). Keywords Everywhere y Brave están **muertas**.

## ⚠️ Cuatro errores míos que corrigió John — leer antes de tocar el catálogo

Todos con la misma raíz: **crucé fuentes del repo (`apps.ts`, sitemap de la app,
`linkify-use-case.tsx`) creyendo que describían el producto. Son vistas parciales y viejas.**

| Lo que publiqué | La realidad |
|---|---|
| Hub sin categoría de hotelería, «porque estaba vacía» | Existe con **12 agentes**, en los dos idiomas |
| 3 agentes que no existen (`Chef Español AI`, `Chatbot Gastronómico Experto`, `ChatGPT para tus estudios`) | Inventados al cruzar fuentes |
| Recetarios como «Mexicana», «Peruana» | Son «Cocina Mexicana», «Cocina Peruana». **CLAUDE.md afirmaba lo contrario y era falso**; ya corregido |
| Iba a publicar los 27 posts EN con los nombres españoles | La plataforma inglesa usa nombres propios: `Allergen ID`, `Waste GenCal`, `Staff Meal`, `Avant-garde Cuisine`… |

**Fuente autorizada a partir de ahora**: los listados de Pickaxe que pasó John (86 agentes ES /
77 EN), volcados en `fase8c-agentes/catalogo-hub.json` y `agentes-en.json`. Ante cualquier duda de
catálogo, **pedirle el listado**, no deducirlo del código.

## 🚧 En curso, a medio terminar

- **Adaptación al inglés de las 26 librerías.** `fase8c-libreria-en.py` está escrito y ya hace
  cabecera, bloques, tips, FAQ, alts, banners bilingües, pares de traducción y ensamblado del
  `.md`… **pero NUNCA se ha ejecutado de principio a fin**. El piloto (`--slug id-alergenos`)
  estaba corriendo al cerrar; sus piezas viven en `/tmp/fase8c-libreria-en/` y **no hay ningún
  `.md` escrito**. Es lo primero que hay que verificar de forma adversarial.
- Decisiones ya tomadas para el inglés: **EE. UU. como mercado por defecto** (FDA Food Code,
  FALCPA, «Big Nine», imperial, dólares) con **guiño a UK (FSA, Natasha's Law), Australia y Nueva
  Zelanda (FSANZ) e India (FSSAI)** nombrando solo al regulador, nunca artículos ni umbrales.
  Los **banners apuntan de momento a la landing ES** (no hay landings de producto en inglés) con
  el UTM del post inglés para poder medir esa fuga.
- `Chef Privado Pro` **no tiene versión inglesa**: se queda fuera de la tanda (26 de 27).

## ⏳ Pendiente de John

1. **Alias de `enblog.aichef.pro` en Netlify + DNS** (runbook `CUTOVER_ENBLOG_PENDIENTE.md`; ojo a
   las A records que recrea el panel de Hostinger).
2. **Search Console**: solicitar indexación de las archives y dar de baja los 5 sitemaps muertos.
3. Decir qué agentes más son **formularios** (GastroIMG Gen+ ya está fuera): según se pidan.

## 🧭 Qué sigue

1. **Verificar el piloto inglés de forma adversarial** antes de generar los otros 25: normativa
   (que FDA/FALCPA no traiga datos inventados y que los guiños a FSA/FSANZ/FSSAI no citen artículos
   falsos), conversiones de unidades, inglés idiomático real, paridad con el molde, hreflang
   recíproco y banners.
2. Generar las 25 restantes en tandas paralelas + **hub `/en/prompt-library`**.
3. Sólo entonces, seguir con agentes nuevos en español (quedan ~58 sin librería, 12 de ellos el
   bloque de hotel, que solo tiene sentido en inglés de momento).

## Commits de la sesión

`4fa041e` ID Alérgenos + generador · `4f26ddb` hub · `e3e32ef` tablas · `4823cfe` banners ·
`f110965` YouTube en Formación + infraestructura EN · `c3da24d` pares de traducción ·
`071f013` hotelería restaurada + mapa EN · `c59f1b3` catálogo real · `6d7ca52` módulos reales.
