import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400) 
seno = np.sin(x)
cuadratica = x**2

fig, axs = plt.subplots(1, 2, figsize=(12, 5))  

# Subplot 1
axs[0].plot(x, seno, color='blue')
axs[0].set_title('Función Senoidal')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')
axs[0].grid(True)

# Subplot 2
axs[1].plot(x, cuadratica, color='red')
axs[1].set_title('Función Cuadrática')
axs[1].set_xlabel('x')
axs[1].set_ylabel('x²')
axs[1].grid(True)

plt.tight_layout()
plt.savefig('Grafico_subplots.png')
plt.show()
