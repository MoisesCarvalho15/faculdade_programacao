# Some todos os números pares de uma lista.

numeros = [10, 2, 5, 7, 6, 3]
soma = 0

for n in numeros:
    if n % 2 == 0:
        soma += n

print(soma)