# Nota para el carril Cursor (landings comerciales, SEO y blog) — Plan de Negocio: Heladería Artesanal

> Sesión Claude Code (carril Mac, productos digitales), 25-oct-2026. Reparto de carriles del 24-oct: estas piezas son de
> Cursor y NO se tocan desde el carril de productos. Hacerlas cuando `/plan-negocio-heladeria` esté LIVE (se avisará en el
> handoff del producto).

## 1. Interenlazado (cero huérfanas)

- Añadir `plan-negocio-heladeria` a los `productIds` de las tres páginas `/usos/` de heladería:
  - `maestro-heladero` → `src/data/use-cases-content.es.ts` (≈ l. 1924)
  - `heladeria` → `src/data/use-cases-content.es.ts` (≈ l. 3138)
  - `heladero-consultor` → `src/data/use-cases-content.es.consultor.ts` (≈ l. 273)
- Enlace contextual al plan desde los tres posts ES del blog: `innovacion-en-heladeria-aplicaciones-practicas-de-chatgpt`,
  `libreria-de-prompts-para-heladeria-creativa-ai`, `libreria-de-prompts-para-heladero-consultor-pro-ai` (banner de producto o
  frase con enlace, según la skill `blog-aichef`).

## 2. Frase que contradice al producto (corregir SOLO esa frase, en los 7 idiomas)

La FAQ 2 de `heladero-consultor` (`src/data/use-cases-content.es.consultor.ts` y sus gemelas por idioma) afirma «rentabilidad
neta del 12-22 %… diversifican… 28-35 %» y «márgenes brutos del 70-80 %». El caso del plan, con la tesorería de invierno, da un
**neto del ≈ 5-6 % a régimen** (research: `scripts/productos-digitales/plan-heladeria/F1-research-heladeria.md` §3). Propuesta:
«un neto de un dígito alto si el invierno se trabaja bien; la estacionalidad (noviembre-febrero deja ≈ 15 % de las ventas) es
lo que decide». La cifra de inversión de su FAQ 1 (60.000-180.000 €) es coherente y se queda.
