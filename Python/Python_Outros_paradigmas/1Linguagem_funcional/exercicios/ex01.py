"""
Considere a lista abaixo:
    veiculos = ['avião', 'carro', 'navio', 'ônibus']
    - Transformar todos os nomes em maiúsculos através da Programação Funcional
"""

veiculos = ['avião', 'carro', 'navio', 'ônibus']

transforma_maiusculos = lambda item: str.upper(item)

nomes_maiusculos = list(map(transforma_maiusculos, veiculos))

print(f"Nomes maiúsculos: {nomes_maiusculos}")
