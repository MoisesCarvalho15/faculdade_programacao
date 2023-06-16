numeros = [1, 2, 3, 4, 5]

nova_lista = map(lambda lista_numeros: lista_numeros * 3, numeros)
nova_lista = list(nova_lista)

print(f"Lista Original: {numeros}")
print(f"Lista do Resultado: {nova_lista}")
