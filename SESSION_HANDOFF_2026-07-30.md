# SESSION HANDOFF — 2026-07-30 (auditoría de riesgo de imagen CERRADA)

> Continuación de `SESSION_HANDOFF_2026-07-29.md`. Doc canónico:
> `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8. Sesión trabajada desde el **VPS**.

## ✅ Qué quedó HECHO y VERIFICADO

**Fase 2 del escáner de riesgo de imagen** (`a92ed1f`) — la que quedaba abierta desde que se
cazó la imagen con parecido a Gordon Ramsay.

- **1.096 imágenes** escaneadas (las que publican los 361 posts, ES **y EN**) → **477 con cara**
  → analizadas una a una en fase 2.
- **Conclusión: aquello fue un incidente aislado, no un patrón.** Sólo 2 críticos.

| Nivel | Nº | Qué se hizo |
|---|---:|---|
| CRÍTICO | 2 | Retiradas y regeneradas |
| ALTO (marca de terceros) | 159 | Nada: ruido o fotos legítimas |
| MEDIO (retrato posado) | 14 | **Nada — decisión de John: se quedan** |
| BAJO (texto ilegible IA) | 112 | Anotado |
| Sin hallazgos | 190 | — |

### Los 2 críticos (los dos eran imagen DESTACADA)

- `chefpriv-destacada-chef-privado.jpg` → el modelo dijo "parecido a Lea Roesi", pero al abrirla
  no era un parecido: la chaquetilla llevaba **bordado un nombre propio inventado con los glifos
  rotos** ("Izab…n Roesi"). Persona ficticia presentada como real + texto ilegible en un post
  comercial. Sustituida por `chefpriv-emplatado-manos.jpg` (manos emplatando sobre mármol).
- `hacks-gestion-restaurantes-aichefpro-4.jpeg` → el modelo dijo "Javier Bardem, confianza alta".
  **Verificada a ojo: NO hay parecido inequívoco**, es un arquetipo genérico de empresario. Se
  retiró igualmente por ser cara en primer plano como destacada (regla de marca del pipeline),
  dejando constancia de la discrepancia. Sustituida por `hacks-gestion-sala-reservas.jpg`.

Ambas generadas con Nano Banana 2 sin caras, sin marcas y sin texto. `modDate` a 2026-07-29 en
los dos posts + regen de `blog-lastmod.json`. **Verificado live**: nuevas en 200, retiradas en
404, `og:image` apuntando a las nuevas.

### Dos fallos del propio escáner, arreglados

- Sólo miraba `content/blog/es/`: **las 93 imágenes del blog EN no se habían escaneado nunca.**
- Daba por limpias las imágenes que fallaban con error de API; ahora las reintenta.
- Modo nuevo `--informe`: ordena por gravedad y dice en qué post vive cada imagen.

## ⚠️ Cómo leer este escáner (sobre-marca)

- Los "marca de tercero" son casi todos ruido: logo de Apple en un portátil, capturas de tutorial
  con Google/WordPress, un horno RATIONAL en una cocina real. Varias son **fotos legítimas del
  entorno de John** (Diego Schattenhofer, 1973 Taste, Michelin, Repsol).
- Parte de lo que llama "marca" son **glifos rotos** de texto generado ("A'Chef Pro", "d Chlef").
- Un "parecido con confianza alta" **no basta para actuar**: hay que abrir la imagen y mirarla.
- El JSON versionado (`fase8c-escaneo-imagenes.json`) hace de caché: al añadir imágenes nuevas,
  fase 1 + fase 2 sólo escanean lo que no ha visto.

## ⏳ Sigue pendiente de John (sin cambios desde el 29)

1. **`enblog.aichef.pro` → alias en Netlify + DNS** (runbook `CUTOVER_ENBLOG_PENDIENTE.md`;
   ojo a las A records que recrea el panel de Hostinger).
2. **Search Console** (sólo UI): solicitar indexación de las archives + posts prioritarios y dar
   de baja los 5 sitemaps muertos de `blog.aichef.pro`.

Él confirmó el 29 que las hará y avisará. **No insistir cada sesión**: preguntar una vez.

## 🧭 Ruta: qué sigue

Del menú de 6 rutas del handoff del 29, la **D (escáner de imagen)** queda **cerrada**. El orden
recomendado que queda:

1. **C — 8C, páginas por agente (~70)**: línea principal. Son las páginas que monetizan, absorben
   las 25 librerías de prompts con 301 y dan esqueleto de enlazado interno, que es justo lo que
   le falta a lo ya publicado. Ojo REGLA CAPITAL: keyword research + SERP **por agente** antes de
   redactar; catálogo canónico en `src/lib/linkify-use-case.tsx` y `src/data/apps.ts`.
2. **B — CTR del blog**: 7.428 impresiones/semana a posición media 8,8 con CTR ~1%. Es la ganancia
   más barata que hay y sirve de relleno para sesiones cortas.
3. **E — blog en it/pt/fr**: 363 clics/90d demostrados que hoy se tiran al hub ES; la
   infraestructura multi-idioma ya está construida. Después de C.
4. **A — cerrar 8B.6** en cuanto John toque el DNS.
5. **F — Fase 9, sustituir Pickaxe**: el salto de producto.

## Commits

`a92ed1f` fase 2 del escáner + 2 destacadas regeneradas.
