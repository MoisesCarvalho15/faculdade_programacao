# Tratamento de exceção de divisão por zero

loop = True
while loop:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(f'A divisão de {num1} / {num2} é = {num1 / num2}')

        continuar = input('Deseja continuar? ').lower()
        if continuar != 'sim':
            print('Até a próxima!')
            loop = False
        else:
            continue

    except ZeroDivisionError:
        print('Não é possível fazer divisão por zero')
        continue
    
    except ValueError:
        print('Verifique os dados e tente novamente')
        continue
        