"""
Variaveis armazenam temporariamente 

qualquer_nome = tipo de dado


[] => Lista


Tamanho é diferente de posição

a lista vai de 0 a 3
mas o tamanho é 4
"""
#            0          1         2          3
pacientes = ["João", "Marcos", "Gabriela", "Fabio"] 
idades = [22, 33, 16, 54]

paciente = {
    "nome": "Alberto Fernandes Couto",
    "idade": 30,
    "covid": True
}

prontuario = [
    {
        "nome": "Alberto Fernandes Couto",
        "idade": 30,
        "covid": False
    },
    {
        "nome": "André Martins",
        "idade": 20,
        "covid": True
    }
]

# ESTRUTURA DE REPETIÇÃO -> Ir do inicio ao final de uma lista
for paciente in prontuario:
    if paciente["idade"] >= 25:
        print(paciente)
