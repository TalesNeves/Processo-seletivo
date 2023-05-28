import pdfplumber
import pandas as pd


file_name = "Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf"
pdf = pdfplumber.open(file_name)
pages  = pdf.pages

columns = []
firstTable = True
for page in pages:
    
    table = page.extract_table()
    if table == None:
        continue
    if firstTable == True:
        firstTable = False
        columns = table[0]
        df = pd.DataFrame(table[1:],columns=columns)
        continue
        
    df_buffer = pd.DataFrame(table[1:],columns=columns)
    df = pd.concat([df,df_buffer])

df['OD'].replace('OD','Seg. Odontológica',inplace=True)
df['AMB'].replace('AMB','Seg. Ambulatorial',inplace=True)

new_file_name = "Teste_(tales_oliveira_neves)"
compression_options = dict(method='zip',archive_name=f'{new_file_name}.csv')
df.to_csv(f'{new_file_name}.zip',compression=compression_options,index=False)
