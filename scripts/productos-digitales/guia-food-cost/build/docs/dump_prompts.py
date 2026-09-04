#!/usr/bin/env python3
"""Vuelca los prompts EXACTOS (los mismos que documentos.py manda a bridge) de los
bloques que aún no están en caché, para que los escriban agentes en paralelo.
Uso: python3 dump_prompts.py  → prompts/index.json + prompts/<id>.txt + system.txt"""
import importlib.util, json, os, sys
REPO = '/Users/johnguerrero/chefpro-modernize'
S = os.path.dirname(os.path.abspath(__file__))
PID = 'guia-food-cost-ingenieria-menu'
SALIDA = os.path.join(S, PID)
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
        cifras = d.resolver_cifras(xlsx_dir, cap.get('cifras', []))
        ctx_cifras = '\n'.join(f'  - {e}: {v}   [fuente: {r}]' for e, v, r, _ in cifras)
        ctx_sector, _, _ = d.bloque_research(idx, cap.get('sector', []))
        tablas = []
        for t in cap.get('tablas', []):
            md, nf = d.construir_tabla(xlsx_dir, t)
            tablas.append(t.get('titulo', ''))
        cap['tablas_anunciadas'] = tablas
        bloques = d.trocear(cap['epigrafes'], cap.get('bloques', 2))
        por_bloque = max(500, int(cap['palabras'] / len(bloques)))
        for i, epis in enumerate(bloques):
            ruta = os.path.join(dir_txt, f'cap{cap["n"]:02d}_b{i + 1}.txt')
            if os.path.exists(ruta):
                t = open(ruta, encoding='utf-8').read().strip()
                if len(t.split()) >= por_bloque * 0.6 and not d.defectos_de_bloque(t):
                    continue
            p = d.prompt_bloque(cap, epis, por_bloque, ctx_cifras, ctx_sector, g,
                                es_ultimo=(i == len(bloques) - 1))
            bid = f'{prefijo}_cap{cap["n"]:02d}_b{i + 1}'
            open(os.path.join(P, bid + '.txt'), 'w', encoding='utf-8').write(p)
            index.append({'id': bid, 'ruta_txt': ruta, 'prompt': os.path.join(P, bid + '.txt'),
                          'palabras_objetivo': por_bloque, 'palabras_min': int(por_bloque * 0.72),
                          'capitulo': cap['titulo'], 'epigrafes': epis})


volcar(guion.CAPITULOS, guia, os.path.join(SALIDA, 'txt'), 'guia')
for b in guion.BONUS:
    gb = dict(guia); gb.update(b['guia'])
    volcar(b['capitulos'], gb, os.path.join(SALIDA, 'txt', b['nombre']), b['nombre'])
json.dump(index, open(os.path.join(P, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(index), 'bloques pendientes;', sum(x['palabras_objetivo'] for x in index), 'palabras objetivo')
for x in index: print(' ', x['id'], x['palabras_objetivo'])
