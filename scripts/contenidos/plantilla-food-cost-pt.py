#!/usr/bin/env python3
"""Cálculo de food cost (PT), modelo Excel GRATIS — lead magnet de /pt/blog/food-cost.

LowFruits PT (nov-2026): «food cost» 110/mes.
Gemelo portugués de plantilla-escandallo-gratis.py (ES: bloque custo → preço sem IVA → com IVA → preço de carta →
food cost real → margem) con la estructura del gemelo IT auditado (plantilla-food-cost-it.py: cantidades limpias en g,
bruta = limpa ÷ rendimento al gramo por exceso, línea de valor fijo, hoja de ejemplo + hoja vacía activa), ADAPTADO:
  - el ejemplo es la tabla del post TAL CUAL (bacalhau à Brás, 1 dose): 120 g 2,40 € · 60 g 0,45 € · 2 ovos/100 g
    0,50 € · 50 g 0,08 € · azeite, azeitonas, salsa e temperos 0,37 € = 3,80 €. Los precios por kg (20,00 · 7,50 ·
    5,00 · 1,60 €/kg) salen de dividir el coste del post por la cantidad, y la hoja lo dice;
  - bloque: food cost pretendido 28 % → 13,57 € sem IVA (la FAQ del post) → 15,33 € com IVA; precio en la ementa
    15,26 € com IVA (= los 13,50 € sem IVA del post + 13 %) → 13,50 € sem IVA → food cost real 28,1 % → margem 9,70 €;
  - «rendimento» (la palabra de los dos posts PT) en vez de merma/calo: vacío = 100 %; ≤ 0 o texto → «verifique o
    rendimento»; > 100 % permitido (productos que ganan peso). Mini bloque con el otro ejemplo del post: 1 kg de peixe a
    10 €/kg → 800 g limpos → rendimento 80 % → 12,50 €/kg limpo;
  - aviso visible (fórmula) si una fila tiene cantidad y no tiene un coste válido (sin precio, texto o rendimento
    inválido) + formato condicional; ningún #DIV/0! ni 0 falso con celdas vacías;
  - IVA editable al 13 % (comida en restauração, continente) con nota de 23 % / Madeira 12 % / Açores 9 %.
Sale: astro-site/public/descargas/calculo-food-cost-excel-gratis-aichef.xlsx — hojas «Exemplo (bacalhau à Brás)» y
«Cálculo em branco» (activa; 15 filas + valor fijo, mismas celdas y fórmulas).
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el NL/DE), un gate data_only, un gate pycel sobre una
COPIA sin caché (las cifras del post salen de las fórmulas), un gate de idioma (nada de español, brasileirismos ni
grafías anteriores al AO90) y parche_xml_xlsx.py --check. `/descargas/*` está en noindex (netlify.toml).
Sesión Claude Code, 25-nov-2026.
"""
import contextlib
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/calculo-food-cost-excel-gratis-aichef.xlsx'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
PARCHE = RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'
GUIA = 'https://aichef.pro/pt/blog/food-cost'
CALC = 'https://aichef.pro/pt/calculadora-food-cost-restaurante'
H_EX, H_BR = 'Exemplo (bacalhau à Brás)', 'Cálculo em branco'

PRETO, DOURADO, CINZA = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borda = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
cinza = PatternFill('solid', fgColor=CINZA)
erro = PatternFill('solid', fgColor='FBE3E3')
NB = ' '  # espaço não separável entre o número e a unidade («28,1 %»)
EUR = '#,##0.00 "€"'
EUR_KG = '#,##0.00 "€/kg"'
G = '#,##0'
PCT0 = f'0"{NB}"%'
PCT1 = f'0.0"{NB}"%'
COLS = 6  # A–F

# Tabela do artigo: (ingrediente, quantidade limpa g, rendimento, preço €/kg) — custo do artigo ÷ quantidade
EXEMPLO = [('Bacalhau demolhado desfiado', 120, None, 20.00), ('Batata palha', 60, None, 7.50),
           ('Ovos (2 unidades)', 100, None, 5.00), ('Cebola', 50, None, 1.60)]
CUSTOS_ARTIGO = [2.40, 0.45, 0.50, 0.08]
FORFAIT_EX = ('Azeite, azeitonas, salsa e temperos', 0.37)
FORFAIT_BR = 'Sal, temperos e outros (valor fixo)'
FC_OBJ, IVA, PRECO_EMENTA = 0.28, 0.13, 15.26
IVA_NOTA = (f'IVA na restauração (continente): 13{NB}% na comida; 23{NB}% nas bebidas alcoólicas e nos refrigerantes '
            f'(Código do IVA, Lista II, verba 3.1). Madeira: 12{NB}%. Açores: 9{NB}%.')
NOTA_REND = (f'Rendimento = peso limpo ÷ peso comprado. Vazio = sem perdas (100{NB}%). A quantidade bruta (a que se '
             'compra) é a limpa ÷ o rendimento, arredondada ao grama por excesso.')
