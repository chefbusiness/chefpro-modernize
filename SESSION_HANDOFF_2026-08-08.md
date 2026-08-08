# Session Handoff — 2026-08-08 → lunes 10

## TL;DR

Jornada de **homologación del italiano**, que era el objetivo declarado de John:
llevar `/it` al nivel de español e inglés para lanzar tráfico a
`itapp.aichef.pro`. Se cierra con el árbol italiano **limpio de castellano
(91/91 páginas), los 61 spokes traducidos, el blog abierto y su primer post
nativo publicado**.

Por el camino, una auditoría adversarial destapó un fallo que **no era del
italiano y costaba dinero desde hacía 20 días**: las descargas de los 44
productos digitales daban 404 en producción.

**HEAD**: `34882cd` · **10 commits, todos pusheados, build verde, gates verdes.**

---

## Lo que se publicó hoy

| Commit | Qué |
|---|---|
| `0067c71` *(repo `chefbusiness-ai`)* | Bridge entero a `~deepseek/deepseek-v4-flash-latest` + `guard_idioma()` |
| `d76b184` | Los CTAs de compra de 6 idiomas iban a la plataforma española |
| `7e050c5` | **Los 524 entregables daban 404 desde el 19-jul** |
| `0eb7f38` | Nota de traspaso de productos digitales |
| `769e70c` | Castellano fuera del cromo italiano |
| `459ce4a` | Informe del catálogo de agentes italiano |
| `e2283e4` | **Los 51 spokes de casos de uso traducidos** |
| `16a9f1d` | Gate del árbol italiano + los 2 últimos focos |
| `9ca1f3b` | **Blog italiano abierto en `/it/blog`** |
| `2242154` | Primer post nativo: los 14 alérgenos |
| `bcbca0d` + `34882cd` | Roadmap del blog italiano (13 posts) |

### El italiano, antes y después

| | Al empezar | Al cerrar |
|---|---|---|
| Páginas sin castellano | **9 de 88** | **91 de 91** |
| Spokes con contenido italiano | 10 de 61 | **61 de 61** |
| Tarjetas en el hub `/it/casi-uso` | 10 | **43** (las mismas que ES) |
| Claves faltantes en `it.json` | 137 | **0** |
| Posts de blog | 0 | **1** (+ infraestructura completa) |

---

## Lo siguiente: lunes 10

**Post 2 del roadmap: `contaminazione crociata`** (1.600/mes, competencia BAJA).

**El cuerpo YA ESTÁ GENERADO Y VERIFICADO**, en
`.work/post2-contaminazione-crociata/`:
- `cuerpo2.html` — 2.589 palabras, 2 tablas, 7 `<h2>`, 0 `<h1>`, 0 acentos mal,
  0 caracteres no latinos, 0 sanciones inventadas, los 7 colores de tablero
  presentes.
- `prompt2.txt` — el prompt exacto, por si hay que regenerarlo.

⚠️ `.work/` está **gitignorado**: vive sólo en el VPS. Si se pierde, son 3
minutos de `bridge.py` con ese mismo prompt.

**Lo que falta para publicarlo** (mismo pipeline que el post 1, que está
documentado paso a paso en `ROADMAP_BLOG_ITALIANO.md`):

1. Generar 3 imágenes con la skill `generate-images` (destacada + 2 de cuerpo)
   y **mirarlas antes de optimizar** — en el post 1, una salía con harina sobre
   la tabla que debía estar limpia, ilustrando lo contrario del texto.
2. FAQ desde el People Also Ask ya recogido (está en
   `.work/research-blog-italiano.md`): «Quali sono i 3 tipi di contaminazione?»,
   «Qual è la differenza tra contaminazione diretta, indiretta e crociata?»,
   «Come si possono evitare le contaminazioni crociate?»… **fundiendo las
   variantes de "cos'è"**, que el PAA repite.
3. Ensamblar con `modDate` en el frontmatter (**sin él NO entra en el sitemap**),
   categoría `gestione-ristorante`, y enlace interno al post 1 (es su pilar).
4. CTA a `ID Allergeni` (`https://itapp.aichef.pro/id-alergenos-g6b6g-it`), que
   tiene la evaluación de riesgo de contacto cruzado como función declarada.
