# Criar uma Função para Encontrar o menor elemento de uma lista de número

def menor_numero(lista):
    n_menor = lista[0]
    for n in lista:
        if n < n_menor:
            n_menor = n
    return n_menor

numeros = [2, 3, 4, 5, 10, 1, 22, 66]

menor = menor_numero(numeros)
print(menor)
