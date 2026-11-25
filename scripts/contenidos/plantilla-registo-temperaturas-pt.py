#!/usr/bin/env python3
"""Registo de temperaturas HACCP (PT), GRATIS — lead magnet de /pt/blog/haccp y /pt/blog/controlo-de-temperaturas.

LowFruits PT (nov-2026): «haccp restauração» 140 + «haccp na restauração» 140; «folha de registo de temperaturas» 20.
Gemelo portugués de plantilla-haccp-lijsten-nl.py (mismo diseño negro/oro, celdas amarillas editables, validaciones con
mensaje, formato condicional rojo, inject_cache + caché «texto vacío», gate de lógica sobre COPIAS sin caché con pycel,
una sola pestaña seleccionada, A4, PDF ≥ 6,5 pt), ADAPTADO a Portugal. Solo las normas verificadas (memoria
reference_normativa-portuguesa-haccp-alergenios, 25-nov-2026):
  - Ley: ultracongelados ≤ −18 °C (DL 251/91) y pescado congelado o ultracongelado ≤ −18 °C, descongelado a la
    temperatura del hielo fundente (DL 37/2004, incluye restaurantes). El Reg. (CE) 852/2004 no fija cifras.
  - Código de Boas Práticas AHRESP 2015 (voluntario): refrigeração 0–7 °C (0–4 °C con una única câmara), congelados no
    ultracongelados (excepto pescado) ≤ −12 °C, confeção ≥ 65 °C en el centro, manutenção a quente ≥ 65 °C,
    arrefecimento hasta 5 °C en ≤ 2 h, reaquecimento a 65 °C una sola vez, > 2 h por debajo de 65 °C → se elimina;
    registo «pelo menos, uma vez por dia».
  - Opción más exigente del plan (ni ley ni AHRESP): confeção a 75 °C (se escribe en la celda amarilla).
  - Registador automático: solo câmaras de ultracongelados ≥ 10 m³ (Reg. 37/2005; ET 4/DGAV/2025).
Hojas:
  - «Frio»: 5 equipos con nombre, mínimo y máximo editables (3 de refrigeração 0–7 °C, arca de congelados −12 °C,
    arca de ultracongelados y pescado −18 °C) × 5 semanas. Dos filas por equipo: abertura (la lectura diaria de la
    AHRESP) y fecho (opcional, recomendación propia, como en el post) + una fila de rubricas por día. «Conforme?» =
    todas las lecturas dentro de [mínimo, máximo]; mínimo vacío = sin límite inferior.
  - «Confeção e arrefecimento» (la pestaña no admite > 31 caracteres; el título nombra las cuatro operaciones):
    confeção, arrefecimento (temperatura inicial opcional; fin y duración obligatorios; MOD(…;1) por la medianoche,
    [h]:mm), reaquecimento (columna «1.º reaquecimento?» Sim/Não: «Não» da NÃO, una sola vez) y manutenção a quente.
  - «Receção»: cada entrega de refrigerados y congelados; tipos con las mismas normas (7, −12, −18), editables.
  - «Termómetro»: verificación en gelo fundente (0 °C); tolerancia editable con 1 °C por defecto y «defina a
    tolerância no seu plano»; en el PDF la tolerancia y la periodicidad quedan en blanco.
  - «Exemplo»: semana 48 (23–29 nov 2026) del «Restaurante O Exemplo (fictício)»; UN desvio (bancada refrigerada, quarta
    al fecho, 9,0 °C) con su ação corretiva.
«Conforme?» = "" si falta un dato necesario o hay TEXTO en una celda numérica (dato o norma): en Excel «abc» >= 65 es
VERDADERO. Normas mostradas con fórmula de texto y duración en [h]:mm (Quick Look, como el gemelo NL).
Gate de idioma: nada de español, brasileirismos, grafías anteriores al AO90 ni neerlandés (xlsx + PDF).

Uso:  python3 scripts/contenidos/plantilla-registo-temperaturas-pt.py
Sale: astro-site/public/descargas/registo-temperaturas-haccp-aichef.xlsx  (5 hojas; las 4 plantillas sin valores)
      astro-site/public/descargas/registo-temperaturas-haccp-aichef.pdf   (A4, 4 páginas para rellenar a mano: frio
      semanal, confeção/arrefecimento/reaquecimento/manutenção a quente, receção, termómetros)
Después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/registo-temperaturas-haccp-aichef.xlsx
`/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import datetime
import math
import re
import shutil
import subprocess
import sys
import tempfile
import warnings
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.pagebreak import Break

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/registo-temperaturas-haccp-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/registo-temperaturas-haccp-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
PARCHE = RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'
ARTIGO = 'https://aichef.pro/pt/blog/haccp'
ARTIGO_TEMP = 'https://aichef.pro/pt/blog/controlo-de-temperaturas'
RODAPE = 'Modelo gratuito da AI Chef Pro · Explicação: aichef.pro/pt/blog/haccp'

PRETO, OURO, CINZA = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borda = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
vermelho = PatternFill('solid', fgColor='F8CBAD')
cinza = PatternFill('solid', fgColor=CINZA)
preto = PatternFill('solid', fgColor=PRETO)
NB = ' '
F_TEMP = '0.0'
F_DESV = '+0.0;-0.0;0.0'
F_HORA = 'hh:mm'
F_DUR = '[h]:mm'   # Quick Look mostra mal '[h]" h "mm' (gemelo NL): duração em [h]:mm
F_DATA = 'dd/mm/yyyy'

# ------------------------------------------------------------------ textos (PT-PT, AO90)
NOTA_LEI = ('Lei: os ultracongelados (Decreto-Lei n.º 251/91) e o pescado congelado ou ultracongelado (Decreto-Lei '
            'n.º 37/2004, que inclui os restaurantes) conservam-se a −18 °C ou menos; o pescado descongelado, à '
            'temperatura do gelo fundente. O Regulamento (CE) n.º 852/2004 não fixa temperaturas.')
NOTA_AHRESP_FRIO = ('Código de Boas Práticas da AHRESP (2015, pequena restauração e bebidas): refrigeração de 0 a 7 °C '
                    '(0 a 4 °C se houver uma única câmara) e congelados que não sejam ultracongelados, exceto o pescado, '
                    'a −12 °C ou menos; registo das temperaturas pelo menos uma vez por dia.')
NOTA_AHRESP_QUENTE = ('Código de Boas Práticas da AHRESP (2015, pequena restauração e bebidas): confeção a 65 °C ou mais '
                      'no centro do alimento, manutenção a quente a 65 °C ou mais, arrefecimento até 5 °C em 2 horas ou '
                      'menos e reaquecimento a 65 °C no centro, uma só vez. O alimento confecionado exposto mais de 2 '
                      'horas abaixo dos 65 °C elimina-se. A lei não fixa estas temperaturas.')
NOTA_PLANO = ('Opção mais exigente do seu plano (não é lei nem código da AHRESP): confeção a 75 °C no centro, como '
              'noutros códigos e guias. Se a adotar, escreva 75 na célula amarela da confeção.')
NOTA_VOLUNTARIO = ('O código da AHRESP é de uso voluntário; o que é obrigatório é ter um sistema baseado no HACCP '
                   '(Reg. 852/2004, art. 5.º) com registos adequados à dimensão do estabelecimento.')
NOTA_FECHO = ('A segunda leitura, ao fecho, é opcional (recomendação nossa, não da lei nem da AHRESP): apanha uma '
              'avaria mais cedo.')
NOTA_PESCADO = ('O pescado congelado guarda-se sempre num equipamento a −18 °C ou menos (Decreto-Lei n.º 37/2004), '
                'nunca na arca de congelados a −12 °C.')
NOTA_REGISTADOR = ('Num restaurante comum, o registador automático de temperatura só é obrigatório em câmaras de '
                   'ultracongelados de 10 m³ ou mais (Regulamento (CE) n.º 37/2005; Esclarecimento Técnico n.º '
                   '4/DGAV/2025).')
NOTA_GUARDAR = 'Guarde os registos durante o tempo que o seu plano definir.'
NOTA_AUXILIAR = 'Esta folha é um auxiliar, não um impresso oficial da ASAE, da DGAV ou da AHRESP.'
NOTA_RECECAO = ('Meça à chegada, antes de assinar a guia: entre duas embalagens e, se houver dúvida, no centro do '
                'produto. As normas por defeito são as do armazenamento (lei e código da AHRESP); se o seu plano fixar '
                'outras, escreva-as nas células amarelas.')
NOTA_TOLERANCIA = ('Defina a tolerância no seu plano; o 1 °C desta célula é só um valor de partida para editar (a ficha '
                   'técnica do termómetro indica a do fabricante).')
NOTA_VERMELHO = ('Cada valor a vermelho pede uma ação corretiva e uma nova leitura que mostre que a norma voltou a ser '
                 'cumprida.')
ORIG_LEI = 'Lei: −18 °C ou menos (ultracongelados: Decreto-Lei n.º 251/91; pescado congelado: Decreto-Lei n.º 37/2004)'
ORIG_CONG = 'Código AHRESP 2015: congelados (não ultracongelados, exceto pescado), −12 °C ou menos'
ORIG_REFR = 'Código AHRESP 2015: refrigeração de 0 a 7 °C (0 a 4 °C se houver uma única câmara)'
# Valores que NÃO são normas portuguesas (de outros países ou inventados) e não podem aparecer em texto
VETADOS = [r'(?<![\d,])60\s?°C', r'(?<![\d,])63\s?°C', r'(?<![\d,])70\s?°C', r'(?<![\d,])72\s?°C',
           r'(?<![\d,])74\s?°C', r'(?<![\d,])100\s?°C', r'(?<![\d,])20\s?°C', r'(?<![\d,])3\s?°C(?!: ajuste a norma se a aceitar)', r'\b180\b',
           r'[−–-]15\b', r'\b24\s?h', r'seis meses', r'um ano', r'duas vezes por dia', r'AIHSA', r'FDA',
           r'±\s?1(?:,0)?\s?°C', r'(?<!\d)1\s?a\s?4\s?°C', r'ASAE exige', r'obrigatório registar duas']

# (nome, mínimo °C, máximo °C) — editáveis nas células amarelas; mínimo vazio = sem limite inferior
EQUIPAMENTOS = [('Câmara de refrigeração', 0, 7), ('Frigorífico da cozinha', 0, 7), ('Bancada refrigerada', 0, 7),
                ('Arca de congelados', None, -12), ('Arca de ultracongelados e pescado', None, -18)]
N_EQ = len(EQUIPAMENTOS)
T0 = 7                    # cabeçalho da tabela de equipamentos (linhas 8–12)
W0 = 16                   # primeiro bloco semanal
BLOCO = 2 * N_EQ + 4      # faixa + cabeçalho + 2 linhas por equipamento + rubricas + linha vazia
N_SEMANAS = 5
DIAS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
CAB_FRIO = ['Equipamento', 'Norma', 'Leitura'] + DIAS + ['Conforme?', 'Desvio e ação corretiva', 'Rubrica']
LARG_GRELHA = {'A': 26, 'B': 15, 'C': 11, 'D': 9, 'E': 9, 'F': 9, 'G': 9, 'H': 9, 'I': 9, 'J': 9, 'K': 11, 'L': 38,
               'M': 9}

# Normas das operações a quente (chave, descrição, valor, unidade, origem) — editáveis nas células amarelas
NORMAS = [
    ('conf_t', 'Confeção – temperatura no centro, pelo menos', 65, '°C',
     'Código AHRESP 2015 (o seu plano pode fixar 75 °C, opção mais exigente)'),
    ('arref_t', 'Arrefecimento – temperatura no fim, no máximo', 5, '°C', 'Código AHRESP 2015'),
    ('arref_d', 'Arrefecimento – duração, no máximo', 2, 'horas', 'Código AHRESP 2015'),
    ('reaq_t', 'Reaquecimento – no centro, pelo menos (uma só vez)', 65, '°C', 'Código AHRESP 2015'),
    ('quente_t', 'Manutenção a quente – temperatura, pelo menos', 65, '°C', 'Código AHRESP 2015'),
]
N0 = 7                    # cabeçalho da tabela de normas (linhas 8–12)
V = {k: f'$E${N0 + 1 + i}' for i, (k, _, _, _, _) in enumerate(NORMAS)}
V_LIT = {k: str(w) for k, _, w, _, _ in NORMAS}  # Exemplo: as mesmas normas como números fixos
N_LINHAS = 8              # linhas por operação
ORDEM = ['conf', 'arref', 'reaq', 'quente']
# (cabeçalho, primeira coluna, última coluna, tipo) na grelha A–M de «Frio»
COLS = {
    'conf': [('Produto', 1, 1, 'texto'), ('Data', 2, 2, 'data'), ('Hora', 3, 3, 'hora'),
             ('Temp. no centro (°C)', 4, 4, 'temp'), ('Conforme?', 5, 5, 'ok'),
             ('Ação corretiva (se houver desvio)', 6, 12, 'texto'), ('Rubrica', 13, 13, 'rubrica')],
    'arref': [('Produto', 1, 1, 'texto'), ('Data', 2, 2, 'data'), ('Hora de início', 3, 3, 'hora'),
              ('Temp. no início (°C, opcional)', 4, 4, 'temp'), ('Hora de fim', 5, 5, 'hora'),
              ('Temp. no fim (°C)', 6, 6, 'temp'), ('Duração (h:mm)', 7, 8, 'dur'), ('Conforme?', 9, 9, 'ok'),
              ('Ação corretiva', 10, 12, 'texto'), ('Rubrica', 13, 13, 'rubrica')],
    'reaq': [('Produto', 1, 1, 'texto'), ('Data', 2, 2, 'data'), ('Hora', 3, 3, 'hora'),
             ('Temp. no centro (°C)', 4, 4, 'temp'), ('1.º reaquecimento? (Sim/Não)', 5, 5, 'simnao'),
             ('Conforme?', 6, 6, 'ok'), ('Ação corretiva (se houver desvio)', 7, 12, 'texto'),
             ('Rubrica', 13, 13, 'rubrica')],
    'quente': [('Produto', 1, 1, 'texto'), ('Data', 2, 2, 'data'), ('Hora', 3, 3, 'hora'),
               ('Temp. no alimento (°C)', 4, 4, 'temp'), ('Conforme?', 5, 5, 'ok'),
               ('Ação corretiva (se houver desvio)', 6, 12, 'texto'), ('Rubrica', 13, 13, 'rubrica')],
}
OK_COL = {tp: next(k1 for _, k1, _, s in cols if s == 'ok') for tp, cols in COLS.items()}

RECECAO = [('Refrigerado', 7, 'Código AHRESP 2015 (refrigeração de 0 a 7 °C)'),
           ('Congelado (exceto pescado)', -12, 'Código AHRESP 2015 (congelados que não sejam ultracongelados)'),
           ('Ultracongelado ou pescado congelado', -18, 'Lei: Decreto-Lei n.º 251/91 e Decreto-Lei n.º 37/2004 '
            '(no transporte de ultracongelados, o DL 251/91 tolera subidas breves até 3 °C: ajuste a norma se a aceitar)')]
R0 = 7                    # cabeçalho das normas de receção (linhas 8–10)
R_CAB, R_N = 13, 20       # cabeçalho e número de linhas da lista de receção
TH_TOL = 8                # célula C8: tolerância
TH_CAB, TH_N = 10, 12

# Exemplo: semana 48 (seg 23 a dom 29 de novembro de 2026), um desvio
VB_CAMPOS = ['Restaurante O Exemplo (fictício)', 'Semana 48 (23 a 29 de novembro de 2026)', 'M. Silva']
VB_SEMANA = 48
VB_ACAO = ('Quarta-feira, ao fecho (23:00): 9,0 °C; a porta ficou mal fechada depois do serviço. Porta fechada e '
           'produtos medidos no centro (6,0 °C, dentro da norma). Nova leitura às 23:30: 5,0 °C.')
VB_FRIO = [  # (abertura seg–dom, fecho seg–dom, ação corretiva, rubrica da ação)
    ([3.0, 3.5, 3.0, 4.0, 3.5, 4.0, 3.5], [4.0, 4.5, 4.0, 4.5, 5.0, 4.5, 4.0], None, None),
    ([4.0, 4.0, 3.5, 4.0, 4.5, 4.0, 4.0], [5.0, 5.5, 5.0, 5.0, 6.0, 5.5, 5.0], None, None),
    ([4.5, 5.0, 5.0, 4.5, 5.0, 5.5, 5.0], [5.5, 6.0, 9.0, 5.5, 6.0, 6.5, 6.0], VB_ACAO, 'JP'),
    ([-18.0, -18.0, -17.0, -18.0, -18.0, -17.0, -18.0], [-17.0, -16.0, -17.0, -17.0, -16.0, -17.0, -17.0], None, None),
    ([-21.0, -20.0, -21.0, -21.0, -20.0, -21.0, -21.0], [-20.0, -19.0, -20.0, -20.0, -19.0, -20.0, -20.0], None, None),
]
VB_RUBRICAS = ['MS/JP'] * 7


def hm(h, m):
    return (h * 60 + m) / 1440


VB_BLOCOS = {  # {coluna: valor}
    'conf': {1: 'Coxas de frango no forno', 2: datetime.date(2026, 11, 24), 3: hm(12, 15), 4: 78.0, 13: 'JP'},
    'arref': {1: 'Caldo de carne no abatedor', 2: datetime.date(2026, 11, 25), 3: hm(15, 0), 4: 85.0, 5: hm(16, 40),
              6: 4.0, 13: 'JP'},
    'reaq': {1: 'Feijoada, por dose', 2: datetime.date(2026, 11, 26), 3: hm(19, 10), 4: 74.0, 5: 'Sim', 13: 'MS'},
    'quente': {1: 'Sopa do dia em banho-maria', 2: datetime.date(2026, 11, 27), 3: hm(12, 30), 4: 70.0, 13: 'MS'},
}


def pt(s):
    """Tipografia portuguesa: espaço fixo entre número e unidade, depois de ≤/≥/± e em «n.º 251/91», «art. 5.º»."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    s = re.sub(r'(n\.º|art\.|Reg\.) (?=\d)', r'\1' + NB, s)
    s = re.sub(r'([≤≥±]) (?=[\d−])', r'\1' + NB, s)
    return re.sub(r'(\d) (°C|h|hora|horas|min|minutos|m³|%)(?![\wçãõáéíóúâêôà])', r'\1' + NB + r'\2', s)


