# SESSION HANDOFF — 2026-08-01 (noche): 8C-inglés completo, SSR de las free tools, limpieza del blog

> Continúa `SESSION_HANDOFF_2026-08-01.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión larga desde el VPS, en modo UltraCode. **Seis commits de trabajo** (más los de documentación), todos pusheados y verificados en producción.

## ✅ Hecho y verificado EN PRODUCCIÓN

| Commit | Qué |
|---|---|
| `9960b1b` | 21 librerías de prompts en inglés + reparación del generador |
| `9e76f6a` | Un solo `<h1>` por página: 26 posts servían dos |
| `c80b148` | Las 5 librerías del molde WordPress antiguo → **26 de 26** |
| `ac83809` | **Las 119 páginas indexables de marketing pasan a SSR** |
| `c36d9ac` | Hub inglés `/en/prompt-libraries` |
| `216d0b3` | Los 2 glosarios delgados ampliados + fuera el CTA de newsletter y las donaciones de Jetpack |

Estado final medido contra el `dist` y contra `aichef.pro`:

- **1.121 URLs indexables y NINGUNA sin texto server-side** (antes: 119 con cero).
- **1.123 páginas con exactamente un `<h1>`, ninguna con dos.**
- Gate de las 26 librerías EN: **26/26 sin errores**.
- Gate de enlaces internos: **191 destinos, 0 rotos**.
- Build verde, 1.248 páginas.
- Los cinco gates del proyecto, en verde.

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

1. **El listado inglés completo de agentes**: los 77 nombres **y los nombres de los 15 módulos del
   menú**. Sin ellos el hub `/en/prompt-libraries` indexa solo las 26 con librería y no puede ser
   el catálogo completo como el español. **No se deduce del código**: es el error que ya costó
   cuatro correcciones.
2. **Dos glosarios ultradelgados sin tocar**: `token-unidad-inteligencia-artificial` con **49
   palabras** y `llm-large-language-model-cocina` con **78** — una frase de definición y un CTA.
   Son páginas indexadas prácticamente vacías. El pipeline de ampliación (`fase8d-ampliar-glosario.py`)
   ya está montado y probado con otros dos; van en una pasada cuando John lo diga.
3. **Alias de `enblog.aichef.pro` en Netlify + DNS** (`CUTOVER_ENBLOG_PENDIENTE.md`), con la
   trampa de las A records de Hostinger.

### Resueltas en esta sesión (estaban pendientes al empezar)

- ~~CTA de newsletter a 404~~ → quitado. Además de romper, afirmaba «+2.500 chefs ya reciben
  nuestro contenido exclusivo» sobre una newsletter que no existe: el formulario del pie está
  desconectado en el propio código.
- ~~Los 2 posts delgados~~ → ampliados con research previo (ver abajo).

## 📈 Los 2 glosarios ampliados: el research cambió el plan en uno

| | cocina molecular | food pairing |
|---|---|---|
| Volumen (DataForSEO) | **880/mes** | **590/mes** |
| GSC | 106 impresiones, pos. 66 | pos. 41 · **pos. 9** en «food pairing que es» |
| Riesgo | ninguno: una sola página compite | **canibalización** |
| Resultado | 352 → **1.437 palabras** | 421 → **938 palabras** |

Lo de food pairing era una trampa: existe un `manual-del-food-pairing` de **3.643 palabras** cuyo
primer `<h2>` es literalmente «¿Qué es el Food Pairing?», y aun así el glosario de 421 palabras
rankea **mejor que él**. Ampliarlo hasta artículo largo habría enfrentado las dos páginas por la
misma keyword. Se amplió como **página de definición**, cediendo la profundidad al manual con
enlace explícito.

La SERP mandó contenido concreto: `cocina molecular` tiene **AI Overview** (cada sección abre con
una respuesta citable) y su People Also Ask exigía cuatro cosas que no estaban — ejemplos, qué
ingredientes se usan, si es saludable y quién la creó.

Los dos **emiten ahora `FAQPage`**, que antes no hacían: su FAQ eran encabezados sueltos en el
cuerpo y ahora va en el frontmatter. Prosa con bridge.py, 4 imágenes con Nano Banana, 3 banners
por post y enlaces internos donde no había ninguno.

## 🧹 Tercer resto de WordPress: donaciones en 35 posts

Buscando el CTA apareció un bloque `wp-block-jetpack-donations` en **35 posts**: «Haz una donación
única / mensual / anual», con botones «Donar» que son enlaces **sin `href`**. Pidiendo donaciones
en el blog de un SaaS comercial y metiendo 105 encabezados falsos. Fuera, con gate propio.

Van ya **tres** familias de resto congelado del WordPress (relacionados, donaciones, CTA de
newsletter). Merece la pena asumir que habrá una cuarta y mirar con `grep` de `wp-block-` cuando
algo no cuadre.

## 🧭 Qué sigue

- Los ~58 agentes españoles sin librería (12 de ellos el bloque de hotelería).
- Las páginas por agente de 8C, que siguen sin arrancar.
- Vigilar en GSC el efecto de las 119 páginas que ahora sí tienen contenido indexable: es el cambio con más potencial de la sesión y hasta ahora no había nada que indexar en ellas.

## 🛠️ Gates nuevos (correr antes de dar nada por bueno)

```bash
python3 scripts/astro-migration/fase8c-libreria-en-gate.py --todos   # 26 librerías EN vs su original ES
python3 scripts/astro-migration/fase8c-h1-unico.py                   # un solo <h1> por página
python3 scripts/astro-migration/fase8c-quitar-relacionados.py        # widget de relacionados congelado
python3 scripts/astro-migration/fase8c-restos-wordpress.py           # donaciones Jetpack y otros restos
python3 scripts/astro-migration/fase8c-enlaces-vivos.py              # enlaces internos vs producción
```

Estado al cierre: **los cinco en verde**, y el de enlaces con **191 destinos y 0 rotos**.

## 📌 El patrón de mis propios errores, para no repetirlo

De los fallos de la sesión que fueron míos, **tres son el mismo**: usar un umbral de longitud como prueba de validez. Prompts de +40 caracteres descartaba `«Dame el escandallo de este plato»`; alts de +15 descartaba `"AI Chef Pro"`; respuestas de +200 rechazaba tandas de alts correctas. En los tres casos el validador bueno ya existía —**el recuento contra la fuente española**— y el umbral solo añadía falsos negativos que parecían fallos del modelo.

Y dos veces estuve a punto de publicar nombres inventados: una porque iba a derivar el `alt` de un fichero llamado `chef-diego-schattenhofer-78.jpg` (una persona real), y otra porque bridge se inventó los agentes «Line Cook», «Sous Chef» y «Pastry Chef» para el hub. **La fuente de los nombres es siempre el listado de la plataforma.**
