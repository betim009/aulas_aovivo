pessoas = [
    {
        "nome": "Ana Silva",
        "idade": 28,
        "email": "ana.silva@example.com",
        "cidade": "São Paulo"
    },
    {
        "nome": "Bruno Souza",
        "idade": 34,
        "email": "bruno.souza@example.com",
        "cidade": "Rio de Janeiro"
    },
    {
        "nome": "Carla Mendes",
        "idade": 22,
        "email": "carla.mendes@example.com",
        "cidade": "Rio de Janeiro"
    },
    {
        "nome": "Diego Oliveira",
        "idade": 40,
        "email": "diego.oliveira@example.com",
        "cidade": "Curitiba"
    }
]

for item in pessoas:
    if item["nome"] == "Diego Oliveira":
        print(item)
    

