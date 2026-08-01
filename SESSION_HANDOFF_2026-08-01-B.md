# SESSION HANDOFF — 2026-08-01 (noche): 8C-inglés completo, SSR de las free tools, limpieza del blog

> Continúa `SESSION_HANDOFF_2026-08-01.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión larga desde el VPS, en modo UltraCode. Cinco commits, todos pusheados y verificados en producción.

## ✅ Hecho y verificado EN PRODUCCIÓN

| Commit | Qué |
|---|---|
| `9960b1b` | 21 librerías de prompts en inglés + reparación del generador |
| `9e76f6a` | Un solo `<h1>` por página: 26 posts servían dos |
| `c80b148` | Las 5 librerías del molde WordPress antiguo → **26 de 26** |
| `ac83809` | **Las 119 páginas indexables de marketing pasan a SSR** |
| `c36d9ac` | Hub inglés `/en/prompt-libraries` |

Estado final medido contra el `dist` y contra `aichef.pro`:

- **1.121 URLs indexables y NINGUNA sin texto server-side** (antes: 119 con cero).
- **1.123 páginas con exactamente un `<h1>`, ninguna con dos.**
- Gate de las 26 librerías EN: **26/26 sin errores**.
- Gate de enlaces internos: **189 destinos, 1 roto** (el de newsletter, dejado a propósito — ver abajo).
- Build verde, 1.248 páginas.

## 🔴 Lo más gordo: las 119 páginas que servían HTML vacío

17 free tools × 7 idiomas se montaban con `client:only="react"`, así que Astro **no las renderizaba en servidor**: `<title>` y meta correctos, cuerpo con **cero caracteres** hasta que corriera el JS. Es literalmente la patología que motivó migrar a Astro (§1 del plan maestro) y ese clúster se quedó fuera del cambio, sin que nadie lo detectara en nueve meses.

Pasarlas a `client:load` exigió resolver dos cosas:

1. **La ubicación.** El shim del router leía `window.location` en el initializer de un `useState` —que corre durante el render— y reventaba con «window is not defined». Ahora la página Astro inyecta su path por contexto.
2. **El idioma, que era el riesgo de verdad.** i18next detecta por `localStorage`/`navigator`, que no existen en servidor, y `useLanguage` lo corrige en un `useEffect` que en SSR **no corre**. Sin fijarlo, las seis versiones no españolas se habrían renderizado **en español**: contenido equivocado servido a Google en `/en/`, `/fr/`, `/de/`… Peor que no tener contenido. Lo resuelve `MarketingShell`.

Más dos bloqueos del build: `AnnouncementBar` leía `localStorage` durante el render, y `jspdf`/`xlsx` (CommonJS) rompen el loader ESM de Node en el pase SSR → `vite.ssr.noExternal`.

**Lo que NO se tocó, a propósito**: las 89 páginas de la zona app siguen con `client:only`. Es contenido de PAGO y renderizarlo en servidor lo metería en el HTML público. Verificado: 0 de las 89 emiten texto. Las 35 legales también siguen igual (fuera del sitemap por D6).

Verificado con navegador real (Playwright): 0 errores y 0 avisos de hidratación en ES/EN/DE/NL, el idioma se mantiene tras hidratar, **la URL gana a la caché de `localStorage`** (con `i18nextLng=en` guardado, la página ES sale en español) y las herramientas siguen siendo interactivas.

## 🧹 Limpieza del blog

- **Widget de relacionados congelado**, en 15 posts: un bloque `wp-block-blocksy-query` serializado al exportar de WordPress. Duplicaba los relacionados que ya pinta el layout, metía 7-8 `<h2>` falsos por post y **enlazaba a tres páginas 404**. En 4 posts ni siquiera tenía título: una rejilla de tarjetas soltada a media página.
- **10 enlaces internos muertos** repuntados a su destino vivo. Aparecieron al barrer los 4.102 enlaces del blog (195 destinos únicos): no se veían desde el repo porque son URLs absolutas dentro del HTML de los posts.
- **26 `<h1>` duplicados** eliminados o degradados. Mi primer censo encontró solo 6 porque miré una sola vía (HTML crudo, no Markdown `#`) y una sola carpeta (ES, no EN).

## 🚧 Pendiente de John — decisiones, no trabajo

1. **El CTA de newsletter.** `context-window-ventana-contexto-ia` tiene un «SUSCRIBIRME GRATIS → /newsletter» que da 404, y el formulario de newsletter del pie está **explícitamente desconectado** en el código. No hay newsletter detrás. Elegir destino o quitar el CTA es decisión de negocio; lo dejé intacto.
2. **Contenido delgado que el widget disfrazaba**: `cocina-molecular-concepto-y-definicion` queda en **381 palabras** y `que-es-el-food-pairing` en **421**. Decidir si ampliar o consolidar con 301.
3. **El listado inglés completo de agentes** (77 nombres + nombres de los módulos del menú). Sin él, el hub inglés indexa solo las 26 con librería; con él puede pasar a ser el catálogo entero, como el español. **No lo deduzco del código**: es el error que ya costó cuatro correcciones.
4. Sigue pendiente lo de siempre: **alias de `enblog.aichef.pro` en Netlify + DNS** (`CUTOVER_ENBLOG_PENDIENTE.md`).

## 🧭 Qué sigue

- Los ~58 agentes españoles sin librería (12 de ellos el bloque de hotelería).
- Las páginas por agente de 8C, que siguen sin arrancar.
- Vigilar en GSC el efecto de las 119 páginas que ahora sí tienen contenido indexable: es el cambio con más potencial de la sesión y hasta ahora no había nada que indexar en ellas.

## 🛠️ Gates nuevos (correr antes de dar nada por bueno)

```bash
python3 scripts/astro-migration/fase8c-libreria-en-gate.py --todos   # 26 librerías EN vs su original ES
python3 scripts/astro-migration/fase8c-h1-unico.py                   # un solo <h1> por página
python3 scripts/astro-migration/fase8c-quitar-relacionados.py        # widget congelado
python3 scripts/astro-migration/fase8c-enlaces-vivos.py              # enlaces internos vs producción
```

## 📌 El patrón de mis propios errores, para no repetirlo

De los fallos de la sesión que fueron míos, **tres son el mismo**: usar un umbral de longitud como prueba de validez. Prompts de +40 caracteres descartaba `«Dame el escandallo de este plato»`; alts de +15 descartaba `"AI Chef Pro"`; respuestas de +200 rechazaba tandas de alts correctas. En los tres casos el validador bueno ya existía —**el recuento contra la fuente española**— y el umbral solo añadía falsos negativos que parecían fallos del modelo.

Y dos veces estuve a punto de publicar nombres inventados: una porque iba a derivar el `alt` de un fichero llamado `chef-diego-schattenhofer-78.jpg` (una persona real), y otra porque bridge se inventó los agentes «Line Cook», «Sous Chef» y «Pastry Chef» para el hub. **La fuente de los nombres es siempre el listado de la plataforma.**
