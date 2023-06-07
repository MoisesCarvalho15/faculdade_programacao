# Importando uma classe de um arquivo externo
from ex18 import Conta

# Objetos sendo instanciados
conta1 = Conta(1, 123, 'Marcos', 0)
conta2 = Conta(2, 456, 'Anna', 0)

# Adicionando saldo na conta e mostrando os dados
conta1.depositar(1000)
conta1.gerarExtrato()

# Transferindo dinheiro de uma conta para outra
print(f'{conta1.transfereValor(conta2, 200)}')

# Imprimindo os dados atualizado das contas
conta2.gerarExtrato()
conta1.gerarExtrato()

# tentando sacar um valor maior que o disponível na conta
print(conta2.sacar(250))
