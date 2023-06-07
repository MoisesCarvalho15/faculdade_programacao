# Criando uma classe
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
    
    # Método com retorno
    def sacar(self, valor):
        if self.saldo < valor:
            return f'Saldo insuficiente na conta para realizar o saque.'
        else:
            self.saldo -= valor
            return f'Saque feito com Sucesso.'

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return f'Saldo insuficiente na conta!'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return f'Transferência realizada com sucesso!'

    def gerarExtrato(self):
        print(f'\nNome Titular: {self.nomeTitular} \ncpf: {self.cpf}\nsaldo: {self.saldo}')
