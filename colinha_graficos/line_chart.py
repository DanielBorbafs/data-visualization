import matplotlib.pyplot as plt 
import random 

dias = ['seg', 'ter', 'quar', 'quin', 'sex', 'sáb', 'dom']

temperatura = [random.randint(15, 33) for _ in range(len(dias))]
temperatura_min = [15, 16, 15, 17, 16, 15, 18]

plt.plot(dias, temperatura, marker='o', label='Temperatura Máxima')
plt.plot(dias, temperatura_min, marker='o', label='Temperatura Miníma')

plt.title("Temperatura durante a semana")
plt.xlabel('Dias')
plt.ylabel('Temperatura em Graus')

plt.legend()

plt.show()