

# Plan: Social Proof con Avatares y Contador en Hero

## Resumen

Reemplazar el Badge actual ("Nuevo: Inteligencia Artificial para Chefs") por un componente visual de social proof que muestre:
- 5 avatares de usuarios (generados con IA)
- 4.5 estrellas de calificacion
- Contador de "Soluciones y recetas generadas"

---

## Diseno Visual

```text
[Avatar1][Avatar2][Avatar3][Avatar4][Avatar5]    ★★★★☆    3.748.149 Soluciones y recetas generadas
    (superpuestos -8px)                          (4.5)
```

---

## Archivos a Crear

### 1. Generar 5 avatares con IA

Crear 5 imagenes de perfiles diversos de chefs/profesionales de hosteleria:
- `src/assets/avatars/chef-avatar-1.jpg` - Chef hombre joven
- `src/assets/avatars/chef-avatar-2.jpg` - Chef mujer
- `src/assets/avatars/chef-avatar-3.jpg` - Chef hombre con gorra
- `src/assets/avatars/chef-avatar-4.jpg` - Pastelera
- `src/assets/avatars/chef-avatar-5.jpg` - Chef senior

### 2. Nuevo componente: `src/components/HeroSocialProof.tsx`

```tsx
// Estructura del componente
<div className="flex items-center gap-4 mb-6">
  {/* Avatares superpuestos */}
  <div className="flex -space-x-3">
    {avatars.map((avatar, i) => (
      <Avatar key={i} className="border-2 border-background w-10 h-10">
        <AvatarImage src={avatar} />
      </Avatar>
    ))}
  </div>
  
  {/* Estrellas y contador */}
  <div className="flex flex-col items-start">
    <div className="flex items-center gap-1">
      {/* 4 estrellas llenas + 1 media */}
      <Star className="fill-accent text-accent" />
      <Star className="fill-accent text-accent" />
      <Star className="fill-accent text-accent" />
      <Star className="fill-accent text-accent" />
      <StarHalf className="fill-accent text-accent" />
    </div>
    <span className="text-sm font-semibold">
      <span className="text-lg font-bold">3.748.149</span> {t('hero.social_proof_label')}
    </span>
  </div>
</div>
```

---

## Traducciones a Agregar (7 idiomas)

Nueva clave: `hero.social_proof_label`

| Idioma | Texto |
|--------|-------|
| ES | "Soluciones y recetas generadas" |
| EN | "Solutions and recipes generated" |
| FR | "Solutions et recettes generees" |
| DE | "Losungen und Rezepte generiert" |
| IT | "Soluzioni e ricette generate" |
| PT | "Solucoes e receitas geradas" |
| NL | "Oplossingen en recepten gegenereerd" |

---

## Cambios en ModernHero.tsx

### Antes:
```tsx
<Badge variant="outline" className="px-4 py-1.5">
  {t('hero.badge')}
</Badge>
```

### Despues:
```tsx
<HeroSocialProof />
```

Se elimina el Badge y se reemplaza por el nuevo componente de social proof.

---

## Archivos a Modificar

1. **Generar con IA**: 5 avatares de chefs profesionales
2. **Crear**: `src/components/HeroSocialProof.tsx` - Nuevo componente
3. **Modificar**: `src/components/ModernHero.tsx` - Reemplazar Badge
4. **Modificar**: `src/i18n/locales/es.json` - Agregar traduccion
5. **Modificar**: `src/i18n/locales/en.json` - Agregar traduccion
6. **Modificar**: `src/i18n/locales/fr.json` - Agregar traduccion
7. **Modificar**: `src/i18n/locales/de.json` - Agregar traduccion
8. **Modificar**: `src/i18n/locales/it.json` - Agregar traduccion
9. **Modificar**: `src/i18n/locales/pt.json` - Agregar traduccion
10. **Modificar**: `src/i18n/locales/nl.json` - Agregar traduccion

---

## Resultado Visual Esperado

```text
                    [👨‍🍳][👩‍🍳][👨][👩‍🍳][👨‍🍳]  ★★★★☆  3.748.149 Soluciones y recetas generadas
                    
                         Transforma tu [Restaurante] con AI Chef Pro
                         
                    55+ Herramientas de IA Especializadas para Chefs...
```

El nuevo componente de social proof:
- Genera confianza visual inmediata
- Muestra una comunidad activa de profesionales
- Destaca el volumen de uso (3.7M+ recetas generadas)
- Mantiene el rating de 5 estrellas pero con visual mas atractivo

---

## Detalles Tecnicos

- Usar componente `Avatar` de shadcn/ui para los avatares
- Avatares con borde blanco y superposicion con `-space-x-3`
- Contador con formato numerico local (3.748.149 en ES, 3,748,149 en EN)
- Icono `StarHalf` de lucide-react para la media estrella (opcional mantener 5 completas)
- Responsive: en movil apilar verticalmente

