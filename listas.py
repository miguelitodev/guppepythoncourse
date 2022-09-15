"""
Arrays

- Dinamico: não tem tamanho fixo
- Qualquer tipo de dado
- São representadas por []
"""

lista1 = [11, 72, 3, 41, 5, 3]
lista2 = ['M', 'i', 'g', 'u', 'e', 'l']
lista3 = []
lista4 = list(range(11))
lista5 = list('Miguel')

# verificar um valor dentro da lista
if 3 in lista1:
    print('Existe')
else:
    print('Não existe')

print()

# ordenar a lista
lista1.sort()
print(lista1)

print()

# quantas vezes um valor aparece na lista
print(lista1.count(3))

print()

# adicionar elementos
lista1.append(60)
print(lista1)

print()

lista1.append([15, 84, 96])  # <- adiciona o array inteiro no array
print(lista1)

print()

lista1.extend([15, 84, 96])  # <- adiciona cada valor do array no array
print(lista1)

print()

lista1.insert(1, 'Valor')  # <- adiciona o valor no indice especeficado
print(lista1)

print()

# inverter a lista
lista1.reverse()
print(lista1)
print(lista1[::-1])  # <- outra forma

print()

# copiar uma lista
lista6 = lista2.copy()
print(lista6)

print()

# pegar o tamanho da lista
print(len(lista1))

print()

# remover o ultimo elemento
print(lista1)
lista1.pop()
print(lista1)

print()

# remover pelo indice
print(lista1)
lista1.pop(0)
print(lista1)

print()

# limpar a lista inteira
lista1.clear()
print(lista1)

print()

# multiplicar os elementos da lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

print()

# converter string pra lista
curso = "programacao python"
curso = curso.split()  # <- separa por espaço por padrao
print(curso)

curso2 = 'programacao,python'
curso = curso2.split(',')
print(curso)

print()

# converter lista em string
listaCurso = ['programacao', 'python']
print(listaCurso)

listaCurso = ' '.join(listaCurso)  # <- adiciona espaço entre cada elemento
print(listaCurso)

listaCurso2 = ['programacao', 'python']
listaCurso2 = '_'.join(listaCurso2)  # <- adiciona espaço entre cada elemento
print(listaCurso2)

print()

# Iterando na lista
for elemento in lista5:
    print(elemento + ' ', end='')

print()

# pegar elementos pelo indice

print(lista5[1])
print(lista5[-1])

print()

# saber o indice de um valor
print([1, 2, 3].index(2))
print([3, 2, 1, 1, 2, 3].index(1, 3))  # <- a partir do indice 1

print()

# revisar o slice
listaSlice = [1, 2, 3, 4]
print(listaSlice[1:])
print(listaSlice[:10])
print(listaSlice[1::2])

print()

# Soma, valor máximo, valor mínimo (só int/float) | tamanho
listaOperacoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(listaOperacoes))  # <- soma dos items da lista
print(max(listaOperacoes))  # <- maior valor da lista
print(min(listaOperacoes))  # <- menor valor da lista
print(len(listaOperacoes))  # <- tamanho da lista

print()

# transformar em tupla
listaTupla = [1, 2, 3, 4]
print(listaTupla, type(listaTupla))

tupla = tuple(listaTupla)
print(tupla, type(tupla))

print()

# desempacotamento de lista
listaDesempacotada = [1, 2, 3]
num1, num2, num3 = listaDesempacotada  # <- n° variaveis = n° de items no array
print(num1)
print(num2)
print(num3)

print()

# Shallow copy != Deep copy

# Deep copy
listaDeepCopy = [1, 2, 3]

novaListaDeepCopy = listaDeepCopy.copy()
novaListaDeepCopy.append(4)

print(listaDeepCopy)
print(novaListaDeepCopy)

# Shallow copy
listaShallowCopy = [1, 2, 3]

novaListaShallowCopy = listaShallowCopy
novaListaShallowCopy.append(4)

print(listaShallowCopy)
print(novaListaShallowCopy)
