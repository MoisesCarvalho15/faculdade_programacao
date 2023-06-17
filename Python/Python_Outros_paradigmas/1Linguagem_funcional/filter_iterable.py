# Objetivo: Retorna os elementos ímpares

numeros = [1, 2, 3, 4, 5, 6, 7]

def impares(lista_numeros):
    resultado = []
    
    for numero in lista_numeros:
        if numero % 2 != 0:
            resultado.append(numero)
            
    return resultado

print(f"Lista de números: {numeros}")
print(f"Números ímpares: {impares(numeros)}")