5. Gates y publicación:
   ```bash
   python3 scripts/astro-migration/fase8d-faq-duplicadas.py --lang it
   python3 scripts/astro-migration/fase8c-h1-unico.py
   python3 scripts/astro-migration/fase8b-regen-lastmod.py
   cd astro-site && rm -rf .astro dist && npm run build
   python3 scripts/astro-migration/fase9-gate-italiano.py --sin-red
   ```
6. Reenviar el sitemap: `https://aichef.pro/sitemap-index.xml` (por API del MCP
   de GSC, ya se hizo dos veces hoy).

**Martes y miércoles**: posts 3, 4 y 5 del clúster de alérgenos y HACCP
(`etichettatura allergeni` 880, `7 principi haccp` 390,
`temperature frigorifero haccp` 260), que cierran el bloque más rentable y
enlazan todos al pilar.

---

## Decisiones que esperan a John (no las tomo yo)

### 1. El catálogo italiano va 35 agentes por detrás → `CATALOGO_ITALIANO_PENDIENTE.md`

`itapp.aichef.pro` sirve **54 agentes de los 89 españoles**. Faltan tres bloques
enteros: los 10 de Consulenza Gastro Pro, los 12 de hotelería y ~13 de
marketing. **Ya hay 10 páginas italianas publicadas vendiendo los de
consulenza**, que el visitante no encontrará al registrarse. Es trabajo de John
en Pickaxe, no de código.

### 2. `itapp` no tiene etiqueta de conversión

Cero apariciones de `AW-17829651892` frente a 9 en la plataforma española.
**Sin eso no se registra ni una conversión del italiano**, así que no se podrá
medir nada de lo que estamos construyendo. 30-45 min manuales en el campo *Body*
del workspace de Pickaxe; el snippet está en `GOOGLE_ADS_PICKAXE.md`.

### 3. Productos digitales, EN PAUSA por decisión suya → `PRODUCTOS_DIGITALES_PENDIENTE.md`

Se retoma desde el Claude Code local. La nota lleva el diagnóstico completo para
no repetir la auditoría.

### 4. Netlify avisó de límite de Edge Functions

Consultado hoy: sólo hay **una viva**, `lang-redirect`, y sólo en la ruta `/`.
Si Netlify la corta, el único efecto es que quien teclee `aichef.pro` verá la
home en español en vez de ir a la suya. **No afecta a SEO** (la función ya salta
a los bots) ni a ninguna URL profunda. La sospecha es que el consumo viene de
bots —la función se factura antes de decidir saltárselos— o de campañas de Ads
apuntando a `/`. Recomendación: mirar *Analytics → Edge Functions* antes de
tocar nada.

---

## Gotchas nuevos, que valen dinero

1. **Lo que vive sólo en `public/` de la raíz NO se publica** desde el cutover
   de Fase 7. Así estuvieron 20 días en 404 los 524 entregables. El build sale
   verde igual y no avisa. Falta escribir el gate que compare `public/` con
   `astro-site/public/`.
2. **Astro enruta por el nombre del DIRECTORIO**, no por el helper de rutas. La
   carpeta del blog italiano tuvo que llamarse `categoria/`, no `category/`, o
   cada enlace de categoría habría sido un 404.
3. **Sin `modDate` un post no entra en el sitemap.** Lo avisa
   `fase8b-regen-lastmod.py`.
4. **`dataforseo.py` apunta a España (2724) por defecto.** Una tanda entera del
   research salió con datos españoles y hubo que tirarla. Toda consulta italiana
   necesita `--pais 2380 --idioma it`.
5. **Los préstamos universales de cocina no son «palabras de otro idioma»**
   (corrección de John): `mise en place`, `chef`, `sous vide`, `food cost`. Casi
   cuesta descartar un post de 18.100 búsquedas/mes. Está documentado en el
   roadmap.
6. **El gemelo de la SPA.** Arreglar `Footer.astro` no basta: 17 páginas
   italianas montan `ModernFooter.tsx` vía island. Hay que tocar los dos.

---

## Estado del entorno

- Repo limpio, `main` == `origin/main`, nada sin commitear.
- Último build: **1.251 páginas, verde**. Gate italiano **91/91**.
- Sitemap reenviado a GSC a las 21:28 (*Pending processing*).
- El research crudo del blog (6 clústeres, ~700 keywords, 60+ SERP) está en
  `.work/research-blog-italiano.md` y `.work/*.json` — **gitignorado**, sólo en
  el VPS.