NOTA_FORMULA = ('Food cost = custo das matérias-primas da dose ÷ preço de venda sem IVA × 100. A margem bruta paga '
                'tudo o resto: pessoal, renda, energia, equipamento e, no fim, o lucro.')
RODAPE = ['O food cost calcula-se sobre o preço de venda sem IVA, e os custos são os das faturas, também sem IVA.',
          f'A banda de referência que o artigo usa como ponto de partida vai de 28{NB}% a 35{NB}%. Não é uma meta: '
          'leia a percentagem com a margem em euros por dose e com as doses vendidas.',
          'Esta é a conta teórica do prato. A do mês (existências iniciais + compras − existências finais, sobre as '
          'vendas sem IVA) é outra: a diferença entre as duas é a informação.']
RODAPE_GUIA = 'Modelo gratuito do AI Chef Pro · Guia:'
RODAPE_CALC = 'Calculadora de food cost gratuita:'
REND_KO = 'verifique o rendimento'
AVISO_1 = ('Atenção: 1 linha tem quantidade, mas não tem preço (ou tem texto em vez de um número, ou o rendimento '
           'não é válido). O custo está incompleto.')
AVISO_N = (' linhas têm quantidade, mas não têm preço (ou têm texto em vez de um número, ou o rendimento não é '
           'válido). O custo está incompleto.')

# Linhas fixas (as duas folhas têm a mesma estrutura → as mesmas células)
R_PRATO, R_DOSES = 4, 5
R_TIT_ING, R_CAB = 7, 8
R_ING1, N_ING = 9, 15
R_INGN = R_ING1 + N_ING - 1          # 23
R_FORF = R_INGN + 1                  # 24
R_AVISO, R_NOTA_REND = R_FORF + 1, R_FORF + 2   # 25, 26
R_TIT_PRECO = R_NOTA_REND + 2        # 28
(R_CT, R_CD, R_FCO, R_PSO, R_IVA, R_PCO, R_PE, R_PVS, R_FCR,
 R_MARG) = range(R_TIT_PRECO + 1, R_TIT_PRECO + 11)   # 29–38
R_NOTA_FORM = R_MARG + 2             # 40
R_TIT_REND = R_NOTA_FORM + 2         # 42
R_RC, R_RL, R_RP, R_RR, R_RK = range(R_TIT_REND + 1, R_TIT_REND + 6)   # 43–47
R_NOTA_RK = R_RK + 1                 # 48
R_RODAPE = R_NOTA_RK + 2             # 50
K = f'IF(N($B${R_DOSES})>1,$B${R_DOSES},1)'
CUSTOS = f'F{R_ING1}:F{R_FORF}'


def n_aviso():
    b, f = f'B{R_ING1}:B{R_INGN}', f'F{R_ING1}:F{R_INGN}'
    return f'SUMPRODUCT(({b}<>"")*(1-ISNUMBER({f})))'


# ---------------------------------------------------------------- estilo
def barra(ws, linha, texto, ate=COLS):
    c = ws.cell(row=linha, column=1, value=texto)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=PRETO)
    ws.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=ate)


def cel(ws, linha, col, valor=None, fmt=None, inp=False, negrito=False, cinzento=False):
    c = ws.cell(row=linha, column=col, value=valor)
    c.border = borda
    if fmt:
        c.number_format = fmt
    if inp:
        c.fill = entrada
    elif cinzento:
        c.fill = cinza
    if negrito:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=True, vertical='center')
    return c


def alto(ws, linha, *textos_e_larguras):
    """Altura explícita (15 pt por linha estimada): o Excel não ajusta sozinho as linhas com células juntas."""
    linhas = max(len(textwrap.wrap(t, w)) if t else 1 for t, w in textos_e_larguras)
    if linhas > 1:
        ws.row_dimensions[linha].height = max(ws.row_dimensions[linha].height or 0, 15 * linhas + 2)


def nota(ws, linha, texto, c0=1, c1=COLS, largura=105, italico=True):
    c = ws.cell(row=linha, column=c0, value=texto)
    c.font = Font(italic=italico, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=linha, start_column=c0, end_row=linha, end_column=c1)
    alto(ws, linha, (texto, largura))


def dv(ws, tipo, op, f1, f2, titulo, msg):
    d = DataValidation(type=tipo, operator=op, formula1=f1, formula2=f2, allow_blank=True, showErrorMessage=True,
                       errorTitle=titulo, error=msg)
    ws.add_data_validation(d)
    return d


