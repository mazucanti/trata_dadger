import pandas as pd
from pathlib import Path


import corta_blocos


def cria_df_ct(dadger):

    dados = []
    colunas = ["Nº Usina", "Sub Sis", "Nome", "Estágio", 
               "Ger Min Pesada", "Cap Ger Pesada", "Custo Ger Pesada", 
               "Ger Min Media", "Cap Ger Media", "Custo Ger Media", 
               "Ger Min Leve", "Cap Ger Leve", "Custo Ger Leve"]

    local = Path("blocos/CT")
    with open(local,'r') as ct:
        for linha in ct:
            to_df = [linha[4:7].strip(), linha[9:11].strip(), 
                    linha[14:24].strip(), linha[24:26].strip(),
                    linha[29:34].strip(), linha[34:39].strip(), linha[39:49].strip(),
                    linha[49:54].strip(), linha[54:59].strip(), linha[59:69].strip(),
                    linha[69:74].strip(), linha[74:79].strip(), linha[79:89].strip()]
            dados.append(to_df)
    df_ct = pd.DataFrame(dados, columns=colunas)
    return df_ct


def cria_df_sb(dadger):

    dados = []
    colunas = ["Sub Sistema", "Mnemônico"]

    local = Path("blocos/SB")
    with open(local,'r') as sb:
        for linha in sb:
            to_df = [linha[4:6], linha[9:11]]
            dados.append(to_df)
    df_sb = pd.DataFrame(dados, columns=colunas)
    df_sb.set_index("Sub Sistema", inplace=True)
    return df_sb


def cria_df_ue(dadger):

    dados = []
    colunas = ["Nº Estação", "Sub Sistema",
               "Nome Estação", "Nº UH Mon", "Nº UH Jus",
               "Vaz Min", "Vaz Max", "Taxa Consumo"]
    
    local = Path("blocos/CT")
    with open(local,'r') as ct:
        for linha in ct:
            to_df = [linha[4:7], linha[9:11], linha[14:26],
                    linha[29:32], linha[34:37], linha[39:49],
                    linha[49:59], linha[59:69]]
            dados.append(to_df)
    df_ue = pd.DataFrame(dados, columns=colunas)
    df_ue.set_index("Nº Estação", inplace=True)
    return df_ue


def cria_df_uh(dadger):

    dados = []
    colunas = ["Nº Usina", "REE", "Vol. Arm. Inicial %", 
               "Vaz. Def. Min", "Evap", "Estágio", 
               "Vol. Morto Inicial", "Lim. Sup. Vertimento",
               "Balanço Hídrico Fio D'água"]

    local = Path("blocos/CT")
    with open(local,'r') as ct:
        for linha in ct:
            if len(linha)>41:
                to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                        linha[39].strip(), linha[44:46].strip(), linha[49:59].strip(), linha[59:69].strip(), linha[69].strip()]
            else:
                to_df = [linha[0:2].strip(), linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                        linha[39].strip(), linha[44:46].strip()]
            dados.append(to_df)
    df_uh = pd.DataFrame(dados, columns=colunas)
    df_uh.set_index("Nº Usina", inplace=True)
    return df_uh