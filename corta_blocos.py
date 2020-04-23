import re
import pandas as pd
from pathlib import Path

def main(rv):
    MN = ['AC', 'AR', 'CD', 'CI', 'CQ', 'CT', 'CV', 'DP',
        'DT', 'EV', 'EZ', 'FC', 'FD', 'FI', 'FT', 'FU',
        'GP', 'HQ', 'HV', 'IA', 'IR', 'LQ', 'LU', 'LV', 
        'MP', 'MT', 'NI', 'PQ', 'RE', 'RQ', 'SB', 'TE',
        'TI', 'TX', 'UE', 'UH', 'VE', 'VI']

    local = Path("DECOMP/DADGER.RV%d" % rv)
    for mn in MN:
        with open('blocos/%s' % mn, 'w') as fp:
            reg = re.compile("^%s.*" % mn)
            with open(local, 'r', encoding="ISO-8859-1") as dadger:
                for linha in dadger:
                    if reg.match(linha) != None:
                        linha = linha.replace(".",",")
                        fp.write(linha)