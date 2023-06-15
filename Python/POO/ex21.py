"""
Criar uma classe veículo com os atributos:
    - Nome do veículo
    - Velocidade Máxima
    - Quilômetros percorridos por litro
Crie uma classe filha "ônibus" que:
    - Herdará todas as variáveis e métodos da classe veículo.
    - Forneça a quantidade de assentos com o valor padrão de 70
"""


class Veiculo:
    def __init__(self, nomeVeiculo, velocidadeMax, quilometroPorLitro):
        self.nomeVeiculo = nomeVeiculo
        self.velocidadeMax = velocidadeMax
        self.quilometroPorLitro = quilometroPorLitro
    
    def capacidadeAssentos(self, capacidade):
        print(f"A capacidade máxima de assentos do veídulo {self.nomeVeiculo} é = {capacidade}.")
    
    def imprimirDados(self):
        print(f"Nome do veículo: {self.nomeVeiculo}")
        print(f"Velocidade Máxima: {self.velocidadeMax} km/h")
        print(f"Quilômetros por litro: {self.quilometroPorLitro}\n")


# Criando uma classe filha de veículo
class Onibus(Veiculo):
    def capacidadeAssentos(self, capacidade = 70):
        return super().capacidadeAssentos(capacidade=70)

# Criando os objetos das classes
carro1 = Veiculo("Civic", 150, 8)
carro2 = Veiculo("Celta", 100, 14)
onibus1 = Onibus("Scania", 120, 8)

# Imprimindo os dados na tela
carro1.imprimirDados()
carro2.imprimirDados()
onibus1.imprimirDados()
onibus1.capacidadeAssentos()