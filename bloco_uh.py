import pandas as pd
from pathlib import Path
import re


def importa_dadger():
    # rv = int(input("Revisão atual: "))
    rv = 2
    bloco_uh = []
    uh = re.compile("^UH.*")

    local_dadger = Path("DECOMP/DADGER.RV%d" % rv)

    with open(local_dadger, 'r', encoding="ISO-8859-1") as dadger:
        for linha in dadger:
            if uh.match(linha) != None:
                bloco_uh.append(linha)
    
    return bloco_uh


uh = importa_dadger()
with open("jaaj.txt", 'w') as fp:
    for linha in uh:
        fp.write(linha)