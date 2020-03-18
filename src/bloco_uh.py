import pandas as pd
import re


def corta_bloco(dadger, rv):

    bloco_uh = []
    uh = re.compile("^UH.*")

    for linha in dadger:
        if uh.match(linha) != None:
            linha = linha.replace(".",",")
            bloco_uh.append(linha)
    
    return bloco_uh


def cria_df(dadger, rv):
    uh = corta_bloco(dadger, rv)
    dados = []
    colunas = ["UH", "Nº Usina", "REE", "Vol. Arm. Inicial %", "Vaz. Def. Min", "Evap", "Estágio", "Vol. Morto Inicial", "Lim. Sup. Vertimento", "Balanço Hídrico Fio D'água"]
    for linha in uh:
        if len(linha)>41:
            to_df = [linha[0:2].strip(), linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                     linha[39].strip(), linha[44:46].strip(), linha[49:59].strip(), linha[59:69].strip(), linha[69].strip()]
        else:
            to_df = [linha[0:2].strip(), linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                     linha[39].strip(), linha[44:46].strip()]
        dados.append(to_df)
    df_uh = pd.DataFrame(dados, columns=colunas)
    return df_uh

def trata_df(dadger, rv):
    df = cria_df(dadger, rv)
    df.drop(["UH"], axis=1, inplace=True)
    df.set_index("Nº Usina", inplace=True)
    return df