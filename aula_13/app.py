"""
Simples:
string
numbers -> int, float
booleans
Complexos:
Dict/Objeto -> { "id": 1, "usuario": "Alberto", "assinante": True }
Lista/Array -> []
"""

pessoas = [
    {"id": 1, "usuario": "Alberto", "assinante": True},
    {"id": 2, "usuario": "Jana", "assinante": True},
]

numeros = [42, 12, 11, 32, 1]
nomes = ["Alberto", "Jana"]
bols = [True, False, False, True]

sistema = {
    "nome_sistema": "Aplicação Python",
    "usuarios": [
        {"id": 1, "usuario": "Alberto", "assinante": True},
        {"id": 2, "usuario": "Jana", "assinante": True},
    ],
    "planos": [
        {"id": 1, "plano": "Simples", "preco": 15.99},
        {"id": 2, "plano": "Moderado", "preco": 39.99},
    ],
    "total_vendas": 1547
}
