"""
PEP8 - Propostas de melhoria

Zen of python
> import this

- Regras para codificar

    1 - Camel case

        class Calculadora:
            pass

        class CalculadoraCientifica:
            pass

    2 - Nomes em minúsculo separado por underline para:
        - Funções
        - Variáveis

        def soma():
            pass

        def soma_dois():
            pass

        numero = 4

        numero_impar = 5

    3 - Utilize 4 espaços para identação

        if 'a' in 'banana':
            print('tem')

    4 - Linhas em branco
        - Funções e definições separados por 2 linhas
        - Métodos dentro de classes separados por 1 linha

    5 - Imports
        - Devem ser feito em linhas separadas

            # Errado
                import sys, os

            # Certo
                import sys
                import os

            # Sem problemas
                from types import StringType, ListType

            # Muitos imports
                from types import (
                    StringType,
                    ListType,
                    SetType,
                    ...
                )

        - Devem estar no inicio do arquivo, antes de tudo

    6 - Espaços em expressões e instruções

        # Não faça
            funcao( algo[ 1 ] , { outro: 2 } )
            funcao (1)
            dict ['chave'] = lista [indice]
            x  = 1

        # Faça
            funcao(algo[1], {outro: 2})
            funcao(1)
            dict['chave'] = lista[indice]
            x = 1

    7 - Termine sempre uma instrução com uma nova linha
"""

import this