def num_txt(ref):
    """Parte de fórmula: −12 → «−12» com o sinal menos tipográfico; 7 → «7»."""
    return f'IF({ref}<0,"−"&ABS({ref}),{ref})'


def texto_norma(mn, mx):
    """Parte de fórmula: (0, 7) → «0 a 7 °C»; (vazio, −18) → «−18 °C ou menos»; (vazio, 7) → «máx. 7 °C»."""
    return (f'IF(OR(NOT(ISNUMBER({mx})),AND({mn}<>"",NOT(ISNUMBER({mn})))),"",IF(ISNUMBER({mn}),{num_txt(mn)}&" a "&'
            f'{num_txt(mx)}&"{NB}°C",IF({mx}<0,"−"&ABS({mx})&"{NB}°C ou menos","máx. "&{mx}&"{NB}°C")))')


def texto_max(ref):
    return f'IF(NOT(ISNUMBER({ref})),"",IF({ref}<0,"−"&ABS({ref})&"{NB}°C ou menos","máx. "&{ref}&"{NB}°C"))'


def celula(ws, r, k, valor=None, fmt=None, ent=False, neg=False, fundo=None, wrap=True, meio=False, tam=None):
    c = ws.cell(row=r, column=k, value=pt(valor))
    c.border = borda
    if fmt:
        c.number_format = fmt
    if ent:
        c.fill = entrada
    elif fundo:
        c.fill = fundo
    if neg or tam:
        c.font = Font(bold=neg, size=tam or 11)
    c.alignment = Alignment(wrap_text=wrap, vertical='center' if meio else 'top', horizontal='center' if meio else None)
    return c


def juntar(ws, r, k1, k2, r2=None):
    if k2 > k1 or (r2 and r2 > r):
        ws.merge_cells(start_row=r, start_column=k1, end_row=r2 or r, end_column=k2)


def bordas(ws, r, k1, k2, fundo=None, r2=None):
    for z in range(r, (r2 or r) + 1):
        for k in range(k1, k2 + 1):
            ws.cell(row=z, column=k).border = borda
            if fundo:
                ws.cell(row=z, column=k).fill = fundo


def cabeca_folha(ws, titulo, explicacao, ultima, altura=30):
    ws['A1'] = pt(titulo)
    ws['A1'].font = Font(bold=True, size=16, color=OURO)
    ws['A1'].fill = preto
    juntar(ws, 1, 1, ultima)
    ws.row_dimensions[1].height = 24
    ws['A2'] = pt(explicacao)
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    juntar(ws, 2, 1, ultima)
    ws.row_dimensions[2].height = altura


def campos(ws, nomes, rotulo_ate, entrada_ate, valores=None):
    for i, nome in enumerate(nomes):
        r = 3 + i
        celula(ws, r, 1, nome, neg=True)
        bordas(ws, r, 1, rotulo_ate)
        juntar(ws, r, 1, rotulo_ate)
        celula(ws, r, rotulo_ate + 1, valores[i] if valores else None, ent=True)
        bordas(ws, r, rotulo_ate + 1, entrada_ate)
        juntar(ws, r, rotulo_ate + 1, entrada_ate)


def cabecalho(ws, r, titulos, altura=32):
    """titulos: lista de (texto, k1, k2)."""
    for texto, k1, k2 in titulos:
        c = ws.cell(row=r, column=k1, value=pt(texto))
        c.font = Font(bold=True, color='FFFFFF')
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        bordas(ws, r, k1, k2, preto)
        juntar(ws, r, k1, k2)
    ws.row_dimensions[r].height = altura


def notas(ws, r, textos, ultima, altura=30):
    for i, n in enumerate(textos):
        c = ws.cell(row=r + i, column=1, value=pt(n))
        c.font = Font(italic=True, color='555555')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        juntar(ws, r + i, 1, ultima)
        ws.row_dimensions[r + i].height = altura
    return r + len(textos)


def ligacoes(ws, r, ultima, ate=2):
    for i, (rotulo, url) in enumerate((('O que é o HACCP na restauração:', ARTIGO),
                                       ('Como medir, registar e verificar o termómetro:', ARTIGO_TEMP))):
        ws.cell(row=r + i, column=1, value=pt(rotulo)).font = Font(bold=True)
        juntar(ws, r + i, 1, ate)
        c = ws.cell(row=r + i, column=ate + 1, value=url)
        c.hyperlink = url
        c.font = Font(color='0563C1', underline='single')
        juntar(ws, r + i, ate + 1, ultima)


def pagina(ws, fixar, larguras, quebras=()):
    for k, w in larguras.items():
        ws.column_dimensions[k].width = w
    ws.sheet_view.showGridLines = False
    if fixar:
        ws.freeze_panes = fixar
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    for r in quebras:
        ws.row_breaks.append(Break(id=r))


def _dv(ws, intervalo, **kw):
    dv = DataValidation(allow_blank=True, showErrorMessage=True, **kw)
    ws.add_data_validation(dv)
    for b in intervalo.split():
        dv.add(b)


def valida_temp(ws, intervalo, mini, maxi):
    _dv(ws, intervalo, type='decimal', operator='between', formula1=str(mini), formula2=str(maxi),
        errorTitle='Temperatura', error=f'Introduza uma temperatura (°C) entre {mini} e {maxi}, por exemplo 3,5 ou -18.')


def valida_inteiro(ws, intervalo, mini, maxi, titulo):
    _dv(ws, intervalo, type='whole', operator='between', formula1=str(mini), formula2=str(maxi), errorTitle=titulo,
        error=f'Introduza um número inteiro entre {mini} e {maxi}.')


def valida_hora(ws, intervalo):
    _dv(ws, intervalo, type='time', operator='between', formula1='0', formula2='0.999305556', errorTitle='Hora',
        error='Introduza uma hora no formato hh:mm (por exemplo, 14:30).')


def valida_data(ws, intervalo):
    _dv(ws, intervalo, type='date', operator='greaterThanOrEqual', formula1='36526', errorTitle='Data',
        error='Introduza uma data, por exemplo 25/11/2026.')


def cf_vermelho(ws, intervalo, formula):
    ws.conditional_formatting.add(intervalo, FormulaRule(formula=[formula], fill=vermelho))


def cf_nao(ws, intervalo):
    ws.conditional_formatting.add(intervalo, CellIsRule(operator='equal', formula=['"NÃO"'], fill=vermelho,
                                                        font=Font(bold=True)))


def nao_num(*refs):
    """Parte de fórmula, VERDADEIRO se uma das células não for um número (vazia ou texto). Necessário porque o Excel
    considera o texto maior do que qualquer número: «abc» >= 65 é VERDADEIRO e dava «Sim»."""
    return 'OR(' + ','.join(f'NOT(ISNUMBER({r}))' for r in refs) + ')'


