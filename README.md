# Web-Scraping-Telelista
Web Scrapping realizado no site da Telelista para raspar dados de todas as cidades do Brasil relacionada alguma atividade ou empresa utilizando o módulo urllib e scrapy.Selector.

# Requisitos Necessários
Para executar o programa é necessário os requisitos a seguir:

* Python 3.6 ou superior para executar o spider
* Framework scrapy (versão 2.1.0 usada no projeto)
* Biblioteca pandas (versão 1.0.3 usada no projeto)
* Módulo pyodbc (versão 4.0.30 usada no projeto)
* IDLE do Python ou alguma IDE para executar a linguagem
* Banco de Dados Microsoft SQL Server (versão SQL Server 2017 usada no projeto) (opcional)
* SQL Server Management Studio (versão 18.4 usada no projeto) (opcional) 

# Desenvolvimento
Para evoluir ou alterar o desenvolvimento, é necessário clonar o projeto do GitHub em algum diretório:

"git clone https://github.com/GVilarim/Web-Scraping-Telelista"

# Features
O projeto faz as raspagens das informações (nome, telefone, logradouro, bairro, cidade, telefone e coordenadas) no site da telelista de acordo com a atividade que você quiser (por padrão o link está direcionado para escolas particulares). Ressalto que, se tratando de um scraper, qualquer alteração realizada no site, pode acabar impactando no funcionamento do programa e que, este projeto é totalmente para praticar a atividade de raspagens de dados e que não é e nem deve ser usado para fins lucrativos de qualquer forma que seja.

# Configurações
Para escolher a atividade que deseja raspar na telelista, recomendamos que pesquise no próprio site exatamento como está o nome da atividade. No link das páginas o padrão da url é https://www.telelista/uf/cidade/atividade sendo que os espaços são substituidos por "+" tanto no nome das cidades quanto nas atividades, por exemplo, "/escolas+particulares". Ressalto que o banco de dados utilizado é o SQL Server com uma base de dados nomeada de "BancoSQLServer". Alternativamente comentado no código, está uma versão utilizando um arquivo cidades.xlsx com as informações das cidades.

# Links
* https://www.telelistas.net/
* https://docs.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15
* https://www.microsoft.com/pt-br/download/details.aspx?id=55994