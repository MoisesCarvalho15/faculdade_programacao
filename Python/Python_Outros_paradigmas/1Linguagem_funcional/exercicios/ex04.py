"""
Considere a lista:
    numeros: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    - Somar todos os números da lista utilizando Programação Funcional
"""
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

somando = lambda x,y : x + y

resultado = reduce(somando, numeros)

print(resultado)