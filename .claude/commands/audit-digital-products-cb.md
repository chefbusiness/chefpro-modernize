---
description: Auditar el flujo de productos digitales en chefbusiness.co buscando los 2 bugs que rompieron aichef.pro el 2026-04-29 (access gates post-pago + paths rotos en función de descargas)
---

# Auditoría de productos digitales — chefbusiness.co

Este comando audita la sección de **productos digitales** del sitio chefbusiness.co (URL pública: https://chefbusiness.co/productos-digitales/) replicando dos bugs críticos que se diagnosticaron y arreglaron en su sitio hermano aichef.pro el 2026-04-29.

**Contexto**: aichef.pro y chefbusiness.co comparten el mismo patrón de productos digitales (landing → Stripe → access gate post-pago → dashboard con descargas firmadas por JWT). Si chefbusiness.co se construyó copiando de aichef.pro o si comparten código/plantillas, es muy probable que tenga los mismos defectos. Cliente real (Alfonso) quedó bloqueado dos veces en aichef.pro por estos bugs.

---

## Bug #1 — Access Gates post-pago rotos

### Síntoma para el usuario
Cliente paga en Stripe → vuelve al sitio → ve **"No se encontró la sesión de pago"**. Pide acceso por el formulario "ya compré", recibe email magic link, hace clic → mismo error.

### 3 sub-bugs en frontend (típicamente en archivos `*AccessGate.tsx`)
1. Frontend hace `fetch('/.netlify/functions/verify-purchase', { body: JSON.stringify({ sessionId }) })` pero el backend espera `{ checkoutSessionId }`. El backend nunca entra en la rama Stripe.
2. Frontend lee `data.token` de la respuesta para guardarlo en localStorage, pero el backend devuelve `{ valid: true, jwt: '...' }`. El JWT nunca se guarda → `useAuth` lo lee como `null` → `ProtectedRoute` redirige.
3. Frontend solo maneja `?session_id=` (vuelta de Stripe) e ignora `?jwt=` (que es lo que envía el email magic link de `resend-access`). Hacer clic al email también da el error inmediato.

### Cómo auditar en chefbusiness.co
1. Localiza todos los componentes de access gate. Busca:
   ```bash
   rg -l "AccessGate|access-gate|verify-purchase" --type tsx --type ts --type jsx --type js
   ```
2. Para cada archivo encontrado, verifica los 3 puntos:
   - ¿Envía `sessionId` o `checkoutSessionId` en el body del fetch?
   - ¿Lee `data.token` o `data.jwt` para guardar en localStorage?
   - ¿Lee `searchParams.get('jwt')` además de `searchParams.get('session_id')`?
3. Cruza con el backend en `netlify/functions/verify-purchase.*` (o el equivalente) para confirmar la API real.
4. Si chefbusiness.co usa Astro/WP en vez de React+Netlify, traduce el bug al stack equivalente: el contrato frontend↔backend tiene los mismos 3 puntos críticos.

### Fix de referencia (aichef.pro, commit `1ad6b04`)
- Crear un componente compartido único `ProductAccessGate` con la lógica correcta (acepta `?session_id=` Y `?jwt=`, envía `checkoutSessionId`, lee `data.jwt`).
- Migrar cada gate individual a un wrapper de ~10 líneas que solo pase la config del producto (productId, storageKey, dashboardPath, landingPath, productLabel).
- Como red de seguridad operativa: añadir una página admin `/admin/generar-acceso` (con `ADMIN_PASSWORD` env var) que firme magic links manualmente cuando un cliente reporte estar bloqueado.

---

## Bug #2 — Paths rotos en función de descargas (SPA fallback los oculta)

### Síntoma para el usuario
Cliente entra al dashboard → ve la lista de descargas → hace clic en "Descargar" de un archivo concreto → ve **404 "Página no encontrada"** del router del sitio (no el 404 nativo del navegador).

### Causa raíz
La función serverless que devuelve la lista de URLs de descargas mapea claves (ej. `'temp-recepcion'`) a paths estáticos (`/dl/pack-appcc/02-temperaturas-recepcion.xlsx`). Si el path **no existe** en `/public/dl/`, Netlify (modo SPA) hace fallback a `index.html` con **HTTP 200** → el navegador recibe HTML en vez del xlsx → el router del SPA renderiza su 404. El error es invisible en logs porque parece un 200 exitoso.

### Cómo auditar en chefbusiness.co
1. Localiza la función que sirve URLs de descargas. Probablemente:
   ```bash
   rg -l "PRODUCT_FILES|get-download-urls|download-urls" netlify/ src/ functions/ 2>/dev/null
   ```
2. Una vez localizada, corre este script de auditoría (ajusta la ruta de la función y la carpeta pública si difieren):

   ```bash
   node -e "
   const fs = require('fs'), path = require('path');
   const FUNCTION_FILE = 'netlify/functions/get-download-urls.ts';  // ← ajustar si difiere
   const PUBLIC_DIR = 'public';                                      // ← ajustar si difiere
   const ts = fs.readFileSync(FUNCTION_FILE, 'utf8');
   const re = /'(\/dl\/[^']+)'/g;
   const paths = new Set();
   let m; while ((m = re.exec(ts)) !== null) paths.add(m[1]);
   let missing = 0;
   [...paths].sort().forEach(p => {
     if (!fs.existsSync(path.join(PUBLIC_DIR, p))) {
       console.log('MISSING:', p);
       missing++;
     }
   });
   console.log('---');
   console.log('Total OK:', paths.size - missing, 'MISSING:', missing);
   "
   ```

3. Para cada `MISSING:` encontrado, busca en disco el archivo más parecido:
   ```bash
   ls public/dl/<carpeta>/ | grep -iE "<palabra-clave-del-path-roto>"
   ```
4. Edita la función para que la clave apunte al filename real. Ejemplo aichef.pro:
   - `'02-temperaturas-recepcion.xlsx'` → `'02-registro-temperaturas-recepcion.xlsx'`
   - `'11-acciones-correctivas.xlsx'` → `'11-registro-acciones-correctivas.xlsx'`
   - `'BONUS-02-protocolo-alerta.xlsx'` → `'BONUS-02-protocolo-alerta-alimentaria.xlsx'`
   - `'11-dashboard-food-cost.xlsx'` → `'11-dashboard-food-cost-mensual.xlsx'`

5. Re-corre el script. Debe dar **`MISSING: 0`**.

### Si chefbusiness.co usa otro stack (Astro/WordPress)
- En **Astro**: las descargas suelen estar en `public/dl/` igual; busca el endpoint que firma o redirige a esos paths (`src/pages/api/...`).
- En **WordPress**: probablemente las descargas se sirven con un plugin (Easy Digital Downloads, WooCommerce, custom). El equivalente del bug sería: URL de descarga apunta a un media ID o slug que no existe / fue renombrado. Verificar en `wp_posts` (post_type=`attachment`) que las URLs guardadas en el campo del producto coincidan con archivos reales.

---

## Lecciones operativas a importar al proyecto

1. **El SPA fallback de Netlify oculta 404 de archivos estáticos**. Siempre que añadas un producto nuevo o renombres archivos en `/public/dl/`, corre el script de auditoría. Considera añadirlo como step de CI o pre-commit hook.
2. **Los 27 access gates de aichef.pro nacieron del mismo template defectuoso**. Si chefbusiness.co tiene N+1 access gates con copy-paste del mismo patrón, asume que **todos** tienen los 3 sub-bugs hasta que verifiques uno por uno. Mejor refactorizar a un componente compartido que vivir parcheando.
3. **El cliente Alfonso encontró el bug sólo porque insistió**. Probablemente otros clientes silenciosos están bloqueados sin reportar. Considera sacar lista de compradores recientes de Stripe (productos: Kit Tareas variants, Guías Cómo Montar, Mega Pack, Plan Financiero, Gestión Personal, Inventario, APPCC, Escandallos) y enviar email proactivo "¿pudiste descargar tus archivos?".

---

## Output esperado de esta auditoría

Genera un informe en `audit-cb-digital-products.md` (en la raíz del repo de chefbusiness.co) con:

1. **Bug #1 (access gates)**:
   - Lista de archivos auditados con tabla `archivo | bug 1.1 | bug 1.2 | bug 1.3 | overall`
   - Para los rotos: snippet del código defectuoso
   - Plan de fix recomendado (componente compartido vs parche individual, según cantidad)

2. **Bug #2 (paths de descargas)**:
   - Resultado del script Node (Total OK / MISSING)
   - Para cada MISSING: el archivo real al que debería apuntar
   - Diff sugerido para la función

3. **Recomendaciones cruzadas**:
   - ¿Tiene chefbusiness.co un equivalente a `/admin/generar-acceso`? Si no, ¿conviene replicarlo?
   - ¿Hay env var `ADMIN_PASSWORD` configurada en su Netlify/host?
   - ¿Lista de compradores afectados a contactar proactivamente?

**No commitees ni pushees nada todavía**. Reporta el diagnóstico y espera luz verde del usuario antes de aplicar fixes. Para los fixes, sigue el patrón de los commits de aichef.pro: `1ad6b04` (access gates) y `8387682` (paths descargas) — están en `github.com/chefbusiness/chefpro-modernize`.

---

## Referencia para inspección directa de aichef.pro (sitio hermano de referencia)

Si necesitas comparar cómo quedó el código fix-eado:
- Repo aichef.pro: `github.com/chefbusiness/chefpro-modernize`
- Componente compartido fix: `src/components/shared/ProductAccessGate.tsx`
- Función de descargas (post-fix): `netlify/functions/get-download-urls.ts`
- Página admin manual: `src/pages/AdminGenerateAccess.tsx` + `netlify/functions/admin-generate-access.ts` + `scripts/generate-access-link.mjs`
- Tags git: `access-gates-fix-2026-04-29` (bug #1), commit `8387682` (bug #2)
