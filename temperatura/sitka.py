import csv
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates  # <-- Adição importante

filename = './data/sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs,lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plotando os gráficos
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs,lows, facecolor='blue', alpha=0.1)

# Formatação do eixo X para mostrar apenas o nome do mês
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # marca uma vez por mês
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # mostra 'July', 'August', etc.

# Formata o Gráfico
plt.title('Temperaturas Máximas e Mínimas de 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # gira as datas para melhor visualização
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
