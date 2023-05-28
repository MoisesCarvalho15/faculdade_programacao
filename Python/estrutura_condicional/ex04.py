"""
- Calcular o valor de uma compra, preço UNITÁRIO é R$10,00
- Se for feita uma compra de até 10 unidades, não há descontos.
- Para compras entre 11 e 20 unidades, é dado um desconto de 10%.
- Acima de 20 unidades, é dado um desconto de 20%.
"""

quantidade = 30
preco_unidade = 10
desconto10 = 0.1
desconto20 = 0.2

if quantidade <= 10:
    valor_total = quantidade * preco_unidade
elif quantidade <= 20:
    valor_total = (quantidade * preco_unidade) * (1 - desconto10)
else:
    valor_total = (quantidade * preco_unidade) * (1 - desconto20)

print(f'O valor total é de: {valor_total}')
