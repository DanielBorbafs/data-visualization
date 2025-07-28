import matplotlib.pyplot as plt


produtos = ['Produto A', 'Produto B', 'Produto C']
vendas = [150, 200, 130]

plt.barh(produtos, vendas, label='Vendas em unidades')

plt.title('Quantidades de produtos vendidos')
plt.legend()
plt.show()