# ---------------------------------------------------------------- folha
def folha(wb, nome, ex):
    ws = wb.create_sheet(nome)
    ws['A1'] = 'Cálculo de food cost do prato'
    ws['A1'].font = Font(bold=True, size=16, color=DOURADO)
    ws['A1'].fill = PatternFill('solid', fgColor=PRETO)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=COLS)
    ws.row_dimensions[1].height = 26
    instr = ('Exemplo do artigo: bacalhau à Brás, uma dose. Os valores são um exemplo, não uma fatura; os preços por '
             'quilo saem dos custos do artigo (2,40 € por 120 g de bacalhau = 20,00 €/kg). Para os seus pratos, use a '
             f'folha «{H_BR}».') if ex else \
        'Preencha só as células amarelas: a quantidade bruta, o custo, o preço e o food cost calculam-se sozinhos.'
    nota(ws, 2, instr)

    d_num = dv(ws, 'decimal', 'greaterThanOrEqual', '0', None, 'Valor inválido',
               'Escreva só o número, igual ou maior do que 0 (por exemplo 120 ou 7,50).')
    d_pct = dv(ws, 'decimal', 'between', '0', '0.99', 'Percentagem',
               'Escreva a percentagem, por exemplo 13 % (ou 0,13).')

    cel(ws, R_PRATO, 1, 'Prato', negrito=True)
    cel(ws, R_PRATO, 2, 'Bacalhau à Brás' if ex else None, inp=True)
    for c in range(3, COLS + 1):
        ws.cell(row=R_PRATO, column=c).border = borda
    ws.merge_cells(start_row=R_PRATO, start_column=2, end_row=R_PRATO, end_column=COLS)
    cel(ws, R_DOSES, 1, 'Doses', negrito=True)
    dv(ws, 'whole', 'greaterThanOrEqual', '1', None, 'Doses', 'Escreva um número inteiro de doses, de 1 para cima.').add(
        cel(ws, R_DOSES, 2, 1 if ex else None, '0', inp=True).coordinate)
    nota(ws, R_DOSES, 'Se a conta é para várias doses, o custo por dose é o total a dividir pelas doses.', 3, COLS, 60)

    barra(ws, R_TIT_ING, 'Ingredientes (quantidades para o número de doses indicado)')
    cab = ['Ingrediente', 'Quantidade limpa (g ou ml)', 'Rendimento (%)', 'Quantidade bruta (g ou ml)',
           'Preço de compra sem IVA (€/kg ou €/L)', 'Custo (€)']
    for col, txt in enumerate(cab, start=1):
        c = cel(ws, R_CAB, col, txt, negrito=True, cinzento=True)
        c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.row_dimensions[R_CAB].height = 48
    d_rend = dv(ws, 'decimal', 'between', '0.01', '5', 'Rendimento',
                'Escreva o rendimento em percentagem, de 1 % a 500 % (por exemplo 80 % ou 0,8). Vazio = sem perdas.')
    linhas = (EXEMPLO if ex else []) + [None] * (N_ING - (len(EXEMPLO) if ex else 0))
    for i, item in enumerate(linhas):
        r = R_ING1 + i
        nome_i, limpa, rend, preco = item if item else (None, None, None, None)
        cel(ws, r, 1, nome_i, inp=True)
        d_num.add(cel(ws, r, 2, limpa, G, inp=True).coordinate)
        d_rend.add(cel(ws, r, 3, rend, PCT0, inp=True).coordinate)
        # bruta = limpa ÷ rendimento, ao grama por excesso; rendimento vazio = 100 %; ≤ 0 ou texto → aviso
        cel(ws, r, 4, f'=IF(OR(B{r}="",NOT(ISNUMBER(B{r}))),"",IF(C{r}="",ROUNDUP(B{r},0),'
                      f'IF(AND(ISNUMBER(C{r}),N(C{r})>0),ROUNDUP(B{r}/C{r},0),"{REND_KO}")))', G, cinzento=True)
        d_num.add(cel(ws, r, 5, preco, EUR_KG, inp=True).coordinate)
        # custo = bruta × preço, ao cêntimo como a tabela do artigo; sem preço válido → vazio (e aviso), nunca 0
        cel(ws, r, 6, f'=IF(AND(ISNUMBER(D{r}),ISNUMBER(E{r})),ROUND(D{r}/1000*E{r},2),"")', EUR, cinzento=True)
    cel(ws, R_FORF, 1, FORFAIT_EX[0] if ex else FORFAIT_BR, inp=True)
    for c in range(2, 6):
        cel(ws, R_FORF, c)
    ws.cell(row=R_FORF, column=2, value='Valor fixo: escreva o custo diretamente na coluna «Custo».').font = \
        Font(italic=True, color='555555')
    ws.merge_cells(start_row=R_FORF, start_column=2, end_row=R_FORF, end_column=5)
    d_num.add(cel(ws, R_FORF, 6, FORFAIT_EX[1] if ex else None, EUR, inp=True).coordinate)
    alto(ws, R_FORF, (FORFAIT_EX[0] if ex else FORFAIT_BR, 40))
    n = n_aviso()
    av = ws.cell(row=R_AVISO, column=1, value=f'=IF({n}=0,"",IF({n}=1,"{AVISO_1}","Atenção: "&{n}&"{AVISO_N}"))')
    av.font = Font(bold=True, color='9C1C1C')
    av.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=R_AVISO, start_column=1, end_row=R_AVISO, end_column=COLS)
    ws.row_dimensions[R_AVISO].height = 32
    nota(ws, R_NOTA_REND, NOTA_REND)
    ws.conditional_formatting.add(f'B{R_ING1}:B{R_INGN}', FormulaRule(
        formula=[f'AND($B{R_ING1}<>"",NOT(ISNUMBER($B{R_ING1})))'], fill=erro))
    ws.conditional_formatting.add(f'D{R_ING1}:D{R_INGN}', FormulaRule(
        formula=[f'AND($D{R_ING1}<>"",NOT(ISNUMBER($D{R_ING1})))'], fill=erro, font=Font(bold=True, color='9C1C1C')))
    ws.conditional_formatting.add(f'E{R_ING1}:E{R_INGN}', FormulaRule(
        formula=[f'AND($B{R_ING1}<>"",NOT(ISNUMBER($E{R_ING1})))'], fill=erro))

    # Custo, preço e food cost (o bloco do gémeo ES)
    barra(ws, R_TIT_PRECO, 'Custo, preço e food cost')
    ct, cd, fco, pso, iva = f'B{R_CT}', f'B{R_CD}', f'B{R_FCO}', f'B{R_PSO}', f'B{R_IVA}'
    pe, pvs = f'B{R_PE}', f'B{R_PVS}'
    bloco = [
        (R_CT, 'Custo total das matérias-primas', f'=IF(COUNT({CUSTOS})=0,"",SUM({CUSTOS}))', EUR, False),
        (R_CD, 'Custo por dose', f'=IF({ct}="","",{ct}/{K})', EUR, False),
        (R_FCO, 'Food cost pretendido', FC_OBJ if ex else None, PCT0, True),
        (R_PSO, 'Preço sem IVA para esse food cost', f'=IF(OR({cd}="",N({fco})<=0),"",ROUND({cd}/{fco},2))', EUR,
         False),
        (R_IVA, 'IVA', IVA, PCT0, True),
        (R_PCO, 'Preço com IVA para esse food cost', f'=IF(OR({pso}="",{iva}=""),"",ROUND({pso}*(1+N({iva})),2))',
         EUR, False),
        (R_PE, 'Preço na ementa, com IVA (o que o cliente paga)', PRECO_EMENTA if ex else None, EUR, True),
        (R_PVS, 'Preço de venda sem IVA', f'=IF(OR(N({pe})<=0,{iva}=""),"",ROUND({pe}/(1+N({iva})),2))', EUR, False),
        (R_FCR, 'Food cost com o preço da ementa', f'=IF(OR({cd}="",{pvs}=""),"",{cd}/{pvs})', PCT1, False),
        (R_MARG, 'Margem bruta por dose', f'=IF(OR({cd}="",{pvs}=""),"",{pvs}-{cd})', EUR, False),
    ]
    for r, rotulo, valor, fmt, inp in bloco:
        cel(ws, r, 1, rotulo, negrito=True)
        z = cel(ws, r, 2, valor, fmt, inp=inp, negrito=True, cinzento=not inp)
        ws.row_dimensions[r].height = 20
        alto(ws, r, (rotulo, 40))
        if r in (R_FCO, R_IVA):
            d_pct.add(z.coordinate)
        if r == R_PE:
            d_num.add(z.coordinate)
    notas_bloco = {
        R_FCO: ('No exemplo do artigo: 3,80 € ÷ 0,28 = 13,57 € sem IVA. É um ponto de partida, não uma meta.' if ex else
                'A percentagem que quer para este prato. É um ponto de partida: leia-a com a margem em euros.'),
        R_IVA: IVA_NOTA,
        R_PE: (f'No exemplo do artigo, o prato vende-se a 13,50 € sem IVA: com 13{NB}% de IVA, 15,26 € na ementa.'
               if ex else 'O preço arredondado que vai escrever na ementa, já com IVA.'),
    }
    for r, txt in notas_bloco.items():
        nota(ws, r, txt, 3, COLS, 58)
    nota(ws, R_NOTA_FORM, NOTA_FORMULA, italico=False)

    # Rendimento de um produto (o outro exemplo do artigo)
    barra(ws, R_TIT_REND, 'Rendimento de um produto: quanto custa o quilo limpo')
    rc, rl, rp, rr = f'B{R_RC}', f'B{R_RL}', f'B{R_RP}', f'B{R_RR}'
    rend = [
        (R_RC, 'Peso comprado (g)', 1000 if ex else None, G, True),
        (R_RL, 'Peso limpo, depois de amanhar e limpar (g)', 800 if ex else None, G, True),
        (R_RP, 'Preço de compra sem IVA (€/kg)', 10.00 if ex else None, EUR_KG, True),
        (R_RR, 'Rendimento (limpo ÷ comprado)', f'=IF(OR(N({rc})<=0,NOT(ISNUMBER({rl}))),"",{rl}/{rc})', PCT1, False),
        (R_RK, 'Custo do quilo limpo', f'=IF(OR({rr}="",N({rr})<=0,NOT(ISNUMBER({rp}))),"",ROUND({rp}/{rr},2))',
         EUR_KG, False),
    ]
    for r, rotulo, valor, fmt, inp in rend:
        cel(ws, r, 1, rotulo, negrito=True)
        z = cel(ws, r, 2, valor, fmt, inp=inp, negrito=True, cinzento=not inp)
        ws.row_dimensions[r].height = 20
        if inp:
            d_num.add(z.coordinate)
    nota(ws, R_NOTA_RK, ('Exemplo do artigo: 1 kg de peixe a 10,00 €/kg dá 800 g de lombos limpos; o quilo limpo custa '
                         '12,50 €, não 10,00 €. Escreva o rendimento na coluna «Rendimento» da tabela.') if ex else
         'Escreva o rendimento que obtiver na coluna «Rendimento» da tabela.')

    barra(ws, R_RODAPE, 'A ter em conta')
    for i, txt in enumerate(RODAPE):
        nota(ws, R_RODAPE + 1 + i, txt, italico=False)
    r0 = R_RODAPE + 1 + len(RODAPE)
    for r, rotulo, url in ((r0, RODAPE_GUIA, GUIA), (r0 + 1, RODAPE_CALC, CALC)):
        ws.cell(row=r, column=1, value=rotulo).font = Font(bold=True)
        link = ws.cell(row=r, column=2, value=url)
        link.hyperlink = url
        link.font = Font(color='0563C1', underline='single')
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=COLS)

    for col, w in {'A': 42, 'B': 13, 'C': 12, 'D': 13, 'E': 17, 'F': 12}.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    return ws


