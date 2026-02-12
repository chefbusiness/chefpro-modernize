
# Plan: Contador Dinamico de Soluciones Generadas

## Concepto

Convertir el numero estatico "48.149" en un contador que crece automaticamente cada dia, sumando entre 60 y 80 unidades diarias de forma determinista (mismo numero para todos los visitantes en el mismo dia).

## Logica

Se usara una fecha base (12 de febrero de 2026) con el valor inicial de 48.149. Cada dia transcurrido desde esa fecha sumara una cantidad pseudo-aleatoria determinista entre 60 y 80, calculada a partir del dia del ano (para que todos los usuarios vean el mismo numero en el mismo dia).

```
Fecha base: 2026-02-12
Valor base: 48.149
Por cada dia transcurrido: +60 a +80 (seeded por fecha)
```

Ejemplo: el 13 de febrero mostraria ~48.219, el 14 ~48.289, etc.

## Cambios

### Archivo: `src/components/HeroSocialProof.tsx`

Agregar una funcion `getDynamicCount()` que:

1. Calcula los dias transcurridos desde la fecha base (2026-02-12)
2. Para cada dia, genera un incremento determinista entre 60 y 80 usando un hash simple del dia
3. Suma todos los incrementos al valor base (48149)
4. Reemplaza el `formatNumber(48149)` estatico por `formatNumber(getDynamicCount())`

### Seccion tecnica

```typescript
function getDynamicCount(): number {
  const BASE_DATE = new Date('2026-02-12');
  const BASE_COUNT = 48149;
  const today = new Date();
  
  // Dias transcurridos
  const diffTime = today.getTime() - BASE_DATE.getTime();
  const diffDays = Math.max(0, Math.floor(diffTime / (1000 * 60 * 60 * 24)));
  
  // Sumar incremento determinista por cada dia
  let total = BASE_COUNT;
  for (let i = 1; i <= diffDays; i++) {
    // Seed basado en el dia para que sea consistente
    const seed = (i * 7 + 13) % 21; // genera 0-20
    const dailyIncrement = 60 + seed; // rango 60-80
    total += dailyIncrement;
  }
  
  return total;
}
```

No se requiere base de datos ni backend: el calculo es puramente frontend y determinista (todos los visitantes ven el mismo numero el mismo dia).
