import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)  

# Calcular sin(x) y cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='orange')

plt.title('Comparación entre sin(x) y cos(x)')
plt.xlabel('x (radianes)')
plt.ylabel('Valor')

plt.grid(True)
plt.legend()

plt.savefig('Grafico_sin_cos.png')
plt.show()
