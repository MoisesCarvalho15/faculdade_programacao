"""
- Visualizar dados de vendas de produtos em um gráfico de barras
- Utilizar os seguintes dados:
- Produtos x = ["A", "B", "C", "D"]
- Vendas y = [3, 8, 1, 10]
- Precisamos instalar o matplotlib
    - pip install matplotlib
"""

import matplotlib.pyplot as plt

x = ["Produto1", "Produto2", "Produto3", "Produto4"]
y = [3, 8, 1, 10]

# Criando o gráfico de barras
plt.bar(x, y)
plt.show()
