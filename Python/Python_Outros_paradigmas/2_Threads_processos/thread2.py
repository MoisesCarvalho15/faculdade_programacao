""" Thread com parâmetro
Ordem de execução do programa:
    - O programa irá executar a linha 16 primeiro
    - Depois irá executar a primeira vez a Thread
    - Depois irá executar a linha 18
    - Depois continuará executando o restante da Thread.
"""
import threading
import time

def funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)
        
print('Iniciando o programa')
x = threading.Thread(target=funcao, args=('Executando a Thread!',))
x.start()
print('Finalizando o programa')
