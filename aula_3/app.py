"""
    1. Você vai criar uma lista de dicionários.
        qualquer tema - sorveteria, pessoas, usuarios ... 
    
    2. Manipular essa lista de dicionários.
        tentar acessar diferentes posições dessa lista.
        tentar adicionar um novo dicionário nessa lista.
        tentar alterar uma informação de um dicionario.
        tentar acrescentar uma chave*coisa dentro de um dicionario. 
"""



lista_pagamentos = [
    {"pagamento": 280, "pessoa": "joão"},
    {"pagamento": 250, "pessoa": "marcela"},
    {"pagamento": 150, "pessoa": "maria"}
]

lista_pagamentos[1]["pagamento"] = 280
lista_pagamentos[1]["data"] = '09/04'

lista_pagamentos.append(
    {"pagamento": 150, "pessoa": "alberto"}
)

print(lista_pagamentos)




pagamento = {
    "pagamento": 280, 
    "pessoa": "joão"
}

