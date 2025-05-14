import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation, FFMpegWriter


# Cargar el archivo CSV
df = pd.read_csv("01 renewable-share-energy.csv")

# Filtrar y ordenar datos para África
df_africa = df[df["Entity"] == "Africa"].copy()
df_africa = df_africa.sort_values("Year")
years_africa = df_africa["Year"].values
renewables_africa = df_africa["Renewables (% equivalent primary energy)"].values

# Filtrar y ordenar datos para Argentina
df_arg = df[df["Entity"] == "Argentina"].copy()
df_arg = df_arg.sort_values("Year")
years_arg = df_arg["Year"].values
renewables_arg = df_arg["Renewables (% equivalent primary energy)"].values

# filtrar y ordenar datos para Colombia
df_col = df[df["Entity"] == "Colombia"].copy()
df_col = df_col.sort_values("Year")
years_colombia = df_col["Year"].values
renewables_colombia = df_col["Renewables (% equivalent primary energy)"].values

# Asegurarse de que ambos arreglos tengan la misma longitud y años (intersección)
common_years = sorted(set(years_africa).intersection(years_arg).intersection(years_colombia))
df_africa = df_africa[df_africa["Year"].isin(common_years)]
df_arg = df_arg[df_arg["Year"].isin(common_years)]
df_col = df_col[df_col["Year"].isin(common_years)]

# Ahora los tres paises tienen los mismos años
years = df_africa["Year"].values  
renewables_africa = df_africa["Renewables (% equivalent primary energy)"].values
renewables_arg = df_arg["Renewables (% equivalent primary energy)"].values
renewables_colombia = df_col["Renewables (% equivalent primary energy)"].values

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, max(renewables_africa.max(), renewables_arg.max(), 
                   renewables_colombia.max()) + 5)
ax.set_title("Energía Renovable: África vs Argentina vs Colombia")
ax.set_xlabel("Año")
ax.set_ylabel("Renovables (% energía primaria)")
ax.grid(True)

# Inicializar líneas y textos
line_africa, = ax.plot([], [], lw=2, color='green', label="África")
line_arg, = ax.plot([], [], lw=2, color='blue', label="Argentina")
line_colombia, = ax.plot([], [], lw=2, color='orange', label="Colombia")
text_africa = ax.text(0.02, 0.9, '', transform=ax.transAxes, color='green')
text_arg = ax.text(0.02, 0.85, '', transform=ax.transAxes, color='blue')
text_colombia = ax.text(0.02, 0.8, '', transform=ax.transAxes, color='orange')

ax.legend()

def init():
    line_africa.set_data([], [])
    line_arg.set_data([], [])
    line_colombia.set_data([], [])
    text_colombia.set_text('')  
    text_africa.set_text('')
    text_arg.set_text('')
    return line_africa, line_arg, line_colombia, text_africa, text_arg, text_colombia

def update(frame):
    x = years[:frame+1]
    y_africa = renewables_africa[:frame+1]
    y_arg = renewables_arg[:frame+1]
    y_colombia = renewables_colombia[:frame+1]

    line_africa.set_data(x, y_africa)
    line_arg.set_data(x, y_arg)
    line_colombia.set_data(x, y_colombia)

    text_africa.set_text(f"África - {x[-1]}: {y_africa[-1]:.2f}%")
    text_arg.set_text(f"Argentina - {x[-1]}: {y_arg[-1]:.2f}%")
    text_colombia.set_text(f"Colombia - {x[-1]}: {y_colombia[-1]:.2f}%")

    return line_africa, line_arg, line_colombia, text_africa, text_arg, text_colombia

# Crear animación
ani = FuncAnimation(fig, update, frames=len(years), init_func=init, blit=True, interval=150)

# Guardar como Video
mpl.rcParams['animation.ffmpeg_path'] = r'C:\Users\vvele\OneDrive\Escritorio\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe'
writer = FFMpegWriter(fps=5, metadata=dict(artist='Val'), bitrate=1800)
ani.save("africa_vs_argentina_vs_colombia_renewables.mp4", writer=writer)

# Guardar como GIF
# ani.save("africa_vs_argentina_vs_colombia_renewables.gif", writer="pillow", fps=5)

# Mostrar (opcional)
plt.show()