def gerar():
    wb = Workbook()
    wb.remove(wb.active)
    folha(wb, H_EX, True)
    folha(wb, H_BR, False)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 1)
    wb.active = 1
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Cálculo de food cost'
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)


# ---------------------------------------------------------------- cache
def cache_texto_vazio(ruta):
    """inject_cache.py não injeta o resultado «""»: a célula fica com cache vazia (<v/>, que um visor sem recálculo
    mostra como 0). Escreve-se como o Excel (t="str" + <v></v>), tocando só o XML das folhas (copiado do gémeo NL)."""
    padrao = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(ruta) as z:
        partes = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(ruta) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dados in partes:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = padrao.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', dados.decode('utf-8'))
                dados, n = xml.encode('utf-8'), n + k
            zout.writestr(info, dados)
    shutil.move(str(ruta) + '.tmp', str(ruta))
    return n


def injetar(ruta):
    out = subprocess.run([sys.executable, str(INJECT), str(ruta)], check=True, capture_output=True, text=True).stdout
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+) fallos_pycel=(\d+)', out)
    assert m and m.group(3) == '0', out
    vazias = cache_texto_vazio(ruta)
    assert int(m.group(1)) == int(m.group(2)) + vazias, (out, vazias)  # toda a fórmula leva cache
    return f'formulas={m.group(1)} cache={m.group(2)} vazias={vazias}'


