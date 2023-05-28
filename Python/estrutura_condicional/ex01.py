# Receba dois números e identifique qual o maior entre eles

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é MAIOR que o número {num2}.')
elif num1 < num2:
    print(f'O número {num2} é MAIOR que o número {num1}.')
else:
    print('Ambos os números são IGUAIS.')
