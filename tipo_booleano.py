"""
Tipo booleano

Álgebra booleana -> criada por george boole

2 constantes -> true ou false

True -> verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

#errado -> true/false
#correto -> True/False

------------------------------------------

Operações básicas

not -> negação
: se o valor for verdadeiro, not fará ser falso, e vice-versa.

or -> ou
: É uma operação que depende de dois valores, um OU o outro deve ser verdadeiro.

and -> E
: Também depende de dois valores, porém os dois devem ser verdadeiros
"""

ativo = True
print(ativo)

print('\nNOT')
print(not ativo)

print('\nOR')
print(True or False)
print(False or False)
print(True or True)

print('\nAND')
print(True and True)
print(False and False)
print(False and True)