# ---------------------------------------------------------------- gates
def vazio(x):
    return x in (None, '')


ESPERADO = {'CT': 3.80, 'CD': 3.80, 'PSO': 13.57, 'PCO': 15.33, 'PVS': 13.50, 'FCR': 28.1, 'MARG': 9.70,
            'RR': 80.0, 'RK': 12.50}


def ler_bloco(get):
    return {'CT': round(get(f'B{R_CT}'), 2), 'CD': round(get(f'B{R_CD}'), 2), 'PSO': round(get(f'B{R_PSO}'), 2),
            'PCO': round(get(f'B{R_PCO}'), 2), 'PVS': round(get(f'B{R_PVS}'), 2),
            'FCR': round(get(f'B{R_FCR}') * 100, 1), 'MARG': round(get(f'B{R_MARG}'), 2),
            'RR': round(get(f'B{R_RR}') * 100, 1), 'RK': round(get(f'B{R_RK}'), 2)}


def gate_ficheiro():
    wf = load_workbook(SALIDA)
    assert wf.sheetnames == [H_EX, H_BR], wf.sheetnames
    assert wf.active.title == H_BR, wf.active.title
    with zipfile.ZipFile(SALIDA) as zf:
        sel = [n for n in sorted(zf.namelist()) if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
               and 'tabSelected="1"' in zf.read(n).decode('utf-8')]
    assert sel == ['xl/worksheets/sheet2.xml'], sel
    for ws in wf.worksheets:
        destinos = {c.hyperlink.target for row in ws.iter_rows() for c in row if c.hyperlink}
        assert destinos == {GUIA, CALC}, (ws.title, destinos)
        textos = [c.value for row in ws.iter_rows() for c in row if isinstance(c.value, str)]
        assert all(t in textos for t in RODAPE + [RODAPE_GUIA, RODAPE_CALC, IVA_NOTA, NOTA_REND]), ws.title
        assert ws[f'B{R_IVA}'].value == IVA, ws.title
        assert all(d.showErrorMessage for d in ws.data_validations.dataValidation), ws.title
        ps = ws.page_setup
        assert str(ps.paperSize) == str(ws.PAPERSIZE_A4) and ps.fitToWidth == 1 and ps.fitToHeight == 0, ws.title
        # 15 linhas livres com fórmulas + a linha de valor fixo
        assert all(ws[f'D{r}'].data_type == 'f' and ws[f'F{r}'].data_type == 'f' for r in range(R_ING1, R_INGN + 1))
        assert ws[f'F{R_FORF}'].data_type != 'f'
    wv = load_workbook(SALIDA, data_only=True)
    e = wv[H_EX]
    linhas = range(R_ING1, R_ING1 + len(EXEMPLO))
    custos = [e[f'F{r}'].value for r in linhas]
    assert all(isinstance(v, (int, float)) for v in custos), custos
    assert [round(v, 2) for v in custos] == CUSTOS_ARTIGO, custos
    assert [e[f'D{r}'].value for r in linhas] == [120, 60, 100, 50]
    assert e[f'F{R_FORF}'].value == FORFAIT_EX[1]
    bloco = ler_bloco(lambda ref: e[ref].value)
    assert bloco == ESPERADO, bloco
    assert vazio(e[f'A{R_AVISO}'].value), e[f'A{R_AVISO}'].value
    branco = wv[H_BR]
    for row in wf[H_BR].iter_rows():
        for c in row:
            if c.data_type == 'f':
                assert vazio(branco[c.coordinate].value), (H_BR, c.coordinate, branco[c.coordinate].value)
    return bloco


