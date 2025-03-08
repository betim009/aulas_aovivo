import pandas as pd 

planilha = pd.read_csv('pacientes.csv')

"""
Destruturar -> diminuir
    planilha -> 5 colunas -> destruturar para 2 coluna

for -> estrutura de repetição -> percorre a lista(planilha, csv)
    vai da primeira linha até a ultima.
    
    [
        {},
        {},
        {},
    ]
"""
nova_lista = []
for index, row in planilha.iterrows():
    nova_lista.append(
        {"Nome": row[1], "Cidade": row[3]}
    )
    
    
nova_planilha = pd.DataFrame(nova_lista)
nova_planilha.to_csv('pacientes_1.csv')