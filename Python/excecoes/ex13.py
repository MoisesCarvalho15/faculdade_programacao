# Tratamento de exceção para verificar se a entrada é de um número

loop = True
while loop:
    try:
        x = int(input('Digite um número: '))
        print('O dado de entrada é um número.')
        
        continuar = input('Deseja continuar? ').lower() 
        if continuar == 'sim':
            continue
        else:
            print('Até a próxima!')
            loop = False
    except ValueError:
        print('Entre com um número válido')
        continue
            