# ------------------------------------------------------------------ tabela de equipamentos + bloco semanal
def tabela_equipamentos(ws):
    for (a, b), txt in (((1, 1), 'Equipamento'), ((2, 4), 'Nome (editável)'), ((5, 5), 'Mínimo (°C)'),
                        ((6, 6), 'Máximo (°C)'), ((7, 13), 'Origem da norma')):
        celula(ws, T0, a, txt, neg=True, fundo=cinza)
        bordas(ws, T0, a, b, cinza)
        juntar(ws, T0, a, b)
    ws.row_dimensions[T0].height = 30
    lei, cong, refr = pt(ORIG_LEI), pt(ORIG_CONG), pt(ORIG_REFR)
    for i, (nome, mn, mx) in enumerate(EQUIPAMENTOS):
        r = T0 + 1 + i
        celula(ws, r, 1, f'Equipamento {i + 1}', neg=True)
        celula(ws, r, 2, nome, ent=True)
        bordas(ws, r, 2, 4)
        juntar(ws, r, 2, 4)
        celula(ws, r, 5, mn, '0', ent=True, neg=True, meio=True)
        celula(ws, r, 6, mx, '0', ent=True, neg=True, meio=True)
        c = celula(ws, r, 7, f'=IF(NOT(ISNUMBER(F{r})),"",IF(F{r}<=-18,"{lei}",IF(F{r}<0,"{cong}","{refr}")))', tam=9)
        c.alignment = Alignment(vertical='center', wrap_text=True)
        bordas(ws, r, 7, 13)
        juntar(ws, r, 7, 13)
        ws.row_dimensions[r].height = 18
    valida_inteiro(ws, f'E{T0 + 1}:F{T0 + N_EQ}', -40, 30, 'Norma')


def formula_frio(z1, z2, t):
    # MAX e COUNT ignoram texto: «9,0» escrito como texto dava «Sim» → texto no intervalo deixa vazio
    rng, mn, mx = f'D{z1}:J{z2}', f'$E${t}', f'$F${t}'
    return (f'=IF(OR(NOT(ISNUMBER({mx})),AND({mn}<>"",NOT(ISNUMBER({mn}))),COUNT({rng})=0,'
            f'SUMPRODUCT(--ISTEXT({rng}))>0),"",IF(AND(MAX({rng})<={mx},IF({mn}="",TRUE,MIN({rng})>={mn})),'
            f'"Sim","NÃO"))')


def bloco_semana(ws, r, semana=None, dados=None, rubricas=None):
    c = ws.cell(row=r, column=1, value='Semana')
    c.font = Font(bold=True, color=OURO)
    c.fill = preto
    c.border = borda
    c.alignment = Alignment(horizontal='right', vertical='center')
    celula(ws, r, 2, semana, '0', ent=True, neg=True, meio=True)
    b = ws.cell(row=r, column=3, value=pt('Leitura diária (°C): pelo menos uma vez por dia, à abertura (código da '
                                          'AHRESP); a leitura do fecho é opcional'))
    b.font = Font(italic=True, color='FFFFFF')
    b.alignment = Alignment(vertical='center')
    bordas(ws, r, 3, 13, preto)
    juntar(ws, r, 3, 13)
    ws.row_dimensions[r].height = 20
    cabecalho(ws, r + 1, [(tx, k, k) for k, tx in enumerate(CAB_FRIO, start=1)])
    e = r + 2
    for i in range(N_EQ):
        z1, z2, t = e + 2 * i, e + 2 * i + 1, T0 + 1 + i
        ab, fe, acao, rub = dados[i] if dados else ([None] * 7, [None] * 7, None, None)
        celula(ws, z1, 1, f'=IF($B${t}="","",$B${t})', neg=True)
        ws.cell(row=z1, column=1).alignment = Alignment(vertical='center', wrap_text=True)
        celula(ws, z1, 2, f'={texto_norma(f"$E${t}", f"$F${t}")}', meio=True)
        celula(ws, z1, 3, 'Abertura', meio=True, tam=9)
        celula(ws, z2, 3, 'Fecho (opcional)', meio=True, tam=9)
        for z, leituras in ((z1, ab), (z2, fe)):
            for k, w in enumerate(leituras, start=4):
                celula(ws, z, k, w, F_TEMP, ent=True, meio=True)
        celula(ws, z1, 11, formula_frio(z1, z2, t), meio=True)
        celula(ws, z1, 12, acao, ent=True)
        ws.cell(row=z1, column=12).alignment = Alignment(wrap_text=True, vertical='center')
        celula(ws, z1, 13, rub, ent=True, meio=True)
        bordas(ws, z1, 1, 2, r2=z2)
        bordas(ws, z1, 11, 13, r2=z2)
        for k in (12, 13):
            ws.cell(row=z2, column=k).fill = entrada
        for k in (1, 2, 11, 12, 13):
            juntar(ws, z1, k, k, z2)
        altura = 15 * math.ceil(len(acao) / 38) + 6 if acao else 40
        ws.row_dimensions[z1].height = ws.row_dimensions[z2].height = max(20, altura / 2)
    zr = e + 2 * N_EQ
    celula(ws, zr, 1, 'Rubrica de quem leu', neg=True, fundo=cinza)
    bordas(ws, zr, 1, 3, cinza)
    juntar(ws, zr, 1, 3)
    for k in range(4, 11):
        celula(ws, zr, k, rubricas[k - 4] if rubricas else None, ent=True, meio=True, tam=9)
    bordas(ws, zr, 11, 13, cinza)
    juntar(ws, zr, 11, 13)
    ws.row_dimensions[zr].height = 20
    valida_temp(ws, f'D{e}:J{zr - 1}', -40, 30)
    valida_inteiro(ws, f'B{r}', 1, 53, 'Número da semana')
    for i in range(N_EQ):  # a norma de cada equipamento está na tabela do topo (a coluna B é texto)
        z1, t = e + 2 * i, T0 + 1 + i
        cf_vermelho(ws, f'D{z1}:J{z1 + 1}', f'AND(ISNUMBER(D{z1}),ISNUMBER($F${t}),OR(D{z1}>$F${t},'
                                            f'AND(ISNUMBER($E${t}),D{z1}<$E${t})))')
    cf_nao(ws, f'K{e}:K{zr - 1}')
    return e


# ------------------------------------------------------------------ operações a quente (também no «Exemplo»)
def faixa(tipo, v):
    if tipo == 'conf':
        return f'="Confeção – pelo menos "&{v["conf_t"]}&"{NB}°C no centro do alimento, na parte mais espessa"'
    if tipo == 'arref':
        return (f'="Arrefecimento – até "&{v["arref_t"]}&"{NB}°C em "&{v["arref_d"]}&IF({v["arref_d"]}=1,"{NB}hora",'
                f'"{NB}horas")&" ou menos"')
    if tipo == 'reaq':
        return f'="Reaquecimento – pelo menos "&{v["reaq_t"]}&"{NB}°C no centro, uma só vez"'
    return (f'="Manutenção a quente – pelo menos "&{v["quente_t"]}&"{NB}°C, medidos no alimento e não na água do '
            f'banho-maria"')


def formula_bloco(tipo, tipo_col, z, v):
    if tipo in ('conf', 'quente'):
        n = v['conf_t' if tipo == 'conf' else 'quente_t']
        return f'=IF({nao_num(f"D{z}", n)},"",IF(D{z}>={n},"Sim","NÃO"))'
    if tipo == 'arref':
        if tipo_col == 'dur':
            return f'=IF({nao_num(f"C{z}", f"E{z}")},"",MOD(E{z}-C{z},1))'
        # início, fim e temperatura final são necessários; a temperatura no início é opcional, mas texto nela → vazio
        falta = nao_num(f'G{z}', f'F{z}', v['arref_d'], v['arref_t'])
        return (f'=IF(OR({falta},AND(D{z}<>"",NOT(ISNUMBER(D{z})))),"",IF(AND(ROUND(G{z}*1440,0)<={v["arref_d"]}*60,'
                f'F{z}<={v["arref_t"]}),"Sim","NÃO"))')
    # reaquecimento: temperatura + «1.º reaquecimento?» (Sim/Não) necessários; «Não» = já reaquecido → NÃO
    return (f'=IF(OR({nao_num(f"D{z}", v["reaq_t"])},AND(E{z}<>"Sim",E{z}<>"Não")),"",'
            f'IF(AND(D{z}>={v["reaq_t"]},E{z}="Sim"),"Sim","NÃO"))')


def bloco_quente(ws, r, tipo, n, v, dados=None):
    b = ws.cell(row=r, column=1, value=faixa(tipo, v))
    b.font = Font(bold=True, size=12, color=OURO)
    b.alignment = Alignment(vertical='center')
    bordas(ws, r, 1, 13, preto)
    juntar(ws, r, 1, 13)
    ws.row_dimensions[r].height = 22
    cols = COLS[tipo]
    cabecalho(ws, r + 1, [(tx, k1, k2) for tx, k1, k2, _ in cols], altura=58)
    e = r + 2
    for z in range(e, e + n):
        for _, k1, k2, tc in cols:
            w = dados.get(k1) if dados else None
            if tc in ('ok', 'dur'):
                celula(ws, z, k1, formula_bloco(tipo, tc, z, v), F_DUR if tc == 'dur' else None, meio=True)
                bordas(ws, z, k1, k2)
            else:
                fmt = {'data': F_DATA, 'hora': F_HORA, 'temp': F_TEMP}.get(tc)
                celula(ws, z, k1, w, fmt, ent=True, meio=tc != 'texto')
                if tc == 'texto':
                    ws.cell(row=z, column=k1).alignment = Alignment(wrap_text=True, vertical='center')
                for k in range(k1 + 1, k2 + 1):
                    ws.cell(row=z, column=k).border = borda
                    ws.cell(row=z, column=k).fill = entrada
            juntar(ws, z, k1, k2)
        ws.row_dimensions[z].height = 30 if dados else 22
    l = e + n - 1
    por_tipo = {s: [] for s in ('data', 'hora', 'temp', 'simnao')}
    for _, k1, _, tc in cols:
        if tc in por_tipo:
            por_tipo[tc].append(k1)
    letra = ' ABCDEFGHIJKLM'
    rng = lambda tc: ' '.join(f'{letra[k]}{e}:{letra[k]}{l}' for k in por_tipo[tc])  # noqa: E731
    valida_data(ws, rng('data'))
    valida_hora(ws, rng('hora'))
    valida_temp(ws, rng('temp'), -30, 110)
    if por_tipo['simnao']:
        _dv(ws, rng('simnao'), type='list', formula1='"Sim,Não"', errorTitle='1.º reaquecimento',
            error='Escolha Sim (primeiro reaquecimento) ou Não (já tinha sido reaquecido).')
    ok = letra[OK_COL[tipo]]
    cf_nao(ws, f'{ok}{e}:{ok}{l}')
    if tipo == 'conf':
        regras = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["conf_t"]})')]
    elif tipo == 'quente':
        regras = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["quente_t"]})')]
    elif tipo == 'arref':
        regras = [('F', f'AND(ISNUMBER(F{e}),F{e}>{v["arref_t"]})'),
                  ('G', f'AND(ISNUMBER(G{e}),G{e}*1440>{v["arref_d"]}*60+0.5)')]
    else:
        regras = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["reaq_t"]})'), ('E', f'E{e}="Não"')]
    for k, f in regras:
        cf_vermelho(ws, f'{k}{e}:{k}{l}', f)
    return e


# ------------------------------------------------------------------ Folha 1: Frio
def folha_frio(wb):
    ws = wb.create_sheet('Frio')
    cabeca_folha(ws, 'Registo de temperaturas – frio (câmaras, frigoríficos e arcas)',
                 'Preencha as células amarelas. Leia a temperatura de cada equipamento pelo menos uma vez por dia, à '
                 'abertura; a leitura do fecho é opcional. «Conforme?» preenche-se automaticamente; se houver um '
                 'desvio, anote a ação corretiva e a rubrica.', 13)
    campos(ws, ['Estabelecimento', 'Semana/mês', 'Responsável'], 1, 6)
    tabela_equipamentos(ws)
    notas(ws, T0 + N_EQ + 1, ['Escreva aqui os seus equipamentos e as normas do seu plano; passam sozinhos para as '
                              'semanas abaixo. Mínimo vazio = sem limite inferior (arcas).', NOTA_PESCADO], 13, 18)
    inicios = [bloco_semana(ws, W0 + j * BLOCO) for j in range(N_SEMANAS)]
    fim = notas(ws, W0 + N_SEMANAS * BLOCO, [NOTA_LEI, NOTA_AHRESP_FRIO, NOTA_FECHO, NOTA_VERMELHO, NOTA_VOLUNTARIO,
                                              NOTA_REGISTADOR, NOTA_GUARDAR, NOTA_AUXILIAR], 13)
    ligacoes(ws, fim + 1, 13)
    pagina(ws, None, LARG_GRELHA, quebras=[W0 + (j + 1) * BLOCO - 1 for j in range(N_SEMANAS - 1)])
    return inicios


