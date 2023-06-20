"""
Exercício 03:
    - Inicie a execução de duas Threads
    - A primeira Thread deve calcular o cubo(x³) de um número
    - A segunda Thread deve calcular o quadrado de um número
    - Coloque a primeira e a segunda Threads para esperar 3 e 2 segundos
    - Informe a ordem de execução e as coloque em uma função
"""

from threading import Thread
from time import sleep

def calcular_cubo(tempo_espera,numero):
    print(f'\nCalculando o cubo do número {numero}...')
    print(f'Resultado = {numero ** 3}') 
    sleep(tempo_espera)
    print(f'Função calcular cubo terminou!')

def calcular_quadrado(tempo_espera, numero):
    print(f'\nCalculando o quadrado do número {numero}...')
    print(f'Resultado = {numero ** 2}')
    sleep(tempo_espera)
    print(f'Função calcular quadrado terminou!')

thread1 = Thread(target=calcular_cubo, args=(3, 5,))
thread2 = Thread(target=calcular_quadrado, args=(2, 5,))

def main():
    print(f'Exercício 03')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(f'\nFim do Exercício 03.')
    
main()