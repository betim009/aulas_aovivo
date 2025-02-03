import pandas as pd

prontuario = [
    {
        "nome": "Alberto Fernandes Couto",
        "idade": 30,
        "covid": True
    },
    {
        "nome": "André Martins",
        "idade": 25,
        "covid": True
    }
]

pd.DataFrame(prontuario).to_csv('prontuario.csv')