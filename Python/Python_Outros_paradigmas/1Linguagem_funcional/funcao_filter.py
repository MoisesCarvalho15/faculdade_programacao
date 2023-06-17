# Objetivo: Retorna os elementos ímpares

numeros = [1, 2, 3, 4, 5, 6, 7]

def impar(numero):
    return numero % 2 != 0

resultado = filter(impar, numeros)
resultado = list(resultado)

print(f"Lista de números: {numeros}")
print(f"Números ímpares: {resultado}")