# ------------------------------------------------------------------ Folha 2: Confeção e arrefecimento
def folha_quente(wb):
    ws = wb.create_sheet('Confeção e arrefecimento')
    cabeca_folha(ws, 'Registo de temperaturas – confeção, arrefecimento, reaquecimento e manutenção a quente',
                 'Preencha as células amarelas (horas no formato hh:mm). A duração e «Conforme?» calculam-se '
                 'automaticamente com as normas da tabela abaixo; se houver um desvio, anote a ação corretiva e a '
                 'rubrica.', 13)
    campos(ws, ['Estabelecimento', 'Semana/mês', 'Responsável'], 1, 6)
    for (a, b), txt in (((1, 4), 'Norma (editável)'), ((5, 5), 'Valor'), ((6, 7), 'Unidade'), ((8, 13), 'Origem')):
        celula(ws, N0, a, txt, neg=True, fundo=cinza)
        bordas(ws, N0, a, b, cinza)
        juntar(ws, N0, a, b)
    for i, (_, texto, valor, unidade, origem) in enumerate(NORMAS):
        r = N0 + 1 + i
        celula(ws, r, 1, texto)
        bordas(ws, r, 1, 4)
        juntar(ws, r, 1, 4)
        celula(ws, r, 5, valor, ent=True, neg=True, meio=True)
        celula(ws, r, 6, unidade)
        bordas(ws, r, 6, 7)
        juntar(ws, r, 6, 7)
        celula(ws, r, 8, origem, tam=9)
        bordas(ws, r, 8, 13)
        juntar(ws, r, 8, 13)
        ws.row_dimensions[r].height = 18
    temps = ' '.join(V[k].replace('$', '') for k in ('conf_t', 'arref_t', 'reaq_t', 'quente_t'))
    valida_inteiro(ws, temps, -30, 110, 'Norma')
    valida_inteiro(ws, V['arref_d'].replace('$', ''), 1, 24, 'Horas')
    rn = N0 + len(NORMAS) + 1
    for j, (txt, alt) in enumerate(((NOTA_AHRESP_QUENTE, 44), (NOTA_PLANO, 30))):
        c = ws.cell(row=rn + j, column=1, value=pt(txt))
        c.font = Font(bold=True, italic=True, color='555555')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        juntar(ws, rn + j, 1, 13)
        ws.row_dimensions[rn + j].height = alt
    inicios, r, quebras = {}, rn + 3, []
    for tipo in ORDEM:
        inicios[tipo] = bloco_quente(ws, r, tipo, N_LINHAS, V)
        r += N_LINHAS + 3
        if tipo in ('conf', 'reaq'):
            quebras.append(r - 1)
    fim = notas(ws, r, [
        '«Conforme?» compara com as normas do topo (células amarelas). A duração conta a passagem da meia-noite.',
        'Arrefecimento: anote a hora a que começa a arrefecer e a hora e a temperatura da medição final; a temperatura '
        'no início é opcional.',
        'Reaquecimento: o código da AHRESP admite um único reaquecimento. Se o alimento já tinha sido reaquecido, '
        'escolha «Não» na coluna «1.º reaquecimento?» e anote a ação corretiva.',
        'Manutenção a quente: meça no alimento, não na água do banho-maria. O alimento confecionado exposto mais de 2 '
        'horas abaixo dos 65 °C elimina-se (código da AHRESP).',
        '«Conforme?» fica vazio enquanto faltar um dado necessário ou se houver texto onde deve estar um número.',
        NOTA_VOLUNTARIO, NOTA_GUARDAR, NOTA_AUXILIAR], 13, 18)
    ligacoes(ws, fim + 1, 13)
    pagina(ws, None, LARG_GRELHA, quebras=quebras)
    return inicios


# ------------------------------------------------------------------ Folha 3: Receção
def norma_rececao(z, refs, forma=lambda r: r):
    """Norma do tipo escolhido na coluna D (número, ou com forma=texto_max o texto); tipo desconhecido → ""."""
    f = '""'
    for (tipo, _, _), ref in reversed(list(zip(RECECAO, refs))):
        f = f'IF(D{z}="{tipo}",{forma(ref)},{f})'
    return f


def folha_rececao(wb):
    ws = wb.create_sheet('Receção')
    cabeca_folha(ws, 'Registo de temperaturas – receção de mercadoria',
                 'Meça a temperatura dos produtos refrigerados e congelados à chegada, antes de assinar a guia. Escolha '
                 'o tipo na lista; a norma e «Conforme?» preenchem-se automaticamente.', 9)
    campos(ws, ['Estabelecimento', 'Semana/mês', 'Responsável'], 1, 3)
    for (a, b), txt in (((1, 2), 'Tipo'), ((3, 3), 'Máximo (°C)'), ((4, 9), 'Origem da norma')):
        celula(ws, R0, a, txt, neg=True, fundo=cinza)
        bordas(ws, R0, a, b, cinza)
        juntar(ws, R0, a, b)
    for i, (tipo, norma, origem) in enumerate(RECECAO):
        r = R0 + 1 + i
        celula(ws, r, 1, tipo, neg=True)
        bordas(ws, r, 1, 2)
        juntar(ws, r, 1, 2)
        celula(ws, r, 3, norma, '0', ent=True, neg=True, meio=True)
        celula(ws, r, 4, origem, tam=9)
        bordas(ws, r, 4, 9)
        juntar(ws, r, 4, 9)
        ws.row_dimensions[r].height = 18
    valida_inteiro(ws, f'C{R0 + 1}:C{R0 + len(RECECAO)}', -40, 30, 'Norma')
    notas(ws, R0 + len(RECECAO) + 1, [NOTA_RECECAO], 9, 30)
    cabecalho(ws, R_CAB, [(tx, k, k) for k, tx in enumerate(
        ['Data', 'Fornecedor', 'Produto', 'Tipo', 'Norma', 'Temperatura medida (°C)', 'Conforme?',
         'Desvio e ação (por exemplo, recusado ou devolvido ao fornecedor)', 'Rubrica'], start=1)], altura=36)
    e, l = R_CAB + 1, R_CAB + R_N
    refs = [f'$C${R0 + 1 + i}' for i in range(len(RECECAO))]
    for z in range(e, l + 1):
        celula(ws, z, 1, None, F_DATA, ent=True, meio=True)
        celula(ws, z, 2, None, ent=True)
        celula(ws, z, 3, None, ent=True)
        celula(ws, z, 4, None, ent=True, meio=True)
        celula(ws, z, 5, '=' + norma_rececao(z, refs, texto_max), meio=True)
        celula(ws, z, 6, None, F_TEMP, ent=True, meio=True)
        norma = norma_rececao(z, refs)
        celula(ws, z, 7, f'=IF(OR(E{z}="",{nao_num(f"F{z}", norma)}),"",IF(F{z}<={norma},"Sim","NÃO"))', meio=True)
        celula(ws, z, 8, None, ent=True)
        celula(ws, z, 9, None, ent=True, meio=True)
        ws.row_dimensions[z].height = 30
    valida_data(ws, f'A{e}:A{l}')
    _dv(ws, f'D{e}:D{l}', type='list', formula1='"' + ','.join(tp for tp, _, _ in RECECAO) + '"', errorTitle='Tipo',
        error='Escolha um tipo da lista: ' + ', '.join(tp for tp, _, _ in RECECAO[:-1]) + f' ou {RECECAO[-1][0]}.')
    valida_temp(ws, f'F{e}:F{l}', -40, 30)
    cf_vermelho(ws, f'F{e}:F{l}', f'AND(ISNUMBER(F{e}),E{e}<>"",F{e}>{norma_rececao(e, refs)})')
    cf_nao(ws, f'G{e}:G{l}')
    fim = notas(ws, l + 2, [NOTA_GUARDAR, NOTA_AUXILIAR], 9, 18)
    ligacoes(ws, fim + 1, 9)
    pagina(ws, f'A{e}', {'A': 13, 'B': 22, 'C': 24, 'D': 34, 'E': 16, 'F': 13, 'G': 11, 'H': 44, 'I': 9})
    return e


# ------------------------------------------------------------------ Folha 4: Termómetro
def folha_termometro(wb):
    ws = wb.create_sheet('Termómetro')
    cabeca_folha(ws, 'Verificação dos termómetros e das sondas',
                 'Verifique cada termómetro e cada sonda com a periodicidade que o seu plano definir, por exemplo num '
                 'copo com gelo fundente (0 °C). Preencha as células amarelas; o desvio e «Conforme?» calculam-se '
                 'automaticamente.', 8)
    campos(ws, ['Estabelecimento', 'Ano', 'Periodicidade (a do seu plano)', 'Responsável'], 2, 5)
    celula(ws, TH_TOL, 1, 'Tolerância (+ ou −)', neg=True, fundo=cinza)
    bordas(ws, TH_TOL, 1, 2, cinza)
    juntar(ws, TH_TOL, 1, 2)
    celula(ws, TH_TOL, 3, 1.0, f'"±{NB}"0.0"{NB}°C"', ent=True, neg=True, meio=True)
    celula(ws, TH_TOL, 4, NOTA_TOLERANCIA, tam=9)
    bordas(ws, TH_TOL, 4, 8)
    juntar(ws, TH_TOL, 4, 8)
    ws.row_dimensions[TH_TOL].height = 30
    _dv(ws, f'C{TH_TOL}', type='decimal', operator='between', formula1='0.1', formula2='5', errorTitle='Tolerância',
        error='Introduza uma tolerância (°C) entre 0,1 e 5.')
    cabecalho(ws, TH_CAB, [(tx, k, k) for k, tx in enumerate(
        ['Data', 'Termómetro ou sonda (nome ou número)', 'Referência (°C)', 'Medido (°C)', 'Desvio (°C)', 'Conforme?',
         'Ação corretiva (se houver desvio)', 'Rubrica'], start=1)], altura=36)
    e, l = TH_CAB + 1, TH_CAB + TH_N
    n = f'$C${TH_TOL}'
    for z in range(e, l + 1):
        celula(ws, z, 1, None, F_DATA, ent=True, meio=True)
        celula(ws, z, 2, None, ent=True)
        celula(ws, z, 3, 0, F_TEMP, ent=True, meio=True)  # gelo fundente; outra referência: escrever por cima
        celula(ws, z, 4, None, F_TEMP, ent=True, meio=True)
        celula(ws, z, 5, f'=IF({nao_num(f"C{z}", f"D{z}")},"",ROUND(D{z}-C{z},1))', F_DESV, meio=True)
        celula(ws, z, 6, f'=IF({nao_num(f"E{z}", n)},"",IF(ABS(E{z})<={n},"Sim","NÃO"))', meio=True)
        celula(ws, z, 7, None, ent=True)
        celula(ws, z, 8, None, ent=True, meio=True)
        ws.row_dimensions[z].height = 22
    valida_data(ws, f'A{e}:A{l}')
    valida_temp(ws, f'C{e}:D{l}', -30, 110)
    cf_vermelho(ws, f'D{e}:E{l}', f'AND(ISNUMBER($C{e}),ISNUMBER($D{e}),ABS(ROUND($D{e}-$C{e},1))>{n})')
    cf_nao(ws, f'F{e}:F{l}')
    fim = notas(ws, l + 2, [
        'Gelo fundente: um copo cheio de gelo com um pouco de água fria; mergulhe a sonda no centro e espere que a '
        'leitura estabilize. A referência é 0 °C. Se usar outra referência, como outro termómetro calibrado, escreva-a '
        'na coluna «Referência».',
        'Se o desvio for maior do que a tolerância, ajuste ou substitua o termómetro e anote-o como ação corretiva.',
        NOTA_GUARDAR, NOTA_AUXILIAR], 8, 30)
    ligacoes(ws, fim + 1, 8)
    pagina(ws, f'A{e}', {'A': 13, 'B': 30, 'C': 14, 'D': 13, 'E': 13, 'F': 11, 'G': 46, 'H': 9})
    return e


