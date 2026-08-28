# Handoff — 2026-08-27 · El `robots.txt` bloqueaba 27 URLs del blog inglés

**Estado: RESUELTO y desplegado.** Commits `3f5c6f6` y `03c82a2` en `main`, producción
verificada. Lo que queda son dos tareas de John y una ventana de verificación en GSC.

---

## 1. Qué pasaba

John trajo el caso desde GSC: «varios posts en inglés» sin indexar. El censo URL a URL
dio el patrón exacto — **las 26 librerías de prompts inglesas (tanda 8C del 1-ago) y su
categoría, ninguna rastreada nunca**, mientras sus gemelas españolas estaban indexadas.

La causa estaba en `astro-site/public/robots.txt`, que protegía la zona de pago con:

```
Disallow: /*-access
Disallow: /*-library
```

**En robots.txt un patrón sin `$` casa por PREFIJO, no «acaba en».** `/*-library` se lee
como «`/` + lo que sea + `-library` + lo que venga detrás», así que también casaba con
`/en/blog/prompt-library-barista-consulting`. La regla es de la Fase 5 (commit `cad7717`);
los posts nacieron después y cayeron dentro sin que nadie lo notara.

Evidencia recogida en GSC (`sc-domain:aichef.pro`):

| URL | coverage_state | last_crawled |
|---|---|---|
| `/en/blog/prompt-library-gastronomy-consulting` | **Blocked by robots.txt** | 2026-08-20 |
| las otras 25 librerías | *URL is unknown* / *Discovered – not indexed* | **Never** |
| `/en/blog/category/prompt-library` | *URL is unknown* | Never |
| `/blog/libreria-de-prompts-para-barista-…` (gemela ES) | Submitted and **indexed** | 2026-08-26 |

**Por qué duró un mes:** el sitemap las declaraba correctamente (1.183 URLs, 0 errores,
leído por Google el 26-ago), las páginas servían 200 con canonical propio y `index, follow`,
y el build salía verde. Un bloqueo de robots.txt no rompe nada, no sale en ningún diff y
no genera ningún aviso.

De regalo, el **mismo patrón mal escrito en el filtro del sitemap** (`astro.config.mjs`,
`endsWith('-library')`) dejaba además la categoría inglesa fuera del sitemap — el mismo
tropiezo que ya tuvo el hub `/en/prompt-libraries` y que entonces se resolvió renombrando.

## 2. Qué se cambió

**`3f5c6f6` — el arreglo**

- **`robots.txt`**: las reglas de la zona app se anclan al **prefijo de cada familia de
  producto** (`/kit-*-library`, `/guia-*-access`… × 6 prefijos × 2 sufijos, en los 5 grupos
  de user-agent). Ninguna URL del blog empieza por `/kit-` ni `/guia-`, así que no puede
  volver a rozarla. **Sin ancla final `$` a propósito**: con ella se escapaban
  `/kit-escandallos-library/` (301) y `?x=1` (200).
- **`astro.config.mjs`**: el filtro del sitemap pasa de `endsWith()` a
  `/^\/[^/]+-(access|library)$/` — la zona app es siempre de **un solo segmento en la raíz**
  (las 88 páginas viven directamente en `src/pages/`, comprobado).
- **`scripts/astro-migration/robots-gate.py`** (nuevo): implementa la spec de Google
  (comodín, `$`, gana el path más largo, empate → Allow) sin dependencias —`pip install`
  choca con PEP 668 en el VPS— y exige, **para cada user-agent del fichero**, que toda URL
  del `dist/` sea rastreable y toda ruta de la zona app esté bloqueada.
- **3 gates existentes** que afirmaban las cadenas viejas y habrían salido rojos:
  `fase5-gate-s1-s2.py`, `fase6-gate.py` (cuyo check de fugas era además **vacuo**: buscaba
  `-access</loc>` sobre una lista de *paths*, no sobre el XML → no casaba nunca) y
  `fase7-vigilancia.py`.
- La trampa documentada en `CLAUDE.md`.

**`03c82a2` — de propina, el vigilante estaba roto**

