

# Plan: Corregir Paginas Legales en Todos los Idiomas

## Problema

Las 4 paginas legales (Legal, Privacy, Terms, Cookies) muestran las claves de traduccion en crudo (ej: "pages.terms.heading") en lugar del contenido real. Esto ocurre porque los archivos de traduccion solo tienen las claves SEO (`seo_title`, `seo_description`, `seo_keywords`) pero faltan las claves `heading` y `content_paragraphs` que los componentes intentan renderizar.

Ademas, en `es.json` hay una clave `"pages"` duplicada (lineas 680 y 1151), lo que causa que la segunda sobreescriba la primera en JSON.

## Cambios a Realizar

### 1. Corregir clave duplicada en `es.json`

Fusionar las dos claves `"pages"` en una sola para evitar perdida de datos (la seccion de mentoria en linea 680 se pierde actualmente).

### 2. Agregar contenido legal a los 7 archivos de idioma

Para cada idioma (es, en, fr, de, it, pt, nl), agregar dentro de `pages.legal`, `pages.privacy`, `pages.terms` y `pages.cookies`:

```json
{
  "heading": "Titulo de la pagina",
  "content_paragraphs": [
    "Parrafo 1 con contenido legal...",
    "Parrafo 2...",
    "Parrafo 3..."
  ]
}
```

### 3. Contenido por pagina

#### Legal (Aviso Legal)
- Identificacion del titular (AI Chef Pro / Chefbusiness Consulting SL)
- Domicilio social, CIF, datos de contacto
- Propiedad intelectual
- Legislacion aplicable

#### Privacidad (Politica de Privacidad)
- Responsable del tratamiento
- Datos recogidos y finalidad
- Base legal (RGPD)
- Derechos del usuario (acceso, rectificacion, supresion)
- Periodo de conservacion
- Contacto DPO

#### Terminos (Terminos de Servicio)
- Aceptacion de condiciones
- Descripcion del servicio
- Planes y suscripciones
- Cancelacion y reembolsos
- Limitacion de responsabilidad
- Modificaciones

#### Cookies (Politica de Cookies)
- Que son las cookies
- Tipos utilizadas (necesarias, analiticas, marketing)
- Como gestionar cookies
- Cookies de terceros

### 4. Archivos a modificar

| Archivo | Cambio |
|---------|--------|
| `src/i18n/locales/es.json` | Fusionar `pages` duplicado + agregar heading/content_paragraphs a legal, privacy, terms, cookies |
| `src/i18n/locales/en.json` | Agregar heading/content_paragraphs (en ingles) |
| `src/i18n/locales/fr.json` | Agregar heading/content_paragraphs (en frances) |
| `src/i18n/locales/de.json` | Agregar heading/content_paragraphs (en aleman) |
| `src/i18n/locales/it.json` | Agregar heading/content_paragraphs (en italiano) |
| `src/i18n/locales/pt.json` | Agregar heading/content_paragraphs (en portugues) |
| `src/i18n/locales/nl.json` | Agregar heading/content_paragraphs (en holandes) |

### 5. Sin cambios en componentes

Los componentes `Legal.tsx`, `Privacy.tsx`, `Terms.tsx` y `Cookies.tsx` ya estan correctamente implementados -- solo falta el contenido en los JSON de traduccion.

## Resultado

Las 4 paginas legales mostraran contenido real traducido profesionalmente en los 7 idiomas, con informacion legal apropiada para una plataforma SaaS con sede en Espana (cumplimiento RGPD/LSSI).

