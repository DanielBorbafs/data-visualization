import matplotlib.pyplot as plt 


categorias = ['Aluguel', 'Comida', 'Transporte', 'Lazer']
cores = ['#537D5D', '#73946B', '#9EBC8A', '#D2D0A0']
gastos = [1200, 600, 300, 200]

plt.pie( gastos,labels=categorias, colors=cores, autopct='%1.1f%%')
plt.show()