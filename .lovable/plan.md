

# Plan: Mejorar Social Proof con Perfiles Diversos y Layout Centrado

## Resumen de Cambios

1. **Reducir el contador** de 3.748.149 a **48.149** (numero mas razonable)
2. **Aumentar avatares de 5 a 8** con perfiles diversos de la industria
3. **Centrar visualmente** el social proof en desktop
4. **Generar nuevos avatares** representando diferentes profesionales

---

## Nuevos Perfiles a Generar (8 avatares diversos)

| # | Archivo | Perfil | Descripcion |
|---|---------|--------|-------------|
| 1 | `avatar-1.jpg` | Bartender hombre | Profesional de bar con chaleco/camisa |
| 2 | `avatar-2.jpg` | Chef mujer | Cocinera profesional |
| 3 | `avatar-3.jpg` | Gerente restaurante | Hombre con camisa formal |
| 4 | `avatar-4.jpg` | Pastelera | Mujer con delantal de reposteria |
| 5 | `avatar-5.jpg` | Dueno restaurante | Persona con aspecto ejecutivo/casual |
| 6 | `avatar-6.jpg` | Bartender mujer | Profesional de cocteleria |
| 7 | `avatar-7.jpg` | Panadero | Hombre con delantal/uniforme panaderia |
| 8 | `avatar-8.jpg` | Chef senior | Chef experimentado |

---

## Cambios en HeroSocialProof.tsx

### Estructura Visual Mejorada

```text
              [Avatar Stack - 8 perfiles superpuestos]
              ★★★★☆  48.149 Soluciones y recetas generadas
```

### Cambios Especificos

1. **Contador**: `3748149` → `48149`
2. **Layout centrado**: Cambiar de `flex-row` a layout apilado verticalmente centrado en todas las resoluciones
3. **Avatares**: Importar 8 avatares en lugar de 5
4. **Alt text**: Cambiar de "Chef X" a "Professional X" para reflejar diversidad

### Codigo Actualizado

```tsx
// 8 avatares diversos
const avatars = [avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7, avatar8];

return (
  <div className="flex flex-col items-center gap-2 mb-4">
    {/* Avatares centrados */}
    <div className="flex -space-x-3 justify-center">
      {avatars.map((avatar, i) => (
        <Avatar key={i} className="...">
          <AvatarImage src={avatar} alt={`Professional ${i + 1}`} />
        </Avatar>
      ))}
    </div>
    
    {/* Estrellas y contador centrados */}
    <div className="flex flex-col items-center gap-0.5">
      <div className="flex items-center gap-0.5">
        {/* 5 estrellas */}
      </div>
      <span className="text-sm text-muted-foreground">
        <span className="font-bold">{formatNumber(48149)}</span>
        {t('hero.social_proof_label')}
      </span>
    </div>
  </div>
);
```

---

## Archivos a Modificar

1. **Generar con IA**: 8 avatares profesionales diversos
   - `src/assets/avatars/avatar-1.jpg` (Bartender hombre)
   - `src/assets/avatars/avatar-2.jpg` (Chef mujer)
   - `src/assets/avatars/avatar-3.jpg` (Gerente restaurante)
   - `src/assets/avatars/avatar-4.jpg` (Pastelera)
   - `src/assets/avatars/avatar-5.jpg` (Dueno restaurante)
   - `src/assets/avatars/avatar-6.jpg` (Bartender mujer)
   - `src/assets/avatars/avatar-7.jpg` (Panadero)
   - `src/assets/avatars/avatar-8.jpg` (Chef senior)

2. **Modificar**: `src/components/HeroSocialProof.tsx`
   - Importar 8 avatares
   - Cambiar contador a 48.149
   - Centrar layout verticalmente
   - Actualizar alt text generico

3. **Eliminar**: Avatares antiguos de chef (opcional, o mantener para otros usos)

---

## Resultado Visual Esperado

### Desktop
```text
                    [👔][👩‍🍳][👨‍💼][👩‍🍰][🧑‍💼][🍸][👨‍🍳][👨‍🍳]
                           ★★★★★
                    48.149 Soluciones y recetas generadas
                    
                    Transforma tu [Restaurante] con AI Chef Pro
```

### Mobile/Tablet (igual, centrado)
```text
        [👔][👩‍🍳][👨‍💼][👩‍🍰][🧑‍💼][🍸][👨‍🍳][👨‍🍳]
               ★★★★★
        48.149 Soluciones y recetas generadas
        
        Transforma tu [Restaurante]
            con AI Chef Pro
```

---

## Beneficios

- **Numero mas creible**: 48.149 vs 3.7 millones
- **Representacion inclusiva**: No solo chefs, incluye bartenders, gerentes, duenos
- **Layout consistente**: Centrado en todas las resoluciones
- **Mejor uso del espacio**: Aprovecha el espacio entre header y contenido en desktop

