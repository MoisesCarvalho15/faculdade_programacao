# Função Pura parte 1
valor = 20

def multiplica(fator):
    global valor
    valor *= fator
    print(f"Resultado: {valor}")
    
def main():
    numero = int(input("Digite um número: "))
    multiplica(numero)
    multiplica(numero)
    
main()
