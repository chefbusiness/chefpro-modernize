
# Plan: Actualizacion de Planes de Precios

## Resumen de Cambios

Segun la captura de app.aichef.pro, los planes han cambiado significativamente:

### Planes Actuales vs Nuevos

```text
ANTES (6 planes)                    AHORA (5 planes)
-----------------                   ----------------
1. Member (Gratis)                  1. AI Chef Miembro (Gratis, 2 usos/mes)
2. Pro (10 EUR/mes)                    [ELIMINADO]
3. Premium (15 EUR/mes)                [ELIMINADO]  
4. Premium Pro (25 EUR/mes)         2. AI Chef Premium Pro (25 EUR/mes, 150 usos/mes)
5. Premium Plus (50 EUR/mes)        3. AI Chef Premium Plus (50 EUR/mes, 350 usos/mes)
   [NO EXISTIA]                     4. AI Chef Premium Max (95 EUR/mes, ilimitado) [NUEVO]
6. Premium Plus Anual (500 EUR/ano) 5. AI Chef Premium Plus Anual (500 EUR/ano, ilimitado)
```

### Detalles de Cada Plan (segun captura)

**1. AI Chef Miembro (Gratis)**
- 2 creditos/mes
- Descripcion: "Prueba gratis con 2 creditos al mes todas las herramientas culinarias mas avanzadas impulsadas por IA para mejorar considerablemente tu rendimiento profesional en cualquier cocina, en cualquier parte del mundo. Ideal y recomendado para ayudantes de cocina, cocineros y jefes de partida."

**2. AI Chef Premium Pro (25 EUR/mes)**
- 150 creditos/mes
- Descripcion: "Ideal y recomendado para Chefs de Cocina, Chefs Ejecutivos, Chefs Corporativos, Directivos en Direccion Gastronomica, Gerentes de Restaurantes y Emprendedores Gastronomicos."

**3. AI Chef Premium Plus (50 EUR/mes)** - MAS POPULAR
- 350 creditos/mes
- Similar descripcion orientada a chefs profesionales

**4. AI Chef Premium Max (95 EUR/mes)** - NUEVO
- Uso ilimitado
- Descripcion: "Este es nuestro plan Premium Max, que incluye todas las herramientas desarrolladas por AI Chef Pro con uso ilimitado mensual."

**5. AI Chef Premium Plus Anual (500 EUR/ano)**
- Uso ilimitado todo el ano
- Ahorra 100 EUR (equivalente a 2 meses)

---

## Archivos a Modificar

### 1. Componente de Precios
**Archivo:** `src/components/ModernPricing.tsx`

Cambios:
- Reducir de 6 a 5 planes
- Eliminar planes "pro" y "premium"
- Agregar nuevo plan "premium_max"
- Actualizar grid de 6 columnas a 5 columnas (xl:grid-cols-5)
- Agregar indicador de "usos" por plan
- Marcar "Premium Plus" como el mas popular

### 2. Archivos de Traduccion (7 idiomas)
Actualizar la seccion `pricing.plans` en cada archivo:

**Archivos:**
- `src/i18n/locales/es.json`
- `src/i18n/locales/en.json`
- `src/i18n/locales/fr.json`
- `src/i18n/locales/de.json`
- `src/i18n/locales/it.json`
- `src/i18n/locales/pt.json`
- `src/i18n/locales/nl.json`

**Estructura nueva para cada idioma:**

```json
{
  "pricing": {
    "plans": {
      "member": {
        "name": "AI Chef Miembro",
        "price": "Gratis",
        "uses": "2/mes",
        "description": "Ideal para ayudantes de cocina, cocineros y jefes de partida",
        "features": { ... }
      },
      "premium_pro": {
        "name": "AI Chef Premium Pro", 
        "price": "25€",
        "period": "/mes",
        "uses": "150/mes",
        "description": "Para Chefs de Cocina, Chefs Ejecutivos...",
        "features": { ... }
      },
      "premium_plus": {
        "name": "AI Chef Premium Plus",
        "price": "50€",
        "period": "/mes",
        "uses": "350/mes",
        "description": "Para Chefs profesionales y restaurantes",
        "features": { ... }
      },
      "premium_max": {
        "name": "AI Chef Premium Max",
        "price": "95€",
        "period": "/mes",
        "uses": "∞",
        "description": "Uso ilimitado mensual para profesionales exigentes",
        "features": { ... }
      },
      "premium_plus_annual": {
        "name": "AI Chef Premium Plus Anual",
        "price": "500€",
        "period": "/año",
        "uses": "∞",
        "original_price": "600€",
        "discount": "Ahorra 100€",
        "description": "...",
        "features": { ... }
      }
    }
  }
}
```

