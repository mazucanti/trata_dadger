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
               "Vaz Min", "Vaz Max", ]