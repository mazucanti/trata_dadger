import pandas as pd
from pathlib import Path


import corta_blocos


def cria_df_ct(bloco):

    dados = []
    colunas = ["Nº Usina", "Sub Sis", "Nome", "Estágio", 
               "Ger Min Pesada", "Cap Ger Pesada", "Custo Ger Pesada", 
               "Ger Min Media", "Cap Ger Media", "Custo Ger Media", 
               "Ger Min Leve", "Cap Ger Leve", "Custo Ger Leve"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), 
                linha[14:24].strip(), linha[24:26].strip(),
                linha[29:34].strip(), linha[34:39].strip(), linha[39:49].strip(),
                linha[49:54].strip(), linha[54:59].strip(), linha[59:69].strip(),
                linha[69:74].strip(), linha[74:79].strip(), linha[79:89].strip()]
        dados.append(to_df)

    df_ct = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/CT.xls')
    df_ct.to_excel(local)


def cria_df_sb(bloco):

    dados = []
    colunas = ["Sub Sistema", "Mnemônico"]

    for linha in bloco:
        to_df = [linha[4:6], linha[9:11]]
        dados.append(to_df)

    df_sb = pd.DataFrame(dados, columns=colunas)
    df_sb.set_index("Sub Sistema", inplace=True)

    local = Path("blocos/SB.xls")
    df_sb.to_excel(local)


def cria_df_ue(bloco):

    dados = []
    colunas = ["Nº Estação", "Sub Sistema",
               "Nome Estação", "Nº UH Mon", "Nº UH Jus",
               "Vaz Min", "Vaz Max", "Taxa Consumo"]
    for linha in bloco:
        to_df = [linha[4:7], linha[9:11], linha[14:26],
                linha[29:32], linha[34:37], linha[39:49],
                linha[49:59], linha[59:69]]
        dados.append(to_df)
    df_ue = pd.DataFrame(dados, columns=colunas)
    df_ue.set_index("Nº Estação", inplace=True)
    local = Path("blocos/UE.xls")
    df_ue.to_excel(local)


def cria_df_uh(bloco):

    dados = []
    colunas = ["Nº Usina", "REE", "Vol. Arm. Inicial %", 
               "Vaz. Def. Min", "Evap", "Estágio", 
               "Vol. Morto Inicial", "Lim. Sup. Vertimento",
               "Balanço Hídrico Fio D'água"]

    for linha in bloco:
        if len(linha)>41:
            to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                    linha[39].strip(), linha[44:46].strip(), linha[49:59].strip(), linha[59:69].strip(), linha[69].strip()]
        else:
            to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                    linha[39].strip(), linha[44:46].strip()]
        dados.append(to_df)

    df_uh = pd.DataFrame(dados, columns=colunas)
    df_uh.set_index("Nº Usina", inplace=True)

    local = Path("blocos/UH.xls")
    df_uh.to_excel(local)


# def cria_df_ac(bloco):

#     dados = []
#     colunas = ["Nº Usina", "Id Param Mod", "Novo Valor Param",
#                "Mês de Alt.",  "Nº Semana", "Ano Alt"]
    
#     for linha in bloco:
#         print(len(linha))

#     df_ac = pd.DataFrame(dados, columns=colunas)
#     df_ac.set_index("Nº Usina", inplace=True)

#     local = Path('blocos/AC.xls')
#     df_ac.to_excel(local)


def cria_df_ar(bloco):

    dados = []
    colunas = ["Período CVaR", "Lambda", "Alfa"]

    for linha in bloco:
        to_df = [linha[5:8].strip(), None, None]
        dados.append(to_df)
    
    df_ar = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/AR.xls')
    df_ar.to_excel(local)


def cria_df_cd(bloco):
    
    dados = []
    colunas = ["Nº Curva", "Subsistema", "Nome", "Indice",
                "1º % da carga", "1º Custo", "2º % da carga",
                "2º Custo", "3º % da carga", "3º Custo"]
    
    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:26].strip(), linha[29:34].strip(), linha[34:44].strip(),
                 linha[44:49].strip(), linha[49:59].strip(), linha[59:64].strip(),
                 linha[64:74].strip()]
        dados.append(to_df)

    df_cd = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/CD.xls')
    df_cd.to_excel(local)


def cria_df_ci(bloco):
    pass


def cria_df_cq(bloco):

    dados = []
    colunas = ["Nº Restr. Vaz.", "Estágio", "Nº Hidrelétrica",
               "Coef. Var.", "Tipo Restr."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)
    
    df_cq = pd.DataFrame(dados, columns=colunas)
    df_cq.set_index("Nº Restr. Vaz.", inplace=True)

    local = Path('blocos/CQ.xls')
    df_cq.to_excel(local)



def cria_df_cv(bloco):

    dados = []
    colunas = ["Nº Rest Vol", "Estágio", "Nº Estação/Usina",
               "Coef.", "Tipo Variável"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)

    df_cv = pd.DataFrame(dados, columns=colunas)
    df_cv.set_index("Nº Rest Vol", inplace=True)

    local = Path('blocos/CV.xls')
    df_cv.to_excel(local)


def cria_df_dp(bloco):

    dados = []
    colunas = ["Estágio", "Subsistema", "Carga Pesada", "Duração Pesada",
               "Carga Média", "Duração Média", "Carga Leve", "Duração Leve"]

    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[19:29].strip(),
                 linha[29:39].strip(), linha[39:49].strip(), linha[49:59].strip(),
                 linha[59:69].strip(), linha[69:79].strip()]
        dados.append(to_df)

    df_dp = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/DP.xls')
    df_dp.to_excel(local)