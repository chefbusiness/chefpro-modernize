#!/usr/bin/env python3
"""Vuelca los prompts EXACTOS (los mismos que documentos.py manda a bridge) de los
bloques que aún no están en caché, para que los escriban agentes en paralelo.
Uso: python3 dump_prompts.py <pid> <dir_salida_de_documentos.py>  → <salida>/prompts/{index.json,<id>.txt,system.txt}
Patrón (John, 2026-09-04): los productos digitales NO se escriben con bridge; cada prompt lo redacta un
subagente Anthropic que guarda el bloque en la caché txt/ y lo verifica con check_bloque.py.
2026-09-10: el prompt lo construye `documentos.contexto_capitulo()` + `documentos.prompts_de_capitulo()`,
las MISMAS funciones que usa generar_capitulo(), así que los «puntos» ya vienen repartidos por tramo (uno
no recibe los de otro) y cada prompt dice qué escriben los demás tramos del capítulo. Esa función común es
lo que impide que este volcado y el pipeline diverjan; el test lo comprueba
(scripts/productos-digitales/tests/test_reparto_puntos.py, gate e)."""
import importlib.util, json, os, sys
REPO = '/Users/johnguerrero/chefpro-modernize'
PID = sys.argv[1]
SALIDA = os.path.abspath(sys.argv[2])
S = SALIDA
sp = importlib.util.spec_from_file_location('d', REPO + '/scripts/productos-digitales/guias-v2_0/documentos.py')
d = importlib.util.module_from_spec(sp); sp.loader.exec_module(d)

guion = d.cargar_guion(PID)
guia = guion.GUIA
xlsx_dir = os.path.join(d.DL, PID)
res = d.cargar_research(); idx = d.indexar_research(res)
hojas = d._hojas_conocidas(xlsx_dir)
P = os.path.join(S, 'prompts'); os.makedirs(P, exist_ok=True)
open(os.path.join(P, 'system.txt'), 'w', encoding='utf-8').write(d.SYSTEM)
index = []


def volcar(capitulos, g, dir_txt, prefijo):
    os.makedirs(dir_txt, exist_ok=True)
    for cap in capitulos:
        ctx = d.contexto_capitulo(cap, xlsx_dir, idx)
        tablas = []
        for t in cap.get('tablas', []):
            md, nf = d.construir_tabla(xlsx_dir, t)
            tablas.append(t.get('titulo', ''))
        cap['tablas_anunciadas'] = tablas
        bloques_p = d.prompts_de_capitulo(cap, g, ctx['ctx_cifras'], ctx['ctx_sector'])
        for i, b in enumerate(bloques_p):
            por_bloque, epis = b['palabras'], b['epigrafes']
            ruta = os.path.join(dir_txt, f'cap{cap["n"]:02d}_b{i + 1}.txt')
            if os.path.exists(ruta):
                t = open(ruta, encoding='utf-8').read().strip()
                if len(t.split()) >= por_bloque * 0.6 and not d.defectos_de_bloque(t):
                    continue
            p = b['prompt']
            bid = f'{prefijo}_cap{cap["n"]:02d}_b{i + 1}'
            open(os.path.join(P, bid + '.txt'), 'w', encoding='utf-8').write(p)
            index.append({'id': bid, 'ruta_txt': ruta, 'prompt': os.path.join(P, bid + '.txt'),
                          'palabras_objetivo': por_bloque, 'palabras_min': int(por_bloque * 0.72),
                          'capitulo': cap['titulo'], 'epigrafes': epis,
                          'puntos': b['puntos']})


volcar(guion.CAPITULOS, guia, os.path.join(SALIDA, 'txt'), 'guia')
for b in guion.BONUS:
    gb = dict(guia); gb.update(b['guia'])
    volcar(b['capitulos'], gb, os.path.join(SALIDA, 'txt', b['nombre']), b['nombre'])
json.dump(index, open(os.path.join(P, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(index), 'bloques pendientes;', sum(x['palabras_objetivo'] for x in index), 'palabras objetivo')
for x in index: print(' ', x['id'], x['palabras_objetivo'])
