# Criar uma função que some todos os números pares de uma lista

def soma_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma
            
numeros = [0, 2, 5 , 7, 10, 13, 44, 59]
resultado = soma_pares(numeros)

print(resultado)
