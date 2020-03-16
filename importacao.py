from pathlib import Path
import pandas as pd


#A codificação do arquivo é ISO-8859-1

def importa_dadger():
    rv = int(input("Revisão atual: "))

    local = Path("DECOMP/DADGER.RV%d" % rv)

    dadger = pd.read_csv(local, encoding="ISO-8859-1")
    return dadger
