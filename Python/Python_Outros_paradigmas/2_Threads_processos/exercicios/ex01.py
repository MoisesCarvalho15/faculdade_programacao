"""
Exercício 01:
    - Inicie a execução de uma Thread
    - Coloque a thread para esperar 2 segundos utilizando como argumento
    - Mostre uma mensagem, como segundo argumento
    - Informe o início e o final da execução da Thread
"""
from threading import Thread
from time import sleep

def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando o Exercício 01. \n{mensagem}')
    sleep(tempo_espera)
    print('Fim do Exercício 01.')

thread = Thread(target=tarefa, args=(2, 'Thread em Execução!',))
thread.start() 
thread.join()

print('A execução foi concluída!')
