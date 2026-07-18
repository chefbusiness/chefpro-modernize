# Gates de la migración Astro — verificación reutilizable

Scripts de verificación usados para cerrar las Fases 2-4 de la migración (ver `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8). Persistidos aquí porque `/private/tmp` **se borra en cada reinicio** (aprendido con los apagones térmicos del 2026-07-18).

Todos son **solo `curl` + `python3`** (red, no CPU — compatibles con la regla térmica). Staging: `https://aichef-astro-staging.netlify.app`.

## Uso

```bash
# 1) Regenerar inputs (listas de URLs desde public/sitemap.xml + payment links desde la API de Netlify — requiere netlify CLI autenticado):
./prepare-inputs.sh

# 2) Ejecutar el gate que toque:
./gates-fase2-use-cases.sh    # espera deploy + barrido 441 URLs use cases + muestra profunda
./gates-fase2-full-441.sh     # criterio de aceptación F2: title/desc/canonical/H1/FAQPage/hreflang en las 441
./gates-fase3-pseo.sh         # 76 URLs pSEO: schemas Service/FAQPage/CollectionPage/Breadcrumb + hreflang=2
./gates-fase4-productos.sh    # ACEPTACIÓN F4: 44 landings con CTA byte-idéntico al payment link real + hub QA 44/44
./smoke-hotfix-functions.sh   # smoke de las 4 netlify functions de productos en PRODUCCIÓN (hotfix 7ab25b7)
```

- `stripe-env-vars.json` (generado, **gitignored**): payment links reales por env var. El gate F4 compara el `href` renderizado en staging contra estos valores — es el check de DINERO.
- Los scripts esperan al deploy ellos solos (poll 60s, timeout 25 min) y salen con exit 1 si algo falla.
- Al añadir el **producto 45**: añadir su env var en producción **Y en staging** (scope builds), añadirlo a los mapas de las 4 netlify functions (Bug #5 de la doctrina), y re-correr `gates-fase4-productos.sh`.