def gate_pycel():
    """As cifras do artigo saem das FÓRMULAS: cópia sem cache + pycel; depois, a folha em branco preenchida em memória,
    com casos de lógica, de células vazias e de valores errados."""
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    wf = load_workbook(SALIDA)
    tmp = tempfile.TemporaryDirectory()
    copia = str(Path(tmp.name) / 'sem-cache.xlsx')
    wf.save(copia)
    with zipfile.ZipFile(copia) as z:
        for n in z.namelist():
            if re.match(r'xl/worksheets/sheet\d+\.xml$', n):
                assert not re.search(r'</f><v>[^<]+</v>', z.read(n).decode('utf-8')), 'a cópia conserva cache'

    def novo(nome):
        xl = ExcelCompiler(filename=copia)

        def val(ref):
            with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
                x = xl.evaluate(f"'{nome}'!{ref}")
            return x.item() if hasattr(x, 'item') else x

        # Aquecimento: o pycel só recalcula, depois de set_value, as fórmulas que já avaliou.
        for row in wf[nome].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    val(c.coordinate)

        def definir(valores):
            # «Apagar» = '' (o pycel ignora set_value(None)); aqui '' e a célula vazia comportam-se igual.
            for ref, x in valores.items():
                val(ref)
                xl.set_value(f"'{nome}'!{ref}", '' if x is None else x)
        return val, definir

    a = R_ING1
    # 1) Exemplo: as cifras do artigo, calculadas pelas fórmulas
    val, _ = novo(H_EX)
    assert [round(val(f'F{a + i}'), 2) for i in range(4)] == CUSTOS_ARTIGO
    assert ler_bloco(val) == ESPERADO, ler_bloco(val)
    # 2) A tabela do artigo copiada para a folha em branco dá o mesmo
    val, definir = novo(H_BR)
    dados = {f'F{R_FORF}': FORFAIT_EX[1], f'B{R_FCO}': FC_OBJ, f'B{R_PE}': PRECO_EMENTA, f'B{R_RC}': 1000,
             f'B{R_RL}': 800, f'B{R_RP}': 10}
    for i, (_, limpa, _, preco) in enumerate(EXEMPLO):
        dados.update({f'B{a + i}': limpa, f'E{a + i}': preco})
    definir(dados)
    assert ler_bloco(val) == ESPERADO, ler_bloco(val)
    # 3) Quatro doses (quantidades × 4): o custo por dose e o food cost não mudam
    definir({f'B{R_DOSES}': 4, f'F{R_FORF}': 1.48, f'B{a}': 480, f'B{a + 1}': 240, f'B{a + 2}': 400, f'B{a + 3}': 200})
    assert round(val(f'B{R_CT}'), 2) == 15.20 and round(val(f'B{R_CD}'), 2) == 3.80
    assert round(val(f'B{R_FCR}') * 100, 1) == 28.1
    # 4) Rendimento: 80 % → 125 g brutos; 70 % → 229 g (ao grama por excesso); 250 % (ganha peso) → 80 g
    definir({f'B{a + 4}': 100, f'C{a + 4}': 0.8, f'E{a + 4}': 10})
    assert val(f'D{a + 4}') == 125 and round(val(f'F{a + 4}'), 2) == 1.25
    definir({f'B{a + 4}': 160, f'C{a + 4}': 0.7})
    assert val(f'D{a + 4}') == 229
    definir({f'B{a + 4}': 200, f'C{a + 4}': 2.5})
    assert val(f'D{a + 4}') == 80 and round(val(f'F{a + 4}'), 2) == 0.80
    # 5) Quantidade sem preço → custo vazio (não 0) e aviso; texto; rendimento 0 ou com texto → «verifique»
    definir({f'B{a + 5}': 50})
    assert vazio(val(f'F{a + 5}')) and val(f'A{R_AVISO}') == AVISO_1, val(f'A{R_AVISO}')
    definir({f'B{a + 6}': '120 g', f'E{a + 6}': 20})
    assert vazio(val(f'D{a + 6}')) and vazio(val(f'F{a + 6}')) and val(f'A{R_AVISO}') == 'Atenção: 2' + AVISO_N
    definir({f'B{a + 7}': 100, f'C{a + 7}': 0, f'E{a + 7}': 10})
    assert val(f'D{a + 7}') == REND_KO and vazio(val(f'F{a + 7}')) and val(f'A{R_AVISO}') == 'Atenção: 3' + AVISO_N
    definir({f'C{a + 7}': '80 %'})
    assert val(f'D{a + 7}') == REND_KO
    definir({f'E{a + 8}': 10, f'C{a + 8}': 0.8})  # preço e rendimento sem quantidade: ignorado, sem aviso
    assert vazio(val(f'D{a + 8}')) and vazio(val(f'F{a + 8}')) and val(f'A{R_AVISO}') == 'Atenção: 3' + AVISO_N
    total_com_avisos = round(val(f'B{R_CT}'), 2)
    for r in range(a + 5, a + 9):
        definir({f'B{r}': None, f'C{r}': None, f'E{r}': None})
    assert vazio(val(f'A{R_AVISO}')) and round(val(f'B{R_CT}'), 2) == total_com_avisos
    # 6) Sem preço na ementa → preço sem IVA, food cost real e margem vazios; sem objetivo → preço sugerido vazio;
    #    IVA vazio → preços com/sem IVA vazios (sem #DIV/0!); IVA a 23 %
    definir({f'B{R_PE}': None})
    assert all(vazio(val(f'B{r}')) for r in (R_PVS, R_FCR, R_MARG))
    definir({f'B{R_FCO}': None})
    assert vazio(val(f'B{R_PSO}')) and vazio(val(f'B{R_PCO}'))
    definir({f'B{R_FCO}': 0.28, f'B{R_PE}': 15.26, f'B{R_IVA}': None})
    assert vazio(val(f'B{R_PCO}')) and vazio(val(f'B{R_PVS}')) and vazio(val(f'B{R_FCR}'))
    definir({f'B{R_IVA}': 0.23, f'B{R_PE}': 16.61})
    assert round(val(f'B{R_PVS}'), 2) == 13.50
    # 7) Rendimento de um produto: outros números; vazio → vazio
    definir({f'B{R_RC}': 2000, f'B{R_RL}': 1500, f'B{R_RP}': 8})
    assert round(val(f'B{R_RR}') * 100, 1) == 75.0 and round(val(f'B{R_RK}'), 2) == 10.67
    definir({f'B{R_RC}': None})
    assert vazio(val(f'B{R_RR}')) and vazio(val(f'B{R_RK}'))
    definir({f'B{R_RC}': 2000, f'B{R_RP}': None})
    assert vazio(val(f'B{R_RK}'))
    # 8) Só o valor fixo; e a folha intacta, tudo vazio
    val, definir = novo(H_BR)
    definir({f'F{R_FORF}': 0.37})
    assert round(val(f'B{R_CT}'), 2) == 0.37 and round(val(f'B{R_CD}'), 2) == 0.37
    val, _ = novo(H_BR)
    for ref in (f'B{R_CT}', f'B{R_CD}', f'B{R_PSO}', f'B{R_PCO}', f'B{R_PVS}', f'B{R_FCR}', f'B{R_MARG}',
                f'B{R_RR}', f'B{R_RK}', f'A{R_AVISO}', f'D{a}', f'F{a}'):
        assert vazio(val(ref)), (ref, val(ref))
    tmp.cleanup()


