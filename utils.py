import json
import pyodbc
import unicodedata
import pandas as pd
import re
from scrapy import Selector
from urllib import request


def parse(page):
    response = Selector(text=page.read())
    print(page.geturl())
    html = response.xpath("//script")[7].extract()
    dicionario = html[html.index("{"):html.rindex("}") + 1]
    json_lista = json.loads(dicionario)

    dados = len(json_lista["items"]["dados"])
    items = []
    if dados > 0:
        for dado in range(dados):
            nome = json_lista["items"]["dados"][dado]["nome"].title()
            if 'location' in json_lista["items"]["dados"][dado]:
                coordenadas = json_lista["items"]["dados"][dado]["location"]
                coordenadas = f'{coordenadas[1]}, {coordenadas[0]}'
            else:
                coordenadas = 'Sem localização'

            endereco = json_lista["items"]["dados"][dado]["addr_full"]
            if len(endereco) > 0:
                informacoes = endereco[1].split('-')
                if 3 >= len(informacoes) > 2:
                    bairro, cidade, uf = informacoes
                elif len(informacoes) > 3:
                    bairro, complemento, cidade, uf = informacoes
                    bairro += '-' + complemento
                else:
                    cidade, uf = informacoes
                    bairro = cidade
                logradouro = endereco[0]
            else:
                bairro = 'Sem Localização'
                logradouro = 'Sem Localização'
                uf = 'Sem Localização'
                cidade = 'Sem Localização'

            telefone = json_lista["items"]["dados"][dado]["telefones"]["Clientes"].strip() \
                if 'Clientes' in json_lista["items"]["dados"][dado]["telefones"] else 'Não existe'

            fornecedor = json_lista["items"]["dados"][dado]["telefones"]["Fornecedores"].strip() \
                if 'Fornecedores' in json_lista["items"]["dados"][dado]["telefones"] else 'Não existe'

            whatsapp = json_lista["items"]["dados"][dado]["telefones"]["Whatsapp"].strip() \
                if 'Whatsapp' in json_lista["items"]["dados"][dado]["telefones"] else 'Não existe'

            items.append([nome, logradouro, bairro, cidade, uf, telefone, whatsapp, fornecedor, coordenadas])

        df_telelista = ler_planilha()
        df_auxiliar = pd.DataFrame(columns=['Nome', 'Logradouro', 'Bairro', 'Cidade', 'UF', 'Telefone',
                                            'WhatsApp', 'Fornecedores', 'Coordenadas'],
                                   data=items)
        df_telelista = pd.concat([df_telelista, df_auxiliar], ignore_index=True)
        salvar_planilha(df_telelista)
        pagina = response.xpath('//div[contains(text(), "Pág.")]/text()').extract()
        if len(pagina) > 0:
            pag_atual = int(re.search(r'[0-9]{1,2}', pagina[0]).group())
            if '?pag=' in page.geturl():
                pos = -1 if pag_atual < 10 else -2
                link = f"{page.geturl()[:pos]}{pag_atual + 1}"
            else:
                link = f"{page.geturl()}?pag={pag_atual + 1}"

            url = request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            parse(request.urlopen(url))


def ler_planilha():
    try:
        df_times = pd.read_excel('output_file\\telelista.xlsx', sheet_name='Escolas')
    except FileNotFoundError:
        df_times = pd.DataFrame(columns=['Nome', 'Logradouro', 'Bairro', 'Cidade', 'UF', 'Telefone',
                                         'WhatsApp', 'Fornecedores', 'Coordenadas'])
    return df_times


def salvar_planilha(df_times):
    writer = pd.ExcelWriter('arquivos\\telelista.xlsx')
    df_times.to_excel(writer, sheet_name='Escolas', index=False)
    writer.save()


def remover_acentos(txt):
    return unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def string_conexao_sql():
    conn = pyodbc.connect('Driver={SQL Server};'
                          r'Server=localhost\SQLEXPRESS01;'
                          'Database=BancoSQLServer;'
                          'Trusted_Connection=yes;')
    return conn.cursor()


def select_sql_server(query):
    cursor = string_conexao_sql()
    cursor.execute(query)
    return list(cursor)
