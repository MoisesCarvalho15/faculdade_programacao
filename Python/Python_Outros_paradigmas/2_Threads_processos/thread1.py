""" Thread Sem parâmetro
Ordem de execução do programa:
    - O programa irá executar a linha 16 primeiro
    - Depois irá executar a primeira vez a Thread
    - Depois irá executar a linha 18
    - Depois continuará executando o restante da Thread.
"""
import threading
import time

def funcao():
    for i in range(3):
        print(i, 'Executando a thread')
        time.sleep(1) # tempo de espera de 1s
    
print('Iniciando o programa')
threading.Thread(target=funcao).start() # iniciando a thread
print('Finalizando o programa')
