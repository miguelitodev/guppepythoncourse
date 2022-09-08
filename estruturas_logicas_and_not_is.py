"""
Estruturas lógicas: and, or, not e is

Operadores unários: not, is
    - Not -> O booleano é invertido not true = false // not false = true
    - Is -> O booleano é comparado com o mesmo is true = true // is false = false

Operadores binários: and, or
    - And -> ambos os valores precisam ser True
    - Or -> ambos os valores precisam ser False

"""

ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta, verifique seu e-mail')
else:
    print('Bem vindo usuário')

print('\n')

print(ativo and True)
print(ativo or True)
print(ativo is False)
print(not ativo)

print('\n')

nome = "Miguel"
print(nome.islower())
print(nome.isupper())
print(nome.istitle())
