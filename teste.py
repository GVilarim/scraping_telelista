# import utils as ut
# import pandas as pd
#
# locais = ut.select_sql_server("SELECT * FROM PORTAL_IBGE")
#
# lista = []
# for local in locais:
#     id_ibge, cidade, num_uf, codigo, uf = local
#     lista.append([id_ibge, cidade, num_uf, codigo, uf])
#
# df_cidades = pd.DataFrame(columns=['id', 'cidade', 'num_uf', 'cod_cidade', 'uf'],
#                           data=lista)
#
# writer = pd.ExcelWriter('cidades.xlsx')
# df_cidades.to_excel(writer, sheet_name='Cidades', index=False)
# writer.save()