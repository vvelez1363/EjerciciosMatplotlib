import matplotlib.pyplot as plt
import random

x = [random.randint(0, 100) for _ in range(50)]
y = [random.randint(0, 100) for _ in range(50)]

plt.scatter(x, y, color='green', alpha=0.6, edgecolors='black')

plt.title('Gráfico de Dispersión con Números Aleatorios')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.savefig('Grafico_dispersión.png')
plt.show()
