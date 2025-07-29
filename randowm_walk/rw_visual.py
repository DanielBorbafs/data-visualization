import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Criando um passeio aleatório e plotando os pontos
rw = RandomWalk()
rw.fill_walk()

plt.figure(figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10)

#Enfatiza o primeiro e o último ponto
plt.scatter(0,0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# remove eixos
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()

   