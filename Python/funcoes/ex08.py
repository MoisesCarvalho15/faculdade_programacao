# Criar uma função para calcular o fatorial de um número

def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat = fat * i
    return fat

numero = fatorial(5)

print(numero)