---

## Cambios en el Componente ModernPricing.tsx

### Nuevo array de planes:

```tsx
const plans = [
  {
    id: 'member',
    name: t('pricing.plans.member.name'),
    price: t('pricing.plans.member.price'),
    uses: t('pricing.plans.member.uses'),
    description: t('pricing.plans.member.description'),
    features: [...],
    popular: false
  },
  {
    id: 'premium_pro',
    name: t('pricing.plans.premium_pro.name'),
    price: t('pricing.plans.premium_pro.price'),
    period: t('pricing.plans.premium_pro.period'),
    uses: t('pricing.plans.premium_pro.uses'),
    description: t('pricing.plans.premium_pro.description'),
    features: [...],
    popular: false
  },
  {
    id: 'premium_plus',
    name: t('pricing.plans.premium_plus.name'),
    price: t('pricing.plans.premium_plus.price'),
    period: t('pricing.plans.premium_plus.period'),
    uses: t('pricing.plans.premium_plus.uses'),
    description: t('pricing.plans.premium_plus.description'),
    features: [...],
    popular: true  // MAS POPULAR
  },
  {
    id: 'premium_max',
    name: t('pricing.plans.premium_max.name'),
    price: t('pricing.plans.premium_max.price'),
    period: t('pricing.plans.premium_max.period'),
    uses: t('pricing.plans.premium_max.uses'),
    description: t('pricing.plans.premium_max.description'),
    features: [...],
    popular: false
  },
  {
    id: 'premium_plus_annual',
    // ... igual que antes con descuento
  }
];
```

### Nuevo indicador de USOS:

Agregar seccion "USOS" debajo del precio:

```tsx
{plan.uses && (
  <div className="text-xs text-muted-foreground mt-1">
    <span className="font-medium uppercase">USOS</span>
    <p>{plan.uses}</p>
  </div>
)}
```

### Grid responsive actualizado:

```tsx
<div className="grid ... xl:grid-cols-5">
```

---

## Traducciones por Idioma

### Espanol (es.json)
- AI Chef Miembro, Gratis, 2/mes
- AI Chef Premium Pro, 25 EUR/mes, 150/mes
- AI Chef Premium Plus, 50 EUR/mes, 350/mes
- AI Chef Premium Max, 95 EUR/mes, ilimitado
- AI Chef Premium Plus Anual, 500 EUR/ano, ilimitado

### English (en.json)
- AI Chef Member, Free, 2/month
- AI Chef Premium Pro, 25 EUR/month, 150/month
- AI Chef Premium Plus, 50 EUR/month, 350/month
- AI Chef Premium Max, 95 EUR/month, unlimited
- AI Chef Premium Plus Annual, 500 EUR/year, unlimited

### Francais (fr.json)
- AI Chef Membre, Gratuit, 2/mois
- illimite para usos infinitos

### Deutsch (de.json)
- AI Chef Mitglied, Kostenlos, 2/Monat
- unbegrenzt para usos infinitos

### Italiano (it.json)
- AI Chef Membro, Gratuito, 2/mese
- illimitato para usos infinitos

### Portugues (pt.json)
- AI Chef Membro, Gratis, 2/mes
- ilimitado para usos infinitos

### Nederlands (nl.json)
- AI Chef Lid, Gratis, 2/maand
- onbeperkt para usos infinitos

---

## Orden de Implementacion

1. Actualizar `src/i18n/locales/es.json` (idioma base)
2. Actualizar los otros 6 archivos de idiomas en paralelo
3. Modificar `src/components/ModernPricing.tsx` para reflejar la nueva estructura

---

## Resultado Visual Esperado

Las cards de precios mostraran:

```text
+------------------+  +------------------+  +------------------+  +------------------+  +------------------+
| AI Chef Miembro  |  | AI Chef          |  | AI Chef          |  | AI Chef          |  | AI Chef          |
|                  |  | Premium Pro      |  | Premium Plus     |  | Premium Max      |  | Premium Plus     |
|     Gratis       |  |     25€/mes      |  |  🔥 MAS POPULAR   |  |     95€/mes      |  | Anual            |
|                  |  |                  |  |     50€/mes      |  |                  |  |    500€/año      |
|  USOS: 2/mes     |  |  USOS: 150/mes   |  |  USOS: 350/mes   |  |  USOS: ∞         |  |  USOS: ∞         |
|                  |  |                  |  |                  |  |                  |  |  Ahorra 100€     |
|  [Agregar]       |  |  [Agregar]       |  |  [Agregar]       |  |  [Agregar]       |  |  [Agregar]       |
+------------------+  +------------------+  +------------------+  +------------------+  +------------------+
```

