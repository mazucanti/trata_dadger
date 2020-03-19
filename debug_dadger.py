from blocos import sb
from pathlib import Path
import pandas as pd


local = Path("DECOMP/DADGER.RV2")
with open(local, 'r', encoding="ISO-8859-1") as dadger:
    df = sb.cria_df(dadger)
    
df.to_excel("debug.xls")