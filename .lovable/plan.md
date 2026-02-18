
# Plan: Cambiar de 2 a 5 usos gratis en el plan AI Chef Miembro

## Cambio

Actualizar el plan gratuito "AI Chef Miembro" de **2 usos/mes** a **5 usos/mes** en los 7 archivos de idioma.

## Dos campos a modificar por idioma

En cada archivo de idioma, se cambian exactamente 2 valores dentro de `pricing.plans.member`:

1. **`uses`** - el texto que aparece junto a "USOS:"
2. **`features.1`** - la linea de creditos mensuales en la lista de caracteristicas

| Idioma | Archivo | `uses` actual -> nuevo | `features.1` actual -> nuevo |
|--------|---------|----------------------|------------------------------|
| ES | es.json | "2/mes" -> "5/mes" | "2 creditos mensuales" -> "5 creditos mensuales" |
| EN | en.json | "2/month" -> "5/month" | "2 monthly credits" -> "5 monthly credits" |
| FR | fr.json | "2/mois" -> "5/mois" | "2 credits mensuels" -> "5 credits mensuels" |
| DE | de.json | "2/Monat" -> "5/Monat" | "2 monatliche Credits" -> "5 monatliche Credits" |
| IT | it.json | "2/mese" -> "5/mese" | "2 crediti mensili" -> "5 crediti mensili" |
| PT | pt.json | "2/mes" -> "5/mes" | "2 creditos mensais" -> "5 creditos mensais" |
| NL | nl.json | "2/maand" -> "5/maand" | "2 maandelijkse credits" -> "5 maandelijkse credits" |

No se requieren cambios en componentes ni logica -- solo datos de traduccion.
