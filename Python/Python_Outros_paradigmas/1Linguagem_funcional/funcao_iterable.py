numeros = [1, 2, 3, 4, 5]

def triplica_numeros(lista_numeros):
    nova_lista = []
    
    for numero in lista_numeros:
        nova_lista.append(numero * 3)
    
    return nova_lista

print(f"Lista original: {numeros}")
print(f"Lista do resultado: {triplica_numeros(numeros)}")