import re
import pandas as pd
from pathlib import Path


MN = ['TE', 'SB', 'UH', 'CT', 'UE', 'DP', 'CD',
      'PQ', 'IA', 'TX', 'GP', 'NI', 'DT', 'MP',
      'MT', 'FD', 'VE', 'RE', 'LU', 'FU', 'FT',
      'FI', 'VI', 'AC', 'IR', 'CI', 'FC', 'TI',
      'RQ', 'EZ', 'HV', 'LV', 'CV', 'HQ', 'LQ', 
      'CQ', 'AR', 'EV']
print(len(MN))
local = Path("DECOMP/DADGER.RV2")
for mn in MN:
    with open('debug/%s.txt' % mn, 'w') as fp:
        reg = re.compile("^%s.*" % mn)
        with open(local, 'r', encoding="ISO-8859-1") as dadger:
            for linha in dadger:
                if reg.match(linha) != None:
                    linha = linha.replace(".",",")
                    fp.write(linha)