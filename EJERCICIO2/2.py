import matplotlib.pyplot as plt

cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]

plt.bar(cursos, cantidad, color='skyblue', edgecolor='black')
plt.title('Cantidad de Estudiantes por Curso')
plt.xlabel('Curso')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Grafico_barras.png')
plt.show()
