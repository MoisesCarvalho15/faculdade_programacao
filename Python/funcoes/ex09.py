# Criar uma função que determine se um número é PRIMO.
# PRIMO: Se for divisível por ele mesmo e por 1.

def primo(numero):
    div = 0
    resultado = ''
    # Fazendo a divisão até chegar no número escolhido
    for n in range(1, numero + 1):
        if numero % n == 0:
            # Acrescenta +1 toda vez que a condição for verdadeira
            div += 1 
    
    # Verificando se é primo ou não
    if div == 2:
        resultado = f'O número {numero} É PRIMO'
    else:
        resultado = f'O número {numero} NÃO É PRIMO'
        
    return resultado

num1 = primo(5)
num2 = primo(2)
num3 = primo(4)
num4 = primo(10)

print(num1)
print(num2)
print(num3)
print(num4)