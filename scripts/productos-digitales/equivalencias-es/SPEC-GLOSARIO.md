# SPEC del glosario — variantes de cada término de España por país

> Sesión Claude Code, 13-oct-2026. Plan en `PLAN.md`; términos en `terminos.json` (206, elegidos sobre el vocabulario
> real de los 51 productos); qué productos usa cada uno en `datos/matriz.json`.

## Para qué

Cada producto lleva una tabla «tu producto en tu país»: el término de España que usa el producto → cómo lo dice **un
profesional de hostelería** (cocinero, camarero, dueño, gestor) en cada país. No es un diccionario: es la palabra que
se oye en una cocina, se escribe en una comanda o se busca en Google en ese país.

## Países (21 códigos)

MX GT HN SV NI CR PA CU DO PR CO VE EC PE BO CL AR UY PY US BR
(US = hispanohablantes de EE. UU.; BR = Brasil, se da el término **en portugués** con `"pt": true`.)

## Formato: `glosario/<lote>.json` = lista de objetos

```json
{
  "id": "camarero",
  "es": "camarero, camarera",
  "variantes": [
    {"termino": "mesero, mesera", "paises": ["MX","GT","HN","SV","NI","CR","PA","CO","VE","EC","DO","PR","US"]},
    {"termino": "mozo, moza", "paises": ["AR","UY","PY","PE","BO"]},
    {"termino": "garzón, garzona", "paises": ["CL"]},
    {"termino": "garçom", "paises": ["BR"], "pt": true}
  ],
  "igual": ["CU"],
  "nota": "En EE. UU. el personal bilingüe también dice «server».",
  "confianza": "alta",
  "evidencia": ["DataForSEO MX «mesero» 8.100/mes", "DataForSEO CL SERP «garzón» = oficio"]
}
```

- `id` y `es`: copiados tal cual de `terminos.json`.
- **Cobertura obligatoria:** los 21 países aparecen exactamente una vez, en una `variantes[].paises` o en `igual`
  (países donde el término de España es también el habitual). Un país puede ir en dos variantes solo si de verdad
  conviven: entonces ponlo en ambas (la primera es la más usada) y explícalo en `nota`.
- Máximo 3 variantes en español + 1 de BR. La variante más extendida, primero.
- `nota` (opcional, ≤ 25 palabras): falsos amigos y matices («tortilla» en México es la de maíz: la de patata es
  «tortilla española»; «tostada» en México es una tortilla frita).
- `confianza`: `alta` (uso profesional seguro o medido) · `media` (país pequeño asimilado al uso regional).
- `evidencia` (opcional): lo que comprobaste con DataForSEO o la SERP.

## Método

1. Conocimiento propio del uso profesional regional, **país a país** (no hay un «término latinoamericano»: Argentina y
   Chile dicen «escandallo», México «receta estándar» o «costeo de recetas»).
2. **Comprueba con datos al menos 25 términos dudosos** con `scripts/dataforseo.py` (desde la raíz del worktree):
   `python3 scripts/dataforseo.py vol "kw1" "kw2" … --pais <código> --idioma es` (varias keywords por llamada).
   Códigos: MX 2484 · CO 2170 · AR 2032 · CL 2152 · PE 2604 · US 2840 · VE 2862 · EC 2218 · DO 2214 · GT 2320 ·
   CR 2188 · UY 2858 · BO 2068 · PY 2600 · PA 2591 · HN 2340 · SV 2222 · NI 2558 · PR 2630 · BR 2076 (`--idioma pt`).
   **El volumen no es la intención**: «garzón» da 18.100 en Colombia porque es un municipio y un apellido. Ante la
   duda, `python3 scripts/dataforseo.py serp "kw" --pais <código> --idioma es`. Tope: ~40 llamadas por agente (cuestan
   dinero).
3. No escribas fuera de `glosario/`. No hagas commit ni push. Valida con `python3 -m json.tool` y con un script de
   cobertura (21 países por término).
