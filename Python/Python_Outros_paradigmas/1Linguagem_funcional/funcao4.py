valores = input("Digite uma sequência de números separados por espaços: ")

valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] += 10
    
    return lista

def main():
    print(f"Nova lista: {altera_lista(valores)}")
    print(f"Nova lista: {altera_lista(valores)}")
    
main()