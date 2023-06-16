valor = 20

# Função Pura
def multiplica(valor, fator):
    valor *= fator
    return valor

def main():
    numero = int(input("Digite um número: "))
    print(f"Resultado: {multiplica(valor, numero)}")
    print(f"Resultado: {multiplica(valor, numero)}")
    
main()

"""
Neste caso a função multiplica é pura
    - Depende apenas dos parâmetros passados para gerar resultados
    - Não acessa e não modifica nenhuma variável externa à função
    - Retorna um valor
"""