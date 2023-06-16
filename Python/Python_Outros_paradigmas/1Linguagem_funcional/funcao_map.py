numeros = [1, 2, 3, 4, 5]

def triplica(lista_numeros):
    return lista_numeros * 3

nova_lista = map(triplica, numeros)
nova_lista = list(nova_lista)

print(f"Lista Original: {numeros}")
print(f"Lista do Resultado: {nova_lista}")