# ------------------------------------------------------------------ Folha 5: Exemplo
def folha_exemplo(wb):
    ws = wb.create_sheet('Exemplo')
    cabeca_folha(ws, 'Exemplo – uma semana preenchida (fictícia)',
                 'Assim pode ficar uma semana preenchida, com um desvio e a respetiva ação corretiva (quarta-feira, '
                 'bancada refrigerada, ao fecho). Para o seu registo, use as outras folhas.', 13)
    campos(ws, ['Estabelecimento', 'Semana/mês', 'Responsável'], 1, 6, VB_CAMPOS)
    tabela_equipamentos(ws)
    e = bloco_semana(ws, W0, VB_SEMANA, VB_FRIO, VB_RUBRICAS)
    r, inicios = W0 + BLOCO, {}
    for tipo in ORDEM:
        inicios[tipo] = bloco_quente(ws, r, tipo, 1, V_LIT, VB_BLOCOS[tipo])
        r += 4
    fim = notas(ws, r, ['Exemplo fictício para ilustrar: estabelecimento, nomes e leituras são inventados.',
                        NOTA_AUXILIAR], 13, 18)
    ligacoes(ws, fim + 1, 13)
    pagina(ws, None, LARG_GRELHA, quebras=(W0 + BLOCO - 1,))
    return e, inicios


# ------------------------------------------------------------------ PDF para imprimir
TIPOS_PDF = [('Refrigeração', '0 a 7 °C')] * 3 + [('Congelados (exceto pescado)', '−12 °C ou menos'),
                                                   ('Ultracongelados e pescado', '−18 °C ou menos')]


def pdf_imprimir():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """Texto do PDF: tipografia portuguesa + WinAnsi da Helvetica (ç, ã, õ, «», –, °, ³). O sinal menos U+2212 não
        existe em WinAnsi: é trocado pelo travessão «–». ≤ e ≥ também não: no PDF escrevem-se por extenso."""
        s = pt(s).replace('−', '–')
        s.encode('cp1252')  # UnicodeEncodeError se um carácter não for imprimível (≤, ≥ …)
        return s

    linha, pr, ouro = colors.HexColor('#999999'), colors.HexColor('#111111'), colors.HexColor('#FFD700')
    cz = colors.HexColor('#F3F3F3')
    s_h = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=10.5, leading=12.5, spaceBefore=5, spaceAfter=1,
                         textColor=pr)
    s_txt = ParagraphStyle('t', fontName='Helvetica', fontSize=8, leading=10)
    s_nota = ParagraphStyle('n', fontName='Helvetica-Oblique', fontSize=7.3, leading=9,
                            textColor=colors.HexColor('#333333'))
    s_th = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=7, leading=8, alignment=1, textColor=colors.white)
    s_lab = ParagraphStyle('lab', fontName='Helvetica', fontSize=6.5, leading=7.5, textColor=colors.HexColor('#777777'))
    s_norma = ParagraphStyle('norma', fontName='Helvetica-Bold', fontSize=7, leading=8, alignment=1)
    s_leit = ParagraphStyle('leit', fontName='Helvetica', fontSize=6.5, leading=7.5, alignment=1,
                            textColor=colors.HexColor('#555555'))
    W = A4[0] - 28 * mm

    def faixa_pdf(texto, tam=13):
        assert stringWidth(t(texto), 'Helvetica-Bold', tam) < W - 12, texto  # uma linha, dentro da faixa
        b = Table([[t(texto)]], colWidths=[W])
        b.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), pr), ('TEXTCOLOR', (0, 0), (-1, -1), ouro),
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), tam),
                               ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
        return b

    def rodape(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 7.5)
        canvas.setFillColor(colors.HexColor('#555555'))
        canvas.drawCentredString(A4[0] / 2, 7 * mm, t(RODAPE))
        canvas.restoreState()

    def info():
        tb = Table([['Estabelecimento:', '', 'Responsável:', '']], colWidths=[W * 0.17, W * 0.38, W * 0.15, W * 0.3],
                   rowHeights=17)
        tb.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                                ('LINEBELOW', (1, 0), (1, 0), 0.5, linha), ('LINEBELOW', (3, 0), (3, 0), 0.5, linha),
                                ('VALIGN', (0, 0), (-1, -1), 'BOTTOM')]))
        return tb

    def cabe(textos, props, fonte, tam, margem):
        """Nenhuma palavra pode ser partida a meio numa coluna estreita («Abertur a», «Conform e?»)."""
        for tx, p in zip(textos, props):
            for palavra in t(tx).split():
                assert stringWidth(palavra, fonte, tam) <= W * p - margem, (palavra, p)

    def grelha(cabs, props, n, altura=22, cab_h=26):
        assert abs(sum(props) - 1) < 1e-9, sum(props)
        cabe(cabs, props, 'Helvetica-Bold', 7, 4)
        tb = Table([[Paragraph(t(x), s_th) for x in cabs]] + [[''] * len(cabs) for _ in range(n)],
                   colWidths=[W * x for x in props], rowHeights=[cab_h] + [altura] * n)
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linha), ('BACKGROUND', (0, 0), (-1, 0), pr),
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
                                ('RIGHTPADDING', (0, 0), (-1, 0), 2), ('TOPPADDING', (0, 0), (-1, 0), 2),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 2)]))
        return tb

    def tabela_frio():
        cabs = ['Equipamento', 'Norma', 'Leitura'] + DIAS + ['Conforme? (sim/não)', 'Desvio e ação corretiva',
                                                           'Rubrica']
        props = [0.13, 0.09, 0.07] + [0.05] * 7 + [0.09, 0.21, 0.06]
        assert abs(sum(props) - 1) < 1e-9
        cabe(cabs, props, 'Helvetica-Bold', 7, 4)
        for tipo, norma in TIPOS_PDF:
            cabe([tipo + ':', norma, 'Abertura'], props[:3], 'Helvetica-Bold', 7, 6)
        linhas = [[Paragraph(t(x), s_th) for x in cabs]]
        est = [('GRID', (0, 0), (-1, -1), 0.5, linha), ('BACKGROUND', (0, 0), (-1, 0), pr),
               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
               ('RIGHTPADDING', (0, 0), (-1, 0), 2), ('LEFTPADDING', (0, 1), (-1, -1), 3),
               ('RIGHTPADDING', (0, 1), (-1, -1), 3), ('LINEAFTER', (2, 0), (2, -1), 1.2, pr),
               ('LINEAFTER', (9, 0), (9, -1), 1.2, pr)]
        for i, (tipo, norma) in enumerate(TIPOS_PDF):
            r1 = 1 + 2 * i
            linhas.append([Paragraph(t(tipo + ':'), s_lab), Paragraph(t(norma), s_norma), Paragraph('Abertura', s_leit)]
                          + [''] * 10)
            linhas.append(['', '', Paragraph('Fecho', s_leit)] + [''] * 10)
            est += [('SPAN', (k, r1), (k, r1 + 1)) for k in (0, 1, 10, 11, 12)]
            est += [('BACKGROUND', (1, r1), (1, r1 + 1), cz), ('VALIGN', (0, r1), (0, r1 + 1), 'TOP')]
            if i:
                est.append(('LINEABOVE', (0, r1), (-1, r1), 1.2 if i == 3 else 0.9, pr))
        rr = 1 + 2 * len(TIPOS_PDF)
        linhas.append([Paragraph(t('Rubrica de quem leu'), s_lab), '', ''] + [''] * 10)
        est += [('SPAN', (0, rr), (2, rr)), ('SPAN', (10, rr), (12, rr)), ('BACKGROUND', (10, rr), (12, rr), cz),
                ('LINEABOVE', (0, rr), (-1, rr), 1.2, pr)]
        tb = Table(linhas, colWidths=[W * x for x in props], rowHeights=[26] + [18] * (2 * len(TIPOS_PDF)) + [20])
        tb.setStyle(TableStyle(est))
        return tb

    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=11 * mm,
                            bottomMargin=14 * mm,
                            title=t('Registo de temperaturas HACCP: frio, confeção, arrefecimento, reaquecimento, '
                                    'receção e termómetros'),
                            author='AI Chef Pro',
                            subject=t('Câmaras, frigoríficos, arcas, confeção, arrefecimento, reaquecimento, '
                                      'manutenção a quente, receção de mercadoria e verificação dos termómetros'))
    # Página 1 — frio, duas semanas
    el = [faixa_pdf('Registo de temperaturas – frio (câmaras, frigoríficos e arcas)'), Spacer(1, 4), info(),
          Spacer(1, 4),
          Paragraph(t('Leia a temperatura de cada equipamento pelo menos uma vez por dia, à abertura (código da AHRESP); '
                      'a leitura do fecho é opcional. Se houver um desvio: ação corretiva e rubrica.'), s_txt)]
    for _ in range(2):
        el += [Paragraph(t('Semana: ……………    De ……………… a ………………'), s_h), tabela_frio()]
    el += [Spacer(1, 6), Paragraph(t(NOTA_LEI), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_AHRESP_FRIO + ' ' + NOTA_FECHO), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_PESCADO + ' Se o seu plano fixar outra norma (por exemplo, 0 a 4 °C com uma única câmara), '
                       'corrija-a à mão.'), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_VOLUNTARIO + ' ' + NOTA_REGISTADOR), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_GUARDAR + ' ' + NOTA_AUXILIAR), s_nota), PageBreak()]

    # Página 2 — confeção, arrefecimento, reaquecimento e manutenção a quente
    a7 = [0.09, 0.24, 0.07, 0.10, 0.09, 0.34, 0.07]
    el += [faixa_pdf('Confeção, arrefecimento, reaquecimento e manutenção a quente', 12), Spacer(1, 4), info(),
           Spacer(1, 2),
           Paragraph(t('<b>Semana: ……………</b>    Uma linha por medição. Se houver um desvio: ação corretiva e rubrica.'),
                     s_txt),
           Paragraph(t('Confeção'), s_h),
           Paragraph(t('Pelo menos 65 °C no centro do alimento, na parte mais espessa (código da AHRESP), ou ……… °C se o '
                       'seu plano for mais exigente (por exemplo, 75 °C).'), s_txt), Spacer(1, 2),
           grelha(['Data', 'Produto', 'Hora', 'Temp. no centro (°C)', 'Conforme? (sim/não)', 'Ação corretiva',
                   'Rubrica'], a7, 4),
           Paragraph(t('Arrefecimento'), s_h),
           Paragraph(t('Até 5 °C em 2 horas ou menos (código da AHRESP).'), s_txt), Spacer(1, 2),
           grelha(['Data', 'Produto', 'Hora de início', '°C no início (opcional)', 'Hora de fim', '°C no fim',
                   'Duração (h:mm)', 'Conforme? (sim/não)', 'Ação corretiva', 'Rubrica'],
                  [0.08, 0.17, 0.07, 0.08, 0.07, 0.07, 0.08, 0.09, 0.22, 0.07], 4, cab_h=34),
           Paragraph(t('Reaquecimento'), s_h),
           Paragraph(t('Pelo menos 65 °C no centro, uma só vez (código da AHRESP).'), s_txt), Spacer(1, 2),
           grelha(['Data', 'Produto', 'Hora', 'Temp. no centro (°C)', '1.º reaquecimento? (sim/não)',
                   'Conforme? (sim/não)', 'Ação corretiva', 'Rubrica'],
                  [0.09, 0.20, 0.07, 0.10, 0.12, 0.09, 0.26, 0.07], 4, cab_h=34),
           Paragraph(t('Manutenção a quente'), s_h),
           Paragraph(t('Pelo menos 65 °C, medidos no alimento e não na água do banho-maria. O alimento confecionado '
                       'exposto mais de 2 horas abaixo dos 65 °C elimina-se (código da AHRESP).'), s_txt),
           Spacer(1, 2),
           grelha(['Data', 'Produto', 'Hora', 'Temp. no alimento (°C)', 'Conforme? (sim/não)', 'Ação corretiva',
                   'Rubrica'], a7, 4),
           Spacer(1, 6),
           Paragraph(t('A lei portuguesa não fixa estas temperaturas: vêm do Código de Boas Práticas da AHRESP (2015, '
                       'pequena restauração e bebidas). Opção mais exigente do seu plano (não é lei nem código da '
                       'AHRESP): confeção a 75 °C no centro, como noutros códigos e guias.'), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_VOLUNTARIO + ' ' + NOTA_GUARDAR + ' ' + NOTA_AUXILIAR), s_nota), PageBreak()]

    def tabela_normas(linhas, props):
        tb = Table([[Paragraph(t(x), s_th) for x in ('Tipo', 'Norma', 'Origem')]]
                   + [[Paragraph(t(a), s_txt), Paragraph(t(b), s_norma), Paragraph(t(c), s_lab)] for a, b, c in linhas],
                   colWidths=[W * x for x in props])
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linha), ('BACKGROUND', (0, 0), (-1, 0), pr),
                                ('BACKGROUND', (1, 1), (1, -1), cz), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        return tb

    # Página 3 — receção de mercadoria (como a folha «Receção»)
    el += [faixa_pdf('Registo de temperaturas – receção de mercadoria'), Spacer(1, 4), info(), Spacer(1, 4),
           Paragraph(t('Meça a temperatura dos produtos refrigerados e congelados à chegada, antes de assinar a guia: '
                       'entre duas embalagens e, se houver dúvida, no centro do produto.'), s_txt), Spacer(1, 4),
           tabela_normas([(tp, f'−{abs(n)} °C ou menos' if n < 0 else f'máx. {n} °C', o) for tp, n, o in RECECAO],
                         [0.32, 0.18, 0.5]), Spacer(1, 3),
           Paragraph(t('As normas são as do armazenamento (lei e código da AHRESP); se o seu plano fixar outras, '
                       'corrija-as à mão.'), s_nota), Spacer(1, 4),
           grelha(['Data', 'Fornecedor', 'Produto', 'Tipo', 'Norma', 'Medido (°C)', 'Conforme? (sim/não)',
                   'Desvio e ação (por exemplo, recusado ou devolvido)', 'Rubrica'],
                  [0.08, 0.14, 0.15, 0.10, 0.08, 0.08, 0.09, 0.22, 0.06], 18, altura=25, cab_h=30),
           Spacer(1, 6), Paragraph(t(NOTA_GUARDAR + ' ' + NOTA_AUXILIAR), s_nota), PageBreak()]

    # Página 4 — verificação dos termómetros (como a folha «Termómetro»)
    el += [faixa_pdf('Verificação dos termómetros e das sondas'), Spacer(1, 4), info(), Spacer(1, 4),
           Paragraph(t('<b>Ano: ……………</b>    Periodicidade da verificação (a do seu plano): ………………………………'), s_txt),
           Spacer(1, 3),
           Paragraph(t('<b>Tolerância definida no seu plano: ± ………… °C</b>    (a ficha técnica do termómetro indica a do '
                       'fabricante)'), s_txt), Spacer(1, 6),
           grelha(['Data', 'Termómetro ou sonda (nome ou número)', 'Referência (°C)', 'Medido (°C)', 'Desvio (°C)',
                   'Conforme? (sim/não)', 'Ação corretiva (se houver desvio)', 'Rubrica'],
                  [0.09, 0.20, 0.09, 0.09, 0.09, 0.09, 0.29, 0.06], TH_N, altura=28, cab_h=30),
           Spacer(1, 6),
           Paragraph(t('Gelo fundente: um copo cheio de gelo com um pouco de água fria; mergulhe a sonda no centro e '
                       'espere que a leitura estabilize. A referência é 0 °C. Se usar outra referência, como outro '
                       'termómetro calibrado, escreva-a na coluna «Referência».'), s_nota), Spacer(1, 2),
           Paragraph(t('Se o desvio for maior do que a tolerância, ajuste ou substitua o termómetro e anote-o como ação '
                       'corretiva.'), s_nota), Spacer(1, 2),
           Paragraph(t(NOTA_GUARDAR + ' ' + NOTA_AUXILIAR), s_nota)]
    doc.build(el, onFirstPage=rodape, onLaterPages=rodape)


