"""
Escopo variáveis

{
    Escopo, tudo que ta dentro das { }
}

1 - Variáveis globais
    - Pega o programa inteiro

2 - Variáveis locais
    - Pega somente o bloco onde foi declarada

Exemplo:

global = "Nome 1"

{
    local = "Nome 2"
}

-------------------------

Tipagem dinamica
: Se não especificar o tipo da variável vai ser qualque tipo

"""

numero = 15  # Escopo global

if numero > 10:
    novo = numero + 10  # Escopo local
    print(novo)
else:
    print(numero)
