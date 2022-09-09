"""
Loop for

Loop - estrutura de repetição.
For - uma dessas estruturas.

ex:
for item in interavel:
    // execução

Utilizamos loops para interar sobre sequencias ou sobre valores interaveis

Interaveis:
    - String
    - Array
    - Range
"""

nome = "Miguel Riquelme"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # vai até o 9, o 10 não

for letra in nome:
    print(letra)

print()

for numero in lista:
    print(numero)

print()

for numero in range(1, 10):
    print(numero)

print()

for indice, _ in enumerate(nome):
    print(nome[indice])

print()

for valor in enumerate(nome):
    print(valor)

print()

qtd = int(input('Quantas vezes esse loop tem que rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Digitel o valor {n}/{qtd} para soma: '))
    soma += num

print(f'Soma é: {soma}')


print()

for letra in nome:
    print(letra, end='')

print()

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F600' * num)
