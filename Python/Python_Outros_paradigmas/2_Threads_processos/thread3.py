""" Sincronizando threads
Ordem de execução do programa:
    - Linha 27 -> Primeira Thread por Completa
    - Linha 31 -> Segunda Thread por completa
    - Linha 33 -> Imprime a lista com os valores Executados da Thread
"""
import threading
import time

# lista para os valores das threads
lista = []

def contador1(n):
    for i in range(1, n+1):
        print(f'Valor da PRIMEIRA Thread: {i}')
        lista.append(i)
        time.sleep(0.4)

def contador2(n):
    for i in range(6, n+1):
        print(f'Valor da SEGUNDA Thread: {i}')
        lista.append(i)
        time.sleep(0.5)

x = threading.Thread(target=contador1, args=(5,))
x.start()
x.join()

y = threading.Thread(target=contador2, args=(10,))
y.start()
y.join()

print(lista)