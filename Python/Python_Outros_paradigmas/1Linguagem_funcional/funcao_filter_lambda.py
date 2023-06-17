# Objetivo: Retorna os elementos ímpares

numeros = [1, 2, 3, 4, 5, 6, 7]

resultado = filter(lambda numero: numero % 2 != 0, numeros)

print(f"Lista de números: {numeros}")
print(f"Números ímpares: {list(resultado)}")
