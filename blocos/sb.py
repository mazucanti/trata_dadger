import pandas as pd
import re


def corta_bloco(dadger):

    bloco_sb = []
    sb = re.compile("^SB.*")

    for linha in dadger:
        if sb.match(linha) != None:
            linha = linha.replace(".",",")
            bloco_sb.append(linha)
    
    return bloco_sb


def cria_df(dadger):

    sb = corta_bloco(dadger)
    dados = []
    colunas = ["Sub Sistema", "Mnemônico"]
    
    for linha in sb:
        to_df = [linha[4:6], linha[9:11]]
        dados.append(to_df)
    df_sb = pd.DataFrame(dados, columns=colunas)
    df_sb.set_index("Sub Sistema", inplace=True)
    return df_sb