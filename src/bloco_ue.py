import pandas as pd
import re


def corta_bloco(dadger):

    bloco_ue = []
    ue = re.compile("^UE.*")
    
    for linha in dadger:
        if ue.match(linha) != None:
            linha = linha.replace(".",",")
            bloco_ue.append(linha)
    
    return bloco_ue


def cria_df(dadger):

    ue = corta_bloco(dadger)
    dados = []
    colunas = ["Nº Estação", "Sub Sistema",
               "Nome Estação", "Nº UH Mon", "Nº UH Jus",
               "Vaz Min", "Vaz Max", "Taxa Consumo"]
    
    for linha in ue:
        to_df = [linha[4:7], linha[9:11], linha[14:26],
                 linha[29:32], linha[34:37], linha[39:49],
                 linha[49:59], linha[59:69]]
        dados.append(to_df)
    df_ue = pd.DataFrame(dados, columns=colunas)
    df_ue.set_index("Nº Estação", inplace=True)
    return df_ue