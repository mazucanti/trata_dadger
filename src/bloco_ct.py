import pandas as pd
import re


def corta_bloco(dadger):

    bloco_ct = []
    ct = re.compile("^CT.*")

    for linha in dadger:
        if ct.match(linha) != None:
            linha = linha.replace(".",",")
            bloco_ct.append(linha)
    
    return bloco_ct


def cria_df(dadger):
    ct = corta_bloco(dadger)
    dados = []
    colunas = ["CT", "Nº Usina", "Sub Sis", "Nome", "Estágio", 
               "Ger Min Pesada", "Cap Ger Pesada", "Custo Ger Pesada", 
               "Ger Min Media", "Cap Ger Media", "Custo Ger Media", 
               "Ger Min Leve", "Cap Ger Leve", "Custo Ger Leve"]
    
    for linha in ct:
        to_df = [linha[0:2].strip(), linha[4:7].strip(), linha[9:11].strip(), 
                 linha[14:24].strip(), linha[24:26].strip(),
                 linha[29:34].strip(), linha[34:39].strip(), linha[39:49].strip(),
                 linha[49:54].strip(), linha[54:59].strip(), linha[59:69].strip(),
                 linha[69:74].strip(), linha[74:79].strip(), linha[79:89].strip()]
        dados.append(to_df)
    df_ct = pd.DataFrame(dados, columns=colunas)
    return df_ct


def trata_df(dadger):
    df = cria_df(dadger)
    df.drop(["CT"], axis=1, inplace=True)
    df.set_index("Nº Usina", inplace=True)
    return df

with open("DECOMP/DADGER.RV1", 'r', encoding="ISO-8859-1") as dadger:
    ct = trata_df(dadger)

ct.to_excel('debug.xls')