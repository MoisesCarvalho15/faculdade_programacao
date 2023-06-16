valor = 20

# Função não Pura
def multiplica(fator):
    # referenciando a variável global
    global valor
    valor *= fator # Multiplicando o valor da variável global pelo valor do fator
    print(f"Resultado: {valor}")
    
def main():
    numero = int(input("Digite um número: "))
    multiplica(numero) # valor da variável global * número digitado
    multiplica(numero) # resultado anterior * valor digitado
    
main()

"""
Neste caso
    - O valor da variável global inicia 20
    - Após solicitar um número para o usuário: Exemplo, o número 3
    - e chamar a função main:
        - No primeiro multiplicar:
            - O valor da variável global será 20 * 3 = 60
        - Na segunda vez:
            - O valor da variável global será 60 * 3 = 180
Ou seja, este exemplo é de uma função não pura.
Porque: 
    - ela não depende apenas dos parâmetros para gerar resultados
    - essa função não retorna valor algum.
    - ela modifica o valor de uma variável externa da função.
"""
