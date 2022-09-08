"""
Tipo String

É string se for texto, se estiver entre qualquer tipo de aspas
"""

nome = 'Miguel'
print(nome)
print(type(nome))

nome = "Miguel's Bar"
print(nome)

nome = "Miguel\nRiquelme"
print(nome)
print(type(nome))

print('\n')

nome = 'Miguel Riquelme'
# Maiusculo
print(nome.upper())

# Minusculo
print(nome.lower())

# Lista
print(nome.split())
print(nome.split()[0])

# Slice de string
print(nome[0:6])

# [::-1] -> Comece do primeiro elemento, vá até o último e inverta
print(nome[::-1])
