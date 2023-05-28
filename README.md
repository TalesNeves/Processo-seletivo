# IntuitiveCare-ProcessoSeletivo

As aplicações e serviços desenvolvidos utilizando python possuem arquivo um arquivo de requiremento em suas respectivas pastas. <br />

# Teste 1 
```
pip install -r requirements.txt
source env/bin/activate
python3 Task1.py
```
Ao final do script os anexos que foram baixados usando web scraping são compactos em um arquivo com o nome "Anexos.zip" <br />

# Teste 2 
```
pip install -r requirements.txt
source env/bin/activate
python3 Task2.py
```
O script desse teste precisa que o arquivo de nome "Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf" esteja presente no diretório atual.<br />
Ao final da execução do script, um arquivo zip com o nome "Teste_(tales_oliveira_neves).zip" é gerado contendo a tabela extraída do arquivo pdf.<br />

# Teste 4

 A infraestrutura da aplicação do teste 4 foi montadada seguinte maneira: <br />
  Back-end: Servidor MySQL (Criado utilizando um servidor RDS da AWS) <br />
  API Server: Servidor Flask-SQLAlchemy (Sendo executado em uma instância EC2 da AWS) <br />
  Front-end: Aplicação em Vue.js (Também sendo executao em uma instância EC2 da AWS) <br />
 
 O banco de dados back-end é composto de apenas uma tabela que possui as 19 colunas do anexo de relatório. <br />
 A API possui duas rotas: <br />
   http://endpoint/all <br />
   http://endpoint/like/<lookforterm> <br />
  
  A rota /all é utilizada para realizar um query de todas as entradas do presentes no banco de dados.<br />
  A rota /like/<lookforterm> é uma query que busca todas as entradas que possuem a string de "lookforterm" no seu campo de razão social.
  
 O front-end é apenas um web site que cabeçalho para navegação e na uma seção "Operadoras" com uma tabela.
 
 # Detalhes e poréns
 A importação dos dados do anexo de relatório foi feita utilizando MySQL Worbench e exigiu que os acentos fossem removidos utilizando o script "fixencoding.py".<br />
 A automatização dos serviços juntamente com um sistema CI/CD ainda não foram implementados.
