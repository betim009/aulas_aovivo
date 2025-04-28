# Operadores de Comparação em Python

A seguir, uma tabela com os principais operadores de comparação em Python:

| Operador | Descrição                                                                       | Exemplo                          |
|----------|---------------------------------------------------------------------------------|----------------------------------|
| `==`     | Igualdade: verifica se dois valores são iguais.                                 | `5 == 5` resulta em `True`       |
| `!=`     | Desigualdade: verifica se dois valores são diferentes.                          | `5 != 3` resulta em `True`       |
| `>`      | Maior que: verifica se o valor da esquerda é maior que o da direita.            | `5 > 3` resulta em `True`        |
| `<`      | Menor que: verifica se o valor da esquerda é menor que o da direita.            | `3 < 5` resulta em `True`        |
| `>=`     | Maior ou igual que: verifica se o valor da esquerda é maior ou igual ao da direita. | `5 >= 5` resulta em `True` |
| `<=`     | Menor ou igual que: verifica se o valor da esquerda é menor ou igual ao da direita. | `3 <= 5` resulta em `True` |
| `is`     | Identidade: verifica se duas variáveis referenciam o mesmo objeto.             | `a is b`                         |
| `is not` | Negação de identidade: verifica se duas variáveis não referenciam o mesmo objeto. | `a is not b`                  |
| `in`     | Pertinência: verifica se um valor está contido em uma sequência.                | `3 in [1,2,3]` resulta em `True` |
| `not in` | Negação de pertinência: verifica se um valor não está contido em uma sequência.  | `4 not in [1,2,3]` resulta em `True` |

---

# Exercício 10.1 Modificado

Neste exercício, vamos trabalhar com uma lista de valores inteiros e realizar diversos cálculos:

- **Soma dos valores ímpares negativos**: identificar todos os números que são ímpares e negativos e somá-los.
- **Quantidade de valores não múltiplos de 7**: contar quantos números não são divisíveis por 7.
- **Porcentagem dos valores menores que 2**: calcular a proporção de números menores que 2 em relação ao total.
- **Média dos valores pares**: calcular a média aritmética de todos os números pares.

## Código em Python

```python
# Lista de números de exemplo
numeros = [1, 2, -3, 4, 5, 6, -7, 10]

# Variáveis de apoio para os cálculos
soma_impares = 0         # Soma dos valores ímpares negativos
nao_multiplos = 0        # Contador de valores não múltiplos de 7
menores_dois = 0         # Contador de valores menores que 2
valor_pares = 0          # Soma dos valores pares
quantidade_pares = 0     # Contador de valores pares

# Percorre cada elemento da lista
for item in numeros:
    # 1) Soma dos valores ímpares negativos
    #    Verifica se o número é negativo e se o resto da divisão por 2 é diferente de zero (ímpar)
    if item < 0 and item % 2 != 0:
        soma_impares += item

    # 2) Contagem dos valores não múltiplos de 7
    #    O operador % retorna o resto da divisão. Se não for zero, não é múltiplo.
    if item % 7 != 0:
        nao_multiplos += 1

    # 3) Contagem dos valores menores que 2
    #    Compara o valor com 2 usando o operador <
    if item < 2:
        menores_dois += 1

    # 4) Soma e contagem para cálculo da média dos valores pares
    #    Verifica se o resto da divisão por 2 é zero (par)
    if item % 2 == 0:
        quantidade_pares += 1
        valor_pares += item

# Exibição dos resultados
print("A soma dos valores ímpares negativos:", soma_impares)
print("A quantidade de valores não múltiplos de 7:", nao_multiplos)
print("Porcentagem dos números menores que 2: {:.2f}%".format((menores_dois * 100) / len(numeros)))
print("Média dos números pares:", valor_pares / quantidade_pares)
```

---

## Explicação Detalhada

1. **Lista de entrada**  
   Definimos uma lista chamada `numeros` com alguns inteiros de exemplo.  
   ```python
   numeros = [1, 2, -3, 4, 5, 6, -7, 10]
   ```  
   Cada elemento será analisado no loop.

2. **Variáveis auxiliares**  
   Criamos variáveis para armazenar resultados parciais:
   - `soma_impares` inicia em 0: guardará a soma de números que são ímpares *e* negativos.  
   - `nao_multiplos` inicia em 0: contará quantos números não são múltiplos de 7.  
   - `menores_dois` inicia em 0: contará quantos números são menores que 2.  
   - `valor_pares` e `quantidade_pares` iniciam em 0: ajudarão a calcular a média dos pares.  

3. **Loop `for item in numeros`**  
   Percorremos cada número da lista:
   - **Ímpares negativos**:  
     ```python
     if item < 0 and item % 2 != 0:
         soma_impares += item
     ```  
     - `item < 0`: garante valor negativo.  
     - `item % 2 != 0`: resto diferente de zero indica ímpar.  
   - **Não múltiplos de 7**:  
     ```python
     if item % 7 != 0:
         nao_multiplos += 1
     ```  
     - `item % 7`: divide e obtém o resto; se for não zero, não é múltiplo.  
   - **Menores que 2**:  
     ```python
     if item < 2:
         menores_dois += 1
     ```  
     - Simples comparação numérica.  
   - **Valores pares**:  
     ```python
     if item % 2 == 0:
         quantidade_pares += 1
         valor_pares += item
     ```  
     - `item % 2 == 0`: resto igual a zero indica par.  
     - Acumula soma e contador.

4. **Cálculos finais e saída**  
   - Soma dos ímpares negativos: já está em `soma_impares`.  
   - Quantidade de não múltiplos de 7: `nao_multiplos`.  
   - Porcentagem de menores que 2:  
     ```python
     (menores_dois * 100) / len(numeros)
     ```  
     - `len(numeros)`: total de elementos.  
   - Média dos pares:  
     ```python
     valor_pares / quantidade_pares
     ```  
     - Soma dividido pelo número de pares.

5. **Formatação de saída**  
   - Usamos `print` para mostrar cada resultado.  
   - Para porcentagem, `"{:.2f}%".format(valor)` formata com duas casas decimais.

---