`fase7-vigilancia.py` derivaba el nº esperado de `<loc>` **solo del blog español**, así que
llevaba rojo desde que nacieron EN/IT/FR/DE/PT («1184 != 1051»). Una alarma siempre roja no
avisa de nada, y es el script que debe despertar a John si producción se desvía. Ahora suma
los 6 idiomas (posts + hub + paginación de 24 + categorías con posts) y se le añadieron a
`_F8_EXTRA` los dos hubs de librerías (`/libreria-de-prompts`, `/en/prompt-libraries`), que
nacieron en 8C y no contabilizaba nadie.

## 3. Verificación

- Cross-check del matcher propio contra **Protego** (parser de la spec de Google):
  **1.313 rutas, 0 discrepancias**.
- **Contraprueba**: con el `robots.txt` anterior el gate canta exactamente **27** URLs
  públicas bloqueadas (las 26 + la categoría) y **0** fugas de zona app; con el nuevo, 0 y 0.
  El gate no es vacuo.
- Build limpio con `.astro` purgado: **1.309 páginas**, sitemap **1.183 → 1.184**; la única
  alta es la categoría y ninguna URL de zona app se cuela.
- En producción, tras el deploy: `robots-gate.py --live` en verde, **27/27 rastreables por
  Googlebot**, `/en/blog/category/prompt-library` en el sitemap vivo, `fase7-vigilancia.py`
  todo verde y sitemap reenviado por GSC (22:39).
- Las 88 páginas de pago siguen protegidas por triple capa: robots + `noindex` en el HTML
  (verificado en las 88) + exclusión del sitemap.

## 4. Pendiente

1. **John, en la UI de GSC** (la API no expone ese botón): *Inspección de URLs* →
   **Solicitar indexación** en 3-4 piezas para acelerar el arranque —
   `prompt-library-allergen-identification`, `prompt-library-barista-consulting`,
   `prompt-library-food-pairing` y `/en/blog/category/prompt-library`. El resto entrará por
   sitemap y por los enlaces del hub `/en/prompt-libraries` (que sí está indexado).
2. **Ventana de verificación**: reinspeccionar en GSC hacia el **3-sep** (¿ya rastreadas?) y
   el **17-sep** (¿indexadas?). Si a las 3 semanas siguen en *Discovered*, el problema ya no
   es técnico sino de demanda/calidad y se decide entonces.
3. **Los 5 posts EN de la 8B.6 que no están indexados en NINGUNA de las dos URLs**
   (`ai-food-cost-calculator-reduce-costs`, `ai-recipe-scaling-guide`,
   `ai-restaurant-management-software`, `haccp-plan-template-restaurant-guide`,
   `restaurant-menu-pricing-strategy-ai`): no es un bug — sirven 200, self-canonical, están
   en el sitemap. En `enblog.aichef.pro` figuran como *Crawled – currently not indexed*, y
   ese WordPress **sigue vivo, en 200 y declarándose canónico de sí mismo**. Argumento
   adicional para el cutover pendiente (`CUTOVER_ENBLOG_PENDIENTE.md`).
4. **Regla de oro que queda**: al publicar contenido nuevo, comprobar que su URL no cae en
   ningún patrón de `robots.txt` → `python3 scripts/astro-migration/robots-gate.py`. Y si
   nace una familia de producto con un prefijo distinto de `guia- kit- mega- pack- plan-
   pro-`, hay que añadirle sus dos líneas al `robots.txt` (el gate lo cantará).

## 5. Datos de referencia (medidos el 27-ago, para no volver a medirlos)

- Blog EN: **66 posts** (40 de la 8B.6 + 26 librerías 8C) — de los 40, **35 indexados**.
- Sitemap de producción: **1.184 URLs**, de las cuales **476 son blog**
  (325 ES · 66 EN · 14 DE · 14 FR · 13 IT · 6 PT).
- Zona app: **88 páginas**, 6 prefijos (`kit-` 46, `plan-` 20, `guia-` 16, `pro-`/`pack-`/
  `mega-` 2 cada uno), todas con `noindex`.
- `/sitemap.xml` responde **301 → /sitemap-index.xml** (la línea `Sitemap:` del robots ya
  apunta directamente al index).
- `llms.txt` **no contiene ninguna URL del blog** (es una descripción del sitio del 28-jul).
  No es una regresión, pero si algún día se quiere que los crawlers de IA lo usen, hay
  trabajo ahí.
