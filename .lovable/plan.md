

# Plan: Actualizar Precio del Plan Anual

## Problema Actual

El plan Premium Plus Anual a 500€ no tiene coherencia con el Premium Max de 95€/mes:
- 95€ x 12 meses = 1.140€
- El plan anual a 500€ representa un ahorro de 640€ (casi 7 meses gratis)

## Nueva Estructura de Precios

| Concepto | Valor Actual | Nuevo Valor |
|----------|--------------|-------------|
| Precio anual | 500€ | **950€** |
| Precio original (tachado) | 600€ | **1.140€** |
| Badge de ahorro | "Ahorra 100€" | **"Ahorra 2 meses"** |
| Descripcion del ahorro | - | **"Equivalente a 190€"** (opcional en descripcion) |

## Cambios por Idioma

### Espanol (es.json)
- `price`: "500€" → "950€"
- `original_price`: "600€" → "1.140€"
- `discount`: "Ahorra 100€" → "Ahorra 2 meses"

### English (en.json)
- `price`: "€500" → "€950"
- `original_price`: "€600" → "€1,140"
- `discount`: "Save €100" → "Save 2 months"

### Francais (fr.json)
- `price`: "500€" → "950€"
- `original_price`: "600€" → "1.140€"
- `discount`: "Économisez 100€" → "Économisez 2 mois"

### Deutsch (de.json)
- `price`: "500€" → "950€"
- `original_price`: "600€" → "1.140€"
- `discount`: "Sparen Sie 100€" → "Sparen Sie 2 Monate"

### Italiano (it.json)
- `price`: "500€" → "950€"
- `original_price`: "600€" → "1.140€"
- `discount`: "Risparmia 100€" → "Risparmia 2 mesi"

### Portugues (pt.json)
- `price`: "500€" → "950€"
- `original_price`: "600€" → "1.140€"
- `discount`: "Poupe 100€" → "Poupe 2 meses"

### Nederlands (nl.json)
- `price`: "€500" → "€950"
- `original_price`: "€600" → "€1.140"
- `discount`: "Bespaar €100" → "Bespaar 2 maanden"

---

## Archivos a Modificar

1. `src/i18n/locales/es.json`
2. `src/i18n/locales/en.json`
3. `src/i18n/locales/fr.json`
4. `src/i18n/locales/de.json`
5. `src/i18n/locales/it.json`
6. `src/i18n/locales/pt.json`
7. `src/i18n/locales/nl.json`

---

## Resultado Visual Esperado

```text
+---------------------------+
|      Ahorra 2 meses       |  <- Badge verde
+---------------------------+
| AI Chef Premium Plus Anual|
|          1.140€           |  <- Precio tachado
|         950€/año          |  <- Precio real
|         USOS: ∞           |
+---------------------------+
| ✓ 55+ herramientas        |
| ✓ Uso ilimitado todo año  |
| ✓ Cocinas del mundo       |
| ✓ Herramientas negocio    |
| ✓ Soporte 24/7            |
| ✓ Consultoría mensual     |
+---------------------------+
```

El mensaje ahora es claro: **"Paga 10 meses, llévate 12"** (ahorro de 2 meses = 190€)

