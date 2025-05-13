#  Gráfico de línea simple
import matplotlib.pyplot as plt
import numpy as np

valores = [3, 7, 1, 5, 12]
x = np.arange(len(valores))

plt.plot(x, valores, marker='o', linestyle='-', color='blue')

plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.savefig('Grafico_linea_simple.png')
plt.show()