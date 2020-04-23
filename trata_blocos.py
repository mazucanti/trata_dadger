import pandas as pd
from pathlib import Path
import re


def cria_df_ct(bloco):

    dados = []
    colunas = ["Nº Usina", "Sub Sis", "Nome", "Estágio", 
               "Ger Min Pesada", "Cap Ger Pesada", "Custo Ger Pesada", 
               "Ger Min Media", "Cap Ger Media", "Custo Ger Media", 
               "Ger Min Leve", "Cap Ger Leve", "Custo Ger Leve"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), 
                linha[14:24].strip(), linha[24:26].strip(),
                linha[29:34].strip(), linha[34:39].strip(), linha[39:49].strip(),
                linha[49:54].strip(), linha[54:59].strip(), linha[59:69].strip(),
                linha[69:74].strip(), linha[74:79].strip(), linha[79:89].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)
    
    
    return df

def cria_df_sb(bloco):

    dados = []
    colunas = ["Sub Sistema", "Mnemônico"]

    for linha in bloco:
        to_df = [linha[4:6], linha[9:11]]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Sub Sistema", inplace=True)

    return df

def cria_df_ue(bloco):

    dados = []
    colunas = ["Nº Estação", "Sub Sistema",
               "Nome Estação", "Nº UH Mon", "Nº UH Jus",
               "Vaz Min", "Vaz Max", "Taxa Consumo"]
    for linha in bloco:
        to_df = [linha[4:7], linha[9:11], linha[14:26],
                linha[29:32], linha[34:37], linha[39:49],
                linha[49:59], linha[59:69]]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Estação", inplace=True)

    return df

def cria_df_uh(bloco):

    dados = []
    colunas = ["Nº Usina", "REE", "Vol. Arm. Inicial %", 
               "Vaz. Def. Min", "Evap", "Estágio", 
               "Vol. Morto Inicial", "Lim. Sup. Vertimento",
               "Balanço Hídrico Fio D'água"]

    for linha in bloco:
        if len(linha)>41:
            to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                    linha[39].strip(), linha[44:46].strip(), linha[49:59].strip(), linha[59:69].strip(), linha[69].strip()]
        else:
            to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(), linha[24:34].strip(),
                    linha[39].strip(), linha[44:46].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    return df

def cria_df_ac(bloco):
    
    dados = []
    colunas = ["Nº Usina", "Id Param Mod", "Parâmetro", "Parâmetro",
                   "Mês de Alt.",  "Nº Semana", "Ano Alt"]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:15].strip()]
        if to_df[1] == "NOMEUH":
            to_df += [linha[19:31].strip(), None]

        elif to_df[1] == "NUMPOS":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "NUMJUS":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "DESVIO":
            to_df += [linha[19:24].strip(), linha[24:34].strip()]

        elif to_df[1] == "VOLMIN":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "VOLMAX":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "COTVOL":
            to_df += [linha[19:24].strip(), linha[24:39].strip()]

        elif to_df[1] == "COTARE":
            to_df += [linha[19:24].strip(), linha[24:39].strip()]

        elif to_df[1] == "COFEVA":
            to_df += [linha[19:24].strip(), linha[24:29].strip()]

        elif to_df[1] == "NUMCON":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "NUMMAQ":
            to_df += [linha[19:24].strip(), linha[24:29].strip()]

        elif to_df[1] == "POTEFE":
            to_df += [linha[19:24].strip(), linha[24:34].strip()]

        elif to_df[1] == "ALTEFE":
            to_df += [linha[19:24].strip(), linha[24:34].strip()]

        elif to_df[1] == "VAZEFE":
            to_df += [linha[19:24].strip(), linha[24:29].strip()]

        elif to_df[1] == "PROESP":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "PERHID":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "NCHAVE":
            to_df += [linha[19:24].strip(), linha[24:34].strip()]

        elif to_df[1] == "COTVAZ":
            to_df += [linha[19:24].strip(), linha[24:29].strip(), linha[29:44].strip()]

        elif to_df[1] == "JUSMED":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "VERTJU":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "VAZMIN":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "NUMBAS":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "TIPTUR":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "TIPERH":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "VAZCCF":
            to_df += [linha[19:29].strip(), linha[29:34].strip(), linha[34:44].strip()]

        elif to_df[1] == "JUSENA":
            to_df += [linha[19:24].strip(), None]

        elif to_df[1] == "VSVERT":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "VMDESV":
            to_df += [linha[19:29].strip(), None]

        elif to_df[1] == "TIPUSI":
            continue

        if len(linha) >= 76: to_df += [linha[69:72].strip(), linha[75], linha[76:80].strip()]
        else: to_df += [None] * 3
        dados.append(to_df)
    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_ar(bloco):

    dados = []
    colunas = ["Período CVaR", "Lambda", "Alfa"]

    for linha in bloco:
        to_df = [linha[5:8].strip(), None, None]
        dados.append(to_df)
    
    df = pd.DataFrame(dados, columns=colunas)
    
    
    return df

