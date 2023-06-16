valores = input("Digite uma sequência de números separados por espaços: ")

# Separando os valores pelo espaço em branco
# e transformando em uma lista
valores  = [int(i) for i in valores.split()]

def altera_lista(lista):
    lista[2] += 10 # valor do terceiro elemento da lista somado a 10
    return lista

def main():
    print(f"Nova lista: {altera_lista(valores)}")
    print(f"Nova lista: {altera_lista(valores)}")

main()
