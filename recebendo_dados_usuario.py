"""
Recebendo dados do usuário
    - Tudo via input() é String
"""

# Entrada de dados
nome = input('Qual o seu nome? ').title()  # Entrada no teclado

print(f'Seja bem vindo(a) {nome}')

idade = int(input('Qual a sua idade? '))

# Procesamento

# Saída
print(f'{nome} nasceu em {2022 - idade}')