def cria_df_cd(bloco):
    
    dados = []
    colunas = ["Nº Curva", "Subsistema", "Nome", "Indice",
                "1º % da carga", "1º Custo", "2º % da carga",
                "2º Custo", "3º % da carga", "3º Custo"]
    
    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:26].strip(), linha[29:34].strip(), linha[34:44].strip(),
                 linha[44:49].strip(), linha[49:59].strip(), linha[59:64].strip(),
                 linha[64:74].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_ci(bloco):
    return pd.DataFrame()


def cria_df_cq(bloco):

    dados = []
    colunas = ["Nº Restr. Vaz.", "Estágio", "Nº Hidrelétrica",
               "Coef. Var.", "Tipo Restr."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)
    
    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restr. Vaz.", inplace=True)

    
    return df

def cria_df_cv(bloco):

    dados = []
    colunas = ["Nº Rest Vol", "Estágio", "Nº Estação/Usina",
               "Coef.", "Tipo Variável"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Rest Vol", inplace=True)

    
    return df

def cria_df_dp(bloco):

    dados = []
    colunas = ["Estágio", "Subsistema", "Carga Pesada", "Duração Pesada",
               "Carga Média", "Duração Média", "Carga Leve", "Duração Leve"]

    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[19:29].strip(),
                 linha[29:39].strip(), linha[39:49].strip(), linha[49:59].strip(),
                 linha[59:69].strip(), linha[69:79].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    
    
    return df

def cria_df_dt(bloco):

    dados = []
    colunas = ["Dia", "Mês", "Ano"]

    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:18].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_ev(bloco):

    dados = []
    colunas = ["Modelo", "Referência"]

    for linha in bloco:
        if len(linha) != 0:
            to_df = [linha[4], linha[9:12]]
        else:
            to_df = [None, None]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_ez(bloco):

    dados = []
    colunas = ["Nº Reservatório", "% Vaz. Min."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:14].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Reservatório", inplace=True)

    return df

def cria_df_fc(bloco):

    dados = []
    colunas = ["Arquivo de Cortes", "Nome do Arquivo"]

    for linha in bloco:
        to_df = [linha[4:10].strip(), linha[14:len(linha)-1].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    
    
    return df

def cria_df_fd(bloco):

    dados = []
    colunas = ["Nº Usina"]
    maximo = 0

    for linha in bloco:
        to_df = [linha[4:7].strip()] + re.findall(".,...", linha)
        fatores = len(to_df) - 1
        maximo = fatores if fatores >= maximo else maximo
        dados.append(to_df)

    for i in range(maximo):
        colunas += ["Fator Estágio %d" % (i+1)]
    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_fi(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", "DE", "PARA", "Fator Participação"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip(),
                 linha[19:21].strip(), linha[24:34].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    
    return df

def cria_df_ft(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", "Nº Térmica", "Subsistema",
               "Fator Particip."]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:21].strip(), linha[24:34].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    
    return df

def cria_df_fu(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Estágio", "Nº Usina", "Fator Particip."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip()]
        dados.append(to_df)
    
    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    
    return df

def cria_df_gp(bloco):

    dados = []
    colunas = ["Tolerância Convergência"]

    for linha in bloco:
        dados.append(linha[4:14].strip())

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_hq(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Estágio Inicial", "Estágio Final"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição", inplace=True)

    
    return df

def cria_df_hv(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Eságio Inicial", "Estágio Final"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição", inplace=True)

    
    return df

def cria_df_ia(bloco):
    
    dados = []
    colunas = ["Estágio", "Subsistema I", "Subsistema J", "Ind. Penalidade",
               "Cap. Max. I para J Pesada", "Cap. Max. J para I Pesada",
               "Cap. Max. I para J Média", "Cap. Max. J para I Média",
               "Cap. Max. I para J Leve", "Cap. Max. J para I Leve"]
    
    for linha in bloco:
        if len(linha) != 0:
            to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:16].strip(), linha[17],
                    linha[19:29].strip(), linha[29:39].strip(), linha[39:49].strip(),
                    linha[49:59].strip(), linha[59:69].strip(), linha[69:79].strip()]
        else:
            to_df = [None] * len(colunas)
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_ir(bloco):
    
    dados = []
    colunas = ["Id. Saída", "Opç. Impressão", "Max. Pág."]

    for linha in bloco:
        opt_saida = linha[4:11].strip()
        if opt_saida == "NORMAL":
            to_df = [opt_saida, linha[14:16].strip(), linha[19:21].strip()]
        elif opt_saida == "ACOPLA":
            to_df = [opt_saida, linha[14:16].strip(), None]
        else:
            to_df = [opt_saida, None, None]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_lq(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", 
               "LI Pesada", "LS Pesada", "LI Média",
               "LS Média", "LI Leve", "LS Leve"]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:34].strip(), linha[34:44].strip(), linha[44:54].strip(),
                 linha[54:64].strip(), linha[64:74].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    
    return df

