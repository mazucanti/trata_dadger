import re
import pandas as pd
from pathlib import Path


MN = ['TE', 'PT', 'SB', 'UH', 'CT', 'UE', 'ME', 'DP', 'CD', 'TD',
      'BE', 'PQ', 'IT', 'IA', 'RC', 'TX', 'PE', 'GP', 'NI', 'PD',
      'DT', 'MP', 'MT', 'FD', 'VE', 'VM', 'DF', 'RE', 'LU', 'FU',
      'FT', 'FI', 'VI', 'QI', 'AC', 'RV', 'FP', 'FQ', 'IR', 'CI',
      'CE', 'RS', 'QA', 'QV', 'FC', 'EA', 'ES', 'TI', 'RQ', 'EZ',
      'HA', 'LA', 'CA', 'HV', 'LV', 'CV', 'HQ', 'LQ', 'CQ', 'HE',
      'CM', 'VR', 'DA', 'PU', 'VP', 'RT', 'SA', 'AR', 'EV', 'TG',
      'GS', 'NL', 'GL']

local = Path("DECOMP/DADGER.RV2")
with open(local, 'r', encoding="ISO-8859-1") as dadger:
    for mn in MN:
        with open('debug/%s.txt' % mn, 'w') as fp:
            reg = re.compile("^%s.*" % mn)

            for linha in dadger:
                if reg.match(linha) != None:
                    linha = linha.replace(".",",")
                    fp.write(linha)
    

        