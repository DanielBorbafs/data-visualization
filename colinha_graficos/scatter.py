import matplotlib.pyplot as plt

horas_estudo = [1, 2, 3, 4, 5, 6, 7]
notas = [50, 55, 60, 65, 70, 80, 90]

plt.scatter(horas_estudo, notas, color='blue')
plt.title('Relação entre Horas de Estudo e Nota da Prova')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota')
plt.grid(True)
plt.show()