def cria_df_lu(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio",
               "LI Pat. 1", "LS Pat. 1", "LI Pat. 2",
               "LS Pat. 2", "LI Pat. 3", "LS Pat. 3"]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(),
                 linha[14:24].strip(), linha[24:34].strip(), linha[34:44].strip(),
                 linha[44:54].strip(), linha[54:64].strip(), linha[64:74].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    return df

def cria_df_lv(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", "LI", "LS"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:34].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição")

    
    return df

def cria_df_mp(bloco):
    
    dados = []
    colunas = ["Nº Usina"]
    maximo = 0

    for linha in bloco:
        to_df = [linha[4:7].strip()] + re.findall(".,...", linha)
        fatores = len(to_df) - 1
        maximo = fatores if fatores >= maximo else maximo
        dados.append(to_df)

    for i in range(maximo):
        colunas += ["Fator Man. Estágio %d" % (i+1)]

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_mt(bloco):

    dados = []
    colunas = ["Nº Usina", "Subsistema"]
    maximo = 0

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip()] + re.findall(".,...", linha)
        fatores = len(to_df) - 2
        maximo = fatores if fatores >= maximo else maximo
        dados.append(to_df)

    for i in range(maximo):
        colunas += ["Fator Man. Estágio %d" % (i+1)]

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_ni(bloco):

    dados = []
    colunas = ["Nº Iterações", "Max/Min"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), None]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_pq(bloco):
    
    dados = []
    colunas = ["Nome Usina", "Subsistema", "Estágio", "Ger. Pat. 1",
               "Ger. Pat. 2", "Ger. Pat. 3"]

    for linha in bloco:
        to_df = [linha[4:14].strip(), linha[14:16].strip(), linha[19:21].strip(),
                 linha[24:29].strip(), linha[29:34].strip(), linha[34:39].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_re(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Estágio Inicial", "Estágio Final"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Restrição", inplace=True)

    
    return df

def cria_df_rq(bloco):
    return pd.DataFrame()


def cria_df_tx(bloco):
    return pd.DataFrame()


def cria_df_te(bloco):

    dados = []
    colunas = ["Título"]

    for linha in bloco:
        to_df = [linha[4:84].strip()]
        dados.append(to_df)

    df = pd.DataFrame(dados, columns=colunas)

    
    return df

def cria_df_ti(bloco):

    dados = []
    colunas = ["Nº Usina"]
    maximo = 0

    for linha in bloco:
        to_df = [linha[4:7].strip()] + re.findall("[0-9]{1,2},[0-9]", linha)
        fatores = len(to_df) - 1
        maximo = fatores if fatores >= maximo else maximo
        dados.append(to_df)

    for i in range(maximo):
        colunas += ["Vaz. Desv. Estágio %d" % (i+1)]

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_ve(bloco):

    dados = []
    colunas = ["Nº Usina"]
    maximo = 0

    for linha in bloco:
        to_df = [linha[4:7].strip()] + re.findall("[0-9]{1,2},[0-9]{2}|[0-9]{3},0",
                                                  linha)
        fatores = len(to_df) - 1
        maximo = fatores if fatores >= maximo else maximo
        dados.append(to_df)

    for i in range(maximo):
        colunas += ["Vol. Esp. Estágio %d" % (i+1)]

    df = pd.DataFrame(dados, columns=colunas)
    df.set_index("Nº Usina", inplace=True)

    
    return df

def cria_df_vi(bloco):
    return pd.DataFrame()

