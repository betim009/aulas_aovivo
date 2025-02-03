"""
a media final é a soma de notas de 2 provas / 2.
"""

# Crio a função
def calc_media(prova1, prova2):
    return (prova1 + prova2) / 2


def calcular_media(provas):
    soma_provas = 0
    qtd_provas = 0
    
    for i in provas:
        soma_provas += i
        qtd_provas += 1
        
    return soma_provas / qtd_provas

# Executar a função
print(calcular_media([5, 7, 8, 10]))