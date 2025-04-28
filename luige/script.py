# Exercício

# 10.1 modificado
# Dados n valores inteiros, elaborar um programa em Python para calcular e exibir:

# A soma dos valores ímpares negativos;

# A quantidade de valores não múltiplos de 7;

# A porcentagem dos valores menores que 2;

# A média dos valores pares.

numeros = [1, 2, -3, 4, 5, 6, -7, 10] # AUTOMATICAMENTE -> FOR
# 1, 3, 5, 7 = 16 <- 
soma_impares = 0
nao_multiplos = 0
menores_dois = 0
valor_pares = 0
quantidade_pares = 0

for item in numeros: # ITEM é cada numero
    # a quantidade de numeros negativos impares
    if item < 0 and item % 2 != 0:
        soma_impares += item
        
    if item % 7 != 0:
        nao_multiplos += 1  

    if item < 2:
        menores_dois += 1
    
    if item % 2 == 0:
        quantidade_pares += 1
        valor_pares += item


print("A soma dos valores ímpares negativos", soma_impares)
print("A quantidade de valores não múltiplos de 7", nao_multiplos)
print("% dos numeros menor que dois", (menores_dois * 100) / len(numeros)) # len pega a quatnidade de numeros dentro da lista
print("media dos numeros pares", valor_pares / quantidade_pares)