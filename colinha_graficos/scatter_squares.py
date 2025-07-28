import matplotlib.pyplot as plt


x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, s=40, edgecolors='none')

plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)


plt.axis([0, 1100, 0, 1100000])

plt.savefig('./colinha_graficos/imgs/squraaes_plot.png', bbox_inches='tight')

