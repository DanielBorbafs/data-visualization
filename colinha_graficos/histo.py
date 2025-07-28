import matplotlib.pyplot as plt

idades = [22, 25, 30, 22, 23, 25, 30, 35, 36, 40, 41, 29, 31, 30, 25]

plt.hist(idades, bins=5, color='skyblue', edgecolor='black')
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
