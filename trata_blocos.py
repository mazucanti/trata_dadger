import pandas as pd
from pathlib import Path
import re


import corta_blocos


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

    df_ct = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/CT.xls')
    df_ct.to_excel(local)


def cria_df_sb(bloco):

    dados = []
    colunas = ["Sub Sistema", "Mnemônico"]

    for linha in bloco:
        to_df = [linha[4:6], linha[9:11]]
        dados.append(to_df)

    df_sb = pd.DataFrame(dados, columns=colunas)
    df_sb.set_index("Sub Sistema", inplace=True)

    local = Path("blocos/SB.xls")
    df_sb.to_excel(local)


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
    df_ue = pd.DataFrame(dados, columns=colunas)
    df_ue.set_index("Nº Estação", inplace=True)
    local = Path("blocos/UE.xls")
    df_ue.to_excel(local)


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

    df_uh = pd.DataFrame(dados, columns=colunas)
    df_uh.set_index("Nº Usina", inplace=True)

    local = Path("blocos/UH.xls")
    df_uh.to_excel(local)


# def cria_df_ac(bloco):

#     dados = []
#     colunas_ini = ["Nº Usina", "Id Param Mod", "Parâmetros", "Parâmetros"]
#     colunas_fin = "Mês de Alt.",  "Nº Semana", "Ano Alt"]
    
#     for linha in bloco:
#         print(len(linha))

#     df_ac = pd.DataFrame(dados, columns=colunas)
#     df_ac.set_index("Nº Usina", inplace=True)

#     local = Path('blocos/AC.xls')
#     df_ac.to_excel(local)


def cria_df_ar(bloco):

    dados = []
    colunas = ["Período CVaR", "Lambda", "Alfa"]

    for linha in bloco:
        to_df = [linha[5:8].strip(), None, None]
        dados.append(to_df)
    
    df_ar = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/AR.xls')
    df_ar.to_excel(local)


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

    df_cd = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/CD.xls')
    df_cd.to_excel(local)


def cria_df_ci(bloco):
    pass


def cria_df_cq(bloco):

    dados = []
    colunas = ["Nº Restr. Vaz.", "Estágio", "Nº Hidrelétrica",
               "Coef. Var.", "Tipo Restr."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)
    
    df_cq = pd.DataFrame(dados, columns=colunas)
    df_cq.set_index("Nº Restr. Vaz.", inplace=True)

    local = Path('blocos/CQ.xls')
    df_cq.to_excel(local)



def cria_df_cv(bloco):

    dados = []
    colunas = ["Nº Rest Vol", "Estágio", "Nº Estação/Usina",
               "Coef.", "Tipo Variável"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip(), linha[34:38].strip()]
        dados.append(to_df)

    df_cv = pd.DataFrame(dados, columns=colunas)
    df_cv.set_index("Nº Rest Vol", inplace=True)

    local = Path('blocos/CV.xls')
    df_cv.to_excel(local)


def cria_df_dp(bloco):

    dados = []
    colunas = ["Estágio", "Subsistema", "Carga Pesada", "Duração Pesada",
               "Carga Média", "Duração Média", "Carga Leve", "Duração Leve"]

    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[19:29].strip(),
                 linha[29:39].strip(), linha[39:49].strip(), linha[49:59].strip(),
                 linha[59:69].strip(), linha[69:79].strip()]
        dados.append(to_df)

    df_dp = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/DP.xls')
    df_dp.to_excel(local)


def cria_df_dt(bloco):

    dados = []
    colunas = ["Dia", "Mês", "Ano"]

    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:18].strip()]
        dados.append(to_df)

    df_dt = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/DT.xls')
    df_dt.to_excel(local)


def cria_df_ev(bloco):

    dados = []
    colunas = ["Modelo", "Referência"]

    for linha in bloco:
        to_df = [linha[4], linha[9:12]]
        dados.append(to_df)

    df_ev = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/EV.xls')
    df_ev.to_excel(local)


def cria_df_ez(bloco):

    dados = []
    colunas = ["Nº Reservatório", "% Vaz. Min."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:14].strip()]
        dados.append(to_df)

    df_ez = pd.DataFrame(dados, columns=colunas)
    df_ez.set_index("Nº Reservatório", inplace=True)

    local = Path("blocos/EZ.xls")
    df_ez.to_excel(local)


def cria_df_fc(bloco):

    dados = []
    colunas = ["Arquivo de Cortes", "Nome do Arquivo"]

    for linha in bloco:
        to_df = [linha[4:10].strip(), linha[14:len(linha)-1].strip()]
        dados.append(to_df)

    df_fc = pd.DataFrame(dados, columns=colunas)
    
    local = Path('blocos/FC.xls')
    df_fc.to_excel(local)


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
    df_fd = pd.DataFrame(dados, columns=colunas)
    df_fd.set_index("Nº Usina", inplace=True)

    local = Path('blocos/FD.xls')
    df_fd.to_excel(local)


