# SESSION HANDOFF — 2026-08-04: tanda 3 de 8D y el hub de prompts del footer

> Continúa `SESSION_HANDOFF_2026-08-02.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión desde el VPS. **1 commit** (`250b103`), pusheado y verificado en producción.

## ✅ Bloque 1 — Los cuatro glosarios del clúster de técnica

| Post | Antes | Ahora |
|---|---|---|
| `yuzu-kosho-condimento-japones-tendencia` | 226 pal. · 0 FAQ · 0 banners | **1.945** · 8 FAQ · 3 banners · 7 enlaces |
| `chili-crisp` *(slug nuevo)* | 268 pal. reales · 0 FAQ | **2.120** · 9 FAQ · 3 banners · 6 enlaces |
| `coccion-a-baja-temperatura-concepto-y-definicion` | 296 pal. reales | **2.686** · 11 FAQ · 3 banners · 8 enlaces |
| `sous-vide-concepto-definicion` *(pilar)* | 1.518 pal. · 0 banners | **2.277** · 12 FAQ · 3 banners · 8 enlaces |

Los cuatro con 2 tablas, ≥2 imágenes de cuerpo y destacada única que no se
repite. 8 imágenes nuevas en `astro-site/public/blog-assets/2026/08/`.

**`chile-crisp` → `chili-crisp`, y se cambia también la URL.** El término con i
son 480 búsquedas/mes en España frente a las 10 de la grafía con e. Cambiar el
slug salía **gratis** porque la URL migrada no tenía una sola fila en GSC; con
histórico habría habido que sopesarlo.

## ⚠️ Bloque 2 — La consolidación fue al post CONTRARIO del que decía el plan

El roadmap y la sesión anterior mandaban 301-ear
`tecnicas-de-coccion-al-vacio-sous-vide` con el argumento de que pierde
«**pos. 85,6 frente a 40,3**» contra el pilar.

**Las dos posiciones son de `blog.aichef.pro`**, el subdominio legacy ya
301-eado. Es exactamente la trampa que `CLAUDE.md` documenta desde
`mise-en-place`, y ha mordido por segunda vez. Las URLs **migradas** del clúster
suman **4 impresiones y 0 clics en 90 días**: no hay canibalización medible, así
que el motivo real de consolidar es estructural (tres páginas propias peleando
una keyword de 3.600/mes), no una posición.

Y comparando los encabezados uno a uno, el duplicado de verdad era otro:

- **`sous-vide-avanzado-concepto-y-definicion`** (1.521 pal.) es el mismo guion
  que el pilar (1.518 pal.) escrito por segunda vez, con otros encabezados y
  otros números. Se llama «avanzado» y no es más avanzado.
- **`tecnicas-de-coccion-al-vacio-sous-vide`** —el candidato del plan— resultó
  ser **el único con contenido que no está en ningún otro sitio**: la taxonomía
  LTLT / pasteurización / HTST / infusión / regeneración, y **dos infografías en
  PDF** (ES e EN, las dos sirviendo 200) que **no enlazaba nadie más en el
  sitio**. Se consolida igual, pero ambas cosas viajan al pilar antes de borrar
  nada.

Los dos van a `sous-vide-concepto-definicion` porque «sous vide» son 3.600
búsquedas/mes y «sous vide avanzado» no lo teclea nadie.

**Script hermano, no el de 8C.** `fase8d-consolidar-sousvide.py` existe porque
`fase8c-consolidar-301.py` **reescribe entero su bloque marcado** de
`_redirects`: cambiarle el MAPA habría borrado sus 24 reglas de julio sin un solo
aviso. El nuevo lleva su propia MARCA y **aborta si el pilar no ha absorbido ya**
la taxonomía, los errores comunes y los PDF (mecanismo `extra_final`, nuevo en
`fase8d-ampliar-glosario.py`).

## ✅ Bloque 3 — El hub de librerías de prompts en el footer (reportado por John)

**El bug:** el footer inglés llevaba a la **categoría del blog**
`prompt-library`, no al hub `/en/prompt-libraries`. Causa raíz: el hub sólo
estaba en la rama ES de `Footer.astro`, así que en inglés se caía de la lista y
**el hub quedaba huérfano — nada en todo el sitio lo enlazaba**.

- Nuevo helper **`promptHubHref(lang)`** en `astro-site/src/lib/blog.ts`, gemelo
  de `blogHubHref`: `/libreria-de-prompts` · `/en/prompt-libraries`, y los
  idiomas sin versión propia caen al ES.
- La categoría `prompt-library` **se excluye** de la lista del footer inglés:
  con el hub presente serían dos entradas contiguas homónimas apuntando a sitios
  distintos. Sigue accesible desde el propio blog.
- **Nombres unificados con la página de destino**, que era la otra mitad de lo
  que John señaló: «Librería de Prompts» en ES (decía «Biblioteca») y «Prompt
  Libraries» en EN (decía «Prompt Library»). **Sin cambiar URLs ni meter 301**:
  el slug `/libreria-de-prompts` ya era el correcto.
- Corregido también el gemelo `src/components/ModernFooter.tsx` de la SPA, que
  apuntaba a `/blog/categoria/libreria-de-prompts`. No se construye, pero es la
  referencia de paridad.

Los textos salen de `src/i18n/locales/*.json`: **la SPA es la fuente única**,
`astro-site/src/i18n/translations.ts` los importa por ruta relativa. No hay copia
que sincronizar.

## 🔍 La revisión adversarial devolvió 21 correcciones sobre contenido «terminado»

Los cinco que costaban dinero:

1. **Una fuente real citada diciendo lo que no dice.** El artículo del blog
   Umami Madrid «Esto no es yuzu kosho» existe, pero es una receta casera de un
   sustituto: **no denuncia nada** sobre los tarros comerciales. Se retira la
   atribución y se deja el hecho comprobable (la lista de ingredientes).
2. **Un `<a>` escapado imprimiéndose literal dentro de una tabla.**
   `html_tabla` escapa el HTML de las celdas, así que el enlace a roner salía
   como `<a href="…">roner</a>` en pantalla. **Ningún enlace puede ir dentro de
   una celda**; bridge los devuelve ahí de vez en cuando y el diff no canta.
3. **Contradicción técnica en la misma página:** la fila HTST listaba «pescados
   delicados» a 70-90 °C cuando su propia tabla de arriba los pone a 45-55 °C.
4. **Dos cifras de merma sin respaldo** (25-30 % / 10-15 %) que además
   contradecían la FAQ del artículo vecino, la cual sostiene que no existe cifra
   única. Sustituidas por «pesa tú la pieza».
5. **Las tablas de tiempos de los dos artículos discrepaban**, y los dos se
   enlazan mutuamente: carrilleras a 75 °C/8-12 h en uno y 65 °C/24-48 h en el
   otro, más muslo y verduras. Armonizadas, y las **dos rutas del colágeno**
   ahora se explican en ambos lados en vez de esconderse.

El resto: `imageAlt` heredado de WordPress que vendía el yuzu kosho como
«sriracha japonés» contra la tesis del propio artículo, una alegación de salud
sin fuente en una respuesta que alimenta el `FAQPage`, «Frio» sin tilde,
markdown sin procesar dentro de bloque HTML, aritmética (8/60 = 0,13 y no 0,15),
Fukuoka presentada como alternativa a Kyushu cuando **es** una de sus
prefecturas, y varias de lengua.

## Gates y verificación en producción

```
build                    1.246 páginas (eran 1.248; −2 consolidados)
fase8b-gate.py           3.528 checks · 0 fallos
fase8b-auditar-301.py    508 URLs · 0 rotos · 0 sin regla · 0 cadenas
fase8c-enlaces-vivos.py  204 destinos · 1 «roto» = el slug nuevo sin desplegar
fase8c-h1-unico.py       limpio     fase8c-restos-wordpress.py  limpio
fase8b-regen-lastmod.py  387 entradas
```

Y en vivo, 120 s después del push:

```
/blog/chili-crisp                                200
/blog/sous-vide-concepto-definicion              200
/en/prompt-libraries                             200   footer EN → «Prompt Libraries»
/libreria-de-prompts                             200   footer ES → «Librería de Prompts»
/blog/chile-crisp-condimento-viral-2026          301 → /blog/chili-crisp
/blog/sous-vide-avanzado-concepto-y-definicion   301 → /blog/sous-vide-concepto-definicion
/blog/tecnicas-de-coccion-al-vacio-sous-vide     301 → /blog/sous-vide-concepto-definicion
```

## 📌 Pendiente de John (sin cambios)

- **`enblog.aichef.pro`**: alias en Netlify + DNS. Las reglas 301 ya están en
  `_redirects` pero no se ejecutan hasta entonces. Trampa de las A records de
  Hostinger y batería de verificación en `CUTOVER_ENBLOG_PENDIENTE.md`.
- **Listado inglés de agentes** para poder exponer públicamente los nuevos.
- Borrar las dos cuentas `test-gads-*@mailinator.com` y vaciar el campo de
  confirmación antiguo de Pickaxe.
