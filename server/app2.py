import pandas as pd

column_names= ["Registro ANS","CNPJ","Razao Social","Nome Fantasia","Modalidade","Logradouro","Numero","Complemento","Bairro","Cidade","UF","CEP","DDD","Telefone","Fax","Endereco eletronico","Representante","Cargo Representante","Data Registro ANS"]

df = pd.read_csv('Backup (copy).csv',header=None, delimiter=";", names=column_names)
df.to_csv('Output.csv',index=False, encoding="utf-8-sig")
print(df) 