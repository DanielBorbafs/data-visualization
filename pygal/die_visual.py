from die import Die
import pygal

# Cria um D6
die1= Die()
die2= Die()

# Faz alguns lançamentos e armazena os resultados em uma lista 
results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualizando os dados 
hist = pygal.Bar()
hist.title = "Resultados de dois dados de 6 lados lançado mil vezes"
hist.x_labels = ['2','3', '4', '5', '6', '7', '8', '9', '10','11', '12'] 
hist.x_title = 'Resultado'
hist.y_tytle = 'Frequencia'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')