import pandas as pd

dados = [
    {
        "id": 520005005,
        "nome": "Abadia de Goiás",
        "municipio": {
            "id": 5200050,
            "nome": "Abadia de Goiás",
            "microrregiao": {
                "id": 52010,
                "nome": "Goiânia",
                "mesorregiao": {
                    "id": 5203,
                    "nome": "Centro Goiano",
                    "UF": {
                        "id": 52,
                        "sigla": "GO",
                        "nome": "Goiás",
                        "regiao": {"id": 5, "sigla": "CO", "nome": "Centro-Oeste"},
                    },
                },
            },
            "regiao-imediata": {
                "id": 520001,
                "nome": "Goiânia",
                "regiao-intermediaria": {
                    "id": 5201,
                    "nome": "Goiânia",
                    "UF": {
                        "id": 52,
                        "sigla": "GO",
                        "nome": "Goiás",
                        "regiao": {"id": 5, "sigla": "CO", "nome": "Centro-Oeste"},
                    },
                },
            },
        },
    },
    {
        "id": 310010405,
        "nome": "Abadia dos Dourados",
        "municipio": {
            "id": 3100104,
            "nome": "Abadia dos Dourados",
            "microrregiao": {
                "id": 31019,
                "nome": "Patrocínio",
                "mesorregiao": {
                    "id": 3105,
                    "nome": "Triângulo Mineiro/Alto Paranaíba",
                    "UF": {
                        "id": 31,
                        "sigla": "MG",
                        "nome": "Minas Gerais",
                        "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"},
                    },
                },
            },
            "regiao-imediata": {
                "id": 310061,
                "nome": "Monte Carmelo",
                "regiao-intermediaria": {
                    "id": 3111,
                    "nome": "Uberlândia",
                    "UF": {
                        "id": 31,
                        "sigla": "MG",
                        "nome": "Minas Gerais",
                        "regiao": {"id": 3, "sigla": "SE", "nome": "Sudeste"},
                    },
                },
            },
        },
    }
]

nova_lista = []
for index, cidade in enumerate(dados):
    nova_lista.append({
        "cidade": cidade['nome'],
        "estado": cidade['municipio']['microrregiao']['nome']
    })


pd.DataFrame(nova_lista).to_csv('cidades.csv')  
print(nova_lista)