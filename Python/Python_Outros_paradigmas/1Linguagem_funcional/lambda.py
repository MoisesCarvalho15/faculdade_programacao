# Função de ordem superior

def multiplicar_por(multiplicador):
    multi = lambda multiplicando: multiplicando * multiplicador
    return multi

multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(1))
print(multiplicar_por_10(2))

multiplicar_por_5 = multiplicar_por(5)
print(multiplicar_por_5(6))
print(multiplicar_por_5(7))

"""
Outra forma:
def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador
"""