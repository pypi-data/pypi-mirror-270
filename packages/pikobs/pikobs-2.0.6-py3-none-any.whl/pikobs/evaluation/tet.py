import matplotlib.pyplot as plt

# Obtener el mapa de colores 'tab20'
cmap = plt.cm.get_cmap('tab20')

# Crear una secuencia de valores escalares desde 0 hasta 1
values = [i / 19 for i in range(20)]  # Para tab20, hay 20 colores en total

# Representar cada color en el mapa de colores
for i, value in enumerate(values):
    color = cmap(value)
    plt.plot([i, i+1], [0, 0], color=color, linewidth=10)

plt.axis('off')
plt.show()
