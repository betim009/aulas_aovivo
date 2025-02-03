import pandas as pd

file = pd.read_csv('./aula_6/usuarios.csv')
df = pd.DataFrame(file)

lista = []
for index, row in df.iterrows():
    lista.append({ "usuario": row['cliente'], "cidade": row["cidade"]})
    
print(lista)