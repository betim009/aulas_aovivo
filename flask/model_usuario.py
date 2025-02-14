import pandas as pd


def read_csv():
    data = []
    file_data = pd.read_csv("data.csv")
    for index, element in file_data.iterrows():
        data.append({
            "id": element['id'],
            "nome": element["nome"],
            "idade": element["idade"]
            })
    return data
