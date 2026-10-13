# SPEC del generador — `build_guia_es.py` (F2)

> Sesión Claude Code, 13-oct-2026. Plan en `PLAN.md`. Solo agentes sonnet/haiku (John).

## Entradas (todas en esta carpeta salvo indicación)

| Fichero | Qué aporta |
|---|---|
| `fichas/*.json` (20) | Ficha por país: 13 campos `{texto, fuentes[{titulo,url,tipo}], verificado}` + `trampas[]` (SPEC-FICHAS.md) |
| `glosario/A.json` + `glosario/B.json` | 206 términos: `{id, es, variantes[{termino, paises[], pt?}], igual[], nota, confianza}` (SPEC-GLOSARIO.md) |
| `terminos.json` | `{id, es, tema, patrones, comun}` |
| `datos/matriz.json` | `productos[slug].terminos[id] = apariciones` en los entregables del producto |
| `textos.json` | Textos fijos (los escribe un redactor; ver abajo) |
| `../../../astro-site/src/lib/zona-app.ts` | `productLabel` de cada producto (nombre en portada) |
| `censo-terminos-es.py` | Registro de los 51 productos ES y sus ficheros (reutilizar sus funciones con `importlib`, no duplicar) |

## Tipo de producto (decide la nota de la sección 1)

`kit_tareas` = `kit-tareas*` + `mega-pack-tareas` · `kit_excel` = `kit-escandallos`, `pack-appcc`,
`kit-gestion-personal`, `kit-inventario`, `kit-plan-financiero` · `plan_negocio` = `plan-*` · `guia_manual` = `guia-*`,
`manual-*` · `ebook` = `pro-prompts-ebook`.

## Salida

Un docx por producto: `astro-site/public/dl/<carpeta>/guia-equivalencias-<slug>.docx`, donde `<carpeta>` es la carpeta
de `dl/` donde están la mayoría de los ficheros del producto. Excepciones: `mega-pack-tareas` →
`dl/mega-pack-tareas/` (nueva) y `pro-prompts-ebook` → `dl/pro-prompts-ebook/` (nueva).

Flags: `--only slug1,slug2` (pruebas), `--check` (gates sobre lo generado), `--out-root` (por defecto `astro-site/public/dl`).

## Formato

Copiar el enfoque de `../equivalents-guide/build_guide.py` (EN): abrir una plantilla docx de un producto ES
(`astro-site/public/dl/guia-food-cost-ingenieria-menu/guia-food-cost-ingenieria-menu.docx` o el plan de
`plan-negocio-bar-restaurante`), vaciar el cuerpo y conservar estilos, tamaño Letter y márgenes; fuentes Georgia
(títulos) y Calibri (texto); `core_properties.language = 'es-419'`, `title`, `subject`, `category = 'Guía bonus'`.
Tablas con cabecera sombreada en negro #111 y texto dorado #FFD700 o el estilo de tabla de la plantilla; nada de marrón.
Enlaces con hipervínculo real (`[texto](url)` en los textos → hyperlink de Word, como `rich()` en el EN).

## Estructura del documento

0. **Portada**: kicker «BONUS · AI Chef Pro» · título «Guía de Equivalencias para tu país» · subtítulo
   «<productLabel> · España ↔ Hispanoamérica, EE. UU. y Brasil» · «Incluida con tu <productLabel>» · «Edición octubre
   2026» · autor «John Guerrero, consultor gastronómico» enlazado a https://johnguerrero.es.
1. **Cómo usar esta guía** (`textos.como_usar`) + **Aviso** (`textos.aviso`) + leyenda de códigos de país (tabla
   compacta código → país, 21 filas en 2-3 columnas).
2. **«1. Tu <productLabel> en tu país»**: `textos.nota_tipo[<tipo>]` + tabla de los términos con apariciones ≥ 1 en
   `matriz.productos[slug]`, **agrupados por tema** (subtítulo con el nombre humano del tema) y, dentro, ordenados por
   apariciones desc. Columnas: «En el producto (España)» · «Cómo se dice en tu país» · «Ojo con». Celda central:
   variantes como `mesero (MX, GT, HN…) · mozo (AR, UY, PY, PE, BO) · garzón (CL)`, luego `igual que en España: CU` si
   `igual` no está vacío, y la variante BR al final como `Brasil (pt): garçom`. Celda «Ojo con» = `nota` (vacía si no hay).
3. **«2. Otros términos que te encontrarás»**: los términos `comun: true` que NO estén ya en la sección 1, misma tabla.
4. **«3. Medidas y unidades»**: `textos.medidas_intro` + tabla `textos.conversiones` + remisión a la ficha de cada país.
5. **«4. Tu país, en una página»**: las 20 fichas por orden alfabético del nombre del país, **cada una en página
   nueva**: H2 con el país + línea «Moneda: … · Datos consultados en oct-2026»; tabla de 2 columnas (tema humano · texto)
   con los 13 campos en este orden: impuesto_consumo, propina_servicio, autoridad_sanitaria, manipulador,
   licencias_apertura, alcohol, forma_juridica, laboral, unidades_mercado, pagos_delivery, apoyos_emprendimiento,
   tipos_local, adaptar_productos. Si un campo legal (los 8 primeros + laboral + apoyos) tiene `verificado: false`,
   añadir en cursiva «Orientativo: confírmalo con la autoridad local.» Debajo, «Falsos amigos» (viñetas con `trampas`)
   y «Fuentes» (lista de enlaces únicos de la ficha, letra pequeña).
6. **«5. ¿Lo adaptamos por ti?»**: `textos.cta` con mailto:info@aichef.pro, https://aichef.pro/productos-digitales y
   https://johnguerrero.es.

Pie de página con «Guía de Equivalencias · <productLabel> · aichef.pro» y número de página.

## `textos.json` (lo escribe un redactor sonnet)

Claves: `como_usar`, `aviso`, `nota_tipo` {kit_tareas, kit_excel, plan_negocio, guia_manual, ebook}, `temas`
(id → nombre humano de los 9 temas), `campos` (id → nombre humano de los 13 campos), `medidas_intro`, `conversiones`
(`head` + `rows`), `cta`, y para la F3: `bonus_landing` {title, value, desc}, `dashboard_card` {title, desc},
`faq_landing` {q, a_plantilla con `{producto}` y `{ejemplos}`} y `email` (asunto + cuerpo corto del broadcast).

## Gates (`--check`)

- Los 51 docx existen, abren con python-docx y pesan > 25 KB.
- Caracteres: solo latinos (se permiten ñ, tildes, ü, ç, ã, õ, ê, «», –, —, ·, ↔, °, ², ×, €, $). Reutilizar la lógica
  de `../gate-no-latinos.py`.
- Enlaces presentes: https://johnguerrero.es, mailto:info@aichef.pro, https://aichef.pro/productos-digitales.
- Sección 1: ≥ 5 términos, y cada término mostrado tiene apariciones ≥ 1 en ese producto.
- Las 20 fichas presentes (busca el nombre de cada país en el texto).
- Sin «vosotros», «os » ni voseo en los textos fijos.
- Estimación de páginas (como el EN) e informe por producto: nº de términos de la sección 1, páginas.
