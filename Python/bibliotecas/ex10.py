# Calcule as raízes de uma equação do segundo grau

import math

def entrada_dados():
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente'))
    return coeficiente

def calc_delta(a, b, c):
    delta = (b * b) - (4 * a * c)
    return delta

def calc_raiz(a, b, c, delta):
    if delta < 0:
        resultado = 'A equação não possui raízes nos números reais.'
    elif delta == 0:
        x = -b / (2 * a)
        resultado = f'A equação possui apenas a raiz: {x}'
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        resultado = f'A equação possui as raízes: {x1} e {x2}'    
    
    return resultado

a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a, b, c)

resultado = calc_raiz(a, b, c, delta)
print(resultado)
