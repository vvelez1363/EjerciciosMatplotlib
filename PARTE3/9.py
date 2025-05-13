import pandas as pd
import matplotlib.pyplot as plt

# 9. Cargar archivo y mostrar las primeras 5 filas
df = pd.read_csv('ventas.csv')
print("Primeras 5 filas del archivo:")
print(df.head())

# 10. Estadísticas básicas
total_ventas = df['Ventas'].sum()
promedio_precio = df['Precio'].mean()
producto_mas_vendido = df.groupby('Producto')['Ventas'].sum().idxmax()

print("\n--- Estadísticas Básicas ---")
print(f"Total de ventas: {total_ventas}")
print(f"Promedio de precio: {promedio_precio:.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")

# 11. Filtrar productos vendidos en enero de 2025
df_enero = df[df['Fecha'].str.startswith('2025-01')]
print("\n--- Productos vendidos en enero de 2025 ---")
print(df_enero)

# 12. Gráfica de barras: cantidad total vendida por producto
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()

plt.figure(figsize=(8,5))
ventas_por_producto.plot(kind='bar', color='skyblue')
plt.title('Total de ventas por producto')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Grafico_ventas_por_producto.png')
plt.show()