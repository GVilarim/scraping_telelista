import utils as ut

# Forma alternativa para ler os dados de cidade e UF a partir do arquivo cidades.xlsx
# df_cidades = ut.pd.read_excel('data\\cidades.xlsx', sheet_name='Cidades')
# locais = [[df.loc[line, 'cidade'], df.loc[line, 'uf']] for line in range(df['cidade'].count())]

locais = ut.select_sql_server("SELECT VC_IBG_UF, VC_IBG_CIDADE FROM PORTAL_IBGE WHERE VC_IBG_UF = 'PE'")

for local in locais:
    uf = local[0].lower()
    cidade = ut.remover_acentos(local[1]).replace(' ', '+').replace('-', '+').lower()
    link = f"https://www.telelistas.net/{uf}/{cidade}/escolas+particulares"
    url = ut.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page = ut.request.urlopen(url)
    ut.parse(page)
