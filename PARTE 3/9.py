import pandas as pd
import matplotlib.pyplot as plt

# PUNTO 9
# CARGAR ARCHIVO
df = pd.read_csv('datos_ventas.csv')

# Mostrar las primeras 5 filas
print(df.head())

# PUNTO 10
# ESTADISTICAS BASICAS

# Total de ventas
total_ventas = df['Ventas'].sum()

# Promedio de precio
promedio_precio = df['Precio'].mean()

# Producto más vendido (por suma de ventas)
producto_mas_vendido = df.groupby('Producto')['Ventas'].sum().idxmax()

print("Total de ventas:", total_ventas)
print("Promedio de precio:", promedio_precio)
print("Producto más vendido:", producto_mas_vendido)

# PUNTO 11
# FILTRAR DATOS

# Convertir columna Fecha a tipo datetime si es necesario
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Filtrar ventas de enero de 2025
enero = df[df['Fecha'].dt.strftime('%Y-%m') == '2025-01']

print(enero)

# PUNTO 12
# GRAFICAS DE BARRAS

# Agrupar por producto y sumar ventas
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()

# Crear gráfico de barras
ventas_por_producto.plot(kind='bar', color='coral', edgecolor='black')

# Título y etiquetas
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Total Vendido')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.tight_layout()
plt.savefig('Grafico_ventas_por_producto.png')
plt.show()
