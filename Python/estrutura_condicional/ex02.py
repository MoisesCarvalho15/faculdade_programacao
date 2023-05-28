# Identificar se um número é par

num1 = input("Digite um número: ")

if num1.isnumeric():
    num1 = float(num1)
    if num1 % 2 == 0:
        print(f'O número {num1} é PAR.')
    else:
        print('NÃO é PAR.')
else:
    print('Verifique o dado digitado e tente novamente.')
