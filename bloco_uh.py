import pandas as pd
from pathlib import Path
import re


def importa_dadger():
    # rv = int(input("Revisão atual: "))
    rv = 1
    bloco_uh = []
    uh = re.compile("^UH.*")

    local_dadger = Path("DECOMP/DADGER.RV%d" % rv)

    with open(local_dadger, 'r', encoding="ISO-8859-1") as dadger:
        for linha in dadger:
            if uh.match(linha) != None:
                linha = linha.replace(".",",")
                bloco_uh.append(linha)
    
    return bloco_uh


def cria_df():
    uh = importa_dadger()
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

def trata_df():
    df = cria_df()
    df.drop(["UH"], axis=1, inplace=True)
    df.set_index("Nº Usina", inplace=True)
    return df

df = trata_df()
df.to_csv("debug.csv")