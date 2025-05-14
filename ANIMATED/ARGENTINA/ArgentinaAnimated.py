import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar el archivo CSV
df = pd.read_csv("01 renewable-share-energy.csv")

# Filtrar datos para Argentina
df_argentina = df[df["Entity"] == "Argentina"].copy()
df_argentina = df_argentina.sort_values("Year")
years = df_argentina["Year"].values
renewables = df_argentina["Renewables (% equivalent primary energy)"].values

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, max(renewables) + 5)
ax.set_title("Energía Renovable en Argentina (1965 en adelante)")
ax.set_xlabel("Año")
ax.set_ylabel("Renovables (% energía primaria)")
ax.grid(True)

line, = ax.plot([], [], lw=2, color='blue')
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# Inicialización
def init():
    line.set_data([], [])
    text.set_text('')
    return line, text

# Función de actualización para cada frame
def update(frame):
    x = years[:frame+1]
    y = renewables[:frame+1]
    line.set_data(x, y)
    text.set_text(f"Año: {x[-1]}, Renovables: {y[-1]:.2f}%")
    return line, text

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(years), init_func=init, blit=True, interval=150)

# Guardar como GIF
ani.save("argentina_renewables.gif", writer="pillow", fps=5)

# Mostrar (opcional)
plt.show()