# Gate de idioma: espanhol (do gerador ES), brasileirismos e grafias anteriores ao AO90.
ESPANHOL = ['ración', 'raciones', 'porción', 'merma', 'mermas', 'alérgeno', 'alérgenos', 'contiene', 'trazas',
            'elaboración', 'conservación', 'emplatado', 'plato', 'platos', 'coste', 'costes', 'pvp', 'appcc',
            'escandallo', 'rellena', 'guía', 'plantilla', 'cocina', 'salmón', 'pescado', 'fuego', 'plancha', 'aove',
            'fecha', 'versión', 'cantidad', 'unidad', 'tiempo', 'categoría', 'precio', 'precios', 'restauración',
            'españa', 'limón', 'ajo', 'cebolla', 'pimiento', 'pimienta', 'perejil', 'con', 'del', 'los', 'las',
            'una', 'sin', 'y', 'el', 'huevo', 'huevos', 'leche', 'rendimiento', 'margen', 'venta', 'ventas', 'neto',
            'neta', 'hoja', 'celda', 'celdas', 'amarillas', 'aceite', 'aceitunas', 'bacalao', 'patata', 'perejil',
            'escriba', 'usted', 'existencias', 'objetivo del']
BRASIL = ['planilha', 'planilhas', 'cardápio', 'cardápios', 'arquivo', 'usuário', 'usuários', 'tela', 'time',
          'equipe', 'registro', 'registros', 'controle', 'contato', 'fato', 'seção', 'recepção', 'geladeira',
          'freezer', 'açougue', 'xícara', 'garçom', 'gerenciar', 'gerenciamento', 'digite', 'baixar', 'celular',
          'ônibus', 'você', 'vocês', 'salvar', 'deletar', 'cadastro', 'esquentar', 'suco', 'aluguel', 'faturamento',
          'insumos', 'creme de leite', 'a gente', 'estoque', 'estoques']
