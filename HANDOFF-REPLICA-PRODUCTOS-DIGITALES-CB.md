# HANDOFF — Réplica en AI Chef Pro del trabajo de productos digitales de ChefBusiness

> **Para el Claude Code que trabaje en este repo (chefpro-modernize).**
> Escrito el 2026-08-08 desde el proyecto `~/chefbusiness-astro`, donde este trabajo ya está hecho y desplegado.
> Este handoff es la guía a medida para AICP. El roadmap completo del área (estado por producto de CB,
> bugs sistémicos, método) vive en el OTRO proyecto: `~/chefbusiness-astro/PRODUCTOS-DIGITALES-ROADMAP.md`
> — consultarlo allí si hace falta contexto; los dos proyectos no se mezclan.

## Qué hay que replicar aquí

Los productos digitales de aichef.pro comparten origen con los de chefbusiness.co:
**los 6 DOCX con texto corrupto CJK son byte-idénticos** entre ambas tiendas, y el stack es el mismo
(config de productos, dashboards React, funciones Netlify, `/dl`). Todo lo diagnosticado y reparado
en CB aplica aquí producto a producto.

**Orden acordado con John: terminar ChefBusiness primero, luego portar.** No arrancar la réplica
sin confirmar con él que CB está cerrado (a 2026-08-08 en CB quedan los financieros de food-truck,
tapas-bar, panadería y coctelería, más 26 productos por revisar).

## Diferencias de marca AICP (innegociables)

1. **Banners de cross-sell en dashboards: SOLO Miselup + Timlup.** NUNCA autorreferenciar AI Chef Pro.
2. **Branding interno de los entregables**: metadata `creator`/`company` = AI Chef Pro (no ChefBusiness),
   y revisar que ningún Excel/DOCX portado mencione la otra marca.
3. Paleta, componentes y rutas de ESTE repo — no copiar estilos de CB a ciegas.

## Herramientas listas para copiar desde `~/chefbusiness-astro`

| Herramienta | Ruta en chefbusiness-astro | Para qué |
|---|---|---|
| `inject_cache.py` | `scripts/` | Fix del Excel-en-blanco (pycel inyecta el cache de valores). SIEMPRE al final, tras el último save |
| `mapa-tildes-es.json` (405 entradas) | `scripts/` | Corrección determinista de ortografía ASCII |
| `aplicar-fixes-literales.py` | `scripts/` | Aplicador run-aware de reemplazos en DOCX/XLSX |
| **Generador financiero cafetería v2.0** | `scripts/productos-digitales/generate_cafeteria_financiero_v2.py` | **El patrón**: 171 fórmulas encadenadas, PE dual, parámetro único |
| **Modelo maestro cafetería** | `scripts/productos-digitales/modelo-cafeteria-v2.json` | Fuente única de cifras; adaptar branding y regenerar |

Pipeline por producto: modelo maestro único → generador → `inject_cache.py` → verificar abriendo
`data_only=True` (los valores DEBEN verse; contar fórmulas no basta) → auditoría adversarial → deploy → verificación LIVE.

## Lecciones que costaron caras (no repetir)

- **Auditoría adversarial multi-lente ANTES de dar OK**: en la cafetería de CB, incluso después de un
  gate aritmético perfecto, 4 lentes escépticas cazaron 62 hallazgos (parámetros duplicados sin cablear,
  break-even sin amortización, promesas de la landing que el fichero no cumplía, notas internas de
  reconstrucción visibles al cliente, DOCX declarado en inglés).
- **Las notas internas de construcción NUNCA van al entregable** (nada de "el Excel original decía…").
- **DOCX**: idioma `es-ES` en styles.xml/settings.xml (si no, Word subraya todo en rojo), metadatos de
  marca, pie de página, y cero placeholders tipo "[Contenido pendiente de generación]".
- **Excel**: break-evens con ROUNDUP (nunca ROUND), IFERROR en divisores editables, parámetros únicos
  cableados por fórmula entre hojas, formatos de número coherentes, números nunca como fecha (bug K),
  fila de holgura dentro de los SUM.
- **Landing/dashboard**: no prometer secciones que no existen, testimonios sin cifras que haya que
  sincronizar, FAQ honesta sobre qué recalcula y qué no.
- **Cualquier `wb.save()` de openpyxl BORRA el cache** → re-ejecutar `inject_cache.py` después.

## Referencias completas

- Roadmap del área (en el proyecto CB, no aquí): `~/chefbusiness-astro/PRODUCTOS-DIGITALES-ROADMAP.md`
- Memoria del proyecto CB: `runbook-reconstruccion-producto-digital`,
  `handoff-2026-07-22-reconstruccion-productos-digitales`, `feedback-openpyxl-cache-valores-excel`,
  `feedback-procedimiento-port-aicp-cb` (procedimiento canónico de porte entre marcas, 10 artefactos)