def cria_df_fi(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", "DE", "PARA", "Fator Participação"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip(),
                 linha[19:21].strip(), linha[24:34].strip()]
        dados.append(to_df)

    df_fi = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/FI.xls')
    df_fi.to_excel(local)


def cria_df_ft(bloco):

    dados = []
    colunas = ["Nº Restrição", "Estágio", "Nº Térmica", "Subsistema",
               "Fator Particip."]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:21].strip(), linha[24:34].strip()]
        dados.append(to_df)

    df_ft = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/FT.xls')
    df_ft.to_excel(local)


def cria_df_fu(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Estágio", "Nº Usina", "Fator Particip."]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:17].strip(),
                 linha[19:29].strip()]
        dados.append(to_df)
    
    df_fu = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/FU.xls')
    df_fu.to_excel(local)



def cria_df_gp(bloco):

    dados = []
    colunas = ["Tolerância Convergência"]

    for linha in bloco:
        dados.append(linha[4:14].strip())

    df_gp = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/GP.xls')
    df_gp.to_excel(local)


def cria_df_hq(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Estágio Inicial", "Estágio Final"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip()]
        dados.append(to_df)

    df_hq = pd.DataFrame(dados, columns=colunas)
    df_hq.set_index("Nº Restrição", inplace=True)

    local = Path('blocos/HQ.xls')
    df_hq.to_excel(local)


def cria_df_hv(bloco):
    
    dados = []
    colunas = ["Nº Restrição", "Eságio Inicial", "Estágio Final"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:16].strip()]
        dados.append(to_df)

    df_hv = pd.DataFrame(dados, columns=colunas)
    df_hv.set_index("Nº Restrição", inplace=True)

    local = Path('blocos/HV.xls')
    df_hv.to_excel(local)


def cria_df_ia(bloco):
    
    dados = []
    colunas = ["Estágio", "Subsistema I", "Subsistema J", "Ind. Penalidade",
               "Cap. Max. I para J Pesada", "Cap. Max. J para I Pesada",
               "Cap. Max. I para J Média", "Cap. Max. J para I Média",
               "Cap. Max. I para J Leve", "Cap. Max. J para I Leve"]
    
    for linha in bloco:
        to_df = [linha[4:6].strip(), linha[9:11].strip(), linha[14:16].strip(), linha[17],
                 linha[19:29].strip(), linha[29:39].strip(), linha[39:49].strip(),
                 linha[49:59].strip(), linha[59:69].strip(), linha[69:79].strip()]
        dados.append(to_df)

    df_ia = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/IA.xls')
    df_ia.to_excel(local)


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

    df_ir = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/IR.xls')
    df_ir.to_excel(local)


def cria_df_lq(bloco):

    dados = []
    colunas = ["Nº Rest. Vaz.", "Estágio", 
               "LI Pesada", "LS Pesada", "LI Média",
               "LS Média", "LI Leve", "LS Leve"]
    
    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:34].strip(), linha[34:44].strip(), linha[44:54].strip(),
                 linha[54:64].strip(), linha[64:74].strip()]
        dados.append(to_df)

    df_lq = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/LQ.xls')
    df_lq.to_excel(local)


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

    df_lu = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/LU.xls')
    df_lu.to_excel(local)


def cria_df_lv(bloco):

    dados = []
    colunas = ["Nº Rest. Vol,", "Estágio", "LI", "LS"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), linha[9:11].strip(), linha[14:24].strip(),
                 linha[24:34].strip()]
        dados.append(to_df)

    df_lv = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/LV.xls')
    df_lv.to_excel(local)


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

    df_mp = pd.DataFrame(dados, columns=colunas)
    df_mp.set_index("Nº Usina", inplace=True)

    local = Path('blocos/MP.xls')
    df_mp.to_excel(local)


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

    df_mt = pd.DataFrame(dados, columns=colunas)
    df_mt.set_index("Nº Usina", inplace=True)

    local = Path('blocos/MT.xls')
    df_mt.to_excel(local)


def cria_df_ni(bloco):

    dados = []
    colunas = ["Nº Iterações", "Max/Min"]

    for linha in bloco:
        to_df = [linha[4:7].strip(), None]
        dados.append(to_df)

    df_ni = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/NI.xls')
    df_ni.to_excel(local)


def cria_df_pq(bloco):
    
    dados = []
    colunas = ["Nome Usina", "Subsistema", "Estágio", "Ger. Pat. 1",
               "Ger. Pat. 2", "Ger. Pat. 3"]

    for linha in bloco:
        to_df = [linha[4:14].strip(), linha[14:16].strip(), linha[19:21].strip(),
                 linha[24:29].strip(), linha[29:34].strip(), linha[34:39].strip()]
        dados.append(to_df)

    df_pq = pd.DataFrame(dados, columns=colunas)

    local = Path('blocos/PQ.xls')
    df_pq.to_excel(local)


def cria_df_re(bloco):
    pass