PRE_AO90 = ['objectivo', 'factura', 'facturas', 'acção', 'actual', 'actualizar', 'actualizado', 'exacto', 'óptimo',
            'direcção', 'selecção', 'protecção', 'inspecção', 'efectivo', 'colecção', 'electrónico', 'adoptar',
            'correcto', 'correcta', 'projecto']
TIPOGRAFIA_OK = set('·€≥÷×«»–—−’…')
PCT_OK = {'1', '9', '12', '13', '23', '28', '35', '80', '100', '500'}


def textos_xlsx():
    wf = load_workbook(SALIDA)
    out = list(wf.sheetnames)
    for ws in wf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    out += re.findall(r'"([^"]*)"', c.value) if c.data_type == 'f' else [c.value]
        for d in ws.data_validations.dataValidation:
            out += [x for x in (d.error, d.errorTitle, d.prompt, d.promptTitle) if x]
    return [t for t in out if t]


def gate_idioma():
    textos = textos_xlsx()
    tudo = '\n'.join(t for t in textos if not t.startswith('https://'))
    for w in ESPANHOL + BRASIL + PRE_AO90:
        m = re.search(rf'(?<![\w]){re.escape(w)}(?![\w])', tudo, flags=re.IGNORECASE)
        assert not m, f'palavra proibida «{w}»: …{tudo[max(0, m.start() - 40):m.end() + 40]}…'
    ger = {g for g in re.findall(r'\b\w+(?:ando|endo|indo)\b', tudo, flags=re.IGNORECASE)} - {'quando', 'Quando'}
    assert not ger, f'gerúndio (estrutura brasileira): {ger}'
    assert '°' not in tudo and not re.search(r'\d\s?º', tudo), 'temperatura nos textos'
    for t in textos:
        for pct in re.findall(r'(\d+(?:,\d+)?)\s?%', t):
            assert pct in PCT_OK, ('percentagem não prevista', t)
    raros = {ch for ch in tudo if ord(ch) > 0x24F and ch not in TIPOGRAFIA_OK}
    assert not raros, f'caracteres fora do alfabeto latino: {sorted(raros)}'
    return len(textos)


def gate_parche():
    r = subprocess.run([sys.executable, str(PARCHE), '--check', str(SALIDA)], capture_output=True, text=True, cwd=RAIZ)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'ok'


def main():
    gerar()
    cache = injetar(SALIDA)
    b = gate_ficheiro()
    gate_pycel()
    n = gate_idioma()
    parche = gate_parche()
    pt = lambda x, d=2: f'{x:.{d}f}'.replace('.', ',')  # noqa: E731
    print(f'OK {SALIDA.relative_to(RAIZ)} · {cache} · Exemplo bacalhau à Brás: 2,40 + 0,45 + 0,50 + 0,08 + 0,37 = '
          f'{pt(b["CT"])} € · 28 % → {pt(b["PSO"])} € sem IVA ({pt(b["PCO"])} € com IVA) · ementa 15,26 € → '
          f'{pt(b["PVS"])} € sem IVA → food cost {pt(b["FCR"], 1)} % · margem {pt(b["MARG"])} € · peixe 10,00 €/kg '
          f'com {pt(b["RR"], 0)} % de rendimento → {pt(b["RK"])} €/kg limpo')
    print(f'   gates: data_only OK · pycel sem cache OK (exemplo + 8 blocos de lógica/células vazias/valores errados) · '
          f'idioma OK ({n} textos: sem espanhol, brasileirismos nem pré-AO90) · parche --check: {parche}')


if __name__ == '__main__':
    main()
