

# Plan: Actualizar Notificaciones de Conversion

## Problema

Los planes mostrados en las notificaciones flotantes estan desactualizados. Aparecen "Premium 15EUR" y "Pro 10EUR" que ya no existen. Ademas, faltan ciudades de paises europeos clave.

## 1. Actualizar Planes (todos los idiomas)

Segun el modelo de precios actual (v7), los planes reales son:

| Plan Actual | Precio EUR | Precio USD |
|-------------|-----------|-----------|
| Premium Pro | 25 | 30 |
| Premium Plus | 50 | 60 |
| Premium Max | 95 | 115 |
| Premium Plus Anual | 950/ano | 1150/ano |

Se eliminan "Premium 15EUR" y "Pro 10EUR" que ya no existen.

## 2. Ampliar Ciudades por Idioma

### Espanol (es) - Agregar:
- Ciudades europeas: Paris, Roma, Lisboa, Berlin (chefs hispanohablantes en Europa)

### Ingles (en) - Agregar:
- Mas ciudades USA: Houston, Seattle, Boston, Las Vegas, Nashville, Austin, Denver, Philadelphia
- Ciudades de Polonia: Warsaw, Krakow

### Frances (fr) - Agregar:
- Lille, Nantes, Rennes

### Aleman (de) - Agregar:
- Leipzig, Dresden, Hannover
- Ciudades de Polonia: Warschau, Krakau

### Italiano (it) - Agregar:
- Genova, Verona, Catania, Bari

### Portugues (pt) - Agregar:
- Faro, Braga, Funchal

### Holandes (nl) - Agregar:
- Breda, Maastricht, Leiden

### NUEVO: Polaco no tiene idioma propio, pero se agregan ciudades polacas al ingles y aleman ya que son los idiomas que mas usarian.

## 3. Archivo a Modificar

`src/data/conversion-notifications.ts`:
- Actualizar `notificationPlans` en los 7 idiomas con los 4 planes correctos
- Ampliar `notificationCities` con las nuevas ciudades en cada idioma

## Resultado

Las notificaciones flotantes mostraran solo planes que existen realmente (Premium Pro 25EUR, Premium Plus 50EUR, Premium Max 95EUR, Premium Plus Anual 950EUR/ano) y tendran mayor diversidad geografica europea y norteamericana.

