"""
Exercício 02:
    - Inicie a execução de 2 threads
    - Coloque ambas Threads para esperar, respectivamente 3 e 2 segundos
    - Informe a ordem da execução das threads
    - Coloque a ordem de execução em uma função e depois a execute
"""
from threading import Thread
from time import sleep

def tarefa(tempo_espera, nome_tarefa ):
    print(f'\nIniciando... \n{nome_tarefa}')
    sleep(tempo_espera)
    print(f'\n{nome_tarefa} foi Executada com Sucesso!')
    
    
th1 = Thread(target=tarefa, args=(3, 'Tarefa da PRIMEIRA thread',))
th2 = Thread(target=tarefa, args=(2, 'Tarefa da SEGUNDA thread',))

def main():
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'A execução foi concluída!')
    
main()