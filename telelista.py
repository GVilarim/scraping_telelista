from urllib import request
import utils as ut

locais = ut.select_sql_server("SELECT VC_IBG_UF, VC_IBG_CIDADE FROM PORTAL_IBGE WHERE VC_IBG_UF = 'PE'")

for local in locais:
    uf = local[0].lower()
    cidade = ut.remover_acentos(local[1]).replace(' ', '+').replace('-', '+').lower()
    link = f"https://www.telelistas.net/{uf}/{cidade}/escolas+particulares"
# link = 'https://www.telelistas.net/pe/recife/escolas+particulares'
    # lista = ["https://www.telelistas.net/sp/sao+paulo/farmacias+de+manipulacao", "https://www.telelistas.net/rj/rio+de+janeiro/farmacias+de+manipulacao"]
# link = "https://www.telelistas.net/PE/recife/farmacias+de+manipulacao"
    url = request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page = request.urlopen(url)
    ut.parse(page)
