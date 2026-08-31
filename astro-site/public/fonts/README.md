# TwemojiCountryFlags.woff2

Subconjunto de **Twemoji** con los glifos de banderas de país (261 ligaduras de
pares de indicadores regionales + las secuencias de subdivisión). 78 KB.

**Por qué está aquí:** Windows no incluye glifos de banderas en Segoe UI Emoji,
así que Chrome/Edge/Firefox sobre Windows pintan las dos LETRAS ISO ("DE", "ES")
en lugar de la bandera. Afecta a 1.023 páginas del sitio (recetarios del mundo,
selector de idioma, avisos de conversión, strips de ciudades).

Se declara en `src/styles/global.css` con `unicode-range` acotado a los 37
codepoints que cubre, y con `local()` delante para que macOS/iOS y Android/Linux
sigan usando su emoji nativo sin descargar nada.

- Origen: https://github.com/mozilla/twemoji-colr (paquete `country-flag-emoji-polyfill`)
- Gráficos: Twemoji © Twitter, Inc y colaboradores — **CC-BY 4.0**
- Código del font: MIT
