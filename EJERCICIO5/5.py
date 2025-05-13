import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400) 

# Calcular y = x^2 - 3x + 2
y = x**2 - 3*x + 2

plt.plot(x, y, color='purple', linewidth=2)

plt.title('Gráfico de y = x² - 3x + 2')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)

plt.savefig('Grafico_funcion_cuadratica.png') 
plt.show()