# ------------------------------------------------------------------ Gates
def cache_texto_vazio(ruta):
    """inject_cache.py não injeta o resultado «""»: a célula fica com cache vazia (<v></v>, lida como 0) e os
    visualizadores sem recálculo (Quick Look, telemóvel) mostram «0». Aqui escreve-se a cache «texto vazio» como no
    Excel (t="str" + <v></v>), sem tocar no resto do zip (igual ao gémeo NL)."""
    padrao = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(ruta) as z:
        partes = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(ruta) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, data in partes:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = padrao.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', data.decode('utf-8'))
                data, n = xml.encode('utf-8'), n + k
            zout.writestr(info, data)
    shutil.move(str(ruta) + '.tmp', str(ruta))
    return n


def injetar(ruta):
    saida = subprocess.run([sys.executable, str(INJECT), str(ruta)], check=True, capture_output=True, text=True).stdout
    assert 'fallos_pycel=0' in saida, saida
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+)', saida)
    vazias = cache_texto_vazio(ruta)
    assert int(m.group(1)) == int(m.group(2)) + vazias, (saida, vazias)  # cada fórmula tem cache (valor ou texto vazio)
    return f'{saida.strip()} cache_texto_vazio={vazias}'


FR, CQ, RC, TM, EX = 'Frio', 'Confeção e arrefecimento', 'Receção', 'Termómetro', 'Exemplo'


def testar(casos, normas=None, extra=()):
    """Valores de teste numa CÓPIA temporária (o ficheiro publicado fica vazio).
    casos: (folha, {(linha, coluna): valor}, (linha, coluna) do resultado, esperado, descrição)."""
    with tempfile.TemporaryDirectory() as tmp:
        copia = Path(tmp) / 'teste.xlsx'
        shutil.copy(XLSX, copia)
        wb = load_workbook(copia)
        for (folha, ref), w in (normas or {}).items():
            wb[folha][ref] = w
        for folha, valores, _, _, _ in casos:
            for (z, k), w in valores.items():
                wb[folha].cell(row=z, column=k).value = w  # cell(..., value=None) NÃO apagaria a célula
        wb.save(copia)
        injetar(copia)
        wv = load_workbook(copia, data_only=True)
        res = []
        for folha, _, (z, k), esp, desc in casos:
            w = wv[folha].cell(row=z, column=k).value
            res.append((folha, desc, esp, None if w == '' else w))
        ex = {(folha, z, k): wv[folha].cell(row=z, column=k).value for folha, z, k in extra}
    return res, ex


def minutos(d):
    return d.total_seconds() / 60 if hasattr(d, 'total_seconds') else d * 1440  # openpyxl lê [h]:mm como timedelta


