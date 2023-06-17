"""
Considere a lista abaixo:
    lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    - Imprimir apenas os números pares utilizando Programação Funcional
"""

lista = [0, 1, 2, 3, 5, 8, 13, 21, 34]

acha_pares = lambda x: x % 2 == 0

lista_pares = list(filter(acha_pares, lista))

print(lista_pares)
