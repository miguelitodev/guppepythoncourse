"""
Ranges

- Precisamos conhecer o loop for para usar o ranges
- Precisamos conhecer o ranges para usar melhor loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

rage(valor_de_parada)

- se não falar onde começa, sempre vai começar em 0
- o final do valor é sempre o valor de parada -1

se quiser ver o range tem que transformar em lista
> list(range(10))

"""

for num in range(11):
    print(num)

print()

for num in range(1, 11):
    print(num)

print()

for num in range(1, 10, 2):
    print(num)

print()

for num in range(10, 0, -1):
    print(num)