def gate_logica(sem, qt, r1, t1, vb):
    def frio(w, i, abertura=None, fecho=None, extra=None):
        """Valores do equipamento i na semana w: abertura/fecho = {dia (0 = Seg): °C}."""
        z1 = sem[w] + 2 * i
        d = {(z1, 4 + k): v for k, v in (abertura or {}).items()}
        d.update({(z1 + 1, 4 + k): v for k, v in (fecho or {}).items()})
        d.update(extra or {})
        return d, (z1, 11)

    def caso_frio(w, i, esp, desc, **kw):
        d, ok = frio(w, i, **kw)
        return (FR, d, ok, esp, desc)

    def linha(folha, z, vals, k_ok, esp, desc):
        return (folha, {(z, k): v for k, v in vals.items()}, (z, k_ok), esp, desc)

    kk, ak, rk, qk = qt['conf'], qt['arref'], qt['reaq'], qt['quente']
    casos = [
        caso_frio(0, 0, 'Sim', 'câmara seg 3,5 °C (0 a 7)', abertura={0: 3.5}),
        caso_frio(0, 1, 'Sim', 'frigorífico ter 7,0 °C exatamente na norma', abertura={0: 4.0, 1: 7.0}, fecho={1: 5.0}),
        caso_frio(0, 2, 'NÃO', 'bancada qua ao fecho 7,1 °C', abertura={0: 4.0}, fecho={2: 7.1}),
        caso_frio(0, 3, 'Sim', 'congelados −12 e −13 °C (norma −12)', abertura={0: -12.0, 1: -13.0}),
        caso_frio(0, 4, 'Sim', 'ultracongelados −18 e −19 °C (norma −18)', abertura={0: -18.0}, fecho={0: -19.0}),
        caso_frio(1, 0, 'NÃO', 'câmara −0,5 °C (abaixo do mínimo 0)', abertura={0: -0.5}),
        caso_frio(1, 1, 'Sim', 'frigorífico 0,0 °C (mínimo incluído)', abertura={3: 0.0}),
        caso_frio(1, 3, 'NÃO', 'congelados −11,5 °C', abertura={4: -11.5}),
        caso_frio(1, 4, 'NÃO', 'ultracongelados dom ao fecho −17,5 °C', abertura={6: -20.0}, fecho={6: -17.5}),
        caso_frio(2, 0, 'Sim', 'só a leitura do fecho (5,0 °C) + rubricas do dia', fecho={4: 5.0},
                  extra={(sem[2] + 2 * N_EQ, 4 + k): 'MS' for k in range(7)}),
        caso_frio(2, 3, 'Sim', 'congelados −25 °C (sem mínimo)', abertura={0: -25.0}),
        caso_frio(2, 1, None, 'só ação corretiva e rubrica → vazio', extra={(sem[2] + 2, 12): 'texto', (sem[2] + 2, 13): 'MS'}),
        caso_frio(4, 4, None, 'linha vazia (semana 5) → vazio'),
        linha(CQ, kk + 0, {4: 65.0}, 5, 'Sim', 'confeção exatamente 65 °C'),
        linha(CQ, kk + 1, {4: 78.0}, 5, 'Sim', 'confeção 78 °C'),
        linha(CQ, kk + 2, {4: 64.9}, 5, 'NÃO', 'confeção 64,9 °C'),
        linha(CQ, kk + 3, {1: 'Frango', 3: hm(12, 0)}, 5, None, 'confeção sem temperatura → vazio'),
        linha(CQ, kk + 4, {4: 'oitenta'}, 5, None, 'confeção: texto como temperatura → vazio (dava «Sim»)'),
        linha(CQ, ak + 0, {3: hm(15, 0), 4: 85.0, 5: hm(16, 40), 6: 4.0}, 9, 'Sim', 'arrefecimento 1 h 40 até 4 °C'),
        linha(CQ, ak + 1, {3: hm(15, 0), 5: hm(17, 0), 6: 5.0}, 9, 'Sim',
              'arrefecimento exatamente 2 h e 5 °C, sem temperatura inicial'),
        linha(CQ, ak + 2, {3: hm(15, 0), 4: 80.0, 5: hm(17, 1), 6: 4.0}, 9, 'NÃO', 'arrefecimento 2 h 01'),
        linha(CQ, ak + 3, {3: hm(15, 0), 4: 80.0, 5: hm(16, 30), 6: 5.5}, 9, 'NÃO', 'arrefecimento fim a 5,5 °C'),
        linha(CQ, ak + 4, {3: hm(23, 30), 4: 80.0, 5: hm(1, 0), 6: 4.0}, 9, 'Sim',
              'arrefecimento 23:30 → 01:00 (meia-noite)'),
        linha(CQ, ak + 5, {3: hm(15, 0), 4: 80.0, 6: 4.0}, 9, None, 'arrefecimento sem hora de fim → vazio'),
        linha(CQ, ak + 6, {3: hm(17, 0), 5: hm(16, 0), 6: 4.0}, 9, 'NÃO', 'arrefecimento: horas trocadas (23 h)'),
        linha(CQ, ak + 7, {3: hm(15, 0), 4: 80.0, 5: hm(16, 0)}, 9, None, 'arrefecimento sem temperatura final → vazio'),
        linha(CQ, rk + 0, {4: 74.0, 5: 'Sim'}, 6, 'Sim', 'reaquecimento 74 °C, primeiro'),
        linha(CQ, rk + 1, {4: 65.0, 5: 'Sim'}, 6, 'Sim', 'reaquecimento exatamente 65 °C'),
        linha(CQ, rk + 2, {4: 64.5, 5: 'Sim'}, 6, 'NÃO', 'reaquecimento 64,5 °C'),
        linha(CQ, rk + 3, {4: 80.0, 5: 'Não'}, 6, 'NÃO', 'reaquecimento: já tinha sido reaquecido'),
        linha(CQ, rk + 4, {4: 80.0}, 6, None, 'reaquecimento sem «1.º reaquecimento?» → vazio'),
        linha(CQ, rk + 5, {5: 'Sim'}, 6, None, 'reaquecimento sem temperatura → vazio'),
        linha(CQ, qk + 0, {4: 70.0}, 5, 'Sim', 'manutenção a quente 70 °C'),
        linha(CQ, qk + 1, {4: 65.0}, 5, 'Sim', 'manutenção a quente exatamente 65 °C'),
        linha(CQ, qk + 2, {4: 64.9}, 5, 'NÃO', 'manutenção a quente 64,9 °C'),
        linha(CQ, qk + 3, {}, 5, None, 'manutenção a quente linha vazia → vazio'),
        linha(CQ, qk + 4, {4: 'quente'}, 5, None, 'manutenção a quente: texto → vazio (dava «Sim»)'),
        linha(RC, r1 + 0, {4: 'Refrigerado', 6: 7.0}, 7, 'Sim', 'receção refrigerado 7,0 °C'),
        linha(RC, r1 + 1, {4: 'Refrigerado', 6: 7.5}, 7, 'NÃO', 'receção refrigerado 7,5 °C'),
        linha(RC, r1 + 2, {4: 'Congelado (exceto pescado)', 6: -12.0}, 7, 'Sim', 'receção congelado −12 °C'),
        linha(RC, r1 + 3, {4: 'Congelado (exceto pescado)', 6: -11.0}, 7, 'NÃO', 'receção congelado −11 °C'),
        linha(RC, r1 + 4, {4: 'Ultracongelado ou pescado congelado', 6: -18.0}, 7, 'Sim', 'receção ultracongelado −18 °C'),
        linha(RC, r1 + 5, {4: 'Ultracongelado ou pescado congelado', 6: -17.5}, 7, 'NÃO',
              'receção pescado congelado −17,5 °C'),
        linha(RC, r1 + 6, {6: 5.0}, 7, None, 'receção temperatura sem tipo → vazio'),
        linha(RC, r1 + 7, {4: 'Refrigerado'}, 7, None, 'receção tipo sem temperatura → vazio'),
        linha(TM, t1 + 0, {4: 0.8}, 6, 'Sim', 'termómetro +0,8 °C'),
        linha(TM, t1 + 1, {4: 1.0}, 6, 'Sim', 'termómetro +1,0 °C (limite incluído)'),
        linha(TM, t1 + 2, {4: -1.0}, 6, 'Sim', 'termómetro −1,0 °C (limite incluído)'),
        linha(TM, t1 + 3, {4: 1.1}, 6, 'NÃO', 'termómetro +1,1 °C'),
        linha(TM, t1 + 4, {4: -1.2}, 6, 'NÃO', 'termómetro −1,2 °C'),
        linha(TM, t1 + 5, {}, 6, None, 'termómetro linha vazia → vazio'),
        linha(TM, t1 + 6, {3: None, 4: 0.5}, 6, None, 'termómetro sem referência → vazio'),
    ]
    extra = [(CQ, ak, 7), (CQ, ak + 4, 7), (CQ, ak + 6, 7), (TM, t1 + 3, 5), (RC, r1 + 4, 5), (RC, r1 + 0, 5),
             (FR, sem[1], 1), (FR, sem[1], 2), (FR, sem[1] + 6, 2), (FR, sem[1] + 8, 2), (FR, T0 + 4, 7),
             (FR, T0 + 5, 7), (FR, T0 + 1, 7)]
    res, ex = testar(casos, extra=extra)
    assert [round(minutos(ex[(CQ, z, 7)])) for z in (ak, ak + 4, ak + 6)] == [100, 90, 1380], ex
    assert abs(ex[(TM, t1 + 3, 5)] - 1.1) < 1e-9, ex[(TM, t1 + 3, 5)]
    assert ex[(RC, r1 + 4, 5)] == f'−18{NB}°C ou menos' and ex[(RC, r1, 5)] == f'máx. 7{NB}°C', ex
    assert ex[(FR, sem[1], 1)] == 'Câmara de refrigeração' and ex[(FR, sem[1], 2)] == f'0 a 7{NB}°C', ex
    assert ex[(FR, sem[1] + 6, 2)] == f'−12{NB}°C ou menos' and ex[(FR, sem[1] + 8, 2)] == f'−18{NB}°C ou menos', ex
    assert [ex[(FR, T0 + k, 7)].replace(NB, ' ') for k in (1, 4, 5)] == [ORIG_REFR, ORIG_CONG, ORIG_LEI], ex
    # Normas editáveis: câmara única 0 a 4 °C, confeção 75 °C, arrefecimento 1 h, refrigerado à receção 4 °C, tolerância
    # 0,5 °C → as mesmas fórmulas seguem.
    casos2 = [caso_frio(0, 0, 'NÃO', 'câmara 0 a 4 °C: 4,5 °C', abertura={0: 4.5}),
              caso_frio(3, 0, 'Sim', 'câmara 0 a 4 °C: semana 4, 4,0 °C', abertura={0: 4.0}),
              linha(CQ, kk, {4: 72.0}, 5, 'NÃO', 'confeção 75 °C no plano: 72 °C'),
              linha(CQ, kk + 1, {4: 75.0}, 5, 'Sim', 'confeção 75 °C no plano: 75 °C'),
              linha(CQ, ak, {3: hm(15, 0), 5: hm(16, 30), 6: 4.0}, 9, 'NÃO', 'arrefecimento 1 h no plano: 1 h 30'),
              linha(CQ, ak + 1, {3: hm(15, 0), 5: hm(15, 55), 6: 4.0}, 9, 'Sim', 'arrefecimento 1 h no plano: 55 min'),
              linha(RC, r1, {4: 'Refrigerado', 6: 5.0}, 7, 'NÃO', 'receção refrigerado 4 °C no plano: 5,0 °C'),
              linha(TM, t1, {4: 0.8}, 6, 'NÃO', 'tolerância 0,5 °C: +0,8 °C'),
              linha(TM, t1 + 1, {4: -0.5}, 6, 'Sim', 'tolerância 0,5 °C: −0,5 °C')]
    res2, ex2 = testar(casos2, {(FR, f'F{T0 + 1}'): 4, (CQ, V['conf_t'].replace('$', '')): 75,
                                (CQ, V['arref_d'].replace('$', '')): 1, (RC, f'C{R0 + 1}'): 4, (TM, f'C{TH_TOL}'): 0.5},
                       extra=[(FR, sem[0], 2), (CQ, kk - 2, 1), (CQ, ak - 2, 1)])
    assert ex2[(FR, sem[0], 2)] == f'0 a 4{NB}°C', ex2
    assert ex2[(CQ, kk - 2, 1)].startswith('Confeção – pelo menos 75'), ex2
    assert ex2[(CQ, ak - 2, 1)].replace(NB, ' ') == 'Arrefecimento – até 5 °C em 1 hora ou menos', ex2
    # Texto em células numéricas (dados e normas) e dados obrigatórios em falta → vazio, nunca «Sim»; também «Exemplo».
    e_vb, vst = vb
    casos3 = [
        caso_frio(0, 0, None, 'câmara: «9,0» como texto num dia → vazio (dava «Sim»)', abertura={0: 3.0, 1: '9,0'}),
        caso_frio(0, 1, None, 'mínimo do frigorífico como texto → vazio', abertura={0: 3.0}),
        caso_frio(0, 2, None, 'máximo da bancada como texto → vazio', abertura={0: 3.0}),
        linha(CQ, kk, {4: '65'}, 5, None, 'confeção: «65» como texto → vazio'),
        linha(CQ, ak, {3: '15.00', 5: hm(16, 0), 6: 4.0}, 9, None, 'arrefecimento: hora de início como texto → vazio'),
        linha(CQ, ak + 1, {3: hm(15, 0), 4: 'quente', 5: hm(16, 0), 6: 4.0}, 9, None,
              'arrefecimento: temperatura inicial como texto → vazio'),
        linha(CQ, ak + 2, {3: hm(15, 0), 5: hm(16, 0), 6: 'frio'}, 9, None,
              'arrefecimento: temperatura final como texto → vazio'),
        linha(CQ, rk, {4: 'quente', 5: 'Sim'}, 6, None, 'reaquecimento: texto como temperatura → vazio'),
        linha(CQ, rk + 1, {4: 70.0, 5: 'talvez'}, 6, None, 'reaquecimento: «1.º reaquecimento?» inválido → vazio'),
        linha(CQ, qk, {4: 70.0}, 5, None, 'norma da manutenção a quente como texto → vazio'),
        linha(RC, r1, {4: 'Refrigerado', 6: 'frio'}, 7, None, 'receção: texto como temperatura → vazio'),
        linha(TM, t1, {4: 'zero'}, 6, None, 'termómetro: texto como leitura → vazio'),
        linha(EX, e_vb + 2, {4: '4,0'}, 11, None, 'Exemplo frigorífico: texto num dia → vazio'),
        linha(EX, vst['conf'], {4: 'oitenta'}, 5, None, 'Exemplo confeção: texto → vazio'),
        linha(EX, vst['arref'], {6: None}, 9, None, 'Exemplo arrefecimento sem temperatura final → vazio'),
        linha(EX, vst['reaq'], {5: None}, 6, None, 'Exemplo reaquecimento sem «1.º reaquecimento?» → vazio'),
        linha(EX, vst['quente'], {4: 'quente'}, 5, None, 'Exemplo manutenção a quente: texto → vazio'),
        linha(EX, e_vb, {}, 11, 'Sim', 'Exemplo câmara sem alterações → Sim'),
    ]
    extra3 = [(CQ, ak, 7), (TM, t1, 5), (FR, sem[0] + 2, 2), (FR, T0 + 3, 7)]
    res3, ex3 = testar(casos3, {(FR, f'E{T0 + 2}'): 'zero', (FR, f'F{T0 + 3}'): 'sete',
                                (CQ, V['quente_t'].replace('$', '')): 'sessenta e cinco'}, extra=extra3)
    assert all(ex3[x] in (None, '') for x in extra3), ex3  # duração, desvio, norma e origem com texto: vazios
    for folha, desc, esp, w in res + res2 + res3:
        print(f'  {"OK " if esp == w else "KO "} [{folha}] {desc} → {w!r} (esperado {esp!r})')
    assert all(esp == w for _, _, esp, w in res + res2 + res3), 'Gate de lógica KO'
    return len(res) + len(res2) + len(res3)


