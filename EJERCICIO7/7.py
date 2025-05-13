import numpy as np

a = np.random.randint(0, 101, 100)
b = np.random.randint(0, 101, 100)

suma_total = np.sum(a + b)
valor_maximo = np.max(a + b)
desviacion = np.std(a + b)

print("Suma total:", suma_total)
print("Valor máximo:", valor_maximo)
print("Desviación estándar:", desviacion)
