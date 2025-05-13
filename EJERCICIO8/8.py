import matplotlib.pyplot as plt
import numpy as np

datos = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(datos, bins=30, color='teal', edgecolor='black', alpha=0.7)

plt.title('Histograma de distribución normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')


plt.grid(True)
plt.savefig('Grafico_histograma.png')
plt.show()