def gate_publicado(sem, qt, r1, t1, vb):
    wv = load_workbook(XLSX, data_only=True)
    assert wv.sheetnames == [FR, CQ, RC, TM, EX], wv.sheetnames
    for folha in (FR, EX):
        ws = wv[folha]
        assert [ws.cell(row=T0 + 1 + i, column=2).value for i in range(N_EQ)] == [n for n, _, _ in EQUIPAMENTOS]
        assert [ws.cell(row=T0 + 1 + i, column=5).value for i in range(N_EQ)] == [m for _, m, _ in EQUIPAMENTOS]
        assert [ws.cell(row=T0 + 1 + i, column=6).value for i in range(N_EQ)] == [m for _, _, m in EQUIPAMENTOS]
        orig = [ws.cell(row=T0 + 1 + i, column=7).value.replace(NB, ' ') for i in range(N_EQ)]
        assert orig == [ORIG_REFR] * 3 + [ORIG_CONG, ORIG_LEI], orig
    ws = wv[FR]
    normas_txt = ['0 a 7 °C'] * 3 + ['−12 °C ou menos', '−18 °C ou menos']
    for e in sem:
        assert ws.cell(row=e - 2, column=2).value is None
        for i in range(N_EQ):
            z1 = e + 2 * i
            assert ws.cell(row=z1, column=1).value == EQUIPAMENTOS[i][0], (e, i)
            assert ws.cell(row=z1, column=2).value.replace(NB, ' ') == normas_txt[i], (e, i)
            assert [ws.cell(row=z1, column=3).value, ws.cell(row=z1 + 1, column=3).value] == ['Abertura',
                                                                                              'Fecho (opcional)']
            for z in (z1, z1 + 1):
                for k in list(range(4, 11)) + [12, 13]:
                    assert ws.cell(row=z, column=k).value is None, (z, k)
            assert ws.cell(row=z1, column=11).value in (None, ''), (z1, 11)
        assert all(ws.cell(row=e + 2 * N_EQ, column=k).value is None for k in range(4, 11)), e
    qs = wv[CQ]
    assert [qs.cell(row=N0 + 1 + i, column=5).value for i in range(len(NORMAS))] == [65, 5, 2, 65, 65]
    faixas = [qs.cell(row=qt[tp] - 2, column=1).value.replace(NB, ' ') for tp in ORDEM]
    assert faixas == ['Confeção – pelo menos 65 °C no centro do alimento, na parte mais espessa',
                      'Arrefecimento – até 5 °C em 2 horas ou menos',
                      'Reaquecimento – pelo menos 65 °C no centro, uma só vez',
                      'Manutenção a quente – pelo menos 65 °C, medidos no alimento e não na água do banho-maria'], faixas
    for tp in ORDEM:
        for z in range(qt[tp], qt[tp] + N_LINHAS):
            for k in range(1, 14):
                assert qs.cell(row=z, column=k).value in (None, ''), (tp, z, k)
    rs = wv[RC]
    assert [rs.cell(row=R0 + 1 + i, column=3).value for i in range(3)] == [7, -12, -18]
    for z in range(r1, r1 + R_N):
        assert all(rs.cell(row=z, column=k).value in (None, '') for k in range(1, 10)), z
    ts = wv[TM]
    assert ts.cell(row=TH_TOL, column=3).value == 1
    for z in range(t1, t1 + TH_N):
        assert ts.cell(row=z, column=3).value == 0, z
        assert all(ts.cell(row=z, column=k).value in (None, '') for k in (1, 2, 4, 5, 6, 7, 8)), z
    # Exemplo: exatamente um desvio, com ação corretiva; o resto «Sim»
    vs = wv[EX]
    e, vst = vb
    oks = [(EQUIPAMENTOS[i][0], vs.cell(row=e + 2 * i, column=11).value) for i in range(N_EQ)]
    oks += [(tp, vs.cell(row=vst[tp], column=OK_COL[tp]).value) for tp in ORDEM]
    desvios = []
    for i, (nome, mn, mx) in enumerate(EQUIPAMENTOS):
        z1 = e + 2 * i
        if vs.cell(row=z1, column=11).value == 'NÃO':
            assert vs.cell(row=z1, column=12).value and vs.cell(row=z1, column=13).value, 'desvio sem ação ou rubrica'
            for z, momento in ((z1, 'abertura'), (z1 + 1, 'fecho')):
                for k in range(4, 11):
                    w = vs.cell(row=z, column=k).value
                    if w > mx or (mn is not None and w < mn):
                        desvios.append(f'{nome} {DIAS[k - 4].lower()} ({momento}) {w:.1f}'.replace('.', ',') + ' °C')
    assert [w for _, w in oks].count('NÃO') == 1 and [w for _, w in oks].count('Sim') == len(oks) - 1, oks
    assert round(minutos(vs.cell(row=vst['arref'], column=7).value)) == 100
    assert vs.cell(row=W0, column=2).value == VB_SEMANA
    # Textos, origens, ligações, validações, uma só folha selecionada
    wf = load_workbook(XLSX)
    tudo = {b.title: ' '.join(str(c.value) for row in b.iter_rows() for c in row if c.value).replace(NB, ' ')
            for b in wf.worksheets}
    for n in (NOTA_LEI, NOTA_AHRESP_FRIO, NOTA_FECHO, NOTA_PESCADO, NOTA_VOLUNTARIO, NOTA_REGISTADOR, NOTA_GUARDAR,
              NOTA_AUXILIAR):
        assert n in tudo[FR], n
    for n in (NOTA_AHRESP_QUENTE, NOTA_PLANO, NOTA_VOLUNTARIO, NOTA_GUARDAR, NOTA_AUXILIAR):
        assert n in tudo[CQ], n
    assert NOTA_RECECAO in tudo[RC] and NOTA_AUXILIAR in tudo[RC] and NOTA_GUARDAR in tudo[RC]
    assert NOTA_TOLERANCIA in tudo[TM] and NOTA_AUXILIAR in tudo[TM] and NOTA_GUARDAR in tudo[TM]
    junto = ' '.join(tudo.values())
    vet = [p for p in VETADOS if re.search(p, junto)]
    assert not vet, vet
    for b in wf.worksheets:
        alvos = {c.hyperlink.target for row in b.iter_rows() for c in row if c.hyperlink}
        assert alvos == {ARTIGO, ARTIGO_TEMP}, (b.title, alvos)
        assert b.data_validations.dataValidation, b.title
        assert all(d.showErrorMessage and d.error for d in b.data_validations.dataValidation), b.title
        assert str(b.page_setup.paperSize) == '9', b.title  # A4
    z = zipfile.ZipFile(XLSX)
    selecionadas = [n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
                    and 'tabSelected="1"' in z.read(n).decode('utf-8')]
    assert selecionadas == ['xl/worksheets/sheet1.xml'], selecionadas
    return desvios


def gate_pdf():
    warnings.filterwarnings('ignore')
    from pypdf import PdfReader
    rd = PdfReader(str(PDF))
    n = len(rd.pages)
    assert n == 4, n
    for p in rd.pages:
        assert abs(float(p.mediabox.width) - 595.28) < 1 and abs(float(p.mediabox.height) - 841.89) < 1, p.mediabox
    textos = [' '.join(p.extract_text().replace(NB, ' ').split()) for p in rd.pages]
    comum = ('Esta folha é um auxiliar, não um impresso oficial da ASAE, da DGAV ou da AHRESP',
             'Guarde os registos durante o tempo que o seu plano definir', 'aichef.pro/pt/blog/haccp')
    esperado = [
        ('Registo de temperaturas – frio (câmaras, frigoríficos e arcas)', '0 a 7 °C', '–12 °C ou menos',
         '–18 °C ou menos', 'Seg', 'Dom', 'Abertura', 'Fecho', 'Rubrica de quem leu', 'Decreto-Lei n.º 251/91',
         'Decreto-Lei n.º 37/2004', 'gelo fundente', 'não fixa temperaturas', 'pelo menos uma vez por dia',
         'recomendação nossa', 'uso voluntário', '10 m³', 'Esclarecimento Técnico n.º 4/DGAV/2025'),
        ('Confeção, arrefecimento, reaquecimento e manutenção a quente', 'Pelo menos 65 °C no centro do alimento',
         '75 °C', 'Até 5 °C em 2 horas ou menos', 'uma só vez', 'banho-maria', 'elimina-se', 'Duração (h:mm)',
         '1.º reaquecimento?', 'A lei portuguesa não fixa estas temperaturas', 'não é lei nem código da AHRESP'),
        ('Registo de temperaturas – receção de mercadoria', 'Refrigerado', 'máx. 7 °C', 'Congelado (exceto pescado)',
         'Ultracongelado ou pescado congelado', 'antes de assinar a guia', 'Fornecedor', 'recusado'),
        ('Verificação dos termómetros e das sondas', 'Periodicidade da verificação (a do seu plano)',
         'Tolerância definida no seu plano: ± ………… °C', 'ficha técnica', 'Gelo fundente', 'Referência (°C)',
         'Desvio (°C)', 'ajuste ou substitua'),
    ]
    for i, verw in enumerate(esperado):
        for x in verw + comum:
            assert x in textos[i], (f'página {i + 1}', x)
    tamanhos = set()
    for pg in rd.pages:
        pg.extract_text(visitor_text=lambda tx, cm, tm, fd, fs: tamanhos.add(round(fs * tm[0], 2))
                        if tx.strip() else None)
    assert min(tamanhos) >= 6.5, sorted(tamanhos)
    tudo = ' '.join(textos)
    vet = [p for p in VETADOS if re.search(p, tudo)]
    assert not vet, vet
    return n, textos


# Gate de idioma: espanhol, brasileirismos, grafias anteriores ao AO90 e neerlandês (do gémeo NL).
ESPANHOL = ['registro', 'registros', 'cámara', 'cámaras', 'nevera', 'neveras', 'congelación', 'refrigeración',
            'cocción', 'enfriamiento', 'recalentamiento', 'mantenimiento', 'caliente', 'recepción', 'proveedor',
            'desviación', 'acción', 'correctora', 'hielo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'lun',
            'mié', 'jue', 'vie', 'responsable', 'ejemplo', 'apertura', 'cierre', 'duración', 'fecha', 'producto',
            'productos', 'establecimiento', 'equipo', 'escriba', 'rellene', 'celdas', 'amarillas', 'hoja', 'plantilla',
            'appcc', 'según', 'más', 'sí', 'una', 'con', 'del', 'los', 'las', 'el', 'y', 'sin', 'dato', 'datos',
            'vacío', 'si', 'cocina', 'plato', 'platos', 'pollo', 'muslos', 'caldo de carne en', 'guía']
BRASIL = ['planilha', 'planilhas', 'cardápio', 'arquivo', 'usuário', 'tela', 'equipe', 'registro', 'registros',
          'registrar', 'registre', 'controle', 'contato', 'fato', 'seção', 'recepção', 'geladeira', 'freezer',
          'termômetro', 'termômetros', 'congelamento', 'descongelamento', 'resfriamento', 'resfriado', 'cozimento',
          'monitorar', 'treinamento', 'aba', 'abas', 'baixar', 'você', 'vocês', 'salvar', 'deletar', 'digite',
          'esquentar', 'derretido', 'câmera', 'checar', 'detectar', 'detecção', 'estoque', 'açougue', 'a gente']
PRE_AO90 = ['objectivo', 'factura', 'acção', 'acções', 'actual', 'actualizar', 'exacto', 'exactamente', 'óptimo',
            'direcção', 'selecção', 'protecção', 'inspecção', 'efectivo', 'efectuar', 'electrónico', 'colecção',
            'adoptar', 'adopte', 'correcto', 'correcta', 'correctiva', 'correctivas', 'correctivo', 'correcção',
            'projecto', 'confecção', 'confeccionado', 'confeccionar', 'respectiva', 'respectivo', 'excepto',
            'excepção', 'afectar', 'afectado', 'colectivo', 'baptismo']
NEERLANDES = ['koeling', 'koelingen', 'vriezer', 'vriezers', 'koken', 'terugkoelen', 'regenereren', 'warmhouden',
              'ontvangst', 'paraaf', 'afwijking', 'maatregel', 'week', 'ja', 'nee', 'voorbeeld', 'hygiënecode', 'KHN',
              'NVWA', 'warenwet', 'uur', 'bedrijf', 'verantwoordelijke', 'het', 'een', 'van', 'en', 'met', 'bij', 'niet',
              'gekoeld', 'smeltend', 'ijs', 'gevogelte', 'diepvries', 'kern', 'orde', 'let op', 'thermometer', 'datum',
              'tijd', 'leverancier']
MESES = r'\b(Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\b'
TIPOGRAFIA_OK = set('·€≤≥÷×«»–—−’…')


def textos_xlsx():
    wf = load_workbook(XLSX)
    out = list(wf.sheetnames)
    for ws in wf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    out += re.findall(r'"([^"]*)"', c.value) if c.data_type == 'f' else [c.value]
        for d in ws.data_validations.dataValidation:
            out += [x for x in (d.error, d.errorTitle, d.prompt, d.promptTitle, d.formula1) if x]
    return [t.replace(NB, ' ') for t in out if t]


def gate_idioma(textos_pdf):
    textos = textos_xlsx() + textos_pdf
    tudo = '\n'.join(t for t in textos if not t.startswith('https://') and 'aichef.pro/' not in t)
    tudo += '\n' + '\n'.join(re.sub(r'\S*aichef\.pro/\S*', '', t) for t in textos_pdf)
    for w in ESPANHOL + BRASIL + PRE_AO90 + NEERLANDES:
        m = re.search(rf'(?<![\w]){re.escape(w)}(?![\w])', tudo, flags=re.IGNORECASE)
        assert not m, f'palavra proibida «{w}»: …{tudo[max(0, m.start() - 40):m.end() + 40]}…'
    ger = {g for g in re.findall(r'\b\w+(?:ando|endo|indo)\b', tudo, flags=re.IGNORECASE)} - {'quando', 'Quando'}
    assert not ger, f'gerúndio (estrutura brasileira): {ger}'
    assert not re.search(MESES, tudo), 'mês com maiúscula (AO90: minúscula)'
    raros = {ch for ch in tudo if ord(ch) > 0x24F and ch not in TIPOGRAFIA_OK}
    assert not raros, f'caracteres fora do alfabeto latino: {sorted(raros)}'
    return len(textos)


def gate_parche():
    r = subprocess.run([sys.executable, str(PARCHE), '--check', str(XLSX)], capture_output=True, text=True, cwd=RAIZ)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'ok'


def main():
    wb = Workbook()
    wb.remove(wb.active)
    sem = folha_frio(wb)
    qt = folha_quente(wb)
    r1 = folha_rececao(wb)
    t1 = folha_termometro(wb)
    vb = folha_exemplo(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 0)
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Registo de temperaturas HACCP'
    wb.properties.language = 'pt-PT'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injetar(XLSX))
    desvios = gate_publicado(sem, qt, r1, t1, vb)
    n = gate_logica(sem, qt, r1, t1, vb)
    pdf_imprimir()
    paginas, textos_pdf = gate_pdf()
    n_txt = gate_idioma(textos_pdf)
    parche = gate_parche()
    print(f'OK {XLSX.name} · 5 folhas · {N_SEMANAS} semanas × {N_EQ} equipamentos (abertura + fecho) · confeção/'
          f'arrefecimento/reaquecimento/manutenção 4 × {N_LINHAS} · receção {R_N} · termómetro {TH_N} · '
          f'Exemplo desvios {desvios} · gate lógica {n}/{n} · idioma OK ({n_txt} textos) · parche --check: {parche} · '
          f'{PDF.name} ({paginas} páginas)')


if __name__ == '__main__':
    main()
