"""
Breaks

> Serve para sairmos de loops
"""

for n in range(1, 11):
    if n == 6:
        break
    else:
        print(n)

print('Sai do loop')

while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break
