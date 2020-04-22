import trata_blocos as tb
from pathlib import Path

funcs = [tb.cria_df_ac, tb.cria_df_ar, tb.cria_df_cd, tb.cria_df_ci, tb.cria_df_cq,
         tb.cria_df_ct, tb.cria_df_cv, tb.cria_df_dp, tb.cria_df_dt, tb.cria_df_ev,
         tb.cria_df_ez, tb.cria_df_fc, tb.cria_df_fd, tb.cria_df_fi, tb.cria_df_ft,
         tb.cria_df_fu, tb.cria_df_gp, tb.cria_df_hq, tb.cria_df_hv, tb.cria_df_ia,
         tb.cria_df_ir, tb.cria_df_lq, tb.cria_df_lu, tb.cria_df_lv, tb.cria_df_mp,
         tb.cria_df_mt, tb.cria_df_ni, tb.cria_df_pq, tb.cria_df_re, tb.cria_df_rq,
         tb.cria_df_sb, tb.cria_df_te, tb.cria_df_ti, tb.cria_df_tx, tb.cria_df_ue,
         tb.cria_df_uh, tb.cria_df_ve, tb.cria_df_vi]

MN = ['AC', 'AR', 'CD', 'CI', 'CQ',
      'CT', 'CV', 'DP', 'DT', 'EV',
      'EZ', 'FC', 'FD', 'FI', 'FT', 
      'FU', 'GP', 'HQ', 'HV', 'IA',
      'IR', 'LQ', 'LU', 'LV', 'MP',
      'MT', 'NI', 'PQ', 'RE', 'RQ',
      'SB', 'TE', 'TI', 'TX', 'UE',
      'UH', 'VE', 'VI']


for i in range(len(MN)):
    entrada = Path("bloco/%s" % MN[i])
    with open(entrada, 'r') as bloco:
        df = funcs[i](bloco)
        saida = Path("bloco/%s.xls" % MN[i])
        df.to_excel(saida)