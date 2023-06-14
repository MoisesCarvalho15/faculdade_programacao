"""
Criar uma classe veículo com os atributos:
    - Nome do veículo
    - Velocidade Máxima
    - Quilômetros percorridos por litro
"""


class Veiculo:
    def __init__(self, nomeVeiculo, velocidadeMax, quilometroPorLitro):
        self.nomeVeiculo = nomeVeiculo
        self.velocidadeMax = velocidadeMax
        self.quilometroPorLitro = quilometroPorLitro
    
    def imprimirDados(self):
        print(f"Nome do veículo: {self.nomeVeiculo}")
        print(f"Velocidade Máxima: {self.velocidadeMax} km/h")
        print(f"Quilômetros por litro: {self.quilometroPorLitro}\n")
        

carro1 = Veiculo("Civic", 150, 8)
carro2 = Veiculo("Celta", 100, 14)

carro1.imprimirDados()
carro2.imprimirDados()
