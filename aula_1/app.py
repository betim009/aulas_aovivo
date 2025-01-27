"""
- Ultima aula:
Tipos de dados
Estrutura de repetições


-> LISTAS


-> Estrutura de repetição possui 2 parametros
o Elemento / o Index

o elemento é o tipo de dado dentro da lista
o index é a posição desse dado na lista
"""

lista_usuarios = [
    { "nome": "Alberto", "email": "alberto@gmail.com", "assinante": False },
    { "nome": "Gustavo", "email": "gustavo@gmail.com", "assinante": True },
    { "nome": "Mario", "email": "mario@gmail.com", "assinante": True }
]

lista_str = ["Alberto", "Gustavo", "Mario"]
lista_num = [100, 999, 1000]
lista_bool = [True, False, False]


objeto_usuario = { "nome": "Mario", "email": "mario@gmail.com", "assinante": True }

"""
Como acessar um dicionario? -> pelo nome da propriedade
Como acessar uma lista? -> é pela ordem -> posição -> index
"""

print(
    lista_usuarios[1]["email"]
)