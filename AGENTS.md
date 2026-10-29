# AGENTS.md

## Fechas evergreen: `{year}` y `{month}` (obligatorio)

En el contenido evergreen de las landings públicas, el año y el mes de title, meta description, H1, `og:title`, `twitter:title` y `headline` de JSON-LD se escriben con placeholder. No se clavan a un año natural.

El sitio es Astro. El build sustituye los tokens con la fecha de **Europe/Madrid** (`Intl.DateTimeFormat`, `timeZone: 'Europe/Madrid'`). El mes sale en el idioma de la página (`es`, `en`, `fr`, `de`, `it`, `pt`, `nl`). Si el literal `{year}` o `{month}` sigue en uno de esos campos del HTML, el build falla.

| Token | Qué escribe el build |
|---|---|
| `{year}` | Año civil en Madrid. El 31 dic 23:30 UTC ya es 1 de enero. |
| `{month}` | Nombre del mes en el idioma de la página (`enero`, `January`, `janvier`…). |

Solo valen esos dos tokens, en minúsculas y sin espacios. `{Year}`, `{ year }` y `{yearly}` no se tocan. Tampoco se reescriben años ya escritos, precios, normas (`RD 1420/2006`), fechas ISO ni hitos (`desde 2010`).

En un `.astro`, `{year}` suelto es una variable. El token tiene que ir dentro de un string: `title="Guía {year}"`, `const title = 'Guía {year}'` o `<h1>{'Guía {year}'}</h1>`. En JSON de i18n y en el frontmatter del blog es texto normal.

La función es `resolveDatePlaceholders(str, now?)` en `astro-site/src/lib/date-placeholders.mjs`. El tercer argumento opcional es el idioma. `BaseLayout` y el layout del blog la aplican al render. Un pase al final de `astro build` cubre el H1 y el `headline` que no pasan por ahí. La edge function `netlify/edge-functions/og-meta.ts` usa la misma función al montar su HTML; no está declarada en `netlify.toml` desde el cutover.

```sh
cd astro-site && npm test
node scripts/astro-migration/auditar-anos-fijos.mjs
```

La auditoría solo lista. No migra títulos ni cambia precios.
