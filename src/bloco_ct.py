import pandas as pd
import re


def corta_bloco(dadger):

    bloco_ct = []
    ct = re.compile("^CT.*")

    for linha in dadger:
        if ct.match(linha) != None:
            bloco_ct.append(linha)
    
    return bloco_ct

with open("DECOMP/DADGER.RV1", 'r', encoding="ISO-8859-1") as dadger:
    ct = corta_bloco(dadger)

with open("../debug", 'w') as fp:
    for linha in ct:
        fp.write(linha)